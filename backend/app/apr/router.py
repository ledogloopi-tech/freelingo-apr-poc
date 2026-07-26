import re
import unicodedata
from typing import Literal

import httpx
from fastapi import APIRouter, Depends, File, Form, HTTPException, Request, UploadFile, status
from fastapi.responses import JSONResponse, Response

from app.apr.lesson_content import ENTER_THE_CONNECTION_LESSON
from app.apr.lesson_content import FEEDBACK_ID as APR_FEEDBACK_ID
from app.apr.lesson_content import MODEL_AUDIO_ID as APR_MODEL_AUDIO_ID
from app.apr.lesson_content import MODEL_SCRIPT as APR_MODEL_AUDIO_TEXT
from app.apr.schemas import (
    AprFeedbackDraftRequest,
    AprFeedbackDraftResponse,
    AprLessonManifest,
    AprModelAudioMetadata,
    AprModelAudioRequest,
    AprModuleMetadata,
    AprTranscriptDraftResponse,
)
from app.core.config import settings
from app.core.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/api/apr", tags=["apr"])

APR_TRANSCRIPTION_MAX_BYTES = 10 * 1024 * 1024
APR_TRANSCRIPTION_MIME_EXTENSIONS = {
    "audio/webm": "webm",
    "audio/mp4": "mp4",
    "audio/wav": "wav",
    "audio/mpeg": "mp3",
    "audio/ogg": "ogg",
    "application/octet-stream": "bin",
}
APR_TRANSCRIPTION_ERROR = (
    "APR could not generate a transcript draft. This is a technical transcription issue, "
    "not a language result."
)
APR_MODEL_AUDIO_ERROR = (
    "APR could not generate technical model audio. This is a technical audio issue, "
    "not a language result."
)
APR_FEEDBACK_ERROR = (
    "La ayuda técnica no estuvo disponible. Esto no es un resultado sobre tu portugués."
)
APR_FEEDBACK_TEXT = {
    "all-components": "En el texto que confirmaste aparecen las cuatro funciones: saludo, presentación, detalle personal e invitación.\n\nEl mensaje tiene una forma clara de abrir la interacción. En un segundo intento, mantén el significado y deja que E você? llegue como una pregunta.",
    "greeting-missing": "Tu mensaje puede contener información personal, pero para entrar en la interacción añade un saludo breve: Oi u Olá.",
    "identification-missing": "Añade una forma breve de presentarte: Eu sou [nome] o Meu nome é [nome].",
    "preference-missing": "Añade un detalle verdadero y seguro con Gosto de [algo].",
    "invitation-missing": "Para abrir espacio a la otra persona, termina con E você?",
    "multiple-components-missing": "Revisa si tu mensaje incluye estos cuatro movimientos:\n\nsaludar → presentarte → compartir algo verdadero → invitar una respuesta\n\nPuedes usar:\n\nOi! Eu sou... Gosto de... E você?",
    "spanish-me-gusta": "En portugués, usa el bloque gosto de: Gosto de música.",
    "preference-missing-de": "En este bloque, conserva de: gosto de música.",
    "uncertain": "No podemos clasificar esta forma con seguridad. Eso no significa que esté incorrecta.\n\nEscucha tu grabación y comprueba si tu mensaje saluda, dice quién eres, comparte algo verdadero e invita una respuesta.",
}
APR_RETRY_INSTRUCTION = "Intenta una vez más, si te resulta útil.\n\nConserva tu nombre y tu detalle verdadero. Piensa en tres movimientos:\n\nentra → comparte → invita\n\nNo necesitas sonar perfecto."
APR_MODEL_AUDIO_LANGUAGE = "pt-BR"
APR_MODEL_AUDIO_MAX_BYTES = 5 * 1024 * 1024
APR_MODEL_AUDIO_MIME_TYPES = {"audio/mpeg", "audio/wav", "audio/ogg", "audio/mp4", "audio/webm"}
APR_MODEL_AUDIO_METADATA = AprModelAudioMetadata(
    model_audio_id=APR_MODEL_AUDIO_ID,
    language="pt-BR",
    status="generated-temporary-testing",
    storage_status="session-only",
    authorized_as_final_content=False,
    required=False,
)


def _ensure_apr_enabled() -> None:
    if not settings.APR_POC_ENABLED:
        raise HTTPException(status_code=404, detail="APR proof of concept is disabled")


def _normalize_mime_type(mime_type: str | None) -> str:
    normalized = (mime_type or "").split(";", 1)[0].strip().lower()
    return normalized or "application/octet-stream"


def _filename_for_mime_type(mime_type: str) -> str:
    extension = APR_TRANSCRIPTION_MIME_EXTENSIONS.get(mime_type, "webm")
    return f"apr-transcription-draft.{extension}"


@router.get("/modules/primeira-conexao", response_model=AprModuleMetadata)
async def get_primeira_conexao_metadata(
    _current_user: User = Depends(get_current_user),
) -> AprModuleMetadata:
    _ensure_apr_enabled()

    return AprModuleMetadata(
        module_id="APR-R1-RM-01",
        title="Primeira Conexão",
        status="internal-instructional-vertical-slice",
        target_language="pt-BR",
        bridge_language="es",
        authorized_for_pilot=False,
        authorized_for_public_release=False,
    )


@router.get(
    "/modules/primeira-conexao/lessons/enter-the-connection",
    response_model=AprLessonManifest,
)
async def get_enter_the_connection_lesson(
    _current_user: User = Depends(get_current_user),
) -> AprLessonManifest:
    _ensure_apr_enabled()

    return ENTER_THE_CONNECTION_LESSON


@router.post(
    "/modules/primeira-conexao/lessons/enter-the-connection/feedback-drafts",
    response_model=AprFeedbackDraftResponse,
)
async def create_enter_the_connection_feedback_draft(
    body: AprFeedbackDraftRequest,
    _current_user: User = Depends(get_current_user),
) -> JSONResponse:
    _ensure_apr_enabled()

    try:
        if body.feedback_id != APR_FEEDBACK_ID:
            raise HTTPException(status_code=400, detail="APR feedback id is not approved")
        feedback_case = _classify_confirmed_transcript(body.confirmed_transcript)
        feedback_text = APR_FEEDBACK_TEXT[feedback_case]
        response = AprFeedbackDraftResponse(
            feedback_id=APR_FEEDBACK_ID,
            feedback_case=feedback_case,
            attempt_role="original",
            source_confirmation_revision=body.transcript_confirmation_revision,
            status="controlled-instructional-guidance",
            source="server-deterministic",
            acknowledgement=feedback_text,
            primary_priority=feedback_text,
            cue="saludo, nombre, Gosto de..., E você?",
            retry_instruction=APR_RETRY_INSTRUCTION,
            uncertainty=(
                "Esta ayuda usa solamente el texto confirmado por ti. No evalúa pronunciación, "
                "fluidez, inteligibilidad, corrección general, mejora ni nivel. No es Evidencia."
            ),
            requires_retry=False,
            retry_allowed=True,
            authorized_as_academic_feedback=False,
            authorized_as_evidence=False,
            storage_status="session-only",
        )
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=503, detail=APR_FEEDBACK_ERROR) from None

    return JSONResponse(content=response.model_dump(), headers={"Cache-Control": "no-store"})


def _normalize_apr_text(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text.lower())
    without_marks = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    without_punctuation = re.sub(r"[^a-z0-9\s]", " ", without_marks)
    return re.sub(r"\s+", " ", without_punctuation).strip()


def _has_phrase(normalized: str, phrase: str) -> bool:
    return re.search(rf"(^|\s){re.escape(phrase)}($|\s)", normalized) is not None


def _classify_confirmed_transcript(transcript: str) -> str:
    normalized = _normalize_apr_text(transcript)
    if _has_phrase(normalized, "me gusta"):
        return "spanish-me-gusta"
    if _has_phrase(normalized, "gosto") and not _has_phrase(normalized, "gosto de"):
        return "preference-missing-de"

    greeting = any(
        _has_phrase(normalized, phrase)
        for phrase in ["oi", "ola", "bom dia", "boa tarde", "boa noite"]
    )
    identification = any(
        _has_phrase(normalized, phrase) for phrase in ["eu sou", "sou", "meu nome e", "eu me chamo"]
    )
    preference = any(
        _has_phrase(normalized, phrase) for phrase in ["gosto de", "eu gosto de", "adoro", "curto"]
    )
    invitation = any(
        _has_phrase(normalized, phrase)
        for phrase in ["e voce", "e tu", "do que gosta", "gosta de que"]
    )
    components = {
        "greeting-missing": greeting,
        "identification-missing": identification,
        "preference-missing": preference,
        "invitation-missing": invitation,
    }
    missing = [case for case, present in components.items() if not present]
    present_count = 4 - len(missing)
    if not missing:
        return "all-components"
    if len(missing) == 1:
        return missing[0]
    if present_count >= 1:
        return "multiple-components-missing"
    return "uncertain"


@router.post(
    "/modules/primeira-conexao/lessons/enter-the-connection/model-audio",
)
async def create_enter_the_connection_model_audio(
    request: Request,
    body: AprModelAudioRequest,
    _current_user: User = Depends(get_current_user),
) -> Response:
    _ensure_apr_enabled()

    if body.model_audio_id != APR_MODEL_AUDIO_ID:
        raise HTTPException(status_code=400, detail="APR model-audio id is not approved")

    tts_service = getattr(request.app.state, "tts_service", None)
    if tts_service is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="APR model-audio service is unavailable",
        )

    apr_voice = settings.APR_TTS_VOICE.strip() or None
    if settings.TTS_PROVIDER == "local" and apr_voice is None:
        raise HTTPException(status_code=503, detail=APR_MODEL_AUDIO_ERROR)

    try:
        result = await tts_service.synthesize_with_metadata(
            APR_MODEL_AUDIO_TEXT, voice=apr_voice, language=APR_MODEL_AUDIO_LANGUAGE
        )
    except httpx.HTTPStatusError:
        raise HTTPException(status_code=502, detail=APR_MODEL_AUDIO_ERROR) from None
    except httpx.RequestError:
        raise HTTPException(status_code=502, detail=APR_MODEL_AUDIO_ERROR) from None
    except Exception:
        raise HTTPException(status_code=503, detail=APR_MODEL_AUDIO_ERROR) from None

    audio = result.audio_bytes
    mime_type = (result.mime_type or "").split(";", 1)[0].strip().lower()
    if (
        not audio
        or len(audio) > APR_MODEL_AUDIO_MAX_BYTES
        or mime_type not in APR_MODEL_AUDIO_MIME_TYPES
    ):
        raise HTTPException(status_code=502, detail=APR_MODEL_AUDIO_ERROR)

    return Response(
        content=audio,
        media_type=mime_type,
        headers={
            "Cache-Control": "no-store",
            "X-APR-Audio-Status": APR_MODEL_AUDIO_METADATA.status,
            "X-APR-Audio-Language": APR_MODEL_AUDIO_METADATA.language,
        },
    )


@router.post(
    "/modules/primeira-conexao/lessons/enter-the-connection/transcription-drafts",
    response_model=AprTranscriptDraftResponse,
)
async def create_enter_the_connection_transcription_draft(
    request: Request,
    audio: UploadFile = File(...),
    attempt_role: Literal["original", "latest_retry"] = Form(...),
    _current_user: User = Depends(get_current_user),
) -> AprTranscriptDraftResponse:
    _ensure_apr_enabled()

    stt_service = getattr(request.app.state, "stt_service", None)
    if stt_service is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="APR transcription service is unavailable",
        )

    mime_type = _normalize_mime_type(audio.content_type)
    if mime_type not in APR_TRANSCRIPTION_MIME_EXTENSIONS:
        raise HTTPException(status_code=415, detail="Unsupported APR transcription audio format")

    audio_bytes = await audio.read(APR_TRANSCRIPTION_MAX_BYTES + 1)
    if not audio_bytes:
        raise HTTPException(status_code=400, detail="APR transcription audio is empty")
    if len(audio_bytes) > APR_TRANSCRIPTION_MAX_BYTES:
        raise HTTPException(status_code=413, detail="APR transcription audio is too large")

    filename = _filename_for_mime_type(mime_type)
    try:
        draft_text = (
            await stt_service.transcribe(
                audio_bytes,
                filename,
                mime_type=mime_type,
                language="pt",
            )
        ).strip()
    except httpx.HTTPStatusError, httpx.RequestError:
        raise HTTPException(status_code=502, detail=APR_TRANSCRIPTION_ERROR) from None
    except Exception:
        raise HTTPException(status_code=503, detail=APR_TRANSCRIPTION_ERROR) from None

    if not draft_text:
        raise HTTPException(status_code=502, detail=APR_TRANSCRIPTION_ERROR)

    return AprTranscriptDraftResponse(
        attempt_role=attempt_role,
        draft_text=draft_text,
        language="pt",
        status="machine-generated-draft",
        requires_learner_confirmation=True,
        authorized_as_evidence=False,
        storage_status="session-only",
    )

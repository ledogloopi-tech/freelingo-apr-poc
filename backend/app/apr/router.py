from typing import Literal

import httpx
from fastapi import APIRouter, Depends, File, Form, HTTPException, Request, UploadFile, status

from app.apr.lesson_content import ENTER_THE_CONNECTION_LESSON
from app.apr.schemas import AprLessonManifest, AprModuleMetadata, AprTranscriptDraftResponse
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
        status="technical-boundary-only",
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
    except (httpx.HTTPStatusError, httpx.RequestError):
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

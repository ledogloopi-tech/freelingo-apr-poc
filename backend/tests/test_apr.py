from pathlib import Path

import httpx
import pytest
from sqlalchemy import func, select

from app.apr import router as apr_router
from app.core.config import settings
from app.main import app
from app.models.progress import Progress
from app.models.study_plan import StudyPlan

pytestmark = pytest.mark.asyncio


async def test_apr_endpoint_requires_authentication(client):
    res = await client.get("/api/apr/modules/primeira-conexao")

    assert res.status_code == 401


async def test_apr_endpoint_returns_404_when_disabled(client, test_user, monkeypatch):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", False)

    res = await client.get("/api/apr/modules/primeira-conexao", headers=headers)

    assert res.status_code == 404
    assert res.json() == {"detail": "APR proof of concept is disabled"}


async def test_apr_endpoint_returns_fixed_metadata_without_study_plan(
    client, test_user, db_session, monkeypatch
):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)

    plans_before = await db_session.scalar(select(func.count()).select_from(StudyPlan))
    progress_before = await db_session.scalar(select(func.count()).select_from(Progress))

    res = await client.get("/api/apr/modules/primeira-conexao", headers=headers)

    assert res.status_code == 200
    assert res.json() == {
        "module_id": "APR-R1-RM-01",
        "title": "Primeira Conexão",
        "status": "technical-boundary-only",
        "target_language": "pt-BR",
        "bridge_language": "es",
        "authorized_for_pilot": False,
        "authorized_for_public_release": False,
    }

    plans_after = await db_session.scalar(select(func.count()).select_from(StudyPlan))
    progress_after = await db_session.scalar(select(func.count()).select_from(Progress))

    assert plans_after == plans_before
    assert progress_after == progress_before


async def test_apr_lesson_endpoint_requires_authentication(client):
    res = await client.get("/api/apr/modules/primeira-conexao/lessons/enter-the-connection")

    assert res.status_code == 401


async def test_apr_lesson_endpoint_returns_404_when_disabled(client, test_user, monkeypatch):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", False)

    res = await client.get(
        "/api/apr/modules/primeira-conexao/lessons/enter-the-connection", headers=headers
    )

    assert res.status_code == 404
    assert res.json() == {"detail": "APR proof of concept is disabled"}


async def test_apr_lesson_endpoint_returns_typed_placeholder_manifest_without_writes(
    client, test_user, db_session, monkeypatch
):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)

    plans_before = await db_session.scalar(select(func.count()).select_from(StudyPlan))
    progress_before = await db_session.scalar(select(func.count()).select_from(Progress))

    res = await client.get(
        "/api/apr/modules/primeira-conexao/lessons/enter-the-connection", headers=headers
    )

    assert res.status_code == 200
    manifest = res.json()
    assert manifest["lesson_id"] == "APR-R1-RM-01-L01-TECH"
    assert manifest["module_id"] == "APR-R1-RM-01"
    assert manifest["version"] == "0.6.0-technical-placeholder"
    assert manifest["title"] == "Enter the Connection"
    assert manifest["internal_title"] == "Lesson Player Technical Demonstration"
    assert manifest["content_status"] == "technical-placeholder"
    assert manifest["authorized_for_pilot"] is False
    assert manifest["authorized_for_public_release"] is False
    assert manifest["current_step_count"] == 5
    assert len(manifest["steps"]) == 5
    assert [step["step_type"] for step in manifest["steps"]] == [
        "orientation",
        "information",
        "single_choice",
        "recording",
        "reflection",
    ]
    assert "Technical placeholder lesson" in manifest["steps"][0]["body"]
    assert "Approved lesson content pending" in manifest["steps"][0]["body"]
    assert (
        "This interaction tests the APR lesson player, not Portuguese capability."
        in manifest["steps"][0]["body"]
    )
    assert "options" in manifest["steps"][2]
    assert all("feedback" in option for option in manifest["steps"][2]["options"])
    recording_step = manifest["steps"][3]
    assert recording_step["step_id"] == "microphone-capture"
    assert recording_step["max_seconds"] == 10
    assert recording_step["allow_retry"] is True
    assert recording_step["preserve_original"] is True
    assert recording_step["storage_status"] == "session-only"
    recording_text = f"{recording_step['body']} {recording_step['prompt']}"
    assert "does not assess Portuguese capability" in recording_text
    assert "not academic evidence" in recording_text
    assert "Transcription starts only after" in recording_text
    assert "machine-generated draft" in recording_text
    assert "review and correct" in recording_text
    assert "does not turn it into academic evidence" in recording_text
    assert "session-only" in recording_text

    expected_recording_fields = {
        "max_seconds": 10,
        "allow_retry": True,
        "preserve_original": True,
        "storage_status": "session-only",
        "transcription_language": "pt",
        "transcription_mode": "on-demand",
        "requires_learner_confirmation": True,
        "transcript_storage_status": "session-only",
        "transcript_authorized_as_evidence": False,
        "model_audio_id": "APR-R1-RM-01-L01-MODEL-TECH",
        "model_audio_mode": "on-demand",
        "model_audio_language": "pt-BR",
        "model_audio_source": "generated-technical-placeholder",
        "model_audio_storage_status": "session-only",
        "model_audio_authorized_as_final_content": False,
        "model_audio_required": False,
        "feedback_id": "APR-R1-RM-01-L01-FEEDBACK-TECH",
        "feedback_mode": "on-demand",
        "feedback_source_attempt": "original",
        "feedback_requires_confirmed_transcript": True,
        "feedback_source": "controlled-technical-placeholder",
        "feedback_storage_status": "session-only",
        "feedback_authorized_as_academic_feedback": False,
        "feedback_authorized_as_evidence": False,
        "feedback_required": False,
        "retry_orchestration_mode": "optional-post-feedback-latest-retry",
        "retry_required": False,
    }
    for field, expected in expected_recording_fields.items():
        assert recording_step[field] == expected
    assert manifest["steps"][4]["max_characters"] == 240

    plans_after = await db_session.scalar(select(func.count()).select_from(StudyPlan))
    progress_after = await db_session.scalar(select(func.count()).select_from(Progress))

    assert plans_after == plans_before
    assert progress_after == progress_before


async def test_apr_does_not_expose_recording_upload_endpoint(client, test_user, monkeypatch):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)
    recordings_path = "/api/apr/modules/primeira-conexao/lessons/enter-the-connection/recordings"

    res = await client.post(recordings_path, headers=headers)

    assert res.status_code == 404
    assert not any(
        getattr(route, "path", None) == recordings_path
        and "POST" in getattr(route, "methods", set())
        for route in app.routes
    )


class MockAprSttService:
    def __init__(self, text=" rascunho técnico ", exc=None):
        self.text = text
        self.exc = exc
        self.calls = []

    async def transcribe(self, audio_bytes, filename, *, mime_type, language):
        self.calls.append(
            {
                "audio_bytes": audio_bytes,
                "filename": filename,
                "mime_type": mime_type,
                "language": language,
            }
        )
        if self.exc:
            raise self.exc
        return self.text


TRANSCRIPTION_URL = (
    "/api/apr/modules/primeira-conexao/lessons/enter-the-connection/transcription-drafts"
)


async def test_apr_transcription_requires_authentication(client):
    res = await client.post(TRANSCRIPTION_URL)

    assert res.status_code == 401


async def test_apr_transcription_returns_404_when_disabled(client, test_user, monkeypatch):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", False)

    res = await client.post(
        TRANSCRIPTION_URL,
        headers=headers,
        data={"attempt_role": "original"},
        files={"audio": ("audio.webm", b"abc", "audio/webm")},
    )

    assert res.status_code == 404


async def test_apr_transcription_requires_stt_service(client, test_user, monkeypatch):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)
    monkeypatch.setattr(app.state, "stt_service", None, raising=False)

    res = await client.post(
        TRANSCRIPTION_URL,
        headers=headers,
        data={"attempt_role": "original"},
        files={"audio": ("audio.webm", b"abc", "audio/webm")},
    )

    assert res.status_code == 503


@pytest.mark.parametrize("attempt_role", ["original", "latest_retry"])
async def test_apr_transcription_returns_typed_draft_and_uses_portuguese(
    client, test_user, db_session, monkeypatch, attempt_role
):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)
    mock = MockAprSttService()
    monkeypatch.setattr(app.state, "stt_service", mock, raising=False)
    plans_before = await db_session.scalar(select(func.count()).select_from(StudyPlan))
    progress_before = await db_session.scalar(select(func.count()).select_from(Progress))

    res = await client.post(
        TRANSCRIPTION_URL,
        headers=headers,
        data={"attempt_role": attempt_role},
        files={"audio": ("ignored.webm", b"abc", "audio/webm;codecs=opus")},
    )

    assert res.status_code == 200
    assert res.json() == {
        "attempt_role": attempt_role,
        "draft_text": "rascunho técnico",
        "language": "pt",
        "status": "machine-generated-draft",
        "requires_learner_confirmation": True,
        "authorized_as_evidence": False,
        "storage_status": "session-only",
    }
    assert mock.calls == [
        {
            "audio_bytes": b"abc",
            "filename": "apr-transcription-draft.webm",
            "mime_type": "audio/webm",
            "language": "pt",
        }
    ]
    assert await db_session.scalar(select(func.count()).select_from(StudyPlan)) == plans_before
    assert await db_session.scalar(select(func.count()).select_from(Progress)) == progress_before


async def test_apr_transcription_accepts_octet_stream_fallback(client, test_user, monkeypatch):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)
    mock = MockAprSttService()
    monkeypatch.setattr(app.state, "stt_service", mock, raising=False)

    res = await client.post(
        TRANSCRIPTION_URL,
        headers=headers,
        data={"attempt_role": "original"},
        files={"audio": ("audio.bin", b"abc", "application/octet-stream")},
    )

    assert res.status_code == 200
    assert mock.calls[0]["mime_type"] == "application/octet-stream"
    assert mock.calls[0]["filename"] == "apr-transcription-draft.bin"


@pytest.mark.parametrize(
    ("files", "data", "expected_status"),
    [
        ({"audio": ("audio.webm", b"", "audio/webm")}, {"attempt_role": "original"}, 400),
        ({"audio": ("audio.txt", b"abc", "text/plain")}, {"attempt_role": "original"}, 415),
        ({"audio": ("audio.webm", b"abc", "audio/webm")}, {"attempt_role": "other"}, 422),
    ],
)
async def test_apr_transcription_rejects_invalid_inputs(
    client, test_user, monkeypatch, files, data, expected_status
):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)
    mock = MockAprSttService()
    monkeypatch.setattr(app.state, "stt_service", mock, raising=False)

    res = await client.post(TRANSCRIPTION_URL, headers=headers, data=data, files=files)

    assert res.status_code == expected_status
    assert mock.calls == []


async def test_apr_transcription_rejects_oversized_audio(client, test_user, monkeypatch):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)
    mock = MockAprSttService()
    monkeypatch.setattr(app.state, "stt_service", mock, raising=False)

    res = await client.post(
        TRANSCRIPTION_URL,
        headers=headers,
        data={"attempt_role": "original"},
        files={"audio": ("audio.webm", b"x" * (10 * 1024 * 1024 + 1), "audio/webm")},
    )

    assert res.status_code == 413
    assert mock.calls == []


async def test_apr_transcription_maps_httpx_provider_failure_to_sanitized_502(
    client, test_user, monkeypatch
):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)
    request = httpx.Request("POST", "https://provider.example/asr")
    response = httpx.Response(500, request=request)
    mock = MockAprSttService(
        exc=httpx.HTTPStatusError("secret provider url", request=request, response=response)
    )
    monkeypatch.setattr(app.state, "stt_service", mock, raising=False)

    res = await client.post(
        TRANSCRIPTION_URL,
        headers=headers,
        data={"attempt_role": "original"},
        files={"audio": ("audio.webm", b"abc", "audio/webm")},
    )

    assert res.status_code == 502
    assert "secret provider url" not in res.text
    assert "provider.example" not in res.text
    assert "technical transcription issue" in res.text


async def test_apr_transcription_sanitizes_provider_failures(client, test_user, monkeypatch):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)
    mock = MockAprSttService(exc=RuntimeError("secret provider url"))
    monkeypatch.setattr(app.state, "stt_service", mock, raising=False)

    res = await client.post(
        TRANSCRIPTION_URL,
        headers=headers,
        data={"attempt_role": "original"},
        files={"audio": ("audio.webm", b"abc", "audio/webm")},
    )

    assert res.status_code == 503
    assert "secret provider url" not in res.text
    assert "technical transcription issue" in res.text


async def test_apr_transcription_treats_empty_provider_output_as_technical_failure(
    client, test_user, monkeypatch
):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)
    mock = MockAprSttService(text="   ")
    monkeypatch.setattr(app.state, "stt_service", mock, raising=False)

    res = await client.post(
        TRANSCRIPTION_URL,
        headers=headers,
        data={"attempt_role": "latest_retry"},
        files={"audio": ("audio.ogg", b"abc", "audio/ogg")},
    )

    assert res.status_code == 502
    assert mock.calls == [
        {
            "audio_bytes": b"abc",
            "filename": "apr-transcription-draft.ogg",
            "mime_type": "audio/ogg",
            "language": "pt",
        }
    ]


async def test_apr_lesson_manifest_day5_transcription_contract(client, test_user, monkeypatch):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)

    res = await client.get(
        "/api/apr/modules/primeira-conexao/lessons/enter-the-connection", headers=headers
    )

    manifest = res.json()
    assert manifest["version"] == "0.6.0-technical-placeholder"
    recording_step = manifest["steps"][3]
    assert recording_step["transcription_language"] == "pt"
    assert recording_step["transcription_mode"] == "on-demand"
    assert recording_step["requires_learner_confirmation"] is True
    assert recording_step["transcript_storage_status"] == "session-only"
    assert recording_step["transcript_authorized_as_evidence"] is False
    assert recording_step["allow_retry"] is True
    assert recording_step["preserve_original"] is True
    assert recording_step["storage_status"] == "session-only"
    assert manifest["authorized_for_pilot"] is False
    assert manifest["authorized_for_public_release"] is False


class MockAprTtsService:
    def __init__(self, audio=b"mp3-bytes", mime_type="audio/mpeg", exc=None):
        self.audio = audio
        self.mime_type = mime_type
        self.exc = exc
        self.calls = []

    async def synthesize_with_metadata(self, text, voice=None, language=None):
        from app.services.tts_service import TTSResult

        self.calls.append({"text": text, "voice": voice, "language": language})
        if self.exc:
            raise self.exc
        return TTSResult(audio_bytes=self.audio, mime_type=self.mime_type)


MODEL_AUDIO_URL = "/api/apr/modules/primeira-conexao/lessons/enter-the-connection/model-audio"
MODEL_AUDIO_ID = "APR-R1-RM-01-L01-MODEL-TECH"
SERVER_CONTROLLED_MODEL_AUDIO_TEXT = (
    "Olá. Este é um teste técnico de áudio em português brasileiro."
)


def enable_apr_tts(monkeypatch, *, provider="local", voice="pt_BR_technical"):
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)
    monkeypatch.setattr(settings, "TTS_PROVIDER", provider)
    monkeypatch.setattr(settings, "APR_TTS_VOICE", voice)


async def test_apr_model_audio_requires_authentication(client):
    res = await client.post(MODEL_AUDIO_URL, json={"model_audio_id": MODEL_AUDIO_ID})

    assert res.status_code == 401


async def test_apr_model_audio_returns_404_when_disabled(client, test_user, monkeypatch):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", False)

    res = await client.post(
        MODEL_AUDIO_URL,
        headers=headers,
        json={"model_audio_id": MODEL_AUDIO_ID},
    )

    assert res.status_code == 404


async def test_apr_model_audio_requires_tts_service(client, test_user, monkeypatch):
    _user, headers = test_user
    enable_apr_tts(monkeypatch)
    monkeypatch.setattr(app.state, "tts_service", None, raising=False)

    res = await client.post(
        MODEL_AUDIO_URL,
        headers=headers,
        json={"model_audio_id": MODEL_AUDIO_ID},
    )

    assert res.status_code == 503


async def test_apr_model_audio_rejects_unknown_identifier(client, test_user, monkeypatch):
    _user, headers = test_user
    enable_apr_tts(monkeypatch)
    mock = MockAprTtsService()
    monkeypatch.setattr(app.state, "tts_service", mock, raising=False)

    res = await client.post(
        MODEL_AUDIO_URL,
        headers=headers,
        json={"model_audio_id": "UNKNOWN"},
    )

    assert res.status_code == 400
    assert mock.calls == []


@pytest.mark.parametrize(
    "extra_payload",
    [
        {"text": "cliente arbitrário"},
        {"language": "en-US"},
        {"voice": "af_heart"},
        {"provider": "local"},
        {"response_format": "wav"},
    ],
)
async def test_apr_model_audio_rejects_extra_request_fields(
    client, test_user, monkeypatch, extra_payload
):
    _user, headers = test_user
    enable_apr_tts(monkeypatch)
    mock = MockAprTtsService()
    monkeypatch.setattr(app.state, "tts_service", mock, raising=False)

    res = await client.post(
        MODEL_AUDIO_URL,
        headers=headers,
        json={"model_audio_id": MODEL_AUDIO_ID, **extra_payload},
    )

    assert res.status_code == 422
    assert mock.calls == []


async def test_apr_model_audio_local_provider_requires_configured_apr_voice(
    client, test_user, monkeypatch
):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)
    monkeypatch.setattr(settings, "TTS_PROVIDER", "local")
    monkeypatch.setattr(settings, "APR_TTS_VOICE", "")
    mock = MockAprTtsService()
    monkeypatch.setattr(app.state, "tts_service", mock, raising=False)

    res = await client.post(
        MODEL_AUDIO_URL,
        headers=headers,
        json={"model_audio_id": MODEL_AUDIO_ID},
    )

    assert res.status_code == 503
    assert "technical audio issue" in res.text
    assert mock.calls == []


@pytest.mark.parametrize("mime_type", ["audio/wav", "audio/mpeg"])
async def test_apr_model_audio_returns_valid_provider_mime_no_store_and_headers_without_writes(
    client, test_user, db_session, monkeypatch, mime_type
):
    _user, headers = test_user
    enable_apr_tts(monkeypatch)
    mock = MockAprTtsService(audio=b"fake-audio", mime_type=mime_type)
    monkeypatch.setattr(app.state, "tts_service", mock, raising=False)
    plans_before = await db_session.scalar(select(func.count()).select_from(StudyPlan))
    progress_before = await db_session.scalar(select(func.count()).select_from(Progress))

    res = await client.post(
        MODEL_AUDIO_URL,
        headers=headers,
        json={"model_audio_id": MODEL_AUDIO_ID},
    )

    assert res.status_code == 200
    assert res.headers["content-type"] == mime_type
    assert res.headers["cache-control"] == "no-store"
    assert res.headers["x-apr-audio-status"] == "generated-technical-placeholder"
    assert res.headers["x-apr-audio-language"] == "pt-BR"
    assert res.content == b"fake-audio"
    assert mock.calls == [
        {
            "text": SERVER_CONTROLLED_MODEL_AUDIO_TEXT,
            "voice": "pt_BR_technical",
            "language": "pt-BR",
        }
    ]
    assert await db_session.scalar(select(func.count()).select_from(StudyPlan)) == plans_before
    assert await db_session.scalar(select(func.count()).select_from(Progress)) == progress_before


@pytest.mark.parametrize("case", ["empty", "oversized"])
async def test_apr_model_audio_empty_or_oversized_provider_audio_fails(
    client, test_user, monkeypatch, case
):
    audio = b"" if case == "empty" else b"x" * (5 * 1024 * 1024 + 1)

    _user, headers = test_user
    enable_apr_tts(monkeypatch)
    monkeypatch.setattr(
        app.state,
        "tts_service",
        MockAprTtsService(audio=audio),
        raising=False,
    )

    res = await client.post(
        MODEL_AUDIO_URL,
        headers=headers,
        json={"model_audio_id": MODEL_AUDIO_ID},
    )

    assert res.status_code == 502
    assert "technical audio issue" in res.text


@pytest.mark.parametrize("mime_type", ["", "text/html", "audio/flac"])
async def test_apr_model_audio_empty_or_unsupported_provider_mime_fails(
    client, test_user, monkeypatch, mime_type
):
    _user, headers = test_user
    enable_apr_tts(monkeypatch)
    monkeypatch.setattr(
        app.state,
        "tts_service",
        MockAprTtsService(audio=b"fake-audio", mime_type=mime_type),
        raising=False,
    )

    res = await client.post(
        MODEL_AUDIO_URL,
        headers=headers,
        json={"model_audio_id": MODEL_AUDIO_ID},
    )

    assert res.status_code == 502
    assert "technical audio issue" in res.text
    assert res.content != b"fake-audio"


async def test_apr_model_audio_sanitizes_provider_failures(client, test_user, monkeypatch):
    _user, headers = test_user
    enable_apr_tts(monkeypatch)
    monkeypatch.setattr(
        app.state,
        "tts_service",
        MockAprTtsService(exc=RuntimeError("secret provider url")),
        raising=False,
    )

    res = await client.post(
        MODEL_AUDIO_URL,
        headers=headers,
        json={"model_audio_id": MODEL_AUDIO_ID},
    )

    assert res.status_code == 503
    assert "secret provider url" not in res.text
    assert "technical audio issue" in res.text


async def test_apr_model_audio_maps_httpx_failure_to_sanitized_error(
    client, test_user, monkeypatch
):
    _user, headers = test_user
    enable_apr_tts(monkeypatch)
    request = httpx.Request("POST", "https://provider.example/tts")
    response = httpx.Response(500, request=request)
    monkeypatch.setattr(
        app.state,
        "tts_service",
        MockAprTtsService(
            exc=httpx.HTTPStatusError("secret provider url", request=request, response=response)
        ),
        raising=False,
    )

    res = await client.post(
        MODEL_AUDIO_URL,
        headers=headers,
        json={"model_audio_id": MODEL_AUDIO_ID},
    )

    assert res.status_code == 502
    assert "secret provider url" not in res.text
    assert "provider.example" not in res.text


async def test_apr_model_audio_maps_request_error_to_sanitized_502(client, test_user, monkeypatch):
    _user, headers = test_user
    enable_apr_tts(monkeypatch)
    request = httpx.Request("POST", "https://provider.example/tts")
    monkeypatch.setattr(
        app.state,
        "tts_service",
        MockAprTtsService(exc=httpx.RequestError("secret provider url", request=request)),
        raising=False,
    )

    res = await client.post(
        MODEL_AUDIO_URL,
        headers=headers,
        json={"model_audio_id": MODEL_AUDIO_ID},
    )

    assert res.status_code == 502
    assert "secret provider url" not in res.text
    assert "provider.example" not in res.text
    assert "technical audio issue" in res.text


async def test_apr_lesson_manifest_day6_model_audio_contract(client, test_user, monkeypatch):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)

    res = await client.get(
        "/api/apr/modules/primeira-conexao/lessons/enter-the-connection", headers=headers
    )

    manifest = res.json()
    assert manifest["version"] == "0.6.0-technical-placeholder"
    assert manifest["current_step_count"] == 5
    recording_step = manifest["steps"][3]
    assert recording_step["model_audio_id"] == MODEL_AUDIO_ID
    assert recording_step["model_audio_mode"] == "on-demand"
    assert recording_step["model_audio_language"] == "pt-BR"
    assert recording_step["model_audio_source"] == "generated-technical-placeholder"
    assert recording_step["model_audio_storage_status"] == "session-only"
    assert recording_step["model_audio_authorized_as_final_content"] is False
    assert recording_step["model_audio_required"] is False
    assert "model_audio_text" not in recording_step
    assert "model_audio_authorized_as_instructional_audio" not in recording_step
    assert "model_audio_authorized_as_evidence" not in recording_step
    assert "requires_human_audio_replacement" not in recording_step
    assert recording_step["transcription_language"] == "pt"
    assert recording_step["transcription_mode"] == "on-demand"
    assert recording_step["requires_learner_confirmation"] is True
    assert recording_step["transcript_storage_status"] == "session-only"
    assert recording_step["transcript_authorized_as_evidence"] is False
    assert recording_step["allow_retry"] is True
    assert recording_step["preserve_original"] is True
    assert recording_step["storage_status"] == "session-only"
    assert manifest["authorized_for_pilot"] is False
    assert manifest["authorized_for_public_release"] is False


async def test_apr_does_not_expose_model_audio_storage_endpoint(client, test_user, monkeypatch):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)
    storage_path = f"{MODEL_AUDIO_URL}/storage"

    res = await client.post(storage_path, headers=headers)

    assert res.status_code == 404
    assert not any(
        getattr(route, "path", None) == storage_path and "POST" in getattr(route, "methods", set())
        for route in app.routes
    )


FEEDBACK_URL = "/api/apr/modules/primeira-conexao/lessons/enter-the-connection/feedback-drafts"
FEEDBACK_ID = "APR-R1-RM-01-L01-FEEDBACK-TECH"


def feedback_payload(**overrides):
    payload = {
        "feedback_id": FEEDBACK_ID,
        "attempt_role": "original",
        "transcript_confirmation_revision": 1,
    }
    payload.update(overrides)
    return payload


async def test_apr_feedback_requires_authentication(client):
    res = await client.post(FEEDBACK_URL, json=feedback_payload())

    assert res.status_code == 401


async def test_apr_feedback_returns_404_when_disabled(client, test_user, monkeypatch):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", False)

    res = await client.post(FEEDBACK_URL, headers=headers, json=feedback_payload())

    assert res.status_code == 404


class SentinelAprSttService:
    def __init__(self):
        self.calls = []

    async def transcribe(self, *args, **kwargs):
        self.calls.append({"args": args, "kwargs": kwargs})
        raise AssertionError("APR feedback endpoint must not call STT")


class SentinelAprTtsService:
    def __init__(self):
        self.calls = []

    async def synthesize_with_metadata(self, *args, **kwargs):
        self.calls.append({"args": args, "kwargs": kwargs})
        raise AssertionError("APR feedback endpoint must not call TTS")


def install_feedback_provider_sentinels(monkeypatch):
    stt = SentinelAprSttService()
    tts = SentinelAprTtsService()
    monkeypatch.setattr(app.state, "stt_service", stt, raising=False)
    monkeypatch.setattr(app.state, "tts_service", tts, raising=False)
    return stt, tts


@pytest.mark.parametrize(
    "payload",
    [
        feedback_payload(feedback_id="unknown"),
        feedback_payload(attempt_role="latest_retry"),
        feedback_payload(transcript_confirmation_revision=0),
        feedback_payload(transcript="text"),
        feedback_payload(transcript_text="text"),
        feedback_payload(confirmed_transcript="text"),
        feedback_payload(audio="blob"),
        feedback_payload(recording="blob"),
        feedback_payload(model_audio_id="APR-R1-RM-01-L01-MODEL-TECH"),
        feedback_payload(language="pt-BR"),
        feedback_payload(score=1),
        feedback_payload(prompt="prompt"),
        feedback_payload(provider="llm"),
        feedback_payload(voice="voice"),
        feedback_payload(learner_id="learner"),
        feedback_payload(user_id="user"),
    ],
)
async def test_apr_feedback_rejects_unapproved_or_extra_request_fields_without_services(
    client, test_user, monkeypatch, payload
):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)
    stt, tts = install_feedback_provider_sentinels(monkeypatch)

    res = await client.post(FEEDBACK_URL, headers=headers, json=payload)

    assert res.status_code in {400, 422}
    assert stt.calls == []
    assert tts.calls == []


async def test_apr_feedback_returns_controlled_no_store_response_without_writes_or_services(
    client, test_user, db_session, monkeypatch
):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)
    stt, tts = install_feedback_provider_sentinels(monkeypatch)
    plans_before = await db_session.scalar(select(func.count()).select_from(StudyPlan))
    progress_before = await db_session.scalar(select(func.count()).select_from(Progress))

    res = await client.post(
        FEEDBACK_URL,
        headers=headers,
        json=feedback_payload(transcript_confirmation_revision=3),
    )

    assert res.status_code == 200
    assert res.headers["Cache-Control"] == "no-store"
    assert res.json() == {
        "feedback_id": FEEDBACK_ID,
        "attempt_role": "original",
        "source_confirmation_revision": 3,
        "status": "technical-placeholder",
        "source": "server-controlled",
        "acknowledgement": "You completed and confirmed an Original technical attempt.",
        "primary_priority": "Keep the main message together for one more optional attempt.",
        "cue": "Pause briefly, then repeat the same intended message once.",
        "retry_instruction": (
            "Record one optional Latest retry after this feedback. APR will preserve "
            "the Original attempt."
        ),
        "uncertainty": (
            "This technical placeholder does not evaluate meaning, grammar, pronunciation, "
            "fluency, intelligibility, correctness, or improvement. This content exists only "
            "to test feedback-and-retry orchestration. It is not final lesson feedback. It "
            "is not Professor Gabriel output. It is not generated by an LLM. It is not "
            "academic feedback. It is not Evidence."
        ),
        "requires_retry": False,
        "retry_allowed": True,
        "authorized_as_academic_feedback": False,
        "authorized_as_evidence": False,
        "storage_status": "session-only",
    }
    forbidden = {
        "transcript",
        "transcript_text",
        "audio",
        "score",
        "confidence",
        "correctness",
        "cefr",
        "proficiency",
        "fluency",
        "pronunciation_result",
        "grammar_result",
        "capability_result",
        "evidence_state",
    }
    assert forbidden.isdisjoint(res.json())
    assert stt.calls == []
    assert tts.calls == []
    assert await db_session.scalar(select(func.count()).select_from(StudyPlan)) == plans_before
    assert await db_session.scalar(select(func.count()).select_from(Progress)) == progress_before


async def test_apr_feedback_unexpected_failure_is_sanitized_without_writes(
    client, test_user, db_session, monkeypatch
):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)
    stt, tts = install_feedback_provider_sentinels(monkeypatch)
    secret = "secret-token http://internal.example/feedback"

    def raise_secret_exception(*args, **kwargs):
        raise RuntimeError(secret)

    monkeypatch.setattr(apr_router, "AprFeedbackDraftResponse", raise_secret_exception)
    plans_before = await db_session.scalar(select(func.count()).select_from(StudyPlan))
    progress_before = await db_session.scalar(select(func.count()).select_from(Progress))

    res = await client.post(FEEDBACK_URL, headers=headers, json=feedback_payload())

    assert res.status_code == 503
    assert res.json() == {
        "detail": "APR could not load technical feedback. This is a feedback-service issue, not a language result."
    }
    body = res.text
    assert "secret-token" not in body
    assert "internal.example" not in body
    assert "transcript" not in body
    assert "audio" not in body
    assert stt.calls == []
    assert tts.calls == []
    assert await db_session.scalar(select(func.count()).select_from(StudyPlan)) == plans_before
    assert await db_session.scalar(select(func.count()).select_from(Progress)) == progress_before


async def test_apr_feedback_has_no_persistence_model_or_migration():
    backend_root = Path(__file__).resolve().parents[1]
    model_dir = backend_root / "app" / "models"
    migration_dir = backend_root / "alembic" / "versions"

    assert model_dir.is_dir()
    assert migration_dir.is_dir()

    apr_persistence_markers = (
        "apr_feedback",
        "apr-r1-rm-01-l01-feedback-tech",
        "apr_feedback_draft",
        "apr_feedback_retry",
    )

    for directory in (model_dir, migration_dir):
        for path in directory.glob("*.py"):
            searchable = (
                f"{path.name}\n{path.read_text(encoding='utf-8')}"
            ).lower()
            assert not any(
                marker in searchable for marker in apr_persistence_markers
            )


async def test_apr_feedback_does_not_expose_storage_route(client, test_user, monkeypatch):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)
    storage_path = f"{FEEDBACK_URL}/storage"

    res = await client.post(storage_path, headers=headers)

    assert res.status_code == 404
    assert not any(
        getattr(route, "path", None) == storage_path and "POST" in getattr(route, "methods", set())
        for route in app.routes
    )


async def test_apr_feedback_manifest_fields(client, test_user, monkeypatch):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)

    res = await client.get(
        "/api/apr/modules/primeira-conexao/lessons/enter-the-connection", headers=headers
    )

    manifest = res.json()
    assert manifest["version"] == "0.6.0-technical-placeholder"
    assert manifest["current_step_count"] == 5
    assert manifest["content_status"] == "technical-placeholder"
    assert manifest["authorized_for_pilot"] is False
    assert manifest["authorized_for_public_release"] is False
    assert [step["step_type"] for step in manifest["steps"]] == [
        "orientation",
        "information",
        "single_choice",
        "recording",
        "reflection",
    ]
    recording_step = manifest["steps"][3]
    expected_recording_fields = {
        "max_seconds": 10,
        "allow_retry": True,
        "preserve_original": True,
        "storage_status": "session-only",
        "transcription_language": "pt",
        "transcription_mode": "on-demand",
        "requires_learner_confirmation": True,
        "transcript_storage_status": "session-only",
        "transcript_authorized_as_evidence": False,
        "model_audio_id": "APR-R1-RM-01-L01-MODEL-TECH",
        "model_audio_mode": "on-demand",
        "model_audio_language": "pt-BR",
        "model_audio_source": "generated-technical-placeholder",
        "model_audio_storage_status": "session-only",
        "model_audio_authorized_as_final_content": False,
        "model_audio_required": False,
        "feedback_id": FEEDBACK_ID,
        "feedback_mode": "on-demand",
        "feedback_source_attempt": "original",
        "feedback_requires_confirmed_transcript": True,
        "feedback_source": "controlled-technical-placeholder",
        "feedback_storage_status": "session-only",
        "feedback_authorized_as_academic_feedback": False,
        "feedback_authorized_as_evidence": False,
        "feedback_required": False,
        "retry_orchestration_mode": "optional-post-feedback-latest-retry",
        "retry_required": False,
    }
    for field, value in expected_recording_fields.items():
        assert recording_step[field] == value


async def test_apr_does_not_expose_session_closure_or_academic_persistence_endpoints(
    client, test_user, monkeypatch
):
    _user, headers = test_user
    monkeypatch.setattr(settings, "APR_POC_ENABLED", True)
    forbidden_paths = [
        "/api/apr/modules/primeira-conexao/lessons/enter-the-connection/session-closure",
        "/api/apr/modules/primeira-conexao/lessons/enter-the-connection/completion",
        "/api/apr/modules/primeira-conexao/completion",
        "/api/apr/modules/primeira-conexao/lessons/enter-the-connection/progress",
        "/api/apr/modules/primeira-conexao/lessons/enter-the-connection/evidence",
    ]

    for path in forbidden_paths:
        res = await client.post(path, headers=headers)
        assert res.status_code == 404
        assert not any(
            getattr(route, "path", None) == path
            and "POST" in getattr(route, "methods", set())
            for route in app.routes
        )


def test_apr_does_not_add_persistence_model_or_migration():
    apr_model_files = list(Path("app/models").glob("*apr*"))
    apr_migration_files = list(Path("alembic/versions").glob("*apr*"))

    assert apr_model_files == []
    assert apr_migration_files == []

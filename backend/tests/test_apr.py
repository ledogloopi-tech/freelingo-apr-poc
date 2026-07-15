import httpx
import pytest
from sqlalchemy import func, select

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
    assert manifest["version"] == "0.3.0-technical-placeholder"
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
    assert manifest["version"] == "0.3.0-technical-placeholder"
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

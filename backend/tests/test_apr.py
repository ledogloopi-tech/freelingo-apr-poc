import pytest
from sqlalchemy import func, select

from app.core.config import settings
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
    res = await client.get(
        "/api/apr/modules/primeira-conexao/lessons/enter-the-connection"
    )

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
    assert manifest["version"] == "0.1.0-technical-placeholder"
    assert manifest["title"] == "Enter the Connection"
    assert manifest["internal_title"] == "Lesson Player Technical Demonstration"
    assert manifest["content_status"] == "technical-placeholder"
    assert manifest["authorized_for_pilot"] is False
    assert manifest["authorized_for_public_release"] is False
    assert manifest["current_step_count"] == 4
    assert len(manifest["steps"]) == 4
    assert [step["step_type"] for step in manifest["steps"]] == [
        "orientation",
        "information",
        "single_choice",
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
    assert manifest["steps"][3]["max_characters"] == 240

    plans_after = await db_session.scalar(select(func.count()).select_from(StudyPlan))
    progress_after = await db_session.scalar(select(func.count()).select_from(Progress))

    assert plans_after == plans_before
    assert progress_after == progress_before

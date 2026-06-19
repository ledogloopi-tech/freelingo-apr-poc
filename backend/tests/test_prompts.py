from __future__ import annotations

from app.routers.chat import _build_tutor_system_prompt
from app.services.conversation_pipeline import _build_conversation_system_prompt
from app.services.prompts.common import JSON_ONLY_INSTRUCTION, get_memory_system_instruction
from app.services.prompts.tutor import (
    build_conversation_system_prompt,
    build_tutor_system_prompt,
)


def test_chat_prompt_wrapper_matches_central_builder() -> None:
    kwargs = {
        "student_name": "Alice",
        "cefr_level": "B1",
        "native_language": "es",
        "target_language_name": "British English",
        "total_xp": 120,
        "streak": 4,
        "lessons_today": 2,
        "skills": "past tense, travel vocabulary",
        "user_context": "Student context:\n- Learning goals: travel\n",
        "memory_context": "Saved memories about the student:\n- Likes hiking\n",
    }

    assert _build_tutor_system_prompt(**kwargs) == build_tutor_system_prompt(**kwargs)


def test_conversation_prompt_wrapper_matches_central_builder() -> None:
    kwargs = {
        "student_name": "Alice",
        "cefr_level": "A2",
        "native_language": "es",
        "target_language_name": "French",
        "user_context": "Student context:\n- About the student: enjoys cooking\n",
        "memory_context": "Saved memories about the student:\n- Studies after work\n",
    }

    assert _build_conversation_system_prompt(**kwargs) == build_conversation_system_prompt(**kwargs)


def test_tutor_prompts_include_shared_memory_instruction() -> None:
    prompt = build_tutor_system_prompt(
        student_name="Alice",
        cefr_level="B1",
        native_language="es",
        target_language_name="German",
        total_xp=0,
        streak=0,
        lessons_today=0,
        skills="None yet",
        user_context="",
        memory_context="",
    )

    assert get_memory_system_instruction("German") in prompt
    assert "<<MEMORY>>" in prompt


def test_json_only_instruction_is_single_shared_block() -> None:
    assert JSON_ONLY_INSTRUCTION == (
        "IMPORTANT: Respond with ONLY a valid JSON object. "
        "No markdown, no code fences, no extra text."
    )

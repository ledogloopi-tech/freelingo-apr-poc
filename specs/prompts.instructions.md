---
description: "Prompt architecture reference: active LLM prompts, builders, shared blocks, variables, and maintenance rules."
---

# Prompt Architecture

This spec documents the prompt architecture after the Phase 0-2 prompt organization work.
The goal of this phase was architectural: centralize prompt text and composition while preserving
the current prompt behavior.

## Goals

- Keep active LLM prompts discoverable in one package.
- Preserve existing prompt wording unless a later prompt-improvement phase explicitly changes it.
- Separate reusable technical and tutoring blocks from service orchestration code.
- Keep service modules responsible for business flow, not prompt text ownership.
- Provide tests that catch accidental prompt-composition drift.

## Location

Prompt templates and builders live in:

```text
backend/app/services/prompts/
├── __init__.py
├── assessment.py      # CEFR placement, free-write assessment, end-of-level tests
├── common.py          # shared JSON, memory, and provider-helper prompt fragments
├── comprehension.py   # reading and listening generation prompts
├── flashcards.py      # flashcard generation and word lookup prompts
├── lesson.py          # lesson generation and exercise evaluation prompts
└── tutor.py           # text tutor and voice conversation system prompts
```

Service and router modules import builders from this package and pass runtime variables into them.

## Shared Blocks

| Block | File | Purpose |
|---|---|---|
| `JSON_ONLY_INSTRUCTION` | `prompts/common.py` | Appended by `llm_adapter.structured_output()` to require a JSON-only response. |
| `STRUCTURED_OUTPUT_RETRY_PROMPT` | `prompts/common.py` | Used by `llm_adapter` when the first structured-output response cannot be parsed. |
| `ANTHROPIC_SYSTEM_ONLY_TRIGGER` | `prompts/common.py` | Minimal user message for Anthropic calls where all task instructions are system messages. |
| `MEMORY_SYSTEM_INSTRUCTION_BASE` | `prompts/common.py` | Shared memory marker instructions appended to text chat and voice tutor prompts. |
| `get_memory_system_instruction()` | `prompts/common.py` | Formats the memory block for the current target language name. |

`memory_service.py` remains responsible for parsing, stripping, formatting, saving, and retrieving
memories. It re-exports the memory instruction helper for backward compatibility.

## Active Prompt Builders

| Builder | File | Caller | Role sent to LLM | Output expectation |
|---|---|---|---|---|
| `build_tutor_system_prompt()` | `prompts/tutor.py` | `routers/chat.py` | `system` | Streaming conversational text response. |
| `build_conversation_system_prompt()` | `prompts/tutor.py` | `services/conversation_pipeline.py` | `system` | Streaming voice-safe tutor response. |
| `build_lesson_generation_prompt()` | `prompts/lesson.py` | `services/lesson_generator.py` | `system` via `structured_output` | `LessonContent` JSON. |
| `build_fill_blank_eval_prompt()` | `prompts/lesson.py` | `services/lesson_generator.py` | `system` via `structured_output` | `FillBlankEvaluation` JSON. |
| `build_free_write_eval_prompt()` | `prompts/lesson.py` | `services/lesson_generator.py` | `system` via `structured_output` | `FreeWriteEvaluation` JSON. |
| `build_pronunciation_eval_prompt()` | `prompts/lesson.py` | `services/lesson_generator.py` | `system` via `structured_output` | `PronunciationEvaluation` JSON. |
| `build_flashcard_generation_prompt()` | `prompts/flashcards.py` | `services/flashcard_sm2.py` | `system` via `structured_output` | `FlashcardGenerateResponse` JSON. |
| `build_word_lookup_prompt()` | `prompts/flashcards.py` | `services/flashcard_sm2.py` | `system` via `structured_output` | `FlashcardCreate` JSON. |
| `build_listening_generation_prompt()` | `prompts/comprehension.py` | `services/listening_service.py` | `user` | Raw JSON parsed with `parse_llm_json()`. |
| `build_reading_generation_prompt()` | `prompts/comprehension.py` | `services/reading_service.py` | `user` | Raw JSON parsed with `parse_llm_json()`. |
| `build_free_write_assessment_prompt()` | `prompts/assessment.py` | `services/assessment.py` | `system` | Raw JSON parsed by assessment service. |
| `build_end_of_level_test_prompt()` | `prompts/assessment.py` | `services/assessment.py` | `system` | Raw JSON with `questions`. |
| `build_legacy_assessment_quiz_prompt()` | `prompts/assessment.py` | `routers/assessment.py` | `system` via `structured_output` | `LegacyQuizResponse` JSON. |
| `build_legacy_assessment_eval_user_prompt()` | `prompts/assessment.py` | `routers/assessment.py` | `user` via `structured_output` | User payload for legacy assessment evaluation. |

## Prompt Inventory

| Area | Template | Current behavior |
|---|---|---|
| Text tutor | `build_tutor_system_prompt()` | FreeLingo text tutor with mandatory scope, content policy, persona lock, progress context, optional user context, optional memories, target-language-only response, and no emoji/pictographic output. |
| Voice tutor | `build_conversation_system_prompt()` | FreeLingo voice conversation partner with the same safety core, shorter spoken responses, restrained correction policy, follow-up questions, and TTS-safe plain text. |
| Memory | `MEMORY_SYSTEM_INSTRUCTION_BASE` | Allows the LLM to append a hidden `<<MEMORY>>...<<ENDMEMORY>>` marker only when it learns a useful new student fact. |
| Lesson generation | `LESSON_GENERATION_PROMPT` | Generates structured lesson JSON constrained by CEFR level, target language, curriculum unit, grammar points, vocabulary sets, exercise schema, and valid grammar slugs. |
| Lesson fill-blank evaluation | `FILL_BLANK_EVAL_PROMPT` | Evaluates a fill-blank answer leniently for minor spelling/case variation and contractions. |
| Lesson free-write evaluation | `FREE_WRITE_EVAL_PROMPT` | Scores a writing answer and returns feedback plus correction objects. |
| Pronunciation evaluation | `PRONUNCIATION_EVAL_PROMPT` | Compares target phrase to STT transcription and returns score, feedback, and correctness. |
| Flashcard generation | `FLASHCARD_GEN_PROMPT` | Generates target-language vocabulary flashcards with native-language definition/translation and strict word cleanup rules. |
| Word lookup | `WORD_LOOKUP_PROMPT` | Generates one flashcard from a selected word and context sentence. |
| Listening generation | `LISTENING_GENERATION_PROMPT` | Generates plain-prose listening text and five multiple-choice comprehension questions. |
| Reading generation | `READING_GENERATION_PROMPT` | Generates plain-prose reading text and five multiple-choice comprehension questions. |
| Free-write assessment | `FREE_WRITE_ASSESSMENT_PROMPT` | Evaluates placement writing with adjusted level, writing score, analysis, strengths, and weaknesses. |
| End-of-level test | `END_OF_LEVEL_TEST_PROMPT` | Generates a 20-question test covering studied grammar and vocabulary for the current CEFR level. |
| Legacy assessment quiz | `LEGACY_ASSESSMENT_QUIZ_PROMPT` | Generates an adaptive CEFR quiz for legacy assessment flow. |
| Legacy assessment evaluation | `LEGACY_ASSESSMENT_EVAL_PROMPT` and `LEGACY_ASSESSMENT_EVAL_USER_PROMPT` | Evaluates legacy assessment answers with quiz/session payload. |

## Dynamic Variables

Common variables:

- `target_language_name`: human-readable target language, derived from BCP-47 code.
- `cefr_level` or `level`: learner level.
- `native_language`: user's native language, used for explanation/translation where relevant.
- `student_name`: display name or username.
- `user_context`: learning goals and bio; explicitly non-authoritative.
- `memory_context`: saved memories; explicitly non-authoritative.

Domain-specific variables:

- Tutor: `total_xp`, `streak`, `lessons_today`, `skills`.
- Lesson generation: `lesson_type`, `topic`, `unit_id`, `grammar_points`, `vocabulary_set_ids`, `week`, `day`, `valid_slugs`.
- Lesson evaluation: `question`, `correct_answer`, `student_answer`, `prompt`, `criteria`, `answer`, `target`, `transcription`.
- Flashcards: `topic`, `count`, `word`, `context`, `lang_hint`.
- Reading/listening: `exercise_type`, `exercise_type_desc`, `topic`, `word_count`.
- Assessment: `preliminary_level`, `next_level`, `grammar_points_studied`, `vocabulary_sets_studied`, `session_id`, `quiz`, `answers`.

## Behavior-Critical Prompts

The following prompts are behavior-critical and should not be changed casually:

- Text tutor and voice tutor system prompts.
- Memory marker instruction.
- Lesson generation prompt and exercise schema.
- Fill-blank, free-write, and pronunciation evaluation prompts.
- Flashcard generation and word lookup prompts.
- Reading/listening generation prompts.
- Assessment generation/evaluation prompts.

Changes to these prompts can alter LLM output quality, safety behavior, schema validity, grading, or
student-facing language. Treat such edits as product behavior changes.

## Maintenance Rules

1. Prefer adding or editing prompt text in `backend/app/services/prompts/`, not in routers.
2. Keep service modules focused on assembling runtime variables and handling LLM responses.
3. Do not duplicate safety, JSON-only, memory, or provider-helper prompt fragments.
4. Preserve current prompt text during architecture-only refactors.
5. If a prompt change intentionally changes behavior, document the reason and expected improvement.
6. For target-language or CEFR improvements, add explicit tests proving the right block is injected.
7. For schema-producing prompts, keep `structured_output()` or explicit JSON parsing tests in place.
8. Do not remove backward-compatible constants/imports until tests and specs are updated together.

## Tests

Prompt architecture is covered by:

- `backend/tests/test_prompts.py` for builder/wrapper equivalence and shared block checks.
- Existing conversation pipeline prompt tests in `backend/tests/test_conversation_pipeline_service.py`.
- Existing service tests that mock LLM calls and validate parsed outputs.

Recommended validation for prompt-only architecture changes:

```bash
python3 -m compileall backend/app backend/alembic -q
./.venv/bin/pytest backend/tests/test_prompts.py backend/tests/test_conversation_pipeline_service.py -q --no-cov
```

The project-level backend test command enforces total coverage. Running only a subset can fail the
coverage threshold even when the selected tests pass.

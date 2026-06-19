"""Prompt templates and builders for reading and listening exercises."""

LISTENING_GENERATION_PROMPT = """\
You are a {target_language_name} language content creator. Generate a listening comprehension exercise \
for a {level} learner. Target language: {target_language_name}.

Requirements:
- Exercise type: {exercise_type} ({exercise_type_desc})
- Length: approximately {word_count} words
- Use {target_language_name} vocabulary and spelling conventions
- Write naturally, as if it will be read aloud
- Do not use headers, markdown, lists, or formatting — plain flowing prose only

Return ONLY valid JSON with no prose, no code fences, no extra text:
{{
  "topic": "<brief topic label, max 10 words>",
  "text": "<exercise text as flowing prose>",
  "questions": [
    {{
      "index": 0,
      "question": "<question text>",
      "options": {{ "A": "<option>", "B": "<option>", "C": "<option>", "D": "<option>" }},
      "correct": "<A|B|C|D>"
    }}
  ]
}}

Include exactly 5 questions ordered by cognitive demand:
- Q0-Q1: literal comprehension (directly stated information)
- Q2-Q3: inference (implied meaning, tone, or purpose)
- Q4: vocabulary or register (word meaning in context or formality level)"""

READING_GENERATION_PROMPT = """\
You are a {target_language_name} language content creator. Generate a reading comprehension exercise \
for a {level} learner. Target language: {target_language_name}.

Requirements:
- Exercise type: {exercise_type} ({exercise_type_desc})
- Topic area: {topic}
- Length: approximately {word_count} words
- Use {target_language_name} vocabulary and spelling conventions
- Write in the natural register appropriate for the exercise type
- Do not use headers, markdown, or lists — plain flowing prose only
  (exception: emails may include a greeting and sign-off)

Return ONLY valid JSON with no prose, no code fences, no extra text:
{{
  "topic": "<brief topic label, max 10 words>",
  "text": "<exercise text as flowing prose>",
  "questions": [
    {{
      "index": 0,
      "question": "<question text>",
      "options": {{ "A": "<option>", "B": "<option>", "C": "<option>", "D": "<option>" }},
      "correct": "<A|B|C|D>"
    }}
  ]
}}

Include exactly 5 questions ordered by cognitive demand:
- Q0-Q1: literal comprehension (directly stated information)
- Q2-Q3: inference (implied meaning, tone, or purpose)
- Q4: vocabulary or register (word meaning in context or formality level)"""


def build_listening_generation_prompt(
    *,
    target_language_name: str,
    level: str,
    exercise_type: str,
    exercise_type_desc: str,
    word_count: int,
) -> str:
    return LISTENING_GENERATION_PROMPT.format(
        target_language_name=target_language_name,
        level=level,
        exercise_type=exercise_type,
        exercise_type_desc=exercise_type_desc,
        word_count=word_count,
    )


def build_reading_generation_prompt(
    *,
    target_language_name: str,
    level: str,
    exercise_type: str,
    exercise_type_desc: str,
    topic: str,
    word_count: int,
) -> str:
    return READING_GENERATION_PROMPT.format(
        target_language_name=target_language_name,
        level=level,
        exercise_type=exercise_type,
        exercise_type_desc=exercise_type_desc,
        topic=topic,
        word_count=word_count,
    )


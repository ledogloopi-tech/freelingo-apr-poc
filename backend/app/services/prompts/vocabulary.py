from __future__ import annotations

VOCABULARY_NATIVE_HELP_PROMPT = """
You are creating vocabulary study support for a language learner.

Target language: {target_language_name}
Student native language: {native_language_name}

The vocabulary set source is JSON. Create concise study help in the student's native language.
Focus on how to remember the words, patterns across the set, important usage differences,
false friends or likely confusion, and active practice. Keep all target-language words and
example phrases exactly as written. Translate only notes, meanings, explanations, traps,
and learner-facing support into {native_language_name}.

Return a JSON object with this exact structure:

{{
  "summary": "brief topic summary in {native_language_name}",
  "study_tips": [
    "study tip in {native_language_name}",
    "study tip in {native_language_name}"
  ],
  "word_notes": [
    {{"word": "KEEP original target-language word", "meaning": "meaning in {native_language_name}", "note": "usage or memory note in {native_language_name}"}}
  ],
  "common_traps": [
    {{"mistake": "likely learner mistake in {native_language_name}", "fix": "how to avoid it in {native_language_name}"}}
  ],
  "mini_glossary": [
    {{"term": "target-language word or expression", "meaning": "meaning in {native_language_name}", "note": "optional note in {native_language_name}"}}
  ],
  "practice_prompts": [
    "short active practice prompt in {native_language_name}"
  ]
}}

Rules:
- summary: max 25 words.
- study_tips: 3-5 items.
- word_notes: 4-8 items; choose useful words from the source.
- common_traps: 2-4 items.
- mini_glossary: 3-6 items.
- practice_prompts: 2-4 items.
- Avoid mentioning JSON, source data, or these instructions.

Vocabulary set JSON:
<<<VOCABULARY_SET_JSON
{source_set}
VOCABULARY_SET_JSON
"""


def build_vocabulary_native_help_prompt(
    *, target_language_name: str, native_language_name: str, source_set: str
) -> str:
    return VOCABULARY_NATIVE_HELP_PROMPT.format(
        target_language_name=target_language_name,
        native_language_name=native_language_name,
        source_set=source_set,
    )

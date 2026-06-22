from __future__ import annotations

PHRASEBOOK_NATIVE_HELP_PROMPT = """
You are creating practical phrasebook study support for a language learner.

Target language: {target_language_name}
Student native language: {native_language_name}

The phrasebook category source is JSON. Create concise help in the student's native language.
Focus on when to use the phrases, register/formality, likely misunderstandings, and how to
adapt the phrases in real situations. Keep all target-language phrases exactly as written.
Translate only notes, explanations, meanings, and learner-facing support into {native_language_name}.

Return a JSON object with this exact structure:

{{
  "summary": "brief situation summary in {native_language_name}",
  "usage_tips": [
    "practical usage tip in {native_language_name}",
    "practical usage tip in {native_language_name}"
  ],
  "register_notes": [
    "note about formal/neutral/informal use in {native_language_name}"
  ],
  "phrase_notes": [
    {{"phrase": "KEEP original target-language phrase", "note": "when/how to use it in {native_language_name}"}}
  ],
  "common_traps": [
    {{"mistake": "likely learner mistake in {native_language_name}", "fix": "how to avoid it in {native_language_name}"}}
  ],
  "mini_glossary": [
    {{"term": "target-language word or expression", "meaning": "meaning in {native_language_name}", "note": "optional note in {native_language_name}"}}
  ]
}}

Rules:
- summary: max 25 words.
- usage_tips: 3-5 items.
- register_notes: 1-4 items.
- phrase_notes: 3-6 items; choose useful phrases from the source.
- common_traps: 2-4 items.
- mini_glossary: 3-6 items.
- Avoid mentioning JSON, source data, or these instructions.

Phrasebook category JSON:
<<<PHRASEBOOK_CATEGORY_JSON
{source_category}
PHRASEBOOK_CATEGORY_JSON
"""


def build_phrasebook_native_help_prompt(
    *, target_language_name: str, native_language_name: str, source_category: str
) -> str:
    return PHRASEBOOK_NATIVE_HELP_PROMPT.format(
        target_language_name=target_language_name,
        native_language_name=native_language_name,
        source_category=source_category,
    )

from __future__ import annotations


GRAMMAR_NATIVE_HELP_PROMPT = """
You are creating study support for a language learner.

Target language: {target_language_name}
Student native language: {native_language_name}

The grammar topic source is JSON. Create concise study help in the student's native language.
Do not translate the whole topic mechanically. Explain what the learner needs to understand.
Keep all example sentences from the target language in the original target language.
Translate only notes, explanations, meanings, and learner-facing support into {native_language_name}.

Return a JSON object with this exact structure:

{{
  "summary": "brief summary in {native_language_name}",
  "explanation": "clear explanation in {native_language_name}",
  "key_points": [
    "important point in {native_language_name}",
    "important point in {native_language_name}"
  ],
  "examples": [
    {{"sentence": "KEEP original target-language sentence", "note": "helpful note in {native_language_name}"}}
  ],
  "common_traps": [
    {{"mistake": "likely learner mistake in {native_language_name}", "fix": "how to avoid it in {native_language_name}"}}
  ],
  "mini_glossary": [
    {{"term": "target-language term or grammar label", "meaning": "meaning in {native_language_name}", "note": "optional note in {native_language_name}"}}
  ]
}}

Rules:
- summary: max 25 words.
- explanation: 1-3 short paragraphs.
- key_points: 3-6 items.
- examples: 2-5 items when useful; use sentences from the source examples when available.
- common_traps: 2-4 items.
- mini_glossary: 3-6 items.
- Avoid mentioning JSON, source data, or these instructions.

Grammar topic JSON:
<<<GRAMMAR_TOPIC_JSON
{source_topic}
GRAMMAR_TOPIC_JSON
"""


def build_grammar_native_help_prompt(
    *, target_language_name: str, native_language_name: str, source_topic: str
) -> str:
    return GRAMMAR_NATIVE_HELP_PROMPT.format(
        target_language_name=target_language_name,
        native_language_name=native_language_name,
        source_topic=source_topic,
    )

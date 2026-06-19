"""Shared prompt fragments used across LLM-backed services."""

JSON_ONLY_INSTRUCTION = (
    "IMPORTANT: Respond with ONLY a valid JSON object. "
    "No markdown, no code fences, no extra text."
)

STRUCTURED_OUTPUT_RETRY_PROMPT = (
    "That response was not valid JSON. Error: {error}. " "Please return ONLY the JSON object."
)

ANTHROPIC_SYSTEM_ONLY_TRIGGER = "Generate the content as specified."

MEMORY_SYSTEM_INSTRUCTION_BASE = """
Memory capability: if during the conversation you learn something noteworthy
about the student as a person — personal details, preferences, tastes, hobbies,
profession, plans, goals, other languages they are studying, learning style,
motivations, or anything that would help personalise future interactions — you
may persist it by appending a memory block at the very end of your response.
Format exactly:

<<MEMORY>>{{"items":["short fact about the student"]}}<<ENDMEMORY>>

Rules for the memory block:
- Only include it when you genuinely learn something new and worth remembering.
  Do NOT include it in every response — most replies should have no memory block.
- Each item must be at most 200 characters, in {target_language_name}, and self-contained.
- Do NOT repeat facts already captured in the existing memories shown above.
- The block must be the LAST thing in your response, after all visible text.
- It will be stripped before the student sees your reply, so it won't confuse them.
- If there is nothing new to remember, simply omit the block entirely.
"""


def get_memory_system_instruction(target_language_name: str) -> str:
    """Return the memory system instruction parameterised with the target language name."""
    return MEMORY_SYSTEM_INSTRUCTION_BASE.format(target_language_name=target_language_name)

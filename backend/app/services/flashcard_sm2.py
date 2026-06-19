import re
from datetime import date, timedelta

from app.models.flashcard import Flashcard
from app.schemas.flashcards import (
    FlashcardCreate,
    FlashcardGenerateResponse,
    GeneratedFlashcard,
)
from app.services.language_helpers import get_language_name
from app.services.llm_adapter import llm_adapter
from app.services.prompts import flashcards as flashcard_prompts
from app.services.prompts.flashcards import (
    build_flashcard_generation_prompt,
    build_word_lookup_prompt,
)

FLASHCARD_GEN_PROMPT = flashcard_prompts.FLASHCARD_GEN_PROMPT
WORD_LOOKUP_PROMPT = flashcard_prompts.WORD_LOOKUP_PROMPT


def sm2_update(card: Flashcard, quality: int) -> Flashcard:
    if quality < 3:
        card.repetitions = 0
        card.interval = 1
    else:
        if card.repetitions == 0:
            card.interval = 1
        elif card.repetitions == 1:
            card.interval = 6
        else:
            card.interval = round(card.interval * card.ease_factor)
        card.repetitions += 1

    card.ease_factor = max(
        1.3,
        card.ease_factor + 0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02),
    )
    card.next_review = date.today() + timedelta(days=card.interval)
    return card


_LANG_HINTS: dict[str, str] = {
    "de": ("Use standard German spelling and vocabulary."),
    "fr": "Use standard French spelling and vocabulary.",
    "es": "Use Spanish from Spain spelling and vocabulary.",
    "it": "Use standard Italian spelling and vocabulary.",
    "pt": "Use European Portuguese spelling and vocabulary.",
    "en-US": ("Use American English spelling and vocabulary (e.g. color, center, organize)."),
    "en-GB": ("Use British English spelling and vocabulary (e.g. colour, centre, organise)."),
}


def _clean_generated_word(value: str) -> str:
    cleaned = value.strip().strip("\"'")
    cleaned = re.sub(r"\s*\([^)]*\)", "", cleaned)
    return re.sub(r"\s+", " ", cleaned).strip()


def _get_lang_hint(target_language: str) -> str:
    hint = _LANG_HINTS.get(target_language)
    if hint is not None:
        return hint
    iso = target_language.split("-")[0].lower()
    return _LANG_HINTS.get(iso, "")


async def generate_flashcards(
    topic: str, count: int, cefr_level: str, native_language: str, target_language: str = "en-GB"
) -> FlashcardGenerateResponse:
    target_language_name = get_language_name(target_language)
    lang_hint = _get_lang_hint(target_language)
    prompt = build_flashcard_generation_prompt(
        topic=topic,
        count=count,
        cefr_level=cefr_level,
        native_language=native_language,
        target_language_name=target_language_name,
        lang_hint=lang_hint,
    )

    result = await llm_adapter.structured_output(
        [{"role": "system", "content": prompt}],
        FlashcardGenerateResponse,
    )
    result.flashcards = [
        GeneratedFlashcard(
            word=_clean_generated_word(card.word),
            definition=card.definition,
            example_sentence=card.example_sentence,
            translation=card.translation,
        )
        for card in result.flashcards
    ]
    return result


async def lookup_word(
    word: str,
    context: str,
    cefr_level: str,
    native_language: str,
    target_language: str = "en-GB",
) -> FlashcardCreate:
    target_language_name = get_language_name(target_language)
    lang_hint = _get_lang_hint(target_language)
    prompt = build_word_lookup_prompt(
        word=word,
        context=context or word,
        cefr_level=cefr_level,
        native_language=native_language,
        target_language_name=target_language_name,
        lang_hint=lang_hint,
    )
    result = await llm_adapter.structured_output(
        [{"role": "system", "content": prompt}],
        FlashcardCreate,
    )
    result.word = _clean_generated_word(result.word)
    return result

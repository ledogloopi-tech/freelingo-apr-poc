"""Shared helpers for Mainland Chinese phrasebook categories."""

from app.data._types import CEFRLevel, PhrasebookCategory, PhrasebookEntry, Register

PhraseSpec = tuple[str, str, Register, str]
CategorySpec = tuple[str, str, str, list[PhraseSpec]]


def build_category(level: CEFRLevel, spec: CategorySpec) -> PhrasebookCategory:
    category_id, situation, icon, phrases = spec
    return PhrasebookCategory(
        id=category_id,
        level=level,
        situation=situation,
        icon=icon,
        phrases=[
            PhrasebookEntry(text=text, context=context, register=register, unit_ref=unit_ref)
            for text, context, register, unit_ref in phrases
        ],
    )

"""Shared helpers for Mainland Chinese phrasebook categories."""

from app.data._types import CEFRLevel, PhrasebookCategory, PhrasebookEntry, Register

# (text, context, register, unit_ref[, romanization])
PhraseSpec = tuple[str, str, Register, str] | tuple[str, str, Register, str, str]
CategorySpec = tuple[str, str, str, list[PhraseSpec]]


def build_category(level: CEFRLevel, spec: CategorySpec) -> PhrasebookCategory:
    category_id, situation, icon, phrases = spec
    entries: list[PhrasebookEntry] = []
    for p in phrases:
        text, context, register, unit_ref = p[0], p[1], p[2], p[3]
        romanization: str | None = p[4] if len(p) >= 5 else None
        entries.append(
            PhrasebookEntry(
                text=text,
                context=context,
                register=register,
                unit_ref=unit_ref,
                romanization=romanization,
            )
        )
    return PhrasebookCategory(
        id=category_id,
        level=level,
        situation=situation,
        icon=icon,
        phrases=entries,
    )

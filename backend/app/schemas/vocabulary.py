from __future__ import annotations

from pydantic import BaseModel


class VocabularyEntryResponse(BaseModel):
    word: str
    pos: str
    definition: str
    example: str
    ipa: str | None = None
    frequency_rank: int | None = None


class VocabularySetResponse(BaseModel):
    id: str
    level: str
    topic: str
    unit_ref: str
    words: list[VocabularyEntryResponse]


class VocabularySetsResponse(BaseModel):
    sets: list[VocabularySetResponse]


class VocabularySetDetailResponse(BaseModel):
    set: VocabularySetResponse


class VocabularyNativeHelpWordNoteResponse(BaseModel):
    word: str
    meaning: str
    note: str


class VocabularyNativeHelpTrapResponse(BaseModel):
    mistake: str
    fix: str


class VocabularyNativeHelpGlossaryResponse(BaseModel):
    term: str
    meaning: str
    note: str | None = None


class VocabularyNativeHelpContentResponse(BaseModel):
    summary: str
    study_tips: list[str]
    word_notes: list[VocabularyNativeHelpWordNoteResponse]
    common_traps: list[VocabularyNativeHelpTrapResponse]
    mini_glossary: list[VocabularyNativeHelpGlossaryResponse]
    practice_prompts: list[str]


class VocabularyNativeHelpResponse(BaseModel):
    native_help: VocabularyNativeHelpContentResponse

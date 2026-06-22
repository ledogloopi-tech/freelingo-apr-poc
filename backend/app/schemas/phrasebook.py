from __future__ import annotations

import warnings

from pydantic import BaseModel

warnings.filterwarnings(
    "ignore",
    message=r'Field name "register" in "PhrasebookEntryResponse" shadows.*',
    category=UserWarning,
)


class PhrasebookEntryResponse(BaseModel):
    text: str
    context: str
    register: str
    unit_ref: str | None = None
    romanization: str | None = None


class PhrasebookCategoryResponse(BaseModel):
    id: str
    level: str
    situation: str
    icon: str
    phrases: list[PhrasebookEntryResponse]


class PhrasebookCategoriesResponse(BaseModel):
    categories: list[PhrasebookCategoryResponse]


class PhrasebookCategoryDetailResponse(BaseModel):
    category: PhrasebookCategoryResponse


class PhrasebookNativeHelpPhraseNoteResponse(BaseModel):
    phrase: str
    note: str


class PhrasebookNativeHelpTrapResponse(BaseModel):
    mistake: str
    fix: str


class PhrasebookNativeHelpGlossaryResponse(BaseModel):
    term: str
    meaning: str
    note: str | None = None


class PhrasebookNativeHelpContentResponse(BaseModel):
    summary: str
    usage_tips: list[str]
    register_notes: list[str]
    phrase_notes: list[PhrasebookNativeHelpPhraseNoteResponse]
    common_traps: list[PhrasebookNativeHelpTrapResponse]
    mini_glossary: list[PhrasebookNativeHelpGlossaryResponse]


class PhrasebookNativeHelpResponse(BaseModel):
    native_help: PhrasebookNativeHelpContentResponse

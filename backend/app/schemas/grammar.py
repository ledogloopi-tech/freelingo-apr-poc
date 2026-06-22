from __future__ import annotations

from pydantic import BaseModel


class GrammarExampleResponse(BaseModel):
    text: str
    translation: str | None = None
    note: str | None = None


class GrammarMistakeResponse(BaseModel):
    wrong: str
    correct: str
    note: str


class GrammarTopicResponse(BaseModel):
    slug: str
    title: str
    level: str
    category: str
    summary: str
    explanation: str
    structure: str | None = None
    rules: list[str]
    examples: list[GrammarExampleResponse]
    common_mistakes: list[GrammarMistakeResponse]
    related: list[str]


class GrammarTopicsResponse(BaseModel):
    topics: list[GrammarTopicResponse]


class GrammarTopicDetailResponse(BaseModel):
    topic: GrammarTopicResponse


class GrammarNativeHelpExampleResponse(BaseModel):
    sentence: str
    note: str


class GrammarNativeHelpTrapResponse(BaseModel):
    mistake: str
    fix: str


class GrammarNativeHelpGlossaryResponse(BaseModel):
    term: str
    meaning: str
    note: str | None = None


class GrammarNativeHelpContentResponse(BaseModel):
    summary: str
    explanation: str
    key_points: list[str]
    examples: list[GrammarNativeHelpExampleResponse]
    common_traps: list[GrammarNativeHelpTrapResponse]
    mini_glossary: list[GrammarNativeHelpGlossaryResponse]


class GrammarNativeHelpResponse(BaseModel):
    native_help: GrammarNativeHelpContentResponse

from typing import Literal

from pydantic import BaseModel, Field


class AprModuleMetadata(BaseModel):
    module_id: str
    title: str
    status: str
    target_language: str
    bridge_language: str
    authorized_for_pilot: bool
    authorized_for_public_release: bool


class AprLessonStepBase(BaseModel):
    step_id: str
    step_type: str
    title: str
    body: str
    required: bool


class AprOrientationStep(AprLessonStepBase):
    step_type: Literal["orientation"]


class AprInformationStep(AprLessonStepBase):
    step_type: Literal["information"]


class AprSingleChoiceOption(BaseModel):
    option_id: str
    label: str
    feedback: str


class AprSingleChoiceStep(AprLessonStepBase):
    step_type: Literal["single_choice"]
    options: list[AprSingleChoiceOption]


class AprRecordingStep(AprLessonStepBase):
    step_type: Literal["recording"]
    prompt: str
    max_seconds: int = Field(gt=0)
    allow_retry: bool
    preserve_original: bool
    storage_status: Literal["session-only"]


class AprReflectionStep(AprLessonStepBase):
    step_type: Literal["reflection"]
    prompt: str
    placeholder: str | None = None
    max_characters: int = Field(gt=0)


AprLessonStep = (
    AprOrientationStep
    | AprInformationStep
    | AprSingleChoiceStep
    | AprRecordingStep
    | AprReflectionStep
)


class AprLessonManifest(BaseModel):
    lesson_id: str
    module_id: str
    version: str
    title: str
    internal_title: str
    content_status: str
    authorized_for_pilot: bool
    authorized_for_public_release: bool
    estimated_minutes: int
    current_step_count: int
    steps: list[AprLessonStep]

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


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
    transcription_language: Literal["pt"]
    transcription_mode: Literal["on-demand"]
    requires_learner_confirmation: bool
    transcript_storage_status: Literal["session-only"]
    transcript_authorized_as_evidence: bool
    model_audio_id: str
    model_audio_mode: Literal["on-demand"]
    model_audio_language: Literal["pt-BR"]
    model_audio_source: Literal["generated-technical-placeholder"]
    model_audio_storage_status: Literal["session-only"]
    model_audio_authorized_as_final_content: bool
    model_audio_required: bool
    feedback_id: str
    feedback_mode: Literal["on-demand"]
    feedback_source_attempt: Literal["original"]
    feedback_requires_confirmed_transcript: bool
    feedback_source: Literal["controlled-technical-placeholder"]
    feedback_storage_status: Literal["session-only"]
    feedback_authorized_as_academic_feedback: bool
    feedback_authorized_as_evidence: bool
    feedback_required: bool
    retry_orchestration_mode: Literal["optional-post-feedback-latest-retry"]
    retry_required: bool


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


class AprTranscriptDraftResponse(BaseModel):
    attempt_role: Literal["original", "latest_retry"]
    draft_text: str
    language: Literal["pt"]
    status: Literal["machine-generated-draft"]
    requires_learner_confirmation: bool
    authorized_as_evidence: bool
    storage_status: Literal["session-only"]


class AprModelAudioRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    model_audio_id: str


class AprModelAudioMetadata(BaseModel):
    model_audio_id: str
    language: Literal["pt-BR"]
    status: Literal["generated-technical-placeholder"]
    storage_status: Literal["session-only"]
    authorized_as_final_content: bool
    required: bool


class AprFeedbackDraftRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    feedback_id: str
    attempt_role: Literal["original"]
    transcript_confirmation_revision: int = Field(ge=1)


class AprFeedbackDraftResponse(BaseModel):
    feedback_id: str
    attempt_role: Literal["original"]
    source_confirmation_revision: int
    status: Literal["technical-placeholder"]
    source: Literal["server-controlled"]
    acknowledgement: str
    primary_priority: str
    cue: str
    retry_instruction: str
    uncertainty: str
    requires_retry: bool
    retry_allowed: bool
    authorized_as_academic_feedback: bool
    authorized_as_evidence: bool
    storage_status: Literal["session-only"]

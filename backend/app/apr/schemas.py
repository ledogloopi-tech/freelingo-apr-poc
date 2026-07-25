from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, StringConstraints


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
    content_ids: list[str] = Field(default_factory=list)


class AprOrientationStep(AprLessonStepBase):
    step_type: Literal["orientation"]


class AprContentBlock(BaseModel):
    content_id: str
    heading: str
    body: str


class AprModelAudioConfig(BaseModel):
    model_audio_id: str
    temporary_audio_id: str
    mode: Literal["on-demand"]
    language: Literal["pt-BR"]
    source: Literal["generated-temporary-testing"]
    storage_status: Literal["session-only"]
    authorized_as_final_content: bool
    required: bool
    disclosure: str


class AprInformationStep(AprLessonStepBase):
    step_type: Literal["information"]
    model_script: str | None = None
    controlled_transcript: str | None = None
    transcript_label: str | None = None
    optional_translation: str | None = None
    translation_label: str | None = None
    spanish_bridge: AprContentBlock | None = None
    pronunciation_guidance: AprContentBlock | None = None
    pragmatic_guidance: AprContentBlock | None = None
    model_audio: AprModelAudioConfig | None = None


class AprSingleChoiceOption(BaseModel):
    option_id: str
    label: str
    feedback: str


class AprSingleChoiceStep(AprLessonStepBase):
    step_type: Literal["single_choice"]
    options: list[AprSingleChoiceOption]
    correct_option_id: str
    prompt_label: str = "Elige una respuesta."
    required_warning: str = "Selecciona una opción antes de continuar."


class AprWrittenAlternative(BaseModel):
    content_id: str
    label: str
    notice: str
    prompt: str
    frame: str
    storage_status: Literal["session-only"]
    practice_classification: Literal["instructional-practice-only"]
    max_characters: int = Field(gt=0, le=240)


class AprRecordingStep(AprLessonStepBase):
    step_type: Literal["recording"]
    prompt: str
    production_frame: str
    privacy_notice: str
    practice_notice: str
    max_seconds: int = Field(gt=0)
    allow_retry: bool
    preserve_original: bool
    storage_status: Literal["session-only"]
    transcription_language: Literal["pt"]
    transcription_mode: Literal["on-demand"]
    requires_learner_confirmation: bool
    transcript_storage_status: Literal["session-only"]
    transcript_authorized_as_evidence: bool
    feedback_id: str
    feedback_mode: Literal["on-demand"]
    feedback_source_attempt: Literal["original"]
    feedback_requires_confirmed_transcript: bool
    feedback_source: Literal["server-deterministic"]
    feedback_storage_status: Literal["session-only"]
    feedback_authorized_as_academic_feedback: bool
    feedback_authorized_as_evidence: bool
    feedback_required: bool
    retry_orchestration_mode: Literal["optional-post-feedback-latest-retry"]
    retry_required: bool
    retry_instruction: str
    written_alternative: AprWrittenAlternative


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


class AprSessionClosureContent(BaseModel):
    content_id: str
    badge: str
    heading: str
    body: str
    primary_action: str
    secondary_action: str


class AprLessonManifest(BaseModel):
    lesson_id: str
    module_id: str
    content_package_id: str
    version: str
    title: str
    internal_title: str
    content_status: str
    practice_classification: str
    authorization_notice: str
    authorized_for_pilot: bool
    authorized_for_public_release: bool
    estimated_minutes: int
    current_step_count: int
    session_closure: AprSessionClosureContent
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
    status: Literal["generated-temporary-testing"]
    storage_status: Literal["session-only"]
    authorized_as_final_content: bool
    required: bool


ConfirmedTranscript = Annotated[
    str, StringConstraints(strip_whitespace=True, min_length=1, max_length=500)
]


class AprFeedbackDraftRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    feedback_id: str
    attempt_role: Literal["original"]
    transcript_confirmation_revision: int = Field(ge=1)
    confirmed_transcript: ConfirmedTranscript


class AprFeedbackDraftResponse(BaseModel):
    feedback_id: str
    feedback_case: str
    attempt_role: Literal["original"]
    source_confirmation_revision: int
    status: Literal["controlled-instructional-guidance"]
    source: Literal["server-deterministic"]
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

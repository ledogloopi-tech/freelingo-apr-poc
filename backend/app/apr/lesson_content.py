from app.apr.schemas import (
    AprInformationStep,
    AprLessonManifest,
    AprOrientationStep,
    AprRecordingStep,
    AprReflectionStep,
    AprSingleChoiceOption,
    AprSingleChoiceStep,
)

ENTER_THE_CONNECTION_LESSON = AprLessonManifest(
    lesson_id="APR-R1-RM-01-L01-TECH",
    module_id="APR-R1-RM-01",
    version="0.3.0-technical-placeholder",
    title="Enter the Connection",
    internal_title="Lesson Player Technical Demonstration",
    content_status="technical-placeholder",
    authorized_for_pilot=False,
    authorized_for_public_release=False,
    estimated_minutes=5,
    current_step_count=5,
    steps=[
        AprOrientationStep(
            step_id="orientation",
            step_type="orientation",
            title="Orientation",
            body=(
                "Technical placeholder lesson. Approved lesson content pending. "
                "This interaction tests the APR lesson player, not Portuguese capability. "
                "It is not academically approved, not authorized for pilot, and not authorized "
                "for public release."
            ),
            required=True,
        ),
        AprInformationStep(
            step_id="information",
            step_type="information",
            title="Information",
            body=(
                "This placeholder screen demonstrates that versioned structured lesson content "
                "can be loaded inside the isolated APR backend and frontend boundary. It does "
                "not contain final Lesson 1 curriculum or language instruction."
            ),
            required=True,
        ),
        AprSingleChoiceStep(
            step_id="interface-choice",
            step_type="single_choice",
            title="Single-choice interaction",
            body=(
                "Choose any interface-testing option. This does not evaluate Portuguese ability, "
                "does not create Entry Evidence, and does not produce Capability Observations."
            ),
            required=True,
            options=[
                AprSingleChoiceOption(
                    option_id="layout-clear",
                    label="The layout is clear enough to continue testing.",
                    feedback="Fixed technical feedback: the lesson player recorded this session-only selection.",
                ),
                AprSingleChoiceOption(
                    option_id="need-review",
                    label="The placeholder needs future academic review.",
                    feedback="Fixed technical feedback: future approved lesson specifications can replace this placeholder.",
                ),
                AprSingleChoiceOption(
                    option_id="not-assessment",
                    label="This is not a Portuguese assessment.",
                    feedback="Fixed technical feedback: no language capability was calculated.",
                ),
            ],
        ),
        AprRecordingStep(
            step_id="microphone-capture",
            step_type="recording",
            title="Microphone capture",
            body=(
                "Record a brief technical microphone test. Transcription starts only after "
                "you request it. The result is a machine-generated draft that you must "
                "review and correct. Confirmation does not turn it into academic evidence, "
                "and transcript state is session-only."
            ),
            required=True,
            prompt=(
                "This recording remains only in this browser session until you request a "
                "transcript draft. Transcript confirmation is not a score, language result, "
                "or academic evidence, and APR does not save transcript state during this POC."
            ),
            max_seconds=10,
            allow_retry=True,
            preserve_original=True,
            storage_status="session-only",
            transcription_language="pt",
            transcription_mode="on-demand",
            requires_learner_confirmation=True,
            transcript_storage_status="session-only",
            transcript_authorized_as_evidence=False,
        ),
        AprReflectionStep(
            step_id="technical-reflection",
            step_type="reflection",
            title="Reflection",
            body=(
                "Enter a short technical note about the shell behavior only. This is not saved "
                "to the backend and does not count as academic Lesson completion."
            ),
            required=False,
            prompt="What should the APR team verify before replacing this placeholder with an approved lesson specification?",
            placeholder="Example: Confirm approved content, evidence rules, and learner-facing copy.",
            max_characters=240,
        ),
    ],
)

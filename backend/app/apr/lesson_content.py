from app.apr.schemas import (
    AprContentBlock,
    AprInformationStep,
    AprLessonManifest,
    AprModelAudioConfig,
    AprOrientationStep,
    AprRecordingStep,
    AprReflectionStep,
    AprSessionClosureContent,
    AprSingleChoiceOption,
    AprSingleChoiceStep,
    AprWrittenAlternative,
)

CONTENT_PACKAGE_ID = "APR-R1-RM01-L01-D9"
MODEL_SCRIPT = "Oi! Eu sou a Marina. Gosto de música. E você?"
MODEL_AUDIO_ID = "APR-AUD-R1-RM01-L01-D9-MDL-001"
TEMPORARY_AUDIO_ID = "APR-AUD-R1-RM01-L01-D9-TMP-001"
FEEDBACK_ID = "APR-FBK-R1-RM01-L01-D9-001"

ENTER_THE_CONNECTION_LESSON = AprLessonManifest(
    lesson_id="APR-R1-RM-01-L01",
    module_id="APR-R1-RM-01",
    content_package_id=CONTENT_PACKAGE_ID,
    version="1.0.0-day9-controlled-slice",
    title="Enter the Connection",
    internal_title="Day 9 Controlled Instructional Vertical Slice",
    content_status="approved-day9-instructional-slice",
    practice_classification="instructional-practice-only",
    authorization_notice=(
        "Internal Day 9 instructional Practice only. Not complete Lesson 1, Evidence, "
        "Progress, Completion, pilot, public release, score, proficiency assessment, or R1A."
    ),
    authorized_for_pilot=False,
    authorized_for_public_release=False,
    estimated_minutes=8,
    current_step_count=5,
    session_closure=AprSessionClosureContent(
        content_id="APR-CNT-R1-RM01-L01-D9-CLS-001",
        badge="Resumen de esta sesión",
        heading="Tu práctica está lista para cerrar",
        body=(
            "Hoy practicaste una forma de abrir contacto en portugués y dejar espacio para una respuesta.\n\n"
            "Esto no genera una nota, una conclusión sobre tu nivel, Evidencia formal ni un registro de finalización.\n\n"
            "Tu grabación, el texto confirmado y la reflexión permanecen solamente durante esta sesión."
        ),
        primary_action="Cerrar esta práctica",
        secondary_action="Reiniciar",
    ),
    steps=[
        AprOrientationStep(
            step_id="orientation",
            step_type="orientation",
            title="Entrar en la conexión",
            body=(
                "Una conversación no empieza con una frase perfecta. Empieza cuando haces espacio para otra persona.\n\n"
                "En esta práctica vas a saludar, decir quién eres, compartir algo verdadero y terminar con una invitación breve: E você?\n\n"
                "Habla con suficiente claridad para que otra persona pueda seguirte. Tu acento no necesita desaparecer."
            ),
            required=True,
            content_ids=["APR-CNT-R1-RM01-L01-D9-ORI-001"],
        ),
        AprInformationStep(
            step_id="model-listening-bridge-notice",
            step_type="information",
            title="Escucha una apertura",
            body="Escucha para entender qué hace la frase. No intentes copiar cada sonido.",
            required=True,
            content_ids=[
                MODEL_AUDIO_ID,
                "APR-TXT-R1-RM01-L01-D9-TR-001",
                "APR-BRG-R1-RM01-L01-D9-001",
                "APR-PRN-R1-RM01-L01-D9-001",
                TEMPORARY_AUDIO_ID,
            ],
            model_script=MODEL_SCRIPT,
            controlled_transcript=MODEL_SCRIPT,
            transcript_label="Ver el texto",
            optional_translation="Hola. Soy Marina. Me gusta la música. ¿Y tú?",
            translation_label="Ver el significado en español",
            spanish_bridge=AprContentBlock(
                content_id="APR-BRG-R1-RM01-L01-D9-001",
                heading="Puente desde el español",
                body=(
                    "En español dices me gusta la música.\n\n"
                    "En portugués, el bloque más útil aquí es:\n\n"
                    "Gosto de música.\n\n"
                    "El significado es cercano, pero la estructura cambia. No traduzcas palabra por palabra. Recupera gosto de + algo verdadero y vuelve al portugués."
                ),
            ),
            pronunciation_guidance=AprContentBlock(
                content_id="APR-PRN-R1-RM01-L01-D9-001",
                heading="Una prioridad de claridad",
                body=(
                    "En você, la fuerza cae al final: vo-CÊ.\n\n"
                    "Busca que la pregunta llegue clara. No necesitas imitar un acento."
                ),
            ),
            pragmatic_guidance=AprContentBlock(
                content_id="APR-CNT-R1-RM01-L01-D9-PRG-001",
                heading="Haz espacio para la otra persona",
                body=(
                    "Oi es un inicio cotidiano y útil en muchas situaciones. Olá también es natural.\n\n"
                    "La calidez no exige sonar efusivo. Puedes hablar con tu propia personalidad y dejar espacio para la respuesta."
                ),
            ),
            model_audio=AprModelAudioConfig(
                model_audio_id=MODEL_AUDIO_ID,
                temporary_audio_id=TEMPORARY_AUDIO_ID,
                mode="on-demand",
                language="pt-BR",
                source="generated-temporary-testing",
                storage_status="session-only",
                authorized_as_final_content=False,
                required=False,
                disclosure="Audio temporal generado para pruebas. No es la grabación final de la Academia.",
            ),
        ),
        AprSingleChoiceStep(
            step_id="recognition-invitation",
            step_type="single_choice",
            title="Abre espacio para una respuesta",
            body="¿Qué hace Marina para convertir su presentación en una invitación a conversar?",
            required=True,
            content_ids=["APR-INT-R1-RM01-L01-D9-REC-001"],
            correct_option_id="invites-response",
            options=[
                AprSingleChoiceOption(
                    option_id="repeats-name",
                    label="Repite su nombre para que la otra persona lo memorice.",
                    feedback="Fíjate en el final. E você? transforma una presentación en una invitación a responder.",
                ),
                AprSingleChoiceOption(
                    option_id="invites-response",
                    label="Comparte algo verdadero y termina con E você?",
                    feedback="La frase no termina en Marina. E você? abre espacio para que la otra persona participe.",
                ),
                AprSingleChoiceOption(
                    option_id="explains-grammar",
                    label="Explica cómo funciona la gramática de gosto de.",
                    feedback="Fíjate en el final. E você? transforma una presentación en una invitación a responder.",
                ),
            ],
        ),
        AprRecordingStep(
            step_id="personal-practice",
            step_type="recording",
            title="Hazlo tuyo",
            body=(
                "Imagina que acabas de conocer a alguien en un contexto cotidiano.\n\n"
                "En portugués:\n\n"
                "1. saluda;\n2. di tu nombre;\n3. comparte algo verdadero y seguro que te gusta;\n4. termina con E você?\n\n"
                "Usa el modelo como apoyo, pero cambia el nombre y el detalle para que sean tuyos."
            ),
            required=True,
            content_ids=[
                "APR-PRM-R1-RM01-L01-D9-SPK-001",
                FEEDBACK_ID,
                "APR-PRM-R1-RM01-L01-D9-RTY-001",
                "APR-ALT-R1-RM01-L01-D9-WRT-001",
            ],
            prompt="Practica tu apertura en portugués cuando estés listo.",
            production_frame="Oi! Eu sou ________. Gosto de ________. E você?",
            privacy_notice="Elige un detalle verdadero que te resulte cómodo compartir. No necesitas dar información privada.",
            practice_notice="Esta grabación es práctica. No genera una nota, una evaluación de pronunciación ni una conclusión sobre tu nivel.",
            max_seconds=20,
            allow_retry=True,
            preserve_original=True,
            storage_status="session-only",
            transcription_language="pt",
            transcription_mode="on-demand",
            requires_learner_confirmation=True,
            transcript_storage_status="session-only",
            transcript_authorized_as_evidence=False,
            feedback_id=FEEDBACK_ID,
            feedback_mode="on-demand",
            feedback_source_attempt="original",
            feedback_requires_confirmed_transcript=True,
            feedback_source="server-deterministic",
            feedback_storage_status="session-only",
            feedback_authorized_as_academic_feedback=False,
            feedback_authorized_as_evidence=False,
            feedback_required=False,
            retry_orchestration_mode="optional-post-feedback-latest-retry",
            retry_required=False,
            retry_instruction=(
                "Intenta una vez más, si te resulta útil.\n\n"
                "Conserva tu nombre y tu detalle verdadero. Piensa en tres movimientos:\n\n"
                "entra → comparte → invita\n\n"
                "No necesitas sonar perfecto."
            ),
            written_alternative=AprWrittenAlternative(
                content_id="APR-ALT-R1-RM01-L01-D9-WRT-001",
                label="Practicar por escrito",
                notice=(
                    "Puedes practicar el mismo mensaje por escrito.\n\n"
                    "Esta ruta mantiene el propósito de construir una apertura personal, pero no permite interpretar habla, pronunciación ni inteligibilidad."
                ),
                prompt="Escribe tu apertura en portugués:",
                frame="Oi! Eu sou ________. Gosto de ________. E você?",
                storage_status="session-only",
                practice_classification="instructional-practice-only",
                max_characters=240,
            ),
        ),
        AprReflectionStep(
            step_id="reflection",
            step_type="reflection",
            title="Reflexiona",
            body="También puedes escribir:\n\nHoy me ayudó ________ porque ________.",
            required=False,
            content_ids=["APR-PRM-R1-RM01-L01-D9-REF-001"],
            prompt="¿Qué bloque te ayudó más a entrar en la interacción: Eu sou..., Gosto de... o E você??\n\nEscribe una frase breve sobre por qué.",
            placeholder="Hoy me ayudó ________ porque ________.",
            max_characters=240,
        ),
    ],
)

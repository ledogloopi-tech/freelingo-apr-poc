import { describe, expect, it, vi, beforeEach } from 'vitest'
import { fireEvent, render, screen } from '@testing-library/react'
import { AprLessonPlayer } from '@/components/apr/AprLessonPlayer'

const { mockApiFetch, mockPush } = vi.hoisted(() => ({
  mockApiFetch: vi.fn(),
  mockPush: vi.fn(),
}))

vi.mock('@/lib/api', () => ({ apiFetch: mockApiFetch }))
vi.mock('next/navigation', () => ({ useRouter: () => ({ push: mockPush }) }))
vi.mock('@/components/apr/AprAudioRecorder', () => ({
  AprAudioRecorder: ({
    hasOriginalAttempt,
    onCapture,
  }: {
    hasOriginalAttempt: boolean
    onCapture: (capture: {
      blob: Blob
      mimeType: string
      durationSeconds: number
    }) => void
  }) => (
    <button
      type="button"
      onClick={() =>
        onCapture({
          blob: new Blob([hasOriginalAttempt ? 'retry' : 'original'], {
            type: 'audio/webm',
          }),
          mimeType: 'audio/webm',
          durationSeconds: hasOriginalAttempt ? 2 : 1,
        })
      }
    >
      {hasOriginalAttempt ? 'Grabar otro intento' : 'Comenzar grabación'}
    </button>
  ),
}))

function jsonResponse(data: unknown, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}

const manifest = {
  lesson_id: 'APR-R1-RM-01-L01',
  module_id: 'APR-R1-RM-01',
  content_package_id: 'APR-R1-RM01-L01-D9',
  version: '1.0.0-day9-controlled-slice',
  title: 'Enter the Connection',
  internal_title: 'Day 9 Controlled Instructional Vertical Slice',
  content_status: 'approved-day9-instructional-slice',
  practice_classification: 'instructional-practice-only',
  authorization_notice: 'Internal Day 9 instructional Practice only.',
  authorized_for_pilot: false,
  authorized_for_public_release: false,
  estimated_minutes: 8,
  current_step_count: 5,
  session_closure: {
    content_id: 'APR-CNT-R1-RM01-L01-D9-CLS-001',
    badge: 'Resumen de esta sesión',
    heading: 'Tu práctica está lista para cerrar',
    body: 'Hoy practicaste una forma de abrir contacto en portugués y dejar espacio para una respuesta.\n\nEsto no genera una nota, una conclusión sobre tu nivel, Evidencia formal ni un registro de finalización.\n\nTu grabación, el texto confirmado y la reflexión permanecen solamente durante esta sesión.',
    primary_action: 'Cerrar esta práctica',
    secondary_action: 'Reiniciar',
  },
  steps: [
    {
      step_id: 'orientation',
      step_type: 'orientation',
      title: 'Entrar en la conexión',
      body: 'Una conversación no empieza con una frase perfecta. Empieza cuando haces espacio para otra persona.\n\nEn esta práctica vas a saludar, decir quién eres, compartir algo verdadero y terminar con una invitación breve: E você?\n\nHabla con suficiente claridad para que otra persona pueda seguirte. Tu acento no necesita desaparecer.',
      required: true,
      content_ids: ['APR-CNT-R1-RM01-L01-D9-ORI-001'],
    },
    {
      step_id: 'model',
      step_type: 'information',
      title: 'Escucha una apertura',
      body: 'Escucha para entender qué hace la frase. No intentes copiar cada sonido.',
      required: true,
      content_ids: ['APR-AUD-R1-RM01-L01-D9-MDL-001'],
      model_script: 'Oi! Eu sou a Marina. Gosto de música. E você?',
      controlled_transcript: 'Oi! Eu sou a Marina. Gosto de música. E você?',
      transcript_label: 'Ver el texto',
      optional_translation: 'Hola. Soy Marina. Me gusta la música. ¿Y tú?',
      translation_label: 'Ver el significado en español',
      spanish_bridge: {
        content_id: 'APR-BRG-R1-RM01-L01-D9-001',
        heading: 'Puente desde el español',
        body: 'En español dices me gusta la música.\n\nEn portugués, el bloque más útil aquí es:\n\nGosto de música.\n\nEl significado es cercano, pero la estructura cambia. No traduzcas palabra por palabra. Recupera gosto de + algo verdadero y vuelve al portugués.',
      },
      pronunciation_guidance: {
        content_id: 'APR-PRN-R1-RM01-L01-D9-001',
        heading: 'Una prioridad de claridad',
        body: 'En você, la fuerza cae al final: vo-CÊ.\n\nBusca que la pregunta llegue clara. No necesitas imitar un acento.',
      },
      pragmatic_guidance: {
        content_id: 'APR-CNT-R1-RM01-L01-D9-PRG-001',
        heading: 'Haz espacio para la otra persona',
        body: 'Oi es un inicio cotidiano y útil en muchas situaciones. Olá también es natural.\n\nLa calidez no exige sonar efusivo. Puedes hablar con tu propia personalidad y dejar espacio para la respuesta.',
      },
      model_audio: {
        model_audio_id: 'APR-AUD-R1-RM01-L01-D9-MDL-001',
        temporary_audio_id: 'APR-AUD-R1-RM01-L01-D9-TMP-001',
        mode: 'on-demand',
        language: 'pt-BR',
        source: 'generated-temporary-testing',
        storage_status: 'session-only',
        authorized_as_final_content: false,
        required: false,
        disclosure:
          'Audio temporal generado para pruebas. No es la grabación final de la Academia.',
      },
    },
    {
      step_id: 'recognition',
      step_type: 'single_choice',
      title: 'Abre espacio para una respuesta',
      body: '¿Qué hace Marina para convertir su presentación en una invitación a conversar?',
      required: true,
      content_ids: ['APR-INT-R1-RM01-L01-D9-REC-001'],
      correct_option_id: 'invites-response',
      prompt_label: 'Elige una respuesta.',
      required_warning: 'Selecciona una opción antes de continuar.',
      options: [
        {
          option_id: 'repeats-name',
          label: 'Repite su nombre para que la otra persona lo memorice.',
          feedback:
            'Fíjate en el final. E você? transforma una presentación en una invitación a responder.',
        },
        {
          option_id: 'invites-response',
          label: 'Comparte algo verdadero y termina con E você?',
          feedback:
            'La frase no termina en Marina. E você? abre espacio para que la otra persona participe.',
        },
      ],
    },
    {
      step_id: 'practice',
      step_type: 'recording',
      title: 'Hazlo tuyo',
      body: 'Imagina que acabas de conocer a alguien en un contexto cotidiano.\n\nEn portugués:\n\n1. saluda;\n2. di tu nombre;\n3. comparte algo verdadero y seguro que te gusta;\n4. termina con E você?\n\nUsa el modelo como apoyo, pero cambia el nombre y el detalle para que sean tuyos.',
      required: true,
      content_ids: ['APR-PRM-R1-RM01-L01-D9-SPK-001'],
      prompt: 'Practica tu apertura en portugués cuando estés listo.',
      production_frame: 'Oi! Eu sou ________. Gosto de ________. E você?',
      privacy_notice:
        'Elige un detalle verdadero que te resulte cómodo compartir. No necesitas dar información privada.',
      practice_notice:
        'Esta grabación es práctica. No genera una nota, una evaluación de pronunciación ni una conclusión sobre tu nivel.',
      max_seconds: 20,
      allow_retry: true,
      preserve_original: true,
      storage_status: 'session-only',
      transcription_language: 'pt',
      transcription_mode: 'on-demand',
      requires_learner_confirmation: true,
      transcript_storage_status: 'session-only',
      transcript_authorized_as_evidence: false,
      feedback_id: 'APR-FBK-R1-RM01-L01-D9-001',
      feedback_mode: 'on-demand',
      feedback_source_attempt: 'original',
      feedback_requires_confirmed_transcript: true,
      feedback_source: 'server-deterministic',
      feedback_storage_status: 'session-only',
      feedback_authorized_as_academic_feedback: false,
      feedback_authorized_as_evidence: false,
      feedback_required: false,
      retry_orchestration_mode: 'optional-post-feedback-latest-retry',
      retry_required: false,
      retry_instruction:
        'Intenta una vez más, si te resulta útil.\n\nConserva tu nombre y tu detalle verdadero. Piensa en tres movimientos:\n\nentra → comparte → invita\n\nNo necesitas sonar perfecto.',
      written_alternative: {
        content_id: 'APR-ALT-R1-RM01-L01-D9-WRT-001',
        label: 'Practicar por escrito',
        notice:
          'Puedes practicar el mismo mensaje por escrito.\n\nEsta ruta mantiene el propósito de construir una apertura personal, pero no permite interpretar habla, pronunciación ni inteligibilidad.',
        prompt: 'Escribe tu apertura en portugués:',
        frame: 'Oi! Eu sou ________. Gosto de ________. E você?',
        storage_status: 'session-only',
        practice_classification: 'instructional-practice-only',
        max_characters: 240,
      },
    },
    {
      step_id: 'reflection',
      step_type: 'reflection',
      title: 'Reflexiona',
      body: 'También puedes escribir:\n\nHoy me ayudó ________ porque ________.',
      required: false,
      content_ids: ['APR-PRM-R1-RM01-L01-D9-REF-001'],
      prompt:
        '¿Qué bloque te ayudó más a entrar en la interacción: Eu sou..., Gosto de... o E você??\n\nEscribe una frase breve sobre por qué.',
      placeholder: 'Hoy me ayudó ________ porque ________.',
      max_characters: 240,
    },
  ],
}

describe('APR Day 9 real lesson vertical slice', () => {
  beforeEach(() => {
    mockApiFetch.mockReset()
    mockPush.mockReset()
    let objectUrlCounter = 0
    vi.stubGlobal('URL', {
      createObjectURL: vi.fn(() => `blob:apr-${++objectUrlCounter}`),
      revokeObjectURL: vi.fn(),
    })
    vi.spyOn(window, 'confirm').mockReturnValue(false)
  })

  it('renders approved content, gates recognition and keeps feedback confirmed-transcript only', async () => {
    mockApiFetch.mockResolvedValueOnce(jsonResponse(manifest))
    render(
      <AprLessonPlayer endpoint="/api/apr/modules/primeira-conexao/lessons/enter-the-connection" />
    )
    await screen.findByText('Entrar en la conexión')
    expect(screen.queryByText(/Technical placeholder lesson/)).toBeNull()
    expect(screen.getByText(/Una conversación no empieza/)).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    expect(
      screen.getAllByText('Oi! Eu sou a Marina. Gosto de música. E você?')
        .length
    ).toBeGreaterThan(0)
    expect(screen.getByText('Puente desde el español')).toBeDefined()
    expect(screen.getByText('Una prioridad de claridad')).toBeDefined()
    expect(screen.getByText('Haz espacio para la otra persona')).toBeDefined()
    expect(
      screen.getAllByText(
        'Audio temporal generado para pruebas. No es la grabación final de la Academia.'
      ).length
    ).toBeGreaterThan(0)
    expect(
      screen.queryByLabelText('Reproducción del audio temporal')
    ).toBeNull()
    mockApiFetch.mockResolvedValueOnce(
      new Response('audio', {
        status: 200,
        headers: {
          'X-APR-Audio-Status': 'generated-temporary-testing',
          'X-APR-Audio-Language': 'pt-BR',
          'Content-Type': 'audio/mpeg',
        },
      })
    )
    fireEvent.click(
      screen.getByRole('button', { name: 'Escuchar audio temporal' })
    )
    await screen.findByLabelText('Reproducción del audio temporal')
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    expect(
      screen.getByText('Selecciona una opción antes de continuar.')
    ).toBeDefined()
    fireEvent.click(
      screen.getByLabelText('Comparte algo verdadero y termina con E você?')
    )
    expect(screen.getByText(/La frase no termina en Marina/)).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    expect(
      screen.getByText('Oi! Eu sou ________. Gosto de ________. E você?')
    ).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Comenzar grabación' }))
    expect(screen.getByText('Original protegido')).toBeDefined()
    fireEvent.click(
      screen.getByRole('button', { name: 'Usar lista de auto-revisión' })
    )
    expect(mockApiFetch).toHaveBeenCalledTimes(2)
    expect(
      screen.getByText(/No podemos verificar con seguridad qué dijiste/)
    ).toBeDefined()
    mockApiFetch.mockResolvedValueOnce(
      jsonResponse({ draft_text: 'Oi eu sou Ana gosto de café e você' })
    )
    fireEvent.click(
      screen.getByRole('button', { name: 'Solicitar transcripción' })
    )
    await screen.findByText('Borrador generado por máquina')
    const textarea = screen.getByLabelText('Texto revisado')
    fireEvent.change(textarea, {
      target: { value: 'Oi! Eu sou Ana. Gosto de café. E você?' },
    })
    fireEvent.click(
      screen.getByRole('button', { name: 'Confirmar este texto' })
    )
    mockApiFetch.mockResolvedValueOnce(
      jsonResponse({
        feedback_id: 'APR-FBK-R1-RM01-L01-D9-001',
        feedback_case: 'all-components',
        attempt_role: 'original',
        source_confirmation_revision: 1,
        status: 'controlled-instructional-guidance',
        source: 'server-deterministic',
        acknowledgement:
          'En el texto que confirmaste aparecen las cuatro funciones: saludo, presentación, detalle personal e invitación.',
        primary_priority:
          'En el texto que confirmaste aparecen las cuatro funciones: saludo, presentación, detalle personal e invitación.',
        cue: 'saludo, nombre, Gosto de..., E você?',
        retry_instruction: 'Intenta una vez más, si te resulta útil.',
        uncertainty: 'No es Evidencia.',
        requires_retry: false,
        retry_allowed: true,
        authorized_as_academic_feedback: false,
        authorized_as_evidence: false,
        storage_status: 'session-only',
      })
    )
    fireEvent.click(
      screen.getByRole('button', { name: 'Pedir ayuda controlada' })
    )
    await screen.findByText('Guía controlada')
    expect(
      JSON.parse(mockApiFetch.mock.calls.at(-1)?.[1]?.body as string)
        .confirmed_transcript
    ).toBe('Oi! Eu sou Ana. Gosto de café. E você?')
    fireEvent.click(screen.getByRole('button', { name: 'Grabar otro intento' }))
    expect(screen.getByText('Latest retry separado')).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    fireEvent.change(screen.getByLabelText(/¿Qué bloque te ayudó/), {
      target: { value: 'Hoy me ayudó E você? porque invita.' },
    })
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    expect(screen.getByText('Tu práctica está lista para cerrar')).toBeDefined()
    expect(screen.getByText(/Esto no genera una nota/)).toBeDefined()
    fireEvent.click(
      screen.getByRole('button', { name: 'Cerrar esta práctica' })
    )
    expect(mockPush).toHaveBeenCalledWith('/apr/primeira-conexao')
  })

  it('allows written Practice to satisfy Step 4 without calling feedback, progress, completion, or evidence APIs', async () => {
    mockApiFetch.mockResolvedValueOnce(jsonResponse(manifest))
    render(
      <AprLessonPlayer endpoint="/api/apr/modules/primeira-conexao/lessons/enter-the-connection" />
    )
    await screen.findByText('Entrar en la conexión')
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    fireEvent.click(
      screen.getByLabelText(
        'Repite su nombre para que la otra persona lo memorice.'
      )
    )
    expect(screen.getByText(/Fíjate en el final/)).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    expect(
      screen.getByText(
        'Graba un Original o completa la práctica escrita antes de continuar.'
      )
    ).toBeDefined()
    fireEvent.click(
      screen.getByRole('button', { name: 'Practicar por escrito' })
    )
    const written = screen.getByLabelText('Escribe tu apertura en portugués:')
    fireEvent.change(written, {
      target: { value: 'Oi! Eu sou Lia. Gosto de livros. E você?' },
    })
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    expect(screen.getByText('Reflexiona')).toBeDefined()
    const requestedUrls = mockApiFetch.mock.calls.map((call) => call[0])
    expect(
      requestedUrls.some((url) => String(url).includes('feedback-drafts'))
    ).toBe(false)
    expect(
      requestedUrls.some((url) =>
        /completion|progress|evidence/i.test(String(url))
      )
    ).toBe(false)
  })
})

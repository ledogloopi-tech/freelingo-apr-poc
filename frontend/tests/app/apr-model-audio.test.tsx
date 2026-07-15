import { fireEvent, render, screen, waitFor } from '@testing-library/react'
import { StrictMode } from 'react'
import { beforeEach, describe, expect, it, vi } from 'vitest'

const { mockApiFetch } = vi.hoisted(() => ({ mockApiFetch: vi.fn() }))

vi.mock('@/lib/api', () => ({ apiFetch: mockApiFetch }))

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
          durationSeconds: 1,
        })
      }
    >
      {hasOriginalAttempt ? 'Record another attempt' : 'Start recording'}
    </button>
  ),
}))

import AprEnterTheConnectionLessonPage from '@/app/(apr)/apr/primeira-conexao/lessons/enter-the-connection/page'

const endpoint =
  '/api/apr/modules/primeira-conexao/lessons/enter-the-connection'
const modelAudioEndpoint = `${endpoint}/model-audio`
const modelAudioId = 'APR-R1-RM-01-L01-MODEL-TECH'

function jsonResponse(data: unknown) {
  return new Response(JSON.stringify(data), {
    status: 200,
    headers: { 'Content-Type': 'application/json' },
  })
}

function audioResponse(bytes = 'mp3') {
  return new Response(bytes, {
    status: 200,
    headers: {
      'Content-Type': 'audio/mpeg',
      'X-APR-Audio-Language': 'pt-BR',
      'X-APR-Audio-Status': 'generated-technical-placeholder',
    },
  })
}

const manifest = {
  lesson_id: 'APR-R1-RM-01-L01-TECH',
  module_id: 'APR-R1-RM-01',
  version: '0.4.0-technical-placeholder',
  title: 'Enter the Connection',
  internal_title: 'Lesson Player Technical Demonstration',
  content_status: 'technical-placeholder',
  authorized_for_pilot: false,
  authorized_for_public_release: false,
  estimated_minutes: 5,
  current_step_count: 5,
  steps: [
    {
      step_id: 'orientation',
      step_type: 'orientation',
      title: 'Orientation',
      body: 'Placeholder.',
      required: true,
    },
    {
      step_id: 'information',
      step_type: 'information',
      title: 'Information',
      body: 'Placeholder.',
      required: true,
    },
    {
      step_id: 'interface-choice',
      step_type: 'single_choice',
      title: 'Single-choice interaction',
      body: 'Choose.',
      required: true,
      options: [
        {
          option_id: 'a',
          label: 'The layout is clear enough to continue testing.',
          feedback: 'Fixed technical feedback.',
        },
      ],
    },
    {
      step_id: 'microphone-capture',
      step_type: 'recording',
      title: 'Microphone capture',
      body: 'Record.',
      required: true,
      prompt: 'Prompt.',
      max_seconds: 10,
      allow_retry: true,
      preserve_original: true,
      storage_status: 'session-only',
      transcription_language: 'pt',
      transcription_mode: 'on-demand',
      requires_learner_confirmation: true,
      transcript_storage_status: 'session-only',
      transcript_authorized_as_evidence: false,
      model_audio_id: modelAudioId,
      model_audio_mode: 'on-demand',
      model_audio_language: 'pt-BR',
      model_audio_source: 'generated-technical-placeholder',
      model_audio_storage_status: 'session-only',
      model_audio_authorized_as_final_content: false,
      model_audio_required: false,
    },
    {
      step_id: 'technical-reflection',
      step_type: 'reflection',
      title: 'Reflection',
      body: 'Reflect.',
      required: false,
      prompt: 'Prompt?',
      max_characters: 20,
    },
  ],
}

async function renderRecordingStep({ strict = false } = {}) {
  mockApiFetch.mockResolvedValueOnce(jsonResponse(manifest))
  if (strict) mockApiFetch.mockResolvedValueOnce(jsonResponse(manifest))
  const result = render(
    strict ? (
      <StrictMode>
        <AprEnterTheConnectionLessonPage />
      </StrictMode>
    ) : (
      <AprEnterTheConnectionLessonPage />
    )
  )
  await screen.findByText('Step 1 of 5.')
  fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
  fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
  fireEvent.click(screen.getByRole('radio'))
  fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
  await screen.findByText('Step 4 of 5.')
  return result
}

async function navigateFromStartToRecordingStep() {
  await screen.findByText('Step 1 of 5.')
  fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
  fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
  fireEvent.click(screen.getByRole('radio'))
  fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
  await screen.findByText('Step 4 of 5.')
}

describe('APR model audio', () => {
  beforeEach(() => {
    mockApiFetch.mockReset()
    vi.stubGlobal('URL', {
      createObjectURL: vi.fn(
        (blob: Blob) => `blob:${blob.size}:${Math.random()}`
      ),
      revokeObjectURL: vi.fn(),
    })
    vi.spyOn(window, 'confirm').mockReturnValue(true)
  })

  it('does not request model audio on render, recording, or transcript success', async () => {
    await renderRecordingStep()
    expect(mockApiFetch).toHaveBeenCalledTimes(1)
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    expect(mockApiFetch).toHaveBeenCalledTimes(1)
    mockApiFetch.mockResolvedValueOnce(jsonResponse({ draft_text: 'rascunho' }))
    fireEvent.click(
      await screen.findByRole('button', { name: 'Generate transcript draft' })
    )
    await waitFor(() => expect(mockApiFetch).toHaveBeenCalledTimes(2))
    expect(mockApiFetch.mock.calls.map((call) => call[0])).not.toContain(
      modelAudioEndpoint
    )
  })

  it('requests only the APR endpoint after explicit activation and creates playback without autoplay', async () => {
    await renderRecordingStep()
    mockApiFetch.mockResolvedValueOnce(audioResponse('abc'))
    fireEvent.click(
      screen.getByRole('button', { name: 'Generate technical model audio' })
    )
    expect(screen.getByText(/Generating technical model audio/)).toBeDefined()
    await screen.findByLabelText('Generated technical model audio playback')
    expect(mockApiFetch).toHaveBeenLastCalledWith(
      modelAudioEndpoint,
      expect.objectContaining({ method: 'POST' })
    )
    const body = JSON.parse(mockApiFetch.mock.lastCall?.[1].body as string)
    expect(body).toEqual({ model_audio_id: modelAudioId })
    expect(Object.keys(body)).toEqual(['model_audio_id'])
    expect(mockApiFetch.mock.calls.some((call) => call[0] === '/api/tts')).toBe(
      false
    )
    expect(URL.createObjectURL).toHaveBeenCalled()
    expect(screen.getByText('Actual MIME type: audio/mpeg')).toBeDefined()
    expect(screen.getByText('Intended language: pt-BR')).toBeDefined()
    expect(screen.getAllByText(/provider-dependent/).length).toBeGreaterThan(0)
    expect(
      screen.getByLabelText('Generated technical model audio playback')
    ).not.toHaveAttribute('autoplay')
    expect(
      screen.queryByText(/grade|CEFR|fluency|XP|streak|pronunciation result/i)
    ).toBeNull()
  })

  it('displays Unknown for a response blob without usable MIME type', async () => {
    await renderRecordingStep()
    mockApiFetch.mockResolvedValueOnce(
      new Response(new Uint8Array([1, 2, 3]).buffer)
    )
    fireEvent.click(
      screen.getByRole('button', { name: 'Generate technical model audio' })
    )
    await screen.findByLabelText('Generated technical model audio playback')
    expect(screen.getByText('Actual MIME type: Unknown')).toBeDefined()
  })

  it('blocks duplicate pending requests and uses technical failure language without blocking Continue', async () => {
    await renderRecordingStep()
    let resolveAudio: (res: Response) => void = () => {}
    mockApiFetch.mockReturnValueOnce(
      new Promise((resolve) => {
        resolveAudio = resolve
      })
    )
    const button = screen.getByRole('button', {
      name: 'Generate technical model audio',
    })
    fireEvent.click(button)
    fireEvent.click(button)
    expect(mockApiFetch).toHaveBeenCalledTimes(2)
    resolveAudio(new Response('fail', { status: 503 }))
    expect(
      await screen.findByText(/technical audio issue, not a language result/i)
    ).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    expect(screen.getByText('Step 5 of 5.')).toBeDefined()
  })

  it('preserves model audio across navigation, clears on confirmed restart, and preserves on cancelled restart', async () => {
    await renderRecordingStep()
    mockApiFetch.mockResolvedValueOnce(audioResponse('abc'))
    fireEvent.click(
      screen.getByRole('button', { name: 'Generate technical model audio' })
    )
    await screen.findByLabelText('Generated technical model audio playback')
    fireEvent.click(screen.getByRole('button', { name: 'Back' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    expect(
      screen.getByLabelText('Generated technical model audio playback')
    ).toBeDefined()
    vi.mocked(window.confirm).mockReturnValueOnce(false)
    fireEvent.click(screen.getByRole('button', { name: 'Restart' }))
    expect(
      screen.getByLabelText('Generated technical model audio playback')
    ).toBeDefined()
    vi.mocked(window.confirm).mockReturnValueOnce(true)
    fireEvent.click(screen.getByRole('button', { name: 'Restart' }))
    expect(URL.revokeObjectURL).toHaveBeenCalled()
    expect(
      screen.queryByLabelText('Generated technical model audio playback')
    ).toBeNull()
  })

  it('revokes replaced and unmounted model-audio URLs only', async () => {
    const view = await renderRecordingStep()
    mockApiFetch.mockResolvedValueOnce(audioResponse('abc'))
    fireEvent.click(
      screen.getByRole('button', { name: 'Generate technical model audio' })
    )
    await screen.findByLabelText('Generated technical model audio playback')
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    mockApiFetch.mockResolvedValueOnce(audioResponse('def'))
    fireEvent.click(
      screen.getByRole('button', {
        name: 'Generate new technical audio',
      })
    )
    await waitFor(() => expect(URL.revokeObjectURL).toHaveBeenCalledTimes(1))
    view.unmount()
    expect(URL.revokeObjectURL).toHaveBeenCalledTimes(3)
  })

  it('ignores stale responses after restart and allows Strict Mode requests', async () => {
    await renderRecordingStep({ strict: true })
    let resolveAudio: (res: Response) => void = () => {}
    mockApiFetch.mockReturnValueOnce(
      new Promise((resolve) => {
        resolveAudio = resolve
      })
    )
    fireEvent.click(
      screen.getByRole('button', { name: 'Generate technical model audio' })
    )
    fireEvent.click(screen.getByRole('button', { name: 'Restart' }))
    resolveAudio(audioResponse('stale'))
    await waitFor(() =>
      expect(
        screen.queryByLabelText('Generated technical model audio playback')
      ).toBeNull()
    )
    expect(URL.createObjectURL).not.toHaveBeenCalled()
  })

  it('prevents an older response from overwriting a newer clip', async () => {
    await renderRecordingStep()
    let resolveOlder: (res: Response) => void = () => {}
    let resolveNewer: (res: Response) => void = () => {}
    mockApiFetch.mockReturnValueOnce(
      new Promise((resolve) => {
        resolveOlder = resolve
      })
    )
    fireEvent.click(
      screen.getByRole('button', { name: 'Generate technical model audio' })
    )
    fireEvent.click(screen.getByRole('button', { name: 'Restart' }))
    await navigateFromStartToRecordingStep()
    mockApiFetch.mockReturnValueOnce(
      new Promise((resolve) => {
        resolveNewer = resolve
      })
    )
    fireEvent.click(
      screen.getByRole('button', { name: 'Generate technical model audio' })
    )
    resolveNewer(audioResponse('newer'))
    await screen.findByLabelText('Generated technical model audio playback')
    resolveOlder(audioResponse('older'))
    await waitFor(() => expect(URL.createObjectURL).toHaveBeenCalledTimes(1))
  })
})

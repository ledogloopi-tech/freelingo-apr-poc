import { StrictMode } from 'react'
import { fireEvent, render, screen, waitFor } from '@testing-library/react'
import { beforeEach, describe, expect, it, vi } from 'vitest'

const { mockApiFetch, recorderConfig } = vi.hoisted(() => ({
  mockApiFetch: vi.fn(),
  recorderConfig: { nextMimeType: 'audio/webm' },
}))

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
      onClick={() => {
        const text = hasOriginalAttempt ? 'retry' : 'original'
        const mimeType = recorderConfig.nextMimeType
        const blob = mimeType
          ? new Blob([text], { type: mimeType })
          : new Blob([text])
        onCapture({
          blob,
          mimeType: mimeType || 'unknown',
          durationSeconds: hasOriginalAttempt ? 2 : 1,
        })
      }}
    >
      {hasOriginalAttempt ? 'Record another attempt' : 'Start recording'}
    </button>
  ),
}))

import { AprLessonPlayer } from '@/components/apr/AprLessonPlayer'

const endpoint =
  '/api/apr/modules/primeira-conexao/lessons/enter-the-connection'
const forbiddenEndpointPattern =
  /\/api\/(stt|tts|conversation|conversations|assessment|progress|billing|llm)/

function deferredResponse() {
  let resolve!: (value: Response) => void
  const promise = new Promise<Response>((res) => {
    resolve = res
  })
  return { promise, resolve }
}

function jsonResponse(data: unknown, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
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
      body: 'Technical placeholder lesson.',
      required: true,
    },
    {
      step_id: 'information',
      step_type: 'information',
      title: 'Information',
      body: 'Info.',
      required: true,
    },
    {
      step_id: 'interface-choice',
      step_type: 'single_choice',
      title: 'Single-choice interaction',
      body: 'Choice.',
      required: true,
      options: [{ option_id: 'ok', label: 'OK', feedback: 'Fixed feedback.' }],
    },
    {
      step_id: 'microphone-capture',
      step_type: 'recording',
      title: 'Microphone capture',
      body: 'Record. This does not assess Portuguese capability.',
      required: true,
      prompt: 'Session-only until transcription is requested.',
      max_seconds: 10,
      allow_retry: true,
      preserve_original: true,
      storage_status: 'session-only',
      transcription_language: 'pt',
      transcription_mode: 'on-demand',
      requires_learner_confirmation: true,
      transcript_storage_status: 'session-only',
      transcript_authorized_as_evidence: false,
      model_audio_id: 'APR-R1-RM-01-L01-MODEL-TECH',
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
      prompt: 'Note?',
      max_characters: 50,
    },
  ],
}

async function renderAtRecordingStep(options: { strict?: boolean } = {}) {
  mockApiFetch.mockResolvedValueOnce(jsonResponse(manifest))
  if (options.strict) mockApiFetch.mockResolvedValueOnce(jsonResponse(manifest))
  const ui = <AprLessonPlayer endpoint={endpoint} />
  const result = render(options.strict ? <StrictMode>{ui}</StrictMode> : ui)
  await screen.findByText('Orientation')
  fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
  fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
  fireEvent.click(screen.getByLabelText('OK'))
  fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
  return result
}

function captureOriginal() {
  fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
}

function captureRetry(mimeType = 'audio/webm') {
  recorderConfig.nextMimeType = mimeType
  fireEvent.click(
    screen.getByRole('button', { name: 'Record another attempt' })
  )
}

function generateButtons() {
  return screen.getAllByRole('button', { name: /Generate.*transcript draft/ })
}

function generateOriginal() {
  fireEvent.click(generateButtons()[0])
}

function generateRetry() {
  fireEvent.click(generateButtons()[1])
}

function latestRequest() {
  return mockApiFetch.mock.calls.at(-1) as [string, RequestInit]
}

function requestForm(callIndex = mockApiFetch.mock.calls.length - 1) {
  return mockApiFetch.mock.calls[callIndex][1].body as FormData
}

function expectNoForbiddenCalls() {
  const urls = mockApiFetch.mock.calls.map(([url]) => String(url))
  expect(urls.every((url) => !forbiddenEndpointPattern.test(url))).toBe(true)
}

describe('APR transcript confirmation', () => {
  beforeEach(() => {
    mockApiFetch.mockReset()
    recorderConfig.nextMimeType = 'audio/webm'
    vi.stubGlobal('URL', {
      createObjectURL: vi.fn(() => `blob:apr-${Math.random()}`),
      revokeObjectURL: vi.fn(),
    })
  })

  it('does not request transcription on render or capture, then uses only the APR endpoint after explicit action', async () => {
    await renderAtRecordingStep()
    expect(mockApiFetch).toHaveBeenCalledTimes(1)
    captureOriginal()
    expect(mockApiFetch).toHaveBeenCalledTimes(1)

    mockApiFetch.mockResolvedValueOnce(jsonResponse({ draft_text: 'máquina' }))
    generateOriginal()

    const [url, options] = latestRequest()
    expect(url).toBe(`${endpoint}/transcription-drafts`)
    expect(url).not.toBe('/api/stt')
    expect(options.headers).toBeUndefined()
    expectNoForbiddenCalls()
    await screen.findByText('Machine-generated transcript draft')
  })

  it('sends original FormData with the selected Blob and known MIME filename', async () => {
    await renderAtRecordingStep()
    captureOriginal()
    mockApiFetch.mockResolvedValueOnce(
      jsonResponse({ draft_text: 'original draft' })
    )
    generateOriginal()

    const formData = requestForm()
    const audio = formData.get('audio') as File
    expect(formData.get('attempt_role')).toBe('original')
    expect(audio).toBeInstanceOf(File)
    expect(audio.name).toBe('apr-recording.webm')
    expect(audio.type).toBe('audio/webm')
    expect(await audio.text()).toBe('original')
  })

  it('uses latest_retry role and .bin filename for unknown browser audio', async () => {
    await renderAtRecordingStep()
    captureOriginal()
    captureRetry('')
    mockApiFetch.mockResolvedValueOnce(
      jsonResponse({ draft_text: 'retry draft' })
    )
    generateRetry()

    const formData = requestForm()
    const audio = formData.get('audio') as File
    expect(formData.get('attempt_role')).toBe('latest_retry')
    expect(audio.name).toBe('apr-recording.bin')
    expect(audio.type).toBe('')
    expect(await audio.text()).toBe('retry')
  })

  it('announces processing and blocks rapid duplicate requests synchronously', async () => {
    const pending = deferredResponse()
    await renderAtRecordingStep()
    captureOriginal()
    mockApiFetch.mockReturnValueOnce(pending.promise)

    generateOriginal()
    generateOriginal()
    generateOriginal()

    expect(mockApiFetch).toHaveBeenCalledTimes(2)
    expect(
      screen.getByText(/Generating transcript draft for Original attempt/)
    ).toBeInTheDocument()
    pending.resolve(jsonResponse({ draft_text: 'one request' }))
    await screen.findByDisplayValue('one request')
  })

  it('preserves machine draft separately, blocks empty confirmation, and allows reconfirmation', async () => {
    await renderAtRecordingStep()
    captureOriginal()
    mockApiFetch.mockResolvedValueOnce(
      jsonResponse({ draft_text: 'rascunho da máquina' })
    )
    generateOriginal()
    await screen.findByText('Machine-generated transcript draft')

    const textarea = screen.getByLabelText('Reviewed transcript correction')
    expect(textarea).toHaveValue('rascunho da máquina')
    fireEvent.change(textarea, { target: { value: '   ' } })
    fireEvent.click(
      screen.getByRole('button', { name: 'Confirm reviewed transcript' })
    )
    expect(
      screen.getByText('Enter a reviewed transcript before confirming.')
    ).toBeInTheDocument()

    fireEvent.change(textarea, { target: { value: 'fala revisada' } })
    expect(screen.getAllByText('rascunho da máquina').length).toBeGreaterThan(0)
    fireEvent.click(
      screen.getByRole('button', { name: 'Confirm reviewed transcript' })
    )
    expect(screen.getByText('Learner-confirmed transcript')).toBeInTheDocument()
    expect(screen.getAllByText('fala revisada').length).toBeGreaterThan(0)

    fireEvent.change(textarea, { target: { value: 'fala reconfirmada' } })
    fireEvent.click(
      screen.getByRole('button', { name: 'Confirm reviewed transcript' })
    )
    expect(screen.getAllByText('fala reconfirmada').length).toBeGreaterThan(0)
    expect(screen.queryByText('fala revisada')).not.toBeInTheDocument()
  })

  it('clears stale confirmation when a new draft succeeds and disables editing while pending', async () => {
    const pending = deferredResponse()
    await renderAtRecordingStep()
    captureOriginal()
    mockApiFetch.mockResolvedValueOnce(
      jsonResponse({ draft_text: 'draft one' })
    )
    generateOriginal()
    await screen.findByDisplayValue('draft one')
    const textarea = screen.getByLabelText('Reviewed transcript correction')
    fireEvent.change(textarea, { target: { value: 'confirmed one' } })
    fireEvent.click(
      screen.getByRole('button', { name: 'Confirm reviewed transcript' })
    )
    expect(screen.getAllByText('confirmed one').length).toBeGreaterThan(0)

    mockApiFetch.mockReturnValueOnce(pending.promise)
    fireEvent.click(
      screen.getByRole('button', { name: 'Generate a new transcript draft' })
    )
    expect(textarea).toBeDisabled()
    expect(
      screen.getByRole('button', { name: 'Confirm reviewed transcript' })
    ).toBeDisabled()
    pending.resolve(jsonResponse({ draft_text: 'draft two' }))

    await screen.findByDisplayValue('draft two')
    expect(screen.queryByText('confirmed one')).not.toBeInTheDocument()
    expect(
      screen.getByLabelText('Original attempt playback')
    ).toBeInTheDocument()
  })

  it('keeps original and retry transcript states separate and retry replacement clears only retry state', async () => {
    await renderAtRecordingStep()
    captureOriginal()
    captureRetry('audio/mp4')
    mockApiFetch
      .mockResolvedValueOnce(jsonResponse({ draft_text: 'original draft' }))
      .mockResolvedValueOnce(jsonResponse({ draft_text: 'retry draft' }))
    generateOriginal()
    await screen.findByDisplayValue('original draft')
    generateRetry()
    await screen.findByDisplayValue('retry draft')

    captureRetry('audio/wav')

    expect(screen.getAllByText('original draft').length).toBeGreaterThan(0)
    expect(screen.queryByText('retry draft')).not.toBeInTheDocument()
    expect(
      screen.getByLabelText('Original attempt playback')
    ).toBeInTheDocument()
    expect(screen.getByLabelText('Latest retry playback')).toBeInTheDocument()
  })

  it('preserves transcripts through Back/Continue and cancelled Restart, then clears them on confirmed Restart', async () => {
    await renderAtRecordingStep()
    captureOriginal()
    mockApiFetch.mockResolvedValueOnce(jsonResponse({ draft_text: 'keep me' }))
    generateOriginal()
    await screen.findByDisplayValue('keep me')

    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    await screen.findByText('Reflection')
    fireEvent.click(screen.getByRole('button', { name: 'Back' }))
    expect(screen.getAllByText('keep me').length).toBeGreaterThan(0)

    vi.spyOn(window, 'confirm').mockReturnValueOnce(false)
    fireEvent.click(screen.getByRole('button', { name: 'Restart' }))
    expect(screen.getAllByText('keep me').length).toBeGreaterThan(0)

    vi.spyOn(window, 'confirm').mockReturnValueOnce(true)
    fireEvent.click(screen.getByRole('button', { name: 'Restart' }))
    expect(screen.queryByText('keep me')).not.toBeInTheDocument()
    expect(screen.getByText('Orientation')).toBeInTheDocument()
  })

  it('ignores stale retry responses after retry replacement', async () => {
    const stale = deferredResponse()
    await renderAtRecordingStep()
    captureOriginal()
    captureRetry('audio/webm')
    mockApiFetch.mockReturnValueOnce(stale.promise)
    generateRetry()
    captureRetry('audio/webm')
    stale.resolve(jsonResponse({ draft_text: 'stale retry' }))
    await waitFor(() =>
      expect(screen.queryByText('stale retry')).not.toBeInTheDocument()
    )
  })

  it('ignores stale responses after Restart and unmount', async () => {
    const afterRestart = deferredResponse()
    const firstRender = await renderAtRecordingStep()
    captureOriginal()
    mockApiFetch.mockReturnValueOnce(afterRestart.promise)
    generateOriginal()
    vi.spyOn(window, 'confirm').mockReturnValueOnce(true)
    fireEvent.click(screen.getByRole('button', { name: 'Restart' }))
    afterRestart.resolve(jsonResponse({ draft_text: 'after restart' }))
    await waitFor(() =>
      expect(screen.queryByText('after restart')).not.toBeInTheDocument()
    )
    firstRender.unmount()

    const afterUnmount = deferredResponse()
    const { unmount } = await renderAtRecordingStep()
    captureOriginal()
    mockApiFetch.mockReturnValueOnce(afterUnmount.promise)
    generateOriginal()
    unmount()
    afterUnmount.resolve(jsonResponse({ draft_text: 'after unmount' }))
    await waitFor(() =>
      expect(screen.queryByText('after unmount')).not.toBeInTheDocument()
    )
  })

  it('keeps React StrictMode mounted state valid for an explicit transcript response', async () => {
    await renderAtRecordingStep({ strict: true })
    captureOriginal()
    mockApiFetch.mockResolvedValueOnce(
      jsonResponse({ draft_text: 'strict draft' })
    )
    generateOriginal()
    await screen.findByDisplayValue('strict draft')
  })

  it('preserves audio and allows Continue when transcription fails without requiring success or confirmation', async () => {
    await renderAtRecordingStep()
    captureOriginal()
    mockApiFetch.mockResolvedValueOnce(new Response('{}', { status: 502 }))
    generateOriginal()
    await screen.findByText(
      'APR could not generate a transcript draft. This is a technical transcription issue, not a language result.'
    )
    expect(
      screen.getByLabelText('Original attempt playback')
    ).toBeInTheDocument()
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    await waitFor(() =>
      expect(screen.getByText('Reflection')).toBeInTheDocument()
    )
  })

  it('requires only original audio for Continue and keeps completion non-academic', async () => {
    await renderAtRecordingStep()
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    expect(
      screen.getByText(
        'Create one technical microphone recording before continuing.'
      )
    ).toBeInTheDocument()
    captureOriginal()
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    await screen.findByText('Reflection')
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    expect(
      screen.getAllByText('Session-only technical summary')[0]
    ).toBeInTheDocument()
    expect(
      screen.getByText(
        'You reached the end of this technical prototype. This summary describes browser-session activity only. It is not lesson completion, Progress, Evidence, a score, or a language result.'
      )
    ).toBeInTheDocument()
    expect(
      screen.queryByText(/CEFR|fluency|grade|XP|streak|pronunciation result/i)
    ).not.toBeInTheDocument()
    expectNoForbiddenCalls()
  })
})

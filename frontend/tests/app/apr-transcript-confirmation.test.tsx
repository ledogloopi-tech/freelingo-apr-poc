import { fireEvent, render, screen, waitFor } from '@testing-library/react'
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

import { AprLessonPlayer } from '@/components/apr/AprLessonPlayer'

const endpoint =
  '/api/apr/modules/primeira-conexao/lessons/enter-the-connection'
function jsonResponse(data: unknown, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}
const manifest = {
  lesson_id: 'APR-R1-RM-01-L01-TECH',
  module_id: 'APR-R1-RM-01',
  version: '0.3.0-technical-placeholder',
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

async function renderAtRecordingStep() {
  mockApiFetch.mockResolvedValueOnce(jsonResponse(manifest))
  render(<AprLessonPlayer endpoint={endpoint} />)
  await screen.findByText('Orientation')
  fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
  fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
  fireEvent.click(screen.getByLabelText('OK'))
  fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
}

describe('APR transcript confirmation', () => {
  beforeEach(() => {
    mockApiFetch.mockReset()
    vi.stubGlobal('URL', {
      createObjectURL: vi.fn(() => 'blob:apr'),
      revokeObjectURL: vi.fn(),
    })
  })

  it('requests a draft only after learner action and uses the APR endpoint', async () => {
    await renderAtRecordingStep()
    expect(mockApiFetch).toHaveBeenCalledTimes(1)
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    expect(mockApiFetch).toHaveBeenCalledTimes(1)
    mockApiFetch.mockResolvedValueOnce(jsonResponse({ draft_text: 'máquina' }))
    fireEvent.click(
      screen.getByRole('button', { name: 'Generate transcript draft' })
    )
    expect(mockApiFetch.mock.calls[1][0]).toBe(
      `${endpoint}/transcription-drafts`
    )
    expect(mockApiFetch.mock.calls[1][0]).not.toBe('/api/stt')
    const options = mockApiFetch.mock.calls[1][1]
    expect(options.body).toBeInstanceOf(FormData)
    await screen.findByText('Machine-generated transcript draft')
    expect(screen.getByDisplayValue('máquina')).toBeInTheDocument()
  })

  it('preserves machine draft separately from learner confirmation and avoids scoring language', async () => {
    await renderAtRecordingStep()
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    mockApiFetch.mockResolvedValueOnce(
      jsonResponse({ draft_text: 'rascunho da máquina' })
    )
    fireEvent.click(
      screen.getByRole('button', { name: 'Generate transcript draft' })
    )
    await screen.findByText('Machine-generated transcript draft')
    const textarea = screen.getByLabelText('Reviewed transcript correction')
    fireEvent.change(textarea, { target: { value: 'fala revisada' } })
    expect(screen.getAllByText('rascunho da máquina').length).toBeGreaterThan(0)
    fireEvent.click(
      screen.getByRole('button', { name: 'Confirm reviewed transcript' })
    )
    expect(screen.getByText('Learner-confirmed transcript')).toBeInTheDocument()
    expect(screen.getAllByText('fala revisada').length).toBeGreaterThan(0)
    expect(
      screen.queryByText(/grade|CEFR|fluency|pronunciation result/i)
    ).not.toBeInTheDocument()
  })

  it('keeps technical failure non-judgmental and continue remains gated only by original audio', async () => {
    await renderAtRecordingStep()
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    mockApiFetch.mockResolvedValueOnce(new Response('{}', { status: 502 }))
    fireEvent.click(
      screen.getByRole('button', { name: 'Generate transcript draft' })
    )
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
})

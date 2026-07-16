import { cleanup, fireEvent, render, screen } from '@testing-library/react'
import { StrictMode } from 'react'
import { beforeEach, describe, expect, it, vi } from 'vitest'

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
const manifest = {
  lesson_id: 'APR-R1-RM-01-L01-TECH',
  module_id: 'APR-R1-RM-01',
  version: '0.6.0-technical-placeholder',
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
      body: 'Orientation.',
      required: true,
    },
    {
      step_id: 'information',
      step_type: 'information',
      title: 'Information',
      body: 'Information.',
      required: true,
    },
    {
      step_id: 'interface-choice',
      step_type: 'single_choice',
      title: 'Choice',
      body: 'Choice.',
      required: true,
      options: [{ option_id: 'ok', label: 'OK', feedback: 'Fixed.' }],
    },
    {
      step_id: 'microphone-capture',
      step_type: 'recording',
      title: 'Microphone capture',
      body: 'Record.',
      required: true,
      prompt: 'Technical prompt.',
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
      feedback_id: 'APR-R1-RM-01-L01-FEEDBACK-TECH',
      feedback_mode: 'on-demand',
      feedback_source_attempt: 'original',
      feedback_requires_confirmed_transcript: true,
      feedback_source: 'controlled-technical-placeholder',
      feedback_storage_status: 'session-only',
      feedback_authorized_as_academic_feedback: false,
      feedback_authorized_as_evidence: false,
      feedback_required: false,
      retry_orchestration_mode: 'optional-post-feedback-latest-retry',
      retry_required: false,
    },
    {
      step_id: 'technical-reflection',
      step_type: 'reflection',
      title: 'Reflection',
      body: 'Reflect.',
      required: false,
      prompt: 'Note?',
      placeholder: 'Optional note.',
      max_characters: 80,
    },
  ],
}

function jsonResponse(
  data: unknown,
  status = 200,
  headers: Record<string, string> = {}
) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json', ...headers },
  })
}
function audioResponse(status = 200) {
  return new Response(new Uint8Array([1, 2, 3]), {
    status,
    headers: {
      'X-APR-Audio-Language': 'pt-BR',
      'X-APR-Audio-Status': 'generated-technical-placeholder',
    },
  })
}
function feedback(revision = 1) {
  return {
    feedback_id: 'APR-R1-RM-01-L01-FEEDBACK-TECH',
    attempt_role: 'original',
    source_confirmation_revision: revision,
    status: 'technical-placeholder',
    source: 'server-controlled',
    acknowledgement: 'Ack',
    primary_priority: 'Priority',
    cue: 'Cue',
    retry_instruction: 'Retry',
    uncertainty: 'Uncertainty',
    requires_retry: false,
    retry_allowed: true,
    authorized_as_academic_feedback: false,
    authorized_as_evidence: false,
    storage_status: 'session-only',
  }
}
async function openRecording(strict = false) {
  mockApiFetch.mockResolvedValueOnce(jsonResponse(manifest))
  if (strict) mockApiFetch.mockResolvedValueOnce(jsonResponse(manifest))
  render(
    strict ? (
      <StrictMode>
        <AprLessonPlayer endpoint={endpoint} />
      </StrictMode>
    ) : (
      <AprLessonPlayer endpoint={endpoint} />
    )
  )
  await screen.findByText('Orientation')
  fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
  fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
  fireEvent.click(screen.getByLabelText('OK'))
  fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
}
function noClosure() {
  expect(
    screen.queryByRole('heading', {
      name: 'Technical session ready for review',
    })
  ).toBeNull()
}
function row(label: string) {
  return screen.getByText(label).parentElement?.textContent
}
async function enterClosure() {
  fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
  await screen.findByRole('heading', { name: 'Reflection' })
  fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
  await screen.findByRole('heading', {
    name: 'Technical session ready for review',
  })
}

describe('APR session closure', () => {
  beforeEach(() => {
    cleanup()
    mockApiFetch.mockReset()
    mockPush.mockReset()
    vi.stubGlobal('URL', {
      createObjectURL: vi.fn(() => 'blob:test'),
      revokeObjectURL: vi.fn(),
    })
    vi.spyOn(window, 'confirm').mockReturnValue(true)
  })

  it('appears only after explicit final Continue and uses exact bounded copy without persistence calls', async () => {
    await openRecording()
    noClosure()
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    noClosure()
    await enterClosure()
    expect(
      screen.getByRole('heading', {
        name: 'Technical session ready for review',
      })
    ).toBeDefined()
    expect(
      screen.getByText(
        'You reached the end of this technical prototype. This summary describes browser-session activity only. It is not lesson completion, Progress, Evidence, a score, or a language result.'
      )
    ).toBeDefined()
    expect(
      screen.getAllByText('Session-only technical summary').length
    ).toBeGreaterThan(0)
    expect(
      screen.getByText(
        'Next: review your session, restart the technical flow, or exit to the APR module.'
      )
    ).toBeDefined()
    expect(row('Original recording')).toContain('Captured')
    expect(row('Original transcript')).toContain('Not confirmed')
    expect(row('Latest retry')).toContain('Not captured')
    expect(row('Technical model audio')).toContain('Not generated')
    expect(row('Controlled technical feedback')).toContain('Not requested')
    expect(row('Post-feedback retry')).toContain('Not applicable')
    expect(
      mockApiFetch.mock.calls.map(([u]) => String(u)).join('\n')
    ).not.toMatch(
      /completion|progress|evidence|closure|save-session|activity-log|learner-summary/
    )
    const summaryText =
      screen.getByText('Original recording').closest('dl')?.textContent ?? ''
    expect(summaryText).not.toMatch(
      /CEFR|proficiency|correctness|improvement|score/i
    )
  })

  it('summarizes optional transcript, model audio, feedback, retries, reflection, back, restart, and exit from session state only', async () => {
    cleanup()
    await openRecording()
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    mockApiFetch.mockResolvedValueOnce(
      jsonResponse({ draft_text: 'texto secreto' })
    )
    fireEvent.click(
      screen.getByRole('button', { name: 'Generate transcript draft' })
    )
    await screen.findByDisplayValue('texto secreto')
    fireEvent.click(
      screen.getByRole('button', { name: 'Confirm reviewed transcript' })
    )
    mockApiFetch.mockResolvedValueOnce(audioResponse())
    fireEvent.click(
      screen.getByRole('button', { name: 'Generate technical model audio' })
    )
    await screen.findByLabelText('Generated technical model audio playback')
    fireEvent.click(
      screen.getByRole('button', { name: 'Record another attempt' })
    )
    mockApiFetch.mockResolvedValueOnce(jsonResponse(feedback(1)))
    fireEvent.click(
      screen.getByRole('button', { name: 'Generate technical feedback' })
    )
    await screen.findByText('Controlled technical feedback')
    await enterClosure()
    expect(row('Post-feedback retry')).toContain('Not captured')
    expect(screen.queryByText('texto secreto')).toBeNull()
    fireEvent.click(screen.getByRole('button', { name: 'Back to reflection' }))
    expect(screen.getByRole('heading', { name: 'Reflection' })).toBeDefined()
    fireEvent.change(screen.getByLabelText('Note?'), {
      target: { value: 'keep this note' },
    })
    fireEvent.click(screen.getByRole('button', { name: 'Back' }))
    fireEvent.click(
      screen.getByRole('button', { name: 'Record another attempt' })
    )
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    expect(screen.getByDisplayValue('keep this note')).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    expect(row('Post-feedback retry')).toContain('Captured')
    expect(screen.queryByText('keep this note')).toBeNull()
    vi.mocked(window.confirm).mockReturnValueOnce(false)
    fireEvent.click(
      screen.getByRole('button', { name: 'Restart technical session' })
    )
    expect(
      screen.getByRole('heading', {
        name: 'Technical session ready for review',
      })
    ).toBeDefined()
    expect(row('Original transcript')).toContain('Confirmed')
    vi.mocked(window.confirm).mockReturnValueOnce(true)
    fireEvent.click(
      screen.getByRole('button', { name: 'Restart technical session' })
    )
    expect(
      await screen.findByRole('heading', { name: 'Orientation' })
    ).toBeDefined()
    expect(screen.queryByDisplayValue('keep this note')).toBeNull()
    cleanup()
    await openRecording()
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    await enterClosure()
    fireEvent.click(screen.getByRole('button', { name: 'Exit to APR module' }))
    expect(mockPush).toHaveBeenCalledWith('/apr/primeira-conexao')
  })

  it('reports technical issues and remains Strict Mode safe', async () => {
    await openRecording(true)
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    mockApiFetch.mockResolvedValueOnce(jsonResponse({}, 500))
    fireEvent.click(
      screen.getByRole('button', { name: 'Generate technical model audio' })
    )
    await screen.findByText(/could not generate technical model audio/i)
    mockApiFetch.mockResolvedValueOnce(jsonResponse({ draft_text: 'draft' }))
    fireEvent.click(
      screen.getByRole('button', { name: 'Generate transcript draft' })
    )
    await screen.findByDisplayValue('draft')
    fireEvent.click(
      screen.getByRole('button', { name: 'Confirm reviewed transcript' })
    )
    mockApiFetch.mockResolvedValueOnce(jsonResponse({}, 500))
    fireEvent.click(
      screen.getByRole('button', { name: 'Generate technical feedback' })
    )
    await screen.findByText(/could not load technical feedback/i)
    await enterClosure()
    expect(row('Technical model audio')).toContain('Technical issue')
    expect(row('Controlled technical feedback')).toContain('Technical issue')
    expect(row('Post-feedback retry')).toContain('Not applicable')
  })
})

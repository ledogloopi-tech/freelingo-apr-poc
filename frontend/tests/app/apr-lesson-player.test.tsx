import { describe, expect, it, vi, beforeEach } from 'vitest'
import { fireEvent, render, screen } from '@testing-library/react'

const { mockApiFetch } = vi.hoisted(() => ({
  mockApiFetch: vi.fn(),
}))

vi.mock('@/lib/api', () => ({
  apiFetch: mockApiFetch,
}))

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
          durationSeconds: hasOriginalAttempt ? 2.2 : 1.1,
        })
      }
    >
      {hasOriginalAttempt ? 'Record another attempt' : 'Start recording'}
    </button>
  ),
}))

import AprEnterTheConnectionLessonPage from '@/app/(apr)/apr/primeira-conexao/lessons/enter-the-connection/page'

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
      body: 'Technical placeholder lesson. Approved lesson content pending. This interaction tests the APR lesson player, not Portuguese capability.',
      required: true,
    },
    {
      step_id: 'information',
      step_type: 'information',
      title: 'Information',
      body: 'Structured content can load inside the APR boundary.',
      required: true,
    },
    {
      step_id: 'interface-choice',
      step_type: 'single_choice',
      title: 'Single-choice interaction',
      body: 'Choose any interface-testing option. This does not evaluate Portuguese ability.',
      required: true,
      options: [
        {
          option_id: 'layout-clear',
          label: 'The layout is clear enough to continue testing.',
          feedback:
            'Fixed technical feedback: selection recorded for this session only.',
        },
        {
          option_id: 'not-assessment',
          label: 'This is not a Portuguese assessment.',
          feedback:
            'Fixed technical feedback: no language capability was calculated.',
        },
      ],
    },
    {
      step_id: 'microphone-capture',
      step_type: 'recording',
      title: 'Microphone capture',
      body: 'Record a brief technical microphone test. This does not assess Portuguese capability.',
      required: true,
      prompt:
        'This recording remains only in this browser session. It is not uploaded, transcribed, scored or saved to the APR backend.',
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
      body: 'Enter a short technical note about the shell behavior only.',
      required: false,
      prompt: 'What should the APR team verify?',
      placeholder: 'Example technical note.',
      max_characters: 20,
    },
  ],
}

describe('APR lesson player', () => {
  beforeEach(() => {
    mockApiFetch.mockReset()
    let objectUrlCounter = 0
    vi.stubGlobal('URL', {
      createObjectURL: vi.fn(
        (blob: Blob) => `blob:${blob.size}:${objectUrlCounter++}`
      ),
      revokeObjectURL: vi.fn(),
    })
  })

  function renderManifest() {
    mockApiFetch.mockResolvedValueOnce(jsonResponse(manifest))
    return render(<AprEnterTheConnectionLessonPage />)
  }

  it('renders loading behavior and the manifest', async () => {
    renderManifest()

    expect(screen.getByRole('status').textContent).toContain(
      'Loading APR technical placeholder lesson'
    )

    expect(await screen.findByText('Enter the Connection')).toBeDefined()
    expect(
      screen.getByText(/Lesson Player Technical Demonstration/)
    ).toBeDefined()
    expect(screen.getByText('technical-placeholder')).toBeDefined()
    expect(mockApiFetch).toHaveBeenCalledWith(
      '/api/apr/modules/primeira-conexao/lessons/enter-the-connection'
    )
  })

  it('supports Step X of Y behavior, Back, and Continue', async () => {
    renderManifest()

    expect(await screen.findByText('Step 1 of 5.')).toBeDefined()
    expect(screen.getByRole('button', { name: 'Back' })).toBeDisabled()

    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    expect(screen.getByText('Step 2 of 5.')).toBeDefined()
    expect(screen.getByRole('button', { name: 'Back' })).not.toBeDisabled()

    fireEvent.click(screen.getByRole('button', { name: 'Back' }))
    expect(screen.getByText('Step 1 of 5.')).toBeDefined()
  })

  it('requires choice selection and shows fixed feedback', async () => {
    renderManifest()

    await screen.findByText('Step 1 of 5.')
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    expect(screen.getByText('Step 3 of 5.')).toBeDefined()

    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    expect(
      screen.getByText('Select one interface-testing option before continuing.')
    ).toBeDefined()

    fireEvent.click(
      screen.getByRole('radio', {
        name: 'This is not a Portuguese assessment.',
      })
    )
    expect(
      screen.getByText(
        'Fixed technical feedback: no language capability was calculated.'
      )
    ).toBeDefined()
  })

  it('preserves reflection text during backward and forward navigation and enforces limits', async () => {
    renderManifest()

    await screen.findByText('Step 1 of 5.')
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('radio', { name: /layout is clear/i }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))

    const textarea = screen.getByLabelText('What should the APR team verify?')
    fireEvent.change(textarea, {
      target: { value: '1234567890123456789012345' },
    })
    expect(textarea).toHaveValue('12345678901234567890')
    expect(screen.getByText('20 of 20 characters.')).toBeDefined()

    fireEvent.click(screen.getByRole('button', { name: 'Back' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    expect(
      screen.getByLabelText('What should the APR team verify?')
    ).toHaveValue('12345678901234567890')
  })

  it('asks for restart confirmation and clears current session state only after confirmation', async () => {
    const confirm = vi.fn().mockReturnValueOnce(false).mockReturnValueOnce(true)
    vi.stubGlobal('confirm', confirm)
    renderManifest()

    await screen.findByText('Step 1 of 5.')
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    expect(screen.getByText('Step 2 of 5.')).toBeDefined()

    fireEvent.click(screen.getByRole('button', { name: 'Restart' }))
    expect(screen.getByText('Step 2 of 5.')).toBeDefined()

    fireEvent.click(screen.getByRole('button', { name: 'Restart' }))
    expect(screen.getByText('Step 1 of 5.')).toBeDefined()
    expect(confirm).toHaveBeenCalledTimes(2)
  })

  it('requires one original recording, preserves original, replaces only latest retry, and clears on confirmed restart', async () => {
    const confirm = vi.fn().mockReturnValueOnce(false).mockReturnValueOnce(true)
    vi.stubGlobal('confirm', confirm)
    renderManifest()

    await screen.findByText('Step 1 of 5.')
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('radio', { name: /layout is clear/i }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))

    expect(screen.getByText('Step 4 of 5.')).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    expect(
      screen.getByText(
        'Create one technical microphone recording before continuing.'
      )
    ).toBeDefined()

    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    expect(screen.getByText('Original attempt')).toBeDefined()
    expect(screen.getByLabelText('Original attempt playback')).toBeDefined()
    const originalSrc = screen
      .getByLabelText('Original attempt playback')
      .getAttribute('src')

    fireEvent.click(
      screen.getByRole('button', { name: 'Record another attempt' })
    )
    expect(screen.getByText('Latest retry')).toBeDefined()
    const retrySrc = screen
      .getByLabelText('Latest retry playback')
      .getAttribute('src')
    fireEvent.click(
      screen.getByRole('button', { name: 'Record another attempt' })
    )
    expect(
      screen.getByLabelText('Original attempt playback').getAttribute('src')
    ).toBe(originalSrc)
    expect(
      screen.getByLabelText('Latest retry playback').getAttribute('src')
    ).not.toBe(retrySrc)
    expect(URL.revokeObjectURL).toHaveBeenCalledWith(retrySrc)

    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    expect(screen.getByText('Step 5 of 5.')).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Back' }))
    expect(screen.getByText('Original attempt')).toBeDefined()
    expect(screen.getByText('Latest retry')).toBeDefined()

    fireEvent.click(screen.getByRole('button', { name: 'Restart' }))
    expect(screen.getByText('Original attempt')).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Restart' }))
    expect(screen.getByText('Step 1 of 5.')).toBeDefined()
    expect(screen.queryByText('Original attempt')).toBeNull()
  })

  it('revokes retained object URLs on immediate unmount after captures', async () => {
    const { unmount } = renderManifest()

    await screen.findByText('Step 1 of 5.')
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('radio', { name: /layout is clear/i }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    const originalSrc = screen
      .getByLabelText('Original attempt playback')
      .getAttribute('src')

    unmount()

    expect(URL.revokeObjectURL).toHaveBeenCalledTimes(1)
    expect(URL.revokeObjectURL).toHaveBeenCalledWith(originalSrc)
  })

  it('revokes original and latest retry on unmount and only replaced retry during replacement', async () => {
    const { unmount } = renderManifest()

    await screen.findByText('Step 1 of 5.')
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('radio', { name: /layout is clear/i }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    const originalSrc = screen
      .getByLabelText('Original attempt playback')
      .getAttribute('src')
    fireEvent.click(
      screen.getByRole('button', { name: 'Record another attempt' })
    )
    const firstRetrySrc = screen
      .getByLabelText('Latest retry playback')
      .getAttribute('src')
    fireEvent.click(
      screen.getByRole('button', { name: 'Record another attempt' })
    )
    const latestRetrySrc = screen
      .getByLabelText('Latest retry playback')
      .getAttribute('src')

    expect(URL.revokeObjectURL).toHaveBeenCalledTimes(1)
    expect(URL.revokeObjectURL).toHaveBeenCalledWith(firstRetrySrc)
    expect(URL.revokeObjectURL).not.toHaveBeenCalledWith(originalSrc)
    expect(URL.revokeObjectURL).not.toHaveBeenCalledWith(latestRetrySrc)

    unmount()

    expect(URL.revokeObjectURL).toHaveBeenCalledTimes(3)
    expect(URL.revokeObjectURL).toHaveBeenCalledWith(originalSrc)
    expect(URL.revokeObjectURL).toHaveBeenCalledWith(latestRetrySrc)
  })

  it('does not revoke retained URLs on cancelled Restart and does not double revoke after confirmed Restart', async () => {
    const confirm = vi.fn().mockReturnValueOnce(false).mockReturnValueOnce(true)
    vi.stubGlobal('confirm', confirm)
    const { unmount } = renderManifest()

    await screen.findByText('Step 1 of 5.')
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('radio', { name: /layout is clear/i }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    const originalSrc = screen
      .getByLabelText('Original attempt playback')
      .getAttribute('src')
    fireEvent.click(
      screen.getByRole('button', { name: 'Record another attempt' })
    )
    const retrySrc = screen
      .getByLabelText('Latest retry playback')
      .getAttribute('src')

    fireEvent.click(screen.getByRole('button', { name: 'Restart' }))
    expect(URL.revokeObjectURL).not.toHaveBeenCalled()

    fireEvent.click(screen.getByRole('button', { name: 'Restart' }))
    expect(URL.revokeObjectURL).toHaveBeenCalledTimes(2)
    expect(URL.revokeObjectURL).toHaveBeenCalledWith(originalSrc)
    expect(URL.revokeObjectURL).toHaveBeenCalledWith(retrySrc)

    unmount()
    expect(URL.revokeObjectURL).toHaveBeenCalledTimes(2)
  })

  it('shows technical completion without academic completion language', async () => {
    renderManifest()

    await screen.findByText('Step 1 of 5.')
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('radio', { name: /layout is clear/i }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))

    expect(screen.getByText('APR lesson-player shell completed')).toBeDefined()
    expect(
      screen.getByText(
        'This technical completion is not academic Lesson completion.'
      )
    ).toBeDefined()
    expect(screen.queryByText(/you completed Lesson 1/i)).toBeNull()
  })

  it('shows disabled-environment and technical error states without learner blame', async () => {
    mockApiFetch.mockResolvedValueOnce(jsonResponse({}, 404))
    const { unmount } = render(<AprEnterTheConnectionLessonPage />)
    expect(await screen.findByRole('alert')).toHaveTextContent(
      'The APR technical proof of concept is disabled in this environment.'
    )
    unmount()

    mockApiFetch.mockResolvedValueOnce(jsonResponse({}, 500))
    render(<AprEnterTheConnectionLessonPage />)
    const alert = await screen.findByRole('alert')
    expect(alert.textContent).toContain(
      'Technical error loading APR lesson player'
    )
    expect(alert.textContent?.toLowerCase()).not.toContain('learner failed')
  })

  it('does not display awards, proficiency claims, or call inherited learning endpoints', async () => {
    renderManifest()

    await screen.findByText('Enter the Connection')

    const allText = document.body.textContent ?? ''
    expect(allText).not.toMatch(/XP|streak|CEFR|fluency|score|grade/i)

    const requestedUrls = mockApiFetch.mock.calls.map(([url]) => String(url))
    expect(requestedUrls).toEqual([
      '/api/apr/modules/primeira-conexao/lessons/enter-the-connection',
    ])
    expect(requestedUrls.join('\n')).not.toMatch(
      /onboarding|study-plan|progress|feedback|billing|assessment|conversation/
    )
  })
})

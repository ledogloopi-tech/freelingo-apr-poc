import { describe, expect, it, vi, beforeEach } from 'vitest'
import { fireEvent, render, screen } from '@testing-library/react'

const { mockApiFetch } = vi.hoisted(() => ({
  mockApiFetch: vi.fn(),
}))

vi.mock('@/lib/api', () => ({
  apiFetch: mockApiFetch,
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
  version: '0.1.0-technical-placeholder',
  title: 'Enter the Connection',
  internal_title: 'Lesson Player Technical Demonstration',
  content_status: 'technical-placeholder',
  authorized_for_pilot: false,
  authorized_for_public_release: false,
  estimated_minutes: 5,
  current_step_count: 4,
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
    vi.unstubAllGlobals()
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

    expect(await screen.findByText('Step 1 of 4.')).toBeDefined()
    expect(screen.getByRole('button', { name: 'Back' })).toBeDisabled()

    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    expect(screen.getByText('Step 2 of 4.')).toBeDefined()
    expect(screen.getByRole('button', { name: 'Back' })).not.toBeDisabled()

    fireEvent.click(screen.getByRole('button', { name: 'Back' }))
    expect(screen.getByText('Step 1 of 4.')).toBeDefined()
  })

  it('requires choice selection and shows fixed feedback', async () => {
    renderManifest()

    await screen.findByText('Step 1 of 4.')
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    expect(screen.getByText('Step 3 of 4.')).toBeDefined()

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

    await screen.findByText('Step 1 of 4.')
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('radio', { name: /layout is clear/i }))
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

    await screen.findByText('Step 1 of 4.')
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    expect(screen.getByText('Step 2 of 4.')).toBeDefined()

    fireEvent.click(screen.getByRole('button', { name: 'Restart' }))
    expect(screen.getByText('Step 2 of 4.')).toBeDefined()

    fireEvent.click(screen.getByRole('button', { name: 'Restart' }))
    expect(screen.getByText('Step 1 of 4.')).toBeDefined()
    expect(confirm).toHaveBeenCalledTimes(2)
  })

  it('shows technical completion without academic completion language', async () => {
    renderManifest()

    await screen.findByText('Step 1 of 4.')
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continue' }))
    fireEvent.click(screen.getByRole('radio', { name: /layout is clear/i }))
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

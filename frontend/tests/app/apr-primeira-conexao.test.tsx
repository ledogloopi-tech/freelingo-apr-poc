import { describe, expect, it, vi, beforeEach } from 'vitest'
import { render, screen, waitFor } from '@testing-library/react'

const { mockApiFetch, mockPush } = vi.hoisted(() => ({
  mockApiFetch: vi.fn(),
  mockPush: vi.fn(),
}))


vi.mock('next-intl', () => ({
  useTranslations: () => (key: string) => key,
}))

vi.mock('next/navigation', () => ({
  useRouter: () => ({
    push: mockPush,
    replace: vi.fn(),
    refresh: vi.fn(),
    back: vi.fn(),
    forward: vi.fn(),
    prefetch: vi.fn(),
  }),
}))

vi.mock('@/lib/api', () => ({
  apiFetch: mockApiFetch,
}))

import AprLayout from '@/app/(apr)/layout'
import AprPrimeiraConexaoPage from '@/app/(apr)/apr/primeira-conexao/page'
import { useAuthStore } from '@/store/auth'

function jsonResponse(data: unknown, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}

const meWithNullLearningGoals = {
  id: 1,
  username: 'apr-user',
  display_name: 'APR User',
  email: 'apr@example.com',
  native_language: 'es',
  target_language: 'en-GB',
  ui_locale: 'en',
  role: 'user',
  conversation_max_duration: 1800,
  conversation_inactivity_timeout: 180,
  avatar: null,
  is_verified: true,
  bio: null,
  learning_goals: null,
  subscription_status: 'none',
  subscription_ends_at: null,
}

describe('AprPrimeiraConexaoPage', () => {
  beforeEach(() => {
    mockApiFetch.mockReset()
    mockPush.mockReset()
    vi.unstubAllGlobals()
    useAuthStore.setState({ accessToken: null, user: null })
  })

  it('renders loading, title, and technical boundary metadata', async () => {
    mockApiFetch.mockResolvedValueOnce(
      jsonResponse({
        module_id: 'APR-R1-RM-01',
        title: 'Primeira Conexão',
        status: 'technical-boundary-only',
        target_language: 'pt-BR',
        bridge_language: 'es',
        authorized_for_pilot: false,
        authorized_for_public_release: false,
      })
    )

    render(<AprPrimeiraConexaoPage />)

    expect(screen.getByRole('status').textContent).toContain(
      'Loading APR technical boundary metadata'
    )
    expect(
      screen.getByText('Academia Português Reconectado')
    ).toBeDefined()
    expect(screen.getByText('Technical proof of concept')).toBeDefined()

    await waitFor(() =>
      expect(mockApiFetch).toHaveBeenCalledWith(
        '/api/apr/modules/primeira-conexao'
      )
    )
    expect(screen.getByText('technical-boundary-only')).toBeDefined()
    expect(screen.getByText('Brazilian Portuguese: pt-BR')).toBeDefined()
    expect(screen.getByText('Spanish bridge language: es')).toBeDefined()
    expect(screen.getByText('No CEFR placement')).toBeDefined()
    expect(screen.getByText('No XP or streak dependency')).toBeDefined()
    expect(screen.getByText('No AI-generated curriculum')).toBeDefined()
    expect(
      screen.getByText('Not authorized for pilot or public release')
    ).toBeDefined()
  })

  it('shows the disabled environment message when the backend returns 404', async () => {
    mockApiFetch.mockResolvedValueOnce(jsonResponse({}, 404))

    render(<AprPrimeiraConexaoPage />)

    const alert = await screen.findByRole('alert')
    expect(alert.textContent).toBe(
      'The APR technical proof of concept is disabled in this environment.'
    )
  })

  it('shows a technical API error without blaming the learner', async () => {
    mockApiFetch.mockResolvedValueOnce(jsonResponse({}, 500))

    render(<AprPrimeiraConexaoPage />)

    const alert = await screen.findByRole('alert')
    expect(alert.textContent).toContain(
      'Technical error loading APR module metadata'
    )
    expect(alert.textContent?.toLowerCase()).not.toContain('learner failed')
  })

  it('does not display XP, streaks, CEFR results, or fluency claims', async () => {
    mockApiFetch.mockResolvedValueOnce(
      jsonResponse({
        module_id: 'APR-R1-RM-01',
        title: 'Primeira Conexão',
        status: 'technical-boundary-only',
        target_language: 'pt-BR',
        bridge_language: 'es',
        authorized_for_pilot: false,
        authorized_for_public_release: false,
      })
    )

    render(<AprPrimeiraConexaoPage />)

    await screen.findByText('technical-boundary-only')

    expect(screen.queryByText(/XP earned/i)).toBeNull()
    expect(screen.queryByText(/streak count/i)).toBeNull()
    expect(screen.queryByText(/CEFR result/i)).toBeNull()
    expect(screen.queryByText(/fluent/i)).toBeNull()
  })

  it('redirects unauthenticated APR users to login', async () => {
    vi.stubGlobal(
      'fetch',
      vi.fn().mockResolvedValueOnce(jsonResponse({}, 401))
    )

    render(
      <AprLayout>
        <div>APR child</div>
      </AprLayout>
    )

    await waitFor(() => expect(mockPush).toHaveBeenCalledWith('/login'))
    expect(screen.queryByText('APR child')).toBeNull()
  })

  it('allows authenticated users without FreeLingo onboarding to render APR', async () => {
    vi.stubGlobal(
      'fetch',
      vi.fn().mockResolvedValueOnce(jsonResponse({ access_token: 'token-1' }))
    )
    mockApiFetch.mockResolvedValueOnce(jsonResponse(meWithNullLearningGoals))

    render(
      <AprLayout>
        <div>APR child</div>
      </AprLayout>
    )

    expect(await screen.findByText('APR child')).toBeDefined()
    expect(mockPush).not.toHaveBeenCalledWith('/onboarding')
    expect(mockApiFetch).toHaveBeenCalledWith('/api/auth/me')
  })

  it('does not request inherited FreeLingo learning or billing endpoints', async () => {
    vi.stubGlobal(
      'fetch',
      vi.fn().mockResolvedValueOnce(jsonResponse({ access_token: 'token-1' }))
    )
    mockApiFetch.mockResolvedValueOnce(jsonResponse(meWithNullLearningGoals))

    render(
      <AprLayout>
        <div>APR child</div>
      </AprLayout>
    )

    await screen.findByText('APR child')

    const requestedUrls = mockApiFetch.mock.calls.map(([url]) => String(url))
    expect(requestedUrls).toEqual(['/api/auth/me'])
    expect(requestedUrls).not.toContain('/api/feedback/unread-summary')
    expect(requestedUrls).not.toContain('/api/study-plan/today')
    expect(requestedUrls).not.toContain('/api/progress/summary')
    expect(requestedUrls).not.toContain('/api/billing/config')
    expect(requestedUrls).not.toContain('/api/assessment')
    expect(requestedUrls).not.toContain('/api/conversation')
  })
})

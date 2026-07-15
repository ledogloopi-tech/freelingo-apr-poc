import { describe, expect, it, vi, beforeEach } from 'vitest'
import { render, screen, waitFor } from '@testing-library/react'

const { mockApiFetch } = vi.hoisted(() => ({
  mockApiFetch: vi.fn(),
}))

vi.mock('@/lib/api', () => ({
  apiFetch: mockApiFetch,
}))

import AprPrimeiraConexaoPage from '@/app/(app)/apr/primeira-conexao/page'

function jsonResponse(data: unknown, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}

describe('AprPrimeiraConexaoPage', () => {
  beforeEach(() => {
    mockApiFetch.mockReset()
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
})

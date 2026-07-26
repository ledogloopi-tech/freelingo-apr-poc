import { describe, expect, it, vi, beforeEach } from 'vitest'
import { render, screen } from '@testing-library/react'
import AprPrimeiraConexaoPage from '@/app/(apr)/apr/primeira-conexao/page'

const { mockApiFetch } = vi.hoisted(() => ({ mockApiFetch: vi.fn() }))
vi.mock('@/lib/api', () => ({ apiFetch: mockApiFetch }))
function jsonResponse(data: unknown, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}

beforeEach(() => mockApiFetch.mockReset())

describe('APR Primeira Conexão module boundary', () => {
  it('requires the protected APR API, honors feature-flag 404, and renders Day 9 module status', async () => {
    mockApiFetch.mockResolvedValueOnce(
      jsonResponse({
        module_id: 'APR-R1-RM-01',
        title: 'Primeira Conexão',
        status: 'internal-instructional-vertical-slice',
        target_language: 'pt-BR',
        bridge_language: 'es',
        authorized_for_pilot: false,
        authorized_for_public_release: false,
      })
    )
    render(<AprPrimeiraConexaoPage />)
    expect(
      await screen.findByText('internal-instructional-vertical-slice')
    ).toBeDefined()
    expect(mockApiFetch).toHaveBeenCalledWith(
      '/api/apr/modules/primeira-conexao'
    )
    expect(
      screen.getByText('Not authorized for pilot or public release')
    ).toBeDefined()
  })

  it('shows disabled and technical error states without unrelated app calls', async () => {
    mockApiFetch.mockResolvedValueOnce(new Response('', { status: 404 }))
    const { unmount } = render(<AprPrimeiraConexaoPage />)
    expect(
      await screen.findByText(
        'The APR technical proof of concept is disabled in this environment.'
      )
    ).toBeDefined()
    unmount()
    mockApiFetch.mockReset()
    mockApiFetch.mockResolvedValueOnce(new Response('', { status: 500 }))
    render(<AprPrimeiraConexaoPage />)
    expect(
      await screen.findByText(/Technical error loading APR module metadata/)
    ).toBeDefined()
    expect(mockApiFetch.mock.calls.map(([url]) => url)).not.toContain(
      '/api/feedback/unread-summary'
    )
  })
})

import { describe, expect, it, vi, beforeEach } from 'vitest'
import { fireEvent, render, screen } from '@testing-library/react'
import { AprLessonPlayer } from '@/components/apr/AprLessonPlayer'
import { day9Manifest, endpoint, jsonResponse } from './apr-day9-fixtures'

const { mockApiFetch, mockPush } = vi.hoisted(() => ({
  mockApiFetch: vi.fn(),
  mockPush: vi.fn(),
}))
vi.mock('@/lib/api', () => ({ apiFetch: mockApiFetch }))
vi.mock('next/navigation', () => ({ useRouter: () => ({ push: mockPush }) }))
vi.mock('@/components/apr/AprAudioRecorder', () => ({
  AprAudioRecorder: ({
    onCapture,
  }: {
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
          blob: new Blob(['original'], { type: 'audio/webm' }),
          mimeType: 'audio/webm',
          durationSeconds: 1,
        })
      }
    >
      Comenzar grabación
    </button>
  ),
}))

beforeEach(() => {
  mockApiFetch.mockReset()
  mockPush.mockReset()
  vi.stubGlobal('URL', {
    createObjectURL: vi.fn(() => 'blob:audio'),
    revokeObjectURL: vi.fn(),
  })
  vi.spyOn(window, 'confirm').mockReturnValue(false)
})
async function reachReflection() {
  mockApiFetch.mockResolvedValueOnce(jsonResponse(day9Manifest()))
  render(<AprLessonPlayer endpoint={endpoint} />)
  await screen.findByText('Entrar en la conexión')
  fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
  fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
  fireEvent.click(
    screen.getByLabelText('Comparte algo verdadero y termina con E você?')
  )
  fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
  fireEvent.click(screen.getByRole('button', { name: 'Comenzar grabación' }))
  fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
  await screen.findByText('Reflexiona')
}

describe('APR Day 9 session closure', () => {
  it('uses approved closure copy and makes no Completion, Progress, or Evidence request', async () => {
    await reachReflection()
    fireEvent.change(screen.getByLabelText(/¿Qué bloque te ayudó/), {
      target: { value: 'Hoy me ayudó E você? porque invita.' },
    })
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    expect(screen.getByText('Tu práctica está lista para cerrar')).toBeDefined()
    expect(screen.getByText(/Esto no genera una nota/)).toBeDefined()
    const urls = mockApiFetch.mock.calls.map(([url]) => String(url))
    expect(urls.some((url) => /completion|progress|evidence/i.test(url))).toBe(
      false
    )
  })

  it('cancelled Restart preserves state, confirmed Restart clears URLs, and Exit routes to the module', async () => {
    await reachReflection()
    fireEvent.change(screen.getByLabelText(/¿Qué bloque te ayudó/), {
      target: { value: 'Hoy me ayudó Gosto de...' },
    })
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    vi.mocked(window.confirm).mockReturnValueOnce(false)
    fireEvent.click(screen.getByRole('button', { name: 'Reiniciar' }))
    expect(screen.getByText('Tu práctica está lista para cerrar')).toBeDefined()
    vi.mocked(window.confirm).mockReturnValueOnce(true)
    fireEvent.click(screen.getByRole('button', { name: 'Reiniciar' }))
    expect(URL.revokeObjectURL).toHaveBeenCalled()
    expect(await screen.findByText('Entrar en la conexión')).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    fireEvent.click(
      screen.getByLabelText('Comparte algo verdadero y termina con E você?')
    )
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    fireEvent.click(screen.getByRole('button', { name: 'Comenzar grabación' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    fireEvent.click(
      screen.getByRole('button', { name: 'Cerrar esta práctica' })
    )
    expect(mockPush).toHaveBeenCalledWith('/apr/primeira-conexao')
  })
})

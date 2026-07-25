import { describe, expect, it, vi, beforeEach } from 'vitest'
import { fireEvent, render, screen } from '@testing-library/react'
import { AprLessonPlayer } from '@/components/apr/AprLessonPlayer'
import { day9Manifest, endpoint, jsonResponse } from './apr-day9-fixtures'

const { mockApiFetch } = vi.hoisted(() => ({ mockApiFetch: vi.fn() }))
vi.mock('@/lib/api', () => ({ apiFetch: mockApiFetch }))
vi.mock('next/navigation', () => ({ useRouter: () => ({ push: vi.fn() }) }))
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
      {hasOriginalAttempt ? 'Grabar otro intento' : 'Comenzar grabación'}
    </button>
  ),
}))

beforeEach(() => {
  mockApiFetch.mockReset()
  vi.stubGlobal('URL', {
    createObjectURL: vi.fn((blob) => `blob:${blob.size}:${Math.random()}`),
    revokeObjectURL: vi.fn(),
  })
})
async function practice() {
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
}

describe('APR Day 9 transcript confirmation', () => {
  it('is optional, starts only by request, remains editable, and confirms explicitly', async () => {
    await practice()
    expect(
      mockApiFetch.mock.calls.some(([url]) =>
        String(url).includes('transcription-drafts')
      )
    ).toBe(false)
    mockApiFetch.mockResolvedValueOnce(
      jsonResponse({ draft_text: 'machine draft' })
    )
    fireEvent.click(
      screen.getByRole('button', { name: 'Solicitar transcripción' })
    )
    expect(
      await screen.findByText('Borrador generado por máquina')
    ).toBeDefined()
    fireEvent.change(screen.getByLabelText('Texto revisado'), {
      target: { value: 'Oi! Eu sou Ana. Gosto de café. E você?' },
    })
    fireEvent.click(
      screen.getByRole('button', { name: 'Confirmar este texto' })
    )
    expect(screen.getByText('Texto confirmado por ti')).toBeDefined()
    expect(
      screen.getByText(
        /No estás enviando Evidencia ni aceptando una puntuación/
      )
    ).toBeDefined()
  })

  it('keeps Original and Latest retry transcript state separate and ignores failed transcription as a technical issue', async () => {
    await practice()
    fireEvent.click(screen.getByRole('button', { name: 'Grabar otro intento' }))
    expect(screen.getByText('Latest retry separado')).toBeDefined()
    mockApiFetch.mockResolvedValueOnce(new Response('', { status: 503 }))
    fireEvent.click(
      screen.getAllByRole('button', { name: 'Solicitar transcripción' })[0]
    )
    expect(
      await screen.findByText(/No pudimos generar la transcripción/)
    ).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    expect(await screen.findByText('Reflexiona')).toBeDefined()
  })
})

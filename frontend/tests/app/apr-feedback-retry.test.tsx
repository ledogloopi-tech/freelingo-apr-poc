import { describe, expect, it, vi, beforeEach } from 'vitest'
import { fireEvent, render, screen } from '@testing-library/react'
import { AprLessonPlayer } from '@/components/apr/AprLessonPlayer'
import {
  day9Feedback,
  day9Manifest,
  endpoint,
  feedbackId,
  jsonResponse,
} from './apr-day9-fixtures'

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
    createObjectURL: vi.fn(() => 'blob:audio'),
    revokeObjectURL: vi.fn(),
  })
})
async function originalWithDraft() {
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
  mockApiFetch.mockResolvedValueOnce(
    jsonResponse({ draft_text: 'unconfirmed machine draft' })
  )
  fireEvent.click(
    screen.getByRole('button', { name: 'Solicitar transcripción' })
  )
  await screen.findByText('Borrador generado por máquina')
}
function feedbackCalls() {
  return mockApiFetch.mock.calls.filter(([url]) =>
    String(url).endsWith('/feedback-drafts')
  )
}

describe('APR Day 9 controlled feedback and retry', () => {
  it('never sends an unconfirmed machine draft and uses static self-check without backend feedback', async () => {
    await originalWithDraft()
    expect(feedbackCalls()).toHaveLength(0)
    fireEvent.click(
      screen.getByRole('button', { name: 'Usar lista de auto-revisión' })
    )
    expect(
      screen.getByText(/No podemos verificar con seguridad qué dijiste/)
    ).toBeDefined()
    expect(feedbackCalls()).toHaveLength(0)
  })

  it('sends only learner-confirmed Original transcript with revision and renders non-scoring guidance', async () => {
    await originalWithDraft()
    fireEvent.change(screen.getByLabelText('Texto revisado'), {
      target: { value: 'Oi! Eu sou Ana. Gosto de café. E você?' },
    })
    fireEvent.click(
      screen.getByRole('button', { name: 'Confirmar este texto' })
    )
    mockApiFetch.mockResolvedValueOnce(jsonResponse(day9Feedback))
    fireEvent.click(
      screen.getByRole('button', { name: 'Pedir ayuda controlada' })
    )
    expect(await screen.findByText('Guía controlada')).toBeDefined()
    const body = JSON.parse(feedbackCalls()[0][1]?.body as string)
    expect(body).toEqual({
      feedback_id: feedbackId,
      attempt_role: 'original',
      transcript_confirmation_revision: 1,
      confirmed_transcript: 'Oi! Eu sou Ana. Gosto de café. E você?',
    })
    expect(screen.getByText(/No evalúa pronunciación/)).toBeDefined()
    expect(
      screen.queryByText(/score|fluency|confidence|improvement/i)
    ).toBeNull()
  })

  it('treats feedback failure as technical and keeps retry optional and separate', async () => {
    await originalWithDraft()
    fireEvent.change(screen.getByLabelText('Texto revisado'), {
      target: { value: 'Oi! Eu sou Ana. Gosto de café. E você?' },
    })
    fireEvent.click(
      screen.getByRole('button', { name: 'Confirmar este texto' })
    )
    mockApiFetch.mockResolvedValueOnce(new Response('', { status: 503 }))
    fireEvent.click(
      screen.getByRole('button', { name: 'Pedir ayuda controlada' })
    )
    expect(
      await screen.findByText(/La ayuda técnica no estuvo disponible/)
    ).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Grabar otro intento' }))
    expect(screen.getByText('Latest retry separado')).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    expect(await screen.findByText('Reflexiona')).toBeDefined()
  })
})

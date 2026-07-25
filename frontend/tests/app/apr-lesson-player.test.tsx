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
          durationSeconds: hasOriginalAttempt ? 2 : 1,
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
  vi.spyOn(window, 'confirm').mockReturnValue(false)
})
async function renderLesson() {
  mockApiFetch.mockResolvedValueOnce(jsonResponse(day9Manifest()))
  render(<AprLessonPlayer endpoint={endpoint} />)
  await screen.findByText('Entrar en la conexión')
}

describe('APR Day 9 lesson player shell', () => {
  it('renders manifest identity, five-step order, controlled IDs, and approved content with placeholder absent', async () => {
    await renderLesson()
    expect(screen.getByText('approved-day9-instructional-slice')).toBeDefined()
    expect(screen.getByText(/1.0.0-day9-controlled-slice/)).toBeDefined()
    expect(screen.queryByText(/Technical placeholder lesson/)).toBeNull()
    const manifest = day9Manifest()
    expect(manifest.content_package_id).toBe('APR-R1-RM01-L01-D9')
    expect(manifest.practice_classification).toBe('instructional-practice-only')
    expect(manifest.authorized_for_pilot).toBe(false)
    expect(manifest.authorized_for_public_release).toBe(false)
    expect(manifest.steps.map((step) => step.step_type)).toEqual([
      'orientation',
      'information',
      'single_choice',
      'recording',
      'reflection',
    ])
    expect(manifest.steps.flatMap((step) => step.content_ids)).toContain(
      'APR-ALT-R1-RM01-L01-D9-WRT-001'
    )
  })

  it('preserves navigation, recognition gate, reflection state, and written Practice gate', async () => {
    await renderLesson()
    expect(screen.getByText('Paso 1 de 5.')).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    expect(screen.getByText('Paso 2 de 5.')).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Atrás' }))
    expect(screen.getByText('Paso 1 de 5.')).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    expect(
      screen.getByText('Selecciona una opción antes de continuar.')
    ).toBeDefined()
    fireEvent.click(
      screen.getByLabelText(
        'Repite su nombre para que la otra persona lo memorice.'
      )
    )
    expect(screen.getByText(/Fíjate en el final/)).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    expect(
      screen.getByText(
        'Graba un Original o completa la práctica escrita antes de continuar.'
      )
    ).toBeDefined()
    fireEvent.click(
      screen.getByRole('button', { name: 'Practicar por escrito' })
    )
    fireEvent.change(
      screen.getByLabelText('Escribe tu apertura en portugués:'),
      { target: { value: 'Oi! Eu sou Lia. Gosto de livros. E você?' } }
    )
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    fireEvent.change(screen.getByLabelText(/¿Qué bloque te ayudó/), {
      target: { value: 'Hoy me ayudó E você?' },
    })
    fireEvent.click(screen.getByRole('button', { name: 'Atrás' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    expect(screen.getByDisplayValue('Hoy me ayudó E você?')).toBeDefined()
  })

  it('protects Original, separates replaceable Latest retry, and revokes object URLs on confirmed Restart', async () => {
    await renderLesson()
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    fireEvent.click(
      screen.getByLabelText('Comparte algo verdadero y termina con E você?')
    )
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    fireEvent.click(screen.getByRole('button', { name: 'Comenzar grabación' }))
    expect(screen.getByText('Original protegido')).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Grabar otro intento' }))
    expect(screen.getByText('Latest retry separado')).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Grabar otro intento' }))
    expect(screen.getByText('Original protegido')).toBeDefined()
    vi.mocked(window.confirm).mockReturnValueOnce(true)
    fireEvent.click(screen.getByRole('button', { name: 'Reiniciar' }))
    expect(URL.revokeObjectURL).toHaveBeenCalled()
    expect(await screen.findByText('Entrar en la conexión')).toBeDefined()
  })
})

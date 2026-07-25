import { describe, expect, it, vi, beforeEach } from 'vitest'
import { fireEvent, render, screen, waitFor } from '@testing-library/react'
import { AprLessonPlayer } from '@/components/apr/AprLessonPlayer'
import {
  day9Manifest,
  endpoint,
  jsonResponse,
  modelAudioId,
} from './apr-day9-fixtures'

const { mockApiFetch } = vi.hoisted(() => ({ mockApiFetch: vi.fn() }))
vi.mock('@/lib/api', () => ({ apiFetch: mockApiFetch }))
vi.mock('next/navigation', () => ({ useRouter: () => ({ push: vi.fn() }) }))
vi.mock('@/components/apr/AprAudioRecorder', () => ({
  AprAudioRecorder: () => <button type="button">Comenzar grabación</button>,
}))

beforeEach(() => {
  mockApiFetch.mockReset()
  vi.stubGlobal('URL', {
    createObjectURL: vi.fn(() => 'blob:model'),
    revokeObjectURL: vi.fn(),
  })
})
async function step2() {
  mockApiFetch.mockResolvedValueOnce(jsonResponse(day9Manifest()))
  render(<AprLessonPlayer endpoint={endpoint} />)
  await screen.findByText('Entrar en la conexión')
  fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
  await screen.findByText('Escucha una apertura')
}

describe('APR Day 9 model audio', () => {
  it('is optional, in Step 2, explicit, server-identified, no-autoplay, temporary, and revokes URLs', async () => {
    await step2()
    expect(mockApiFetch).toHaveBeenCalledTimes(1)
    expect(
      screen.getAllByText(
        'Audio temporal generado para pruebas. No es la grabación final de la Academia.'
      ).length
    ).toBeGreaterThan(0)
    mockApiFetch.mockResolvedValueOnce(
      new Response('audio', {
        status: 200,
        headers: {
          'Content-Type': 'audio/mpeg',
          'X-APR-Audio-Status': 'generated-temporary-testing',
          'X-APR-Audio-Language': 'pt-BR',
        },
      })
    )
    fireEvent.click(
      screen.getByRole('button', { name: 'Escuchar audio temporal' })
    )
    const audio = await screen.findByLabelText(
      'Reproducción del audio temporal'
    )
    expect(audio).not.toHaveAttribute('autoplay')
    expect(JSON.parse(mockApiFetch.mock.calls[1][1].body)).toEqual({
      model_audio_id: modelAudioId,
    })
    mockApiFetch.mockResolvedValueOnce(
      new Response('new', {
        status: 200,
        headers: { 'Content-Type': 'audio/mpeg' },
      })
    )
    fireEvent.click(
      screen.getByRole('button', { name: 'Generar de nuevo audio temporal' })
    )
    await waitFor(() =>
      expect(URL.revokeObjectURL).toHaveBeenCalledWith('blob:model')
    )
  })

  it('treats TTS failure as technical and still allows progression', async () => {
    await step2()
    mockApiFetch.mockResolvedValueOnce(new Response('', { status: 503 }))
    fireEvent.click(
      screen.getByRole('button', { name: 'Escuchar audio temporal' })
    )
    expect(
      await screen.findByText(/No pudimos generar el audio temporal/)
    ).toBeDefined()
    fireEvent.click(screen.getByRole('button', { name: 'Continuar' }))
    expect(
      await screen.findByText('Abre espacio para una respuesta')
    ).toBeDefined()
  })
})

import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import {
  act,
  cleanup,
  fireEvent,
  render,
  screen,
  waitFor,
} from '@testing-library/react'
import { AprAudioRecorder } from '@/components/apr/AprAudioRecorder'

class MockMediaRecorder {
  static isTypeSupported = vi.fn((type: string) => type === 'audio/webm')
  static instances: MockMediaRecorder[] = []
  mimeType: string
  ondataavailable: ((event: { data: Blob }) => void) | null = null
  onerror: (() => void) | null = null
  onstop: (() => void) | null = null

  constructor(_stream: MediaStream, options?: MediaRecorderOptions) {
    this.mimeType = options?.mimeType ?? 'browser-default'
    MockMediaRecorder.instances.push(this)
  }

  start = vi.fn()
  stop = vi.fn(() => {
    this.ondataavailable?.({
      data: new Blob(['audio'], { type: this.mimeType }),
    })
    this.onstop?.()
  })
}

function setupMedia() {
  const stop = vi.fn()
  const stream = { getTracks: () => [{ stop }] }
  const getUserMedia = vi.fn().mockResolvedValue(stream)
  Object.defineProperty(navigator, 'mediaDevices', {
    configurable: true,
    value: { getUserMedia },
  })
  vi.stubGlobal('MediaRecorder', MockMediaRecorder)
  return { getUserMedia, stop }
}

describe('AprAudioRecorder', () => {
  beforeEach(() => {
    vi.useRealTimers()
    MockMediaRecorder.instances = []
    MockMediaRecorder.isTypeSupported.mockClear()
  })

  afterEach(() => {
    cleanup()
    vi.unstubAllGlobals()
    vi.useRealTimers()
  })

  it('does not request microphone permission or record on render', () => {
    const { getUserMedia } = setupMedia()
    render(
      <AprAudioRecorder
        maxSeconds={10}
        hasOriginalAttempt={false}
        onCapture={vi.fn()}
      />
    )

    expect(getUserMedia).not.toHaveBeenCalled()
    expect(MockMediaRecorder.instances).toHaveLength(0)
    expect(
      screen.getByRole('button', { name: 'Start recording' })
    ).toBeDefined()
  })

  it('requests permission after Start recording and captures non-empty audio', async () => {
    const onCapture = vi.fn()
    const { getUserMedia, stop } = setupMedia()
    render(
      <AprAudioRecorder
        maxSeconds={10}
        hasOriginalAttempt={false}
        onCapture={onCapture}
      />
    )

    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))

    await waitFor(() =>
      expect(getUserMedia).toHaveBeenCalledWith({ audio: true })
    )
    expect(await screen.findByText(/Recording status: recording/)).toBeDefined()

    fireEvent.click(screen.getByRole('button', { name: 'Stop recording' }))

    await waitFor(() => expect(onCapture).toHaveBeenCalledTimes(1))
    expect(onCapture.mock.calls[0][0].blob.size).toBeGreaterThan(0)
    expect(onCapture.mock.calls[0][0].mimeType).toBe('audio/webm')
    expect(stop).toHaveBeenCalled()
  })

  it('shows required permission, no-device, unsupported, and empty technical messages', async () => {
    const denied = vi
      .fn()
      .mockRejectedValue(new DOMException('', 'NotAllowedError'))
    Object.defineProperty(navigator, 'mediaDevices', {
      configurable: true,
      value: { getUserMedia: denied },
    })
    vi.stubGlobal('MediaRecorder', MockMediaRecorder)
    const { unmount } = render(
      <AprAudioRecorder
        maxSeconds={10}
        hasOriginalAttempt={false}
        onCapture={vi.fn()}
      />
    )
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    expect(
      await screen.findByText(/Microphone access was not granted/)
    ).toBeDefined()
    unmount()

    const noDevice = vi
      .fn()
      .mockRejectedValue(new DOMException('', 'NotFoundError'))
    Object.defineProperty(navigator, 'mediaDevices', {
      configurable: true,
      value: { getUserMedia: noDevice },
    })
    render(
      <AprAudioRecorder
        maxSeconds={10}
        hasOriginalAttempt={false}
        onCapture={vi.fn()}
      />
    )
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    expect(await screen.findByText(/No microphone was detected/)).toBeDefined()
    unmount()
    cleanup()

    vi.stubGlobal('MediaRecorder', undefined)
    render(
      <AprAudioRecorder
        maxSeconds={10}
        hasOriginalAttempt={false}
        onCapture={vi.fn()}
      />
    )
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    expect(
      await screen.findByText(/This browser cannot record audio/)
    ).toBeDefined()
    unmount()
    cleanup()

    class EmptyRecorder extends MockMediaRecorder {
      stop = vi.fn(() => {
        this.onstop?.()
      })
    }
    setupMedia()
    vi.stubGlobal('MediaRecorder', EmptyRecorder)
    render(
      <AprAudioRecorder
        maxSeconds={10}
        hasOriginalAttempt={false}
        onCapture={vi.fn()}
      />
    )
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    await screen.findByText(/Recording status: recording/)
    fireEvent.click(screen.getByRole('button', { name: 'Stop recording' }))
    expect(
      await screen.findByText(/No usable audio was captured/)
    ).toBeDefined()
  })

  it('auto-stops at the maximum duration and cleans up on unmount', async () => {
    vi.useFakeTimers()
    const onCapture = vi.fn()
    const { stop } = setupMedia()
    const { unmount } = render(
      <AprAudioRecorder
        maxSeconds={10}
        hasOriginalAttempt={false}
        onCapture={onCapture}
      />
    )

    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    await act(async () => {})
    expect(screen.getByText(/Recording status: recording/)).toBeDefined()
    act(() => {
      vi.advanceTimersByTime(10_000)
    })

    expect(onCapture).toHaveBeenCalledTimes(1)
    expect(stop).toHaveBeenCalled()
    unmount()
    expect(stop).toHaveBeenCalled()
  })
})

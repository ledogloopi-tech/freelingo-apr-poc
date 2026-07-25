import { describe, expect, it, vi, beforeEach, afterEach } from 'vitest'
import { fireEvent, render, screen, waitFor } from '@testing-library/react'
import { AprAudioRecorder } from '@/components/apr/AprAudioRecorder'

class MockMediaRecorder {
  static instances: MockMediaRecorder[] = []
  static isTypeSupported = vi.fn(() => true)
  state = 'inactive'
  mimeType = 'audio/webm;codecs=opus'
  ondataavailable: ((event: BlobEvent) => void) | null = null
  onstop: (() => void) | null = null
  onerror: (() => void) | null = null
  constructor(public stream: MediaStream) {
    MockMediaRecorder.instances.push(this)
  }
  start() {
    this.state = 'recording'
  }
  stop() {
    this.state = 'inactive'
    this.ondataavailable?.({
      data: new Blob(['audio'], { type: 'audio/webm' }),
    } as BlobEvent)
    this.onstop?.()
  }
}

function track() {
  return { stop: vi.fn() } as unknown as MediaStreamTrack
}
function streamWith(trackRef = track()) {
  return { getTracks: () => [trackRef] } as unknown as MediaStream
}

beforeEach(() => {
  MockMediaRecorder.instances = []
  vi.stubGlobal('MediaRecorder', MockMediaRecorder)
  Object.defineProperty(navigator, 'mediaDevices', {
    configurable: true,
    value: { getUserMedia: vi.fn(async () => streamWith()) },
  })
})
afterEach(() => {
  vi.unstubAllGlobals()
})

describe('AprAudioRecorder Day 9 recorder guarantees', () => {
  it('does not request microphone permission until learner action, then captures session-only audio', async () => {
    const onCapture = vi.fn()
    render(
      <AprAudioRecorder
        maxSeconds={20}
        hasOriginalAttempt={false}
        onCapture={onCapture}
      />
    )
    expect(navigator.mediaDevices.getUserMedia).not.toHaveBeenCalled()
    fireEvent.click(screen.getByRole('button', { name: 'Comenzar grabación' }))
    await waitFor(() =>
      expect(navigator.mediaDevices.getUserMedia).toHaveBeenCalledWith({
        audio: true,
      })
    )
    fireEvent.click(screen.getByRole('button', { name: 'Detener grabación' }))
    await waitFor(() => expect(onCapture).toHaveBeenCalledTimes(1))
    expect(
      screen.getByText('Grabación de práctica capturada solo para esta sesión.')
    ).toBeDefined()
  })

  it('stops media tracks and suppresses capture on unmount while permission is pending', async () => {
    const pendingTrack = track()
    let resolve!: (stream: MediaStream) => void
    Object.defineProperty(navigator, 'mediaDevices', {
      configurable: true,
      value: {
        getUserMedia: vi.fn(
          () =>
            new Promise<MediaStream>((r) => {
              resolve = r
            })
        ),
      },
    })
    const onCapture = vi.fn()
    const { unmount } = render(
      <AprAudioRecorder
        maxSeconds={20}
        hasOriginalAttempt={false}
        onCapture={onCapture}
      />
    )
    fireEvent.click(screen.getByRole('button', { name: 'Comenzar grabación' }))
    unmount()
    resolve(streamWith(pendingTrack))
    await Promise.resolve()
    expect(pendingTrack.stop).toHaveBeenCalled()
    expect(onCapture).not.toHaveBeenCalled()
  })

  it('presents microphone failures as technical issues and offers the written Practice recovery route in copy', async () => {
    Object.defineProperty(navigator, 'mediaDevices', {
      configurable: true,
      value: {
        getUserMedia: vi.fn(async () => {
          throw new DOMException('denied', 'NotAllowedError')
        }),
      },
    })
    render(
      <AprAudioRecorder
        maxSeconds={20}
        hasOriginalAttempt={false}
        onCapture={vi.fn()}
      />
    )
    fireEvent.click(screen.getByRole('button', { name: 'Comenzar grabación' }))
    expect(
      await screen.findByText(/No pudimos usar el micrófono/)
    ).toBeDefined()
    expect(screen.getByText(/continuar con la práctica escrita/)).toBeDefined()
  })
})

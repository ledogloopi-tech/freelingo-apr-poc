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

type ChunkPlan = Array<{ body: BlobPart; type?: string }>

let nextChunks: ChunkPlan = [{ body: 'audio', type: 'audio/webm' }]
let nextRecorderMimeType = 'audio/webm'
let autoStopOnStop = true

class MockMediaRecorder {
  static isTypeSupported = vi.fn((type: string) => type === 'audio/webm')
  static instances: MockMediaRecorder[] = []
  mimeType: string
  state: RecordingState = 'inactive'
  ondataavailable: ((event: { data: Blob }) => void) | null = null
  onerror: (() => void) | null = null
  onstop: (() => void) | null = null

  constructor(_stream: MediaStream, options?: MediaRecorderOptions) {
    this.mimeType = nextRecorderMimeType || options?.mimeType || ''
    MockMediaRecorder.instances.push(this)
  }

  start = vi.fn(() => {
    this.state = 'recording'
  })

  stop = vi.fn(() => {
    this.state = 'inactive'
    if (!autoStopOnStop) return
    nextChunks.forEach((chunk) => {
      this.ondataavailable?.({
        data: new Blob([chunk.body], { type: chunk.type ?? this.mimeType }),
      })
    })
    this.onstop?.()
  })

  emitStop() {
    nextChunks.forEach((chunk) => {
      this.ondataavailable?.({
        data: new Blob([chunk.body], { type: chunk.type ?? this.mimeType }),
      })
    })
    this.state = 'inactive'
    this.onstop?.()
  }

  emitErrorThenStop() {
    this.onerror?.()
    this.emitStop()
  }
}

function deferred<T>() {
  let resolve!: (value: T) => void
  let reject!: (reason?: unknown) => void
  const promise = new Promise<T>((promiseResolve, promiseReject) => {
    resolve = promiseResolve
    reject = promiseReject
  })
  return { promise, resolve, reject }
}

function setupMedia(options?: { deferred?: boolean }) {
  const stop = vi.fn()
  const stream = { getTracks: () => [{ stop }] } as unknown as MediaStream
  const pending = deferred<MediaStream>()
  const getUserMedia = options?.deferred
    ? vi.fn().mockReturnValue(pending.promise)
    : vi.fn().mockResolvedValue(stream)
  Object.defineProperty(navigator, 'mediaDevices', {
    configurable: true,
    value: { getUserMedia },
  })
  vi.stubGlobal('MediaRecorder', MockMediaRecorder)
  return { getUserMedia, pending, stop, stream }
}

function renderRecorder(onCapture = vi.fn()) {
  return render(
    <AprAudioRecorder
      maxSeconds={10}
      hasOriginalAttempt={false}
      onCapture={onCapture}
    />
  )
}

describe('AprAudioRecorder', () => {
  beforeEach(() => {
    vi.useRealTimers()
    nextChunks = [{ body: 'audio', type: 'audio/webm' }]
    nextRecorderMimeType = 'audio/webm'
    autoStopOnStop = true
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
    renderRecorder()

    expect(getUserMedia).not.toHaveBeenCalled()
    expect(MockMediaRecorder.instances).toHaveLength(0)
    expect(
      screen.getByRole('button', { name: 'Start recording' })
    ).toBeDefined()
  })

  it('requests permission after Start recording and captures non-empty audio', async () => {
    const onCapture = vi.fn()
    const { getUserMedia, stop } = setupMedia()
    renderRecorder(onCapture)

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

  it('stops a stream returned after unmount while permission is pending without starting MediaRecorder', async () => {
    const onCapture = vi.fn()
    const { pending, stop, stream } = setupMedia({ deferred: true })
    const { unmount } = renderRecorder(onCapture)

    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    unmount()

    await act(async () => {
      pending.resolve(stream)
    })

    expect(stop).toHaveBeenCalledTimes(1)
    expect(MockMediaRecorder.instances).toHaveLength(0)
    expect(onCapture).not.toHaveBeenCalled()
  })

  it('cancels an active MediaRecorder on unmount and suppresses late onstop capture', async () => {
    const onCapture = vi.fn()
    const { stop } = setupMedia()
    const { unmount } = renderRecorder(onCapture)

    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    await screen.findByText(/Recording status: recording/)
    const recorder = MockMediaRecorder.instances[0]

    unmount()
    recorder.emitStop()

    expect(recorder.stop).toHaveBeenCalledTimes(1)
    expect(stop).toHaveBeenCalledTimes(1)
    expect(onCapture).not.toHaveBeenCalled()
  })

  it('suppresses capture when unmounted during processing before a late stop event', async () => {
    autoStopOnStop = false
    const onCapture = vi.fn()
    setupMedia()
    const { unmount } = renderRecorder(onCapture)

    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    await screen.findByText(/Recording status: recording/)
    const recorder = MockMediaRecorder.instances[0]
    fireEvent.click(screen.getByRole('button', { name: 'Stop recording' }))

    unmount()
    recorder.emitStop()

    expect(onCapture).not.toHaveBeenCalled()
  })

  it('does not create a capture when recorder error is followed by onstop', async () => {
    const onCapture = vi.fn()
    setupMedia()
    renderRecorder(onCapture)

    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    await screen.findByText(/Recording status: recording/)
    MockMediaRecorder.instances[0].emitErrorThenStop()

    expect(
      await screen.findByText(/A technical microphone error occurred/)
    ).toBeDefined()
    expect(onCapture).not.toHaveBeenCalled()
  })

  it('blocks rapid repeated Start activation synchronously', async () => {
    const { getUserMedia, pending, stream } = setupMedia({ deferred: true })
    renderRecorder()
    const start = screen.getByRole('button', { name: 'Start recording' })

    fireEvent.click(start)
    fireEvent.click(start)
    fireEvent.click(start)

    expect(getUserMedia).toHaveBeenCalledTimes(1)
    await act(async () => {
      pending.resolve(stream)
    })
    expect(MockMediaRecorder.instances).toHaveLength(1)
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
    const { unmount } = renderRecorder()
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    expect(
      await screen.findByText(/Microphone access was not granted/)
    ).toBeDefined()
    unmount()
    cleanup()

    const noDevice = vi
      .fn()
      .mockRejectedValue(new DOMException('', 'NotFoundError'))
    Object.defineProperty(navigator, 'mediaDevices', {
      configurable: true,
      value: { getUserMedia: noDevice },
    })
    renderRecorder()
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    expect(await screen.findByText(/No microphone was detected/)).toBeDefined()
    unmount()
    cleanup()

    vi.stubGlobal('MediaRecorder', undefined)
    renderRecorder()
    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    expect(
      await screen.findByText(/This browser cannot record audio/)
    ).toBeDefined()
    unmount()
    cleanup()

    nextChunks = []
    setupMedia()
    vi.stubGlobal('MediaRecorder', MockMediaRecorder)
    renderRecorder()
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
    const { unmount } = renderRecorder(onCapture)

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

  it('uses a typed data chunk when the browser-default recorder has an empty mimeType', async () => {
    MockMediaRecorder.isTypeSupported.mockReturnValue(false)
    nextRecorderMimeType = ''
    nextChunks = [{ body: 'audio', type: 'audio/mp4' }]
    const onCapture = vi.fn()
    setupMedia()
    renderRecorder(onCapture)

    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    await screen.findByText(/Recording status: recording/)
    fireEvent.click(screen.getByRole('button', { name: 'Stop recording' }))

    expect(onCapture).toHaveBeenCalledTimes(1)
    expect(onCapture.mock.calls[0][0].blob.type).toBe('audio/mp4')
    expect(onCapture.mock.calls[0][0].mimeType).toBe('audio/mp4')
  })

  it('uses an honest unknown metadata fallback when no MIME information exists', async () => {
    MockMediaRecorder.isTypeSupported.mockReturnValue(false)
    nextRecorderMimeType = ''
    nextChunks = [{ body: 'audio', type: '' }]
    const onCapture = vi.fn()
    setupMedia()
    renderRecorder(onCapture)

    fireEvent.click(screen.getByRole('button', { name: 'Start recording' }))
    await screen.findByText(/Recording status: recording/)
    fireEvent.click(screen.getByRole('button', { name: 'Stop recording' }))

    expect(onCapture).toHaveBeenCalledTimes(1)
    expect(onCapture.mock.calls[0][0].blob.type).toBe('')
    expect(onCapture.mock.calls[0][0].mimeType).toBe('unknown')
    expect(onCapture.mock.calls[0][0].mimeType).not.toBe('browser-default')
  })
})

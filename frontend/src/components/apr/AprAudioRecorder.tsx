'use client'

import { useEffect, useRef, useState } from 'react'
import { Button } from '@/components/ui/button'

export type AprCapturedAudio = {
  blob: Blob
  mimeType: string
  durationSeconds: number
}

type RecorderState =
  | 'idle'
  | 'requesting_permission'
  | 'recording'
  | 'processing'
  | 'ready'
  | 'technical_error'
  | 'unsupported'

type AprAudioRecorderProps = {
  maxSeconds: number
  hasOriginalAttempt: boolean
  onCapture: (capture: AprCapturedAudio) => void
}

const MIME_CANDIDATES = ['audio/webm;codecs=opus', 'audio/webm', 'audio/mp4']

const ERROR_MESSAGES = {
  permission:
    'Microphone access was not granted. This is a technical access issue, not a language failure.',
  noDevice:
    'No microphone was detected. This is a technical access issue, not a language failure.',
  unsupported:
    'This browser cannot record audio for the APR technical proof of concept.',
  empty: 'No usable audio was captured. Try the technical recording again.',
  generic:
    'A technical microphone error occurred. No language result was recorded.',
}

function selectMimeType(): string | undefined {
  if (typeof MediaRecorder === 'undefined') return undefined
  const supports = MediaRecorder.isTypeSupported
  if (typeof supports !== 'function') return undefined
  return MIME_CANDIDATES.find((candidate) => supports(candidate))
}

function stopStream(stream: MediaStream | null): void {
  stream?.getTracks().forEach((track) => track.stop())
}

function formatElapsed(seconds: number): string {
  return `${seconds.toFixed(1)} seconds`
}

export function AprAudioRecorder({
  maxSeconds,
  hasOriginalAttempt,
  onCapture,
}: AprAudioRecorderProps) {
  const [state, setState] = useState<RecorderState>('idle')
  const [elapsedSeconds, setElapsedSeconds] = useState(0)
  const [message, setMessage] = useState(
    'Recorder is idle. Microphone access has not been requested.'
  )
  const recorderRef = useRef<MediaRecorder | null>(null)
  const streamRef = useRef<MediaStream | null>(null)
  const chunksRef = useRef<Blob[]>([])
  const startedAtRef = useRef<number>(0)
  const intervalRef = useRef<ReturnType<typeof setInterval> | null>(null)
  const autoStopRef = useRef<ReturnType<typeof setTimeout> | null>(null)

  function clearTimers() {
    if (intervalRef.current) clearInterval(intervalRef.current)
    if (autoStopRef.current) clearTimeout(autoStopRef.current)
    intervalRef.current = null
    autoStopRef.current = null
  }

  function cleanupStream() {
    stopStream(streamRef.current)
    streamRef.current = null
  }

  function finishWithError(nextMessage: string, nextState: RecorderState) {
    clearTimers()
    cleanupStream()
    recorderRef.current = null
    chunksRef.current = []
    setMessage(nextMessage)
    setState(nextState)
  }

  function stopRecording() {
    const recorder = recorderRef.current
    if (!recorder) return
    setState('processing')
    setMessage('Processing technical microphone recording.')
    clearTimers()
    try {
      recorder.stop()
    } catch {
      finishWithError(ERROR_MESSAGES.generic, 'technical_error')
    }
  }

  async function startRecording() {
    if (state === 'recording' || state === 'requesting_permission') return
    if (
      typeof MediaRecorder === 'undefined' ||
      !navigator.mediaDevices?.getUserMedia
    ) {
      finishWithError(ERROR_MESSAGES.unsupported, 'unsupported')
      return
    }

    setState('requesting_permission')
    setElapsedSeconds(0)
    setMessage('Requesting microphone access for the APR technical recording.')

    let stream: MediaStream | null = null
    try {
      stream = await navigator.mediaDevices.getUserMedia({ audio: true })
      streamRef.current = stream
      chunksRef.current = []
      const selectedMimeType = selectMimeType()
      const recorder = selectedMimeType
        ? new MediaRecorder(stream, { mimeType: selectedMimeType })
        : new MediaRecorder(stream)
      recorderRef.current = recorder
      startedAtRef.current = Date.now()

      recorder.ondataavailable = (event: BlobEvent) => {
        if (event.data?.size > 0) chunksRef.current.push(event.data)
      }

      recorder.onerror = () => {
        finishWithError(ERROR_MESSAGES.generic, 'technical_error')
      }

      recorder.onstop = () => {
        clearTimers()
        const durationSeconds = Math.max(
          0,
          (Date.now() - startedAtRef.current) / 1000
        )
        const mimeType =
          recorder.mimeType || selectedMimeType || 'browser-default'
        const blob = new Blob(chunksRef.current, { type: mimeType })
        cleanupStream()
        recorderRef.current = null
        chunksRef.current = []
        if (blob.size <= 0) {
          setState('technical_error')
          setMessage(ERROR_MESSAGES.empty)
          return
        }
        onCapture({ blob, mimeType: blob.type || mimeType, durationSeconds })
        setState('ready')
        setMessage(
          'Technical recording captured for this browser session only.'
        )
      }

      recorder.start()
      setState('recording')
      setMessage(
        'Recording technical microphone test. No audio is being uploaded.'
      )
      intervalRef.current = setInterval(() => {
        setElapsedSeconds((Date.now() - startedAtRef.current) / 1000)
      }, 100)
      autoStopRef.current = setTimeout(() => {
        stopRecording()
      }, maxSeconds * 1000)
    } catch (error) {
      if (stream) stopStream(stream)
      const name = error instanceof DOMException ? error.name : ''
      if (name === 'NotAllowedError' || name === 'SecurityError') {
        finishWithError(ERROR_MESSAGES.permission, 'technical_error')
      } else if (name === 'NotFoundError' || name === 'DevicesNotFoundError') {
        finishWithError(ERROR_MESSAGES.noDevice, 'technical_error')
      } else {
        finishWithError(ERROR_MESSAGES.generic, 'technical_error')
      }
    }
  }

  useEffect(() => {
    return () => {
      clearTimers()
      cleanupStream()
      recorderRef.current = null
    }
  }, [])

  const isRecording = state === 'recording'
  const isBusy = state === 'requesting_permission' || state === 'processing'
  const buttonLabel = isRecording
    ? 'Stop recording'
    : hasOriginalAttempt
      ? 'Record another attempt'
      : 'Start recording'

  return (
    <div className="space-y-4 rounded-lg border p-4">
      <div role="status" aria-live="polite" className="space-y-1 text-sm">
        <p className="font-medium">
          Recording status: {state.replace('_', ' ')}
        </p>
        <p>{message}</p>
        {(isRecording || elapsedSeconds > 0) && (
          <p>Elapsed recording time: {formatElapsed(elapsedSeconds)}</p>
        )}
      </div>
      <Button
        type="button"
        onClick={isRecording ? stopRecording : startRecording}
        disabled={isBusy}
      >
        {buttonLabel}
      </Button>
    </div>
  )
}

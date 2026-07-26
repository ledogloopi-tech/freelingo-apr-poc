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

type CaptureSession = {
  id: number
  cancelled: boolean
}

const MIME_CANDIDATES = ['audio/webm;codecs=opus', 'audio/webm', 'audio/mp4']
const UNKNOWN_MIME_TYPE_LABEL = 'unknown'

const ERROR_MESSAGES = {
  permission:
    'No pudimos usar el micrófono. Esto es un problema técnico, no un resultado sobre tu portugués. Puedes intentarlo de nuevo, continuar con la práctica escrita o cerrar la sesión.',
  noDevice:
    'No pudimos usar el micrófono. Esto es un problema técnico, no un resultado sobre tu portugués. Puedes intentarlo de nuevo, continuar con la práctica escrita o cerrar la sesión.',
  unsupported:
    'No pudimos usar el micrófono. Esto es un problema técnico, no un resultado sobre tu portugués. Puedes intentarlo de nuevo, continuar con la práctica escrita o cerrar la sesión.',
  empty:
    'No pudimos usar el micrófono. Esto es un problema técnico, no un resultado sobre tu portugués. Puedes intentarlo de nuevo, continuar con la práctica escrita o cerrar la sesión.',
  generic:
    'No pudimos usar el micrófono. Esto es un problema técnico, no un resultado sobre tu portugués. Puedes intentarlo de nuevo, continuar con la práctica escrita o cerrar la sesión.',
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

function recorderIsActive(recorder: MediaRecorder): boolean {
  return recorder.state !== 'inactive'
}

export function AprAudioRecorder({
  maxSeconds,
  hasOriginalAttempt,
  onCapture,
}: AprAudioRecorderProps) {
  const [state, setState] = useState<RecorderState>('idle')
  const [elapsedSeconds, setElapsedSeconds] = useState(0)
  const [message, setMessage] = useState(
    'La grabadora está lista. El micrófono se pedirá solo cuando lo indiques.'
  )
  const recorderRef = useRef<MediaRecorder | null>(null)
  const streamRef = useRef<MediaStream | null>(null)
  const chunksRef = useRef<Blob[]>([])
  const startedAtRef = useRef<number>(0)
  const intervalRef = useRef<ReturnType<typeof setInterval> | null>(null)
  const autoStopRef = useRef<ReturnType<typeof setTimeout> | null>(null)
  const mountedRef = useRef(false)
  const nextCaptureIdRef = useRef(0)
  const activeCaptureRef = useRef<CaptureSession | null>(null)

  function isActiveSession(session: CaptureSession): boolean {
    return (
      mountedRef.current &&
      activeCaptureRef.current === session &&
      !session.cancelled
    )
  }

  function clearTimers() {
    if (intervalRef.current) clearInterval(intervalRef.current)
    if (autoStopRef.current) clearTimeout(autoStopRef.current)
    intervalRef.current = null
    autoStopRef.current = null
  }

  function detachRecorderHandlers(recorder: MediaRecorder | null) {
    if (!recorder) return
    recorder.ondataavailable = null
    recorder.onstop = null
    recorder.onerror = null
  }

  function clearCaptureReferences() {
    cleanupStream()
    recorderRef.current = null
    chunksRef.current = []
  }

  function cleanupStream() {
    stopStream(streamRef.current)
    streamRef.current = null
  }

  function cancelActiveCapture() {
    const session = activeCaptureRef.current
    if (session) session.cancelled = true
    activeCaptureRef.current = null
    clearTimers()
    const recorder = recorderRef.current
    detachRecorderHandlers(recorder)
    if (recorder && recorderIsActive(recorder)) {
      try {
        recorder.stop()
      } catch {
        // Cancellation is best effort; tracks and refs are still cleared below.
      }
    }
    clearCaptureReferences()
  }

  function finishWithError(nextMessage: string, nextState: RecorderState) {
    cancelActiveCapture()
    if (!mountedRef.current) return
    setMessage(nextMessage)
    setState(nextState)
  }

  function stopRecording() {
    const session = activeCaptureRef.current
    const recorder = recorderRef.current
    if (!session || !recorder || !isActiveSession(session)) return
    setState('processing')
    setMessage('Preparando tu grabación de práctica.')
    clearTimers()
    try {
      recorder.stop()
    } catch {
      finishWithError(ERROR_MESSAGES.generic, 'technical_error')
    }
  }

  async function startRecording() {
    if (activeCaptureRef.current) return
    if (
      typeof MediaRecorder === 'undefined' ||
      !navigator.mediaDevices?.getUserMedia
    ) {
      if (mountedRef.current) {
        setMessage(ERROR_MESSAGES.unsupported)
        setState('unsupported')
      }
      return
    }

    const session: CaptureSession = {
      id: nextCaptureIdRef.current + 1,
      cancelled: false,
    }
    nextCaptureIdRef.current = session.id
    activeCaptureRef.current = session

    setState('requesting_permission')
    setElapsedSeconds(0)
    setMessage('Solicitando acceso al micrófono para tu práctica.')

    let stream: MediaStream | null = null
    try {
      stream = await navigator.mediaDevices.getUserMedia({ audio: true })
      if (!isActiveSession(session)) {
        stopStream(stream)
        if (activeCaptureRef.current === session)
          activeCaptureRef.current = null
        return
      }

      streamRef.current = stream
      chunksRef.current = []
      const selectedMimeType = selectMimeType()
      const recorder = selectedMimeType
        ? new MediaRecorder(stream, { mimeType: selectedMimeType })
        : new MediaRecorder(stream)
      if (!isActiveSession(session)) {
        stopStream(stream)
        return
      }
      recorderRef.current = recorder
      startedAtRef.current = Date.now()

      recorder.ondataavailable = (event: BlobEvent) => {
        if (!isActiveSession(session)) return
        if (event.data?.size > 0) chunksRef.current.push(event.data)
      }

      recorder.onerror = () => {
        if (!isActiveSession(session)) return
        finishWithError(ERROR_MESSAGES.generic, 'technical_error')
      }

      recorder.onstop = () => {
        if (!isActiveSession(session)) return
        clearTimers()
        const durationSeconds = Math.max(
          0,
          (Date.now() - startedAtRef.current) / 1000
        )
        const chunks = chunksRef.current
        const firstChunkType = chunks.find((chunk) => chunk.type)?.type
        const finalMimeType =
          recorder.mimeType || selectedMimeType || firstChunkType
        const blob = finalMimeType
          ? new Blob(chunks, { type: finalMimeType })
          : new Blob(chunks)
        cleanupStream()
        detachRecorderHandlers(recorder)
        recorderRef.current = null
        chunksRef.current = []
        activeCaptureRef.current = null
        if (blob.size <= 0) {
          if (!mountedRef.current) return
          setState('technical_error')
          setMessage(ERROR_MESSAGES.empty)
          return
        }
        onCapture({
          blob,
          mimeType: blob.type || finalMimeType || UNKNOWN_MIME_TYPE_LABEL,
          durationSeconds,
        })
        if (!mountedRef.current) return
        setState('ready')
        setMessage('Grabación de práctica capturada solo para esta sesión.')
      }

      if (!isActiveSession(session)) {
        stopStream(stream)
        return
      }
      recorder.start()
      if (!isActiveSession(session)) {
        cancelActiveCapture()
        return
      }
      setState('recording')
      setMessage('Grabando tu práctica. No se está subiendo audio.')
      intervalRef.current = setInterval(() => {
        if (!isActiveSession(session)) return
        setElapsedSeconds((Date.now() - startedAtRef.current) / 1000)
      }, 100)
      autoStopRef.current = setTimeout(() => {
        if (!isActiveSession(session)) return
        stopRecording()
      }, maxSeconds * 1000)
    } catch (error) {
      if (stream) stopStream(stream)
      if (!isActiveSession(session)) {
        if (activeCaptureRef.current === session)
          activeCaptureRef.current = null
        return
      }
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
    mountedRef.current = true
    return () => {
      mountedRef.current = false
      cancelActiveCapture()
    }
    // cancelActiveCapture intentionally reads refs at unmount time.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const isRecording = state === 'recording'
  const isBusy = state === 'requesting_permission' || state === 'processing'
  const buttonLabel = isRecording
    ? 'Detener grabación'
    : hasOriginalAttempt
      ? 'Grabar otro intento'
      : 'Comenzar grabación'

  return (
    <div className="space-y-4 rounded-lg border p-4">
      <div role="status" aria-live="polite" className="space-y-1 text-sm">
        <p className="font-medium">
          Estado de grabación: {state.replace('_', ' ')}
        </p>
        <p>{message}</p>
        {(isRecording || elapsedSeconds > 0) && (
          <p>Tiempo grabado: {formatElapsed(elapsedSeconds)}</p>
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

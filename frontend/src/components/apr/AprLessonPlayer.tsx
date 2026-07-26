'use client'

import { useEffect, useRef, useState } from 'react'
import { useRouter } from 'next/navigation'
import {
  AprAudioRecorder,
  type AprCapturedAudio,
} from '@/components/apr/AprAudioRecorder'
import {
  AprFeedbackRetry,
  createEmptyFeedbackState,
  type AprFeedbackResponse,
  type AprFeedbackState,
} from '@/components/apr/AprFeedbackRetry'
import {
  AprModelAudio,
  createEmptyModelAudioState,
  type AprModelAudioMetadata,
  type AprModelAudioState,
} from '@/components/apr/AprModelAudio'
import {
  AprTranscriptDraft,
  createEmptyTranscriptState,
  type AprTranscriptState,
} from '@/components/apr/AprTranscriptDraft'
import {
  AprSessionClosure,
  type AprSessionClosureContent,
  type AprSessionSummary,
} from '@/components/apr/AprSessionClosure'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/components/ui/card'
import { apiFetch } from '@/lib/api'

const APR_DISABLED_MESSAGE =
  'The APR technical proof of concept is disabled in this environment.'

type AprBaseStep = {
  step_id: string
  step_type:
    | 'orientation'
    | 'information'
    | 'single_choice'
    | 'recording'
    | 'reflection'
  title: string
  body: string
  required: boolean
  content_ids: string[]
}
type AprContentBlock = { content_id: string; heading: string; body: string }
type AprModelAudioConfig = {
  model_audio_id: string
  temporary_audio_id: string
  mode: 'on-demand'
  language: 'pt-BR'
  source: string
  storage_status: 'session-only'
  authorized_as_final_content: boolean
  required: boolean
  disclosure: string
}
type AprInformationStep = AprBaseStep & {
  step_type: 'information'
  model_script?: string
  controlled_transcript?: string
  transcript_label?: string
  optional_translation?: string
  translation_label?: string
  spanish_bridge?: AprContentBlock
  pronunciation_guidance?: AprContentBlock
  pragmatic_guidance?: AprContentBlock
  model_audio?: AprModelAudioConfig
}
type AprSingleChoiceOption = {
  option_id: string
  label: string
  feedback: string
}
type AprSingleChoiceStep = AprBaseStep & {
  step_type: 'single_choice'
  options: AprSingleChoiceOption[]
  correct_option_id: string
  prompt_label: string
  required_warning: string
}
type AprWrittenAlternative = {
  content_id: string
  label: string
  notice: string
  prompt: string
  frame: string
  storage_status: 'session-only'
  practice_classification: string
  max_characters: number
}
type AprRecordingStep = AprBaseStep & {
  step_type: 'recording'
  prompt: string
  production_frame: string
  privacy_notice: string
  practice_notice: string
  max_seconds: number
  allow_retry: boolean
  preserve_original: boolean
  storage_status: 'session-only'
  transcription_language: 'pt'
  transcription_mode: 'on-demand'
  requires_learner_confirmation: boolean
  transcript_storage_status: 'session-only'
  transcript_authorized_as_evidence: boolean
  feedback_id: string
  feedback_mode: 'on-demand'
  feedback_source_attempt: 'original'
  feedback_requires_confirmed_transcript: boolean
  feedback_source: 'server-deterministic'
  feedback_storage_status: 'session-only'
  feedback_authorized_as_academic_feedback: boolean
  feedback_authorized_as_evidence: boolean
  feedback_required: boolean
  retry_orchestration_mode: 'optional-post-feedback-latest-retry'
  retry_required: boolean
  retry_instruction: string
  written_alternative: AprWrittenAlternative
}
type AprReflectionStep = AprBaseStep & {
  step_type: 'reflection'
  prompt: string
  placeholder?: string | null
  max_characters: number
}
type AprLessonStep =
  | (AprBaseStep & { step_type: 'orientation' })
  | AprInformationStep
  | AprSingleChoiceStep
  | AprRecordingStep
  | AprReflectionStep
type AprLessonManifest = {
  lesson_id: string
  module_id: string
  content_package_id: string
  version: string
  title: string
  internal_title: string
  content_status: string
  practice_classification: string
  authorization_notice: string
  authorized_for_pilot: boolean
  authorized_for_public_release: boolean
  estimated_minutes: number
  current_step_count: number
  session_closure: AprSessionClosureContent
  steps: AprLessonStep[]
}
type StepResponses = Record<string, { choice?: string; reflection?: string }>
type AprRecordingAttempt = AprCapturedAudio & { id: number; objectUrl: string }
type AttemptRole = 'original' | 'latestRetry'
type AprTranscriptCollection = {
  original: AprTranscriptState
  latestRetry: AprTranscriptState
}

function isNonEmptyString(value: unknown): value is string {
  return typeof value === 'string' && value.trim().length > 0
}
function paragraphs(text: string) {
  return text.split('\n\n').map((paragraph) => (
    <p key={paragraph} className="whitespace-pre-line">
      {paragraph}
    </p>
  ))
}
function isValidFeedbackResponse(
  value: unknown,
  expectedFeedbackId: string,
  expectedRevision: number
): value is AprFeedbackResponse {
  if (!value || typeof value !== 'object') return false
  const candidate = value as Record<string, unknown>
  return (
    candidate.feedback_id === expectedFeedbackId &&
    candidate.attempt_role === 'original' &&
    candidate.source_confirmation_revision === expectedRevision &&
    candidate.status === 'controlled-instructional-guidance' &&
    candidate.source === 'server-deterministic' &&
    candidate.requires_retry === false &&
    candidate.retry_allowed === true &&
    candidate.authorized_as_academic_feedback === false &&
    candidate.authorized_as_evidence === false &&
    candidate.storage_status === 'session-only' &&
    isNonEmptyString(candidate.feedback_case) &&
    isNonEmptyString(candidate.acknowledgement)
  )
}

export function AprLessonPlayer({ endpoint }: { endpoint: string }) {
  const router = useRouter()
  const [manifest, setManifest] = useState<AprLessonManifest | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [currentStepIndex, setCurrentStepIndex] = useState(0)
  const [responses, setResponses] = useState<StepResponses>({})
  const [choiceWarning, setChoiceWarning] = useState(false)
  const [recordingWarning, setRecordingWarning] = useState(false)
  const [writtenSelected, setWrittenSelected] = useState(false)
  const [writtenPractice, setWrittenPractice] = useState('')
  const [recordingAttempts, setRecordingAttempts] = useState<{
    original?: AprRecordingAttempt
    latestRetry?: AprRecordingAttempt
  }>({})
  const [modelAudio, setModelAudio] = useState<AprModelAudioState>(() =>
    createEmptyModelAudioState()
  )
  const modelAudioRef = useRef<AprModelAudioState>(createEmptyModelAudioState())
  const modelAudioRequestRef = useRef<{
    generation: number
    controller?: AbortController
  }>({ generation: 0 })
  const [transcripts, setTranscripts] = useState<AprTranscriptCollection>(
    () => ({
      original: createEmptyTranscriptState(),
      latestRetry: createEmptyTranscriptState(),
    })
  )
  const transcriptsRef = useRef<AprTranscriptCollection>({
    original: createEmptyTranscriptState(),
    latestRetry: createEmptyTranscriptState(),
  })
  const [feedback, setFeedback] = useState<AprFeedbackState>(() =>
    createEmptyFeedbackState()
  )
  const feedbackRef = useRef<AprFeedbackState>(createEmptyFeedbackState())
  const feedbackRequestRef = useRef<{
    generation: number
    activeGeneration: number | null
    controller?: AbortController
  }>({ generation: 0, activeGeneration: null })
  const latestRetrySequenceRef = useRef(0)
  const originalConfirmationRevisionRef = useRef(0)
  const [showSessionClosure, setShowSessionClosure] = useState(false)
  const headingRef = useRef<HTMLHeadingElement>(null)
  const attemptsRef = useRef(recordingAttempts)
  const mountedRef = useRef(true)
  const nextAttemptIdRef = useRef(0)
  const requestRefs = useRef({
    original: {
      generation: 0,
      activeGeneration: null as number | null,
      controller: undefined as AbortController | undefined,
    },
    latestRetry: {
      generation: 0,
      activeGeneration: null as number | null,
      controller: undefined as AbortController | undefined,
    },
  })

  useEffect(() => {
    let active = true
    async function loadLesson() {
      try {
        const res = await apiFetch(endpoint)
        if (res.status === 404) throw new Error(APR_DISABLED_MESSAGE)
        if (!res.ok)
          throw new Error(`APR lesson API returned HTTP ${res.status}`)
        const data = (await res.json()) as AprLessonManifest
        if (active) setManifest(data)
      } catch (err) {
        if (!active) return
        setError(
          err instanceof Error && err.message === APR_DISABLED_MESSAGE
            ? APR_DISABLED_MESSAGE
            : err instanceof Error
              ? `Technical error loading APR lesson player: ${err.message}`
              : 'Technical error loading APR lesson player.'
        )
      } finally {
        if (active) setLoading(false)
      }
    }
    loadLesson()
    return () => {
      active = false
    }
  }, [endpoint])
  useEffect(() => {
    headingRef.current?.focus()
  }, [currentStepIndex, showSessionClosure])
  useEffect(
    () => () => {
      mountedRef.current = false
      abortTranscriptRequest('original')
      abortTranscriptRequest('latestRetry')
      abortModelAudioRequest()
      abortFeedbackRequest()
      if (modelAudioRef.current.objectUrl)
        URL.revokeObjectURL(modelAudioRef.current.objectUrl)
      const current = attemptsRef.current
      if (current.original) URL.revokeObjectURL(current.original.objectUrl)
      if (current.latestRetry)
        URL.revokeObjectURL(current.latestRetry.objectUrl)
    },
    []
  )
  function setTranscriptsState(next: AprTranscriptCollection) {
    transcriptsRef.current = next
    setTranscripts(next)
  }
  function updateTranscriptState(role: AttemptRole, next: AprTranscriptState) {
    setTranscriptsState({ ...transcriptsRef.current, [role]: next })
  }
  function setFeedbackState(next: AprFeedbackState) {
    feedbackRef.current = next
    setFeedback(next)
  }
  function abortFeedbackRequest() {
    feedbackRequestRef.current.generation += 1
    feedbackRequestRef.current.activeGeneration = null
    feedbackRequestRef.current.controller?.abort()
    feedbackRequestRef.current.controller = undefined
  }
  function invalidateFeedback() {
    abortFeedbackRequest()
    setFeedbackState(createEmptyFeedbackState())
  }
  function setModelAudioState(next: AprModelAudioState) {
    modelAudioRef.current = next
    setModelAudio(next)
  }
  function clearModelAudioUrl() {
    if (modelAudioRef.current.objectUrl)
      URL.revokeObjectURL(modelAudioRef.current.objectUrl)
    setModelAudioState(createEmptyModelAudioState())
  }
  function abortModelAudioRequest() {
    modelAudioRequestRef.current.generation += 1
    modelAudioRequestRef.current.controller?.abort()
    modelAudioRequestRef.current.controller = undefined
  }
  function metadataFromHeaders(res: Response): AprModelAudioMetadata {
    return {
      language: res.headers.get('X-APR-Audio-Language') ?? 'pt-BR',
      status:
        res.headers.get('X-APR-Audio-Status') ?? 'generated-temporary-testing',
    }
  }
  async function requestModelAudio(config: AprModelAudioConfig) {
    if (modelAudioRef.current.status === 'requesting') return
    abortModelAudioRequest()
    const generation = modelAudioRequestRef.current.generation + 1
    modelAudioRequestRef.current.generation = generation
    const controller = new AbortController()
    modelAudioRequestRef.current.controller = controller
    setModelAudioState({
      ...modelAudioRef.current,
      status: 'requesting',
      technicalError: '',
      requestGeneration: generation,
    })
    try {
      const res = await apiFetch(`${endpoint}/model-audio`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ model_audio_id: config.model_audio_id }),
        signal: controller.signal,
      })
      if (!res.ok) throw new Error('model-audio failure')
      const blob = await res.blob()
      if (
        !mountedRef.current ||
        controller.signal.aborted ||
        modelAudioRequestRef.current.generation !== generation
      )
        return
      const objectUrl = URL.createObjectURL(blob)
      const previousUrl = modelAudioRef.current.objectUrl
      if (previousUrl) URL.revokeObjectURL(previousUrl)
      setModelAudioState({
        status: 'ready',
        objectUrl,
        mimeType: blob.type || 'unknown',
        byteSize: blob.size,
        technicalError: '',
        requestGeneration: generation,
        metadata: metadataFromHeaders(res),
      })
    } catch {
      if (
        !mountedRef.current ||
        controller.signal.aborted ||
        modelAudioRequestRef.current.generation !== generation
      )
        return
      setModelAudioState({
        ...modelAudioRef.current,
        status: 'technical_error',
        technicalError:
          'No pudimos generar el audio temporal. Esto es un problema técnico, no un resultado sobre tu portugués.',
        requestGeneration: generation,
      })
    } finally {
      if (modelAudioRequestRef.current.generation === generation)
        modelAudioRequestRef.current.controller = undefined
    }
  }
  function abortTranscriptRequest(role: AttemptRole) {
    const request = requestRefs.current[role]
    request.generation += 1
    request.activeGeneration = null
    request.controller?.abort()
    request.controller = undefined
  }
  function abortAllTranscriptRequests() {
    abortTranscriptRequest('original')
    abortTranscriptRequest('latestRetry')
  }
  async function requestFeedbackDraft(step: AprRecordingStep) {
    const currentFeedback = feedbackRef.current
    if (currentFeedback.status === 'requesting') return
    const revision = originalConfirmationRevisionRef.current
    const confirmed = transcriptsRef.current.original.confirmedTranscript
    if (!confirmed || revision < 1) return
    abortFeedbackRequest()
    const generation = feedbackRequestRef.current.generation + 1
    feedbackRequestRef.current.generation = generation
    feedbackRequestRef.current.activeGeneration = generation
    const controller = new AbortController()
    feedbackRequestRef.current.controller = controller
    setFeedbackState({
      ...currentFeedback,
      status: 'requesting',
      feedbackId: step.feedback_id,
      sourceAttemptRole: 'original',
      sourceConfirmationRevision: revision,
      technicalError: '',
      requestGeneration: generation,
      postFeedbackRetryCaptured: false,
    })
    try {
      const res = await apiFetch(`${endpoint}/feedback-drafts`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          feedback_id: step.feedback_id,
          attempt_role: 'original',
          transcript_confirmation_revision: revision,
          confirmed_transcript: confirmed,
        }),
        signal: controller.signal,
      })
      if (!res.ok) throw new Error('feedback failure')
      const data = (await res.json()) as unknown
      if (
        !mountedRef.current ||
        controller.signal.aborted ||
        feedbackRequestRef.current.generation !== generation ||
        originalConfirmationRevisionRef.current !== revision ||
        !transcriptsRef.current.original.confirmedTranscript
      )
        return
      if (!isValidFeedbackResponse(data, step.feedback_id, revision))
        throw new Error('invalid feedback response')
      const snapshot = latestRetrySequenceRef.current
      setFeedbackState({
        status: 'ready',
        feedbackId: data.feedback_id,
        sourceAttemptRole: 'original',
        sourceConfirmationRevision: data.source_confirmation_revision,
        response: data,
        technicalError: '',
        requestGeneration: generation,
        retrySequenceSnapshot: snapshot,
        postFeedbackRetryCaptured: latestRetrySequenceRef.current > snapshot,
      })
    } catch {
      if (
        !mountedRef.current ||
        controller.signal.aborted ||
        feedbackRequestRef.current.generation !== generation
      )
        return
      setFeedbackState({
        ...feedbackRef.current,
        status: 'technical_error',
        technicalError:
          'La ayuda técnica no estuvo disponible. Esto no es un resultado sobre tu portugués.',
        requestGeneration: generation,
        retrySequenceSnapshot: null,
        postFeedbackRetryCaptured: false,
      })
    } finally {
      if (feedbackRequestRef.current.activeGeneration === generation) {
        feedbackRequestRef.current.activeGeneration = null
        feedbackRequestRef.current.controller = undefined
      }
    }
  }
  function resetTranscripts() {
    originalConfirmationRevisionRef.current = 0
    invalidateFeedback()
    setTranscriptsState({
      original: createEmptyTranscriptState(),
      latestRetry: createEmptyTranscriptState(),
    })
  }
  function clearRecordingAttempts() {
    abortAllTranscriptRequests()
    const current = attemptsRef.current
    if (current.original) URL.revokeObjectURL(current.original.objectUrl)
    if (current.latestRetry) URL.revokeObjectURL(current.latestRetry.objectUrl)
    attemptsRef.current = {}
    setRecordingAttempts({})
    resetTranscripts()
  }
  function handleAudioCapture(capture: AprCapturedAudio) {
    const attempt = {
      ...capture,
      id: ++nextAttemptIdRef.current,
      objectUrl: URL.createObjectURL(capture.blob),
    }
    const current = attemptsRef.current
    const replacingRetry = Boolean(current.original)
    const replacedRetry = replacingRetry ? current.latestRetry : undefined
    const next = !current.original
      ? { original: attempt }
      : { ...current, latestRetry: attempt }
    if (replacingRetry) {
      abortTranscriptRequest('latestRetry')
      latestRetrySequenceRef.current += 1
      setTranscriptsState({
        ...transcriptsRef.current,
        latestRetry: createEmptyTranscriptState(),
      })
    }
    if (replacedRetry) URL.revokeObjectURL(replacedRetry.objectUrl)
    attemptsRef.current = next
    setRecordingWarning(false)
    setRecordingAttempts(next)
    const currentFeedback = feedbackRef.current
    if (
      replacingRetry &&
      currentFeedback.status === 'ready' &&
      currentFeedback.retrySequenceSnapshot !== null &&
      latestRetrySequenceRef.current > currentFeedback.retrySequenceSnapshot &&
      !currentFeedback.postFeedbackRetryCaptured
    )
      setFeedbackState({ ...currentFeedback, postFeedbackRetryCaptured: true })
  }
  function filenameForAttempt(attempt: AprRecordingAttempt) {
    const mime = attempt.blob.type || attempt.mimeType
    if (mime.includes('mp4')) return 'apr-recording.mp4'
    if (mime.includes('wav')) return 'apr-recording.wav'
    if (mime.includes('mpeg')) return 'apr-recording.mp3'
    if (mime.includes('ogg')) return 'apr-recording.ogg'
    if (mime.includes('webm')) return 'apr-recording.webm'
    return 'apr-recording.bin'
  }
  async function requestTranscriptDraft(role: AttemptRole) {
    const attempt = attemptsRef.current[role]
    const request = requestRefs.current[role]
    if (!attempt || request.activeGeneration !== null) return
    const requestId = request.generation + 1
    request.generation = requestId
    request.activeGeneration = requestId
    const controller = new AbortController()
    request.controller = controller
    updateTranscriptState(role, {
      ...transcriptsRef.current[role],
      status: 'requesting',
      requestId,
      attemptId: attempt.id,
      technicalError: '',
    })
    const formData = new FormData()
    formData.append('audio', attempt.blob, filenameForAttempt(attempt))
    formData.append(
      'attempt_role',
      role === 'original' ? 'original' : 'latest_retry'
    )
    try {
      const res = await apiFetch(`${endpoint}/transcription-drafts`, {
        method: 'POST',
        body: formData,
        signal: controller.signal,
      })
      if (!res.ok) throw new Error('transcription failure')
      const data = (await res.json()) as { draft_text: string }
      if (!mountedRef.current || controller.signal.aborted) return
      const currentTranscript = transcriptsRef.current[role]
      if (
        currentTranscript.requestId !== requestId ||
        currentTranscript.attemptId !== attempt.id ||
        attemptsRef.current[role]?.id !== attempt.id
      )
        return
      if (role === 'original') {
        originalConfirmationRevisionRef.current = 0
        invalidateFeedback()
      }
      updateTranscriptState(role, {
        ...currentTranscript,
        status: 'draft_ready',
        machineDraft: data.draft_text,
        workingTranscript: data.draft_text,
        confirmedTranscript: '',
        technicalError: '',
      })
    } catch {
      if (!mountedRef.current || controller.signal.aborted) return
      const currentTranscript = transcriptsRef.current[role]
      if (
        currentTranscript.requestId !== requestId ||
        currentTranscript.attemptId !== attempt.id
      )
        return
      updateTranscriptState(role, {
        ...currentTranscript,
        status: 'technical_error',
        technicalError:
          'No pudimos generar la transcripción. Esto es un problema técnico, no un resultado sobre tu portugués.',
      })
    } finally {
      if (requestRefs.current[role].activeGeneration === requestId) {
        requestRefs.current[role].activeGeneration = null
        requestRefs.current[role].controller = undefined
      }
    }
  }
  function updateWorkingTranscript(role: AttemptRole, value: string) {
    updateTranscriptState(role, {
      ...transcriptsRef.current[role],
      workingTranscript: value,
      technicalError: '',
    })
  }
  function confirmTranscript(role: AttemptRole) {
    const currentTranscript = transcriptsRef.current[role]
    const reviewed = currentTranscript.workingTranscript.trim()
    if (!reviewed) {
      updateTranscriptState(role, {
        ...currentTranscript,
        technicalError: 'Escribe el texto revisado antes de confirmar.',
      })
      return
    }
    const originalChanged =
      role === 'original' &&
      reviewed !== transcriptsRef.current.original.confirmedTranscript
    if (originalChanged) {
      originalConfirmationRevisionRef.current += 1
      invalidateFeedback()
    }
    updateTranscriptState(role, {
      ...currentTranscript,
      status: 'confirmed',
      confirmedTranscript: reviewed,
      technicalError: '',
    })
  }
  function formatDuration(seconds: number) {
    return `${seconds.toFixed(1)} seconds`
  }
  function restart() {
    if (
      window.confirm(
        '¿Reiniciar esta práctica y borrar el estado de esta sesión?'
      )
    ) {
      setResponses({})
      setCurrentStepIndex(0)
      setChoiceWarning(false)
      setRecordingWarning(false)
      setWrittenSelected(false)
      setWrittenPractice('')
      clearRecordingAttempts()
      abortModelAudioRequest()
      clearModelAudioUrl()
      originalConfirmationRevisionRef.current = 0
      latestRetrySequenceRef.current = 0
      invalidateFeedback()
      setShowSessionClosure(false)
    }
  }
  function updateStepResponse(stepId: string, response: StepResponses[string]) {
    setResponses((current) => ({
      ...current,
      [stepId]: { ...(current[stepId] ?? {}), ...response },
    }))
  }
  function showStaticSelfCheck() {
    setFeedbackState({
      ...createEmptyFeedbackState(),
      status: 'static_self_check',
      technicalError:
        'No podemos verificar con seguridad qué dijiste. La transcripción es una ayuda opcional, no una evaluación.\n\nEscucha tu grabación y comprueba si incluiste:\n\nsaludo, nombre, Gosto de..., E você?',
    })
  }

  if (loading)
    return (
      <div role="status" className="rounded-lg border p-4 text-sm">
        Loading APR Day 9 lesson…
      </div>
    )
  if (error)
    return (
      <div
        role="alert"
        className="border-destructive/30 bg-destructive/10 text-destructive rounded-lg border p-4 text-sm"
      >
        {error}
      </div>
    )
  if (!manifest) return null
  const currentStep = manifest.steps[currentStepIndex]
  const currentResponse = responses[currentStep.step_id] ?? {}
  const selectedOption =
    currentStep.step_type === 'single_choice'
      ? currentStep.options.find(
          (option) => option.option_id === currentResponse.choice
        )
      : undefined
  const writtenReady = writtenSelected && writtenPractice.trim().length > 0
  function continueForward() {
    if (currentStep.step_type === 'single_choice' && !currentResponse.choice) {
      setChoiceWarning(true)
      return
    }
    if (
      currentStep.step_type === 'recording' &&
      !recordingAttempts.original &&
      !writtenReady
    ) {
      setRecordingWarning(true)
      return
    }
    setChoiceWarning(false)
    setRecordingWarning(false)
    if (currentStepIndex === (manifest?.steps.length ?? 0) - 1) {
      setShowSessionClosure(true)
      return
    }
    setCurrentStepIndex((index) => index + 1)
  }
  function buildSessionSummary(): AprSessionSummary {
    const feedbackIsCurrent =
      feedback.status === 'ready' &&
      feedback.sourceConfirmationRevision ===
        originalConfirmationRevisionRef.current &&
      Boolean(transcripts.original.confirmedTranscript) &&
      originalConfirmationRevisionRef.current > 0
    return {
      originalRecording: recordingAttempts.original
        ? 'Captured'
        : 'Not captured',
      originalTranscript:
        transcripts.original.confirmedTranscript &&
        originalConfirmationRevisionRef.current > 0
          ? 'Confirmed'
          : 'Not confirmed',
      latestRetry: recordingAttempts.latestRetry ? 'Captured' : 'Not captured',
      technicalModelAudio:
        modelAudio.status === 'ready'
          ? 'Generated'
          : modelAudio.status === 'technical_error'
            ? 'Technical issue'
            : 'Not generated',
      controlledTechnicalFeedback: feedbackIsCurrent
        ? 'Ready'
        : feedback.status === 'technical_error'
          ? 'Technical issue'
          : 'Not requested',
      postFeedbackRetry: !feedbackIsCurrent
        ? 'Not applicable'
        : feedback.postFeedbackRetryCaptured
          ? 'Captured'
          : 'Not captured',
      writtenPractice: writtenReady ? 'Provided' : 'Not provided',
    }
  }
  if (showSessionClosure)
    return (
      <AprSessionClosure
        headingRef={headingRef}
        summary={buildSessionSummary()}
        closure={manifest.session_closure}
        onBackToReflection={() => setShowSessionClosure(false)}
        onRestart={restart}
        onExit={() => router.push('/apr/primeira-conexao')}
      />
    )

  return (
    <Card>
      <CardHeader>
        <Badge className="w-fit" variant="secondary">
          {manifest.content_status}
        </Badge>
        <CardTitle className="text-2xl sm:text-3xl">{manifest.title}</CardTitle>
        <CardDescription>
          {manifest.internal_title} · Version {manifest.version}
        </CardDescription>
      </CardHeader>
      <CardContent className="space-y-6">
        <section
          aria-label="Lesson authorization"
          className="rounded-lg border p-4 text-sm"
        >
          <p>{manifest.authorization_notice}</p>
          <p>No autorizado para piloto ni lanzamiento público.</p>
        </section>
        <div
          role="status"
          aria-live="polite"
          className="rounded-lg border p-3 text-sm"
        >
          Paso {currentStepIndex + 1} de {manifest.current_step_count}.
        </div>
        <article className="space-y-4">
          <h2
            ref={headingRef}
            tabIndex={-1}
            className="font-heading text-xl font-semibold"
          >
            {currentStep.title}
          </h2>
          <div className="text-muted-foreground space-y-3">
            {paragraphs(currentStep.body)}
          </div>
          {currentStep.step_type === 'information' && (
            <div className="space-y-4">
              {currentStep.model_script && (
                <p
                  className="rounded-lg border p-3 text-lg font-medium"
                  lang="pt-BR"
                >
                  {currentStep.model_script}
                </p>
              )}
              {currentStep.controlled_transcript && (
                <details>
                  <summary className="cursor-pointer font-medium">
                    {currentStep.transcript_label}
                  </summary>
                  <p className="mt-2" lang="pt-BR">
                    {currentStep.controlled_transcript}
                  </p>
                </details>
              )}
              {currentStep.optional_translation && (
                <details>
                  <summary className="cursor-pointer font-medium">
                    {currentStep.translation_label}
                  </summary>
                  <p className="mt-2">{currentStep.optional_translation}</p>
                </details>
              )}
              {[
                currentStep.spanish_bridge,
                currentStep.pronunciation_guidance,
                currentStep.pragmatic_guidance,
              ]
                .filter(Boolean)
                .map(
                  (block) =>
                    block && (
                      <section
                        key={block.content_id}
                        className="space-y-2 rounded-lg border p-4"
                      >
                        <h3 className="font-medium">{block.heading}</h3>
                        {paragraphs(block.body)}
                      </section>
                    )
                )}
              {currentStep.model_audio && (
                <>
                  <p className="text-sm font-medium">
                    {currentStep.model_audio.disclosure}
                  </p>
                  <AprModelAudio
                    state={modelAudio}
                    modelAudioId={currentStep.model_audio.model_audio_id}
                    intendedLanguage={currentStep.model_audio.language}
                    isRequired={currentStep.model_audio.required}
                    onGenerate={() =>
                      requestModelAudio(currentStep.model_audio!)
                    }
                  />
                </>
              )}
            </div>
          )}
          {currentStep.step_type === 'single_choice' && (
            <fieldset className="space-y-3">
              <legend className="font-medium">
                {currentStep.prompt_label}
              </legend>
              {currentStep.options.map((option) => (
                <label
                  key={option.option_id}
                  className="focus-within:ring-ring flex cursor-pointer gap-3 rounded-lg border p-3 focus-within:ring-2"
                >
                  <input
                    type="radio"
                    name={currentStep.step_id}
                    value={option.option_id}
                    checked={currentResponse.choice === option.option_id}
                    onChange={() => {
                      setChoiceWarning(false)
                      updateStepResponse(currentStep.step_id, {
                        choice: option.option_id,
                      })
                    }}
                  />
                  <span>{option.label}</span>
                </label>
              ))}
              {choiceWarning && (
                <p role="alert" className="text-destructive text-sm">
                  {currentStep.required_warning}
                </p>
              )}
              {selectedOption && (
                <p className="rounded-lg border p-3 text-sm" aria-live="polite">
                  {selectedOption.feedback}
                </p>
              )}
            </fieldset>
          )}
          {currentStep.step_type === 'recording' && (
            <div className="space-y-4">
              <p
                className="rounded-lg border p-3 text-lg font-medium"
                lang="pt-BR"
              >
                {currentStep.production_frame}
              </p>
              <p>{currentStep.privacy_notice}</p>
              <p>{currentStep.practice_notice}</p>
              <AprAudioRecorder
                maxSeconds={currentStep.max_seconds}
                hasOriginalAttempt={Boolean(recordingAttempts.original)}
                onCapture={handleAudioCapture}
              />
              <section className="space-y-3 rounded-lg border p-4">
                <h3 className="font-medium">
                  {currentStep.written_alternative.label}
                </h3>
                {paragraphs(currentStep.written_alternative.notice)}
                <Button
                  type="button"
                  variant="outline"
                  onClick={() => setWrittenSelected(true)}
                >
                  {currentStep.written_alternative.label}
                </Button>
                {writtenSelected && (
                  <>
                    <label
                      className="block font-medium"
                      htmlFor="apr-written-practice"
                    >
                      {currentStep.written_alternative.prompt}
                    </label>
                    <p lang="pt-BR">{currentStep.written_alternative.frame}</p>
                    <textarea
                      id="apr-written-practice"
                      className="border-input bg-background ring-offset-background focus-visible:ring-ring min-h-28 w-full rounded-md border px-3 py-2 text-sm focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:outline-none"
                      maxLength={currentStep.written_alternative.max_characters}
                      value={writtenPractice}
                      onChange={(event) =>
                        setWrittenPractice(
                          event.target.value.slice(
                            0,
                            currentStep.written_alternative.max_characters
                          )
                        )
                      }
                    />
                  </>
                )}
              </section>
              {recordingWarning && (
                <p role="alert" className="text-destructive text-sm">
                  Graba un Original o completa la práctica escrita antes de
                  continuar.
                </p>
              )}
              {recordingAttempts.original && (
                <section
                  aria-label="Original attempt"
                  className="space-y-2 rounded-lg border p-4"
                >
                  <h3 className="font-medium">Original protegido</h3>
                  <audio
                    controls
                    preload="metadata"
                    src={recordingAttempts.original.objectUrl}
                    aria-label="Original attempt playback"
                  />
                  <p className="text-muted-foreground text-sm">
                    Formato: {recordingAttempts.original.mimeType}. Duración
                    aproximada:{' '}
                    {formatDuration(recordingAttempts.original.durationSeconds)}
                    .
                  </p>
                  <AprTranscriptDraft
                    attemptLabel="Original"
                    state={transcripts.original}
                    onGenerate={() => requestTranscriptDraft('original')}
                    onWorkingChange={(value) =>
                      updateWorkingTranscript('original', value)
                    }
                    onConfirm={() => confirmTranscript('original')}
                  />
                  <AprFeedbackRetry
                    state={
                      transcripts.original.confirmedTranscript
                        ? {
                            ...(feedback.sourceConfirmationRevision ===
                            originalConfirmationRevisionRef.current
                              ? feedback
                              : createEmptyFeedbackState()),
                            status:
                              feedback.sourceConfirmationRevision ===
                                originalConfirmationRevisionRef.current &&
                              feedback.status !== 'ineligible'
                                ? feedback.status
                                : 'not_requested',
                          }
                        : feedback.status === 'static_self_check'
                          ? feedback
                          : createEmptyFeedbackState()
                    }
                    isEligible={Boolean(
                      transcripts.original.confirmedTranscript
                    )}
                    hasOriginal={Boolean(recordingAttempts.original)}
                    onStaticSelfCheck={showStaticSelfCheck}
                    onGenerate={() => requestFeedbackDraft(currentStep)}
                  />
                  {feedback.status === 'static_self_check' && (
                    <div className="rounded-lg border p-3 text-sm whitespace-pre-line">
                      {feedback.technicalError}
                    </div>
                  )}
                  <p className="rounded-lg border p-3 text-sm whitespace-pre-line">
                    {currentStep.retry_instruction}
                  </p>
                </section>
              )}
              {recordingAttempts.latestRetry && (
                <section
                  aria-label="Latest retry"
                  className="space-y-2 rounded-lg border p-4"
                >
                  <h3 className="font-medium">Latest retry separado</h3>
                  <audio
                    controls
                    preload="metadata"
                    src={recordingAttempts.latestRetry.objectUrl}
                    aria-label="Latest retry playback"
                  />
                  <AprTranscriptDraft
                    attemptLabel="Latest retry"
                    state={transcripts.latestRetry}
                    onGenerate={() => requestTranscriptDraft('latestRetry')}
                    onWorkingChange={(value) =>
                      updateWorkingTranscript('latestRetry', value)
                    }
                    onConfirm={() => confirmTranscript('latestRetry')}
                  />
                </section>
              )}
            </div>
          )}
          {currentStep.step_type === 'reflection' && (
            <div className="space-y-2">
              <label
                htmlFor={`${currentStep.step_id}-reflection`}
                className="font-medium whitespace-pre-line"
              >
                {currentStep.prompt}
              </label>
              <p className="text-muted-foreground whitespace-pre-line">
                {currentStep.body}
              </p>
              <textarea
                id={`${currentStep.step_id}-reflection`}
                className="border-input bg-background ring-offset-background focus-visible:ring-ring min-h-32 w-full rounded-md border px-3 py-2 text-sm focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:outline-none"
                placeholder={currentStep.placeholder ?? undefined}
                maxLength={currentStep.max_characters}
                value={currentResponse.reflection ?? ''}
                onChange={(event) =>
                  updateStepResponse(currentStep.step_id, {
                    reflection: event.target.value.slice(
                      0,
                      currentStep.max_characters
                    ),
                  })
                }
              />
              <p className="text-muted-foreground text-sm">
                {(currentResponse.reflection ?? '').length} de{' '}
                {currentStep.max_characters} caracteres.
              </p>
            </div>
          )}
        </article>
        <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
          <Button type="button" variant="outline" onClick={restart}>
            Reiniciar
          </Button>
          <div className="flex gap-3">
            <Button
              type="button"
              variant="outline"
              disabled={currentStepIndex === 0}
              onClick={() =>
                setCurrentStepIndex((index) => Math.max(0, index - 1))
              }
            >
              Atrás
            </Button>
            <Button type="button" onClick={continueForward}>
              Continuar
            </Button>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}

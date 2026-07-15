'use client'

import { useEffect, useRef, useState } from 'react'
import {
  AprAudioRecorder,
  type AprCapturedAudio,
} from '@/components/apr/AprAudioRecorder'
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
}
type AprSingleChoiceOption = {
  option_id: string
  label: string
  feedback: string
}
type AprSingleChoiceStep = AprBaseStep & {
  step_type: 'single_choice'
  options: AprSingleChoiceOption[]
}
type AprRecordingStep = AprBaseStep & {
  step_type: 'recording'
  prompt: string
  max_seconds: number
  allow_retry: boolean
  preserve_original: boolean
  storage_status: 'session-only'
  transcription_language: 'pt'
  transcription_mode: 'on-demand'
  requires_learner_confirmation: boolean
  transcript_storage_status: 'session-only'
  transcript_authorized_as_evidence: boolean
  model_audio_id: string
  model_audio_mode: 'on-demand'
  model_audio_language: 'pt-BR'
  model_audio_source: 'generated-technical-placeholder'
  model_audio_storage_status: 'session-only'
  model_audio_authorized_as_final_content: boolean
  model_audio_required: boolean
}
type AprReflectionStep = AprBaseStep & {
  step_type: 'reflection'
  prompt: string
  placeholder?: string | null
  max_characters: number
}
type AprLessonStep =
  | (AprBaseStep & { step_type: 'orientation' | 'information' })
  | AprSingleChoiceStep
  | AprRecordingStep
  | AprReflectionStep
type AprLessonManifest = {
  lesson_id: string
  module_id: string
  version: string
  title: string
  internal_title: string
  content_status: string
  authorized_for_pilot: boolean
  authorized_for_public_release: boolean
  estimated_minutes: number
  current_step_count: number
  steps: AprLessonStep[]
}
type StepResponses = Record<string, { choice?: string; reflection?: string }>
type AprRecordingAttempt = AprCapturedAudio & { id: number; objectUrl: string }
type AttemptRole = 'original' | 'latestRetry'

export function AprLessonPlayer({ endpoint }: { endpoint: string }) {
  const [manifest, setManifest] = useState<AprLessonManifest | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [currentStepIndex, setCurrentStepIndex] = useState(0)
  const [responses, setResponses] = useState<StepResponses>({})
  const [choiceWarning, setChoiceWarning] = useState(false)
  const [recordingWarning, setRecordingWarning] = useState(false)
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
  }>({
    generation: 0,
  })
  const [transcripts, setTranscripts] = useState<{
    original: AprTranscriptState
    latestRetry: AprTranscriptState
  }>(() => ({
    original: createEmptyTranscriptState(),
    latestRetry: createEmptyTranscriptState(),
  }))
  const [complete, setComplete] = useState(false)
  const headingRef = useRef<HTMLHeadingElement>(null)
  const attemptsRef = useRef(recordingAttempts)
  const mountedRef = useRef(true)
  const nextAttemptIdRef = useRef(0)
  const requestRefs = useRef<{
    original: {
      generation: number
      activeGeneration: number | null
      controller?: AbortController
    }
    latestRetry: {
      generation: number
      activeGeneration: number | null
      controller?: AbortController
    }
  }>({
    original: { generation: 0, activeGeneration: null },
    latestRetry: { generation: 0, activeGeneration: null },
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
  }, [currentStepIndex, complete])

  useEffect(() => {
    mountedRef.current = true
    return () => {
      mountedRef.current = false
      abortTranscriptRequest('original')
      abortTranscriptRequest('latestRetry')
      abortModelAudioRequest()
      if (modelAudioRef.current.objectUrl)
        URL.revokeObjectURL(modelAudioRef.current.objectUrl)
      modelAudioRef.current = createEmptyModelAudioState()
      const current = attemptsRef.current
      if (current.original) URL.revokeObjectURL(current.original.objectUrl)
      if (current.latestRetry)
        URL.revokeObjectURL(current.latestRetry.objectUrl)
      attemptsRef.current = {}
    }
  }, [])

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
        res.headers.get('X-APR-Audio-Status') ??
        'generated-technical-placeholder',
    }
  }

  async function requestModelAudio(step: AprRecordingStep) {
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
        body: JSON.stringify({
          model_audio_id: step.model_audio_id,
        }),
        signal: controller.signal,
      })
      if (!res.ok) throw new Error('technical model-audio failure')
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
      if (!mountedRef.current || controller.signal.aborted) return
      if (modelAudioRequestRef.current.generation !== generation) return
      setModelAudioState({
        ...modelAudioRef.current,
        status: 'technical_error',
        technicalError:
          'APR could not generate technical model audio. This is a technical audio issue, not a language result.',
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

  function resetTranscripts() {
    setTranscripts({
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
      setTranscripts((t) => ({
        ...t,
        latestRetry: createEmptyTranscriptState(),
      }))
    }
    if (replacedRetry) URL.revokeObjectURL(replacedRetry.objectUrl)

    attemptsRef.current = next
    setRecordingWarning(false)
    setRecordingAttempts(next)
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
    setTranscripts((t) => ({
      ...t,
      [role]: {
        ...t[role],
        status: 'requesting',
        requestId,
        attemptId: attempt.id,
        technicalError: '',
      },
    }))
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
      if (!res.ok) throw new Error('technical transcription failure')
      const data = (await res.json()) as { draft_text: string }
      if (!mountedRef.current || controller.signal.aborted) return
      setTranscripts((t) => {
        if (
          t[role].requestId !== requestId ||
          t[role].attemptId !== attempt.id ||
          attemptsRef.current[role]?.id !== attempt.id
        )
          return t
        return {
          ...t,
          [role]: {
            ...t[role],
            status: 'draft_ready',
            machineDraft: data.draft_text,
            workingTranscript: data.draft_text,
            confirmedTranscript: '',
            technicalError: '',
          },
        }
      })
    } catch {
      if (!mountedRef.current || controller.signal.aborted) return
      setTranscripts((t) =>
        t[role].requestId !== requestId || t[role].attemptId !== attempt.id
          ? t
          : {
              ...t,
              [role]: {
                ...t[role],
                status: 'technical_error',
                technicalError:
                  'APR could not generate a transcript draft. This is a technical transcription issue, not a language result.',
              },
            }
      )
    } finally {
      if (requestRefs.current[role].activeGeneration === requestId) {
        requestRefs.current[role].activeGeneration = null
        requestRefs.current[role].controller = undefined
      }
    }
  }

  function updateWorkingTranscript(role: AttemptRole, value: string) {
    setTranscripts((t) => ({
      ...t,
      [role]: { ...t[role], workingTranscript: value, technicalError: '' },
    }))
  }
  function confirmTranscript(role: AttemptRole) {
    setTranscripts((t) => {
      const reviewed = t[role].workingTranscript.trim()
      return reviewed
        ? {
            ...t,
            [role]: {
              ...t[role],
              status: 'confirmed',
              confirmedTranscript: reviewed,
              technicalError: '',
            },
          }
        : {
            ...t,
            [role]: {
              ...t[role],
              technicalError: 'Enter a reviewed transcript before confirming.',
            },
          }
    })
  }
  function formatDuration(seconds: number) {
    return `${seconds.toFixed(1)} seconds`
  }
  function restart() {
    if (
      window.confirm(
        'Restart this technical placeholder lesson and clear current session responses?'
      )
    ) {
      setResponses({})
      setCurrentStepIndex(0)
      setChoiceWarning(false)
      setRecordingWarning(false)
      clearRecordingAttempts()
      abortModelAudioRequest()
      clearModelAudioUrl()
      setComplete(false)
    }
  }

  if (loading)
    return (
      <div role="status" className="rounded-lg border p-4 text-sm">
        Loading APR technical placeholder lesson…
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
  function updateStepResponse(stepId: string, response: StepResponses[string]) {
    setResponses((current) => ({
      ...current,
      [stepId]: { ...(current[stepId] ?? {}), ...response },
    }))
  }
  function continueForward() {
    if (currentStep.step_type === 'single_choice' && !currentResponse.choice) {
      setChoiceWarning(true)
      return
    }
    if (currentStep.step_type === 'recording' && !recordingAttempts.original) {
      setRecordingWarning(true)
      return
    }
    setChoiceWarning(false)
    setRecordingWarning(false)
    if (currentStepIndex === (manifest?.steps.length ?? 0) - 1) {
      setComplete(true)
      return
    }
    setCurrentStepIndex((index) => index + 1)
  }

  if (complete)
    return (
      <Card>
        <CardHeader>
          <Badge className="w-fit" variant="secondary">
            Technical completion only
          </Badge>
          <CardTitle ref={headingRef} tabIndex={-1} className="text-2xl">
            APR lesson-player shell completed
          </CardTitle>
          <CardDescription>
            This technical completion is not academic Lesson completion.
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <p>
            The shell reached the end of the placeholder manifest. No learning
            rewards, proficiency claims, progress credit, Entry Evidence, or
            Capability Observation were created.
          </p>
          <Button type="button" variant="outline" onClick={restart}>
            Restart
          </Button>
        </CardContent>
      </Card>
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
          <p>Technical placeholder lesson. Approved lesson content pending.</p>
          <p>
            This interaction tests the APR lesson player, not Portuguese
            capability.
          </p>
          <p>Not authorized for pilot or public release.</p>
        </section>
        <div
          role="status"
          aria-live="polite"
          className="rounded-lg border p-3 text-sm"
        >
          Step {currentStepIndex + 1} of {manifest.current_step_count}.
        </div>
        <article className="space-y-4">
          <h2
            ref={headingRef}
            tabIndex={-1}
            className="font-heading text-xl font-semibold"
          >
            {currentStep.title}
          </h2>
          <p className="text-muted-foreground">{currentStep.body}</p>
          {currentStep.step_type === 'single_choice' && (
            <fieldset className="space-y-3">
              <legend className="font-medium">
                Choose one interface-testing option.
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
                  Select one interface-testing option before continuing.
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
              <p className="rounded-lg border p-3 text-sm">
                {currentStep.prompt}
              </p>
              <AprModelAudio
                state={modelAudio}
                modelAudioId={currentStep.model_audio_id}
                intendedLanguage={currentStep.model_audio_language}
                isRequired={currentStep.model_audio_required}
                onGenerate={() => requestModelAudio(currentStep)}
              />
              <AprAudioRecorder
                maxSeconds={currentStep.max_seconds}
                hasOriginalAttempt={Boolean(recordingAttempts.original)}
                onCapture={handleAudioCapture}
              />
              {recordingWarning && (
                <p role="alert" className="text-destructive text-sm">
                  Create one technical microphone recording before continuing.
                </p>
              )}
              {recordingAttempts.original && (
                <section
                  aria-label="Original attempt"
                  className="space-y-2 rounded-lg border p-4"
                >
                  <h3 className="font-medium">Original attempt</h3>
                  <audio
                    controls
                    preload="metadata"
                    src={recordingAttempts.original.objectUrl}
                    aria-label="Original attempt playback"
                  />
                  <p className="text-muted-foreground text-sm">
                    Technical format: {recordingAttempts.original.mimeType}.
                    Approximate duration:{' '}
                    {formatDuration(recordingAttempts.original.durationSeconds)}
                    .
                  </p>
                  <p className="text-muted-foreground text-sm">
                    This attempt remains session-only and is not uploaded unless
                    you explicitly request a transcript draft. It is not scored
                    or saved to the APR backend.
                  </p>
                  <AprTranscriptDraft
                    attemptLabel="Original attempt"
                    state={transcripts.original}
                    onGenerate={() => requestTranscriptDraft('original')}
                    onWorkingChange={(value) =>
                      updateWorkingTranscript('original', value)
                    }
                    onConfirm={() => confirmTranscript('original')}
                  />
                </section>
              )}
              {recordingAttempts.latestRetry && (
                <section
                  aria-label="Latest retry"
                  className="space-y-2 rounded-lg border p-4"
                >
                  <h3 className="font-medium">Latest retry</h3>
                  <audio
                    controls
                    preload="metadata"
                    src={recordingAttempts.latestRetry.objectUrl}
                    aria-label="Latest retry playback"
                  />
                  <p className="text-muted-foreground text-sm">
                    Technical format: {recordingAttempts.latestRetry.mimeType}.
                    Approximate duration:{' '}
                    {formatDuration(
                      recordingAttempts.latestRetry.durationSeconds
                    )}
                    .
                  </p>
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
                className="font-medium"
              >
                {currentStep.prompt}
              </label>
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
                {(currentResponse.reflection ?? '').length} of{' '}
                {currentStep.max_characters} characters.
              </p>
            </div>
          )}
        </article>
        <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
          <Button type="button" variant="outline" onClick={restart}>
            Restart
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
              Back
            </Button>
            <Button type="button" onClick={continueForward}>
              Continue
            </Button>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}

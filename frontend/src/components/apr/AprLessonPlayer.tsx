'use client'

import { useEffect, useRef, useState } from 'react'
import { apiFetch } from '@/lib/api'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/components/ui/card'

const APR_DISABLED_MESSAGE =
  'The APR technical proof of concept is disabled in this environment.'

type AprBaseStep = {
  step_id: string
  step_type: 'orientation' | 'information' | 'single_choice' | 'reflection'
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

type AprReflectionStep = AprBaseStep & {
  step_type: 'reflection'
  prompt: string
  placeholder?: string | null
  max_characters: number
}

type AprLessonStep =
  | (AprBaseStep & { step_type: 'orientation' | 'information' })
  | AprSingleChoiceStep
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

export function AprLessonPlayer({ endpoint }: { endpoint: string }) {
  const [manifest, setManifest] = useState<AprLessonManifest | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [currentStepIndex, setCurrentStepIndex] = useState(0)
  const [responses, setResponses] = useState<StepResponses>({})
  const [choiceWarning, setChoiceWarning] = useState(false)
  const [complete, setComplete] = useState(false)
  const headingRef = useRef<HTMLHeadingElement>(null)

  useEffect(() => {
    let active = true

    async function loadLesson() {
      try {
        const res = await apiFetch(endpoint)
        if (res.status === 404) {
          throw new Error(APR_DISABLED_MESSAGE)
        }
        if (!res.ok) {
          throw new Error(`APR lesson API returned HTTP ${res.status}`)
        }
        const data = (await res.json()) as AprLessonManifest
        if (active) setManifest(data)
      } catch (err) {
        if (!active) return
        if (err instanceof Error && err.message === APR_DISABLED_MESSAGE) {
          setError(APR_DISABLED_MESSAGE)
        } else {
          setError(
            err instanceof Error
              ? `Technical error loading APR lesson player: ${err.message}`
              : 'Technical error loading APR lesson player.'
          )
        }
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

  function restart() {
    if (
      window.confirm(
        'Restart this technical placeholder lesson and clear current session responses?'
      )
    ) {
      setResponses({})
      setCurrentStepIndex(0)
      setChoiceWarning(false)
      setComplete(false)
    }
  }

  if (loading) {
    return (
      <div role="status" className="rounded-lg border p-4 text-sm">
        Loading APR technical placeholder lesson…
      </div>
    )
  }

  if (error) {
    return (
      <div
        role="alert"
        className="border-destructive/30 bg-destructive/10 text-destructive rounded-lg border p-4 text-sm"
      >
        {error}
      </div>
    )
  }

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
    if (!manifest) return
    if (currentStep.step_type === 'single_choice' && !currentResponse.choice) {
      setChoiceWarning(true)
      return
    }
    setChoiceWarning(false)
    if (currentStepIndex === manifest.steps.length - 1) {
      setComplete(true)
      return
    }
    setCurrentStepIndex((index) => index + 1)
  }

  if (complete) {
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
  }

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

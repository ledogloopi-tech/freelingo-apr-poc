import type { RefObject } from 'react'
import { Button } from '@/components/ui/button'
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
} from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'

export type AprSessionSummary = {
  originalRecording: 'Captured' | 'Not captured'
  originalTranscript: 'Confirmed' | 'Not confirmed'
  latestRetry: 'Captured' | 'Not captured'
  technicalModelAudio: 'Generated' | 'Not generated' | 'Technical issue'
  controlledTechnicalFeedback: 'Ready' | 'Not requested' | 'Technical issue'
  postFeedbackRetry: 'Captured' | 'Not captured' | 'Not applicable'
  writtenPractice: 'Provided' | 'Not provided'
}

export type AprSessionClosureContent = {
  content_id: string
  badge: string
  heading: string
  body: string
  primary_action: string
  secondary_action: string
}

type Props = {
  headingRef: RefObject<HTMLHeadingElement | null>
  summary: AprSessionSummary
  closure: AprSessionClosureContent
  onBackToReflection: () => void
  onRestart: () => void
  onExit: () => void
}

const summaryRows: { key: keyof AprSessionSummary; label: string }[] = [
  { key: 'originalRecording', label: 'Original' },
  { key: 'originalTranscript', label: 'Texto confirmado' },
  { key: 'latestRetry', label: 'Latest retry' },
  { key: 'technicalModelAudio', label: 'Audio temporal' },
  { key: 'controlledTechnicalFeedback', label: 'Ayuda controlada' },
  { key: 'postFeedbackRetry', label: 'Retry posterior' },
  { key: 'writtenPractice', label: 'Práctica escrita' },
]

export function AprSessionClosure({
  headingRef,
  summary,
  closure,
  onBackToReflection,
  onRestart,
  onExit,
}: Props) {
  return (
    <Card>
      <CardHeader>
        <Badge className="w-fit" variant="secondary">
          {closure.badge}
        </Badge>
        <h1
          ref={headingRef}
          tabIndex={-1}
          className="font-heading text-2xl font-medium sm:text-3xl"
        >
          {closure.heading}
        </h1>
        <CardDescription className="whitespace-pre-line">
          {closure.body}
        </CardDescription>
      </CardHeader>
      <CardContent className="space-y-6">
        <section
          aria-labelledby="apr-session-summary-heading"
          className="space-y-3"
        >
          <h2
            id="apr-session-summary-heading"
            className="font-heading text-xl font-semibold"
          >
            Resumen técnico de la sesión
          </h2>
          <dl className="grid gap-3 sm:grid-cols-2">
            {summaryRows.map((row) => (
              <div key={row.key} className="rounded-lg border p-3">
                <dt className="text-muted-foreground text-sm">{row.label}</dt>
                <dd className="mt-1 font-medium break-words">
                  {summary[row.key]}
                </dd>
              </div>
            ))}
          </dl>
        </section>
        <p className="text-muted-foreground text-sm">
          Puedes revisar tu reflexión, reiniciar con confirmación o salir al
          módulo APR.
        </p>
        <div className="flex flex-col gap-3 sm:flex-row sm:flex-wrap">
          <Button type="button" variant="outline" onClick={onBackToReflection}>
            Volver a la reflexión
          </Button>
          <Button type="button" variant="outline" onClick={onRestart}>
            {closure.secondary_action}
          </Button>
          <Button type="button" onClick={onExit}>
            {closure.primary_action}
          </Button>
        </div>
      </CardContent>
    </Card>
  )
}

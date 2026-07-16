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
}

type Props = {
  headingRef: RefObject<HTMLHeadingElement | null>
  summary: AprSessionSummary
  onBackToReflection: () => void
  onRestart: () => void
  onExit: () => void
}

const summaryRows: { key: keyof AprSessionSummary; label: string }[] = [
  { key: 'originalRecording', label: 'Original recording' },
  { key: 'originalTranscript', label: 'Original transcript' },
  { key: 'latestRetry', label: 'Latest retry' },
  { key: 'technicalModelAudio', label: 'Technical model audio' },
  {
    key: 'controlledTechnicalFeedback',
    label: 'Controlled technical feedback',
  },
  { key: 'postFeedbackRetry', label: 'Post-feedback retry' },
]

export function AprSessionClosure({
  headingRef,
  summary,
  onBackToReflection,
  onRestart,
  onExit,
}: Props) {
  return (
    <Card>
      <CardHeader>
        <Badge className="w-fit" variant="secondary">
          Session-only technical summary
        </Badge>
        <h1
          ref={headingRef}
          tabIndex={-1}
          className="font-heading text-2xl font-medium sm:text-3xl"
        >
          Technical session ready for review
        </h1>
        <CardDescription>
          You reached the end of this technical prototype. This summary
          describes browser-session activity only. It is not lesson completion,
          Progress, Evidence, a score, or a language result.
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
            Session-only technical summary
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
          Next: review your session, restart the technical flow, or exit to the
          APR module.
        </p>
        <div className="flex flex-col gap-3 sm:flex-row sm:flex-wrap">
          <Button type="button" variant="outline" onClick={onBackToReflection}>
            Back to reflection
          </Button>
          <Button type="button" variant="outline" onClick={onRestart}>
            Restart technical session
          </Button>
          <Button type="button" onClick={onExit}>
            Exit to APR module
          </Button>
        </div>
      </CardContent>
    </Card>
  )
}

import { Button } from '@/components/ui/button'

export type AprFeedbackStatus =
  | 'ineligible'
  | 'not_requested'
  | 'requesting'
  | 'ready'
  | 'technical_error'

export type AprFeedbackResponse = {
  feedback_id: string
  attempt_role: 'original'
  source_confirmation_revision: number
  status: 'technical-placeholder'
  source: 'server-controlled'
  acknowledgement: string
  primary_priority: string
  cue: string
  retry_instruction: string
  uncertainty: string
  requires_retry: boolean
  retry_allowed: boolean
  authorized_as_academic_feedback: boolean
  authorized_as_evidence: boolean
  storage_status: 'session-only'
}

export type AprFeedbackState = {
  status: AprFeedbackStatus
  feedbackId: string
  sourceAttemptRole: 'original'
  sourceConfirmationRevision: number
  response?: AprFeedbackResponse
  technicalError: string
  requestGeneration: number
  retrySequenceSnapshot: number | null
  postFeedbackRetryCaptured: boolean
}

export function createEmptyFeedbackState(): AprFeedbackState {
  return {
    status: 'ineligible',
    feedbackId: '',
    sourceAttemptRole: 'original',
    sourceConfirmationRevision: 0,
    technicalError: '',
    requestGeneration: 0,
    retrySequenceSnapshot: null,
    postFeedbackRetryCaptured: false,
  }
}

type Props = {
  state: AprFeedbackState
  isEligible: boolean
  onGenerate: () => void
}

export function AprFeedbackRetry({ state, isEligible, onGenerate }: Props) {
  if (!isEligible) {
    return (
      <section
        className="space-y-2 rounded-lg border p-4"
        aria-label="APR technical feedback"
      >
        <h3 className="font-medium">Optional technical feedback</h3>
        <p className="text-muted-foreground text-sm">
          Confirm the Original transcript to make optional technical feedback
          available.
        </p>
      </section>
    )
  }

  const isRequesting = state.status === 'requesting'

  return (
    <section
      className="space-y-3 rounded-lg border p-4"
      aria-label="APR technical feedback"
    >
      <h3 className="font-medium">Optional technical feedback</h3>
      {(state.status === 'not_requested' ||
        state.status === 'ineligible' ||
        state.status === 'technical_error') && (
        <Button type="button" onClick={onGenerate} disabled={isRequesting}>
          {state.status === 'technical_error'
            ? 'Try technical feedback again'
            : 'Generate technical feedback'}
        </Button>
      )}
      {isRequesting && (
        <p role="status" aria-live="polite" className="text-sm">
          Generating technical feedback…
        </p>
      )}
      {state.status === 'technical_error' && (
        <p role="alert" className="text-destructive text-sm">
          APR could not load technical feedback. This is a feedback-service
          issue, not a language result.
        </p>
      )}
      {state.status === 'ready' && state.response && (
        <div
          className="space-y-3 rounded-md border p-3 text-sm"
          role="status"
          aria-live="polite"
        >
          <h3 className="font-medium">Controlled technical feedback</h3>
          <p className="font-medium">Session-only technical placeholder</p>
          <p>This feedback does not evaluate your Portuguese.</p>
          <p>
            <span className="font-medium">Acknowledgement: </span>
            {state.response.acknowledgement}
          </p>
          <p>
            <span className="font-medium">Primary priority: </span>
            {state.response.primary_priority}
          </p>
          <p>
            <span className="font-medium">Cue: </span>
            {state.response.cue}
          </p>
          <p>
            <span className="font-medium">Retry instruction: </span>
            {state.response.retry_instruction}
          </p>
          <p>{state.response.uncertainty}</p>
          <p aria-live="polite">
            {state.postFeedbackRetryCaptured
              ? 'Post-feedback retry captured.'
              : 'Waiting for an optional post-feedback retry.'}
          </p>
          {state.postFeedbackRetryCaptured && (
            <p>
              This completes the technical feedback-and-retry flow only. It does
              not indicate improvement or a language result.
            </p>
          )}
        </div>
      )}
    </section>
  )
}

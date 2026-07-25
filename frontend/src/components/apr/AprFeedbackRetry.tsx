import { Button } from '@/components/ui/button'

export type AprFeedbackStatus =
  | 'ineligible'
  | 'not_requested'
  | 'requesting'
  | 'ready'
  | 'technical_error'
  | 'static_self_check'

export type AprFeedbackResponse = {
  feedback_id: string
  feedback_case: string
  attempt_role: 'original'
  source_confirmation_revision: number
  status: 'controlled-instructional-guidance'
  source: 'server-deterministic'
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
  hasOriginal: boolean
  onGenerate: () => void
  onStaticSelfCheck: () => void
}

export function AprFeedbackRetry({
  state,
  isEligible,
  hasOriginal,
  onGenerate,
  onStaticSelfCheck,
}: Props) {
  const isRequesting = state.status === 'requesting'
  if (!isEligible) {
    return (
      <section
        className="space-y-2 rounded-lg border p-4"
        aria-label="Ayuda controlada opcional"
      >
        <h3 className="font-medium">Ayuda controlada opcional</h3>
        <p className="text-muted-foreground text-sm">
          La transcripción es opcional. Solo el texto confirmado por ti puede
          usarse para pedir ayuda controlada.
        </p>
        {hasOriginal && (
          <Button type="button" variant="outline" onClick={onStaticSelfCheck}>
            Usar lista de auto-revisión
          </Button>
        )}
      </section>
    )
  }
  return (
    <section
      className="space-y-3 rounded-lg border p-4"
      aria-label="Ayuda controlada opcional"
    >
      <h3 className="font-medium">Ayuda controlada opcional</h3>
      {(state.status === 'not_requested' ||
        state.status === 'ineligible' ||
        state.status === 'technical_error') && (
        <Button type="button" onClick={onGenerate} disabled={isRequesting}>
          {state.status === 'technical_error'
            ? 'Intentar ayuda de nuevo'
            : 'Pedir ayuda controlada'}
        </Button>
      )}
      {isRequesting && (
        <p role="status" aria-live="polite" className="text-sm">
          Preparando ayuda controlada…
        </p>
      )}
      {state.status === 'technical_error' && (
        <p role="alert" className="text-destructive text-sm">
          La ayuda técnica no estuvo disponible. Esto no es un resultado sobre
          tu portugués. Puedes escuchar tu grabación, usar la lista de cuatro
          movimientos e intentar de nuevo.
        </p>
      )}
      {state.status === 'ready' && state.response && (
        <div
          className="space-y-3 rounded-md border p-3 text-sm"
          aria-live="polite"
        >
          <p className="font-medium">Guía controlada</p>
          {state.response.acknowledgement.split('\n\n').map((paragraph) => (
            <p key={paragraph}>{paragraph}</p>
          ))}
          <p>{state.response.retry_instruction}</p>
          <p>{state.response.uncertainty}</p>
          <p>
            {state.postFeedbackRetryCaptured
              ? 'Latest retry capturado.'
              : 'El retry sigue siendo opcional.'}
          </p>
        </div>
      )}
    </section>
  )
}

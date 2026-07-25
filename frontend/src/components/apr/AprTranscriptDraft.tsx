import { Button } from '@/components/ui/button'

export type AprTranscriptStatus =
  | 'not_requested'
  | 'requesting'
  | 'draft_ready'
  | 'confirmed'
  | 'technical_error'

export type AprTranscriptState = {
  status: AprTranscriptStatus
  machineDraft: string
  workingTranscript: string
  confirmedTranscript: string
  technicalError: string
  requestId: number
  attemptId?: number
}

type Props = {
  attemptLabel: string
  state: AprTranscriptState
  onGenerate: () => void
  onWorkingChange: (value: string) => void
  onConfirm: () => void
}

export function createEmptyTranscriptState(): AprTranscriptState {
  return {
    status: 'not_requested',
    machineDraft: '',
    workingTranscript: '',
    confirmedTranscript: '',
    technicalError: '',
    requestId: 0,
  }
}

export function AprTranscriptDraft({
  attemptLabel,
  state,
  onGenerate,
  onWorkingChange,
  onConfirm,
}: Props) {
  const hasDraft = state.machineDraft.length > 0
  const isRequesting = state.status === 'requesting'
  const textareaId = `${attemptLabel.toLowerCase().replace(/[^a-z0-9]+/g, '-')}-transcript`
  return (
    <section
      className="space-y-3 rounded-lg border p-4"
      aria-label={`${attemptLabel} transcript draft`}
    >
      <h4 className="font-medium">{attemptLabel} transcript review</h4>
      <p className="text-muted-foreground text-sm">
        La transcripción es una ayuda técnica. Puede equivocarse y no evalúa tu
        portugués.
      </p>
      <Button type="button" onClick={onGenerate} disabled={isRequesting}>
        {hasDraft ? 'Generar otra transcripción' : 'Solicitar transcripción'}
      </Button>
      {isRequesting && (
        <p role="status" aria-live="polite" className="text-sm">
          Generando transcripción para {attemptLabel}. La reproducción sigue
          disponible.
        </p>
      )}
      {state.status === 'technical_error' && (
        <div role="alert" className="space-y-2 text-sm">
          <p>
            No pudimos generar la transcripción. Esto es un problema técnico, no
            un resultado sobre tu portugués.
          </p>
          <Button type="button" variant="outline" onClick={onGenerate}>
            Intentar transcripción de nuevo
          </Button>
        </div>
      )}
      {hasDraft && (
        <div className="space-y-3">
          <div className="rounded-md border p-3 text-sm">
            <p className="font-medium">Borrador generado por máquina</p>
            <p>{state.machineDraft}</p>
          </div>
          <p className="text-sm">
            Puedes editar el borrador antes de confirmarlo.
          </p>
          <label htmlFor={textareaId} className="block font-medium">
            Texto revisado
          </label>
          <textarea
            id={textareaId}
            className="border-input bg-background ring-offset-background focus-visible:ring-ring min-h-28 w-full rounded-md border px-3 py-2 text-sm focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:outline-none"
            value={state.workingTranscript}
            disabled={isRequesting}
            onChange={(event) => onWorkingChange(event.target.value)}
          />
          <Button type="button" onClick={onConfirm} disabled={isRequesting}>
            Confirmar este texto
          </Button>
          {state.technicalError && state.status !== 'technical_error' && (
            <p role="alert" className="text-destructive text-sm">
              {state.technicalError}
            </p>
          )}
          {state.confirmedTranscript && (
            <div className="rounded-md border p-3 text-sm">
              <p className="font-medium">Texto confirmado por ti</p>
              <p>{state.confirmedTranscript}</p>
              <p className="text-muted-foreground mt-2">
                Al confirmar, indicas que este texto representa lo que quisiste
                decir. No estás enviando Evidencia ni aceptando una puntuación.
              </p>
            </div>
          )}
        </div>
      )}
    </section>
  )
}

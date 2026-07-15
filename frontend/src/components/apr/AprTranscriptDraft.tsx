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
  const textareaId = `${attemptLabel.toLowerCase().replace(/[^a-z0-9]+/g, '-')}-transcript`
  return (
    <section
      className="space-y-3 rounded-lg border p-4"
      aria-label={`${attemptLabel} transcript draft`}
    >
      <h4 className="font-medium">{attemptLabel} transcript review</h4>
      <p className="text-muted-foreground text-sm">
        When you request a transcript draft, this recording is sent to the
        configured speech-to-text service. APR does not save the audio or
        transcript in its database during this technical proof of concept.
      </p>
      <Button
        type="button"
        onClick={onGenerate}
        disabled={state.status === 'requesting'}
      >
        {hasDraft
          ? 'Generate a new transcript draft'
          : 'Generate transcript draft'}
      </Button>
      {state.status === 'requesting' && (
        <p role="status" aria-live="polite" className="text-sm">
          Generating transcript draft for {attemptLabel}. Audio playback remains
          available.
        </p>
      )}
      {state.status === 'technical_error' && (
        <div role="alert" className="space-y-2 text-sm">
          <p>
            APR could not generate a transcript draft. This is a technical
            transcription issue, not a language result.
          </p>
          <Button type="button" variant="outline" onClick={onGenerate}>
            Retry transcript draft
          </Button>
        </div>
      )}
      {hasDraft && (
        <div className="space-y-3">
          <div className="rounded-md border p-3 text-sm">
            <p className="font-medium">Machine-generated transcript draft</p>
            <p>{state.machineDraft}</p>
          </div>
          <p className="text-sm">
            Review and correct this draft before confirming it.
          </p>
          <label htmlFor={textareaId} className="block font-medium">
            Reviewed transcript correction
          </label>
          <textarea
            id={textareaId}
            className="border-input bg-background ring-offset-background focus-visible:ring-ring min-h-28 w-full rounded-md border px-3 py-2 text-sm focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:outline-none"
            value={state.workingTranscript}
            onChange={(event) => onWorkingChange(event.target.value)}
          />
          <Button type="button" onClick={onConfirm}>
            Confirm reviewed transcript
          </Button>
          {state.technicalError && state.status !== 'technical_error' && (
            <p role="alert" className="text-destructive text-sm">
              {state.technicalError}
            </p>
          )}
          {state.confirmedTranscript && (
            <div className="rounded-md border p-3 text-sm">
              <p className="font-medium">Learner-confirmed transcript</p>
              <p>{state.confirmedTranscript}</p>
              <p className="text-muted-foreground mt-2">
                This confirmation records what you intended to say. It is not a
                score, pronunciation judgment or academic evidence.
              </p>
            </div>
          )}
        </div>
      )}
    </section>
  )
}

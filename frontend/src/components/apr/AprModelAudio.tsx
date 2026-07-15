import { Button } from '@/components/ui/button'

export type AprModelAudioStatus =
  | 'not_requested'
  | 'requesting'
  | 'ready'
  | 'technical_error'

export type AprModelAudioMetadata = {
  language: string
  status: string
}

export type AprModelAudioState = {
  status: AprModelAudioStatus
  objectUrl: string
  mimeType: string
  byteSize: number
  technicalError: string
  requestGeneration: number
  metadata?: AprModelAudioMetadata
}

export function createEmptyModelAudioState(): AprModelAudioState {
  return {
    status: 'not_requested',
    objectUrl: '',
    mimeType: '',
    byteSize: 0,
    technicalError: '',
    requestGeneration: 0,
  }
}

type Props = {
  state: AprModelAudioState
  modelAudioId: string
  intendedLanguage: string
  isRequired: boolean
  onGenerate: () => void
}

export function AprModelAudio({
  state,
  modelAudioId,
  intendedLanguage,
  isRequired,
  onGenerate,
}: Props) {
  const isRequesting = state.status === 'requesting'
  const hasAudio = state.status === 'ready' && state.objectUrl

  return (
    <section
      className="space-y-3 rounded-lg border p-4"
      aria-labelledby="apr-model-audio-heading"
    >
      <h3 id="apr-model-audio-heading" className="font-medium">
        Technical model audio
      </h3>
      <p className="text-muted-foreground text-sm">
        This is generated technical model audio for the APR proof of concept. It
        is not approved final human-recorded Academy audio, not a pronunciation
        standard, not a pronunciation judgment, and not academic evidence.
      </p>
      <p className="text-muted-foreground text-sm">
        When you request model audio, APR sends only the approved model-audio
        identifier to the APR backend. The backend resolves the controlled
        technical text and uses the configured text-to-speech service. APR does
        not save the generated audio in its database during this proof of
        concept.
      </p>
      <p className="text-muted-foreground text-sm">
        Intended content language: {intendedLanguage}. Generated provider voice
        and accent are temporary and provider-dependent, not verified Brazilian
        Portuguese. Model audio is {isRequired ? 'required' : 'optional'} and
        remains session-only.
      </p>
      <Button type="button" onClick={onGenerate} disabled={isRequesting}>
        {hasAudio
          ? 'Generate a new technical model audio clip'
          : 'Generate technical model audio'}
      </Button>
      {isRequesting && (
        <p role="status" aria-live="polite" className="text-sm">
          Generating technical model audio. Learner recording playback remains
          available.
        </p>
      )}
      {state.status === 'technical_error' && (
        <div role="alert" className="space-y-2 text-sm">
          <p>
            APR could not generate technical model audio. This is a technical
            audio issue, not a language result.
          </p>
          <Button type="button" variant="outline" onClick={onGenerate}>
            Retry technical model audio
          </Button>
        </div>
      )}
      {hasAudio && (
        <div className="space-y-2 rounded-md border p-3 text-sm">
          <p className="font-medium">
            Generated technical model audio playback
          </p>
          <audio
            controls
            preload="metadata"
            src={state.objectUrl}
            aria-label="Technical model audio playback"
          />
          <p>Model-audio id: {modelAudioId}</p>
          <p>Technical status: {state.metadata?.status}</p>
          <p>Intended language: {state.metadata?.language}</p>
          <p>Actual MIME type: {state.mimeType}</p>
          <p>Approximate size: {state.byteSize} bytes.</p>
          <p>
            Generated provider voice/accent is temporary and provider-dependent.
          </p>
        </div>
      )}
    </section>
  )
}

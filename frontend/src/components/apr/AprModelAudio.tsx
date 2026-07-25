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
        Audio temporal de modelo
      </h3>
      <p className="text-muted-foreground text-sm">
        Audio temporal generado para pruebas. No es la grabación final de la
        Academia.
      </p>
      <p className="text-muted-foreground text-sm">
        El audio se solicita solo cuando tú lo pides. El servidor usa el texto
        aprobado; no envías texto libre.
      </p>
      <p className="text-muted-foreground text-sm">
        Idioma del modelo: {intendedLanguage}. El audio es{' '}
        {isRequired ? 'obligatorio' : 'opcional'} y permanece solo durante esta
        sesión.
      </p>
      <Button type="button" onClick={onGenerate} disabled={isRequesting}>
        {hasAudio
          ? 'Generar de nuevo audio temporal'
          : 'Escuchar audio temporal'}
      </Button>
      {isRequesting && (
        <p role="status" aria-live="polite" className="text-sm">
          Generando audio temporal. Puedes continuar si no está disponible.
        </p>
      )}
      {state.status === 'technical_error' && (
        <div role="alert" className="space-y-2 text-sm">
          <p>
            No pudimos generar el audio temporal. Esto es un problema técnico,
            no un resultado sobre tu portugués.
          </p>
          <Button type="button" variant="outline" onClick={onGenerate}>
            Intentar audio temporal de nuevo
          </Button>
        </div>
      )}
      {hasAudio && (
        <div className="space-y-2 rounded-md border p-3 text-sm">
          <p className="font-medium">Reproducción del audio temporal</p>
          <audio
            controls
            preload="metadata"
            src={state.objectUrl}
            aria-label="Reproducción del audio temporal"
          />
          <p>ID de audio: {modelAudioId}</p>
          <p>Estado técnico: {state.metadata?.status}</p>
          <p>Idioma: {state.metadata?.language}</p>
          <p>
            Tipo MIME:{' '}
            {state.mimeType === 'unknown' ? 'Unknown' : state.mimeType}
          </p>
          <p>Tamaño aproximado: {state.byteSize} bytes.</p>
          <p>
            Audio temporal generado para pruebas. No es la grabación final de la
            Academia.
          </p>
        </div>
      )}
    </section>
  )
}

# APR Day 6 Model Audio

## 1. Goal

Day 6 proves a controlled APR-only technical model-audio boundary. A learner can explicitly request generated technical model audio by identifier, play it without autoplay, and continue without scoring or persistence.

## 2. Branch

`codex/apr-day6-model-audio-boundary`

## 3. Fixed model_audio_id

The public lesson manifest exposes only this controlled model-audio identifier:

`APR-R1-RM-01-L01-MODEL-TECH`

The frontend sends only this identifier in the request body. It never sends spoken text, language, voice, provider, or response-format overrides.

## 4. Server-side controlled text

The backend resolves the identifier to this server-controlled technical placeholder sentence:

`Olá. Este é um teste técnico de áudio em português brasileiro.`

The sentence is not exposed as editable lesson content and is not approved lesson prose.

## 5. Why APR does not call generic `/api/tts`

APR uses its own authenticated endpoint so the APR feature flag, fixed identifier, provider-boundary rules, no-store headers, response-size limit, sanitized errors, and non-persistence language stay inside the APR boundary. The generic `/api/tts` route remains separate for FreeLingo tutor behavior.

## 6. APR model-audio endpoint

`POST /api/apr/modules/primeira-conexao/lessons/enter-the-connection/model-audio`

Request JSON contains only:

- `model_audio_id`

Unknown identifiers are rejected before any provider call.

## 7. Provider-boundary reuse

The APR router retrieves `request.app.state.tts_service` and calls the provider-neutral metadata method with the server-controlled text, APR voice configuration when required, and intended content language `pt-BR`. The router does not import vendor SDKs and does not call OpenAI or Kokoro directly.

## 8. Provider language limitations

`pt-BR` describes the intended controlled content language. Current TTS provider methods do not verify Brazilian Portuguese accent quality through an explicit locale control. For providers that infer language from text, the generated voice/accent remains provider-dependent and not approved.

## 9. No silent generic English local voice

For the local provider, APR requires an explicitly configured `APR_TTS_VOICE`. APR does not silently use the generic default local voice. If no APR-compatible voice is configured for local TTS, the endpoint returns a sanitized technical 503 response.

## 10. Human-audio replacement requirement

Day 6 is not final instructional audio. Release 1 still requires approved human-recorded Brazilian Portuguese Academy audio. The generated clip is temporary technical model audio only, not final human audio, not official pronunciation, not academic evidence, and not a score.

## 11. Provider-neutral MIME handling

The provider boundary returns both audio bytes and MIME type. APR returns the provider MIME type as the response `Content-Type`. Current providers may return `audio/mpeg` because they request MP3, but APR does not hardcode a contradictory MIME type.

## 12. Response limit and headers

APR enforces a generated-audio response limit of 5 MB. Empty provider audio and audio larger than 5 MB become sanitized technical failures and are not returned to the browser.

Successful responses include:

- `Content-Type`: provider result MIME type
- `Cache-Control: no-store`
- `X-APR-Audio-Status: generated-technical-placeholder`
- `X-APR-Audio-Language: pt-BR`

`X-APR-Audio-Language` describes intended content language, not verified human accent quality.

## 13. No APR backend persistence

The endpoint returns generated audio bytes directly. It does not write model audio, text, progress, study-plan state, chat history, transcript state, evidence, files, object storage, or database rows. No migration was added.

## 14. Model-audio state

The lesson player owns session-only model-audio state separately from learner recordings and transcripts. State includes status, object URL, MIME type, byte size, technical error, request generation, and response metadata.

## 15. Object URL lifecycle

The browser creates an object URL only after an explicit successful request. Replaced model-audio URLs are revoked. Confirmed Restart and unmount abort in-flight requests and revoke retained model-audio URLs. Cancelled Restart preserves model audio. Learner audio URLs are not revoked by model-audio failures.

## 16. Stale-request protection

The frontend uses `AbortController` plus request-generation checks. Responses after Restart, unmount, or newer requests are ignored.

## 17. Continue behavior

Continue on the recording step remains gated only by the Original learner recording. Model-audio generation and playback are optional and never create academic completion.

## 18. Accessibility

The model-audio UI uses semantic headings, real buttons, status and alert regions, a labeled audio control, and no autoplay.

## 19. Systems deliberately not used

Day 6 deliberately does not use final human audio, final Lesson 1 content, pronunciation scoring, learner/model comparison, transcript scoring, grammar correction, AI feedback, Professor Gabriel, LLM prompts, CEFR classification, fluency judgment, evidence records, Entry Evidence, Capability Observations, model-audio persistence, transcript persistence, audio persistence, database migrations, progress persistence, XP, streaks, grades, badges, missions, localStorage, IndexedDB, subscriptions, billing, public deployment, or generic `/api/tts` from the APR frontend.

## 20. Known limitations

Live generation depends on the configured TTS provider and configured APR voice. Generated voice/accent is provider-dependent and not approved Brazilian Portuguese human instruction. State remains session-only and may be lost on reload.

## 21. Day 7 readiness

READY WITH CONSTRAINTS

Day 7 can build controlled feedback/retry behavior only if it preserves Day 4 original/retry recording separation, Day 5 transcript separation, Day 6 model-audio separation, explicit learner control, no persistence, and non-scoring boundaries.

# APR Day 5 Transcript Confirmation

## 1. Goal

Add on-demand speech-to-text draft generation and learner transcript confirmation to the APR technical-placeholder lesson without scoring, persistence, academic evidence, final curriculum, or AI feedback.

## 2. Branch

`codex/apr-day5-transcript-confirmation`

## 3. Why APR does not call the generic `/api/stt` route directly

APR uses its own authenticated endpoint so the APR feature flag, Portuguese language requirement, typed APR response, upload boundaries, and non-evidence language stay inside the APR boundary. The generic route remains available for FreeLingo behavior, but the APR frontend does not call it.

## 4. APR transcription endpoint

`POST /api/apr/modules/primeira-conexao/lessons/enter-the-connection/transcription-drafts`

Multipart form fields:

- `audio`
- `attempt_role`, limited to `original` or `latest_retry`

## 5. Portuguese language enforcement

The endpoint calls the configured STT service with `language="pt"`. It does not use the service default of English.

## 6. Existing STT provider reuse

APR retrieves `request.app.state.stt_service` and calls its `transcribe` method. It does not create a new Whisper, OpenAI, or APR-specific provider implementation.

## 7. Upload limits and MIME handling

The POC limit is 10 MB. MIME validation normalizes codec parameters before checking the type. Accepted normalized types are:

- `audio/webm`
- `audio/mp4`
- `audio/wav`
- `audio/mpeg`
- `audio/ogg`
- `application/octet-stream` as the honest unknown-format fallback for browsers that do not report a known audio type. APR uses `.bin` filenames for this fallback and passes `application/octet-stream` unchanged; provider support for unknown audio remains constrained.

## 8. Temporary audio transmission

When the learner requests a transcript draft, the selected recording is transmitted to the configured speech-to-text service for that request. The UI does not claim that audio remains only in the browser after transcription is requested.

## 9. No APR backend persistence

The endpoint reads at most the 10 MB limit plus one byte before deciding whether to reject the upload, then passes only bounded valid audio to STT. It does not write audio or transcript content to the filesystem, database, object storage, chat history, progress, study plan, or evidence records. No migration was added. The Day 4 recording-upload path has no APR route; requests to it receive the framework default 404.

## 10. Privacy-safe logging

Existing STT implementations now log transcript character counts rather than raw transcript text. Audio bytes, learner identity, and learner-confirmed corrections are not logged by the APR flow.

## 11. Machine-draft state

The lesson player stores the exact machine-generated draft separately in React session state for each attempt role.

## 12. Learner working transcript

The editable working transcript starts as a copy of the machine draft. Learner edits do not mutate the stored machine draft.

## 13. Learner-confirmed transcript

The learner confirms explicitly with `Confirm reviewed transcript`. Confirmation stores the reviewed text separately from the machine draft and may be replaced by a later confirmation in the same session. When a later transcript draft succeeds, APR replaces the machine draft and working transcript and clears the stale learner-confirmed transcript.

## 14. Original and retry separation

Original and Latest retry have separate transcript state. Replacing Latest retry clears only retry transcript state. Original audio and Original transcript state remain protected until confirmed Restart or page reload.

## 15. Stale-request protection

The frontend uses `AbortController`, attempt identities, synchronous per-role request ownership refs, and request generations. Rapid duplicate activations for the same attempt role are blocked before React rerenders. Stale responses after retry replacement, Restart, unmount, or a newer request are ignored. The lifecycle effect explicitly restores mounted state during setup so React Strict Mode cleanup/setup cycles do not strand the player as unmounted.

## 16. Technical failure separation

STT failures show: “APR could not generate a transcript draft. This is a technical transcription issue, not a language result.” Failure does not mark the learner wrong.

## 17. Continue behavior

Continue on the recording step remains gated only by the required Original audio recording. Transcript generation and confirmation are not required for technical completion.

## 18. Accessibility

The transcript UI uses semantic headings, labeled textarea controls, real buttons, keyboard-operable interactions, status and alert regions, and no automatic audio playback or automatic submission.

## 19. Tests run

- Backend APR tests were added for the new endpoint, manifest contract, validation, provider boundary, sanitized failures, and no StudyPlan/Progress writes.
- Frontend APR transcript confirmation tests were expanded for explicit request, APR endpoint usage, FormData roles and filenames, no manual multipart header, duplicate-request prevention, machine draft preservation, learner confirmation and reconfirmation, regeneration clearing stale confirmation, original/retry separation, retry replacement, Back/Continue preservation, Restart behavior, stale response handling, Strict Mode behavior, failure language, Continue behavior, and forbidden endpoint checks.

## 20. Tests blocked

Local dependency availability may block full validation in this environment. The APR GitHub workflow remains the expected Python 3.14 and Node 25 validation path.

## 21. Systems deliberately not used

- Pronunciation scoring
- Transcript accuracy scoring
- Semantic scoring
- Grammar correction
- AI-generated feedback
- Professor Gabriel
- LLM prompts
- Model-answer comparison
- CEFR classification
- Fluency judgment
- Evidence records
- Transcript persistence
- Audio persistence
- Database migrations
- Progress persistence
- XP, streaks, grades, badges, missions
- TTS or human model audio
- localStorage or IndexedDB
- Billing or subscriptions

## 22. Known limitations

Transcript and audio state remain session-only and may be lost on reload. The endpoint uses the configured STT provider, so live behavior depends on that provider’s availability and policy. `application/octet-stream` is accepted only as a technical unknown-format fallback.

## 23. Day 6 readiness

READY WITH CONSTRAINTS

Day 5 proves explicit learner-requested STT draft generation and confirmation. Day 6 can address the model-audio provider boundary and controlled TTS playback only if it preserves the same non-scoring, no-persistence, and explicit-control boundaries.

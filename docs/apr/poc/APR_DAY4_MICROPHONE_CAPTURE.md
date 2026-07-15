# APR Day 4 Microphone Capture

## 1. Goal

Add session-only browser microphone capture to the APR technical-placeholder lesson while proving that the first successful recording is preserved as the original attempt and later retries remain separate.

## 2. Branch

`codex/apr-day4-microphone-capture`

## 3. Why FreeLingo VoiceRecorder was not reused directly

The inherited FreeLingo `VoiceRecorder` is tied to speech-to-text submission behavior. Day 4 deliberately avoids STT, TTS, AI, uploads, WebSockets, conversation services, and backend audio storage. APR therefore uses a dedicated `AprAudioRecorder` that captures audio only in the browser and returns the Blob to the APR lesson player.

## 4. Recording-step contract

The APR lesson manifest now uses version `0.2.0-technical-placeholder` and contains five steps: orientation, information, single choice, recording, and reflection.

The typed recording step is `microphone-capture` with:

- `step_type`: `recording`
- `title`: `Microphone capture`
- `required`: `true`
- `max_seconds`: `10`
- `allow_retry`: `true`
- `preserve_original`: `true`
- `storage_status`: `session-only`

The placeholder copy states that the recording is a technical microphone test, not a Portuguese assessment, not academic evidence, not uploaded, and not saved after the browser session ends.

## 5. Browser recording architecture

`AprAudioRecorder` uses the browser `MediaRecorder` API. It never calls APR or FreeLingo network endpoints. The recorder returns a Blob, MIME type, and approximate duration to `AprLessonPlayer`, which owns the session attempt state.

## 6. Supported MIME selection behavior

The recorder checks preferred MIME candidates at runtime with `MediaRecorder.isTypeSupported` when that function exists. The preferred order is:

- `audio/webm;codecs=opus`
- `audio/webm`
- `audio/mp4`

If none are explicitly supported, the recorder uses the browser default `MediaRecorder` constructor. The actual Blob MIME type is stored with the captured attempt.

## 7. Permission behavior

Microphone permission is requested only after the learner activates the Start recording button. No permission request is made while the page loads or when the recording step first renders.

## 8. Original-attempt preservation

The first successful non-empty capture becomes the Original attempt. It remains unchanged for the current lesson session and is never silently replaced by a retry.

## 9. Retry behavior

After an original exists, the learner may record another attempt. The retry is displayed as Latest retry. Later retries replace only the previous Latest retry, and the previous retry object URL is revoked.

## 10. Player-owned session state

`AprLessonPlayer` owns the Original attempt and Latest retry state, including Blob metadata and object URLs. This preserves attempts while the learner moves backward and forward through the lesson.

## 11. Object URL lifecycle

The player creates object URLs for retained attempts. It revokes the replaced retry URL, all retained URLs on confirmed Restart, and all retained URLs when the lesson player unmounts. It does not revoke the original merely because the recording step is temporarily hidden.

## 12. Stream cleanup

The recorder stops all MediaStream tracks after capture, after permission or recording errors, and when the recorder unmounts.

## 13. Continue gating

The recording step is required only as a technical requirement. Continue is blocked until one Original attempt exists, with the message: “Create one technical microphone recording before continuing.” A retry is optional.

## 14. Restart behavior

Restart asks for confirmation. Cancel preserves responses and attempts. Confirmed Restart clears choice responses, reflection text, current position, completion state, Original attempt, Latest retry, and recording object URLs.

## 15. Privacy and non-upload behavior

The UI states: “This recording remains only in this browser session. It is not uploaded, transcribed, scored or saved to the APR backend.” Day 4 does not claim guarantees beyond implemented session-only browser behavior.

## 16. Accessibility behavior

The recording UI uses real buttons, keyboard-operable controls, visible status text, elapsed time, `aria-live` status announcements, and labeled audio controls. Playback controls are not autoplaying.

## 17. Tests run

- Backend focused APR pytest was attempted locally.
- Frontend focused APR Vitest tests were run locally.
- Frontend lint and TypeScript checks were attempted locally.

## 18. Tests blocked

Local backend execution may remain constrained when the environment Python is older than the repository target of Python 3.14. The APR GitHub workflow keeps Python 3.14 focused backend validation.

## 19. Systems deliberately not used

Day 4 deliberately does not use:

- Speech-to-text
- Transcription
- Transcript editing
- Audio upload
- Backend audio storage
- Database audio records
- Evidence records
- Capability Observations
- Pronunciation scoring
- Language scoring
- Grades
- AI feedback
- LLM prompts
- Text-to-speech
- WebSockets
- Conversation endpoints
- LocalStorage
- IndexedDB
- Durable browser persistence
- Database migrations
- Progress persistence
- XP
- Streaks
- Badges
- Missions
- Subscriptions or billing

## 20. Known limitations

Recordings are available only in the current browser session and are lost on reload, browser close, page unload, or confirmed Restart. Browser MIME support varies. Day 4 does not analyze or transcribe the recording.

## 21. Day 5 readiness

READY WITH CONSTRAINTS

APR can now capture session-only browser audio and preserve the original attempt separately from retries. Day 5 can build transcript-draft behavior only if it continues to respect explicit learner confirmation, non-evidence boundaries, and the no-persistence rule until an approved evidence model exists.

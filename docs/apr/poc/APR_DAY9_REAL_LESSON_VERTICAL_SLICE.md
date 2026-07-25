# APR Day 9 Real Lesson Vertical Slice

## Day 9 objective
Replace the technical placeholder lesson at `/apr/primeira-conexao/lessons/enter-the-connection` with the first Founder-approved, real instructional vertical slice for Academia Português Reconectado.

The learner transformation is: “With guided support, the learner begins a first exchange in Brazilian Portuguese by opening contact, sharing one safe and personally true point of reference, and inviting a simple response.”

## Approved content package
- Content package ID: `APR-R1-RM01-L01-D9`
- Version: `1.0`
- Manifest version: `1.0.0-day9-controlled-slice`

## Founder approval boundary
“I approve APR-R1-RM01-L01-D9 — Minimum Controlled Lesson 1 Content Package v1.0 for Day 9 instructional vertical-slice implementation, including its target Portuguese, Spanish Bridge, model and human-audio script, recognition item, spoken prompt, controlled feedback, retry, reflection, accessibility route, five-step mapping, content boundaries, academic nonclaims, and acceptance criteria. This approval authorizes internal Day 9 implementation only. It does not approve the complete Lesson 1, formal Evidence, Progress, Completion, R1A activation, external pilot use, public release, or final audio until the required human recording and reviews are complete.”

## Implementation base and branch
- Base commit: `3909f8372f0681765ef5738ae3b85a698d0a5413`
- Base identity: Day 8 session-closure merge
- Branch: `codex/apr-day9-real-lesson-vertical-slice`

## Manifest identity
- Lesson ID: `APR-R1-RM-01-L01`
- Module ID: `APR-R1-RM-01`
- Content package ID: `APR-R1-RM01-L01-D9`
- Version: `1.0.0-day9-controlled-slice`
- Title: `Enter the Connection`
- Internal title: `Day 9 Controlled Instructional Vertical Slice`
- Content status: `approved-day9-instructional-slice`
- Estimated minutes: `8`
- Current step count: `5`
- Practice classification: `instructional-practice-only`
- Authorized for pilot: `false`
- Authorized for public release: `false`

## Controlled content and asset IDs
- `APR-R1-RM01-L01-D9`
- `APR-CNT-R1-RM01-L01-D9-ORI-001`
- `APR-BRG-R1-RM01-L01-D9-001`
- `APR-AUD-R1-RM01-L01-D9-MDL-001`
- `APR-TXT-R1-RM01-L01-D9-TR-001`
- `APR-INT-R1-RM01-L01-D9-REC-001`
- `APR-PRN-R1-RM01-L01-D9-001`
- `APR-PRM-R1-RM01-L01-D9-SPK-001`
- `APR-FBK-R1-RM01-L01-D9-001`
- `APR-PRM-R1-RM01-L01-D9-RTY-001`
- `APR-PRM-R1-RM01-L01-D9-REF-001`
- `APR-CNT-R1-RM01-L01-D9-CLS-001`
- `APR-ALT-R1-RM01-L01-D9-WRT-001`
- `APR-AUD-R1-RM01-L01-D9-TMP-001`

## Implemented five-step flow
1. Human-purpose orientation in Spanish.
2. Portuguese model language, learner-controlled transcript, optional Spanish meaning, Spanish Bridge, pronunciation guidance, pragmatic notice, and optional temporary generated model audio.
3. Required controlled recognition decision about communicative purpose.
4. Personally true spoken Practice with protected Original, separate Latest retry, optional transcript, deterministic guidance, optional retry, and session-only written Practice alternative.
5. Session-only reflection and controlled session closure.

## Schema changes
- Added step-level `content_ids`.
- Added manifest-level `content_package_id`, `practice_classification`, `authorization_notice`, and structured `session_closure`.
- Added structured information-step fields for model script, controlled transcript, translation, Bridge, pronunciation, pragmatic guidance, and model audio configuration.
- Added recording-step fields for production frame, privacy notice, Practice notice, retry instruction, and written alternative.
- Added required bounded `confirmed_transcript` to the feedback request.
- Added machine-readable `feedback_case` to the feedback response.

## Deterministic feedback rules
The backend uses conservative, content-specific normalization and classification. It recognizes only approved greeting, self-identification, preference, and invitation forms for this bounded Practice. It prioritizes Spanish-shaped `me gusta`, then `gosto` without `de`, then missing-component classification, and falls back to uncertain without calling the learner incorrect.

## Written Practice alternative
The written alternative is intentionally selected by the learner, session-only, limited to 240 characters, and can satisfy the Step 4 gate when non-empty. It is not oral performance, spoken Evidence, pronunciation proof, or formal equivalent Evidence.

## Audio boundary
Temporary generated audio is requested only after explicit learner action, uses the approved server-side script, and is disclosed as non-final test audio. No final human audio asset was added.

## Session-only boundary
Recordings, object URLs, transcript drafts, confirmed transcript text, written Practice, feedback state, retries, and reflection remain frontend/browser-session state. No APR persistence, database model, migration, Completion, Progress, or Evidence endpoint was added.

## Files changed
- Backend APR manifest, schemas, router, and tests.
- Frontend APR lesson player, model audio, transcript, feedback/retry, recorder, closure, and tests.
- APR GitHub Actions workflow.
- Day 9 documentation and founder test guide.

## Tests run
See final implementation report for exact commands and results.

## Workflow changes
The APR frontend workflow command now includes `frontend/tests/app/apr-day9-real-lesson.test.tsx` while preserving the existing focused APR test list.

## Preserved Days 1–8 guarantees
Authentication, protected APR access, `APR_POC_ENABLED=false` default, request cancellation, stale-response protection, object-URL cleanup, protected Original recording, separate replaceable Latest retry, optional transcription, learner transcript editing and confirmation, optional generated audio, optional feedback, optional retry, restart confirmation, exit routing, reflection preservation before confirmed restart, and session-only technical state were preserved.

## Approved instructional content
The approved orientation, Portuguese model and transcript, Spanish Bridge, pronunciation guidance, pragmatic notice, recognition item, Practice prompt, written alternative, deterministic feedback cases, retry instruction, reflection prompt, and closure copy became controlled instructional content.

## Temporary content
Generated model audio remains temporary provider-generated test audio and is not final Academy audio.

## Deferred scope
Complete Lesson 1, formal Evidence, Evidence Definitions, Capability Observations, Progress, Completion, scoring, proficiency assessment, R1A activation, external pilot, public release, final human audio, unrestricted AI tutoring, audio analysis, and pronunciation analysis remain deferred.

## Known external-service constraints
TTS and STT depend on configured providers. Their failures are treated as technical failures and do not block reflection, written Practice, playback, session closure, or safe exit.

## Final implementation commit
Final commit SHA is reported in the final implementation report because embedding a Git commit's own SHA in tracked content changes that SHA.

## Regression correction update

### Recovery path used
Rule A was used during the regression-correction resume. The rehydrated `work` branch at `9cd47380b8dc7b2749e7de103d2917cd71e38035` contained the complete approved Day 9 implementation, including `APR-R1-RM01-L01-D9`, `1.0.0-day9-controlled-slice`, the exact Portuguese model, Day 9 documentation, and the Day 9 frontend test. No reset, bundle import, or patch application was performed. The branch was renamed to `codex/apr-day9-real-lesson-vertical-slice` because the desired branch name did not already exist locally.

### Migrated legacy frontend suites
The focused APR frontend regression files were migrated from placeholder-era English labels and placeholder schema fixtures to the approved Day 9 contract:

- `apr-primeira-conexao.test.tsx` now validates the Day 9 module status, protected APR API call, feature-flag 404 behavior, and absence of unrelated app calls.
- `apr-lesson-player.test.tsx` now validates manifest identity, five-step order, controlled IDs, Step navigation, recognition gating, written Practice gating, reflection preservation, protected Original, replaceable Latest retry, restart cleanup, and placeholder absence.
- `apr-audio-recorder.test.tsx` now validates learner-action microphone permission, capture, stream cleanup, unmount suppression, and Day 9 microphone-failure recovery copy.
- `apr-transcript-confirmation.test.tsx` now validates optional transcription, explicit request, editable machine draft, explicit confirmation, Original/latest retry transcript separation, and technical failure continuation.
- `apr-model-audio.test.tsx` now validates Step 2 temporary model audio, explicit request, server-controlled ID, no autoplay, object URL revocation, and TTS failure continuation.
- `apr-feedback-retry.test.tsx` now validates no unconfirmed machine-draft submission, static self-check without backend feedback, confirmed-transcript feedback request body and revision, non-scoring/non-Evidence guidance, feedback failure continuation, and optional retry separation.
- `apr-session-closure.test.tsx` now validates approved closure copy, no Completion/Progress/Evidence request, cancelled Restart preservation, confirmed Restart cleanup, and Exit routing.
- `apr-day9-real-lesson.test.tsx` remains the broad approved Day 9 vertical-slice integration test.

### Placeholder-only assertions replaced
Assertions whose sole purpose was to prove placeholder English content or technical-placeholder metadata existed were replaced with assertions that approved Day 9 content is present and placeholder content is absent. Obsolete labels such as English `Continue`, technical model-audio copy, technical feedback copy, and technical closure copy were migrated to the approved Spanish Day 9 learner-facing contract.

### Preserved Days 1–8 guarantees
The migrated suite continues to protect authentication-facing API boundaries, APR feature-flag behavior, five-step structure, single-choice gating, Original/retry separation, session-only recording state, microphone action gating, MediaRecorder/MediaStream cleanup, object-URL revocation, optional transcription, editable and confirmable transcript drafts, optional model audio, no autoplay, optional feedback, confirmed-transcript-only feedback, retry optionality, reflection preservation, Restart behavior, Exit routing, closure nonclaims, and absence of Evidence/Progress/Completion requests.

### Final focused frontend totals
The complete focused APR frontend command passed with 8 test files and 19 tests: zero failed files and zero failed tests.

### Backend execution limitation
`ruff check app/apr tests/test_apr.py` passed. Backend pytest was attempted locally but could not execute because this workspace runs Python 3.12 while the repository uses Python 3.14 syntax; collection fails before tests run on multi-exception `except` syntax.

### Production-build environmental limitation
`npm run build` remains blocked by non-Day-9 environment/project issues: Google Fonts fetch failures in the Codex environment and missing `messages/en.json` resolution from `src/i18n/request.ts`.

### Corrective commit
To be recorded in the final correction report after committing: `PENDING_CORRECTIVE_COMMIT_SHA`.

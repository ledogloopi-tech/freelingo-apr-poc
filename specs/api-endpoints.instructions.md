---
description: "Complete API reference for FreeLingo: all REST endpoints and the WebSocket voice conversation endpoint, grouped by router."
applyTo: "backend/**"
---

# API Endpoints — FreeLingo

Most REST endpoints are prefixed under `/api`. The public health check is at `/health`. The WebSocket endpoint is at `/ws/conversation`.

---

## Health — `/health`

- **GET `/health`** — Rate limit: 60/min. Public liveness check. Returns `{"status":"ok"}` only and does not expose DB, Redis, TTS, or STT dependency details.

---

## Config — `/api/config`

- **GET `/api/config`** — Rate limit: 60/min. Public runtime configuration flags for the frontend. Returns non-sensitive values including Stripe enablement/prices, TTS provider/voice, and `maintenance_mode`.

---

## Auth — `/api/auth`

- **POST `/register`** — Rate limit: 5/min (+ invite-gated). Creates account (respects `ALLOW_REGISTRATION`, invite token, and `BLOCKED_EMAIL_DOMAINS`). Password policy: 10–25 chars, at least one uppercase letter, one number, and one symbol. Returns `access_token` + sets httpOnly refresh cookie — no separate login step needed. Rejects blocked domains or invalid password with HTTP 422.
- **POST `/login`** — Rate limit: 10/min. Returns access_token (JWT, 15 min) + refresh_token in httpOnly cookie (30 days)
- **POST `/refresh`** — Rate limit: 60/min. Rotates refresh token, returns new access_token
- **POST `/logout`** — Rate limit: 60/min. Deletes refresh token from Redis, clears cookie
- **GET `/me`** — Rate limit: 60/min. Returns authenticated user profile, including subscription fields (`subscription_status`, `subscription_ends_at`, `trial_used`, `assessment_voice_trial_used`) so the frontend can distinguish Stripe trial eligibility, post-assessment voice-demo eligibility, and active subscription state.
- **PATCH `/me`** — Rate limit: 60/min. Updates display_name, email, password, target_language, conversation settings
- **POST `/me/avatar`** — Rate limit: 60/min. Uploads the authenticated user's profile avatar (JPEG/PNG, max 2 MB). Validates the declared content type, image signature, and minimal image structure, stores the image on disk under `/app/avatars` using a non-predictable UUID filename, and returns the user profile with `avatar` set to a cache-busted internal reference (`/api/avatars/{uuid}.{ext}?v={ms}`). The file reference is not publicly served.
- **GET `/me/avatar-file`** — Rate limit: 60/min. Authenticated current-user avatar retrieval endpoint. Returns only the authenticated user's own avatar file; this is the supported image retrieval path used by the frontend. Responses are marked `Cache-Control: private, no-store`; client-side avatar reuse is handled by the frontend blob cache keyed by the stored avatar reference.
- **DELETE `/me/avatar`** — Rate limit: 60/min. Removes profile avatar (sets to null)
- **DELETE `/me`** — Rate limit: 5/min. Deletes own account and all associated data (CASCADE). Forbidden for admin accounts.
- **GET `/quota`** — Rate limit: 60/min. Returns live conversation quota status for the authenticated user (sessions this week, minutes today, minutes this week)
- **GET `/verify-email`** — Rate limit: 60/min. Verifies email via one-time token (query param `token`, TTL 24h in Redis)
- **POST `/resend-verification`** — Rate limit: 3/min. Sends a new verification email to the authenticated user
- **POST `/forgot-password`** — Rate limit: 5/min. Sends password reset link to the given email. Always returns 200 (anti-enumeration).
- **POST `/reset-password`** — Rate limit: 5/min. Resets password using one-time token (TTL 1h in Redis)

---

## Admin — `/api/admin`

Requires `role="admin"`. All endpoints return 403 for non-admin users.

- **GET `/stats`** — Rate limit: 60/min. Aggregated admin overview metrics: total/active/inactive users, active/trialing/past_due subscriptions, total feedback, pending feedback, pending bug reports, and reviews pending approval.
- **GET `/health`** — Rate limit: 60/min. Private admin diagnostic health check. Returns DB, Redis, TTS, and STT dependency status as `{"status":"ok"|"degraded","checks":{...}}`; returns HTTP 503 when any dependency check fails.
- **GET `/users`** — Rate limit: 60/min. Lists users (paginated). Query params: `skip` (default 0), `limit` (default 10, max 100), `q` (search by username or email), `subscription` (`none`, `trialing`, `active`, `past_due`, `canceled`, `incomplete`, `incomplete_expired`, `unpaid`, `paused`), `role` (`user`, `admin`), and `is_active` (`true`, `false`). Returns `{items, total, skip, limit}`.
- **POST `/users`** — Rate limit: 60/min. Creates user directly (bypasses `ALLOW_REGISTRATION`). Body requires `username`, `email`, `password`, `display_name`, `native_language`, `target_language`, and optional `role`; sends verification email if `EMAIL_ENABLED=true`.
- **GET `/users/{id}`** — Rate limit: 60/min. User detail, including admin-only Stripe identifiers (`stripe_customer_id`, `stripe_subscription_id`) and subscription state.
- **PATCH `/users/{id}`** — Rate limit: 60/min. Edit role, is_active, is_verified, display_name, conversation quotas
- **DELETE `/users/{id}`** — Rate limit: 5/min. Deletes account and all associated data (CASCADE)
- **GET `/users/{id}/stats`** — Rate limit: 60/min. Usage statistics: XP, streak, lessons, exercises, tokens
- **GET `/users/{id}/quota`** — Rate limit: 60/min. Live quota status from Redis (sessions this week, minutes today, minutes this week)
- **POST `/invite`** — Rate limit: 60/min. Generates single-use invite link (48h Redis TTL)
- **GET `/maintenance`** — Returns `{"maintenance_mode": bool}` — current maintenance mode state
- **PATCH `/maintenance`** — Toggles maintenance mode on/off in Redis. Returns `{"maintenance_mode": bool}`
- **PUT `/maintenance`** — Sets maintenance mode explicitly. Body: `{maintenance_mode: bool}`. Returns `{"maintenance_mode": bool}`
- **GET `/reviews`** — Rate limit: 60/min. Lists reviews for admin moderation. Query params: `is_approved`, `rating` (1–5), `target_language`, `order` (`asc`|`desc`), `skip`, `limit`. Returns `{items, total, skip, limit}`.
- **PATCH `/reviews/{review_id}`** — Rate limit: 60/min. Updates review approval state. Body: `{is_approved: bool}`. Returns updated review.
- **DELETE `/reviews/{review_id}`** — Rate limit: 60/min. Permanently deletes a review. Returns HTTP 204.

---

## Billing — `/api/billing`

Registered only when `STRIPE_ENABLED=true`.

- **POST `/checkout`** — Rate limit: 60/min. Auth: get_current_user. Creates a Stripe Checkout Session for `monthly` or `yearly`. Does not require an existing subscription because unsubscribed users must be able to subscribe.
- **POST `/portal`** — Rate limit: 60/min. Auth: get_current_user. Creates a Stripe Customer Portal session for users with a `stripe_customer_id`.
- **POST `/webhook`** — Rate limit: 200/min. Public network access but requires a valid Stripe signature before processing. Handles checkout/session and subscription lifecycle events. Checkout completion verifies the Stripe Subscription before granting access and persists the current `stripe_subscription_id`; subscription update/delete and invoice payment-failed events are ignored as stale when their subscription ID differs from the user's current `stripe_subscription_id`. Invoice payment-failed handling supports both legacy `invoice.subscription` and current `invoice.parent.subscription_details.subscription` shapes. Subscription updates accept real Stripe statuses (`trialing`, `active`, `past_due`, `canceled`, `incomplete`, `incomplete_expired`, `unpaid`, `paused`) and keep the existing status for unknown values. Valid payload/signature errors return 400; internal processing failures return 500 so Stripe retries the event.

---

## Assessment — `/api/assessment`

3-step onboarding flow plus end-of-level testing.

- **GET `/start`** — Rate limit: 10/min. Begins adaptive quiz (LLM-generated questions, static fallback)
- **GET `/bank`** — Rate limit: 60/min. Returns the full static assessment bank for the given language (query param `language`, default `en-GB`). Auth required. Response: `{questions: [{id, skill, difficulty, question, options, correct, grammar_slug}]}`. `ja-JP`, `ko-KR`, and `zh-CN` return static assessment banks in the target language.
- **POST `/submit`** — Rate limit: 10/min. Legacy: submits answers for CEFR evaluation
- **POST `/evaluate`** — Rate limit: 60/min. Deterministic CEFR evaluation (no LLM — groups by difficulty)
- **POST `/free-write`** — Rate limit: 10/min. Evaluates free-write text for CEFR placement (LLM)
- **POST `/complete`** — Rate limit: 10/min. Persists results and creates a StudyPlan. When `STRIPE_ENABLED=true`, the user is not subscribed, and `assessment_voice_trial_used=false`, the response includes `voice_trial: {available, token, duration_seconds, expires_in_seconds}` for a one-time 5-minute voice demo.
- **POST `/voice-trial`** — Rate limit: 10/min. Body: `{target_language?}`. Regenerates a fresh post-assessment voice demo token for the user's active study plan in that language when `STRIPE_ENABLED=true`, the user is not subscribed, and `assessment_voice_trial_used=false`. Used when the student previously skipped the demo and returns to the assessment page.
- **GET `/level-test/questions/{plan_id}`** — Rate limit: 5/min. Generates 20-question level test (LLM, constrained to studied content)
- **POST `/level-test/submit`** — Rate limit: 10/min. Submits level test answers → score + recommendation
- **GET `/level-test/result/{plan_id}`** — Rate limit: 60/min. Returns test result and recommendation (`"advance"`, `"extend"`, or `"repeat"`)

---

## Languages — `/api/languages`

All endpoints require `get_current_user`. These endpoints manage the user's independent target-language study tracks.

- **GET ``** — Rate limit: 60/min. Lists all learning languages for the authenticated user.
- **GET `/active`** — Rate limit: 60/min. Returns the user's active learning language.
- **POST ``** — Rate limit: 60/min. Adds a new target language and initializes the associated language record.
- **PUT `/active`** — Rate limit: 60/min. Switches the active target language.
- **DELETE `/{target_language}`** — Rate limit: 5/min. Deletes a target-language track and its associated study data according to backend ownership checks.

---

## Curriculum — `/api/curriculum`

Auth required (`get_current_user`). Returns static curriculum data for all supported target languages.

- GET — Path: ``; Auth: get_current_user; Description: Full curriculum for all 6 CEFR levels. Query param: `language` (BCP-47, default `en-GB`).
- GET — Path: `/{level}`; Auth: get_current_user; Description: Units for a specific CEFR level. Query param: `language` (BCP-47).

---

## Vocabulary — `/api/vocabulary`

Auth required (`get_current_user`). Serves static vocabulary data across the backend language modules, organized per CEFR level. `ja-JP` includes 152 vocabulary sets, while `ko-KR` and `zh-CN` each include 155 vocabulary sets referenced by their curricula.

- **GET ``** — Auth: get_current_user. All vocabulary sets for the given language. Query param: `language` (BCP-47, default `en-GB`). Response: `{sets: [{id, level, topic, unit_ref, words: [{word, pos, definition, example, ipa?, frequency_rank?}]}]}`.
- **GET `/level/{level}`** — Auth: get_current_user. Vocabulary sets filtered by CEFR level (A1–C2). Query param: `language` (BCP-47). Returns 400 for invalid levels.
- **GET `/{set_id}`** — Auth: get_current_user. A single vocabulary set by ID. Query param: `language` (BCP-47). Response: `{set: {...}}`. Returns 404 if not found.
- **POST `/{set_id}/native-help`** — Rate limit: 10/min. Auth: get_current_user. Query param: `language` (BCP-47, default `en-GB`). Generates or returns cached native-language study help for a vocabulary set, keyed globally by set ID, target language, native language, and source-content hash. Response: `{native_help: {summary, study_tips, word_notes, common_traps, mini_glossary, practice_prompts}}`. Returns 404 if the set does not exist and 503 if generation is unavailable or already in progress.

---

## Study Plan — `/api/study-plan`

- **GET `/current`** — Rate limit: 60/min. User's active plan with curriculum progress
- **POST `/generate`** — Rate limit: 10/min. Creates new plan from CEFR level, goals, and duration
- **GET `/today`** — Rate limit: 20/min. Today's lessons; auto-generates missing content via LLM on first access; auto-advances `progress_day` when all lessons for the current day are complete. Returns `plan_id`, `cefr_level`, `lessons`, `progress_day`, `total_days`, `pending_count`.
- **POST `/skip-day`** — Rate limit: 60/min. Increments `progress_day` by 1 (capped at `total_days`). Returns `{progress_day, total_days}`.
- **GET `/pending-lessons`** — Rate limit: 60/min. Returns incomplete lessons from days before `progress_day` (generated but not completed).

---

## Lessons — `/api/lessons`

- **GET `/{lesson_id}`** — Rate limit: 60/min. Lesson detail with exercises. Exercise responses include optional `native_explanation` and `native_hint` copied from generated lesson JSON when available. Lesson content may include enriched vocabulary items with optional native-language translation, example translation, usage note, and reading fields.
- **POST `/{lesson_id}/start`** — Rate limit: 60/min. Marks lesson as in-progress.
- **POST `/{lesson_id}/complete`** — Rate limit: 60/min. Marks the lesson as completed and updates progress and competencies.
- **POST `/{lesson_id}/native-explanation`** — Rate limit: 10/min. Generates and caches a native-language explanation for existing lessons at any CEFR level whose `content.native_explanation` is missing. Returned support includes translated text, key points, examples, common traps, and a mini-glossary. If already present, returns the cached explanation idempotently.
- **POST `/exercises/{id}/native-explanation`** — Rate limit: 10/min. Generates and caches a concise native-language clarification for an exercise whose target-language `explanation` exists but whose generated JSON lacks `native_explanation`. If already present, returns the cached exercise-level explanation idempotently.
- **POST `/exercises/{id}/native-hint`** — Rate limit: 10/min. Generates and caches a concise pre-answer native-language hint for an exercise whose generated JSON lacks `native_hint`. Hints must help without revealing the correct answer. If already present, returns the cached hint idempotently.
- **POST `/exercises/{id}/regenerate`** — Rate limit: 5/hour. Regenerates one unanswered, technically invalid exercise on demand while preserving the rest of the lesson. Rejects completed lessons, answered exercises, and exercises that pass validation.
- **POST `/exercises/{id}/answer`** — Rate limit: 20/min. Submits an answer, evaluates multiple choice, fill, free-write, or pronunciation exercises, and returns score plus feedback.

---

## Flashcards — `/api/flashcards`

- **GET `/due`** — Rate limit: 60/min. Cards pending review today (SM-2 ordering)
- **GET `/all`** — Rate limit: 60/min. All user's flashcards
- **POST `/`** — Rate limit: 60/min. Creates flashcard manually
- **POST `/bulk`** — Rate limit: 60/min. Creates multiple flashcards at once; skips duplicates (by word) for the user
- **POST `/{card_id}/review`** — Rate limit: 60/min. Records SM-2 review (quality 0–5)
- **POST `/generate`** — Rate limit: 20/min. Generates N flashcards via LLM with native-language translations
- **POST `/from-word`** — Rate limit: 30/min. Saves a single word as a flashcard: body `{word, context, cefr_level}`; AI generates definition/example/translation; sets `source="from_text"`; returns `FlashcardResponse`
- **GET `/vocabulary`** — Rate limit: 60/min. Returns user's saved-from-text flashcards (`source="from_text"`), ordered by `created_at` desc
- **DELETE `/{card_id}`** — Rate limit: 60/min. Permanently deletes a flashcard owned by the user; 204 No Content

---

## Grammar — `/api/grammar`

All endpoints require `get_current_user`.

- **GET ``** — Rate limit: 60/min. Auth: get_current_user. Returns all grammar topics for the given target language. Query param: `language` (BCP-47, default `en-GB`). Response: `{topics: [{slug, title, level, category, summary, explanation, structure, rules, examples, common_mistakes, related}]}`. `ja-JP` includes 130 grammar topics, while `ko-KR` and `zh-CN` include 126 grammar topics aligned with their curriculum slugs.
- **GET `/{slug}`** — Rate limit: 60/min. Auth: get_current_user. Returns a single grammar topic by slug. Query param: `language`. Returns 404 if not found.
- **POST `/{slug}/native-help`** — Rate limit: 10/min. Auth: get_current_user. Query param: `language` (BCP-47, default `en-GB`). Generates or returns cached native-language study help for a static grammar topic, keyed globally by grammar slug, target language, native language, and source-content hash. Response: `{native_help: {summary, explanation, key_points, examples, common_traps, mini_glossary}}`. Returns 404 if the topic does not exist and 503 if generation is unavailable or already in progress.

---

## Chat — `/api/chat`

- GET — Path: `/conversations`; Description: Rate limit: 60/min. Lists user's conversations (text + voice), ordered by `updated_at` desc. Response includes `source` (`chat` or `voice`).
- POST — Path: `/conversations`; Description: Rate limit: 60/min. Creates new conversation
- DELETE — Path: `/conversations/{id}`; Description: Rate limit: 60/min. Deletes conversation and its messages (CASCADE)
- GET — Path: `/conversations/{id}/messages`; Description: Rate limit: 60/min. Returns messages for a conversation
- POST — Path: `/`; Description: Rate limit: 30/min. Sends message → streams AI tutor response (SSE)
- GET — Path: `/history`; Description: Rate limit: 60/min. All chat history (legacy)

---

## Progress — `/api/progress`

- GET — Path: `/summary`; Description: Streak, XP, skills breakdown, and current-level vocabulary progress for the active study language
- GET — Path: `/history`; Description: Daily progress for last 90 days
- GET — Path: `/competencies`; Description: Per-unit competency scores and mastery status

`GET /api/progress/summary` returns totals scoped to the active study plan/language: `total_xp`, `current_streak`, `total_lessons`, `total_exercises`, `exercises_correct`, `accuracy`, `skills`, plus vocabulary summary fields for the plan's current CEFR level and `target_language`: `vocabulary_level`, `vocabulary_mastered`, `vocabulary_total`, and `vocabulary_progress`. Vocabulary progress counts words from the current level's backend vocabulary sets whose flashcard exists in the active `study_plan_id` with `repetitions > 0`.

---

## TTS — `/api/tts`

- **POST ``** — Rate limit: 20/min. Text → MP3 audio. Uses Kokoro TTS (local) or OpenAI TTS, controlled by `TTS_PROVIDER`. Supports optional trace correlation via request header `X-TTS-Trace-ID`. Returns diagnostic headers: `X-TTS-Trace-ID`, `X-TTS-Backend-Synth-Ms`, `X-TTS-Backend-Total-Ms` (and, when passing through the Next.js proxy, `X-TTS-Proxy-Fetch-Ms`, `X-TTS-Proxy-Buffer-Ms`, `X-TTS-Proxy-Total-Ms`).
- **GET `/preview/{voice}`** — Rate limit: 60/min. Returns a short MP3 preview for an OpenAI TTS voice when supported.

---

## STT — `/api/stt`

- POST — Path: ``; Rate limit: 20/min; Description: Audio → transcribed text. Uses faster-whisper (local) or OpenAI Whisper, controlled by `STT_PROVIDER`.

---

## Contact — `/api/contact`

- **POST ``** — Rate limit: 5/hour. Submits a contact form. Body: `{ email, subject, description }`. Forwards the message to `CONTACT_EMAIL` via SMTP. Returns 204 on success, 502 if email sending fails. No auth required.

---

## WebSocket — `/ws/conversation`

Full-duplex voice conversation pipeline.

Both `POST /api/conversation/warmup` and `/ws/conversation` require an authenticated user with subscription access when `STRIPE_ENABLED=true`, except for a valid post-assessment voice trial token. Both reject non-admin users while maintenance mode is active.

- **POST `/api/conversation/warmup`** — Rate limit: 20/min. Pre-heats TTS and STT models before opening the WebSocket. Optional body: `{trial_token}` for the post-assessment demo.

**Authentication**: After the WebSocket handshake is accepted, the client must send a JSON message `{"type": "auth", "token": "<access_token>"}` within 10 seconds. If missing, malformed, or invalid, the server closes the connection with code 1008.

**Message flow**: Client sends audio chunks → STT transcription → LLM generates full response → sentence-level TTS → MP3 audio chunks returned. The server starts the greeting as a cancellable task and immediately enters the receive loop; backend barge-in protocol remains available, while the current frontend ignores user speech during active tutor turns for stability.

**Client → Server message types:**

- **`auth`** — Payload: `{"type":"auth","token":"<jwt>","voice":"nova","target_language":"en-GB","context":[...],"voice_trial_token":"..."}`. Description: First message — authenticates the session and may include voice preference, target language, optional chat context, and a post-assessment voice trial token. Trial sessions are consumed when the WebSocket starts and are capped to 300 seconds.
- **binary frame** — Payload: raw audio bytes. Description: WAV audio chunk from VAD
- **`interrupt`** — Payload: `{"type":"interrupt"}`. Description: Optional manual interruption; cancels current generation

**Server → Client message types:**

- **`status`** — Payload: `{"value":"transcribing" | "thinking" | "listening"}`. Description: Pipeline state hint
- **`transcript`** — Payload: `{"role":"user" | "assistant","text":"...","final":true | false}`. Description: User STT result and assistant streaming/final text
- **binary frame** — Payload: MP3 bytes. Description: MP3 audio for a TTS sentence
- **`barge_in`** — Payload: `{}`. Description: Current greeting/response was cancelled by new audio; client cancels playback
- **`turn_complete`** — Payload: `{}`. Description: Assistant turn fully streamed and audio sent
- **`session_warning`** — Payload: `{"remaining_seconds": N, "reason": "inactivity" | "max_duration"}`. Description: Timeout warning at 60 s
- **`session_end`** — Payload: `{"reason": "..."}`. Description: Session closed by server
- **`error`** — Payload: `{"code":"...","message":"..."}`. Description: Pipeline or policy error

**Features:**

- **Barge-in protocol**: explicit interrupts or new audio input can cancel the initial greeting or any ongoing LLM/TTS response server-side; the current frontend disables automatic interruption during active tutor turns
- **Empty STT guard**: empty/whitespace transcriptions are ignored and do not trigger an assistant reply
- **Serialized server sends**: JSON frames, binary audio chunks, timeout warnings, and close frames are written through one send lock to avoid concurrent WebSocket writes
- **VAD**: browser-level voice activity detection (`@ricky0123/vad-react` + onnxruntime-web threaded WASM)
- **Gapless playback**: `AudioQueue` schedules consecutive `AudioBufferSourceNode`s
- **Session timeouts**: max duration (default 30 min) and inactivity (default 3 min), each with 60 s warning
- **In-memory history**: last 20 messages kept for LLM context during session (not persisted to DB)
- **Warmup**: `POST /api/conversation/warmup` pre-heats TTS and STT models before opening the WebSocket

---

## Listening — `/api/listening`

All endpoints require `require_subscription`. Audio file path is built from the integer exercise ID — never from a DB string — to prevent path traversal.

- **GET `/next`** — Rate limit: 10/min. Auth: require_subscription. Returns the oldest unplayed `ListeningExercise` for the user's current CEFR level and target language (questions included, **text and correct answers omitted**). Returns `{"available": false, "generating": false}` when the pool is empty, or `{"available": false, "generating": true}` while generation is in progress (Redis lock held).
- **POST `/generate`** — Rate limit: 5/min. Auth: require_subscription. Acquires a per-(level, language) Redis lock (`nx=True, ex=60`) and enqueues a `BackgroundTask` that calls LLM + TTS, saves the exercise and MP3. Returns HTTP 202. Returns 409 if a generation job is already running.
- **GET `/audio/{exercise_id}`** — Rate limit: 60/min. Auth: require_subscription. Serves the MP3 for the given exercise as a `FileResponse` (`audio/mpeg`). Returns 404 if the exercise or its audio file does not exist.
- **POST `/attempt`** — Rate limit: 20/min. Auth: require_subscription. Submits answers (`{exercise_id, answers: [str]}`) for scoring. Returns score (0–5), XP earned (0–50), correct answers, and the full transcript. Returns 404 (exercise not found), 409 (already attempted), 400 (wrong number of answers).
- **GET `/history`** — Rate limit: 60/min. Auth: require_subscription. Returns paginated list of the user's past attempts with scores, XP, and transcripts. Query params: `skip` (default 0), `limit` (default 10, max 50).

## Reading — `/api/reading`

All endpoints require `require_subscription`. Unlike Listening, exercise text is included in the exercise response — there is no audio endpoint and no transcript reveal on submit.

- **GET `/next`** — Rate limit: 10/min. Auth: require_subscription. Returns the oldest uncompleted `ReadingExercise` for the user's current CEFR level and target language. **Text and questions are included immediately.** Returns `{"available": false}` when the pool is empty. Supports `?wait=true` for long-polling (max 90 s) while generation is in progress.
- **POST `/generate`** — Rate limit: 5/min. Auth: require_subscription. Acquires a per-(level, language) Redis lock (`nx=True, ex=60`) and enqueues a `BackgroundTask` that calls LLM and saves the exercise. Returns HTTP 202 with `{"status": "generating"}`. Returns 202 (no-op) if a generation job is already running.
- **POST `/attempt`** — Rate limit: 20/min. Auth: require_subscription. Submits answers (`{exercise_id, answers: dict[str,str], replay: bool}`) for scoring. Returns score (0–5), XP earned (0–50), and correct answers. Returns 404 (exercise not found), 409 (already attempted), 400 (wrong number of answers).
- **GET `/history`** — Rate limit: 60/min. Auth: require_subscription. Returns paginated list of the user's past attempts with scores, XP, exercise text, and correct answers. Query params: `skip` (default 0), `limit` (default 10, max 50).

---

## Feedback — `/api/feedback`

All endpoints require `get_current_user`. Status update requires `require_admin`.

- **GET ``** — Rate limit: 60/min. Auth: get_current_user. Returns paginated list of feedback entries. Query params: `q` (search by title, description, username, or display name; max 100 chars), `type` (`feature`\|`bug`), `status` (`pending`\|`planned`\|`in_progress`\|`done`\|`declined`), `sort` (`votes`\|`date`, default `votes`), `order` (`asc`\|`desc`, default `desc`), `skip` (default 0), `limit` (default 20, max 100). When `status` is omitted, entries with `status=done` are excluded from the public board and admin queue; they are returned only with `status=done`. Response: `{items, total, skip, limit}`. Each item includes `voted_by_me` and `comment_count` fields injected server-side.
- **POST ``** — Rate limit: 10/hour. Auth: get_current_user. Creates a new feature request or bug report. Body: `{type, title, description}`. Returns HTTP 201 + the created entry.
- **GET `/{id}`** — Rate limit: 60/min. Auth: get_current_user. Returns a single entry with its full comment thread ordered by `created_at ASC`.
- **DELETE `/{id}`** — Rate limit: 60/min. Auth: get_current_user. Deletes an entry. Author can delete their own; admin can delete any. Cascade-deletes all votes and comments. Returns HTTP 204.
- **POST `/{id}/vote`** — Rate limit: 60/min. Auth: get_current_user. Toggles the authenticated user's vote on a feature request. Returns `{voted: bool, vote_count: int}`. Returns 400 if entry type is `bug`.
- **PATCH `/{id}/status`** — Rate limit: 60/min. Auth: require_admin. Updates the entry status. Body: `{status}`. Valid values: `pending`, `planned`, `in_progress`, `done`, `declined`. Returns the updated entry.
- **GET `/{id}/comments`** — Rate limit: 60/min. Auth: get_current_user. Returns all comments for an entry ordered by date ASC. Response: `{items, total}`.
- **POST `/{id}/comments`** — Rate limit: 20/hour. Auth: get_current_user. Adds a comment to an entry. Body: `{body}` (max 2000 chars). Returns HTTP 201 + the created comment.
- **DELETE `/{id}/comments/{cid}`** — Rate limit: 60/min. Auth: get_current_user. Deletes a comment. Author can delete their own; admin can delete any. Returns HTTP 204.

## Reviews — `/api/reviews`

User review endpoints. Admin moderation endpoints live under `/api/admin/reviews`.

- **GET `/me`** — Rate limit: 60/min. Auth: get_current_user. Returns `{has_review, review}` for the authenticated user. `review` is `null` when the user has not submitted one.
- **POST ``** — Rate limit: 5/hour. Auth: get_current_user. Creates the authenticated user's single review and queues an admin email notification to `CONTACT_EMAIL` when email is configured. Body: `{rating: 1-5, comment?: string}`. Stores display-name and active-learning-language snapshots server-side, creates with `is_approved=false`, returns HTTP 201, and returns HTTP 409 with `review_already_exists` if the user already has a review.
- **PATCH `/me`** — Rate limit: 10/hour. Auth: get_current_user. Updates the authenticated user's existing review. Body: `{rating: 1-5, comment?: string}`. Refreshes display-name and active-learning-language snapshots, resets `is_approved=false`, returns the updated review, and returns HTTP 404 with `review_not_found` if the user has not submitted one yet.
- **DELETE `/me`** — Rate limit: 10/hour. Auth: get_current_user. Deletes the authenticated user's existing review and returns HTTP 204. Returns HTTP 404 with `review_not_found` if the user has not submitted one yet.
- **GET `/public`** — Rate limit: 60/min. Public. Returns approved landing reviews only (`is_approved=true` and `rating >= 4`), ordered newest-first. Query param: `limit` (default 20, max 100). Response omits `user_id` and `is_approved`.

## Memories — `/api/memories`

All endpoints require `require_subscription`: users still need subscription access when Stripe is enabled, but maintenance mode does not block memory management.

- GET — Path: ``; Rate limit: 60/min; Auth: require_subscription; Description: Returns all memories for the authenticated user. Response: `{memories: [{id, content, source, created_at}]}`.
- DELETE — Path: `/{id}`; Rate limit: 60/min; Auth: require_subscription; Description: Deletes a single memory by ID. Returns HTTP 204. Returns 404 if not found or not owned by the user.
- DELETE — Path: ``; Rate limit: 10/min; Auth: require_subscription; Description: Clears all memories for the authenticated user. Response: `{deleted: int}`.

---

## Phrasebook — `/api/phrasebook`

All endpoints require `get_current_user`.

- **GET ``** — Rate limit: 60/min. Auth: get_current_user. Returns all phrasebook categories for the given target language. Query param: `language` (BCP-47, default `en-GB`). Response: `{categories: [{id, level, situation, icon, phrases: [{text, context, register, unit_ref}]}]}`. `ja-JP` includes 44 A1-C2 phrasebook categories, `ko-KR` includes 34 A1-C2 phrasebook categories, and `zh-CN` includes 24 A1-C2 phrasebook categories in the target language.
- **GET `/level/{level}`** — Rate limit: 60/min. Auth: get_current_user. Returns phrasebook categories filtered by CEFR level (A1–C2). Returns 400 for invalid levels. Query param: `language`.
- **GET `/{category_id}`** — Rate limit: 60/min. Auth: get_current_user. Returns a single phrasebook category by ID. Query param: `language`. Returns 404 if not found.
- **POST `/{category_id}/native-help`** — Rate limit: 10/min. Auth: get_current_user. Query param: `language` (BCP-47, default `en-GB`). Generates or returns cached native-language study help for a phrasebook category, keyed globally by category ID, target language, native language, and source-content hash. Response: `{native_help: {summary, usage_tips, register_notes, phrase_notes, common_traps, mini_glossary}}`. Returns 404 if the category does not exist and 503 if generation is unavailable or already in progress.
- **GET `/audio/{category_id}/{phrase_index}`** — Rate limit: 30/min. Auth: get_current_user. Returns cached TTS audio (audio/mpeg) for a specific phrase. Generates and caches on first request; subsequent requests serve from disk. Query param: `language`. Returns 404 if category or phrase index not found, 503 if TTS service unavailable.

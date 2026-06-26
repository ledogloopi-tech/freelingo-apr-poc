---
description: "Rate limiting strategy for FreeLingo: slowapi with Redis storage, IP-based keys, per-endpoint limits for auth, admin, LLM-heavy operations, TTS/STT, and a default global limit."
applyTo: "backend/app/main.py, backend/app/core/config.py, backend/app/core/limiter.py, backend/app/routers/**/*.py"
---

# Rate Limiting — FreeLingo

## Approach

FreeLingo uses [**slowapi**](https://github.com/laurentS/slowapi), backed by Redis via `settings.REDIS_URL`. Redis is already required for refresh tokens, so rate limiting shares the existing infrastructure and works across backend restarts or multiple backend instances.

### Configuration

| Variable | Default | Purpose |
| --- | --- | --- |
| `RATE_LIMIT_ENABLED` | `true` | Enable or disable rate limiting globally |

The global default limit is `60/minute` for endpoints without an explicit `@limiter.limit()` decorator.

### Key Strategy

All configured limits are currently **IP-based**. The limiter is initialized with `key_func=_get_real_ip`, which resolves the client key in this order:

1. `X-Real-IP`
2. First value from `X-Forwarded-For`
3. Socket client host fallback

This means authenticated users do not get separate per-user rate buckets. Multiple users behind one IP share a bucket, and one user changing IP gets a different bucket.

---

## Explicit Endpoint Limits

Only endpoints with explicit `@limiter.limit()` decorators are listed here. Everything else falls back to the global default `60/minute`.

| Endpoint | Limit | Access | Rationale |
| --- | --- | --- | --- |
| `GET /health` | 60/minute | Public | Public liveness probe with explicit protection |
| `GET /api/config` | 60/minute | Public | Public runtime flags |
| `POST /api/contact` | 5/hour | Public | Contact-form email abuse protection |
| `POST /api/auth/register` | 5/minute | Public | Account-creation abuse protection; registration may also require invite |
| `POST /api/auth/login` | 10/minute | Public | Credential brute-force protection |
| `POST /api/auth/refresh` | 60/minute | Refresh cookie | Normal SPA token rotation |
| `POST /api/auth/logout` | 60/minute | Refresh cookie | Logout endpoint protection |
| `GET /api/auth/me` | 60/minute | Authenticated | Profile fetch |
| `PATCH /api/auth/me` | 60/minute | Authenticated | Profile updates |
| `POST /api/auth/me/avatar` | 60/minute | Authenticated | Avatar upload |
| `GET /api/auth/me/avatar-file` | 60/minute | Authenticated | Private avatar retrieval |
| `DELETE /api/auth/me/avatar` | 60/minute | Authenticated | Avatar deletion |
| `DELETE /api/auth/me` | 5/minute | Authenticated | Destructive account deletion |
| `GET /api/auth/quota` | 60/minute | Authenticated | Quota status |
| `GET /api/auth/verify-email` | 60/minute | Public token | Email verification token endpoint |
| `POST /api/auth/resend-verification` | 3/minute | Authenticated | Email-sending abuse protection |
| `POST /api/auth/forgot-password` | 5/minute | Public | Email-sending and enumeration protection |
| `POST /api/auth/reset-password` | 5/minute | Public token | Reset-token brute-force protection |
| `GET /api/admin/health` | 60/minute | Admin | Dependency diagnostics |
| `GET /api/admin/stats` | 60/minute | Admin | Operational overview |
| `GET /api/admin/users` | 60/minute | Admin | User listing |
| `POST /api/admin/users` | 60/minute | Admin | User creation |
| `GET /api/admin/users/{user_id}` | 60/minute | Admin | User detail |
| `PATCH /api/admin/users/{user_id}` | 60/minute | Admin | User edit |
| `GET /api/admin/users/{user_id}/stats` | 60/minute | Admin | User stats |
| `GET /api/admin/users/{user_id}/quota` | 60/minute | Admin | User quota |
| `DELETE /api/admin/users/{user_id}` | 5/minute | Admin | Destructive account deletion |
| `POST /api/admin/invite` | 60/minute | Admin | Invite generation |
| `GET /api/admin/maintenance` | 60/minute | Admin | Maintenance state |
| `PATCH /api/admin/maintenance` | 60/minute | Admin | Maintenance toggle |
| `PUT /api/admin/maintenance` | 60/minute | Admin | Maintenance set |
| `GET /api/admin/reviews` | 60/minute | Admin | Review moderation list |
| `PATCH /api/admin/reviews/{review_id}` | 60/minute | Admin | Review moderation update |
| `DELETE /api/admin/reviews/{review_id}` | 60/minute | Admin | Review deletion |
| `POST /api/billing/checkout` | 60/minute | Authenticated | Stripe Checkout creation |
| `POST /api/billing/portal` | 60/minute | Authenticated | Stripe Customer Portal creation |
| `POST /api/billing/webhook` | 200/minute | Stripe signature | Stripe webhook burst tolerance |
| `GET /api/assessment/start` | 10/minute | Authenticated | Placement assessment start |
| `GET /api/assessment/bank` | 60/minute | Authenticated | Static bank fetch |
| `POST /api/assessment/submit` | 10/minute | Authenticated | Legacy placement submission |
| `POST /api/assessment/evaluate` | 60/minute | Authenticated | Deterministic quiz evaluation |
| `POST /api/assessment/free-write` | 10/minute | Authenticated | LLM-backed writing evaluation |
| `POST /api/assessment/complete` | 10/minute | Authenticated | Study plan creation flow |
| `GET /api/assessment/level-test/questions/{plan_id}` | 5/minute | Authenticated | LLM-backed level test generation |
| `POST /api/assessment/level-test/submit` | 10/minute | Authenticated | Level test submission |
| `GET /api/assessment/level-test/result/{plan_id}` | 60/minute | Authenticated | Level test result retrieval |
| `GET /api/languages` | 60/minute | Authenticated | Language list |
| `GET /api/languages/active` | 60/minute | Authenticated | Active language |
| `POST /api/languages` | 60/minute | Authenticated | Add learning language |
| `PUT /api/languages/active` | 60/minute | Authenticated | Switch active language |
| `DELETE /api/languages/{target_language}` | 5/minute | Authenticated | Destructive language deletion |
| `GET /api/study-plan/current` | 60/minute | Authenticated | Current plan |
| `POST /api/study-plan/generate` | 10/minute | Authenticated | Plan generation |
| `GET /api/study-plan/today` | 20/minute | Authenticated | May generate missing lesson content |
| `POST /api/study-plan/skip-day` | 60/minute | Authenticated | Plan progress mutation |
| `GET /api/study-plan/pending-lessons` | 60/minute | Authenticated | Pending lessons |
| `GET /api/lessons/{lesson_id}` | 60/minute | Authenticated | Lesson detail |
| `POST /api/lessons/{lesson_id}/start` | 60/minute | Authenticated | Lesson status mutation |
| `POST /api/lessons/{lesson_id}/complete` | 60/minute | Authenticated | Lesson completion |
| `POST /api/lessons/exercises/{exercise_id}/answer` | 20/minute | Authenticated | Exercise answer evaluation |
| `POST /api/lessons/exercises/{exercise_id}/regenerate` | 5/hour | Authenticated | LLM-backed exercise repair |
| `POST /api/lessons/exercises/{exercise_id}/native-explanation` | 10/minute | Authenticated | LLM-backed native explanation |
| `POST /api/lessons/exercises/{exercise_id}/native-hint` | 10/minute | Authenticated | LLM-backed native hint |
| `POST /api/lessons/{lesson_id}/native-explanation` | 10/minute | Authenticated | LLM-backed lesson explanation |
| `GET /api/curriculum` | 60/minute | Authenticated | Curriculum fetch |
| `GET /api/curriculum/{level}` | 60/minute | Authenticated | Curriculum by level |
| `GET /api/grammar` | 60/minute | Authenticated | Grammar list |
| `GET /api/grammar/{slug}` | 60/minute | Authenticated | Grammar detail |
| `POST /api/grammar/{slug}/native-help` | 10/minute | Authenticated | LLM-backed grammar helper |
| `GET /api/vocabulary` | 60/minute | Authenticated | Vocabulary list |
| `GET /api/vocabulary/level/{level}` | 60/minute | Authenticated | Vocabulary by level |
| `GET /api/vocabulary/{set_id}` | 60/minute | Authenticated | Vocabulary detail |
| `POST /api/vocabulary/{set_id}/native-help` | 10/minute | Authenticated | LLM-backed vocabulary helper |
| `GET /api/phrasebook` | 60/minute | Authenticated | Phrasebook list |
| `GET /api/phrasebook/level/{level}` | 60/minute | Authenticated | Phrasebook by level |
| `GET /api/phrasebook/{category_id}` | 60/minute | Authenticated | Phrasebook detail |
| `POST /api/phrasebook/{category_id}/native-help` | 10/minute | Authenticated | LLM-backed phrasebook helper |
| `GET /api/phrasebook/audio/{category_id}/{phrase_index}` | 30/minute | Authenticated | TTS phrase audio |
| `GET /api/flashcards/due` | 60/minute | Authenticated | Due cards |
| `GET /api/flashcards/all` | 60/minute | Authenticated | All cards |
| `POST /api/flashcards` | 60/minute | Authenticated | Manual card creation |
| `POST /api/flashcards/bulk` | 60/minute | Authenticated | Bulk card creation |
| `POST /api/flashcards/{card_id}/review` | 60/minute | Authenticated | SM-2 review |
| `POST /api/flashcards/generate` | 20/minute | Authenticated | LLM-backed card generation |
| `POST /api/flashcards/from-word` | 30/minute | Authenticated | LLM-backed word lookup |
| `GET /api/flashcards/vocabulary` | 60/minute | Authenticated | Saved vocabulary cards |
| `DELETE /api/flashcards/{card_id}` | 60/minute | Authenticated | Card deletion |
| `GET /api/progress/summary` | 60/minute | Authenticated | Progress summary |
| `GET /api/progress/history` | 60/minute | Authenticated | Progress history |
| `GET /api/progress/competencies` | 60/minute | Authenticated | Competencies |
| `GET /api/chat/conversations` | 60/minute | Subscription + no maintenance | Conversations list |
| `POST /api/chat/conversations` | 60/minute | Subscription + no maintenance | Conversation creation |
| `DELETE /api/chat/conversations/{conversation_id}` | 60/minute | Subscription + no maintenance | Conversation deletion |
| `GET /api/chat/conversations/{conversation_id}/messages` | 60/minute | Subscription + no maintenance | Conversation messages |
| `POST /api/chat` | 30/minute | Subscription + no maintenance | SSE chat generation |
| `GET /api/chat/history` | 60/minute | Subscription + no maintenance | Legacy chat history |
| `POST /api/conversation/warmup` | 20/minute | Subscription + no maintenance | TTS/STT warmup |
| `POST /api/tts` | 20/minute | Authenticated | Audio generation |
| `GET /api/tts/preview/{voice}` | 60/minute | Authenticated | Voice preview |
| `POST /api/stt` | 20/minute | Authenticated | Audio transcription |
| `GET /api/listening/next` | 10/minute | Subscription + no maintenance | Listening exercise pool |
| `POST /api/listening/generate` | 5/minute | Subscription + no maintenance | LLM+TTS exercise generation |
| `GET /api/listening/audio/{exercise_id}` | 60/minute | Subscription + no maintenance | Exercise audio |
| `POST /api/listening/attempt` | 20/minute | Subscription + no maintenance | Attempt scoring |
| `GET /api/listening/history` | 60/minute | Subscription + no maintenance | Attempt history |
| `GET /api/reading/next` | 10/minute | Subscription + no maintenance | Reading exercise pool |
| `POST /api/reading/generate` | 5/minute | Subscription + no maintenance | LLM exercise generation |
| `POST /api/reading/attempt` | 20/minute | Subscription + no maintenance | Attempt scoring |
| `GET /api/reading/history` | 60/minute | Subscription + no maintenance | Attempt history |
| `GET /api/memories` | 60/minute | Subscription | Memory list |
| `DELETE /api/memories/{memory_id}` | 60/minute | Subscription | Single memory deletion |
| `DELETE /api/memories` | 10/minute | Subscription | Bulk memory deletion |
| `GET /api/feedback` | 60/minute | Authenticated | Feedback list |
| `POST /api/feedback` | 10/hour | Authenticated | Feedback creation |
| `GET /api/feedback/{entry_id}` | 60/minute | Authenticated | Feedback detail |
| `DELETE /api/feedback/{entry_id}` | 60/minute | Authenticated | Feedback deletion |
| `POST /api/feedback/{entry_id}/vote` | 60/minute | Authenticated | Vote toggle |
| `PATCH /api/feedback/{entry_id}/status` | 60/minute | Admin | Status update |
| `GET /api/feedback/{entry_id}/comments` | 60/minute | Authenticated | Comment list |
| `POST /api/feedback/{entry_id}/comments` | 20/hour | Authenticated | Comment creation |
| `DELETE /api/feedback/{entry_id}/comments/{comment_id}` | 60/minute | Authenticated | Comment deletion |
| `GET /api/reviews/me` | 60/minute | Authenticated | Current user's review |
| `POST /api/reviews` | 5/hour | Authenticated | Review creation |
| `PATCH /api/reviews/me` | 10/hour | Authenticated | Review update |
| `DELETE /api/reviews/me` | 10/hour | Authenticated | Review deletion |
| `GET /api/reviews/public` | 60/minute | Public | Landing reviews |

---

## WebSocket Rate Limiting

The WebSocket conversation endpoint (`/ws/conversation`) is **not decorated with slowapi**. Protection is handled by:

- JWT authentication in the first JSON message after connection accept
- Subscription checks when Stripe is enabled
- Maintenance-mode rejection for non-admin users
- Session max-duration and inactivity timeouts
- Conversation quota checks in the voice pipeline

---

## Error Response Format

On rate limit exceed, slowapi returns:

- **HTTP status**: `429 Too Many Requests`
- **Header**: `Retry-After: <seconds>` when provided by the limiter backend
- **Body**: `{ "detail": "Rate limit exceeded: ..." }`

Frontend code should not trigger token refresh for `429` responses; only `401` should attempt silent refresh.

---

## Self-hosted Considerations

- Defaults are intended to prevent accidental or malicious bursts without blocking normal self-hosted usage.
- Because the key is IP-based, users behind one NAT share limits.
- Set `RATE_LIMIT_ENABLED=false` only for trusted development or private deployments where limits are undesirable.

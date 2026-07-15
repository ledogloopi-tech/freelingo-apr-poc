# APR Day 1 Findings

## Decision

Day 2 readiness decision: READY WITH CONSTRAINTS.

## Confirmed by execution

- A local branch named `apr/poc-primeira-conexao` was created or selected.
- The local checkout has no configured Git remote and no local tags. Therefore `v1.8.24` was not found locally and its exact tag commit could not be resolved from this checkout.
- Docker is not installed in this Codex environment. The documented Docker Compose application start could not be attempted beyond checking Docker availability.
- Backend tests did not run because the repository-local `.venv` Python environment was missing.
- Frontend validation passed with `cd frontend && npm run lint && npx tsc --noEmit && npm run test:run`. Vitest reported 33 test files and 420 tests passing.

## Confirmed by source-code inspection

- STT has a standalone backend router and service separate from the WebSocket conversation pipeline: `backend/app/routers/stt.py` and `backend/app/services/stt_service.py`.
- TTS has a standalone backend router and service separate from the WebSocket conversation pipeline: `backend/app/routers/tts.py` and `backend/app/services/tts_service.py`.
- The conversation pipeline composes STT, LLM, and TTS for real-time WebSocket conversation, but the provider services are not only embedded there.
- The LLM layer is centralized in `backend/app/services/llm_adapter.py`, with prompt builders in `backend/app/services/prompts/`. APR-specific prompts should be feasible as a separate constrained prompt path.
- Authentication is implemented separately from assessment and study-plan generation. It should be possible to authenticate a user without APR using CEFR placement, although the existing FreeLingo UI currently routes users toward onboarding and assessment flows.
- Existing progress is tightly tied to XP and streak concepts. APR should create a separate progress/evidence model rather than adapting FreeLingo's current progress model.
- Existing learner-generated audio is generally streamed or submitted for processing. Listening exercise audio storage preserves generated listening MP3 files, not original learner recordings. APR will need explicit storage for original learner attempts and retries.
- Conversation transcripts are persisted as chat history entries, but this is not the same as APR academic evidence with separate technical failure states.

## Documented but not verified

- README and `.env.example` document local and OpenAI provider options for LLM, TTS, and STT.
- README documents Docker Compose deployment with PostgreSQL, Redis, backend, frontend, Kokoro, and Whisper.
- AGENTS.md documents FreeLingo version state as v1.8.24, but the corresponding Git tag was not present locally.

## Inferred

- APR can have a separate route under the Next.js app and separate backend routers/models without depending on XP or streaks.
- APR can preserve original learner recording, editable transcript, confirmed transcript, feedback, retry recording, and failure status if new APR-specific tables and file/object storage paths are added.
- APR should treat STT output as draft text, not academic evidence, until the learner confirms or edits it.

## Blocked

- Starting the application was blocked by missing Docker.
- Backend tests were blocked by missing `.venv`.
- Resolving the exact `v1.8.24` tag commit was blocked by missing local tag and missing configured remote.
- Live LLM/STT/TTS calls were intentionally not performed because the audit must not use paid services or credentials.

## Not found

- No existing APR-specific route, model, or authored APR lesson system was found.
- No existing model dedicated to preserving original learner audio attempts and retries as academic evidence was found.
- No Brazilian Portuguese target language package was found; the current Portuguese support is `pt-PT`, and prompt guidance explicitly avoids Brazilian Portuguese in the European Portuguese path.

## Five largest architectural risks

1. FreeLingo's main learner flow is built around CEFR placement, generated study plans, XP, and streaks, all of which APR wants to avoid.
2. Current real-time conversation is intentionally broad and interactive; APR needs controlled turn-based evidence with transcript confirmation and retry boundaries.
3. Audio evidence storage for original learner recordings and retries is not already modeled for APR.
4. Existing Portuguese support is European Portuguese, not Brazilian Portuguese, so APR must avoid inheriting incorrect language defaults.
5. Deployment and backend test validation could not be fully verified in this environment because Docker and `.venv` were unavailable.

## Day 2 recommendation

Proceed to Day 2 only with constraints: design APR as a separate module with its own routes, models, storage paths, and prompt contract. Reuse FreeLingo infrastructure where it is generic: auth, database, migrations, API conventions, STT/TTS adapters, LLM adapter, and selected UI primitives.

# APR FreeLingo Dependency Map

## High-level map

FreeLingo is a FastAPI backend plus Next.js frontend. It already contains accounts, database models, migrations, lessons, progress, STT, TTS, LLM adapters, audio recording components, and WebSocket conversation code.

## APR-relevant reusable foundation

- Authentication: `backend/app/routers/auth.py`, `backend/app/core/security.py`, `backend/app/core/deps.py`, `backend/app/models/user.py`, `frontend/src/store/auth.ts`, `frontend/src/lib/api.ts`.
- Database and migrations: `backend/app/core/database.py`, `backend/app/core/config.py`, `backend/alembic/env.py`, `backend/alembic/versions/`.
- STT: `backend/app/routers/stt.py`, `backend/app/services/stt_service.py`, `frontend/src/app/api/stt/route.ts`.
- TTS: `backend/app/routers/tts.py`, `backend/app/services/tts_service.py`, `frontend/src/app/api/tts/route.ts`.
- LLM adapter and prompts: `backend/app/services/llm_adapter.py`, `backend/app/services/prompts/`.
- Recording UI primitives: `frontend/src/components/ui/VoiceRecorder.tsx`, `frontend/src/lib/audio.ts`.
- Existing transcript persistence pattern: `backend/app/models/chat_history.py`, `backend/app/services/conversation_pipeline.py`.

## Systems APR should avoid depending on directly

- CEFR placement and level tests: `backend/app/routers/assessment.py`, `backend/app/services/assessment.py`, `frontend/src/app/(app)/assessment/`.
- AI-generated study plans: `backend/app/routers/study_plan.py`, `backend/app/services/study_plan_generator.py`.
- AI-generated lessons: `backend/app/services/lesson_generator.py`.
- XP and streaks: `backend/app/models/progress.py`, `backend/app/services/progress_service.py`, `frontend/src/app/(app)/progress/page.tsx`.
- Subscriptions and quotas: `backend/app/routers/billing.py`, `backend/app/services/subscription_service.py`, `backend/app/services/quota_service.py`.
- Unrestricted real-time conversation: `backend/app/routers/conversation.py`, `backend/app/services/conversation_pipeline.py`, `frontend/src/app/(app)/conversation/page.tsx`, `frontend/src/lib/conversation-ws.ts`.

## Initial architecture conclusion

APR can likely use FreeLingo as a foundation if it adds a separate APR route, separate APR data models, and a constrained APR feedback service. The safest path is to reuse auth, database, migrations, provider adapters, and selected UI primitives, while not reusing FreeLingo's CEFR placement, generated curriculum, XP/streak progress, subscriptions, or unrestricted WebSocket conversation flow as APR academic evidence.

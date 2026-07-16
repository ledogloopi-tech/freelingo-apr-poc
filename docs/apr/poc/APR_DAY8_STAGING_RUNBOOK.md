# APR Day 8 Staging Runbook

1. Purpose: prepare a private APR technical smoke environment without making APR public.
2. Current repository deployment architecture: FastAPI backend, Next.js frontend, PostgreSQL, Redis, optional local Kokoro TTS, optional local faster-whisper STT, and Docker Compose files for container startup.
3. Hosted preview mechanism: no repository-native hosted preview provider configuration was found; external deployment remains an operational decision.
4. Required services: backend, frontend, PostgreSQL, Redis, STT provider, TTS provider.
5. Required environment variables: `DATABASE_URL`, `REDIS_URL`, `SECRET_KEY`, `CORS_ORIGINS`, `APP_BASE_URL`, `STT_PROVIDER`, `STT_BASE_URL`, `TTS_PROVIDER`, `TTS_BASE_URL`, `APR_TTS_VOICE`, `OPENAI_API_KEY`, `OPENAI_TTS_MODEL`, `OPENAI_TTS_VOICE`, `OPENAI_STT_MODEL`, `STRIPE_BASE_URL` when billing links are used, and `APR_POC_ENABLED` when applicable.
6. APR default: `APR_POC_ENABLED=false` keeps APR unavailable by default.
7. Private staging enablement: set `APR_POC_ENABLED=true` only in the private staging environment.
8. Authentication: sign in with an authorized user; APR routes use normal authenticated API access.
9. Database: PostgreSQL is required for the application even though APR Day 8 creates no APR tables or migrations.
10. STT: configure local or OpenAI STT before testing transcript drafts.
11. TTS: configure local or OpenAI TTS before testing model audio.
12. APR TTS voice: local TTS requires explicit `APR_TTS_VOICE`; do not rely on a generic fallback.
13. Frontend startup: use the repository frontend build/start process for the chosen environment.
14. Backend startup: start the FastAPI backend with required environment values and migrations already handled by the normal app startup path.
15. Docker or compose startup: container operators can use the existing compose files; local developer machines for this fork may not have Docker.
16. Exact local staging-style commands: backend checks use `source .venv/bin/activate && cd backend && pytest tests/test_apr.py -v --no-cov`; frontend checks use `cd frontend && npm run lint && npx tsc --noEmit && npm run test:run -- apr-primeira-conexao.test.tsx apr-lesson-player.test.tsx apr-audio-recorder.test.tsx apr-transcript-confirmation.test.tsx apr-model-audio.test.tsx apr-feedback-retry.test.tsx apr-session-closure.test.tsx`.
17. Exact APR route: `/apr/primeira-conexao/lessons/enter-the-connection`.
18. Login requirement: log in before opening the APR route.
19. Technical smoke test: navigate through orientation, information, choice, recording, reflection, and closure.
20. Session-closure smoke test: verify the heading `Technical session ready for review` and the six summary rows.
21. Mobile-width check: inspect the closure at a narrow viewport and confirm readable rows and buttons.
22. Microphone permission check: permission is requested only after pressing Start recording.
23. Transcription check: request a draft only after Original recording; confirm it is optional.
24. Model-audio check: generate audio only by explicit action; no autoplay.
25. Feedback check: confirm Original transcript, request feedback, and verify it remains technical.
26. Retry check: record a retry before and after feedback to verify post-feedback status.
27. Exit and Restart check: exit routes to `/apr/primeira-conexao`; cancelled Restart preserves state; confirmed Restart clears state.
28. Logs to inspect: backend application logs, frontend build/runtime logs, STT/TTS provider logs, reverse-proxy logs if present.
29. Rollback: set `APR_POC_ENABLED=false` or revert the Day 8 branch deployment.
30. Secret-handling rules: do not commit real secrets; store credentials only in the private environment secret manager or operator-controlled environment.
31. Known blockers: no hosted preview provider is defined in the repository; a private URL cannot be claimed until an operator deploys one.
32. Hosted staging readiness: READY WITH CONSTRAINTS.

# APR Day 1 Runbook

## Purpose

This runbook records what was attempted during the Day 1 repository audit for using FreeLingo as a technical foundation for an Academia Português Reconectado proof of concept. No product behavior was changed.

## Branch and tag checks

- Working branch created or selected: `apr/poc-primeira-conexao`.
- Git tag checked: `v1.8.24`.
- Exact tag commit recorded in `APR_DAY1_INVENTORY.json`.

## Repository instructions inspected

- `AGENTS.md`
- `README.md`
- `CONTRIBUTING.md`
- `CONTRIBUTOR_LICENSE_AGREEMENT.md`
- `.env.example`
- `docker-compose.yml`
- `backend/Dockerfile`
- `frontend/Dockerfile`
- `frontend/Dockerfile.dev`
- `scripts/format.sh`
- `scripts/pre-push.sh`

## Application start attempt

Documented production start command is `docker compose up -d` after preparing `.env` and host services.

Attempted checks:

```bash
docker --version
docker compose version
```

Result: blocked. Docker is not installed in this Codex environment, so the app was not started. This is an environment blocker, not evidence that the repository cannot start on a proper Docker host.

## Test and validation attempts

Commands attempted:

```bash
if [ -f .venv/bin/activate ]; then source .venv/bin/activate && cd backend && pytest -q; else echo '.venv missing'; fi
```

Result: blocked. The repository-local Python virtual environment `.venv` was not present, so backend tests were not run.

```bash
cd frontend && npm run lint && npx tsc --noEmit && npm run test:run
```

Result: passed. Frontend lint, TypeScript type-checking, and Vitest tests completed successfully. Vitest reported 33 test files and 420 tests passing.

## Paid services and secrets

No live paid LLM, STT, or TTS calls were performed. No paid credentials were requested. No secrets were printed beyond inspecting placeholder values already present in `.env.example`.

## Day 2 suggested local/CI checks

On an environment that is intended to run FreeLingo, validate with:

- Docker availability and compose start.
- Backend Python environment creation.
- Backend unit tests.
- Frontend lint, type-check, and tests.
- A non-paid mocked STT/TTS/LLM integration test for the APR turn-based flow before any real provider is used.

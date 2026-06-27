---
name: pre-push
description: Use when the user asks to check before pushing, pre-push, verificar antes de pushear, run all checks, or quiere validar que todo pasa antes de hacer push. Auto-formats code then runs the same checks as CI (pytest, eslint, tsc).
---

# Pre-Push Checks — FreeLingo

Auto-formats code, then validates everything CI enforces on `develop`. Mirrors `.github/workflows/pr-develop-checks.yml`.

## Order

Run in this sequence, stopping on first failure:

### 0. Auto-format (always run first)

```bash
source .venv/bin/activate && cd backend && ruff check --fix . && black . && cd ../frontend && npx eslint src/ --ext .ts,.tsx --fix && npx prettier --write src/
```

Fixes what can be fixed automatically: Python lint + format, JS/TS lint + format.

### 1. Backend tests

```bash
source .venv/bin/activate && cd backend && pytest -v
```

919 backend tests, >= 70% backend coverage required. Current backend coverage is 85.06% last measured. SQLite in-memory, no Docker needed.

Use a command timeout of at least 600 seconds for the full backend suite; the current run takes about 4 minutes and can exceed shorter 120-second tool defaults.

### 2. Frontend lint + typecheck + tests

```bash
cd frontend && npm run lint && npx tsc --noEmit && npm run test:run
```

## What each step does

- Step 0: `ruff --fix` auto-fixes Python lint issues.
- Step 0: `black` auto-formats Python code.
- Step 0: `eslint --fix` auto-fixes JS/TS lint issues.
- Step 0: `prettier --write` auto-formats JS/TS/CSS code.
- Step 1: `pytest` runs 919 backend tests with SQLite in-memory.
- Step 2: `eslint` verifies no remaining JS/TS lint errors.
- Step 2: `tsc --noEmit` runs TypeScript type checking.
- Step 2: `vitest` runs 419 frontend tests; frontend coverage is not configured.

**Note:** CI does not run ruff/black checks — only pytest, eslint, tsc, and vitest. Backend lint (ruff/black) is kept in step 0 as auto-format only.

## Requirements

- `.venv/` at project root (create once: `python3 -m venv .venv && source .venv/bin/activate && pip install -r backend/requirements.txt`)
- `frontend/node_modules` exists (install once: `cd frontend && npm install`)

## If something fails

1. If step 0 fails, fix manually — it means auto-fix couldn't handle something
2. If steps 1-2 fail after step 0 passed, the issue needs manual fix
3. Re-run **only the failing step** (no need to restart from step 0)
4. Once all pass, the branch is safe to push

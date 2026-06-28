#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

"${ROOT_DIR}/scripts/format.sh"

source "${ROOT_DIR}/.venv/bin/activate"

pushd "${ROOT_DIR}/backend" >/dev/null
pytest -v
popd >/dev/null

pushd "${ROOT_DIR}/frontend" >/dev/null
npm run lint
npx tsc --noEmit
npm run test:run
popd >/dev/null

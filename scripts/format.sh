#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

source "${ROOT_DIR}/.venv/bin/activate"

pushd "${ROOT_DIR}/backend" >/dev/null
ruff check --fix .
black .
popd >/dev/null

pushd "${ROOT_DIR}/frontend" >/dev/null
npx eslint src/ --ext .ts,.tsx --fix
npx prettier --write src/
popd >/dev/null

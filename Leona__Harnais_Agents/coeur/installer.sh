#!/usr/bin/env bash
# Installe les outils gratuits du harnais dans coeur/ (idempotent) : venv Python, Chromium Playwright, html-validate, lychee.
set -euo pipefail
C="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)"; cd "$C"
if command -v uv >/dev/null; then [ -x .venv/bin/python ] || uv venv -q .venv; uv pip install -q --python .venv/bin/python -r requirements.txt
else [ -x .venv/bin/python ] || python3 -m venv .venv; .venv/bin/pip install -q -r requirements.txt; fi
if [ "${HARNAIS_DEPS_SYSTEME:-0}" = 1 ]; then .venv/bin/python -m playwright install --with-deps chromium; else .venv/bin/python -m playwright install chromium; fi
mkdir -p node; [ -f node/package.json ] || (cd node && npm init -y >/dev/null)
[ -x node/node_modules/.bin/html-validate ] || (cd node && npm i -s html-validate@11.21.0)
mkdir -p outils_bin
if [ ! -x outils_bin/lychee ]; then
  curl -sSfL https://github.com/lycheeverse/lychee/releases/download/lychee-v0.24.2/lychee-x86_64-unknown-linux-gnu.tar.gz | tar xz -C outils_bin --strip-components=1 --wildcards '*/lychee' \
  || curl -sSfL https://github.com/lycheeverse/lychee/releases/latest/download/lychee-x86_64-unknown-linux-gnu.tar.gz | tar xz -C outils_bin --strip-components=1 --wildcards '*/lychee'
fi
command -v rg >/dev/null || echo "AVERTISSEMENT : ripgrep absent (apt-get install -y ripgrep)"
command -v pdftotext >/dev/null || echo "AVERTISSEMENT : poppler-utils absent (apt-get install -y poppler-utils)"
chmod +x bin/harnais harnais.py ../surveillance/*.sh 2>/dev/null || true
echo "installer.sh : OK"

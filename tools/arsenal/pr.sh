#!/usr/bin/env bash
# pr.sh "<titre>" [SSP …] : rebase origin/main, régénère (mono_build, cours/appliquer <SSP>, ck_build),
# vérifie lot.py auto, pousse, ouvre la PR avec la section « Automates actifs ». Sortie : l'URL seule.
set -euo pipefail
t=${1:?titre}; shift || true
cd "$(git rev-parse --show-toplevel)"
b=$(git rev-parse --abbrev-ref HEAD)
git fetch -q origin main && git rebase -q origin/main
python3 tools/mono_build.py >/dev/null
for s in "$@"; do python3 tools/cours/appliquer.py "$s" >/dev/null; done
python3 tools/ck_build.py >/dev/null 2>&1 || python3 tools/ck_build.py
git add -A assets data && { git diff --cached --quiet || git commit -qm "Régénération (arsenal/pr.sh)"; }
python3 tools/arsenal/lot.py auto
git push -q --force-with-lease -u origin "$b" 2>/dev/null
auto=$(git diff --name-only origin/main...HEAD | grep -E '^tools/.*\.(py|sh)$' | sed 's/.*/- `&`/' || true)
auto=$(printf '%s\n- `tools/arsenal/lot.py`\n- `tools/arsenal/ci_attente.sh`' "$auto")
u=$(gh pr view "$b" --json url -q .url 2>/dev/null || true)
[ -n "$u" ] || u=$(gh pr create -B main -H "$b" -t "$t" -b "$(printf '## Automates actifs\n%s\n\n## Objet\nAudit : `python3 tools/arsenal/audit_diff.py`' "$auto")")
echo "$u"

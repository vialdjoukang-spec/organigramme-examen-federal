#!/usr/bin/env bash
# Chaîne complète : parse → mapping → dry-run → injection (stage) → idempotence → vérification → annexe.
set -euo pipefail
cd "$(dirname "$0")/.."
MHT=${1:-/home/box/agent-data/agents/db322130-de1f-49d9-a669-bd9b54729c37/attachments/60a804b6baf1e8df1e3a2695482b70ab1eac38651dd4c5c13cfb1bc0d201a07d.mht}
git -C /workspace/grok/etude/repo fetch -q origin main:refs/remotes/origin/main
git -C /workspace/grok/etude/repo show origin/main:ChatGPT_Codex/_outils/controle3.py > scripts/_controle3_main.py
python3 scripts/parse_mht.py "$MHT" out > /dev/null
python3 scripts/mapping.py
python3 scripts/inject.py --dry-run
rm -rf out/stage && python3 scripts/inject.py --apply
cp out/inject_journal.json /tmp/_j && cp out/INJECTION.md /tmp/_i && cp out/CONFLITS.md /tmp/_c
rm -rf out/stage0 && cp -r out/stage out/stage0 && python3 scripts/inject.py --apply --base out/stage0 > /dev/null
diff -r out/stage0 out/stage > /dev/null && echo "IDEMPOTENCE : 0 diff" || { echo "IDEMPOTENCE : ÉCHEC"; exit 1; }
cp /tmp/_j out/inject_journal.json && cp /tmp/_i out/INJECTION.md && cp /tmp/_c out/CONFLITS.md && rm -rf out/stage0
python3 scripts/verifier.py | tail -1
python3 scripts/annexe_md.py out/REFERENTIEL_EPIDEMIO_PROFILES.md > /dev/null
cp out/REFERENTIEL_EPIDEMIO_PROFILES.md /workspace/Leona__Brief_Redaction_LOTs_20261115/

#!/usr/bin/env bash
# INSTALLER — à lancer une fois au début d'une nouvelle session (machine vierge) : restaure caches et garde-fous.
#   bash Claude/_harnais/installer.sh
set -e
H=$(cd "$(dirname "$0")" && pwd)
mkdir -p ~/.cache/medina_aips ~/.cache/medina_sources ~/.claude/hooks
cp -u "$H/donnees/AipsDownload_20261008.zip" "$H/donnees/aips_corpus_index.json" ~/.cache/medina_aips/
mv -f ~/.cache/medina_aips/aips_corpus_index.json ~/.cache/medina_aips/corpus_index.json
cp -u "$H/verrou_medina.py" ~/.claude/hooks/
[ -f ~/.claude/settings.json ] || cat > ~/.claude/settings.json <<'J'
{"hooks":{"PreToolUse":[{"matcher":"*","hooks":[{"type":"command","command":"python3 /root/.claude/hooks/verrou_medina.py"}]}]}}
J
python3 -m py_compile "$H"/*.py
(cd "$H/../.." && python3 Claude/_harnais/aips_fiche.py trouve Mestinon | head -1)
echo "Harnais installé. Veille : nohup bash Claude/_harnais/veille_harnais.sh 23 24 25 >/dev/null 2>&1 &"

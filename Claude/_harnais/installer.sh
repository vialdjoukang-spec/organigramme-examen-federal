#!/usr/bin/env bash
# INSTALLER — à lancer une fois au début d'une nouvelle session (machine vierge) : restaure caches et garde-fous.
#   bash Claude/_harnais/installer.sh
set -e
H=$(cd "$(dirname "$0")" && pwd)
mkdir -p ~/.cache/medina_aips ~/.cache/medina_sources ~/.claude/hooks
cp -u "$H/donnees/AipsDownload_20261008.zip" "$H/donnees/aips_corpus_index.json" ~/.cache/medina_aips/
mv -f ~/.cache/medina_aips/aips_corpus_index.json ~/.cache/medina_aips/corpus_index.json
cp -u "$H/verrou_medina.py" "$H/verrou_lecture.py" ~/.claude/hooks/
python3 - <<'PY'
import json, os
p = os.path.expanduser('~/.claude/settings.json')
try: s = json.load(open(p))
except Exception: s = {}
pre = s.setdefault('hooks', {}).setdefault('PreToolUse', [])
bloc = next((b for b in pre if b.get('matcher') == '*'), None)
if bloc is None: bloc = {'matcher': '*', 'hooks': []}; pre.append(bloc)
for v in ('verrou_medina', 'verrou_lecture'):
    c = f'python3 /root/.claude/hooks/{v}.py'
    if not any(h.get('command') == c for h in bloc['hooks']): bloc['hooks'].append({'type': 'command', 'command': c})
json.dump(s, open(p, 'w'), indent=1)
print('Verrous actifs :', [h['command'].split('/')[-1] for h in bloc['hooks']])
PY
python3 -m py_compile "$H"/*.py
(cd "$H/../.." && python3 Claude/_harnais/aips_fiche.py trouve Mestinon | head -1)
echo "Harnais installé. Veille : nohup bash Claude/_harnais/veille_harnais.sh 23 24 25 >/dev/null 2>&1 &"

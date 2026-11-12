#!/usr/bin/env python3
"""VERROU_LECTURE — crochet PreToolUse : transforme l'alerte G3 du Gaspillon en blocage réel.
Refuse la lecture intégrale d'un HTML de plus de 50 Ko (Read sans `limit`, ou `cat` d'un .html) : première fuite
mesurée (≈ 150 M éq.). Voie permise : extrait.py plan|point|cherche, Read avec limit, grep ciblé. Code 2 = refus motivé.
"""
import sys, json, os, re
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
n, i = d.get('tool_name'), d.get('tool_input') or {}
cand = []
if n == 'Read' and not i.get('limit'):
    cand = [i.get('file_path', '')]
elif n == 'Bash':
    cand = re.findall(r'(?:^|[;&|]\s*)cat\s+([^\s;&|<>]+\.html?)\b', i.get('command', '') or '')
for p in cand:
    q = p if os.path.isabs(p) else os.path.join(d.get('cwd') or os.getcwd(), p)
    if p.endswith(('.html', '.htm')) and os.path.exists(q) and os.path.getsize(q) > 50000:
        print(f'VERROU LECTURE : {os.path.basename(p)} fait {os.path.getsize(q)//1000} Ko. '
              'Lis par morceaux : extrait.py plan <fichier> · point <fichier> N · cherche <fichier> <motif> (ou Read avec limit).', file=sys.stderr)
        sys.exit(2)
sys.exit(0)

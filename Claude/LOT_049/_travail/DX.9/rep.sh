cd /home/user/wt/lot-049; export PAQUET_CACHE=/tmp/claude_paquet_cache
L=/home/user/organigramme-examen-federal/Claude/_outils/lecon.py; D=Claude/LOT_049/_travail/DX.9
(cd $D && python3 conv.py)
python3 $L finir --lot 049 --cible DX.9 --ex 100 --titre "DX.9 — Pneumothorax spontané (dont pneumothorax compressif)" 2>&1 | head -3 | cut -c1-300
python3 - <<'P'
import json
R=json.load(open('Claude/LOT_049/_travail/DX.9/controle.json'))[0]
for k,v in R['defauts'].items():
    print('##',k,v['n'])
    for e in v['ex']: print('  ',e[:200])
P

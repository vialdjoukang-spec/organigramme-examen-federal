cd /home/user/wt/lot-050; export PAQUET_CACHE=/tmp/claude_paquet_cache
python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 050 --cible DX.3 --titre "DX.3 — Fibrillation atriale" --ex 60 > /tmp/claude-0/dx3_fin.txt 2>&1
python3 - <<'P'
import json
r=json.load(open('/home/user/wt/lot-050/Claude/LOT_050/_travail/DX.3/controle.json'))
r=r[0] if isinstance(r,list) else r
print({k:r[k] for k in ('verdict','octets','connecteur%','paragraphes_sans_connecteur')})
for k,v in r['defauts'].items():
    print(k,v['n'])
    if k.startswith(('A_','C_','B_phrase_part','B_phrase_dup')) : 
        for e in v['ex']: print('   ',e[:230])
P

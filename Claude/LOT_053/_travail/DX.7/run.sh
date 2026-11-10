cd /home/user/wt/lot-053; export PAQUET_CACHE=/tmp/claude_paquet_cache
python3 Claude/LOT_053/_travail/DX.7/conv.py
python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 053 --cible DX.7 --titre "DX.7 — Ascite maligne (carcinose péritonéale, notamment cancer de l'ovaire)" >/dev/null 2>&1
cd Claude/LOT_053; python3 /home/user/organigramme-examen-federal/Claude/_outils/controle3.py LOT_053_Phase_B_V0_DX.7.html --paquet _travail/DX.7/paquet.json --points 14 --min 100000 --max 200000 --ex 80 > /tmp/claude_c.json 2>&1
python3 - <<'P'
import json
s=open('/tmp/claude_c.json').read()
c=json.loads(s[s.index('['):] if s.lstrip().startswith('[') else s[s.index('{'):])
c=c[0] if isinstance(c,list) else c
print(c['verdict'],c['octets'],c['connecteur%'],c['paragraphes_sans_connecteur'])
d=c['defauts']
for k in d:
    print('##',k,d[k]['n'])
    for x in d[k]['ex']: print('  ',x[:int(__import__('os').environ.get('W','170'))])
P

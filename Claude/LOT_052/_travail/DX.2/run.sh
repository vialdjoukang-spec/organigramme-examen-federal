cd /home/user/wt/lot-052/Claude/LOT_052/_travail/DX.2 && for f in p1_3 p4_6 p7_9 p10_11 p12_14; do python3 $f.py 2>&1 | tail -2 | cut -c1-200; done
cd /home/user/wt/lot-052; export PAQUET_CACHE=/tmp/claude_paquet_cache
python3 Claude/_outils/lecon.py finir --lot 052 --cible DX.2 --titre "DX.2 — Lithiase biliaire symptomatique (colique biliaire, cholécystite aiguë)" > /dev/null 2>&1
python3 - <<'P'
import json
R=json.load(open('Claude/LOT_052/_travail/DX.2/controle.json'))[0]
print({k:R[k] for k in ('verdict','octets','connecteur%','paragraphes_sans_connecteur')})
for k,v in R['defauts'].items(): print(k,v['n'])
P

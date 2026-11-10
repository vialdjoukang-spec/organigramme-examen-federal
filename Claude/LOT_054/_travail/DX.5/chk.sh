cd /home/user/wt/lot-054; export PAQUET_CACHE=/tmp/claude_paquet_cache
(cd Claude/LOT_054/_travail/DX.5 && python3 build.py)
python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 054 --cible DX.5 --titre "DX.5 — Anévrisme de l'aorte abdominale" >/dev/null 2>&1
python3 /home/user/organigramme-examen-federal/Claude/_outils/controle3.py Claude/LOT_054/LOT_054_Phase_B_V0_DX.5.html --paquet Claude/LOT_054/_travail/DX.5/paquet.json --ex 200 > /tmp/claude_paquet_cache/c.json
python3 - <<'P'
import json,re,html
r=json.load(open('/tmp/claude_paquet_cache/c.json'))[0]
print(r['verdict'],r['octets'],r['connecteur%'],r['paragraphes_sans_connecteur'],r['phrases'])
for k,v in r['defauts'].items():
    print('==',k,v['n'])
    for e in v['ex']: print('  ',e)
# paragraphes sans connecteur
import sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
h=open('Claude/LOT_054/LOT_054_Phase_B_V0_DX.5.html').read()
for p in re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S):
    t=c.texte(p)
    if len(t.split())>40 and not c.CONNECT.search(t): print('SANSCONN:',t[:110])
P

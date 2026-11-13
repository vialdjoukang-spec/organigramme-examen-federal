cd /home/user/wt/lot-045/Claude/LOT_045/_travail/DX.3
python3 /tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils/controle3.py "$@" --paquet paquet.json --ex 8 --min 0 --max 999999 --points 0 2>&1 | python3 -c "
import sys,json
t=sys.stdin.read()
try:
  for r in json.loads(t):
    print(r['fichier'],r['octets'],r['verdict'],'conn',r['connecteur%'],'sansconn',r['paragraphes_sans_connecteur'])
    for k,v in r['defauts'].items():
        if k.startswith('C_'): continue
        print(' ',k,v['n']); [print('    ',e) for e in v['ex']]
except Exception as e: print(t[:2000])
"

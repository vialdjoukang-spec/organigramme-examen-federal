import json,sys,re
d=json.load(open('/home/user/wt/lot-054/Claude/LOT_054/_travail/PA/paquet.json'))
P={p['id']:p['texte'] for p in d['passages']}
pre=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 900
pat=re.compile(sys.argv[3],re.I) if len(sys.argv)>3 else None
for k in sorted((k for k in P if k.startswith(pre)), key=lambda x:int(x.split('-')[-1])):
    if pat and not pat.search(P[k]): continue
    print(k,P[k][:n]);print()

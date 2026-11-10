import json,re,sys
p=json.load(open('/home/user/wt/lot-047/Claude/LOT_047/_travail/DX.10/paquet.json'))
pre=sys.argv[1]; pat=re.compile(sys.argv[2],re.I) if len(sys.argv)>2 else None
for x in p['passages']:
    if x['id'].startswith(pre) and (not pat or pat.search(x['texte'])): print('['+x['id']+']',x['texte'][:1100],'\n')

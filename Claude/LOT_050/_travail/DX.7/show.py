import json,sys
p=json.load(open('/home/user/wt/lot-050/Claude/LOT_050/_travail/DX.7/paquet.json'))
pre=sys.argv[1]; mx=int(sys.argv[2]) if len(sys.argv)>2 else 900
for x in p['passages']:
    if x['id'].startswith(pre+'-'): print('['+x['id']+']',x['texte'][:mx])

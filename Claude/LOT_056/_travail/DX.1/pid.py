import json,sys
d=json.load(open('/home/user/wt/lot-056/Claude/LOT_056/_travail/DX.1/paquet.json'))
m={p['id']:p for p in d['passages']}
for i in sys.argv[1:]:
    p=m.get(i)
    print('['+i+']', p['texte'] if p else 'ABSENT'); print()

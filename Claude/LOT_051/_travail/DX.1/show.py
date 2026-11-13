import json,sys
p=json.load(open('/home/user/wt/lot-051/Claude/LOT_051/_travail/DX.1/paquet.json'))
k=sys.argv[1]; n=int(sys.argv[2]); a=int(sys.argv[3]) if len(sys.argv)>3 else 0; b=int(sys.argv[4]) if len(sys.argv)>4 else 999
for q in p['passages']:
    if q['id'].startswith(k+'-'):
        i=int(q['id'].split('-')[1])
        if a<=i<=b: print(q['id'],'|',q['texte'][:n])

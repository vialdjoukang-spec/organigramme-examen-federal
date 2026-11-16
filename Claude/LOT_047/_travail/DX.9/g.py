import json,re,sys
P=json.load(open('Claude/LOT_047/_travail/DX.9/paquet.json'))['passages']
pre=sys.argv[1]; rx=re.compile(sys.argv[2],re.I); n=int(sys.argv[3]) if len(sys.argv)>3 else 40
k=0
for p in P:
    if p['id'].startswith(pre) and rx.search(p['texte']):
        print(f"[{p['id']}] {p['texte'][:int(sys.argv[4]) if len(sys.argv)>4 else 600]}\n"); k+=1
        if k>=n: break

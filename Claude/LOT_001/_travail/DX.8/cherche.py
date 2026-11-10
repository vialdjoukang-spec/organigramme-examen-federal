import json,re,sys
P=json.load(open('Claude/LOT_001/_travail/DX.8/paquet.json'))['passages']
pat=re.compile(sys.argv[1],re.I); pre=sys.argv[2] if len(sys.argv)>2 else ''
w=int(sys.argv[3]) if len(sys.argv)>3 else 160
for p in P:
    if pre and not p['id'].startswith(pre): continue
    for m in pat.finditer(p['texte']):
        a=max(0,m.start()-w); b=min(len(p['texte']),m.end()+w)
        print(f"[{p['id']}] …{p['texte'][a:b]}…\n"); break

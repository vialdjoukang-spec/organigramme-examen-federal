import json,re,sys
p=json.load(open('Claude/LOT_050/_travail/DX.4/paquet.json'))
pat=re.compile(sys.argv[1],re.I); src=sys.argv[2] if len(sys.argv)>2 else ''
mx=int(sys.argv[3]) if len(sys.argv)>3 else 700
for x in p['passages']:
    if x['id'].startswith('aips') or src not in x['source']: continue
    t=x['texte']; m=pat.search(t)
    if m:
        s=max(0,m.start()-250); print(f"[{x['id']}] …{t[s:s+mx]}\n")

import json,re,sys
pre,mot=sys.argv[1],sys.argv[2]; n=int(sys.argv[3]) if len(sys.argv)>3 else 900
P=json.load(open('/home/user/wt/lot-049/Claude/LOT_049/_travail/DX.7/paquet.json'))['passages']
m=re.compile(mot,re.I); tot=0
for p in P:
    if p['id'].startswith(pre) and m.search(p['texte']):
        s=f"[{p['id']}] {p['texte'][:n]}\n"; tot+=len(s)
        if tot>22000: print('...TRONQUE'); break
        print(s)

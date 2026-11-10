import json,sys,re
p=json.load(open('Claude/LOT_053/_travail/PA/paquet.json'))['passages']
a=sys.argv[1:]
mode=a[0]
if mode=='src':   # all passages of id prefix
    for q in p:
        if q['id'].rsplit('-',1)[0]==a[1]: print(f"[{q['id']}] {q['texte']}\n")
elif mode=='id':
    d={q['id']:q for q in p}
    for i in a[1:]: print(f"[{i}] {d[i]['texte']}\n")
else:
    rx=re.compile(a[1],re.I); pre=a[2] if len(a)>2 else ''; w=int(a[3]) if len(a)>3 else 600; lim=int(a[4]) if len(a)>4 else 8; n=0
    for q in p:
        if n>=lim: break
        if q['id'].startswith(pre):
            m=rx.search(q['texte'])
            if m:
                n+=1; s=max(0,m.start()-w//3); print(f"[{q['id']}] …{q['texte'][s:s+w]}\n")

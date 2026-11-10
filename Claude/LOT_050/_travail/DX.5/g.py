import json,re,sys
p=json.load(open('Claude/LOT_050/_travail/DX.5/paquet.json'))['passages']
pre,pat=sys.argv[1],sys.argv[2]; w=int(sys.argv[3]) if len(sys.argv)>3 else 700
for q in p:
    if q['id'].startswith(pre):
        t=q['texte']
        for m in re.finditer(pat,t,re.I):
            a=max(0,m.start()-w//3); print(q['id'],'…',t[a:a+w].replace('\n',' '),'\n'); break

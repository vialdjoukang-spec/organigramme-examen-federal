import json,re,sys
P=json.load(open('paquet.json'))['passages']
pf=sys.argv[1]; pat=re.compile(sys.argv[2],re.I); w=int(sys.argv[3]) if len(sys.argv)>3 else 160
pre={'esc':'w480b78','hug':'w8db60a','ch':'w0bafbb','hf':'w5d77ce','smw':'w63390a','bfs':'w19cae6'}.get(pf,pf)
for x in P:
    if x['id'].startswith(pre):
        t=x['texte'].replace('­','·')
        for m in list(pat.finditer(t))[:2]:
            print(x['id'],'…'+t[max(0,m.start()-w):m.end()+w].replace('\n',' ')+'…');print()

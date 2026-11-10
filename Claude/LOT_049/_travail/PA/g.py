import json,re,sys
d=json.load(open('Claude/LOT_049/_travail/PA/paquet.json'))
pre=sys.argv[1].split(','); m=re.compile(sys.argv[2],re.I); n=int(sys.argv[3]) if len(sys.argv)>3 else 600
for p in d['passages']:
    if any(p['id'].startswith(x) for x in pre) and m.search(p['texte']):
        t=p['texte']; i=m.search(t).start(); print(p['id'],'|',t[max(0,i-n//3):i+n].replace('\n',' '));print()

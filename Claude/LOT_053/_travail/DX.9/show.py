import json,sys
p=json.load(open('paquet.json'))
pre=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3]); m=int(sys.argv[4]) if len(sys.argv)>4 else 1400
for x in p['passages']:
    pf,n=x['id'].rsplit('-',1)
    if pf==pre and a<=int(n)<=b: print(f"[{x['id']}] {x['texte'][:m]}\n")

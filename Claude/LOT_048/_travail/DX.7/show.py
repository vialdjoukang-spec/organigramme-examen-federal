import json,sys,re
P=json.load(open('paquet.json'))['passages']
pre=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 700
lo=int(sys.argv[3]) if len(sys.argv)>3 else 0; hi=int(sys.argv[4]) if len(sys.argv)>4 else 10**6
for p in P:
    if p['id'].startswith(pre+'-'):
        k=int(p['id'].split('-')[-1])
        if lo<=k<=hi: print(f"[{p['id']}] {p['texte'][:n]}\n")

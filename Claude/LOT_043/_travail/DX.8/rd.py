import json,sys,re
P=json.load(open('paquet.json'))['passages']
pre=sys.argv[1]; lo=int(sys.argv[2]); hi=int(sys.argv[3]); mx=int(sys.argv[4]) if len(sys.argv)>4 else 600
for p in P:
    if p['id'].startswith(pre+'-'):
        n=int(p['id'].split('-')[1])
        t=p['texte']
        if lo<=n<=hi and len(t)>120 and not re.search(r'Find articles by|Google Scholar|\[ DOI',t): print(f"[{p['id']}] {t[:mx]}\n")

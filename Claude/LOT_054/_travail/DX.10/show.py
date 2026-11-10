import sys,re,json
p=json.load(open('paquet.json'))
pre=sys.argv[1]; w=int(sys.argv[2]) if len(sys.argv)>2 else 1200
for x in p['passages']:
    if not x['id'].startswith(pre): continue
    t=x['texte']
    if re.search(r'\(\d+\)[A-Z]',t) and t.count('(')>6: continue
    if re.search(r'Conflict of interest|reports personal fees|Disclosure|declares? no',t): continue
    print(f"[{x['id']}] {t[:w]}")

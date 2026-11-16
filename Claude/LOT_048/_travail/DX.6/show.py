import json,sys,re
p=json.load(open('paquet.json'))['passages']
pat=re.compile(sys.argv[2],re.I) if len(sys.argv)>2 else None
n=int(sys.argv[3]) if len(sys.argv)>3 else 700
for q in p:
    if q['id'].startswith(sys.argv[1]+'-') and (not pat or pat.search(q['texte'])):
        print(f"[{q['id']}] {q['texte'][:n]}")

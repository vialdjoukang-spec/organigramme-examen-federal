import json,sys,re
p=json.load(open('Claude/LOT_053/_travail/PA/paquet.json'))['passages']
args=sys.argv[1:]
if args[0]=='-m':
    rx=re.compile(args[1],re.I); src=args[2] if len(args)>2 else ''
    for q in p:
        if src in q['source'] and rx.search(q['texte']): print(f"[{q['id']}] {q['texte'][:900]}\n")
else:
    d={q['id']:q for q in p}
    for i in args: print(f"[{i}] {d[i]['texte']}\n")

import json,re,sys
p=json.load(open('Claude/LOT_054/_travail/DX.3/paquet.json'))
src=sys.argv[1]; rx=re.compile(sys.argv[2],re.I); n=int(sys.argv[3]) if len(sys.argv)>3 else 700
for q in p['passages']:
    if src in q['source'] or src in q['url'] or src in q['id']:
        if rx.search(q['texte']): print('['+q['id']+']',q['texte'][:n].replace('\n',' '),'\n')

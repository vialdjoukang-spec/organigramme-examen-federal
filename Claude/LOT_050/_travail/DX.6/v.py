import json,sys,re
p=json.load(open('paquet.json'))
src=sys.argv[1]; pat=re.compile(sys.argv[2],re.I) if len(sys.argv)>2 else None
mx=int(sys.argv[3]) if len(sys.argv)>3 else 700
for x in p['passages']:
    if src in x['source'] or src==x['id'][:len(src)]:
        if pat is None or pat.search(x['texte']): print('['+x['id']+']',x['texte'][:mx],'\n')

import json,re,sys
p=json.load(open('Claude/LOT_047/_travail/DX.7/paquet.json'))
pre=sys.argv[1].split(',');pat=re.compile(sys.argv[2],re.I);mx=int(sys.argv[3]) if len(sys.argv)>3 else 500
for x in p['passages']:
    if x['id'].rsplit('-',1)[0] in pre or (x['id'].startswith('aips') and 'aips' in pre):
        t=x['texte'].replace('\n',' ')
        if pat.search(t): print(x['id'],t[:mx]);print()

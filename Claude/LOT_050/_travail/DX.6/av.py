import json,re,sys
p=json.load(open('paquet.json'))
a=[x for x in p['passages'] if x['id'].startswith('aips')]
src=sys.argv[1]; pat=sys.argv[2]; mx=int(sys.argv[3]); lim=int(sys.argv[4])
n=0
for x in a:
    if src in x['source'] and re.search(pat,x['texte'],re.I):
        print('['+x['id']+']',x['texte'][:mx],'\n'); n+=1
        if n>=lim: break

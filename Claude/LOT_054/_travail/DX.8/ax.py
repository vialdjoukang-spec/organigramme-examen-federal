import json,re,sys
p=json.load(open('paquet.json'))['passages']
num,rx=sys.argv[1],sys.argv[2]; n=int(sys.argv[3]) if len(sys.argv)>3 else 3; w=int(sys.argv[4]) if len(sys.argv)>4 else 700
c=0
for x in p:
    if x['id'].startswith('aips-'+num+'-') and re.search(rx,x['texte']):
        m=re.search(rx,x['texte']); s=max(0,m.start()-150)
        print(f"[{x['id']}] …{x['texte'][s:s+w]}\n"); c+=1
        if c>=n: break

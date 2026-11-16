import json,sys,re
P=json.load(open('paquet.json'))['passages']
rx=re.compile(sys.argv[1],re.I); pre=sys.argv[2] if len(sys.argv)>2 else ''; w=int(sys.argv[3]) if len(sys.argv)>3 else 350; mx=int(sys.argv[4]) if len(sys.argv)>4 else 4
c=0
for p in P:
    if pre and not re.match(pre,p['id']): continue
    if re.search(r'Google Scholar|\[ DOI|\d{6,}\d{2}10\.\d',p['texte']): continue
    m=rx.search(p['texte'])
    if m:
        t=p['texte']; print(f"[{p['id']}] …{t[max(0,m.start()-w//2):m.end()+w]}\n"); c+=1
        if c>=mx: break

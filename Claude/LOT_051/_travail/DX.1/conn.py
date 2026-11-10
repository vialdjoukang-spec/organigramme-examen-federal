import re,glob,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
cs=['Par ailleurs, ','En outre, ']
k=0
for f in sorted(glob.glob('src/p*.txt')):
    s=open(f).read(); blocks=s.split('\n\n'); ch=False
    for i,b in enumerate(blocks):
        head=''
        if b.startswith('#### ') and '\n' in b:
            head,b=b.split('\n',1); head+='\n'
        if re.match(r'\s*(####|\||- |@@|\s*- )',b): continue
        t=re.sub(r'\{[^}]*\}','',b); t=re.sub(r'\[\[(.+?)\|f\d+\]\]',r'\1',t)
        if len(t.split())>40 and not c.CONNECT.search(t):
            sents=re.split(r'(?<=\.)\s+(?=[A-ZÀ-Ý«])',b)
            if len(sents)<2: print('single',f,b[:50]); continue
            last=sents[-1]
            if re.match(r'(Enfin|Ensuite|D\'abord|Dès)',last): continue
            conn=cs[k%2]; k+=1
            first=last[0].lower()+last[1:] if re.match(r'(Le |La |Les |L\'|Un |Une |Dans |Chez |Cette |Ces |Il |Elle |Ils |On |Pour |Au |Aux |Lorsqu|Une )',last) else last
            sents[-1]=conn+first
            blocks[i]=head+' '.join(sents); ch=True
    if ch: open(f,'w').write('\n\n'.join(blocks))
print('edits',k)

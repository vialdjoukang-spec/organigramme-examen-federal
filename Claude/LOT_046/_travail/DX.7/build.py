import json,re,sys,os
P=json.load(open('paquet.json'))['passages']
PFX={'hug':'wfef614-','esc':'esc24-','pmc':'w82b6b4-','col':'w891d98-','hf':'w149687-','rms':'w42735c-','ger':'we914c7-',
'xa':'aips-58728-','pr':'aips-61385-','ap':'aips-70399-','me':'aips-59206-','am':'aips-59528-'}
def norm(s): return re.sub(r'[\s\u00ad]+','',s.replace('’',"'")).lower()
N=[(x['id'],norm(x['texte'])) for x in P]
bad=0
def res(tok):
    global bad
    if tok.startswith('#'): return tok[1:]
    k,ph=tok.split(':',1); q=norm(ph)
    c=[i for i,t in N if i.startswith(PFX[k]) and q in t]
    if not c: print('INTROUVABLE',tok); bad+=1; return None
    return c[0]
for f in sorted(os.listdir('src')):
    s=open('src/'+f).read()
    s=re.sub(r'([.!?])((?:⟦.*?⟧)+)',lambda m:m.group(2)+m.group(1),s)
    def rep(m):
        out=''
        for t in re.findall(r'⟦(.*?)⟧',m.group(0)):
            i=res(t)
            if i: out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
        return out
    open('fragments/'+f.replace('.src',''),'w').write(re.sub(r'(?:⟦.*?⟧)+',rep,s))
print('ok' if not bad else f'{bad} manquants')

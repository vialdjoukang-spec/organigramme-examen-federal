import json,re,sys,os
P=json.load(open('paquet.json'))['passages']
PFX={'ers':'wa346e0-','bts':'w7915e8-','btsf':'w2e276b-','r23':'wfad2fa-','r21':'w37bf2a-','r20':'w60d6fe-','r04':'wb2c98e-',
'r08':'wc1db35-','mend':'w06d6b2-','sch':'wf584c1-','sch2':'w774ef2-','nop':'wff2c57-','cep':'wf36769-','sf':'w6f6583-',
'li':'aips-30015-','df':'aips-69266-','ersa':'wb415c3-'}
def norm(s): return re.sub(r'[\s­‐‑\-]+','',s.replace('’',"'").replace('’',"'")).lower()
N=[(x['id'],norm(x['texte'])) for x in P]
bad=0
def res(tok):
    global bad
    if tok.startswith('#'): return tok[1:]
    k,ph=tok.split(':',1); q=norm(ph)
    c=[i for i,t in N if i.startswith(PFX[k]) and q in t]
    if not c: print('INTROUVABLE',tok); bad+=1; return None
    return c[0]
os.makedirs('fragments',exist_ok=True)
for f in sorted(os.listdir('src')):
    s=open('src/'+f).read()
    s=re.sub(r'([.!?])((?:⟦.*?⟧)+)',lambda m:m.group(2)+m.group(1),s)
    def rep(m):
        out=''
        for t in re.findall(r'⟦(.*?)⟧',m.group(0)):
            i=res(t)
            if i and f'#sb-{i}"' not in out: out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
        return out
    open('fragments/'+f.replace('.src',''),'w').write(re.sub(r'(?:⟦.*?⟧)+',rep,s))
print('ok' if not bad else f'{bad} manquants')

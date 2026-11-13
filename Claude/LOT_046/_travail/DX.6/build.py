import json,re,sys,os
P=json.load(open('paquet.json'))['passages']
PFX={'esc':['w480b78'],'hug':['w8db60a'],'ch':['w0bafbb'],'hf':['w5d77ce'],'bfs':['w19cae6'],'smw':['w63390a'],
'hugq':['w969895'],'rms':['wcec5bd'],'mt':['wd806ba'],'aty':['wd48815'],'jcm':['w1848ee'],'tts':['w8c6c30'],'pe':['we47104'],'life':['w167ec9'],'libby':['w73df9f'],'eros':['w7b9a15'],'lifea':['w0a4b5c'],'hfm':['w5bb991'],'kil':['w4635f7'],'kb':['w19462d'],'lus':['w17b7a2'],'hfa':['wceb5ad'],'un':['w512b09']}
for no in ('69596','59136','69837','65957','49456','46613','55459','59206','68105'): PFX['a'+no]=['aips-%s-'%no]
def norm(s): return re.sub(r'\s+','',s.replace('­','')).lower()
N=[(x['id'],norm(x['texte'])) for x in P]
def res(tok):
    if tok.startswith('#'): return tok[1:]
    pf,ph=tok.split(':',1)
    ids=PFX[pf]; q=norm(ph)
    c=[i for i,t in N if any(i.startswith(p) for p in ids) and q in t]
    if not c: print('INTROUVABLE',tok); return None
    return c[0]
bad=0
os.makedirs('fragments',exist_ok=True)
for f in sorted(os.listdir('src')):
    s=open('src/'+f).read()
    def rep(m):
        global bad
        out=''
        for t in re.findall(r'⟦(.*?)⟧',m.group(0)):
            i=res(t)
            if i is None: bad+=1; continue
            if f'<sup class="r"><a href="#sb-{i}">' in out: continue
            out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
        return out
    s=re.sub(r'([.!?])((?:⟦.*?⟧)+)',lambda m:m.group(2)+m.group(1),s)
    s2=re.sub(r'(?:⟦.*?⟧)+',rep,s)
    open('fragments/'+f.replace('.src',''),'w').write(s2)
print('ok' if not bad else f'{bad} manquants')

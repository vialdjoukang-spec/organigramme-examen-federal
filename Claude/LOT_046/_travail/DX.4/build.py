import json,re,sys,os
P=json.load(open('paquet.json'))['passages']
PFX={'hug':['w11618b'],'g26':['gina26ch9','gina26intro'],'g25':['wfebf77'],'aud':['wf6dd43'],'mg1':['w323e53'],'mg2':['w5bc6dd'],
'mg3':['w1d49b8'],'icu':['wbb99ba'],'swg':['w81fba5'],'ers':['w96c75f'],'aafp':['we20579'],'rms':['w9226c4'],'ic':['w149687'],'bpco':['w18c561'],'pac':['w1147a0'],'tvp':['wa70cb5'],'anx':['we22718']}
for no in ('58253','52584','55568','69640','35112','66994','52845','55568','68470','66747','50821'): PFX['aips'+no]=['aips-%s-'%no]
def norm(s): return re.sub(r'\s+','',s).lower()
N=[(x['id'],norm(x['texte'])) for x in P]
def res(tok):
    if tok.startswith('#'): return tok[1:]
    pf,ph=tok.split(':',1)
    ids=PFX[pf]; q=norm(ph)
    c=[i for i,t in N if any(i.startswith(p) for p in ids) and q in t]
    if not c: print('INTROUVABLE',tok); return None
    return c[0]
bad=0
groups={}
for f in sorted(os.listdir('src')):
    groups.setdefault(f[:3],[]).append(f)
for g,fs in sorted(groups.items()):
    f=g+'.src.html'
    s=''.join(open('src/'+x).read() for x in fs)
    def rep(m):
        out=''
        for t in re.findall(r'⟦(.*?)⟧',m.group(0)):
            i=res(t)
            if i is None:
                global bad; bad+=1; continue
            out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
        return out
    s=re.sub(r'([.!?])((?:⟦.*?⟧)+)',lambda m:m.group(2)+m.group(1),s)
    s2=re.sub(r'(?:⟦.*?⟧)+',rep,s)
    open('fragments/'+f.replace('.src',''),'w').write(s2)
print('ok' if not bad else f'{bad} manquants')

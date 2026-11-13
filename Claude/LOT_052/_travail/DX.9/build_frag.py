import re,glob,os
D=os.path.dirname(os.path.abspath(__file__))
M={'E':'we01db4','W':'wae2fea','A':'wc66130','C':'wa26575','B':'w85447d','M':'wb102b7','N':'w33e7c2','Dv':'w7d8ee9','Cl':'w80d265','L':'wcf4ea0','An':'w436068','Y':'w7ecc9b','V':'w0c98e0','H':'w683c0b','R':'rms528','S':'w2ab1c2','Hp':'aips-67780','Pt':'aips-58459','Ro':'aips-44625','He':'aips-67702','Ac':'aips-48313','Rv':'aips-65739'}
def rep(m):
    out=''
    for t in m.group(1).split(','):
        k,n=t.strip().split(':'); i=f'{M[k]}-{n}'
        out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
    return out
for f in sorted(glob.glob(D+'/src/p*.html')):
    s=open(f).read()
    s=re.sub(r'\[\[([^\]]+)\]\]',rep,s)
    open(D+'/fragments/'+os.path.basename(f),'w').write(s)

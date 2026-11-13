import re,sys,os,glob
AL={'L':'w2a1b3e','S':'w8e4199','U':'wdc4ab4','C':'wf2638c','R':'wf80782','E1':'w76902d','E2':'w35cc18','B':'w688bfe','T':'w1f4933','P':'w116b26','Q':'w73f485','M':'wa12200','N':'w3fc4ec','D':'w2aac93','A':'wd122d9','NX':'aips-55609','PA':'aips-59834','OM':'aips-56313','LA':'aips-57801','PR':'aips-55090','AG':'aips-51969','F':'w2df0cf','G':'w7e05da'}
def sup(m):
    out=''
    for t in m.group(1).split('|'):
        k,n=t.split('.')
        i=AL[k]+'-'+n
        out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
    return out
for f in sorted(glob.glob('src/p*.html')):
    n=int(re.search(r'p(\d+)',f).group(1))
    s=open(f).read()
    s=re.sub(r'([.!?])\s*(\[\[[^\]]*\]\])',r'\2\1',s)
    s=re.sub(r'\[\[([A-Z0-9]+\.\d+(?:\|[A-Z0-9]+\.\d+)*)\]\]',sup,s)
    s=re.sub(r'\{\{(f\d+)\|([^}]*)\}\}',lambda m:f'<button class="w" popovertarget="dx1-p{n}-{m.group(1)}">{m.group(2)}</button>',s)
    s=re.sub(r'<F (f\d+)>',lambda m:f'<div id="dx1-p{n}-{m.group(1)}" popover class="fenetre">',s)
    s=s.replace('</F>','</div>')
    s=s.replace('<div class="t">','<div class="t" style="overflow-x:auto">')
    s=re.sub(r'\n\s*\n','\n',s)
    open(f'fragments/p{n:02d}.html','w').write(s)

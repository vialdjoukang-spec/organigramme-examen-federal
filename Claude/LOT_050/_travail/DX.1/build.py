#!/usr/bin/env python3
import re,glob,os
AL={'R':'w07e241','Q':'w40e656','S':'w9b018b','A':'w374bf3','M':'w6d9042','P':'wc048d6','E':'w49fefc','KO':'w2f50e6','C':'wf513f5','Z':'wf611de','V':'wdd02e7','H':'w40fa33','B':'wd1b3ed','CF':'w44075d','AL':'w815cdf','CM':'wb9e1d0','SH':'w09080c','AT':'w3c9c70','EC':'wfcd167','CO':'w4c9906','JP':'w0af021','PA':'w5e569f','OT':'w25153a','TE':'w775d5c','F':'w844b43'}
def cit(m):
    out=''
    for t in m.group(1).split(','):
        t=t.strip()
        if t.startswith('aips'): i=t
        else:
            k=re.match(r'([A-Z]+)(\d+)$',t); i=f'{AL[k.group(1)]}-{k.group(2)}'
        out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
    return out
for f in sorted(glob.glob('src/p*.txt')):
    n=int(re.search(r'p(\d+)',f).group(1))
    s=open(f,encoding='utf-8').read()
    s=re.sub(r'\[\[(f\d+)\|([^\]]+)\]\]',lambda m:f'<button class="w" popovertarget="dx1-p{n}-{m.group(1)}">{m.group(2)}</button>',s)
    s=re.sub(r'<<(f\d+)',lambda m:f'<div id="dx1-p{n}-{m.group(1)}" popover class="fenetre">',s)
    s=s.replace('>>','</div>')
    s=re.sub(r'\{([^{}]+)\}',cit,s)
    s=re.sub(r'\n{2,}','\n',s)
    open(f'fragments/p{n:02d}.html','w',encoding='utf-8').write(s)

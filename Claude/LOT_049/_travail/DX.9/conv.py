import re,glob,os
M={'R':'w52767b-','J':'wb1b10e-','F':'wede9aa-','B':'w345ee3-','E':'wa68911-','X':'w37e9cd-','V':'wea19e4-','N':'w1f4b08-','L':'w4d8bbd-','I':'wbadb0e-','M':'w646124-','S':'wdebe26-','D':'w6bdea1-','H':'w7c66f5-','U':'wfba9d7-','Z':'w0b5a11-','K':'w548dc3-','A':'w51eede-'}
def cit(m):
    out=''
    for t in m.group(1).split():
        if re.match(r'^a\d{5}-\d+$',t): i='aips-'+t[1:]
        elif t[0] in M and re.match(r'^[A-Z]\d+$',t): i=M[t[0]]+t[1:]
        else: raise SystemExit('cit inconnue '+t)
        out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
    return out
def conv(s):
    s=re.sub(r'\{([^{}]+)\}',cit,s)
    s=re.sub(r'<B ([\w-]+)>(.*?)</B>',lambda m:f'<button class="w" popovertarget="dx9-{m.group(1)}">{m.group(2)}</button>',s)
    s=re.sub(r'<W ([\w-]+)>',lambda m:f'<div id="dx9-{m.group(1)}" popover class="fenetre">',s)
    s=s.replace('</W>','</div>').replace('<P>','<div class="p">').replace('</P>','</div>')
    s=s.replace('<T>','<div class="t" style="overflow-x:auto"><table>').replace('</T>','</table></div>')
    return s
for f in sorted(glob.glob('src/p*.txt')):
    o='fragments/'+os.path.basename(f).replace('.txt','.html')
    open(o,'w').write(conv(open(f).read()))

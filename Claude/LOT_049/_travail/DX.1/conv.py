import re,sys,glob,os
M={'H':'w51eede-','G':'w779563-','S':'w0b5a11-','K':'w7552b2-','E':'w96c75f-','Y':'wdd804d-','M':'w0635dd-','D':'w033f5c-','C':'wc8b86d-','P':'we931aa-','Q':'w6a2c47-'}
def cit(m):
    out=''
    for t in m.group(1).split():
        if re.match(r'^a\d{5}-\d+$',t): i='aips-'+t[1:]
        elif re.match(r'^w[0-9a-f]{5,6}-\d+$',t): i=t
        elif t[0] in M and re.match(r'^[A-Z]\d+$',t): i=M[t[0]]+t[1:]
        else: raise SystemExit('cit inconnue '+t)
        out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
    return out
def conv(s):
    s=re.sub(r'\{([^{}]+)\}',cit,s)
    s=re.sub(r'<B ([\w-]+)>(.*?)</B>',lambda m:f'<button class="w" popovertarget="dx1-{m.group(1)}">{m.group(2)}</button>',s)
    s=re.sub(r'<W ([\w-]+)>',lambda m:f'<div id="dx1-{m.group(1)}" popover class="fenetre">',s)
    s=s.replace('</W>','</div>').replace('<P>','<div class="p">').replace('</P>','</div>')
    s=s.replace('<T>','<div class="t" style="overflow-x:auto"><table>').replace('</T>','</table></div>')
    return s
for f in sorted(glob.glob('src/p*.txt')):
    o='fragments/'+os.path.basename(f).replace('.txt','.html')
    open(o,'w').write(conv(open(f).read()))

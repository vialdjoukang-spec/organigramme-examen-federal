import re,sys,glob,os
def conv(t):
    S=lambda i:'<sup class="r"><a href="#sb-%s">%s</a></sup>'%(i,i)
    def rep(m):
        ids=re.findall(r'\{([^}]+)\}',m.group(2))
        return ''.join(S(i) for i in ids)+m.group(1)
    t=re.sub(r'([.!?])((?:\{[a-z0-9-]+\})+)',rep,t)
    t=re.sub(r'\{([a-z0-9]+(?:-[a-z0-9]+)*-\d+)\}',lambda m:S(m.group(1)),t)
    out=[]
    for b in re.split(r'\n\s*\n',t.strip()):
        b=b.strip()
        if not b: continue
        if b.startswith('#h '): out.append('<h4><em>%s</em></h4>'%b[3:])
        elif b.startswith('<'): out.append(b.replace('<div class="t">','<div class="t" style="overflow-x:auto">'))
        elif b.startswith('- '):
            out.append('<ul>'+''.join('<li>%s</li>'%l[2:] for l in b.split('\n- ') for l in [l if l.startswith('- ') else '- '+l])+'</ul>')
        else: out.append('<div class="p">%s</div>'%b.replace('\n',' '))
    return '\n'.join(out)+'\n'
for f in sorted(glob.glob('src/p*.txt')):
    open('fragments/'+os.path.basename(f)[:-4]+'.html','w').write(conv(open(f).read()))

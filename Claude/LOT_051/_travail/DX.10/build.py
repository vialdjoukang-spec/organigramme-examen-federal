import re,sys,glob,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def conv(txt,n):
    def cit(m):
        ids=m.group(1).split('|')
        return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)
    out=[]
    for line in txt.split('\n'):
        mm=re.match(r'@@(f\d+) (.*)$',line)
        if mm:
            line=f'<div id="dx10-p{n}-{mm.group(1)}" popover class="fenetre"><div class="p">{mm.group(2)}</div></div>'
        line=line.replace('<div class="t">','<div class="t" style="overflow-x:auto">')
        line=re.sub(r' ?\[\[([^\]]+)\]\]',cit,line)
        line=re.sub(r'\{\{(f\d+)\|([^}]+)\}\}',lambda m:f'<button class="w" popovertarget="dx10-p{n}-{m.group(1)}">{m.group(2)}</button>',line)
        out.append(line)
    return '\n'.join(out)
for f in sorted(glob.glob('src/p*.txt')):
    n=int(re.search(r'p(\d+)',f).group(1))
    open(f'fragments/p{n:02d}.html','w').write(conv(open(f).read(),n))
print('ok')

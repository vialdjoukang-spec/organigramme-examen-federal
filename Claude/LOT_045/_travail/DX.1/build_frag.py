import re,glob,os
AL={'CC':'w94f46f-','B':'w1b740f-','F':'wb0784f-','I':'we19809-','S':'w429799-','G':'w7fdfc0-','Z':'wad3e0f-','H':'w114eaf-','L':'w74e94f-','M':'w2c7601-','D':'w369380-','IR':'aips-67815-','BI':'aips-61441-','T':'aips-55196-'}
def cite(m):
    out=''
    for r in m.group(1).split(','):
        k=re.match(r'([A-Z]+)(\d+)$',r.strip()); i=AL[k.group(1)]+k.group(2)
        out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
    return out
for f in sorted(glob.glob('src/p*.txt')):
    n=int(re.search(r'p(\d+)',f).group(1)); s=open(f,encoding='utf-8').read()
    s=s.replace('<div class="t"><table>','<div class="t" style="overflow-x:auto"><table>')
    s=re.sub(r'\[\[([A-Z0-9, ]+)\]\]',cite,s)
    s=re.sub(r'\{\{(\d+)\|([^}]+)\}\}',lambda m:f'<button class="w" popovertarget="dx1-p{n}-f{m.group(1)}">{m.group(2)}</button>',s)
    s=re.sub(r'<<(\d+)>>',lambda m:f'<div id="dx1-p{n}-f{m.group(1)}" popover class="fenetre">',s)
    s=s.replace('<</>>','</div>')
    open(f'fragments/p{n:02d}.html','w',encoding='utf-8').write(s)
print('ok')

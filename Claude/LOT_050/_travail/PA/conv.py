import re,glob,os,sys
for f in sorted(glob.glob('src/p*.src')):
    s=open(f,encoding='utf-8').read()
    s=re.sub(r'\s*\{c:([^}]+)\}', lambda m:''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(',')), s)
    s=re.sub(r'\{w:([^|}]+)\|([^}]+)\}', lambda m:f'<button class="w" popovertarget="pa-{m.group(1)}">{m.group(2)}</button>', s)
    s=re.sub(r'<<pop ([\w-]+)>>', r'<div id="pa-\1" popover class="fenetre">', s)
    s=s.replace('<</pop>>','</div>')
    s=re.sub(r'\n{2,}','\n',s)
    open('fragments/'+os.path.basename(f).replace('.src','.html'),'w',encoding='utf-8').write(s)
print('ok')

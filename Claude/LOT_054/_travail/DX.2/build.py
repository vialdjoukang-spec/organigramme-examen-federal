import re,glob,os
for f in sorted(glob.glob('src/p*.txt')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'\[\[([\w.\-,]+)\]\]',lambda m:''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in m.group(1).split(',')),t)
    t=re.sub(r'\{\{([\w\-]+)\|([^}]*)\}\}',lambda m:f'<button class="w" popovertarget="{m.group(1)}">{m.group(2)}</button>',t)
    t=t.replace('<TAB>','<div class="t" style="overflow-x:auto">').replace('</TAB>','</div>')
    open('fragments/'+os.path.basename(f).replace('.txt','.html'),'w',encoding='utf-8').write(t)

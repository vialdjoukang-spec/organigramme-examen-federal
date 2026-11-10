import re,glob,os
os.makedirs('fragments',exist_ok=True)
for f in sorted(glob.glob('src/p*.txt')):
    s=open(f,encoding='utf-8').read()
    s=re.sub(r'\.\s*((?:\{\{[\w.\-]+\}\}\s*)+)',lambda m:''.join(re.findall(r'\{\{[\w.\-]+\}\}',m.group(1)))+'. ',s)
    s=re.sub(r'\{\{([\w.\-]+)\}\}',lambda m:f'<sup class="r"><a href="#sb-{m.group(1)}">{m.group(1)}</a></sup>',s)
    s=re.sub(r'@w\(([\w\-]+)\|([^)]*)\)',lambda m:f'<button class="w" popovertarget="dx1-{m.group(1)}">{m.group(2)}</button>',s)
    s=re.sub(r'@pop\(([\w\-]+)\)',lambda m:f'<div id="dx1-{m.group(1)}" popover class="fenetre">',s)
    s=s.replace('@end','</div>')
    open('fragments/'+os.path.basename(f).replace('.txt','.html'),'w',encoding='utf-8').write(s)

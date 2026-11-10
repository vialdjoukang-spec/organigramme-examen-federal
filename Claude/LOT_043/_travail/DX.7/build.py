#!/usr/bin/env python3
# DX.7 : src/pNN.txt (citations en [[id,id]]) -> fragments/pNN.html
import re,os,glob
for f in sorted(glob.glob('src/p*.txt')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'([.!?])\[\[([^\]]+)\]\]',lambda m:''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(2).split(','))+m.group(1),t)
    t=re.sub(r'\[\[([^\]]+)\]\]',lambda m:''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(',')),t)
    t=re.sub(r'<div class="p">\s*','<div class="p">',t)
    open('fragments/'+os.path.basename(f).replace('.txt','.html'),'w',encoding='utf-8').write(t)

import re,glob,os,sys
d=os.path.dirname(os.path.abspath(__file__))
for f in sorted(glob.glob(d+'/src/p*.html')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'\[\[([\w.\-:]+)\]\]',lambda m:f'<sup class="r"><a href="#sb-{m.group(1)}">{m.group(1)}</a></sup>',t)
    t=re.sub(r'\[w:(p\d+-f\d+)\|([^\]]+)\]',lambda m:f'<button class="w" popovertarget="dx2-{m.group(1)}">{m.group(2)}</button>',t)
    t=re.sub(r'<fen id="(p\d+-f\d+)">',lambda m:f'<div id="dx2-{m.group(1)}" popover class="fenetre">',t)
    t=t.replace('</fen>','</div>').replace('<div class="t">','<div class="t" style="overflow-x:auto">')
    open(d+'/fragments/'+os.path.basename(f),'w',encoding='utf-8').write(t)

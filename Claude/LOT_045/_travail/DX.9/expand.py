import re,glob,os,sys
D=os.path.dirname(os.path.abspath(__file__))
def cit(m):
    return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in m.group(1).split(','))
for f in sorted(glob.glob(D+'/src/p*.html')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'\[\[([\w.\-:]+(?:,[\w.\-:]+)*)\]\]',cit,t)
    t=re.sub(r'\{\{b ([\w-]+)\|([^}]*)\}\}',r'<button class="w" popovertarget="dx9-\1">\2</button>',t)
    t=re.sub(r'\{\{f ([\w-]+)\}\}',r'<div id="dx9-\1" popover class="fenetre">',t)
    t=t.replace('{{/f}}','</div>').replace('<div class="t"><table>','<div class="t" style="overflow-x:auto"><table>')
    assert '{{' not in t and '[[' not in t, f
    open(D+'/fragments/'+os.path.basename(f),'w',encoding='utf-8').write(t)

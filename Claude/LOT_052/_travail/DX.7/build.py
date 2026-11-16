import re,os,sys
d=os.path.dirname(os.path.abspath(__file__))
os.makedirs(d+'/fragments',exist_ok=True)
for f in sorted(os.listdir(d+'/src')):
    t=open(d+'/src/'+f).read()
    t=re.sub(r'\.((?:\[\[[\w.\-]+\]\])+)',lambda m:m.group(1)+'.',t)
    t=t.replace('<div class="t">','<div class="t" style="overflow-x:auto">')
    t=re.sub(r'\[\[([\w.\-]+)\]\]',lambda m:f'<sup class="r"><a href="#sb-{m.group(1)}">{m.group(1)}</a></sup>',t)
    open(d+'/fragments/'+f,'w').write(t)
print('ok')

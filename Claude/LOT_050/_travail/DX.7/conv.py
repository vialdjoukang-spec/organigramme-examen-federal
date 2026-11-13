import re,glob,os
d=os.path.dirname(os.path.abspath(__file__))
for f in sorted(glob.glob(d+'/src/p*.txt')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'\[\[([\w.\-]+)\]\]',lambda m:'<sup class="r"><a href="#sb-%s">%s</a></sup>'%(m.group(1),m.group(1)),t)
    t=re.sub(r'>\s*<sup class="r">','><sup class="r">',t)
    t=t.replace('<div class="t"><table','<div class="t" style="overflow-x:auto"><table')
    open(d+'/fragments/'+os.path.basename(f).replace('.txt','.html'),'w',encoding='utf-8').write(t)

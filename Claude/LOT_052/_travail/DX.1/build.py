import re,glob,os
d=os.path.dirname(os.path.abspath(__file__))
for f in sorted(glob.glob(d+'/src/p*.html')):
    t=open(f).read()
    t=re.sub(r'\[\[([\w.\-:]+)\]\]',lambda m:f'<sup class="r"><a href="#sb-{m.group(1)}">{m.group(1)}</a></sup>',t)
    open(d+'/fragments/'+os.path.basename(f),'w').write(t)

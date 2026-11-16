import re,glob,os
for f in sorted(glob.glob('src/p*.src')):
    t=open(f).read()
    t=re.sub(r'\{([\w.\-:]+)\}',lambda m:f'<sup class="r"><a href="#sb-{m.group(1)}">{m.group(1)}</a></sup>',t)
    open('fragments/'+os.path.basename(f).replace('.src','.html'),'w').write(t)
    print(f,len(t.encode()))

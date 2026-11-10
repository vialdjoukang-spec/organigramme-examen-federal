import re,glob,os
for f in sorted(glob.glob('src/p*.src')):
    t=open(f).read()
    t=re.sub(r'\[\[([^\]]+)\]\]',lambda m:''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in m.group(1).split('|')),t)
    open('fragments/'+os.path.basename(f)[:-4]+'.html','w').write(t)

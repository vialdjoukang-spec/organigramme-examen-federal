import re,glob,os
for f in sorted(glob.glob('src/p*.src.html')):
    s=open(f).read()
    def rep(m):
        return ''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(','))
    s=re.sub(r'([.!?])((?:\[\[[^\]]+\]\])+)',lambda m:m.group(2)+m.group(1),s)
    s=re.sub(r'\[\[([^\]]+)\]\]',rep,s)
    s=s.replace('<div class="t">','<div class="t" style="overflow-x:auto">')
    out='fragments/'+os.path.basename(f).replace('.src','')
    open(out,'w').write(s)

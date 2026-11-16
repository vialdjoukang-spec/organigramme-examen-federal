import re,glob,os
d=os.path.dirname(os.path.abspath(__file__))
def exp(m):
    ids=[i.strip() for i in m.group(1).split(',')]
    return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)
for f in sorted(glob.glob(d+'/src/p*.txt')):
    t=open(f).read()
    t=re.sub(r'\[\[([^\]]+)\]\]',exp,t)
    open(d+'/fragments/'+os.path.basename(f).replace('.txt','.html'),'w').write(t)

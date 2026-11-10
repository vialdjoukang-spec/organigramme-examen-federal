import re,sys,os,glob
D=os.path.dirname(os.path.abspath(__file__))
pat=re.compile(r'\s*\[((?:[a-z0-9]+(?:-\d+)+)(?:\s*,\s*[a-z0-9]+(?:-\d+)+)*)\]')
def rep(m):
    return ''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(','))
for f in sorted(glob.glob(D+'/src/p*.html')):
    h=open(f).read()
    h=pat.sub(rep,h)
    open(D+'/fragments/'+os.path.basename(f),'w').write(h)

import re,glob,os,sys
D=os.path.dirname(os.path.abspath(__file__))
for f in sorted(glob.glob(D+'/src/p*.html')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'\[\[([\w.\-:, ]+)\]\]',lambda m:''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(',')),t)
    open(D+'/fragments/'+os.path.basename(f),'w',encoding='utf-8').write(t)
print('ok')

import re,glob,os
for f in sorted(glob.glob('src/p*.html')):
    t=open(f,encoding='utf-8').read()
    def r(m):
        ids=[i.strip() for i in m.group(1).split(',')]
        return '<sup class="r">'+''.join(f'<a href="#sb-{i}">{i}</a>' for i in ids)+'</sup>'
    t=re.sub(r'\[\[([^\]]+)\]\]',r,t)
    open('fragments/'+os.path.basename(f),'w',encoding='utf-8').write(t)
print('ok')

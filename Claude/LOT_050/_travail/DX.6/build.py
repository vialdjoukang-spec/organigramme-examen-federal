import re,glob,os
for f in sorted(glob.glob('src/p*.html')):
    t=open(f,encoding='utf-8').read()
    def r(m):
        ids=[i.strip() for i in m.group(1).split(',')]
        return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)
    t=re.sub(r'\[\[([^\]]+)\]\]',r,t)
    # séparer les sup à plusieurs ancres
    while re.search(r'</a><a href="#sb-',t):
        t=re.sub(r'</a><a href="#sb-([\w.\-:]+)">',r'</a></sup><sup class="r"><a href="#sb-\1">',t)
    t=re.sub(r'<div class="p"><strong>([^<]+)</strong></div>',r'<h5>\1</h5>',t)
    t=t.replace('<div class="t">','<div class="t" style="overflow-x:auto">')
    open('fragments/'+os.path.basename(f),'w',encoding='utf-8').write(t)
print('ok')

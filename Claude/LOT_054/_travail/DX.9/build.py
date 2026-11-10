import re,glob,os
os.makedirs('fragments',exist_ok=True)
def sup(m):
    return ''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(','))
for f in sorted(glob.glob('src/p*.txt')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'\[\[([^\]]+)\]\]',sup,t)
    t=re.sub(r'^P: ?(.*)$',r'<div class="p">\1</div>',t,flags=re.M)
    open('fragments/'+os.path.basename(f)[:-4]+'.html','w',encoding='utf-8').write(t)
print('ok')

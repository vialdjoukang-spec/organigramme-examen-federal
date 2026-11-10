import re,glob,os
for f in sorted(glob.glob('src/p*.txt')):
    t=open(f,encoding='utf-8').read()
    def rep(m):
        ids=m.group(1).split()
        return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)
    t=re.sub(r'\[\[([^\]]+)\]\]',rep,t)
    open('fragments/'+os.path.basename(f).replace('.txt','.html'),'w',encoding='utf-8').write(t)
print('ok')

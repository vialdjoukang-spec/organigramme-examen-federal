import re,sys,glob,os
def sup(m):
    return ''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(','))
for f in sorted(glob.glob('src/p*.txt')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'([.!?])((?:\[\[[^\]]+\]\])+)',r'\2\1',t)
    t=re.sub(r'\[\[([^\]]+)\]\]',sup,t)
    open('fragments/'+os.path.basename(f).replace('.txt','.html'),'w',encoding='utf-8').write(t)

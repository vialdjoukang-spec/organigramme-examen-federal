import re,glob,os
for f in sorted(glob.glob('src/p*.txt')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'\[\[([\w.\-,\s]+?)\]\]',lambda m:''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(',')),t)
    open('fragments/'+os.path.basename(f).replace('.txt','.html'),'w',encoding='utf-8').write(t)

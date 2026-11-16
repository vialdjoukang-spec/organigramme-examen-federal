import re,sys,glob,os
d=os.path.dirname(os.path.abspath(__file__))
for f in sorted(glob.glob(d+'/src/p*.txt')):
    s=open(f,encoding='utf-8').read()
    s=re.sub(r'\[\[([\w.\-]+)\]\]',lambda m:f'<sup class="r"><a href="#sb-{m.group(1)}">{m.group(1)}</a></sup>',s)
    open(d+'/fragments/'+os.path.basename(f).replace('.txt','.html'),'w',encoding='utf-8').write(s)
print('ok')

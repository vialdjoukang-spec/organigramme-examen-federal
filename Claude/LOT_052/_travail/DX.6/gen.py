import re,glob,os
D=os.path.dirname(os.path.abspath(__file__))
for f in sorted(glob.glob(D+'/raw/p*.txt')):
    t=open(f,encoding='utf8').read()
    t=re.sub(r'\.((?:\[\[[a-z0-9\-]+\]\])+)',r'\1.',t)
    t=re.sub(r'\[\[([a-z0-9\-]+)\]\]',lambda m:'<sup class="r"><a href="#sb-%s">%s</a></sup>'%(m.group(1),m.group(1)),t)
    open(D+'/fragments/'+os.path.basename(f).replace('.txt','.html'),'w',encoding='utf8').write(t)

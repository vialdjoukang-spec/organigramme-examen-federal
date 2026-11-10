import re,glob,os
D=os.path.dirname(os.path.abspath(__file__))
ID=r'(?:(?:w[0-9a-f]{6}|aips-\d+)-\d+)'
for f in sorted(glob.glob(D+'/src/p*.txt')):
    t=open(f).read()
    t=re.sub(r'\.((?:\[%s\])+)'%ID,r'\1.',t)   # sup avant le point final
    t=re.sub(r'\[(%s)\]'%ID,lambda m:'<sup class="r"><a href="#sb-%s">%s</a></sup>'%(m.group(1),m.group(1)),t)
    open(D+'/fragments/'+os.path.basename(f).replace('.txt','.html'),'w').write(t)

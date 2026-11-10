import re,glob,os
for f in sorted(glob.glob('src/p*.src')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'\{([a-z0-9\-,]+)\}',lambda m:''.join('<sup class="r"><a href="#sb-%s">%s</a></sup>'%(i,i) for i in m.group(1).split(',')),t)
    t=t.replace('<div class="t">','<div class="t" style="overflow-x:auto">')
    t='\n'.join(l.rstrip() for l in t.strip().split('\n'))
    open('fragments/'+os.path.basename(f)[:-4]+'.html','w',encoding='utf-8').write(t+'\n')

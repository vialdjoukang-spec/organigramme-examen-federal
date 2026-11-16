import sys,re
# usage: rp.py file  (reads pairs from stdin separated by lines '@@' ; old\n===\nnew)
f=sys.argv[1]; t=open(f,encoding='utf-8').read()
for blk in sys.stdin.read().split('\n@@\n'):
    if not blk.strip(): continue
    a,b=blk.split('\n===\n'); a=a.strip('\n'); b=b.strip('\n')
    if a not in t: print('MANQUE:',a[:70]); continue
    t=t.replace(a,b,1)
open(f,'w',encoding='utf-8').write(t)

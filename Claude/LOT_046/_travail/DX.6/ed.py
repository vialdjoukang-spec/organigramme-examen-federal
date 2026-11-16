import sys
# usage: python3 ed.py src/pNN.src.html < pairs ; pairs: lines "A\n=>\nB\n----"
p=sys.argv[1]; s=open(p).read()
blocks=sys.stdin.read().split('\n----\n')
bad=0
for b in blocks:
    if not b.strip(): continue
    a,_,c=b.partition('\n=>\n')
    a=a.strip('\n'); c=c.rstrip('\n')
    if a not in s: print('ABSENT:',a[:70]); bad+=1; continue
    s=s.replace(a,c,1)
open(p,'w').write(s); print('ok' if not bad else f'{bad} absents')

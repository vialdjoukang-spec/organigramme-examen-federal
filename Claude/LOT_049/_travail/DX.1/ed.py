import sys,json
# usage: python3 ed.py file <<< JSON list of [old,new]
f=sys.argv[1]; s=open(f).read()
for a,b in json.load(sys.stdin):
    if a not in s: print('ABSENT:',a[:70]); continue
    s=s.replace(a,b)
open(f,'w').write(s)

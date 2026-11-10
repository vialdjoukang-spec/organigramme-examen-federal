import sys,re,json
sys.argv=[sys.argv[0]]
exec(open('build.py').read().split("bad=0")[0])
for l in sys.stdin:
    l=l.strip()
    if not l: continue
    r=res(l) if ':' in l else None
    print('OK ' if r else 'NO ',l[:90],r)

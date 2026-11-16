import re,glob,os,json
B='/home/user/wt/lot-047/Claude/LOT_047/_travail/DX.8/'
P={p['id'] for p in json.load(open(B+'paquet.json'))['passages']}
bad=set()
for f in sorted(glob.glob(B+'src/p*.txt')):
    t=open(f,encoding='utf-8').read()
    def rep(m):
        out=''
        for i in m.group(1).split():
            if i not in P: bad.add((os.path.basename(f),i))
            out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
        return out
    t=t.replace('<div class="t">','<div class="t" style="overflow-x:auto">')
    t=re.sub(r'\[\[([^\]]+)\]\]',rep,t)
    open(B+'fragments/'+os.path.basename(f).replace('.txt','.html'),'w',encoding='utf-8').write(t)
print('ids inconnus:',bad)

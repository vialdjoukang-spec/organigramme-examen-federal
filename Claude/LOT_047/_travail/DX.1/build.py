import re,glob,os,json
P={p['id'] for p in json.load(open('/home/user/wt/lot-047/Claude/LOT_047/_travail/DX.1/paquet.json'))['passages']}
bad=set()
for f in sorted(glob.glob('/home/user/wt/lot-047/Claude/LOT_047/_travail/DX.1/src/p*.txt')):
    t=open(f,encoding='utf-8').read()
    def rep(m):
        out=''
        for i in m.group(1).split():
            if i not in P: bad.add((f,i))
            out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
        return out
    t=t.replace('<div class="t">','<div class="t" style="overflow-x:auto">')
    t=re.sub(r'\[\[([^\]]+)\]\]',rep,t)
    open('/home/user/wt/lot-047/Claude/LOT_047/_travail/DX.1/fragments/'+os.path.basename(f).replace('.txt','.html'),'w',encoding='utf-8').write(t)
print('ids inconnus:',bad)

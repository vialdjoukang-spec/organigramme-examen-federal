import re,json,os,sys
D=os.path.dirname(os.path.abspath(__file__))
P={q['id'] for q in json.load(open(D+'/paquet.json'))['passages']}
AL=dict(EP='w6877fd',DX='w188bab',DM='w4d7c27',FU='w50a8a6',IN='w42c3c1',NU='wd4a7d0',R541='w0e3172',R585='w6f0f4a',R537='w4f6a68',HP='we08a4b',NG='wd076bd',OS='wd8a513',VH='w0546a8',DB='w116bdf',BA='w8b4588')
def one(k):
    k=k.strip()
    m=re.match(r'^a(\d{5})-(\d+)$',k)
    if m: i=f'aips-{m.group(1)}-{m.group(2)}'
    else:
        a,n=k.rsplit('-',1); i=f'{AL[a]}-{n}'
    if i not in P: print('ID INCONNU',k,i); sys.exit(1)
    return f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
def conv(t):
    t=re.sub(r'([.!?])((?:\[\[[^\]]+\]\])+)',lambda m:m.group(2)+m.group(1),t)
    t=t.replace('<div class="t"><table>','<div class="t" style="overflow-x:auto"><table>')
    return re.sub(r'\[\[([^\]]+)\]\]',lambda m:''.join(one(x) for x in m.group(1).split(',')),t)
for f in sorted(os.listdir(D+'/src')):
    if f.endswith('.html'):
        open(D+'/fragments/'+f,'w').write(conv(open(D+'/src/'+f).read()))

import re,glob,os,json
M=dict(G='w468b64',V='w75f58a',R='w7a56a8',M='we8402b',H='wfba9d7',N='w44a799',L='wcdaf96',S='wa9a226',C='w85b6d6',T='wf5b747',Z='w5c9e98',P='w9c2a9c',U='w5ff785',O='wfb1b36',A='aips-67940',B='aips-51480',D='aips-61859')
ids={x['id'] for x in json.load(open('paquet.json'))['passages']}
os.makedirs('fragments',exist_ok=True)
def rep(m):
    k=M[m.group(1)]+'-'+m.group(2)
    if k not in ids: print('ID INCONNU',k)
    return f'<sup class="r"><a href="#sb-{k}">{k}</a></sup>'
for f in sorted(glob.glob('src/p*.html')):
    t=open(f).read()
    t=re.sub(r'([.!?])((?:\[\[[A-Z]\d+\]\])+)',lambda m:m.group(2)+m.group(1),t)
    t=re.sub(r'\[\[([A-Z])(\d+)\]\]',rep,t)
    open('fragments/'+os.path.basename(f),'w').write(t)

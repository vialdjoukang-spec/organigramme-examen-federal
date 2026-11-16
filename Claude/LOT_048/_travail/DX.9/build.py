import re,os,glob
os.chdir('/home/user/wt/lot-048/Claude/LOT_048/_travail/DX.9')
AL={'FI':'w3828cc','ES':'wa52961','IS':'w3089ba','ZP':'wf0e5a6','AG':'w9add71','ZH':'wa798ec','AE':'wef4817','PR':'w372974','MO':'wc4851f','BE':'wd84325','MA':'wa2c582','AC':'wafe6e7','GE':'wa228b2','NM':'wc3aac2','DC':'w9b1872','SC':'w129249','UE':'w2aac93','RM':'we1bd8b','LA':'w00d881'}
def sup(m):
    out=''
    for t in m.group(1).split('|'):
        k,n=t.split('.')
        i=AL[k]+'-'+n
        out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
    return out
for f in sorted(glob.glob('src/p*.html')):
    n=int(re.search(r'p(\d+)',f).group(1))
    s=open(f).read()
    s=re.sub(r'([.!?])\s*(\[\[[^\]]*\]\])',r'\2\1',s)
    s=re.sub(r'\[\[([A-Z0-9]+\.\d+(?:\|[A-Z0-9]+\.\d+)*)\]\]',sup,s)
    s=re.sub(r'\{\{(f\d+)\|([^}]*)\}\}',lambda m:f'<button class="w" popovertarget="dx9-p{n}-{m.group(1)}">{m.group(2)}</button>',s)
    s=re.sub(r'<F (f\d+)>',lambda m:f'<div id="dx9-p{n}-{m.group(1)}" popover class="fenetre">',s)
    s=s.replace('</F>','</div>')
    s=s.replace('<div class="t">','<div class="t" style="overflow-x:auto">')
    s=re.sub(r'\n\s*\n','\n',s)
    open(f'fragments/p{n:02d}.html','w').write(s)

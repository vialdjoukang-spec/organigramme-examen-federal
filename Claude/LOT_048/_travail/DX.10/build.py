import re,os,glob
os.chdir('/home/user/wt/lot-048/Claude/LOT_048/_travail/DX.10')
AL={'RM':'w10bfcf','US':'w776395','LI':'w9420e5','GK':'wacc0d8','UE':'w6e934f','DY':'w2aac93','CC':'w6abe9a','KB':'w5d17c9','SA':'w8e1b4d','BE':'w3f89ed','MO':'w70a360','KU':'w4afef9','SR':'w72502e','CA':'w95ca10','CM':'w286eef','PS':'w5acecb','PR':'we65184','EK':'w4b5269','WE':'wb2ddec','ES':'aips-60574','BX':'aips-52433','NI':'aips-52896'}
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
    s=re.sub(r'\{\{(f\d+)\|([^}]*)\}\}',lambda m:f'<button class="w" popovertarget="dx10-p{n}-{m.group(1)}">{m.group(2)}</button>',s)
    s=re.sub(r'<F (f\d+)>',lambda m:f'<div id="dx10-p{n}-{m.group(1)}" popover class="fenetre">',s)
    s=s.replace('</F>','</div>')
    s=s.replace('<div class="t">','<div class="t" style="overflow-x:auto">')
    s=re.sub(r'\n\s*\n','\n',s)
    open(f'fragments/p{n:02d}.html','w').write(s)

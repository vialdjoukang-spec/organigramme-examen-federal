import re,os,glob
os.chdir('/home/user/wt/lot-048/Claude/LOT_048/_travail/DX.7')
AL={'OF':'wc83488','LI':'wa5ae37','EU':'w7f8b35','EM':'w0cbb91','DE':'w0534a2','SE':'wf7ceda','NC':'wefbded','GN':'wa0dd43','HT':'w9f1282','EN':'wc77f53','NU':'w433018','GB':'w688bfe','GS':'w7f6649','GD':'w362cb2','CH':'w6ef819','SA':'w54d06d','OP':'aips-65660','CI':'aips-51077','FA':'aips-66825','FT':'aips-47160','DO':'aips-62537','CB':'aips-54829','PX':'aips-60228','OX':'aips-61663','KY':'aips-66231','OS':'aips-70192','AC':'w2aac93','AK':'w6e934f','FB':'w7e05da','AM':'wd122d9'}
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
    s=re.sub(r'\{\{(f\d+)\|([^}]*)\}\}',lambda m:f'<button class="w" popovertarget="dx7-p{n}-{m.group(1)}">{m.group(2)}</button>',s)
    s=re.sub(r'<F (f\d+)>',lambda m:f'<div id="dx7-p{n}-{m.group(1)}" popover class="fenetre">',s)
    s=s.replace('</F>','</div>')
    s=s.replace('<div class="t">','<div class="t" style="overflow-x:auto">')
    s=re.sub(r'\n\s*\n','\n',s)
    open(f'fragments/p{n:02d}.html','w').write(s)

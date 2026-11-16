import re,os,glob
os.chdir('/home/user/wt/lot-048/Claude/LOT_048/_travail/DX.6')
AL={'OF':'wc83488','PA':'w657eba','GO':'w03f598','GB':'wd9eb68','AJ':'w84e0f3','RA':'wbe892a','IN':'w862f60','KN':'w4cb2c8','EX':'w013178','NM':'we77875','K4':'w44f9c7','GU':'w4863cc','DE':'w0e7ca6','DY':'w575f2d','LI':'w9053b2','HP':'w7a3d88','EH':'we506cd','KY':'aips-66231','ER':'aips-56072','CI':'aips-51077','FA':'aips-66825','FT':'aips-47160'}
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
    s=re.sub(r'\{\{(f\d+)\|([^}]*)\}\}',lambda m:f'<button class="w" popovertarget="dx6-p{n}-{m.group(1)}">{m.group(2)}</button>',s)
    s=re.sub(r'<F (f\d+)>',lambda m:f'<div id="dx6-p{n}-{m.group(1)}" popover class="fenetre">',s)
    s=s.replace('</F>','</div>')
    s=s.replace('<div class="t">','<div class="t" style="overflow-x:auto">')
    s=re.sub(r'\n\s*\n','\n',s)
    open(f'fragments/p{n:02d}.html','w').write(s)

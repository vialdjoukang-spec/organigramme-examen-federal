import re,glob,os
M=dict(WS='wfb88fb',RV='waf9584',N184='w2082ec',N141='we8827d',UNI='w918a70',JAMA='w86e9fe',OECD='w072d64',ASP='w9121ea',FIN='wc9ba77',LAN='wed298d',SMW='w432b6d',MA='wa677e9',E21='w5eb23b',E26='w84c524',PYL='aips-66366',PAN='aips-59834',OME='aips-56313',ESO='aips-62581',AMX='aips-56203',CLA='aips-57129',MTZ='aips-55280')
def sup(m):
    out=''
    for t in m.group(1).split(','):
        a,n=t.strip().rsplit('-',1); i=f'{M[a]}-{n}'
        out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
    return out
for f in sorted(glob.glob('src/p*.txt')):
    s=open(f).read(); s=re.sub(r'\[\[([^\]]+)\]\]',sup,s)
    open('fragments/'+os.path.basename(f).replace('.txt','.html'),'w').write(s)

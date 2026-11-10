import re,os,glob
AL=dict(R='wc1f218',E='w8cd9a7',S='w50e063',X='wb57d5d',H='w9c617d',C='wc4541d',W='w42f5d4',I='wc03bf7',T='w60d8c0',B='wbe0973',D='w6f37d7',F='w3e6245',N='w18812c',U='wa22f62',SO='aips-54085',CR='aips-56139',AS='aips-66097')
def sup(m):
    out=''
    for a,n in re.findall(r'([A-Z]+)(\d+)',m.group(1)):
        i=AL[a]+'-'+n
        out+='<sup class="r"><a href="#sb-%s">%s</a></sup>'%(i,i)
    return out
def btn(m):
    n,k,l=m.group(1),m.group(2),m.group(3)
    return '<button class="w" popovertarget="dx5-p%s-f%s">%s</button>'%(n,k,l)
for f in sorted(glob.glob('draft/p*.html')):
    s=open(f).read()
    s=re.sub(r'\[\[((?:[A-Z]+\d+[ ,]*)+)\]\]',sup,s)
    s=re.sub(r'\{\{(\d+)-(\d+)\|([^}]*)\}\}',btn,s)
    open('fragments/'+os.path.basename(f),'w').write(s)

import re,glob,os
D='/home/user/wt/lot-053/Claude/LOT_053/_travail/DX.3/'
PM={'M':'w6b9663','U':'wf79658','C':'w042c3a','S':'wfc57ba','Z':'w800e43','W':'wc4f3d4','SH':'wf3083d','IT':'w3b175f','SC':'w95480b','SP':'w9343bf','PR':'w720c7e','B':'w9f1458','L':'aips-53055','A':'wbe29d1','K':'wdf3c85','AT':'aips-61510','IB':'aips-66138'}
def cit(m):
    out=''
    for t in m.group(1).split():
        mm=re.fullmatch(r'([A-Z]+)(\d+)',t)
        i=PM[mm.group(1)]+'-'+mm.group(2)
        out+='<sup class="r"><a href="#sb-%s">%s</a></sup>'%(i,i)
    return out
for f in sorted(glob.glob(D+'src/p*.txt')):
    s=open(f,encoding='utf8').read()
    s=re.sub(r'\[\[([A-Z0-9 ]+)\]\]',cit,s)
    s=s.replace('<table>','<table>')
    open(D+'fragments/'+os.path.basename(f).replace('.txt','.html'),'w',encoding='utf8').write(s)

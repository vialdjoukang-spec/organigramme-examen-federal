import re,glob,os
D=os.path.dirname(os.path.abspath(__file__))
M={'A':'wa773d2','N1':'w6b8b39','N2':'w5084dc','N3':'w080a44','N4':'w97aa13','C':'wa5dccd','G':'wf6b17e','Y':'w3f4350','R':'w69f6d7',
'D':'wbfc377','Gd':'wabe6d6','Sw':'w0ef8be','W':'wa32d20','Sd':'wdc03d2','Ch':'w6b3307','Fx':'wec0c4f','H':'w515373','Ae':'w84cbf8',
'S':'wa02fca','Hu':'w683c0b','Rh':'aips-53609','Me':'aips-57272','Ne':'aips-65839','Mi':'aips-65378','Nx':'w11a3a4'}
def rep(m):
    out=''
    for t in m.group(1).split(','):
        k,n=t.strip().split(':'); i=f'{M[k]}-{n}'
        out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
    return out
for f in sorted(glob.glob(D+'/src/p*.html')):
    s=open(f).read()
    s=re.sub(r'\[\[([^\]]+)\]\]',rep,s)
    open(D+'/fragments/'+os.path.basename(f),'w').write(s)

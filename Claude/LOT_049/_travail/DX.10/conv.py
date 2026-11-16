import re,glob,os
AL={'B':'w59987b','P':'wb83870','F':'w81672a','I':'w2da823','H':'w0b5a11','J':'wcf2ed3','K':'wab8001','Q':'we8a658','S':'w341f05','L':'wb46eaa','R':'wadb7e0','M':'w87cf05','E':'w3c8ecc','C':'wad3042','N':'wd0cf25','A':'w574a4f','T':'wf1368b','Z':'w9abb86'}
def rep(m):
    return ''.join(f'<sup class="r"><a href="#sb-{AL[x[0]]}-{x[1:]}">{AL[x[0]]}-{x[1:]}</a></sup>' for x in m.group(1).split())
here=os.path.dirname(os.path.abspath(__file__))
for f in sorted(glob.glob(here+'/src/p*.txt')):
    t=open(f).read()
    t=re.sub(r'\[\[([A-Z]\d+(?: [A-Z]\d+)*)\]\]',rep,t)
    open(here+'/fragments/'+os.path.basename(f).replace('.txt','.html'),'w').write(t)
print('ok')

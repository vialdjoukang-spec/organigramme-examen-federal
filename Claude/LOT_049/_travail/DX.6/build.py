import re,sys,os
AL={'P':'w5b3ed9','LA':'aips-30630','N1':'aips-55459','N2':'aips-70562','E26':'wa046a5','AJ':'w773561','PK':'w57f1e1','CA':'wb5e447','MB':'wdf0ae3','TK':'w123bd2','DE':'wfa97d8','CP':'w85dbbe','L1':'w584bf8','L2':'wcabe41','L3':'w5d105e','MO':'w1c91e3','CO':'w27ff16','DO':'w65f53f','HG':'w98d0e4','U21':'we36cd8','U23':'wb8230a'}
def cit(m):
    out=''
    for t in m.group(1).split(','):
        t=t.strip(); a,n=t.rsplit('-',1); i=AL[a]+'-'+n
        out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
    return out
d=os.path.dirname(os.path.abspath(__file__))
for f in sorted(os.listdir(d+'/src')):
    if not f.endswith('.src'): continue
    s=open(d+'/src/'+f,encoding='utf-8').read()
    s=re.sub(r'\{((?:[A-Z0-9]+-\d+(?:\s*,\s*)?)+)\}',cit,s)
    open(d+'/fragments/'+f.replace('.src','.html'),'w',encoding='utf-8').write(s)
print('ok')

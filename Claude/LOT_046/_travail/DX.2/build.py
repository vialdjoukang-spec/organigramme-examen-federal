import re,os,sys
AL={'H':'w149687','E21':'we36cd8','E23':'w0514b9','ADV':'wb9fda7','STR':'w0f96c8','DOS':'w65f53f','LUS':'w584bf8','LU2':'w6483eb','CH':'w382b62','CPO':'w85dbbe','CG':'w5b3ed9','TS':'w4856f7','DU':'w67f662','AC':'we1c591','PR':'wb7be93','UD':'w6bda98','BFS':'w19cae6','BP':'w7e1b15'}
def cit(m):
    out=''
    for i in m.group(1).split('|'):
        i=i.strip()
        k=re.match(r'([A-Za-z0-9]+?)-(\d+)$',i)
        if not i.startswith('aips') and k and k.group(1) in AL: i=AL[k.group(1)]+'-'+k.group(2)
        out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
    return out
os.makedirs('fragments',exist_ok=True)
for f in sorted(os.listdir('src')):
    if not f.endswith('.html'): continue
    t=open('src/'+f).read()
    t=re.sub(r'\[\[([^\]]+)\]\]',cit,t)
    t=t.replace('<div class="t"><table>','<div class="t" style="overflow-x:auto"><table>')
    open('fragments/'+f,'w').write(t)
print('ok')

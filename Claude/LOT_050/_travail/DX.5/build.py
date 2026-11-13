import re,os,glob
D=os.path.dirname(os.path.abspath(__file__))
os.makedirs(D+'/fragments',exist_ok=True)
def cite(m):
    return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in m.group(1).split(','))
for f in sorted(glob.glob(D+'/src/p*.txt')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'\^([\w.\-:,]+)\^',cite,t)
    t=t.replace('<div class="t">','<div class="t" style="overflow-x:auto">')
    t='\n'.join(l.strip() for l in t.split('\n') if l.strip())+'\n'
    open(D+'/fragments/'+os.path.basename(f).replace('.txt','.html'),'w',encoding='utf-8').write(t)
print('ok')

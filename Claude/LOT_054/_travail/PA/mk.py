import re,glob,os
os.chdir('/home/user/wt/lot-054/Claude/LOT_054/_travail/PA')
def cite(m):
    return ''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(','))
for f in sorted(glob.glob('src/p*.html')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'([.!?])((?:\{\{[^}]+\}\})+)',r'\2\1',t)
    t=re.sub(r'\{\{([^}]+)\}\}',cite,t)
    t=t.replace('<div class="t"><table>','<div class="t" style="overflow-x:auto"><table>')
    open('fragments/'+os.path.basename(f),'w',encoding='utf-8').write(t)
print('ok')

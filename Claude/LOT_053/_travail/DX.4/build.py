import re,glob,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def sup(m):
    return ''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(','))
for f in sorted(glob.glob('src/p*.txt')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'\{\{([^}]+)\}\}',sup,t)
    t=t.replace('<table>','<div class="t" style="overflow-x:auto;"><table>').replace('</table>','</table></div>')
    open('fragments/'+os.path.basename(f).replace('.txt','.html'),'w',encoding='utf-8').write(t)

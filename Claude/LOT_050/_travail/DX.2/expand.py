import re,glob,os
for f in sorted(glob.glob('src/p*.txt')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'\{\{([^}]+)\}\}',lambda m:''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(',')),t)
    t=t.replace('<TABLE>','<div class="t" style="overflow-x:auto"><table>').replace('</TABLE>','</table></div>')
    open('fragments/'+os.path.basename(f).replace('.txt','.html'),'w',encoding='utf-8').write(t)

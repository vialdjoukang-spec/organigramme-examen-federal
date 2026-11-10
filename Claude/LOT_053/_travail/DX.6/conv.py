import re,glob,os
D='/home/user/wt/lot-053/Claude/LOT_053/_travail/DX.6/'
def cit(m):
    return ''.join('<sup class="r"><a href="#sb-%s">%s</a></sup>'%(t,t) for t in m.group(1).split())
for f in sorted(glob.glob(D+'src/p*.txt')):
    s=open(f,encoding='utf8').read()
    s=re.sub(r'\[\[([A-Za-z0-9\- ]+)\]\]',cit,s)
    s=s.replace('<div class="t"><table>','<div class="t" style="overflow-x:auto;"><table>')
    open(D+'fragments/'+os.path.basename(f).replace('.txt','.html'),'w',encoding='utf8').write(s)

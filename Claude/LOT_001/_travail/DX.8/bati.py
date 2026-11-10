import re,glob,os
AL={'D':'wedbb38','H':'w2a9a6a','E':'w5984aa','O':'w446bbb','A':'w0211eb','V':'w985243','C':'wd3b7d1','B':'wad7cf6','b':'w192b8b','P':'wd99f25','G':'wc9a494','R':'w1d8720','F':'w50e187','BK':'aips-66834','DV':'aips-67313','TV':'aips-57316','TI':'aips-63052','BA':'aips-48306'}
def sup(m):
    out=''
    for t in m.group(1).split():
        a,n=re.match(r'([A-Za-z]+)(\d+)$',t).groups()
        i=f'{AL[a]}-{n}'
        out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
    return out
for f in sorted(glob.glob('src/p*.txt')):
    h=open(f,encoding='utf-8').read()
    h=re.sub(r'\{([A-Za-z]+\d+(?: [A-Za-z]+\d+)*)\}',sup,h)
    h=h.replace('<TAB>','<div class="t" style="overflow-x:auto"><table>').replace('</TAB>','</table></div>')
    open('fragments/'+os.path.basename(f).replace('.txt','.html'),'w',encoding='utf-8').write(h)

import re,glob,os
def exp(s):
    def r(m):
        return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in m.group(1).split('|'))
    return re.sub(r'\[\[([\w\-|]+)\]\]',r,s)
for f in sorted(glob.glob('src/p*.txt')):
    t=open(f,encoding='utf-8').read()
    out='fragments/'+os.path.basename(f).replace('.txt','.html')
    open(out,'w',encoding='utf-8').write(exp(t))
print('ok')

import re,glob,os
A={'L':'w8c25c3','V':'wde04e0','N':'w6c9eaf','S':'w8afa22','M':'w0b53b9','R':'wbce3de','P':'w134096','T':'w75f58a','X':'wcdaf96','F':'waaf6e8','G':'w3beb70','E':'aips-62581','Z':'aips-52710'}
def cit(m):
    out=''
    for t in m.group(1).split(','):
        t=t.strip(); i=A[t[0]]+'-'+t[1:]
        out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
    return out
def btn(m):
    return f'<button class="w" popovertarget="{m.group(1)}">{m.group(2)}</button>'
for f in sorted(glob.glob('src/p*.html')):
    s=open(f,encoding='utf-8').read()
    s=re.sub(r'([.!?])(\[\[[^\]]+\]\])',r'\2\1',s)
    s=s.replace('<div class="t">','<div class="t" style="overflow-x:auto">')
    s=re.sub(r'\[\[([^\]]+)\]\]',cit,s)
    s=re.sub(r'\{\{([\w-]+)\|([^}]+)\}\}',btn,s)
    s=re.sub(r'\n\s*\n','\n',s)
    open('fragments/'+os.path.basename(f),'w',encoding='utf-8').write(s)

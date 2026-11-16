import re,sys,glob,os
AL={'H':'w18c561','G':'w1aad15','E':'w747e82','L':'w49bdc7','F':'wbb4b76','S':'wf6fa28','R':'wed98bf','Y':'wc950f6','Z':'wfeea81','A':'we8719b','P':'w70b4ea'}
def ex(m):
    out=[]
    for tok in m.group(1).split(';'):
        tok=tok.strip()
        if tok.startswith('aips-'):
            out.append(tok)
        else:
            k,ns=tok.split(':')
            out+= [f'{AL[k]}-{n}' for n in ns.split(',')]
    return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in out)
for f in sorted(glob.glob('drafts/p*.src')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'\[\[([^\]]+)\]\]',ex,t)
    open('fragments/'+os.path.basename(f).replace('.src','.html'),'w',encoding='utf-8').write(t)

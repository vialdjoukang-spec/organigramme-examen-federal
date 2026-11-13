import re,sys,os
M={'K':'w1d36ef','C':'w1280e5','R':'w405dc9','D':'w174b3d','F':'wda45ff','E':'wf664d9','S':'wf38a30','T':'w070298','Y':'w15bb5b','A':'w9e1de4','G':'wdd6672','L':'wfc8bb3','M':'w6eb6e8','P':'w3dfe1b','H':'wfbf21d','Q':'wadef15','W':'w1b7508','V':'waecbda','Z':'wccacc7','N':'w57687d','U':'wf4ca70','B':'w75f58a','J':'wfba9d7','X':'wcdaf96','I':'w08e537','O':'w31946b','DP':'wd65a33','DI':'w5b21f8','CO':'w65e588'}
def cid(t):
    t=t.strip()
    if t.startswith('a'): return 'aips-'+t[1:]
    m=re.match(r'([A-Z]{1,2})(\d+)$',t)
    return M[m.group(1)]+'-'+m.group(2)
def cite(m):
    return ''.join(f'<sup class="r"><a href="#sb-{cid(t)}">{cid(t)}</a></sup>' for t in m.group(1).split(','))
for f in sorted(os.listdir('src')):
    if not f.endswith('.txt'): continue
    n=int(f[1:3]); s=open('src/'+f,encoding='utf-8').read()
    s=re.sub(r'\[\[([^\]]+)\]\]',cite,s)
    s=re.sub(r'\{\{(\d+)\.(\d+)\|([^}]+)\}\}',lambda m:f'<button class="w" popovertarget="dx7-p{m.group(1)}-f{m.group(2)}">{m.group(3)}</button>',s)
    s=re.sub(r'^%%F (\d+)\.(\d+)\s*$',lambda m:f'<div id="dx7-p{m.group(1)}-f{m.group(2)}" popover class="fenetre">',s,flags=re.M)
    s=re.sub(r'^%%E\s*$','</div>',s,flags=re.M)
    s=s.replace('<div class="t"><table>','<div class="t" style="overflow-x:auto"><table>')
    s=s.replace('~',' ')  # insécable fine
    open(f'fragments/p{n:02d}.html','w',encoding='utf-8').write(s)

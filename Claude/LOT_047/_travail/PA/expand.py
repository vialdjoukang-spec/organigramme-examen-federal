import re,glob,os,json
P={p['id']:p['texte'] for p in json.load(open('paquet.json'))['passages']}
def cit(m):
    ids=[i.strip() for i in m.group(1).split(',')]
    for i in ids:
        if i not in P: raise SystemExit('ID INCONNU '+i)
    return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)
for f in sorted(glob.glob('src/p*.txt')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'[ \t]*\[\[([^\]]+)\]\]',cit,t)
    t=re.sub(r'@w\(([^|)]+)\|([^)]+)\)',lambda m:f'<button class="w" popovertarget="pa-{m.group(1)}">{m.group(2)}</button>',t)
    t=re.sub(r'@f\(([^)]+)\)',lambda m:f'<div id="pa-{m.group(1)}" popover class="fenetre">',t)
    t=t.replace('@/f','</div>')
    open('fragments/'+os.path.basename(f).replace('.txt','.html'),'w',encoding='utf-8').write(t)
print('ok')

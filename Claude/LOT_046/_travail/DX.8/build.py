import re,json,os
P={x['id'] for x in json.load(open('paquet.json'))['passages']}
bad=0
def sub(m):
    global bad
    out=''
    for i in m.group(1).split(','):
        i=i.strip()
        if i not in P: print('ID INCONNU',i); bad+=1
        out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
    return out
os.makedirs('fragments',exist_ok=True)
for f in sorted(os.listdir('src')):
    s=open('src/'+f).read()
    open('fragments/'+f.replace('.src.html','.html'),'w').write(re.sub(r'\{\{([^}]+)\}\}',sub,s))
print('ok' if not bad else f'{bad} ids inconnus')

import re,os,json
P={x['id'] for x in json.load(open('paquet.json'))['passages']}
bad=0
for f in sorted(os.listdir('src')):
    s=open('src/'+f).read()
    def rep(m):
        global bad
        out=''
        for i in m.group(1).split(','):
            i=i.strip()
            if i not in P: print('ID INCONNU',i,f); bad+=1
            out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
        return out
    open('fragments/'+f.replace('.src',''),'w').write(re.sub(r'\[\[(.*?)\]\]',rep,s))
print('ok' if not bad else bad)

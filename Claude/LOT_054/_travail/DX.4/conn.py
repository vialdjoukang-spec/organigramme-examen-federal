import re,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
tot=cn=0
for n in range(1,15):
    h=open(f'fragments/p{n:02d}.html').read()
    ph=[(t,b) for tg,b,t in c.phrases_html(h) if tg!='td']
    k=sum(1 for t,b in ph if c.CONNECT.search(t)); tot+=len(ph); cn+=k
    paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S)
    bad=[c.texte(p)[:90] for p in paras if len(c.texte(p).split())>40 and not c.CONNECT.search(c.texte(p))]
    print(n,len(ph),k,round(100*k/max(1,len(ph))),'sans conn:',len(bad))
    for b in bad: print('    -',b)
print(tot,cn,round(100*cn/tot))

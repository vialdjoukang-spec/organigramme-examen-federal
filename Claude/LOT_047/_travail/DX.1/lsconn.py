import re,sys,glob,html
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
for f in sorted(glob.glob('fragments/p*.html')):
    h=open(f).read()
    paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
    for i,p in enumerate(paras):
        t=C.texte(re.sub(r'<sup class="r">.*?</sup>','',p,flags=re.S))
        if len(t.split())>40 and not C.CONNECT.search(t):
            print(f[-8:-5],i,len(t.split()),t[:110])

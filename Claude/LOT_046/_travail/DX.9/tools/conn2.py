import re,sys,glob,os
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as c
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
i=0
for f in sorted(glob.glob(D+'/fragments/p*.html')):
    h=open(f).read(); name=os.path.basename(f)
    for p in re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I):
        t=c.texte(p)
        if len(t.split())>40 and not c.CONNECT.search(t):
            ss=re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])', re.sub(r'<sup class="r">.*?</sup>','',p,flags=re.S))
            ss=[c.texte(s) for s in ss]
            # drop heading-only
            print(i,name,'|', ' || '.join(s[:70] for s in ss[:5])); i+=1

import re,sys,html
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as c
h=open('/tmp/dx4test.html',encoding='utf-8').read()
for p in re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S):
    t=c.texte(p)
    if len(t.split())>40 and not c.CONNECT.search(t): print(len(t.split()),t[:110])

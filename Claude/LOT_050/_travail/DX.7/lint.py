import re,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
h=open('/home/user/wt/lot-050/Claude/LOT_050/LOT_050_Phase_B_V0_DX.7.html',encoding='utf-8').read()
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
for p in paras:
    t=c.texte(p)
    if len(t.split())>40 and not c.CONNECT.search(t): print('SANSCONN:',t[:160])
for tag,b,t in c.phrases_html(c.SOURCES.sub(' ',h)):
    if tag!='td' and len(t.split())>=4 and not c.CONNECT.search(t) and '-v' in sys.argv: print('  noconn:',t[:100])

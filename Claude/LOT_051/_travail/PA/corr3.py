import sys
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad')
from rep import R,sup
r=R('PA')
r('p09.html',"la stratégie ESC 2024 choisit le test selon la probabilité prétest. Elle recommande","la stratégie ESC choisit le test selon la probabilité prétest. Dans la version de 2024, elle recommande")
r('p11.html',"puis 100 mg par jour"+sup('aips-51795-4')+". Les recommandations lux","puis 100 mg par jour"+sup('aips-51795-0','aips-51795-4')+". Les recommandations lux")
print(r.fail)

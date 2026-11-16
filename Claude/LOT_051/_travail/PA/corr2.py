import sys
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad')
from rep import R,sup
r=R('PA')
r('p11.html',"exceptionnellement 2 capsules de 1,6 mg","exceptionnellement deux capsules (1,6 mg)")
r('p11.html',"Swissmedic 58094) est contre-indiqué au troisième trimestre, en cas d'insuffisance cardiaque grave (NYHA III–IV) et chez l'enfant de moins de 14 ans"+sup('aips-58094-7'),"Swissmedic 58094) est contre-indiqué au troisième trimestre, en cas d'insuffisance cardiaque grave (NYHA III–IV) et chez l'enfant de moins de 14 ans"+sup('aips-58094-0','aips-58094-7'))
r('p11.html',"sauf si la systolique est inférieure à 90 mmHg"+sup('aips-40558-3','aips-40558-5')+".","sauf si la systolique est inférieure à 90 mmHg"+sup('aips-40558-0','aips-40558-3','aips-40558-5')+".")
r('p11.html',"elle ne doit pas être administrée, sauf en cas de nécessité absolue"+sup('aips-36830-2','aips-36830-17'),"elle ne doit pas être administrée, sauf en cas de nécessité absolue"+sup('aips-36830-0','aips-36830-2','aips-36830-17'))
r('p09.html',"Une fois les urgences écartées, la stratégie ESC 2024 choisit le test selon la probabilité prétest : un score calcique de 5 à 15 %, le scanner coronaire ou l'imagerie de stress de 15 à 50 %","Une fois les urgences écartées, la stratégie ESC 2024 choisit le test selon la probabilité prétest. Elle recommande un score calcique de 5 à 15 %, le scanner coronaire ou l'imagerie de stress de 15 à 50 %")
r('p10.html',"alors on évoque un angor stable et on choisit le test selon la probabilité prétest : score calcique de 5 à 15 %, scanner coronaire ou imagerie de stress de 15 à 50 %","alors on évoque un angor stable et on choisit le test selon la probabilité prétest, de 5 à 50 %")
print(r.fail)

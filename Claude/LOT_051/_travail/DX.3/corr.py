import sys,json,glob
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad')
from rep import R,sup
r=R('DX.3')
A=json.load(open('/home/user/wt/lot-051/Claude/LOT_051/audits/LOT_051_Phase_B_V0_DX.3.html.audit.json'))['corrections']
SKIP=("Cette leçon ne peut donner aucune dose","Leur posologie ne figure pas","L'ergométrie est, en raison","Le sémaglutide réduit les événements cardiovasculaires chez les patients obèses","L'ergométrie est le test de base")
for c in A:
    av=c['avant']; ap=c['apres']
    if av.startswith(SKIP): continue
    hit=None
    for f in sorted(glob.glob(r.d+'p*.html')):
        t=open(f,encoding='utf-8').read()
        if t.count(av)==1: hit=f.split('/')[-1]; break
    if not hit: print('INTROUVABLE',av[:60]); r.fail+=1; continue
    r(hit,av,ap)
# AIPS nicorandil et sémaglutide
r('p11.html',"La trimétazidine et le nicorandil figurent dans les recommandations européennes. Cette leçon ne peut donner aucune dose, car aucune information professionnelle suisse correspondante n'a été retrouvée dans le corpus lu. La colchicine à faible dose et le sémaglutide reçoivent une recommandation de classe IIa dans les cas indiqués"+sup('w42e5fe-23')+". Leur posologie ne figure pas dans cette leçon, faute d'une information professionnelle suisse lue pour cette indication.</div>",
 "La trimétazidine figure dans les recommandations européennes, mais aucune information professionnelle suisse correspondante n'a été retrouvée : elle est citée comme classe, sans dose.</div>"
 "<div class=\"p\">Le nicorandil (Nicorandil Rivopharm, Swissmedic 60431) traite l'angor stable de l'adulte insuffisamment contrôlé par les traitements de première ligne ou intolérant à ceux-ci"+sup('aips-60431-0','aips-60431-1')+". On administre en général 1 comprimé à 10 mg deux fois par jour, et jusqu'à 1 comprimé à 20 mg deux fois par jour en cas de réponse insuffisante"+sup('aips-60431-3')+". Il est contre-indiqué en cas de choc, d'hypotension grave et d'association aux inhibiteurs de la phosphodiestérase de type 5"+sup('aips-60431-5')+". Des ulcérations gastro-intestinales, cutanées et muqueuses ont été rapportées, et elles imposent l'arrêt durable du traitement"+sup('aips-60431-6','aips-60431-7')+".</div>"
 "<div class=\"p\">La colchicine à faible dose reçoit une recommandation de classe IIa dans les cas indiqués, mais aucune information professionnelle suisse correspondante n'a été retrouvée : elle est citée comme classe, sans dose"+sup('w42e5fe-23')+". Le sémaglutide reçoit lui aussi une recommandation de classe IIa"+sup('w42e5fe-23')+". Wegovy (Swissmedic 68798) est indiqué pour réduire le risque d'événements cardiovasculaires graves chez l'adulte atteint de maladie cardiovasculaire établie et d'un IMC d'au moins 27 kg/m²"+sup('aips-68798-0','aips-68798-2')+". La dose augmente de 0,25 mg une fois par semaine pendant 16 semaines jusqu'à la dose d'entretien de 2,4 mg une fois par semaine, par voie sous-cutanée"+sup('aips-68798-5','aips-68798-11')+".</div>")
r('p12.html',"Le sémaglutide réduit les événements cardiovasculaires chez les patients obèses ou en surpoids sans diabète, avec une recommandation de classe IIa, niveau B"+sup('w42e5fe-23'),
 "Le sémaglutide réduit les événements cardiovasculaires chez l'adulte en surpoids atteint d'une maladie cardiovasculaire établie, en classe IIa, niveau B"+sup('w42e5fe-23')+". L'AIPS limite d'ailleurs cette indication à la maladie cardiovasculaire établie, ce qui exclut la prévention primaire"+sup('aips-68798-2'))
# ergométrie
r('p08.html',"L'ergométrie est le test de base lorsque la probabilité clinique est intermédiaire, entre 15 et 85 %"+sup('wfba9d7-13'),"Selon la stratégie ESC récente, une probabilité modérée de 15 à 50 % justifie un scanner coronaire ou une imagerie de stress"+sup('w42e5fe-16')+", et le texte HUG ancien qui faisait de l'ergométrie le test de base n'est plus la référence")
r('p09.html',"L'ergométrie est, en raison de son coût et de son accessibilité, l'examen de dépistage de choix en l'absence de contre-indication"+sup('wfba9d7-10')+". Sa sensibilité atteint",
 "Les recommandations européennes récentes choisissent le test diagnostique selon la probabilité prétest, et non plus l'ergométrie par défaut"+sup('w42e5fe-16')+". Selon l'ancien texte HUG, la sensibilité de l'ergométrie atteint")
r('p08.html',"inférieure ou égale à 80"+sup('w863027-17'),"inférieure ou égale à 0,80"+sup('w863027-17'))
r('p08.html',"FFR inférieure ou égale à 80</td>","FFR inférieure ou égale à 0,80</td>")
# connecteurs mécaniques
r('p03.html',"En outre, dans le syndrome coronarien aigu, au contraire, la rupture","Dans le syndrome coronarien aigu, la rupture")
r('p03.html',"Par ailleurs, un thrombus intracoronaire","Un thrombus intracoronaire")
r('p08.html',"Ainsi, un homme de 55 ans","Par exemple, un homme de 55 ans")
r('p01.html',"Ainsi, la classe la plus légère","La classe la plus légère")
r('p12.html',"Ainsi, une alimentation à base de végétaux","Une alimentation à base de végétaux")
r('p11.html',"Ainsi, la décision revient","La décision revient")
r('p11.html',"Ainsi, un angor récent expose","Un angor récent expose")
r('p11.html',"Par ailleurs, les recommandations européennes servent","Les recommandations européennes servent")
r('p11.html',"Par conséquent, des garde-fous","Des garde-fous") if False else None
print('fail',r.fail)

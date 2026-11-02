"""Première PhaseA structurée ; revue interne, iconographie et sources à compléter."""
from pathlib import Path
from html import escape
import re
from format_lecon import Lesson,paras,table,steps
D=Path(__file__).resolve().parent
raw=(D/'PHASE_A_REDACTION.md').read_text()
parts=re.split(r'\n## \d+\. [^\n]+\n',raw)[1:15]
assert len(parts)==14
def md(s):
 s=escape(s)
 return re.sub(r'\*\*(.*?)\*\*',r'<strong>\1</strong>',s)
def body(s):return paras(*(md(x.strip()) for x in s.strip().split('\n\n') if x.strip()))
l=Lesson('Anomalies à l’inspection')
dx=[
('Accident vasculaire cérébral','Asymétrie faciale ou motrice brutale, parole inhabituelle.','Heure de début, examen neurologique et filière urgente avec imagerie.','🚩 Urgence immédiate même si les signes régressent.'),
('Sepsis avec purpura','Lésions non blanchissantes et altération générale, fièvre possible.','Évaluer circulation et vigilance ; filière urgente, prélèvements sans retarder les soins.','🚩 Urgence immédiate ; critères pédiatriques distincts.'),
('Insuffisance respiratoire aiguë','Effort respiratoire, posture, cyanose possible.','Constantes, oxygénation et ventilation selon gravité ; rechercher le mécanisme.','🚩 Détresse : action immédiate ; absence de cyanose non excluante.'),
('Anémie','Pâleur avec fatigue, dyspnée ou saignement selon contexte.','Hémogramme puis mécanisme de l’anémie, en intégrant la tolérance.','Urgence si instabilité ou hémorragie ; couleur seule non diagnostique.'),
('Obstruction biliaire','Ictère, urines foncées ou selles décolorées selon contexte.','Bilan hépatique et exploration dirigée des voies biliaires.','Urgence si signes infectieux ou instabilité ; ictère non spécifique.'),
('Hépatopathie chronique décompensée','Ictère, distension abdominale, œdèmes ou signes cutanés possibles.','Rechercher défaillance, infection, saignement et confusion ; bilan spécialisé.','Urgence devant complication aiguë ; aspect seul insuffisant.'),
('Insuffisance cardiaque','Gonflement des chevilles, dyspnée et modification rapide du poids.','Examen cardiorespiratoire et confirmation fonctionnelle selon présentation.','🚩 Étouffement ou malaise : urgence ; œdème non spécifique.'),
('Thrombose veineuse profonde','Asymétrie récente d’un membre, gonflement et douleur possibles.','Estimer la probabilité clinique et choisir le parcours de confirmation.','Urgence si dyspnée ou douleur thoracique associée ; inspection non confirmatoire.'),
('Thrombopénie','Pétéchies, ecchymoses ou saignement muqueux selon le tableau.','Numération plaquettaire et recherche du mécanisme ; apprécier gravité hémorragique.','Urgence si saignement important ou atteinte générale.'),
('Cancer bronchopulmonaire','Hippocratisme acquis possible avec symptômes respiratoires ou généraux.','Confirmer le signe et explorer selon le contexte ; plusieurs causes possibles.','Investigation orientée ; le signe photographique ne prouve pas la tumeur.')]
comparison=table(['Diagnostic proposé','Indices à l’inspection et contexte','Confirmation ou décision','Priorité et limite'],[[f'DX.{i} — {a}',b,c,d] for i,(a,b,c,d) in enumerate(dx,1)])
comparison+=paras('<strong>Ordre pédagogique, sans classement suisse de fréquence.</strong> Ces dix propositions organisent le raisonnement et ne couvrent pas toutes les anomalies visibles. Elles doivent être relues et documentées avant gel de la liste. Le contexte peut imposer une autre urgence : traumatisme, anaphylaxie, infection cutanée profonde ou autre défaillance.')
refmap={1:(4,),2:(4,),3:(4,5),4:(1,2,3),5:(1,2,3,5),6:(4,5),7:(1,2,3,5),8:(1,5),9:(1,2,3,4,5),10:(1,2,3),11:(1,2,3,5),12:(3,),13:(1,2,3,4,5)}
main=[
'Une {anomalie visible} est un constat clinique à décrire avant d’en nommer la cause. L’examen précise sa distribution et son évolution, puis recherche son retentissement.',
'Le {contexte de découverte} modifie la probabilité et la priorité. Aucun classement unique des causes ne convient à toutes les populations ; une anomalie aiguë se distingue d’une particularité ancienne stable.',
'Les {mécanismes} concernent la couleur, le volume et le mouvement. L’apparence oriente la confirmation, mais ne mesure pas directement la fonction d’un organe.',
'La {gravité} dépend de l’état général et des signes associés. Détresse respiratoire, déficit brutal, altération de vigilance ou purpura fébrile préoccupant imposent une évaluation urgente.',
'L’{anamnèse} date le signe et recherche symptômes associés, expositions et traitements. Une photographie antérieure peut aider, à condition d’en connaître les limites.',
'L’{examen physique} associe observation globale, comparaison des côtés et exploration ciblée. Les constantes et les autres gestes complètent ce que l’inspection ne peut établir.',
'Le {regroupement syndromique} relie couleur, morphologie et dynamique. Les hypothèses doivent rester compatibles avec le contexte et les constatations objectives.',
'La {confirmation du signe} précède le diagnostic étiologique. Un purpura, un ictère ou un hippocratisme ne suffit pas à identifier sa cause.',
'Les {examens complémentaires} répondent à une question précise. Leur choix dépend du signe, des hypothèses et de la gravité ; aucune batterie identique ne convient à tous.',
'L’{algorithme clinique} commence par la stabilité, puis décrit le signe et explore son mécanisme. Une situation menaçante doit être traitée sans attendre un dossier exhaustif.',
'La {prise en charge} vise la cause et le retentissement. Les prescriptions dépendent du diagnostic, de l’âge et du contexte, avec vérification suisse de toute posologie.',
'La {surveillance} compare des éléments définis dans des conditions cohérentes. Une amélioration visible doit être confrontée aux symptômes et à la fonction.',
'Les {points clés} séparent constat, danger, hypothèse et action. Les limites de l’examen et les incertitudes doivent accompagner la conclusion.'
]
for i in range(1,14):
 clinical=parts[i-1]
 if i==9:clinical=clinical.split('**Déclencheur iconographique :**')[0]
 detail=body(clinical)
 if i==7:detail+=comparison
 if i==9:
  detail+=paras('<strong>Interpréter sans attribuer trop vite :</strong> une même image peut illustrer un signe partagé par plusieurs maladies. La photographie documente l’apparence ; elle ne mesure pas la perfusion, la ventilation ou la numération sanguine. Les clichés des examens demandés doivent ensuite être lus selon leur technique et leur question.')
 l.add(main[i-1],detail,refmap[i])
quiz=[]
for line in parts[13].split('\n'):
 m=re.match(r'\d+\. \*\*(.*?)\*\* (.+)',line)
 if m:quiz.append((m[1],m[2]))
assert len(quiz)==14
l.quiz(quiz,(1,2,3,4,5));l.write()

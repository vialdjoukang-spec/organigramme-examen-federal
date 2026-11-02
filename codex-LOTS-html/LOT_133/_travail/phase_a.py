"""Première PhaseA structurée ; revue interne, iconographie et sources à compléter."""
from pathlib import Path
from html import escape
import re
from format_lecon import Lesson,paras,table,steps,ref
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
('Accident vasculaire cérébral','Asymétrie faciale ou motrice, parole inhabituelle, début brutal.','Examen neurologique, fonctions vitales et imagerie cérébrale urgente.','Scanner et/ou IRM ; bilan vasculaire et cardiaque orienté ensuite.','🚩 Appeler immédiatement le 144, même si les signes régressent.',(2,5)),
('Sepsis avec purpura (suspecté)','Lésions non blanchissantes et altération générale ; rechercher une infection.','Conscience, circulation, respiration et diurèse ; lactate, hémogramme, hémostase, fonctions rénale/hépatique et cultures ciblées.','Infection avec défaillance d’organe ; cultures négatives non excluantes.','🚩 Purpura fulminans : prise en charge immédiate ; prélèvements sans retard de l’antibiothérapie. Le purpura seul ne prouve pas le sepsis.',(6,)),
('Insuffisance respiratoire aiguë','Effort respiratoire, tirage, cyanose possible, épuisement ou trouble de conscience.','Fréquence respiratoire, saturation pulsée et qualité du signal ; radiographie thoracique et ECG orientent la cause.','Gazométrie artérielle : oxygénation, gaz carbonique et pH, interprétés avec l’oxygène reçu.','🚩 Détresse : stabiliser sans attendre ; absence de cyanose non excluante.',(7,)),
('Anémie','Pâleur avec fatigue, dyspnée ou saignement selon le contexte.','Hémogramme, volume globulaire moyen, réticulocytes ; ferritine, B12/folates ou hémolyse selon la branche.','Hémoglobine mesurée ; caractérisation biologique puis recherche de cause.','Urgence si instabilité ou hémorragie ; pâleur seule non diagnostique.',(8,)),
('Obstruction biliaire','Ictère, urines foncées, selles décolorées ; douleur ou fièvre possibles.','Bilirubine et profil hépatique, échographie ; bilan infectieux si indiqué.','Obstacle localisé par imagerie ; cholangio-IRM ou écho-endoscopie selon suspicion et échographie.','Urgence si angiocholite suspectée ou instabilité ; triade douleur-fièvre-ictère parfois incomplète.',(11,12,13)),
('Hépatopathie chronique décompensée','Ictère, ascite, œdèmes ; rechercher saignement, infection et confusion.','Hémogramme, hémostase, fonction rénale, ionogramme, albumine et bilan hépatique ; ponction si ascite croissante ou complication.','Documenter terrain et complication séparément ; ascite : neutrophiles, protides/albumine et cultures.','Urgence devant défaillance, hémorragie ou infection ; culture d’ascite négative non excluante.',(14,15)),
('Insuffisance cardiaque','Œdèmes des chevilles, dyspnée, intolérance à l’effort ou variation rapide du poids.','Examen cardiorespiratoire, ECG et peptides natriurétiques interprétés dans le contexte.','Concordance clinique et anomalies objectives à l’échocardiographie ; peptide élevé insuffisant isolément.','🚩 Étouffement, douleur thoracique, malaise ou perte de connaissance : 144 selon les consignes HUG. Œdème non spécifique.',(3,16,17)),
('Thrombose veineuse profonde','Asymétrie récente d’un membre inférieur, gonflement et douleur possibles.','Probabilité de Wells : vraisemblable, échographie ; invraisemblable, D-dimères puis échographie si positifs.','Échographie veineuse ; si négative malgré forte probabilité, nouvel ultrason à 5–7 jours selon HUG 2023.','Dyspnée ou douleur thoracique : rechercher une embolie pulmonaire en urgence. Même sans ces signes, poursuivre le bilan de thrombose.',(18,)),
('Thrombopénie','Pétéchies, ecchymoses ou saignement muqueux.','Hémogramme et frottis ; rechercher autres cytopénies, cellules anormales, schizocytes, médicaments et hémolyse selon le contexte.','Numération contrôlée ; agrégats : rechercher une fausse thrombopénie, notamment par prélèvement citraté.','Urgence si saignement important, cellules anormales ou microangiopathie suspectée ; purpura non synonyme de thrombopénie.',(9,10)),
('Cancer bronchopulmonaire','Hippocratisme acquis possible avec symptômes respiratoires ou généraux.','Confirmer le signe et rechercher ses autres causes ; scanner thoracique si suspicion de tumeur.','Prélèvement tissulaire et anatomopathologie habituellement nécessaires ; bilan d’extension distinct.','Filière spécialisée ; hippocratisme et photographie ne prouvent pas la tumeur.',(19,20))]
comparison=table(['Diagnostic proposé','Indices à l’inspection et contexte','Bilan initial adulte','Confirmation ou décision','Priorité et limite'],[[f'DX.{i} — {a}'+ref(rs),b,c,d,e] for i,(a,b,c,d,e,rs) in enumerate(dx,1)])
comparison+=paras('<strong>Sélection pédagogique adulte, sans classement suisse de fréquence.</strong> Ces dix hypothèses relient signes de couleur, volume et mouvement à un bilan et à une décision. La liste pédagogique est non exhaustive, figée après contre-audit ciblé du 02.11.2026 ; grossesse et pédiatrie nécessitent un parcours adapté. Traumatisme, anaphylaxie ou infection cutanée profonde peuvent imposer une autre urgence. Le rappel HUG pédiatrique du point 4 reste distinct.')
refmap={1:(4,),2:(4,),3:(7,8,20),4:(1,2,3,6,7),5:(2,3,8,10),6:(2,3,7,20),7:tuple([2,3,5,6]+list(range(7,21))),8:(5,6,7,8,9,10,11,14,15,16,17,18,19,20),9:tuple([5,6]+list(range(7,21))),10:(2,3,6,18),11:(2,3,6,7),12:(3,),13:(2,3,7,18,20)}
main=[
'Chez l’adulte, une {anomalie visible} est un constat clinique à décrire avant d’en nommer la cause. L’examen précise sa distribution et son évolution, puis recherche son retentissement.',
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
'La {surveillance} contribue à prévenir l’aggravation d’une insuffisance cardiaque connue : suivre le traitement prescrit, le poids, le souffle et les œdèmes. Les consignes de recours dépendent des symptômes ; une amélioration visible ne suffit pas à clôturer le suivi.',
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
 if m:quiz.append((md(m[1]),md(m[2])))
assert len(quiz)==14
l.quiz(quiz,(1,2,3,7,8,9,10,11,18,19,20));l.write()

# Corrections locales de présentation ; le formatter partagé reste inchangé.
dest=D.parent/'LOT_133_Phase_A_V0.html'
rendered=dest.read_text().replace('couverture documentaire et iconographie incomplètes ; liste différentielle proposée, non gelée.', 'liste pédagogique figée après contre-audit ciblé du 02.11.2026 ; iconographie non intégrée ; lot incomplet.').replace('<h2>Anomalies à l’inspection</h2>','<h1>Anomalies à l’inspection</h1>',1)
chunks=re.split(r'(<[^>]+>)',rendered)
in_body=False
for index,chunk in enumerate(chunks):
 if chunk.startswith('<body'):in_body=True
 if in_body and not chunk.startswith('<') and 'Contenu établi à partir des sources citées' not in chunk:
  chunks[index]=re.sub(r' (?=[:;!?])', '\u00a0', chunk)
dest.write_text(''.join(chunks))

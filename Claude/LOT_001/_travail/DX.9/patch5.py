from patch import P
P('p01',[
("En revanche, les sueurs nocturnes isolées n'ont pas prédit une mortalité accrue dans deux cohortes de personnes âgées, après ajustement pour l'âge, le sexe, l'indice de masse corporelle, la formation et le revenu{ML:3}.","En revanche, les sueurs nocturnes isolées n'ont pas prédit une mortalité accrue dans deux cohortes de personnes âgées{ML:3}. L'ajustement portait sur l'âge, le sexe, l'indice de masse corporelle, la formation et le revenu{ML:3}."),
])
P('p03',[
("Le paracétamol intraveineux, donné toutes les 6 heures, n'a pas amélioré le nombre de jours sans soins intensifs à 28 jours{HE:7}.","Le paracétamol intraveineux, donné toutes les 6 heures, est resté sans effet sur le nombre de jours sans soins intensifs à 28 jours{HE:7}."),
("Cette classification explique pourquoi le bilan d'une fièvre prolongée ne cible pas seulement les agents infectieux{AN:2}.","Cette classification est utile, car le bilan d'une fièvre prolongée ne cible pas seulement les agents infectieux{AN:2}."),
])
P('p04',[
("Ce sont une fièvre continue, une durée inférieure à 180 jours, une vitesse de sédimentation, une protéine C réactive ou une lactate déshydrogénase élevées, une leucopénie, une thrombocytose et une imagerie thoracique ou TEP anormale{FU:3,FU:4}.","Ce sont une fièvre continue, une durée inférieure à 180 jours, une leucopénie, une thrombocytose et une imagerie thoracique ou TEP anormale{FU:3,FU:4}. La vitesse de sédimentation, la protéine C réactive ou la lactate déshydrogénase élevées jouent le même rôle{FU:3}."),
])
P('p08',[
("Le diagnostic positif d'une infection fébrile s'appuie sur des critères publiés.","Le diagnostic positif d'une infection fébrile repose sur des critères publiés."),
("Le choc septique ajoute un besoin de vasopresseurs pour une pression moyenne d'au moins 65 mmHg, avec un lactate supérieur à 2 mmol/L{S3:10}.","Le choc septique est un sepsis qui exige des vasopresseurs pour une pression moyenne d'au moins 65 mmHg, avec un lactate supérieur à 2 mmol/L{S3:10}."),
("Les critères sont une fréquence respiratoire d'au moins 30 par minute, une pression diastolique d'au plus 60 mmHg ou systolique inférieure à 90 mmHg, un trouble de la conscience et un âge d'au moins 65 ans{AW:86}.","Les critères sont une fréquence respiratoire d'au moins 30 par minute et un trouble de la conscience{AW:86}. S'y ajoutent une pression diastolique d'au plus 60 mmHg ou systolique inférieure à 90 mmHg, et un âge d'au moins 65 ans{AW:86}."),
])
P('p11',[
("Chez le nourrisson fébrile de 0 à 3 mois, la directive de l'Inselspital renvoie aux recommandations antibiotiques internes, car l'épidémiologie locale diffère{KI:3}.","Chez le nourrisson fébrile de 0 à 3 mois, la directive de l'Inselspital renvoie aux recommandations antibiotiques internes, car l'épidémiologie locale est particulière{KI:3}."),
])
P('p14',[
("L'examen fédéral teste surtout la reconnaissance","L'examen fédéral porte surtout sur la reconnaissance"),
("Première situation : un homme âgé consulte pour une fièvre brutale","Première situation : un homme âgé est vu pour une fièvre brutale"),
("L'absence de foyer clinique ne rassure donc pas.","L'absence de foyer clinique ne doit donc pas rassurer."),
])
# flatten arbre
p='/home/user/wt/lot-001/Claude/LOT_001/_travail/DX.9/s/p10.html'
t=open(p,encoding='utf-8').read()
t=t.replace('<li>Si le patient est fébrile et instable, il faut chercher un sepsis, car le qSOFA est un score simple{S3:10}. Il retient une fréquence respiratoire d\'au moins 22 par minute, un trouble de la conscience et une pression systolique d\'au plus 100 mmHg{S3:10}.','<li>Si le patient est fébrile et instable, il faut chercher un sepsis, car le qSOFA est un score simple{S3:10}. Ce score retient une fréquence respiratoire d\'au moins 22 par minute, un trouble de la conscience, et une pression systolique d\'au plus 100 mmHg{S3:10}.</li>')
import re
t=t.replace('</li>\n<ul>','\n<ul>')
# rebuild flat: remove nested ul/li wrappers
t=re.sub(r'<ul>\n<li>',r'<li class="n2" style="margin-left:1.6em">',t)
open(p,'w',encoding='utf-8').write(t)

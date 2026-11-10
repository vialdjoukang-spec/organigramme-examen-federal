#!/usr/bin/env python3
"""Phase A LOT_052 — phrases construites seulement depuis le paquet PA."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from moteur import Moteur

m = Moteur(os.path.join(os.path.dirname(__file__), 'paquet.json'))
S = m.S
W = m.W
H = m.HTML

# --- 1 Définition ---
S(1, "Sinz, Schmied et Ukegjini décrivent l'[[pa-p1-f1|abdomen aigu]] comme un état temporaire, car ce nom ne constitue pas un diagnostic.", "sinz_fms_2021-4")
S(1, "Cet état associe trois symptômes, car la douleur est soudaine, forte et persistante, avec une défense rigide et un trouble du péristaltisme.", "sinz_fms_2021-4")
S(1, "Le texte sépare donc l'abdomen aigu de la douleur abdominale aiguë d'origine indéterminée, lorsque le tableau reste incomplet.", "sinz_fms_2021-4")
S(1, "La littérature francophone emploie souvent les deux termes comme synonymes, cependant cette équivalence efface une différence utile.", "sinz_fms_2021-4")
S(1, "Les Hôpitaux universitaires de Genève décrivent la douleur aiguë comme des douleurs spontanées projetées sur l'abdomen depuis moins de 7 jours.", "hug_daa_2017-1")
S(1, "Cette borne de 7 jours vient du colloque genevois du 11 octobre 2017, car Dupuis et Ris citent Flament.", "hug_daa_2017-1")
S(1, "La stratégie genevoise de 2023 définit la douleur chronique comme continue ou intermittente depuis au moins 3 mois.", "hug_dac_2023-3")
S(1, "Le symptôme chronique n'est donc pas un abdomen aigu, car la durée dépasse le cadre de l'urgence immédiate.", "hug_dac_2023-3")
S(1, "Zahnd et ses collègues d'Unisanté rappellent que la douleur abdominale aiguë est un motif de consultation, car elle n'est pas une maladie unique.", "zahnd_rms_2024-12")
S(1, "Börner et ses collègues de Munich définissent l'abdomen aigu par une douleur maximale d'apparition soudaine, parfois avec une défense.", "boerner_2025-6")
S(1, "Le terme désigne ainsi un syndrome clinique et non une lésion d'organe, ce qui impose de chercher ensuite la cause.", "boerner_2025-6")
S(1, "On évite le mot péritonite pour toute défense, car la défense traduit une irritation péritonéale dont la cause reste à nommer.", "sinz_fms_2021-11")
S(1, "On évite aussi le diagnostic de douleur non spécifique tant qu'une cause grave n'est pas écartée, car cette étiquette est un reste.", "sinz_fms_2021-5")
S(1, "Le voisinage comprend la colique, la douleur pariétale et la douleur projetée thoracique, car ces mécanismes ne se recouvrent pas.", "sinz_fms_2021-8")

W(1, "pa-p1-f1", "Abdomen aigu selon Sinz, Forum Médical Suisse, 2021", [
    ("La définition opératoire retient trois éléments conjoints, car l'absence de l'un d'eux change le nom du tableau.", "sinz_fms_2021-4"),
    ("La douleur doit être d'apparition soudaine, forte et persistante, donc un simple inconfort ancien ne suffit pas.", "sinz_fms_2021-4"),
    ("La défense avec rigidité musculaire signe l'irritation de la paroi, ce qui rapproche le patient d'une cause chirurgicale.", "sinz_fms_2021-4"),
    ("Le trouble du péristaltisme complète la triade, cependant son absence auscultatoire ne confirme pas un intestin normal.", "sinz_fms_2021-11"),
    ("Le piège d'examen consiste à traiter le synonyme francophone comme une définition, car Sinz refuse cette fusion.", "sinz_fms_2021-4"),
])

# --- 2 Épidémiologie ---
S(2, "Zahnd écrit que la douleur abdominale aiguë représente le 9e motif de consultation en médecine générale.", "zahnd_rms_2024-12")
S(2, "Un tiers des étiologies restent non spécifiques, cependant environ 10 % nécessitent un traitement hospitalier.", "zahnd_rms_2024-12")
S(2, "Une anamnèse précise donne un diagnostic correct dans 76 % des cas, car la palpation cherche ensuite un abdomen chirurgical.", "zahnd_rms_2024-12")
S(2, "Sinz indique qu'une prévalence exacte de l'abdomen aigu n'est pas disponible, car les causes sont documentées par organe.", "sinz_fms_2021-5")
S(2, "Jusqu'à 44,3 % des cas restent sans [[pa-p2-f1|cause déterminée]], et l'on parle alors de douleur abdominale non spécifique.", "sinz_fms_2021-5")
S(2, "Environ 10 % des cas relèvent de causes extra-intestinales, donc le thorax et le métabolisme restent dans le champ.", "sinz_fms_2021-5")
S(2, "L'appendicite aiguë représente 6,7 à 28,1 % des causes gastro-intestinales citées, ce qui la place en tête de liste.", "sinz_fms_2021-5")
S(2, "La cholécystite suit avec 2,9 à 31,5 %, car les fourchettes de la littérature se chevauchent et ne se trient pas.", "sinz_fms_2021-5")
S(2, "La hernie incarcérée compte pour 10 à 18,2 %, donc une cause mécanique fréquente garde un rang élevé.", "sinz_fms_2021-5")
S(2, "L'iléus mécanique couvre 4,1 à 45 %, ce qui montre une dispersion large selon les séries réunies par Sinz.", "sinz_fms_2021-5")
S(2, "La perforation du tractus gastro-intestinal représente 2,3 à 18 %, cependant sa gravité ne suit pas sa fréquence.", "sinz_fms_2021-5")
S(2, "L'hémorragie gastro-intestinale est chiffrée à 5 %, et l'occlusion vasculaire mésentérique à 9,4 %.", "sinz_fms_2021-5")
S(2, "La diverticulite représente 8,2 à 9 %, la pancréatite aiguë 3,2 à 4 %, et les maladies inflammatoires de l'intestin 0,6 %.", "sinz_fms_2021-5")
S(2, "Börner indique une incidence de l'abdomen aigu autour de 5 à 7 pour 1000 personnes et par an.", "boerner_2025-19")
S(2, "5 à 12 % des patients des urgences présentent une douleur abdominale aiguë, et jusqu'à un tiers nécessitent un traitement urgent.", "boerner_2025-19")
S(2, "Hors la douleur non spécifique, Börner décrit l'appendicite pour 8 à 30 % et une incidence de 100 pour 100 000.", "boerner_2025-20")
S(2, "La cholécystite y représente 9 à 11 % avec une incidence de 60 pour 100 000, donc un dénominateur différent de Sinz.", "boerner_2025-20")
S(2, "Le colloque genevois rapporte 10 % des consultations aux urgences, car Bouillot et Bressler sont cités pour 2004.", "hug_daa_2017-1")
S(2, "La colonne 2004 du colloque genevois sert de repère, car elle compare plusieurs séries de douleur abdominale.", "hug_daa_2017-2")
S(2, "Dans cette série, la douleur non spécifiée atteint 34,8 %, donc elle reste un reliquat et non un diagnostic.", "hug_daa_2017-3")
S(2, "La même colonne indique 7,5 % d'appendicite, 11 % de colique néphrétique et 4,3 % de pancréatite.", "hug_daa_2017-3")
S(2, "Avant 30 ans, le colloque décrit l'appendicite, les affections gynécologiques et la douleur non spécifiée en tête.", "hug_daa_2017-2")
S(2, "Après 70 ans, les hernies étranglées, les anévrismes rompus, les cancers, les sigmoïdites, les cholécystites et les péritonites dominent.", "hug_daa_2017-2")
S(2, "La mortalité de la chirurgie abdominale urgente reste de 2 à 12 % selon Börner, car chaque heure sans traitement pèse.", "boerner_2025-6")
S(2, "La stratégie genevoise rappelle que la prévalence de la douleur chronique est difficile à établir, donc elle ne se confond pas avec l'aigu.", "hug_dac_2023-5")

H(2, '''<div class="t" style="overflow-x:auto"><table>
<caption>Chiffres recopiés, dénominateurs séparés.</caption>
<thead><tr><th>Indicateur</th><th>Valeur</th><th>Population</th><th>Source</th></tr></thead>
<tbody>
<tr><td>Motif en médecine générale</td><td>9e motif</td><td>pratique de premier recours</td><td>Zahnd, Revue Médicale Suisse, 2024</td></tr>
<tr><td>Part hospitalière</td><td>environ 10 %</td><td>douleur abdominale aiguë en médecine générale</td><td>Zahnd, 2024</td></tr>
<tr><td>Anamnèse correcte</td><td>76 %</td><td>même article</td><td>Zahnd, 2024</td></tr>
<tr><td>Cause non déterminée</td><td>jusqu'à 44,3 %</td><td>abdomen aigu</td><td>Sinz, Forum Médical Suisse, 2021</td></tr>
<tr><td>Causes extra-intestinales</td><td>environ 10 %</td><td>abdomen aigu</td><td>Sinz, 2021</td></tr>
<tr><td>Appendicite aiguë</td><td>6,7 à 28,1 %</td><td>causes gastro-intestinales citées</td><td>Sinz, 2021</td></tr>
<tr><td>Incidence de l'abdomen aigu</td><td>5 à 7 pour 1000 par an</td><td>population</td><td>Börner, 2025</td></tr>
<tr><td>Douleur aux urgences</td><td>5 à 12 %</td><td>passages aux urgences</td><td>Börner, 2025</td></tr>
</tbody></table></div>''')

W(2, "pa-p2-f1", "Pourquoi l'ordre suit la phrase de Sinz", [
    ("Les fourchettes se chevauchent, donc un tri par médiane inventerait un rang que l'article ne donne pas.", "sinz_fms_2021-5"),
    ("L'ordre retenu est celui de l'énumération, car Sinz écrit les causes les plus fréquentes dans cette suite.", "sinz_fms_2021-5"),
    ("La douleur non spécifique atteint 44,3 %, cependant elle ne constitue pas un diagnostic concurrent distinct.", "sinz_fms_2021-5"),
    ("Börner publie d'autres pourcentages aux urgences, ce qui interdit de fusionner les deux dénominateurs.", "boerner_2025-20"),
    ("Le piège consiste à citer 11 % de colique néphrétique comme rang suisse, car ce chiffre est une série de 2004.", "hug_daa_2017-3"),
])

# --- 3 Physiopathologie ---
S(3, "Sinz distingue [[pa-p3-f1|trois douleurs]], car le mécanisme viscéral, pariétal ou projeté oriente déjà l'organe.", "sinz_fms_2021-8")
S(3, "La douleur viscérale naît d'une distension, d'une tension, d'une torsion ou d'une contraction, donc elle reste médiocrement localisée.", "sinz_fms_2021-8")
S(3, "Proximalement au ligament de Treitz, cette douleur est perçue dans l'épigastre, car l'intestin antérieur s'y projette.", "sinz_fms_2021-8")
S(3, "Entre Treitz et l'angle colique droit, le territoire de l'artère mésentérique supérieure projette la douleur en péri-ombilical.", "sinz_fms_2021-8")
S(3, "Au-delà de l'angle droit, l'intestin terminal projette la douleur dans l'hypogastre, ce qui sépare le côlon gauche.", "sinz_fms_2021-8")
S(3, "La douleur somatique naît du péritoine, donc le patient la décrit comme aiguë ou lancinante et la localise mieux.", "sinz_fms_2021-8")
S(3, "La douleur projetée résulte d'une convergence d'afférences, ce qui explique une scapulalgie d'origine biliaire.", "sinz_fms_2021-8")
S(3, "Börner décrit la douleur viscérale comme sourde, profonde et souvent crampoïde, car la capsule ou le viscère creux se distend.", "boerner_2025-9")
S(3, "La douleur somatique est vive et brûlante, donc une perforation ou une cholécystite la produit plus qu'une simple colique.", "boerner_2025-9")
S(3, "L'irritation péritonéale provoque la défense, car toute vibration, la toux ou la palpation réveille la contraction.", "sinz_fms_2021-11")
S(3, "Si des signes inflammatoires s'y ajoutent, alors Sinz conclut à une péritonite, ce qui change l'urgence du contrôle du foyer.", "sinz_fms_2021-11")
S(3, "Le passage à la douleur pariétale marque l'irritation du péritoine, donc l'examen cherche la défense plutôt qu'un nouveau récit.", "boerner_2025-9")
S(3, "L'ischémie mésentérique masque souvent ses symptômes, car Sinz le signale chez l'enfant, le sujet âgé et l'immunodéprimé.", "sinz_fms_2021-9")
S(3, "Une corticothérapie participe à ce masque, ce qui impose de ne pas attendre une défense franche pour agir.", "sinz_fms_2021-9")

H(3, '''<div class="t" style="overflow-x:auto"><table>
<caption>Perturbation, exploration et traitement, d'après Sinz.</caption>
<thead><tr><th>Perturbation</th><th>Ce que l'examen montre</th><th>Ce que le traitement corrige</th></tr></thead>
<tbody>
<tr><td>Distension d'un viscère creux</td><td>Douleur viscérale mal localisée, selon l'étage embryonnaire</td><td>Lever l'obstacle ou la distension, après avoir nommé l'organe</td></tr>
<tr><td>Irritation du péritoine</td><td>Douleur somatique localisée, défense, douleur à la toux</td><td>Contrôle du foyer lorsque la péritonite est retenue</td></tr>
<tr><td>Convergence d'afférences</td><td>Douleur projetée à distance de l'organe</td><td>Traiter l'organe source, non la zone où la douleur est ressentie</td></tr>
<tr><td>Ischémie mésentérique</td><td>Symptômes souvent masqués, surtout chez le sujet âgé</td><td>Réduire le délai entre le début, le diagnostic et le traitement</td></tr>
</tbody></table></div>''')

W(3, "pa-p3-f1", "Carte embryonnaire de la douleur viscérale", [
    ("L'étage proximal au ligament de Treitz correspond à l'intestin antérieur, donc la douleur siège dans l'épigastre.", "sinz_fms_2021-8"),
    ("Le territoire de l'artère mésentérique supérieure correspond à l'intestin moyen, ce qui centre la douleur.", "sinz_fms_2021-8"),
    ("L'intestin terminal, après l'angle colique droit, projette la douleur vers l'hypogastre, ce qui sépare le côlon gauche.", "sinz_fms_2021-8"),
    ("Un exemple est la douleur biliaire épigastrique initiale, car le foie et les voies biliaires relèvent de cet étage.", "sinz_fms_2021-8"),
    ("Le piège est de conclure à une gastrite dès que la douleur est épigastrique, car l'étage ne nomme pas la maladie.", "sinz_fms_2021-8"),
])

# --- 4 Démarche ---
S(4, "La règle de Sinz limite l'intervalle entre le début des symptômes, le diagnostic et le traitement, car le temps aggrave le pronostic.", "sinz_fms_2021-7")
S(4, "L'occlusion des vaisseaux mésentériques reçoit le [[pa-p4-f1|rang E1]], car ses symptômes sont souvent masqués et le retard est meurtrier.", "sinz_fms_2021-9")
S(4, "La perforation reçoit le rang E2, car le choc septique impose un contrôle du foyer et une antibiothérapie sans délai.", "sinz_fms_2021-16")
S(4, "La hernie incarcérée reçoit le rang E3, car l'incarcération menace l'intestin et figure parmi les causes fréquentes citées.", "sinz_fms_2021-5")
S(4, "L'hémorragie gastro-intestinale reçoit le rang E4, car elle peut réaliser l'hypotension que Sinz traite comme une alarme.", "sinz_fms_2021-11")
S(4, "Ces quatre causes gardent pourtant leur rang de fréquence, donc E1 n'est pas le diagnostic le plus fréquent.", "sinz_fms_2021-5")
S(4, "L'appendicite aiguë constitue la tête de liste, car Sinz la décrit la première parmi les causes gastro-intestinales.", "sinz_fms_2021-5")
S(4, "Le diagnostic clinique seul atteint une sensibilité de 88 % et une spécificité de 41 %, ce qui ne dispense pas de l'imagerie ciblée.", "sinz_fms_2021-7")
S(4, "Une étude de 1000 patients retient comme facteurs chirurgicaux une douleur de moins de 48 heures et une défense.", "sinz_fms_2021-9")
S(4, "Les vomissements après la douleur, l'âge d'au moins 65 ans et une chirurgie antérieure complètent ces facteurs.", "sinz_fms_2021-9")
S(4, "Börner confirme une sensibilité de 88 % et une spécificité de 41 % pour l'histoire et l'examen bien conduits.", "boerner_2025-16")
S(4, "La tomodensitométrie confirme le diagnostic clinique dans plus de 70 % des cas d'appendicite, selon le même article.", "boerner_2025-16")

H(4, '''<div class="t" style="overflow-x:auto"><table>
<caption>Dix concurrents et cinq colonnes, dans l'ordre écrit par Sinz.</caption>
<thead><tr><th>Signe clé</th><th>Examen qui tranche</th><th>Mécanisme</th><th>Conduite immédiate</th><th>Rang E</th></tr></thead>
<tbody>
<tr><td>DX.1 Appendicite aiguë : douleur qui se déplace, avec défense de la fosse iliaque droite</td><td>Échographie, puis tomodensitométrie si le doute persiste</td><td>Inflammation appendiculaire, puis irritation péritonéale</td><td>Stratifier le risque et ne pas retarder le contrôle si la forme est compliquée</td><td>Fréquent, sans rang E</td></tr>
<tr><td>DX.2 Cholécystite : douleur de l'hypocondre droit et signe de Murphy</td><td>Échographie des voies biliaires</td><td>Inflammation vésiculaire</td><td>Imagerie biliaire, car l'échographie y est plus sensible que la tomodensitométrie</td><td>Sans rang E</td></tr>
<tr><td>DX.3 Hernie incarcérée : voussure douloureuse et irréductible à un orifice</td><td>Inspection et palpation des orifices</td><td>Incarcération, avec risque d'ischémie intestinale</td><td>Lever l'incarcération en urgence si le tableau est étranglé</td><td>E3</td></tr>
<tr><td>DX.4 Iléus mécanique : arrêt des gaz, vomissements et météorisme</td><td>Tomodensitométrie si l'examen ne tranche pas</td><td>Obstacle mécanique</td><td>Chercher une strangulation, qui rejoint alors la voie de la perforation</td><td>Sans rang E propre</td></tr>
<tr><td>DX.5 Perforation : défense diffuse et douleur à la toux</td><td>Air libre, surtout sur le cliché qui le montre</td><td>Irruption du contenu digestif dans le péritoine</td><td>Contrôle du foyer, et antibiotique dans l'heure si le sepsis est identifié</td><td>E2</td></tr>
<tr><td>DX.6 Hémorragie gastro-intestinale : instabilité et extériorisation de sang</td><td>Constantes, puis endoscopie selon la porte d'entrée</td><td>Perte sanguine</td><td>Remplissage et hémostase si la pression systolique est basse</td><td>E4</td></tr>
<tr><td>DX.7 Occlusion des vaisseaux mésentériques : douleur intense et symptômes souvent pauvres</td><td>Tomodensitométrie avec injection, et lactate dans le bilan</td><td>Ischémie intestinale</td><td>Réduire le délai diagnostique, car le tableau est masqué</td><td>E1</td></tr>
<tr><td>DX.8 Diverticulite : douleur de la fosse iliaque gauche et fièvre</td><td>Tomodensitométrie, plus sensible que l'échographie pour cette question</td><td>Inflammation diverticulaire</td><td>Distinguer la forme locale de la perforation libre</td><td>Sans rang E</td></tr>
<tr><td>DX.9 Pancréatite aiguë : douleur épigastrique transfixiante</td><td>Lipase, puis imagerie si le doute ou la gravité l'exigent</td><td>Activation enzymatique pancréatique</td><td>Bilan de Sinz, qui inclut la lipase et l'amylase</td><td>Sans rang E</td></tr>
<tr><td>DX.10 Maladies inflammatoires de l'intestin : douleur et trouble du transit</td><td>Le diagnostic de poussée ne se pose pas sur la seule douleur aiguë</td><td>Inflammation chronique de la paroi</td><td>Ne pas les confondre avec une perforation, qui reste E2</td><td>Sans rang E</td></tr>
</tbody></table></div>''')

W(4, "pa-p4-f1", "Pourquoi E1 n'est pas le diagnostic le plus fréquent", [
    ("L'occlusion mésentérique est citée à 9,4 %, donc elle n'ouvre pas la liste de fréquence.", "sinz_fms_2021-5"),
    ("Elle passe pourtant en tête de l'algorithme, car les symptômes sont souvent masqués.", "sinz_fms_2021-9"),
    ("Une autopsie de 2121 cas a retrouvé un abdomen aigu non détecté dans 5 % des décès après 70 ans.", "sinz_fms_2021-11"),
    ("Le piège est de rassurer un sujet âgé peu douloureux, car la pauvreté des signes ne diminue pas le risque.", "sinz_fms_2021-11"),
    ("La conduite positive est de réduire l'intervalle jusqu'au traitement, comme Sinz le formule en règle d'or.", "sinz_fms_2021-7"),
])

# --- 5 Anamnèse ---
S(5, "Sinz fait poser [[pa-p5-f1|cinq questions]], car le moment, le mode, la durée, le pourquoi et le lieu structurent le récit.", "sinz_fms_2021-8")
S(5, "Le moment cherche l'événement déclenchant et le caractère nocturne, donc une perforation se sépare d'une douleur ancienne.", "sinz_fms_2021-8")
S(5, "Le mode décrit le caractère et l'irradiation, ce qui distingue une colique d'une douleur pariétale fixe.", "sinz_fms_2021-8")
S(5, "La durée précise le début et l'évolution, car une douleur de moins de 48 heures pèse vers une cause chirurgicale.", "sinz_fms_2021-9")
S(5, "Le pourquoi relie la douleur aux maladies antérieures et aux médicaments, donc les anti-inflammatoires orientent vers l'ulcère.", "sinz_fms_2021-8")
S(5, "Le lieu sur l'abdomen utilise la carte embryonnaire, ce qui évite de nommer un organe sur la seule topographie.", "sinz_fms_2021-8")
S(5, "Börner demande le début, la durée, le site, l'intensité et la nature, car la douleur viscérale est sourde et la somatique vive.", "boerner_2025-9")
S(5, "Il faut demander si la douleur s'est déplacée, car ce trajet est typique de l'appendicite dans cet article.", "boerner_2025-9")
S(5, "L'anorexie, les nausées, les vomissements, la fièvre, la diarrhée ou la constipation accompagnent le récit et changent la probabilité.", "boerner_2025-9")
S(5, "Les médicaments et les antécédents font partie de l'histoire, donc une chirurgie ancienne oriente vers l'occlusion.", "sinz_fms_2021-9")
S(5, "Une douleur thoracique, une dyspnée ou un saignement vaginal évoquent une cause extra-abdominale, ce qui ouvre le tableau de Sinz.", "sinz_fms_2021-10")
S(5, "Zahnd accorde 76 % de diagnostics corrects à une anamnèse précise, cependant ce chiffre ne remplace pas l'examen.", "zahnd_rms_2024-12")
S(5, "La stratégie chronique des Hôpitaux universitaires de Genève impose aussi une anamnèse détaillée, car une néoplasie peut manquer de symptômes B.", "hug_dac_2023-3")
S(5, "Un changement récent du transit fait chercher cette néoplasie même avant 50 ans, donc l'âge seul ne rassure pas.", "hug_dac_2023-3")

H(5, '''<div class="t" style="overflow-x:auto"><table>
<caption>Drapeaux et action, d'après les seuils lus.</caption>
<thead><tr><th>Drapeau</th><th>Signification</th><th>Action immédiate</th></tr></thead>
<tbody>
<tr><td>Fréquence cardiaque supérieure à 95 par minute</td><td>Sinz associe cette tachycardie à une morbidité accrue dans l'abdomen aigu</td><td>Traiter le patient comme instable jusqu'à preuve du contraire</td></tr>
<tr><td>Pression artérielle systolique de 90 mm Hg ou moins</td><td>Hypotension associée à une morbidité et à une mortalité accrues</td><td>Remplissage et recherche d'une hémorragie ou d'un sepsis</td></tr>
<tr><td>Température corporelle inférieure à 36,5 °C</td><td>Hypothermie dans le même cadre d'alarme</td><td>Ne pas attendre un frisson fébrile pour engager la réanimation</td></tr>
<tr><td>Douleur depuis moins de 48 heures, suivie de vomissements, avec défense</td><td>Facteurs de cause chirurgicale dans une série de 1000 patients</td><td>Poursuivre vers l'imagerie et l'avis chirurgical</td></tr>
<tr><td>Âge d'au moins 65 ans</td><td>Le même travail identifie l'âge avancé comme facteur chirurgical</td><td>Abaisser le seuil de la tomodensitométrie</td></tr>
<tr><td>Sujet âgé, enfant, immunodépression ou corticoïde</td><td>Les symptômes d'ischémie et d'infection sont souvent masqués</td><td>Ne pas exiger une défense franche pour engager le bilan</td></tr>
</tbody></table></div>''')

W(5, "pa-p5-f1", "Les cinq questions de Sinz", [
    ("Quand cherche l'heure et l'événement, car une perforation se distingue d'une douleur qui traîne.", "sinz_fms_2021-8"),
    ("Comment décrit le caractère et l'irradiation, donc la colique ne se raconte pas comme une brûlure fixe.", "sinz_fms_2021-8"),
    ("Combien de temps fixe le début et la pente, ce qui rejoint le seuil de 48 heures.", "sinz_fms_2021-9"),
    ("Pourquoi explique le lien avec les médicaments, car un anti-inflammatoire change la probabilité d'ulcère.", "sinz_fms_2021-8"),
    ("Où utilise la carte de l'abdomen, cependant le lieu ressenti n'est pas toujours le lieu de la lésion.", "sinz_fms_2021-8"),
])

# --- 6 Examen ---
S(6, "Le normal précède le pathologique, car Sinz mesure d'abord le pouls, la pression, la respiration, la température et la vigilance.", "sinz_fms_2021-11")
S(6, "Une fréquence cardiaque supérieure à 95 par minute constitue une alarme, donc l'examen local vient après les constantes.", "sinz_fms_2021-11")
S(6, "Une pression systolique de 90 mm Hg ou moins, ou une température sous 36,5 °C, augmente la morbidité dans ce cadre.", "sinz_fms_2021-11")
S(6, "L'inspection cherche la [[pa-p6-f1|posture en chien de fusil]], car le patient péritonéal replie les jambes.", "sinz_fms_2021-11")
S(6, "Les cicatrices, les hernies, les stomies et l'ictère se voient avant la palpation, ce qui évite de manquer un orifice.", "sinz_fms_2021-11")
S(6, "L'auscultation reste obligatoire, cependant l'absence de bruits n'exclut pas une fonction intestinale normale.", "sinz_fms_2021-11")
S(6, "Les études ne confirment aucune concordance entre examinateurs pour des bruits dits normaux, réduits ou augmentés.", "sinz_fms_2021-11")
S(6, "L'auscultation aide néanmoins au diagnostic d'iléus, donc on la garde sans lui donner un seuil chiffré inexistant.", "sinz_fms_2021-11")
S(6, "La palpation recherche la défense, la douleur à la décompression et le péritonisme, car elle juge l'urgence.", "sinz_fms_2021-11")
S(6, "La palpation profonde recherche une hypertrophie du foie, de la rate, de la vésicule ou de la vessie.", "sinz_fms_2021-11")
S(6, "La toux, le choc du lit ou une percussion légère reproduisent la douleur péritonéale, ce qui confirme l'irritation.", "sinz_fms_2021-11")
S(6, "Chez le sujet âgé peu musclé, ces signes manquent souvent, donc un abdomen souple n'élimine pas la cause.", "sinz_fms_2021-11")
S(6, "Börner décrit l'inspection, puis l'auscultation des quatre quadrants, puis la percussion et la palpation.", "boerner_2025-10")
S(6, "Le point de McBurney, décrit en 1889, est spécifique de 50 à 80 % et sensible jusqu'à 45 %.", "boerner_2025-16")
S(6, "Le signe de Murphy, décrit en 1903, est spécifique de 62 à 97 % et sensible de 47 à 96 %.", "boerner_2025-16")
S(6, "Börner rappelle que l'analgésie précoce ne gêne pas l'évaluation clinique, donc la douleur se traite avant la fin du bilan.", "boerner_2025-10")
S(6, "Les orifices herniaires se palpent, car le colloque genevois et Sinz font de la hernie un diagnostic visible.", "sinz_fms_2021-11")

W(6, "pa-p6-f1", "Technique de la défense", [
    ("Le patient est allongé, car la posture en chien de fusil se juge avant toute pression.", "sinz_fms_2021-11"),
    ("On demande une toux, donc la douleur provoquée traduit l'irritation sans appuyer fort.", "sinz_fms_2021-11"),
    ("Une percussion légère suffit souvent, ce qui évite une palpation brutale sur un abdomen déjà contracté.", "sinz_fms_2021-11"),
    ("La valeur diminue chez le sujet âgé, car une série autopsique a manqué 5 % d'abdomens aigus après 70 ans.", "sinz_fms_2021-11"),
    ("Le piège est de conclure à l'absence de péritonite parce que les bruits existent, car l'auscultation n'a pas de seuil consensuel.", "sinz_fms_2021-11"),
])

# --- 7 Syndromes ---
H(7, '<h4><em>7.1 Abdomen aigu</em></h4>')
S(7, "Le [[pa-p7-f1|premier syndrome]] est l'abdomen aigu de Sinz, car la triade réunit douleur, défense et trouble du péristaltisme.", "sinz_fms_2021-4")
S(7, "Ses signes fonctionnels sont la douleur soudaine et les vomissements, et ses signes physiques sont la rigidité et la posture antalgique.", "sinz_fms_2021-11")
S(7, "Le geste est la recherche de la douleur à la toux, car ce signe relie l'irritation péritonéale au mécanisme pariétal.", "sinz_fms_2021-11")
H(7, '<h4><em>7.2 Douleur viscérale</em></h4>')
S(7, "Le deuxième syndrome est la douleur viscérale pure, donc elle est mal localisée et suit l'étage embryonnaire.", "sinz_fms_2021-8")
H(7, '<h4><em>7.3 Douleur somatique</em></h4>')
S(7, "Le troisième syndrome est la douleur somatique localisée, car le patient désigne un point et la défense s'y limite.", "sinz_fms_2021-8")
H(7, '<h4><em>7.4 Douleur projetée</em></h4>')
S(7, "Le quatrième syndrome est la douleur projetée, ce qui explique une plainte thoracique ou scapulaire d'origine abdominale.", "sinz_fms_2021-8")
H(7, '<h4><em>7.5 Instabilité</em></h4>')
S(7, "Le cinquième syndrome est l'instabilité, car la tachycardie, l'hypotension ou l'hypothermie précèdent le diagnostic.", "sinz_fms_2021-11")
H(7, '<h4><em>7.6 Tableau masqué</em></h4>')
S(7, "Le sixième syndrome est le masque du sujet fragile, donc l'enfant, le sujet âgé et le patient sous corticoïde restent suspects.", "sinz_fms_2021-9")
H(7, '<h4><em>7.7 Douleur chronique</em></h4>')
S(7, "Le septième syndrome est la douleur chronique depuis au moins 3 mois, car la stratégie genevoise la sépare de l'urgence.", "hug_dac_2023-3")
S(7, "Dans ce cadre chronique, le syndrome de l'intestin irritable repose sur les critères de Rome IV mis à jour en 2016.", "hug_dac_2023-36")
S(7, "Börner décrit le sepsis abdominal jusqu'à 26 % de mortalité, et jusqu'à 43 % si le traitement est retardé.", "boerner_2025-17")
S(7, "Le qSOFA retient un Glasgow inférieur à 15, une fréquence respiratoire d'au moins 22 par minute et une systolique de 100 mm Hg ou moins.", "boerner_2025-17")

H(7, '''<div class="t" style="overflow-x:auto"><table>
<caption>Syndromes numérotés.</caption>
<thead><tr><th>Syndrome</th><th>Signes fonctionnels</th><th>Signes physiques</th></tr></thead>
<tbody>
<tr><td>7.1 Abdomen aigu</td><td>Douleur soudaine, forte, persistante</td><td>Défense rigide et trouble du péristaltisme</td></tr>
<tr><td>7.2 Douleur viscérale</td><td>Crampe, nausée, mauvaise localisation</td><td>Abdomen encore souple au début</td></tr>
<tr><td>7.3 Douleur somatique</td><td>Douleur fixe, aiguë ou lancinante</td><td>Défense, douleur à la toux</td></tr>
<tr><td>7.4 Douleur projetée</td><td>Plainte à distance de l'organe</td><td>Zone douloureuse sans lésion locale obligatoire</td></tr>
<tr><td>7.5 Instabilité</td><td>Malaise, soif, confusion</td><td>Tachycardie, hypotension ou hypothermie</td></tr>
<tr><td>7.6 Tableau masqué</td><td>Plainte pauvre chez le sujet fragile</td><td>Défense absente malgré une cause grave</td></tr>
<tr><td>7.7 Douleur chronique</td><td>Douleur continue ou intermittente depuis au moins 3 mois</td><td>Examen souvent pauvre, drapeaux à chercher quand même</td></tr>
</tbody></table></div>''')

W(7, "pa-p7-f1", "qSOFA selon Börner", [
    ("Le score simplifié cherche un trouble de vigilance, car le Glasgow est alors inférieur à 15.", "boerner_2025-17"),
    ("Une fréquence respiratoire d'au moins 22 par minute constitue le deuxième item.", "boerner_2025-17"),
    ("Une pression systolique de 100 mm Hg ou moins constitue le troisième item.", "boerner_2025-17"),
    ("Jusqu'à 66 % des patients chirurgicaux septiques ont leur foyer dans l'abdomen, donc la question se pose d'emblée.", "boerner_2025-17"),
    ("Le piège est d'attendre la fièvre, car l'hypothermie de Sinz est déjà une alarme à 36,5 °C.", "sinz_fms_2021-11"),
])

# --- 8 Critères ---
S(8, "Sinz fixe la triade de l'abdomen aigu, donc la douleur isolée ne suffit pas à porter ce nom.", "sinz_fms_2021-4")
S(8, "La douleur d'origine indéterminée reste un autre cadre, car elle ne réunit pas la défense et le trouble du péristaltisme.", "sinz_fms_2021-4")
S(8, "La sensibilité clinique de 88 % et la spécificité de 41 % disent ce que l'examen peut et ne peut pas affirmer.", "sinz_fms_2021-7")
S(8, "Une spécificité de 41 % signifie que l'examen seul ne confirme pas la cause, donc l'imagerie reste nécessaire si le doute persiste.", "sinz_fms_2021-7")
S(8, "Les facteurs chirurgicaux de la série de 1000 patients ne sont pas un score nommé, cependant ils structurent la probabilité.", "sinz_fms_2021-9")
S(8, "Börner date le point de McBurney de 1889 et le signe de Murphy de 1903, car ces manœuvres gardent une valeur chiffrée.", "boerner_2025-16")
S(8, "McBurney ne confirme pas l'appendicite à lui seul, car sa sensibilité ne dépasse pas 45 % dans cette synthèse.", "boerner_2025-16")
S(8, "Murphy ne confirme pas non plus toute cholécystite, car sa sensibilité peut descendre à 47 %.", "boerner_2025-16")
S(8, "La stratégie genevoise date les critères de Rome IV de 2016 pour le syndrome de l'intestin irritable.", "hug_dac_2023-36")
S(8, "Ces critères ne s'appliquent pas à l'abdomen aigu, donc on ne les utilise pas pour éviter une imagerie urgente.", "hug_dac_2023-3")
S(8, "Börner indique que la tomodensitométrie confirme le diagnostic clinique d'appendicite dans plus de 70 % des cas.", "boerner_2025-16")
S(8, "Ce pourcentage ne constitue pas un critère diagnostique autonome, car il mesure l'accord avec la clinique.", "boerner_2025-16")

H(8, '''<div class="t" style="overflow-x:auto"><table>
<caption>Ce qui suffit et ce qui ne suffit pas.</caption>
<thead><tr><th>Critère</th><th>Année et source</th><th>Ce qu'il permet</th><th>Ce qu'il ne permet pas</th></tr></thead>
<tbody>
<tr><td>Triade douleur, défense, trouble du péristaltisme</td><td>Sinz, Forum Médical Suisse, 2021</td><td>Nommer un abdomen aigu</td><td>Nommer l'organe</td></tr>
<tr><td>Sensibilité 88 % et spécificité 41 % de la clinique</td><td>Sinz, 2021, et Börner, 2025</td><td>Savoir que l'examen oriente</td><td>Affirmer la cause sans autre examen</td></tr>
<tr><td>McBurney, spécificité 50 à 80 %, sensibilité jusqu'à 45 %</td><td>Börner, rappel de 1889</td><td>Renforcer une suspicion d'appendicite</td><td>Écarter l'appendicite s'il est absent</td></tr>
<tr><td>Murphy, spécificité 62 à 97 %, sensibilité 47 à 96 %</td><td>Börner, rappel de 1903</td><td>Renforcer une suspicion biliaire</td><td>Remplacer l'échographie</td></tr>
<tr><td>Rome IV</td><td>Stratégie des HUG, mise à jour 2016</td><td>Structurer une douleur chronique fonctionnelle</td><td>Classer un abdomen aigu</td></tr>
</tbody></table></div>''')

# --- 9 Examens ---
H(9, '<h4><em>9.a Gold standard</em></h4>')
S(9, "Sinz ne désigne pas un seul examen comme étalon pour tout abdomen aigu, car la cause décide de la modalité.", "sinz_fms_2021-14")
S(9, "La clinique reste le point de départ, cependant sa spécificité de 41 % interdit de s'y arrêter si le risque est réel.", "sinz_fms_2021-7")
S(9, "Lorsque l'[[pa-p9-f1|air libre]] est démontré et que le tableau colle, l'indication opératoire peut être posée sans autre examen.", "sinz_fms_2021-14")
H(9, '<h4><em>9.b Première intention</em></h4>')
S(9, "Le bilan de Sinz comprend l'hémogramme, la protéine C réactive, le bilan hépatique, la lipase ou l'amylase, les électrolytes et le glucose.", "sinz_fms_2021-12")
S(9, "Le lactate, la coagulation et l'analyse d'urine avec sédiment complètent ce premier bilan, car la cause est encore ouverte.", "sinz_fms_2021-12")
S(9, "Chez la femme en âge de procréer, un test de grossesse est exigé, donc une grossesse extra-utérine n'est pas oubliée.", "sinz_fms_2021-12")
S(9, "L'échographie vient ensuite, car elle est non irradiante, répétable, et utile pour le liquide, la perfusion et la vésicule.", "sinz_fms_2021-14")
S(9, "Sa sensibilité se situe entre 67 et 74 % et sa spécificité entre 81 et 88 %, donc l'examinateur limite la performance.", "sinz_fms_2021-14")
S(9, "L'obésité, le manque de coopération et l'air gênent l'échographie, ce qui conduit alors à la tomodensitométrie.", "sinz_fms_2021-14")
H(9, '<h4><em>9.c Alternatives</em></h4>')
S(9, "Chez la femme enceinte, si l'échographie ne tranche pas, Sinz recommande l'imagerie par résonance magnétique.", "sinz_fms_2021-14")
S(9, "Une [[pa-p9-f2|exposition fœtale]] de 10 mGy augmenterait de 40 % l'incidence des cancers de l'enfance, donc le choix de modalité compte.", "sinz_fms_2021-14")
S(9, "Le produit de contraste iodé se discute si le débit de filtration estimé dépasse 45 ml par minute et par 1,73 mètre carré.", "sinz_fms_2021-14")
S(9, "En dessous de ce seuil, le risque de néphropathie n'est plus qualifié de minime par la synthèse de Sinz.", "sinz_fms_2021-14")
S(9, "Chez le patient instable, le diagnostic rapide prime sur ce risque, donc l'injection n'est pas refusée pour ce seul motif.", "sinz_fms_2021-14")
H(9, '<h4><em>9.d Deuxième intention</em></h4>')
S(9, "La tomodensitométrie avec injection intraveineuse atteint une sensibilité jusqu'à 94 % et une spécificité jusqu'à 77 %.", "sinz_fms_2021-14")
S(9, "Le contraste oral ou rectal n'augmente pas utilement la précision en urgence et allonge le délai, donc Sinz ne le retient pas.", "sinz_fms_2021-14")
S(9, "La tomodensitométrie dépasse l'échographie pour l'appendicite, la diverticulite, la pancréatite, la perforation, l'iléus et l'ischémie.", "sinz_fms_2021-14")
S(9, "L'échographie reste plus sensible pour les voies biliaires, ce qui réserve la tomodensitométrie aux questions qu'elle tranche mieux.", "sinz_fms_2021-14")
S(9, "La radiographie conventionnelle ne change le diagnostic que dans 4 à 7,2 % des douleurs aiguës, donc elle n'est plus l'examen de base.", "sinz_fms_2021-14")
S(9, "Dans une étude de 1021 personnes, le diagnostic clinique reste identique après la radiographie d'abdomen.", "sinz_fms_2021-14")
S(9, "La dose d'une tomodensitométrie abdominale atteint jusqu'à 10 mSv, et le risque de cancer radio-induit est jugé très faible chez l'adulte.", "sinz_fms_2021-14")
S(9, "Après 65 ans, une série de 380 patients a compté 5 % de décès et 22 % de traitements chirurgicaux, donc le seuil d'imagerie baisse.", "sinz_fms_2021-14")
S(9, "L'endoscopie et l'angiographie ne sont pas des examens de routine de l'abdomen aigu selon Sinz, car elles répondent à une question précise.", "sinz_fms_2021-14")

H(9, '''<div class="t" style="overflow-x:auto"><table>
<caption>Interprétation des résultats cités.</caption>
<thead><tr><th>Résultat</th><th>Signification</th><th>Conduite</th></tr></thead>
<tbody>
<tr><td>Air libre démontré</td><td>Perforation d'organe creux possible</td><td>L'indication opératoire peut être posée sans examen supplémentaire si le tableau clinique concorde</td></tr>
<tr><td>Échographie non contributive</td><td>Sensibilité limitée, entre 67 et 74 %</td><td>Passer à la tomodensitométrie, surtout si l'obésité ou l'air gênent</td></tr>
<tr><td>Tomodensitométrie positive pour une cause chirurgicale</td><td>Sensibilité jusqu'à 94 %</td><td>Engager le traitement de la cause, sans refaire une radiographie simple</td></tr>
<tr><td>Débit de filtration estimé supérieur à 45</td><td>Risque de néphropathie de contraste qualifié de minime</td><td>L'injection intraveineuse reste acceptable dans ce cadre</td></tr>
<tr><td>Lactate et instabilité</td><td>Le bilan de Sinz inclut le lactate</td><td>Ne pas attendre le résultat pour commencer la réanimation</td></tr>
</tbody></table></div>''')

H(9, '''<figure>
<img src="images/0fa3bad94e3ca02b.png" alt="Fichier brut : radiographie thoracique en décubitus et coupe de tomodensitométrie, déjà légendées par l'auteur.">
<figcaption>Cliché brut, pixels d'origine non modifiés. Cerevisae, CC BY-SA 4.0, Wikimedia Commons, fichier « Chest X-ray showing presence of free air under left diaphragm.png », consulté le 2026-11-10. L'inscription visible dit SUPINE et RESUS, avec un marqueur L. L'auteur a déjà écrit « air under diaphragm », « Pneumoperitoneum » et « Stomach ». La description Commons parle d'air libre sous le diaphragme gauche ; le cours ne tranche pas cette latéralité au-delà de cette description. Aucun diamètre et aucune date de perforation ne se lisent.</figcaption>
</figure>
<figure>
<div style="position:relative;max-width:100%">
<img src="images/0fa3bad94e3ca02b.png" alt="Même fichier, repères numérotés en surimpression, pixels d'origine inchangés." style="width:100%;height:auto;display:block">
<svg viewBox="0,0,1280,731" style="position:absolute;left:0;top:0;width:100%;height:100%">
<circle cx="250" cy="560" r="28" fill="none" stroke="#9b1c1c" stroke-width="4"/>
<text x="240" y="568" fill="#9b1c1c" font-size="32" font-family="Verdana,sans-serif">1</text>
<circle cx="860" cy="300" r="28" fill="none" stroke="#9b1c1c" stroke-width="4"/>
<text x="850" y="310" fill="#9b1c1c" font-size="32" font-family="Verdana,sans-serif">2</text>
<circle cx="1080" cy="430" r="28" fill="none" stroke="#9b1c1c" stroke-width="4"/>
<text x="1070" y="440" fill="#9b1c1c" font-size="32" font-family="Verdana,sans-serif">3</text>
</svg>
</div>
<figcaption>Œuvre dérivée sous la même licence. Le repère 1 numérote la légende déjà imprimée « air under diaphragm ». Le repère 2 numérote la bande que l'auteur appelle Pneumoperitoneum. Le repère 3 numérote la structure que l'auteur appelle Stomach. Ces numéros ne mesurent rien.</figcaption>
</figure>''')

S(9, "Ce signe sépare la perforation, qui est le rang E2, des douleurs sans air libre, car Sinz relie l'air libre à l'opération.", "sinz_fms_2021-14")
S(9, "Sinz retient le cliché debout ou le décubitus latéral gauche pour l'air libre, car la position change sa visibilité.", "sinz_fms_2021-14")
S(9, "Un air libre acquis peut indiquer l'opération sans autre examen, ce qui ne dispense pas de réanimer le patient instable.", "sinz_fms_2021-14")
S(9, "Le piège est d'en déduire l'organe, car l'air ne dit pas si la perforation est ulcéreuse, diverticulaire ou traumatique.", "sinz_fms_2021-14")

W(9, "pa-p9-f1", "Air libre et décision opératoire", [
    ("Sinz retient le cliché debout ou le décubitus latéral gauche, car l'air libre s'y cherche avant la tomodensitométrie.", "sinz_fms_2021-14"),
    ("Si l'air libre est démontré et que la clinique concorde, l'indication opératoire peut se poser sans examen supplémentaire.", "sinz_fms_2021-14"),
    ("Le diagnostic ne reste modifié par la radiographie conventionnelle que dans 4 à 7,2 % des douleurs aiguës.", "sinz_fms_2021-14"),
    ("Cette étude de 1021 personnes montre que le diagnostic clinique reste inchangé après le cliché simple.", "sinz_fms_2021-14"),
    ("Le piège est de croire que l'air nomme l'organe perforé, car il ne remplace ni les constantes ni le récit.", "sinz_fms_2021-14"),
])

W(9, "pa-p9-f2", "Contraste et irradiation, selon Sinz", [
    ("Une tomodensitométrie abdominale expose jusqu'à 10 mSv, et le risque de cancer radio-induit est jugé très faible chez l'adulte.", "sinz_fms_2021-14"),
    ("Une exposition fœtale de 10 mGy augmenterait de 40 % l'incidence des cancers de l'enfance.", "sinz_fms_2021-14"),
    ("Le risque de néphropathie est qualifié de minime si le débit de filtration estimé dépasse 45 ml par minute.", "sinz_fms_2021-14"),
    ("Chez le patient instable, le diagnostic rapide prime, donc l'injection n'est pas refusée pour ce seul motif.", "sinz_fms_2021-14"),
    ("Après 65 ans, une série de 380 patients a compté 5 % de décès et 22 % d'opérations, donc le seuil d'imagerie baisse.", "sinz_fms_2021-14"),
])

# --- 10 Arbre ---
S(10, "L'algorithme part de [[pa-p10-f1|E1]], car l'occlusion mésentérique se recherche avant les causes plus fréquentes.", "sinz_fms_2021-9")
S(10, "Si la pression systolique est de 90 mm Hg ou moins, alors la réanimation commence et l'hémorragie ou le sepsis se recherche.", "sinz_fms_2021-11")
S(10, "Si la douleur est intense et le ventre pauvre, surtout après 65 ans, alors E1 mène à une tomodensitométrie injectée.", "sinz_fms_2021-9")
S(10, "Si une défense diffuse ou un air libre apparaît, alors E2 conduit au contrôle du foyer sans série radiologique supplémentaire.", "sinz_fms_2021-14")
S(10, "Si un orifice herniaire est douloureux et irréductible, alors E3 impose de traiter l'incarcération.", "sinz_fms_2021-11")
S(10, "Si le sang s'extériorise avec une instabilité, alors E4 oriente vers l'hémostase après la mise en condition.", "sinz_fms_2021-11")
S(10, "Si les gaz sont arrêtés sans défense, alors l'iléus mécanique se confirme par l'imagerie et l'on cherche une strangulation.", "sinz_fms_2021-11")
S(10, "Si la douleur migre vers la fosse iliaque droite, alors l'appendicite constitue la branche la plus fréquente.", "sinz_fms_2021-5")
S(10, "Si le signe de Murphy est présent, alors l'échographie biliaire cherche la cholécystite, car elle y surpasse la tomodensitométrie.", "sinz_fms_2021-14")
S(10, "Si la fosse iliaque gauche est inflammatoire, alors la diverticulite se distingue de la perforation libre par l'imagerie.", "sinz_fms_2021-14")
S(10, "Si la lipase est élevée avec une douleur transfixiante, alors la pancréatite entre dans le bilan que Sinz a listé.", "sinz_fms_2021-12")
S(10, "Si aucune de ces branches ne tranche, alors la laparoscopie diagnostique n'intervient qu'après l'échec de l'imagerie.", "sinz_fms_2021-18")

H(10, '''<div class="t" style="overflow-x:auto"><table>
<caption>Algorithme, les graves d'abord, en commençant par E1.</caption>
<thead><tr><th>Si</th><th>Alors</th></tr></thead>
<tbody>
<tr><td>La pression systolique est de 90 mm Hg ou moins</td><td>La réanimation commence, et l'hémorragie ou le sepsis se recherche</td></tr>
<tr><td>La douleur est intense et le ventre pauvre, surtout après 65 ans</td><td>E1 conduit à une tomodensitométrie injectée si le patient peut la recevoir</td></tr>
<tr><td>Une défense diffuse ou un air libre apparaît</td><td>E2 conduit au contrôle du foyer sans série radiologique supplémentaire</td></tr>
<tr><td>Un orifice herniaire est douloureux et irréductible</td><td>E3 impose de traiter l'incarcération</td></tr>
<tr><td>Le sang s'extériorise avec une instabilité</td><td>E4 oriente vers l'hémostase après la mise en condition</td></tr>
<tr><td>Les gaz sont arrêtés sans défense</td><td>L'iléus mécanique se confirme par l'imagerie, et l'on cherche une strangulation</td></tr>
<tr><td>La douleur migre vers la fosse iliaque droite</td><td>L'appendicite, DX.1, constitue la branche la plus fréquente</td></tr>
<tr><td>Le signe de Murphy est présent</td><td>L'échographie biliaire cherche la cholécystite</td></tr>
<tr><td>La fosse iliaque gauche est inflammatoire</td><td>La diverticulite se distingue de la perforation libre</td></tr>
<tr><td>La lipase est élevée avec une douleur transfixiante</td><td>La pancréatite entre dans le bilan</td></tr>
<tr><td>Aucune branche ne tranche</td><td>La laparoscopie diagnostique n'intervient qu'après l'échec de l'imagerie</td></tr>
</tbody></table></div>''')

W(10, "pa-p10-f1", "Laparoscopie seulement en dernier", [
    ("Sinz la réserve au diagnostic encore incertain après les examens non invasifs, donc elle n'ouvre pas l'arbre.", "sinz_fms_2021-18"),
    ("Sa précision diagnostique va de 70 à 99 % dans les séries qu'il cite.", "sinz_fms_2021-18"),
    ("Elle modifie la stratégie dans 10 à 58 % des cas et traite jusqu'à 83 % des patients dans le même temps.", "sinz_fms_2021-18"),
    ("Un taux de conversion de 8 % est rapporté, ce qui se dit au patient avant le geste.", "sinz_fms_2021-18"),
    ("Pendant la grossesse, un accouchement prématuré ou un avortement peut survenir dans jusqu'à 6 % des laparoscopies citées.", "sinz_fms_2021-19"),
])

# --- 11 Prise en charge ---
H(11, '<h4><em>11.A But</em></h4>')
S(11, "Le but immédiat est de réduire l'intervalle jusqu'au traitement, car Sinz en fait la règle d'or de l'abdomen aigu.", "sinz_fms_2021-7")
S(11, "Chaque heure supplémentaire avant l'antibiotique, lorsque le sepsis est identifié, est associée à une hausse de mortalité de 7,6 %.", "sinz_fms_2021-17")
S(11, "L'antibiotique doit donc être administré dans l'[[pa-p11-f1|heure]] qui suit l'identification des symptômes de sepsis.", "sinz_fms_2021-17")
H(11, '<h4><em>11.B Moyens</em></h4>')
S(11, "Sinz sépare le traitement de stabilisation, comme le remplissage et l'analgésie, du traitement de la cause.", "sinz_fms_2021-16")
S(11, "Börner indique que l'analgésie précoce ne gêne pas l'examen, donc on ne laisse pas le patient sans traitement de la douleur.", "boerner_2025-10")
S(11, "[[pa-p11-f2|Dafalgan]] est indiqué pour des douleurs d'intensité faible à modérée, ce qui ne couvre pas à lui seul un abdomen aigu sévère.", "aips-47503-2")
S(11, "La dose journalière maximale de paracétamol oral ne doit pas dépasser 4000 mg, car l'information professionnelle le fixe ainsi.", "aips-47503-2")
S(11, "Au-dessus de 40 kg, la prise va de 500 à 1000 mg, et le maximum indiqué est de 4 g.", "aips-47503-3")
S(11, "L'intervalle entre deux prises orales est de 4 à 8 heures chez l'adulte, car le texte fixe cette borne.", "aips-47503-3")
S(11, "Les comprimés pelliculés de 1 g exigent un poids supérieur à 50 kg, car en dessous ils exposent à un surdosage.", "aips-47503-4")
S(11, "Lorsque la voie orale est impossible, Dafalgan intraveineux traite une douleur légère à modérée, par une perfusion de 15 minutes.", "aips-66702-2")
S(11, "Au-dessus de 50 kg, la dose intraveineuse est de 1 g par administration, jusqu'à 4 fois par jour, sans dépasser 4 g en 24 heures.", "aips-66702-2")
S(11, "De 33 à 50 kg, la dose intraveineuse est de 15 mg par kg, au plus 4 fois par jour.", "aips-66702-2")
S(11, "Dans cette tranche de poids, la dose sur 24 heures ne dépasse pas 60 mg par kg, car le texte fixe ce plafond.", "aips-66702-2")
S(11, "L'intervalle minimal intraveineux est de 4 heures, et la préparation est réservée aux patients de plus de 33 kg.", "aips-66702-2")
S(11, "[[pa-p11-f3|Algifor]] Liquid Caps 400 n'a pas la douleur abdominale parmi ses indications, donc il n'est pas l'antalgique de ce syndrome.", "aips-65372-2")
S(11, "Il est contre-indiqué en cas d'ulcère ou d'hémorragie gastro-intestinale et en cas de maladie inflammatoire intestinale.", "aips-65372-2")
S(11, "Sa dose maximale d'automédication est de 1200 mg par jour pendant 3 jours au plus, ce qui ne constitue pas un protocole d'abdomen aigu.", "aips-65372-2")
S(11, "Le troisième trimestre de la grossesse contre-indique cet ibuprofène, donc on ne l'ajoute pas chez une femme enceinte douloureuse.", "aips-65372-2")
S(11, "Pour une péritonite communautaire sans facteur de risque, Sinz retient une céphalosporine de deuxième génération ou une fluoroquinolone, avec le métronidazole.", "sinz_fms_2021-17")
S(11, "L'alternative est une aminopénicilline avec un inhibiteur de bêta-lactamase, car l'article cite l'amoxicilline associée à l'acide clavulanique.", "sinz_fms_2021-17")
S(11, "Aucune dose en milligrammes n'est recopiée pour ces antibiotiques, car leur information professionnelle suisse n'a pas été ouverte dans ce lot.", "sinz_fms_2021-17")
S(11, "Une administration unique suffit souvent pour une péritonite locale, et l'arrêt se discute après trois jours si l'état s'améliore.", "sinz_fms_2021-17")
S(11, "Pour une péritonite locale avancée avec foyer contrôlé, 4 à 5 jours ne font pas pire que 8 à 10 jours.", "sinz_fms_2021-17")
S(11, "Une durée de 7 à 10 jours au maximum ne se recommande que pour la péritonite nosocomiale sévère avec instabilité.", "sinz_fms_2021-17")
S(11, "En cas de péritonite diffuse, Sinz retient trois piliers, car la chirurgie, l'antibiotique et la réanimation vont ensemble.", "sinz_fms_2021-16")
S(11, "Le paracétamol pendant la grossesse a un risque jugé faible à posologie correcte, et l'information professionnelle dit l'absence d'études contrôlées.", "aips-47503-10")
S(11, "Si la clairance est de 30 ml par minute ou moins, l'intervalle intraveineux minimal atteint 6 heures.", "aips-66702-2")
S(11, "En dessous de 10 ml par minute de clairance, le paracétamol intraveineux ne doit pas être utilisé, faute de données.", "aips-66702-2")
S(11, "En maladie hépatique active décompensée, le paracétamol est contre-indiqué, car le texte vise notamment l'hépatite alcoolique.", "aips-47503-10")
S(11, "Les hémocultures précèdent l'antibiotique en cas de sepsis ou de fièvre, donc le prélèvement ne retarde pas l'heure limite.", "sinz_fms_2021-12")

H(11, '<h4><em>11.C Surveillance</em></h4>')
S(11, "On surveille le pouls, la pression, la température et la vigilance, car ce sont les constantes que Sinz place avant l'abdomen.", "sinz_fms_2021-11")
S(11, "Une néphropathie de contraste se manifeste souvent par une baisse légère du débit, qui se normalise en trois à sept jours.", "sinz_fms_2021-14")
S(11, "La fonction peut rester altérée dans jusqu'à 30 % des cas si un rein malade, un diabète, une insuffisance cardiaque ou une hypertension préexistent.", "sinz_fms_2021-14")
S(11, "L'arrêt de l'antibiotique se discute à trois jours si la péritonite locale s'améliore et qu'aucun facteur de risque spécifique n'est présent.", "sinz_fms_2021-17")

H(11, '<h4><em>11.D Pronostic et sortie</em></h4>')
S(11, "Börner indique une mortalité de 2 à 12 % pour la chirurgie abdominale urgente, donc la seule sédation ne suffit pas à sortir.", "boerner_2025-6")
S(11, "La mortalité du sepsis abdominal atteint 26 %, et 43 % si le traitement est retardé, ce qui fixe l'enjeu du délai.", "boerner_2025-17")
S(11, "Chez plus de 65 ans, 5 % des patients d'une série de 380 sont morts de la cause et 22 % ont été opérés.", "sinz_fms_2021-14")
S(11, "La sortie suppose des constantes stabilisées, une cause nommée ou un plan de révision, car Zahnd rappelle que 10 % relèvent de l'hôpital.", "zahnd_rms_2024-12")
S(11, "Un patient renvoyé doit être revu, car un tableau peu inquiétant au premier contact peut masquer une cause chez le sujet fragile.", "sinz_fms_2021-9")
S(11, "La guérison du symptôme ne se décrète pas sans cause, donc la douleur non spécifique n'est qu'un reliquat après exclusion.", "sinz_fms_2021-5")

H(11, '''<div class="t" style="overflow-x:auto"><table>
<caption>Médicaments dont l'information professionnelle a été lue.</caption>
<thead><tr><th>Spécialité</th><th>Dose lue</th><th>Voie et durée</th><th>Contre-indication majeure lue</th><th>Extrait</th></tr></thead>
<tbody>
<tr><td>Dafalgan, paracétamol, n° 47503<sup class="r"><a href="#sb-aips-47503-10">aips-47503-10</a></sup></td><td>Adulte de plus de 40 kg : 500 à 1000 mg par prise, maximum 4 g, sans dépasser 4000 mg par jour<sup class="r"><a href="#sb-aips-47503-2">aips-47503-2</a></sup><sup class="r"><a href="#sb-aips-47503-3">aips-47503-3</a></sup></td><td>Orale, intervalle de 4 à 8 heures<sup class="r"><a href="#sb-aips-47503-3">aips-47503-3</a></sup></td><td>Maladie hépatique active décompensée<sup class="r"><a href="#sb-aips-47503-10">aips-47503-10</a></sup></td><td>aips-47503</td></tr>
<tr><td>Dafalgan i.v., n° 66702<sup class="r"><a href="#sb-aips-66702-2">aips-66702-2</a></sup></td><td>Plus de 50 kg : 1 g jusqu'à 4 fois par jour, maximum 4 g ; de 33 à 50 kg : 15 mg par kg, maximum 60 mg par kg<sup class="r"><a href="#sb-aips-66702-2">aips-66702-2</a></sup></td><td>Perfusion de 15 minutes, intervalle minimal de 4 heures<sup class="r"><a href="#sb-aips-66702-2">aips-66702-2</a></sup></td><td>Clairance de créatinine inférieure à 10 ml par minute<sup class="r"><a href="#sb-aips-66702-2">aips-66702-2</a></sup></td><td>aips-66702</td></tr>
<tr><td>Algifor Liquid Caps 400, ibuprofène, n° 65372<sup class="r"><a href="#sb-aips-65372-2">aips-65372-2</a></sup></td><td>Non retenu comme traitement de l'abdomen aigu ; maximum d'automédication 1200 mg par jour<sup class="r"><a href="#sb-aips-65372-2">aips-65372-2</a></sup></td><td>Orale, au plus 3 jours en automédication<sup class="r"><a href="#sb-aips-65372-2">aips-65372-2</a></sup></td><td>Ulcère ou hémorragie, maladie inflammatoire intestinale, troisième trimestre<sup class="r"><a href="#sb-aips-65372-2">aips-65372-2</a></sup></td><td>aips-65372</td></tr>
</tbody></table></div>''')

W(11, "pa-p11-f1", "Urgence — conduite chronologique", [
    ("À la première minute, les constantes sont mesurées, car une systolique de 90 mm Hg ou moins change l'ordre.", "sinz_fms_2021-11"),
    ("Dans la même minute, une voie et un remplissage commencent si l'instabilité est présente, sans attendre l'imagerie.", "sinz_fms_2021-16"),
    ("L'analgésie est autorisée tôt, car Börner écrit qu'elle ne gêne pas l'évaluation clinique.", "boerner_2025-10"),
    ("Dès que le sepsis est identifié, l'antibiotique part dans l'heure, après les hémocultures si la fièvre ou le sepsis sont là.", "sinz_fms_2021-17"),
    ("Chaque heure de retard est associée à 7,6 % de mortalité supplémentaire dans les études que Sinz cite pour ce point.", "sinz_fms_2021-17"),
    ("Le contrôle du foyer ne reste pas différé au seul motif d'une stabilisation prolongée en soins intensifs.", "sinz_fms_2021-16"),
])

W(11, "pa-p11-f2", "Dafalgan oral, information professionnelle", [
    ("La spécialité couvre des douleurs faibles à modérées et la fièvre, donc un abdomen aigu sévère dépasse cette indication.", "aips-47503-2"),
    ("Le maximum journalier est de 4000 mg chez l'adulte, et de 2000 mg entre 9 et 12 ans.", "aips-47503-2"),
    ("Au-dessus de 40 kg, la prise va de 500 à 1000 mg, soit un à deux comprimés sécables, au plus 4 g.", "aips-47503-3"),
    ("L'intervalle adulte est de 4 à 8 heures, et l'on vérifie qu'un autre produit ne contient pas déjà du paracétamol.", "aips-47503-2"),
    ("Pendant la grossesse, le risque est jugé faible à posologie correcte, et aucune étude contrôlée n'est disponible.", "aips-47503-10"),
    ("Les effets à annoncer incluent l'atteinte hépatique en cas de dépassement, car la dose maximale existe pour cette raison.", "aips-47503-2"),
])

W(11, "pa-p11-f3", "Pourquoi l'ibuprofène n'est pas le réflexe", [
    ("Algifor Liquid Caps 400 est autorisé en automédication pour des douleurs articulaires, dorsales, dentaires ou menstruelles, et pour la fièvre grippale.", "aips-65372-2"),
    ("La liste lue ne contient pas la douleur abdominale, donc l'indication ne se devine pas.", "aips-65372-2"),
    ("L'ulcère, l'hémorragie et la maladie inflammatoire intestinale figurent parmi les contre-indications, ce qui croise le diagnostic différentiel.", "aips-65372-2"),
    ("Le troisième trimestre contre-indique la molécule, et une insuffisance rénale sévère avec clairance sous 30 ml par minute aussi.", "aips-65372-2"),
    ("Le piège d'examen est de prescrire un anti-inflammatoire pour faire taire une douleur dont la cause peut être un ulcère.", "aips-65372-2"),
])

# --- 12 Prévention ---
S(12, "La prévention primaire vise les facteurs que l'anamnèse peut modifier, car les médicaments ulcérogènes figurent dans le récit de Sinz.", "sinz_fms_2021-8")
S(12, "Éviter un anti-inflammatoire chez un patient déjà ulcéreux relève de cette prévention, puisque Algifor est contre-indiqué dans ce cas.", "aips-65372-2")
S(12, "La stratégie genevoise de la douleur chronique demande un bilan lorsque des drapeaux existent, donc on ne rassure pas sur la seule durée.", "hug_dac_2023-3")
S(12, "La prévention secondaire reconnaît tôt la récidive, car un patient déjà opéré de l'abdomen a un risque d'occlusion identifié par Sinz.", "sinz_fms_2021-9")
S(12, "Revoir un patient renvoyé dans un délai court constitue cette prévention, puisque le premier contact peut être faussement rassurant.", "sinz_fms_2021-9")
S(12, "La prévention tertiaire limite les séquelles du sepsis et de l'opération, car la mortalité augmente lorsque le foyer est contrôlé trop tard.", "sinz_fms_2021-17")
S(12, "Après une injection de contraste, surveiller le rein pendant trois à sept jours relève de cette prévention chez le patient à risque.", "sinz_fms_2021-14")
S(12, "Zahnd rappelle qu'environ 10 % des douleurs aiguës en médecine générale nécessitent l'hôpital, donc le seuil d'adressage fait partie de la prévention.", "zahnd_rms_2024-12")
S(12, "Après 70 ans, le colloque genevois décrit des causes plus souvent chirurgicales, donc le seuil d'imagerie baisse.", "hug_daa_2017-2")
S(12, "Aucune de ces mesures ne remplace le traitement de la cause déjà constituée, car la prévention tertiaire suppose le foyer contrôlé.", "sinz_fms_2021-16")

# --- 13 Points clés ---
S(13, "L'abdomen aigu est un état temporaire et non un diagnostic, donc la triade de Sinz ouvre le travail sans le fermer.", "sinz_fms_2021-4")
S(13, "On exclut d'abord l'occlusion mésentérique, la perforation, la hernie incarcérée et l'hémorragie, car leur rang E ne suit pas leur fréquence.", "sinz_fms_2021-5")
S(13, "Une systolique de 90 mm Hg ou moins, un pouls au-delà de 95 ou une température sous 36,5 °C imposent la réanimation avant le diagnostic d'organe.", "sinz_fms_2021-11")
S(13, "L'antibiotique part dans l'heure du sepsis identifié, car chaque heure supplémentaire est associée à 7,6 % de mortalité en plus.", "sinz_fms_2021-17")
S(13, "Le paracétamol a une dose maximale lue de 4000 mg par jour, car l'information professionnelle interdit de la dépasser.", "aips-47503-2")
S(13, "L'air libre peut indiquer l'opération sans autre imagerie si la clinique concorde, cependant il ne nomme pas l'organe perforé.", "sinz_fms_2021-14")

# --- 14 Pièges ---
S(14, "Pourquoi une douleur épigastrique ne suffit-elle pas à diagnostiquer une gastrite, alors que l'étage embryonnaire y projette aussi la voie biliaire ?", "sinz_fms_2021-8")
S(14, "La bonne réponse est que le lieu ressenti suit l'étage et non l'organe, donc l'échographie biliaire reste possible.", "sinz_fms_2021-8")
S(14, "Peut-on affirmer l'appendicite sur un McBurney positif, puisque sa sensibilité ne dépasse pas 45 % dans la synthèse de Börner ?", "boerner_2025-16")
S(14, "La bonne réponse est non, car une sensibilité basse laisse passer des appendicites, et la spécificité de 50 à 80 % ne confirme pas seule.", "boerner_2025-16")
S(14, "Faut-il refuser l'analgésie avant l'examen, alors que Börner écrit qu'elle ne gêne pas l'évaluation ?", "boerner_2025-10")
S(14, "La bonne réponse est non, car l'analgésie précoce est compatible avec un examen fiable.", "boerner_2025-10")
S(14, "Quelle est la dose journalière maximale de Dafalgan oral chez l'adulte, et pourquoi un dépassement est-il une erreur ?", "aips-47503-2")
S(14, "La bonne réponse est 4000 mg, car l'information professionnelle fixe ce plafond et non un chiffre arrondi au-dessus.", "aips-47503-2")
S(14, "Pourquoi Algifor est-il un mauvais réflexe devant une douleur abdominale non diagnostiquée ?", "aips-65372-2")
S(14, "La bonne réponse est que l'ulcère, l'hémorragie et la maladie inflammatoire intestinale contre-indiquent cet ibuprofène.", "aips-65372-2")
S(14, "Dans quel délai l'antibiotique doit-il partir lorsque le sepsis abdominal est identifié, et que vaut une heure de plus ?", "sinz_fms_2021-17")
S(14, "La bonne réponse est dans l'heure, car chaque heure supplémentaire est associée à une mortalité augmentée de 7,6 %.", "sinz_fms_2021-17")
S(14, "Un abdomen souple après 70 ans permet-il de rentrer le patient, puisque la défense manque souvent ?", "sinz_fms_2021-11")
S(14, "La bonne réponse est non, car 5 % des autopsies après 70 ans ont retrouvé un abdomen aigu non détecté.", "sinz_fms_2021-11")

H(14, '''<div class="t" style="overflow-x:auto"><table>
<caption>Questions, réponses, raisons.</caption>
<thead><tr><th>Question</th><th>Réponse</th><th>Raison</th></tr></thead>
<tbody>
<tr><td>L'abdomen aigu est-il un diagnostic ?</td><td>Non, c'est un état temporaire.</td><td>Sinz refuse le synonyme qui efface cette distinction.</td></tr>
<tr><td>Quel rang exclut-on en premier ?</td><td>L'occlusion mésentérique, E1.</td><td>Les symptômes sont souvent masqués, malgré une fréquence de 9,4 %.</td></tr>
<tr><td>Quelle dose orale maximale de paracétamol ?</td><td>4000 mg par jour<sup class="r"><a href="#sb-aips-47503-2">aips-47503-2</a></sup>.</td><td>Chiffre lu dans l'information professionnelle, sans arrondi.</td></tr>
<tr><td>L'ibuprofène d'automédication traite-t-il l'abdomen aigu ?</td><td>Non.</td><td>Indication non lue pour ce symptôme, et contre-indications croisant le différentiel.</td></tr>
</tbody></table></div>''')

H(14, '<div class="finale">Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ? La réponse est réservée à l’audit de Bitunder.</div>')

# Compléments sourcés, pour atteindre la bande sans répéter une phrase.
S(2, "La douleur non spécifique représente 30 à 41 % des douleurs aiguës aux urgences dans le tableau de Börner.", "boerner_2025-20")
S(2, "Börner décrit l'iléus pour 4 à 5 % des douleurs aiguës aux urgences, avec une incidence de 50 à 100 pour 100 000.", "boerner_2025-20")
S(2, "La pancréatite aiguë y représente 2 à 4 %, avec une incidence de 13 à 43 pour 100 000.", "boerner_2025-20")
S(2, "L'ulcère peptique, parfois perforé, représente 1 à 3 %, avec une incidence de 7 à 15 pour 100 000.", "boerner_2025-20")
S(2, "La diverticulite, parfois perforée, représente 1 à 2 %, avec une incidence de 150 à 160 pour 100 000.", "boerner_2025-20")
S(2, "L'ischémie abdominale représente 0 à 1 %, avec une incidence de 6 à 8 pour 100 000.", "boerner_2025-20")
S(2, "Un foyer gynécologique représente 1 à 4 % et un foyer urologique 2 à 4 % dans le même tableau.", "boerner_2025-20")
S(2, "Une cause oncologique représente 1 à 2 % des douleurs aiguës aux urgences, sans incidence chiffrée dans ce tableau.", "boerner_2025-20")
S(2, "Börner indique que la mortalité augmente à chaque heure sans traitement spécifique, au-delà de la fourchette de 2 à 12 %.", "boerner_2025-6")
S(2, "Börner ne sépare pas ici les cas pédiatriques et gériatriques, car l'article se concentre sur les causes fréquentes de l'adulte.", "boerner_2025-19")
S(2, "Les causes fréquentes qu'il retient incluent l'appendicite, la cholécystite, la pancréatite et la diverticulite, ainsi que les troubles moteurs.", "boerner_2025-19")
S(2, "Le traumatisme abdominal et les tumeurs de la cavité figurent aussi parmi les causes, donc le champ dépasse l'inflammation.", "boerner_2025-19")

S(6, "La palpation de la paroi est la partie la plus importante de l'examen, car elle juge la défense et l'urgence du traitement.", "sinz_fms_2021-11")
S(6, "Des critères définitifs des bruits intestinaux doivent encore être déterminés, car aucune méthode standard ne fait consensus.", "sinz_fms_2021-11")

S(9, "Au moins un tiers des patients a des manifestations atypiques, donc le laboratoire complète un examen qui peut tromper.", "sinz_fms_2021-12")
S(9, "Le bilan recommandé comprend la bilirubine, les transaminases, la gamma-glutamyltransférase et la phosphatase alcaline.", "sinz_fms_2021-12")
S(9, "Ces enzymes servent aussi de valeur de référence pour suivre l'évolution, car Sinz ne les réserve pas au seul diagnostic initial.", "sinz_fms_2021-12")

S(10, "La Society of American Gastrointestinal Surgeons admet la laparoscopie lorsque les examens non invasifs sont épuisés.", "sinz_fms_2021-18")
S(10, "Le diagnostic doit alors rester incertain, car cette société ne place pas la laparoscopie avant l'imagerie.", "sinz_fms_2021-18")

S(11, "Sinz indique le céfuroxime et le céfotaxime comme exemples de céphalosporines de deuxième génération.", "sinz_fms_2021-17")
S(11, "La ciprofloxacine est l'exemple de fluoroquinolone que Sinz associe au métronidazole dans la péritonite communautaire.", "sinz_fms_2021-17")
S(11, "En milieu ambulatoire, Escherichia coli, Bacteroides fragilis et les entérocoques dominent, car la flore dépend du siège.", "sinz_fms_2021-17")
S(11, "Le choix de l'antibiotique tient compte de l'immunodépression, du traitement préalable et des résistances locales.", "sinz_fms_2021-17")
S(11, "Un prélèvement bactériologique est recommandé, donc le spectre réel peut corriger le traitement probabiliste.", "sinz_fms_2021-17")
S(11, "Azuhata décrit une corrélation entre l'heure d'admission, la chirurgie et la létalité, donc le délai de contrôle compte.", "sinz_fms_2021-16")
S(11, "Chez le patient de plus de 33 kg avec maladie hépatique chronique, la dose quotidienne ne dépasse pas 2 g.", "aips-66702-2")
S(11, "La même limite de 2 g vise l'alcoolisme chronique, la dénutrition, la déshydratation et la cachexie de l'adulte.", "aips-66702-2")
S(11, "La durée maximale du traitement intraveineux est de 2 jours chez l'adulte et chez l'enfant, car le texte fixe ce plafond.", "aips-66702-2")
S(11, "Le paracétamol oral peut provoquer une nécrolyse ou un syndrome de Stevens-Johnson, donc on doit l'arrêter au premier signe cutané.", "aips-47503-10")
S(11, "Le paracétamol passe dans le lait, car sa concentration y est proche de celle du plasma maternel.", "aips-47503-10")
S(11, "Des éruptions ont été rapportées chez le nourrisson allaité, cependant aucune conséquence durable n'est connue.", "aips-47503-10")
S(11, "Les études neurologiques des enfants exposés in utero ne restent pas concluantes, car les résultats ne sont pas clairs.", "aips-47503-10")
S(11, "Aucune donnée clinique sur la fertilité n'est disponible, donc ce point ne se déduit pas de la posologie antalgique.", "aips-47503-10")
S(11, "À la posologie recommandée, le paracétamol reste sans influence négative connue sur la conduite, selon les expériences à long terme.", "aips-47503-10")
S(11, "Le déficit en glucose-6-phosphate déshydrogénase contre-indique le paracétamol intraveineux, car il peut entraîner une anémie hémolytique.", "aips-66702-2")
S(11, "L'hyperbilirubinémie constitutionnelle, appelée syndrome de Gilbert, contre-indique la forme intraveineuse de paracétamol.", "aips-66702-2")

S(12, "En l'absence de red flags, certains éléments anamnestiques doivent faire chercher une cause organique, donc le traitement peut être ciblé.", "hug_dac_2023-3")
S(12, "Une néoplasie digestive peut survenir sans symptômes B, donc leur absence ne rassure pas, même avant 50 ans.", "hug_dac_2023-3")
S(5, "Des maux de dos peuvent accompagner une cause extra-abdominale, donc Sinz prévoit d'impliquer une autre discipline.", "sinz_fms_2021-10")
S(11, "Entre 9 et 12 ans, la dose journalière maximale de paracétamol oral est de 2000 mg, car le texte distingue cet âge.", "aips-47503-2")
S(11, "Un comprimé effervescent à 500 mg de paracétamol contient 197 mg de sodium, car la composition le précise.", "aips-47503-2")
S(11, "Une pustulose exanthématique aiguë généralisée figure parmi les réactions graves, donc le traitement doit cesser au premier signe cutané.", "aips-47503-10")
S(11, "En cas de péritonite locale, une administration unique suffit dans la plupart des cas, selon la synthèse de Sinz.", "sinz_fms_2021-17")

out = os.path.join(os.path.dirname(__file__), 'fragments')
m.ecrire(out)
print('fenêtres', m.fen)

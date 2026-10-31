#!/usr/bin/env python3
"""Fenêtres 4 à 14 de la Phase A, puis assemblage."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from moteur import GLOSSAIRE, SOURCES_LI, bouton, ecrire, fenetre, page
from phase_a import D1, D2, D3, F1, F2, F3, bloc, section
from plus_a import PLUS

F4 = """
On relit d'abord les triglycérides avant de croire un LDL calculé.

On cherche ensuite une cause secondaire, puis on situe le risque, puis seulement on choisit l'intensité du traitement.

Un prélèvement lactescent ou une douleur abdominale passe devant le calcul du risque à dix ans.
"""

D4 = """
Étape 1. Noter si le patient est à jeun, ce qu'il a bu, et s'il a une douleur abdominale. Un sérum opalescent oriente vers les chylomicrons.

Étape 2. Calculer le LDL seulement si les triglycérides sont à 4,5 mmol/l ou moins.|s1

Étape 3. Calculer toujours le non HDL, qui reste valide quand Friedewald s'arrête.|s1

Étape 4. Demander la thyréostimuline, la glycémie ou l'hémoglobine glyquée, la créatinine, le rapport albumine sur créatinine, les transaminases et une bandelette urinaire si le contexte le suggère.

Étape 5. Lister l'alcool, les œstrogènes, les corticoïdes, les rétinoïdes, les diurétiques thiazidiques, les bêtabloquants, les antipsychotiques, les inhibiteurs de protéase et la ciclosporine.

Étape 6. Chercher une grossesse. Une statine et Nustendi y sont écartés. Le texte de Sortis dit que l'atorvastatine peut être délétère pour le fœtus par la baisse de synthèse du cholestérol.|s6

Nustendi est contre-indiqué pendant la grossesse et l'allaitement.|s13

Étape 7. Situer le risque avec le GSLA de 20 à 69 ans sans diabète, ou avec SCORE2 et SCORE2-OP de 40 à 89 ans sans diabète.|s3

On n'utilise pas SCORE2 chez une personne qui a déjà une maladie athérosclérotique, ni pour recalculer le risque après le début d'un hypolipémiant.|s2

Étape 8. Si le LDL non traité est très haut, ou s'il y a un xanthome, un arc cornéen avant 45 ans, ou une famille touchée jeune, appliquer le réseau néerlandais en entier.|s1

Étape 9. Doser la lipoprotéine(a) une fois dans la vie adulte. Le guide de 2019 le propose pour repérer les valeurs héritées très hautes.|s1

La mise à jour de 2025 retient une lipoprotéine(a) au-dessus de 50 mg/dl, soit 105 nmol/l, comme modificateur de risque.|s2

Étape 10. Fixer la cible de LDL selon la catégorie, puis choisir le médicament dont l'information professionnelle suisse porte la dose. Mesurer à nouveau quatre à six semaines après un changement, délai écrit dans la mise à jour de 2025.|s2

Les informations de Sortis et de Crestor parlent, elles, d'un intervalle d'au moins quatre semaines avant d'adapter la dose.|s6

Un LDL déjà traité ne sert pas de valeur de départ pour le réseau néerlandais, qui demande le LDL sans traitement.|s1

Si le patient prend déjà une statine, on estime la valeur passée avec prudence ou on cherche une ancienne biologie. On n'invente pas le LDL d'avant.
"""

F5 = """
On demande l'âge du premier infarctus, du premier AVC et des pontages dans la famille du premier degré.

Une pancréatite, une douleur épigastrique après un repas gras, ou un alcool massif changent l'ordre des priorités.

Les drapeaux rouges sont le sérum lactescent, les triglycérides au-dessus de 10 mmol/l, le xanthome tendineux et le LDL d'enfant déjà très haut.|s1
"""

D5 = """
L'âge coronaire précoce retenu par le réseau néerlandais est inférieur à 55 ans chez l'homme et inférieur à 60 ans chez la femme, pour le parent comme pour le patient.|s1

Un parent du premier degré avec un xanthome tendineux ou un arc cornéen, ou un enfant de moins de 18 ans avec un LDL au-dessus du 95e percentile, vaut 2 points.|s1

Un parent avec une maladie coronaire ou vasculaire précoce, ou un LDL au-dessus du 95e percentile, vaut 1 point.|s1

La maladie coronaire précoce du patient vaut 2 points. Une atteinte cérébrale ou périphérique précoce vaut 1 point.|s1

On additionne ces antécédents une seule fois par groupe, en gardant le nombre le plus haut du groupe.|s1

On cherche une hypothyroïdie par la fatigue, le froid, la constipation et la prise de poids. On la confirme par la thyréostimuline avant d'attribuer tout le LDL à une forme familiale.

Un syndrome néphrotique se devine par les œdèmes et les urines mousseuses. Il élève le LDL et demande le traitement de la maladie rénale, pas seulement une statine.

Une cholestase élève le cholestérol par une lipoprotéine anormale. Les transaminases et la phosphatase alcaline précèdent le choix du médicament.

L'alcool élève surtout les triglycérides. C'est le facteur aggravant le plus cité quand le pancréas est menacé.|s1

Une grossesse récente, un contraceptif oral ou un traitement par œstrogènes oraux orientent vers une poussée de triglycérides.

Les drapeaux rouges qui font hospitaliser ou appeler dans la journée sont une douleur abdominale avec triglycérides hauts, un déficit neurologique, une douleur coronarienne, et un enfant avec un LDL extrême.

Un xanthome tendineux n'est pas un drapeau de pancréatite. C'est un drapeau de forme familiale et de risque vasculaire très haut.

Un arc cornéen après 60 ans est banal. Avant 45 ans, il entre dans le réseau néerlandais pour 4 points.|s1

On demande les médicaments un par un. Le patient oublie souvent le rétinoïde, l'antipsychotique et le corticoïde pris par intermittence.

Le tabac, la tension et le diabète ne sont pas des lipides. Ils changent la catégorie de risque et donc la cible de LDL.
"""

F6 = """
On regarde les tendons, les paumes, les coudes, les genoux, les paupières et la cornée.

On ouvre les fenêtres sur le xanthome tendineux, le xanthome éruptif, le xanthome palmaire et l'arc cornéen.

Un examen cutané normal n'écarte pas une forme familiale. Beaucoup d'hétérozygotes n'ont pas de xanthome.
"""

D6 = """
Le xanthome tendineux est un dépôt ferme, souvent au tendon d'Achille ou aux extenseurs des doigts. Il vaut 6 points et ne se confond pas avec un nodule rhumatoïde.|s1

Le xanthome éruptif est une poussée de petites papules jaunes sur les fesses, les coudes et le dos. Il accompagne les triglycérides très hauts, pas le LDL isolé.

Le xanthome palmaire est un dépôt jaune dans les plis de la main. Il oriente vers la dysbêtalipoprotéinémie, phénotype III.

Le xanthome tubéreux siège aux coudes et aux genoux. On le voit dans les formes sévères, y compris l'homozygote.

Le xanthelasma des paupières est fréquent et peu spécifique. Seul, il ne fait pas le diagnostic de forme familiale.

L'arc cornéen avant 45 ans vaut 4 points. L'examen du xanthome et celui de l'arc sont exclusifs l'un de l'autre pour le total : le maximum du groupe est 6 points.|s1

On palpe les deux tendons d'Achille, pas seulement le plus visible. On regarde les paumes en pleine lumière.

Une hépatomégalie avec LDL haut et HDL bas fait chercher le déficit en lipase acide lysosomale.|s1

Une rétine lipémique, blanc laiteux des vaisseaux, accompagne les triglycérides extrêmes.

Un enfant avec des xanthomes cutanés et un LDL très haut fait évoquer la forme homozygote avant l'âge adulte.

L'examen neurologique et la recherche d'une stéatorrhée comptent quand le LDL est au contraire extrêmement bas, vers l'abêtalipoprotéinémie.|s1
"""

EXAM = (
    fenetre(
        "a-tendon",
        "Xanthome tendineux",
        bloc(
            """
Le dépôt est dur, indolore, collé au tendon. Le tendon d'Achille et les extenseurs de la main sont les sièges classiques.

On le distingue d'un épaississement rhumatoïde par l'absence d'arthrite et par le LDL très haut.

Dans le réseau néerlandais, ce signe vaut 6 points. On ne lui ajoute pas les 4 points de l'arc cornéen.|s1

Sa présence, chez un adulte jeune, fait traiter le risque comme très élevé dès qu'une maladie vasculaire ou un autre facteur majeur existe.|s1
"""
        ),
    )
    + fenetre(
        "a-eruptif",
        "Xanthome éruptif",
        bloc(
            """
Les papules sont jaunes, petites, nombreuses, souvent prurigineuses, sur les faces d'extension et les fesses.

Elles apparaissent quand les triglycérides sont très hauts, en particulier au-dessus de 10 mmol/l, zone où le risque de pancréatite devient cliniquement significatif.|s1

Elles régressent si les triglycérides baissent. Elles ne comptent pas comme xanthome tendineux dans le réseau néerlandais.

Les voir impose de suspendre l'alimentation grasse et l'alcool, pas d'augmenter d'abord une statine.
"""
        ),
    )
    + fenetre(
        "a-palmaire",
        "Xanthome palmaire",
        bloc(
            """
Le pli palmaire se colore en jaune orangé. Le signe oriente vers l'accumulation de remnants, phénotype III de Fredrickson.|s5

Le cholestérol et les triglycérides sont souvent élevés ensemble, dans des proportions proches.

Le LDL calculé par Friedewald est alors trompeur, car le cholestérol voyage dans les IDL autant que dans les LDL.|s1

On confirme par l'électrophorèse ou le génotype de l'apolipoprotéine E quand le tableau clinique est typique. Le cours ne fixe pas un laboratoire unique.
"""
        ),
    )
    + fenetre(
        "a-arc",
        "Arc cornéen",
        bloc(
            """
L'arc est un cercle gris ou blanc en périphérie de la cornée. Avant 45 ans, il vaut 4 points.|s1

Après la cinquantaine, il est fréquent et ne porte pas ces 4 points.

On ne l'additionne pas au xanthome tendineux. Le guide dit de ne garder que le nombre le plus haut de ce groupe, avec un maximum de 6.|s1

Un arc isolé, sans LDL haut ni famille touchée, ne lance pas un traitement intensif.
"""
        ),
    )
)

F7 = """
Le phénotype de Fredrickson classe le plasma, pas le gène.

Les six images sont le type I, le IIa, le IIb, le III, le IV et le V. Aucune ne se retire du tableau.|s5

Le type I et le type V menacent le pancréas. Le IIa et le IIb menacent les artères. Le III fait les deux.
"""

TABLE_F = """
<div class="tw"><table>
<caption>Phénotypes de Fredrickson, Levy et Lees</caption>
<thead><tr><th>Type</th><th>Particules</th><th>Lecture simple</th></tr></thead>
<tbody>
<tr><td>I</td><td>Chylomicrons</td><td>Triglycérides extrêmes, plasma lactescent, pancréatite. Forme monogénique rare de lipase.</td></tr>
<tr><td>IIa</td><td>LDL</td><td>Cholestérol haut, triglycérides ordinaires. Forme familiale ou polygénique.</td></tr>
<tr><td>IIb</td><td>LDL et VLDL</td><td>Cholestérol et triglycérides hauts ensemble. Hyperlipidémie combinée.</td></tr>
<tr><td>III</td><td>Remnants</td><td>Cholestérol et triglycérides proches, xanthome palmaire, apoE souvent en cause.</td></tr>
<tr><td>IV</td><td>VLDL</td><td>Triglycérides hauts, cholestérol peu déplacé. Le plus fréquent dans l'étude américaine de 2019.</td></tr>
<tr><td>V</td><td>Chylomicrons et VLDL</td><td>Triglycérides très hauts, mélange acquis et génétique, risque de pancréatite.</td></tr>
</tbody></table></div>
"""

D7 = """
Fredrickson, Levy et Lees ont séparé cinq phénotypes, I à V, selon les lipoprotéines. Le II se divise en IIa et IIb. L'ensemble fait six images cliniques. L'OMS a repris ce cadre en 1972.|s5

Le type I est l'excès de chylomicrons. Le type V ajoute les VLDL aux chylomicrons.|s5

Le type IIa est l'excès de LDL. Le type IIb ajoute les VLDL aux LDL.|s5

Le type III est l'excès de remnants. Le type IV est l'excès de VLDL.|s5

Le cadre ne dit pas si la cause est génétique ou acquise. Un type IV peut être l'alcool, le diabète ou une charge polygénique.|s5

Il ne classe ni le HDL ni la lipoprotéine(a). Un HDL bas ou une lipoprotéine(a) haute se lit à part.|s5

La plupart des phénotypes II à V sont polygéniques. Les vraies maladies d'un seul gène sont surtout la chylomicronémie familiale, ancien type I, et une partie des LDL très hauts, ancien type IIa.|s5

Au laboratoire, un plasma laissé au repos montre un surnageant crémeux s'il y a des chylomicrons. Un trouble diffus oriente vers les VLDL.

Le type III se confirme mal par le seul calcul de Friedewald. Le cholestérol des remnants est compté avec le LDL.|s1

On traite la menace visible. Pancréatite d'abord si les triglycérides dépassent 10 mmol/l. Artères d'abord si le LDL porte le risque et que les triglycérides sont modestes.|s1

Le même patient peut changer de phénotype si l'alcool, le diabète ou un médicament s'ajoutent. On reclasse après avoir retiré la cause.
"""

F8 = """
Le diagnostic positif d'une forme familiale hétérozygote repose sur le réseau néerlandais complet, pas sur un seul LDL.

Au-dessus de 8 points, le diagnostic est certain. De 6 à 8 points, il est probable. De 3 à 5 points, il est possible.|s1

Un total sous 3 points n'atteint pas la bande possible. Le guide lu ne nomme pas une quatrième étiquette au-dessous.
"""

TABLE_D = """
<div class="tw"><table>
<caption>Réseau néerlandais, critères complets</caption>
<thead><tr><th>Groupe</th><th>Critère</th><th>Points</th></tr></thead>
<tbody>
<tr><td>Famille</td><td>Parent du premier degré avec maladie coronaire ou vasculaire précoce, ou LDL au-dessus du 95e percentile</td><td>1</td></tr>
<tr><td>Famille</td><td>Parent avec xanthome tendineux ou arc, ou enfant de moins de 18 ans avec LDL au-dessus du 95e percentile</td><td>2</td></tr>
<tr><td>Patient</td><td>Maladie coronaire avant 55 ans chez l'homme ou 60 ans chez la femme</td><td>2</td></tr>
<tr><td>Patient</td><td>Atteinte cérébrale ou périphérique aux mêmes âges</td><td>1</td></tr>
<tr><td>Examen</td><td>Xanthome tendineux</td><td>6</td></tr>
<tr><td>Examen</td><td>Arc cornéen avant 45 ans</td><td>4</td></tr>
<tr><td>LDL sans traitement</td><td>Au moins 8,5 mmol/l</td><td>8</td></tr>
<tr><td>LDL sans traitement</td><td>De 6,5 à 8,4 mmol/l</td><td>5</td></tr>
<tr><td>LDL sans traitement</td><td>De 5,0 à 6,4 mmol/l</td><td>3</td></tr>
<tr><td>LDL sans traitement</td><td>De 4,0 à 4,9 mmol/l</td><td>1</td></tr>
<tr><td>Gène</td><td>Mutation fonctionnelle de LDLR, de l'apolipoprotéine B ou de PCSK9</td><td>8</td></tr>
</tbody></table></div>
<p>On ne garde qu'un nombre par groupe, le plus haut. L'examen vaut au plus 6 points même si le xanthome et l'arc sont tous les deux présents.<sup class="s">1</sup></p>
"""

D8 = """
Le guide de 2019 publie le tableau entier du réseau néerlandais. Le diagnostic certain demande plus de 8 points. Le diagnostic probable demande 6 à 8 points. Le diagnostic possible demande 3 à 5 points.|s1

Exemple. LDL sans traitement à 6,8 mmol/l, soit 5 points. Xanthome tendineux, 6 points. Père infarctus à 50 ans, 1 point. Total 12. Diagnostic certain, sans attendre l'ADN.|s1

Si l'on ajoutait aussi 4 points d'arc cornéen, on tricherait. Le groupe examen est plafonné à 6.|s1

Un LDL à 5,2 mmol/l vaut 3 points. Sans famille ni signe cutané, le dossier reste possible, pas certain.|s1

Une mutation fonctionnelle vaut 8 points à elle seule et rend le diagnostic certain.|s1

Le dépistage en cascade de la famille est recommandé dès que le cas index est reconnu.|s1

Chez l'enfant, le test se discute dès 5 ans, plus tôt si l'on craint une forme homozygote.|s1

Une statine se discute chez l'enfant à partir de 8 à 10 ans. La cible citée après 10 ans est un LDL inférieur à 3,5 mmol/l.|s1

Les autres critères cités par le guide, Simon Broome et les critères OMS, existent. Le cours détaille le réseau néerlandais parce que le GSLA s'y réfère pour l'adulte.|s3

Le diagnostic d'une dyslipidémie secondaire est positif quand la cause se démontre et que les lipides bougent avec elle. Une thyréostimuline haute avec un LDL haut en est l'exemple.

Le diagnostic de pancréatite liée aux triglycérides est positif quand la douleur et les enzymes pancréatiques rencontrent des triglycérides au-dessus de 10 mmol/l, ou parfois déjà entre 5 et 10.|s1

Le diagnostic d'élévation de la lipoprotéine(a) est positif au-dessus de 50 mg/dl, environ 105 nmol/l, sur un dosage fait une fois, sans être à jeun obligatoire dans le texte lu.|s2
"""

F9 = """
Le bilan de première ligne est le profil lipidique, la thyréostimuline, la glycémie, la créatinine et les transaminases.

La lipoprotéine(a) se dose une fois. La créatine kinase se discute avant une statine si le muscle est déjà douloureux.

On ne répète pas un génotypage large sans une question clinique précise.
"""

D9 = """
Profil à demander. Cholestérol total, HDL, triglycérides, LDL calculé si la formule est licite, non HDL toujours.|s1

Apolipoprotéine B si les triglycérides sont hauts, si le LDL calculé est douteux, ou si l'on vise la cible secondaire.|s1

Lipoprotéine(a) une fois chez l'adulte, et de nouveau comme modificateur si le risque est proche d'une décision.|s2

Thyréostimuline avant de conclure à une forme familiale ou de lancer une statine chez un LDL inexpliqué.

Glycémie à jeun ou hémoglobine glyquée, tension, tour de taille et taille pour l'IMC. Le syndrome métabolique change le phénotype et la cible.

Créatinine et estimation du débit. Un débit inférieur à 30 ml/min/1,73 m2 sans diabète ni maladie athérosclérotique place dans le risque très élevé de la page suisse.|s4

Rapport albumine sur créatinine quand le diabète ou le rein est en jeu. Les bornes de la page suisse distinguent 30 et 300 mg/g.|s4

Transaminases avant une statine, puis selon l'information du produit. Crestor propose un contrôle avant le traitement et trois mois après.|s7

Créatine kinase si les muscles ont déjà souffert sous une statine, si le patient est fragile, ou si une douleur apparaît. On n'invente pas un rythme unique pour tout le monde.

Électrophorèse des lipoprotéines ou génotype de l'apoE si le tableau III est probable.

Panel des gènes de la lipase si les triglycérides restent extrêmes après avoir retiré l'alcool et le diabète.

Recherche de mutation LDLR, apolipoprotéine B ou PCSK9 si le réseau néerlandais est probable ou certain, ou si le LDL dépasse 5 mmol/l chez l'adulte.|s1

Le guide cite aussi 4 mmol/l chez l'enfant comme niveau qui fait chercher la forme familiale.|s1

Imagerie. La page suisse accepte la preuve de plaques. Elle dit manquer de preuves pour utiliser le score calcique et l'épaisseur intima-média comme facteurs dans le diabète de type 2.|s4

Le mot score, ici, désigne le score calcique. Il ne remplace pas SCORE2.|s4
"""

F10 = """
L'arbre commence par la menace immédiate, puis par la cause réversible, puis par la catégorie de risque.

Les cibles de LDL de 2019 restent 1,4, 1,8, 2,6 et 3,0 mmol/l. La mise à jour de 2025 ne les change pas.|s2

SCORE2 s'adresse aux personnes de moins de 70 ans. SCORE2-OP s'adresse à celles de 70 ans et plus.|s2
"""

TABLE_R = """
<div class="tw"><table>
<caption>Cibles de LDL, guide ESC/EAS 2019, inchangées en 2025</caption>
<thead><tr><th>Catégorie</th><th>Cible de LDL</th><th>Baisse relative</th></tr></thead>
<tbody>
<tr><td>Très haut risque</td><td>Inférieure à 1,4 mmol/l</td><td>Au moins 50 pour cent depuis la valeur de départ</td></tr>
<tr><td>Haut risque</td><td>Inférieure à 1,8 mmol/l</td><td>Au moins 50 pour cent</td></tr>
<tr><td>Risque modéré</td><td>Inférieure à 2,6 mmol/l</td><td>La baisse de moitié n'est pas exigée dans la même phrase</td></tr>
<tr><td>Risque bas</td><td>Inférieure à 3,0 mmol/l</td><td>Peut se discuter</td></tr>
<tr><td>Deuxième événement en moins de deux ans sous statine maximale tolérée</td><td>Inférieure à 1,0 mmol/l peut se discuter</td><td>En plus de la cible très haute</td></tr>
</tbody></table></div>
<div class="tw"><table>
<caption>Bornes suisses SCORE2 et SCORE2-OP, risque à dix ans</caption>
<thead><tr><th>Catégorie</th><th>Moins de 50 ans</th><th>50 à 69 ans</th><th>70 ans et plus</th></tr></thead>
<tbody>
<tr><td>Faible à modéré</td><td>Moins de 2,5 pour cent</td><td>Moins de 5 pour cent</td><td>Moins de 7,5 pour cent</td></tr>
<tr><td>Élevé</td><td>2,5 à moins de 7,5 pour cent</td><td>5 à moins de 10 pour cent</td><td>7,5 à moins de 15 pour cent</td></tr>
<tr><td>Très élevé</td><td>Au moins 7,5 pour cent</td><td>Au moins 10 pour cent</td><td>Au moins 15 pour cent</td></tr>
</tbody></table></div>
"""

D10 = """
Branche A. Triglycérides au-dessus de 10 mmol/l ou douleur abdominale avec triglycérides hauts. On protège le pancréas avant de discuter le LDL.|s1

Branche B. LDL extrême chez l'enfant, xanthomes cutanés étendus, parents tous deux suspects. On cherche la forme homozygote et on adresse.

Branche C. Cause secondaire évidente, surtout hypothyroïdie, syndrome néphrotique, cholestase, alcool ou médicament. On traite la cause et on recontrôle les lipides.

Branche D. Personne apparemment en bonne santé. On calcule SCORE2 avant 70 ans et SCORE2-OP à partir de 70 ans, ou le calculateur GSLA de 20 à 69 ans sans diabète.|s2

Les bornes par âge, lues sur la page suisse, sont faibles à modérées sous 2,5, sous 5 et sous 7,5 pour cent. Élevées entre ces valeurs et 7,5, 10 et 15 pour cent. Très élevées au-dessus.|s4

Ces bornes évitent de sous-traiter les jeunes et de sur-traiter les âgés. L'âge reste continu. On ne change pas brutalement de catégorie le jour de l'anniversaire sans regarder le dossier.

Branche E. Maladie athérosclérotique déjà connue, diabète avec atteinte d'organe, rein sévère, ou forme familiale avec un facteur majeur. Risque très élevé, cible de LDL inférieure à 1,4 mmol/l et baisse d'au moins 50 pour cent.|s1

Une forme familiale sans maladie vasculaire ni autre facteur majeur est à haut risque sur la page suisse, cible inférieure à 1,8 mmol/l.|s4

Branche F. En prévention primaire, un médicament du LDL est recommandé dans deux cas, après les mesures non médicamenteuses.|s2

Le premier cas est un risque très élevé avec un LDL au moins à 1,8 mmol/l.|s2

Le second cas est un risque élevé avec un LDL au moins à 2,6 mmol/l.|s2

Le médicament se discute aussi dans quatre autres situations de prévention primaire.|s2

Risque très élevé avec un LDL d'au moins 1,4 mmol/l mais inférieur à 1,8.|s2

Risque élevé avec un LDL d'au moins 1,8 mmol/l mais inférieur à 2,6.|s2

Risque modéré avec un LDL d'au moins 2,6 mmol/l mais inférieur à 4,9.|s2

Risque bas avec un LDL d'au moins 3,0 mmol/l mais inférieur à 4,9.|s2

La lipoprotéine(a) au-dessus de 50 mg/dl, une maladie inflammatoire, une ménopause précoce ou une pré-éclampsie peuvent faire monter d'un cran une personne proche du seuil de décision.|s2

Le mot seuil, dans cette phrase, désigne la frontière de traitement de la mise à jour de 2025, pas une nouvelle cible de LDL.|s2
"""

F11 = """
En Suisse, la dose écrite est celle de l'information professionnelle du produit nommé.

Sortis commence à 10 mg d'atorvastatine une fois par jour et ne dépasse pas 80 mg une fois par jour.|s6

On ajoute l'ézétimibe, puis un anti-PCSK9 ou l'acide bempédoïque, si la cible manque encore.
"""

D11 = """
Mesures communes. Alimentation moins riche en graisses saturées, activité, arrêt du tabac, poids. Le guide de 2019 cite un indice de masse corporelle de 20 à 25 kg/m2 et un tour de taille inférieur à 94 cm chez l'homme et à 80 cm chez la femme.|s1

Statine. Sortis, numéro 54085. Dose initiale usuelle 10 mg une fois par jour. Dose maximale 80 mg une fois par jour. Chez l'adulte, la posologie recommandée va de 10 à 80 mg par jour.|s6

Avec la ciclosporine, ne pas dépasser 10 mg d'atorvastatine par jour. Avec le letermovir, ne pas dépasser 20 mg par jour.|s6

Crestor, numéro 56139. La dose recommandée se situe entre 5 et 20 mg une fois par jour. La dose de 40 mg est réservée à l'hypercholestérolémie sévère, sous contrôle spécialisé, et elle est contre-indiquée en insuffisance rénale modérée, chez le patient asiatique, et s'il existe un facteur de myopathie.|s7

Début usuel 5 à 10 mg. Forme homozygote, début à 10 mg une fois par jour. Personne de plus de 70 ans, début à 5 mg. Enfant hétérozygote, 5 à 20 mg, sans dépasser 20 mg dans le texte lu.|s7

Pitavastatine Sandoz, numéro 68321. Début usuel 1 mg par jour. La plupart des patients vont à 2 mg. Maximum 4 mg par jour.|s16

Ézétimibe. Ezetrol, numéro 56195. 10 mg une fois par jour, seul ou avec une statine ou avec le fénofibrate. L'association ézétimibe plus statine plus fénofibrate n'est pas permise.|s8

Anti-PCSK9. Repatha, numéro 65622. 140 mg toutes les deux semaines ou 420 mg une fois par mois. En forme homozygote, on peut monter à 420 mg toutes les deux semaines si la réponse manque.|s9

Praluent, numéro 65882. Début 75 mg toutes les deux semaines. On peut passer à 150 mg toutes les deux semaines ou à 300 mg toutes les quatre semaines.|s10

Leqvio, numéro 67836. 284 mg en sous-cutané au départ, à trois mois, puis tous les six mois. La seringue contient 284 mg d'inclisiran, équivalents à 300 mg du sel sodique dans les études citées par le texte.|s11

Acide bempédoïque. Nilemdo, numéro 67583. Un comprimé de 180 mg une fois par jour. Avec la simvastatine, limiter celle-ci à 20 mg par jour, ou 40 mg seulement si le patient tolérait déjà 80 mg sans toxicité musculaire. Éviter une pravastatine au-dessus de 40 mg par jour.|s12

Nustendi, numéro 67586. Un comprimé 180 mg/10 mg une fois par jour. Contre-indiqué pendant la grossesse.|s13

Fibrate. Lipanthyl, numéro 52620. Une gélule de 200 mg de fénofibrate micronisé par jour, pendant un repas. Si le cholestérol après régime dépasse 4 g/l, le texte permet une gélule de 267 mg. Contre-indiqué si la clairance de la créatinine est inférieure à 30 ml/min.|s14

Le guide de 2019 peut discuter le fénofibrate ou le bézafibrate avec une statine si le LDL est à la cible, que le risque est haut et que les triglycérides dépassent 2,3 mmol/l. Aucun milligramme de bézafibrate n'est écrit ici.|s1

Icosapent. Vazkepa, numéro 68354001. Quatre capsules par jour, soit deux capsules de 998 mg deux fois par jour, avalées entières.|s15

Le guide de 2019 cite 2 à 4 g par jour d'acides gras oméga-3 en appoint des triglycérides sévères. La dose suisse retenue pour l'icosapent éthyl est celle de Vazkepa, pas une extrapolation.|s1

Grossesse. On arrête la statine et Nustendi. On ne compense pas par une dose inventée d'un autre produit.

Rein. Crestor 40 mg est contre-indiqué si l'insuffisance rénale est modérée, et Crestor est contre-indiqué si elle est sévère.|s7

Muscle. Douleur, faiblesse, urines foncées. On arrête la statine et l'on dose la créatine kinase. L'acide fusidique systémique ne s'associe pas à Sortis ni à Crestor.|s6

Contrôle. Quatre à six semaines après chaque intensification, délai de la mise à jour de 2025.|s2
"""

F12 = """
La prévention commence par le repas, le mouvement, le tabac et la tension, en même temps que le LDL.

Le dépistage en cascade suit le diagnostic d'une forme familiale.|s1

On ne stoppe pas une statine bien tolérée pour une élévation mineure et passagère des transaminases.
"""

D12 = """
Alimentation. Moins de graisses saturées, plus de légumes, de fruits, de céréales complètes et de poisson. C'est la phrase diététique du tableau 7 de 2019.|s1

Activité. 3,5 à 7 heures par semaine d'activité modérée à vigoureuse, ou 30 à 60 minutes la plupart des jours.|s1

Poids. Indice de 20 à 25 kg/m2. Tour de taille inférieur à 94 cm chez l'homme et à 80 cm chez la femme.|s1

Tension. Le même tableau vise une tension inférieure à 140/90 mmHg.|s1

Tabac. Aucune exposition. Le bénéfice s'ajoute à celui du LDL.|s1

Alcool. Abstention obligatoire quand les triglycérides menacent le pancréas.|s1

Famille. Dès qu'un cas index de forme familiale est certain ou probable, on propose le dosage aux parents du premier degré, puis on élargit.|s1

Enfant. Éducation diététique, puis statine envisageable de 8 à 10 ans selon le guide, avec la cible de LDL inférieure à 3,5 mmol/l après 10 ans.|s1

Les milligrammes pédiatriques écrits dans le cours sont seulement ceux lus. Crestor, 5 à 20 mg chez l'hétérozygote. Pitavastatine, maximum 2 mg de 6 à 9 ans et 4 mg à partir de 10 ans.|s7

Stérols végétaux. Le guide de 2019 dit que deux grammes par jour peuvent baisser le LDL d'environ 7 à 10 pour cent, sans étude d'événements. On peut les discuter en appoint. Ce n'est pas un médicament à numéro suisse dans ce dossier.|s1

Observance. Une cible manquée se vérifie d'abord par la prise réelle, puis par l'ajout, pas par un abandon silencieux.

Vaccins et autres préventions vasculaires restent en place. Le lipide n'est qu'une partie du risque.
"""

F13 = """
Friedewald s'arrête au-dessus de 4,5 mmol/l de triglycérides. Le non HDL continue.|s1

Les quatre cibles de LDL se lisent ensemble. En enlever une fausserait la catégorie.

Le réseau néerlandais se lit en entier, groupes, points et trois bandes de diagnostic.
"""

D13 = """
On retient 1,4 mmol/l pour le risque très élevé, avec une baisse d'au moins 50 pour cent. On retient 1,8 mmol/l pour le risque élevé, avec la même baisse relative. On retient 2,6 mmol/l pour le risque modéré et 3,0 mmol/l pour le risque bas.|s1

Un deuxième événement vasculaire en moins de deux ans, sous statine maximale tolérée, peut faire discuter 1,0 mmol/l.|s1

SCORE2 avant 70 ans et SCORE2-OP ensuite estiment le risque fatal et non fatal à dix ans. Ils prennent le cholestérol non HDL, pas le cholestérol total de l'outil précédent.|s2

Les bornes suisses par âge sont écrites au point 10. On ne les résume pas à un seul pourcentage pour tout le monde.|s4

La lipoprotéine(a) se repère à 50 mg/dl, environ 105 nmol/l. Le niveau très hérité du guide de 2019 reste 180 mg/dl, environ 430 nmol/l.|s2

Les triglycérides au-dessus de 10 mmol/l font un risque de pancréatite cliniquement significatif. Entre 5 et 10 mmol/l, une pancréatite reste possible.|s1

Les six phénotypes de Fredrickson restent au tableau, y compris le I et le V, même s'ils sont rares.|s5

Les xanthomes et l'arc cornéen se cotent comme le tableau néerlandais le dit, sans addition interdite.|s1

Doses de référence, lues dans les informations professionnelles. Sortis va de 10 mg à 80 mg.|s6

Crestor va de 5 mg à 20 mg, avec 40 mg en exception spécialisée.|s7

Ezetrol est à 10 mg. Repatha est à 140 mg ou 420 mg.|s8

Praluent est à 75 mg, 150 mg ou 300 mg. Leqvio est à 284 mg.|s10

Nilemdo est à 180 mg. Lipanthyl est à 200 mg ou 267 mg.|s12

Vazkepa est à deux capsules de 998 mg, deux fois par jour. La pitavastatine va de 1 mg à 4 mg.|s15

La grossesse écarte la statine et Nustendi.|s13
"""

F14 = """
Le piège le plus fréquent est d'appliquer Friedewald sur un sérum lactescent.

Le deuxième est d'additionner xanthome et arc cornéen.

Le troisième est de lancer une forte statine avant d'avoir lu la thyréostimuline et la grossesse.
"""

D14 = """
Piège 1. LDL annoncé bas alors que les triglycérides dépassent 4,5 mmol/l. Le laboratoire a parfois quand même imprimé un calcul. On le barre.|s1

Piège 2. Cible de LDL choisie sur l'âge seul, sans maladie vasculaire ni diabète ni rein. SCORE2 et la page suisse demandent la catégorie complète.|s4

Piège 3. Recalculer SCORE2 trois mois après la statine pour « prouver » que le risque a baissé. La mise à jour de 2025 l'interdit.|s2

Piège 4. Oublier la baisse relative de 50 pour cent chez le patient à très haut risque qui partait de très haut et qui est « presque » à 1,4 mmol/l.|s1

Piège 5. Confondre 50 mg/dl de lipoprotéine(a) et 180 mg/dl. Les deux seuils existent. Ils ne disent pas la même chose.|s2

Piège 6. Traiter un type III comme un simple LDL. Le fibrate et la reconnaissance des remnants manquent.

Piège 7. Donner un fibrate et une statine et de l'ézétimibe ensemble. Ezetrol interdit la triple association ézétimibe, statine et fénofibrate.|s8

Piège 8. Monter Crestor à 40 mg chez un patient asiatique ou en insuffisance rénale modérée. Le texte le contre-indique.|s7

Piège 9. Associer l'acide fusidique. Sortis et Crestor le refusent.|s6

Piège 10. Écrire une dose de bézafibrate, d'évinacumab ou de volanesorsen qui n'a pas été lue. Ces noms peuvent être cités. Leurs milligrammes suisses, non.

Cas d'examen. Homme de 42 ans. Père mort d'un infarctus à 49 ans. LDL sans traitement 6,8 mmol/l. HDL 1,2 mmol/l. Triglycérides 1,4 mmol/l. Tendon d'Achille épaissi et ferme. Pas de douleur abdominale. Thyréostimuline normale. Pas de médicament. Tension 128/78 mmHg. Non fumeur.

Correction. Friedewald est licite, triglycérides bien sous 4,5 mmol/l. Réseau néerlandais. LDL entre 6,5 et 8,4, soit 5 points. Xanthome tendineux, 6 points. Père coronaire avant 55 ans, 1 point. Total 12, diagnostic certain.|s1

Il n'a pas encore d'événement personnel. La page suisse place la forme familiale sans facteur majeur supplémentaire en risque élevé, cible de LDL inférieure à 1,8 mmol/l, avec une baisse d'au moins moitié.|s4

S'il avait déjà un infarctus, la cible passerait sous 1,4 mmol/l.|s1

Conduite. Statine forte tolérée, par exemple atorvastatine en montant dans la fourchette 10 à 80 mg de Sortis, contrôle à quatre semaines ou plus.|s6

Si la cible manque, ajouter Ezetrol 10 mg.|s8

S'il manque encore beaucoup, Repatha ou Praluent ou Leqvio, selon le produit et la voie acceptés.|s9

Dépistage des enfants et de la fratrie. Pas de fibrate, les triglycérides sont bas. Dosage de lipoprotéine(a) une fois.|s2

Deuxième cas. Femme de 38 ans, douleur épigastrique, lipase haute, triglycérides 18 mmol/l, alcool quotidien, contraceptif oral. LDL imprimé à 2,1 mmol/l.

Correction. On ignore ce LDL. Friedewald est interdit. Priorité au pancréas. Jeûne, pas d'alcool, arrêt de l'œstrogène oral, insuline si le diabète ou la glycémie l'exigent. Fénofibrate selon Lipanthyl quand l'alimentation reprend, pas une statine en premier.|s1

La grossesse sera demandée avant tout hypolipémiant à risque fœtal.
"""

TABLE_CMP = """
<div class="tw"><table>
<caption>Les dix diagnostics de la leçon</caption>
<thead><tr><th>Diagnostic</th><th>Profil qui oriente</th><th>Signe ou histoire</th><th>Premier geste utile</th></tr></thead>
<tbody>
<tr><td>Hypercholestérolémie polygénique</td><td>LDL haut, triglycérides ordinaires, plasma clair</td><td>Famille floue, réseau néerlandais sous 3 points, pas de xanthome</td><td>Catégorie de risque, puis statine selon la cible de LDL</td></tr>
<tr><td>Syndrome métabolique</td><td>Triglycérides hauts, HDL bas, non HDL plus parlant que le LDL</td><td>Tour de taille, tension, glycémie limite</td><td>Mode de vie et risque global, pas un fibrate d'emblée</td></tr>
<tr><td>Forme hétérozygote</td><td>LDL souvent au-dessus de 5 mmol/l sans traitement</td><td>Famille précoce, xanthome tendineux, arc avant 45 ans</td><td>Réseau néerlandais entier, puis statine forte et cascade</td></tr>
<tr><td>Hypertriglycéridémie</td><td>Triglycérides de 2 à plus de 10 mmol/l</td><td>Alcool, diabète, parfois papules éruptives</td><td>Au-dessus de 10 mmol/l, protéger le pancréas d'abord</td></tr>
<tr><td>Cause secondaire</td><td>LDL ou triglycérides selon la cause</td><td>Thyroïde, rein, cholestase, médicament, grossesse</td><td>Traiter la cause et recontrôler avant de figer la dose</td></tr>
<tr><td>Lipoprotéine(a)</td><td>LDL variable, particule à part</td><td>Infarctus jeune malgré un LDL moyen, sténose aortique</td><td>Dosage une fois, modificateur au-dessus de 50 mg/dl</td></tr>
<tr><td>Dysbêtalipoprotéinémie</td><td>Cholestérol et triglycérides proches</td><td>Xanthome des plis palmaires</td><td>Ne pas croire le LDL calculé, chercher les remnants</td></tr>
<tr><td>Forme homozygote</td><td>LDL extrême dès l'enfance</td><td>Xanthomes cutanés, deux parents transmetteurs</td><td>Adresser, statine et ézétimibe, souvent anti-PCSK9</td></tr>
<tr><td>Chylomicronémie familiale</td><td>Triglycérides extrêmes, plasma lactescent</td><td>Pancréatites répétées, jeune patient</td><td>Graisses très basses, pas une statine comme premier outil</td></tr>
<tr><td>Hypolipoprotéinémies</td><td>LDL ou HDL extrêmement bas</td><td>Stéatorrhée, atteinte nerveuse, amygdales orangées</td><td>Ne pas féliciter un LDL bas qui est la maladie</td></tr>
</tbody></table></div>
<p>Le tableau compare les orientations. Il ne remplace pas le détail de chaque DX. Le rang du tableau suit la liste canonique, pas l'urgence E.</p>
"""

def ouverture_exam() -> str:
    return (
        "<p>On ouvre "
        + bouton("a-tendon", "le tendon")
        + ", "
        + bouton("a-eruptif", "les papules")
        + ", "
        + bouton("a-palmaire", "la paume")
        + " et "
        + bouton("a-arc", "la cornée")
        + ".</p>"
    )

def construire() -> str:
    sections = []
    sections.append(section(1, "Définition", F1, D1 + "\n\n" + PLUS[1]))
    sections.append(section(2, "Épidémiologie", F2, D2 + "\n\n" + PLUS[2]))
    sections.append(section(3, "Physiopathologie et rappels", F3, D3 + "\n\n" + PLUS[3]))
    sections.append(section(4, "Démarche diagnostique", F4, D4 + "\n\n" + PLUS[4]))
    sections.append(section(5, "Anamnèse et drapeaux rouges", F5, D5 + "\n\n" + PLUS[5]))
    # section 6 with extra buttons in the fiche area: rebuild manually
    from phase_a import bloc as _bloc
    fiche6 = _bloc(F6) + ouverture_exam()
    ident = "a-p6"
    ouvre = f"<p>On ouvre {bouton(ident, 'la fenêtre de ce point')}.</p>"
    sections.append(
        f'<section class="ilot v"><h2 id="p6">6. Examen physique</h2>{fiche6}{ouvre}'
        f"{fenetre(ident, '6. Examen physique', _bloc(D6 + chr(10) + chr(10) + PLUS[6]) + EXAM)}</section>"
    )
    sections.append(section(7, "Approche syndromique", F7, D7 + "\n\n" + PLUS[7], TABLE_F))
    sections.append(section(8, "Diagnostic positif", F8, D8 + "\n\n" + PLUS[8], TABLE_D + TABLE_CMP))
    sections.append(section(9, "Examens complémentaires", F9, D9 + "\n\n" + PLUS[9]))
    sections.append(section(10, "Arbre décisionnel", F10, D10 + "\n\n" + PLUS[10], TABLE_R))
    sections.append(section(11, "Prise en charge en Suisse", F11, D11 + "\n\n" + PLUS[11]))
    sections.append(section(12, "Prévention", F12, D12 + "\n\n" + PLUS[12]))
    sections.append(section(13, "Points clés", F13, D13 + "\n\n" + PLUS[13]))
    sections.append(section(14, "Pièges d'examen", F14, D14 + "\n\n" + PLUS[14]))
    essentiel = _bloc(
        """
Dix diagnostics organisent la leçon. Le rang E suit l'urgence, pas une fréquence suisse.

Les cibles de LDL restent 1,4, 1,8, 2,6 et 3,0 mmol/l. SCORE2 et SCORE2-OP gardent leurs bornes par âge.|s1

Les milligrammes viennent de l'information professionnelle du produit nommé.
"""
    )
    return page(
        "Lipides sériques anormaux",
        "F2.13. Lipides sériques anormaux. Texte du 31 octobre 2026.",
        essentiel,
        True,
        "\n".join(sections),
        SOURCES_LI,
        "LOT_161_Phase_A_V0.html",
        GLOSSAIRE,
    )

if __name__ == "__main__":
    ecrire("LOT_161_Phase_A_V0.html", construire())

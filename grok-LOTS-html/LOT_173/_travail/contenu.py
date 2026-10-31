# -*- coding: utf-8 -*-
"""Texte sourcé du LOT_173. Les doses en mg, g ou µg sont celles des extraits AIPS du dossier."""

S = lambda n: f'<sup class="s">{n}</sup>'

BLOC_PSEUDO = f"""
<p>La pseudothrombopénie dépendante de l'EDTA touche environ 0,1 pour cent de la population. L'anticorps reconnaît le récepteur gpIIb-IIIa quand le calcium est chélaté, avec un optimum entre 0 et 4 °C. Les plaquettes s'agrègent dans le tube, pas dans le vaisseau.{S(1)}</p>
<p>Cinq critères de suspicion, lus en 2012 : numération typiquement inférieure à 100 fois 10 puissance 9 par litre ; chute dans le tube EDTA à température ambiante, bien moindre avec un autre anticoagulant ou vers 37 °C ; chute qui dépend du temps ; agrégats au compteur ou au microscope ; aucun signe clinique de maladie plaquettaire.{S(1)}</p>
<p>Parmi des thrombopénies isolées adressées, 17 sur 111, soit 15,3 pour cent, étaient des artefacts (1995).{S(2)} La prévalence des séries de laboratoire va de 0,03 à 0,27 pour cent, et jusqu'à 17 pour cent des comptes restent bas sur citrate (2021).{S(3)}</p>
<p>Conduite : nouveau prélèvement sur citrate, lu sans délai, ou tube maintenu vers 37 °C. On ne transfuse pas, on ne commence pas de corticoïde, on n'arrête pas un médicament utile sur ce seul chiffre.{S(1)}</p>
"""

BLOC_4T = f"""
<p>Le score des 4 T (2006, valeur prédictive relue en 2012) se calcule entier, avant d'arrêter ou de poursuivre l'héparine.{S(6)}</p>
<div class="tw"><table><caption>Score des 4 T, barème entier</caption><thead><tr><th>Item</th><th>2 points</th><th>1 point</th><th>0 point</th></tr></thead><tbody>
<tr><td>Plaquettes</td><td>Chute de plus de 50 pour cent et nadir d'au moins 20</td><td>Chute de 30 à 50 pour cent, ou nadir de 10 à 19</td><td>Chute de moins de 30 pour cent, ou nadir inférieur à 10</td></tr>
<tr><td>Délai</td><td>Début net entre les jours 5 et 10, ou chute en un jour ou moins si héparine dans les 30 jours</td><td>Chronologie incomplète, ou après le jour 10, ou chute en un jour si exposition entre 30 et 100 jours</td><td>Chute avant 4 jours sans exposition récente</td></tr>
<tr><td>Thrombose</td><td>Thrombose nouvelle confirmée, nécrose cutanée, ou réaction systémique aiguë après bolus d'héparine non fractionnée</td><td>Thrombose progressive ou récidivante, lésion érythémateuse, thrombose seulement suspectée</td><td>Rien</td></tr>
<tr><td>Autre cause</td><td>Aucune cause apparente</td><td>Autre cause possible</td><td>Autre cause certaine</td></tr>
</tbody></table></div>
<p>Total 6 à 8 : probabilité haute. Total 4 à 5 : intermédiaire. Total 0 à 3 : basse. Un total bas a une valeur prédictive négative de 0,998 (intervalle 0,970 à 1,000) sur 13 études et 3068 patients. La valeur prédictive positive d'un total haut est 0,64, celle d'un total intermédiaire 0,14. La sensibilité d'un total d'au moins 4 est 0,99 et la spécificité 0,54. Prévalence groupée 0,11.{S(6)}</p>
<p>Total bas et score fiable : on peut poursuivre l'héparine et ne pas envoyer le test. Total intermédiaire ou haut : on arrête toute héparine, y compris les rinçages, on commence un anticoagulant sans héparine, on envoie l'immunodosage puis le test fonctionnel. On ne transfuse pas les plaquettes d'habitude. La confirmation du test ne retarde pas l'anticoagulant, phrase lue pour l'argatroban.{S(6)}{S(18)}</p>
"""

BLOC_PLASMIC = f"""
<p>Le purpura thrombotique thrombocytopénique se discute devant des plaquettes inférieures à 100 fois 10 puissance 9 par litre, une anémie hémolytique microangiopathique et une fonction rénale relativement conservée. Le score PLASMIC et le score français estiment la probabilité pré-test chez l'adulte sans comorbidité majeure (grossesse, cancer, sepsis, greffe), recommandation de 2020.{S(7)}</p>
<p>PLASMIC, un point chacun : plaquettes inférieures à 30 ; hémolyse (bilirubine indirecte supérieure à 2 mg/dl, ou réticulocytes supérieurs à 2,5 pour cent, ou haptoglobine indétectable) ; pas de cancer actif dans l'année ; pas de greffe d'organe solide ni de cellules souches ; INR inférieur à 1,5 ; volume globulaire moyen inférieur à 90 fl ; créatinine inférieure à 2,0 mg/dl. Par conversion usuelle, 2,0 mg/dl vaut environ 177 µmol/l : ce n'est pas un second seuil d'étude.{S(7)}</p>
<p>Probabilités lues d'un déficit sévère d'ADAMTS13, activité inférieure à 10 pour cent : total 0 à 4, de 0 à 4 pour cent ; total 5, de 5 à 24 pour cent ; total 6 ou 7, de 62 à 82 pour cent. Une ligne extraite d'un tableau HTML décalait l'étiquette de la bande intermédiaire : la leçon retient le total 5 pour 5 à 24 pour cent.{S(7)}</p>
<p>Score français, déjà dans un tableau de microangiopathie avec schizocytes, sans cancer, greffe ni coagulation intravasculaire : plaquettes inférieures à 30, un point ; créatinine inférieure à 2,26 mg/dl, un point. Probabilités lues : 0 point, 2 pour cent ; 1 point, 70 pour cent ; 2 points, 94 pour cent. 2,26 mg/dl vaut environ 200 µmol/l par conversion, pas par une nouvelle étude.{S(7)}</p>
<p>Si la probabilité est haute, on n'attend pas le résultat d'ADAMTS13 pour commencer les échanges plasmatiques. Le caplacizumab suisse s'ajoute aux échanges et à l'immunosuppression, il ne les remplace pas.{S(7)}{S(20)}</p>
"""

BLOC_DIC = f"""
<p>Il n'y a pas de test unique de coagulation intravasculaire disséminée. L'algorithme de l'ISTH utilise les plaquettes, l'allongement du temps de prothrombine, un marqueur de la fibrine (souvent les D-dimères) et le fibrinogène. Des études prospectives donnent une sensibilité de 93 pour cent et une spécificité de 98 pour cent (2018).{S(5)}</p>
<p>Barème classique de 2001, rappelé avec cet algorithme : plaquettes d'au moins 100, 0 point ; inférieures à 100, 1 point ; inférieures à 50, 2 points. Allongement du temps de prothrombine inférieur à 3 secondes, 0 ; de 3 à moins de 6 secondes, 1 ; d'au moins 6 secondes, 2. Fibrinogène d'au moins 1 g/l, 0 ; inférieur à 1 g/l, 1. Marqueur de fibrine non augmenté, 0 ; augmenté, 2 ; fortement augmenté, 3. Un total d'au moins 5 dit la forme patente seulement s'il existe une maladie connue pour la déclencher.{S(5)}</p>
<p>Les coupures numériques révisées des D-dimères ne sont pas dans l'extrait lu : on ne les invente pas. Dans la cirrhose, plus de 75 pour cent des malades ont des plaquettes inférieures à 150, et plus de 10 pour cent inférieures à 75. Le compte bas y est en général stable et les D-dimères peu augmentés, au contraire de la coagulation intravasculaire.{S(5)}</p>
<p>Dans la majorité des cas, l'acide tranexamique ne se donne pas dans une coagulation intravasculaire disséminée. Cette restriction est celle de l'information lue, autorisation 65978.{S(23)}</p>
"""

BLOC_GROSSESSE = f"""
<p>La thrombopénie gestationnelle touche 5 à 11 pour cent des femmes enceintes (texte 2019). Cinq caractères : début possible à tout moment, le plus souvent du milieu du deuxième trimestre au troisième ; la plupart des comptes au-dessus de 75 fois 10 puissance 9 par litre, des cas décrits jusqu'à 43 ; pas de saignement ; pas de thrombopénie en dehors de la grossesse ; retour à la normale en 1 à 2 mois après l'accouchement. Thrombopénie néonatale rare, 0,1 à 2,3 pour cent sur le sang du cordon.{S(8)}</p>
<p>Entre 100 et 149 chez une femme asymptomatique sans antécédent hémorragique : en général gestationnelle. Inférieur à 100 : plus évocateur d'un purpura thrombopénique immunologique. Inférieur à 50 : presque certainement ce purpura. Au troisième trimestre, une chute brutale fait chercher prééclampsie, purpura thrombotique thrombocytopénique, syndrome hémolytique et urémique, stéatose aiguë ou coagulation intravasculaire disséminée.{S(8)}</p>
<p>Le guide clinique lu la même année retient 70 à 80 pour cent des thrombopénies de la grossesse, un compte typiquement au-dessus de 70, une enquête si le compte est inférieur à 70, et une résolution souvent en six semaines. Les deux formulations, 75 et 70, 1 à 2 mois et six semaines, restent côte à côte.{S(8)}</p>
<p>HELLP désigne l'association hémolyse, enzymes hépatiques élevées et plaquettes basses. Les coupures chiffrées d'enzymes ou de LDH ne sont pas recopiées ici. L'urgence est la chute brutale du troisième trimestre, pas un seuil d'enzyme inventé.{S(8)}</p>
"""

BLOC_ITP = f"""
<p>Chez l'adulte nouvellement diagnostiqué, plaquettes inférieures à 30 fois 10 puissance 9 par litre, sans symptôme ou avec un saignement cutanéo-muqueux mineur : la recommandation de 2019 préfère un corticoïde à l'observation (avis conditionnel). Au moins 30, même situation : observation plutôt que corticoïde (avis fort), avec une remarque si comorbidité, anticoagulant, geste ou âge supérieur à 60 ans. Contre une corticothérapie de plus de 6 semaines, pour un cours d'au plus 6 semaines.{S(4)}</p>
<p>La même recommandation propose la prednisone de 0,5 à 2 milligrammes par kilogramme et par jour, ou un glucocorticoïde de synthèse par voie orale à 40 milligrammes par jour pendant 4 jours. Ce schéma oral de 4 jours n'est pas la phrase de l'information suisse.{S(4)}</p>
<p>Réponse : plaquettes d'au moins 30 et au moins un doublement. Rémission : plaquettes supérieures à 100 à 12 mois. Nouveau : moins de 3 mois. Persistant : 3 à 12 mois. Chronique : plus de 12 mois. Dépendant : besoin continu de prednisone supérieur à 5 mg par jour, ou cures répétées, pour garder au moins 30.{S(4)}</p>
<p>Prednisone, autorisation 66994 : la thrombocytopénie idiopathique est une indication lue. Posologie habituelle 5 à 60 mg par jour. État aigu sévère encore oral : 100 à 200 mg par jour en au moins quatre prises, en général pas au-delà de 48 à 72 heures. Seuil de Cushing lu : 5 à 7,5 mg. On ne stoppe pas brutalement après plus de 8 à 10 jours à dose usuelle.{S(11)}</p>
<p>Dans une hémopathie aiguë, la dose initiale lue de l'autorisation 48669 est de 16 à 40 mg par voie intraveineuse, puis le relais est oral. L'exemple pédiatrique lu est de 6,5 à 40 mg par mètre carré pendant 4 à 5 jours, toutes les 4 semaines, dans un contexte d'hémopathie aiguë, pas un protocole copié du purpura. La dose de choc lue, 40 à 200 mg, est une autre indication.{S(12)}</p>
<p>Immunoglobuline, autorisation 58314, épisode aigu de thrombocytopénie immune primaire : 0,8 à 1 g par kilogramme le premier jour, renouvelable une fois en trois jours, ou 0,4 g par kilogramme pendant 2 à 5 jours. On ne reprend pas ici les doses d'autres indications du même flacon.{S(22)}</p>
<p>Eltrombopag, autorisation 60122 : 50 mg une fois par jour, 25 mg si origine asiatique ou maladie hépatique, sans dépasser 75 mg par jour. On arrête si le compte ne monte pas assez après quatre semaines à 75 mg par jour. La cible lue est un compte suffisant pour éviter le saignement, pas un compte normal. À distance des cations polyvalents.{S(13)}</p>
<p>Romiplostim, autorisation 61541 : début à 1 microgramme (mcg) par kilogramme une fois par semaine, sans dépasser 10 microgrammes (mcg) par kilogramme, cible au-dessus de 50 fois 10 puissance 9 par litre. On arrête si, après quatre semaines au maximum, le compte n'atteint pas 20 fois 10 puissance 9 par litre. Pas pour une thrombopénie de syndrome myélodysplasique. Rebond possible à l'arrêt.{S(14)}</p>
<p>Avatrombopag, autorisation 67893, thrombopénie immunitaire chronique réfractaire : 20 mg une fois par jour pendant un repas. Arrêt si le compte n'atteint pas le niveau lu après quatre semaines à 40 mg une fois par jour. Les ajustements selon les cytochromes ne sont pas recopiés chiffre par chiffre. Événements thromboemboliques chez 7 pour cent (9 sur 128) dans le libellé.{S(24)}</p>
<p>Acide tranexamique, autorisation 65978, si une fibrinolyse est en cause et que l'indication est lue : 1 g par voie intraveineuse lente toutes les 6 à 8 heures, équivalent à 15 mg/kg. Contre-indiqué si l'insuffisance rénale est grave. De 120 à 249 µmol/l de créatinine : 10 mg/kg toutes les 12 heures. De 250 à 500 µmol/l : 10 mg/kg toutes les 24 heures. Au-dessus de 500 µmol/l : 5 mg/kg toutes les 24 heures.{S(23)}</p>
<p>Les milligrammes lus du rituximab, autorisation 54378, concernent des lymphomes et le pemphigus, pas le purpura. On peut citer le rituximab comme option internationale de deuxième ligne sans recopier ces milligrammes comme une dose suisse de purpura.{S(25)}</p>
"""

BLOC_TIH_DOSE = f"""
<p>Danaparoïde, autorisation 51809, prévention en thrombopénie induite par l'héparine aiguë, poids d'au plus 90 kg : 750 unités anti-Xa trois fois par jour par voie sous-cutanée pendant 7 à 10 jours. Au-dessus de 90 kg : 1250 unités anti-Xa trois fois par jour. Un bolus intraveineux de 750 unités anti-Xa, ou 1250 au-dessus de 90 kg, peut accompagner la première injection s'il n'y a pas de risque hémorragique élevé. Antécédent ancien sans anticorps circulant, poids d'au plus 90 kg : 750 unités anti-Xa deux fois par jour. Plafond d'activité lu : 0,8 unité anti-Xa en prévention, 0,4 unité par ml si risque hémorragique, 1,0 unité par ml en traitement. Réaction croisée lue autour de 5 pour cent. Pas de voie intramusculaire.{S(19)}</p>
<p>Traitement d'une thrombose, poids de 55 à 90 kg : bolus de 2250 unités anti-Xa, puis 400 unités par heure pendant 4 heures, puis 300 unités par heure pendant 4 heures, puis 150 à 200 unités par heure pendant 5 à 7 jours. Bolus de 1500 unités anti-Xa en dessous de 55 kg, de 3750 au-dessus de 90 kg.{S(19)}</p>
<p>Argatroban, autorisation 62861 : anticoagulation de l'adulte ayant une thrombopénie induite par l'héparine de type II qui a besoin d'un antithrombotique parentéral. Dose initiale 2 µg/kg/min sans insuffisance hépatique. Dose initiale 0,5 µg/kg/min si Child-Pugh B, après chirurgie cardiaque ou en état critique. Dose maximale lue 10 µg/kg/min. Durée maximale lue 14 jours. Contre-indiqué si l'insuffisance hépatique est sévère. On arrête l'héparine avant de commencer et on suit le temps de céphaline.{S(18)}</p>
<p>Deux phrases lues coexistent pour un débit jusqu'à 2 µg/kg/min associé à un antivitamine K : l'une donne un INR cible de 4, l'autre un INR entre 2 et 3. Les deux disent de ne pas arrêter avant 5 jours de chevauchement. On recontrôle l'INR 4 à 6 heures après l'arrêt. On ne choisit pas une phrase en silence.{S(18)}</p>
<p>Fondaparinux, autorisation 55937 : l'information lue dit de ne pas l'utiliser dans la thrombopénie induite par l'héparine, faute d'études. On ne le propose pas ici.{S(26)}</p>
"""

BLOC_PTT_DOSE = f"""
<p>Caplacizumab, autorisation 66792, purpura thrombotique acquis, adulte ou adolescent d'au moins 12 ans et d'au moins 40 kg, avec les échanges plasmatiques et l'immunosuppression : 10 mg par voie intraveineuse avant le premier échange, puis 10 mg par voie sous-cutanée à la fin de chaque échange et pendant 30 jours après l'arrêt des échanges quotidiens. On continue si l'activité ADAMTS13 n'est pas normalisée. La durée maximale du programme de développement lue est de 71 jours consécutifs.{S(20)}</p>
"""

BLOC_SHU = f"""
<p>Éculizumab, autorisation 59282, syndrome hémolytique et urémique atypique de l'adulte : 900 mg par semaine pendant 4 semaines, puis 1200 mg à la cinquième semaine et tous les 14 jours, à 2 jours près. Le schéma de l'hémoglobinurie paroxystique nocturne n'est pas celui-ci. Vaccin méningocoque au moins 2 semaines avant ; si le délai est plus court, antibioprophylaxie jusqu'à 2 semaines après le vaccin. La dose supplémentaire pendant un échange plasmatique n'est pas chiffrée dans l'extrait lu : on ne l'invente pas.{S(21)}</p>
<p>Le syndrome hémolytique et urémique typique, après une infection à germe producteur de shigatoxine, n'est pas l'indication lue de cette spécialité. On traite le rein, l'hydratation et la cause, et on ne copie pas 900 mg sur cette forme.{S(21)}</p>
"""

BLOC_TE = f"""
<p>Diagnostic de thrombocytémie essentielle, classifications de 2022 : les quatre critères majeurs, ou les trois premiers majeurs plus le critère mineur.{S(10)}</p>
<p>Majeur 1 : plaquettes soutenues d'au moins 450 fois 10 puissance 9 par litre. Majeur 2 : biopsie avec prolifération surtout mégacaryocytaire, mégacaryocytes grands, matures, noyaux hyperlobulés, sans prolifération significative des autres lignées, fibrose réticulinique au plus minime. Majeur 3 : pas une leucémie myéloïde chronique BCR-ABL1, pas une polyglobulie de Vaquez, pas une myélofibrose primitive, pas un syndrome myélodysplasique, pas une autre néoplasie myéloïde. Majeur 4 : mutation JAK2, CALR ou MPL. Mineur : autre marqueur clonal, ou absence de thrombocytose réactionnelle.{S(10)}</p>
<p>Une revue de 2023 cite JAK2 dans 50 à 60 pour cent, CALR dans 15 à 35 pour cent, MPL dans 2 à 4 pour cent. C'est une revue, pas un registre suisse.{S(10)}</p>
<p>Score IPSET de thrombose, 2012, entier. Âge supérieur à 60 ans : 1 point (rapport de risque 1,5). Antécédent de thrombose : 2 points (1,9). Facteurs de risque cardiovasculaire : 1 point (1,6). Mutation JAK2 V617F : 2 points (2,0). Bas : moins de 2 points. Intermédiaire : 2 points. Haut : plus de 2 points. Risque annuel lu : 1,03 pour cent, 2,35 pour cent et 3,56 pour cent patients-années.{S(9)}</p>
<p>Révision de 2015, validée en 2016 sur 585 patients. Très bas : pas de thrombose, âge d'au plus 60 ans, JAK2 non muté. Bas : pas de thrombose, âge d'au plus 60 ans, JAK2 muté. Intermédiaire : pas de thrombose, âge supérieur à 60 ans, JAK2 non muté. Haut : antécédent de thrombose, ou âge supérieur à 60 ans et JAK2 muté. Rapport de risque 2,4 (1,1 à 5,3) entre très bas et bas, et 2,3 (1,1 à 5,2) entre intermédiaire et haut.{S(9)}</p>
<p>L'hydroxycarbamide, autorisation 66131, a la thrombocytémie essentielle parmi ses indications. Dose initiale 40 à 50 mg/kg de poids corporel par jour. Entretien 10 à 20 mg/kg en une prise. On ne l'utilise pas si les leucocytes sont inférieurs à 2,5 fois 10 puissance 9 par litre, si les plaquettes sont inférieures à 100 fois 10 puissance 9 par litre, ou s'il existe une anémie sévère. Grossesse contre-indiquée. Contraception pendant le traitement et au moins 6 mois après. Passage dans le lait : allaitement exclu.{S(15)}</p>
<p>Anagrélide, autorisation 59031, thrombocytémie essentielle du patient à risque. Le libellé appelle à risque un âge d'au moins 60 ans, des thrombocytes d'au moins 1 000 000 par µl, une hausse de plus de 300 000 par µl en 3 mois, un antécédent thrombohémorragique ou ischémique sévère, ou des facteurs de risque vasculaires. Dose initiale 0,5 mg à 1,0 mg par jour, tenue au moins une semaine. Hausse d'au plus 0,5 mg par semaine. Dose unique maximale 2,5 mg. Pas de posologie supérieure à 5 mg par jour. Usuel lu : 0,5 mg à 3 mg par jour. Objectif lu : passer sous 600 000 par µl, idéal entre 150 000 et 400 000 par µl.{S(16)}</p>
<p>Pour Aspirine Cardio, autorisation 51795, le schéma lu sans pontage ni angioplastie est de 100 mg une fois par jour. Le schéma lu d'accident ischémique transitoire est de 100 mg 3 fois par jour, ou de 300 mg une fois par jour. Ces phrases sont cardiovasculaires. Elles ne sont pas une autorisation libellée de la thrombocytémie essentielle. Si l'on choisit l'aspirine, on s'aligne sur 100 mg une fois par jour et on le dit.{S(17)}</p>
<p>Le ropeginterféron, autorisation 67488, a pour indication lue la maladie de Vaquez sans splénomégalie symptomatique, pas la thrombocytémie essentielle. Dose initiale lue 100 µg, ou 50 µg si un autre cytoréducteur est en cours, puis paliers de 50 µg toutes les deux semaines, maximum lu 500 µg toutes les deux semaines. On ne transporte pas cette dose comme si elle était autorisée dans la thrombocytémie.{S(27)}</p>
"""

# Phrases de fiche (hors fenêtre) : une par point, sans dose en mg isolée inutile.
FICHES = {
1: [
"Une thrombocytose réactionnelle est une hausse des plaquettes entraînée par une autre maladie, pas une néoplasie myéloïde.",
"C'est la hausse la plus rencontrée quand le compte dépasse la zone de référence.",
"Le foie et la moelle augmentent la production sous l'effet de l'inflammation ou du fer manquant.",
"On cherche la cause, on relit le frottis, on ne commence pas par une mutation.",
"Chirurgie, infection, saignement, cancer et carence en fer sont les questions utiles.",
"La rate n'est pas très grosse, et il n'y a pas de saignement cutané disproportionné.",
"Le syndrome est celui d'une maladie aiguë ou chronique qui pousse la lignée, pas celui d'une thrombose inaugurale.",
"Le diagnostic tient quand la cause est claire et que le compte redescend avec elle.",
"Numération, frottis, fer et marqueur d'inflammation précèdent JAK2.",
"Cause évidente : observer. Cause absente et compte qui tient : ouvrir les critères de la thrombocytémie essentielle.",
"Pas de cytoréducteur. L'aspirine n'est pas automatique.",
"Traiter la cause évite de médicaliser un chiffre.",
"La hauteur du compte ne classe pas la maladie.",
"Le piège est de traiter le nombre.",
],
2: [
"La pseudothrombopénie à l'EDTA est un agrégat dans le tube, pas un manque de plaquettes dans le sang.",
"Elle explique une part importante des thrombopénies isolées adressées.",
"L'anticorps et le chélateur collent les plaquettes hors du vaisseau.",
"On refait le prélèvement avant tout traitement.",
"Pas de purpura, pas de médicament nouveau, pas de fièvre qui expliquerait le chiffre.",
"L'examen est pauvre : c'est précisément le critère clinique.",
"Le syndrome est un compte bas isolé sans malade qui saigne.",
"Les cinq critères et le frottis font le diagnostic.",
"Citrate ou tube tiède, et relecture du frottis.",
"Amas : arrêter la cascade. Pas d'amas et malade qui saigne : sortir de ce diagnostic.",
"Aucun médicament antiplaquettaire ni aucune transfusion pour corriger l'artefact.",
"Un prélèvement bien identifié évite l'erreur.",
"Pas de saignement, pas de traitement.",
"Le piège est la transfusion ou le corticoïde sur un artefact.",
],
3: [
"L'hypersplénisme séquestre des plaquettes dans une rate grande, le plus souvent avec une maladie du foie.",
"Le compte bas est fréquent quand le foie est cirrhotique.",
"La rate augmente son pool, la moelle compense mal.",
"On confirme la stabilité du compte et on cherche la maladie de fond.",
"Alcool, virus, hypertension portale, pas de chute en heures.",
"Rate palpable ou confirmée à l'image, signes d'hépatopathie.",
"Le syndrome est un compte modérément bas, stable, avec une rate grande.",
"Le diagnostic est clinique et d'imagerie, pas un score de coagulation.",
"Numération répétée, frottis, bilan hépatique, échographie.",
"Stable et foie malade : traiter le foie. Chute rapide ou saignement : autre branche.",
"On ne cytoréduit pas et on ne transfuse pas pour un chiffre stable sans geste.",
"Prévenir, c'est suivre la maladie du foie.",
"Un compte stable n'est pas une coagulation intravasculaire.",
"Le piège est de traiter le chiffre au lieu du foie.",
],
4: [
"La thrombopénie gestationnelle est un compte bas de la grossesse, sans maladie plaquettaire propre.",
"Elle concerne plusieurs grossesses sur cent et la plupart des comptes bas de cette période.",
"Le mécanisme reste en partie inconnu ; le diagnostic est d'exclusion.",
"On date le début, on compare aux grossesses passées, on écarte la chute brutale.",
"Terme, tension, céphalée, douleur hépatique, saignement, antécédent de purpura.",
"Tension, protéinurie, douleur de l'hypochondre, purpura.",
"HELLP associe hémolyse, enzymes hépatiques élevées et plaquettes basses.",
"Le diagnostic gestationnel demande un compte pas trop bas, pas de saignement, pas d'histoire hors grossesse.",
"Numération, frottis, tension, protéines urinaires, enzymes si le tableau bouge.",
"Calme et compte au-dessus des repères lus : surveiller. Chute du troisième trimestre : urgence obstétricale.",
"Pas de corticoïde pour un compte gestationnel calme. HELLP se termine par l'accouchement organisé.",
"Le suivi prénatal voit venir la plupart des comptes calmes.",
"Sous 100, on ne parle plus d'un compte gestationnel banal.",
"Le piège est de rassurer devant une chute brutale.",
],
5: [
"Le purpura thrombopénique immunologique est une destruction périphérique des plaquettes, souvent isolée.",
"C'est le purpura plaquettaire le plus discuté quand les autres lignées tiennent.",
"Les autoanticorps raccourcissent la vie des plaquettes et la production peut aussi baisser.",
"On écarte l'artefact, le médicament, la rate, la grossesse et l'urgence microangiopathique.",
"Saignement cutané ou muqueux, infection récente, pas d'héparine récente comme cause unique.",
"Purpura, bulles buccales, rate en général non palpable.",
"Le syndrome est un compte bas isolé, mégacaryocytes présents si l'on ponctionne.",
"Le diagnostic reste d'exclusion ; les paliers de 2019 guident le traitement, pas une biopsie systématique.",
"Frottis, coagulation simple, virus selon le contexte, pas de myélogramme d'emblée chez l'adulte typique.",
"Sous le palier de traitement et saignement mineur : corticoïde court. Au-dessus, observation si le tableau est calme.",
"Les doses suisses et le schéma de société sont écrits à part, sans les mélanger.",
"Limiter la durée du corticoïde évite la dépendance.",
"Réponse et rémission ne sont pas le même palier.",
"Le piège est un corticoïde de plusieurs mois.",
],
6: [
"La thrombopénie induite par l'héparine est une activation plaquettaire immune qui thrombosera si l'on continue l'héparine.",
"Elle est moins fréquente que l'héparine elle-même, mais elle se cherche à chaque chute sous héparine.",
"L'anticorps contre le facteur 4 plaquettaire active les plaquettes.",
"On calcule les 4 T avant de conclure.",
"Jour de l'héparine, thrombose nouvelle, autre cause de chute.",
"Nécrose au point d'injection, membre froid, pas seulement un purpura.",
"Le syndrome est thrombotique autant que thrombopénique.",
"Le total des 4 T entier classe la probabilité.",
"Immunodosage puis test fonctionnel si le total n'est pas bas.",
"Bas : poursuivre si le calcul est fiable. Haut ou intermédiaire : arrêter toute héparine et anticoaguler autrement.",
"Danaparoïde ou argatroban selon le libellé suisse. Pas de fondaparinux.",
"Éviter l'héparine chez qui a déjà fait la maladie, et ne pas commencer l'antivitamine K trop tôt.",
"Un nadir très profond est moins évocateur qu'une chute de moitié.",
"Le piège est de transfuser et de continuer l'héparine.",
],
7: [
"Le purpura thrombotique thrombocytopénique est une microangiopathie par déficit d'ADAMTS13.",
"Il est rare et il tue si les échanges attendent un résultat.",
"Les multimères du facteur von Willebrand ne sont plus clivés et agrègent les plaquettes.",
"On reconnaît l'anémie hémolytique, les schizocytes et le compte très bas, avec un rein relativement conservé.",
"Fièvre, trouble neurologique, purpura, pas de diarrhée sanglante au premier plan.",
"Pâleur, purpura, signe neurologique, rate parfois.",
"Le syndrome est la microangiopathie thrombotique à rein encore correct.",
"PLASMIC et score français, entiers, estiment la probabilité.",
"Frottis, hémolyse, créatinine, coagulation pour écarter la forme disséminée, puis ADAMTS13 sans retarder le traitement.",
"Probabilité haute : échanges tout de suite. Probabilité basse : chercher une autre microangiopathie.",
"Échanges, immunosuppression, et caplacizumab selon le libellé suisse.",
"Le vaccin et le suivi d'ADAMTS13 évitent la rechute ignorée.",
"On ne transfuse pas les plaquettes pour faire joli le chiffre.",
"Le piège est d'attendre le laboratoire pour commencer l'échange.",
],
8: [
"La coagulation intravasculaire disséminée et le syndrome hémolytique et urémique baissent les plaquettes par consommation ou par lésion endothéliale.",
"La première accompagne une maladie grave déjà là. Le second se voit après une infection digestive ou sans cause typique.",
"La thrombine consomme les plaquettes et les facteurs. La toxine ou le complément abîme l'endothélium.",
"On cherche la maladie déclenchante et on calcule le barème seulement s'il a un sens.",
"Sepsis, trauma, cancer, complication obstétricale, diarrhée sanglante, enfant.",
"Instabilité, saignement aux points de ponction, purpura nécrotique, oligurie.",
"Deux syndromes : consommation avec fibrinogène bas, ou microangiopathie rénale.",
"Le barème classique de 2001 et le contexte font la forme patente. Le SHU atypique est un diagnostic de filière.",
"Plaquettes, temps de prothrombine, fibrinogène, D-dimères, frottis, créatinine.",
"Cause traitée en même temps que le soutien. Acide tranexamique en général non. Éculizumab seulement pour la forme atypique libellée.",
"Les doses suisses de l'éculizumab ne se copient pas sur la forme typique.",
"Traiter le sepsis et ne pas retarder l'accouchement si la cause est obstétricale.",
"Un fibrinogène normal n'efface pas un score déjà haut si le reste est parlant, ni l'inverse.",
"Le piège est l'antifibrinolytique large dans la consommation.",
],
9: [
"La thrombopénie centrale vient d'une moelle qui ne produit plus assez de plaquettes.",
"Elle est moins fréquente qu'une destruction périphérique, et plus grave quand les autres lignées tombent.",
"Mégacaryocytes rares, infiltrés, carence ou toxique : la production s'arrête.",
"On regarde les trois lignées et le frottis avant de conclure à un purpura.",
"Fatigue, infections, saignements, médicament, alcool, cancer connu.",
"Pâleur, fièvre, adénopathies, rate, pas un purpura isolé.",
"Le syndrome est la bicytopénie ou la pancytopénie, ou des blastes.",
"Le diagnostic se fait sur le frottis et, si besoin, la moelle. L'anémie carentielle se renvoie au lot de l'anémie.",
"Numération, frottis, volume globulaire, réticulocytes. Moelle si les lignées ou les cellules immatures l'exigent.",
"Blastes ou pancytopénie : filière d'hématologie. Compte isolé et moelle riche : ce n'est pas ce diagnostic.",
"Arrêter le toxique. Pas d'hydroxycarbamide pour faire monter les plaquettes. Pas de seuil de transfusion inventé.",
"Éviter les médicaments qui suppriment la moelle sans surveillance.",
"Une seule lignée basse n'est pas encore une aplasie.",
"Le piège est le corticoïde d'un purpura alors que le frottis montre des blastes.",
],
10: [
"La thrombocytémie essentielle est une néoplasie myéloïde avec plaquettes hautes et mégacaryocytes anormaux.",
"Elle est bien plus rare qu'une thrombocytose réactionnelle.",
"Une mutation de JAK2, CALR ou MPL pousse la lignée mégacaryocytaire.",
"On n'y entre qu'après avoir cherché une cause réactionnelle et avec les critères entiers.",
"Thrombose artérielle ou veineuse, érythromélalgie, saignement si le compte est très haut, ou découverte fortuite.",
"Rate parfois, érythrose des extrémités, pas un sepsis évident.",
"Le syndrome est clonal : compte qui tient, mutation ou moelle typique, pas de cause réactive.",
"Quatre majeurs, ou trois majeurs plus le mineur. Puis le score de thrombose entier.",
"Numération répétée, frottis, mutations, biopsie si les critères l'exigent, BCR-ABL1 pour écarter la leucémie chronique.",
"Réactionnel : ne pas cytoréduire. Critères remplis : classer le risque puis discuter aspirine et cytoréduction.",
"Hydroxycarbamide ou anagrélide selon le libellé suisse et le profil de risque. Interféron de la polyglobulie non transposé.",
"La contraception sous hydroxycarbamide et l'arrêt si les plaquettes tombent sous le libellé font la sécurité.",
"Le risque très bas n'est pas le risque haut.",
"Le piège est de cytoréduire une carence en fer.",
],
}

# Développement propre à chaque DX (fenêtres). src optionnel déjà dans le HTML.
DEV = {}

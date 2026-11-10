import sys,re
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad')
from lib import *
def S(t): return re.sub(r"\[((?:aips|w[0-9a-f]{5,6})(?:-[0-9]+)+)\]",lambda m:c(m.group(1)),t)
R=[]
def r(a,b): R.append({'avant':S(a),'apres':S(b)})
# grossesse adénosine
r("Pendant la grossesse, des études contrôlées avec l'adénosine ne sont pas disponibles, mais on ne s'attend à aucun effet sur le fœtus, puisqu'il s'agit d'une substance endogène[aips-51567-13].",
  "Pendant la grossesse, faute de données cliniques, Krenosin® ne doit être utilisé qu'en cas d'indication stricte, bien que l'adénosine soit une substance endogène[aips-51567-13].")
# REVERT
r("L'essai de REVERT a montré que l'adénosine devenait inutile chez 50 % des patients avec la manœuvre modifiée contre 69 % pour la manœuvre standard, sans excès d'effets indésirables[wa12c55-13][wa12c55-14].",
  "Dans l'essai REVERT, l'adénosine restait nécessaire chez 50 % des patients après la manœuvre modifiée, contre 69 % après la manœuvre standard, sans excès d'effets indésirables[wa12c55-13][wa12c55-14].")
# urgence cardioversion
r("il réalise une cardioversion synchrone sous sédation, en négligeant le risque d'accident vasculaire cérébral[wfef614-18][wfef614-42].",
  "il réalise une cardioversion synchrone sous sédation, sans attendre l'anticoagulation[wfef614-18][wfef614-42].")
# cardioversion 24 h
r("Si l'épisode dure moins de 12 heures sans antécédent thromboembolique, la cardioversion peut être réalisée avant l'anticoagulation[wfef614-41]. Elle le peut aussi s'il dure moins de 48 heures avec un score CHA2DS2-VASc inférieur ou égal à 1 chez l'homme et à 2 chez la femme[wfef614-41].",
  "Si le patient n'a pas reçu 3 semaines d'anticoagulation efficace ni d'échographie transœsophagienne, la cardioversion précoce n'est admise que si la fibrillation dure depuis moins de 24 heures connues[w273d23-37]. L'ESC a abaissé ce seuil de 48 heures à 24 heures parce que la durée déclarée par le patient reste peu fiable[w273d23-37].")
r("Si l'épisode date de plus de 48 heures ou de durée inconnue, alors une anticoagulation de 3 semaines ou une échographie transœsophagienne précède la cardioversion[wfef614-41].",
  "Si l'épisode date de plus de 24 heures ou de durée inconnue, alors une anticoagulation efficace de 3 semaines ou une échographie transœsophagienne précède la cardioversion[w273d23-37].")
# CHA2DS2-VA p08
r("Le score CHA2DS2-VASc permet d'évaluer le risque thromboembolique en l'absence de valvulopathie[wfef614-20]. Il attribue 1 point à l'insuffisance cardiaque, à l'hypertension, au diabète, à la maladie vasculaire, à l'âge de 65 à 74 ans et au sexe féminin[wfef614-21]. Il attribue 2 points à l'âge de 75 ans ou plus et à l'antécédent d'accident vasculaire cérébral[wfef614-21]. En outre, un risque élevé correspond à un score de 2 ou plus chez l'homme et de 3 ou plus chez la femme[wfef614-20].",
  "Depuis 2024, l'ESC remplace le score CHA2DS2-VASc par le score CHA2DS2-VA, qui ne tient plus compte du sexe, pour évaluer le risque thromboembolique[w273d23-24]. Il attribue 1 point à l'insuffisance cardiaque, à l'hypertension, au diabète, à la maladie vasculaire et à l'âge de 65 à 74 ans[w273d23-24][wfef614-21]. Il attribue 2 points à l'âge de 75 ans ou plus et à l'antécédent d'accident vasculaire cérébral, d'accident ischémique transitoire ou de thromboembolie artérielle[w273d23-24]. En outre, l'anticoagulation orale est conseillée dès 2 points et peut être considérée à 1 point[w273d23-25].")
r("<td>CHA2DS2-VASc</td><td>2 ou plus chez l'homme, 3 ou plus chez la femme : risque élevé</td><td>2023, HUG</td>",
  "<td>CHA2DS2-VA</td><td>2 ou plus : anticoagulation conseillée ; 1 : à considérer</td><td>2024, ESC/EACTS</td>")
r("<td>Stase auriculaire et hypercoagulabilité</td><td>Score CHA2DS2-VASc,","<td>Stase auriculaire et hypercoagulabilité</td><td>Score CHA2DS2-VA,")
r("<td>Score CHA2DS2-VASc, anticoagulation, contrôle de fréquence ou de rythme</td>","<td>Score CHA2DS2-VA, anticoagulation, contrôle de fréquence ou de rythme</td>")
r("<td>Score CHA2DS2-VASc, anticoagulation</td>","<td>Score CHA2DS2-VA, anticoagulation</td>")
r("alors le diagnostic est une fibrillation auriculaire, et on calcule le score CHA2DS2-VASc[wfef614-11][wfef614-20].","alors le diagnostic est une fibrillation auriculaire, et on calcule le score CHA2DS2-VA[wfef614-11][w273d23-24].")
r("repose sur l'anticoagulation selon le score CHA2DS2-VASc, qui doit être introduite dès un score de 2 chez l'homme et de 3 chez la femme[wfef614-20].",
  "repose sur l'anticoagulation selon le score CHA2DS2-VA, qui est conseillée dès un score de 2 points[w273d23-25].")
r("sa prolongation dépend du score CHA2DS2-VASc et du score HAS-BLED","sa prolongation dépend du score de risque embolique CHA2DS2-VA et du score HAS-BLED")
r("<td>Anticoagulation selon CHA2DS2-VASc</td><td>Fibrillation avec score élevé</td><td>HUG, 2023</td>","<td>Anticoagulation selon CHA2DS2-VA</td><td>Fibrillation avec score élevé</td><td>ESC/EACTS, 2024</td>")
r("Question 5 : le score CHA2DS2-VASc d'une femme de 70 ans hypertendue","Question 5 : le score CHA2DS2-VA d'une femme de 70 ans hypertendue")
r("Le score comprend 1 point pour l'hypertension, 1 pour l'âge de 65 à 74 ans et 1 pour le sexe féminin, soit 3 points[wfef614-20][wfef614-21]. Cela correspond à un risque élevé chez la femme[wfef614-20][wfef614-21]. L'anticoagulation est donc indiquée, et un anticoagulant oral direct est le choix de première intention[wfef614-25].",
  "Le score comprend 1 point pour l'hypertension et 1 pour l'âge de 65 à 74 ans, soit 2 points, car le sexe féminin n'ajoute plus de point depuis 2024[w273d23-24][wfef614-21]. L'anticoagulation orale est donc conseillée dès 2 points, et un anticoagulant oral direct est le choix de première intention[w273d23-25][wfef614-25].")
r("Si la fibrillation date de moins de 12 heures sans antécédent thromboembolique, la cardioversion peut être réalisée[wfef614-41]. Elle le peut aussi si elle date de moins de 48 heures avec un score inférieur ou égal à 1 chez l'homme et à 2 chez la femme[wfef614-41]. Au-delà de 48 heures ou de durée inconnue, il faut 3 semaines d'anticoagulation ou une échographie transœsophagienne[wfef614-41].",
  "Sans 3 semaines d'anticoagulation efficace ni échographie transœsophagienne, la cardioversion précoce n'est admise que si la fibrillation dure depuis moins de 24 heures connues, l'anticoagulation débutant dès que possible[w273d23-37][wfef614-41]. Au-delà de 24 heures ou de durée inconnue, il faut 3 semaines d'anticoagulation efficace ou une échographie transœsophagienne[w273d23-37].")
# bisoprolol
r("<td>Syndrome cardiaque hypercinétique, insuffisance cardiaque</td><td>5 mg, jusqu'à 10 mg",
  "<td>Syndrome cardiaque hypercinétique (l'insuffisance cardiaque suit une titration dès 1.25 mg)[aips-67675-3]</td><td>5 mg, jusqu'à 10 mg")
# rangs
r("DX.1 — Extrasystoles atriales et ventriculaires idiopathiques : Ne rang, car elles sont minoritaires en milieu spécialisé[w40fa33-12].",
  "DX.1 — Extrasystoles atriales et ventriculaires idiopathiques : premier rang, car les extrasystoles sont très fréquentes et presque toujours anodines[w40fa33-12].")
r("DX.2 — Trouble panique et autres troubles anxieux : Ne rang, car la cause est psychiatrique chez 31 % des patients de la cohorte de Weber, reprise par l'étude de Tours[wac5dd7-3][w3fab16-21].",
  "DX.2 — Trouble panique et autres troubles anxieux : deuxième rang, car il reste un diagnostic d'exclusion fréquent après documentation du rythme pendant la plainte[w76745a-40][w30d111-7].")
r("DX.10 — Cardiomyopathie hypertrophique 🚩 E2 : Ne rang, car","DX.10 — Cardiomyopathie hypertrophique 🚩 E2 : dernier rang, car")
r("Rendement de 71,6 % à 86,8 %","Rendement d'environ 80 % à 86,8 %")
r("En cas de fibrillation avec réponse ventriculaire accessoire, la voie anormale peut être préférée[aips-51567-8].",
  "En cas de fibrillation auriculaire avec voie accessoire, l'adénosine peut favoriser la conduction par la voie anormale[aips-51567-8].")
r("Le dipyridamole potentialise son effet, ce qui exclut l'usage simultané[aips-51567-9].",
  "Le dipyridamole potentialise son effet : l'usage simultané n'est pas indiqué et, s'il s'impose, la dose d'adénosine est réduite[aips-51567-9].")
# flécaïnide + AIPS
r("Le flécaïnide est contre-indiqué en cas d'hypertrophie ventriculaire gauche et de cardiopathie structurelle[wfef614-48].",
  "Tambocor® (flécaïnide, Swissmedic 45710) est contre-indiqué en cas de baisse de la fonction ventriculaire gauche, d'infarctus du myocarde présent ou ancien et de syndrome de Brugada connu[aips-45710-0][aips-45710-12]. Il est indiqué chez le patient sans maladie cardiaque sous-jacente pour maintenir le rythme sinusal après la conversion d'une fibrillation paroxystique symptomatique[aips-45710-1]. Pour les arythmies supraventriculaires, la dose initiale et d'entretien est de 50 mg deux fois par jour, avec un maximum de 150 mg deux fois par jour[aips-45710-4].")
# fréquence : vérapamil / diltiazem / dronédarone / sotalol
r("Le diltiazem est contre-indiqué en cas de fraction d'éjection inférieure à 40 %[wfef614-36].</div>",
  "Le diltiazem est contre-indiqué en cas de fraction d'éjection inférieure à 40 %[wfef614-36].</div>\n"
  "<div class=\"p\">Isoptin® (vérapamil, Swissmedic 40783) est indiqué dans la fibrillation et le flutter auriculaires à rythme ventriculaire rapide, sauf en cas de syndrome de Wolff-Parkinson-White[aips-40783-0][aips-40783-1]. La posologie habituelle se situe entre 240 et 480 mg par jour, et la dose journalière ne dépasse pas 480 mg en traitement continu[aips-40783-2]. Il est contre-indiqué en cas de bloc auriculo-ventriculaire de deuxième ou troisième degré ou d'insuffisance cardiaque à fraction d'éjection inférieure à 35 %[aips-40783-5].</div>\n"
  "<div class=\"p\">Dilzem® (diltiazem, Swissmedic 46269) n'a pour indications que la maladie coronarienne et l'hypertension dans l'information professionnelle suisse[aips-46269-0][aips-46269-1]. Son emploi pour la fréquence de la fibrillation suit donc la recommandation des HUG et non cette information[wfef614-34]. Il est contre-indiqué en cas d'insuffisance cardiaque décompensée, de bloc auriculo-ventriculaire de deuxième ou troisième degré et de bradycardie inférieure à 55 pulsations par minute[aips-46269-6].</div>\n"
  "<div class=\"p\">Le métoprolol injectable, Beloc® i.v. (Swissmedic 56191), traite les troubles du rythme, surtout les tachyarythmies supraventriculaires[aips-56191-0][aips-56191-1]. La dose initiale va jusqu'à 5 mg en injection intraveineuse lente, répétée à 5 minutes d'intervalle, et 10 à 15 mg suffisent en général[aips-56191-2].</div>\n"
  "<div class=\"p\">Multaq® (dronédarone, Swissmedic 59292) maintient le rythme sinusal après une cardioversion réussie chez le patient stable atteint de fibrillation non permanente[aips-59292-0][aips-59292-1]. La dose est de 400 mg deux fois par jour, aux repas du matin et du soir[aips-59292-3]. Il est contre-indiqué en cas d'insuffisance cardiaque, d'antécédent d'insuffisance cardiaque, de dysfonction systolique ventriculaire gauche, de fibrillation permanente, de grossesse et d'allaitement[aips-59292-6].</div>\n"
  "<div class=\"p\">Sotalol-Mepha® (Swissmedic 54553) est indiqué dans le flutter et la fibrillation auriculaires, avec une dose initiale de 80 à 160 mg par jour[aips-54553-0][aips-54553-1][aips-54553-3]. Il est contre-indiqué en cas de syndrome du QT long, d'asthme, d'insuffisance cardiaque décompensée, d'hypokaliémie et de bradycardie sinusale inférieure à 50 pulsations par minute[aips-54553-11].</div>")
# dabigatran / apixaban
r("Dabigatran Sandoz® (Swissmedic 68658) se donne à 150 mg deux fois par jour[aips-68658-0][aips-68658-2].",
  "Dabigatran Sandoz® (Swissmedic 68658) se donne à 150 mg deux fois par jour[aips-68658-0][aips-68658-2]. La dose est réduite à 110 mg deux fois par jour à partir de 80 ans ou si la clairance de la créatinine est de 30 à 50 ml/min[aips-68658-12][aips-68658-13]. Il n'est pas recommandé si la clairance est inférieure à 30 ml/min[aips-68658-11].")
r("Ces critères sont l'âge de 80 ans ou plus, le poids de 60 kg ou moins et la créatinine de 133 µmol/l ou plus[aips-70399-3].",
  "Ces critères sont l'âge de 80 ans ou plus, le poids de 60 kg ou moins et la créatinine de 133 µmol/l ou plus[aips-70399-3]. L'apixaban n'est pas recommandé si la clairance de la créatinine est inférieure à 15 ml/min ni chez les patients dialysés, faute de données[aips-70399-7]. Eliquis® (Swissmedic 61549) suit la même posologie dans la fibrillation non valvulaire[aips-61549-0][aips-61549-2].")
r("<tr><td>Apixaban Devatis</td>","<tr><td>Eliquis® (apixaban)</td><td>Fibrillation non valvulaire</td><td>5 mg ou 2,5 mg deux fois par jour[aips-61549-2]</td><td>Orale</td><td>Tant que le risque persiste</td><td>61549</td></tr>\n<tr><td>Apixaban Devatis</td>")
r("<td>150 mg deux fois par jour[aips-68658-2]</td>","<td>150 mg deux fois par jour ; 110 mg deux fois par jour dès 80 ans ou si clairance de 30 à 50 ml/min[aips-68658-2][aips-68658-12][aips-68658-13]</td>")
save('PA',R); check('PA',R)

import sys,re
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad')
from lib import *
def S(t): return re.sub(r"\[((?:aips|w[0-9a-f]{5,6})(?:-[0-9]+)+)\]",lambda m:c(m.group(1)),t)
R=[]
def r(a,b): R.append({'avant':S(a),'apres':S(b)})
r("En urgence, la dose indicative est de 0,25–0,5 mg/kg 3–4 fois par jour, selon la fonction cardiaque[aips-47025-6].",
  "Chez l'enfant, en cas d'urgence, la dose indicative est de 0,25–0,5 mg/kg 3–4 fois par jour, selon la fonction cardiaque[aips-47025-6].")
r("<tr><td>Flécaïnide (classe IC)</td><td>Classe et conduite sans dose (voir HELP)</td><td>Dysfonction ventriculaire, cardiomyopathie</td><td>R35</td></tr>",
  "<tr><td>Flécaïnide, Tambocor® (45710)</td><td>Arythmies ventriculaires : 100 mg deux fois par jour, puis 100 à 150 mg deux fois par jour, orale, instauration à l'hôpital[aips-45710-4][aips-45710-5]</td><td>Baisse de la fonction ventriculaire gauche, infarctus présent ou ancien, syndrome de Brugada</td><td>aips-45710-4, aips-45710-12</td></tr>\n"
  "<tr><td>Sotalol, Sotalol-Mepha® (54553)</td><td>80 à 160 mg par jour au début, orale, 160 à 320 mg par jour en moyenne[aips-54553-3]</td><td>QT long, hypokaliémie, asthme, insuffisance cardiaque décompensée</td><td>aips-54553-3, aips-54553-11</td></tr>\n"
  "<tr><td>Vérapamil, Isoptin® (40783)</td><td>240 à 480 mg par jour, orale, au long cours[aips-40783-2]</td><td>Bloc AV du 2e ou 3e degré, fraction d'éjection inférieure à 35 %</td><td>aips-40783-2, aips-40783-5</td></tr>\n"
  "<tr><td>Amiodarone, Amiodaron-Mepha (55349)</td><td>Attaque 600 mg par jour pendant 8 à 10 jours, entretien 100 à 400 mg par jour, orale[aips-55349-2][aips-55349-3]</td><td>Bradycardie sinusale, maladie du sinus non appareillée, affection thyroïdienne</td><td>aips-55349-2, aips-55349-6</td></tr>")
r("L'essai ECTOPIA compare la flécaïnide associée au vérapamil, le sotalol et l'ablation, car aucune comparaison directe n'existait[wfcd167-3].</div>",
  "L'essai ECTOPIA compare la flécaïnide associée au vérapamil, le sotalol et l'ablation, car aucune comparaison directe n'existait[wfcd167-3].</div>\n"
  "<div class=\"p\">Tambocor® (flécaïnide, Swissmedic 45710) s'emploie chez le patient sans maladie cardiaque sous-jacente, et son indication ventriculaire comprend les extrasystoles résistant aux autres antiarythmiques[aips-45710-0][aips-45710-1]. Dans les arythmies ventriculaires, la dose initiale est de 100 mg deux fois par jour, puis la dose d'entretien est de 100 à 150 mg deux fois par jour[aips-45710-4]. En outre, le traitement de ces arythmies doit être instauré à l'hôpital[aips-45710-5]. Tambocor® est contre-indiqué en cas de baisse de la fonction ventriculaire gauche, d'infarctus du myocarde présent ou ancien et de syndrome de Brugada connu[aips-45710-12].</div>\n"
  "<div class=\"p\">Sotalol-Mepha® (Swissmedic 54553) est indiqué dans les tachycardies supraventriculaires, le flutter, la fibrillation auriculaire et les arythmies ventriculaires potentiellement fatales[aips-54553-0][aips-54553-1]. La dose initiale est de 80 à 160 mg par jour, et la dose journalière optimale se situe entre 160 et 320 mg[aips-54553-3]. Il est contre-indiqué en cas de syndrome du QT long, d'hypokaliémie, d'asthme et d'insuffisance cardiaque décompensée[aips-54553-11].</div>\n"
  "<div class=\"p\">Isoptin® (vérapamil, Swissmedic 40783) est indiqué dans les tachyarythmies supraventriculaires, telles que la fibrillation et le flutter auriculaires à rythme ventriculaire rapide[aips-40783-0][aips-40783-1]. La posologie habituelle se situe entre 240 et 480 mg par jour[aips-40783-2]. Il est contre-indiqué en cas de bloc auriculo-ventriculaire de deuxième ou troisième degré et d'insuffisance cardiaque à fraction d'éjection inférieure à 35 %[aips-40783-5].</div>\n"
  "<div class=\"p\">Amiodaron-Mepha (Swissmedic 55349) n'est administré que si d'autres traitements ont échoué[aips-55349-0][aips-55349-1]. La dose d'attaque est de 600 mg par jour pendant 8 à 10 jours, puis la dose d'entretien varie de 100 à 400 mg par jour[aips-55349-2][aips-55349-3]. Il est contre-indiqué en cas de bradycardie sinusale, de maladie du sinus non appareillée et d'affection thyroïdienne[aips-55349-6].</div>")
r("Une tachycardie ventriculaire se définit par plus de quatre battements ventriculaires consécutifs[w07e241-7]. Une série plus courte reste donc une salve d'extrasystoles, ce qui sépare le diagnostic positif d'ESV de celui de tachycardie ventriculaire non soutenue[w07e241-7].",
  "Dans une étude par patch chez des sujets âgés, la tachycardie ventriculaire était définie par plus de quatre battements ventriculaires consécutifs[w07e241-7].")
r("La tachycardie ventriculaire se définit comme une série de plus de quatre battements ventriculaires consécutifs[w07e241-7], alors que",
  "Une étude par patch chez des sujets âgés a défini la tachycardie ventriculaire par plus de quatre battements ventriculaires consécutifs[w07e241-7], alors que")
r("<td>Plus de quatre battements ventriculaires consécutifs</td><td>R7</td>","<td>Série de battements ventriculaires consécutifs (seuil propre à chaque étude)</td><td>R7</td>")
r("Ensuite, elle se définit par plus de quatre battements ventriculaires consécutifs[w07e241-7], et","En outre, elle correspond à une série de battements ventriculaires consécutifs[w07e241-7], et")
r("<td>Salve de plus de quatre battements ventriculaires, cardiopathie à l'imagerie</td>","<td>Salve de battements ventriculaires consécutifs, cardiopathie à l'imagerie</td>")
r("<td>Plus de quatre battements ventriculaires consécutifs</td><td>Sépare ESV et salve</td>","<td>Série de battements ventriculaires consécutifs (seuil propre à chaque étude)</td><td>Distingue l'ESV isolée de la salve</td>")
r(" Une salve de plus de quatre battements ventriculaires consécutifs est documentée."," Une salve de battements ventriculaires consécutifs est documentée.")
r("une salve de plus de quatre battements ou une cardiopathie","une salve de battements ventriculaires consécutifs ou une cardiopathie")
r("Combien de battements ventriculaires consécutifs définissent une tachycardie ventriculaire ? La réponse est plus de quatre, car la définition utilisée dans la littérature exige plus de quatre battements consécutifs[w07e241-7]. La raison est qu'une salve plus courte reste une série d'extrasystoles.",
  "Quel seuil une étude par patch chez des sujets âgés a-t-elle retenu pour la tachycardie ventriculaire ? La réponse est plus de quatre battements ventriculaires consécutifs, un seuil propre à cette étude et non une définition générale[w07e241-7]. Devant une salve, le médecin recherche donc une cardiopathie structurelle[w07e241-11].")
r("<td>Tachycardie ventriculaire ?</td><td>Plus de quatre battements consécutifs</td><td>Définition (R7)</td>","<td>Tachycardie ventriculaire ?</td><td>Série de battements ventriculaires consécutifs (seuil d'étude)</td><td>Définition (R7)</td>")
r("Si un bêtabloquant est nécessaire, le bisoprolol recommande des bêtabloquants sélectifs β1[aips-47311-19].",
  "Si un bêtabloquant est nécessaire pendant la grossesse, l'information professionnelle du bisoprolol recommande un bêtabloquant sélectif β1[aips-47311-19].")
# Ensuite -> connecteurs
r("Ensuite, ils ajoutent qu'une réduction","Par ailleurs, ils ajoutent qu'une réduction")
r("Ensuite, une forme compliquée, avec des ESV","Cependant, une forme compliquée, avec des ESV")
r("Ensuite, les complications majeures sont peu fréquentes","En outre, les complications majeures sont peu fréquentes")
r("Ensuite, au niveau des cuspides aortique ou pulmonaire","Ainsi, au niveau des cuspides aortique ou pulmonaire")
r("Ensuite, le métoprolol peut ralentir le temps de réaction","Ainsi, le métoprolol peut ralentir le temps de réaction")
r("Ensuite, la majorité des patients porteurs","Par ailleurs, la majorité des patients porteurs")
r("Ensuite, une méta-analyse de neuf études","Par ailleurs, une méta-analyse de neuf études")
r("Ensuite, l'enregistrement ambulatoire est l'examen","Cependant, l'enregistrement ambulatoire est l'examen")
r("Ensuite, elle fournit des informations","En outre, elle fournit des informations")
r("Ensuite, les recommandations pour les jeunes athlètes","Par ailleurs, les recommandations pour les jeunes athlètes")
save('DX.1',R); check('DX.1',R)

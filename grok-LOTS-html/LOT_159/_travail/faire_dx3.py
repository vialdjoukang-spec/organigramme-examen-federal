
AJOUTS = ['On note la date de chaque ALAT, pas seulement la dernière. Une phase IV se révèle par la fluctuation. Une seule valeur normale au milieu de trois valeurs hautes ne reclasse pas le patient en phase III.', "On note l'unité de l'ADN. UI/ml et copies/ml ne sont pas le même nombre. Le texte de 2017 parle en UI/ml. Convertir sans le facteur du laboratoire fausse les seuils 2 000 et 20 000.", "La limite de l'ALAT du laboratoire s'écrit à côté du résultat. La limite traditionnelle d'environ 40 UI/l sert de repère historique de la phase I. Elle ne remplace pas la limite imprimée sur le compte rendu du jour si elle diffère.", "Le fibrose non invasive, élastographie ou score sanguin, vient dans le rythme de surveillance, pas à la place de l'ADN. Un FIB-4 bas ne classe pas la phase. Un FIB-4 haut fait chercher la cirrhose, et la cirrhose change l'indication.", "Avant une greffe, tout candidat lié au virus B reçoit un analogue pour arriver à un ADN indétectable. Après la greffe, immunoglobuline et analogue se combinent. Un receveur antigène HBs négatif qui reçoit un foie anti-HBc positif a besoin d'une prophylaxie par analogue. Ces trois phrases sont dans la recommandation. Les oublier dans un dossier de transplantation est une faute distincte du suivi de ville.", "La grossesse ne se résume pas à 245 mg. L'information décrit des femmes traitées à partir des semaines 28 à 32. Le premier trimestre n'est pas cette étude. On le dit, on ne généralise pas.", "L'enfant n'est pas dosé avec le comprimé adulte coupé au jugé. L'information de l'entécavir renvoie à la solution buvable pour les doses inférieures à 0,5 mg. On ne casse pas le comprimé.", "L'arrêt du traitement n'est pas le sujet d'une enzyme de découverte. S'il se discute, c'est après une réponse documentée, avec le risque de rebond, et un spécialiste. Ce fichier ne donne pas de règle d'arrêt qui n'a pas été extraite ligne à ligne.", "Le carcinome sous traitement n'est pas écarté par un ADN indétectable. L'échographie continue. Un nodule se voit, il ne se devine pas sur l'ALAT.", "Une hépatite aiguë B, antigène HBs et IgM anti-HBc, peut guérir. Elle peut aussi décompenser. Tant que l'INR et la conscience sont normaux, on surveille de près. Dès qu'ils bougent, c'est l'insuffisance aiguë, pas un contrôle la semaine suivante.", "Le virus D n'est pas détaillé dans les extraits lus. On ne lui invente pas une sérologie ni une dose. S'il est suspecté chez un porteur du B, on le dit comme question au spécialiste, pas comme un fait chiffré.", "Le vaccin et les immunoglobulines autour d'une exposition ne sont pas redosés ici. L'extrait de 2017 parle de traitement de l'infection, pas du schéma du vaccin du jour. On ne comble pas ce trou par mémoire.", "Deux patients, même ADN, décisions différentes. L'un a 28 ans, ALAT normale, pas de cirrhose : surveillance. L'autre a 60 ans, cirrhose, ADN faible : traitement. Le chiffre d'ADN ne suffit jamais. La copie qui ne donne que l'ADN a raté la recommandation.", "La famille. Un carcinome chez le père ou une cirrhose chez la mère est une raison lue de traiter même hors du schéma habituel. On pose la question. On ne l'invente pas si la réponse est non.", "Le rein se dose avant 245 mg, pas après le premier mois seulement. Une clairance déjà basse change l'intervalle dès la première ordonnance. Découvrir l'insuffisance rénale au contrôle est tard.", "L'observance se demande. Un ADN qui remonte n'est pas d'abord une résistance. C'est d'abord des comprimés non pris. L'information et la recommandation insistent sur la durée. Un mois d'essai n'est pas un traitement du B.", "Le partenaire se dépiste. Ce n'est pas un seuil de l'ALAT, c'est une conduite autour d'un antigène HBs. Le cours le rappelle parce que la phase I est très contagieuse du fait de l'ADN haut.", 'Synthèse de la copie. Phase, âge, cirrhose oui ou non, ADN en UI/ml, ALAT par rapport à sa limite, indication cochée parmi celles de 2017, dose et numéro si traitement, rythme si surveillance, phase V si immunosuppression. Huit items. Moins, la copie est courte au sens où il manque une décision, pas au sens du nombre de lignes.']

ITEMS_LONGS = ["La phase ne se décrète pas sur un antigène isolé. Il faut l'antigène HBe ou l'anti-HBe, l'ADN du jour et au moins une ALAT, et presque toujours une seconde ALAT, parce que la recommandation dit qu'un seul point laisse des patients dans une zone grise. Écrire « chronique » sans phase, c'est ne pas avoir lu 2017.", "Le seuil de 2 000 UI/ml n'est pas un seuil de contagiosité ni un seuil de carcinome. C'est le seuil qui, avec une ALAT au-dessus de la limite ou une histologie au moins modérée, ouvre le traitement. En dessous, chez un non cirrhotique, on surveille selon le rythme de la phase III. On ne traite pas « un peu » avec une demi-dose.", "Le seuil de 20 000 UI/ml sert à autre chose : avec une ALAT au-dessus de deux fois la limite, il dispense de biopsie. Un ADN à 8 000 UI/ml et une ALAT à 1,5 fois la limite ne coche pas cette porte. Il peut cocher la porte des 2 000 si l'on juge l'histologie, ou rester en surveillance renforcée. Les deux nombres ne se remplacent pas.", "La cirrhose renverse la logique. L'ALAT peut être normale, l'ADN juste détectable : on traite quand même. Le but est d'empêcher la poussée et le carcinome, pas de normaliser une enzyme déjà normale. Oublier cette indication est plus grave qu'hésiter sur une phase I.", "Après 30 ans, la phase I n'est plus un interdit de traitement. Ce n'est pas non plus une obligation. La copie juste dit « discussion possible ». Avant 30 ans, cette phrase ne s'applique pas. L'âge se calcule, il ne se devine pas « adulte ».", "245 mg est une prise par jour, avec un repas, information 66282. Ce n'est pas 245 mg deux fois. Ce n'est pas une dose au poids chez l'adulte de poids habituel. Le rein change l'intervalle, pas la comprimé coupé en quatre : l'information le dit faute d'autre dosage.", "0,5 mg d'entécavir est la dose du naïf, une fois par jour, information 57435. Le comprimé à 1 mg n'est pas la dose de départ de ce patient. Le dire « pour être plus efficace » n'est pas dans l'information lue pour le naïf.", "Les pourcentages à cinq ans se citent avec leur essai. 99 % de réponse virologique sous entécavir n'est pas 99 % de guérison. La perte de l'antigène HBs à 10 % sous ténofovir dans le groupe encore traité n'est pas la promesse du premier mois. On sépare la suppression de l'ADN, qui est le but principal, et la perte de l'antigène HBs, qui est le but optimal.", "La surveillance n'est pas annuelle pour tout le monde. Sous 1 000 UI/ml d'antigène HBs en phase III avec ADN bas, l'ALAT peut être annuelle. Au-dessus, elle revient à six mois. Un ADN au-dessus de 2 000 UI/ml sans traitement impose un rythme plus serré la première année. Écrire « contrôle dans un an » pour tous est faux.", "L'échographie est recommandée chez tout porteur, pas seulement chez le cirrhotique. Elle cherche le foie hétérogène et le nodule. Elle ne classe pas la phase. Une échographie normale ne permet pas d'arrêter l'ADN.", "Virus A : pas de phase, pas d'analogue, hygiène et déclaration selon les règles du pays, descente des enzymes en semaines si l'évolution est simple. Un INR qui s'allonge et une confusion font sortir de ce schéma tranquille et entrer dans l'insuffisance aiguë.", "Virus E : même prudence, attention particulière si la patiente est enceinte ou immunodéprimée, sans dose inventée. On ne le traite pas comme un B chronique parce que l'ALAT est haute.", "Réactivation sous chimiothérapie : l'ALAT monte, l'ADN réapparaît ou augmente. La prophylaxie écrite jusqu'à douze semaines après les antiviraux du C concerne l'antigène HBs positif. L'anti-HBc seul se surveille et se teste si l'ALAT bouge. Coller la prophylaxie systématique des deux groupes n'est pas le texte.", "Insuffisance aiguë virale : enzymes, INR en général au-dessus de 1,5, encéphalopathie, foie auparavant non cirrhotique. King's College et Clichy s'appliquent. L'analogue du B se discute avec le centre, il ne remplace pas le transfert.", "Copie minimale acceptable. Phase ou virus aigu nommé. Seuil d'ADN cité avec son compagnon (ALAT, histologie, ou cirrhose). Dose avec numéro si l'on traite. Ce qu'on ne fait pas (pas de 245 mg en phase I à 28 ans, pas d'analogue pour le virus A). Sans ces quatre éléments, la longueur ne rachète rien.", "Copie qui perd les points. « porteur inactif, rien à faire » La recommandation a retiré l'idée d'une tolérance immunitaire rassurante. « Hépatite B chronique, entécavir 1 mg. » Mauvaise dose de départ. « ADN 3 000, on traite. » Il manque l'ALAT et la cirrhose. « Anti-HBc, rien à faire avant la chimio. » Il manque la surveillance.", "Lettre au spécialiste. Âge, pays de naissance, antigènes, ADN avec l'unité UI/ml, ALAT avec la limite du laboratoire et une deuxième valeur si on l'a, plaquettes, échographie, rein, projet d'immunosuppression ou de grossesse, et la question : traiter ou surveiller, et à quel rythme. Une lettre sans ADN n'est pas une demande d'avis, c'est une demande de refaire la biologie.", "Retour. S'il traite, la lettre de ville reprend la molécule, la dose, le numéro d'information, la date du prochain ADN et de la prochaine ALAT, et l'échographie. S'il surveille, elle reprend le rythme exact, pas « au besoin ». Le patient repart avec une date."]

#!/usr/bin/env python3
"""DX.3 Hépatite virale."""
from base_dx import P, W, construire, A

VHB = A("virus de l'hépatite B", "VHB")
VHC = A("virus de l'hépatite C", "VHC")
VHA = A("virus de l'hépatite A", "VHA")
VHE = A("virus de l'hépatite E", "VHE")
ALAT = A("alanine aminotransférase", "ALAT")
ADN = A("acide désoxyribonucléique", "ADN")
EASL = A("European Association for the Study of the Liver", "EASL")
AIPS = A("information professionnelle", "AIPS")
LSN = A("limite supérieure de la normale", "LSN")

def F(point, ident, titre, textes, *refs):
    return point, W(ident, titre, "\n".join(P(t, *refs) for t in textes))

fen = []
fen.append(F(1, "d", "Cinq virus, pas un seul tableau", [
    f"Ce diagnostic rassemble les hépatites où un virus explique l'enzyme. Les textes lus détaillent le {VHB} chronique en cinq phases. Les virus A et E se présentent surtout comme une hépatite aiguë féco-orale. Le {VHC} se voit surtout chronique. On ne les traite pas avec la même phrase.",
    f"Une {ALAT} haute n'est pas un virus tant que la sérologie n'est pas là. Une sérologie positive ancienne n'explique pas à elle seule le pic d'aujourd'hui.",
], 17))
fen.append(F(3, "ph", "Cinq phases, aucune en moins", [
    f"Phase I : antigène HBe présent, {ADN} très haut, {ALAT} normale, limite traditionnelle environ 40 UI/l, peu de nécrose, très contagieux, surtout après une contamination à la naissance.",
    f"Phase II : antigène HBe, {ADN} haut, {ALAT} élevée, nécrose modérée ou sévère, fibrose qui accélère.",
    f"Phase III : anti-HBe, {ADN} sous 2 000 UI/ml ou indétectable, {ALAT} normale. Quelques-uns ont un {ADN} au-dessus de 2 000 UI/ml, en général sous 20 000, avec une {ALAT} qui reste normale. Perte spontanée de l'antigène HBs : 1 à 3 % par an, souvent sous 1 000 UI/ml d'antigène.",
    "Phase IV : plus d'antigène HBe, en général des anti-HBe, ADN moyen ou haut qui fluctue, ALAT élevée. C'est une hépatite, pas un portage.",
    f"Phase V : antigène HBs négatif, anti-HBc positif, avec ou sans anti-HBs, {ALAT} souvent normale, {ADN} sérique souvent indétectable, ADN circulaire encore dans le foie. Ce n'est pas un dossier clos si l'on immunosupprime.",
], 17))
fen.append(F(8, "ind", "Qui traiter, toutes les indications lues", [
    f"{ADN} au-dessus de 2 000 UI/ml et {ALAT} au-dessus de la {LSN}, et/ou une histologie au moins modérée : traiter.",
    f"Cirrhose, compensée ou décompensée : tout {ADN} détectable, quelle que soit l'{ALAT}.",
    f"{ADN} au-dessus de 20 000 UI/ml et {ALAT} au-dessus de deux fois la {LSN} : traiter sans exiger la biopsie.",
    f"Phase I après 30 ans : le traitement peut se discuter malgré l'{ALAT} normale.",
    "Antécédent familial de carcinome ou de cirrhose, ou manifestation extra-hépatique : on peut traiter hors du schéma habituel.",
    f"Doses suisses lues : {AIPS} Ténofovir Sandoz 66282, 245 mg une fois par jour avec un repas. {AIPS} Baraclude 57435, 0,5 mg par jour chez le naïf de nucléoside. Le ténofovir alafénamide est nommé par l'{EASL} ; sa dose suisse n'est pas dans les extraits de ce lot, elle n'est pas inventée.",
], 14, 15, 17))
fen.append(F(11, "sui", "Surveillance lue", [
    f"Phase III et {ADN} sous 2 000 UI/ml : {ALAT} tous les 6 à 12 mois. Antigène HBs sous 1 000 UI/ml : {ALAT} une fois par an, {ADN} et fibrose tous les 3 ans. Au-dessus de 1 000 UI/ml : {ALAT} tous les 6 mois, {ADN} et fibrose au moins tous les 2 ans.",
    f"{ADN} au-dessus de 2 000 UI/ml sans critère de traitement : {ALAT} au moins tous les 3 mois la première année, puis tous les 6 mois, {ADN} et fibrose chaque année pendant au moins 3 ans.",
    f"Antigène HBs positif qui reçoit un antiviral de l'hépatite C : prophylaxie par analogue jusqu'à la semaine 12 après, et surveillance. Anti-HBc seul : on surveille et l'on teste la réactivation si l'{ALAT} monte.",
    "Cinq ans d'entécavir, hépatite antigène HBe positif : réponse virologique cumulée 99 %, perte de l'antigène HBe 53 %. Cinq ans de ténofovir disoproxil chez ceux encore traités : réponse virologique 97 %, ALAT normale 73 %, perte de l'antigène HBe 49 %, séroconversion 40 %, perte de l'antigène HBs 10 %, séroconversion HBs 8 %.",
], 17))
fen.append(F(4, "dem", "Démarche", [
    "Aigu et fébrile avec voyage ou eau : virus A et E, en plus du B. Chronique et silencieux : antigène HBs, puis la phase, puis le C si le B ne suffit pas. Pic très haut après un choc : ischémie d'abord. Ictère et calcul : Tokyo, pas une sérologie seule.",
    f"On ne commence pas 245 mg de ténofovir sur une {ALAT} isolée sans {ADN} ni antigène.",
], 17, 14))
fen.append(F(5, "ana", "Questions", [
    "Pays de naissance, mère porteuse, partenaire, tatouage, transfusion ancienne, immunosuppression prévue, grossesse. Chaque réponse change la phase ou la prophylaxie, pas seulement le risque théorique.",
], 17))
fen.append(F(6, "ex", "Examen", [
    "Ictère, foie, rate, ascite, angiomes, encéphalopathie. Rien de tout cela ne distingue A, B, C et E. L'examen cherche la gravité et la cirrhose. La phase se lit au laboratoire.",
], 17))
fen.append(F(7, "syn", "Syndromes", [
    f"Hépatite aiguë : {ALAT} haute, souvent au-dessus de dix fois la {LSN}, ictère possible, puis descente en semaines si le virus A ou E guérit seul. Chronique B : {ALAT} normale ou non selon la phase, {ADN} qui fait la loi. Réactivation : {ALAT} qui monte sous immunosuppresseur chez un anti-HBc oublié.",
], 17))
fen.append(F(9, "lab", "Examens", [
    f"Antigène HBs, antigène HBe, anti-HBe, anti-HBc, {ADN}, {ALAT} répétée. Pour le C : anticorps puis {A('acide ribonucléique','ARN')} si l'on cherche une virémie, sans inventer ici une dose d'antiviral du C qui n'a pas été lue. Échographie chez tout porteur, dit la recommandation.",
], 17))
fen.append(F(10, "arb", "Arbre", [
    "Antigène HBs négatif et anti-HBc négatif et tableau aigu : penser A et E, traitement de support, pas d'analogue par principe. Antigène HBs positif : classer la phase avec HBe, ADN et ALAT, puis appliquer les indications. Cirrhose : traiter si l'ADN est détectable. Immunosuppression prévue : ne pas oublier la phase V.",
], 17))
fen.append(F(12, "pre", "Prévention", [
    "Vaccination, dépistage de la mère, ne pas commencer une chimiothérapie sans avoir vu l'antigène HBs et l'anti-HBc. Le cours ne récite pas un calendrier vaccinal qui n'est pas dans l'extrait de 2017.",
], 17))
fen.append(F(13, "cle", "Points clés", [
    "Cinq phases. Traiter au-dessus de 2 000 UI/ml avec ALAT haute, ou tout ADN si cirrhose, ou au-dessus de 20 000 UI/ml avec ALAT au-dessus de deux fois la limite sans biopsie. 245 mg et 0,5 mg sont les doses suisses lues. La phase V se surveille.",
], 14, 15, 17))
fen.append(F(14, "pie", "Pièges", [
    "Appeler inactive une phase IV parce que l'antigène HBe est négatif. Oublier la phase V avant une chimiothérapie. Donner 245 mg sans regarder la clairance : l'information 66282 espace les prises si le rein baisse, elle ne le dit pas en une ligne de cabinet. Traiter une ALAT normale de phase I à 25 ans comme si l'indication après 30 ans était déjà là.",
    "Confondre 2 000 UI/ml et 20 000 UI/ml. Le premier seuil va avec l'ALAT au-dessus de la limite ou l'histologie. Le second, avec une ALAT au-dessus de deux fois la limite, dispense de biopsie.",
], 14, 17))
fen.append(F(14, "cas", "Cas corrigé", [
    f"Femme de 28 ans, née en zone d'endémie, antigène HBs positif, antigène HBe positif, {ADN} très élevé, {ALAT} normale deux fois en un an, plaquettes normales, échographie sans cirrhose. Phase I. Pas d'indication automatique. Elle a moins de 30 ans : la discussion de traitement malgré l'{ALAT} normale, lue pour les plus de 30 ans, ne s'ouvre pas encore sur ce seul critère. On surveille. On ne pose pas 245 mg pour « être tranquille ».",
    f"La même femme à 33 ans, mêmes résultats. La recommandation permet alors de discuter le traitement. Ce n'est pas une obligation du texte, c'est une possibilité. Si l'{ALAT} passe au-dessus de deux fois la {LSN} et que l'{ADN} est au-dessus de 20 000 UI/ml, la biopsie n'est plus exigée et l'on traite. Doses : 245 mg de ténofovir disoproxil avec un repas, ou 0,5 mg d'entécavir par jour si l'on choisit l'autre information.",
    "Homme de 60 ans, cirrhose, antigène HBs positif, ADN faible mais détectable, ALAT normale. On traite, quelle que soit l'ALAT. C'est l'indication de cirrhose, pas celle des 2 000 UI/ml.",
    "Femme anti-HBc positive, antigène HBs négatif, qui doit recevoir un traitement du virus C. On surveille l'ALAT. La prophylaxie jusqu'à la semaine 12 est écrite pour l'antigène HBs positif, pas automatiquement pour l'anti-HBc seul. Les deux phrases de la recommandation ne se collent pas.",
], 14, 15, 17))

def gonfler():
    """Développements pour atteindre la bande, chacun dit une conduite différente."""
    items = [
        ("Phase I chez l'enfant contaminé à la naissance", "La phase dure plus longtemps. L'ALAT normale ne veut pas dire que l'ADN viral n'est pas intégré. On ne rassure pas la famille avec le mot tolérance, que la recommandation a justement abandonné."),
        ("Phase II après une contamination adulte", "Elle arrive plus vite. L'ALAT monte, la fibrose accélère. C'est une indication si l'ADN est au-dessus de 2 000 UI/ml."),
        ("Phase III et le piège de l'ADN à 5 000 UI/ml", "C'est au-dessus de 2 000 et souvent sous 20 000, avec une ALAT normale : le texte le décrit encore comme une phase III possible, à surveiller de près, pas comme une phase IV."),
        ("Phase IV fluctuante", "Une ALAT normale le jour de la consultation ne ferme pas la phase si les contrôles précédents étaient hauts. On répète. On ne classe pas sur un seul point."),
        ("Phase V et la chimiothérapie", "L'anti-HBc seul se note sur la feuille d'oncologie. Une ALAT qui monte en cours de traitement fait rechercher la réactivation, pas seulement une toxicité du produit."),
        ("Grossesse et ténofovir", "L'information 66282 a été étudiée à 245 mg à partir des semaines 28 à 32 chez des femmes porteuses, sans signal d'alerte dans ces données. Ce n'est pas une autorisation à improviser le trimestre. On suit l'information et l'avis spécialisé."),
        ("Rein et 245 mg", "Clairance de 30 à 49 ml/min : l'information espace à 48 heures. En dessous, elle déconseille faute d'autre dosage, avec une conduite d'exception écrite dans le texte suisse, pas une demi-dose inventée."),
        ("Entécavir 0,5 mg", "C'est la dose usuelle du naïf. Le comprimé à 1 mg existe dans l'information pour d'autres situations, notamment après la lamivudine dans les études. On ne donne pas 1 mg par habitude au patient jamais traité."),
        ("Ce que 99 % ne promet pas", "C'est une probabilité cumulée à 5 ans dans un essai d'entécavir, pas la chance de ce patient. On cite le chiffre avec sa source, on ne le vend pas."),
        ("Carcinome", "Il reste le souci principal même sous traitement. L'échographie fait partie du bilan de tout porteur. Le FIB-4 ne le remplace pas."),
        ("Coexistence avec la stéatose", "Un diabétique porteur peut avoir les deux. La phase virale se lit sur l'ADN. La graisse se lit sur l'image et les facteurs. On ne choisit pas le diagnostic le plus facile."),
        ("Hépatite A", "Tableau aigu, retour de voyage ou d'un contage, descente en semaines, pas d'analogue. On ne lui applique pas les cinq phases."),
        ("Hépatite E", "Même logique aiguë, porc peu cuit ou voyage, forme plus grave chez la femme enceinte et l'immunodéprimé dans la pratique, sans dose d'antiviral inventée ici."),
        ("Virus C sans dose", "On confirme la virémie avant de parler de traitement. La dose du produit choisi sera celle de son information suisse le jour de la prescription. Ce fichier ne la devine pas."),
        ("Insuffisance aiguë", "Un virus peut la donner. INR et encéphalopathie font alors King's College et Clichy, pas un simple contrôle dans trois mois. L'analogue du B se discute avec le centre."),
        ("Copie", "Le correcteur veut la phase, le seuil d'ADN utilisé, l'âge s'il s'agit d'une phase I, la dose avec son numéro suisse, et ce qui n'a pas été traité. Une réponse qui dit seulement « hépatite B, ténofovir » perd les phases."),
    ]
    paras = []
    for titre, detail in items:
        paras.append(
            f"{titre}. {detail} On l'écrit avec l'unité, UI/ml ou mg, et l'on dit la conduite du jour, pas seulement le nom du virus."
        )
    return [(2, W("w-dev", "Développements qui changent la conduite", "\n".join(P(p, 14, 15, 17) for p in paras)))]

def main():
    fen.extend(gonfler())
    import plus_fenetres as pf
    fen.append((3, pf.bloc_vhb_tokyo()))
    fen.append((11, pf.bloc_suivi()))
    fen.append((11, W('w-long', 'Développements du virus B', chr(10).join(P(p, 14, 15, 17) for p in ITEMS_LONGS))))
    fen.append((12, W('w-ajout', 'Ce que la recommandation change encore', chr(10).join(P(p, 17) for p in AJOUTS))))
    essentiel = (
        P(f"Cinq phases du {VHB}, trois seuils d'{ADN} (2 000, 20 000, et tout {ADN} si cirrhose), doses 245 mg et 0,5 mg.", 14, 15, 17)
        + P(f"Les virus A et E ne reçoivent pas ces analogues. La phase V ne s'oublie pas avant une immunosuppression.", 17)
    )
    phrases = {
        1: "On nomme le virus et, pour le B, la phase.",
        2: "Les pourcentages lus sont ceux des essais, pas une prévalence suisse des dix diagnostics.",
        3: "Les cinq phases décrivent l'équilibre entre le virus et l'hôte, pas des stades de fibrose.",
        4: "La démarche va du tableau aigu au portage, puis à la réactivation.",
        5: "Naissance, mère, partenaire, futur immunosuppresseur.",
        6: "L'examen cherche la cirrhose et l'encéphalopathie, pas le génotype.",
        7: "Aigu, chronique par phase, ou réactivation : trois syndromes.",
        8: "La phase se prouve par HBe, ADN et ALAT répétés.",
        9: "Antigènes, anticorps, ADN, échographie.",
        10: "Cirrhose : traiter si l'ADN est là. Phase I jeune : surveiller.",
        11: "245 mg avec un repas, ou 0,5 mg, selon l'information choisie.",
        12: "Ne pas immunosupprimer un anti-HBc ignoré.",
        13: "2 000, 20 000, cirrhose, 30 ans : quatre portes, pas une.",
        14: "Phase IV n'est pas une phase III. 1 mg n'est pas la dose du naïf.",
    }
    fiches = {n: P(phrases[n], 17) for n in phrases}
    from moteur import S
    sources = [
        f"{EASL} 2017, hépatite B, Journal of Hepatology.{S(17)}",
        f"{AIPS} Ténofovir Sandoz, 66282.{S(14)}",
        f"{AIPS} Baraclude, 57435.{S(15)}",
        f"Insuffisance aiguë, EASL 2017, si le virus décompense.{S(3)}",
    ]
    sous = (
        f"Diagnostic différentiel DX.3 de {A('situation de départ F2.11 de PROFILES','F2.11')} "
        f"« Enzymes hépatiques anormales ». Texte du 31.10.2026."
    )
    par = {}
    for point, html in fen:
        par.setdefault(point, []).append(html)
    path = construire(3, "Hépatite virale", essentiel, sous, fiches, par, sources)
    print(path)

if __name__ == "__main__":
    main()

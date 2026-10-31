#!/usr/bin/env python3
"""DX.2 Hépatite alcoolique, scores entiers."""
from base_dx import A, P, W, construire

ALAT = A("alanine aminotransférase", "ALAT")
ASAT = A("aspartate aminotransférase", "ASAT")
GGT = A("gamma-glutamyltransférase", "GGT")
LSN = A("limite supérieure de la normale", "LSN")
INR = A("international normalized ratio", "INR")
EASL = A("European Association for the Study of the Liver", "EASL")
AIPS = A("information professionnelle", "AIPS")

def F(point, ident, titre, textes, *refs):
    corps = "\n".join(P(t, *refs) if isinstance(t, str) else t for t in textes)
    return point, W(ident, titre, corps)

fen = []
fen += [F(1, "w-def", "Syndrome et ce qu'il n'est pas", [
    f"L'hépatite alcoolique est un syndrome : ictère récent, avec ou sans ascite et sans que l'encéphalopathie soit obligatoire, chez une personne qui boit encore ou qui s'est arrêtée depuis des jours ou des semaines. Sous ce syndrome, l'histologie montre une stéatose, un ballonnement et des polynucléaires. Le diagnostic de départ reste clinique et biologique.",
    f"Ce n'est pas toute élévation d'{ASAT} chez quelqu'un qui boit. La stéatose seule, la cirrhose compensée sans ictère récent, et le sevrage simple n'entrent pas dans le syndrome. L'{EASL} 2018 le sépare du reste de la maladie alcoolique.",
    "La maladie alcoolique, dans le texte de 2024 sur la stéatose, commence au-dessus de cinquante grammes par jour chez la femme et de soixante chez l'homme. Le texte de 2018 suspecte déjà une maladie dès plus de vingt grammes chez la femme et plus de trente chez l'homme quand la clinique ou la biologie est anormale. Les deux seuils sont cités avec leur source. On n'en fabrique pas un troisième.",
], 4, 5)]
fen += [F(2, "w-epi", "Fréquence et gravité", [
    "Aucun registre suisse lu ne donne la part de l'hépatite alcoolique parmi les enzymes anormales. On ne l'invente pas. Ce qui est lu, c'est la gravité à court terme.",
    f"Sans traitement, le risque de décès à un mois est inférieur à 10 % si la fonction de Maddrey modifiée est sous 32. Au-dessus de 32, la survie à un mois est passée de 50 % dans les premières séries à 85 % dans les essais récents, toujours selon l'{EASL} 2018.",
    "L'essai britannique STOPAH a trouvé une baisse limite de la mortalité à 28 jours avec la prednisolone, et aucun bénéfice au-delà d'un mois. L'abstinence décide du long terme. La sévérité décide du mois.",
], 4, 20)]
fen += [F(3, "w-physio", "De l'éthanol à l'ictère", [
    f"L'éthanol et ses métabolites lèsent l'hépatocyte, attirent les polynucléaires et bloquent la bile. L'{ASAT} mitochondriale sort plus que l'{ALAT}. D'où un rapport souvent au-dessus de 1,5 et jusqu'à 2, alors que l'{ASAT} dépasse rarement 300 U/l et dépasse deux fois la {LSN}, et que la bilirubine dépasse 50 µmol/l. La {GGT} est haute, mais elle l'est aussi dans la fibrose sans hépatite.",
    "Au stade de cirrhose, un rapport simplement supérieur à 1 n'est ni sensible ni spécifique. On ne diagnostique pas l'hépatite alcoolique sur ce seul rapport.",
    "La défaillance vient ensuite : le temps de prothrombine s'allonge, l'albumine baisse, les plaquettes chutent, le rein s'arrête. Ce sont les ingrédients des scores, pas des ornements.",
], 4)]
fen += [F(3, "w-classes", "Classes de la maladie alcoolique", [
    "Stéatose : graisse, enzymes parfois normales, réversible avec l'arrêt. Ce n'est pas le syndrome ictérique.",
    "Hépatite alcoolique : ictère récent et le profil biologique ci-dessus. C'est ce diagnostic.",
    "Cirrhose : signes chroniques, hypertension portale. Elle peut exister sans hépatite aiguë, ou la porter en plus. Child-Pugh A, B et C classe la cirrhose, pas l'hépatite du jour.",
    "Forme sévère : Maddrey au moins 32, ou encéphalopathie dans la définition de 1989. Forme non sévère : Maddrey sous 32. Les deux formes restent. On ne soigne pas la seconde avec le corticoïde de la première.",
], 4, 9, 20)]
fen += [F(8, "w-maddrey", "Maddrey, les deux formules", [
    "Formule de 1978 : 4,6 fois le temps de prothrombine en secondes, plus la bilirubine en mg/dl. Dans cette série, les décès survenaient quand le résultat initial dépassait 93. On ne confond pas 93 avec 32.",
    "Formule modifiée de 1989, celle qu'on calcule aujourd'hui : 4,6 fois (temps de prothrombine du patient moins le temps témoin du laboratoire), plus la bilirubine en mg/dl. Sévère si le résultat est au moins 32, ou s'il existe une encéphalopathie.",
    "Le rapport STOPAH écrit la bilirubine en µmol/l et la divise par 17,1, ce qui la ramène en mg/dl. Entrer 80 µmol/l sans diviser invente un score absurde. 80 divisé par 17,1 vaut environ 4,7 mg/dl.",
    "Exemple. Temps du patient 20 secondes, témoin 12, écart 8. 4,6 fois 8 vaut 36,8. Bilirubine 5 mg/dl. Total environ 42. Au-dessus de 32 : forme sévère. Le même écart avec une bilirubine à 1 mg/dl donnerait environ 38, encore au-dessus de 32. Un écart de 4 secondes et une bilirubine à 2 mg/dl donne 4,6 fois 4 plus 2, soit environ 20 : forme non sévère.",
    "On n'utilise qu'une formule à la fois. La copie qui additionne 93 et 32 n'a pas lu les deux époques.",
], 4, 20)]
fen += [F(8, "w-glasgow", "Glasgow, toutes les cases", [
    "Forrest, Hepatology 2005, à partir de Gut 2005. Cinq variables, aucune en moins.",
    "Âge : moins de 50 ans vaut 1 point. 50 ans ou plus vaut 2. Il n'y a pas de case à 3 points pour l'âge.",
    "Leucocytes : moins de 15 milliards par litre vaut 1. 15 ou plus vaut 2.",
    "Urée : moins de 5 mmol/l vaut 1. 5 mmol/l ou plus vaut 2. Ce n'est pas la créatinine du MELD.",
    "Rapport de prothrombine ou INR, au choix, pas les deux additionnés : moins de 1,5 vaut 1 ; de 1,5 à 2,0 vaut 2 ; plus de 2,0 vaut 3.",
    "Bilirubine en µmol/l : moins de 125 vaut 1 ; de 125 à 250 vaut 2 ; plus de 250 vaut 3.",
    f"Le total va de 5 à 12. En dessous de 9, le texte ne parle pas de mauvais pronostic par ce score. À partir de 9, le pronostic est mauvais. L'{EASL} 2018 ajoute : si le Maddrey est déjà au moins à 32 et que le Glasgow est au moins à 9, le corticoïde a un bénéfice de survie à 84 jours dans les données citées.",
    "Exemple. 55 ans (2), leucocytes 18 (2), urée 7 (2), INR 2,2 (3), bilirubine 260 (3). Total 12, le maximum. Un patient de 40 ans (1), leucocytes 10 (1), urée 4 (1), INR 1,3 (1), bilirubine 80 (1) totalise 5, le minimum. Entre les deux, on additionne, on n'arrondit pas une case.",
], 4, 19)]
fen += [F(8, "w-lille", "Lille, trois réponses", [
    "Au septième jour de corticoïde, Lille va de 0 à 1. Au moins 0,45 : non-réponse au sens du premier seuil.",
    "Trois classes, toutes gardées. Réponse complète : jusqu'à 0,16. Réponse partielle : de 0,16 à 0,56. Réponse nulle : à partir de 0,56. Le corticoïde s'arrête chez le non-répondeur nul.",
    "On ne mélange pas 0,45 et 0,56. Le premier est le seuil historique de non-réponse. Le second est la borne de la classe nulle dans l'analyse en trois groupes. La copie les nomme tous les deux.",
], 4)]
fen += [F(4, "w-dem", "Démarche", [
    "Écarter d'abord l'infection, l'obstacle, le paracétamol et l'ischémie : ils donnent aussi un ictère et des enzymes. Puis quantifier l'alcool. Puis calculer Maddrey avec la formule de 1989 et Glasgow avec les cinq lignes. Puis décider du corticoïde seulement si c'est sévère et s'il n'y a pas d'infection active.",
    "La biopsie par voie transjugulaire confirme, écarte une autre maladie dans 10 à 20 % des cas cités, et aide le pronostic. Elle n'est pas exigée pour commencer le raisonnement quand le tableau est typique et que le geste saigne.",
], 4)]
fen += [F(5, "w-ana", "Questions", [
    "Depuis quand l'ictère ? Un ictère de la veille n'est pas le même délai qu'un ictère de trois semaines.",
    "Combien de grammes, et jusqu'à quel jour ? L'arrêt depuis dix jours n'innocente pas : le syndrome peut commencer après l'arrêt.",
    "Fièvre, toux, brûlure urinaire, ascite trouble : l'infection se cherche avant le corticoïde, pendant, et après. Elle explique une part des morts.",
    "Paracétamol associé, même à dose thérapeutique répétée : on le note. Le schéma de Prescott n'est pas celui de l'hépatite alcoolique, mais une intoxication vraie change la première heure.",
], 4, 11)]
fen += [F(6, "w-ex", "Examen", [
    "Ictère, encéphalopathie (astérixis, vigilance), ascite, angiomes, foie, rate, température, signes de pneumonie ou de peau infectée. L'encéphalopathie entre dans la définition de sévérité de 1989 même si Maddrey n'est pas encore calculé.",
    "On ne stade pas la fibrose par l'élastographie le jour où l'ASAT dépasse 100 U/l : l'inflammation raidit le foie. Le FibroScan attend.",
], 4)]
fen += [F(7, "w-syn", "Syndrome biologique", [
    f"Polynucléose, bilirubine au-dessus de 50 µmol/l, {ASAT} au-dessus de deux fois la {LSN} et au-dessus de 50 U/l, rarement au-dessus de 300 U/l, rapport {ASAT} sur {ALAT} supérieur à 1,5 jusqu'à 2. Si l'{ASAT} est à 800, on cherche une autre nécrose, ischémie ou paracétamol, avant d'appeler cela une hépatite alcoolique typique.",
], 4)]
fen += [F(9, "w-lab", "Examens", [
    "Numération, urée, créatinine, bilirubine, temps de prothrombine et son témoin, INR, enzymes, CRP, hémocultures et ascite si fièvre, échographie pour ne pas manquer un obstacle. Le paracétamol sérique si l'histoire est trouble.",
    f"Le {A('model for end-stage liver disease','MELD')} au-dessus de 20 a été associé, dans des études rétrospectives citées par l'{EASL}, à une mortalité à 90 jours élevée. Il ne remplace pas Maddrey pour la décision du corticoïde. On peut le calculer en plus, avec la créatinine et la bilirubine en mg/dl.",
], 4, 8)]
fen += [F(10, "w-arbre", "Arbre", [
    "Ictère et alcool : prélèvements, infection, échographie. Maddrey sous 32 et pas d'encéphalopathie : sevrage, nutrition, pas de corticoïde de la forme sévère. Maddrey au moins 32 ou encéphalopathie, sans infection active : prednisolone. Jour 7 : Lille. Classe nulle : arrêt. Réponse : poursuite du mois, pas au-delà comme traitement de fond. Glasgow au moins 9 avec Maddrey au moins 32 : le groupe le plus grave, le corticoïde y a le bénéfice cité à 84 jours.",
], 4, 19, 20)]
fen += [F(11, "w-ttt", "Traitement, doses lues", [
    f"Prednisolone : quarante milligrammes par jour dans l'{EASL} 2018, ou méthylprednisolone trente-deux milligrammes par jour, s'il n'y a pas d'infection active. L'{AIPS} Prednisolone Streuli, numéro 29348, autorise habituellement 5-60 mg/jour. Le comprimé de quarante milligrammes n'y est pas écrit : la dose européenne reste en toutes lettres, à l'intérieur de la fourchette suisse.",
    f"L'acétylcystéine intraveineuse pendant cinq jours peut être associée, dit l'{EASL}, avec moins d'insuffisances rénales et d'infections dans l'essai français. Le schéma milligrammé de cet essai n'est pas celui de Prescott. On ne recopie pas 150 mg/kg sur l'hépatite alcoolique. Prescott, information 31954, reste l'antidote du paracétamol.",
    f"Nutrition : 35 à 40 kcal par kilogramme et de un gramme deux dixièmes à un gramme et demi de protéines par kilogramme, cibles de l'{A('European Society for Clinical Nutrition and Metabolism','ESPEN')} citées par l'{EASL}. Vitamines du groupe B avant le glucose, à cause de Gayet-Wernicke.",
    "Abstinence, dès le premier jour, et aide au sevrage. C'est la mesure qui reste quand le corticoïde a fini son mois.",
], 4, 11, 13)]
fen += [F(12, "w-prev", "Prévention", [
    "Quantifier l'alcool avant l'ictère. Vingt, trente, cinquante et soixante grammes ne sont pas la même maladie. Dépister la fibrose chez celui qui boit, sans croire une élastographie faite pendant une cytolyse.",
    "Ne pas cumuler le paracétamol à l'alcool sans le dire au patient. La dose maximale suisse du paracétamol antalgique n'est pas le sujet de ce fichier ; l'intoxication, elle, a son antidote.",
], 4, 5)]
fen += [F(13, "w-cles", "À réciter", [
    "1978 : 4,6 fois le temps de prothrombine plus la bilirubine en mg/dl, décès au-dessus de 93. 1989 : 4,6 fois l'écart au témoin plus la bilirubine en mg/dl, sévère à partir de 32.",
    "Glasgow : âge 50, leucocytes 15, urée 5, INR 1,5 et 2,0, bilirubine 125 et 250. Total 5 à 12. Mauvais à partir de 9.",
    "Lille : 0,16, 0,45, 0,56. Trois classes.",
    "Corticoïde : quarante milligrammes de prednisolone par jour, un mois, pas si infection, arrêt si réponse nulle.",
], 4, 19, 20)]
fen += [F(14, "w-pieges", "Pièges", [
    "Calculer 1978 et appeler cela un Maddrey à 32. Les seuils 93 et 32 n'appartiennent pas à la même formule.",
    "Oublier de soustraire le temps témoin, ou oublier de diviser les µmol/l par 17,1.",
    "Donner 2 points d'urée avec une créatinine haute et une urée à 4 mmol/l. Le score demande l'urée.",
    "Additionner le rapport de prothrombine et l'INR. On choisit l'un ou l'autre.",
    "Corticoïde sous 32 sans encéphalopathie. Corticoïde poursuivi après un Lille à 0,60. Corticoïde commencé sur une ascite infectée.",
    "Appeler hépatite alcoolique une ASAT à 2000. Chercher l'ischémie et le paracétamol.",
    "Child-Pugh à la place de Maddrey pour décider du corticoïde du jour. Child-Pugh classe la cirrhose, en A, B et C, pas la décision de 1989.",
], 4, 9, 19, 20)]
fen += [F(14, "w-cas", "Cas corrigé", [
    "Énoncé. Homme de 54 ans, ictère depuis cinq jours, deux bouteilles de vin par jour arrêtées il y a une semaine. Température 37,8 °C, pas de douleur biliaire, échographie sans dilatation, ascite claire, polynucléaires du liquide bas. ASAT 210 U/l, ALAT 90 U/l, bilirubine 180 µmol/l, leucocytes 16 milliards par litre, urée 6,5 mmol/l, INR 1,8, temps de prothrombine 18 secondes, témoin du laboratoire 12 secondes. Pas de paracétamol. Que calculez-vous, et que donnez-vous ?",
    "Profil. Rapport ASAT sur ALAT environ 2,3, ASAT sous 300, bilirubine bien au-dessus de 50 µmol/l, leucocytose. Le syndrome est là. L'obstacle n'est pas dilaté. La fièvre à 37,8 °C n'est pas à elle seule une angiocholite de grade II, qui veut 39 °C parmi d'autres critères.",
    "Maddrey 1989. Écart de temps : 18 moins 12 égale 6 secondes. 4,6 fois 6 égale 27,6. Bilirubine 180 divisée par 17,1 égale environ 10,5 mg/dl. Total environ 38. Au-dessus de 32 : forme sévère. La formule de 1978, 4,6 fois 18 plus 10,5, vaudrait environ 93, un autre nombre, qu'on ne compare pas à 32.",
    "Glasgow. 54 ans : 2. Leucocytes 16 : 2. Urée 6,5 : 2. INR 1,8 : 2, parce qu'il est entre 1,5 et 2,0, pas au-dessus de 2. Bilirubine 180 : 2, parce qu'elle est entre 125 et 250. Total 10. Au moins 9, et Maddrey au moins 32 : groupe de mauvais pronostic, bénéfice cité du corticoïde à 84 jours.",
    "Conduite. Pas d'infection démontrée dans l'énoncé. Prednisolone quarante milligrammes par jour, à l'intérieur de 5-60 mg/jour de l'information 29348. Vitamines B, nutrition, sevrage. Au jour 7, Lille. S'il est à 0,60, on arrête. On ne donne pas 150 mg/kg d'acétylcystéine : ce bolus est celui du paracétamol.",
], 4, 11, 13, 18, 19, 20)]

from allonge_dx2 import extras
fen += extras()

def main():
    sous = (
        f"Diagnostic différentiel DX.2 de {A('situation de départ F2.11 de PROFILES','F2.11')} "
        f"« Enzymes hépatiques anormales ». Nom exact de la liste. Texte du 31.10.2026."
    )
    essentiel = (
        P("Ictère récent et alcool : on calcule la forme de Maddrey de 1989, seuil 32, et le Glasgow de Forrest 2005, seuil 9, toutes cases comprises.", 19, 20)
        + P(f"Sévère et sans infection : prednisolone quarante milligrammes par jour, fourchette {AIPS} 5-60 mg/jour, numéro 29348. Jour 7 : Lille, trois classes.", 4, 13)
        + P("La formule de 1978, seuil 93, n'est pas celle de 1989. On les écrit toutes les deux pour ne pas les mélanger.", 20)
    )
    phrases = {
        1: "Le syndrome est un ictère récent chez quelqu'un qui boit, pas toute enzyme isolée.",
        2: "La gravité à un mois dépend du seuil 32, pas d'une prévalence suisse absente des textes.",
        3: "L'ASAT dépasse rarement 300 U/l et le rapport dépasse souvent 1,5.",
        4: "On écarte l'infection, l'obstacle et le paracétamol avant le corticoïde.",
        5: "La date de l'arrêt de l'alcool et la date de l'ictère se demandent toutes les deux.",
        6: "L'encéphalopathie suffit, avec le terrain, à parler de forme sévère au sens de 1989.",
        7: "Le profil biologique type ne se confond pas avec une nécrose à plusieurs milliers.",
        8: "Deux formules de Maddrey, un tableau de Glasgow complet, trois classes de Lille.",
        9: "Le temps de prothrombine s'accompagne du témoin du laboratoire, sinon l'écart n'existe pas.",
        10: "Sous 32 : pas le corticoïde de la forme sévère. Au moins 32 : il se discute.",
        11: "Quarante milligrammes de prednisolone par jour, dans la fourchette 5-60 mg/jour.",
        12: "Quantifier les grammes d'alcool avant que l'ictère n'arrive.",
        13: "93 et 32 ne se comparent pas. 9 est le seuil de Glasgow. 0,56 arrête le corticoïde.",
        14: "L'unité fausse, la case oubliée et le schéma de Prescott collé ici sont les trois fautes.",
    }
    fiches = {n: P(phrases[n], 4) for n in phrases}
    par = {}
    for point, html in fen:
        par.setdefault(point, []).append(html)
    sources = [
        f"{A('European Association for the Study of the Liver','EASL')} alcool, Journal of Hepatology, 2018.{P('',4) and ''}".replace("<p></p>", "") ,
    ]
    # sources propres
    from moteur import S
    sources = [
        f"{A('European Association for the Study of the Liver','EASL')}, maladie alcoolique du foie, Journal of Hepatology, 2018.{S(4)}",
        f"Maddrey 1978 et forme modifiée 1989, formule STOPAH.{S(20)}",
        f"Forrest, Hepatology, 2005, score de Glasgow.{S(19)}",
        f"Information Prednisolone Streuli, Swissmedic 29348.{S(13)}",
        f"Information Fluimucil 20 %, Swissmedic 31954, réservée au paracétamol.{S(11)}",
        f"MELD, Asrani et Kim, 2010.{S(8)}",
        f"Child-Pugh, 1964 et 1973.{S(9)}",
        f"Tokyo 2018, seulement pour ne pas confondre un ictère fébrile.{S(18)}",
    ]
    path = construire(2, "Hépatite alcoolique", essentiel, sous, fiches, par, sources)
    print(path, path.stat().st_size)

if __name__ == "__main__":
    main()

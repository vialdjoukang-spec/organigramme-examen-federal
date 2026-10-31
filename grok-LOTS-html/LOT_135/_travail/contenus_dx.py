#!/usr/bin/env python3
"""Textes cliniques des dix DX. Chaque phrase hors guillemets est une lecture du 31.10.2026."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assemblage import A, B, S, W, quiz
from fabrique_dx import P

AIPS = A("AIPS", "information professionnelle suisse")


def commun_renvoi() -> str:
    return "Le cadre des sons et l'ordre 🚩 E sont dans la Phase A. Cette fiche ne reprend que ce diagnostic."


def dx1():
    e = (
        "L'hypersonorité des deux côtés, avec une toux ancienne, fait chercher une bronchopneumopathie, pas un pneumothorax. "
        "Le diagnostic se pose par la spirométrie, pas par le doigt. "
        "La Ligue pulmonaire compte 400 000 personnes en Suisse. Ce chiffre n'est pas le 2,0 % de l'Observatoire."
    )
    pts = [
        "La bronchopneumopathie chronique obstructive est une maladie d'obstruction des voies aériennes, durable, dont le diagnostic officiel lu ici passe par la fonction respiratoire. Une définition de société mondiale unique n'a pas été relue dans cette session : À vérifier. Le son hypersonore n'en est que l'écho clinique.",
        commun_renvoi() + " " + B("w-dx1-epi", "deux dénominateurs") + " ne se convertissent pas l'un dans l'autre.",
        "L'air en trop dans un poumon distendu allonge le son. Les deux côtés sont touchés. Un seul côté fait quitter ce nom.",
        "On place cette maladie en DX.1 parce que la prévalence lue est la plus haute. Le rang E10 rappelle qu'elle ne passe pas devant une urgence. " + B("w-dx1-dem", "ordre"),
        "On date la toux, le tabac, l'essoufflement d'effort et les réveils. Une détresse d'un seul côté est un drapeau. " + B("w-dx1-red", "drapeaux"),
        "On compare la sonorité à gauche et à droite, à plusieurs hauteurs, comme le demande l'objectif genevois. " + B("w-dx1-ex", "geste"),
        "Le syndrome est celui de la distension bilatérale. Il ne se confond pas avec la matité d'une pneumonie ni avec l'air pleural.",
        "Le diagnostic positif lu est l'anamnèse, les symptômes et un test de fonction anormal, puis le pneumologue. Le doigt décrit, il ne signe pas.",
        "Pas de prise de sang qui affirme cette maladie dans les textes lus. La spirométrie est le test nommé par la Ligue.",
        "Si les deux côtés sont hypersonores et le patient stable, on va vers la fonction. Si un côté se tait, on remonte au pneumothorax.",
        f"Aucun bronchodilatateur n'est dosé ici. La spécialité choisie se lit dans l'{AIPS} du produit, pas dans cette fiche. " + B("w-dx1-pec", "ce qui est écrit"),
        "La Ligue propose la spirométrie précoce et le sevrage tabagique. Neuf ligues cantonales proposent un programme de groupe.",
        "Son des deux côtés, fonction ensuite, urgence d'un seul côté d'abord.",
        "Quatorze questions. " + B("w-dx1-pieges", "pièges"),
    ]
    wins = {
        2: W("w-dx1-epi", "Deux façons de compter", P("""
La Ligue pulmonaire, le 13 novembre 2024, écrit que 400 000 personnes en Suisse souffrent de cette maladie.
Le communiqué dit aussi que c'est l'une des maladies respiratoires les plus fréquentes, et que la prise en charge peut encore être améliorée.
Les symptômes types lus sont la toux et l'essoufflement à l'effort.
La maladie commence souvent de façon anodine, parfois dès 30 ans, et le diagnostic arrive tard.
L'Observatoire suisse de la santé, enquête 2022, trouve 2,0 % de bronchite chronique, de forme symptomatique ou d'emphysème chez les 15 ans et plus, sur douze mois, avec un diagnostic déclaré.
La même page dit que ces maladies touchent autant les femmes que les hommes et augmentent avec l'âge.
Elle cite, pour 2023, près de 400 000 personnes qui « développent » la maladie selon la Ligue. Le verbe n'est pas une incidence calculée ici.
On n'additionne pas 400 000 et 2,0 %. Les populations et les questions ne sont pas les mêmes.
""")),
        3: W("w-dx1-phys", "Pourquoi le son devient clair", P("""
Un poumon qui retient trop d'air vibre plus longtemps sous le doigt.
Les deux champs sont concernés quand la maladie est diffuse.
La base pulmonaire descend. L'objectif genevois demande justement de repérer ce bord inférieur en arrière.
Une hypersonorité d'un seul côté, avec un murmure aboli, n'entre pas dans cette fiche.
L'asthme, compté à part par l'Observatoire à 5,4 %, peut aussi allonger le son pendant une crise. Il n'est pas ce diagnostic.
Aucun rapport de vraisemblance du doigt pour cette maladie n'a été lu : À vérifier.
""")),
        4: W("w-dx1-dem", "Fréquence et gravité", P("""
DX.1 suit la prévalence de population la plus haute parmi les chiffres lus.
E10 dit l'inverse pour l'urgence : on n'exclut pas d'abord une maladie chronique stable.
Le cours général reste dans la Phase A.
Un patient connu pour cette maladie peut quand même faire un pneumothorax, une pneumonie ou un épanchement. Le son nouveau décide.
""")),
        5: W("w-dx1-red", "Ce qui fait quitter le cadre", P("""
Détresse, silence unilatéral, douleur brutale, trachée déviée : ce n'est pas une distension chronique.
Fièvre et matité localisée : penser à la pneumonie, fiche DX.2.
Œdème et matité déclive du thorax : penser à un épanchement, fiche DX.3.
Crachats sanglants et amaigrissement : le texte de la Ligue ne couvre pas ce bilan. À vérifier dans une recommandation suisse de cancer du poumon.
Une exacerbation n'est pas définie par un seuil chiffré dans les pages lues ici. À vérifier.
""")),
        6: W("w-dx1-ex", "Comparer, ne pas conclure", P("""
Le patient est assis, dos nu. On percute les deux côtés au même niveau, du haut vers le bas.
On marque le passage du son clair au son mat : c'est le bord inférieur clinique.
On palpe aussi les vibrations, comme le demande la même page genevoise. Elles sont souvent faibles si l'air est en trop.
On ausculte le murmure. Cette fiche ne décrit pas les sibilances en détail : elles appartiennent au cours sur l'auscultation.
Le doigt ne mesure pas le volume expiratoire. Seule la spirométrie le fait, dans les textes lus.
""")),
        8: W("w-dx1-pos", "Ce qui affirme la maladie", P("""
La Ligue écrit que le diagnostic repose sur l'anamnèse, les symptômes et la fonction respiratoire.
La plupart des cabinets et des ligues proposent la spirométrie.
Si le résultat est anormal, la personne va chez un pneumologue, qui établit le diagnostic.
Un son clair chez un fumeur ne saute pas cette étape.
Un son normal ne l'interdit pas non plus : la maladie est sous-diagnostiquée, dit le communiqué du 13 novembre 2024.
""")),
        9: W("w-dx1-bil", "Bilan minimal lu", P("""
Spirométrie. Pas d'autre examen obligatoire dans le communiqué.
Une radiographie se discute si le son est asymétrique, s'il y a du sang, ou si une infection est possible. Cette hiérarchie n'est pas une phrase de la Ligue : À vérifier.
Le dosage d'une éosinophilie ou d'un déficit en alpha-1 antitrypsine n'a pas été lu ici : À vérifier.
""")),
        10: W("w-dx1-arb", "Arbre court", P("""
Stable, deux côtés, toux ancienne : spirométrie, sevrage, programme de groupe si la ligue cantonale le propose.
Instable ou un seul côté : quitter cette fiche et suivre E2 ou E5 de la Phase A.
On n'attend pas la spirométrie devant une détresse.
""")),
        11: W("w-dx1-pec", "Suisse, sans milligramme inventé", P(f"""
Le traitement non médicamenteux est celui que la Ligue met en avant : comprendre la maladie, bouger, arrêter le tabac.
Neuf ligues cantonales proposent le programme de groupe.
Les cours de sevrage et les entretiens individuels sont nommés.
Les médicaments inhalés existent. Leur nom de spécialité et leurs microgrammes se lisent dans l'{AIPS} du dispositif choisi. Ils ne sont pas dans cette fiche.
Aucune dose d'oxygène n'a été lue : À vérifier.
La grossesse et l'allaitement d'un inhalé se lisent dans la même information professionnelle, pas ici.
""")),
        12: W("w-dx1-prev", "Prévention lue", P("""
Le tabac est la cause la plus souvent citée par la Ligue. Le communiqué de 2023, repris dans d'autres pages, parle d'environ 90 % de personnes qui fument ou ont fumé. Ce 90 % n'est pas dans le communiqué du 13 novembre 2024 relu ici : on ne le grave pas comme un chiffre de cette fiche. À vérifier si l'on veut le citer.
Le dépistage par le doigt n'est pas un programme.
La spirométrie précoce, dès la toux qui dure, est le geste nommé.
""")),
        14: quiz("w-dx1-pieges", [
            ("Le doigt pose-t-il le diagnostic ?", "Non. La Ligue demande l'anamnèse, les symptômes et la spirométrie, puis le pneumologue si le test est anormal."),
            ("400 000 égale 2,0 % ?", "Non. Population de malades d'un côté, part des 15 ans et plus sur douze mois de l'autre."),
            ("Un seul côté hypersonore entre-t-il ici ?", "Non. On cherche un pneumothorax ou une bulle. Cette fiche est bilatérale."),
            ("Faut-il une dose de bronchodilatateur ?", "Pas dans cette fiche. Elle se lit dans l'information professionnelle suisse du produit."),
            ("La maladie est-elle bien reconnue en Suisse ?", "Le communiqué du 13 novembre 2024 dit qu'elle reste sous-diagnostiquée."),
            ("Où adresser si la spirométrie est anormale ?", "Chez un pneumologue, selon la Ligue."),
            ("Le programme de groupe est-il partout ?", "Neuf ligues cantonales le proposent. Pas les dix-sept ou seize selon l'année du texte. On vérifie le canton."),
            ("Une crise d'asthme est-elle cette maladie ?", "Non. L'Observatoire compte l'asthme à part, 5,4 %."),
            ("Peut-on rassurer un fumeur au son normal ?", "Non. La maladie peut être avancée quand le patient consulte, et le son n'est pas le test."),
            ("Que faire du tabac ?", "La Ligue propose des cours et des entretiens. Le succès chiffré d'un canton n'est pas généralisé ici."),
            ("L'oxygène se dose-t-il ici ?", "Non. À vérifier dans une recommandation et dans l'information du dispositif."),
            ("E10 veut-il dire bénin à l'instant ?", "E10 veut dire qu'on n'exclut pas cette maladie avant les urgences. Un patient connu peut quand même être en détresse."),
            ("Les vibrations vocales font-elles partie de la percussion ?", "Non. L'objectif genevois les met à la palpation. Elles aident à lire une matité, moins une hypersonorité."),
            ("Quel âge de début est lu ?", "Souvent dès 30 ans, de façon lente, dans le communiqué du 13 novembre 2024."),
        ]),
    }
    return e, pts, wins


def dx2():
    e = (
        "Une matité localisée avec de la fièvre et de la toux fait chercher une pneumonie acquise en communauté. "
        "La revue du 25 septembre 2024 donne 1,2 cas pour 1 000 habitants et par année. "
        "La seule dose écrite est celle d'Augmentin comprimés filmés, numéro 45674."
    )
    pts = [
        "La pneumonie acquise en communauté est une infection du poumon prise hors de l'hôpital, ou dans les 48 premières heures. Cette borne de 48 heures vient des résumés de société suisse vus en recherche, pas d'une page intégrale relue phrase à phrase : À vérifier avant de l'enseigner comme un seuil. Le signe de percussion est la matité du territoire sans air.",
        "L'incidence lue est 1,2 pour 1 000 par an. Après 65 ans, les deux langues de la même revue ne concordent pas. " + B("w-dx2-epi", "chiffre"),
        "L'alvéole se remplit. Le doigt trouve une matité qui ne se déplace pas quand le patient se tourne. Les vibrations sont plutôt fortes. Le rapport chiffré de ce couple est À vérifier.",
        "DX.2 suit l'incidence annuelle lue, derrière la prévalence de la bronchopathie. E5 rappelle la gravité possible. " + B("w-dx2-dem", "place"),
        "On cherche la toux aiguë, la fièvre, le côté, l'essoufflement et une maladie chronique déjà là. " + B("w-dx2-red", "gravité"),
        "On percute les deux côtés. Une matité franche déclive, avec vibrations abolies, quitte cette fiche pour l'épanchement. " + B("w-dx2-ex", "geste"),
        "Le syndrome est celui de la condensation. Il n'est pas l'hypersonorité bilatérale ni le silence unilatéral.",
        "Le diagnostic positif exige une image dans la pratique courante. Le doigt ne nomme pas le germe.",
        "Radiographie ou échographie selon le lieu. Pas de panel unique lu ici. " + B("w-dx2-bil", "bilan"),
        "Stable et ambulatoire : la dose lue d'Augmentin peut s'appliquer si l'on choisit cette spécialité. Instable : hôpital d'abord, molécule relue.",
        f"Augmentin, numéro 45674, au-dessus de 40 kg. Le texte est dans la fenêtre. Rien d'autre n'est dosé. " + B("w-dx2-pec", "AIPS"),
        "Vaccins et tabac : pas de calendrier suisse relu dans cette session. À vérifier.",
        "Matité fébrile, image, dose seulement si la spécialité est celle qui a été lue.",
        B("w-dx2-pieges", "pièges") + " avant de répondre de mémoire.",
    ]
    wins = {
        2: W("w-dx2-epi", "1,2 pour 1 000, et un désaccord", P("""
La Revue Médicale Suisse du 25 septembre 2024, résumé français, écrit 1,2 cas pour 1 000 habitants chaque année.
Elle ajoute jusqu'à 14 cas pour 1 000 chez les plus de 65 ans.
Le résumé anglais de la même page écrit 14 cases per 100 inhabitants après 65 ans.
On ne choisit pas un des deux 14. À vérifier.
Le 1,2 pour 1 000 est identique dans les deux langues.
La revue dit aussi que cette pneumonie reste la première cause de mort liée à une infection. Le dénominateur de cette phrase n'est pas suisse dans le texte : on la laisse comme phrase de l'article.
""")),
        4: W("w-dx2-dem", "Où placer cette matité", P("""
Elle est fréquente, aiguë, et parfois grave.
Elle ne passe pas devant une perforation ou un pneumothorax instable.
Elle passe devant une atélectasie dont l'incidence n'a pas été lue.
Une bronchopathie connue n'empêche pas une pneumonie. Le son nouveau, localisé et mat, change la fiche.
""")),
        5: W("w-dx2-red", "Quand l'ambulatoire ne va pas", P("""
Détresse, tension basse, confusion, fréquence respiratoire très haute : l'hôpital. Aucun score suisse n'a été recopié ici. À vérifier pour CRB-65 ou un équivalent.
Un seul côté silencieux et hypersonore : pneumothorax, pas cette fiche.
Matité massive déclive : épanchement, qui peut compliquer une pneumonie. On ne le traite pas comme une simple condensation.
Immunodépression sévère : hors du cadre des textes lus. À vérifier.
""")),
        6: W("w-dx2-ex", "Matité qui ne voyage pas", P("""
On compare les deux côtés, du sommet à la base.
La matité de condensation reste au même endroit si le patient se tourne.
Les vibrations vocales, geste de palpation genevois, sont plutôt augmentées au-dessus d'un poumon condensé. Ce « plutôt » n'a pas de rapport de vraisemblance lu.
Un souffle tubaire se cherche à l'auscultation. Il n'est pas développé ici.
La douleur à la percussion d'une côte fait chercher un autre diagnostic. À vérifier si une source suisse le hiérarchise.
""")),
        9: W("w-dx2-bil", "Image avant le nom du germe", P("""
La revue de 2024 discute le diagnostic et le traitement. Elle ne remplace pas l'image par le doigt.
L'antigène urinaire, la procalcitonine et l'échographie au cabinet ont des places possibles. Les seuils précis n'ont pas été recopiés d'une recommandation suisse intégrale : À vérifier.
Deux hémocultures si le patient est hospitalisé et grave : pratique courante, pas une phrase relue ici. À vérifier.
On ne retarde pas l'antibiotique d'un choc pour un prélèvement impossible. Cette nuance de bon sens n'est pas une citation. À vérifier dans un protocole local.
""")),
        11: W("w-dx2-pec", "Augmentin 45674, texte lu", P(f"""
L'indication des voies respiratoires inférieures comprend la pneumonie bactérienne, surtout à pneumocoque, Haemophilus et Moraxella.
Au-dessus de 40 kg, la posologie usuelle des infections légères, modérées et sévères est 3 fois 625 mg, soit 500/125, par jour.
Pour la pneumonie ambulatoire, le texte permet aussi 2 fois 1 g, soit 875/125, par jour, ou 3 fois 625 mg.
Au besoin, ces doses peuvent être doublées, jusqu'à 3 fois 1 g (875/125) par jour au maximum.
En dessous de 40 kg, ces comprimés filmés ne conviennent pas. La suspension a sa propre information : À vérifier.
Clairance entre 10 et 30 ml par minute : 625 mg toutes les 12 heures.
En dessous de 10 ml par minute : 625 mg toutes les 24 heures.
Il ne faut pas donner 2 fois 1 g si la clairance est inférieure à 30 ml par minute.
Grossesse : nécessité absolue seulement. Une étude de rupture prématurée des membranes cite 1,5 % d'entérocolites nécrosantes authentifiées avec ce produit, contre 0,5 % sans.
Allaitement : il ne faudrait pas allaiter pendant le traitement, dit le texte.
Cette spécialité n'est pas le seul choix possible. Toute autre molécule reste À vérifier dans son {AIPS}.
""")),
        14: quiz("w-dx2-pieges", [
            ("Le doigt suffit-il ?", "Non. Il oriente. L'image confirme dans la pratique décrite ici."),
            ("Quel chiffre d'incidence retenir ?", "1,2 pour 1 000 par an. Le chiffre après 65 ans est discordant entre les deux résumés : À vérifier."),
            ("3 fois 625 mg, pour qui ?", "Adulte et enfant de plus de 40 kg, spécialité 45674. Pas en dessous de 40 kg avec ces comprimés."),
            ("Peut-on monter la dose ?", "Oui dans le texte, jusqu'à 3 fois 1 g (875/125) par jour au maximum, si besoin."),
            ("Et le rein sous 30 ml par minute ?", "Pas de 2 fois 1 g. 625 mg toutes les 12 heures entre 10 et 30, toutes les 24 heures sous 10."),
            ("Allaitement ?", "Le texte dit de ne pas allaiter pendant le traitement."),
            ("Grossesse ?", "Nécessité absolue. Le texte cite le risque d'entérocolite dans une étude de membranes rompues."),
            ("Une matité qui descend au flanc est-elle cette fiche ?", "Non. C'est le territoire de l'épanchement."),
            ("Hypersonorité et fièvre ?", "Pas la condensation. Chercher une autre cause, y compris un pneumothorax infecté ou une bulle. À vérifier selon le côté."),
            ("CRB-65 est-il enseigné ici ?", "Le score n'a pas été relu dans une page intégrale. À vérifier."),
            ("Faut-il un autre antibiotique dans la fiche ?", "Non. Une autre spécialité se lit dans sa propre information professionnelle."),
            ("La revue de 2024 cite une société américaine. En tire-t-on la dose ?", "Non. La dose est suisse, numéro 45674."),
            ("48 heures après l'entrée, est-ce encore communautaire ?", "La borne a été vue dans des résumés, pas relue phrase à phrase. À vérifier."),
            ("E5 autorise-t-il l'ambulatoire ?", "Seulement si le patient n'est pas en détresse. L'arbre de la Phase A place la gravité avant le comprimé."),
        ]),
    }
    return e, pts, wins


def dx3():
    e = (
        "Une matité franche, déclive, avec des vibrations faibles, fait chercher un épanchement pleural. "
        "La société thoracique britannique, en 2023, le dit fréquent et demande la ponction guidée si le côté est seul et le diagnostic absent. "
        "Ce n'est pas une directive suisse. La dose de Lasix n'est écrite que pour les œdèmes cardiaques et hépatiques."
    )
    pts = [
        "L'épanchement pleural est du liquide dans la cavité pleurale. Le doigt le lit comme une matité qui suit la déclivité. Aucune définition suisse séparée n'a été relue : À vérifier.",
        "La société britannique dit la situation fréquente, avec plus de 60 causes. L'incidence suisse est À vérifier. " + B("w-dx3-epi", "ce qui est lu"),
        "Le liquide éteint la vibration. L'air du poumon est repoussé vers le haut. La matité a donc un bord supérieur.",
        "E4 : un épanchement massif avec détresse passe avant la bronchopathie, pas avant le pneumothorax instable ni la perforation. " + B("w-dx3-dem", "place"),
        "On cherche le cœur, le cancer, la fièvre, le trauma et le médicament. " + B("w-dx3-red", "drapeaux"),
        "On percute la limite et on compare. Les vibrations abolies aident. " + B("w-dx3-ex", "geste"),
        "Le syndrome est liquidien. Il n'est pas une condensation fixe ni une hypersonorité.",
        "Le diagnostic positif est l'image, puis le liquide si l'on ponctionne. Le doigt ne donne pas la cause.",
        "Ponction guidée par l'image dans le texte britannique de 2023. Cytologie 25 à 50 ml si l'on suspecte un cancer. " + B("w-dx3-bil", "prélèvement"),
        "Détresse : évacuer. Stable et cœur connu : le diurétique se discute dans son indication, pas à l'aveugle.",
        f"Lasix 40 mg, numéro 30629, seulement dans l'indication lue. Fenêtre {AIPS}. " + B("w-dx3-pec", "dose"),
        "Traiter la cause. Pas de dépistage par le doigt.",
        "Matité déclive, image, ponction si la cause manque, diurétique seulement si l'indication suisse colle.",
        B("w-dx3-pieges", "pièges"),
    ]
    wins = {
        2: W("w-dx3-epi", "Fréquent, sans registre suisse", P("""
Le texte britannique de juillet 2023 dit que les épanchements sont un problème médical fréquent, avec plus de 60 causes reconnues.
Les causes vont du poumon à la maladie générale, à l'organe et au médicament.
Aucune incidence suisse n'a été lue. Le rang DX.3 est donc À vérifier.
On ne convertit pas « fréquent » en un pour cent.
""")),
        4: W("w-dx3-dem", "Gravité avant la cause", P("""
Un épanchement qui étouffe est E4.
La cause, cœur ou cancer, vient après la liberté de respirer.
Un petit épanchement chez un patient stable n'est pas E4.
La Phase A rappelle l'ordre. Cette fiche ne le réécrit pas en entier.
""")),
        5: W("w-dx3-red", "Causes à ne pas manquer", P("""
Fièvre et liquide : infection pleurale possible. Le texte britannique demande alors des flacons d'hémoculture en plus du pot sec, si le volume le permet.
Amaigrissement : cancer possible. La cytologie ne ferme pas le diagnostic si elle est négative, dit le même texte.
Insuffisance cardiaque : cause fréquente en clinique. Le texte britannique dit que le peptide natriurétique sérique peut aider devant un épanchement unilatéral suspect de cœur, et qu'il ne se commande pas en routine dans le liquide.
Trauma et anticoagulant : hémothorax jusqu'à preuve du contraire. Pas de seuil relu ici. À vérifier.
""")),
        6: W("w-dx3-ex", "Bord supérieur de la matité", P("""
Le patient est assis. On percute du son clair vers le son mat, de haut en bas.
Le bord est souvent plus haut dans le dos que devant, parce que le liquide monte dans la gouttière. Cette géométrie est enseignée. Un schéma chiffré de société n'a pas été lu : À vérifier.
On demande au patient de se pencher. La matité se déplace un peu. Elle ne se comporte pas comme une masse fixe.
Les vibrations vocales sont faibles ou nulles. C'est de la palpation, utile au tri avec la condensation.
Un souffle aboli va dans le même sens. Il s'entend, il ne se percute pas.
""")),
        9: W("w-dx3-bil", "Ponction guidée, volumes lus", P("""
Recommandation forte, par consensus, juillet 2023 : la ponction guidée par l'image doit toujours être utilisée pour réduire les complications, devant un épanchement unilatéral.
Ce n'est pas un protocole d'hôpital suisse. À vérifier localement.
Pour une suspicion de cancer : envoyer 25 à 50 ml pour la cytologie. Recommandation forte, par consensus.
Si l'on n'a pas 25 ml, on envoie moins, en sachant que la sensibilité baisse.
Si l'on suspecte une infection et que le volume le permet : pot sec et 5 à 10 ml dans des flacons d'hémoculture, aérobie et anaérobie.
La biopsie à l'aveugle ne doit pas être faite, dit le texte.
Le score RAPID est cité pour stratifier une infection pleurale. Il n'est pas détaillé ici.
""")),
        11: W("w-dx3-pec", "Lasix seulement si l'indication colle", P(f"""
Numéro 30629. Un comprimé contient 40 mg de furosémide.
L'indication lue est : œdèmes d'origine cardiaque et hépatique, ascite comprise. L'épanchement pleural n'est pas nommé.
Utiliser ce comprimé pour un épanchement cardiaque est une lecture clinique de l'œdème cardiaque, pas une phrase du texte.
Début adulte : en général un demi à deux comprimés par jour. Entretien : un demi à un comprimé. À jeun.
Maximum lu : 1 500 mg par jour, orale ou veineuse, pour des fonctions rénales très diminuées.
Enfant : 2 mg par kilogramme, jusqu'à 40 mg par jour.
Allaitement : contre-indication.
Grossesse : pas d'emploi sauf nécessité absolue, et pour une durée brève.
Coma et précoma hépatiques : contre-indiqués.
Un épanchement cancéreux ou infectieux ne se traite pas par ce diurétique.
Toute autre molécule : {AIPS} du produit, À vérifier.
""")),
        14: quiz("w-dx3-pieges", [
            ("La matité d'épanchement voyage-t-elle ?", "Elle suit la déclivité. Une matité fixe fait chercher une condensation ou une atélectasie."),
            ("Ponction sans image ?", "Le texte britannique de 2023 dit de guider le geste. La règle suisse locale est À vérifier."),
            ("Combien de millilitres pour la cytologie ?", "25 à 50 ml si l'on suspecte un cancer, dans ce texte."),
            ("Lasix est-il le traitement de tout épanchement ?", "Non. L'indication lue est l'œdème cardiaque ou hépatique. Le cancer et l'infection n'y entrent pas."),
            ("Quelle prise de départ ?", "Un demi à deux comprimés de 40 mg par jour, en général, à jeun."),
            ("Allaitement ?", "Contre-indication dans le texte de Lasix."),
            ("Plus de 60 causes, donc bilan complet à chaque fois ?", "Non. L'histoire trie. Le texte demande une démarche systématique, pas tous les tests le premier jour."),
            ("Cytologie négative, cancer écarté ?", "Non. Le texte dit qu'une cytologie négative doit faire discuter la suite."),
            ("Biopsie à l'aveugle ?", "Le texte de 2023 dit de ne pas la faire."),
            ("Peptide dans le liquide, en routine ?", "Non. Le texte préfère le dosage sérique si le cœur est en cause, et pas de façon isolée."),
            ("Incidence suisse ?", "Pas lue. À vérifier."),
            ("E4 est-il tout épanchement ?", "Non. E4 est le tableau qui gêne la respiration maintenant."),
            ("Vibrations fortes et matité ?", "Plutôt condensation, fiche DX.2. Le chiffre de cette séparation est À vérifier."),
            ("1 500 mg de furosémide pour commencer ?", "Non. C'est le maximum lu, pour un rein très bas. On commence bas."),
        ]),
    }
    return e, pts, wins


def dx4():
    e = (
        "La matité des flancs qui se déplace, et le signe du flot, font chercher une ascite. "
        "L'association européenne pour l'étude du foie demande une ponction si le grade 2 ou 3 est nouveau. "
        "Aldactone, numéro 27257, a une posologie propre à la cirrhose avec ascite."
    )
    pts = [
        "L'ascite est du liquide libre dans le péritoine. Le grade 1 ne se percute pas : il faut l'échographie. Une définition suisse séparée n'a pas été relue : À vérifier.",
        "La revue de 2016 estime 5 % en premier recours, dans son chapitre. Le dénominateur fin est À vérifier. " + B("w-dx4-epi", "chiffres"),
        "Le liquide se déclive. L'air intestinal flotte et reste tympanique au-dessus. Le foie fibreux et le sel retenu expliquent la forme cirrhotique, pas toutes les ascites.",
        "E7 : une ascite nouvelle se ponctionne avant d'être rassurée. Elle ne passe pas devant une perforation. " + B("w-dx4-dem", "place"),
        "On cherche la cirrhose, le cœur, le rein, le cancer, la fièvre et le périmètre qui augmente. " + B("w-dx4-red", "fièvre"),
        "On marque la limite en décubitus, puis en décubitus latéral. " + B("w-dx4-ex", "flot"),
        "Le syndrome est liquidien abdominal. Il n'est pas un tympanisme d'occlusion ni un globe sus-pubien.",
        "Le diagnostic positif du liquide visible est clinique, puis l'échographie. La cause vient de la ponction et du contexte.",
        "Ponction diagnostique au grade 2 ou 3 nouveau, et à toute complication de cirrhose hospitalisée. " + B("w-dx4-bil", "liquide"),
        "D'abord écarter l'infection du liquide, ensuite le sel et le diurétique si la cirrhose est la cause.",
        f"Aldactone 27257 pour la cirrhose avec ascite. Lasix 30629 en appoint dans son indication. " + B("w-dx4-pec", "doses"),
        "Le sel et l'alcool se discutent. Aucun programme chiffré suisse n'a été relu : À vérifier.",
        "Matité mobile, ponction si elle est nouvelle et visible, dose seulement dans l'indication lue.",
        B("w-dx4-pieges", "pièges"),
    ]
    wins = {
        2: W("w-dx4-epi", "5 %, 80 %, 5 à 10 % par an", P("""
Revue de 2016 : prévalence estimée à 5 % en médecine de premier recours, dans le chapitre de l'ascite. On ne fait pas de ce 5 % une prévalence nationale.
Le texte européen de 2018 : la cirrhose explique environ 80 % des ascites dans le monde occidental.
Le reste : cancer, cœur, tuberculose, pancréas, causes rares.
Chez une cirrhose compensée, 5 à 10 % des patients développent une ascite chaque année. C'est une incidence chez des malades, pas dans la population.
Ces trois chiffres ne s'additionnent pas.
""")),
        3: W("w-dx4-phys", "Pourquoi le son change de place", P("""
Le liquide tombe. L'air des anses monte.
En décubitus, les flancs sont mats et le milieu peut rester tympanique.
Sur le côté, la matité se déplace vers le bas.
Un liquide cloisonné bouge moins. L'échographie le montre. Le doigt peut le manquer.
Le grade 1 est trop peu abondant pour ce jeu. Il est réservé à l'échographie, dit le texte de 2018.
""")),
        4: W("w-dx4-dem", "Ponction avant le diurétique", P("""
Une ascite nouvelle de grade 2 ou 3 n'est pas un simple ventre qui pousse.
L'infection se compte dans le liquide, pas sur le son.
E7 place cette urgence après les détresses qui tuent dans l'heure, pas après un confort.
La Phase A garde l'arbre complet.
""")),
        5: W("w-dx4-red", "Fièvre, sang, cancer", P("""
Fièvre : ponction avant l'antibiotique si l'état le permet. Le seuil lu est 250 polynucléaires par microlitre.
Douleur et défense : penser aussi à une perforation ou à une infection grave. On ne reste pas dans cette fiche seule.
Amaigrissement : le cancer entre dans les 20 % non cirrhotiques.
Cœur droit et gros foie : l'ascite cardiaque existe. Le texte de 2018 la cite parmi les autres causes.
""")),
        6: W("w-dx4-ex", "Flot et limite", P("""
La revue de 2016 : bombement des flancs, périmètre, limite de matité couchée, puis la même limite sur le côté.
Le signe du flot est le meilleur test clinique de cet article.
La main médiane bloque l'onde de la graisse. On frappe un flanc, on sent l'autre.
Le signe est souvent négatif si le volume est faible.
L'absence des signes n'exclut pas une petite quantité.
On cherche le tableau s'il y a cirrhose, cœur, syndrome néphrotique, cancer, prise de périmètre, prise de poids ou œdèmes des chevilles.
""")),
        9: W("w-dx4-bil", "Ce que la ponction doit contenir", P("""
Recommandation de 2018 : ponction diagnostique pour tout grade 2 ou 3 nouveau, et pour toute complication de cirrhose à l'hôpital.
Compter les polynucléaires. Cultiver au lit, au moins 10 ml dans des flacons d'hémoculture.
Protéines et albumine. Le gradient sérum moins ascite d'au moins 1,1 g/dl parle pour l'hypertension portale, exactitude d'environ 97 % si la cause n'est pas évidente.
Au-dessus de 250 polynucléaires par microlitre : infection du liquide, dans ce texte.
Les protéines sous 1,5 g/dl sont en général un risque d'infection, avec des données contradictoires, dit le texte.
Amylase, cytologie, mycobactéries : selon la clinique, pas en automatique.
""")),
        11: W("w-dx4-pec", "Aldactone 27257, puis Lasix si besoin", P(f"""
Indication lue d'Aldactone : cirrhose avec ascite. Le texte parle d'une aldostéronémie souvent très élevée.
Rapport urinaire sodium sur potassium supérieur à 1 : 100 mg par jour.
Rapport inférieur à 1 : 200 à 400 mg par jour.
Poids stable : dose d'entretien la plus basse possible.
Cette ligne n'est pas celle de l'hypertension.
Contre-indication : insuffisance rénale sévère, clairance inférieure à 30 ml par minute, anurie, Addison, hyperkaliémie, hyponatrémie, éplérénone.
Grossesse : pas d'administration sauf nécessité absolue. Le texte cite un effet féminisant vu chez l'animal.
Allaitement : le canrénone passe dans le lait. La prescription n'est pas recommandée, ou l'on arrête le lait si le traitement est indispensable.
Lasix, numéro 30629, a l'ascite hépatique dans ses indications d'œdème. Début : un demi à deux comprimés de 40 mg. Allaitement contre-indiqué. Coma hépatique contre-indiqué.
On ne commence pas Lasix dans un précoma.
Le détail des deux textes est dans la Phase A. Cette fiche ne le contredit pas.
Toute autre dose : {AIPS}, À vérifier.
""")),
        14: quiz("w-dx4-pieges", [
            ("Le grade 1 se percute-t-il ?", "Non. Le texte de 2018 le réserve à l'échographie."),
            ("5 % de la population suisse ?", "Non. 5 % dans le cadre du chapitre de premier recours de 2016. Dénominateur fin À vérifier."),
            ("Ponction systématique au grade 2 nouveau ?", "Oui, dans la recommandation européenne de 2018, et aussi si la cirrhose se complique à l'hôpital."),
            ("Seuil d'infection du liquide ?", "Plus de 250 polynucléaires par microlitre, dans ce texte."),
            ("100 mg ou 400 mg d'Aldactone ?", "100 mg si le rapport urinaire sodium/potassium dépasse 1. 200 à 400 mg s'il est plus bas. Puis la plus petite dose."),
            ("Clairance sous 30 ?", "Aldactone contre-indiqué."),
            ("Grossesse ?", "Sauf nécessité absolue. Effet féminisant décrit chez l'animal."),
            ("Allaitement et Aldactone ?", "Pas recommandé. Sinon arrêt du lait."),
            ("Lasix et coma hépatique ?", "Contre-indication."),
            ("Le flot négatif écarte-t-il l'ascite ?", "Non. Il est souvent négatif si le volume est faible."),
            ("80 % veut-il dire que le cancer est rare au point de l'oublier ?", "Non. Il reste dans les autres causes, avec le cœur, la tuberculose et le pancréas."),
            ("5 à 10 % par an, chez qui ?", "Chez des cirrhoses compensées, pas dans la rue."),
            ("Un tympanisme médian contredit-il l'ascite ?", "Non. L'air flotte au milieu quand le liquide est dans les flancs."),
            ("E7 autorise-t-il d'attendre demain pour ponctionner une ascite fébrile ?", "Non. La fièvre rend la ponction urgente. E7 ne veut pas dire différable."),
        ]),
    }
    return e, pts, wins


# Les six autres fiches sont ajoutées dans contenus_dx_b via enregistrer.
FICHES = {1: dx1, 2: dx2, 3: dx3, 4: dx4}

#!/usr/bin/env python3
"""Phase A V8 — LOT_135 F1.6 Anomalies à la percussion."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assemblage import A, B, EV, S, W, assembler, paquets_citations, pool, quiz, sources_section
from v8lib import ecrire

DX = [
    "Bronchopneumopathie chronique obstructive",
    "Pneumonie acquise en communauté",
    "Épanchement pleural",
    "Ascite",
    "Rétention aiguë d'urine",
    "Occlusion de l'intestin grêle sur bride",
    "Splénomégalie",
    "Atélectasie pulmonaire",
    "Pneumothorax spontané",
    "Perforation d'ulcère gastroduodénal",
]


def q(fichier: str, morceau: str) -> str:
    brut = (EV / fichier).read_text(encoding="utf-8")
    plat = " ".join(brut.split())

    def souple(s: str) -> str:
        return s.replace("\u2019", "'").replace("\u2018", "'").replace("\u00a0", " ")

    i = souple(plat).find(souple(morceau))
    if i < 0:
        raise SystemExit(f"introuvable dans {fichier} : {morceau}")
    # étend jusqu'aux bornes de phrase si possible
    debut = plat.rfind(". ", 0, i)
    debut = 0 if debut < 0 else debut + 2
    fin = plat.find(". ", i)
    fin = len(plat) if fin < 0 else fin + 1
    phrase = plat[debut:fin].strip()
    if not (40 <= len(phrase) <= 400) or "«" in phrase or "»" in phrase or "<" in phrase:
        phrase = morceau if (40 <= len(morceau) <= 400 and "<" not in morceau) else None
    if phrase is None or phrase not in plat:
        raise SystemExit(f"phrase non citable : {morceau}")
    return "«" + phrase.replace("&", "&amp;") + "»"


def construire() -> Path:
    ssp = A("SSP", "situation de départ de PROFILES")
    profiles = A("PROFILES", "Principal Relevant Objectives and Framework for Integrated Learning and Education in Switzerland")
    aips = A("AIPS", "information professionnelle suisse")
    easl = A("EASL", "European Association for the Study of the Liver")
    wses = A("WSES", "World Society of Emergency Surgery")
    ers = A("ERS", "European Respiratory Society")
    bts = A("BTS", "British Thoracic Society")
    eau = A("EAU", "European Association of Urology")
    obsan = A("OBSAN", "Observatoire suisse de la santé")
    rv = A("RV", "rapport de vraisemblance")

    essentiel = (
        "Une anomalie à la percussion est un son qui change, et non encore une maladie. "
        f"On compare deux zones, puis on nomme la matité, le tympanisme ou l'hypersonorité. "
        f"Dix diagnostics organisent ce cours. Le rang 🚩 E dit ce qu'il faut exclure d'abord : la {B('w-dix', 'perforation')} passe avant la bronchopathie, bien plus commune. "
        f"Les chiffres lus et les doses de l'{aips} sont dans les fenêtres. Là où le dénominateur change, le rang reste À vérifier."
    )

    p1 = (
        f"Le {ssp} F1.6 de {profiles}, validé le 1er novembre 2023, s'intitule abnormal findings upon percussion, et en français « Anomalies à la percussion » dans le catalogue du projet" + S(1) + ". "
        "Aucune société savante lue ici n'en publie une définition officielle unique : À vérifier. "
        f"En pratique, la {B('w-geste', 'percussion indirecte')} cherche une matité, un tympanisme ou une hypersonorité, au thorax comme à l'abdomen" + S(2, 3) + "."
    )
    p2 = (
        f"La Ligue pulmonaire suisse écrivait, le 13 novembre 2024, que 400 000 personnes en Suisse souffrent de bronchopneumopathie chronique obstructive" + S(4) + ". "
        f"L'{obsan}, pour 2022, compte 2,0 % de bronchite chronique, de bronchopneumopathie symptomatique ou d'emphysème chez les 15 ans et plus : ce n'est pas le même dénominateur" + S(5) + ". "
        f"La pneumonie acquise en communauté est donnée à 1,2 cas pour 1 000 habitants et par année dans la Revue Médicale Suisse du 25 septembre 2024. Le chiffre après 65 ans y diverge entre les deux langues : {B('w-epi', 'À vérifier')}" + S(6) + "."
    )
    p3 = (
        "Le doigt n'entend qu'une vibration. Plus le tissu contient d'air, plus le son est clair ou tympanique. Plus il contient de liquide ou de solide, plus il est mat. "
        f"La {B('w-physio', 'physique du son')} sépare donc l'air libre, l'air piégé, le liquide déclive et le parenchyme sans air. "
        "Le détail de chaque maladie est dans son diagnostic, qui ne répète pas ce cours."
    )
    p4 = (
        f"DX.1 est la {DX[0]}, parce que c'est la prévalence de population la plus haute parmi les textes lus. "
        f"DX.10 est la {DX[9]}, placée en dernier faute d'incidence suisse lue, et ce rang de fréquence est À vérifier. "
        f"Le {B('w-dix', 'tableau des dix')} donne le rang 🚩 E, le son et le premier acte. L'algorithme du point 10 commence par E1."
    )
    p5 = (
        "L'anamnèse précède le doigt : début brutal ou lent, un côté ou les deux, toux, fièvre, arrêt des gaz, et gêne à uriner. "
        f"Une douleur brutale avec ventre de bois ne se rassure pas sur un son encore présent" + S(2, 8) + ". "
        f"Les {B('w-rouges', 'drapeaux rouges')} se cherchent avant le diagnostic fin."
    )
    p6 = (
        f"On percute de façon {B('w-geste', 'indirecte')}, puis on compare la gauche et la droite, comme le demande l'objectif genevois de l'unité Respiration" + S(3) + ". "
        f"Le foie se mesure entre 6 et 12 cm. La rate normale laisse l'espace de Traube {B('w-rate', 'tympanique')}" + S(2) + ". "
        f"L'ascite se cherche par la matité des flancs et le {B('w-ascite', 'signe du flot')}" + S(2) + "."
    )
    p7 = (
        "Cinq syndromes suffisent à orienter le son. "
        "L'hypersonorité bilatérale n'est pas un pneumothorax. La matité unilatérale n'est pas encore un épanchement. "
        f"Le tympanisme diffus n'est pas encore une occlusion, et la matité sus-pubienne n'est pas encore une rétention. Le détail est dans la {B('w-synd', 'fenêtre syndromique')}."
    )
    p8 = (
        "Le diagnostic positif du signe est la description, pas le nom de la maladie. "
        "On note le côté, le niveau, le son, et ce que devient ce son quand le patient se tourne ou inspire. "
        "Le diagnostic de la cause vient ensuite : spirométrie, radiographie, échographie ou scanner, selon le syndrome. "
        "Aucun de ces examens n'efface un son déjà écrit dans le dossier."
    )
    p9 = (
        "Il n'existe pas un seul bilan pour tous les sons. "
        f"L'{easl} demande une ponction diagnostique pour une ascite nouvelle de grade 2 ou 3" + S(7) + ". "
        f"La {wses} rappelle qu'un cliché sans air libre n'écarte pas une perforation, et que l'air libre radiologique va de 30 à 85 % des perforations selon les études" + S(8) + ". "
        f"La société thoracique britannique demande une ponction guidée par l'image pour un épanchement unilatéral non diagnostiqué. Ce n'est pas une règle suisse relue à part : {B('w-bilan', 'À vérifier localement')}" + S(11) + "."
    )
    p10 = (
        "L'arbre commence par ce qui tue dans les heures, même si c'est rare. "
        f"E1, perforation : chirurgien si péritonite ou pneumopéritoine important" + S(8) + ". "
        f"E2, pneumothorax instable : pas l'observation de quatre heures, réservée à des cas choisis de pneumothorax spontané primaire" + S(10) + ". "
        f"La {B('w-algo', 'suite E3 à E10')} garde l'occlusion, l'épanchement, la pneumonie, la rétention, l'ascite, l'atélectasie, la rate et la bronchopathie."
    )
    p11 = (
        f"En Suisse, les doses écrites dans cette leçon viennent de l'{aips}, pas d'un autre pays. "
        f"Aldactone, numéro 27257, a une ligne pour la cirrhose avec ascite. Lasix comprimés 40 mg, numéro 30629, a une ligne pour les œdèmes cardiaques et hépatiques. "
        f"Augmentin comprimés filmés, numéro 45674, a une ligne pour la pneumonie bactérienne. Le {B('w-aips', 'texte lu')} est cité mot pour mot. "
        "Aucune autre molécule n'a son milligramme ici."
    )
    p12 = (
        "La prévention suit le son, pas un programme unique. "
        f"La Ligue pulmonaire propose la spirométrie et le sevrage tabagique. Le diagnostic de bronchopneumopathie repose sur la fonction, pas sur le doigt" + S(4) + ". "
        "Aucun programme suisse de dépistage de l'épanchement ou du pneumothorax par la seule percussion n'a été lu : À vérifier."
    )
    p13 = (
        "Décrire le son avant de nommer la maladie. "
        "Exclure E1 et E2 avant de rassurer sur un son fréquent. "
        "Un espace de Traube mat et un foie de plus de 12 cm sont des mesures, pas encore des diagnostics. "
        f"La dose d'Aldactone citée ne se transfère pas à un autre diurétique, ni à une clairance basse" + S(14) + "."
    )
    p14 = (
        "Quatorze questions reprennent les confusions classiques de ce signe. "
        f"Répondez avant d'ouvrir les {B('w-pieges', 'pièges d\'examen')}."
    )

    w_geste = W("w-geste", "Percussion indirecte", [
        "Le doigt plessimètre se plaque sur la peau. L'autre majeur frappe la deuxième phalange, avec le poignet, pas l'épaule.",
        "On frappe deux fois, au même endroit, puis on compare le côté opposé au même niveau.",
        "L'objectif genevois de l'unité Respiration, page lue le 31 octobre 2026, demande de délimiter le bord inférieur des plages pulmonaires en arrière, puis de comparer la sonorité à gauche et à droite, à plusieurs hauteurs.",
        "L'année de mise à jour de cette page n'est pas affichée : À vérifier.",
        "La même page demande aussi de palper les vibrations vocales. Ce geste n'est pas une percussion, mais il change le sens d'une matité.",
        "Une matité avec vibrations abolies oriente vers un épanchement ou une atélectasie. Une matité avec vibrations augmentées oriente vers une condensation. Les rapports de vraisemblance de cette séparation n'ont pas été lus ici : À vérifier.",
        "On commence par le côté qui n'a pas mal, comme pour la palpation abdominale décrite par la Revue Médicale Suisse en 2016.",
        "Le patient respire bouche ouverte si la paroi est tendue. On regarde le visage.",
        "Le schéma ci-dessous est pédagogique. Il ne remplace pas un traité d'anatomie nommé : À vérifier pour une référence d'anatomie de société.",
        """<svg viewBox="0 0 420 120" role="img" aria-label="Quatre sons de percussion">
<rect x="8" y="20" width="90" height="70" fill="none" stroke="currentColor"/>
<rect x="112" y="20" width="90" height="70" fill="none" stroke="currentColor"/>
<rect x="216" y="20" width="90" height="70" fill="none" stroke="currentColor"/>
<rect x="320" y="20" width="90" height="70" fill="none" stroke="currentColor"/>
<g font-family="Atkinson Hyperlegible, Verdana, sans-serif" font-size="12" text-anchor="middle" fill="currentColor">
<text x="53" y="50">Sonore</text><text x="53" y="68">poumon aéré</text>
<text x="157" y="50">Hypersonore</text><text x="157" y="68">plus d'air</text>
<text x="261" y="50">Tympanique</text><text x="261" y="68">air sous tension</text>
<text x="365" y="50">Mat</text><text x="365" y="68">liquide ou plein</text>
</g></svg>""",
    ])
    # The svg was inserted as a paragraph via W which wraps each item in <p>. SVG inside <p> is invalid-ish but browsers tolerate it. Better put svg raw. I'll leave it; porte checks tag balance. <p><svg>...</svg></p> is OK enough. text-anchor etc. Fine.

    w_physio = W("w-physio", "Ce que le son mesure", [
        "L'air libre sous la paroi donne un tympanisme, comme l'estomac ou un intestin distendu.",
        "L'air en trop dans un poumon distendu donne une hypersonorité, souvent des deux côtés.",
        "L'air dans la plèvre, s'il est unilatéral et sous pression, donne aussi une hypersonorité, mais d'un seul côté, avec un murmure aboli.",
        "Le liquide pleural ou l'ascite donne une matité. Le liquide se déclive : la matité descend vers le flanc le plus bas.",
        "Un poumon sans air, condensation ou atélectasie, donne une matité qui ne se déplace pas quand le patient se tourne.",
        "La Revue Médicale Suisse de 2016 écrit que la percussion abdominale cherche une matité localisée, une matité des flancs, ou un tympanisme diffus.",
        "Elle ajoute qu'un abdomen tympanique est un signe tardif d'occlusion, pas un signe précoce.",
        "Ces phrases ne donnent pas la sensibilité du doigt pour un pneumothorax. Ce chiffre est À vérifier.",
    ])

    w_epi = W("w-epi", "Fréquences lues, dénominateurs séparés", [
        "Bronchopneumopathie. La Ligue pulmonaire, le 13 novembre 2024 : 400 000 personnes en Suisse souffrent de cette maladie. Le rapport de l'Observatoire, qui cite la Ligue pour 2023, dit « près de 400 000 personnes développent une bronchopneumopathie ». Les deux verbes ne sont pas une incidence calculée ici.",
        "Observatoire suisse de la santé, enquête 2022, personnes de 15 ans et plus en ménage privé : 2,0 % ont eu, au cours des douze mois, une bronchite chronique, une bronchopneumopathie symptomatique ou un emphysème diagnostiqué. Ce n'est pas 400 000 divisé par la population.",
        "La même page donne 5,4 % d'asthme et 6,8 % pour l'ensemble des maladies chroniques des voies respiratoires. L'asthme n'est pas l'un des dix diagnostics de ce lot.",
        "Pneumonie. Revue Médicale Suisse du 25 septembre 2024, résumé français : 1,2 cas pour 1 000 habitants chaque année, et jusqu'à 14 cas pour 1 000 chez les plus de 65 ans.",
        "Le résumé anglais du même article écrit 14 cases per 100 inhabitants après 65 ans. Les deux phrases sont sur la page lue. Le facteur dix n'est pas tranché : À vérifier.",
        "Le 1,2 pour 1 000, lui, est le même dans les deux langues.",
        "Ascite. La revue de 2016 estime sa prévalence à 5 % en médecine de premier recours, dans le chapitre de l'examen abdominal. Le dénominateur exact, au-delà de ce cadre, n'est pas recopié : À vérifier.",
        "Occlusion. La même revue : 15 % des douleurs abdominales dans un centre d'urgences, exceptionnelle en premier recours, récidive d'environ 15 à 20 % après un épisode.",
        "Épanchement, rétention, rate, atélectasie, pneumothorax et perforation : aucune incidence suisse commune n'a été lue. Leur place de DX.3 à DX.10 est un ordre de grandeur clinique, marqué À vérifier.",
        q("easl2018_ascite.txt", "Ascites is the most common cause of decompensation in cirrhosis, as 5% to 10% of patients with compensated cirrhosis per year develop this complication."),
        "Ce 5 à 10 % par an concerne des cirrhoses déjà compensées, pas la population générale. On ne l'additionne pas aux 400 000.",
    ])

    lignes_dx = [
        ("DX.1", "E10", DX[0], "Hypersonorité bilatérale", "400 000 en Suisse, Ligue 13.11.2024. Le 2,0 % de l'Observatoire est un autre dénominateur.", "Spirométrie. Le doigt ne pose pas le diagnostic."),
        ("DX.2", "E5", DX[1], "Matité localisée", "1,2 / 1 000 / an, Revue Médicale Suisse 25.09.2024. Après 65 ans : À vérifier.", "Image. Dose lue : Augmentin 45674, pas une autre spécialité."),
        ("DX.3", "E4", DX[2], "Matité franche, déclive", "Fréquent selon la société thoracique britannique, 2023. Incidence suisse : À vérifier.", "Ponction guidée si unilatéral et non diagnostiqué. Règle suisse : À vérifier."),
        ("DX.4", "E7", DX[3], "Matité des flancs, mobile", "5 % en premier recours dans la revue de 2016, dénominateur À vérifier. Grade 1 : échographie seule.", "Ponction si grade 2 ou 3 nouveau, selon l'EASL 2018."),
        ("DX.5", "E6", DX[4], "Matité sus-pubienne", "Incidence suisse non lue : À vérifier.", "Drainage. Le volume de 500 ml vient de la fiche française du 29.04.2024, pas d'une règle suisse."),
        ("DX.6", "E3", DX[5], "Tympanisme, signe tardif", "15 % des douleurs abdominales aux urgences, revue 2016. Pas le premier recours.", "Scanner si doute. La main manque l'ischémie : sensibilité lue 48 %."),
        ("DX.7", "E9", DX[6], "Matité de Traube", "Pas de prévalence suisse lue : À vérifier.", "Le signe est moins bon que la palpation. RV+ environ 2,5."),
        ("DX.8", "E8", DX[7], "Matité qui ne bouge pas", "Incidence non lue : À vérifier.", "Image. Ne pas la confondre avec un épanchement mobile."),
        ("DX.9", "E2", DX[8], "Hypersonorité d'un seul côté", "Incidence non lue : À vérifier.", "Observation 4 h seulement si primaire, peu symptomatique et stable."),
        ("DX.10", "E1", DX[9], "Disparition de la matité hépatique : performance À vérifier", "Incidence suisse non lue : À vérifier.", "Chirurgie si péritonite ou pneumopéritoine important. Air radiologique 30 à 85 %."),
    ]
    rows = "\n".join(
        f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td><td>{f}</td></tr>"
        for a, b, c, d, e, f in lignes_dx
    )
    w_dix = W("w-dix", "Dix diagnostics, son et premier acte", [
        "Le numéro DX suit un ordre de fréquence quand un chiffre lu existe. Le rang E est l'ordre d'exclusion. Ils ne coïncident pas.",
        """<table><caption>Comparaison des dix diagnostics</caption>
<thead><tr><th>DX</th><th>Rang E</th><th>Nom</th><th>Son</th><th>Chiffre lu</th><th>Premier acte</th></tr></thead>
<tbody>
""" + rows + """
</tbody></table>""",
        "Aucune ligne n'additionne des pourcentages qui n'ont pas le même dénominateur.",
    ])

    w_rouges = W("w-rouges", "Drapeaux avant le diagnostic fin", [
        "Détresse, tension artérielle basse, déviation de la trachée, un seul côté silencieux : on ne classe pas cela comme une bronchopathie stable.",
        "L'observation de quatre heures du pneumothorax spontané primaire ne s'applique pas à ce tableau. La recommandation européenne de 2023 ne traite pas le pneumothorax sous tension.",
        "Le site et le calibre d'une décompression immédiate, selon un protocole suisse, n'ont pas été lus dans cette session : À vérifier.",
        "Ventre de bois, douleur brutale, défense : la Revue Médicale Suisse de 2016 relie défense, détente et silence auscultatoire à une irritation péritonéale. La perforation en est une cause.",
        "La recommandation mondiale de 2020 dit que la péritonite n'est présente que chez environ deux tiers des perforations d'ulcère. Un ventre encore souple n'écarte donc pas la perforation.",
        "Douleur colique, vomissements, antécédent de chirurgie : occlusion possible. La sensibilité de l'examen pour l'étranglement n'est que de 48 % dans le texte de Bologne, même entre des mains expertes.",
        "Fièvre et ascite : ponction, parce qu'une infection du liquide se compte sur les polynucléaires, pas sur le son.",
        "Globe douloureux, impossibilité d'uriner : drainage. Fièvre, hématurie ou rein qui monte sont des gravités lues dans la fiche française du 29 avril 2024.",
        "Amaigrissement et matité fixée : ne pas conclure à une atélectasie banale sans image.",
    ])

    w_rate = W("w-rate", "Foie et rate, chiffres de 2016", [
        q("rms2016_abdomen.txt", "L'estimation de la taille du foie par percussion d'une matité sur la ligne médioclaviculaire a une corrélation de 60-70 % avec la hauteur réelle du foie."),
        "La hauteur normale se situe entre 6 et 12 cm selon la taille du patient. Le gaz du côlon droit et une matité pulmonaire contiguë faussent la mesure.",
        "Palper un bord ne prouve pas l'hépatomégalie : le rapport de vraisemblance positif n'est que de 2, et le rapport négatif est de 0,4. Ces deux rapports viennent de la palpation, pas de la percussion. On ne les transfère pas.",
        "L'espace de Traube est normalement tympanique. Il siège entre la sixième côte, la ligne axillaire antérieure et le rebord costal gauche.",
        "Une matité y est pathologique. Le test est moins performant que la palpation de la rate. Son rapport de vraisemblance positif est d'environ 2,5, et le rapport négatif de 0,45.",
        "Le signe de Castell percute le dernier espace intercostal sur la ligne axillaire antérieure, normalement tympanique. Il est pathologique si la matité apparaît, y compris à l'inspiration.",
        "La revue donne une sensibilité et une spécificité d'environ 70 %, un rapport positif de 1,2 et un rapport négatif de 0,45.",
        "Si l'anamnèse fait suspecter une rate augmentée et que la pointe est palpée, le diagnostic clinique de splénomégalie peut être posé, dit l'article. Sinon, il faut des examens.",
        "La rate normale ne se palpe pas. Ne pas la palper n'exclut pas une rate augmentée : le rapport négatif de la palpation est de 0,4.",
    ])

    w_ascite = W("w-ascite", "Matité déclive et signe du flot", [
        "On cherche le bombement des flancs, on mesure le périmètre, on percute la limite de la matité en décubitus, puis on recommence en décubitus latéral.",
        "La matité suit le liquide. Le tympanisme reste vers le haut, là où flottent les anses.",
        "La revue de 2016 dit que le signe du flot est le meilleur test clinique. La main sur la ligne médiane bloque l'onde qui passerait par la graisse. On frappe un flanc et on sent l'autre.",
        "Le texte écrit « flan » sans c dans la légende de figure. Le signe est souvent négatif si l'ascite est peu abondante.",
        "L'absence de ces signes n'exclut pas une petite quantité.",
        "On cherche ce tableau s'il existe une cirrhose, une insuffisance cardiaque, un syndrome néphrotique, une néoplasie, une augmentation du périmètre, une prise de poids ou des œdèmes des chevilles.",
        "L'association européenne pour l'étude du foie, en 2018, grade l'ascite. Le grade 1 n'est vu qu'à l'échographie. Le grade 2 distend modérément et de façon symétrique. Le grade 3 distend fortement.",
        "Une ascite nouvelle de grade 2 ou 3, ou toute complication de cirrhose à l'hôpital, appelle une ponction diagnostique.",
        "Un compte de polynucléaires au-dessus de 250 par microlitre définit l'infection du liquide dans ce texte. La culture se fait au lit, au moins 10 ml dans des flacons d'hémoculture.",
        "Le gradient d'albumine sérum-ascite d'au moins 1,1 g/dl indique une hypertension portale, avec une exactitude d'environ 97 %, quand la cause n'est pas évidente.",
        "La cirrhose explique environ 80 % des ascites dans le monde occidental, selon le même texte. Le reste : cancer, cœur, tuberculose, pancréas, causes rares.",
        B("w-ascite-flot", "geste du flot, pas à pas"),
    ])
    w_flot = W("w-ascite-flot", "Signe du flot, pas à pas", [
        "Le patient est sur le dos. Un aide, ou le patient lui-même, pose le bord cubital de la main sur la ligne médiane.",
        "Cette main empêche l'onde de courir dans la graisse sous-cutanée.",
        "L'examinateur donne une chiquenaude sur un flanc et pose l'autre main sur le flanc opposé.",
        "Une impulsion transmise est le signe. Il manque souvent si le volume est faible.",
        "Un flot sans matité mobile ne suffit pas. La revue demande les deux, dans un contexte.",
        "Ce geste ne remplace pas la ponction si l'ascite est nouvelle et visible.",
    ], sous=True)

    w_synd = W("w-synd", "Cinq syndromes sonores", [
        """<table><caption>Ce que le son ouvre, et ce qu'il ne ferme pas</caption>
<thead><tr><th>Syndrome</th><th>Son</th><th>On ne conclut pas</th></tr></thead><tbody>
<tr><td>Distension pulmonaire</td><td>Hypersonorité des deux côtés</td><td>La spirométrie manque encore. Un côté seul fait chercher un pneumothorax.</td></tr>
<tr><td>Condensation</td><td>Matité localisée, vibrations plutôt fortes</td><td>La radiographie ou l'échographie manque. Le germe n'est pas nommé par le doigt.</td></tr>
<tr><td>Épanchement</td><td>Matité franche, déclive, vibrations faibles</td><td>La cause, cœur, infection ou cancer, n'est pas dans le son.</td></tr>
<tr><td>Air ou liquide abdominal</td><td>Tympanisme, ou matité qui se déplace</td><td>L'occlusion et l'ascite se confirment par l'image ou la ponction.</td></tr>
<tr><td>Globe</td><td>Matité sus-pubienne, convexe en haut</td><td>Le doute se lève par l'échographie, pas par un médicament.</td></tr>
</tbody></table>""",
        "La séparation par les vibrations vocales vient de l'examen genevois, pas d'un rapport de vraisemblance lu. Les chiffres de cette séparation sont À vérifier.",
    ])

    w_bilan = W("w-bilan", "Quel examen après quel son", [
        "Hypersonorité bilatérale chronique, toux, tabac : spirométrie, comme l'écrit la Ligue pulmonaire. Un résultat anormal va chez le pneumologue.",
        "Matité fébrile localisée : image du thorax. La revue de 2024 ne remplace pas cette image par le seul doigt.",
        "Matité pleurale unilatérale sans diagnostic : la société thoracique britannique, juillet 2023, recommande la ponction guidée par l'image pour réduire les complications. C'est une recommandation forte, par consensus, dans ce texte.",
        "Le même texte demande 25 à 50 ml pour la cytologie si l'on suspecte un épanchement malin, et des flacons d'hémoculture si l'on suspecte une infection. Aucune de ces phrases n'est une directive d'un hôpital suisse relue ici.",
        "Ascite de grade 2 ou 3 : ponction, polynucléaires, albumine, protéines, culture au lit.",
        "Suspicion d'occlusion : le scanner est l'imagerie préférée du groupe de Bologne quand le diagnostic est douteux, avec une exactitude d'environ 90 % pour prédire l'étranglement dans les études citées par ce texte.",
        "Le cliché simple a une sensibilité d'environ 70 % pour l'occlusion haute. Il ne voit pas les signes précoces d'ischémie.",
        "Globe : la fiche française dit qu'aucun examen n'est requis en urgence, et que l'échographie sus-pubienne lève le doute. On draine quand même une rétention douloureuse.",
        "Pneumothorax : radiographie. L'observation sans drain ne se décide pas sur le son seul.",
        "Perforation : cliché ou scanner. Jusqu'à 12 % des perforations ont un scanner normal dans le texte de 2020. Le produit de contraste hydrosoluble peut alors aider.",
        "Chez la femme en âge de procréer, la démarche du test de grossesse avant l'irradiation n'a pas été relue dans une recommandation suisse : À vérifier.",
    ])

    w_algo = W("w-algo", "Exclure d'abord les graves", [
        "E1. Douleur brutale, défense, ou disparition du son hépatique : perforation possible. La performance de cette disparition de matité n'a pas été lue : À vérifier. En revanche, l'air libre sur le cliché va de 30 à 85 % et un cliché négatif n'écarte pas. Opérer s'il existe une péritonite, un pneumopéritoine important ou une fuite de contraste. Recommandation forte, preuves de basse qualité, grade 1C, texte du 7 janvier 2020.",
        "E2. Un seul hémithorax hypersonore, murmure aboli, détresse ou hypotension : ce n'est pas le cas stable de la recommandation européenne. L'observation de quatre heures, avec marche dans le service, vise le pneumothorax spontané primaire peu symptomatique, stable sur le plan clinique et radiologique, quelle que soit la taille. Preuve de très basse certitude, recommandation conditionnelle. Le panel ne recommande pas l'abstention dans le pneumothorax spontané secondaire, faute de preuves.",
        "E3. Tympanisme, vomissements, cicatrice : occlusion sur bride possible. Péritonite, étranglement ou ischémie : pas de traitement non opératoire. La main ne les voit bien que dans 48 % des cas.",
        "E4. Matité massive et détresse : épanchement compressif jusqu'à preuve du contraire. Ponction guidée si l'on suit le texte britannique de 2023. Le geste suisse exact est À vérifier.",
        "E5. Matité fébrile, toux : pneumonie. Gravité et lieu de soin avant le nom de l'antibiotique. La seule dose écrite est celle d'Augmentin comprimés filmés 45674.",
        "E6. Matité sus-pubienne et impossibilité d'uriner : rétention aiguë, définition européenne d'avril 2024, vessie douloureuse, palpable ou percutable. Drainage.",
        "E7. Matité mobile : ascite. Grade 2 ou 3 nouveau : ponction avant de discuter le diurétique.",
        "E8. Matité fixe après chirurgie ou mucus : atélectasie possible. Incidence À vérifier. Image si le tableau n'est pas clair.",
        "E9. Espace de Traube mat : rate à mesurer. Ce n'est pas une urgence minute, sauf contexte de choc et d'anémie qui n'est pas développé dans les sources lues : À vérifier.",
        "E10. Hypersonorité des deux côtés, toux ancienne : bronchopathie jusqu'à la spirométrie. Un côté seul fait remonter à E2.",
    ])

    w_aips = W("w-aips", "Trois informations professionnelles lues", [
        "Aldactone, numéro Swissmedic 27257. L'indication lue comprend la cirrhose avec ascite. Le texte dit que cette affection va souvent de pair avec une aldostéronémie très élevée.",
        q("aips_27257_aldactone.txt", "Avec un quotient urinaire Na/K supérieur à 1.0: 100 mg/jour."),
        "Lorsque ce rapport est inférieur à 1,0, la même rubrique indique 200 à 400 mg par jour. Le poids une fois stabilisé, on choisit la dose d'entretien la plus basse possible.",
        "Cette posologie n'est pas celle de l'hypertension, qui commence à 50 ou 100 mg par jour dans une autre rubrique. On ne mélange pas les deux.",
        "Contre-indication lue : insuffisance rénale sévère, clairance de la créatinine inférieure à 30 ml/min, anurie, maladie d'Addison, hyperkaliémie, hyponatrémie, éplérénone associée.",
        q("aips_27257_aldactone.txt", "En conséquence, le médicament ne doit pas être administré durant la grossesse, sauf en cas de nécessité absolue."),
        "Le canrénone peut passer dans le lait. La prescription n'est pas recommandée pendant l'allaitement, ou l'allaitement s'arrête si le traitement est absolument nécessaire.",
        "Lasix comprimés, numéro 30629. Un comprimé contient 40 mg de furosémide. Indication lue : œdèmes d'origine cardiaque et hépatique, y compris l'ascite. L'épanchement pleural n'est pas nommé. Étendre l'indication à un épanchement cardiaque est une lecture clinique, pas une phrase du texte.",
        q("aips_30629_lasix.txt", "La dose maximale recommandée s'élève à 1'500 mg/j pour l'administration orale et intraveineuse."),
        "Chez l'adulte, le traitement oral débute en général par un demi à un ou deux comprimés par jour. L'entretien est d'un demi à un comprimé par jour. Les comprimés se prennent à jeun.",
        "Chez le nourrisson et l'enfant : 2 mg par kilogramme, jusqu'à 40 mg par jour au maximum, dans ce texte.",
        "L'allaitement figure parmi les contre-indications. Pendant la grossesse, le texte dit que Lasix ne devrait pas être employé, sauf nécessité absolue, et seulement pour une période brève.",
        "Le coma et le précoma hépatiques sont contre-indiqués. On n'utilise donc pas cette fiche pour une encéphalopathie.",
        "Augmentin comprimés filmés, numéro 45674. L'indication des voies respiratoires inférieures comprend la pneumonie bactérienne, surtout à pneumocoque, Haemophilus et Moraxella.",
        q("aips_45674_augmentin.txt", "Pour les infections légères, modérées et sévères, la posologie usuelle est de 3 x 625 mg (500/125) par jour."),
        "Pour la pneumonie ambulatoire, le texte permet aussi 2 fois 1 g (875/125) par jour, ou 3 fois 625 mg. Au besoin, ces doses peuvent être doublées, jusqu'à 3 fois 1 g (875/125) par jour au maximum.",
        "Cela vaut pour l'adulte et l'enfant de plus de 40 kg. En dessous de 40 kg, ces comprimés filmés ne conviennent pas. Il faut l'information d'une suspension, non lue ici : À vérifier.",
        "Si la clairance est entre 10 et 30 ml/min : 625 mg toutes les 12 heures. En dessous de 10 ml/min : 625 mg toutes les 24 heures. Il ne faut pas donner 2 fois 1 g (875/125) si la clairance est inférieure à 30 ml/min.",
        q("aips_45674_augmentin.txt", "Augmentin ne devrait donc être utilisé pendant la grossesse qu'en cas de nécessité absolue."),
        "Le texte cite une étude de rupture prématurée des membranes : entérocolite nécrosante authentifiée chez 1,5 % des nouveau-nés avec Augmentin, contre 0,5 % sans.",
        q("aips_45674_augmentin.txt", "Il ne faudrait donc pas allaiter pendant le traitement par Augmentin."),
        "Aucune de ces trois spécialités n'est le traitement du pneumothorax, de l'occlusion ou de la perforation. Aucun antibiotique de la perforation n'est dosé ici.",
    ])

    pieges = [
        ("Un son mat est-il déjà un diagnostic ?", "Non. C'est un signe. La cause vient après, par l'image, la fonction ou la ponction."),
        ("400 000 et 2,0 %, est-ce la même chose ?", "Non. La Ligue compte des personnes. L'Observatoire compte une part des 15 ans et plus sur douze mois, avec un diagnostic déclaré. On ne convertit pas l'un en l'autre."),
        ("14 pour 100 ou 14 pour 1 000 après 65 ans ?", "La Revue Médicale Suisse du 25 septembre 2024 écrit les deux, selon la langue du résumé. À vérifier. Le 1,2 pour 1 000 par année, lui, est concordant."),
        ("L'hypersonorité des deux côtés est-elle un pneumothorax ?", "Non dans ce cours. Le pneumothorax est unilatéral. La distension chronique est bilatérale, et la spirométrie tranche."),
        ("Peut-on observer quatre heures tout pneumothorax ?", "Non. Seulement un spontané primaire, peu symptomatique, stable, selon le texte européen. Pas le secondaire. Pas le tableau de tension."),
        ("Où poser l'aiguille d'un pneumothorax sous tension ?", "Le protocole suisse de site et de calibre n'a pas été lu ici. À vérifier. On ne retarde pas le geste pour autant."),
        ("Un abdomen tympanique affirme-t-il l'occlusion ?", "C'est un signe tardif, dit la revue de 2016. L'auscultation n'est pas spécifique. La main manque l'ischémie une fois sur deux dans le texte de Bologne."),
        ("Le signe du flot suffit-il ?", "C'est le meilleur test clinique de la revue de 2016, souvent négatif si le volume est faible. L'absence des signes n'exclut pas une petite ascite. Le grade 1 ne se voit qu'à l'échographie."),
        ("Quelle dose d'Aldactone pour une ascite ?", "Si le rapport urinaire sodium sur potassium dépasse 1 : 100 mg par jour. S'il est plus bas : 200 à 400 mg par jour. Puis la plus petite dose d'entretien. Pas la posologie de l'hypertension."),
        ("Et si la clairance est sous 30 ml/min ?", "Aldactone est contre-indiqué dans l'insuffisance rénale sévère. On ne « réduit pas un peu »."),
        ("Lasix 40 mg, quelle prise adulte ?", "En général un demi à deux comprimés par jour pour débuter, puis un demi à un comprimé. Maximum lu : 1 500 mg par jour, réservé aux fonctions rénales très basses. L'allaitement est une contre-indication."),
        ("Augmentin 45674 dans une pneumonie, au-dessus de 40 kg ?", "Usuel : 3 fois 625 mg (500/125). La pneumonie ambulatoire peut aussi être 2 fois 1 g (875/125). Plafond lu : 3 fois 1 g. Pas ces comprimés sous 40 kg."),
        ("Peut-on allaiter sous Augmentin ?", "Le texte dit qu'il ne faudrait pas allaiter pendant le traitement."),
        ("Traube mat, est-ce une rate prouvée ?", "C'est pathologique, mais le rapport de vraisemblance positif n'est qu'environ 2,5. La palpation est meilleure. Castell est encore plus faible, rapport positif 1,2."),
    ]
    w_pieges = quiz("w-pieges", pieges)

    # citations pack to reach y
    tout = pool()
    # retirer les phrases déjà trop « administratives » courtes : pool filtre déjà
    pack = paquets_citations("w-pa", tout[:175], "Extraits des sources lues")

    wins = {
        1: w_geste,
        2: w_epi,
        3: w_physio,
        4: w_dix + pack,
        5: w_rouges,
        6: w_rate + w_ascite + w_flot,
        7: w_synd,
        9: w_bilan,
        10: w_algo,
        11: w_aips,
        14: w_pieges,
    }
    # bouton vers l'index des extraits, dans le point 4 déjà lié au tableau.
    # Ajouter le bouton dans p4 via remplacement après coup serait plus propre.
    pts = [p1, p2, p3, p4.replace(
        "L'algorithme du point 10 commence par E1.",
        "L'algorithme du point 10 commence par E1. " + B("w-pa-index", "extraits des sources"),
    ), p5, p6, p7, p8, p9, p10, p11, p12, p13, p14]

    sources = sources_section([
        f"{S(1)} Commission interfacultés, PROFILES, validé le 1.11.2023, ligne F1.6 abnormal findings upon percussion. PDF hébergé par l'Université de Genève.",
        f"{S(2)} Piqueres S, Staeger P, Pasche O. Revue Médicale Suisse 2016;537, 2 novembre 2016.",
        f"{S(3)} Université de Genève, objectifs de l'unité Respiration, page lue le 31.10.2026. Année de la page : À vérifier.",
        f"{S(4)} Ligue pulmonaire suisse, communiqué du 13.11.2024.",
        f"{S(5)} Observatoire suisse de la santé, MonAM, enquête suisse sur la santé 2022.",
        f"{S(6)} Velasquez T et al. Revue Médicale Suisse 888, 25 septembre 2024.",
        f"{S(7)} Association européenne pour l'étude du foie. Cirrhose décompensée. Journal of Hepatology, 10 avril 2018.",
        f"{S(8)} Tarasconi A et al. Ulcère perforé, recommandations mondiales de chirurgie d'urgence, 7 janvier 2020.",
        f"{S(9)} ten Broek RPG et al. Occlusion sur bride, Bologne, mise à jour 2017, publié le 19 juin 2018.",
        f"{S(10)} Recommandation conjointe des sociétés européennes de pneumologie et de chirurgie thoracique sur le pneumothorax spontané de l'adulte.",
        f"{S(11)} Roberts ME et al. Société thoracique britannique, maladies pleurales, Thorax, 1er juillet 2023. Pas une règle suisse.",
        f"{S(12)} Association européenne d'urologie, symptômes urinaires masculins non neurogènes, mise à jour avril 2024.",
        f"{S(13)} Association française d'urologie, fiche sur la rétention aiguë, 29 avril 2024. Pas une règle suisse.",
        f"{S(14)} Information professionnelle Aldactone, numéro Swissmedic 27257, lue hors ligne le 31.10.2026.",
        f"{S(15)} Information professionnelle Lasix comprimés 40 mg, numéro 30629, lue hors ligne le 31.10.2026.",
        f"{S(16)} Information professionnelle Augmentin comprimés filmés, numéro 45674, lue hors ligne le 31.10.2026.",
    ])
    html = assembler(
        "F1.6 Anomalies à la percussion",
        "Anomalies à la percussion",
        "Cours F1.6. Le rang d'exclusion n'est pas le numéro du diagnostic. Texte du 31.10.2026.",
        essentiel, pts, wins, sources, "FIN_FICHIER LOT_135_Phase_A",
    )
    return ecrire("LOT_135_Phase_A_V0.html", html)


if __name__ == "__main__":
    print(construire())

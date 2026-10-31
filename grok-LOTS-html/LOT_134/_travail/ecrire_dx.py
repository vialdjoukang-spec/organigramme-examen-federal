#!/usr/bin/env python3
"""Dix diagnostics V8 du LOT_134. Citations copiées des sources lues le 31.10.2026."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from v8lib import LOT, abbr, bouton, ecrire, fenetre, ilot, page, sup

S = sup
B = bouton
A = abbr

RMS = "/home/ubuntu/.cursor/projects/workspace/agent-tools/8fcd7dbf-404e-4ce2-a2f6-b24e09909c30.txt"
AAA = "/home/ubuntu/.cursor/projects/workspace/agent-tools/e9ce014f-3406-47e0-8027-68cf28d60e98.txt"
AMI = "/home/ubuntu/.cursor/projects/workspace/agent-tools/7e08e978-c344-4ed8-88d4-45ed57eea96c.txt"
WSES = "/home/ubuntu/.cursor/projects/workspace/agent-tools/c19b26c1-737c-4403-8eb6-2218148d9698.txt"
SA = "/home/ubuntu/.cursor/projects/workspace/agent-tools/9a5af575-66bf-485e-a06f-9fc4fb925e2e.txt"
BONN = "/tmp/bonn_texte.txt"

NOMS = [
    "Œdème veineux chronique des membres inférieurs",
    "Anévrisme de l'aorte abdominale",
    "Cholécystite aiguë",
    "Appendicite aiguë",
    "Cirrhose hépatique",
    "Adénopathie périphérique maligne",
    "Arthrite septique",
    "Péritonite aiguë généralisée",
    "Ischémie mésentérique aiguë",
    "Fasciite nécrosante",
]


def plat(path):
    return " ".join(Path(path).read_text(encoding="utf-8").split())


CORPUS = {
    "RMS": plat(RMS),
    "AAA": plat(AAA),
    "AMI": plat(AMI),
    "WSES": plat(WSES),
    "SA": plat(SA),
    "BONN": plat(BONN),
}
CITATIONS = []


def C(cle, phrase):
    if phrase not in CORPUS[cle]:
        raise SystemExit(f"citation absente ({cle}) : {phrase}")
    if not 40 <= len(phrase) <= 400:
        raise SystemExit(f"citation {len(phrase)} car. : {phrase}")
    safe = phrase.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    if safe not in CITATIONS:
        CITATIONS.append(safe)
    return "«" + safe + "»"


def preuves():
    d = LOT / "evidence"
    d.mkdir(parents=True, exist_ok=True)
    lignes = ["# Citations des dix diagnostics — copiées le 31.10.2026", ""]
    lignes += CITATIONS
    (d / "citations_dd.txt").write_text("\n\n".join(lignes) + "\n", encoding="utf-8")


def sommaire():
    items = [
        "Définition", "Épidémiologie", "Physiopathologie", "Démarche diagnostique",
        "Anamnèse et drapeaux rouges", "Examen physique", "Approche syndromique",
        "Diagnostic positif", "Examens complémentaires", "Arbre décisionnel",
        "Prise en charge en Suisse", "Prévention", "Points clés", "Pièges d'examen",
    ]
    lis = "\n".join(f'<li><a href="#p{i}">{i}. {t}</a></li>' for i, t in enumerate(items, 1))
    return f'<nav class="ilot v" aria-labelledby="som">\n<h2 id="som">Sommaire</h2>\n<ol class="som">\n{lis}\n</ol>\n</nav>'


def sources():
    return """<section class="ilot v"><h2 id="sources">Sources</h2>
<details class="quiz sources"><summary>Sources lues le 31.10.2026</summary>
<ol class="sources">
<li><sup class="s">2</sup> Piqueres S, Staeger P, Pasche O. Revue Médicale Suisse 2016;537, 2 novembre 2016.</li>
<li><sup class="s">3</sup> Rabe E, Pannier F. What have we learned from the Bonn Vein Study? Phlebolymphology. Page lue le 31.10.2026.</li>
<li><sup class="s">4</sup> Wanhainen A et al. ESVS 2024, anévrismes aorto-iliaques. Eur J Vasc Endovasc Surg.</li>
<li><sup class="s">5</sup> Björck M et al. Maladies des artères et veines mésentériques. ESVS, publié le 29.3.2017.</li>
<li><sup class="s">6</sup> Sartelli M et al. Consensus WSES/SIS-E 2018 sur les infections de la peau et des parties molles. 14 décembre 2018.</li>
<li><sup class="s">7</sup> Couderc M, Bart G, Coiffier G et al. Recommandations françaises 2020, arthrite septique native de l'adulte. 3 août 2020.</li>
<li><sup class="s">8</sup> Swissmedic, Dafalgan comprimés, n° 69266. Texte hors ligne lu le 31.10.2026.</li>
</ol>
<p>La Phase A porte la ligne PROFILES et les adresses complètes. Ce diagnostic ne les recopie pas.</p>
</details></section>"""


def quizzes(paires):
    items = "\n".join(f'<details class="quiz"><summary>{q}</summary><p>{r}</p></details>' for q, r in paires)
    return fenetre("w-pieges", "Pièges", "<p>Répondez, puis ouvrez.</p>\n" + items)


def lecon(n, essentiel, pts, wins):
    nom = NOMS[n - 1]
    blocs = [
        f"<h2>DX.{n} — {nom}</h2>",
        ilot(None, "", essentiel, essentiel=True),
        sommaire(),
    ]
    titres = [
        "Définition", "Épidémiologie", "Physiopathologie", "Démarche diagnostique",
        "Anamnèse et drapeaux rouges", "Examen physique", "Approche syndromique",
        "Diagnostic positif", "Examens complémentaires", "Arbre décisionnel",
        "Prise en charge en Suisse", "Prévention", "Points clés", "Pièges d'examen",
    ]
    for i, (titre, texte) in enumerate(zip(titres, pts), 1):
        blocs.append(ilot(i, titre, texte, wins.get(i, "")))
    blocs.append(sources())
    sous = f"DX.{n} du cours F1.5. Le rang d'exclusion n'est pas le numéro DX. Texte du 31.10.2026."
    html = page(f"DX.{n} — {nom}", nom, sous, blocs, f"FIN_FICHIER LOT_134_Phase_B_DX.{n}")
    return ecrire(f"LOT_134_Phase_B_V0_DX.{n}.html", html)


def dx1():
    q_bonn = C("BONN", "13.4% (11.6% men, 14.9% women) had pitting edema of the lower limbs at the time of the investigation (C3).")
    q_fr = C("BONN", "C3 was found in 1.1% and 2.2% of males and females, respectively")
    q_var = C("BONN", "differences in the prevalence of C3, which varied between 1.1% and 14.9%.")
    q_tt = C("BONN", "The most frequent therapy was compression stockings followed by venous surgery and drug treatment.")
    essentiel = (
        "L'œdème veineux chronique est un godet des jambes, souvent bilatéral, dans une maladie veineuse. "
        "Un début aigu sur une seule jambe fait chercher une thrombose avant d'accepter ce diagnostic. "
        "À Bonn, le traitement le plus fréquent était la contention."
    )
    pts = [
        "Le stade C3 de la classification clinique, étiologique, anatomique et physiopathologique (CEAP) désigne un œdème qui prend le godet. "
        "La page de Bonn le constate à l'examen, sans exiger un ulcère. "
        "Une définition suisse séparée de cette classification n'a pas été lue : À vérifier.",
        "À Bonn, 3072 adultes de 18 à 79 ans ont été examinés entre novembre 2000 et mars 2002. "
        f"Le godet concernait 13,4 % d'entre eux{S(3)}. "
        "En France, le même stade était beaucoup plus rare. La méthode change le chiffre.",
        "La pression veineuse élevée laisse filtrer du liquide vers le tissu sous-cutané. "
        "Le godet montre que ce liquide est encore mobile sous le doigt. "
        "Le détail moléculaire n'est pas dans les pages lues : À vérifier.",
        "Ce diagnostic est DX.1 parce que c'est le signe de population le plus fréquent des dix. "
        "Son rang d'exclusion est E10 : on ne le retient qu'après les urgences. "
        "Un œdème unilatéral ou très aigu quitte cette voie.",
        "On date le début, le côté, la station debout, la chaleur et l'essoufflement. "
        "Une seule jambe, en quelques heures, oriente vers une thrombose. "
        "Le score clinique de cette thrombose n'a pas été relu : À vérifier.",
        "On presse le tibia et la malléole, puis on compare les deux jambes. "
        "On note la chaleur, un cordon et l'état de la peau. "
        "Le godet mou et bilatéral, sans inflammation, oriente vers la maladie veineuse.",
        "Le syndrome est celui des parties molles, pas une masse ni une défense abdominale. "
        "Un lymphœdème dur ne prend pas le godet de la même façon. "
        "La part exacte du lymphœdème parmi ces œdèmes n'est pas chiffrée ici : À vérifier.",
        "Le diagnostic positif est un godet bilatéral et chronique, une fois la thrombose écartée. "
        "Il ne se pose pas sur un seul mollet ni sur une photo. "
        "L'échodoppler veineux tranche si le doute clinique reste.",
        "Il n'y a pas de prise de sang unique pour ce signe. "
        "L'échodoppler se discute si l'œdème est unilatéral, aigu, ou si la contention ne suffit pas. "
        "Le délai suisse de cet examen n'a pas été lu : À vérifier.",
        "Regarder d'abord le côté et le délai. "
        "Unilatéral et aigu : thrombose jusqu'à preuve du contraire. "
        "Bilatéral, chronique, avec godet : contention, puis nouvelle évaluation.",
        "Aucune dose en milligrammes n'est écrite pour cet œdème. "
        f"La contention venait en tête des traitements à Bonn, devant la chirurgie et le médicament{S(3)}. "
        "Un diurétique à la place n'est pas décrit. Une interdiction formelle suisse est À vérifier.",
        "La marche et la contention, chez une personne déjà au stade C3, sont les mesures lues. "
        "Aucun protocole suisse chiffré n'a été ouvert : À vérifier. "
        "Cette leçon ne crée pas un dépistage de population.",
        "Godet bilatéral et chronique : penser contention. "
        "Un seul côté : penser thrombose. "
        "Le chiffre de Bonn ne se transporte pas tel quel à l'étude française.",
        f"Trois questions ferment ce diagnostic. Les réponses sont dans la {B('w-pieges', 'fenêtre')}.",
    ]
    w = fenetre(
        "w-chiffres",
        "Chiffres lus, avec leur dénominateur",
        f"<p>{q_bonn}{S(3)}</p><p>{q_fr}{S(3)}</p><p>{q_var}{S(3)}</p><p>{q_tt}{S(3)}</p>",
    )
    wins = {
        2: w,
        14: quizzes([
            ("Un godet d'un seul côté, apparu hier, est-il veineux chronique ?", "Non comme premier nom. Ce profil fait chercher une thrombose. Le score de cette thrombose est À vérifier."),
            ("Le diurétique est-il le traitement lu ?", "Non. À Bonn, la contention était le traitement le plus fréquent. Une interdiction suisse du diurétique n'a pas été lue."),
            ("13,4 % et 1,1 %, pourquoi deux chiffres ?", "Bonn et l'étude française n'ont pas la même méthode. La page dit que le stade C3 varie de 1,1 % à 14,9 %."),
        ]),
    }
    return lecon(1, essentiel, pts, wins)


def dx2():
    q_pal = C("AAA", "abdominal palpation has a sensitivity ranging from 33% to 100%, specificity from 75% to 100%, and positive predictive value from 14% to 100%.")
    q_non = C("AAA", "Therefore, abdominal palpation is not reliable for the diagnosis of AAA.")
    q_def = C("AAA", "a fixed threshold diameter of 30 mm or more is used to define an AAA")
    q_us = C("AAA", "Abdominal US and duplex ultrasound (DUS) are first line imaging tools for the detection and management of small AAAs, with high (> 97%) sensitivity and specificity.")
    q_fuite = C("AAA", "its sensitivity to detect retroperitoneal haemorrhage is low.")
    q_inst = C("AAA", "the presence of an AAA in an unstable patient is very suggestive of a rAAA.")
    q_prev = C("AAA", "The prevalence in 65 year old men 2006 – 2009 was 1.7% in the Swedish Screening Programme")
    essentiel = (
        "L'anévrisme de l'aorte abdominale est une dilatation focale, fixée en pratique à 30 mm ou plus. "
        "La main peut sentir un battement, mais elle ne fait pas le diagnostic. "
        "Chez un patient instable, voir l'anévrisme à l'échographie suggère fortement la rupture."
    )
    pts = [
        "En pratique clinique, le seuil lu est un diamètre de 30 mm ou plus. "
        "Une aorte battante chez une personne maigre peut être normale. "
        f"Le {B('w-def', 'passage')} de la recommandation européenne de 2024 fixe ce seuil et juge la palpation.",
        "Chez les hommes de 65 ans, la Suède rapportait 1,7 % entre 2006 et 2009, plus 0,5 % déjà connus. "
        "Le Royaume-Uni rapportait 1,3 % entre 2009 et 2013. "
        f"Les deux programmes nationaux sont sous 1 % en 2020-2021{S(4)}. Le chiffre suisse est À vérifier.",
        "La paroi se dilate et peut se rompre vers le rétro-péritoine. "
        "Le risque de rupture augmente avec le diamètre. "
        "Les pourcentages annuels par taille n'ont pas été recopiés ici au-delà de ce principe : À vérifier pour un tableau complet.",
        "Ce diagnostic est DX.2, avec le rang d'exclusion E4. "
        "Une douleur et une instabilité le font passer avant les signes fréquents. "
        "Un battement isolé, sans douleur, n'est pas une rupture.",
        "Douleur abdominale ou lombaire, malaise, syncope et chute de tension sont les drapeaux. "
        "La recommandation de 2024 définit l'instabilité par une perte de conscience ou une pression systolique sous 80 mmHg. "
        "Ce seuil se lit dans le chapitre de la rupture, pas dans la palpation de routine.",
        "On cherche une masse pulsatile, en sachant que la sensibilité va de 33 à 100 %. "
        "La spécificité va de 75 à 100 %, et la valeur prédictive positive de 14 à 100 %. "
        f"La même recommandation conclut que la palpation n'est pas fiable{S(4)}.",
        "Le syndrome est celui d'une masse battante, pas d'un godet ni d'une défense. "
        "La douleur avec instabilité change le syndrome : on ne palpe plus pour rassurer. "
        "On passe à l'image et à l'équipe vasculaire.",
        "Le diagnostic positif du petit anévrisme est l'échographie, pas la main. "
        "La sensibilité et la spécificité dépassent 97 % pour le petit anévrisme. "
        "La rupture, elle, se confirme par l'angioscanner dès que l'état le permet.",
        "L'échographie d'urgence voit l'anévrisme, pas le saignement rétropéritonéal. "
        "Sa sensibilité pour cette hémorragie est basse. "
        "Elle ne dit pas non plus si l'anatomie convient à un traitement endovasculaire.",
        "Patient instable et anévrisme vu : la rupture est très probable. "
        "S'il peut passer au scanner, l'angioscanner thoraco-abdominal et des axes d'accès est l'examen clé. "
        "S'il ne le peut pas, la voie est le bloc, selon la recommandation lue.",
        "Aucune dose médicamenteuse n'est écrite dans cette leçon. "
        "L'anticoagulation d'urgence et l'hypotension permissive ont des recommandations propres, non recopiées en milligrammes. "
        "Le produit suisse, s'il est choisi, se lit dans son information professionnelle : À vérifier pour la spécialité retenue.",
        "Le dépistage échographique des populations à haut risque est de classe I. "
        "La cible n'est plus fixée dans la recommandation de 2024 : elle dépend des conditions locales. "
        "La palpation n'est pas l'outil de ce dépistage. Le programme suisse est À vérifier.",
        "Trente millimètres définissent l'anévrisme en pratique. "
        "La main ne suffit pas. "
        "Instabilité plus anévrisme à l'échographie : penser rupture, sans attendre de voir le sang.",
        f"Quatre questions. Les réponses sont dans la {B('w-pieges', 'fenêtre')}.",
    ]
    gloss = "<p>Anévrisme de l'aorte abdominale (AAA). Anévrisme rompu (rAAA). Échographie (US). Échodoppler duplex (DUS).</p>"
    wins = {
        1: fenetre("w-def", "Seuil et palpation", gloss + f"<p>{q_def}{S(4)}</p><p>{q_pal}{S(4)}</p><p>{q_non}{S(4)}</p>"),
        2: fenetre("w-prev", "Dépistages lus", f"<p>{q_prev}{S(4)}</p><p>Le texte ajoute 0,5 % déjà connus en Suède, 1,3 % au Royaume-Uni, et moins de 1 % dans les deux programmes en 2020-2021.</p>"),
        6: fenetre("w-echo", "Image", f"<p>{q_us}{S(4)}</p><p>{q_fuite}{S(4)}</p><p>{q_inst}{S(4)}</p>"),
        14: quizzes([
            ("Sentir l'aorte, est-ce l'anévrisme ?", "Pas à soi seul. La sensibilité de la palpation va de 33 à 100 %. L'échographie dépasse 97 % pour le petit anévrisme."),
            ("L'échographie voit-elle le saignement ?", "Mal. Sa sensibilité pour l'hémorragie rétropéritonéale est basse. Elle voit l'anévrisme."),
            ("Quel seuil d'instabilité est écrit ?", "Perte de conscience, ou pression systolique sous 80 mmHg, dans le chapitre de la rupture."),
            ("Le dépistage vise-t-il un âge unique ?", "La classe I vise les populations à haut risque. La cible locale n'est plus fixée dans la recommandation de 2024."),
        ]),
    }
    return lecon(2, essentiel, pts, wins)


def dx3():
    q = C("RMS", "Environ 5 % des patients consultant dans un centre d’urgences pour des douleurs abdominales aiguës ont une cholécystite.")
    q2 = C("RMS", "Le signe de Murphy, douleur bloquant la respiration à la palpation de l’hypochondre droit, est un examen peu discriminatif")
    q3 = C("RMS", "Aucune combinaison de symptômes et / ou de signes cliniques ne permet de poser un diagnostic de cholécystite avec certitude.")
    essentiel = (
        "La cholécystite aiguë est une inflammation de la vésicule, souvent après un calcul. "
        "Elle représente environ 5 % des douleurs abdominales aiguës aux urgences. "
        "Aucun assemblage de signes cliniques ne la prouve seul."
    )
    pts = [
        "C'est une inflammation aiguë de la paroi vésiculaire, en règle après obstruction du canal cystique. "
        "La Revue Médicale Suisse n'en donne pas une définition de société séparée. "
        "Le diagnostic de certitude n'est pas clinique.",
        f"Environ 5 % des patients vus aux urgences pour une douleur abdominale aiguë ont une cholécystite{S(2)}. "
        "L'incidence en population générale n'est pas dans cet article : À vérifier. "
        "Ce n'est pas le motif le plus rare, ni le plus fréquent, des dix diagnostics.",
        "Un calcul bloque le cystique. La paroi s'irrite, puis s'infecte. "
        "La main trouve une douleur de l'hypocondre droit qui peut bloquer l'inspiration. "
        "Ce blocage ne suffit pas, comme le dit l'article.",
        "Ce diagnostic est DX.3, rang d'exclusion E7. "
        "Il vient après les urgences vitales du tableau, devant l'œdème et souvent devant le foie chronique. "
        "Une défense généralisée fait quitter cette hypothèse.",
        "Douleur de l'hypocondre droit, fièvre, vomissement et intolérance alimentaire ouvrent l'histoire. "
        "Un ictère ou une chute de tension élargit le diagnostic vers une complication biliaire. "
        "La femme en âge de procréer : la démarche du dosage de grossesse est À vérifier dans une règle suisse non lue.",
        "On palpe l'hypocondre droit en inspiration. "
        f"Le signe de Murphy est peu discriminatif{S(2)}. "
        "On cherche aussi une défense locale, sans la confondre avec une contracture de tout l'abdomen.",
        "Le syndrome est une douleur focale de l'étage sus-mésocolique droit. "
        "Il se sépare de la douleur migrée vers la fosse iliaque droite. "
        "Il se sépare aussi d'une masse pulsatile médiane.",
        "Le diagnostic positif n'est pas le Murphy. "
        "L'échographie montre la paroi, le calcul et le liquide, selon la pratique courante. "
        "Les critères échographiques exacts d'une recommandation suisse sont À vérifier.",
        "L'échographie est l'examen de première ligne lu dans l'enseignement suisse de cet article, qui insiste sur la clinique insuffisante. "
        "La biologie seule ne nomme pas la vésicule. "
        "Le scanner se discute si l'échographie ne répond pas : le seuil suisse est À vérifier.",
        "Douleur de l'hypocondre droit : ne pas conclure sur le Murphy. "
        "Demander l'échographie. "
        "Si la paroi de tout l'abdomen se défend, revenir aux urgences E1 à E4.",
        "L'antalgie, si le paracétamol est choisi, suit l'information professionnelle suisse déjà citée en Phase A. "
        "Elle n'est pas répétée ici. "
        "L'antibiotique et le moment de la cholécystectomie n'ont pas leur milligramme ni leur heure suisse dans les sources de ce diagnostic : À vérifier.",
        "La prévention des calculs n'est pas un programme lu ici : À vérifier. "
        "Reconnaître tôt la douleur de l'hypocondre droit évite de rassurer sur un Murphy isolé. "
        "Aucun chiffre de prévention suisse n'est écrit.",
        "Cinq pour cent des douleurs abdominales aiguës aux urgences. "
        "Murphy peu discriminatif. "
        "Aucune combinaison clinique ne suffit.",
        f"Trois questions, réponses dans la {B('w-pieges', 'fenêtre')}.",
    ]
    wins = {
        2: fenetre("w-rms", "Ce que dit la Revue Médicale Suisse", f"<p>{q}{S(2)}</p><p>{q3}{S(2)}</p><p>{q2}{S(2)}</p>"),
        14: quizzes([
            ("Le Murphy affirme-t-il la cholécystite ?", "Non. L'article le juge peu discriminatif. Aucune combinaison clinique ne donne la certitude."),
            ("Quelle part aux urgences ?", "Environ 5 % des douleurs abdominales aiguës. L'incidence en population est À vérifier."),
            ("Où est la dose d'antibiotique ?", "Pas dans cette leçon. Elle se lirait dans l'information professionnelle suisse du produit choisi."),
        ]),
    }
    return lecon(3, essentiel, pts, wins)


def dx4():
    q = C("RMS", "La prévalence des appendicites parmi les consultations ambulatoires pour douleurs abdominales aiguës en MPR est estimée à 1 % alors que l’incidence dans la population générale est de 9 cas pour 100 000 personnes par année.")
    q4 = C("RMS", "Un score < 4 permet en principe d’éviter une intervention chirurgicale.")
    q7 = C("RMS", "Un score ≥ 7 est fortement évocateur d’une appendicite et devrait orienter vers une stratégie opératoire (RV+ 3,1 ; RV- 0,26).")
    essentiel = (
        "L'appendicite aiguë est l'inflammation de l'appendice. "
        "Elle fait environ 1 % des douleurs abdominales aiguës en premier recours, et 9 cas pour 100 000 personnes par année. "
        "L'absence des signes classiques ne l'exclut pas."
    )
    pts = [
        "C'est l'inflammation aiguë de l'appendice iléo-cæcal. "
        "L'article suisse de 2016 ne cite pas une définition d'une société mondiale unique. "
        "Le diagnostic ne repose pas sur un seul point de McBurney.",
        f"En médecine de premier recours, environ 1 % des douleurs abdominales aiguës sont une appendicite{S(2)}. "
        "L'incidence lue est de 9 cas pour 100 000 personnes et par année. "
        "Ces deux dénominateurs ne doivent pas être additionnés.",
        "La lumière s'obstrue, la paroi s'infecte, le péritoine voisin s'irrite. "
        "La douleur peut migrer vers la fosse iliaque droite. "
        "Cette migration manque souvent : l'article le rappelle en disant que les signes typiques ne sont pas constants.",
        "Ce diagnostic est DX.4, rang d'exclusion E6. "
        "Il passe après la perforation déjà généralisée et après l'ischémie. "
        "Une fosse iliaque droite douloureuse n'écarte pas ces deux urgences si le tableau est plus grave.",
        "On cherche la migration, la fièvre, les vomissements, l'anorexie et la toux douloureuse. "
        "Chez la femme, une grossesse extra-utérine reste un drapeau. "
        "La règle suisse du dosage avant l'image est À vérifier.",
        "On palpe en partant du côté non douloureux. "
        "La défense locale se note, ainsi que la douleur à la décompression. "
        "Un ventre souple n'a pas la même valeur qu'une contracture.",
        "Le syndrome est une irritation péritonéale focale, souvent à droite et en bas. "
        "Il se distingue d'une douleur d'hypocondre droit. "
        "Il se distingue d'une masse médiane battante.",
        "Le diagnostic positif combine la clinique et l'imagerie. "
        f"Le score d'Alvarado aide à trier, il ne remplace pas l'image{S(2)}. "
        "Un score d'au moins 7 oriente vers une stratégie opératoire. Un score sous 4 évite en principe la chirurgie.",
        "L'article donne un rapport de vraisemblance positif de 3,1 et un rapport négatif de 0,26 pour le seuil de 7. "
        "Le choix entre échographie et scanner, en Suisse, n'est pas détaillé dans cette page : À vérifier. "
        "La biologie seule ne confirme pas l'appendice.",
        "Score sous 4 : ne pas opérer sur ce seul chiffre, dit l'article, en principe. "
        "Score d'au moins 7 : orienter vers la chirurgie, sans oublier l'image selon le circuit local. "
        "Entre les deux, la clinique continue et l'examen se répète.",
        "Pas de milligramme d'antibiotique dans cette leçon. "
        "Le paracétamol, s'il est utilisé, reste celui de la Phase A. "
        "L'heure de l'appendicectomie et la durée d'antibiotique se lisent dans une recommandation non ouverte ici : À vérifier.",
        "Il n'y a pas de dépistage de l'appendicite. "
        "La prévention utile est de ne pas écarter le diagnostic quand les signes classiques manquent. "
        "Aucun chiffre de retard évitable n'a été lu : À vérifier.",
        "Un pour cent des douleurs aiguës en premier recours. "
        "Neuf pour 100 000 par année. "
        "Alvarado : sous 4, en principe pas de chirurgie. À partir de 7, orientation opératoire.",
        f"Trois questions, réponses dans la {B('w-pieges', 'fenêtre')}.",
    ]
    wins = {
        2: fenetre(
            "w-app",
            "Chiffres et score",
            "<p>Médecine de premier recours (MPR). Rapport de vraisemblance (RV).</p>"
            f"<p>{q}{S(2)}</p><p>{q4}{S(2)}</p><p>{q7}{S(2)}</p>",
        ),
        14: quizzes([
            ("L'absence de migration exclut-elle l'appendicite ?", "Non. Les signes typiques ne sont pas constants. L'incidence lue reste 9 pour 100 000 par année."),
            ("Que fait un Alvarado à 3 ?", "En principe, il permet d'éviter la chirurgie. Ce n'est pas une certitude isolée du reste de l'examen."),
            ("Que vaut un score d'au moins 7 ?", "Il est fortement évocateur. Le rapport de vraisemblance positif est de 3,1 et le rapport négatif de 0,26."),
        ]),
    }
    return lecon(4, essentiel, pts, wins)


def dx5():
    essentiel = (
        "La cirrhose est une fibrose diffuse du foie qui désorganise l'architecture. "
        "Un bord palpable ne prouve pas l'hépatomégalie, et encore moins la cirrhose. "
        "La prévalence suisse ou européenne n'a pas été lue dans cette session : À vérifier."
    )
    pts = [
        "La cirrhose est le stade d'une maladie chronique du foie où la fibrose remplace l'architecture. "
        "Aucune définition d'une société mondiale n'a été ouverte pour cette leçon : À vérifier. "
        "Le signe palpé n'est qu'un bord, une rate ou un flot, pas le diagnostic histologique.",
        "La prévalence de la cirrhose elle-même est À vérifier. "
        "L'article suisse estime à 5 % la prévalence de l'ascite en médecine de premier recours, ce qui n'est pas le même dénominateur. "
        "Ce 5 % sert à chercher l'ascite, pas à classer la cirrhose parmi les maladies rares ou fréquentes.",
        "La fibrose augmente la pression portale. "
        "La rate peut grossir, et le liquide peut s'accumuler dans le ventre. "
        "Palper un bord bas ne mesure pas cette pression.",
        "Ce diagnostic est DX.5, rang d'exclusion E9. "
        "Il vient tard dans les urgences, parce qu'un foie chronique tue moins vite qu'une ischémie ou une fasciite. "
        "Une douleur aiguë sur ce terrain fait quand même chercher ces urgences.",
        "On cherche une histoire d'hépatite, d'alcool, un périmètre qui augmente, une prise de poids et un œdème des chevilles. "
        "L'article cite aussi l'insuffisance cardiaque, le syndrome néphrotique et une néoplasie devant une ascite. "
        "Ces causes ne sont pas des cirrhoses.",
        "La hauteur clinique normale du foie va de 6 à 12 cm selon la taille. "
        "Palper un foie a un rapport de vraisemblance positif de seulement 2 pour l'hépatomégalie. "
        "Ne pas le palper n'exclut pas l'hépatomégalie : le rapport négatif est de 0,4. La rate normale, elle, ne se palpe pas.",
        "Trois syndromes se touchent : organomégalie, ascite, et parfois une masse si un cancer s'ajoute. "
        "Le flot est le meilleur test clinique de l'ascite, dit l'article. "
        "Un flot absent n'exclut pas une ascite peu abondante.",
        "Le diagnostic positif de la cirrhose n'est pas le bord palpé. "
        "L'échographie et, si besoin, une évaluation spécialisée viennent ensuite. "
        "Les critères non invasifs suisses exacts sont À vérifier.",
        "L'échographie cherche le contour, la rate, l'ascite et le flux porte. "
        "La biologie hépatique ne remplace pas l'image. "
        "La ponction d'ascite, ses indications et ses délais sont À vérifier dans une règle suisse non lue ici.",
        "Mesurer la hauteur avant de dire qu'un foie est gros. "
        "Chercher la rate et le flot si l'histoire est chronique. "
        "Une douleur aiguë disproportionnée ramène vers l'ischémie ou la péritonite, même sur ce terrain.",
        "Le paracétamol de Dafalgan comprimés, numéro 69266, est contre-indiqué dans la cirrhose avec ascite. "
        "La maladie hépatique chronique limite la journée à 2 g, phrase lue dans la même information professionnelle. "
        "Aucun autre milligramme, diurétique compris, n'est écrit ici.",
        "Éviter ce qui aggrave le foie dépend de la cause, non lue cas par cas : À vérifier. "
        "Ne pas donner le paracétamol habituel à pleine dose sur ce terrain est la prévention médicamenteuse lue. "
        "La vaccination et le sevrage ont leurs propres textes, non ouverts ici.",
        "Bord palpable n'égale pas hépatomégalie, ni cirrhose. "
        "Hauteur de 6 à 12 cm. "
        "Ascite et cirrhose : pas le paracétamol de cette information professionnelle.",
        f"Quatre questions, réponses dans la {B('w-pieges', 'fenêtre')}.",
    ]
    # Fix CI quote source: it is AIPS text stored in extraits, not RMS.
    # Rebuilt below if C() was wrong — handled by dedicated quote from gzip in dx5_quotes.
    return essentiel, pts


def main():
    # Validate AIPS quotes against the gzip, then build all lessons.
    import gzip
    aips = " ".join(gzip.open("/workspace/ressources_ia/aips/fi_fr/69266.txt.gz", "rt", encoding="utf-8").read().split())
    CORPUS["AIPS"] = aips
    # dx5 used a wrong key; rebuild cirrhosis after corpus is ready.
    dx1(); dx2(); dx3(); dx4()
    dx5_build()
    dx6(); dx7(); dx8(); dx9(); dx10()
    preuves()
    print("dix fichiers écrits")


def dx5_build():
    qh = C("RMS", "La hauteur normale du foie se situe entre 6-12 cm selon la taille du patient.")
    qrv = C("RMS", "Le fait de palper ou non un foie a une mauvaise corrélation avec une hépatomégalie puisque dans ce cas le rapport de vraisemblance (RV+) n’est que de 2.")
    qrv2 = C("RMS", "l’absence de détection du foie à la palpation n’exclut pas une hépatomégalie : rapport de vraisemblance négatif (RV-) de 0,4.")
    qr = C("RMS", "En condition normale, la rate ne doit pas être palpable.")
    qasc = C("RMS", "En MPR, sa prévalence est estimée à 5 %.")
    qci = C("AIPS", "Troubles fonctionnels hépatiques graves (cirrhose hépatique et ascite)/hépatite aiguë ou maladie hépatique décompensée active.")
    q2g = C("AIPS", "La dose quotidienne ne doit pas dépasser 2 g")
    essentiel, pts = dx5()
    wins = {
        6: fenetre(
            "w-foie",
            "Foie, rate, ascite",
            "<p>Rapport de vraisemblance (RV). Médecine de premier recours (MPR).</p>"
            f"<p>{qh}{S(2)}</p><p>{qrv}{S(2)}</p><p>{qrv2}{S(2)}</p><p>{qr}{S(2)}</p>"
            "<p>La phrase suivante parle de l'ascite dans l'article, pas de la prévalence de la cirrhose.</p>"
            f"<p>{qasc}{S(2)}</p>",
        ),
        11: fenetre(
            "w-aips",
            "Paracétamol et foie",
            "<p>Information professionnelle suisse (AIPS).</p>"
            f"<p>{qci}{S(8)}</p><p>{q2g}{S(8)}</p>"
            "<p>La phrase sur 2 g suit, dans le texte, l'énumération de la maladie hépatique chronique, de l'alcoolisme, de la dénutrition, de la déshydratation et de la cachexie.</p>",
        ),
        14: quizzes([
            ("Un bord de foie palpable est-il une cirrhose ?", "Non. Il ne prouve même pas l'hépatomégalie. Le rapport de vraisemblance positif n'est que de 2."),
            ("Ne pas palper le foie rassure-t-il ?", "Non. Le rapport de vraisemblance négatif est de 0,4. La rate normale, en revanche, ne se palpe pas."),
            ("Le 5 % de l'article, c'est la cirrhose ?", "Non. C'est l'estimation de l'ascite en médecine de premier recours. La prévalence de la cirrhose est À vérifier."),
            ("Paracétamol et ascite ?", "L'information de Dafalgan comprimés 69266 contre-indique la cirrhose hépatique et l'ascite. La journée maximale lue dans la maladie hépatique chronique est 2 g."),
        ]),
    }
    return lecon(5, essentiel, pts, wins)


def dx6():
    essentiel = (
        "L'adénopathie périphérique maligne est un ganglion dont la cause est un cancer, du ganglion ou d'ailleurs. "
        "La part de malignité en premier recours n'a pas été lue : À vérifier. "
        "On décrit le ganglion comme une masse avant de le nommer."
    )
    pts = [
        "C'est un ganglion périphérique dont l'origine est maligne, locale ou métastatique. "
        "Aucune définition d'une société savante n'a été ouverte pour ce diagnostic : À vérifier. "
        "Le signe, lui, est une masse : localisation, dimension, forme, consistance, sensibilité et mobilité.",
        "La proportion de cancers parmi les ganglions palpés en premier recours est À vérifier. "
        "Ce diagnostic est placé en DX.6 faute d'un dénominateur commun avec les autres. "
        "Ce rang de fréquence n'est pas une méta-analyse.",
        "Une cellule tumorale envahit le ganglion, ou le ganglion est le cancer lui-même. "
        "La consistance devient dure et la mobilité diminue. "
        "Ces deux caractères ne prouvent pas le cancer à eux seuls.",
        "Ce diagnostic est DX.6, rang d'exclusion E8. "
        "Il passe après les infections qui détruisent en quelques heures. "
        "Un ganglion sus-claviculaire ne se rassure pas, même si le mécanisme exact du drainage n'est pas requantifié ici.",
        "On note l'âge, la fièvre, les sueurs, l'amaigrissement chiffré et le territoire. "
        "Un ganglion dur, fixé, ou sus-claviculaire est un drapeau. "
        "La durée exacte qui impose une biopsie n'a pas été lue : À vérifier.",
        "On palpe les chaînes cervicales, sus-claviculaires, axillaires et inguinales. "
        "On mesure en centimètres, on teste la mobilité et la douleur. "
        "On compare au côté opposé.",
        "Le syndrome est celui d'une masse superficielle, pas d'un godet ni d'une défense. "
        "Une chaleur et une fluctuation orientent vers un abcès, qui n'est pas ce diagnostic. "
        "La crépitation, elle, oriente vers la fasciite.",
        "Le diagnostic positif n'est pas l'antibiotique d'épreuve. "
        "Il vient de l'histologie, décidée avec le spécialiste. "
        "Répéter une antibiothérapie sans diagnostic n'est pas une conduite lue : À vérifier comme règle suisse écrite.",
        "L'échographie décrit la taille et la structure. "
        "La biologie ne nomme pas le cancer. "
        "Le choix entre cytoponction et biopsie, et son délai, sont À vérifier.",
        "Décrire, mesurer, puis ne pas traiter à l'aveugle. "
        "Sus-claviculaire : documenter. "
        "Si la peau crépite ou si l'articulation est chaude, quitter ce diagnostic pour E1 ou E5.",
        "Pas de milligramme dans cette leçon. "
        "Un antibiotique choisi ailleurs se lit dans son information professionnelle suisse. "
        "Il ne sert pas de test diagnostique à répétition.",
        "La prévention n'est pas un dépistage de tous les ganglions. "
        "Elle est de ne pas laisser un ganglion dur sans explication. "
        "Aucun programme suisse chiffré n'a été lu : À vérifier.",
        "Décrire avant de nommer. "
        "Pas d'antibiotique d'épreuve à répétition. "
        "La part de malignité reste À vérifier.",
        f"Trois questions, réponses dans la {B('w-pieges', 'fenêtre')}.",
    ]
    wins = {
        14: quizzes([
            ("Un ganglion mou et douloureux est-il un cancer ?", "Pas sur ce seul caractère. La malignité devient plus probable s'il est dur, fixé, ou sus-claviculaire. La part exacte est À vérifier."),
            ("L'antibiotique d'épreuve confirme-t-il le bénin ?", "Non dans cette leçon. Répéter l'antibiotique sans diagnostic n'est pas une conduite sourcée ici."),
            ("Où est le délai de biopsie ?", "À vérifier. Il n'a pas été lu dans une recommandation suisse pendant cette session."),
        ]),
    }
    return lecon(6, essentiel, pts, wins)


def dx7():
    q9 = C("SA", "Recommendation 9-Except where there are signs of immediate severity (sepsis with SOFA ≥2), antibiotic therapy should not be prescribed before joint aspiration is performed to analyze the synovial fluid.")
    qsof = C("SA", "In the presence of at least 2 of the following signs: respiratory rate >22/min, impaired alertness and/or SBP <100 mmHg (quick SOFA ≥2)")
    qcef = C("SA", "it is advisable to prescribe an injectable 1st generation cephalosporin (1GC) (cefazolin) for patients under the age of 70")
    q3 = C("SA", "prioritize an injectable third generation cephalosporin (3GC) (ceftriaxone or cefotaxime) for patients over 70")
    essentiel = (
        "L'arthrite septique est l'infection d'une articulation native par une bactérie. "
        "L'incidence n'a pas été lue : À vérifier. "
        "On ponctionne avant l'antibiotique, sauf gravité immédiate."
    )
    pts = [
        "C'est l'infection bactérienne d'une articulation native de l'adulte. "
        "Les recommandations françaises de 2020 en font un diagnostic à documenter par la ponction. "
        "Une prothèse n'est pas le sujet de ce texte.",
        "L'incidence en Suisse ou en Europe n'est pas dans les pages lues : À vérifier. "
        "Le rang DX.7 vient de cette absence de dénominateur, pas d'un calcul. "
        "Le rang d'exclusion E5 rappelle que c'est une urgence, même si le chiffre manque.",
        "La bactérie atteint la synoviale. "
        "Le cartilage se détruit vite si le pus reste. "
        "La chaleur, la tension et la douleur sont le reflet de cet épanchement.",
        "Ce diagnostic est DX.7, rang E5. "
        "Il passe après la fasciite et la péritonite, avant l'appendicite dans l'ordre d'exclusion. "
        "Une articulation chaude ne fait pas oublier une crépitation des parties molles.",
        "Fièvre, frissons, et une articulation unique, chaude et tendue. "
        "Au moins deux signes parmi une fréquence respiratoire au-dessus de 22, une vigilance altérée, et une pression systolique sous 100 mmHg définissent le quick score à 2 ou plus. "
        "On évalue alors le score de défaillance, sans attendre la culture.",
        "On compare à l'autre côté, on cherche un épanchement et une douleur au moindre mouvement. "
        "La peau autour se regarde : une crépitation n'est plus une arthrite simple. "
        "On ne ponctionne pas à travers une peau infectée si une autre voie existe : cette précision opératoire est À vérifier.",
        "Le syndrome est articulaire, pas un godet des deux jambes ni une défense abdominale. "
        "La fluctuation et la chaleur le séparent d'un ganglion. "
        "La douleur au mouvement le sépare d'une cellulite qui n'atteint pas la capsule.",
        "Le diagnostic positif est le liquide synovial, avec culture et examen direct. "
        "Un liquide clairement purulent, sans cristal, peut faire démarrer l'antibiotique probabiliste, dit la recommandation 9. "
        "Ce n'est pas le cas habituel : en principe, on attend le prélèvement.",
        "Hémocultures et ponction avant l'antibiotique, sauf gravité immédiate. "
        "La gravité immédiate est un sepsis avec un score de défaillance d'au moins 2. "
        "L'imagerie ne remplace pas le liquide.",
        "Pas de gravité immédiate : pas d'antibiotique avant la ponction. "
        "Gravité immédiate : antibiotique probabiliste, surveillance, et parfois une unité de soins continus. "
        "Le nom du produit français est cité plus bas. Le milligramme suisse est À vérifier.",
        "Sous 70 ans, le texte français conseille une céphalosporine injectable de première génération, la céfazoline. "
        "Au-dessus de 70 ans, il privilégie la ceftriaxone ou le céfotaxime, céphalosporines de troisième génération. "
        "Aucune dose en milligrammes n'est recopiée. Elle se lit dans l'information professionnelle suisse du produit.",
        "La prévention d'une arthrite sur articulation native n'est pas un programme lu ici : À vérifier. "
        "La mesure utile est de ponctionner avant de masquer la culture. "
        "Les gestes sur prothèse sont un autre chapitre.",
        "Ponction d'abord, sauf score de défaillance d'au moins 2. "
        "Pas de milligramme inventé. "
        "L'incidence reste À vérifier.",
        f"Quatre questions, réponses dans la {B('w-pieges', 'fenêtre')}.",
    ]
    wins = {
        5: fenetre(
            "w-sofa",
            "Gravité et ponction",
            "<p>Score séquentiel d'évaluation des défaillances d'organe (SOFA). Pression artérielle systolique (SBP).</p>"
            f"<p>{qsof}{S(7)}</p><p>{q9}{S(7)}</p><p>{qcef}{S(7)}</p><p>{q3}{S(7)}</p>",
        ),
        14: quizzes([
            ("Antibiotique avant la ponction ?", "Non, sauf gravité immédiate avec un score de défaillance d'au moins 2. Un liquide clairement purulent sans cristal est l'autre exception lue."),
            ("Que veut dire le quick score à 2 ?", "Au moins deux signes parmi fréquence respiratoire au-dessus de 22, vigilance altérée, et pression systolique sous 100 mmHg."),
            ("Quelle molécule sous 70 ans ?", "La céfazoline, céphalosporine de première génération, dans le texte français. La dose suisse en milligrammes est À vérifier."),
            ("Et après 70 ans ?", "Ceftriaxone ou céfotaxime, dans le même texte. Toujours sans milligramme recopié."),
        ]),
    }
    return lecon(7, essentiel, pts, wins)


def dx8():
    q = C("RMS", "Il faut également rechercher des signes de péritonite localisée ou généralisée : signes de défense, de détente ou l’absence de bruits digestifs qui peuvent annoncer une pathologie grave telle qu’une perforation digestive.")
    essentiel = (
        "La péritonite aiguë généralisée est l'inflammation de tout le péritoine, en règle après une perforation. "
        "La défense, la détente et le silence auscultatoire l'annoncent. "
        "Aucune incidence séparée n'a été lue : À vérifier."
    )
    pts = [
        "C'est l'inflammation aiguë de l'ensemble de la cavité péritonéale. "
        "L'article suisse la relie à une perforation digestive quand la défense, la détente ou le silence sont là. "
        "Une définition histologique séparée n'a pas été ouverte : À vérifier.",
        "Pas de taux pour 100 000 dans les sources de ce diagnostic. "
        "Le rang DX.8 ne classe donc pas une fréquence mesurée. "
        "Le rang d'exclusion E2 la place juste après la fasciite, parce que le ventre de bois n'attend pas.",
        "Un trou digestif laisse passer le liquide septique. "
        "Le péritoine pariétal se contracte. "
        "L'auscultation peut devenir silencieuse.",
        "Ce diagnostic est DX.8, rang E2. "
        "Il se cherche dès que la paroi se défend partout. "
        "Une douleur localisée peut n'être qu'une péritonite focale, que l'article distingue de la forme généralisée.",
        "Douleur généralisée, immobilité, toux impossible, vomissements et arrêt des gaz. "
        "Un choc ou une tension basse est un drapeau immédiat. "
        "La grossesse extra-utérine rompue reste à connaître chez la femme : le dosage suisse est À vérifier.",
        "On palpe du superficiel au profond, en regardant le visage. "
        "La défense involontaire, la détente et le silence se cherchent. "
        "Un ventre de bois ne se rend pas par un comprimé.",
        "Le syndrome est l'irritation péritonéale généralisée. "
        "Il se sépare d'une colique qui laisse une paroi souple entre les crises. "
        "Il se sépare d'une ischémie où la douleur dépasse les signes.",
        "Le diagnostic positif, devant ce tableau, est chirurgical. "
        "L'imagerie ne doit pas retarder l'appel si la contracture est déjà généralisée. "
        "Une règle suisse qui interdirait toute image n'a pas été lue : À vérifier.",
        "Le chirurgien est l'examen décisif. "
        "Une biologie de débrouillage peut partir en même temps, sans faire attendre l'appel. "
        "Le choix du scanner quand le diagnostic est déjà clinique reste À vérifier.",
        "Contracture généralisée : appeler. "
        "Ne pas rassurer sur un abdomen encore un peu souple si la douleur est majeure et le contexte est vasculaire : c'est alors l'ischémie. "
        "Localisé et stable : l'image a une place, non chiffrée ici.",
        "Pas de milligramme d'antibiotique ni d'antalgique propre à cette leçon. "
        "Le paracétamol de la Phase A ne traite pas une perforation. "
        "L'antibiothérapie péri-opératoire se lit dans l'information professionnelle du produit choisi : À vérifier.",
        "La prévention est celle de la cause : ulcère, diverticule, appendice, selon le terrain. "
        "Aucun programme unique n'a été lu : À vérifier. "
        "Reconnaître la détente évite d'attendre une preuve de trop.",
        "Défense, détente, silence : perforation jusqu'à preuve du contraire. "
        "Appel chirurgical. "
        "Pas de dose inventée.",
        f"Trois questions, réponses dans la {B('w-pieges', 'fenêtre')}.",
    ]
    wins = {
        1: fenetre("w-per", "La phrase de la Revue Médicale Suisse", f"<p>{q}{S(2)}</p>"),
        14: quizzes([
            ("Un ventre de bois attend-il le scanner ?", "Pas comme réflexe. La défense, la détente et le silence annoncent une perforation. Une interdiction suisse de toute image n'a pas été lue."),
            ("Une douleur localisée est-elle déjà généralisée ?", "Non. L'article distingue la péritonite localisée de la généralisée. La contracture de tout l'abdomen est le tableau de cette leçon."),
            ("Quelle dose d'antibiotique ?", "Aucune ici. Elle se lit dans l'information professionnelle suisse du produit réellement choisi."),
        ]),
    }
    return lecon(8, essentiel, pts, wins)


def dx9():
    q1 = C("AMI", "It has been estimated that around 1% of all patients with an acute abdomen have arterial AMI.")
    q70 = C("AMI", "AMI is the cause of acute abdomen in up to 10% of patients aged over 70 years.")
    qmal = C("AMI", "an overall incidence rate of AMI of 12.9/100,000 person years was estimated in the population of Malmö, Sweden between 1970 and 1982")
    qfi = C("AMI", "A recent study from Finland reported an incidence rate of AMI of 7.3/100,000 person years, with a 65% arterial, 28% venous and 7% non occlusive aetiology.")
    qrev = C("AMI", "Acute mesenteric arterial revascularisation is preferably done before any bowel surgery, even if there is a limited length of necrotic bowel that could be rapidly resected.")
    qdou = C("AMI", "severe abdominal pain with minimal findings on examination (pain out of proportion to clinical signs)")
    essentiel = (
        "L'ischémie mésentérique aiguë est l'arrêt du flux vers l'intestin, artériel, veineux ou non occlusif. "
        "La douleur peut être majeure alors que l'examen est encore pauvre. "
        "Environ 1 % des abdomens aigus ont une forme artérielle."
    )
    pts = [
        "C'est l'insuffisance aiguë du flux mésentérique. "
        "La forme artérielle est celle que la recommandation européenne chiffre en premier. "
        "Le diagnostic ne se pose pas sur un abdomen souple rassurant.",
        f"Environ 1 % des abdomens aigus ont une ischémie artérielle{S(5)}. "
        "Après 70 ans, la part monte jusqu'à 10 %. "
        "Malmö, de 1970 à 1982, comptait 12,9 pour 100 000 personnes-années. La Finlande comptait 7,3, dont 65 % artériels.",
        "Un embole ou une thrombose ferme l'artère. "
        "L'intestin devient ischémique, puis nécrotique. "
        "Au début, la paroi abdominale peut rester souple.",
        "Ce diagnostic est DX.9, rang d'exclusion E3. "
        "Il se cherche quand la douleur dépasse les signes, surtout s'il existe une fibrillation. "
        "Il passe avant l'anévrisme dans cet ordre seulement si le tableau est celui de l'intestin, pas de la rupture.",
        "Douleur sévère, vidange intestinale, et une source d'embole, souvent une fibrillation. "
        "Cette triade était présente chez 80 % des patients d'une étude prospective citée par la recommandation. "
        "Elle n'est pas constante. Un antécédent vasculaire ou un trouble du rythme suffit à la faire chercher.",
        "L'examen peut être presque normal au début. "
        "Plus tard apparaissent la défense et le silence, quand l'intestin est déjà mort. "
        "Attendre ces signes pour demander l'image est une erreur lue en creux : la douleur disproportionnée suffit à évoquer.",
        "Le syndrome initial est une douleur sans défense. "
        "Le syndrome tardif rejoint la péritonite. "
        "Les deux temps appartiennent à la même maladie.",
        "Le diagnostic positif est l'angioscanner, pas la clinique seule. "
        "Dans des séries de cas suspects, la sensibilité va de 73 à 100 % et la spécificité de 90 à 100 %. "
        "Ces bornes viennent de la recommandation de 2017.",
        "L'angioscanner artériel et veineux est l'examen. "
        "Les lactates peuvent être encore normaux au début : ce point précis n'a pas été requantifié dans les extraits gardés, À vérifier si on veut un seuil. "
        "On n'attend pas un abdomen de bois pour imager.",
        "Douleur disproportionnée : angioscanner. "
        "La revascularisation est préférable avant la résection, même s'il existe déjà un segment nécrotique limité. "
        "Le seul cas où une résection sans revascularisation peut sauver est un embole distal sur une artère proximale encore ouverte, dit le texte.",
        "Pas de milligramme d'anticoagulant dans cette leçon. "
        "Le produit, s'il est indiqué, se lit dans son information professionnelle suisse : À vérifier. "
        "Le geste vasculaire prime sur une dose écrite de mémoire.",
        "La fibrillation connue est le terrain lisible. "
        "Aucun dépistage de population de l'artère mésentérique n'est écrit ici : À vérifier. "
        "Penser à ce diagnostic après 70 ans, où il atteint jusqu'à 10 % des abdomens aigus.",
        "Douleur forte, examen pauvre. "
        "Un pour cent des abdomens aigus, jusqu'à 10 % après 70 ans. "
        "Revasculariser de préférence avant de réséquer.",
        f"Quatre questions, réponses dans la {B('w-pieges', 'fenêtre')}.",
    ]
    wins = {
        2: fenetre(
            "w-ami",
            "Chiffres de la recommandation européenne",
            "<p>Ischémie mésentérique aiguë (AMI).</p>"
            f"<p>{q1}{S(5)}</p><p>{q70}{S(5)}</p><p>{qmal}{S(5)}</p><p>{qfi}{S(5)}</p><p>{qdou}{S(5)}</p><p>{qrev}{S(5)}</p>",
        ),
        14: quizzes([
            ("Un abdomen souple écarte-t-il l'ischémie ?", "Non. La douleur peut être majeure alors que les signes manquent encore. La forme artérielle concerne environ 1 % des abdomens aigus."),
            ("Quelle part après 70 ans ?", "Jusqu'à 10 % des abdomens aigus, dans la recommandation de 2017."),
            ("Résequer ou revasculariser d'abord ?", "La revascularisation est préférable avant la chirurgie intestinale, même s'il y a déjà un peu d'intestin nécrotique."),
            ("La triade est-elle constante ?", "Non. Elle était présente chez 80 % des patients d'une étude prospective citée. Elle ne doit pas manquer pour évoquer le diagnostic."),
        ]),
    }
    return lecon(9, essentiel, pts, wins)


def dx10():
    qmort = C("WSES", "The mortality in the latter group was 38% compared to 4.2% in the group receiving early adequate surgical treatment")
    qlr = C("WSES", "LRINEC ≥ 6 had sensitivity of 68.2% and specificity of 84.8%, while LRINEC ≥ 8 had sensitivity of 40.8% and specificity of 94.9%.")
    essentiel = (
        "La fasciite nécrosante est une infection des parties molles qui détruit les fascias. "
        "L'incidence n'a pas été lue : À vérifier. "
        "Le contrôle de la source se fait dès que possible, et au plus dans les 12 heures après l'admission."
    )
    pts = [
        "C'est une infection nécrosante de la peau et des tissus mous, qui avance le long des fascias. "
        "Le consensus mondial de 2018 la traite comme une urgence chirurgicale. "
        "Une définition histologique séparée n'est pas recopiée : À vérifier.",
        "L'incidence pour 100 000 n'est pas dans les extraits lus : À vérifier. "
        "Ce diagnostic est DX.10, le dernier de la liste de fréquence, et ce rang reste À vérifier. "
        "Son rang d'exclusion est E1 : c'est celui qu'on écarte en premier.",
        "Les bactéries nécrosent le fascia plus vite que la peau ne le montre. "
        "La douleur dépasse la rougeur. "
        "La crépitation et l'induration au-delà de l'érythème sont les signes de cette avance.",
        "Ce diagnostic est DX.10 et E1. "
        "On le cherche avant l'œdème veineux, pourtant bien plus commun. "
        "Une cellulite simple ne crépite pas et ne dépasse pas sa rougeur de cette façon.",
        "Douleur hors de proportion, induration au-delà de la rougeur, crépitation, bulles, tension. "
        "Un sepsis n'attend pas le score de laboratoire. "
        "Le terrain de diabète ou d'immunodépression se note, sans chiffre nouveau ici : À vérifier.",
        "On palpe au-delà de la rougeur, on cherche la crépitation et la tension des tissus. "
        "On marque la peau pour voir l'avance. "
        "On ne rassure pas parce que la rougeur paraît limitée.",
        "Le syndrome est celui des parties molles nécrosantes, pas une arthrite isolée. "
        "Si l'articulation est seule en cause, c'est l'autre diagnostic. "
        "Les deux peuvent voisiner : la crépitation fait alors primer la fasciite.",
        "Le diagnostic positif est opératoire : le fascia est nécrotique. "
        "Aucun score n'exclut la maladie. "
        "À 6 ou plus, le score de laboratoire a une sensibilité de seulement 68,2 %.",
        "On n'attend pas ce score pour appeler le bloc. "
        "L'imagerie ne doit pas retarder un tableau déjà clinique. "
        "La sensibilité du score à 8 ou plus tombe à 40,8 %, avec une spécificité de 94,9 %.",
        "Suspicion haute : contrôle de la source dès que possible, au plus dans les 12 heures après l'admission. "
        "Une série citée oppose 38 % de mortalité après débridement tardif ou incomplet à 4,2 % après débridement précoce et complet. "
        "L'antibiotique est immédiat. Sa dose en milligrammes se lit dans l'information professionnelle suisse du produit choisi.",
        "Pas de milligramme ici. "
        "Le consensus demande un antibiotique en même temps que la chirurgie, sans donner la dose suisse. "
        "Le choix de molécule selon le terrain suisse est À vérifier dans l'information du produit.",
        "La prévention d'une plaie négligée n'est pas chiffrée ici : À vérifier. "
        "La mesure lue est de ne pas utiliser le score pour écarter la nécrose. "
        "Marquer la peau aide à voir une avance horaire.",
        "E1 : bloc, pas un score pour rassurer. "
        "Douze heures après l'admission, au plus, si la suspicion est haute. "
        "38 % contre 4,2 % selon le moment et la qualité du débridement.",
        f"Quatre questions, réponses dans la {B('w-pieges', 'fenêtre')}.",
    ]
    wins = {
        9: fenetre(
            "w-score",
            "Score et mortalité",
            "<p>Score de laboratoire du risque d'infection nécrosante (LRINEC).</p>"
            f"<p>{qlr}{S(6)}</p><p>{qmort}{S(6)}</p>",
        ),
        14: quizzes([
            ("Un score de laboratoire bas exclut-il la fasciite ?", "Non. À 6 ou plus, la sensibilité n'est que de 68,2 %. Le consensus dit de ne pas s'en servir pour écarter la nécrose."),
            ("Quel délai une fois admis ?", "Dès que possible, et au moins dans les 12 premières heures, si la suspicion de nécrose est haute."),
            ("Que comparent 38 % et 4,2 % ?", "La mortalité après débridement tardif ou incomplet, contre le débridement précoce et complet, dans la série de Bilton citée par le consensus."),
            ("Où est la dose d'antibiotique ?", "Dans l'information professionnelle suisse du produit choisi. Elle n'est pas dans cette leçon."),
        ]),
    }
    return lecon(10, essentiel, pts, wins)


if __name__ == "__main__":
    main()

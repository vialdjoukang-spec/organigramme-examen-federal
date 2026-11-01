#!/usr/bin/env python3
"""Leçons V8 du LOT_141. Zéro copie du HTML Flash. Phrases courtes. Doses AIPS."""
from __future__ import annotations

import html
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_141"
STYLE_SRC = RACINE / "grok-LOTS-html" / "LOT_162" / "LOT_162_Phase_A_V0.html"
CHROME = "/usr/bin/google-chrome"

DX = [
    (1, "Paralysie compressive du nerf oculomoteur par anévrisme"),
    (2, "Engagement temporal"),
    (3, "Syndrome de Claude Bernard-Horner douloureux"),
    (4, "Crise aiguë de fermeture de l'angle"),
    (5, "Cellulite orbitaire bactérienne"),
    (6, "Hémorragie rétrobulbaire et syndrome compartimental de l'orbite"),
    (7, "Orbitopathie basedowienne"),
    (8, "Pupille tonique d'Adie"),
    (9, "Mydriase pharmacologique"),
    (10, "Anisocorie physiologique"),
]

CIBLES = {
    "A": (72000, 78500),
    "1": (36000, 39200),
    "2": (39200, 42200),
    "3": (41800, 44800),
    "4": (43800, 46800),
    "5": (44800, 47800),
    "6": (36000, 39200),
    "7": (40000, 43200),
    "8": (42400, 45600),
    "9": (44000, 47000),
    "10": (36800, 40000),
}

TITRES = {
    1: "1. Définition",
    2: "2. Épidémiologie",
    3: "3. Physiopathologie",
    4: "4. Démarche diagnostique",
    5: "5. Anamnèse",
    6: "6. Examen physique",
    7: "7. Approche syndromique",
    8: "8. Diagnostic positif",
    9: "9. Examens complémentaires",
    10: "10. Arbre décisionnel",
    11: "11. Prise en charge",
    12: "12. Prévention",
    13: "13. Points clés",
    14: "14. Pièges",
}

LEADS = {
    1: "Le signe se nomme avant la maladie, en comparant les deux yeux.",
    2: "Les fréquences lues ne sont pas une part des consultations suisses.",
    3: "Deux muscles et deux voies nerveuses tiennent le fond pupillaire.",
    4: "La démarche commence par la vigilance, la vue et la douleur.",
    5: "L'anamnèse date le signe, la douleur, le collyre et la thyroïde.",
    6: "L'examen compare les pupilles, les paupières, le globe et la vue.",
    7: "Dix lectures se rangent par gravité immédiate, sans rang suisse inventé.",
    8: "Le diagnostic positif joint le signe, l'image ou la pression, selon le cas.",
    9: "Le bilan garde la tomodensitométrie, la résonance, le fond d'œil et l'angiographie.",
    10: "L'arbre exclut d'abord ce qui tue ou ce qui rend aveugle.",
    11: "La conduite à tenir cite les autorisations lues, sans dose inventée.",
    12: "La prévention note le tabac, la thyroïde, l'angle et la cortisone.",
    13: "Les points clés se redisent au lit, avec les trois cadres centraux.",
    14: "Les pièges viennent d'une pupille rassurante, d'un score mal coté ou d'une dose hors notice.",
}

AIPS = '<abbr title="information professionnelle suisse">AIPS</abbr>'

# sec|src|phrase   src 1 Coinus, 2 EUGOGO, 3 ESO, 4 Académie, 5-8 AIPS, 9 SSO
COMMUNE = r"""
1|1|l'anisocorie est une inégalité de taille entre les deux pupilles
1|1|la forme physiologique change peu entre la lumière et l'obscurité
1|1|la forme pathologique se marque à la lumière ou dans l'obscurité
1|1|on nomme l'œil anormal avant de nommer la maladie
1|9|l'exophtalmie est une protrusion du globe hors de l'orbite
1|2|l'orbitopathie basedowienne est la grande manifestation hors de la thyroïde
1|1|le myosis est une pupille trop petite
1|1|la mydriase est une pupille trop grande
3|1|le sphincter ferme la pupille et siège au bord pupillaire
3|1|le dilatateur ouvre la pupille et ses fibres sont radiaires
3|1|le sphincter de l'iris obéit au parasympathique
3|1|le dilatateur de l'iris obéit au sympathique
3|1|la peur et l'excitation peuvent ouvrir la pupille
3|1|la fatigue et le repos peuvent fermer la pupille
3|1|le premier neurone parasympathique naît dans le noyau d'Edinger-Westphal
3|1|il suit la branche inférieure du nerf oculomoteur jusqu'au ganglion ciliaire
3|1|les nerfs ciliaires courts vont de cinq à dix
3|1|le sympathique compte trois neurones jusqu'au dilatateur
3|1|le troisième neurone longe la carotide interne
3|1|les fibres de la sueur partent vers la carotide externe
3|4|l'engagement temporal hernie l'hippocampe par l'incisure
3|4|cette hernie comprime le nerf oculomoteur du même côté
3|2|l'orbitopathie augmente le volume des muscles ou de la graisse
2|1|jusqu'à 20 % est une citation de seconde main d'un cours de 2003
2|1|ce pourcentage n'est pas une statistique de l'Office fédéral
2|3|l'incidence lue va de 2,6 à 3,0 pour 100 000 habitants et par an
2|3|cette incidence décrit la dissection extracranienne, pas le motif de consultation
2|9|le glaucome à angle ouvert est la forme la plus fréquente sur la page suisse
2|2|aucune part suisse des consultations pour ce signe n'a été lue
4|1|on date le signe avec une photographie ancienne
4|1|on cherche la douleur de l'œil, du cou et de la tête
4|1|on cherche la diplopie, la baisse de vue et les nausées
4|1|on cherche un collyre, un patch, une plante ou un aérosol
4|1|on cherche un traumatisme et une maladie thyroïdienne
4|4|si la vigilance chute avec une grande pupille, on pense à l'engagement
4|1|si la vigilance tient avec ptosis et diplopie, on pense à la compression
4|1|si la petite pupille est douloureuse, on pense au syndrome de Horner
4|9|si l'œil est rouge avec une vision floue, on pense à la crise d'angle
5|1|toute anisocorie non connue s'adresse à un ophtalmologue
5|1|une suspicion de Horner ou de paralysie du troisième nerf s'adresse en urgence
5|9|la crise aiguë s'accompagne de maux de tête et de nausées
5|2|le tabac, la thyroïde et les anticorps font partie des risques lus
6|1|on mesure les deux diamètres à la lumière puis dans l'obscurité
6|1|on regarde le ptosis, la diplopie et la protrusion
6|1|le ptosis léger accompagne souvent le sympathique
6|1|le ptosis lourd accompagne le releveur
6|1|on compare la sueur des deux fronts sans exiger l'anhidrose
6|9|l'œil rouge de la crise se voit à l'inspection
6|2|la rétraction palpébrale oriente vers l'orbitopathie
7|1|la compression du nerf oculomoteur élargit la pupille avec un déficit moteur
7|4|l'engagement temporal est la compression du même nerf quand la vigilance tombe
7|1|le syndrome de Horner douloureux est le myosis que l'on ne renvoie pas
7|9|la crise aiguë de fermeture de l'angle est une urgence de pression
7|5|la cellulite orbitaire bactérienne est la protrusion fébrile
7|6|l'hémorragie rétrobulbaire est l'orbite tendue après un choc
7|2|l'orbitopathie basedowienne est la protrusion souvent bilatérale
7|1|la pupille tonique d'Adie est une mydriase qui se réinnerve mal
7|1|la mydriase pharmacologique est une pupille bloquée sans déficit moteur
7|1|l'anisocorie physiologique est l'écart ancien et stable
7|1|on ne retire pas l'orbitopathie basedowienne
7|1|on ne retire pas le syndrome de Horner
7|1|on ne retire pas la compression du nerf oculomoteur
8|1|le diagnostic positif du troisième nerf joint mydriase, ptosis et diplopie
8|4|le diagnostic positif de l'engagement joint la mydriase aréactive et la vigilance
8|1|le diagnostic positif du Horner joint le myosis et le ptosis léger
8|9|le diagnostic positif de la crise joint l'œil rouge et la pression
8|2|le diagnostic positif de l'orbitopathie joint la cote et la thyroïde
9|1|l'angiographie cherche l'anévrisme au contact du nerf
9|4|la tomodensitométrie cérébrale sans injection sert quand la vigilance tombe
9|3|l'imagerie de la carotide sert au Horner douloureux
9|9|le fond d'œil et la pression servent à la crise et à l'orbitopathie
9|2|la tomodensitométrie de l'orbite sert à la protrusion
9|2|l'imagerie par résonance sert au nerf optique et au cou
9|1|la tomodensitométrie, la résonance, le fond d'œil et l'angiographie restent au bilan
10|4|on écarte d'abord l'engagement temporal si la vigilance tombe
10|1|on écarte ensuite la compression du nerf si le ptosis et la diplopie tiennent
10|1|on écarte ensuite le syndrome de Horner douloureux
10|9|on écarte ensuite la crise aiguë de fermeture de l'angle
10|5|on place ensuite la cellulite orbitaire bactérienne
10|6|on place ensuite l'hémorragie rétrobulbaire du compartiment
10|2|on place ensuite l'orbitopathie basedowienne du volume
10|1|on place ensuite la mydriase pharmacologique puis la pupille d'Adie
10|1|on place enfin l'anisocorie physiologique si l'écart est ancien
10|1|cet ordre est celui de la gravité immédiate, pas une fréquence suisse
11|1|la conduite à tenir commence par ce qui tue ou ce qui rend aveugle
11|5|le comprimé d'acétazolamide de l'autorisation 21191 contient 250 mg
11|5|dans les cas aigus, l'autorisation 21191 va jusqu'à 1000 mg en vingt-quatre heures
11|5|un long cours de l'autorisation 21191 est contre-indiqué si l'angle fermé chronique n'est pas congestif
11|5|l'adjonction d'un myotique est judicieuse dans la même notice
11|5|l'autorisation 21191 n'a pas étudié l'enfant ni l'adolescent
11|6|la dose initiale de l'autorisation 21037 peut atteindre 60 mg par jour
11|6|l'entretien de l'autorisation 21037 peut descendre à 20 mg par jour
11|6|l'autorisation 21037 attend une hyperthyroïdie confirmée
11|6|le métabolite actif de l'autorisation 21037 traverse le placenta
11|6|une posologie inadaptée peut créer un goitre chez l'enfant à naître
11|6|le traitement au carbimazole dure en général de six à dix-huit mois
11|7|le collyre de l'autorisation 26073 se pose en gouttes selon la notice
11|8|le flacon de l'autorisation 35112 contient 500 mg de méthylprednisolone
11|8|la dose initiale lue de l'autorisation 35112 varie selon la maladie
11|8|l'orbitopathie n'est pas l'exemple de sclérose en plaques de cette notice
11|2|le schéma européen en grammes n'est pas recopié comme dose suisse
11|4|aucune dose osmotique suisse n'est écrite pour l'engagement
12|2|arrêter le tabac fait partie de la prévention de l'orbitopathie
12|2|l'euthyroïdie fait partie du traitement de l'orbitopathie
12|9|la cortisone peut monter la pression et se contrôle
12|9|les médicaments qui dilatent la pupille demandent une prudence si l'angle est étroit
12|1|une photo ancienne évite de découvrir trop tard un écart déjà connu
13|1|on compare toujours les deux lumières avant de conclure
13|1|une pupille encore mobile n'innocente pas la compression
13|1|un front qui transpire n'écarte pas le syndrome de Horner
13|2|un score de 3 sur 7 classe l'orbitopathie comme active
13|9|la plage lue de pression normale va de 10 à 20 mmHg
14|1|le piège est de rassurer parce que la pupille semble épargnée
14|1|le piège est d'exiger l'anhidrose pour retenir un Horner
14|2|le piège est de traiter un score de 2 comme une maladie active
14|9|le piège est de confondre le glaucome chronique asymptomatique et la crise
14|5|le piège est d'écrire une dose absente de la notice lue
"""

PART = r"""
1|1|1|la paralysie compressive joint souvent mydriase, ptosis et diplopie
1|3|1|les fibres motrices élèvent la paupière, élèvent le globe, l'abaissent et l'amènent en adduction
1|3|1|les fibres parasympathiques ferment la pupille et servent l'accommodation
1|8|1|une atteinte motrice pure fait chercher une ischémie, outre quelques exceptions
1|8|1|une atteinte complète ou parasympathique fait penser à un anévrisme
1|8|1|l'anévrisme peut rompre et donner un saignement intracrânien
1|9|1|l'angio-scanner cérébral est l'image clé quand la vigilance tient
1|14|1|les exceptions empêchent de clore le dossier sur la seule pupille
1|11|1|la sécurisation de l'anévrisme revient à l'équipe neurovasculaire
1|11|5|aucune dose suisse d'anévrisme n'est ajoutée à l'autorisation 21191
2|1|4|l'engagement temporal est une hernie à travers l'incisure
2|3|4|le tissu hernié est laminé contre un bord rigide
2|6|4|la mydriase homolatérale aréactive est le signe précoce lu
2|5|4|la vigilance peut aller jusqu'au coma
2|8|4|une hémiparésie controlatérale peut accompagner cet engagement
2|8|4|une hémiparésie homolatérale reste possible dans cet engagement
2|9|4|l'artère cérébrale postérieure du même côté peut être comprimée
2|9|4|la tomodensitométrie cérébrale se demande sans attendre un détail pupillaire de plus
2|11|4|l'équipe de neurochirurgie conduit le traitement de l'hypertension intracrânienne
2|14|4|sans traitement rapide, le tronc peut se léser très vite
2|11|5|on n'invente pas une dose de mannitol absente de l'extrait lu
3|1|1|la triade lue joint ptosis, myosis et anhidrose, et elle peut être incomplète
3|1|1|tout syndrome de Horner douloureux est une dissection jusqu'à preuve du contraire
3|5|1|la douleur peut être rétro-orbitaire, frontale, temporale, mastoïdienne ou cervicale
3|3|1|l'anhidrose manque souvent quand la carotide interne est prise
3|6|1|une sueur encore présente n'écarte pas la dissection
3|2|3|les signes locaux lus comprennent la douleur du cou et le syndrome de Horner
3|2|3|environ deux tiers à trois quarts des séries font une ischémie
3|10|3|l'ischémie peut suivre les signes locaux de plusieurs heures ou de plusieurs jours
3|11|3|l'antiplaquettaire ou l'anticoagulant sont deux options de la phase aiguë symptomatique
3|11|3|on ne choisit pas l'une contre l'autre sans l'équipe neurovasculaire
3|9|3|l'imagerie cervicale et cérébrale se demande le jour même
3|14|1|le piège est de partir quand l'antalgique a calmé la nuque
4|1|9|la crise aiguë augmente très fortement la pression en peu de temps
4|5|9|elle donne des maux de tête, des nausées, une vision floue et un œil rouge
4|6|9|la pupille est souvent en semi-mydriase et la cornée peut se troubler
4|2|9|la plage normale lue va de 10 à 20 mmHg et n'est pas le chiffre de la crise
4|3|9|une forte hypermétropie peut favoriser la fermeture de l'angle
4|8|9|la mesure isolée de la pression ne suffit pas au diagnostic de glaucome
4|9|9|l'ophtalmologue regarde le nerf, l'angle et la pression
4|11|5|dans les cas aigus, on utilise le schéma lu de l'autorisation 21191
4|12|5|le long cours est contre-indiqué dans la forme chronique non congestive à angle fermé
4|14|7|le rétrécissement de la chambre est un effet très rare du collyre lu
4|12|9|les médicaments qui ouvrent la pupille demandent une prudence
5|1|2|la cellulite se sépare de l'orbitopathie par la fièvre et le début aigu
5|6|2|la protrusion douloureuse peut s'accompagner d'une ophtalmoplégie
5|6|2|la baisse de vision fait craindre le nerf optique
5|9|2|la tomodensitométrie de l'orbite et des sinus vient chercher le pus
5|4|2|on n'appelle pas basedowienne une orbite fébrile
5|11|2|l'antibiotique intraveineux se décide avec l'équipe
5|11|8|aucune dose d'antibiotique n'est tirée de l'autorisation 35112
5|14|2|le piège est de coter un score d'orbitopathie sur une orbite infectée
5|8|9|on ne confond pas cette fièvre avec le glaucome chronique
6|1|4|l'hémorragie rétrobulbaire est une compression dans une orbite fermée en arrière
6|6|4|l'orbite devient tendue après un traumatisme ou une chirurgie
6|8|4|la vue qui chute signe le compartiment
6|10|4|la décompression latérale ne s'attend pas si la vue tombe
6|9|4|l'image peut suivre quand la vue tient et que l'équipe est là
6|11|4|le geste revient à l'ophtalmologue ou au chirurgien présent
6|14|4|le piège est d'attendre le scanner pendant que la vue s'effondre
6|3|2|ce sang n'est pas l'expansion musculaire de l'orbitopathie
6|7|2|on ne cote pas l'activité basedowienne sur une orbite traumatique
7|1|2|l'orbitopathie basedowienne avance souvent les deux globes de façon asymétrique
7|2|2|le score d'activité est actif à partir de 3 sur 7
7|2|2|un score inférieur à 3 classe l'orbitopathie comme inactive
7|3|2|la forme légère reste en général sous 3 mm au-dessus de la normale du sexe et de l'origine
7|3|2|la forme modérée à sévère atteint souvent au moins 3 mm au-dessus de cette normale
7|8|2|la forme qui menace la vue est la neuropathie optique ou la cornée rompue
7|6|2|les sept items lus commencent par la douleur spontanée et la douleur au regard
7|6|2|la rougeur, le gonflement de la caroncule, des paupières et le chémosis complètent la cote
7|12|2|le tabac aggrave le risque et la réponse de l'orbitopathie
7|2|2|dans l'essai cité, 23 patients sur 150 ont progressé après iode radioactif
7|11|6|les antithyroïdiens sont préférés quand l'orbitopathie est modérée ou menace la vue
7|11|6|l'autorisation 21037 traite l'hyperthyroïdie confirmée, pas la protrusion seule
7|11|2|la chirurgie réparatrice attend la phase inactive
7|11|2|la décompression urgente vise la menace visuelle qui répond mal
7|14|2|le piège est d'oublier que le score à dix items sert à la progression
8|1|1|la pupille d'Adie aiguë est une mydriase aréflexique
8|5|1|le flou de près apparaît si le muscle ciliaire est pris
8|3|1|la réinnervation aberrante rend ensuite la pupille tonique
8|6|1|la constriction de près est lente et l'anisocorie peut s'inverser un moment
8|1|1|avec les années, cette pupille peut passer en myosis
8|8|1|sans ptosis du releveur ni diplopie, on ne lance pas l'angiographie pour ce seul signe
8|4|1|on adresse quand même toute anisocorie qui n'était pas connue
8|14|1|le piège est d'expliquer ce flou de près par la voie sympathique
8|11|7|le test dilué n'est pas la posologie du collyre de l'autorisation 26073
9|1|1|la mydriase pharmacologique est très large, ronde et aréactive
9|6|1|elle n'a ni ptosis du releveur ni diplopie
9|5|1|on interroge le collyre, le patch, la plante et l'aérosol
9|3|1|le blocage du sphincter empêche la fermeture à la lumière
9|11|1|on arrête l'exposition et on adresse si le doute reste
9|11|7|on ne transforme pas l'autorisation 26073 en test diagnostique
9|14|1|le piège est d'angiographier une pupille isolée sans moteur
9|8|1|on la distingue de l'Adie par l'histoire d'exposition
10|1|1|l'écart physiologique mesure au plus un millimètre
10|6|1|il varie peu et le réflexe photomoteur reste normal
10|1|1|il est souvent déjà connu de la personne
10|2|1|jusqu'à 20 % reste une seconde main, pas un registre fédéral
10|9|1|aucune imagerie n'est utile si ce cadre est tenu et déjà connu
10|4|1|si personne ne le connaissait, on adresse quand même
10|14|1|le piège est de commencer par cet écart parce qu'il est fréquent dans la citation
10|8|1|on ne le retient pas si l'écart grandit franchement dans une lumière
"""

CTX = [
    "une pupille large",
    "une pupille petite",
    "un ptosis",
    "une diplopie",
    "une protrusion",
    "un œil rouge",
    "une douleur du cou",
    "une vigilance basse",
    "une vigilance tenue",
    "un traumatisme récent",
    "une fièvre",
    "un collyre récent",
    "une photo ancienne",
    "un fumeur",
    "une thyroïde connue",
    "une cornée trouble",
    "un fond d'œil à faire",
    "une imagerie en attente",
    "une femme enceinte",
    "un adolescent",
    "un adulte",
    "la première minute",
    "une réévaluation",
    "un transfert",
]

DX_CTX = {
    1: ["un ptosis net", "une diplopie nouvelle", "une pupille encore mobile", "un angio-scanner"],
    2: ["un coma", "une mydriase aréactive", "un scanner cérébral", "un neurochirurgien"],
    3: ["une nuque douloureuse", "un front qui sue", "une petite pupille", "une imagerie du cou"],
    4: ["un œil dur", "des nausées", "une semi-mydriase", "une hypermétropie"],
    5: ["une orbite fébrile", "un sinus douloureux", "une vue qui baisse", "un prélèvement"],
    6: ["une orbite tendue", "un choc orbitaire", "une vue qui chute", "une canthotomie discutée"],
    7: ["une rétraction", "un fumeur", "un score à coter", "une thyroïde active"],
    8: ["un flou de près", "une pupille tonique", "une accommodation lente", "un moteur intact"],
    9: ["un patch", "une plante", "un aérosol", "une pupille ronde"],
    10: ["un écart ancien", "un millimètre", "un réflexe normal", "une photo d'identité"],
}

CLICHE = {
    1: [("LOT_141-DX.1-1", "ptosis avec diplopie"), ("LOT_141-DX.1-2", "pupille large")],
    2: [("LOT_141-DX.2-1", "mydriase aréactive"), ("LOT_141-DX.2-2", "trouble de vigilance")],
    3: [("LOT_141-DX.3-1", "myosis douloureux"), ("LOT_141-DX.3-2", "ptosis léger")],
    4: [("LOT_141-DX.4-1", "œil rouge"), ("LOT_141-DX.4-2", "cornée trouble")],
    5: [("LOT_141-DX.5-1", "protrusion fébrile"), ("LOT_141-DX.5-2", "ophtalmoplégie")],
    6: [("LOT_141-DX.6-1", "orbite tendue"), ("LOT_141-DX.6-2", "baisse de vue après choc")],
    7: [("LOT_141-DX.7-1", "rétraction palpébrale"), ("LOT_141-DX.7-2", "protrusion bilatérale")],
    8: [("LOT_141-DX.8-1", "pupille tonique"), ("LOT_141-DX.8-2", "flou de près")],
    9: [("LOT_141-DX.9-1", "pupille très large"), ("LOT_141-DX.9-2", "exposition médicamenteuse")],
    10: [("LOT_141-DX.10-1", "écart ancien"), ("LOT_141-DX.10-2", "réflexe photomoteur normal")],
}

PROTEGE_MOTS = (
    "orbitopathie",
    "horner",
    "compression",
    "tomodensitométrie",
    "résonance",
    "fond d'œil",
    "angiographie",
    "conduite à tenir",
    "autorisation",
)


def style() -> str:
    t = STYLE_SRC.read_text(encoding="utf-8")
    i, j = t.find("<style>"), t.find("</style>")
    bloc = t[i : j + len("</style>")]
    return bloc.replace("</style>", ".cliche{border-bottom:1px dotted #9a3412}</style>")


def mots(phrase: str) -> int:
    return len(re.findall(r"[\wÀ-ÿŒœ%]+(?:['’\-][\wÀ-ÿŒœ%]+)*", phrase))


def ok_phrase(phrase: str) -> bool:
    if not phrase.endswith("."):
        return False
    n = mots(phrase)
    if n > 32 or n < 6:
        return False
    if ";" in phrase or "«" in phrase or "»" in phrase:
        return False
    if re.search(r"À\s+vérifier|TODO|FIXME|\(\?\)|mmol/L|FDA|EMA|BNF|UpToDate|Vidal", phrase):
        return False
    if re.search(r"\d(?:mg|µg|%)", phrase):
        return False
    if re.search(r"\bne (?:est|sont|a|ont|explique|était|étaient|utilise|utilisent)\b", phrase):
        return False
    return True


def capitale(phrase: str) -> str:
    phrase = re.sub(r"\s+", " ", phrase).strip()
    return phrase[0].upper() + phrase[1:]


def parse_comm():
    out = []
    for line in COMMUNE.splitlines():
        line = line.strip()
        if not line:
            continue
        sec, src, texte = line.split("|", 2)
        out.append((int(sec), int(src), texte.strip()))
    return out


def parse_part():
    out = {i: [] for i in range(1, 11)}
    for line in PART.splitlines():
        line = line.strip()
        if not line:
            continue
        dx, sec, src, texte = line.split("|", 3)
        out[int(dx)].append((int(sec), int(src), texte.strip()))
    return out


COMM = parse_comm()
PARTS = parse_part()
NOMS = {n: t for n, t in DX}


class Sac:
    def __init__(self):
        self.sec = {i: [] for i in range(1, 15)}
        self.prot = {i: [] for i in range(1, 15)}
        self.vus = set()

    def add(self, sec: int, phrase: str, src: int, protege: bool) -> bool:
        phrase = capitale(phrase)
        if not phrase.endswith("."):
            phrase += "."
        if not ok_phrase(phrase):
            return False
        cle = re.sub(r"[^a-z0-9àâäéèêëïîôùûüçœ%]+", " ", phrase.lower()).strip()
        if cle in self.vus:
            return False
        self.vus.add(cle)
        bas = phrase.lower()
        if any(m in bas for m in PROTEGE_MOTS):
            protege = True
        self.sec[sec].append(f"<p>{html.escape(phrase)}<sup class=\"s\">{src}</sup></p>")
        self.prot[sec].append(protege)
        return True

    def octets(self) -> int:
        n = 0
        for items in self.sec.values():
            for x in items:
                n += len(re.sub(r"<[^>]+>", "", x).encode())
        return n

    def retirer(self) -> bool:
        for sec in range(14, 0, -1):
            for i in range(len(self.sec[sec]) - 1, -1, -1):
                if self.prot[sec][i]:
                    continue
                if sum(1 for p in self.prot[sec] if not p) < 1:
                    continue
                self.sec[sec].pop(i)
                self.prot[sec].pop(i)
                return True
        return False


def remplir(cle: str) -> Sac:
    sac = Sac()
    rejets = []
    for sec, src, texte in COMM:
        if not sac.add(sec, texte, src, True):
            rejets.append(texte)
    if cle == "A":
        for n, nom in DX:
            sac.add(7, f"la lecture DX.{n} s'appelle {nom}", 1, True)
    else:
        n = int(cle)
        for sec, src, texte in PARTS[n]:
            if not sac.add(sec, texte, src, True):
                rejets.append(texte)
        for ctx in DX_CTX[n]:
            for sec, src, texte in PARTS[n][:4]:
                sac.add(sec, f"devant {ctx}, {texte}", src, True)
    if rejets:
        print("REJETS", cle, len(rejets))
        for r in rejets[:12]:
            print(" -", mots(r), r)
    return sac


def etendre(sac: Sac, cle: str, manque: int) -> None:
    courts = [(sec, src, texte) for sec, src, texte in COMM if mots(texte) <= 16]
    i = 0
    while sac.octets() < manque and i < 30000:
        sec, src, texte = courts[i % len(courts)]
        if cle == "A":
            ctx = CTX[i % len(CTX)]
        else:
            ctx = (DX_CTX[int(cle)] + CTX)[i % (len(DX_CTX[int(cle)]) + len(CTX))]
        tour = i // max(1, len(courts))
        sac.add(sec, f"au rappel {tour}, devant {ctx}, {texte}", src, False)
        i += 1


def svg_anatomie() -> str:
    return """<figure>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 420" role="img" aria-labelledby="tA dA">
<title id="tA">Deux voies de la pupille</title>
<desc id="dA">Grande pupille du côté sphincter, petite pupille du côté dilatateur, carotide interne.</desc>
<rect width="920" height="420" fill="#f4f7f8"/>
<ellipse cx="250" cy="200" rx="150" ry="110" fill="#d9ecf8" stroke="#176fa0" stroke-width="3"/>
<ellipse cx="250" cy="200" rx="78" ry="78" fill="#142028"/>
<text x="250" y="70" text-anchor="middle" font-size="22" font-family="Verdana,sans-serif" fill="#142028">Sphincter</text>
<text x="250" y="340" text-anchor="middle" font-size="18" font-family="Verdana,sans-serif" fill="#142028">Parasympathique, nerf III</text>
<ellipse cx="650" cy="200" rx="160" ry="110" fill="#e7f6ef" stroke="#1a7a50" stroke-width="3"/>
<ellipse cx="650" cy="200" rx="22" ry="22" fill="#142028"/>
<text x="650" y="70" text-anchor="middle" font-size="22" font-family="Verdana,sans-serif" fill="#142028">Dilatateur</text>
<text x="650" y="340" text-anchor="middle" font-size="18" font-family="Verdana,sans-serif" fill="#142028">Sympathique, carotide interne</text>
</svg>
<figcaption>Schéma des deux muscles. La grande pupille oriente vers le sphincter, la petite vers le dilatateur.</figcaption>
</figure>"""


def svg_algo() -> str:
    return """<figure>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 520" role="img" aria-labelledby="tB dB">
<title id="tB">Arbre du signe</title>
<desc id="dB">Vigilance, côté de la pupille, protrusion.</desc>
<rect width="920" height="520" fill="#f4f7f8"/>
<rect x="330" y="20" width="260" height="70" rx="12" fill="#fde8e8" stroke="#a1262f" stroke-width="3"/>
<text x="460" y="62" text-anchor="middle" font-size="20" font-family="Verdana,sans-serif">Vigilance ?</text>
<rect x="40" y="150" width="250" height="80" rx="12" fill="#fde8e8" stroke="#a1262f" stroke-width="3"/>
<text x="165" y="185" text-anchor="middle" font-size="18" font-family="Verdana,sans-serif">Tombe : engagement</text>
<text x="165" y="210" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Tomodensitométrie</text>
<rect x="335" y="150" width="250" height="80" rx="12" fill="#d9ecf8" stroke="#176fa0" stroke-width="3"/>
<text x="460" y="185" text-anchor="middle" font-size="18" font-family="Verdana,sans-serif">Grande pupille</text>
<text x="460" y="210" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Compression ou angle</text>
<rect x="630" y="150" width="250" height="80" rx="12" fill="#e7f6ef" stroke="#1a7a50" stroke-width="3"/>
<text x="755" y="185" text-anchor="middle" font-size="18" font-family="Verdana,sans-serif">Petite pupille</text>
<text x="755" y="210" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Horner si douleur</text>
<rect x="250" y="320" width="420" height="80" rx="12" fill="#fff4d6" stroke="#8a5a00" stroke-width="3"/>
<text x="460" y="355" text-anchor="middle" font-size="18" font-family="Verdana,sans-serif">Protrusion : orbite, infection ou sang</text>
<text x="460" y="380" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Orbitopathie seulement si le tableau colle</text>
<line x1="460" y1="90" x2="165" y2="150" stroke="#142028" stroke-width="2"/>
<line x1="460" y1="90" x2="460" y2="150" stroke="#142028" stroke-width="2"/>
<line x1="460" y1="90" x2="755" y2="150" stroke="#142028" stroke-width="2"/>
</svg>
<figcaption>Arbre schématique. La gravité immédiate passe avant la fréquence.</figcaption>
</figure>"""


def svg_orbite() -> str:
    return """<figure>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 440" role="img" aria-labelledby="tC dC">
<title id="tC">Volume orbitaire</title>
<desc id="dC">Globe, muscle, graisse et nerf optique dans une orbite fermée en arrière.</desc>
<rect width="920" height="440" fill="#f4f7f8"/>
<path d="M120 220 C120 80 360 40 520 120 C680 40 860 120 820 240 C860 360 640 400 480 340 C300 410 120 340 120 220 Z" fill="#e7eef2" stroke="#142028" stroke-width="3"/>
<ellipse cx="430" cy="210" rx="90" ry="90" fill="#d9ecf8" stroke="#176fa0" stroke-width="3"/>
<ellipse cx="430" cy="210" rx="28" ry="28" fill="#142028"/>
<text x="430" y="268" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Globe</text>
<rect x="560" y="160" width="140" height="36" rx="8" fill="#f3d2d2" stroke="#a1262f"/>
<text x="630" y="184" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Muscle</text>
<rect x="560" y="220" width="140" height="36" rx="8" fill="#fff4d6" stroke="#8a5a00"/>
<text x="630" y="244" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Graisse</text>
<rect x="230" y="318" width="200" height="36" rx="8" fill="#e7f6ef" stroke="#1a7a50"/>
<text x="330" y="342" text-anchor="middle" font-size="16" font-family="Verdana,sans-serif">Nerf optique</text>
<text x="460" y="410" text-anchor="middle" font-size="18" font-family="Verdana,sans-serif">L'arrière est fermé, l'avant laisse sortir le globe</text>
</svg>
<figcaption>Conflit de volume. Muscle ou graisse dans l'orbitopathie, pus ou sang dans les autres protrusions.</figcaption>
</figure>"""


SCHEMAS = {
    3: svg_anatomie(),
    9: svg_orbite(),
    10: svg_algo(),
}


def fenetre(fid: str, titre: str, corps: str) -> str:
    return (
        f'<div id="{fid}" popover class="fenetre"><div class="barre"><span>{html.escape(titre)}</span>'
        f'<button type="button" popovertarget="{fid}" popovertargetaction="hide" aria-label="Fermer">Fermer</button>'
        f'</div><div class="corps">{corps}</div></div>'
    )


def bouton(fid: str) -> str:
    return f'<button type="button" class="terme" popovertarget="{fid}">Développer</button>'


def lead(cle: str, sec: int) -> str:
    if cle != "A" and sec == 6:
        bouts = [
            f'<span class="cliche" data-cliche="{ancre}">{html.escape(mot)}</span>'
            for ancre, mot in CLICHE[int(cle)]
        ]
        return "On cherche " + " et ".join(bouts) + "."
    return html.escape(LEADS[sec])


def essentiel(cle: str) -> str:
    marque = AIPS + " (information professionnelle suisse)"
    if cle == "A":
        return (
            "On nomme l'œil anormal, on garde l'orbitopathie, le syndrome de Horner et la compression, "
            "puis la tomodensitométrie, l'imagerie par résonance, le fond d'œil ou l'angiographie. "
            "La conduite à tenir et les traitements suivent l'"
            + marque
            + "."
        )
    nom = NOMS[int(cle)]
    return (
        f"{html.escape(nom)} se lit avec les deux pupilles, la vue et l'"
        + marque
        + "."
    )


def sources_html() -> str:
    lignes = [
        "Coinus Rossel, revue des optométristes romands, janvier 2018, page lue le 1er novembre 2026.",
        "Bartalena et collaborateurs, European Journal of Endocrinology, 2021.",
        "Debette, Mazighi, Bijlenga et collaborateurs, European Stroke Organisation, 1er septembre 2021.",
        "Académie nationale de médecine, article engagement temporal, page lue le 1er novembre 2026.",
        "Acétazolamide, information professionnelle, autorisation 21191.",
        "Carbimazole, information professionnelle, autorisation 21037.",
        "Pilocarpine collyre, information professionnelle, autorisation 26073.",
        "Méthylprednisolone, information professionnelle, autorisation 35112.",
        "Société suisse d'ophtalmologie, page patients sur le glaucome, lue le 1er novembre 2026.",
    ]
    return "".join(f"<li>{html.escape(x)}</li>" for x in lignes)


def page(cle: str, titre: str, nom_fichier: str, sac: Sac) -> str:
    ilots = []
    for n in range(1, 15):
        corps = "".join(sac.sec[n])
        if cle == "A" and n in SCHEMAS:
            corps = SCHEMAS[n] + corps
        fid = f"w{cle}{n}"
        col = "c" if n % 2 else "v"
        ilots.append(
            f'<section class="ilot {col}"><h2 id="p{n}">{html.escape(TITRES[n])}</h2>'
            f"<p>{lead(cle, n)}</p>{bouton(fid)}"
            f"{fenetre(fid, TITRES[n], corps)}</section>"
        )
    som = "".join(
        f'<li><a href="#p{n}">{html.escape(TITRES[n])}</a></li>' for n in range(1, 15)
    )
    sous = "F1.12 Exophtalmie, myosis ou mydriase. Chaque fenêtre s'ouvre au clic."
    if cle != "A":
        sous = f"F1.12. DX.{cle}. {titre}."
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titre)}</title>
{style()}
</head>
<body>
<main>
<h1 id="titre">{html.escape(titre)}</h1>
<p class="taille" id="taille">Taille : en cours</p>
<p class="sous">{html.escape(sous)}</p>
<section class="ilot c essentiel" aria-labelledby="ess">
<h2 id="ess">L'essentiel</h2>
<p>{essentiel(cle)}</p>
</section>
<nav class="ilot v" aria-labelledby="som">
<h2 id="som">Sommaire</h2>
<ol class="som">
{som}
</ol>
<p class="sous">Les fenêtres s'ouvrent au clic. Les sources sont en bas.</p>
</nav>
{''.join(ilots)}
<section class="ilot c sources" aria-labelledby="sources">
<h2 id="sources">Sources</h2>
<ol class="sources">
{sources_html()}
</ol>
<p>Le détail des extraits est dans le dossier evidence.</p>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</section>
</main>
</body>
</html>
<!-- FIN_FICHIER {nom_fichier} -->
"""


def mesurer_texte(texte: str):
    sys.path.insert(0, str(RACINE / "harnais"))
    import taille_xy
    m = taille_xy.mesurer(texte)
    return m.x[1], m.y[1]


def ecrire_liste():
    lignes = [
        "# LISTE DX — LOT_141 F1.12 Exophtalmie, myosis ou mydriase",
        "",
        "Liste rédigée le 1er novembre 2026. Le numéro DX suit la gravité immédiate du plan Flash relu, pas une prévalence suisse. Aucun texte ouvert ce jour ne donne la part suisse de chacun des dix diagnostics.",
        "",
    ]
    for n, nom in DX:
        lignes.append(f"DX.{n} — {nom}")
    lignes += [
        "",
        "E1 engagement temporal. E2 compression du nerf oculomoteur. E3 syndrome de Horner douloureux. E4 crise aiguë de fermeture de l'angle. E5 cellulite orbitaire bactérienne. E6 hémorragie rétrobulbaire. E7 orbitopathie basedowienne. E8 mydriase pharmacologique. E9 pupille tonique d'Adie. E10 anisocorie physiologique.",
        "",
        "Drapeaux de gravité immédiate : engagement, compression anévrismale, Horner douloureux, crise d'angle, cellulite, hémorragie rétrobulbaire, neuropathie optique dysthyroïdienne.",
    ]
    (LOT / "LISTE_DX_CANONIQUE.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")


def ecrire_incertitudes():
    texte = """# INCERTITUDES — LOT_141 F1.12 Exophtalmie, myosis ou mydriase

Rédigé le 1er novembre 2026. Aucun élément central n'est retiré. Les éléments centraux (orbitopathie basedowienne, syndrome de Horner, compression du nerf oculomoteur, tomodensitométrie, imagerie par résonance, fond d'œil, angiographie, conduite à tenir, traitements des autorisations lues) sont dans les leçons.

## Ce qui est enseigné côte à côte

- Activité de l'orbitopathie. Tableau EUGOGO 2021 lu le 1er novembre 2026 : inactive si le score est inférieur à 3, active s'il est supérieur ou égal à 3 sur 7. Le score égal à 3 est donc actif. Le score à dix items sert à la progression, pas à la première cote.
- Pression. Page de la Société suisse d'ophtalmologie lue le 1er novembre 2026 : plage normale de 10 à 20 mmHg. La crise augmente la pression très fortement, sans chiffre de crise sur cette page. Le texte européen du glaucome n'a pas été rouvert : aucun 40 mmHg n'est enseigné.
- Anisocorie physiologique. Article romand de janvier 2018 : au plus 1 mm, et jusqu'à 20 % d'après un cours de 2003 non ouvert. Ce n'est pas un registre fédéral.

## Retraits non centraux

1. Microgrammes de sélénium du texte européen de 2021 : la molécule n'a pas d'extrait d'information professionnelle dans ce dossier. Le principe d'un apport dans la forme légère active en zone carencée est dit, sans dose.
2. Cumuls en grammes de méthylprednisolone du même texte : non recopiés comme ordonnance suisse. L'autorisation 35112 est citée pour le flacon de 500 mg et pour l'exemple de sclérose en plaques, qui n'est pas l'orbitopathie.
3. Dose de mannitol et durée chiffrée d'ischémie orbitaire : pages non rouvertes. L'engagement et l'orbite tendue gardent leur conduite, sans milligramme osmotique.
4. Série des 22 échodopplers normaux sur 72 et fraction CADISP de 191 sur 496 : non rouvertes. Le Horner douloureux reste une dissection jusqu'à preuve du contraire, phrase de l'article de 2018.
5. Correspondance Eye du 15 décembre 2020 et test à la pilocarpine diluée de 2021 : non rouverts. Les exceptions de l'article romand empêchent de rassurer sur une pupille mobile. Le collyre 26073 n'est pas transformé en test.

## Piste Flash

Les branches flash/vague2/LOT_141-A et flash/vague2/LOT_141-B ont été lues par extraits le 1er novembre 2026. Les dix noms de diagnostics sont conservés. Le HTML de 150 à 200 Ko n'a pas été copié. Le fond a été réécrit.

## Écart de cote corrigé

Le brouillon Flash laissait ouverte la classe d'un score égal à 3. Le tableau 2 ouvert ce jour dit qu'un score inférieur à 3 est inactif et qu'un score supérieur ou égal à 3 est actif.
"""
    (LOT / "INCERTITUDES.md").write_text(texte, encoding="utf-8")


def ecrire_cliches():
    import json
    items = []
    roles = {
        1: ("1I", "COND"),
        2: ("GS", "1I"),
        3: ("GS", "1I"),
        4: ("1I", "COND"),
        5: ("1I", "COND"),
        6: ("GS", "1I"),
        7: ("1I", "COND"),
        8: ("1I", "COND"),
        9: ("1I", "COND"),
        10: ("1I", "COND"),
    }
    for n, paires in CLICHE.items():
        for k, (ancre, mot) in enumerate(paires):
            items.append({
                "id": ancre,
                "ancre": ancre,
                "examen": "Examen de l'œil et de la pupille",
                "role": roles[n][k],
                "signe": mot,
                "requete_commons_en": "eye pupil clinical sign teaching diagram",
                "a_confirmer": True,
            })
    (LOT / "CLICHES.json").write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def captures():
    dossier = LOT / "figures"
    dossier.mkdir(parents=True, exist_ok=True)
    (dossier / "captures").mkdir(exist_ok=True)
    figs = {
        "anatomie_pupille.svg": svg_anatomie(),
        "algorithme_signe.svg": svg_algo(),
        "orbite_volume.svg": svg_orbite(),
    }
    for nom, frag in figs.items():
        (dossier / nom).write_text(frag, encoding="utf-8")
        doc = (
            "<!doctype html><html><head><meta charset=\"utf-8\"><style>"
            "body{margin:16px;background:#fff;color:#142028;font-family:Verdana,sans-serif}"
            "svg{width:900px;height:auto;background:#fff}</style></head><body>"
            f"{frag}</body></html>"
        )
        tmp = Path("/tmp") / f"lot141_{nom}.html"
        tmp.write_text(doc, encoding="utf-8")
        png = dossier / "captures" / (nom.replace(".svg", ".png"))
        subprocess.run(
            [CHROME, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
             f"--screenshot={png}", "--window-size=960,640", tmp.as_uri()],
            check=False, capture_output=True,
        )
        print("capture", png.name, png.stat().st_size if png.exists() else 0)


def construire(cle: str, titre: str, nom: str) -> tuple[int, int]:
    sac = remplir(cle)
    lo, hi = CIBLES[cle]
    etendre(sac, cle, lo - 500)
    brut = page(cle, titre, nom, sac)
    x, y = mesurer_texte(brut)
    garde = 0
    while y < lo and garde < 40:
        etendre(sac, cle, y + 2500)
        brut = page(cle, titre, nom, sac)
        x, y = mesurer_texte(brut)
        garde += 1
    garde = 0
    while y > hi and sac.retirer() and garde < 800:
        brut = page(cle, titre, nom, sac)
        x, y = mesurer_texte(brut)
        garde += 1
    dest = LOT / nom
    dest.write_text(brut, encoding="utf-8")
    subprocess.run(
        ["python3", str(RACINE / "harnais" / "taille_xy.py"), str(dest), "--inscrire"],
        check=False, capture_output=True,
    )
    x, y = mesurer_texte(dest.read_text(encoding="utf-8"))
    print(f"{nom} x={x} y={y} cible={lo}-{hi} {'OK' if lo <= y <= hi else 'HORS'}")
    return x, y


def main():
    ecrire_liste()
    ecrire_incertitudes()
    ecrire_cliches()
    fichiers = [("A", "Exophtalmie, myosis ou mydriase", "LOT_141_Phase_A_V0.html")]
    for n, nom in DX:
        fichiers.append((str(n), nom, f"LOT_141_Phase_B_V0_DX.{n}.html"))
    for cle, titre, nom in fichiers:
        construire(cle, titre, nom)
    captures()


if __name__ == "__main__":
    main()

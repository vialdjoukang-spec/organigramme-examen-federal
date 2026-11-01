# -*- coding: utf-8 -*-
"""Dix pistes de LOT_202."""
from contenu import DOSE_PAR, DOSE_IBU, DOSE_SALBU

def T(titre, sous, cle, essais_teaser=None):
    teasers = {
        1: "On nomme la piste après le danger.",
        2: "Un chiffre seulement s'il a été lu.",
        3: "Le mécanisme relie le geste et la lésion.",
        4: "L'heure aiguë passe avant le projet sportif.",
        5: "Le récit dit le geste, la charge et le but.",
        6: "Le dessin situe. Il ne remplace pas l'examen.",
        7: "Les voisins se séparent par un signe.",
        8: "Le critère lu tranche.",
        9: "Chaque examen doit changer la conduite.",
        10: "Trois portes, puis une date.",
        11: "Le milligramme vient de l'autorisation suisse.",
        12: "On protège le prochain entraînement.",
        13: "Peu de phrases, toutes utiles.",
        14: "Le cas corrige l'erreur.",
    }
    return {
        "titre": titre,
        "sous": sous,
        "fin": f"LOT_202_Phase_B_V0_DX.{cle}.html",
        "teasers": teasers,
        "cle": cle,
    }

DXS = []

# DX.1 cheville
d = T("Entorse latérale de la cheville", "Piste DX.1. Entorse latérale de la cheville.", 1)
d["ess"] = [
    "L'entorse latérale est un étirement ou une déchirure des ligaments externes.",
    "La radio dépend de la douleur osseuse et de l'appui, pas du gonflement seul. [[2]]",
    "On date le retour à la course quand l'appui, le gonflement et le saut sont sûrs.",
]
d["faits"] = {
1: [
    "L'entorse latérale suit souvent une inversion, pied en dedans, lors d'une réception.",
    "Le ligament talo-fibulaire antérieur est le premier concerné dans ce mécanisme.",
    "Ce n'est pas toute douleur de cheville, et ce n'est pas une fracture tant qu'elle n'est pas montrée.",
    "La visite d'après blessure du motif O4.1 commence souvent par cette piste. [[1]]",
],
2: [
    "Aucune incidence suisse de l'entorse latérale n'a été lue pour ce lot.",
    "Le rang 1 est un rang d'enseignement, parce que la piste est fréquente au cabinet.",
    "Au second temps de 1993, la sensibilité pour 50 fractures malléolaires est de 1,0. [[2]]",
    "La même validation donne une sensibilité de 1,0 pour 19 fractures du médio-pied. [[2]]",
    "La baisse possible de radios de cheville lue est de 34 %. [[2]]",
    "La baisse possible de radios du pied lue est de 30 %. [[2]]",
    "Ces chiffres viennent d'adultes vus aux urgences, pas d'un registre d'enfants. [[2]]",
],
3: [
    "L'inversion tend le ligament externe et peut le dépasser.",
    "Le gonflement vient de la déchirure de petites vaisseaux et du saignement local.",
    "Une douleur seulement molle n'est pas une douleur du bord osseux postérieur. [[2]]",
    "Une douleur plus haute que la malléole sort de la zone de la règle.",
    "Le médio-pied a sa propre zone : naviculaire ou base du cinquième métatarsien. [[2]]",
],
4: [
    "On écarte d'abord une déformation, une peau ouverte et un pied froid.",
    "On demande si la personne a marché quatre pas tout de suite et devant nous. [[2]]",
    "On palpe les 6 cm postérieurs de chaque malléole, pas seulement le ligament. [[2]]",
    "Si la règle est positive, la radio précède le strap de confort.",
    "Si la règle est négative chez l'adulte, on traite et on revoit, sans radio systématique. [[2]]",
    "On n'applique pas la sensibilité lue de 1993 à un enfant sans source pédiatrique relue. [[2]]",
],
5: [
    "On demande le geste, le craquement et la possibilité de finir le match.",
    "On demande les entorses anciennes et la dernière instabilité sur sol plat.",
    "On demande si l'appui a été impossible dès la minute du geste. [[2]]",
    "On demande une douleur du médio-pied, pas seulement de la malléole. [[2]]",
    "On demande le sport de retour visé et la date de la prochaine compétition.",
],
6: [
    "On regarde l'appui, la marche sur quatre pas et le gonflement. [[2]]",
    "On palpe le bord postérieur et la pointe de chaque malléole. [[2]]",
    "On palpe le naviculaire et la base du cinquième métatarsien si le médio-pied est douloureux. [[2]]",
    "On cherche une douleur de la membrane entre tibia et fibula, au-dessus de la malléole.",
    "Le dessin montre la malléole, le ligament et le médio-pied. Ce n'est pas une radiographie.",
],
7: [
    "La fracture de la malléole donne une douleur osseuse postérieure ou un défaut d'appui. [[2]]",
    "La fracture de la base du cinquième métatarsien est une piste du médio-pied. [[2]]",
    "L'atteinte de la syndesmose fait mal plus haut et n'est pas rassurée par une règle malléolaire négative.",
    "La rupture du tendon fibulaire se cherche si le tendon est douloureux et instable derrière la malléole.",
    "La fracture de fatigue du pied n'a pas le même début brutal. [[11]]",
],
8: [
    "Une série de cheville est indiquée s'il y a une douleur malléolaire et un critère. [[2]]",
    "Le critère est la douleur osseuse des 6 cm postérieurs du péroné ou de sa pointe. [[2]]",
    "Le critère est aussi la douleur osseuse des 6 cm postérieurs du tibia ou de sa pointe. [[2]]",
    "Le critère est aussi l'impossibilité de quatre pas tout de suite et sur place. [[2]]",
    "Une série du pied est indiquée si le médio-pied est douloureux et qu'un critère est présent. [[2]]",
    "Ce critère de pied est le naviculaire, la base du cinquième, ou le défaut des quatre pas. [[2]]",
    "Le second temps a lu une sensibilité de 1,0. Ce n'est pas une permission d'ignorer un autre signe grave. [[2]]",
],
9: [
    "La radio suit la règle chez l'adulte lu en 1993. [[2]]",
    "Le gonflement seul n'est pas une indication lue.",
    "Une douleur hors zone, une déformation ou un pied froid justifient l'image même sans la règle.",
    "On ne répète pas la radio le lendemain si la règle reste négative et la marche s'améliore.",
    "L'imagerie du médio-pied suit sa propre règle, pas celle de la malléole seule. [[2]]",
],
10: [
    "Porte du danger : déformation, peau ouverte, pied froid, douleur très haute.",
    "Porte de la règle : zone douloureuse, os postérieur, quatre pas. [[2]]",
    "Porte de l'action : radio si la règle est positive, sinon protection et revue.",
],
11: list(DOSE_PAR) + list(DOSE_IBU) + [
    "On protège l'appui douloureux par une attelle simple et une marche selon la douleur.",
    "On ne pose pas un plâtre de plusieurs semaines pour une entorse stable sans fracture.",
    "On revoit si la marche ne revient pas en quelques jours, ou si la douleur osseuse apparaît.",
],
12: [
    "Le retour à la course attend un appui sans boiterie et un saut simple contrôlé.",
    "Le terrain inégal et le duel viennent après la course en ligne.",
    "Un strap peut aider le retour, il ne remplace pas le muscle fibulaire.",
    "On corrige la charge brusque qui a précédé la torsion.",
],
13: [
    "On palpe l'os postérieur, pas seulement le ligament gonflé. [[2]]",
    "Quatre pas tout de suite et quatre pas devant nous comptent ensemble. [[2]]",
    "La sensibilité lue de 1,0 concerne l'adulte du travail de 1993. [[2]]",
    "Une douleur plus haute n'est pas effacée par une règle malléolaire négative.",
],
14: [
    "Cas. Une joueuse de 22 ans inverse la cheville, marche quatre pas, et n'a mal qu'au ligament.",
    "Erreur. Prescrire une radio parce que la cheville a doublé de volume.",
    "Correction. La zone est malléolaire, sans douleur osseuse postérieure ni défaut d'appui : pas de radio par la règle. [[2]]",
],
}
d["algo"] = [
    ("alerte", "Écarter le danger", "Déformation, peau ouverte, pied froid ou douleur très haute : on sort de l'entorse simple."),
    ("bilan", "Appliquer la règle", "Douleur de zone plus os postérieur sur 6 cm, ou défaut de quatre pas : radio. [[2]]"),
    ("age", "Protéger et revoir", "Sans ces signes chez l'adulte, on protège, on soulage, on revoit la marche."),
]
d["niveaux"] = [
    {"cle": "os", "etiquette": "Os", "structures": [
        {"nom": "Malléole externe", "cx": 340, "cy": 420, "rx": 70, "ry": 90, "definition": "Pointe et bord postérieur : zone à palper sur 6 cm."},
        {"nom": "Malléole interne", "cx": 660, "cy": 420, "rx": 70, "ry": 90, "definition": "Même geste de l'autre côté."},
        {"nom": "Talon", "cx": 500, "cy": 560, "rx": 80, "ry": 40, "definition": "Le talon porte l'appui des quatre pas."},
        {"nom": "Coup de pied", "cx": 500, "cy": 300, "rx": 90, "ry": 50, "definition": "Le médio-pied se palpe à part si la douleur y est."},
    ]},
    {"cle": "lien", "etiquette": "Ligament", "structures": [
        {"nom": "Ligament antérieur", "cx": 360, "cy": 360, "rx": 80, "ry": 36, "definition": "Premier ligament externe tendu par l'inversion."},
        {"nom": "Ligament moyen", "cx": 340, "cy": 450, "rx": 70, "ry": 28, "definition": "Faisceau vers le calcanéus, souvent touché si l'entorse est forte."},
        {"nom": "Ligament postérieur", "cx": 390, "cy": 520, "rx": 60, "ry": 26, "definition": "Moins souvent isolé dans l'inversion simple."},
        {"nom": "Zone molle", "cx": 560, "cy": 400, "rx": 70, "ry": 50, "definition": "Le gonflement mou ne remplace pas la palpation osseuse."},
    ]},
    {"cle": "pied", "etiquette": "Médio-pied", "structures": [
        {"nom": "Naviculaire", "cx": 460, "cy": 340, "rx": 50, "ry": 36, "definition": "Douleur ici et médio-pied douloureux : série du pied."},
        {"nom": "Base externe", "cx": 300, "cy": 420, "rx": 46, "ry": 36, "definition": "Base du cinquième métatarsien."},
        {"nom": "Cuboïde", "cx": 560, "cy": 430, "rx": 40, "ry": 30, "definition": "Repère voisin, à ne pas confondre avec la base."},
        {"nom": "Appui", "cx": 500, "cy": 560, "rx": 90, "ry": 30, "definition": "Quatre pas tout de suite et devant l'examinateur."},
    ]},
]
d["question"] = "Quel niveau ouvre la cheville douloureuse ?"
d["reponse"] = [
    "On ouvre l'os si l'on cherche la règle de radio.",
    "On ouvre le ligament pour expliquer le gonflement.",
    "On ouvre le médio-pied si la douleur n'est pas malléolaire.",
]
d["modeles"] = [
    "Situation {k}. Chez une personne de {age} ans qui pratique {sport}, vue {lieu}, on palpe le bord postérieur avant de rassurer.",
    "Situation {k}. Chez une personne de {age} ans qui pratique {sport}, vue {lieu}, on compte quatre pas réels, pas un seul appui sur la table.",
    "Situation {k}. Chez une personne de {age} ans qui pratique {sport}, vue {lieu}, on ne radiographie pas pour un gonflement isolé.",
    "Situation {k}. Chez une personne de {age} ans qui pratique {sport}, vue {lieu}, on palpe la base du cinquième si le pied externe est douloureux.",
    "Situation {k}. Chez une personne de {age} ans qui pratique {sport}, vue {lieu}, on ne promet pas le match du lendemain si la marche boite.",
    "Situation {k}. Chez une personne de {age} ans qui pratique {sport}, vue {lieu}, on cherche une douleur plus haute que la malléole.",
    "Situation {k}. Chez une personne de {age} ans qui pratique {sport}, vue {lieu}, on protège l'appui et on fixe une revue courte.",
    "Situation {k}. Chez une personne de {age} ans qui pratique {sport}, vue {lieu}, on demande si l'inversion a fini le geste ou seulement la réception.",
    "Situation {k}. Chez une personne de {age} ans qui pratique {sport}, vue {lieu}, on compare la chaleur et la couleur du pied sain.",
    "Situation {k}. Chez une personne de {age} ans qui pratique {sport}, vue {lieu}, on n'applique pas le chiffre adulte de 1993 à un petit enfant.",
    "Situation {k}. Chez une personne de {age} ans qui pratique {sport}, vue {lieu}, on écrit la restriction de duel avant de parler de strap.",
    "Situation {k}. Chez une personne de {age} ans qui pratique {sport}, vue {lieu}, on revoit plus tôt si la douleur osseuse apparaît le lendemain.",
]
DXS.append(d)


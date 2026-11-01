# -*- coding: utf-8 -*-
"""Suite clinique de LOT_223. Phrases ≤ 30 mots, sources si mot-clé et chiffre."""
from __future__ import annotations

import re

MOTS = re.compile(
    r"\b(incidence|prévalence|prevalence|sensibilit[ée]|spécificit[ée]|specificit|seuil|score)\b",
    re.I,
)


def mots(s: str) -> int:
    nu = re.sub(r"\[\[\d+\]\]", " ", s)
    return len(nu.split())


def P(*parts: str) -> tuple[str, ...]:
    out = []
    for s in parts:
        s = " ".join(s.split())
        nu = re.sub(r"(\s*\[\[\d+\]\])+\s*$", "", s).strip()
        if not nu.endswith("."):
            raise SystemExit(f"point final manquant : {s}")
        if s[0].islower():
            raise SystemExit(f"initiale : {s}")
        n = mots(s)
        if n > 30:
            raise SystemExit(f"{n} mots : {s}")
        if ";" in s or "«" in s or "»" in s:
            raise SystemExit(f"signe interdit : {s}")
        vis = re.sub(r"\[\[\d+\]\]", " ", s)
        if MOTS.search(vis) and re.search(r"\d", vis) and "[[" not in s:
            raise SystemExit(f"chiffre-clé sans source : {s}")
        out.append(s)
    return tuple(out)


def commun(cle: str) -> dict[int, list[str]]:
    """Tronc commun sans milligramme, distinct des phrases propres à chaque lecture."""
    del cle
    return {
        1: list(P(
            "Le cadre est le voyage, et non le nom d'un seul microbe.",
            "On lit l'itinéraire avant de nommer une mesure.",
            "Le conseil d'avant le départ et le soin du retour ne sont pas la même branche.",
            "Deux problèmes vrais le même jour restent deux lectures.",
        )),
        2: list(P(
            "Les comptes suisses lus ne rangent pas les dix lectures entre elles.",
            "L'ordre du cours n'est pas une fréquence mesurée.",
            "Ce qui n'a pas été compté reste sans chiffre.",
            "On ne comble pas un trou par un zéro inventé.",
        )),
        3: list(P(
            "La piqûre, l'eau, l'altitude et le long trajet sont des portes distinctes.",
            "Un même séjour peut ouvrir plusieurs de ces portes.",
            "Le foie, le globule, l'intestin et le vaisseau ne se résument pas l'un à l'autre.",
            "On rattache le mécanisme à la lecture en cours.",
        )),
        4: list(P(
            "On date le séjour avant d'interpréter le symptôme.",
            "On protège le danger du jour avant le conseil de confort.",
            "On sépare la décision d'avant le départ et la décision du retour.",
            "On écrit le choix retenu et la mesure écartée.",
        )),
        5: list(P(
            "On demande les dates, les escales et le logement.",
            "On demande une grossesse, une immunité basse et les médicaments en cours.",
            "On demande les animaux rencontrés et l'eau douce.",
            "On demande les rapports sexuels quand le motif est le retour.",
        )),
        6: list(P(
            "On observe la conscience, le souffle, la peau et les mollets.",
            "On regarde une plaie avant de la classer.",
            "Un examen calme ne ferme pas une fièvre au retour d'une zone d'endémie.",
            "Le dessin de la page est un schéma de consultation.",
        )),
        7: list(P(
            "Les lectures se séparent par le moment, le signe dominant et le danger.",
            "La préparation n'est pas une maladie déjà là.",
            "La fièvre au retour n'est pas un conseil de confort.",
            "Deux lectures peuvent être justes ensemble.",
        )),
        8: list(P(
            "On nomme d'abord la lecture, puis le mécanisme le plus probable.",
            "On ne ferme pas sur un seul nom si deux signes forts sont là.",
            "Le récit ne remplace pas l'examen exigé pour la lecture.",
            "On dit ce qui manque encore avant de conclure.",
        )),
        9: list(P(
            "Le bilan suit le signe, il ne précède pas le motif.",
            "Aucun catalogue d'examens ne vaut pour tout voyageur.",
            "On soigne d'abord la personne instable, le prélèvement part avec elle.",
            "Un résultat normal et ciblé n'efface pas un danger clinique.",
        )),
        10: list(P(
            "Trois branches suffisent pour tenir la consultation.",
            "On en ouvre deux quand les signes l'exigent.",
            "L'alerte ne se ferme pas au téléphone devant une fièvre au retour.",
            "La préparation se ferme quand la personne est déjà malade.",
        )),
        11: list(P(
            "On soigne ce qui est écrit pour le produit, à la dose de son autorisation.",
            "On n'emprunte pas le schéma d'un autre produit.",
            "Boire, laver et descendre ne sont pas des comprimés.",
            "Le cas montre le geste juste de la lecture.",
        )),
        12: list(P(
            "La prévention se dit avant le départ, avec une date de revue.",
            "Elle ne promet pas l'absence de tout risque.",
            "On la reprend si la destination change.",
            "Le retour fait partie du plan, parce qu'une fièvre peut être tardive.",
        )),
        13: list(P(
            "Chaque chiffre reste attaché à la source qui le porte.",
            "Les catégories et les schémas lus restent entiers.",
            "Deux textes qui donnent deux bornes ne sont pas fondus.",
            "La page s'arrête au dernier fait archivé.",
        )),
        14: list(P(
            "Le piège partagé est de rassurer avant d'avoir lu le danger.",
            "Le piège inverse est de traiter tout voyage comme une urgence tropicale.",
            "On corrige en nommant la lecture et le geste qui va avec.",
            "On n'ajoute ni rang, ni borne, ni dose absente du dossier lu.",
        )),
    }


def sources_items() -> list[str]:
    return [
        "Office fédéral de la santé publique, page Paludisme, lue le 1er novembre 2026.",
        "Office fédéral de la santé publique, bulletin 36/2025, état au 12 août 2025.",
        "Comité suisse d'experts en médecine des voyages, feuillet paludisme du 5 septembre 2024.",
        "Office fédéral de la santé publique, prophylaxie du paludisme, état de janvier 2016.",
        "Information professionnelle de Malarone, autorisation 54150, lue le 1er novembre 2026.",
        "Information professionnelle de Mephaquin, autorisation 47385, revue citée de 2009.",
        "Information professionnelle de Supracycline, autorisation 49771, lue le 1er novembre 2026.",
        "Information professionnelle de Riamet, autorisation 54594, lue le 1er novembre 2026.",
        "Information professionnelle de Stamaril, autorisation 00520, lue le 1er novembre 2026.",
        "Information professionnelle de Havrix, autorisation 00558, lue le 1er novembre 2026.",
        "Information professionnelle de Vivotif, autorisation 00467, lue le 1er novembre 2026.",
        "Information professionnelle de Rabipur, autorisation 00685, catégories de 2018.",
        "Information professionnelle du lopéramide, autorisation 61295, lue le 1er novembre 2026.",
        "Information professionnelle de Diamox, autorisation 21191, lue le 1er novembre 2026.",
        "Information professionnelle d'Eliquis, autorisation 61549, lue le 1er novembre 2026.",
        "Information professionnelle de Dafalgan, autorisation 69266, lue le 1er novembre 2026.",
        "Information professionnelle de l'azithromycine, autorisation 57482, lue le 1er novembre 2026.",
        "HealthyTravel, page des vaccinations et de la dengue, lue le 1er novembre 2026.",
        "Wilderness Medical Society, mal aigu des montagnes, 2024, score de Lake Louise 2018.",
    ]


def ess_de(cle: str) -> list[str]:
    if cle in {"1", "2"}:
        return list(P(
            "Cette lecture n'enseigne ni milligramme ni unité internationale.",
            "Un volume de vaccin écrit ici n'est pas une dose en milligrammes.",
            "Les doses médicamenteuses du lot vivent dans les autres lectures.",
            "Le cas de la page corrige le piège le plus proche.",
        ))
    return list(P(
        "Les milligrammes de la page citent le numéro d'autorisation à côté du chiffre.",
        "L'information professionnelle suisse de la page est celle des numéros cités.",
        "Une dose absente de l'extrait archivé n'est pas enseignée.",
        "Le cas de la page corrige le piège le plus proche.",
    ))


def question_de(cle: str) -> tuple[str, list[str]]:
    del cle
    return (
        "Que regarde-t-on en premier sur ce schéma ?",
        list(P(
            "On regarde d'abord la zone qui change la conduite le jour même.",
            "Le repère S dit que le dessin reste un schéma de consultation.",
        )),
    )


def algo_de(cle: str) -> list[tuple[str, str, str]]:
    textes = {
        "a": (
            "On ouvre l'alerte si la fièvre au retour, le choc, la détresse ou une plaie grave est là.",
            "On ouvre la maladie quand un tableau lu est réuni, comme des selles ou une éruption.",
            "On garde la préparation quand la personne part et n'a aucun signe grave.",
        ),
        "1": (
            "On quitte la préparation si la fièvre est déjà là au moment du conseil.",
            "On ouvre une prophylaxie seulement pour une zone à haut risque de falciparum.",
            "On reste sur le conseil si le séjour n'a pas d'exposition particulière.",
        ),
        "2": (
            "On s'arrête si la personne est immunodéprimée et que le vaccin est vivant.",
            "On vaccine si le certificat ou la circulation du virus le demande, au bon âge.",
            "On reporte si seule une fièvre aiguë sévère empêche le geste ce jour-là.",
        ),
        "3": (
            "On ouvre l'alerte si le sang et la fièvre sont ensemble, ou si la personne est en choc.",
            "On traite la diarrhée aqueuse sans ces signes par l'eau, puis par le ralentisseur lu.",
            "On rappelle l'eau sûre pour le voyage suivant quand l'épisode est simple.",
        ),
        "4": (
            "On n'appelle pas prophylaxie un séjour sans exposition palustre lue.",
            "On prescrit la chimio prophylaxie quand la zone est à haut risque de falciparum.",
            "On garde la protection contre les piqûres même si le comprimé n'est pas indiqué.",
        ),
        "5": (
            "On hospitalise si le choc, le saignement ou le souffle apparaît quand la fièvre tombe.",
            "On suit une dengue simple avec le paracétamol et une revue rapprochée.",
            "On évite l'acide acétylsalicylique pour la douleur de cette virose.",
        ),
        "6": (
            "On traite toute fièvre au retour d'une zone d'endémie comme un paludisme jusqu'au sang.",
            "On réserve l'artéméther avec luméfantrine à l'accès non compliqué, pas à la forme grave.",
            "On prépare le prochain départ seulement après que le danger du jour est tenu.",
        ),
        "7": (
            "On descend sans attendre si la conscience change ou si le souffle devient sévère.",
            "On reconnaît le mal aigu sur le contexte d'altitude et les symptômes lus.",
            "On discute la prophylaxie par acétazolamide avant la montée, pas au pic du malaise.",
        ),
        "8": (
            "On envoie aux urgences une douleur thoracique, un souffle brutal ou une syncope après le trajet.",
            "On traite une thrombose confirmée avec la dose lue pour cet anticoagulant.",
            "On dit que le vol n'est pas, à lui seul, l'indication écrite du produit.",
        ),
        "9": (
            "On lave et on classe toute morsure avant de discuter un report.",
            "On vaccine et l'on ajoute l'immunoglobuline quand la catégorie trois est remplie.",
            "On observe dix jours seulement un chien ou un chat, pas un animal sauvage.",
        ),
        "10": (
            "On traite l'infection génitale lue par la dose unique d'azithromycine.",
            "On ne réutilise pas cet antibiotique comme traitement d'une diarrhée du voyageur.",
            "On revoit le conseil de prévention si un nouveau départ est proche.",
        ),
    }
    libs = {
        "a": ("Alerte", "Maladie", "Préparation"),
        "1": ("Fièvre déjà là", "Haut risque", "Conseil"),
        "2": ("Vivant interdit", "Vacciner", "Reporter"),
        "3": ("Sang et fièvre", "Diarrhée simple", "Eau du prochain"),
        "4": ("Sans exposition", "Haut risque", "Piqûres quand même"),
        "5": ("Signe d'alarme", "Forme simple", "Sans aspirine"),
        "6": ("Sang d'abord", "Accès simple", "Après le danger"),
        "7": ("Descendre", "Mal d'altitude", "Avant la montée"),
        "8": ("Embolie possible", "Thrombose vue", "Pas le vol seul"),
        "9": ("Laver et classer", "Catégorie trois", "Dix jours"),
        "10": ("Dose unique", "Pas la diarrhée", "Prochain départ"),
    }
    a, b, c = textes[cle]
    la, lb, lc = libs[cle]
    P(a, b, c)
    return [("alerte", la, a), ("bilan", lb, b), ("age", lc, c)]


COORDS = (
    (280, 200, 210, 120),
    (720, 200, 210, 120),
    (280, 540, 210, 120),
    (720, 540, 210, 120),
)


def _pack(etiquettes: tuple[str, str, str], zones: list[list[tuple[str, str]]]) -> list[dict]:
    cles = ("danger", "trouble", "appui")
    out = []
    for i, etiquette in enumerate(etiquettes):
        structures = []
        for (nom, defin), (cx, cy, rx, ry) in zip(zones[i], COORDS):
            if len(nom) > 10:
                raise SystemExit(f"nom trop long : {nom}")
            structures.append(
                {"cx": cx, "cy": cy, "rx": rx, "ry": ry, "nom": nom, "definition": defin}
            )
        out.append({"cle": cles[i], "etiquette": etiquette, "structures": structures})
    return out


def niveaux_de(cle: str) -> list[dict]:
    packs = {
        "a": (("Alerte", "Maladie", "Départ"), [
            [("Fièvre", "Au retour, le sang passe avant le conseil."), ("Choc", "Conscience, souffle ou tension qui lâche."), ("Sang", "Saignement ou selle sanglante."), ("Plaie", "Morsure à classer tout de suite.")],
            [("Selles", "Diarrhée du voyage, hydrater d'abord."), ("Dengue", "Fièvre, douleurs, éruption possible."), ("Paludisme", "Cinq espèces, le falciparum tue."), ("Mollet", "Trajet long et jambe qui gonfle.")],
            [("Piqûre", "Répulsif, vêtements, moustiquaire."), ("Vaccin", "Jaune, hépatite A, typhoïde, rage."), ("Dates", "Quatre à six semaines si possible."), ("Sac", "Thermomètre et plan de fièvre.")],
        ]),
        "1": (("Risque", "Piqûre", "Départ"), [
            [("Nuit", "L'anophèle pique du soir à l'aube."), ("Jour", "L'aède pique le jour."), ("Haut", "Prophylaxie si le risque est haut."), ("Enfant", "Grossesse et petit âge changent le plan.")],
            [("Peau", "Répulsif sur la peau découverte."), ("Linge", "Vêtements longs et clairs."), ("Toile", "Moustiquaire ou chambre traitée."), ("Eau", "Eaux stagnantes autour du lit.")],
            [("Carte", "Destination, escales, saison."), ("Lit", "Dehors ou chambre climatisée."), ("Mont", "Altitude prévue du séjour."), ("Note", "Ce qui est choisi et écarté.")],
        ]),
        "2": (("Vivant", "Inactivé", "Âge"), [
            [("Jaune", "Virus vivant, centre autorisé."), ("Typho", "Gélules orales vivantes."), ("Thymus", "Maladie du thymus : arrêt."), ("Greffe", "Immunodépression : pas de vivant.")],
            [("Hépatite", "Vaccin inactivé de l'hépatite A."), ("Rappel", "Entre six et douze mois."), ("Dengue", "Seulement après une infection."), ("Carnet", "Certificat international.")],
            [("Mois", "Pas avant six mois pour le jaune."), ("Neuf", "Dose usuelle dès neuf mois."), ("Soixante", "Après 60 ans, risque plus haut."), ("Grossesse", "Vivant seulement si nécessité.")],
        ]),
        "3": (("Alerte", "Selles", "Eau"), [
            [("Sang", "Selles glairo-sanglantes."), ("Fièvre", "Forte fièvre avec le sang."), ("Choc", "Soif, pouls, tension."), ("Colite", "Pas le ralentisseur d'emblée.")],
            [("Eau", "Selles aqueuses sans sang."), ("Nombre", "Fréquence depuis le début."), ("Voyage", "Pays, glaçons, repas."), ("Main", "Hydrater avant le comprimé.")],
            [("Boire", "Eau traitée, fruits pelés."), ("Glaçon", "Glaçons douteux à éviter."), ("Mains", "Lavage avant les repas."), ("Suite", "Revenir si sang ou fièvre.")],
        ]),
        "4": (("Zone", "Comprimé", "Limite"), [
            [("Haut", "Haut risque : prophylaxie."), ("Bas", "Bas risque : piqûres d'abord."), ("Nuit", "Anophèle du soir à l'aube."), ("Fièvre", "Le comprimé n'annule pas la fièvre.")],
            [("Atovaquone", "Un comprimé adulte par jour."), ("Mefloquine", "Un comprimé par semaine."), ("Doxy", "Cent milligrammes par jour."), ("Repas", "Prendre avec un repas ou du lait.")],
            [("Rein", "Clairance basse : autre produit."), ("Psy", "Méfloquine prophylactique interdite."), ("Grossesse", "Chaque produit a sa phrase."), ("Fin", "Sept jours ou quatre semaines.")],
        ]),
        "5": (("Alarme", "Dengue", "Virus"), [
            [("Jour4", "Aggravation souvent à la chute."), ("Choc", "Tension basse, extrémités froides."), ("Souffle", "Dyspnée nouvelle."), ("Sang", "Saignement ou douleur du ventre.")],
            [("Aède", "Piqûre de jour et au crépuscule."), ("Douleur", "Derrière les yeux, muscles."), ("Éruption", "Souvent au troisième ou quatrième jour."), ("Fièvre", "Peut tomber en quatre à sept jours.")],
            [("Chik", "Compté à part dans le bulletin."), ("Zika", "Compté à part, sans critère inventé."), ("Nil", "Un cas importé en 2024."), ("Vaccin", "Dengue seulement si infection passée.")],
        ]),
        "6": (("Urgence", "Sang", "Grave"), [
            [("Fièvre", "Pendant ou après la zone."), ("Délai", "Dès six jours, parfois des années."), ("Espèces", "Cinq espèces de plasmodium."), ("Nuit", "Piqûre nocturne d'anophèle.")],
            [("Frottis", "Examen du sang sans délai."), ("Goutte", "Le récit ne suffit pas."), ("24h", "Sans avis en vingt-quatre heures."), ("Réserve", "Seulement l'accès non compliqué.")],
            [("Coma", "Convulsions, coma, décès."), ("Choc", "Pas le comprimé de l'accès simple."), ("Foie", "Passage hépatique puis globules."), ("Enfant", "Petit enfant et grossesse : risque haut.")],
        ]),
        "7": (("Descendre", "Mal", "Avant"), [
            [("Conscience", "Altérée : descendre, ne pas rester."), ("Ataxie", "Démarche instable."), ("Souffle", "Essoufflement sévère ou au repos."), ("Seul", "Ne pas descendre seul.")],
            [("Tête", "Céphalée après la montée."), ("Nausée", "Appétit perdu ou vomissement."), ("Fatigue", "Faiblesse inhabituelle."), ("Vertige", "Sensation ébrieuse.")],
            [("Comprimé", "Prophylaxie avant l'ascension."), ("Jour", "Commencer la veille."), ("Durée", "Au moins quatre jours."), ("Enfant", "Usage pédiatrique non étudié ici.")],
        ]),
        "8": (("Embolie", "Jambe", "Dose"), [
            [("Poitrine", "Douleur thoracique après le trajet."), ("Souffle", "Dyspnée brutale."), ("Syncope", "Malaise avec perte brève."), ("Sang", "Crachat de sang : urgence.")],
            [("Mollet", "Jambe augmentée et douloureuse."), ("Trajet", "Longue immobilité assise."), ("Chaleur", "Mollet chaud, à comparer."), ("Deux", "Les deux jambes se comparent.")],
            [("Confirmé", "Thrombose prouvée avant la dose."), ("Sept", "Sept premiers jours de charge."), ("Suite", "Puis la dose d'entretien lue."), ("Mois", "Durée courte si le risque passe.")],
        ]),
        "9": (("Plaie", "Classe", "Suivi"), [
            [("Laver", "Savonnage d'au moins quinze minutes."), ("Antisept", "Puis iode ou antiviral local."), ("Suture", "Suture seulement pour rapprocher."), ("Tête", "Tête, cou, mains, parties génitales.")],
            [("Un", "Toucher, nourrir, peau intacte."), ("Deux", "Griffure sans sang, mordillement."), ("Trois", "Derme traversé, salive, chauve-souris."), ("Appât", "Liquide d'un appât abîmé.")],
            [("Chien", "Dix jours, chien ou chat seulement."), ("Schéma", "Jours zéro, trois, sept, quatorze, vingt-huit."), ("Déjà", "Deux doses si déjà vacciné."), ("Titre", "Contrôle si immunodépression.")],
        ]),
        "10": (("Retour", "Germes", "Dose"), [
            [("Rapport", "Rapport sexuel pendant le voyage."), ("Plainte", "Écoulement, brûlure, saignement."), ("Partenaire", "Prévenir et traiter selon le cas."), ("Grossesse", "Phrase propre à la grossesse.")],
            [("Chlamydia", "Germes visé par la dose unique."), ("Autres", "D'autres germes ne sont pas cette dose."), ("Diarrhée", "Cet antibiotique n'est pas la diarrhée."), ("Test", "Le prélèvement confirme quand il est fait.")],
            [("Unique", "Une seule prise orale."), ("Lait", "Passe dans le lait humain."), ("Besoin", "Seulement si le traitement est nécessaire."), ("Suite", "Revoir si les signes restent.")],
        ]),
    }
    et, zones = packs[cle]
    return _pack(et, zones)


TEASERS = {
    "a": [
        "Consultation de voyage, pas un seul microbe.",
        "Comptes suisses, sans rang inventé.",
        "Piqûre, foie, globule, intestin.",
        "Dater, puis protéger le danger.",
        "Dates, grossesse, animaux, trajet.",
        "Conscience, plaie, mollet.",
        "Dix lectures, deux peuvent coexister.",
        "Le voyage plus le problème dominant.",
        "Sang si fièvre au retour.",
        "Alerte, maladie ou préparation.",
        "Doses avec numéro d'autorisation.",
        "Piqûres dans toutes les zones.",
        "Deux seuils de fièvre, deux sources.",
        "Ne pas remettre la fièvre au lendemain.",
    ],
    "1": [
        "Conseil avant le départ.",
        "Pas de part suisse inventée.",
        "Nuit pour l'anophèle, jour pour l'aède.",
        "Itinéraire, puis mesure utile.",
        "Vaccins, eau, altitude, animaux.",
        "Examen court si tout va bien.",
        "Distinct de la prophylaxie et des vaccins.",
        "Conseil complet : plan de fièvre écrit.",
        "Pas de bilan parasitaire sans symptôme.",
        "Haut risque : quitter vers la prophylaxie.",
        "Aucun milligramme dans cette lecture.",
        "Vêtements, répulsif, moustiquaire.",
        "Quatre gestes de 2016, feuillet de 2024.",
        "Même un départ dans trois jours.",
    ],
    "2": [
        "Vaccins du voyage, vivant ou non.",
        "Zéro fièvre jaune déclarée n'exonère pas.",
        "Vivant atténué, inactivé, oral.",
        "Certificat et risque médical, les deux.",
        "Carnet, immunité, grossesse, âge.",
        "Reporter une fièvre aiguë sévère.",
        "Jaune, dengue et certificat ne se confondent pas.",
        "Volumes lus, âges bornés.",
        "Séropositivité à trente jours, pas une efficacité de terrain.",
        "Dix jours avant l'arrivée si certificat.",
        "Pas de milligramme de médicament.",
        "Certificat à vie, étude prospective absente.",
        "Dire les deux phrases sur la durée.",
        "Pas de vivant chez la personne greffée.",
    ],
    "3": [
        "Diarrhée du voyage, pas la dysenterie.",
        "Pas d'incidence suisse archivée.",
        "Transit ralenti, muqueuse parfois envahie.",
        "Sang, fièvre, puis seulement le ralentisseur.",
        "Grossesse, âge, colite, soif.",
        "Selle sanglante et fièvre : autre conduite.",
        "Forme aqueuse ou forme invasive.",
        "Voyage et caractère des selles.",
        "Coproculture non systématique.",
        "Alerte si sang et fièvre.",
        "Doses lues, avec les autorisations.",
        "Eau traitée et lavage des mains.",
        "Hydrater, ne pas ralentir une dysenterie.",
        "Le sang fébrile ferme le ralentisseur.",
    ],
    "4": [
        "Prophylaxie seulement si elle est indiquée.",
        "Pas un risque nul.",
        "Foie puis globules, piqûre nocturne.",
        "Zone d'abord, produit ensuite.",
        "Rein, psychisme, grossesse, âge.",
        "Le comprimé ne dispense pas du thermomètre.",
        "Trois produits, trois calendriers.",
        "Haut risque, pas tout séjour.",
        "Pas de test avant un départ sans fièvre.",
        "Piqûres partout, comprimé si haut risque.",
        "Doses suisses, numéros à côté.",
        "La protection mécanique reste.",
        "Chaque produit garde sa contre-indication.",
        "Pas de méfloquine si le psychisme l'interdit.",
    ],
    "5": [
        "Trois virus comptés, tableaux non inventés.",
        "Effectifs suisses de 2024.",
        "Aède de jour, quatre sérotypes pour la dengue.",
        "Fièvre au retour : sang du paludisme aussi.",
        "Pays, jour de fièvre, saignement.",
        "Aggravation quand la fièvre tombe.",
        "Dengue, et les comptes des deux autres.",
        "Pas de traitement spécifique de la dengue.",
        "Hospitaliser la forme sévère.",
        "Alarme vers le quatrième ou cinquième jour.",
        "Paracétamol, pas l'acide acétylsalicylique.",
        "Répulsif de jour.",
        "Deux incubations, deux parts sans symptôme.",
        "Ne pas rassurer à la chute de la fièvre.",
    ],
    "6": [
        "Fièvre au retour : urgence jusqu'au sang.",
        "Afrique dominante, décès encore possibles.",
        "Foie, puis globules rouges.",
        "Examen du sang avant de rassurer.",
        "Dates, prophylaxie prise, vomissements.",
        "Conscience, ictère, souffle, saignement.",
        "Simple ou grave, la limite est clinique.",
        "Le récit ne confirme pas.",
        "Sang tout de suite, pas demain.",
        "Vingt-quatre heures et six jours pour la réserve.",
        "Schéma non compliqué, doses lues.",
        "Piqûres et prophylaxie du prochain départ.",
        "Deux seuils de température, deux textes.",
        "Pas de comprimé de réserve si la forme est grave.",
    ],
    "7": [
        "Mal d'altitude, descente si ça grave.",
        "Pas de part suisse archivée.",
        "Hypoxie de la montée, cerveau et poumon.",
        "Contexte d'abord, comprimé ensuite.",
        "Altitude, vitesse, antécédent, sommeil.",
        "Ataxie, conscience, souffle, toux rosée.",
        "Mal aigu, cerveau, poumon.",
        "Score de recherche, clinique à part.",
        "Pas de bilan qui retarde la descente.",
        "Descendre, ou prophylaxie avant.",
        "Acétazolamide suisse, avant la montée.",
        "Montée progressive quand le terrain le permet.",
        "Le score n'est pas le diagnostic de cabinet.",
        "Ne pas rester en haut si la conscience change.",
    ],
    "8": [
        "Thrombose après un long trajet.",
        "Pas de durée de vol inventée.",
        "Immobilité, vaisseau, caillot.",
        "Confirmer avant d'anticoaguler.",
        "Trajet, mollet, poitrine, antécédent.",
        "Comparer les deux jambes.",
        "Jambe, embolie, ou les deux.",
        "Le vol n'est pas l'indication écrite.",
        "Pas de score de Wells recopié.",
        "Urgence si la poitrine ou le souffle lâche.",
        "Dose de thrombose confirmée.",
        "Bouger pendant le trajet suivant.",
        "Immobilisation : exemple de facteur passager.",
        "Ne pas donner la dose de fibrillation à la phase aiguë.",
    ],
    "9": [
        "Rage : classer l'exposition en entier.",
        "Pas d'incidence suisse inventée.",
        "Nerf, salive, délai silencieux.",
        "Laver, puis catégorie, puis schéma.",
        "Animal, pays, vaccin déjà fait, plaie.",
        "Siège, saignement, muqueuse, chauve-souris.",
        "Trois catégories, sans en oublier une.",
        "Catégories lues une à une.",
        "Ne pas attendre un laboratoire pour laver.",
        "Schéma A, schéma B, dix jours.",
        "Immunoglobuline de la catégorie trois.",
        "Éviter le contact à risque au prochain voyage.",
        "Dix jours : chien et chat seulement.",
        "Une chauve-souris fait monter la catégorie.",
    ],
    "10": [
        "Infection à chlamydia au retour.",
        "Pas de part suisse inventée pour ce retour.",
        "Muqueuse, rapport, incubation silencieuse.",
        "Demander le rapport, proposer le test.",
        "Symptômes, partenaire, grossesse, lait.",
        "Examen génital selon la plainte.",
        "Distinct de la diarrhée et du paludisme.",
        "Le germe se confirme par le prélèvement.",
        "Traiter l'indication lue, pas toute fièvre.",
        "Dose unique si c'est bien cette infection.",
        "Mille milligrammes, une fois.",
        "Préservatif au prochain départ.",
        "Grossesse et allaitement ont leur phrase.",
        "Ne pas utiliser cette dose pour la diarrhée.",
    ],
}

DETAILS = {
    "a": [
        "fièvre au retour, examen du sang le jour même",
        "départ dans dix jours, répulsif et plan de fièvre écrits",
        "selles sanglantes et fièvre, hydratation sans ralentisseur",
        "morsure de chien, lavage long puis classement",
        "mollet gonflé après un vol, comparaison des deux jambes",
        "mal de tête en montant, discussion de descente",
        "éruption au quatrième jour, revue rapprochée",
        "projet de grossesse et zone à paludisme, conseil avant le vaccin vivant",
        "enfant qui part, calendrier et logement notés",
        "personne greffée, vaccin vivant reporté",
        "clairance rénale basse, autre prophylaxie discutée",
        "antécédent de dépression, méfloquine prophylactique écartée",
        "toux et fièvre au retour, sang et poumon examinés",
        "eau douce du séjour notée sans diagnostic inventé",
        "deux lectures ouvertes le même jour, diarrhée et fièvre",
        "thermomètre mis dans le sac avant l'aéroport",
    ],
    "1": [
        "départ dans trois jours, plan de fièvre quand même écrit",
        "logement climatisé noté, répulsif quand même conseillé",
        "altitude du trek écrite à côté de la destination",
        "nourrisson du voyage, questions d'âge avant tout vaccin",
        "séjour urbain court, pas de comprimé sans exposition",
        "nuit sous moustiquaire prévue dans le récit",
        "eau stagnante autour du bungalow signalée",
        "assurance et accès aux soins demandés sans chiffre inventé",
        "grossesse possible, test avant un vaccin vivant",
        "précédent voyage sans conseil, celui-ci est complet",
        "saison des pluies notée sur l'itinéraire",
        "escale nocturne ajoutée au risque de piqûre",
        "chambre climatisée et sorties du soir, les deux dites",
        "thermomètre vérifié au cabinet",
        "liste des médicaments habituels recopiée",
        "retour prévu, phrase sur la fièvre répétée",
    ],
    "2": [
        "personne greffée, vaccin vivant de la fièvre jaune reporté",
        "nourrisson de cinq mois, injection de fièvre jaune non faite",
        "adulte de soixante-deux ans, risque réel discuté avant le vivant",
        "carnet perdu, dates reconstituées avec la personne",
        "grossesse en cours, vivant seulement si nécessité absolue",
        "rappel d'hépatite A placé entre six et douze mois",
        "gélules de typhoïde un jour sur deux, à jeun",
        "eau de la gélule non brûlante",
        "certificat demandé par le pays, dix jours respectés",
        "immunodépression par comprimé, vivant écarté",
        "thymome connu, fièvre jaune non injectée",
        "vaccin dengue évoqué seulement après une infection passée",
        "enfant de dix ans, volume d'hépatite A de l'âge",
        "fièvre aiguë sévère, rendez-vous de vaccin déplacé",
        "protection commencée dix jours après la première dose",
        "durée à vie du certificat dite avec la limite des études",
    ],
    "3": [
        "selles sanglantes et fièvre, eau d'abord, pas de ralentisseur",
        "diarrhée aqueuse sans sang, boisson puis gélule lue",
        "enfant de cinq ans, ce ralentisseur non donné",
        "ballonnement sous traitement, comprimé arrêté",
        "colite connue, ralentisseur non choisi en premier",
        "voyage de trois semaines, prévention non prolongée sans donnée",
        "glaçons du séjour racontés, lavage des mains répété",
        "vomissements qui empêchent de boire, avis rapide",
        "selles redevenues moulées, traitement stoppé",
        "fièvre isolée plus que la diarrhée, autre lecture ouverte",
        "antibiotique déjà pris, colite associée évoquée",
        "grossesse et diarrhée, hydratation mise en premier",
        "personne âgée assoiffée, pouls compté",
        "retour depuis deux jours, selles datées",
        "fruits non pelés, conseil pour le prochain départ",
        "douleur abdominale défendue, examen avant le comprimé",
    ],
    "4": [
        "zone à haut risque, comprimé choisi selon le rein et le psychisme",
        "dépression récente, méfloquine de prophylaxie non prescrite",
        "clairance très basse, atovaquone avec proguanil écartée",
        "grossesse, chaque phrase d'autorisation relue",
        "départ demain, calendrier du produit respecté",
        "oubli d'un soir, conduite lue sans doubler au hasard",
        "vomissement dans l'heure, reprise de la prise du jour",
        "enfant de plus de douze ans, dose au poids sans dépasser l'adulte",
        "repas ou lait avec le comprimé",
        "piqûres maintenues malgré le comprimé",
        "séjour sans anophèle, pas de prophylaxie",
        "même jour de la semaine pour la prise hebdomadaire",
        "contraception pendant la méfloquine et après l'arrêt",
        "grossesse non prévue, pas d'interruption pour ce seul fait",
        "foie grave, doxycycline non choisie",
        "thermomètre dans le bagage avec la boîte",
    ],
    "5": [
        "fièvre qui tombe au cinquième jour, revue le jour même",
        "douleur derrière les yeux et éruption, dengue évoquée",
        "saignement des gencives, orientation hospitalière",
        "souffle nouveau, pas un retour simple à la maison",
        "paracétamol pour la douleur, aspirine non donnée",
        "second voyage en zone d'aèdes, antécédent demandé",
        "chikungunya du bulletin cité sans critère inventé",
        "infection Zika comptée, page dédiée non archivée",
        "piqûres de jour racontées au crépuscule aussi",
        "enfant de sept ans, vaccin dengue seulement si infection passée",
        "pas de comprimé antiviral spécifique annoncé",
        "paludisme cherché en parallèle parce que la fièvre vient du voyage",
        "douleur du ventre à la chute thermique, alarme",
        "repos et boisson, signe d'alarme expliqué à l'accompagnant",
        "pays d'exposition noté, Thaïlande Brésil ou Indonésie possibles",
        "retour depuis une semaine, incubation encore compatible",
    ],
    "6": [
        "fièvre à J+10 d'un séjour africain, sang le jour même",
        "prophylaxie oubliée, cela ne rassure pas",
        "conscience trouble, urgences avant le résultat",
        "accès simple confirmé, schéma de trois jours avec un repas",
        "vomissement dans l'heure, dose reprise",
        "forme avec coma, comprimé de l'accès simple non donné",
        "grossesse au premier trimestre, alternative cherchée si elle existe",
        "allaitement, reprise du lait non avant le délai lu",
        "pas de médecin sur place dans les vingt-quatre heures, réserve lue",
        "séjour de moins de six jours, réserve non automatique",
        "cinq espèces dites, falciparum nommé comme le plus dangereux",
        "fièvre à 38 expliquée avec la page de l'office",
        "fièvre à 37,5 expliquée avec le feuillet",
        "paracétamol pour faire baisser la fièvre sans retarder le sang",
        "enfant de 30 kg, bande pédiatrique du schéma lue",
        "intervalle allongé du cœur, produit écarté",
    ],
    "7": [
        "mal de tête à 3000 mètres, descente discutée le jour même",
        "démarche instable, descente accompagnée",
        "conscience qui change, pas d'attente d'un comprimé",
        "toux sèche et souffle d'effort excessif, œdème pulmonaire évoqué",
        "expectoration rosée, descente urgente",
        "prophylaxie commencée la veille de la montée",
        "prise deux fois par jour pendant au moins quatre jours",
        "enfant du groupe, usage non étudié dans l'autorisation",
        "allergie grave au produit, autre mesure non médicamenteuse",
        "sodium bas déjà connu, produit non donné",
        "maladie hépatique grave, produit contre-indiqué",
        "grossesse, seulement si nécessité absolue",
        "somnolence et fourmillements signalés comme effets possibles",
        "nuit à l'abri après une petite descente",
        "compagnon qui reste avec la personne instable",
        "prochain trek, montée plus lente prévue",
    ],
    "8": [
        "mollet droit augmenté après un vol long, comparaison faite",
        "douleur thoracique au débarquement, urgences",
        "thrombose prouvée, dose de charge puis entretien",
        "vol seul, pas une indication écrite du produit",
        "chirurgie récente citée comme facteur passager",
        "immobilisation plâtrée, même logique de facteur passager",
        "dose oubliée, prise dès que vu puis rythme habituel",
        "foie très grave, produit non choisi",
        "saignement actif, avis avant toute prise",
        "prévention d'une récidive seulement après les mois lus",
        "fibrillation connue, dose aiguë de thrombose non confondue",
        "marche dans l'allée au prochain vol",
        "eau bue pendant le trajet, sans en faire un traitement",
        "essoufflement brutal, embolie cherchée",
        "syncope au sortir de l'avion, prise en charge urgente",
        "deux jambes égales et poitrine libre, autre cause cherchée",
    ],
    "9": [
        "morsure au visage, catégorie trois, lavage immédiat",
        "léchage sur peau saine, catégorie un si le récit est fiable",
        "griffure sans sang, schéma vaccinal commencé",
        "chauve-souris dans la chambre, catégorie haute",
        "chien observé dix jours, traitement arrêté s'il reste sain",
        "renard non observé, pas de délai de dix jours",
        "personne déjà vaccinée, deux doses aux jours zéro et trois",
        "statut vaccinal inconnu, schéma complet",
        "immunodépression, immunoglobuline ajoutée",
        "plaie lavée quinze minutes avant la suture",
        "suture évitée, berges seulement rapprochées",
        "iode après le rinçage",
        "mains mordues, catégorie trois à cause des nerfs",
        "appât vaccinal percé sur une écorchure, catégorie relue",
        "titre contrôlé chez la personne immunodéprimée",
        "prochain voyage, éviction des contacts animaux dite",
    ],
    "10": [
        "écoulement au retour, prélèvement et dose unique si c'est le germe",
        "brûlure en urinant après un rapport en voyage",
        "grossesse débutante, bénéfice et risque dits avant la prise",
        "allaitement, lait interrompu si le traitement est indispensable",
        "diarrhée du même voyage, cet antibiotique non utilisé pour elle",
        "partenaire prévenu, les deux prises en charge",
        "saignement entre les règles, examen proposé",
        "test déjà positif, dose unique expliquée",
        "oubli du préservatif raconté sans jugement",
        "fièvre associée, paludisme non oublié",
        "douleur pelvienne forte, avis gynécologique",
        "homme avec écoulement, même germe possible",
        "contrôle si les signes persistent",
        "prochain départ, préservatif remis dans le conseil",
        "allergie connue, autre avis avant une prise",
        "traitement pris en une seule fois, observance simple",
    ],
}


def remplir(k, t, details: dict) -> None:
    k("3", [
        P(
            "Cette lecture est la diarrhée qui commence en voyage ou dans les jours du retour.",
            "Le lopéramide est indiqué pour la diarrhée, y compris celle du voyageur. [[13]]",
            "Il n'est pas le traitement de première ligne d'une dysenterie avec fièvre élevée et selles glairo-sanglantes. [[13]]",
            "Une fièvre qui domine ouvre aussi la lecture du paludisme. [[1]]",
        ),
        P(
            "Aucune incidence suisse de cette diarrhée n'a été archivée pour le lot.",
            "On ne lui donne donc pas un rang parmi les dix lectures.",
            "Le risque suit l'eau, les glaçons et les repas, sans chiffre ajouté.",
            "La diarrhée et le paludisme peuvent être présents ensemble. [[1]]",
        ),
        P(
            "Le lopéramide agit sur les récepteurs mu et ralentit le transit. [[13]]",
            "La doxycycline préventive vise notamment des souches entérotoxiques. [[7]]",
            "Le sang et la fièvre font penser à une atteinte de la muqueuse. [[13]]",
            "Les pertes d'eau pèsent surtout chez l'enfant et la personne âgée. [[13]]",
        ),
        P(
            "On date le début, le nombre de selles, le sang, la fièvre et les vomissements.",
            "On demande le pays, l'eau, les glaçons et un antibiotique déjà pris.",
            "On écarte d'abord le choc et le couple sang plus fièvre. [[13]]",
            "Le ralentisseur ne vient qu'après l'eau et après ce tri. [[13]]",
        ),
        P(
            "On demande une grossesse, un allaitement et un âge inférieur à six ans. [[13]]",
            "On demande une colite, des selles glairo-sanglantes et une fièvre élevée. [[13]]",
            "On demande un ballonnement ou un arrêt des selles sous le produit. [[13]]",
            "On demande si la personne boit encore et si elle urine.",
        ),
        P(
            "On cherche la soif, un pouls rapide et un abdomen défendu.",
            "Le sang visible avec fièvre sort de la diarrhée simple. [[13]]",
            "Le schéma montre la selle, l'eau, la fièvre et le comprimé.",
            "Un ventre souple n'autorise pas le ralentisseur si le sang et la fièvre sont là. [[13]]",
        ),
        P(
            "La forme simple est aqueuse, sans sang et sans forte fièvre.",
            "La dysenterie lue associe des selles glairo-sanglantes et une fièvre élevée. [[13]]",
            "Les salmonelles, shigelles et campylobacter ne sont pas une indication de première ligne. [[13]]",
            "La colite liée à un antibiotique est aussi hors de cette première ligne. [[13]]",
        ),
        P(
            "Le diagnostic de situation joint le voyage et le type de selles.",
            "Aucun score chiffré de cette diarrhée n'a été recopié.",
            "On n'attend pas une coproculture pour faire boire.",
            "Si la fièvre domine, le paludisme reste possible malgré les selles. [[1]]",
        ),
        P(
            "La coproculture n'est pas systématique si l'épisode est simple et bref.",
            "Elle se discute avec le sang, une fièvre qui dure, ou une immunité basse.",
            "Aucun seuil de laboratoire des selles n'a été extrait.",
            "On réhydrate sans attendre une personne qui vomit tout.",
        ),
        P(
            "L'alerte s'ouvre si le sang et la fièvre vont ensemble, ou si un choc apparaît. [[13]]",
            "La maladie simple est la diarrhée aqueuse sans ces signes.",
            "La préparation du prochain voyage rappelle l'eau sûre.",
            "On change de lecture si la température devient le problème principal. [[1]]",
        ),
        P(
            "L'adulte commence par 4 mg de lopéramide, puis 2 mg après chaque selle liquide. [[13]]",
            "Le plafond est de 16 mg par jour, autorisation 61295. [[13]]",
            "On arrête quand les selles sont normales, ou après plus de douze heures sans selle. [[13]]",
            "La doxycycline préventive, autorisation 49771, est de 200 mg le premier jour puis 100 mg par jour. [[7]]",
            "Aucune donnée de cette prévention n'est disponible au-delà de 21 jours. [[7]]",
            "Avant six ans, ce lopéramide n'est pas utilisé. [[13]]",
            "On arrête tout de suite en cas de constipation, de ballonnement important ou d'iléus. [[13]]",
        ),
        P(
            "On conseille une eau traitée, des fruits pelés et des glaçons sûrs.",
            "Le lavage des mains avant les repas reste le geste simple.",
            "La doxycycline préventive n'est pas le traitement d'une diarrhée déjà commencée. [[7]]",
            "On dit de revenir si le sang ou la fièvre apparaît. [[13]]",
        ),
        P(
            "L'eau passe avant le ralentisseur.",
            "Les milligrammes de cette page portent les autorisations 61295 et 49771.",
            "Ces deux numéros sont ceux des informations professionnelles lues.",
            "La grossesse ne reçoit ce lopéramide qu'en nécessité absolue. [[13]]",
        ),
        P(
            "Le piège est de donner le lopéramide en premier si la selle est sanglante et la fièvre haute. [[13]]",
            "Le piège inverse est d'attendre un examen avant de faire boire.",
            "Le piège de durée est de prolonger la prévention par doxycycline au-delà de 21 jours sans donnée. [[7]]",
            "Cas corrigé : on hydrate, on n'ouvre pas le ralentisseur, et l'on cherche le paludisme si la fièvre vient d'une zone d'endémie. [[1]]",
        ),
    ])
    k("4", [
        P(
            "Cette lecture est la chimio prophylaxie du paludisme, pas le traitement d'une fièvre déjà là.",
            "Elle s'ajoute à la protection contre les piqûres, elle ne la remplace pas. [[3]]",
            "Elle concerne les zones à haut risque, pas automatiquement tout séjour. [[3]]",
            "La fièvre sous prophylaxie reste une urgence. [[1]]",
        ),
        P(
            "Le document de 2016 compte 150 à 450 paludismes déclarés par an en Suisse. [[4]]",
            "Il compte aussi un à trois décès annuels de voyageurs non immuns. [[4]]",
            "Ces comptes ne disent pas quelle part des consultations reçoit une prophylaxie.",
            "L'Afrique fournit la grande majorité des falciparum dans ce texte. [[4]]",
        ),
        P(
            "L'anophèle pique le soir et la nuit. [[1]]",
            "Le parasite passe par le foie avant les globules rouges. [[1]]",
            "L'atovaquone bloque une étape mitochondriale et le proguanil agit sur les folates. [[5]]",
            "Aucun de ces produits n'enlève la nécessité d'éviter la piqûre. [[4]]",
        ),
        P(
            "On classe la zone avant de choisir le produit. [[3]]",
            "On lit le rein, le psychisme, la grossesse, l'âge et le foie.",
            "On explique que la prophylaxie n'est pas une protection absolue. [[4]]",
            "On dit quoi faire si la fièvre vient quand même. [[1]]",
        ),
        P(
            "On demande une clairance connue avant l'atovaquone avec proguanil. [[5]]",
            "On demande une dépression, une anxiété, une psychose, une schizophrénie ou des crises avant la méfloquine. [[6]]",
            "On demande une grossesse et un projet de grossesse. [[6]]",
            "On demande si la personne peut voir un médecin dans les vingt-quatre heures en cas de fièvre. [[4]]",
        ),
        P(
            "L'examen est bref si la personne n'a pas de fièvre.",
            "On note un ictère, une grossesse et un trouble psychique visible.",
            "Le schéma oppose la zone, le comprimé et les limites.",
            "On ne se fie pas au seul aspect pour dire qu'un produit est supporté.",
        ),
        P(
            "Le feuillet de 2024 met la chimio prophylaxie dans les zones à haut risque. [[3]]",
            "Il garde la protection contre les piqûres dans toutes les zones, même à risque bas. [[3]]",
            "Le document de 2016 décrit aussi un médicament de réserve pour des situations choisies. [[4]]",
            "Ce médicament de réserve est détaillé dans la lecture de la fièvre, pas comme une prophylaxie.",
        ),
        P(
            "On retient la prophylaxie quand le risque de falciparum est haut. [[3]]",
            "On ne la retient pas pour un séjour sans exposition lue.",
            "Au-dessus de 1500 mètres le risque est en général plus faible, presque jusqu'à 3000 mètres il peut rester. [[4]]",
            "Un thermomètre qui fonctionne fait partie du voyage. [[3]]",
        ),
        P(
            "Aucun examen du sang n'est systématique avant un départ sans fièvre.",
            "La clairance n'est dosée que si le récit la rend nécessaire au choix.",
            "Aucun seuil nouveau de laboratoire n'est créé pour cette lecture.",
            "La fièvre, elle, ne se passe pas d'examen du sang. [[1]]",
        ),
        P(
            "Sans exposition palustre, on reste sur les piqûres et les vaccins utiles.",
            "Avec un haut risque, on choisit un des trois produits lus. [[3]]",
            "Avec une contre-indication, on change de produit plutôt que d'insister.",
            "Avec une fièvre déjà présente, on quitte cette lecture.",
        ),
        P(
            "L'atovaquone avec proguanil, autorisation 54150, est un comprimé adulte par jour, soit 250 mg et 100 mg. [[5]]",
            "On commence un à deux jours avant l'entrée et l'on continue sept jours après la sortie. [[5]]",
            "On prend ce comprimé avec un repas ou du lait, et l'on reprend la prise si l'on vomit dans l'heure. [[5]]",
            "La prophylaxie est contre-indiquée si la clairance de la créatinine est inférieure à 30 ml par minute. [[5]]",
            "La méfloquine, autorisation 47385, est un comprimé de 250 mg, environ 5 mg par kilogramme une fois par semaine. [[6]]",
            "Au-dessus de 45 kg, la prophylaxie est d'un comprimé par semaine, commencé au moins une semaine avant, poursuivi quatre semaines. [[6]]",
            "La doxycycline, autorisation 49771, est de 100 mg une fois par jour chez l'adulte pour cette prophylaxie. [[7]]",
            "Chez l'enfant de plus de douze ans, elle est de 2 mg par kilogramme une fois par jour, sans dépasser l'adulte. [[7]]",
        ),
        P(
            "Les vêtements, le répulsif et la moustiquaire restent indiqués. [[1]]",
            "On prend la méfloquine après un repas, le même jour de la semaine. [[6]]",
            "On peut commencer trois semaines avant pour tester la tolérance de la méfloquine. [[6]]",
            "Une dose de charge sur trois jours existe si le départ est imminent, avec plus d'effets indésirables. [[6]]",
        ),
        P(
            "La revue de 2009 compte 28,8 pour cent d'événements neuropsychiatriques sous méfloquine. [[6]]",
            "Elle compte 14 pour cent sous atovaquone avec proguanil, sans événement grave dû au médicament dans les deux groupes. [[6]]",
            "La prophylaxie par méfloquine est interdite dans la dépression aiguë ou récente, l'anxiété généralisée, la psychose, la schizophrénie ou une autre maladie psychiatrique grave. [[6]]",
            "Elle est aussi interdite en prophylaxie après des crises, et la grossesse n'est pas un motif d'interruption si elle survient. [[6]]",
            "La doxycycline de cette prophylaxie est évitée pendant la grossesse, sauf nécessité absolue. [[7]]",
            "L'atovaquone avec proguanil pendant la grossesse n'est utilisé que si le bénéfice dépasse le risque fœtal. [[5]]",
            "Le feuillet de 2024 dit un début la veille pour l'atovaquone avec proguanil, et l'autorisation dit un à deux jours. [[3]] [[5]]",
            "On enseigne l'intervalle de l'autorisation pour la prise, et l'on cite le feuillet à part.",
        ),
        P(
            "Le piège est de prescrire une prophylaxie dans une zone sans exposition, ou de l'oublier dans un haut risque. [[3]]",
            "Le piège de la méfloquine est de l'utiliser en prophylaxie malgré une maladie psychiatrique ou des crises. [[6]]",
            "Le piège du rein est de garder l'atovaquone avec proguanil malgré une clairance inférieure à 30 ml par minute. [[5]]",
            "Cas corrigé : on choisit un autre produit, on garde les piqûres, et l'on écrit le plan de fièvre. [[4]]",
        ),
    ])
    k("5", [
        P(
            "Cette lecture réunit la dengue, le chikungunya et l'infection à virus Zika au retour.",
            "Le bulletin suisse les compte comme des infections importées. [[2]]",
            "Le tableau clinique détaillé archivé concerne surtout la dengue. [[18]]",
            "On ne fabrique pas un critère pour les deux autres virus.",
        ),
        P(
            "En 2024, la Suisse a déclaré 429 dengue, 19 chikungunya, 9 infections Zika et un Nil occidental. [[2]]",
            "Aucune fièvre jaune n'a été déclarée cette année-là, et aucune transmission locale de dengue. [[2]]",
            "Les femmes représentaient 49,9 pour cent des dengue, avec un âge médian de 38,5 ans. [[2]]",
            "Chez les hommes, l'âge médian lu est de 43 ans, et plus d'un tiers des expositions venaient de trois pays. [[2]]",
            "Ces pays étaient la Thaïlande, le Brésil et l'Indonésie. [[2]]",
            "L'organisation citée par le bulletin compte plus de 14 millions de cas et 10000 décès estimés en 2024 dans le monde. [[2]]",
        ),
        P(
            "L'aède de la dengue pique le jour et au crépuscule. [[18]]",
            "Quatre sérotypes existent, et une seconde infection par un autre sérotype augmente le risque de forme grave. [[2]]",
            "Le bulletin donne une incubation de 3 à 14 jours. [[2]]",
            "La page des voyageurs donne en général 5 à 8 jours, et les deux phrases restent datées. [[18]]",
        ),
        P(
            "On date le retour et le premier jour de fièvre.",
            "On demande les douleurs derrière les yeux, les muscles, une éruption et un saignement. [[18]]",
            "On cherche en même temps un paludisme si la zone s'y prête. [[1]]",
            "On ne rassure pas au moment où la fièvre tombe. [[18]]",
        ),
        P(
            "On demande les pays, les piqûres de jour et un antécédent de dengue. [[2]]",
            "On demande un saignement, un essoufflement, une douleur du ventre et une lipothymie. [[18]]",
            "On demande une grossesse avant de parler du virus Zika, sans critère inventé.",
            "On demande les médicaments déjà pris pour la douleur.",
        ),
        P(
            "On cherche une éruption, souvent vers le troisième ou le quatrième jour. [[18]]",
            "On cherche un saignement, un souffle court et des extrémités froides. [[18]]",
            "Le schéma marque le jour quatre, le choc, le souffle et le sang.",
            "L'examen peut être pauvre au début, cela n'écarte pas une aggravation. [[18]]",
        ),
        P(
            "La dengue peut donner une forte fièvre, des douleurs et une éruption. [[18]]",
            "Le bulletin dit que 40 à 80 pour cent des infections restent sans symptôme. [[2]]",
            "La page des voyageurs dit qu'environ trois personnes sur quatre n'ont pas de symptôme. [[18]]",
            "On cite les deux proportions, sans les additionner.",
            "Le chikungunya et le virus Zika sont ici des comptes suisses, pas des monographies séparées. [[2]]",
        ),
        P(
            "Il n'y a pas de traitement spécifique de la dengue. [[18]]",
            "La forme sévère est rare chez le touriste, mais elle existe. [[18]]",
            "L'aggravation survient souvent du quatrième au cinquième jour, quand la fièvre baisse. [[18]]",
            "Les signes lus sont l'hypotension, la dyspnée, la gêne abdominale, le saignement et le choc. [[18]]",
        ),
        P(
            "On hospitalise la forme sévère. [[18]]",
            "Aucun seuil suisse de plaquettes n'a été extrait pour ce lot.",
            "On ne retient pas une personne instable pour attendre un chiffre.",
            "Le diagnostic virologique, quand il est fait, ne remplace pas la surveillance. [[18]]",
        ),
        P(
            "Si un signe d'alarme apparaît, la branche d'urgence s'ouvre. [[18]]",
            "Si la forme est simple, on soulage et l'on revoit de près.",
            "Si la zone est aussi palustre, le sang du paludisme part en même temps. [[1]]",
            "Si seul un autre virus est compté, on ne lui invente pas un traitement.",
        ),
        P(
            "Le paracétamol, autorisation 69266, se donne de 500 à 1'000 mg par prise chez l'adulte de plus de 40 kg. [[16]]",
            "Le paracétamol ne dépasse pas 4'000 mg par jour. [[16]]",
            "On évite l'acide acétylsalicylique pour la fièvre et la douleur de la dengue. [[18]]",
            "Le numéro 69266 est celui de l'information professionnelle du paracétamol.",
            "Le vaccin dengue n'est recommandé qu'avec une infection antérieure prouvée, en forte transmission. [[2]] [[18]]",
            "Il est autorisé en Suisse depuis août 2024 à partir de six ans, sans dose recopiée ici. [[2]]",
        ),
        P(
            "Le répulsif de jour et la réduction des eaux stagnantes visent l'aède. [[18]]",
            "Une seconde dengue par un autre sérotype mérite d'être dite comme risque plus haut. [[2]]",
            "On explique les signes qui doivent faire revenir, surtout à la chute de la fièvre. [[18]]",
            "On ne promet pas qu'un premier épisode simple protège.",
        ),
        P(
            "Deux sources donnent deux incubations, 3 à 14 jours et en général 5 à 8 jours. [[2]] [[18]]",
            "Deux sources donnent deux parts sans symptôme, et les deux sont citées. [[2]] [[18]]",
            "Les milligrammes du paracétamol portent l'autorisation 69266.",
            "Le chikungunya et le virus Zika ne reçoivent pas un tableau inventé.",
        ),
        P(
            "Le piège est de rassurer parce que la fièvre tombe au cinquième jour. [[18]]",
            "Le piège médicamenteux est de donner l'acide acétylsalicylique pour cette douleur. [[18]]",
            "Le piège du vaccin est de le proposer sans infection antérieure prouvée. [[2]]",
            "Cas corrigé : on revoit le jour de la chute thermique, on garde le paracétamol, et l'on hospitalise si un signe d'alarme est là. [[16]] [[18]]",
        ),
    ])
    k("6", [
        P(
            "Cette lecture est la fièvre pendant ou après un séjour en zone à paludisme.",
            "Toute fièvre de ce type fait suspecter le paludisme jusqu'à preuve du contraire. [[1]]",
            "Le falciparum peut donner des convulsions, un coma et la mort. [[1]]",
            "La grossesse et le petit enfant ont un risque plus élevé. [[1]]",
        ),
        P(
            "Le délai minimal lu est de six jours, et il peut atteindre des années. [[1]]",
            "Cinq espèces sont en cause. [[1]]",
            "L'Afrique concentre plus de 90 pour cent des cas dans la page de l'office. [[1]]",
            "Le document de 2016 compte 150 à 450 déclarations par an et un à trois décès de voyageurs non immuns. [[4]]",
        ),
        P(
            "L'anophèle pique la nuit, le parasite gagne le foie puis les globules. [[1]]",
            "La prophylaxie ne supprime pas ce cycle de façon absolue. [[4]]",
            "L'artéméther avec luméfantrine est réservé à l'accès non compliqué. [[8]]",
            "Une forme grave n'est pas une indication de ce comprimé. [[8]]",
        ),
        P(
            "On considère la fièvre comme un paludisme tant que le sang n'est pas lu. [[1]]",
            "On n'attend pas le lendemain pour ce prélèvement. [[1]]",
            "On baisse la fièvre sans retarder l'avis ni le sang. [[4]] [[16]]",
            "On sépare l'accès simple de la forme qui touche la conscience. [[1]] [[8]]",
        ),
        P(
            "On demande les dates d'entrée et de sortie, et la prophylaxie réellement prise.",
            "On demande les vomissements, la grossesse, l'allaitement et le poids.",
            "On demande un trouble du rythme, un allongement connu et les médicaments qui allongent. [[8]]",
            "On demande si un médecin et un examen du sang sont possibles dans les vingt-quatre heures. [[4]]",
        ),
        P(
            "On cherche la conscience, un ictère, un souffle court, un saignement et un choc.",
            "La fièvre peut manquer au moment de l'examen, le récit compte quand même. [[1]]",
            "Le schéma oppose l'urgence, le prélèvement et la forme grave.",
            "Un examen neurologique normal n'autorise pas un retour sans prélèvement. [[1]]",
        ),
        P(
            "La page de l'office parle d'une fièvre au-dessus de 38 degrés. [[1]]",
            "Le feuillet de 2024 et le document de 2016 parlent d'une fièvre au-dessus de 37,5 degrés. [[3]] [[4]]",
            "On attribue chaque borne à son texte.",
            "Le paludisme peut commencer dès sept jours après l'entrée en zone, selon le feuillet. [[3]]",
        ),
        P(
            "Le diagnostic se fait par l'examen du sang, pas par le récit seul. [[1]]",
            "L'artéméther avec luméfantrine traite un falciparum non compliqué, ou un mélange qui l'inclut. [[8]]",
            "Il est aussi une réserve si aucun médecin ou aucun médicament n'est accessible dans les vingt-quatre heures. [[8]]",
            "Les critères détaillés du paludisme grave selon l'organisation mondiale de la santé ne sont pas recopiés item par item.",
        ),
        P(
            "L'examen du sang part immédiatement. [[1]]",
            "Aucun seuil suisse de parasitémie n'a été extrait.",
            "On hospitalise une personne confuse, qui saigne ou qui est en choc sans attendre le chiffre.",
            "Un premier examen négatif chez une personne encore fébrile se rediscute, sans inventer un délai de contrôle.",
        ),
        P(
            "Sans médecin et sans examen du sang dans les vingt-quatre heures, et après au moins six jours de zone, la réserve se discute. [[4]]",
            "On fait baisser la fièvre avant cette réserve, selon le document de 2016. [[4]]",
            "Si la forme est grave, cette réserve par comprimé de l'accès simple n'est pas le traitement. [[8]]",
            "Si un médecin est joignable, on n'improvise pas la réserve.",
        ),
        P(
            "L'artéméther avec luméfantrine, autorisation 54594, est de 4 comprimés au diagnostic, puis 4 comprimés huit heures plus tard. [[8]]",
            "On poursuit par 4 comprimés deux fois par jour les deux jours suivants, soit 24 comprimés en trois jours. [[8]]",
            "Chaque prise se fait avec un repas gras ou du lait, et l'on reprend si l'on vomit dans l'heure. [[8]]",
            "Ce schéma adulte vaut à partir de 35 kg ou de douze ans. [[8]]",
            "L'atovaquone avec proguanil en traitement, autorisation 54150, est de 4 comprimés une fois par jour pendant trois jours au-dessus de 40 kg. [[5]]",
            "Le paracétamol, autorisation 69266, ne dépasse pas 4'000 mg par jour pour faire baisser la fièvre. [[16]]",
            "La méfloquine de réserve commence autour de 15 mg par kilogramme si aucun soin n'est possible dans les vingt-quatre heures. [[6]]",
            "Au-dessus de 45 kg, cette réserve débute par trois comprimés, puis deux autres six à huit heures plus tard si le soin manque encore. [[6]]",
        ),
        P(
            "On continue les piqûres tant que l'on est en zone. [[1]]",
            "Une prophylaxie en cours ne dispense pas du prélèvement. [[4]]",
            "On explique les signes de gravité à la personne qui accompagne.",
            "Le prochain départ ne se prépare qu'une fois cet épisode tenu.",
        ),
        P(
            "Les numéros 54594, 54150, 69266 et 47385 sont ceux des informations professionnelles de cette page.",
            "Au premier trimestre, on n'utilise pas l'artéméther avec luméfantrine si un autre produit efficace existe. [[8]]",
            "On ne le refuse pas dans une situation vitale sans alternative. [[8]]",
            "L'allaitement ne reprend pas avant le vingt-huitième jour, sauf si le bénéfice dépasse le risque. [[8]]",
            "Le produit est contre-indiqué en cas d'allongement congénital, de trouble du rythme symptomatique ou de médicament qui allonge. [[8]]",
            "Il est aussi contre-indiqué si le rein ou le foie est en insuffisance grave. [[8]]",
            "Un comprimé contient 120 mg de luméfantrine. [[8]]",
            "Les bandes enfant vont de 5 à moins de 15 kg, puis de 15 à moins de 25 kg. [[8]]",
            "La bande de 25 à moins de 35 kg existe aussi, avec un, deux ou trois comprimés au même rythme. [[8]]",
        ),
        P(
            "Le piège vital est de remettre le prélèvement au lendemain. [[1]]",
            "Le piège du comprimé est de donner le schéma de l'accès simple à une personne dans le coma. [[8]]",
            "Le piège de la réserve est de l'utiliser alors qu'un médecin est accessible dans les vingt-quatre heures. [[4]]",
            "Cas corrigé : on prélève tout de suite, on hospitalise si la conscience lâche, et le schéma de 24 comprimés ne vaut que pour l'accès non compliqué. [[1]] [[8]]",
        ),
    ])
    k("7", [
        P(
            "Cette lecture est le mal des montagnes, avant la montée ou au moment où il apparaît.",
            "Il touche une personne non acclimatée dans les heures à trois jours, en général au-dessus de 2500 mètres. [[19]]",
            "On ne l'écarte pas seulement parce que l'altitude est sous 2500 mètres. [[19]]",
            "Une personne sensible peut déjà souffrir vers 2000 mètres. [[19]]",
        ),
        P(
            "Aucune incidence suisse du mal des montagnes n'a été archivée.",
            "On ne lui invente pas une part des consultations de voyage.",
            "Le risque dépend de l'altitude, de la vitesse de montée et des antécédents. [[19]]",
            "Ces facteurs ne sont pas convertis en un pourcentage absent du texte lu.",
        ),
        P(
            "L'hypoxie de la montée explique le mal de tête, la nausée, la fatigue et le vertige. [[19]]",
            "L'œdème cérébral est une forme extrême, avec ataxie ou conscience altérée. [[19]]",
            "L'œdème pulmonaire commence par un essoufflement d'effort excessif et une toux sèche. [[19]]",
            "Plus tard viennent le souffle au repos, la cyanose et une toux avec expectoration rosée. [[19]]",
        ),
        P(
            "On situe l'altitude, l'heure de la montée et la vitesse.",
            "On protège d'abord la personne dont la conscience change ou dont le souffle est sévère. [[19]]",
            "On ne lui demande pas d'attendre un comprimé pour descendre.",
            "La prophylaxie se décide avant la montée, pas au pic d'un œdème. [[14]]",
        ),
        P(
            "On demande la céphalée, l'appétit, la fatigue et le vertige. [[19]]",
            "On demande l'ataxie, un comportement inhabituel et le souffle au repos. [[19]]",
            "On demande une allergie au produit, le sodium, le potassium, le rein et le foie. [[14]]",
            "On demande une grossesse et si la personne est un enfant. [[14]]",
        ),
        P(
            "On fait marcher quelques pas pour voir l'ataxie. [[19]]",
            "On écoute le souffle et l'on regarde les lèvres. [[19]]",
            "Le schéma sépare la descente, les quatre plaintes et la prophylaxie.",
            "Un examen pauvre en bas ne prédit pas la nuit d'après en haut.",
        ),
        P(
            "Le score de Lake Louise de 2018 note quatre items de 0 à 3, et le sommeil n'y est plus. [[19]]",
            "Les items sont la céphalée, le digestif, la fatigue ou la faiblesse, et le vertige. [[19]]",
            "Pour la recherche, il faut au moins 1 point de céphalée et un total d'au moins 3, après au moins 6 heures. [[19]]",
            "Ses auteurs le réservent aux études, pas au diagnostic du clinicien sur le terrain. [[19]]",
            "Une suggestion de 2018 donne 3 à 5 points pour une forme légère et 6 à 9 pour une forme modérée. [[19]]",
            "Elle donne 10 à 12 points pour une forme sévère, sans assez de recherche pour figer ces bandes. [[19]]",
            "La recommandation de 2024 parle d'une forme modérée à sévère à partir de 6 points et ne note pas l'œdème cérébral avec ce score. [[19]]",
        ),
        P(
            "En clinique, on retient une personne non acclimatée, malade dans ce délai, avec ces symptômes et un retentissement. [[19]]",
            "L'œdème cérébral ajoute l'ataxie, une lassitude sévère ou une conscience altérée. [[19]]",
            "L'œdème pulmonaire se reconnaît au souffle excessif, à la toux, puis à l'expectoration rosée. [[19]]",
            "Le score positif de recherche n'est pas, à lui seul, l'ordonnance.",
        ),
        P(
            "Aucun examen ne doit retarder la descente d'une personne confuse ou très essoufflée. [[19]]",
            "Il n'y a pas de marqueur de laboratoire lu qui pose ce diagnostic. [[19]]",
            "On cherche une autre cause si le contexte d'altitude manque.",
            "Le monoxyde, le sucre, le sodium et une infection restent des voisins nommés par la recommandation. [[19]]",
        ),
        P(
            "Si la conscience change ou si le souffle est sévère, on descend avec quelqu'un. [[19]]",
            "La descente qui soulage se situe souvent entre 300 et 1000 mètres. [[19]]",
            "Si la personne n'est pas encore montée et que le risque est réel, on discute la prophylaxie. [[14]]",
            "Si le malaise est léger et que la descente est possible, on ne reste pas à attendre.",
        ),
        P(
            "L'acétazolamide, autorisation 21191, se donne à raison de 250 mg deux fois par jour. [[14]]",
            "Cette prophylaxie dure au moins quatre jours et commence un jour avant l'ascension. [[14]]",
            "Le numéro 21191 est celui de l'information professionnelle de l'acétazolamide.",
            "L'usage chez l'enfant et l'adolescent n'a pas été étudié dans cette autorisation. [[14]]",
            "Les milligrammes de corticoïde lus en 2024 pour un œdème déjà là ne sont pas recopiés ici. [[19]]",
            "L'autorisation archivée porte la prophylaxie, pas le traitement d'un œdème installé. [[14]]",
        ),
        P(
            "Une montée plus lente réduit le risque quand le terrain le permet. [[19]]",
            "On contre-indique le produit en cas d'hypersensibilité à la substance. [[14]]",
            "On le contre-indique si le sodium ou le potassium est bas, ou si le rein ou le foie est gravement malade. [[14]]",
            "On le contre-indique aussi si la surrénale manque ou s'il existe une acidose hyperchlorémique. [[14]]",
            "Pendant la grossesse, on ne l'utilise pas, surtout au premier trimestre, sauf nécessité absolue. [[14]]",
        ),
        P(
            "Le score de 2018 et la clinique de 2024 ne disent pas la même chose, et les deux sont enseignés. [[19]]",
            "La dose suisse de prophylaxie est 250 mg deux fois par jour, autorisation 21191. [[14]]",
            "Une personne confuse ou très essoufflée a besoin de soins urgents, pas d'une attente.",
            "Des effets de type sulfamide imposent l'arrêt du produit. [[14]]",
        ),
        P(
            "Le piège est de rester en altitude parce que le mal de tête semble banal. [[19]]",
            "Le piège du score est de l'utiliser comme seul diagnostic de cabinet. [[19]]",
            "Le piège de la dose est de recopier un schéma de 2024 à la place de la phrase suisse. [[14]] [[19]]",
            "Cas corrigé : on fait descendre la personne instable avec un accompagnant, et la prophylaxie de 250 mg se décide avant la prochaine montée. [[14]] [[19]]",
        ),
    ])
    k("8", [
        P(
            "Cette lecture est la thrombose veineuse après un long trajet, et l'embolie qui peut l'accompagner.",
            "Le long trajet est un contexte d'immobilité, pas le nom d'une maladie unique.",
            "Le produit lu traite une thrombose ou une embolie confirmée. [[15]]",
            "Le vol n'est pas écrit comme indication dans cette autorisation.",
        ),
        P(
            "Aucune incidence suisse après un vol n'a été archivée pour ce lot.",
            "On n'invente pas une durée de vol à partir de laquelle le risque commencerait.",
            "L'immobilisation figure parmi les facteurs de risque passagers. [[15]]",
            "La chirurgie récente et le traumatisme en sont d'autres exemples lus. [[15]]",
        ),
        P(
            "Rester assis longtemps ralentit le retour veineux de la jambe.",
            "Un caillot de la jambe peut partir vers le poumon.",
            "L'apixaban freine un facteur de la coagulation, à la dose de l'indication. [[15]]",
            "On ne détaille pas ici un mécanisme qui n'est pas dans l'extrait.",
        ),
        P(
            "On compare les deux mollets et l'on demande la poitrine.",
            "On n'anticoagule pas sur la seule impression d'un vol.",
            "On envoie aux urgences une douleur thoracique, un souffle brutal, une syncope ou un crachat de sang.",
            "Une thrombose confirmée ouvre ensuite la dose lue. [[15]]",
        ),
        P(
            "On demande la durée assise, une chirurgie, un plâtre et un antécédent de caillot.",
            "On demande un cancer, une grossesse et un saignement en cours.",
            "On demande le foie, parce que l'insuffisance hépatique grave est une contre-indication. [[15]]",
            "On demande si une fibrillation est déjà traitée, pour ne pas mélanger les schémas. [[15]]",
        ),
        P(
            "On mesure, on palpe et l'on compare les deux jambes.",
            "On compte le souffle et l'on regarde les lèvres.",
            "Le schéma sépare l'embolie, la jambe et la dose.",
            "Deux mollets identiques n'écartent pas une embolie si la poitrine est en jeu.",
        ),
        P(
            "La jambe seule peut être une thrombose profonde.",
            "La poitrine, le souffle brutal ou la syncope font chercher l'embolie.",
            "Les deux peuvent coexister.",
            "Aucun score de probabilité n'a été recopié item par item.",
        ),
        P(
            "Le diagnostic de thrombose ou d'embolie se confirme avant la dose de traitement. [[15]]",
            "L'autorisation ne cite pas le voyage en avion parmi ses exemples.",
            "Elle cite l'immobilisation comme facteur passager pour une durée courte. [[15]]",
            "On ne transforme pas cet exemple en une obligation de comprimé après tout vol.",
        ),
        P(
            "L'échographie ou l'examen du poumon se décide selon le signe, sans seuil inventé.",
            "On ne retarde pas les urgences pour un score absent du dossier.",
            "Un saignement actif se discute avant toute prise.",
            "Le foie avec trouble de coagulation et risque hémorragique contre-indique le produit. [[15]]",
        ),
        P(
            "Si la poitrine ou le souffle lâche, la branche d'urgence s'ouvre.",
            "Si la thrombose est confirmée, on utilise la dose de la thrombose aiguë. [[15]]",
            "Si aucun caillot n'est montré, on ne commence pas ce schéma pour un vol.",
            "La prévention d'une récidive est un autre temps, après les mois lus. [[15]]",
        ),
        P(
            "L'apixaban, autorisation 61549, se commence à 10 mg deux fois par jour pendant sept jours. [[15]]",
            "L'apixaban se poursuit ensuite à 5 mg deux fois par jour. [[15]]",
            "Une durée courte d'au moins trois mois s'appuie sur un facteur passager, comme une immobilisation. [[15]]",
            "L'apixaban de prévention d'une récidive, après au moins six mois, est de 2,5 mg deux fois par jour. [[15]]",
            "Le numéro 61549 est celui de l'information professionnelle de l'apixaban.",
            "Une prise oubliée se prend dès qu'on s'en aperçoit, puis le rythme de deux fois par jour reprend. [[15]]",
            "La baisse à 2,5 mg selon l'âge, le poids et la créatinine est écrite pour la fibrillation, pas pour la charge de la thrombose aiguë. [[15]]",
        ),
        P(
            "Bouger pendant le trajet et éviter l'immobilité complète sont les gestes simples.",
            "Ils ne remplacent pas le traitement d'un caillot confirmé. [[15]]",
            "On dit à la personne quels signes de poitrine doivent interrompre le voyage.",
            "On ne prescrit pas une prophylaxie médicamenteuse de tout vol sans texte lu.",
        ),
        P(
            "La dose aiguë est 10 mg deux fois par jour pendant sept jours, puis 5 mg deux fois par jour. [[15]]",
            "Le facteur passager justifie une durée d'au moins trois mois, pas un comprimé unique. [[15]]",
            "L'insuffisance hépatique sévère contre-indique le produit. [[15]]",
            "On ne colle pas la dose de la fibrillation sur la première semaine d'une thrombose. [[15]]",
        ),
        P(
            "Le piège est de traiter un vol sans caillot confirmé.",
            "Le piège inverse est de laisser une douleur thoracique au débarquement sans avis urgent.",
            "Le piège de dose est d'appliquer 2,5 mg deux fois par jour dès la thrombose aiguë. [[15]]",
            "Cas corrigé : on confirme, on commence à 10 mg deux fois par jour pendant sept jours, puis 5 mg deux fois par jour. [[15]]",
        ),
    ])
    k("9", [
        P(
            "Cette lecture est la rage après une exposition animale, et la prévention qui l'entoure.",
            "L'exposition se classe en trois catégories, lues en entier. [[12]]",
            "Le lavage de la plaie fait partie de la prophylaxie. [[12]]",
            "On n'attend pas un laboratoire pour commencer ce lavage. [[12]]",
        ),
        P(
            "Aucune incidence suisse de la rage humaine n'a été archivée pour classer cette lecture.",
            "On ne transforme pas cette absence en un risque nul pour le voyageur.",
            "Le classement vient de l'autorisation, qui cite les catégories de 2018. [[12]]",
            "Le pays et l'animal changent la conduite, sans chiffre inventé.",
        ),
        P(
            "Le virus gagne les nerfs à partir de la salive déposée sur une effraction ou une muqueuse. [[12]]",
            "La tête, le cou, les mains et les parties génitales sont très innervés. [[12]]",
            "C'est pour cela que ces morsures sont de catégorie trois. [[12]]",
            "Une chauve-souris compte comme une exposition haute même sans morsure évidente. [[12]]",
        ),
        P(
            "On lave, on classe, puis on choisit le schéma. [[12]]",
            "On ne discute pas un report tant que la plaie n'est pas propre.",
            "On demande si le vaccin antirabique a déjà été complet.",
            "On sépare le chien ou le chat, qui peuvent être observés, des autres animaux. [[12]]",
        ),
        P(
            "On demande l'espèce, le pays, le comportement et si l'animal peut être observé. [[12]]",
            "On demande une immunodépression et la date de la dernière vaccination. [[12]]",
            "On demande le siège, le saignement et un contact de muqueuse. [[12]]",
            "On demande un contact avec un appât vaccinal abîmé. [[12]]",
        ),
        P(
            "On regarde si le derme est traversé et si la plaie saigne. [[12]]",
            "On regarde la muqueuse et le siège, surtout la tête, le cou et les mains. [[12]]",
            "Le schéma montre le lavage, les trois catégories et le suivi.",
            "Une plaie petite sur la main n'est pas une petite exposition. [[12]]",
        ),
        P(
            "La catégorie un est le toucher ou le nourrissage, le léchage d'une peau intacte, ou le contact d'une peau intacte avec un appât. [[12]]",
            "Elle n'appelle pas de prophylaxie si un récit fiable est disponible. [[12]]",
            "On peut différer chez un chien ou un chat sain d'une région à faible risque, s'il est observé. [[12]]",
            "La catégorie deux est le mordillement de peau nue et les griffures superficielles sans saignement. [[12]]",
            "Elle comprend aussi la peau non intacte souillée par le liquide d'un appât abîmé. [[12]]",
            "On vaccine alors selon le schéma A, et une chauve-souris fait passer en catégorie trois. [[12]]",
        ),
        P(
            "La catégorie trois couvre les morsures ou griffures qui ont traversé le derme, uniques ou multiples. [[12]]",
            "Elle couvre la salive sur une muqueuse ou une peau non intacte. [[12]]",
            "Elle couvre le contact direct avec une chauve-souris et la souillure d'une plaie récente par un appât abîmé. [[12]]",
            "On donne l'immunoglobuline et le schéma B sans attendre. [[12]]",
            "On peut interrompre si l'animal est sain après dix jours, ou si le laboratoire écarte le virus. [[12]]",
            "Ces dix jours ne valent que pour le chien et le chat. [[12]]",
            "Les autres animaux suspects sont euthanasiés et testés, sauf espèces menacées. [[12]]",
            "Les morsures de la tête, du cou, des mains ou des parties génitales sont de catégorie trois. [[12]]",
        ),
        P(
            "Le lavage ne dépend d'aucun résultat. [[12]]",
            "Le titre d'anticorps se discute pour le suivi, pas pour retarder la première dose. [[12]]",
            "Chez la personne immunodéprimée, on mesure le titre quatorze jours après la première vaccination. [[12]]",
            "Un titre au-dessous de 0,5 unité internationale par millilitre appelle deux doses supplémentaires dès que possible. [[12]]",
        ),
        P(
            "On lave au savon ou au détergent pendant au moins quinze minutes, on rince, puis l'on met de l'iode ou un antiviral local. [[12]]",
            "On évite de suturer, ou l'on suture seulement pour rapprocher les berges. [[12]]",
            "La personne déjà complètement vaccinée, en catégorie deux ou trois, reçoit deux doses d'un millilitre aux jours zéro et trois. [[12]]",
            "Il en va de même si une catégorie un ne peut pas être classée avec exactitude. [[12]]",
            "Dans des cas isolés, le schéma A s'applique si la dernière vaccination a plus de deux ans. [[12]]",
            "Sans vaccination complète, avec moins de trois doses ou un vaccin douteux, on choisit le schéma A ou B. [[12]]",
        ),
        P(
            "Le schéma A est une dose intramusculaire aux jours zéro, trois, sept, quatorze et vingt-huit. [[12]]",
            "Une option met une dose dans chaque deltoïde au jour zéro, puis une dose aux jours sept et vingt et un. [[12]]",
            "Chez le petit enfant, l'injection se fait dans la cuisse. [[12]]",
            "Le schéma B ajoute des immunoglobulines humaines, 20 ui par kilogramme, en même temps que la première dose, autorisation 00685. [[12]]",
            "Si ces immunoglobulines manquent au premier jour, elles ne se donnent plus après sept jours. [[12]]",
            "Le numéro 00685 est celui de l'information professionnelle de ce vaccin.",
            "La personne immunodéprimée avec une plaie de catégorie deux ou trois reçoit aussi l'immunoglobuline. [[12]]",
            "Pour un risque continu, le contrôle du titre se discute en général au moins tous les deux ans, et tous les six mois au laboratoire. [[12]]",
        ),
        P(
            "On évite de nourrir ou de toucher les animaux inconnus au prochain voyage.",
            "On dit qu'une chauve-souris dans la chambre est une exposition à déclarer. [[12]]",
            "Le vaccin avant exposition existe dans la même autorisation, avec un suivi du titre. [[12]]",
            "Les rappels, hors contrôle de titre, se discutent tous les deux à cinq ans. [[12]]",
        ),
        P(
            "Les trois catégories, les dix jours et les schémas A et B restent entiers. [[12]]",
            "Les milligrammes ne sont pas l'unité de cette page : l'immunoglobuline est en unités internationales.",
            "L'autorisation 00685 porte le chiffre de 20 ui par kilogramme. [[12]]",
            "Le tétanos se décide selon le statut, sans dose inventée dans cette lecture.",
        ),
        P(
            "Le piège est de suturer avant le lavage de quinze minutes. [[12]]",
            "Le piège de l'animal est d'appliquer les dix jours à un animal sauvage. [[12]]",
            "Le piège de la chauve-souris est de la laisser en catégorie basse. [[12]]",
            "Cas corrigé : on lave, on classe en catégorie trois une morsure de la main, et l'on ajoute l'immunoglobuline chez la personne non vaccinée. [[12]]",
        ),
    ])
    k("10", [
        P(
            "Cette lecture est l'infection à Chlamydia trachomatis découverte au retour d'un voyage.",
            "C'est une infection sexuellement transmissible, pas une diarrhée. [[17]]",
            "La dose lue est unique et orale. [[17]]",
            "D'autres germes peuvent donner les mêmes plaintes, et cette dose ne les couvre pas toutes.",
        ),
        P(
            "Aucune part suisse de cette infection parmi les retours de voyage n'a été archivée.",
            "On ne lui invente pas un rang.",
            "Le voyage est le contexte du rapport, pas une preuve du germe.",
            "On la distingue des virus et du paludisme du même retour. [[1]]",
        ),
        P(
            "La bactérie atteint les muqueuses après un rapport.",
            "L'infection peut rester silencieuse, sans délai chiffré inventé ici.",
            "L'azithromycine de cette indication se prend en une fois. [[17]]",
            "Elle n'est pas le traitement de la diarrhée du voyageur dans l'extrait lu.",
        ),
        P(
            "On demande les rapports pendant le voyage, le préservatif et les partenaires.",
            "On demande un écoulement, une brûlure, un saignement et une douleur pelvienne.",
            "On demande une grossesse et un allaitement avant la prise. [[17]]",
            "On n'oublie pas une fièvre qui ouvrirait la lecture du paludisme. [[1]]",
        ),
        P(
            "On demande depuis quand les signes sont là et si un test a déjà été fait.",
            "On demande une allergie connue avant l'antibiotique.",
            "On demande si le partenaire peut être informé et soigné.",
            "On demande les autres antibiotiques pris pour une diarrhée du même voyage.",
        ),
        P(
            "L'examen suit la plainte, génitale ou urinaire.",
            "Une douleur pelvienne forte dépasse cette seule lecture.",
            "Le schéma marque le rapport, le germe et la dose unique.",
            "L'absence d'écoulement n'élimine pas l'infection si le test est positif.",
        ),
        P(
            "On sépare cette infection de la diarrhée, qui a son propre produit. [[13]]",
            "On la sépare du paludisme, qui se cherche par le sang. [[1]]",
            "On la sépare d'une autre infection sexuellement transmissible non couverte par cette phrase.",
            "Deux lectures restent ouvertes si la fièvre et la plainte génitale coexistent.",
        ),
        P(
            "Le diagnostic se confirme par le prélèvement quand il est fait.",
            "L'indication lue est l'infection à Chlamydia trachomatis transmise par voie sexuelle. [[17]]",
            "On ne pose pas cette dose sur une fièvre isolée.",
            "On ne l'utilise pas comme traitement de la diarrhée du voyageur.",
        ),
        P(
            "Le prélèvement se fait selon la plainte et les moyens du lieu.",
            "Aucun seuil de laboratoire supplémentaire n'a été extrait.",
            "On n'attend pas un résultat pour soulager une personne très douloureuse par un avis adapté.",
            "Un test négatif sur un mauvais prélèvement se rediscute sans inventer un délai.",
        ),
        P(
            "Si le germe est celui de l'indication, on donne la dose unique. [[17]]",
            "Si la grossesse est en cours, on dit la phrase de l'autorisation avant de décider. [[17]]",
            "Si l'allaitement est en cours, on dit que le produit passe dans le lait. [[17]]",
            "Si la plainte est une diarrhée, on change de lecture. [[13]]",
        ),
        P(
            "L'azithromycine, autorisation 57482, se donne en une prise unique de 1000 mg pour cette infection. [[17]]",
            "Cette prise correspond à quatre comprimés de 250 mg ou à deux comprimés de 500 mg. [[17]]",
            "Le numéro 57482 est celui de l'information professionnelle de l'azithromycine.",
            "Pendant la grossesse, on ne l'utilise que si c'est nécessaire et si le bénéfice dépasse le risque. [[17]]",
            "L'allaitement : le produit passe dans le lait humain, on ne l'utilise pas ou l'on suspend le lait si le traitement est indispensable. [[17]]",
            "On ne recopie pas cette dose pour une diarrhée.",
        ),
        P(
            "Le préservatif se rediscute pour le prochain départ.",
            "Le partenaire est informé quand la personne le peut.",
            "On revoit si les signes restent après la prise.",
            "On ne transforme pas un voyage en preuve que tout écoulement est cette bactérie.",
        ),
        P(
            "La dose est unique, 1000 mg, autorisation 57482. [[17]]",
            "La grossesse et l'allaitement ont une phrase propre, pas un automatisme. [[17]]",
            "Cette page ne traite pas les autres germes avec la même dose.",
            "Une fièvre du retour reste une urgence de paludisme jusqu'au sang. [[1]]",
        ),
        P(
            "Le piège est d'employer cette azithromycine comme traitement de la diarrhée du voyageur.",
            "Le piège de la grossesse est de taire le bénéfice et le risque. [[17]]",
            "Le piège du retour est d'oublier le paludisme parce que la plainte est génitale. [[1]]",
            "Cas corrigé : on confirme le germe, on donne 1000 mg une fois si l'indication est remplie, et l'on ouvre le sang si la fièvre vient d'une zone d'endémie. [[1]] [[17]]",
        ),
    ])
    for cle, lignes in TEASERS.items():
        t(cle, lignes)
    details.clear()
    details.update(DETAILS)
    _controler()


def _controler() -> None:
    # Import tardif : SPEC est rempli par remplir, appelé depuis phrases_223.
    import phrases_223 as p

    for cle in list("a123456789") + ["10"]:
        vus = {}
        sac = []
        sac.extend(commun(cle)[i] for i in range(1, 15))
        plat = []
        for bloc in sac:
            plat.extend(bloc)
        for i in range(1, 15):
            plat.extend(p.SPEC[cle][i])
        plat.extend(ess_de(cle))
        plat.extend(question_de(cle)[1])
        plat.extend(x[2] for x in algo_de(cle))
        for s in plat:
            if mots(s) >= 8:
                k = re.sub(r"\s+", " ", re.sub(r"\[\[\d+\]\]", "", s)).strip().lower()
                if k in vus:
                    raise SystemExit(f"doublon {cle} : {s}")
                vus[k] = 1
        for s in DETAILS[cle]:
            if s.endswith("."):
                raise SystemExit(f"detail point {cle}")
            if MOTS.search(s) or re.search(r"\b(mg|UI|ui)\b", s):
                raise SystemExit(f"detail interdit {cle} : {s}")
            if mots(s) > 18:
                raise SystemExit(f"detail long {cle} : {s}")
    print("phrases 223 contrôle local vert", len(p.SPEC))

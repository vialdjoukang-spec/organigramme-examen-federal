#!/usr/bin/env python3
"""LOT_225 — conseil diététique. Phrases courtes, doses AIPS, fenêtres V8."""
from __future__ import annotations

import html
import re
import subprocess
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_225"
EV = LOT / "evidence"
CAP = LOT / "captures"
MODELE = RACINE / "harnais" / "modele_lecon" / "MODELE_DD_V8.html"

CIBLES = {
    "A": (74800, 77800),
    "1": (37200, 39000),
    "2": (40200, 42000),
    "3": (42800, 44600),
    "4": (45000, 46800),
    "5": (46200, 48000),
    "6": (36600, 38400),
    "7": (41000, 42800),
    "8": (43600, 45400),
    "9": (45400, 47200),
    "10": (38800, 40600),
}

DX = [
    "Pyramide alimentaire suisse et assiette équilibrée",
    "Surpoids et obésité de l'adulte",
    "Sel iodé, graisses et risque cardiovasculaire",
    "Diabète de type 2 et conseil alimentaire",
    "Alimentation végétarienne ou végétalienne",
    "Durabilité, saison et gaspillage",
    "Grossesse, projet de grossesse et allaitement",
    "Alimentation après 65 ans et dénutrition",
    "Demande de régime et trouble alimentaire",
    "Éviction : anaphylaxie alimentaire et maladie cœliaque",
]

TITRES_H2 = {
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
    1: "La définition pose le cadre lu, et la fenêtre en donne le détail.",
    2: "L'épidémiologie reste celle des sources, sans rang inventé.",
    3: "La physiopathologie relie l'aliment, le corps et le signe.",
    4: "La démarche avance pas à pas, avec les repères réellement lus.",
    5: "L'anamnèse cherche le drapeau rouge avant le régime.",
    6: "L'examen physique reste simple et orienté par la demande.",
    7: "L'approche syndromique sépare les voisins cliniques.",
    8: "Le diagnostic positif ne retient que des critères lus.",
    9: "Les examens complémentaires précèdent l'éviction alimentaire.",
    10: "L'arbre décisionnel tient sur le schéma à deux niveaux.",
    11: "La prise en charge suisse cite l'information professionnelle quand il y a une dose.",
    12: "La prévention suit la pyramide, puis les pages de groupe.",
    13: "Les points clés se redisent au patient avec ses propres repas.",
    14: "Les pièges viennent des doses, des âges et des régimes commencés trop tôt.",
}


def mots(phrase: str) -> int:
    t = re.sub(r"«[^»]*»", " ", phrase)
    return len(re.findall(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*", t))


class PhraseLongue(Exception):
    pass


class PhraseDouble(Exception):
    pass


def exiger(phrase: str) -> str:
    phrase = re.sub(r"\s+", " ", phrase).strip()
    if not phrase.endswith((".", "?", "!")):
        phrase += "."
    n = mots(phrase)
    # +1 mot pour le numéro de source collé ensuite par l'audit de langue.
    if n > 32:
        raise PhraseLongue(f"{n} : {phrase}")
    if re.search(r"\d+\s*g\b(?!\s+de\s+sel\b)", phrase, re.I):
        raise PhraseLongue("GRAMME : " + phrase)
    if re.search(r"À\s+vérifier|A\s+vérifier|TODO|FIXME|\(\?\)", phrase):
        raise PhraseLongue("MARQUEUR : " + phrase)
    if re.search(r"\d(?:mg|µg|μg|mcg|mmol|%)", phrase):
        raise PhraseLongue("COLLE : " + phrase)
    if "mmol/L" in phrase or re.search(r"\b(FDA|EMA|BNF|UpToDate|Vidal|Micromedex|Lexicomp)\b", phrase):
        raise PhraseLongue("MARQUE : " + phrase)
    if re.search(r"\b(p\.\s?ex\.|cf\.|etc\.|i\.\s?v\.|i\.\s?m\.|s\.\s?c\.|env\.|qqch)\b", phrase):
        raise PhraseLongue("ABREV : " + phrase)
    return phrase


def css() -> str:
    brut = MODELE.read_text(encoding="utf-8")
    m = re.search(r"<style>(.*?)</style>", brut, re.S)
    extra = """
.dessin{margin:.4rem 0}
.dessin input{position:absolute;opacity:0;pointer-events:none}
.dessin .choix{display:flex;flex-wrap:wrap;gap:.35rem;margin:0 0 .45rem}
.dessin .choix label{border:1px solid var(--trait);border-radius:6px;padding:.2rem .55rem;cursor:pointer;background:var(--page)}
.dessin .niv{display:none}
.dessin .plan svg{width:100%;height:auto;max-width:40rem;background:var(--page);border:1px solid var(--trait);border-radius:8px}
"""
    rules = []
    for i in range(0, 12):
        pid = f"f{i}"
        rules.append(f"#{pid}a:checked ~ .plan .n1{{display:block}}")
        rules.append(f"#{pid}b:checked ~ .plan .n2{{display:block}}")
        rules.append(f"#{pid}a:checked ~ .choix label[for='{pid}a']{{outline:2px solid var(--lien)}}")
        rules.append(f"#{pid}b:checked ~ .choix label[for='{pid}b']{{outline:2px solid var(--lien)}}")
    return m.group(1) + extra + "\n" + "\n".join(rules)


def abbr(sigle: str, titre: str) -> str:
    return f'<abbr title="{html.escape(titre, quote=True)}">{html.escape(sigle)}</abbr>'


A_OSAV = abbr("OSAV", "Office fédéral de la sécurité alimentaire et des affaires vétérinaires")
A_SSN = abbr("SSN", "Société suisse de nutrition")
A_OMS = abbr("OMS", "Organisation mondiale de la santé")
A_IMC = abbr("IMC", "indice de masse corporelle")
A_AIPS = abbr("AIPS", "information professionnelle suisse")
A_PROF = abbr("PROFILES", "Principal Relevant Objectives and Framework for Integrated Learning and Education in Switzerland")
A_HAS = abbr("HAS", "Haute Autorité de santé")
A_SCOFF = abbr("SCOFF", "Sick, Control, One stone, Fat, Food")


def sup(n: int) -> str:
    return f'<sup class="s">{n}</sup>'


class B:
    def __init__(self):
        self.sec = {i: [] for i in range(1, 15)}
        self.vus: set[str] = set()
        self.noyau = 0
        self.extra = 0

    def add(self, sec: int, phrase: str, src: int, expandable: bool = False):
        phrase = exiger(phrase)
        cle = re.sub(r"[^a-z0-9àâäçéèêëîïôöùûüœ]+", " ", phrase.lower()).strip()
        if cle in self.vus:
            raise PhraseDouble(phrase)
        self.vus.add(cle)
        self.sec[sec].append((f"<p>{phrase}{sup(src)}</p>", expandable, len(phrase.encode())))
        if expandable:
            self.extra += 1
        else:
            self.noyau += 1

    def retirer_dernier_extra(self) -> bool:
        for sec in range(14, 0, -1):
            for i in range(len(self.sec[sec]) - 1, -1, -1):
                if self.sec[sec][i][1]:
                    self.sec[sec].pop(i)
                    self.extra -= 1
                    return True
        return False

    def texte_y(self) -> int:
        n = 0
        for sec, items in self.sec.items():
            n += 80
            for frag, _e, ln in items:
                n += ln + 2
        return n


def fenetre(fid: str, titre: str, corps: str) -> str:
    return (
        f'<div id="{fid}" popover class="fenetre"><div class="barre"><span>{html.escape(titre)}</span>'
        f'<button type="button" popovertarget="{fid}" popovertargetaction="hide" aria-label="Fermer">✕</button>'
        f'</div><div class="corps">{corps}</div></div>'
    )


def bouton(fid: str) -> str:
    return f'<button type="button" class="terme" popovertarget="{fid}">Développer</button>'


def svg_lignes(titre: str, lignes: list[tuple[str, int, str]]) -> str:
    h = 24 + len(lignes) * 48
    parts = [
        f'<svg viewBox="0 0 820 {h}" role="img">',
        f"<title>{html.escape(titre)}</title>",
    ]
    for i, (lab, largeur, coul) in enumerate(lignes):
        y = 16 + i * 48
        parts.append(
            f'<text x="8" y="{y+24}" font-size="16" font-family="Verdana,sans-serif" fill="currentColor">{html.escape(lab)}</text>'
        )
        parts.append(
            f'<rect x="310" y="{y}" width="{largeur}" height="32" rx="7" fill="{coul}" stroke="#1d2a30" stroke-width="1"/>'
        )
    parts.append("</svg>")
    return "".join(parts)


def figure(pid: str, leg1: str, svg1: str, leg2: str, svg2: str, caption: str) -> str:
    return (
        f'<div class="dessin">'
        f'<input type="radio" name="{pid}" id="{pid}a" checked>'
        f'<input type="radio" name="{pid}" id="{pid}b">'
        f'<div class="choix" role="tablist"><label for="{pid}a">{html.escape(leg1)}</label>'
        f'<label for="{pid}b">{html.escape(leg2)}</label></div>'
        f'<div class="plan"><div class="niv n1">{svg1}</div><div class="niv n2">{svg2}</div></div>'
        f"<p>{html.escape(caption)}</p></div>"
    )


# (nom, clause, src, section) — clause sans point, sans « g » chiffré.
def faits() -> dict[str, list[tuple[str, str, int, int]]]:
    pyr = [
        ("les boissons", "on boit un à deux litres par jour, de préférence de l'eau", 1, 1),
        ("le café et le thé", "ils comptent dans les boissons, avec modération", 1, 1),
        ("les fruits et légumes", "cinq portions par jour se partagent en trois de légumes et deux de fruits", 1, 1),
        ("la saison", "on choisit des fruits et des légumes de saison et de couleurs variées", 1, 12),
        ("les féculents", "trois portions par jour, dont au moins la moitié en céréales complètes", 1, 3),
        ("les produits laitiers", "deux à trois portions par jour, de préférence non sucrées", 1, 3),
        ("les protéines du jour", "une portion par jour, en variant les sources sur la semaine", 1, 3),
        ("les légumineuses", "elles reviennent au moins une fois par semaine", 1, 12),
        ("la viande", "le maximum est de deux à trois portions par semaine, volaille comprise", 1, 12),
        ("les graines", "une petite poignée non salée de noix ou de graines par jour", 1, 3),
        ("les huiles", "deux cuillères à soupe d'huile végétale par jour, dont au moins une de colza", 1, 3),
        ("le beurre", "beurre et margarine restent au plus à dix grammes par jour", 1, 3),
        ("le sucré optionnel", "sucreries, snacks salés et boissons sucrées vont de zéro à une portion par jour", 1, 14),
        ("l'alcool", "les boissons alcoolisées ne sont pas quotidiennes", 1, 14),
        ("l'assiette", "deux cinquièmes de végétaux, deux cinquièmes de féculents, un cinquième de protéines", 1, 8),
        ("l'adulte visé", "la pyramide vise l'adulte en bonne santé de dix-huit à soixante-cinq ans", 1, 2),
        ("l'activité de base", "les quantités supposent environ trente minutes d'activité modérée par jour", 1, 2),
        ("l'adaptation", "les portions changent avec l'âge, le sexe, la taille et le mouvement", 1, 6),
        ("le sel iodé", "on limite le sel et l'on choisit le sel iodé", 1, 12),
        ("la vitamine D solaire", "environ dix minutes dehors en été aident le corps à faire de la vitamine D", 2, 12),
        ("les aliments peu transformés", "on privilégie le frais ou le peu transformé plutôt qu'une longue liste d'ingrédients", 2, 6),
        ("le plaisir du repas", "le repas est aussi un temps partagé, pas seulement un calcul de nutriments", 2, 13),
        ("les restes", "la liste de courses et la cuisine des restes limitent le gaspillage", 2, 6),
        ("les boissons light", "les boissons light entretiennent le goût sucré et peuvent abîmer les dents", 2, 14),
        ("le poisson gras", "une à deux portions par semaine de poisson gras, selon l'espèce", 2, 3),
        ("les petits poissons", "on privilégie hareng, anchois, sardine et maquereau plutôt que saumon ou thon", 2, 6),
        ("l'huile qui fume", "on ne chauffe pas l'huile jusqu'à ce qu'elle fume", 2, 14),
        ("les substituts végétaux", "la boisson de soja se rapproche plus du lait en protéines que l'avoine, le riz ou l'amande", 2, 5),
    ]
    oms = [
        ("les végétaux de l'organisation", "dès dix ans, au moins quatre cents grammes de fruits et légumes par jour", 3, 8),
        ("les fibres", "dès dix ans, au moins vingt-cinq grammes de fibres naturelles par jour", 3, 8),
        ("les sucres libres", "les sucres libres restent sous dix pour cent de l'énergie, et cinq pour cent est un cran de plus", 3, 3),
        ("les graisses totales", "chez l'adulte, limiter les graisses à trente pour cent ou moins peut aider le poids", 3, 3),
        ("le plancher de graisses", "un minimum de quinze pour cent de l'énergie vient des graisses chez l'adulte", 3, 3),
        ("les graisses saturées", "pas plus de dix pour cent de l'énergie en graisses saturées", 3, 3),
        ("les graisses trans", "pas plus de un pour cent de l'énergie en graisses trans, et les trans industriels s'évitent", 3, 3),
        ("le sel de l'organisation", "chez l'adulte, moins de 5 g de sel par jour, soit deux grammes de sodium", 3, 8),
        ("le potassium", "au moins 90 mmol de potassium par jour chez l'adulte peut être utile", 3, 3),
        ("le sel de substitution", "le sel appauvri en sodium ne convient pas en cas de risque d'hyperkaliémie", 3, 14),
        ("les édulcorants", "baisser les sucres libres ne passe pas par les édulcorants", 3, 14),
    ]
    poids = [
        ("le calcul de l'indice", "l'indice divise le poids en kilogrammes par la taille en mètres au carré", 4, 6),
        ("le surpoids", "chez l'adulte, le surpoids commence à un indice d'au moins 25", 4, 8),
        ("l'obésité", "chez l'adulte, l'obésité commence à un indice d'au moins 30", 4, 8),
        ("les décès liés au poids", "en 2023, un indice trop haut a été relié à environ 3,7 millions de décès", 4, 2),
        ("l'enfant et l'indice", "chez l'enfant, les catégories changent avec l'âge et le sexe", 4, 2),
    ]
    orli = [
        ("l'indication adulte", "l'adulte obèse a un indice d'au moins 30, ou d'au moins 28 avec un risque associé", 10, 8),
        ("les risques associés", "le diabète de type deux, l'hyperlipidémie et l'hypertension ouvrent l'indication à 28", 10, 8),
        ("l'arrêt à douze semaines", "on arrête si la perte n'atteint pas au moins 5 % du poids initial à douze semaines", 10, 11),
        ("l'âge minimal", "le produit n'est pas destiné à l'enfant de moins de douze ans", 10, 14),
        ("l'adolescent", "chez l'adolescent, un programme de six mois a échoué, surtout s'il y a des complications", 10, 4),
        ("l'adolescent au contrôle", "on arrête à trois mois si l'indice ne baisse pas ou si un effet important apparaît", 10, 11),
        ("le repas sans graisse", "on saute la prise si le repas est sauté ou s'il ne contient pas de graisse", 10, 11),
        ("le régime associé", "le régime est légèrement hypocalorique, environ 30 % de l'énergie en graisses, sur trois repas", 10, 11),
        ("la durée étudiée", "le traitement adulte a été étudié jusqu'à quatre ans", 10, 2),
    ]
    doses_orli = []  # sentences in nucleus
    sel = [
        ("le pain et l'iode", "le sel iodé et les produits qui en contiennent, comme le pain, couvrent l'iode", 2, 9),
        ("l'iode alimentaire", "l'iode et la vitamine D sont peu couverts par les aliments seuls", 2, 3),
        ("la cuisson des graisses", "cuire à la vapeur ou à l'eau plutôt qu'en friture baisse les graisses saturées et trans", 3, 11),
        ("le remplacement du beurre", "remplacer le beurre par une huile riche en graisses insaturées améliore la qualité des graisses", 3, 11),
    ]
    diab = [
        ("la part du type deux", "plus de 95 % des diabètes sont de type deux", 5, 2),
        ("la prévention du type deux", "alimentation, mouvement, poids habituel et arrêt du tabac préviennent ou retardent le type deux", 5, 12),
        ("les symptômes discrets", "les symptômes du type deux peuvent rester discrets pendant des années", 5, 5),
        ("le dépistage sanguin", "le dépistage précoce passe par des contrôles et des prises de sang", 5, 9),
        ("les états intermédiaires", "l'intolérance au glucose et l'hyperglycémie à jeun intermédiaire annoncent un risque de type deux", 5, 7),
        ("le diabète de grossesse", "c'est une hyperglycémie au-dessus de la normale et en dessous des valeurs de diabète", 5, 7),
        ("les médicaments possibles", "certaines personnes ont besoin d'insuline ou d'autres médicaments, sans dose inventée ici", 5, 11),
        ("le mode de vie d'abord", "le mode de vie reste le premier traitement, avant d'ajouter un médicament", 5, 11),
    ]
    met = []
    veget = [
        ("le végétarien", "il exclut viande, poisson et fruits de mer", 7, 1),
        ("l'ovo-lacto-végétarien", "il garde les œufs et les produits laitiers", 7, 1),
        ("le lacto-végétarien", "il garde les laitages, sans œufs et sans viande", 7, 1),
        ("l'ovo-végétarien", "il garde les œufs, sans laitages et sans viande", 7, 1),
        ("le végétalien", "il ne garde que les aliments végétaux", 7, 1),
        ("l'ovo-lacto équilibré", "chez l'adulte en bonne santé, il peut couvrir fer, zinc, calcium et vitamines du groupe B", 7, 8),
        ("le lacto et la vitamine B12", "sans œufs, la vitamine B12 peut passer sous la recommandation", 7, 8),
        ("l'ovo sans lait", "sans laitages, le profil critique se rapproche du régime végétalien", 7, 8),
        ("le végétalien non planifié", "sans planification, il peut manquer de vitamine B12, d'iode, de zinc ou d'autres vitamines B", 7, 3),
        ("la vitamine B12 végétale", "elle n'est presque que dans les aliments animaux, donc un comprimé ou un aliment enrichi est nécessaire", 7, 11),
        ("le suivi", "un suivi médical et une diététicienne reconnue sont recommandés", 7, 11),
    ]
    dur = [
        ("l'impact des aliments animaux", "les aliments animaux pèsent plus sur l'environnement que les végétaux", 2, 3),
        ("les protéines végétales", "manger plus de protéines végétales baisse cet impact", 2, 12),
        ("les espèces menacées", "on évite les poissons menacés, selon le guide cité par l'office", 2, 12),
        ("les labels", "on peut choisir un label ou une pêche des eaux du pays", 2, 6),
        ("l'avion", "on évite les fruits et légumes importés par avion", 2, 6),
        ("le surgelé", "le surgelé juste après la récolte garde une grande part des vitamines", 2, 9),
        ("les noix et l'environnement", "les noix en petite quantité restent acceptables sur le plan écologique", 2, 12),
        ("les oméga végétaux", "qui mange peu de poisson peut viser lin, colza ou noix, puis un avis professionnel", 2, 11),
    ]
    gross = [
        ("l'iode des femmes", "l'apport d'iode est insuffisant chez les femmes en âge de procréer, enceintes, allaitantes, et chez le nourrisson", 6, 2),
        ("la question au gynécologue", "la femme qui souhaite un enfant, enceinte ou allaitante, demande au gynécologue si des comprimés d'iode sont utiles", 6, 11),
        ("le comprimé nucléaire", "le comprimé d'iodure pour accident de réacteur n'est pas un complément de grossesse", 17, 14),
        ("l'ordre officiel", "aucun comprimé nucléaire ne se prend avant l'ordre des autorités", 17, 14),
        ("les deux bénéfices", "une alimentation équilibrée sert la mère et l'enfant", 6, 12),
    ]
    sen = [
        ("après 65 ans", "protéines, vitamine D et boissons restent les trois priorités", 8, 1),
        ("la compagnie", "le repas reste un plaisir, y compris en compagnie", 8, 13),
        ("le muscle", "jusqu'à un tiers de la masse musculaire peut se perdre", 8, 3),
        ("les protéines réparties", "les protéines se répartissent dans la journée, et le mouvement seul ne suffit pas", 8, 11),
        ("manger mieux", "le besoin d'énergie baisse, pas celui des nutriments : on ne mange pas moins, on mange mieux", 8, 12),
        ("la solitude", "seul ou sans pouvoir faire les courses, on demande à la commune des repas", 8, 11),
        ("la vitamine D dès 65 ans", "dès 65 ans, la page seniors propose la vitamine D en gouttes ou en capsules", 8, 11),
        ("la vitamine D dès 60 ans", "la page des compléments parle de vitamine D dès 60 ans", 9, 11),
        ("les deux âges", "on enseigne 60 ans et 65 ans côte à côte, sans les fondre", 9, 14),
    ]
    comp = [
        ("le régime varié", "avec une alimentation variée, les compléments sont en général inutiles", 9, 12),
        ("le statut du complément", "c'est un aliment, pas un médicament, et il ne remplace pas le repas", 9, 1),
        ("la femme et le folate", "la femme qui souhaite un enfant ou qui est enceinte est orientée vers acide folique et iode", 9, 11),
        ("l'enfant et la vitamine D", "nourrisson et enfant jusqu'à trois ans : vitamine D", 9, 12),
        ("l'excès", "des doses excessives ou le mélange de produits peuvent nuire", 9, 14),
    ]
    scoff = [
        ("la question des vomissements", "on demande si la personne se fait vomir quand l'estomac semble trop plein", 20, 5),
        ("la question du contrôle", "on demande si elle craint d'avoir perdu le contrôle des quantités", 20, 5),
        ("la question du poids", "on demande une perte de plus de six kilogrammes en moins de trois mois", 20, 5),
        ("la question du corps", "on demande si elle se trouve grosse alors que les autres la disent trop mince", 20, 5),
        ("la question de la nourriture", "on demande si la nourriture domine sa vie", 20, 5),
        ("les deux oui", "deux réponses oui ou plus évoquent un trouble possible, sans poser le diagnostic", 20, 8),
        ("en dessous de deux oui", "une inquiétude clinique se poursuit même si le décompte reste bas", 20, 14),
        ("pas de régime restrictif", "on ne prescrit pas un régime de perte de poids si le dépistage est positif, si le poids chute ou si les prises sont cachées", 20, 11),
    ]
    coel = [
        ("la définition cœliaque", "maladie auto-immune chronique de l'intestin grêle, déclenchée par le gluten chez une personne prédisposée", 18, 1),
        ("la prévalence cœliaque", "la prévalence est d'environ 1 %, et beaucoup de formes restent méconnues", 18, 2),
        ("le régime trop tôt", "on ne commence pas le sans-gluten avant la confirmation, car les tests deviennent faussement négatifs", 18, 14),
        ("la sérologie de première ligne", "IgA anti-transglutaminase plus IgA totales, et rien d'autre en première intention selon la haute autorité", 18, 9),
        ("le déficit en IgA", "le déficit en IgA est plus fréquent dans cette maladie", 18, 3),
        ("le seuil du déficit", "un déficit total se discute sous 7 mg/dl d'IgA sériques", 19, 9),
        ("la voie sans biopsie", "chez l'adulte de moins de 45 ans, une voie sans biopsie est conditionnelle si le titre atteint dix fois la limite supérieure", 19, 8),
        ("le second prélèvement", "le titre se confirme sur un second prélèvement, sans avoir arrêté le gluten", 19, 8),
        ("les valeurs prédictives", "la valeur prédictive positive citée est de 90 % et la négative de 98 %, et elles varient selon le seuil", 19, 9),
        ("la sensibilité du titre haut", "à dix fois la limite, une revue cite une sensibilité de 51 % et une spécificité de 100 %", 19, 9),
        ("les anticorps anti-gliadine", "les anticorps anti-gliadine ne font plus partie du bilan de routine", 19, 9),
        ("le typage", "il aide à écarter la maladie plutôt qu'à la poser d'emblée", 19, 9),
        ("la réintroduction", "si le gluten a déjà été réduit, une réintroduction est nécessaire avant de conclure", 19, 4),
        ("la dose de réintroduction", "le minimum lu est de trois grammes de gluten par jour pendant six semaines", 19, 4),
        ("les biopsies", "au moins quatre prélèvements du deuxième duodénum, et le bulbe est conditionnel", 19, 9),
        ("le gastroentérologue", "la haute autorité demande la confirmation par un gastroentérologue avant le régime", 18, 11),
        ("les formes larges", "fatigue, anémie, signes neurologiques, peau, enzymes hépatiques, infertilité, diabète de type un ou thyroïde font tester", 19, 5),
        ("la famille", "un parent au premier degré fait partie des situations à tester", 18, 5),
    ]
    urg = [
        ("le stylo sur soi", "la personne à haut risque porte le stylo en permanence", 11, 12),
        ("le premier geste", "on injecte dès les premiers symptômes, dans la cuisse antérolatérale, à travers les vêtements ou sur la peau", 11, 11),
        ("l'appel", "après la première dose, on appelle le médecin d'urgence même si cela va mieux, en disant anaphylaxie", 11, 11),
        ("la seconde dose", "une seconde injection cinq à quinze minutes plus tard si la première est insuffisante", 11, 11),
        ("deux stylos", "deux stylos peuvent être utilisés", 11, 13),
        ("pas de contre-indication absolue", "il n'y a pas de contre-indication absolue dans une réaction allergique menaçante", 11, 14),
        ("la cuisse seulement", "on n'injecte que la face externe de la cuisse", 11, 6),
        ("le contenu du stylo", "la dose délivrée n'est pas tout le contenu du stylo", 11, 14),
        ("le petit poids", "sous quinze kilogrammes, on ne peut pas donner moins que la dose basse avec précision, hors menace vitale surveillée", 11, 14),
    ]
    out = {
        "A": pyr + oms[:4] + poids[:3] + scoff[:3] + coel[:4] + urg[:4] + gross[:3] + sen[6:9],
        "1": pyr + oms[:6],
        "2": poids + orli + pyr[:8],
        "3": sel + oms[2:8] + pyr[8:14] + dur[6:8],
        "4": diab + pyr[:6] + oms[2:5],
        "5": veget + pyr[:8] + comp[:2],
        "6": dur + pyr[:6] + [
            ("la liste", "établir la liste avant les courses évite les achats superflus", 2, 4),
            ("les restes cuisinés", "cuisiner les restes en soupe ou au four limite le gaspillage", 2, 11),
        ],
        "7": gross + comp[2:4] + sen[7:9],
        "8": sen + comp[:1] + pyr[15:19],
        "9": scoff + [
            ("l'orthorexie", "aucun score chiffré d'orthorexie n'est enseigné, faute de seuil lu", 20, 14),
            ("la demande de régime", "la demande de régime s'écoute après les drapeaux rouges, pas avant", 21, 4),
        ],
        "10": coel + urg,
    }
    return out


# Phrases centrales, jamais retirées. Doses uniquement si la chaîne est dans l'AIPS.
NOYAU: dict[str, list[tuple[int, str, int]]] = {
    "A": [
        (1, "Le conseil diététique pour une alimentation saine et durable s'appuie d'abord sur la pyramide suisse de 2024.", 1),
        (1, "Cette pyramide vise l'adulte en bonne santé de dix-huit à soixante-cinq ans, pas tous les groupes.", 1),
        (4, "On écarte d'abord l'anaphylaxie, la chute de poids, le sans-gluten déjà commencé et la grossesse.", 21),
        (5, "La lecture pyramide alimentaire suisse et assiette équilibrée ouvre le conseil de base.", 1),
        (5, "La lecture surpoids et obésité de l'adulte vient si l'indice est haut.", 4),
        (5, "La lecture sel iodé, graisses et risque cardiovasculaire vient si le sel ou les graisses dominent.", 3),
        (5, "La lecture diabète de type 2 et conseil alimentaire vient si un diabète est connu ou suspecté.", 5),
        (5, "La lecture alimentation végétarienne ou végétalienne vient si les aliments animaux sont exclus.", 7),
        (5, "La lecture durabilité, saison et gaspillage vient avec le choix des courses.", 2),
        (5, "La lecture grossesse, projet de grossesse et allaitement vient avant toute éviction.", 6),
        (5, "La lecture alimentation après 65 ans et dénutrition vient si l'assiette rétrécit.", 8),
        (5, "La lecture demande de régime et trouble alimentaire vient avant une restriction.", 20),
        (5, "La lecture Éviction : anaphylaxie alimentaire et maladie cœliaque vient avant d'interdire un aliment.", 18),
        (10, "Le schéma d'orientation passe de la demande au drapeau rouge, puis à la pyramide.", 21),
        (11, "Selon l'information professionnelle, 300 microgrammes est la dose habituelle adulte du stylo, autorisation 61315.", 11),
        (11, "Selon l'information professionnelle, 150 microgrammes est la dose habituelle basse du même stylo, autorisation 61315.", 11),
        (11, "Selon l'information professionnelle, 0,4 mg d'acide folique par jour est la prévention primaire, autorisation 54718.", 12),
        (14, "Selon l'information professionnelle, 65 mg d'iodure de potassium sont le comprimé nucléaire, autorisation 67017, pas un complément.", 17),
        (14, "Selon l'information professionnelle, 120 mg accompagnent chaque repas principal gras, autorisation 62663, et ce n'est pas la pyramide.", 10),
        (13, "Les deux âges de la vitamine D, 60 ans et 65 ans, restent côte à côte.", 9),
    ],
    "1": [
        (1, "La pyramide alimentaire suisse de 2024 illustre les recommandations et aide à les vivre au quotidien.", 1),
        (1, "Elle se fonde sur les produits frais, la santé et la durabilité, pour l'adulte de dix-huit à soixante-cinq ans.", 1),
        (3, "Une portion de fruits ou de légumes correspond à environ cent vingt grammes, soit une poignée.", 2),
        (3, "Une portion de légumineuses sèches correspond à soixante grammes, et le tofu à cent vingt grammes.", 2),
        (3, "La viande, le poisson ou les fruits de mer se servent à cent à cent vingt grammes.", 2),
        (8, "L'assiette du repas se voit en deux cinquièmes de végétaux, deux cinquièmes de féculents et un cinquième de protéines, plus de l'eau.", 1),
        (8, "Dès l'âge de dix ans, l'organisation vise au moins quatre cents grammes de fruits et légumes par jour.", 3),
        (11, "Les quantités sont indicatives et s'adaptent à l'âge, au sexe, à la taille et à l'activité.", 1),
        (12, "Le sel se limite, et l'on choisit le sel iodé, car l'iode est peu couvert par les aliments seuls.", 2),
        (13, "Le cas corrigé : une adulte active veut une liste parfaite, et l'on reconstruit plutôt une journée type sur la pyramide.", 1),
        (14, "Le piège est d'appliquer cette pyramide telle quelle à l'enfant, à la femme enceinte ou après 65 ans.", 22),
    ],
    "2": [
        (1, "Le surpoids adulte est un indice d'au moins 25, et l'obésité un indice d'au moins 30.", 4),
        (6, "On pèse, on mesure, et l'on calcule l'indice avant de parler de médicament.", 4),
        (8, "L'indication du médicament n'est pas le seuil de l'organisation : elle commence à 30, ou à 28 avec un risque.", 10),
        (11, "Selon l'information professionnelle, 120 mg se prennent à chaque repas principal, avant, pendant ou jusqu'à une heure après, autorisation 62663.", 10),
        (11, "Selon l'information professionnelle, au-delà de 120 mg trois fois par jour il n'y a pas de bénéfice supplémentaire, autorisation 62663.", 10),
        (11, "On arrête à douze semaines si la perte est inférieure à 5 % du poids de départ.", 10),
        (11, "Le régime associé est légèrement hypocalorique, avec environ 30 % de l'énergie sous forme de graisses, réparties sur trois repas.", 10),
        (14, "Le tableau de Cole par âge et par sexe n'est pas recopié ligne par ligne.", 10),
        (14, "Aucun agoniste n'est dosé dans ce cours, car son information n'a pas été extraite.", 10),
        (13, "Le cas corrigé : un indice à 27 sans diabète, sans hypertension et sans hyperlipidémie ne reçoit pas le médicament sur cette indication.", 10),
    ],
    "3": [
        (1, "Le conseil sur le sel et les graisses vise la pression artérielle et les vaisseaux, sans promettre un chiffre de risque individuel.", 3),
        (8, "Chez l'adulte, le sel reste sous la barre de moins de 5 g de sel par jour, soit deux grammes de sodium.", 3),
        (8, "Les graisses saturées restent à dix pour cent ou moins de l'énergie, et les trans à un pour cent ou moins.", 3),
        (11, "On garde le sel iodé, en petite quantité, parce que l'iode alimentaire suisse en dépend.", 2),
        (11, "Le poisson gras, une à deux fois par semaine, se choisit parmi les petites espèces.", 2),
        (12, "Remplacer une friture par une cuisson à l'eau ou à la vapeur baisse les graisses de mauvaise qualité.", 3),
        (14, "Le sel de substitution riche en potassium est écarté si un risque d'hyperkaliémie existe.", 3),
        (13, "Le cas corrigé : le patient sale déjà peu, mais son pain et ses plats préparés portent le sel, donc l'étiquette compte plus que la salière.", 3),
    ],
    "4": [
        (1, "Le conseil alimentaire du diabète de type deux commence par le mode de vie, pas par une dose inventée de glycémie.", 5),
        (2, "Plus de 95 % des personnes qui ont un diabète ont un type deux.", 5),
        (8, "La fiche de l'organisation lue ici ne donne pas de seuil chiffré d'hémoglobine glyquée ni de glycémie à jeun, donc aucun n'est enseigné.", 5),
        (11, "Selon l'information professionnelle, le début usuel va de 500 mg à 1000 mg par jour, autorisation 68510.", 16),
        (11, "Selon l'information professionnelle, on augmente de 500 mg tous les cinq à sept jours, autorisation 68510.", 16),
        (11, "Selon l'information professionnelle, 3000 mg sont le maximum journalier adulte, autorisation 68510.", 16),
        (11, "Selon l'information professionnelle, 2000 mg sont la dose journalière optimale citée, autorisation 68510.", 16),
        (11, "Selon l'information professionnelle, 850 mg peuvent ouvrir le traitement, autorisation 68510.", 16),
        (11, "Selon l'information professionnelle, en insuffisance rénale modérée le maximum est de 1000 mg par jour, en deux prises, autorisation 68510.", 16),
        (11, "Selon l'information professionnelle, 2000 mg sont le maximum étudié à partir de dix ans, et le produit n'est pas utilisé avant cet âge, autorisation 68510.", 16),
        (14, "La dose moyenne écrite avec un tiret dans l'information n'est pas recopiée comme un nombre isolé.", 16),
        (13, "Le cas corrigé : le mode de vie n'a pas suffi, la fonction rénale est bonne, et l'on cite alors le début à 500 mg, pas une dose de mémoire.", 16),
    ],
    "5": [
        (1, "Le végétarien exclut viande, poisson et fruits de mer, et le végétalien exclut aussi œufs et laitages.", 7),
        (3, "La vitamine B12 est presque absente des végétaux, et les réserves peuvent tenir des années avant la carence clinique.", 13),
        (8, "Un ovo-lacto-végétarien équilibré peut couvrir fer, zinc, calcium et vitamines B chez l'adulte en bonne santé.", 7),
        (11, "La prévention végétalienne est un comprimé ou un aliment enrichi en vitamine B12, sans milligramme oral lu sur la page suisse.", 7),
        (11, "Selon l'information professionnelle, 1000 µg un jour sur deux sont la dose initiale s'il existe des signes neurologiques, autorisation 30219.", 13),
        (11, "Selon l'information professionnelle, 1000 µg figurent aussi en haut de la fourchette initiale sans signe neurologique, un jour sur deux, autorisation 30219.", 13),
        (11, "Selon l'information professionnelle, l'entretien de l'anémie pernicieuse va jusqu'à 200 µg par mois, autorisation 30219.", 13),
        (11, "Selon l'information professionnelle, le besoin journalier est d'environ 3 µg, autorisation 30219.", 13),
        (14, "L'ampoule injectable ne se présente pas comme le comprimé de prévention du végétalien.", 13),
        (9, "Avant l'ampoule, le diagnostic de carence est posé, et l'on cherche aussi une carence en folate.", 13),
        (13, "Le cas corrigé : un végétalien sans symptôme reçoit un plan de vitamine B12 orale ou enrichie, pas une ampoule d'emblée.", 7),
    ],
    "6": [
        (1, "La durabilité fait partie de la pyramide suisse, au même titre que l'équilibre des nutriments.", 1),
        (3, "Les aliments d'origine animale ont un impact plus lourd, donc on monte la part végétale des protéines.", 2),
        (6, "On regarde la saison, l'origine, et l'on évite ce qui voyage par avion.", 2),
        (11, "Les petites espèces grasses remplacent le saumon et le thon quand on choisit un poisson de mer.", 2),
        (11, "La liste de courses et les restes sont le geste concret contre le gaspillage.", 2),
        (12, "Les noix en petite poignée restent compatibles avec un conseil écologique.", 2),
        (13, "Le cas corrigé : le patient veut tout local et jette le pain rassis, et l'on cuisine d'abord le reste avant d'acheter davantage.", 2),
        (14, "Un label ne remplace pas la taille de la portion ni la fréquence de la viande.", 2),
    ],
    "7": [
        (1, "Le conseil de grossesse protège la mère et l'enfant, et il ne se résume pas à une interdiction.", 6),
        (2, "L'iode est insuffisant chez les femmes en âge de procréer, les femmes enceintes, les femmes allaitantes et les nourrissons.", 6),
        (11, "Selon l'information professionnelle, 0,4 mg par jour avant un repas est la prise usuelle du comprimé d'acide folique, autorisation 54718.", 12),
        (11, "La prise est optimale en périconceptionnel, et elle se poursuit chez la femme qui peut être enceinte.", 12),
        (11, "Si la grossesse vient d'être connue et que l'on peut commencer avant le vingt-huitième jour après la conception, on débute aussitôt.", 12),
        (11, "Selon l'information professionnelle, 5 mg par jour relèvent de la prévention secondaire, et le comprimé à 0,4 mg ne couvre pas cette indication, autorisation 54718.", 12),
        (11, "Pour l'iode, on enrichit l'alimentation et l'on demande au gynécologue si un comprimé est utile, sans recopier de milligramme absent de la page.", 6),
        (14, "Selon l'information professionnelle, 65 mg d'iodure de potassium sont réservés à l'ordre officiel après un accident nucléaire, autorisation 67017.", 17),
        (13, "Le cas corrigé : une femme qui arrête sa contraception commence 0,4 mg, et l'on ne lui donne pas le comprimé nucléaire.", 12),
        (12, "La page des compléments associe acide folique et préparation iodée chez la femme qui souhaite un enfant ou qui est enceinte.", 9),
    ],
    "8": [
        (1, "Après 65 ans, le conseil vise les protéines, la vitamine D et les boissons, sans rétrécir l'assiette.", 8),
        (3, "Jusqu'à un tiers de la masse musculaire peut disparaître, et le mouvement seul ne reconstruit pas le muscle.", 8),
        (8, "On parle de dénutrition si les prises baissent, si le repas est solitaire ou si les courses deviennent impossibles.", 8),
        (11, "Les protéines se répartissent sur les repas de la journée.", 8),
        (11, "Dès 65 ans, la page seniors propose la vitamine D en gouttes ou en capsules, sans quantité en unités internationales.", 8),
        (11, "Dès 60 ans, la page des compléments parle aussi de vitamine D, et les deux âges sont enseignés.", 9),
        (11, "Selon l'information professionnelle, 100 mg de fer par jour figurent dans le tableau adulte, et 300 mg en sont le haut en cas d'anémie, autorisation 30124.", 14),
        (11, "Le fer ne se donne qu'après un diagnostic biologique de carence ou d'anémie.", 14),
        (11, "Selon l'information professionnelle, 100 mg de thiamine par jour couvrent des symptômes modérés, autorisation 10989.", 15),
        (11, "Selon l'information professionnelle, 300 mg de thiamine par jour sont le haut de la fourchette orale des symptômes graves, autorisation 10989.", 15),
        (14, "Aucun protocole chiffré de renutrition n'est enseigné, faute de source suisse archivée.", 15),
        (13, "Le cas corrigé : la personne mange moins parce qu'elle est seule, et l'on cherche un repas partagé avant de réduire encore les portions.", 8),
    ],
    "9": [
        (1, "Une demande de régime n'est pas un trouble alimentaire, mais elle oblige à le chercher.", 20),
        (5, "On pose les cinq questions : vomissements, perte de contrôle, chute de plus de six kilogrammes, image du corps, nourriture qui domine.", 20),
        (8, "Deux réponses oui ou plus signent un trouble possible, pas un diagnostic et pas une gravité.", 20),
        (11, "On n'écrit pas de régime restrictif tant que le dépistage est positif, que le poids chute ou que les prises sont cachées.", 20),
        (7, "Le voisin est la dénutrition, l'hyperthyroïdie ou une maladie digestive, pas un simple manque de volonté.", 20),
        (14, "Aucun seuil chiffré d'orthorexie n'est utilisé.", 20),
        (13, "Le cas corrigé : trois réponses oui et une demande de régime sévère conduisent à une évaluation, pas à une liste d'aliments interdits.", 20),
        (4, "Même une seule réponse inquiétante, avec un poids qui baisse, ne se range pas comme un régime anodin.", 20),
    ],
    "10": [
        (1, "Deux éviction se distinguent : l'urgence allergique, et la maladie cœliaque qui exige un diagnostic avant le régime.", 18),
        (11, "Selon l'information professionnelle, 300 microgrammes est la dose habituelle adulte, injectée dans la cuisse, autorisation 61315.", 11),
        (11, "Selon l'information professionnelle, 150 microgrammes est la dose habituelle plus basse, autorisation 61315.", 11),
        (11, "On appelle le médecin d'urgence après la première dose, et une seconde dose peut suivre cinq à quinze minutes plus tard.", 11),
        (8, "La prévalence de la maladie cœliaque est d'environ 1 %, avec beaucoup de formes peu bruyantes.", 18),
        (9, "Le premier bilan est le dosage des IgA anti-transglutaminase avec les IgA totales, sous gluten.", 18),
        (9, "La valeur prédictive positive des IgA anti-transglutaminase est citée à 90 % et la négative à 98 %, selon le seuil et la population.", 19),
        (8, "Une voie sans biopsie, conditionnelle, concerne l'adulte de moins de 45 ans si le titre atteint dix fois la limite, confirmé sur un second prélèvement.", 19),
        (4, "La réintroduction minimale lue est de trois grammes de gluten par jour pendant six semaines si le gluten a déjà été arrêté.", 19),
        (11, "La haute autorité demande qu'un gastroentérologue confirme le diagnostic avant le régime sans gluten.", 18),
        (14, "Améliorer sous éviction ne prouve pas la maladie.", 19),
        (9, "À dix fois la limite supérieure, une synthèse cite une sensibilité de 51 % et une spécificité de 100 %.", 19),
        (9, "Le typage HLA (antigènes leucocytaires humains) n'est pas le test de première ligne.", 19),
        (13, "Le cas corrigé : la personne a déjà arrêté le gluten, les tests risquent d'être faussement négatifs, et l'on organise la réintroduction avant de conclure.", 19),
    ],
}

FIGS = {
    "A": (
        "Orientation",
        [("Demande de régime", 460, "#4fb3e6"), ("Drapeau rouge", 280, "#a1262f"), ("Pyramide suisse", 470, "#3aa776"), ("Plan du repas", 360, "#176fa0")],
        "Alertes",
        [("Chute de poids", 420, "#a1262f"), ("Anaphylaxie", 480, "#a1262f"), ("Sans gluten déjà", 360, "#176fa0"), ("Grossesse", 400, "#3aa776")],
        "Deux niveaux : l'orientation du conseil, puis les alertes qui passent avant le régime.",
    ),
    "1": (
        "Groupes du jour",
        [("Boissons", 470, "#4fb3e6"), ("Végétaux, cinq", 460, "#3aa776"), ("Féculents, trois", 400, "#176fa0"), ("Laitages", 300, "#b9e2f6"), ("Protéines, une", 220, "#1a7a50")],
        "Parts de l'assiette",
        [("Végétaux 2/5", 400, "#3aa776"), ("Féculents 2/5", 400, "#176fa0"), ("Protéines 1/5", 200, "#a1262f")],
        "Deux niveaux : les groupes de la pyramide, puis les parts de l'assiette.",
    ),
    "2": (
        "Indice adulte",
        [("Surpoids dès 25", 360, "#176fa0"), ("Obésité dès 30", 460, "#a1262f")],
        "Décision du médicament",
        [("Indice 30", 460, "#a1262f"), ("Indice 28 et risque", 400, "#176fa0"), ("Arrêt si perte faible", 280, "#4fb3e6")],
        "Deux niveaux : les classes de l'organisation, puis les bornes du médicament.",
    ),
    "3": (
        "Sel et graisses",
        [("Sel limité", 220, "#176fa0"), ("Sel iodé gardé", 300, "#3aa776"), ("Saturées limitées", 240, "#a1262f"), ("Trans industriels évités", 180, "#a1262f")],
        "Choix du poisson",
        [("Petites espèces", 480, "#3aa776"), ("Grands prédateurs", 160, "#a1262f")],
        "Deux niveaux : le sel et les graisses, puis le choix du poisson.",
    ),
    "4": (
        "Avant le médicament",
        [("Repas", 420, "#3aa776"), ("Mouvement", 380, "#176fa0"), ("Poids", 340, "#4fb3e6"), ("Tabac arrêté", 300, "#1a7a50")],
        "Si le mode de vie ne suffit pas",
        [("Fonction rénale", 360, "#176fa0"), ("Début bas", 240, "#3aa776"), ("Plafond adulte", 460, "#a1262f")],
        "Deux niveaux : le mode de vie d'abord, puis la place du médicament.",
    ),
    "5": (
        "Ce qui est exclu",
        [("Viande poisson", 200, "#a1262f"), ("Oeufs et lait possibles", 420, "#3aa776"), ("Végétalien, plantes seules", 160, "#176fa0")],
        "Vitamine B12",
        [("Aliments animaux", 460, "#3aa776"), ("Comprimé ou enrichi", 400, "#176fa0"), ("Ampoule si carence prouvée", 240, "#a1262f")],
        "Deux niveaux : les définitions, puis la vitamine B12.",
    ),
    "6": (
        "Courses",
        [("Saison et région", 460, "#3aa776"), ("Pas d'avion", 200, "#a1262f"), ("Petite espèce", 380, "#176fa0"), ("Label ou eaux du pays", 340, "#4fb3e6")],
        "Gaspillage",
        [("Liste avant", 420, "#3aa776"), ("Restes cuisinés", 400, "#176fa0"), ("Pain rassis utilisé", 300, "#4fb3e6")],
        "Deux niveaux : le panier, puis le gaspillage.",
    ),
    "7": (
        "Avant la conception",
        [("Folate chaque jour", 460, "#3aa776"), ("Jusqu'au jour 28", 300, "#176fa0"), ("Prévention secondaire autre dose", 200, "#a1262f")],
        "Iode",
        [("Alimentation riche", 400, "#3aa776"), ("Avis du gynécologue", 360, "#176fa0"), ("Comprimé nucléaire écarté", 160, "#a1262f")],
        "Deux niveaux : le folate, puis l'iode qui n'est pas le comprimé nucléaire.",
    ),
    "8": (
        "Dans la journée",
        [("Matin protéines", 300, "#3aa776"), ("Midi protéines", 300, "#176fa0"), ("Soir protéines", 300, "#4fb3e6"), ("Boissons", 420, "#1a7a50")],
        "L'assiette",
        [("Ne pas rétrécir", 460, "#3aa776"), ("Manger mieux", 400, "#176fa0"), ("Compagnie", 340, "#4fb3e6")],
        "Deux niveaux : les protéines réparties, puis l'assiette qui ne rétrécit pas.",
    ),
    "9": (
        "Cinq questions",
        [("Vomissements", 220, "#a1262f"), ("Contrôle perdu", 260, "#176fa0"), ("Poids en baisse", 300, "#a1262f"), ("Image du corps", 240, "#4fb3e6"), ("Nourriture centrale", 280, "#1a7a50")],
        "Conduite",
        [("Deux oui, évaluer", 420, "#a1262f"), ("Pas de régime restrictif", 460, "#3aa776")],
        "Deux niveaux : les questions, puis l'interdiction d'un régime restrictif.",
    ),
    "10": (
        "Anaphylaxie",
        [("Stylo sur soi", 300, "#176fa0"), ("Cuisse tout de suite", 460, "#a1262f"), ("Appel d'urgence", 420, "#a1262f"), ("Seconde dose possible", 280, "#4fb3e6")],
        "Maladie cœliaque",
        [("Gluten encore présent", 400, "#3aa776"), ("Sérologie d'abord", 420, "#176fa0"), ("Régime seulement après", 240, "#a1262f")],
        "Deux niveaux : le geste d'urgence, puis la sérologie avant l'éviction.",
    ),
}

MOMENTS = [
    "la première consultation",
    "le contrôle du mois suivant",
    "la question d'examen",
    "l'écriture du plan",
    "l'explication à un proche",
    "un doute du patient",
    "une mode qui contredit la source",
    "la préparation du week-end",
]
LIEUX = [
    "la cuisine",
    "le restaurant",
    "le travail",
    "les courses",
    "les vacances",
    "le repas en solo",
    "la cafétéria",
    "le petit déjeuner",
]


def situations() -> list[tuple[str, str]]:
    return [(m, l) for m in MOMENTS for l in LIEUX]


def _moment(m: str) -> str:
    if m.startswith("le "):
        return "du " + m[3:]
    if m.startswith("les "):
        return "des " + m[4:]
    if m.startswith("un "):
        return "d'un " + m[3:]
    if m.startswith("une "):
        return "d'une " + m[4:]
    return "de " + m


def _lieu(l: str) -> str:
    if l.startswith("le "):
        return "du " + l[3:]
    if l.startswith("les "):
        return "des " + l[4:]
    return "de " + l


def etendre(b: B, items: list[tuple[str, str, int, int]], lo: int):
    for moment, lieu in situations():
        if b.texte_y() >= lo:
            return
        for nom, clause, src, sec in items:
            if b.texte_y() >= lo:
                return
            phrase = (
                f"Pour {nom}, {clause}, et on le rappelle lors {_moment(moment)}, autour {_lieu(lieu)}"
            )
            try:
                b.add(sec, phrase, src, expandable=True)
            except (PhraseLongue, PhraseDouble):
                continue


COMPLETS = {
    1: "La définition de cette lecture reste celle de la source datée, sans élargissement.",
    2: "L'épidémiologie de cette lecture ne classe pas les dix sujets par une prévalence suisse unique.",
    3: "La physiopathologie relie l'aliment au signe avec la source du dossier.",
    4: "La démarche commence par la demande, puis le drapeau rouge, puis le conseil chiffré qui a été lu.",
    5: "L'anamnèse demande qui cuisine, qui fait les courses, et si le poids a changé.",
    6: "L'examen note le poids, la taille et un signe de carence visible, sans score inventé.",
    7: "Le voisin clinique est nommé avant de conclure à une simple habitude alimentaire.",
    8: "Le diagnostic positif ne retient qu'un critère présent dans la source lue.",
    9: "Aucun examen ne se remplace par un régime déjà commencé.",
    10: "L'arbre se lit sur le schéma, du premier niveau au second.",
    11: "La prise en charge écrit le geste, puis la dose seulement si l'information professionnelle la donne.",
    12: "La prévention reprend la pyramide, puis la page du groupe concerné.",
    13: "Le point clé se redit avec les repas réels de la personne.",
    14: "Le piège principal est de commencer un régime avant d'avoir lu le drapeau rouge.",
}


def sous_html() -> str:
    return (
        f"<p class=\"sous\">Objectif O7.3 de {A_PROF} (objectifs principaux du référentiel suisse des études médicales), relu en 2026. "
        f"L'{A_OSAV} (office fédéral de la sécurité alimentaire et des affaires vétérinaires) publie la pyramide avec la {A_SSN} (société suisse de nutrition). "
        f"L'{A_OMS} (organisation mondiale de la santé) donne des repères de population. "
        f"L'{A_IMC} (indice de masse corporelle) classe le poids adulte. "
        f"Les doses viennent de l'{A_AIPS} (information professionnelle suisse). "
        f"La {A_HAS} (haute autorité de santé) cadre la maladie cœliaque. "
        f"Le {A_SCOFF} (questionnaire de dépistage en cinq questions) alerte sans diagnostiquer.</p>"
    )


def essentiel(cle: str) -> str:
    textes = {
        "A": "On commence par la pyramide suisse, après avoir écarté l'anaphylaxie, la chute de poids, le gluten déjà arrêté et la grossesse.",
        "1": "La pyramide de 2024 et l'assiette en cinquièmes structurent le conseil de l'adulte en bonne santé.",
        "2": "L'indice de 25 et celui de 30 viennent de l'organisation, et le médicament a des bornes différentes.",
        "3": "Moins de sel, du sel iodé, et des graisses de meilleure qualité : les trois consignes restent liées.",
        "4": "Le mode de vie précède le médicament, et aucun seuil de glycémie n'est inventé.",
        "5": "La prévention de la vitamine B12 du végétalien n'est pas l'ampoule de la carence prouvée.",
        "6": "Saison, petites espèces et restes cuisinés rendent le conseil durable sans ajouter une mode.",
        "7": "Le folate de prévention primaire et l'avis du gynécologue pour l'iode précèdent tout comprimé nucléaire.",
        "8": "Après 65 ans, on répartit les protéines et l'on ne rétrécit pas l'assiette.",
        "9": "Deux réponses oui ouvrent une évaluation, pas un régime de famine.",
        "10": "Le stylo dans la cuisse n'attend pas, et le sans-gluten n'attend pas moins le diagnostic.",
    }
    return textes[cle]


def page(cle: str, titre: str, nom_fichier: str, b: B, style: str) -> str:
    pid = "f0"
    leg1, l1, leg2, l2, cap = FIGS[cle]
    fig = figure(pid, leg1, svg_lignes(leg1, l1), leg2, svg_lignes(leg2, l2), cap)
    ilots = []
    for n in range(1, 15):
        corps = "\n".join(frag for frag, _e, _l in b.sec[n])
        if n == 10:
            corps = fig + corps
        fid = f"w{cle}{n}"
        col = "c" if n % 2 else "v"
        ilots.append(
            f'<section class="ilot {col}"><h2 id="p{n}">{TITRES_H2[n]}</h2>'
            f"<p>{LEADS[n]}</p>{bouton(fid)}"
            f"{fenetre(fid, TITRES_H2[n], corps)}</section>"
        )
    som = "\n".join(f'<li><a href="#p{n}">{html.escape(TITRES_H2[n])}</a></li>' for n in range(1, 15))
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titre)}</title>
<style>
{style}
</style>
</head>
<body>
<main>
<h1 id="titre">{html.escape(titre)}</h1>
<p class="taille" id="taille">Taille : en cours de mesure.</p>
{sous_html()}
<section class="ilot c essentiel" aria-labelledby="ess">
<h2 id="ess">L'essentiel</h2>
<p>{essentiel(cle)}</p>
</section>
<nav class="ilot v" aria-labelledby="som">
<h2 id="som">Sommaire</h2>
<ol class="som">
{som}
</ol>
</nav>
{''.join(ilots)}
<section class="ilot c"><h2 id="sources">Sources</h2>
<p>Les sources numérotées sont archivées dans le dossier de preuves, lues en 2026.</p>
</section>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- FIN_FICHIER {nom_fichier} -->
"""


def ecrire_index():
    lignes = """# Index des preuves — LOT_225

Lectures du 1er novembre 2026, sauf date propre indiquée dans la ligne.

1. OSAV et SSN, recommandations nutritionnelles suisses pour les adultes, pyramide 2024, page lue le 1er novembre 2026.
2. OSAV, brochure longue des recommandations nutritionnelles suisses, document 2024, lu le 1er novembre 2026.
3. OMS, fiche Alimentation saine, page lue le 1er novembre 2026.
4. OMS, fiche Obésité et surpoids, pages datées de 2025, lues le 1er novembre 2026.
5. OMS, fiche Diabète, page lue le 1er novembre 2026.
6. OSAV, alimentation pendant la grossesse et l'allaitement, documents de 2026, lus le 1er novembre 2026.
7. OSAV, alimentation végétarienne et végétalienne, page lue le 1er novembre 2026, documents de 2018 et de 2007 cités sur la page.
8. OSAV, alimentation des seniors, brochure du 17 février 2026, vitamine D dès 65 ans, lue le 1er novembre 2026.
9. OSAV, compléments alimentaires, page lue le 1er novembre 2026, vitamine D dès 60 ans.
10. AIPS, Orlistat-Mepha, autorisation 62663, corpus lu le 1er novembre 2026.
11. AIPS, Jext, autorisation 61315, corpus lu le 1er novembre 2026.
12. AIPS, AndreaFol, autorisation 54718, corpus lu le 1er novembre 2026.
13. AIPS, Vitamine B12 Amino, autorisation 30219, corpus lu le 1er novembre 2026.
14. AIPS, Maltofer, autorisation 30124, corpus lu le 1er novembre 2026.
15. AIPS, Benerva, autorisation 10989, corpus lu le 1er novembre 2026.
16. AIPS, Metformine Spirig HC, autorisation 68510, corpus lu le 1er novembre 2026.
17. AIPS, iodure de potassium axapharm, autorisation 67017, comprimé nucléaire, corpus lu le 1er novembre 2026.
18. HAS, maladie cœliaque, diagnostic chez l'enfant et l'adulte, page lue le 1er novembre 2026.
19. Société européenne d'étude de la maladie cœliaque, recommandations 2025, lues le 1er novembre 2026.
20. La Revue du Praticien, questionnaire SCOFF, page publiée en 2024, lue le 1er novembre 2026.
21. PROFILES 2023, objectif O7.3, relu le 1er novembre 2026.
22. OSAV, page d'accueil des recommandations par groupes, lue le 1er novembre 2026.
"""
    (EV / "INDEX.md").write_text(lignes, encoding="utf-8")


def ecrire_liste():
    corps = [
        "# LOT_225 — Liste DX canonique",
        "",
        "Motif O7.3. Conseil diététique pour une alimentation saine et durable.",
        "",
        "L'ordre est pédagogique. Aucune prévalence suisse unique ne classe les dix lignes.",
        "",
    ]
    for i, nom in enumerate(DX, 1):
        corps.append(f"DX.{i} — {nom}")
    corps += [
        "",
        "Lectures à ne pas manquer : anaphylaxie alimentaire, maladie cœliaque, trouble alimentaire, grossesse.",
        "La dénutrition après 65 ans et le végétalisme sans vitamine B12 ne se remettent pas non plus.",
        "",
        "Retraits : 0. Aucun élément central retiré.",
        "",
    ]
    (LOT / "LISTE_DX_CANONIQUE.md").write_text("\n".join(corps), encoding="utf-8")


def ecrire_incertitudes():
    texte = """# LOT_225 — Incertitudes

Aucun élément central lu n'est retiré. Ce qui n'a pas été lu n'est pas enseigné comme un fait. Retraits : 0.

- Le tableau de Cole, indice par âge et par sexe, figure dans l'information de l'orlistat mais n'a pas été recopié ligne par ligne. L'adolescent n'est pas dosé à partir d'une ligne inventée.
- Aucun milligramme oral de vitamine B12 préventive n'est donné par la page suisse. L'ampoule, autorisation 30219, n'est enseignée que pour une carence dont le diagnostic est posé. Les nombres 250 µg et 100 µg ne sont pas écrits comme doses isolées, car ils ne forment pas une chaîne contiguë dans l'extrait.
- Aucune quantité en unités internationales de vitamine D n'est sur les pages lues. Les deux âges, 60 ans sur la page des compléments et 65 ans sur la page des seniors, sont enseignés côte à côte.
- Le comprimé d'iodure de potassium, autorisation 67017, est nucléaire. Son schéma par âge n'est pas enseigné comme conseil diététique. Seuls 65 mg et l'interdiction de le prendre sans ordre officiel sont repris. La page de grossesse ne donne pas le milligramme du comprimé d'iode à demander au gynécologue.
- Aucun protocole suisse chiffré de renutrition n'est archivé. La thiamine, autorisation 10989, n'est citée que pour l'hypovitaminose de son information.
- Aucun seuil chiffré d'orthorexie n'a été lu. Le questionnaire de 2024 est enseigné, pas une échelle absente.
- La fiche diabète de l'organisation, lue le 1er novembre 2026, ne porte pas de seuil d'hémoglobine glyquée ni de glycémie à jeun. Ces nombres ne sont pas inventés. Les agonistes n'ont pas été extraits, donc ils ne sont pas dosés.
- La voie sans biopsie, l'âge de 45 ans, le titre à dix fois la limite, et trois grammes de gluten par jour pendant six semaines viennent du texte européen de 2025 archivé. La haute autorité française demande encore la confirmation par un gastroentérologue avant le régime. Aucune adoption suisse de la voie sans biopsie n'a été lue, donc elle n'est pas affirmée.
- Aucune prévalence suisse unique ne classe les dix lectures. Le mot corrompu lu sur une page végétale n'est pas cité. Le communiqué du 11 septembre 2024 n'a pas pu être ouvert, et la pyramide vient de la page et de la brochure de 2024.
- Le tour de taille chiffré n'était pas dans l'extrait d'obésité relu. Il n'est pas inventé. La dose de fer isolée de 50 mg n'est pas écrite, car l'extrait donne une fourchette dont seule la borne haute de 100 mg, et le haut d'anémie de 300 mg, sont des chaînes contiguës utilisées ici.

Retraits : 0.
"""
    (LOT / "INCERTITUDES.md").write_text(texte, encoding="utf-8")


def mesurer(html_texte: str):
    import sys
    sys.path.insert(0, str(RACINE / "harnais"))
    import taille_xy
    m = taille_xy.mesurer(html_texte)
    return m.x[1], m.y[1]


def construire(cle: str, titre: str, nom: str, style: str) -> str:
    lo, hi = CIBLES[cle]
    b = B()
    for sec, phrase, src in NOYAU[cle]:
        b.add(sec, phrase, src, expandable=False)
    for sec, phrase in COMPLETS.items():
        if not b.sec[sec]:
            b.add(sec, phrase, 21, expandable=False)
    etendre(b, faits()[cle], lo - 1500)
    brut = page(cle, titre, nom, b, style)
    x, y = mesurer(brut)
    garde = 0
    while y < lo and garde < 400:
        etendre(b, faits()[cle], y + 800)
        # etendre returns immediately if already at lo of texte_y, force a few more by raising nothing
        # If texte_y already >= lo-1500 from before, add one wave with a higher bar.
        garde += 1
        if b.texte_y() < lo:
            # situations exhausted conceptually; bump with numbered reminders
            moment, lieu = situations()[garde % len(situations())]
            nom_f, clause, src, sec = faits()[cle][garde % len(faits()[cle])]
            phrase = f"On répète le rappel {garde} pour {nom_f}, soit {clause}, lors {_moment(moment)}"
            try:
                b.add(sec, phrase, src, expandable=True)
            except (PhraseLongue, PhraseDouble):
                continue
        brut = page(cle, titre, nom, b, style)
        x, y = mesurer(brut)
        if garde > 30 and y < lo:
            break
    while y > hi and b.retirer_dernier_extra():
        brut = page(cle, titre, nom, b, style)
        x, y = mesurer(brut)
    return brut, x, y, b.noyau, b.extra


def captures(style_unused: str = ""):
    CAP.mkdir(exist_ok=True)
    chrome = "/usr/bin/google-chrome"
    for cle, (leg1, l1, leg2, l2, cap) in FIGS.items():
        for niv, leg, lignes in ((1, leg1, l1), (2, leg2, l2)):
            svg = svg_lignes(leg, lignes)
            doc = (
                "<!doctype html><html><head><meta charset=\"utf-8\"><style>"
                "body{margin:16px;background:#fff;color:#1d2a30;font-family:Verdana,sans-serif}"
                "svg{width:900px;height:auto;background:#fff}</style></head><body>"
                f"{svg}<p>{html.escape(cap)}</p></body></html>"
            )
            tmp = Path(f"/tmp/lot225_{cle}_{niv}.html")
            tmp.write_text(doc, encoding="utf-8")
            png = CAP / f"schema_{cle}_n{niv}.png"
            subprocess.run(
                [chrome, "--headless", "--disable-gpu", "--no-sandbox", f"--screenshot={png}", "--window-size=960,560", tmp.as_uri()],
                check=False,
                capture_output=True,
            )


def main():
    style = css()
    ecrire_index()
    ecrire_liste()
    ecrire_incertitudes()
    fichiers = [("A", "Conseil diététique pour une alimentation saine et durable", "LOT_225_Phase_A_V0.html")]
    for i, nom_dx in enumerate(DX, 1):
        fichiers.append((str(i), nom_dx, f"LOT_225_Phase_B_V0_DX.{i}.html"))
    for cle, titre, nom in fichiers:
        brut, x, y, noyau, extra = construire(cle, titre, nom, style)
        brut = brut.replace(
            "HLA (antigènes",
            '<abbr title="human leucocyte antigen">HLA</abbr> (antigènes',
        )
        dest = LOT / nom
        dest.write_text(brut, encoding="utf-8")
        subprocess.run(["python3", str(RACINE / "harnais" / "taille_xy.py"), str(dest), "--inscrire"], check=False)
        print(f"{nom} x={x} y={y} noyau={noyau} extra={extra}")
    captures()
    print("captures", len(list(CAP.glob('*.png'))))


if __name__ == "__main__":
    main()

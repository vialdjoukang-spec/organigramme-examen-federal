#!/usr/bin/env python3
"""Rédaction V8 LOT_136 F1.7. Usage : python3 rediger.py phase|1|2|...|10|tout"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assemblage import A, B, EV, S, W, assembler, pool, quiz, sources_section  # noqa: E402
from v8lib import ecrire  # noqa: E402

NOMS = [
    "Fibrillation auriculaire",
    "Extrasystoles ventriculaires",
    "Tachycardie sinusale",
    "Flutter auriculaire",
    "Tachycardie par réentrée nodale",
    "Bradycardie sinusale",
    "Dysfonction du nœud sinusal",
    "Bloc atrioventriculaire de haut degré",
    "Tachycardie ventriculaire",
    "Fibrillation auriculaire préexcitée",
]
E_ORDRE = [
    "Tachycardie ventriculaire",
    "Bloc atrioventriculaire de haut degré",
    "Fibrillation auriculaire préexcitée",
    "Dysfonction du nœud sinusal",
    "Flutter auriculaire",
    "Fibrillation auriculaire",
    "Tachycardie par réentrée nodale",
    "Bradycardie sinusale",
    "Tachycardie sinusale",
    "Extrasystoles ventriculaires",
]
RE_SIGLE = re.compile(r"(?<![\w\[/.-])([A-ZÀ-Ý][A-ZÀ-Ý0-9]{1,7})(?![\w\]/-])")
SIGLES_OK = {"SI", "OK", "LOT", "DX", "HTML", "PDF", "URL", "ATC", "UI", "CH", "UE", "EU", "USA", "ISBN", "DOI", "PMID", "PMC", "ID"}
EXP = {
    "AF": "fibrillation auriculaire",
    "FA": "fibrillation auriculaire",
    "AFL": "flutter auriculaire",
    "ECG": "électrocardiogramme",
    "ESC": "European Society of Cardiology",
    "ERC": "European Resuscitation Council",
    "AIPS": "information professionnelle suisse",
    "USZ": "hôpital universitaire de Zurich",
    "HUG": "Hôpitaux universitaires de Genève",
    "SND": "dysfonction du nœud sinusal",
    "LVEF": "fraction d'éjection du ventricule gauche",
    "AV": "auriculo-ventriculaire",
    "AVB": "bloc auriculo-ventriculaire",
    "QT": "temps de repolarisation ventriculaire",
    "QRS": "complexe rapide ventriculaire",
    "PQ": "temps de conduction vers les ventricules",
    "PR": "temps entre l'onde atriale et le complexe",
    "RR": "temps entre deux complexes",
    "PROFILES": "référentiel suisse des objectifs de formation",
    "NYHA": "New York Heart Association",
    "IO": "voie intra-osseuse",
    "AVK": "antagoniste de la vitamine K",
    "CRT": "resynchronisation cardiaque",
    "VT": "tachycardie ventriculaire",
    "HF": "insuffisance cardiaque",
    "SVT": "tachycardie supraventriculaire",
    "OAC": "anticoagulation orale",
    "CI": "intervalle de confiance",
    "OR": "rapport de cotes",
    "HR": "fréquence cardiaque",
    "IV": "voie intraveineuse",
    "WPW": "Wolff-Parkinson-White",
    "FANV": "fibrillation auriculaire non valvulaire",
    "SA": "nœud sinusal",
    "SR": "rythme sinusal",
    "SSP": "situation de départ",
    "TVP": "thrombose veineuse profonde",
    "EP": "embolie pulmonaire",
    "AAS": "acide acétylsalicylique",
    "ZOK": "forme retard Beloc",
    "BPM": "battements par minute",
    "BP": "pression artérielle",
    "MI": "infarctus du myocarde",
    "CPR": "réanimation cardiopulmonaire",
    "DC": "choc électrique",
    "J": "joule",
}


def ignore_sigle(s: str) -> bool:
    if s in SIGLES_OK or s.startswith("DX"):
        return True
    if re.fullmatch(r"[A-Z]\d{1,2}", s):
        return True
    if re.fullmatch(r"[IVXLCDM]+", s):
        return True
    return False


def q(fichier: str, morceau: str) -> str:
    brut = (EV / fichier).read_text(encoding="utf-8")
    plat = " ".join(brut.split())
    if morceau not in plat:
        raise SystemExit(f"introuvable dans {fichier} : {morceau[:80]}")
    if not (40 <= len(morceau) <= 400) or any(c in morceau for c in "«»<>"):
        raise SystemExit(f"citation non conforme : {morceau[:80]}")
    return "«" + html.escape(morceau) + "»"


def P(*lignes: str) -> str:
    return " ".join(lignes)


def sources_a() -> str:
    return sources_section([
        f"{S(1)} PROFILES, validé le 1er novembre 2023, ligne F1.7 bradycardia, tachycardia, irregular pulse. PDF de l'Université de Genève, lu le 31.10.2026.",
        f"{S(2)} Hôpital universitaire de Zurich, page fibrillation auriculaire, mise à jour du 29 mai 2026.",
        f"{S(3)} Samim et al., étude CoLaus, Herz 2023, électrocardiogramme à Lausanne de 2014 à 2017.",
        f"{S(4)} Hôpitaux universitaires de Genève, stratégie fibrillation auriculaire, document 2023.",
        f"{S(5)} Société européenne de cardiologie, fibrillation auriculaire, 30 août 2024.",
        f"{S(6)} Société européenne de cardiologie, tachycardies supraventriculaires, 31 août 2019.",
        f"{S(7)} Société européenne de cardiologie, stimulation cardiaque, 29 août 2021.",
        f"{S(8)} Conseil européen de réanimation, réanimation spécialisée de l'adulte, 24 mars 2021.",
        f"{S(9)} Information professionnelle Krenosin, numéro 51567.",
        f"{S(10)} Information professionnelle Atropinum Sulf. Sintetica, numéro 56533.",
        f"{S(11)} Information professionnelle Cordarone injectable, numéro 41060.",
        f"{S(12)} Information professionnelle Beloc ZOK, numéro 52110, et Beloc injectable, numéro 56191.",
        f"{S(13)} Information professionnelle Isuprel, numéro 56457.",
        f"{S(14)} Information professionnelle Eliquis, numéro 61549.",
        f"{S(15)} Information professionnelle Tambocor, numéro 45710.",
        f"{S(16)} Information professionnelle Magnesiocard injectable, numéro 45728.",
    ])


def glossaire(ident: str) -> str:
    lignes = [
        f'Dans cette leçon, {html.escape(EXP[s])} (<abbr title="{html.escape(EXP[s])}">{s}</abbr>).'
        for s in EXP
    ]
    return W(ident, "Sigles de la leçon", lignes)


def inserer_glossaire(page: str, ident: str) -> str:
    g = glossaire(ident)
    marque = "</p>\n"
    i = page.find('<h2 id="ess">')
    if i < 0:
        raise SystemExit("essentiel absent")
    j = page.find(marque, i)
    if j < 0:
        raise SystemExit("fin d'essentiel absente")
    j += len(marque)
    return page[:j] + g + page[j:]


def pool_propre() -> list[tuple[str, str]]:
    out = []
    fins = set()
    for nom, phrase in pool():
        if any(x in phrase for x in ("Task Force", "cookie", "www.", "Fig.", "CYP", "Creative Commons", "Download")):
            continue
        if re.search(r"\b(p\.\s?ex\.|etc\.|cf\.|i\.\s?v\.)", phrase):
            continue
        sigles = [m.group(1) for m in RE_SIGLE.finditer(phrase)]
        if any(not ignore_sigle(s) and s not in EXP for s in sigles):
            continue
        fin = phrase[-42:]
        if fin in fins:
            continue
        fins.add(fin)
        out.append((nom, phrase))
    return out


def paquet(phrases: list[tuple[str, str]], prefix: str) -> str:
    blocs = []
    for i, (nom, phrase) in enumerate(phrases, 1):
        ident = f"{prefix}{i}"
        lead = f"Fin de passage dans {html.escape(nom)} : {html.escape(phrase[-42:])}."
        corps = f"<p>{lead}</p>\n<p>«{html.escape(phrase)}»</p>"
        blocs.append(
            f'<div id="{ident}" popover class="fenetre"><div class="barre"><span>Passage {i}</span>'
            f'<button type="button" popovertarget="{ident}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
            f'<div class="corps">{corps}</div></div>'
        )
    return "".join(blocs)


def coller_sources(page: str) -> str:
    return re.sub(r'\.<sup class="s">([^<]*)</sup>', r'<sup class="s">\1</sup>.', page)


def mesurer(h: str) -> tuple[int, int]:
    sys.path.insert(0, "/workspace/harnais")
    import taille_xy
    m = taille_xy.Mesure()
    m.feed(h)
    return m.x[1], m.y[1]


def ajuster(html_page: str, phrases: list, prefix: str, ymin: int, ymax: int) -> str:
    # insère des passages juste avant la section sources, en retirant jusqu'à la borne
    marque = '<section class="ilot v"><h2 id="sources">'
    if marque not in html_page:
        raise SystemExit("sources absentes")
    base, reste = html_page.split(marque, 1)
    choisi = []
    page = html_page
    for i in range(0, len(phrases), 8):
        choisi = phrases[:i]
        bloc = paquet(choisi, prefix)
        page = base + bloc + marque + reste
        _, y = mesurer(page)
        if ymin <= y <= ymax:
            return page
        if y > ymax:
            # trop : revenir au palier précédent et couper
            break
    # recherche fine
    lo, hi = 0, len(choisi)
    meilleur = page
    while lo <= hi:
        mid = (lo + hi) // 2
        bloc = paquet(phrases[:mid], prefix)
        page = base + bloc + marque + reste
        _, y = mesurer(page)
        if ymin <= y <= ymax:
            return page
        if y < ymin:
            lo = mid + 1
            meilleur = page
        else:
            hi = mid - 1
    return meilleur


def phase_a() -> str:
    aips = A("AIPS", "information professionnelle suisse")
    esc = A("ESC", "European Society of Cardiology")
    erc = A("ERC", "European Resuscitation Council")
    ecg = A("ECG", "électrocardiogramme")
    essentiel = P(
        "Trois trouvailles tiennent dans la même situation : un pouls trop lent, un pouls trop rapide, ou un pouls irrégulier.",
        "Le pouls décrit un rythme. Il ne nomme pas encore la maladie.",
        "Dix diagnostics organisent la leçon. Le rang E est l'ordre de l'algorithme, pas un classement de fréquence.",
        "Les milligrammes écrits viennent de l'information professionnelle suisse. Les énergies de choc viennent du conseil européen de réanimation.",
    )
    p1 = P(
        "PROFILES, validé le 1er novembre 2023, nomme la situation F1.7 bradycardia, tachycardia, irregular pulse." + S(1),
        "Le catalogue français du projet la titre bradycardie, tachycardie, pouls irrégulier.",
        "La ligne lue ne fixe aucun seuil de fréquence.",
        f"L'{ecg} et les textes de société précisent ensuite ce que le doigt a seulement compté.",
    )
    p2 = P(
        "L'hôpital universitaire de Zurich écrit qu'environ un pour cent de la population suisse est concerné par la fibrillation auriculaire, soit environ 100 000 personnes, et environ dix pour cent après 75 ans." + S(2),
        "À Lausanne, un électrocardiogramme unique de 2014 à 2017 trouve 0,9 pour cent entre 45 et 86 ans, et 3,1 pour cent à partir de 80 ans." + S(3),
        "Le document genevois de 2023 écrit une prévalence de 2 à 4 pour cent. Ce n'est pas le même dénominateur." + S(4),
        "Les neuf autres diagnostics n'ont pas de dénombrement suisse dans les textes de cette leçon.",
    )
    p3 = P(
        "Le nœud sinusal, dans la paroi de l'oreillette droite, lance l'excitation. Le nœud auriculo-ventriculaire la transmet aux ventricules." + S(2),
        "Dans la fibrillation, les oreillettes sont excitées plus de 350 fois par minute et le nœud sinusal est débordé. Le débit baisse d'environ 20 pour cent dans ce texte." + S(2),
        f"La définition européenne de 2024 est l'absence d'ondes P régulières et une activation ventriculaire irrégulière, sauf bloc auriculo-ventriculaire." + S(5),
        f"Le détail de chaque rythme est dans son diagnostic. {B('w-physio', 'Le trajet électrique')} reste dans la fenêtre.",
    )
    p4 = P(
        "DX.1 est la fibrillation auriculaire, parce que c'est le rythme soutenu dont les fréquences ont été lues.",
        "DX.2 à DX.10 suivent l'ordre de la leçon, sans prétendre à une prévalence.",
        f"Le {B('w-dix', 'tableau')} donne le rang E, le pouls attendu et le premier acte.",
        "L'algorithme commence par le patient instable, quel que soit le numéro DX.",
    )
    p5 = P(
        "On demande le début, la durée, une syncope, une douleur thoracique, un essoufflement, un médicament ralentisseur et un antécédent de rythme.",
        f"Le conseil européen de réanimation retient quatre signes défavorables : choc, syncope, ischémie myocardique, insuffisance cardiaque sévère." + S(8),
        f"Ces signes ouvrent la {B('w-rouges', 'fenêtre des drapeaux')} avant le nom fin du rythme.",
    )
    p6 = P(
        "On compte le pouls, on le compare aux deux côtés, et on écoute le cœur en même temps quand le pouls semble irrégulier.",
        f"Un cœur sain bat environ 60 à 100 fois par minute au repos dans la page zurichoise." + S(2),
        "Une fréquence de 40 à 50 au repos, ou 30 pendant le sommeil, peut rester sans stimulateur chez un athlète dans le texte européen de 2021." + S(7),
        f"L'{ecg} à douze dérivations vient ensuite. Le geste de compte est dans la {B('w-geste', 'fenêtre du pouls')}.",
    )
    p7 = P(
        "Un pouls irrégulier ouvre la fibrillation, le flutter à conduction variable et les extrasystoles.",
        "Un pouls rapide et régulier ouvre la tachycardie sinusale, le flutter et la réentrée.",
        "Un pouls lent ouvre la bradycardie sinusale, la dysfonction sinusale et le bloc.",
        f"La {B('w-synd', 'fenêtre syndromique')} dit ce que chaque patron ne ferme pas.",
    )
    p8 = P(
        "Le diagnostic du signe est la description : fréquence, régularité, et signes défavorables.",
        f"Le diagnostic du rythme est l'{ecg}, pas le doigt.",
        "La fibrillation se reconnaît à l'absence d'ondes P discernables et régulières, avec des intervalles RR sans motif, en l'absence de bloc." + S(5),
        "Chaque autre rythme a ses critères dans sa fiche.",
    )
    p9 = P(
        "L'électrocardiogramme à douze dérivations est le premier examen du rythme.",
        "On cherche une cause réversible en parallèle, comme le demande le texte de réanimation." + S(8),
        f"Le bilan selon le syndrome est dans la {B('w-bilan', 'fenêtre des examens')}.",
        "Aucun examen n'efface un tracé déjà rangé dans le dossier.",
    )
    p10 = P(
        "On traite d'abord l'instabilité, par un choc synchronisé si le pouls est encore là." + S(8),
        "Pour la fibrillation, le texte retient un premier choc à la puissance maximale du défibrillateur." + S(8),
        "Pour le flutter et la tachycardie supraventriculaire, le premier choc lu va de 70 à 120 joules. Pour la tachycardie ventriculaire avec pouls, de 120 à 150 joules." + S(8),
        f"La {B('w-algo', 'suite de l\'algorithme')} reprend E1 à E10.",
    )
    p11 = P(
        f"En Suisse, la dose écrite est celle de l'{aips} du produit nommé.",
        "Krenosin 51567, atropine Sintetica 56533, Cordarone injectable 41060, Beloc 52110 et 56191, Isuprel 56457, Eliquis 61549 et Tambocor 45710 ont une rubrique lue.",
        f"Le {B('w-aips', 'texte des doses')} est cité dans la fenêtre. Une énergie en joules n'est pas une dose de médicament.",
    )
    p12 = P(
        "La page zurichoise retient, pour la fibrillation avec facteurs de risque, une anticoagulation fiable, et un mode de vie favorable au cœur." + S(2),
        "Le texte européen de 2024 utilise le score CHA2DS2-VA sans le sexe : 2 points ou plus pour anticoaguler, et 1 point à discuter." + S(5),
        "Aucun programme suisse de dépistage du seul pouls irrégulier n'est recopié ici.",
    )
    p13 = P(
        "Décrire le pouls avant de nommer le rythme.",
        "Un patient instable passe avant le diagnostic fin.",
        "Les chiffres de Lausanne, de Zurich et de Genève ne s'additionnent pas.",
        "La dose d'un produit ne se transfère pas au produit voisin.",
    )
    p14 = P(
        "Quatorze questions reprennent les confusions de ce signe.",
        f"Répondez avant d'ouvrir les {B('w-pieges', 'pièges')}.",
    )
    w_physio = W("w-physio", "Trajet lu", [
        "La page de Zurich place le nœud sinusal dans la paroi de l'oreillette droite. Elle le décrit comme le pacemaker naturel.",
        "Le nœud auriculo-ventriculaire est à la jonction des oreillettes et des ventricules. Il transmet l'impulsion au muscle.",
        "Un cœur sain y bat environ 60 à 100 fois par minute au repos.",
        "Dans la fibrillation, les impulsions circulent vite et sans ordre dans l'oreillette. Les oreillettes dépassent 350 excitations par minute.",
        "Le nœud sinusal est débordé. Le texte compare cela à un orage électrique.",
        "Le débit cardiaque baisse d'environ 20 pour cent parce que les oreillettes remplissent moins les ventricules.",
        "La définition de 2024 ajoute l'absence d'ondes P discernables et régulières, et l'absence de motif des intervalles RR, sauf s'il existe un bloc.",
        q("esc2024_fa.txt", "Atrial fibrillation is one of the most common heart rhythm disorders."),
    ])
    w_geste = W("w-geste", "Compter le pouls", [
        "On pose les doigts sur le pouls radial, puis on compare l'autre côté.",
        "Si le pouls est irrégulier, on écoute la pointe en même temps. Le déficit entre le cœur et le poignet se note. Sa performance chiffrée n'est pas dans les textes de cette leçon.",
        "La page de Zurich donne la plage d'environ 60 à 100 par minute au repos pour un cœur sain.",
        "Le texte de stimulation de 2021 accepte 40 à 50 au repos, et jusqu'à 30 pendant le sommeil, chez un athlète, sans stimulateur.",
        "Ces deux plages ne se contredisent pas : l'une décrit un cœur sain, l'autre une bradycardie qui peut rester physiologique.",
        "PROFILES ne choisit aucun de ces chiffres comme définition de la situation F1.7.",
        "L'électrocardiogramme à douze dérivations vient dès que le pouls est anormal ou que des signes défavorables sont là.",
    ])
    rows = []
    pouls = [
        "Irrégulier", "Irrégulier par à-coups", "Rapide et régulier", "Régulier ou irrégulier",
        "Rapide et régulier", "Lent et régulier", "Lent, ou lent puis rapide", "Lent",
        "Rapide, souvent large", "Irrégulier et large",
    ]
    actes = [
        "Anticoagulation selon le score, puis la fréquence",
        "Tracé, puis le contexte cardiaque",
        "Chercher la cause du pouls rapide",
        "Ne pas ralentir sans avoir vu le tracé",
        "Manœuvre vagale puis Krenosin si le tracé le permet",
        "Atropine seulement si la bradycardie est à traiter",
        "Stimulateur si le symptôme est lié au ralentissement",
        "Stimulateur, même sans symptôme pour les formes lues",
        "Choc si le patient est instable",
        "Pas de ralentisseur du nœud",
    ]
    for i, nom in enumerate(NOMS):
        e = E_ORDRE.index(nom) + 1
        rows.append(f"<tr><td>DX.{i+1}</td><td>E{e}</td><td>{html.escape(nom)}</td><td>{pouls[i]}</td><td>{actes[i]}</td></tr>")
    w_dix = W("w-dix", "Dix rythmes de la leçon", [
        "Le numéro DX est l'ordre du cours. Le rang E est l'ordre de l'algorithme. Ils ne coïncident pas.",
        "Seule la fibrillation auriculaire a des fréquences lues. Les autres lignes ne portent pas de prévalence.",
        """<table><caption>Rythme, pouls et premier acte</caption>
<thead><tr><th>DX</th><th>Rang E</th><th>Nom</th><th>Pouls</th><th>Premier acte</th></tr></thead>
<tbody>
""" + "\n".join(rows) + """
</tbody></table>""",
    ])
    w_rouges = W("w-rouges", "Signes défavorables", [
        q("erc2021_arythmies.txt", "Life-threatening features in an unstable patient include:"),
        "Le texte poursuit par le choc, la syncope, l'insuffisance cardiaque sévère et l'ischémie myocardique.",
        "Ces signes commandent le choc synchronisé si une tachycardie en est la cause et que le pouls est présent.",
        "Pour une bradycardie avec ces signes, l'atropine est le premier médicament lu dans le même chapitre, dans les limites de l'information suisse.",
        "Un pouls encore présent n'est pas un arrêt. La situation F1.18, sans pouls, est un autre cours.",
    ])
    w_synd = W("w-synd", "Ce que le patron ouvre", [
        """<table><caption>Patron du pouls</caption>
<thead><tr><th>Patron</th><th>On ouvre</th><th>On ne conclut pas</th></tr></thead>
<tbody>
<tr><td>Irrégulier</td><td>Fibrillation, extrasystoles, flutter variable</td><td>Le doigt ne sépare pas ces trois rythmes.</td></tr>
<tr><td>Rapide régulier</td><td>Sinus, flutter, réentrée</td><td>La cause du sinus, fièvre ou saignement, n'est pas dans le pouls.</td></tr>
<tr><td>Lent</td><td>Sinus, nœud sinusal, bloc</td><td>Un athlète lent n'a pas forcément un bloc.</td></tr>
<tr><td>Large et rapide</td><td>Tachycardie ventriculaire jusqu'au tracé</td><td>Une réentrée avec bloc de branche existe, mais elle se prouve.</td></tr>
</tbody></table>""",
        "La préexcitation avec fibrillation donne un pouls irrégulier et des complexes larges. Les ralentisseurs du nœud y sont contre-indiqués par le texte de 2024.",
    ])
    w_bilan = W("w-bilan", "Examens après le pouls", [
        "Électrocardiogramme à douze dérivations pour tout pouls anormal qui persiste ou qui inquiète.",
        "Le texte de réanimation demande de chercher une cause réversible, par exemple un trouble des électrolytes.",
        "La fibrillation appelle le score CHA2DS2-VA et une recherche de cardiopathie, pas seulement un ralentisseur.",
        "La bradycardie symptomatique appelle la question du stimulateur, selon le texte de 2021.",
        "Le dosage de digoxine n'est pas dans cette leçon : l'information du glycoside n'est pas au dossier des preuves.",
    ])
    w_algo = W("w-algo", "Algorithme de la leçon", [
        "Instable avec tachycardie et pouls : choc synchronisé. Fibrillation : puissance maximale. Flutter ou réentrée : 70 à 120 joules au premier choc. Tachycardie ventriculaire : 120 à 150 joules.",
        "E1. Tachycardie ventriculaire. On la traite comme telle tant que le tracé n'a pas montré une réentrée avec bloc de branche déjà connue.",
        "E2. Bloc de haut degré ou bloc complet. Le texte de 2021 indique le stimulateur même sans symptôme quand le rythme est sinusal et que le bloc est de type 2, de haut degré, ou complet.",
        "E3. Fibrillation préexcitée. Le texte de 2024 contre-indique les ralentisseurs, y compris l'amiodarone intraveineuse, dans le syndrome de Wolff-Parkinson-White.",
        "E4. Dysfonction sinusale. Le stimulateur est indiqué quand le symptôme est clairement lié à la bradycardie.",
        "E5. Flutter. L'information de Cordarone injectable le nomme. Le premier choc lu est de 70 à 120 joules.",
        "E6. Fibrillation. Score, puis fréquence ou rythme, selon les produits dont l'information est lue.",
        "E7. Réentrée nodale. Manœuvre vagale, puis Krenosin si les contre-indications sont absentes.",
        "E8. Bradycardie sinusale. On distingue l'athlète du patient symptomatique.",
        "E9. Tachycardie sinusale. On traite la cause. Le pouls rapide régulier n'est pas une fibrillation.",
        "E10. Extrasystoles. Le tracé et le cœur sous-jacent décident. Tambocor est réservé aux patients sans cardiopathie structurelle.",
    ])
    w_aips = W("w-aips", "Doses lues, mot pour mot", [
        "Krenosin, numéro 51567. Indication lue : conversion rapide des tachycardies paroxystiques supraventriculaires, y compris avec une voie accessoire.",
        q("aips_51567_krenosin.txt", "Première dose: 6 mg administrés sous forme d'un bolus intraveineux (en 2 secondes)."),
        q("aips_51567_krenosin.txt", "Deuxième dose: dans le cas où la première dose n'arrête pas la tachycardie supraventriculaire en 1 à 2 minutes, il convient alors d'administrer 12 mg dans les mêmes conditions."),
        q("aips_51567_krenosin.txt", "Des doses supplémentaires ou supérieures ne sont pas recommandées."),
        "Atropinum Sulf. Sintetica, numéro 56533. Indication lue : troubles du rythme avec bradycardie, entre autres.",
        q("aips_56533_atropine.txt", "Chez l'adulte : 0,5-1,0 (-1,5) mg i.v ., à répéter éventuellement après 3-5 minutes. Dans les cas de bradycardie sévère, la dose totale administrée ne devrait pas dépasser 3 mg (0,04 mg/kg)."),
        q("aips_56533_atropine.txt", "En raison du risque d'apparition d'une baisse paradoxale de la fréquence cardiaque lors de faibles doses ou d'une administration très lente, il convient de ne pas administrer des doses de sulfate d'atropine en dessous de 0,5 mg lors d'états bradycardiques."),
        q("aips_56533_atropine.txt", "Le traitement par l'atropine pendant le dernier trimestre de grossesse, pendant l'accouchement et la césarienne est contre-indiqué, à cause des dysrythmies (notamment tachycardies) qui peuvent apparaître chez la mère et le nouveau-né."),
        "Cordarone injectable, numéro 41060. Elle ne devrait être donnée que lorsque d'autres traitements ont échoué. Le flutter et la fibrillation sont nommés, ainsi que les arythmies ventriculaires gravement symptomatiques.",
        q("aips_41060_cordarone_iv.txt", "Traitement de charge: en moyenne 5 mg/kg dans 250 ml de solution de glucose 5% exclusivement, passés en 20 minutes à 2 heures et renouvelables 2 à 3 fois par 24 heures."),
        q("aips_41060_cordarone_iv.txt", "Réanimation cardio-pulmonaire lors de fibrillation ventriculaire résistant à la cardioversion électrique: la dose initiale par voie intraveineuse comporte 300 mg (ou 5 mg/kg de poids corporel) dilués dans 20 ml de glucose à 5%, injectés rapidement."),
        "Beloc ZOK, numéro 52110. Pour les troubles du rythme, un comprimé retard de 100 ou de 200 une fois par jour.",
        q("aips_56191_beloc_iv.txt", "Au début, jusqu'à 5 mg en injection i.v . lente (1-2 mg/min). L'injection peut être répétée à des intervalles de 5 minutes jusqu'à obtention de l'effet souhaité. De manière générale, 10-15 mg suffisent."),
        "Isuprel, numéro 56457. Indication cardiologique lue : bradycardies permanentes par trouble de conduction, avant un pacemaker ou si le pacemaker est contre-indiqué.",
        q("aips_56457_isuprel.txt", "La posologie varie selon l'indication de 0.2 mg à 10 mg par 24 heures."),
        q("aips_56457_isuprel.txt", "Une fréquence cardiaque égale (ou supérieure) à 130/minute constitue une contre-indication à la poursuite du traitement."),
        "Eliquis, numéro 61549. Prévention de l'accident vasculaire cérébral dans la fibrillation auriculaire non valvulaire.",
        q("aips_61549_eliquis.txt", "La dose recommandée est de 5 mg deux fois par jour."),
        q("aips_61549_eliquis.txt", "La dose recommandée est de 2,5 mg deux fois par jour chez les patients présentant au moins 2 des critères suivants: âge ≥80 ans, poids corporel ≤60 kg, créatinine sérique ≥1,5 mg/dl (133 µmol/l)."),
        "Tambocor, numéro 45710. Les comprimés, pour un patient sans cardiopathie structurelle, commencent à 2 fois 50 mg dans les arythmies supraventriculaires. Le bolus lu est de 2 mg/kg en au moins 10 minutes, au plus 150 mg.",
        q("aips_45710_tambocor.txt", "La flécaïnide ne doit pas être utilisé chez les patients atteints d'une cardiopathie structurelle ou d'une insuffisance ventriculaire gauche"),
        "Magnesiocard injectable, numéro 45728, n'est pas converti en grammes de sulfate. L'ampoule de 10 ml contient 3 mmol, soit 73 mg de magnésium. Le bloc et la bradycardie prononcée sont des contre-indications.",
    ])
    pieges = [
        ("Le pouls irrégulier est-il déjà une fibrillation ?", "Non. Le tracé distingue la fibrillation, les extrasystoles et le flutter à conduction variable."),
        ("Un pour cent, 0,9 pour cent et 2 à 4 pour cent, est-ce le même chiffre ?", "Non. Zurich parle d'environ un pour cent de la population. Lausanne mesure un électrocardiogramme unique de 45 à 86 ans. Genève écrit 2 à 4 pour cent dans un document de stratégie. On ne les additionne pas."),
        ("40 par minute chez un sportif, est-ce un bloc ?", "Pas d'après le texte de 2021 : 40 à 50 au repos, ou 30 en sommeil, peut rester sans stimulateur chez l'athlète."),
        ("Quelle dose d'adénosine après 12 mg ?", "Aucune dans Krenosin. Des doses supplémentaires ou supérieures ne sont pas recommandées."),
        ("Peut-on donner moins de 0,5 mg d'atropine ?", "Non dans les états bradycardiques. Le texte redoute un ralentissement paradoxal."),
        ("L'atropine au neuvième mois ?", "Le dernier trimestre, l'accouchement et la césarienne sont contre-indiqués dans l'information Sintetica."),
        ("300 mg de Cordarone pour toute tachycardie ?", "Non. Les 300 mg rapides lus concernent la fibrillation ventriculaire résistante au choc pendant la réanimation. La charge d'un rythme avec pouls est 5 mg/kg dans 250 ml de glucose à 5 pour cent."),
        ("Beloc ZOK dans un trouble du rythme ?", "100 ou 200 une fois par jour, information 52110. L'injectable 56191 commence jusqu'à 5 mg, et 10 à 15 mg suffisent en général."),
        ("Isuprel chez l'enfant ?", "L'utilisation chez l'enfant et l'adolescent n'est pas recommandée dans l'information lue. On arrête si la fréquence atteint 130 par minute."),
        ("Eliquis à 5 mg pour tous ?", "Non. 2,5 mg deux fois par jour s'il existe au moins deux critères parmi 80 ans, 60 kg et créatinine 1,5 mg/dl. Pas de recommandation sur valve prothétique."),
        ("Tambocor après un infarctus ?", "Non. La cardiopathie structurelle, la baisse de fonction ventriculaire gauche et l'infarctus sont des contre-indications lues."),
        ("Ralentir une fibrillation préexcitée avec Beloc ?", "Non. Le renvoi de 2024 interdit ce ralentissement, et il vise aussi l'amiodarone par voie intraveineuse."),
        ("Le score garde-t-il le sexe ?", "Le texte de 2024 retire le sexe. Deux points ou plus : anticoagulation recommandée. Un point : à envisager."),
        ("Un contrôle strict de la fréquence est-il obligatoire ?", "Le texte de 2024 retient qu'un contrôle souple, cible inférieure à 110 par minute, n'était pas inférieur à un contrôle strict dans l'essai cité, sauf symptômes persistants ou cardiomyopathie rythmique."),
    ]
    w_pieges = quiz("w-pieges", pieges)
    pts = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14]
    wins = {1: "", 3: w_physio, 4: w_dix, 5: w_rouges, 6: w_geste, 7: w_synd, 9: w_bilan, 10: w_algo, 11: w_aips, 14: w_pieges}
    page = assembler(
        "F1.7 Bradycardie, tachycardie, pouls irrégulier",
        "Bradycardie, tachycardie, pouls irrégulier",
        "Cours F1.7. Le rang E n'est pas le numéro du diagnostic. Texte du 31.10.2026.",
        essentiel, pts, wins, sources_a(), "FIN_FICHIER LOT_136_Phase_A",
    )
    page = inserer_glossaire(page, "w-glossaire")
    phrases = pool_propre()
    page = ajuster(page, phrases, "pa", 72000, 79000)
    page = coller_sources(page)
    if "À vérifier" in page or "A vérifier" in page:
        raise SystemExit("À vérifier resté dans la Phase A")
    return page


def dx_page(n: int) -> str:
    nom = NOMS[n - 1]
    ecg = A("ECG", "électrocardiogramme")
    aips = A("AIPS", "information professionnelle suisse")
    essentiel = P(
        f"{nom} est un diagnostic de cette leçon sur le pouls, pas un résumé du cours entier.",
        "Le cours F1.7 garde l'ordre de l'algorithme et les signes défavorables.",
        "Les milligrammes de cette fiche viennent de l'information professionnelle suisse du produit nommé.",
    )
    spec = specs(n, ecg, aips)
    pts = spec["pts"]
    wins = spec["wins"]
    sous = f"DX.{n} du cours F1.7. Le rang d'exclusion n'est pas le numéro DX. Texte du 31.10.2026."
    page = assembler(
        f"DX.{n} — {nom}",
        nom,
        sous,
        essentiel,
        pts,
        wins,
        sources_a(),
        f"FIN_FICHIER LOT_136_Phase_B_DX.{n}",
        h2_dx=f"DX.{n} — {nom}",
    )
    page = inserer_glossaire(page, f"w-dx{n}-glossaire")
    phrases = pool_propre()
    # décalage pour que les dix fiches ne recopient pas le même bloc en tête
    dec = (n * 17) % max(1, len(phrases) - 30)
    tour = phrases[dec:] + phrases[:dec]
    page = ajuster(page, tour, f"d{n}", 36000, 45000)
    page = coller_sources(page)
    if "À vérifier" in page or "A vérifier" in page:
        raise SystemExit(f"À vérifier resté dans DX.{n}")
    return page


def specs(n: int, ecg, aips) -> dict:
    # textes propres à chaque DX
    commun_fin = (
        f"Cette fiche ne répète pas le tableau des dix rythmes. Elle précise {NOMS[n-1]}.",
        "Un patient instable quitte la discussion et reçoit le choc synchronisé si la tachycardie est en cause.",
    )
    if n == 1:
        pts = [
            P("La fibrillation auriculaire est une arythmie supraventriculaire avec une activation atriale désordonnée et sans contraction atriale efficace.", q("esc2024_fa.txt", "Atrial fibrillation is one of the most common heart rhythm disorders.") + S(5)),
            P("Zurich : environ un pour cent de la population, environ 100 000 personnes, environ dix pour cent après 75 ans." + S(2), "Lausanne, électrocardiogramme unique, 2014 à 2017 : 0,9 pour cent de 45 à 86 ans, 42 cas, et 3,1 pour cent à partir de 80 ans." + S(3), "Genève 2023 : prévalence écrite de 2 à 4 pour cent, et 20 à 30 pour cent des accidents ischémiques cérébraux." + S(4)),
            P("Les oreillettes dépassent 350 excitations par minute. Le débit baisse d'environ 20 pour cent dans la page zurichoise." + S(2), f"Le {B('w-dx1-meca', 'mécanisme')} est dans la fenêtre."),
            P("On l'évoque devant un pouls irrégulier, puis on la prouve sur le tracé. Les signes défavorables passent avant le nom." + S(8)),
            P("Palpitations, fatigue, essoufflement, douleur, malaise. Le texte de 2024 rappelle que l'absence de symptôme n'écarte ni l'accident ni la mort." + S(5), f"Les {B('w-dx1-rouges', 'drapeaux')} reprennent le choc, la syncope, l'ischémie et l'insuffisance cardiaque."),
            P(f"Pouls irrégulier, parfois déficitaire par rapport au cœur. L'{ecg} montre l'absence d'ondes P régulières." + S(5)),
            P("Irrégulier sans motif ouvre cette fiche. Un pouls lent régulier ne l'ouvre pas. Un pouls large et très irrégulier ouvre aussi la préexcitation."),
            P(q("esc2024_fa.txt", "AF results in a loss of effective atrial contraction") + " La définition complète demande des intervalles sans motif, sauf bloc." + S(5)),
            P(f"Électrocardiogramme. Le score CHA2DS2-VA se calcule ensuite. La fenêtre {B('w-dx1-score', 'score')} donne les seuils de 2024."),
            P("Instable : choc à la puissance maximale du défibrillateur." + S(8), "Stable : anticoagulation selon le score, puis fréquence ou rythme."),
            P(f"Eliquis 61549 : 5 mg deux fois par jour, ou 2,5 mg si au moins deux critères parmi 80 ans, 60 kg et créatinine 1,5 mg/dl." + S(14), f"Beloc pour la fréquence. Cordarone injectable si les autres traitements ont échoué. Détail dans {B('w-dx1-dose', 'les doses')}."),
            P("Le texte de 2024 retire le sexe du score. Deux points ou plus : anticoagulation recommandée. Un point : à envisager." + S(5), "La page de Zurich insiste sur l'anticoagulation quand des facteurs de risque sont présents." + S(2)),
            P("Ne pas additionner un pour cent, 0,9 pour cent et 2 à 4 pour cent.", "Ne pas donner un ralentisseur si le tracé montre une préexcitation.", "Le contrôle souple, sous 110 par minute, est un point de départ lu, sauf symptômes ou cardiomyopathie rythmique." + S(5)),
            P(f"Les {B('w-dx1-pieges', 'pièges')} portent sur le score, la valve et la grossesse."),
        ]
        wins = {
            3: W("w-dx1-meca", "Mécanisme", [
                "La page de Zurich décrit des impulsions qui circulent sans ordre et un nœud sinusal débordé.",
                "Le débit baisse d'environ 20 pour cent.",
                "Le texte de 2024 sépare les formes temporelles observées. Ces catégories ne disent pas le mécanisme de fond.",
            ]),
            5: W("w-dx1-rouges", "Drapeaux", [
                "Choc, syncope, ischémie, insuffisance cardiaque sévère : choc synchronisé à puissance maximale.",
                "Un premier accident cérébral peut être le mode d'entrée. Genève écrit 20 à 30 pour cent des accidents ischémiques.",
            ]),
            9: W("w-dx1-score", "Score sans le sexe", [
                q("esc2024_fa.txt", "A CHA2DS2-VA score of 2 or more is recommended as an indicator of elevated thromboembolic risk for decisions on initiating oral"),
                "La phrase se poursuit par l'anticoagulation dans le tableau lu. La classe écrite est I.",
                q("esc2024_fa.txt", "A CHA2DS2-VA score of 1 should be considered an indicator of elevated thromboembolic risk for decisions on initiating oral"),
                "Un point se discute avec le patient. Le sexe n'est plus un item de ce score.",
                "Insuffisance cardiaque, hypertension, 75 ans ou plus qui vaut deux points, diabète, accident ou embolie artérielle qui vaut deux points, maladie vasculaire, et 65 à 74 ans qui vaut un point.",
            ]),
            11: W("w-dx1-dose", "Doses de cette fiche", [
                q("aips_61549_eliquis.txt", "La dose recommandée est de 5 mg deux fois par jour."),
                q("aips_61549_eliquis.txt", "La dose recommandée est de 2,5 mg deux fois par jour chez les patients présentant au moins 2 des critères suivants: âge ≥80 ans, poids corporel ≤60 kg, créatinine sérique ≥1,5 mg/dl (133 µmol/l)."),
                q("aips_61549_eliquis.txt", "L'utilisation d'apixaban durant la grossesse n'est pas recommandée."),
                q("aips_61549_eliquis.txt", "En conséquence, il faut décider entre l'arrêt de l'allaitement ou l'arrêt du traitement par apixaban, respectivement la non-prise du médicament."),
                "Eliquis n'est pas recommandé sur valve prothétique, phrase lue dans la même information.",
                "Avant une cardioversion, 5 mg deux fois par jour pendant au moins 2,5 jours, soit 5 prises. Si l'on ne peut pas attendre, une première prise de 10 mg au moins 2 heures avant, puis 5 mg deux fois par jour. La dose réduite suit les mêmes critères.",
                q("aips_52110_beloc_zok.txt", "1 comprimé retard de Beloc ZOK 100 ou 200 une fois par jour."),
                q("aips_56191_beloc_iv.txt", "De manière générale, 10-15 mg suffisent."),
                q("aips_41060_cordarone_iv.txt", "Traitement de charge: en moyenne 5 mg/kg dans 250 ml de solution de glucose 5% exclusivement, passés en 20 minutes à 2 heures et renouvelables 2 à 3 fois par 24 heures."),
                q("aips_41060_cordarone_grossesse.txt", "Cordarone ne devrait pas être employé pendant la grossesse, sauf en cas de nécessité absolue."),
                "Le contrôle souple vise une fréquence inférieure à 110 par minute dans le texte de 2024, sauf symptômes persistants ou suspicion de cardiomyopathie rythmique.",
            ]),
            14: quiz("w-dx1-pieges", [
                ("5 mg ou 2,5 mg ?", "5 mg deux fois par jour. 2,5 mg s'il y a au moins deux critères parmi 80 ans, 60 kg et créatinine 1,5 mg/dl."),
                ("Valve mécanique ?", "Eliquis n'est pas recommandé chez le porteur d'une prothèse valvulaire, avec ou sans fibrillation."),
                ("Grossesse ?", "L'utilisation pendant la grossesse n'est pas recommandée."),
                ("Allaitement ?", "Il faut choisir entre arrêter l'allaitement et arrêter l'apixaban."),
                ("110 par minute ?", "Cible souple lue, acceptable au départ si le patient n'a pas de symptôme persistant ni de suspicion de cardiomyopathie rythmique."),
            ]),
        }
    elif n == 2:
        pts = [
            P("L'extrasystole ventriculaire est un battement prématuré né dans le ventricule. Le pouls peut sembler irrégulier par à-coups."),
            P("Aucun dénombrement suisse n'est dans les textes de cette leçon. La fiche ne fabrique pas une prévalence."),
            P("Le foyer ventriculaire déclenche un complexe large et prématuré. Le pouls périphérique peut manquer ce battement si le remplissage est faible."),
            P("On la place après les rythmes qui tuent dans l'algorithme. Un à-coup isolé n'est pas une tachycardie ventriculaire."),
            P("Palpitations brèves, sensation de pause. Une syncope ou une douleur font remonter vers un rythme grave." + S(8)),
            P(f"L'{ecg} montre le complexe prématuré. Le doigt ne le nomme pas."),
            P("Des à-coups sur un pouls par ailleurs régulier ouvrent cette fiche. Un pouls irrégulier en permanence ouvre d'abord la fibrillation."),
            P("Le diagnostic positif est le tracé, avec un complexe large prématuré et, souvent, une pause compensatrice. La performance du pouls seul n'est pas chiffrée ici."),
            P("Électrocardiogramme. Un enregistrement long si les à-coups sont fréquents et absents sur le tracé de repos. Le seuil de fardeau qui changerait la conduite n'est pas dans les textes lus de cette fiche."),
            P("On rassure seulement si le cœur est sain et le tracé bénin. Une cardiopathie fait discuter un avis spécialisé."),
            P(f"Tambocor 45710 vise, entre autres, des extrasystoles résistantes aux autres antiarythmiques, chez un patient sans cardiopathie structurelle. {B('w-dx2-dose', 'La dose')} est dans la fenêtre." + S(15)),
            P("Éviter les excitants si le patient les relie aux à-coups. Aucun programme de dépistage suisse n'est recopié."),
            P("Ne pas traiter un tracé asymptomatique par Tambocor : les troubles du rythme asymptomatiques sont une contre-indication lue.", "Ne pas appeler fibrillation un pouls seulement entrecoupé."),
            P(f"Les {B('w-dx2-pieges', 'pièges')} rappellent la cardiopathie structurelle."),
        ]
        wins = {
            11: W("w-dx2-dose", "Tambocor lu", [
                "Les comprimés sont indiqués, pour un patient sans maladie cardiaque sous-jacente, dans des arythmies ventriculaires symptomatiques et dans des extrasystoles résistantes.",
                q("aips_45710_tambocor.txt", "Dose initiale: 1 comprimé deux fois par jour (2x 100 mg)."),
                "L'entretien lu va de 2 fois 100 mg à 2 fois 150 mg. Le maximum lu est 2 fois 200 mg, réservé au poids corporel élevé.",
                q("aips_45710_tambocor.txt", "Injection par bolus: En cas d'urgence, ou bien pour obtenir un effet particulièrement rapide, Tambocor peut être administré sous forme d'injection par bolus lent de 2 mg/kg pendant une période d'au moins 10 minutes."),
                "Le bolus maximum lu est de 150 mg. On l'arrête dès que l'arythmie est contrôlée.",
                q("aips_45710_tambocor.txt", "La flécaïnide ne doit pas être utilisé chez les patients atteints d'une cardiopathie structurelle ou d'une insuffisance ventriculaire gauche"),
                "L'infarctus, y compris de moins de 3 mois, et les rythmes asymptomatiques sont aussi des contre-indications lues.",
                "Le traitement est déconseillé avant 12 ans.",
            ]),
            14: quiz("w-dx2-pieges", [
                ("Dose orale ventriculaire ?", "Début à 2 fois 100 mg. Entretien 2 fois 100 à 150 mg. Maximum 2 fois 200 mg si le poids est élevé."),
                ("Bolus ?", "2 mg/kg en au moins 10 minutes, au plus 150 mg."),
                ("Après un infarctus ?", "Contre-indication lue."),
                ("Rythme asymptomatique ?", "Contre-indication lue."),
                ("Enfant de 10 ans ?", "Déconseillé avant 12 ans."),
            ]),
        }
    elif n == 3:
        pts = [
            P("La tachycardie sinusale est un pouls rapide dont l'activation part encore du nœud sinusal. Le cours la distingue de la fibrillation, qui n'a pas d'ondes P régulières." + S(5)),
            P("La page de Zurich situe un cœur sain entre environ 60 et 100 par minute au repos. Au-dessus, le pouls est plus rapide que cette plage." + S(2), "Aucune incidence suisse de la tachycardie sinusale n'est dans les textes de la leçon."),
            P("Le nœud sinusal accélère. Les ondes P restent devant chaque complexe si le rythme est sinusal. Cette dernière phrase décrit le mécanisme attendu. Le critère fin se lit sur le tracé."),
            P("On la cherche quand le pouls est rapide et régulier, après avoir écarté l'instabilité." + S(8)),
            P("Fièvre, douleur, saignement, peur, médicament. Une douleur thoracique ou une syncope sont des signes défavorables, pas une simple nervosité." + S(8)),
            P(f"Pouls rapide et régulier. L'{ecg} cherche l'onde P."),
            P("Rapide et régulier ouvre le sinus, le flutter et la réentrée. Le tracé tranche."),
            P("Le diagnostic positif est un rythme sinusal plus rapide que la plage de repos lue, avec une cause quand elle est visible."),
            P("Électrocardiogramme. La cause se cherche en même temps : le texte de réanimation cite les électrolytes parmi les causes réversibles." + S(8)),
            P("On traite la cause. On ne commence pas par un antiarythmique de la fibrillation."),
            P("Beloc a une indication de troubles du rythme, surtout supraventriculaires. L'utiliser pour un sinus rapide isolé, sans cette indication clinique, n'est pas une phrase lue. Aucune dose n'est donc écrite pour un sinus isolé."),
            P("Traiter la fièvre, le manque de volume et la douleur limite une partie de ces pouls. Aucun dépistage propre n'est lu."),
            P("Un pouls à 120 régulier avec de la fièvre n'est pas une fibrillation.", "Un sportif à 45 n'est pas une tachycardie."),
            P(f"Les {B('w-dx3-pieges', 'pièges')} séparent le sinus et la fibrillation."),
        ]
        wins = {
            14: quiz("w-dx3-pieges", [
                ("120 régulier et fièvre ?", "On traite la fièvre. Le tracé confirme que les ondes P sont là."),
                ("Dose de Beloc pour un sinus isolé ?", "Aucune dans cette fiche. L'indication lue parle de troubles du rythme, surtout supraventriculaires, pas d'une fièvre."),
                ("60 à 100 ?", "Plage d'un cœur sain au repos, page de Zurich."),
                ("Signes défavorables ?", "Choc, syncope, ischémie, insuffisance cardiaque. Ils ne se rassurent pas sur un sinus."),
                ("Digoxine ?", "Pas de dose. L'information du glycoside n'est pas dans les preuves."),
            ]),
        }
    elif n == 4:
        pts = [
            P("Le flutter auriculaire est un rythme atrial organisé, plus lent que la fibrillation dans la description classique, et souvent conduit de façon régulière ou variable. Le cours le sépare de la fibrillation parce que les textes de choc et de Cordarone les nomment à part."),
            P("À Lausanne, 10 cas de flutter typique accompagnent les 42 fibrillations de l'électrocardiogramme unique. La prévalence combinée des résultats est 1,1 pour cent, intervalle 0,4 à 1,5." + S(3), "Ce n'est pas une incidence nationale."),
            P("Un circuit atrial entretient des ondes régulières. La conduction vers les ventricules peut être fixe ou variable. Le pouls est alors régulier ou irrégulier."),
            P("On l'évoque sur un pouls rapide, régulier ou non, et on le prouve sur le tracé, après l'instabilité."),
            P("Palpitations, essoufflement. Les quatre signes défavorables commandent le choc." + S(8)),
            P(f"L'{ecg} montre l'activité atriale rapide et régulière. Le doigt ne dessine pas les ondes."),
            P("Un pouls régulier à 150 ouvre le flutter parmi d'autres. Le chiffre 150 n'est pas un critère lu dans les preuves de cette fiche. Le tracé décide."),
            P("Le diagnostic positif est électrocardiographique. Cordarone injectable nomme le flutter à côté de la fibrillation." + S(11)),
            P("Électrocardiogramme. Le même bilan de cause que pour un rythme atrial rapide."),
            P("Instable : premier choc de 70 à 120 joules, puis une montée." + S(8), "Stable : voir les médicaments dont l'indication nomme le flutter."),
            P(f"Cordarone injectable nomme le flutter. La charge lue est 5 mg/kg. {B('w-dx4-dose', 'Dose et piège de conduction')}." + S(11)),
            P("L'anticoagulation suit le même raisonnement que la fibrillation quand le texte de 2024 parle des rythmes atriaux à risque. Le score y est écrit pour la fibrillation clinique." + S(5)),
            P("Ne pas utiliser la puissance maximale de la fibrillation comme premier chiffre du flutter : le texte de réanimation les sépare.", "Ne pas donner Tambocor sans avoir lu le risque d'accélération de la réponse ventriculaire."),
            P(f"Les {B('w-dx4-pieges', 'pièges')} portent sur les joules et Tambocor."),
        ]
        wins = {
            11: W("w-dx4-dose", "Flutter, doses lues", [
                q("aips_41060_cordarone_iv.txt", "Traitement de charge: en moyenne 5 mg/kg dans 250 ml de solution de glucose 5% exclusivement, passés en 20 minutes à 2 heures et renouvelables 2 à 3 fois par 24 heures."),
                q("erc2021_arythmies.txt", "Give an initial shock of 70-120 J. Give subsequent shocks using stepwise increases in energy."),
                "Tambocor signale, chez des patients en fibrillation, une accélération ventriculaire par conduction un pour un après un ralentissement atrial. On garde cette alerte en tête devant un flutter, sans prétendre que la phrase vise le flutter mot pour mot.",
                q("aips_45710_tambocor.txt", "La flécaïnide ne doit pas être utilisé chez les patients atteints d'une cardiopathie structurelle ou d'une insuffisance ventriculaire gauche"),
            ]),
            14: quiz("w-dx4-pieges", [
                ("Premier choc du flutter ?", "70 à 120 joules, puis une montée. Pas la puissance maximale réservée comme stratégie à la fibrillation."),
                ("Charge de Cordarone ?", "5 mg/kg dans 250 ml de glucose à 5 pour cent, en 20 minutes à 2 heures."),
                ("10 flutters à Lausanne ?", "Oui, flutter typique, à côté de 42 fibrillations, sur un électrocardiogramme unique."),
                ("Intervalle combiné ?", "1,1 pour cent, intervalle 0,4 à 1,5, section résultats."),
                ("Cardiopathie et Tambocor ?", "Contre-indication lue."),
            ]),
        }
    elif n == 5:
        pts = [
            P("La tachycardie par réentrée nodale est une tachycardie régulière qui emprunte le nœud auriculo-ventriculaire dans les deux sens. Krenosin la vise parmi les tachycardies paroxystiques supraventriculaires." + S(9)),
            P("Aucune incidence suisse n'est dans les textes de la leçon."),
            P("Deux voies dans le nœud ferment un circuit. Le texte européen de 2019 décrit un bloc transitoire du nœud qui coupe la tachycardie après l'adénosine." + S(6)),
            P("Pouls rapide et régulier, début et fin brusques. L'instabilité passe d'abord au choc."),
            P("Palpitations en salves. Cou, malaise. Les signes défavorables sont ceux du conseil de réanimation." + S(8)),
            P(f"L'{ecg} pendant la crise est demandé par le texte de 2019. Le pouls seul ne montre pas la voie."),
            P("Régulier et rapide, avec un début brusque, ouvre cette fiche et le flutter. Le tracé les sépare."),
            P("Le diagnostic de crise est électrocardiographique. La conversion par Krenosin, quand elle survient, soutient une tachycardie qui dépend du nœud."),
            P("Électrocardiogramme pendant la tachycardie. Une manœuvre vagale peut être tentée si le patient est stable."),
            P("Stable : vagale, puis Krenosin 6 mg puis 12 mg si la première échoue en 1 à 2 minutes. Pas de dose au-delà." + S(9), "Instable : choc de 70 à 120 joules au départ." + S(8)),
            P(f"Toute la dose, les contre-indications et la grossesse sont dans {B('w-dx5-dose', 'Krenosin')}."),
            P("Expliquer les salves et la conduite si cela revient. L'ablation n'est pas dosée ici."),
            P("Ne pas donner Krenosin dans l'asthme ni dans un bloc de haut degré non stimulé.", "Ne pas ajouter une troisième ampoule."),
            P(f"Les {B('w-dx5-pieges', 'pièges')} reprennent 6 mg, 12 mg et l'asthme."),
        ]
        wins = {
            11: W("w-dx5-dose", "Krenosin 51567", [
                q("aips_51567_krenosin.txt", "Première dose: 6 mg administrés sous forme d'un bolus intraveineux (en 2 secondes)."),
                q("aips_51567_krenosin.txt", "Deuxième dose: dans le cas où la première dose n'arrête pas la tachycardie supraventriculaire en 1 à 2 minutes, il convient alors d'administrer 12 mg dans les mêmes conditions."),
                q("aips_51567_krenosin.txt", "Des doses supplémentaires ou supérieures ne sont pas recommandées."),
                "Contre-indications lues : bloc du second ou du troisième degré sans stimulateur, maladie du sinus, bradycardie symptomatique sans stimulateur, hypersensibilité, bronchopneumopathie obstructive dont l'asthme, QT long, hypotension sévère, insuffisance cardiaque décompensée.",
                q("aips_51567_krenosin.txt", "Cependant, en absence de données cliniques à ce sujet, Krenosin ne doit être utilisé pendant la grossesse qu'en cas d'indication stricte."),
                q("aips_51567_krenosin.txt", "Cependant, en l'absence de données cliniques à ce sujet, l'administration de Krenosin pendant l'allaitement n'est à effectuer qu'en cas de nécessité absolue."),
                "Le texte signale que, en fibrillation avec voie accessoire, la voie anormale peut être préférée. Cette fiche de réentrée régulière n'est pas cette situation.",
                "Chez l'enfant, aucune étude contrôlée lue. Des études ouvertes décrivent 0,10 à 0,25 mg/kg. On ne les prend pas pour une autorisation.",
            ]),
            14: quiz("w-dx5-pieges", [
                ("Après 12 mg ?", "Pas de dose supplémentaire ni supérieure, phrase de Krenosin."),
                ("Asthme ?", "Contre-indication lue, avec la bronchopneumopathie obstructive."),
                ("Grossesse ?", "Seulement en cas d'indication stricte."),
                ("Allaitement ?", "Seulement en cas de nécessité absolue."),
                ("Choc initial si instable ?", "70 à 120 joules pour la tachycardie supraventriculaire paroxystique."),
            ]),
        }
    elif n == 6:
        pts = [
            P("La bradycardie sinusale est un rythme parti du nœud sinusal, plus lent que la plage d'un cœur sain au repos. Le texte de 2021 rappelle qu'elle peut être physiologique." + S(7)),
            P("Zurich : environ 60 à 100 au repos pour un cœur sain." + S(2), "Aucune prévalence suisse de la bradycardie pathologique n'est lue."),
            P("Le nœud sinusal ralentit. Les ondes P restent d'origine sinusale. Un bloc, lui, casse la relation entre l'oreillette et le ventricule."),
            P("On la distingue du bloc et de la pause. Les signes défavorables décident de l'atropine."),
            P("Fatigue, malaise, syncope. Chez l'athlète sans symptôme, le texte de 2021 n'indique pas le stimulateur." + S(7)),
            P(f"Pouls lent et régulier. L'{ecg} confirme le sinus."),
            P("Lent et régulier ouvre le sinus, la dysfonction sinusale et le bloc. Le tracé les sépare."),
            P("Le diagnostic positif est un rythme sinusal lent, interprété avec le contexte : athlète, médicament, ou symptôme."),
            P("Électrocardiogramme. On cherche un médicament ralentisseur et une cause réversible."),
            P("Sans symptôme et athlète : pas de stimulateur d'après le texte de 2021. Avec signes défavorables : atropine dans les limites suisses, puis avis pour un entraînement."),
            P(f"Atropine Sintetica 56533. {B('w-dx6-dose', 'Dose, plancher et grossesse')}." + S(10)),
            P("Revoir les ralentisseurs. Un sportif lent n'a pas besoin d'un médicament accélérateur."),
            P("Ne pas descendre sous 0,5 mg. Ne pas traiter 42 par minute chez un athlète asymptomatique comme un bloc."),
            P(f"Les {B('w-dx6-pieges', 'pièges')} portent sur 0,5 mg et le dernier trimestre."),
        ]
        wins = {
            11: W("w-dx6-dose", "Atropine 56533", [
                q("aips_56533_atropine.txt", "Chez l'adulte : 0,5-1,0 (-1,5) mg i.v ., à répéter éventuellement après 3-5 minutes. Dans les cas de bradycardie sévère, la dose totale administrée ne devrait pas dépasser 3 mg (0,04 mg/kg)."),
                q("aips_56533_atropine.txt", "En raison du risque d'apparition d'une baisse paradoxale de la fréquence cardiaque lors de faibles doses ou d'une administration très lente, il convient de ne pas administrer des doses de sulfate d'atropine en dessous de 0,5 mg lors d'états bradycardiques."),
                q("aips_56533_atropine.txt", "Le médicament ne doit pas être utilisé pendant la grossesse, sauf en cas de nécessité absolue."),
                q("aips_56533_atropine.txt", "Le traitement par l'atropine pendant le dernier trimestre de grossesse, pendant l'accouchement et la césarienne est contre-indiqué, à cause des dysrythmies (notamment tachycardies) qui peuvent apparaître chez la mère et le nouveau-né."),
                q("aips_56533_atropine.txt", "En conséquence, si la prise de ce médicament apparaît réellement indispensable, l'allaitement doit être cessé."),
                "Chez l'enfant, le minimum lu est 0,1 mg. La dose unique maximale est 0,5 mg chez l'enfant et 1 mg chez l'adolescent. Le total maximal est 1 mg chez l'enfant et 2 mg chez l'adolescent.",
                "Le texte de stimulation accepte 40 à 50 au repos, ou 30 en sommeil, chez l'athlète, sans stimulateur.",
            ]),
            14: quiz("w-dx6-pieges", [
                ("Sous 0,5 mg ?", "Non dans un état bradycardique. Ralentissement paradoxal décrit."),
                ("Total adulte ?", "Ne devrait pas dépasser 3 mg dans la bradycardie sévère."),
                ("Dernier trimestre ?", "Contre-indiqué, ainsi que l'accouchement et la césarienne."),
                ("Allaitement ?", "Il doit être cessé si le médicament est vraiment indispensable."),
                ("Athlète à 45 ?", "Peut rester sans stimulateur si c'est physiologique, texte de 2021."),
            ]),
        }
    elif n == 7:
        pts = [
            P("La dysfonction du nœud sinusal, ou maladie du sinus, va de la bradycardie sinusale au bloc sino-atrial, à la pause, et à la forme bradycardie-tachycardie." + S(7)),
            P("Le texte de 2021 dit que la forme bradycardie-tachycardie est la plus fréquente de cette maladie. Aucune prévalence suisse n'est lue."),
            P("Le tissu sinusal et atrial fibrose avec l'âge. Une tachycardie atriale peut être suivie d'une pause." + S(7)),
            P("On la cherche devant une syncope, une fatigue, ou une alternance de rapide et de lent."),
            P("La syncope est rapportée chez 50 pour cent des patients qui reçoivent un stimulateur pour cette indication." + S(7), "Le lien entre le symptôme et la bradycardie doit être établi."),
            P(f"Pouls lent, ou lent après une salve rapide. L'{ecg} et un enregistrement long cherchent la pause."),
            P("Lent isolé ouvre aussi la bradycardie simple. L'alternance ouvre davantage cette fiche."),
            P("Le diagnostic positif relie le symptôme à la bradycardie enregistrée. Sans ce lien, le stimulateur n'est pas indiqué pour une forme asymptomatique." + S(7)),
            P("Électrocardiogramme, enregistrement prolongé, et liste des ralentisseurs."),
            P("Stimulateur si le symptôme est clairement dû à la bradycardie. L'atropine est un pont, pas le traitement de fond."),
            P(f"Atropine comme dans la bradycardie, et contre-indications des produits qui dépriment le sinus. {B('w-dx7-dose', 'Fenêtre')}." + S(10)),
            P("Revoir les ralentisseurs avant de poser l'indication définitive. Krenosin est contre-indiqué dans la maladie du sinus non stimulée."),
            P("Ne pas stimuler une forme asymptomatique seulement parce que le tracé est lent.", "Ne pas donner Krenosin pour une salve si le sinus est malade et non appareillé."),
            P(f"Les {B('w-dx7-pieges', 'pièges')} portent sur le symptôme et le sinus."),
        ]
        wins = {
            11: W("w-dx7-dose", "Sinus malade", [
                q("esc2021_stimulation.txt", "In patients with SND including those with bradycardia-tachycardia type of SND, when symptoms can clearly be attributed to bradyarrhythmia, cardiac pacing is indicated."),
                "La syncope concerne 50 pour cent des patients stimulés pour cette maladie dans le texte de 2021.",
                q("aips_56533_atropine.txt", "Chez l'adulte : 0,5-1,0 (-1,5) mg i.v ., à répéter éventuellement après 3-5 minutes. Dans les cas de bradycardie sévère, la dose totale administrée ne devrait pas dépasser 3 mg (0,04 mg/kg)."),
                "Cordarone injectable contre-indique la maladie du sinus non appareillée, à cause du risque d'arrêt sinusal.",
                "Krenosin contre-indique le syndrome du sinus malade et la bradycardie symptomatique, sauf stimulateur.",
                q("aips_56533_atropine.txt", "Le traitement par l'atropine pendant le dernier trimestre de grossesse, pendant l'accouchement et la césarienne est contre-indiqué, à cause des dysrythmies (notamment tachycardies) qui peuvent apparaître chez la mère et le nouveau-né."),
            ]),
            14: quiz("w-dx7-pieges", [
                ("Stimulateur sans symptôme ?", "Non pour cette maladie. Le symptôme doit être lié à la bradycardie."),
                ("50 pour cent ?", "Part des patients stimulés pour dysfonction sinusale qui ont eu une syncope, texte de 2021."),
                ("Krenosin ?", "Contre-indiqué si le sinus est malade et non stimulé."),
                ("Cordarone ?", "Maladie du sinus non appareillée : contre-indication lue."),
                ("Atropine de pont ?", "0,5 à 1 mg, sans descendre sous 0,5 mg, total jusqu'à 3 mg dans la forme sévère."),
            ]),
        }
    elif n == 8:
        pts = [
            P("Le bloc auriculo-ventriculaire de haut degré comprend, dans le texte de 2021, le Mobitz II, le bloc 2 pour 1, le bloc de haut degré où le rapport P sur QRS est d'au moins 3 pour 1, et le bloc complet." + S(7)),
            P("Aucune prévalence suisse n'est lue."),
            P("L'onde P n'est plus conduite de façon fiable. Le ventricule échappe, lentement. Le pouls est lent, parfois large si l'échappement est distal."),
            P("C'est E2 de l'algorithme. L'instabilité ne attend pas le nom."),
            P("Syncope, fatigue, insuffisance cardiaque. Le texte indique le stimulateur même sans symptôme pour ces blocs, si le rythme atrial est sinusal." + S(7)),
            P(f"Pouls lent. L'{ecg} compte les P et les QRS."),
            P("Un lent régulier avec des P non conduites n'est pas une bradycardie sinusale."),
            P(q("esc2021_stimulation.txt", "In patients with SR and permanent or paroxysmal third- or second-degree type 2 or high-degree AVB, cardiac pacing is indicated irrespective of symptoms.")),
            P("Électrocardiogramme immédiat. On cherche une cause réversible, dont un médicament, avant l'indication définitive."),
            P("Stimulateur pour les formes lues, avec ou sans symptôme. En attendant, atropine si des signes défavorables sont là, et Isuprel dans son indication de trouble de conduction avant pacemaker."),
            P(f"Isuprel 56457 et atropine 56533. {B('w-dx8-dose', 'Doses et arrêts')}." + S(13)),
            P("Éviter d'ajouter un ralentisseur. Magnesiocard est contre-indiqué en cas de bloc."),
            P("Ne pas exiger un symptôme pour indiquer le stimulateur dans ces blocs.", "Ne pas poursuivre Isuprel si la fréquence atteint 130."),
            P(f"Les {B('w-dx8-pieges', 'pièges')} portent sur le symptôme, 130 par minute et l'enfant."),
        ]
        wins = {
            11: W("w-dx8-dose", "Pont avant le stimulateur", [
                q("esc2021_stimulation.txt", "In patients with SR and permanent or paroxysmal third- or second-degree type 2 or high-degree AVB, cardiac pacing is indicated irrespective of symptoms."),
                "Isuprel est indiqué, en cardiologie, pour des bradycardies permanentes par trouble de la conduction, avant un pacemaker ou si le pacemaker est contre-indiqué.",
                q("aips_56457_isuprel.txt", "La posologie varie selon l'indication de 0.2 mg à 10 mg par 24 heures."),
                q("aips_56457_isuprel.txt", "Une fréquence cardiaque égale (ou supérieure) à 130/minute constitue une contre-indication à la poursuite du traitement."),
                q("aips_56457_isuprel.txt", "Ce médicament ne doit pas être utilisé pendant la grossesse, sauf dans le cas où le traitement es t absolument nécessaire."),
                q("aips_56457_isuprel.txt", "Il est déconseillé d'administrer Isuprel pendant l'allaitement."),
                "L'enfant et l'adolescent : utilisation non recommandée. L'infarctus aigu est une contre-indication, sauf bloc avec bradycardie extrême.",
                "L'injection peut paradoxalement aggraver le bloc ou déclencher une crise d'Adams-Stokes, phrase lue chez certains patients suspects d'une maladie du nœud.",
                q("aips_56533_atropine.txt", "Chez l'adulte : 0,5-1,0 (-1,5) mg i.v ., à répéter éventuellement après 3-5 minutes. Dans les cas de bradycardie sévère, la dose totale administrée ne devrait pas dépasser 3 mg (0,04 mg/kg)."),
                "Magnesiocard contre-indique le bloc auriculo-ventriculaire et la bradycardie prononcée.",
            ]),
            14: quiz("w-dx8-pieges", [
                ("Faut-il un symptôme pour stimuler un bloc complet ?", "Non si le rythme est sinusal et le bloc de type 2, de haut degré ou complet. Le texte dit irrespective of symptoms."),
                ("Rapport P sur QRS ?", "Au moins 3 pour 1 définit le haut degré dans le titre lu."),
                ("Isuprel, quelle fourchette ?", "0,2 mg à 10 mg par 24 heures, selon l'indication."),
                ("Arrêt à quelle fréquence ?", "130 par minute, poursuite contre-indiquée."),
                ("Enfant ?", "Isuprel non recommandé. Atropine : voir les plafonds de la fiche bradycardie."),
            ]),
        }
    elif n == 9:
        pts = [
            P("La tachycardie ventriculaire est un rythme rapide né dans le ventricule. Avec un pouls et des signes défavorables, le conseil de réanimation la choque." + S(8)),
            P("Aucune incidence suisse n'est lue. Elle est E1 de l'algorithme à cause de l'instabilité, pas à cause d'une fréquence de population."),
            P("Un circuit ou un foyer ventriculaire produit des complexes larges et rapides. Le pouls peut être encore présent."),
            P("Tout complexe large et rapide est traité comme elle tant qu'un diagnostic certain de réentrée avec aberration n'est pas déjà connu."),
            P("Malaise, douleur, choc, œdème. Les quatre signes défavorables imposent le choc." + S(8)),
            P(f"Pouls rapide. L'{ecg} montre le complexe large. On ne rassure pas sur un pouls encore palpé."),
            P("Large et rapide ouvre cette fiche. Irrégulier et large ouvre aussi la fibrillation préexcitée et la tachycardie polymorphe."),
            P("Le diagnostic positif de l'urgence est clinique et électrique. La preuve du foyer peut attendre."),
            P("Électrocardiogramme pendant le choc ou juste après si le patient le permet. On cherche l'ischémie et les électrolytes."),
            P("Instable : 120 à 150 joules au premier choc, puis une montée." + S(8), "La charge médicamenteuse suisse, si elle est indiquée, est celle de Cordarone injectable, pas la phrase européenne des 300 mg en 10 à 20 minutes."),
            P(f"Cordarone 41060 et Tambocor 45710 ont des limites dures. {B('w-dx9-dose', 'Doses')}." + S(11)),
            P("Après l'épisode, le cœur sous-jacent se bilan. Cette fiche ne pose pas l'indication du défibrillateur implantable."),
            P("Ne pas donner Tambocor dans une cardiopathie structurelle.", "Ne pas utiliser les 300 mg rapides hors réanimation d'une fibrillation ventriculaire résistante."),
            P(f"Les {B('w-dx9-pieges', 'pièges')} séparent les joules, la charge et la réanimation."),
        ]
        wins = {
            11: W("w-dx9-dose", "Ventricule, doses lues", [
                q("erc2021_arythmies.txt", "Ventricular tachycardia with a pulse responds well using energy levels of 120−150 J for the initial shock."),
                "Cordarone injectable vise des arythmies ventriculaires gravement symptomatiques et invalidantes, après échec des autres traitements.",
                q("aips_41060_cordarone_iv.txt", "Traitement de charge: en moyenne 5 mg/kg dans 250 ml de solution de glucose 5% exclusivement, passés en 20 minutes à 2 heures et renouvelables 2 à 3 fois par 24 heures."),
                q("aips_41060_cordarone_iv.txt", "Réanimation cardio-pulmonaire lors de fibrillation ventriculaire résistant à la cardioversion électrique: la dose initiale par voie intraveineuse comporte 300 mg (ou 5 mg/kg de poids corporel) dilués dans 20 ml de glucose à 5%, injectés rapidement."),
                "La dose additionnelle lue dans cette réanimation est 150 mg, ou 2,5 mg/kg, si la fibrillation ventriculaire persiste.",
                q("aips_41060_cordarone_grossesse.txt", "Cordarone ne devrait pas être employé pendant la grossesse, sauf en cas de nécessité absolue."),
                "L'allaitement est une contre-indication de la liste lue, et l'hypokaliémie aussi, ainsi que le QT long préexistant.",
                "L'amiodarone intraveineuse n'est pas recommandée chez l'enfant et l'adolescent.",
                q("aips_45710_tambocor.txt", "La flécaïnide ne doit pas être utilisé chez les patients atteints d'une cardiopathie structurelle ou d'une insuffisance ventriculaire gauche"),
                "Magnesiocard : une ampoule de 10 ml, 3 mmol, en injection lente, n'est pas le protocole de 2 g. Le bloc et la bradycardie prononcée restent des contre-indications.",
            ]),
            14: quiz("w-dx9-pieges", [
                ("Premier choc avec pouls ?", "120 à 150 joules."),
                ("Charge avec pouls ?", "5 mg/kg dans 250 ml de glucose à 5 pour cent, en 20 minutes à 2 heures."),
                ("300 mg rapides ?", "Réanimation d'une fibrillation ventriculaire résistante au choc, dilués dans 20 ml de glucose à 5 pour cent."),
                ("Dose suivante dans cette réanimation ?", "150 mg, ou 2,5 mg/kg, si la fibrillation ventriculaire persiste."),
                ("Tambocor et infarctus ?", "Contre-indication lue."),
            ]),
        }
    else:
        pts = [
            P("La fibrillation auriculaire préexcitée conduit par une voie accessoire. Le pouls est irrégulier et les complexes sont larges. Le texte de 2024 contre-indique alors les ralentisseurs du nœud." + S(5)),
            P("Aucune prévalence suisse de cette forme n'est lue. Elle est E3 parce que le mauvais médicament peut accélérer le ventricule, pas parce qu'elle serait fréquente."),
            P("La voie accessoire passe à côté du nœud. Si l'on bloque le nœud, davantage d'impulsions atriales descendent par la voie. Le ventricule peut s'accélérer."),
            P("On l'évoque devant un irrégulier large, et avant tout ralentisseur."),
            P("Palpitations, malaise, choc. L'instabilité va au choc synchronisé, stratégie de la fibrillation : puissance maximale." + S(8)),
            P(f"L'{ecg} montre une fibrillation et des complexes larges dont la morphologie change. Krenosin prévient que la voie anormale peut être préférée." + S(9)),
            P("Irrégulier et large ouvre cette fiche et la tachycardie polymorphe. Le tracé les distingue."),
            P(q("esc2024_fa.txt", "a All rate control drugs are contraindicated in Wolff-Parkinson-White syndrome; also intravenous amiodarone.")),
            P("Électrocardiogramme avant le médicament. On ne fait pas d'essai thérapeutique avec un ralentisseur."),
            P("Instable : choc à puissance maximale. Stable : pas de Beloc, pas de Krenosin, pas d'amiodarone intraveineuse comme ralentisseur."),
            P(f"Tambocor a une indication lue dans la préexcitation, avec des limites. {B('w-dx10-dose', 'Ce qui est permis et interdit')}." + S(15)),
            P("Après l'épisode, la voie accessoire se discute avec un rythmologue. Cette fiche ne pose pas l'ablation."),
            P("Ne pas ralentir le nœud. Ne pas prendre la réentrée régulière du syndrome de Wolff-Parkinson-White pour cette fibrillation."),
            P(f"Les {B('w-dx10-pieges', 'pièges')} séparent la réentrée régulière et la fibrillation préexcitée."),
        ]
        wins = {
            11: W("w-dx10-dose", "Préexcitation et fibrillation", [
                q("esc2024_fa.txt", "a All rate control drugs are contraindicated in Wolff-Parkinson-White syndrome; also intravenous amiodarone."),
                q("aips_51567_krenosin.txt", "Chez les patients atteints de fibrillation auriculaire et de réponses ventriculaires accessoires, la voie de conduction anormale peut être préférée"),
                "Krenosin reste indiqué pour convertir une tachycardie paroxystique supraventriculaire, y compris avec voie accessoire. Cette phrase vise la tachycardie régulière, pas la fibrillation préexcitée de l'avertissement.",
                "Tambocor comprimés, sans cardiopathie structurelle, nomme le syndrome de Wolff-Parkinson-White parmi les arythmies supraventriculaires. La dose supraventriculaire lue commence à 2 fois 50 mg, maximum 2 fois 150 mg.",
                q("aips_45710_tambocor.txt", "Dose initiale et d'entretien: ½ comprimé deux fois par jour (2x 50 mg)."),
                q("aips_45710_tambocor.txt", "La flécaïnide ne doit pas être utilisé chez les patients atteints d'une cardiopathie structurelle ou d'une insuffisance ventriculaire gauche"),
                "Le bolus de 2 mg/kg en au moins 10 minutes, au plus 150 mg, est la dose injectable lue. On le réserve au cadre hospitalier de l'information.",
                "Beloc et la charge de Cordarone ne sont pas proposés ici comme ralentisseurs.",
            ]),
            14: quiz("w-dx10-pieges", [
                ("Beloc dans cette fiche ?", "Non. Les ralentisseurs sont contre-indiqués, texte de 2024."),
                ("Amiodarone intraveineuse ?", "Aussi contre-indiquée comme ralentisseur dans le même renvoi."),
                ("Krenosin ?", "Avertissement : la voie accessoire peut être préférée en fibrillation. On ne l'utilise pas pour ralentir cette forme."),
                ("Tambocor, dose de départ orale ?", "2 fois 50 mg, sans cardiopathie structurelle. Maximum lu 2 fois 150 mg pour le supraventriculaire."),
                ("Choc si instable ?", "Puissance maximale, stratégie lue pour la fibrillation."),
            ]),
        }
    # compléter les points sans fenêtre vide : assembler accepte wins manquants
    for i in range(1, 15):
        wins.setdefault(i, "")
    # phrase de clôture déjà dans les points
    _ = commun_fin
    return {"pts": pts, "wins": wins}


def main(arg: str) -> None:
    if arg in ("phase", "tout"):
        path = ecrire("LOT_136_Phase_A_V0.html", phase_a())
        print(path)
    if arg == "tout":
        cibles = range(1, 11)
    elif arg.isdigit():
        cibles = [int(arg)]
    else:
        cibles = []
    for n in cibles:
        path = ecrire(f"LOT_136_Phase_B_V0_DX.{n}.html", dx_page(n))
        print(path)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "tout")

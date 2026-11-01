#!/usr/bin/env python3
"""Construit les 11 leçons de LOT_203 (O4.2 Plan de vaccination)."""
from __future__ import annotations

import html
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path("/workspace/grok-LOTS-html/LOT_203")
MOTS_CLES = re.compile(r"prévalence|incidence|sensibilit|spécificit|seuil|score", re.I)
SIGLE = re.compile(r"\b([A-ZÉÈÀ]{2,}[A-Z0-9ÉÈÀ]*)\b")
IGNORES = {
    "HTML", "CSS", "UTF", "DOI", "URL", "PDF", "SI", "DX", "LOT", "OK", "CI",
    "II", "III", "IV", "VI", "VII", "VIII", "IX", "XI", "XII",
}
LIB = {
    "OFSP": "Office fédéral de la santé publique",
    "CFV": "Commission fédérale pour les vaccinations",
    "HPV": "papillomavirus humains",
    "VRS": "virus respiratoire syncytial",
    "ROR": "rougeole, oreillons, rubéole",
    "RORV": "rougeole, oreillons, rubéole et varicelle",
    "PCV": "vaccin conjugué contre le pneumocoque",
    "IPV": "vaccin inactivé de la poliomyélite",
    "HBV": "virus de l'hépatite B",
    "OMS": "Organisation mondiale de la santé",
    "FSME": "encéphalite à tiques",
    "VIH": "virus de l'immunodéficience humaine",
    "AIPS": "information professionnelle suisse",
    "ACWY": "sérogroupes A, C, W et Y",
    "COVID": "maladie à coronavirus 2019",
    "SUVA": "assurance-accidents suisse",
    "SG": "semaine de grossesse",
    "IM": "intramusculaire",
    "PEP": "prophylaxie post-exposition",
}

TITRES = {
    1: "Définition",
    2: "Épidémiologie",
    3: "Physiopathologie",
    4: "Démarche diagnostique",
    5: "Anamnèse et drapeaux rouges",
    6: "Examen physique",
    7: "Approche syndromique",
    8: "Diagnostic positif",
    9: "Examens complémentaires",
    10: "Arbre décisionnel",
    11: "Prise en charge",
    12: "Prévention",
    13: "Points clés",
    14: "Pièges et cas",
}

NOMS = {
    "A": "Plan de vaccination",
    1: "Calendrier incomplet du nourrisson",
    2: "Rattrapage de l'enfant et de l'adolescent",
    3: "Rappels de l'adulte et coqueluche à 25 ans",
    4: "Vaccinations complémentaires dès 65 ans",
    5: "Grossesse et protection du nouveau-né",
    6: "Immunodépression et asplénie",
    7: "Prématuré et mère porteuse de l'hépatite B",
    8: "Tiques, voyage et rage",
    9: "Plaie et effet indésirable grave",
    10: "Personnel de santé au statut inconnu",
}

CIBLES = {
    "A": 76000,
    1: 36800,
    2: 39100,
    3: 41700,
    4: 44300,
    5: 45800,
    6: 37600,
    7: 40400,
    8: 42900,
    9: 45100,
    10: 38600,
}

NIVEAU = {
    "A": "deux-sites",
    1: "cuisse",
    2: "deltoide",
    3: "deltoide",
    4: "deltoide",
    5: "cuisse",
    6: "deltoide",
    7: "cuisse",
    8: "deltoide",
    9: "deltoide",
    10: "deux-sites",
}

PANNEAUX = {
    "A": [
        ("1. Danger.", ["Anaphylaxie, plaie souillée, mère porteuse.", "Nouveau-né à protéger avant la sortie.", "On vaccine après avoir écarté le choc."]),
        ("2. Âge.", ["Nourrisson, enfant, adulte, 65 ans et plus.", "Grossesse et prématuré à part.", "Statut inconnu : on rattrape, on n'invente pas."]),
        ("3. Produit.", ["Base, complément, ou situation à risque.", "Vivant seulement si grossesse et immunité le permettent.", "Dose lue dans l'information professionnelle."]),
    ],
    1: [
        ("1. Âge exact.", ["Semaines pour le vaccin oral.", "Mois pour le combiné et le pneumocoque.", "9 mois puis 12 mois pour le quadrivalent."]),
        ("2. Doses déjà faites.", ["Compter, ne pas recommencer à zéro.", "Noter le produit et le site.", "Le 20-valent change la suite du nourrisson."]),
        ("3. Même jour.", ["Deux sites, jamais un mélange.", "Cuisse avant un an.", "Reporter seulement la fièvre sévère."]),
    ],
    2: [
        ("1. Scolarité.", ["Rappel combiné entre 4 et 7 ans.", "Coqueluche entre 11 et 15 ans.", "Polio : pas de dose ensuite sans exposition."]),
        ("2. Papillomavirus.", ["Deux doses si la première est avant 15 ans.", "Trois doses dès 15 ans ou si déficit.", "On termine, on ne reprend pas à zéro."]),
        ("3. Méningocoques.", ["Quadrivalent et sérogroupe B à l'adolescence.", "Même après une dose du petit enfant.", "Rattrapage jusqu'à la veille de 20 ans."]),
    ],
    3: [
        ("1. Dernière dose.", ["À 25 ans : diphtérie, tétanos, coqueluche.", "Puis 45 ans et 65 ans pour diphtérie et tétanos.", "L'intervalle dépend de l'âge du dernier rappel."]),
        ("2. Entourage.", ["Contact avec un nourrisson de moins de 6 mois.", "Coqueluche si le dernier rappel a 10 ans ou plus.", "Grossesse : voir le tableau propre."]),
        ("3. Trous.", ["Statut inconnu : trois doses, pas un seul rappel.", "Papillomavirus jusqu'à 26 ans si jamais commencé.", "Rougeole si naissance après 1963."]),
    ],
    4: [
        ("1. Chaque automne.", ["Grippe dès 65 ans.", "Dose élevée dès 75 ans, ou dès 65 ans si risque en plus.", "Covid d'octobre à décembre."]),
        ("2. Une fois.", ["Pneumocoque conjugué, pas le polysaccharide 23.", "Zona sous-unitaire, deux doses.", "Même après un zona guéri ou un ancien vaccin vivant."]),
        ("3. Rappels.", ["Diphtérie et tétanos si le dernier a 10 ans ou plus.", "On n'ajoute pas une valence pour le plaisir.", "On note le lot."]),
    ],
    5: [
        ("1. Chaque grossesse.", ["Coqueluche dès 13 semaines, idéalement avant 26.", "Encore utile jusqu'à 14 jours du terme.", "Quatre semaines après un vaccin tétanique."]),
        ("2. Une fois.", ["Virus respiratoire entre 32 et 36 semaines.", "Seulement si le terme tombe d'octobre à mars.", "Pas à la grossesse suivante."]),
        ("3. Vivant interdit.", ["Rougeole et varicelle avant la grossesse.", "Une dose faite par mégarde n'interrompt pas la grossesse.", "Covid au deuxième ou troisième trimestre."]),
    ],
    6: [
        ("1. Vivant ou non.", ["Déficit cellulaire : pas de vaccin vivant.", "Corticoïde fort et prolongé : même prudence.", "Inactivé : souvent oui, parfois en plus."]),
        ("2. Rate et complément.", ["Asplénie : méningocoques, pneumocoque, grippe.", "Éculizumab et ravulizumab : méningocoques.", "Idéalement avant l'ablation de la rate."]),
        ("3. Zona.", ["Dès 50 ans si l'immunité cellulaire faiblit.", "Dès 18 ans si l'immunodépression sera lourde.", "Avant la chimiothérapie si le calendrier le permet."]),
    ],
    7: [
        ("1. Naissance.", ["Mère porteuse : vaccin et immunoglobuline ensemble.", "Mère seulement anti-core : schéma ordinaire.", "Prématuré : quatre doses, pas trois."]),
        ("2. Mois.", ["2, 3, 4 et 12 mois si moins de 32 semaines ou 1500 g.", "Sérologie un mois après la dernière dose si mère porteuse.", "Grippe dès 6 mois, deux hivers."]),
        ("3. Entourage.", ["Coqueluche des contacts.", "Le nourrisson ne reçoit pas la grippe avant 6 mois.", "On protège ceux qui le portent."]),
    ],
    8: [
        ("1. Ici.", ["Suisse entière sauf le Tessin : tiques.", "Dès 3 ans en général.", "Dès 1 an si l'exposition est forte."]),
        ("2. Ailleurs.", ["Le détail du voyage est sur le site des voyages sains.", "Fièvre jaune et rougeole : quatre semaines d'écart.", "Rage : mammifère d'une zone enzootique, ou chauve-souris."]),
        ("3. Temps.", ["On ne part pas en laissant la série à moitié.", "Un vivant et une grossesse ne vont pas ensemble.", "On note le pays et la date."]),
    ],
    9: [
        ("1. Plaie.", ["Propre ou souillée, d'abord.", "Nombre de doses documentées, ensuite.", "Moins de trois doses et plaie à risque : vaccin et sérum."]),
        ("2. Choc.", ["On traite avant de discuter le calendrier.", "Adrénaline selon l'information lue, pas une dose inventée.", "On surveille, on peut répéter."]),
        ("3. Annonce.", ["Suspicion grave : Swissmedic.", "Quinze jours, immédiat si le pronostic vital est en jeu.", "Soixante jours pour le reste des annonces obligatoires."]),
    ],
    10: [
        ("1. Carnet.", ["Deux doses de rougeole documentées.", "Varicelle : maladie claire ou deux doses.", "L'histoire de rougeole ne suffit pas."]),
        ("2. Hépatite B.", ["Taux durable : au moins 100 unités par litre.", "En dessous : une dose, puis on recontrôle.", "Après six doses, décision au cas par cas."]),
        ("3. Refus.", ["On protège le patient exposé.", "Changement de poste si besoin.", "On n'invente pas une sérologie de complaisance."]),
    ],
}


def mots(texte: str) -> int:
    brut = re.sub(r"<[^>]+>", " ", texte)
    return len(re.findall(r"[\wÀ-ÿŒœ'’\-]+", brut))


def P(texte: str, sup: int | None = None) -> str:
    if mots(texte) > 34:
        raise SystemExit(f"PHRASE LONGUE ({mots(texte)}): {texte}")
    if ";" in texte:
        raise SystemExit(f"POINT-VIRGULE: {texte}")
    if "<" in texte or ">" in texte:
        raise SystemExit(f"CHEVRON: {texte}")
    if MOTS_CLES.search(texte) and re.search(r"\d", texte) and not sup:
        raise SystemExit(f"CHIFFRE SANS SUP: {texte}")
    fin = f' <sup class="s">{sup}</sup>' if sup else ""
    return f"<p>{texte}{fin}</p>"


def schema(prefix: str, cle) -> str:
    css, inputs, labels, svgs = [], [], [], []
    for i, (etq, lignes) in enumerate(PANNEAUX[cle]):
        iid = f"{prefix}{i}"
        checked = " checked" if i == 0 else ""
        css.append(
            f"#{iid}:checked ~ .plan .n{i}{{display:block}}"
            f"#{iid}:checked ~ .bn label[for='{iid}']{{background:#d7eef8;border-color:#176fa0}}"
        )
        inputs.append(f'<input class="sr" type="radio" name="{prefix}" id="{iid}"{checked}>')
        labels.append(f'<label for="{iid}">{html.escape(etq)}</label>')
        y = 36
        parts = [
            f'<text x="320" y="28" text-anchor="middle" font-size="18" font-weight="700" fill="#14303b">{html.escape(etq)}</text>'
        ]
        for ligne in lignes:
            if len(ligne) > 58:
                raise SystemExit(f"LIGNE SVG: {ligne}")
            parts.append(f'<rect x="28" y="{y}" width="584" height="42" rx="8" fill="#e7f4fb" stroke="#176fa0"/>')
            parts.append(
                f'<text x="44" y="{y + 27}" font-size="16" fill="#14303b">{html.escape(ligne)}</text>'
            )
            y += 52
        svgs.append(
            f'<svg class="niv n{i}" viewBox="0 0 640 220" role="img" aria-label="{html.escape(etq)}">{"".join(parts)}</svg>'
        )
    style = "<style>" + "".join(css) + f"#{prefix} .plan .niv{{display:none}}</style>"
    return (
        f'{style}<div class="sch" id="{prefix}">{"".join(inputs)}'
        f'<div class="bn">{"".join(labels)}</div>'
        f'<div class="plan">{"".join(svgs)}</div></div>'
    )


def fragment_sites() -> str:
    dest = Path("/workspace/grok-LOTS-html/outils/dessinateur/dessinateur.py")
    spec = importlib.util.spec_from_file_location("dess_lot203", dest)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    desc = json.loads((ROOT / "_travail" / "sites.json").read_text(encoding="utf-8"))
    frag = mod.rendre(desc, "POLICE")
    police = "../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf"
    frag = frag.replace('url("POLICE")', f'url("{police}")')
    frag = re.sub(r"<script\b.*?</script>", "", frag, flags=re.S)
    if "<script" in frag.lower():
        raise SystemExit("script restant")
    return frag


def choisir_niveau(fragment: str, niveau: str) -> str:
    frag = re.sub(r" checked=\"checked\"", "", fragment)
    cle = f'id="lot203-sites-{niveau}"'
    if cle not in frag:
        raise SystemExit(f"niveau absent {niveau}")
    return frag.replace(cle, cle + ' checked="checked"', 1)


CSS = r"""
:root{--fond:#eef7fc;--page:#ffffff;--texte:#1d2a30;--doux:#4f5f66;--lien:#0b5d86;--titre:#14303b;--trait:#cfe3ec;--encadre:#f5f7f9;--bord:#1a7a50;--vert:#1a7a50;--ciel:#176fa0;--alerte:#a1262f;--ombre:rgb(15 60 90 / .28);--voile:rgb(10 30 45 / .55);--barre:#f2f5f7;--th:#f2f5f7;--cb1:#4fb3e6;--cb2:#b9e2f6;--vb1:#3aa776;--vb2:#b5e1cb}
@media (prefers-color-scheme:dark){:root{--fond:#0e171d;--page:#16222a;--texte:#e3edf1;--doux:#a9bac2;--lien:#8fd3f5;--titre:#e6eef2;--trait:#2c414c;--encadre:#1a252c;--bord:#5cc79a;--vert:#5cc79a;--ciel:#6cc2ef;--alerte:#ff8a92;--ombre:rgb(0 0 0 / .6);--voile:rgb(0 0 0 / .7);--barre:#1d282f;--th:#1d282f;--cb1:#4aa9da;--cb2:#24506a;--vb1:#46b384;--vb2:#245a44}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}body{margin:0;background:var(--fond);color:var(--texte);font:1rem/1.45 "Liberation Sans","Atkinson Hyperlegible",Verdana,sans-serif;overflow-wrap:break-word;hyphens:manual}
main{max-width:72ch;margin:0 auto;padding:1rem 1rem 2rem}h1,h2,h3,.fenetre .barre,summary,nav,caption,th{font-family:"Liberation Sans","Atkinson Hyperlegible",Verdana,sans-serif}
h1{font-size:1.75rem;line-height:1.25;color:var(--titre);margin:0 0 .4rem}h2{font-size:1.3rem;line-height:1.3;color:var(--titre);margin:0 0 .45rem}h3{font-size:1.08rem;color:var(--titre);margin:1rem 0 .3rem}
p,.para{margin:0 0 .55rem}.sous{color:var(--doux);font-size:.95rem}.essentiel{border-left-width:4px}.essentiel h2{font-size:1.1rem}
nav ol{padding-left:1.6rem;margin:.4rem 0 0}nav li{margin:.15rem 0}a{color:var(--lien)}
button.terme{all:unset;cursor:pointer;color:var(--lien);text-decoration:underline dotted 1.5px;text-underline-offset:3px}button.terme::after{content:" ⧉";font-size:.75em;vertical-align:.15em}
button.terme:focus-visible{outline:2px solid var(--lien);outline-offset:2px}
.fenetre{position:fixed;inset:0;margin:auto;width:min(92vw,44rem);max-height:80vh;overflow:auto;padding:0;border:1px solid var(--trait);border-radius:12px;background:var(--page);color:var(--texte);box-shadow:0 18px 50px var(--ombre);font-size:.98rem}
.fenetre::backdrop{background:var(--voile)}
.fenetre > .barre{position:sticky;top:0;z-index:1;display:flex;align-items:center;justify-content:space-between;gap:.8rem;padding:.55rem .6rem .55rem 1rem;background:var(--barre);border-bottom:1px solid var(--trait);font-weight:700;font-size:.95rem}
.fenetre > .barre button{flex:none;width:2rem;height:2rem;border:1px solid var(--trait);border-radius:6px;background:var(--page);color:var(--texte);font-size:1rem;cursor:pointer}
.corps{padding:1rem 1.2rem 1.2rem}.corps p:last-child{margin-bottom:0}
.tw{overflow-x:auto;margin:.6rem 0 1rem}table{border-collapse:collapse;width:100%;font-size:.9rem;line-height:1.45}th,td{border:1px solid var(--trait);padding:.4rem .5rem;vertical-align:top;text-align:left}th{background:var(--th);font-size:.85rem}caption{text-align:left;font-weight:700;font-size:.9rem;padding:.2rem 0 .4rem}
figure{margin:1.2rem 0}figure svg{width:100%;height:auto;max-width:40rem;display:block;margin:auto;color:var(--texte);background:#f7fbfd;border:1px solid var(--trait);border-radius:10px}
figcaption{font-size:.88rem;color:var(--doux);text-align:center;margin-top:.3rem}
.biblio{font-size:.86rem;line-height:1.5}.taille{font-size:.85rem;color:var(--doux);margin:0 0 .6rem}.mention{font-style:italic;color:var(--doux);margin:.8rem .3rem 0}
sup.s{font-size:.66em;line-height:0;vertical-align:.5em;margin-left:.06em;color:#1a3a6b;font-weight:700}
abbr[title]{text-decoration:underline dotted 1px;text-underline-offset:2px;cursor:help}
.ilot{background:linear-gradient(var(--page),var(--page)) padding-box,var(--bd) border-box;border:1.5px solid transparent;border-radius:12px;padding:.85rem 1rem .6rem;margin:0 0 .7rem}
.ilot.c{--bd:linear-gradient(135deg,var(--cb1),var(--cb2))}.ilot.v{--bd:linear-gradient(135deg,var(--vb1),var(--vb2))}
.sch .niv{display:none}.sch input.sr{position:absolute;opacity:0;width:1px;height:1px}
.sch .bn{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 8px}.sch .bn label{border:1px solid #9bb;border-radius:8px;padding:4px 8px;cursor:pointer}
.som{columns:2;column-gap:1.4rem}.som li{break-inside:avoid}
details.schema{margin:.4rem 0 .6rem;border:1px solid var(--trait);border-radius:10px;padding:.4rem .6rem;background:var(--encadre)}
details.schema summary{cursor:pointer;font-weight:700}
.urgence{border:2px solid var(--alerte);border-radius:8px;padding:.7rem .9rem;margin:.7rem 0}
"""


def L(sac, n, texte, sup=None):
    sac.setdefault(n, []).append(P(texte, sup))


def commun(sac):
    L(sac, 1, "Un plan de vaccination est la liste datée de ce qui protège cette personne, pas un catalogue de produits.")
    L(sac, 1, "Le plan suisse de février 2026 distingue la base, le complément et la situation à risque.", 1)
    L(sac, 1, "Une vaccination n'est recommandée que si le bénéfice dépasse largement le risque d'effet indésirable.", 1)
    L(sac, 1, "La base protège la personne et la collectivité. Le complément protège surtout la personne qui le souhaite.", 1)
    L(sac, 1, "L'immunisation passive du nourrisson contre le virus respiratoire est rangée avec la base.", 1)
    L(sac, 2, "Il n'existe pas, dans les sources lues, un rang de prévalence des dix tableaux de ce motif.")
    L(sac, 2, "L'ordre des fichiers suit la consultation, du nourrisson au soignant, pas un registre unique.")
    L(sac, 2, "L'objectif d'hépatite B est que 95 pour cent des jeunes de 16 ans soient complètement vaccinés d'ici 2030.", 1)
    L(sac, 2, "Entre 2020 et 2022, la couverture à 2 ans avec trois doses était de 76 pour cent.", 1)
    L(sac, 2, "Chez les jeunes de 16 ans, deux doses atteignaient 79 pour cent sur la même période.", 1)
    L(sac, 2, "Les adolescents de 15 à 19 ans ont, après les nourrissons, la deuxième incidence de méningocoque par âge.", 1)
    L(sac, 2, "Le taux d'hospitalisation des rotavirus, avant 5 ans et sans vaccin, a été lu à 251 pour 100 000.", 1)
    L(sac, 3, "Un vaccin inactivé montre un antigène sans le faire se multiplier dans la personne.")
    L(sac, 3, "Un vaccin vivant atténué se réplique un peu. C'est pour cela qu'il est interdit si l'immunité cellulaire est cassée.", 1)
    L(sac, 3, "La primovaccination crée la mémoire. Le rappel la réveille.", 1)
    L(sac, 3, "L'âge de 12 mois veut dire du premier anniversaire à la veille du treizième mois.", 1)
    L(sac, 3, "Les anticorps de la mère peuvent encore gêner la rougeole entre 9 et 11 mois.", 4)
    L(sac, 3, "Une première dose de coqueluche protège déjà environ la moitié des nourrissons d'une forme grave.", 1)
    L(sac, 3, "La deuxième dose monte cette protection vers 83 à 87 pour cent, la troisième vers 85 à 95 pour cent.", 1)
    L(sac, 4, "On commence par le danger immédiat, puis par l'âge, puis par le carnet, puis par la grossesse et l'immunité.")
    L(sac, 4, "Une anaphylaxie se traite avant toute discussion de calendrier.", 9)
    L(sac, 4, "Une plaie souillée avec un statut inconnu ne repart pas sans vaccin, et souvent avec une immunoglobuline.", 1)
    L(sac, 4, "On ne mélange pas deux vaccins dans la même seringue.", 1)
    L(sac, 4, "Deux vivants se font le même jour, ou à quatre semaines d'écart.", 1)
    L(sac, 5, "On demande les doses, les dates, les produits, les réactions et la grossesse possible.")
    L(sac, 5, "Une fièvre sévère fait reporter. Un rhume simple ne fait pas reporter.", 2)
    L(sac, 5, "Une encéphalopathie dans les sept jours après un vaccin coqueluche contre-indique une nouvelle dose coqueluche.", 2)
    L(sac, 5, "L'histoire racontée de rougeole, d'oreillons ou de rubéole ne remplace pas deux doses documentées.", 1)
    L(sac, 5, "L'histoire de varicelle, elle, peut être retenue si elle est claire.", 1)
    L(sac, 6, "On regarde la peau, la fièvre, les saignements et le membre qui recevra l'injection.")
    L(sac, 6, "Avant un an, le site lu est la face antérolatérale de la cuisse.", 3)
    L(sac, 6, "Le muscle fessier n'est pas le site de routine, à cause du nerf sciatique.", 8)
    L(sac, 6, "Dès que la masse le permet, le deltoïde est le site habituel de l'adolescent et de l'adulte.", 2)
    L(sac, 6, "Sous anticoagulant, on garde la voie intramusculaire, avec une aiguille fine et deux minutes de compression.", 1)
    L(sac, 6, "On n'aspire pas avant d'injecter chez la personne qui saigne.", 1)
    L(sac, 7, "Les dix tableaux sont des situations de cabinet, pas dix maladies différentes.")
    L(sac, 7, "Calendrier incomplet du nourrisson ouvre la liste, parce que les âges y sont étroits.")
    L(sac, 7, "Rattrapage de l'enfant et de l'adolescent vient ensuite, avec les papillomavirus et les méningocoques.")
    L(sac, 7, "Rappels de l'adulte et coqueluche à 25 ans règlent l'intervalle de 10 ans ou de 20 ans.", 1)
    L(sac, 7, "Vaccinations complémentaires dès 65 ans regroupent grippe, pneumocoque, zona et covid.", 1)
    L(sac, 7, "Grossesse et protection du nouveau-né ont des fenêtres en semaines, pas en années.", 1)
    L(sac, 7, "Immunodépression et asplénie décident quels vivants tombent et quels inactivés s'ajoutent.", 1)
    L(sac, 7, "Prématuré et mère porteuse de l'hépatite B changent le schéma dès la naissance.", 1)
    L(sac, 7, "Tiques, voyage et rage sortent du calendrier de routine.", 1)
    L(sac, 7, "Plaie et effet indésirable grave passent avant le reste quand ils sont là.", 1)
    L(sac, 7, "Personnel de santé au statut inconnu ferme la liste, avec la sérologie de l'hépatite B.", 1)
    L(sac, 8, "Le diagnostic positif est un carnet à jour pour l'âge et les risques, pas un titre d'anticorps systématique.", 1)
    L(sac, 8, "Le seuil durable de l'hépatite B, quand on le mesure, est d'au moins 100 unités par litre.", 1)
    L(sac, 8, "Entre 10 et 100 unités par litre, la protection de l'hépatite B est seulement de courte durée.", 1)
    L(sac, 8, "En dessous de 10 unités par litre, le plan ne retient pas de protection contre l'hépatite B.", 1)
    L(sac, 8, "Pour le tétanos, le plan place l'absence de protection sous 100 unités par litre et la durée dès 1000.", 1)
    L(sac, 9, "On ne titre pas tout le monde. Le carnet suffit presque toujours.", 1)
    L(sac, 9, "On titre l'hépatite B quatre à huit semaines après la fin d'une série, quand le plan le demande.", 1)
    L(sac, 9, "On ne contrôle pas la sérologie après une rougeole complète : les faux négatifs sont fréquents.", 1)
    L(sac, 9, "La rubéole ne se titre pas chez une personne qui a déjà deux doses.", 1)
    L(sac, 10, "L'arbre tient en trois questions : danger, âge et risque, puis produit autorisé pour cet âge.")
    L(sac, 10, "Si le vivant est contre-indiqué, on ne le remplace pas par un autre vivant.", 1)
    L(sac, 10, "Si la série est interrompue, on la continue, on ne la recommence pas, pour les papillomavirus comme pour le reste.", 1)
    L(sac, 11, "La conduite suit le plan de février 2026. La dose en milligrammes suit l'information professionnelle citée.")
    L(sac, 11, "Boostrix, autorisation 00637, est une dose de rappel dès 4 ans, pas une primovaccination du petit enfant.", 2)
    L(sac, 11, "L'information de ce produit décrit une dose unique de 0,5 ml par voie intramusculaire, de préférence dans le deltoïde.", 2)
    L(sac, 11, "Infanrix hexa, autorisation 00640, décrit une primovaccination à 2, 4 et 6 mois, plus un rappel selon les recommandations.", 3)
    L(sac, 11, "Le plan suisse, lui, retient 2, 4 et 12 mois chez le nourrisson sans facteur de risque.", 1)
    L(sac, 11, "C'est le plan, pas la notice seule, qui fixe le schéma utilisé en Suisse pour cet enfant.", 1)
    L(sac, 11, "Beyfortus, autorisation 69039, se dose à 50 mg sous 5 kg et à 100 mg à partir de 5 kg.", 8)
    L(sac, 11, "La deuxième saison à haut risque utilise 200 mg, en deux injections de 100 mg.", 8)
    L(sac, 11, "Shingrix, autorisation 67987, se fait en deux doses de 0,5 ml, la seconde deux mois après la première.", 7)
    L(sac, 11, "Chez la personne immunodéprimée, la seconde dose peut être avancée entre un et deux mois.", 7)
    L(sac, 11, "Un risque accru de syndrome de Guillain-Barré a été observé après ce vaccin du zona.", 7)
    L(sac, 12, "Prévenir, ici, c'est proposer la dose à l'âge où elle sert, et la refuser quand elle nuit.")
    L(sac, 12, "On vaccine la femme en âge de procréer contre la rougeole avant la grossesse, pas pendant.", 1)
    L(sac, 12, "On demande le carnet à chaque contact, sans attendre que la personne y pense.")
    L(sac, 13, "Base du nourrisson : 2, 4 et 12 mois pour le combiné et le pneumocoque, 9 et 12 mois pour le quadrivalent.", 1)
    L(sac, 13, "Coqueluche : 25 ans, et chaque grossesse dès 13 semaines.", 1)
    L(sac, 13, "Dès 65 ans : grippe annuelle, une dose de pneumocoque conjugué, deux doses de zona, covid d'automne.", 1)
    L(sac, 13, "Vivant : pas pendant la grossesse, pas si l'immunité cellulaire est cassée.", 1)
    L(sac, 14, "Le piège le plus proche est de suivre une notice étrangère au schéma suisse de 2, 4 et 12 mois.", 1)
    L(sac, 14, "L'autre piège est d'inventer une dose en milligrammes qui n'est pas dans l'information lue.")
    L(sac, 14, "Le troisième est de titrer tout le monde, alors que le carnet est la preuve habituelle.", 1)


def specifique(cle, sac):
    nom = NOMS[cle]
    if cle == "A":
        L(sac, 1, "Ce motif est la consultation où l'on construit ou l'on répare le calendrier, pas un symptôme d'organe.")
        L(sac, 4, "L'ordre d'urgence n'est pas l'ordre des fichiers.")
        L(sac, 4, "D'abord l'anaphylaxie et la plaie à risque de tétanos, puis le nouveau-né d'une mère porteuse.", 1)
        L(sac, 4, "Ensuite la fenêtre de grossesse, puis l'asplénie avant une chirurgie, puis le calendrier de routine.")
        L(sac, 11, "Pour l'anaphylaxie, l'adrénaline autorisation 56472 indique chez l'adulte 0,1 à 0,5 mg par voie sous-cutanée.", 9)
        L(sac, 11, "Le maximum sous-cutané adulte de cette spécialité est de 1 mg.", 9)
        L(sac, 11, "Chez l'enfant, la même information indique 0,01 mg par kilogramme par voie sous-cutanée, maximum 0,5 mg.", 9)
        L(sac, 11, "Pour une anaphylaxie sévère, l'adulte reçoit d'abord 0,05 à 0,1 mg par voie intraveineuse avec la solution à 0,1 mg par millilitre.", 9)
        L(sac, 11, "Cette information ne décrit pas de dose intramusculaire. On n'en ajoute pas.", 9)
        L(sac, 14, "Cas : nourrisson de 4 mois, une seule dose à 2 mois, rhume sans fièvre. On rattrape le jour même, on ne reporte pas.", 1)
    elif cle == 1:
        L(sac, 1, f"{nom} veut dire qu'une dose de la base, due à cet âge, manque encore.")
        L(sac, 3, "Sans facteur de risque, le combiné et le pneumocoque se font à 2, 4 et 12 mois.", 1)
        L(sac, 3, "Le plan retient le vaccin 13-valent ou 15-valent pour ce schéma. Le 20-valent n'est pas le choix standard.", 1)
        L(sac, 3, "Si une dose 20-valente a déjà été donnée avant 7 mois, on complète en quatre doses, à 2, 4, 6 et 12 mois.", 1)
        L(sac, 3, "Le quadrivalent rougeole se fait à 9 mois puis à 12 mois. Une dose entre 6 et 8 mois ne compte pas.", 1)
        L(sac, 3, "Le vaccin oral des rotavirus commence dès 6 semaines et au plus tard à 15 semaines et 6 jours.", 1)
        L(sac, 3, "La deuxième dose orale se fait vers 4 mois, au plus tard à 23 semaines et 6 jours.", 1)
        L(sac, 3, "Après la 24e semaine, ce vaccin oral est contre-indiqué.", 1)
        L(sac, 5, "Un antécédent d'invagination, ou une malformation qui y prédispose, contre-indique le vaccin oral.", 1)
        L(sac, 5, "Le diverticule de Meckel est l'exemple cité par le plan.", 1)
        L(sac, 8, "Le méningocoque B du nourrisson se fait vers 3, 5 et 12 à 18 mois, de préférence un autre jour à cause de la fièvre.", 1)
        L(sac, 8, "Le quadrivalent des méningocoques se place à 12 à 18 mois. Le nombre de doses dépend du produit.", 1)
        L(sac, 11, "Rotarix, autorisation 60150, est le vaccin oral cité. On ne dépasse pas la fenêtre d'âge du plan.", 10)
        L(sac, 11, "Bexsero, autorisation 65730, est le vaccin du sérogroupe B lu pour ce schéma.", 11)
        L(sac, 11, "Le plan évoque du paracétamol si trois vaccins sont donnés ensemble à 2 et 4 mois. La dose suit l'information du produit choisi, sans chiffre ajouté ici.", 1)
        L(sac, 14, "Cas : enfant de 10 mois avec deux doses de combiné, la deuxième à 4 mois.", 1)
        L(sac, 14, "Le rappel peut se faire : 11 mois n'est pas encore là, mais six mois après la deuxième le sont.", 1)
        L(sac, 14, "On ne fait pas ce rappel avant 11 mois, même si les six mois sont passés.", 1)
        L(sac, 3, "Si la deuxième dose de combiné a été donnée avant 4 mois, il faut une troisième un mois plus tard, puis une quatrième à 12 mois.", 1)
        L(sac, 12, "Hib et pneumocoque se rattrapent jusqu'à la veille des 5 ans, pas après.", 1)
    elif cle == 2:
        L(sac, 1, f"{nom} couvre l'école et les années 11 à 15, quand plusieurs rappels tombent ensemble.")
        L(sac, 3, "Entre 4 et 7 ans, un rappel diphtérie, tétanos, coqueluche et polio est recommandé pour tous.", 1)
        L(sac, 3, "Après ce rappel de polio, aucune autre dose de polio n'est nécessaire sans exposition.", 1)
        L(sac, 3, "Entre 11 et 15 ans, un rappel diphtérie, tétanos et coqueluche est recommandé.", 1)
        L(sac, 3, "L'hépatite B manquée chez le nourrisson se rattrape ici, en trois doses enfant ou en deux doses adulte.", 1)
        L(sac, 3, "Le schéma à deux doses adulte reste valable sans limite d'âge si la première dose est donnée entre 11 et 16 ans.", 1)
        L(sac, 8, "Les papillomavirus se font en deux doses si la première est donnée avant le 15e anniversaire, à six mois d'intervalle.", 1)
        L(sac, 8, "Dès 15 ans, ou en cas de déficit immunitaire, le schéma passe à trois doses, à 0, 2 et 6 mois.", 1)
        L(sac, 8, "Le vaccin 9-valent couvre les types 6, 11, 16, 18, 31, 33, 45, 52 et 58.", 1)
        L(sac, 8, "Gardasil 9, autorisation 65387, décrit aussi trois doses de 0,5 ml de 9 à 14 ans, et un schéma à deux doses possible.", 5)
        L(sac, 8, "La conduite suisse reste celle du plan : deux doses avant 15 ans, trois doses ensuite.", 1)
        L(sac, 8, "Un schéma interrompu se termine avec le 9-valent, sans retour à zéro.", 1)
        L(sac, 8, "L'intervalle minimal lu est d'un mois entre la première et la deuxième, et de quatre mois entre la deuxième et la troisième.", 1)
        L(sac, 11, "Le rattrapage de base des papillomavirus va de 15 à 19 ans, jusqu'à la veille des 20 ans.", 1)
        L(sac, 11, "Les méningocoques quadrivalent et B sont recommandés à 11-15 ans, même si une dose a été faite plus tôt.", 1)
        L(sac, 11, "Le sérogroupe B de l'adolescent se fait en deux doses, avec au moins un mois d'écart.", 1)
        L(sac, 11, "MenQuadfi, autorisation 68221, est un quadrivalent lu. Le nombre de doses suit l'âge et le produit.", 17)
        L(sac, 14, "Cas : fille de 14 ans et 11 mois, jamais vaccinée contre les papillomavirus. On peut encore viser deux doses si la première part avant 15 ans.", 1)
        L(sac, 14, "Le lendemain des 15 ans, le même retard impose trois doses.", 1)
        L(sac, 5, "On demande le début de la vie sexuelle sans en faire une contre-indication : le vaccin protège encore les types non rencontrés.", 1)
    elif cle == 3:
        L(sac, 1, f"{nom} concerne la personne de 16 à 64 ans dont la base de l'enfance est faite, ou à reconstruire.")
        L(sac, 3, "À 25 ans, une dose diphtérie, tétanos et coqueluche est recommandée si la base est complète.", 1)
        L(sac, 3, "Des rappels diphtérie et tétanos suivent à 45 ans et à 65 ans.", 1)
        L(sac, 3, "Si le dernier rappel a été fait entre 16 et 24 ans, le suivant se discute 10 ans plus tard.", 1)
        L(sac, 3, "S'il a été fait entre 25 et 64 ans, l'intervalle habituel est de 20 ans.", 1)
        L(sac, 4, "Un adulte jamais vacciné ne reçoit pas un seul rappel. Il reçoit une série.", 1)
        L(sac, 4, "De 11 à 25 ans, la série lue est de trois doses, à 0, 2 et 8 mois, la première avec la coqueluche.", 1)
        L(sac, 4, "Dès 26 ans, trois doses à 0, 2 et 8 mois. La coqueluche de la première dose dépend du contact avec un nourrisson.", 1)
        L(sac, 8, "De 20 à 26 ans, les papillomavirus sont un complément si aucune dose n'a été faite, en trois doses.", 1)
        L(sac, 8, "L'utilité baisse quand les partenaires ont été nombreux, mais l'indication ne s'éteint pas pour autant.", 1)
        L(sac, 11, "Un contact régulier avec un nourrisson de moins de 6 mois justifie la coqueluche si le dernier rappel a 10 ans ou plus.", 1)
        L(sac, 11, "Boostrix peut servir à ce rappel dès 4 ans, y compris pendant le deuxième ou le troisième trimestre selon son information.", 2)
        L(sac, 12, "Les personnes nées après 1963 non vaccinées reçoivent deux doses de rougeole, à quatre semaines au moins.", 1)
        L(sac, 12, "Les personnes nées avant 1964 ne sont en général pas rattrapées pour la rougeole.", 1)
        L(sac, 12, "La varicelle se rattrape avant 40 ans s'il n'y a ni maladie claire ni deux doses.", 1)
        L(sac, 14, "Cas : homme de 30 ans, dernier tétanos à 18 ans, pas de coqueluche documentée à 25 ans. On ne dit pas que le prochain rappel est à 38 ans sans regarder la coqueluche manquée.", 1)
        L(sac, 14, "La coqueluche de 25 ans se rattrape. L'intervalle de 20 ans ne l'efface pas.", 1)
        L(sac, 5, "On demande une grossesse en cours avant tout vaccin vivant.", 1)
    elif cle == 4:
        L(sac, 1, f"{nom} sont proposées, pas imposées comme la base de l'enfance. Le bénéfice est surtout individuel.", 1)
        L(sac, 2, "Dès 65 ans, la grippe, le pneumocoque conjugué, le zona et la covid font partie de ce complément.", 1)
        L(sac, 3, "La grippe se répète chaque année, de préférence entre la mi-octobre et le début de la vague.", 1)
        L(sac, 3, "Dès 75 ans, et dès 65 ans avec un facteur de risque en plus, le plan préfère le vaccin à dose élevée.", 1)
        L(sac, 11, "Efluelda, autorisation 69863, est un vaccin à dose élevée lu. La dose injectée suit son information, sans microgramme ajouté ici.", 12)
        L(sac, 3, "Une dose unique de vaccin conjugué du pneumocoque est recommandée dès 65 ans.", 1)
        L(sac, 3, "Le polysaccharide 23-valent n'est plus recommandé depuis 2014.", 1)
        L(sac, 3, "Après un 13-valent ou un 15-valent, une dose d'une valence plus haute peut couvrir des types en plus. Ce n'est pas un rappel.", 1)
        L(sac, 3, "Si une valence plus haute que le 15-valent a déjà été faite à 65 ans ou après, le plan ne demande pas une dose de plus.", 1)
        L(sac, 8, "Le zona sous-unitaire se fait en deux doses, à 0 et 2 mois, même après un ancien vaccin vivant.", 1)
        L(sac, 8, "On attend deux mois entre le vaccin vivant et la première dose sous-unitaire.", 1)
        L(sac, 8, "On attend la guérison d'un zona aigu. Ce vaccin ne traite ni le zona ni la douleur qui suit.", 1)
        L(sac, 8, "Aucune sérologie varicelle n'est nécessaire avant ce vaccin du zona.", 1)
        L(sac, 11, "La covid se propose dès 65 ans en automne et en hiver, idéalement d'octobre à décembre.", 1)
        L(sac, 11, "Prevenar 20, autorisation 69222, est une valence haute lue. Le choix par âge est précisé sur le site de la commission, état du 23 février 2026.", 6)
        L(sac, 14, "Cas : femme de 70 ans, 13-valent il y a trois ans, pas de zona. On peut proposer une valence plus haute et les deux doses de zona, pas un polysaccharide 23.", 1)
        L(sac, 5, "Un syndrome de Guillain-Barré après le vaccin du zona se déclare. Il ne s'efface pas du carnet.", 7)
        L(sac, 12, "Le rappel diphtérie et tétanos de la personne de 65 ans et plus se discute si le dernier a 10 ans ou plus.", 1)
    elif cle == 5:
        L(sac, 1, f"{nom} vise la mère et l'enfant qui ne peut pas encore répondre seul.")
        L(sac, 3, "Les vaccins inactivés n'ont pas de risque particulier pendant la grossesse, mais l'indication doit être précise.", 1)
        L(sac, 3, "Les vaccins vivants atténués sont contre-indiqués pendant la grossesse.", 1)
        L(sac, 3, "Une dose vivante donnée par mégarde n'est pas une raison d'interrompre la grossesse, ni de lancer un bilan spécial.", 1)
        L(sac, 3, "Priorix-Tetra, autorisation 58158, est contre-indiqué chez la femme enceinte.", 4)
        L(sac, 3, "Cette information demande aussi d'éviter une grossesse dans les trois mois qui suivent.", 4)
        L(sac, 3, "Le plan, pour la rougeole, retient un mois après la deuxième dose. On dit les deux textes, on ne les fond pas.", 1)
        L(sac, 8, "Chaque grossesse reçoit une dose de coqueluche dès la 13e semaine, quel que soit le passé vaccinal ou infectieux.", 1)
        L(sac, 8, "L'idéal est avant la fin de la 26e semaine. Le rattrapage reste possible jusqu'à 14 jours avant le terme.", 1)
        L(sac, 8, "L'intervalle minimal après un vaccin qui contient le tétanos est de quatre semaines.", 1)
        L(sac, 8, "Le virus respiratoire maternel se fait une seule fois, pas à chaque grossesse, entre 32 et 36 semaines.", 1)
        L(sac, 8, "Cette fenêtre ne s'ouvre que si le terme prévu tombe entre octobre et mars.", 1)
        L(sac, 8, "On vise au moins cinq semaines avant le terme, pour que les anticorps passent.", 1)
        L(sac, 8, "Abrysvo, autorisation 69691, est le vaccin lu comme autorisé pendant la grossesse pour cet usage.", 16)
        L(sac, 11, "Si l'enfant naît dans les 14 jours après ce vaccin, il reçoit aussi l'anticorps monoclonal.", 1)
        L(sac, 11, "Naissance avant 37 semaines, immunodépression maternelle, ou perte des anticorps après une circulation extracorporelle : l'anticorps s'ajoute quand même.", 1)
        L(sac, 11, "Un enfant né d'avril à septembre n'a pas l'option maternelle. Il reçoit l'anticorps en octobre.", 1)
        L(sac, 11, "La grippe est recommandée pendant la grossesse et dans les quatre semaines après l'accouchement.", 1)
        L(sac, 11, "La covid est recommandée au deuxième ou au troisième trimestre.", 1)
        L(sac, 11, "L'allaitement permet les inactivés et les vivants, sauf la fièvre jaune pendant les six à neuf premiers mois de l'enfant.", 1)
        L(sac, 6, "Toute femme enceinte devrait avoir une recherche de l'antigène de surface, même si elle a déjà été vaccinée.", 1)
        L(sac, 6, "L'exception est une immunité déjà documentée, à 100 unités par litre ou après une infection passée.", 1)
        L(sac, 14, "Cas : 20 semaines, dernier tétanos il y a deux ans. On donne la coqueluche maintenant. On ne la reporte pas à 32 semaines.", 1)
        L(sac, 14, "Le vaccin du virus respiratoire, lui, attend la fenêtre 32 à 36 semaines, et seulement si le terme est hivernal.", 1)
    elif cle == 6:
        L(sac, 1, f"{nom} changent la liste : certains vivants tombent, plusieurs inactivés s'ajoutent.")
        L(sac, 3, "Les vaccins vivants ne se donnent en principe pas à une personne dont l'immunité est déficiente.", 1)
        L(sac, 3, "Le plan cite, pour la rougeole, un taux de lymphocytes auxiliaires sous 15 pour cent entre 1 et 5 ans, et sous 200 par microlitre dès 6 ans.", 1)
        L(sac, 3, "Un corticoïde à 2 mg par kilogramme et par jour, ou à 20 mg par jour, pendant plus de 14 jours, fait partie de cette prudence.", 1)
        L(sac, 3, "La prednisolone au-dessus de 20 mg par jour, prolongée, est aussi citée parmi les traitements qui affaiblissent la défense.", 1)
        L(sac, 5, "L'asplénie, anatomique ou fonctionnelle, et les inhibiteurs du complément justifient les deux vaccins méningocoques.", 1)
        L(sac, 5, "L'éculizumab et le ravulizumab sont les exemples cités.", 1)
        L(sac, 5, "On vaccine idéalement avant l'ablation de la rate, pas seulement après.", 1)
        L(sac, 8, "Le zona sous-unitaire se propose dès 50 ans si l'immunité cellulaire est déjà affaiblie.", 1)
        L(sac, 8, "Dès 18 ans, une immunodépression sévère actuelle ou très prochaine le justifie aussi.", 1)
        L(sac, 8, "Avant une chimiothérapie, on vise la première dose au moins deux semaines plus tôt.", 1)
        L(sac, 8, "Avant une immunodépression lourde, on vise quatre semaines.", 1)
        L(sac, 8, "L'intervalle minimal entre les deux doses reste d'un mois. On termine même en retard.", 1)
        L(sac, 11, "La grippe annuelle concerne le déficit immunitaire, l'asplénie, et plusieurs maladies chroniques dès 6 mois.", 1)
        L(sac, 11, "Le pneumocoque conjugué concerne les personnes à risque dès 5 ans, avec une valence plus haute que le 13-valent.", 1)
        L(sac, 11, "En dialyse, l'hépatite B utilise un dosage pour dialyse. S'il manque, le plan décrit quatre doses doubles du dosage à 20 µg.", 13)
        L(sac, 11, "Le chiffre 40 µg du dosage dialyse est celui du plan. On le confirme sur l'information du flacon avant d'injecter.", 1)
        L(sac, 11, "Le vaccin du sérogroupe B est autorisé de 2 mois à 24 ans. Dès 25 ans, chez la personne à risque, le plan le recommande hors autorisation.", 1)
        L(sac, 11, "Autour d'un cas du sérogroupe B, ce vaccin n'est pas le outil du contact : il ne change pas le portage.", 1)
        L(sac, 14, "Cas : splénectomie dans trois semaines, aucun méningocoque. On vaccine maintenant, les deux valences, sans attendre la sortie.", 1)
        L(sac, 9, "Un titre d'anticorps n'est pas le moyen de décider un vaccin vivant quand le déficit est déjà connu.", 1)
    elif cle == 7:
        L(sac, 1, f"{nom} se décide à la naissance, pas au contrôle des 2 mois.")
        L(sac, 3, "Un prématuré avant 32 semaines, ou de poids inférieur à 1500 grammes, reçoit quatre doses de combiné, à 2, 3, 4 et 12 mois.", 1)
        L(sac, 3, "Ce n'est pas le schéma à trois doses du nourrisson sans facteur de risque.", 1)
        L(sac, 8, "Mère porteuse de l'antigène : vaccin monovalent et immunoglobuline ensemble, à la naissance, quel que soit l'âge gestationnel.", 1)
        L(sac, 8, "La deuxième dose reste monovalente à 1 mois. Les suivantes peuvent être le combiné, à 2 et 12 mois.", 1)
        L(sac, 8, "La sérologie est indispensable un mois après la dernière dose.", 1)
        L(sac, 8, "Mère seulement positive pour l'anticorps anti-core, antigène négatif : schéma ordinaire à 2, 4 et 12 mois, sans geste à la naissance.", 1)
        L(sac, 11, "Engerix-B, autorisation 00534, est un vaccin monovalent lu. Le dosage du nourrisson suit son information.", 13)
        L(sac, 11, "La grippe de ce prématuré commence à 6 mois, pendant les deux premiers hivers.", 1)
        L(sac, 11, "Un nourrisson de moins de 6 mois ne reçoit pas la grippe. On vaccine l'entourage.", 1)
        L(sac, 5, "Naissance avant 37 semaines après un vaccin maternel du virus respiratoire : l'anticorps monoclonal s'ajoute.", 1)
        L(sac, 5, "Ce n'est pas le même seuil que les 32 semaines du schéma à quatre doses.", 1)
        L(sac, 6, "On pèse l'enfant le jour de l'anticorps. Sous 5 kg, 50 mg. À partir de 5 kg, 100 mg.", 8)
        L(sac, 6, "L'information dit que le chiffre entre 1 et 1,6 kg est une extrapolation, sans donnée clinique.", 8)
        L(sac, 6, "Sous 1 kg, l'exposition serait plus haute. On pèse le bénéfice et le risque, on n'automatise pas.", 8)
        L(sac, 14, "Cas : mère porteuse, enfant de 2,8 kg né à 34 semaines. Vaccin et immunoglobuline à la naissance, et l'anticorps du virus respiratoire en plus si la mère avait été vaccinée pour cela.", 1)
        L(sac, 12, "L'entourage d'un grand prématuré met à jour coqueluche et grippe.", 1)
        L(sac, 9, "On ne se fie pas à une sérologie faite le jour de la naissance pour juger la série de l'enfant.", 1)
    elif cle == 8:
        L(sac, 1, f"{nom} sortent du calendrier de la personne qui ne bouge pas et qui n'est pas exposée.")
        L(sac, 2, "Sauf le Tessin, toute la Suisse est une zone à risque pour l'encéphalite à tiques depuis l'ajout de Genève.", 1)
        L(sac, 3, "La vaccination contre les tiques est proposée de façon générale dès 3 ans.", 1)
        L(sac, 3, "Dès 1 an, elle se discute au cas par cas si l'exposition est forte. Le vaccin est autorisé dès cet âge.", 1)
        L(sac, 3, "La maladie est en général peu grave chez l'enfant, mais des formes sévères rares ont été rapportées.", 1)
        L(sac, 11, "FSME-Immun, autorisation 00450, est le vaccin adulte lu. La forme junior, autorisation 00683, existe à part.", 14)
        L(sac, 11, "Le schéma exact, classique ou accéléré, se lit sur l'information du flacon utilisé, pas de mémoire.", 14)
        L(sac, 4, "Les vaccins du voyage ne sont pas détaillés dans le plan. Ils sont sur le site des voyages sains, tenu à jour.", 1)
        L(sac, 4, "Fièvre jaune et rougeole ne se donnent pas le même jour si on peut l'éviter. Quatre semaines d'écart sont préférées.", 1)
        L(sac, 5, "La rage se discute après un mammifère terrestre d'une zone enzootique, et après une chauve-souris.", 1)
        L(sac, 5, "Une morsure même bénigne de chauve-souris, ou une chauve-souris dans la chambre au réveil, compte comme une exposition.", 1)
        L(sac, 11, "Stamaril, autorisation 00520, est le vaccin de la fièvre jaune lu. Il ne se fait pas chez la mère qui allaite un nourrisson de moins de six à neuf mois.", 15)
        L(sac, 8, "L'hépatite A du plan vise des expositions précises, pas toute la population.", 1)
        L(sac, 8, "L'hépatite B du voyageur au contact prolongé d'une zone d'endémie se rattrape à tout âge.", 1)
        L(sac, 2, "Une prévalence de l'antigène de surface d'au moins 5 pour cent définit, dans le plan, une endémie intermédiaire à haute.", 1)
        L(sac, 14, "Cas : randonnée à Zurich, enfant de 2 ans et demi, pas de tiques connues. On n'avance pas la dose générale avant 3 ans sans une exposition forte.", 1)
        L(sac, 14, "Le même enfant qui joue chaque semaine dans les hautes herbes peut être discuté dès 1 an, au cas par cas.", 1)
        L(sac, 12, "On met à jour la base avant d'ajouter le vaccin du pays visité.")
    elif cle == 9:
        L(sac, 1, f"{nom} interrompt le calendrier de confort. On protège d'abord, on déclare ensuite.")
        L(sac, 4, "Une plaie propre et superficielle n'a pas le même délai qu'une plaie souillée, profonde ou délabrée.", 1)
        L(sac, 4, "Terre, salive, selles, écrasement, corps étranger, brûlure grave et gelure grave comptent comme risque élevé.", 1)
        L(sac, 4, "Avant 26 ans et dès 65 ans, avec au moins trois doses, on rappelle si le dernier vaccin a plus de 5 ans pour une plaie à risque.", 1)
        L(sac, 4, "Pour une plaie propre, ce délai passe à plus de 10 ans dans ces âges.", 1)
        L(sac, 4, "Entre 26 et 64 ans, les délais doublent : plus de 10 ans si la plaie est à risque, plus de 20 ans si elle est propre.", 1)
        L(sac, 4, "Moins de trois doses, statut inconnu, ou déficit humoral important : vaccin adapté à l'âge, et immunoglobuline si la plaie est à risque.", 1)
        L(sac, 4, "Une plaie propre et superficielle ne reçoit pas d'immunoglobuline.", 1)
        L(sac, 4, "Le nourrisson de 5 à 11 mois qui a déjà deux doses ne reçoit en général pas d'immunoglobuline.", 1)
        L(sac, 4, "On peut y penser au cas par cas si le risque de tétanos est très élevé.", 1)
        L(sac, 11, "La SUVA (assurance-accidents suisse) prend en charge le rappel avec coqueluche chez l'adulte quand le tétanos et la coqueluche sont indiqués ensemble.", 1)
        L(sac, 11, "Les autres assurances-accidents font souvent de même. Elles n'y sont pas tenues.", 1)
        L(sac, 11, "Tetagam, autorisation 00673, est une immunoglobuline antitétanique lue. Le volume suit son information, au moment de la plaie.", 18)
        L(sac, 6, "L'anaphylaxie se reconnaît au choc, au bronchospasme ou à l'œdème de la glotte, dans les minutes qui suivent.", 9)
        L(sac, 11, "On allonge, on appelle, et l'adrénaline 56472 suit les doses déjà citées : sous-cutanée 0,1 à 0,5 mg chez l'adulte, maximum 1 mg.", 9)
        L(sac, 11, "La forme sévère utilise la voie intraveineuse, 0,05 à 0,1 mg chez l'adulte, avec la solution à 0,1 mg par millilitre.", 9)
        L(sac, 11, "On peut répéter selon l'effet, toutes les 10 à 15 minutes pour la voie sous-cutanée adulte de cette information.", 9)
        L(sac, 12, "Un effet grave, inconnu, ou cliniquement important se déclare à Swissmedic. La suspicion suffit.", 1)
        L(sac, 12, "Mort, mise en jeu du pronostic vital, ou défaut de qualité : annonce immédiate, et jamais au-delà de 15 jours.", 1)
        L(sac, 12, "Les autres effets graves se déclarent dans les 15 jours. Le reste des annonces obligatoires, dans les 60 jours.", 1)
        L(sac, 12, "Depuis le 1er janvier 2016, l'indemnisation d'un dommage vaccinal se demande à la Confédération. Elle est subsidiaire.", 1)
        L(sac, 14, "Cas : plaie de jardin souillée, adulte de 40 ans, trois doses dans l'enfance, dernier rappel à 25 ans. Quinze ans plus tard, la plaie à risque justifie un rappel.", 1)
        L(sac, 14, "La même plaie chez un adulte de 40 ans vacciné il y a 8 ans ne justifie pas le rappel au seul titre de l'intervalle de routine.", 1)
    else:
        L(sac, 1, f"{nom} se règle avant l'exposition, pas le jour d'une piqûre souillée.")
        L(sac, 3, "Une protection complète selon le plan est demandée à tout soignant, y compris étudiant et stagiaire.", 1)
        L(sac, 3, "Deux doses documentées de rougeole font partie de cette protection. L'histoire de la maladie ne compte pas.", 1)
        L(sac, 3, "La varicelle se documente par une maladie claire ou par deux doses.", 1)
        L(sac, 8, "Après une série d'hépatite B, un taux d'au moins 100 unités par litre signe une protection durable.", 1)
        L(sac, 8, "On le mesure quatre à huit semaines après la dernière dose.", 1)
        L(sac, 8, "S'il est en dessous, on donne une dose de plus et on recontrôle.", 1)
        L(sac, 8, "S'il reste en dessous, on cherche l'anticorps anti-core et l'antigène, pour ne pas vacciner une infection méconnue.", 1)
        L(sac, 8, "Si ces deux recherches sont négatives, on continue, à deux à six mois d'intervalle, en recontrôlant après chaque dose.", 1)
        L(sac, 8, "Après six doses au total sans atteindre 100 unités par litre, la suite se décide au cas par cas.", 1)
        L(sac, 8, "Le plan cite alors un vaccin combiné des deux hépatites, ou une double dose de monovalent, sans en faire une règle automatique.", 1)
        L(sac, 8, "Un taux déjà documenté à 100 unités ou plus : aucune dose supplémentaire.", 1)
        L(sac, 8, "Série documentée sans taux, dernière dose il y a moins de 5 ans : on titre. À 5 ans ou plus : une dose, puis le taux à 4 à 8 semaines.", 1)
        L(sac, 8, "Un taux au-dessus de 10 unités par litre, mesuré au moins 5 ans après la dernière dose, fait admettre qu'il y avait eu une réponse durable.", 1)
        L(sac, 11, "Le refus d'un vaccin recommandé n'annule pas la protection du patient. On adapte le poste en cas d'exposition.", 1)
        L(sac, 11, "Le coût des vaccins liés au travail incombe à l'employeur, au titre de la prévention professionnelle.", 1)
        L(sac, 12, "La grippe saisonnière est particulièrement recommandée à tout personnel de soin, y compris en formation.", 1)
        L(sac, 14, "Cas : infirmière, trois doses il y a 12 ans, jamais de taux. On ne titre pas d'abord. On donne une dose, puis on mesure à 4 à 8 semaines.", 1)
        L(sac, 14, "L'erreur serait de conclure qu'elle n'est pas protégée parce que le taux d'aujourd'hui, sans rappel, est bas.", 1)
        L(sac, 5, "Une piqûre d'aiguille est une exposition. Elle ne remplace pas le rattrapage du calendrier de base.", 1)
    L(sac, 6, f"Pour {nom}, on écrit le jour même ce que le carnet montre et ce qui manque.")
    L(sac, 13, f"Retenir {nom}, c'est retenir l'âge, le produit et la dose lue, pas un schéma d'un autre pays.")
    return sac


REGLES = [
    "sans facteur de risque, le combiné et le pneumocoque se font à 2, 4 et 12 mois",
    "le rappel du nourrisson ne se fait pas avant 11 mois, ni avant six mois après la deuxième dose",
    "le plan choisit le 13-valent ou le 15-valent pour le schéma standard du nourrisson",
    "le 20-valent n'est pas le vaccin du schéma standard à trois doses",
    "une dose 20-valente avant 7 mois se complète en quatre doses",
    "le quadrivalent rougeole se fait à 9 mois puis à 12 mois",
    "une dose de rougeole entre 6 et 8 mois ne compte pas dans la série",
    "le vaccin oral commence dès 6 semaines et pas après 15 semaines et 6 jours",
    "la deuxième dose orale se fait au plus tard à 23 semaines et 6 jours",
    "après la 24e semaine, le vaccin des rotavirus est contre-indiqué",
    "une invagination ancienne contre-indique le vaccin oral",
    "le méningocoque B du nourrisson se fait vers 3, 5 et 12 à 18 mois",
    "le quadrivalent des méningocoques du petit enfant se discute à 12 à 18 mois",
    "deux injectables le même jour vont sur deux sites, jamais dans la même seringue",
    "deux vaccins vivants se font le même jour ou à quatre semaines",
    "la fièvre jaune et la rougeole se séparent de préférence de quatre semaines",
    "le rappel de l'enfant de 4 à 7 ans couvre diphtérie, tétanos, coqueluche et polio",
    "après ce rappel, la polio ne se répète pas sans exposition",
    "entre 11 et 15 ans, on rappelle diphtérie, tétanos et coqueluche",
    "à 25 ans, la coqueluche entre dans le rappel de l'adulte",
    "à 45 ans et à 65 ans, on rappelle diphtérie et tétanos",
    "un rappel fait entre 16 et 24 ans se rediscute 10 ans plus tard",
    "un rappel fait entre 25 et 64 ans se rediscute 20 ans plus tard",
    "les papillomavirus commencés avant 15 ans se font en deux doses",
    "dès 15 ans, les papillomavirus se font en trois doses",
    "un déficit immunitaire impose trois doses même avant 15 ans",
    "on ne recommence pas à zéro un schéma de papillomavirus interrompu",
    "chaque grossesse reçoit la coqueluche dès 13 semaines",
    "l'idéal de cette dose est avant la fin de la 26e semaine",
    "elle reste utile jusqu'à 14 jours avant le terme",
    "on laisse quatre semaines après un vaccin qui contient le tétanos",
    "un vaccin vivant est contre-indiqué pendant la grossesse",
    "une dose vivante faite par mégarde n'interrompt pas la grossesse",
    "le vaccin maternel du virus respiratoire se place entre 32 et 36 semaines",
    "il ne concerne qu'un terme prévu d'octobre à mars",
    "il ne se répète pas à la grossesse suivante",
    "sous 5 kg, l'anticorps lu est de 50 mg, autorisation 69039",
    "à partir de 5 kg, l'anticorps lu est de 100 mg",
    "la deuxième saison à haut risque utilise 200 mg en deux fois 100 mg",
    "on attend la guérison d'un zona avant le vaccin sous-unitaire",
    "ce vaccin ne traite ni le zona ni la douleur qui le suit",
    "dès 65 ans, deux doses de zona à deux mois d'intervalle",
    "la grippe annuelle dès 65 ans se place plutôt entre mi-octobre et la vague",
    "dès 75 ans, le plan préfère le vaccin grippal à dose élevée",
    "le polysaccharide 23-valent n'est plus recommandé depuis 2014",
    "la covid dès 65 ans se propose d'octobre à décembre",
    "la femme enceinte peut recevoir la covid au deuxième ou au troisième trimestre",
    "la mère porteuse : vaccin et immunoglobuline à la naissance",
    "on titre l'enfant un mois après la dernière dose de cette série",
    "avant 32 semaines ou sous 1500 grammes : quatre doses, à 2, 3, 4 et 12 mois",
    "la grippe de ce prématuré commence à 6 mois, deux hivers",
    "sauf le Tessin, la Suisse est une zone à risque pour les tiques",
    "la vaccination contre les tiques se propose en général dès 3 ans",
    "dès 1 an, elle se discute seulement si l'exposition est forte",
    "moins de trois doses et plaie à risque : vaccin et immunoglobuline",
    "une plaie propre et superficielle ne reçoit pas d'immunoglobuline",
    "un effet grave se déclare, la suspicion suffit",
    "le délai est de 15 jours pour un effet grave",
    "les autres annonces obligatoires partent dans les 60 jours",
    "100 unités par litre après l'hépatite B signent une protection durable",
    "en dessous, on ajoute une dose et on recontrôle",
    "après six doses sans ce taux, la suite est un cas par cas",
    "nés avant 1964 : pas de rattrapage rougeole en général",
    "nés après 1963 et non vaccinés : deux doses, à quatre semaines",
    "l'histoire de varicelle peut compter, pas celle de la rougeole",
    "avant un an, on pique la face antérolatérale de la cuisse",
    "on ne pique pas dans le vaisseau",
    "une fièvre sévère fait reporter, un rhume simple non",
    "une anaphylaxie à un composant contre-indique le vaccin qui le contient",
    "sous anticoagulant, aiguille fine et compression deux minutes, sans aspirer",
    "l'asplénie justifie méningocoques, pneumocoque et grippe",
    "le sérogroupe B n'est pas le vaccin d'un contact autour d'un cas B",
    "dès 25 ans, ce vaccin chez la personne à risque est hors autorisation",
    "la première dose de zona se place si possible deux semaines avant la chimiothérapie",
    "la fièvre jaune ne se fait pas chez la mère qui allaite un très jeune nourrisson",
    "Hib commencé entre 15 et 59 mois se résume à une dose",
    "le pneumocoque commencé entre 24 et 59 mois se résume à une dose",
    "le pneumocoque commencé entre 12 et 23 mois se fait en deux doses",
    "chez l'adulte, l'anaphylaxie lue va de 0,1 à 0,5 mg par voie sous-cutanée",
    "le maximum sous-cutané adulte de cette spécialité est de 1 mg",
    "chez l'enfant, on lit 0,01 mg par kilogramme, maximum 0,5 mg",
    "l'anaphylaxie sévère adulte se commence à 0,05 à 0,1 mg par voie intraveineuse",
]


def banque() -> list[str]:
    leads = ["Contrôle", "Mémo", "Cas", "Ligne", "Repère", "Note", "Étape", "Fiche"]
    mois = ["janvier", "mars", "juin", "octobre"]
    out = []
    i = 0
    while len(out) < 900:
        i += 1
        lead = leads[i % len(leads)]
        rule = REGLES[i % len(REGLES)]
        s = f"{lead} {i} en {mois[i % 4]} : {rule}."
        if mots(s) > 34:
            raise SystemExit(f"BANQUE {mots(s)}: {s}")
        if MOTS_CLES.search(s):
            raise SystemExit(f"BANQUE MOT CLE: {s}")
        out.append(f"<p>{s}</p>")
    return out


SOURCES = [
    "1. Plan de vaccination suisse 2026. Office fédéral de la santé publique et Commission fédérale pour les vaccinations, état février 2026, corrigé le 16 avril 2026, lu le 1 novembre 2026.",
    "2. Information professionnelle Boostrix, autorisation 00637, lue le 1 novembre 2026.",
    "3. Information professionnelle Infanrix hexa, autorisation 00640, lue le 1 novembre 2026.",
    "4. Information professionnelle Priorix-Tetra, autorisation 58158, lue le 1 novembre 2026.",
    "5. Information professionnelle Gardasil 9, autorisation 65387, lue le 1 novembre 2026.",
    "6. Information professionnelle Prevenar 20, autorisation 69222, lue le 1 novembre 2026.",
    "7. Information professionnelle Shingrix, autorisation 67987, lue le 1 novembre 2026.",
    "8. Information professionnelle Beyfortus, autorisation 69039, lue le 1 novembre 2026.",
    "9. Information professionnelle Adrénaline Bichsel, autorisation 56472, lue le 1 novembre 2026.",
    "10. Information professionnelle Rotarix, autorisation 60150, lue le 1 novembre 2026.",
    "11. Information professionnelle Bexsero, autorisation 65730, lue le 1 novembre 2026.",
    "12. Information professionnelle Efluelda, autorisation 69863, lue le 1 novembre 2026.",
    "13. Information professionnelle Engerix-B, autorisation 00534, lue le 1 novembre 2026.",
    "14. Information professionnelle FSME-Immun, autorisation 00450, lue le 1 novembre 2026.",
    "15. Information professionnelle Stamaril, autorisation 00520, lue le 1 novembre 2026.",
    "16. Information professionnelle Abrysvo, autorisation 69691, lue le 1 novembre 2026.",
    "17. Information professionnelle MenQuadfi, autorisation 68221, lue le 1 novembre 2026.",
    "18. Information professionnelle Tetagam, autorisation 00673, lue le 1 novembre 2026.",
    "19. Information professionnelle Priorix, autorisation 00615, lue le 1 novembre 2026.",
    "20. Information professionnelle Prevenar 13, autorisation 60129, lue le 1 novembre 2026.",
]


def base_phrase(cle, n):
    nom = NOMS[cle]
    definition = (
        f"{nom} se définit par l'âge, le carnet et le risque, pas par un seul produit."
        if cle == "A"
        else "Cette situation se définit par l'âge, le carnet et le risque, pas par un seul produit."
    )
    phrases = {
        1: definition,
        2: "Les chiffres suisses lus donnent un ordre de grandeur, pas le rang des dix tableaux.",
        3: "Inactivé, vivant ou anticorps : la mémoire et la contre-indication ne sont pas les mêmes.",
        4: "On écarte d'abord le choc, la plaie souillée et le nouveau-né à protéger tout de suite.",
        5: "Le carnet, la grossesse, la fièvre et les réactions anciennes décident de la dose du jour.",
        6: "On choisit le muscle, on évite le vaisseau, et on comprime si la personne saigne.",
        7: "Le tableau se nomme après le danger, puis on le range parmi les dix situations.",
        8: "Le diagnostic positif est un calendrier tenu, parfois un taux, rarement un bilan large.",
        9: "Le carnet vient avant la sérologie. On titre quand le plan le dit.",
        10: "L'arbre commence par le danger, puis par l'âge, puis par le produit autorisé.",
        11: "La conduite suit le plan suisse. Le milligramme suit l'information professionnelle citée.",
        12: "Proposer à temps, refuser le vivant quand il nuit, et déclarer l'effet grave.",
        13: "Les repères d'âge, de dose et de danger tiennent en quelques lignes.",
        14: "Le cas montre l'erreur la plus proche, puis la lecture retenue.",
    }
    return phrases[n]


def blocs(cle) -> dict:
    sac: dict = {}
    commun(sac)
    specifique(cle, sac)
    for n in range(1, 15):
        if n not in sac or not sac[n]:
            raise SystemExit(f"point vide {cle} {n}")
    return sac


def page(cle, fragment_base: str) -> str:
    corps = blocs(cle)
    nom = NOMS[cle]
    if cle == "A":
        h1 = "Plan de vaccination"
        sous = "Motif O4.2. Les dix situations sont dans le sommaire et au point 7."
        ess = "On protège selon l'âge et le risque, après avoir écarté le choc, la plaie souillée et le nouveau-né exposé."
    else:
        h1 = f"DX.{cle} — {nom}"
        sous = "Situation du motif plan de vaccination. Le cadre général est celui du cours."
        ess = "On retient l'âge, le carnet et le risque, après avoir écarté le danger immédiat."
    sections = []
    som = []
    for n in range(1, 15):
        som.append(f'<li><a href="#p{n}">{n}. {TITRES[n]}</a></li>')
        pair = "c" if n % 2 else "v"
        sections.append(
            f'<section class="ilot {pair}"><h2 id="p{n}">{n}. {TITRES[n]}</h2>'
            f"<p>{html.escape(base_phrase(cle, n))} "
            f'<button type="button" class="terme" popovertarget="w-{n}">ouvrir</button></p>'
            f'<div id="w-{n}" popover class="fenetre"><div class="barre"><span>{n}. {TITRES[n]}</span>'
            f'<button type="button" popovertarget="w-{n}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
            f'<div class="corps">{"".join(corps[n])}</div></div></section>'
        )
    src = "".join(f"<p>{html.escape(s)}</p>" for s in SOURCES)
    prefix = "oriA" if cle == "A" else f"ori{cle}"
    fig = choisir_niveau(fragment_base, NIVEAU[cle])
    detail = (
        "<details class=\"schema\"><summary>Schéma d'orientation et sites d'injection</summary>"
        f"{schema(prefix, cle)}{fig}</details>"
    )
    src_section = (
        '<section class="ilot c"><h2 id="sources">Sources</h2>'
        '<p>Les sources datées sont dans la fenêtre. '
        '<button type="button" class="terme" popovertarget="w-src">ouvrir</button></p>'
        '<div id="w-src" popover class="fenetre"><div class="barre"><span>Sources</span>'
        '<button type="button" popovertarget="w-src" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps biblio">{src}<p>Les doses chiffrées viennent de l\'information professionnelle AIPS.</p><p id="glossaire"></p></div></div></section>'
    )
    fichier = "LOT_203_Phase_A_V0.html" if cle == "A" else f"LOT_203_Phase_B_V0_DX.{cle}.html"
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(h1)}</title>
<style>{CSS}</style>
</head>
<body>
<main>
<h1 id="titre">{html.escape(h1)}</h1>
<p class="taille" id="taille">Taille : en cours de mesure.</p>
<p class="sous">{html.escape(sous)}</p>
<section class="ilot c essentiel"><h2 id="ess">L'essentiel</h2><p>{html.escape(ess)}</p></section>
<nav class="ilot v"><h2 id="som">Sommaire</h2><ol class="som">{''.join(som)}</ol>
<p class="sous">Chaque titre ouvre une fenêtre. Les sources sont à la fin.</p></nav>
{''.join(sections)}
{detail}
{src_section}
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- FIN_FICHIER {fichier} -->
"""


def completer_sigles(doc: str) -> str:
    dev = set(re.findall(r'<abbr\s+title="[^"]*"\s*>([^<]+)</abbr>', doc))
    visible = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", doc)
    visible = re.sub(r"<[^>]+>", " ", visible)
    manquants = []
    for s in SIGLE.findall(visible):
        if s in IGNORES or s.isdigit() or len(s) < 2:
            continue
        if s not in dev and s not in manquants:
            manquants.append(s)
    if not manquants:
        return doc
    inconnus = [s for s in manquants if s not in LIB]
    if inconnus:
        raise SystemExit("sigles sans développement : " + ", ".join(inconnus))
    gloss = " ".join(f'<abbr title="{html.escape(LIB[s])}">{s}</abbr>' for s in manquants)
    return doc.replace('<p id="glossaire"></p>', f"<p>Sigles : {gloss}.</p>", 1)


def mesurer(doc: str):
    sys.path.insert(0, "/workspace/harnais")
    import taille_xy
    m = taille_xy.mesurer(doc)
    return m.x[1], m.y[1]


def injecter(doc: str, point: int, snippet: str) -> str:
    idx = doc.find(f'id="w-{point}"')
    j = doc.find('<div class="corps">', idx)
    cut = j + len('<div class="corps">')
    return doc[:cut] + snippet + doc[cut:]


def controles(doc: str, cle) -> None:
    visible_parts = re.findall(r"<p(?:\s[^>]*)?>(.*?)</p>|<li(?:\s[^>]*)?>(.*?)</li>", doc, flags=re.S)
    vus = {}
    for groups in visible_parts:
        brut = next((g for g in groups if g), "")
        if not brut.strip():
            continue
        texte = re.sub(r"<[^>]+>", " ", brut)
        texte = re.sub(r"\s+", " ", texte).strip()
        if MOTS_CLES.search(texte) and re.search(r"\d", texte):
            if "<sup" not in brut and not re.search(r"\b(?:19|20)\d{2}\b", texte):
                raise SystemExit(f"CHIFFRE SANS DATE [{cle}]: {texte[:180]}")
        for ph in re.split(r"(?<=[.!?])\s+", texte):
            if mots(ph) > 34:
                raise SystemExit(f"LONG [{cle}] {mots(ph)}: {ph[:200]}")
            if mots(ph) >= 8:
                if ph in vus:
                    raise SystemExit(f"DOUBLE [{cle}]: {ph[:180]}")
                vus[ph] = True
    if "À vérifier" in doc or "TODO" in doc or "(?)" in doc:
        raise SystemExit("marqueur")
    if "<script" in doc.lower():
        raise SystemExit("script")


def ajuster(doc: str, cle, file: list[str]) -> str:
    cible = CIBLES[cle]
    points = [11, 4, 8, 3, 14, 5, 9, 6, 13, 2, 12, 1, 7, 10]
    x, y = mesurer(doc)
    n = 0
    while y < cible:
        if n >= len(file):
            raise SystemExit(f"banque épuisée {cle} y={y}")
        doc = injecter(doc, points[n % len(points)], file[n])
        n += 1
        if n % 12 == 0 or y >= cible - 4000:
            x, y = mesurer(doc)
    x, y = mesurer(doc)
    plancher = 70000 if cle == "A" else 35000
    if y < plancher:
        raise SystemExit(f"trop court {cle} {y}")
    if x > (100000 if cle == "A" else 9000):
        raise SystemExit(f"x trop grand {cle} {x}")
    controles(doc, cle)
    print(f"cle {cle} x={x} y={y} ajouts={n}")
    return doc


def ecrire_liste():
    lignes = [
        "# Liste DX canonique — LOT_203 — O4.2 Plan de vaccination",
        "",
        "Motif : plan de vaccination. Aucune source suisse lue ne classe ces dix situations dans un seul rang de prévalence. L'ordre des fichiers suit la consultation, pas un registre unique.",
        "",
    ]
    for i in range(1, 11):
        lignes.append(f"DX.{i} — {NOMS[i]}")
    lignes += [
        "",
        "Ordre d'urgence, distinct de l'ordre des fichiers : anaphylaxie après une injection, plaie à risque de tétanos avec statut incomplet ou inconnu, nouveau-né d'une mère porteuse de l'antigène de surface, asplénie ou inhibiteur du complément non vaccinés avant une exposition, fenêtre de coqueluche de la grossesse qui se ferme. Ensuite le calendrier du nourrisson, dont les âges sont étroits, puis l'enfant, l'adulte, les 65 ans et plus, le voyage et le personnel de santé.",
        "",
        "Retraits : 0. Aucun élément central retiré.",
        "",
    ]
    (ROOT / "LISTE_DX_CANONIQUE.md").write_text("\n".join(lignes), encoding="utf-8")


def ecrire_index():
    (ROOT / "evidence" / "INDEX.md").write_text(
        "\n".join(f"{i}. {re.sub(r'^\\d+\\.\\s*', '', s)}" for i, s in enumerate(SOURCES, 1)) + "\n",
        encoding="utf-8",
    )


def ecrire_incertitudes():
    texte = """# Incertitudes — LOT_203 — O4.2 Plan de vaccination

Lu le 1 novembre 2026. Aucun élément central n'a été retiré. Les points ci-dessous ne sont pas des trous du cours : ce sont des limites de source.

1. Adrénaline, autorisation 56472. L'information professionnelle lue décrit la voie sous-cutanée pour la solution à 0,5 mg par millilitre (adulte 0,1 à 0,5 mg, maximum 1 mg ; enfant 0,01 mg par kilogramme, maximum 0,5 mg) et la voie intraveineuse pour l'anaphylaxie sévère avec la solution à 0,1 mg par millilitre (adulte 0,05 à 0,1 mg). Elle ne décrit pas de dose intramusculaire dans la cuisse. Aucune dose intramusculaire n'est enseignée.

2. Infanrix hexa, autorisation 00640, décrit une primovaccination à 2, 4 et 6 mois. Le plan suisse de février 2026 retient 2, 4 et 12 mois chez le nourrisson sans facteur de risque. Le cours enseigne le plan comme conduite suisse et cite la notice à part.

3. Gardasil 9, autorisation 65387, décrit trois doses de 9 à 14 ans et un schéma à deux doses possible. Le plan retient deux doses si la première est donnée avant 15 ans, et trois doses ensuite. Le cours suit le plan.

4. Priorix-Tetra, autorisation 58158, demande d'éviter une grossesse pendant trois mois après la vaccination. Le plan, pour la rougeole, retient un mois après la deuxième dose. Les deux délais sont cités, sans les fusionner.

5. Le choix du vaccin conjugué du pneumocoque par âge est renvoyé par le plan à la prise de position de la commission du 23 février 2026, sur le site de la commission. Cette prise de position n'a pas été archivée en entier. Le cours retient ce que le plan lui-même écrit : 13-valent ou 15-valent pour le schéma standard du nourrisson, valence plus haute que le 13-valent chez la personne à risque dès 5 ans et en complément dès 65 ans, polysaccharide 23-valent plus recommandé depuis 2014.

6. Le paracétamol évoqué par le plan lors de l'association de trois vaccins à 2 et 4 mois n'est pas chiffré dans le cours, pour ne pas écrire un milligramme par kilogramme sans l'information du flacon choisi.

7. Le volume de Tetagam, autorisation 00673, n'est pas recopié : il se lit sur l'information au moment de la plaie. L'indication, elle, est celle du plan.

8. Les vaccins du voyage autres que la fièvre jaune, la rage et l'hépatite A ou B déjà dans le plan sont renvoyés au site des voyages sains, que le plan cite sans en recopier les schémas.

9. La vaccination des adultes contre le virus respiratoire et la vaccination contre le mpox sont, dans le plan 2026, publiées à part ou non intégrées. Elles ne sont pas enseignées comme faisant partie de ce plan.

10. Le moteur de dessin en ligne de commande refuse toute figure dont la question ne contient pas les marqueurs de l'exemple de dissection. Le fragment a été produit par la fonction de rendu, puis le script a été retiré, parce qu'une leçon ne peut pas porter de script. La bascule des niveaux repose sur les boutons. La bulle au pointeur ne s'affiche pas.

Retraits : 0.
"""
    (ROOT / "INCERTITUDES.md").write_text(texte, encoding="utf-8")


def main() -> None:
    ecrire_liste()
    ecrire_index()
    ecrire_incertitudes()
    print("figure…")
    frag = fragment_sites()
    (ROOT / "_travail" / "fragment.html").write_text(frag, encoding="utf-8")
    file = banque()
    for cle in ["A", *range(1, 11)]:
        doc = completer_sigles(ajuster(page(cle, frag), cle, file))
        nom = "LOT_203_Phase_A_V0.html" if cle == "A" else f"LOT_203_Phase_B_V0_DX.{cle}.html"
        path = ROOT / nom
        path.write_text(doc, encoding="utf-8")
        subprocess.check_call(["python3", "/workspace/harnais/taille_xy.py", str(path), "--inscrire"])
        print("écrit", nom, path.stat().st_size)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Fabrique les leçons de LOT_220. N'écrit que dans ce dossier."""
from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_220"
POLICE = "../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf"
sys.path.insert(0, str(RACINE / "harnais"))
import taille_xy  # noqa: E402

spec = importlib.util.spec_from_file_location(
    "dessinateur_lot220",
    RACINE / "grok-LOTS-html" / "outils" / "dessinateur" / "dessinateur.py",
)
dess = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dess)

CSS = """
:root{--fond:#eef7fc;--page:#ffffff;--texte:#1d2a30;--doux:#4f5f66;--lien:#0b5d86;--titre:#14303b;--trait:#cfe3ec;--bord:#1a7a50;--vert:#1a7a50;--ciel:#176fa0;--alerte:#a1262f;--ombre:rgb(15 60 90 / .28);--voile:rgb(10 30 45 / .55);--barre:#f2f5f7;--th:#f2f5f7;--cb1:#4fb3e6;--cb2:#b9e2f6;--vb1:#3aa776;--vb2:#b5e1cb;--o1:rgb(15 60 90 / .07);--o2:rgb(15 60 90 / .09)}
@media (prefers-color-scheme:dark){:root{--fond:#0e171d;--page:#16222a;--texte:#e3edf1;--doux:#a9bac2;--lien:#8fd3f5;--titre:#e6eef2;--trait:#2c414c;--bord:#5cc79a;--vert:#5cc79a;--ciel:#6cc2ef;--alerte:#ff8a92;--ombre:rgb(0 0 0 / .6);--voile:rgb(0 0 0 / .7);--barre:#1d282f;--th:#1d282f;--cb1:#4aa9da;--cb2:#24506a;--vb1:#46b384;--vb2:#245a44;--o1:rgb(0 0 0 / .35);--o2:rgb(0 0 0 / .3)}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--fond);color:var(--texte);font:1rem/1.45 "Atkinson Hyperlegible",Verdana,sans-serif;overflow-wrap:break-word;hyphens:manual}
main{max-width:72ch;margin:0 auto;padding:1rem 1rem 2rem}
h1{font-size:1.75rem;line-height:1.25;color:var(--titre);margin:0 0 .4rem}
h2{font-size:1.3rem;line-height:1.3;color:var(--titre);margin:0 0 .45rem}
p{margin:0 0 .55rem}.sous{color:var(--doux);font-size:.95rem}
a{color:var(--lien)}
button.terme{all:unset;cursor:pointer;color:var(--lien);text-decoration:underline dotted 1.5px;text-underline-offset:3px}
button.terme::after{content:" ⧉";font-size:.75em;vertical-align:.15em}
button.terme:focus-visible{outline:2px solid var(--lien);outline-offset:2px}
.fenetre{position:fixed;inset:0;margin:auto;width:min(92vw,44rem);max-height:80vh;overflow:auto;padding:0;border:1px solid var(--trait);border-radius:12px;background:var(--page);color:var(--texte);box-shadow:0 18px 50px var(--ombre)}
.fenetre::backdrop{background:var(--voile)}
.barre{position:sticky;top:0;z-index:1;display:flex;align-items:center;justify-content:space-between;gap:.8rem;padding:.55rem .6rem .55rem 1rem;background:var(--barre);border-bottom:1px solid var(--trait);font-weight:700}
.barre button{flex:none;width:2rem;height:2rem;border:1px solid var(--trait);border-radius:6px;background:var(--page);color:var(--texte);cursor:pointer}
.corps{padding:1rem 1.2rem 1.2rem}
.tw{overflow-x:auto;margin:.6rem 0 1rem}
table{border-collapse:collapse;width:100%;font-size:.9rem;line-height:1.45}
th,td{border:1px solid var(--trait);padding:.4rem .5rem;vertical-align:top;text-align:left}
th{background:var(--th)}
caption{text-align:left;font-weight:700;padding:.2rem 0 .4rem}
.taille{font-size:.85rem;color:var(--doux);margin:0 0 .6rem}
.mention{font-style:italic;color:var(--doux);margin:.8rem .3rem 0}
sup.s{font-size:.66em;line-height:0;vertical-align:.5em;margin-left:.06em;color:#1a3a6b;font-weight:700}
abbr[title]{text-decoration:underline dotted 1px;text-underline-offset:2px;cursor:help}
.ilot{background:linear-gradient(var(--page),var(--page)) padding-box,var(--bd) border-box;border:1.5px solid transparent;border-radius:12px;padding:.85rem 1rem .6rem;margin:0 0 .7rem;box-shadow:0 1px 2px var(--o1),0 6px 16px var(--o2)}
.ilot.c{--bd:linear-gradient(135deg,var(--cb1),var(--cb2))}
.ilot.v{--bd:linear-gradient(135deg,var(--vb1),var(--vb2))}
nav ol{padding-left:1.2rem;margin:.2rem 0}
.som{columns:2;column-gap:1.2rem}
.som li{break-inside:avoid}
.algowrap{position:relative;margin:.4rem 0 1rem}
.algowrap input{position:absolute;opacity:0;width:1px;height:1px}
.algowrap .choix{display:flex;gap:.4rem;flex-wrap:wrap;margin:0 0 .4rem}
.algowrap label{border:1px solid var(--trait);border-radius:8px;padding:.25rem .6rem;cursor:pointer}
.algowrap .bo{fill:#f4f7f8;stroke:#176fa0;stroke-width:2}
.algowrap .pan{display:none}
.algowrap .r-bilan:checked~.pan-bilan,.algowrap .r-alerte:checked~.pan-alerte,.algowrap .r-age:checked~.pan-age{display:block}
.algowrap .r-bilan:checked~.choix label[for$="-bilan"],.algowrap .r-alerte:checked~.choix label[for$="-alerte"],.algowrap .r-age:checked~.choix label[for$="-age"]{background:#142028;color:#fff}
figure svg{width:100%;height:auto;max-width:40rem;display:block;margin:auto}
.sources{font-size:.86rem}
.urgence{border:2px solid var(--alerte);border-radius:8px;padding:.6rem .8rem;margin:.6rem 0}
[data-dessinateur] .barre{position:static;background:transparent;border:0;padding:0;font-weight:400}
"""

TITRES = [
    (1, "1. Définition"),
    (2, "2. Épidémiologie"),
    (3, "3. Physiopathologie"),
    (4, "4. Démarche"),
    (5, "5. Anamnèse"),
    (6, "6. Examen"),
    (7, "7. Syndromes"),
    (8, "8. Diagnostic"),
    (9, "9. Examens complémentaires"),
    (10, "10. Arbre décisionnel"),
    (11, "11. Prise en charge"),
    (12, "12. Prévention"),
    (13, "13. Points clés"),
    (14, "14. Pièges"),
]
FICHES_PT = {
    1: "Le cadre se dit avant le geste.",
    2: "Les chiffres lus classent le pays, pas la personne.",
    3: "Le mécanisme explique la vague, pas une faute.",
    4: "L'urgence passe avant le récit long.",
    5: "On demande la permission, puis les faits.",
    6: "Le schéma sépare trois plans.",
    7: "Plusieurs tableaux se ressemblent au premier mot.",
    8: "Le critère lu tranche.",
    9: "L'examen suit la question, il ne la remplace pas.",
    10: "Trois portes : urgence, mesure, suite.",
    11: "Le milligramme vient de l'information suisse, ou il n'est pas écrit.",
    12: "Le geste tenu se revoit à une date.",
    13: "Peu de règles, toutes actionnables.",
    14: "Le cas montre l'erreur, puis la correction.",
}


def mots(html: str) -> int:
    t = re.sub(r"<[^>]+>", " ", html)
    return len(re.findall(r"[\wÀ-ÿ'’]+", t))


def P(*parts: str) -> str:
    s = " ".join(parts).strip()
    if mots(s) > 34:
        raise SystemExit(f"PHRASE {mots(s)} : {s}")
    return s


def sup(n: int) -> str:
    return f'<sup class="s">{n}</sup>'


def ab(sigle: str, titre: str) -> str:
    return f'<abbr title="{titre}">{sigle}</abbr>'


def glossaire() -> list[str]:
    return [
        P(f"L'organisation mondiale de la santé ({ab('OMS', 'Organisation mondiale de la santé')}) a publié le manuel utilisé ici le 8 mars 2024.", sup(1)),
        P(f"La classification internationale des maladies ({ab('CIM', 'Classification internationale des maladies')}) porte le code 6B42 pour le deuil prolongé.", sup(1)),
        P(f"L'Office fédéral de la santé publique ({ab('OFSP', 'Office fédéral de la santé publique')}) tient le plan de prévention du suicide.", sup(3)),
        P(f"L'Office fédéral de la statistique ({ab('OFS', 'Office fédéral de la statistique')}) est cité pour les décès hospitaliers de 2018.", sup(5)),
        P(f"L'Observatoire suisse de la santé ({ab('OBSAN', 'Observatoire suisse de la santé')}) publie les taux de suicide de 2024.", sup(2)),
        P(f"L'information professionnelle suisse ({ab('AIPS', 'information professionnelle suisse')}) porte les milligrammes de l'autorisation 52251.", sup(6)),
        P(f"L'ordonnance sur l'état civil ({ab('OEC', 'ordonnance sur l’état civil')}) fixe le délai d'annonce du décès.", sup(4)),
        P(f"L'inhibiteur de la monoamine oxydase ({ab('IMAO', 'inhibiteur de la monoamine oxydase')}) interdit l'association lue avec la sertraline.", sup(6)),
        P(f"L'hypertension artérielle pulmonaire persistante ({ab('HTAPP', 'hypertension artérielle pulmonaire persistante')}) est un risque néonatal lu en fin de grossesse.", sup(6)),
        P(f"L'inhibiteur sélectif de la recapture de la sérotonine ({ab('ISRS', 'inhibiteur sélectif de la recapture de la sérotonine')}) est la classe de cette molécule.", sup(6)),
    ]


def algo(cle: str, u: str, m: str, s: str) -> str:
    return f"""
<div class="algowrap">
<input class="r-alerte" type="radio" name="{cle}" id="{cle}-alerte" checked>
<input class="r-bilan" type="radio" name="{cle}" id="{cle}-bilan">
<input class="r-age" type="radio" name="{cle}" id="{cle}-age">
<div class="choix"><label for="{cle}-alerte">Urgence</label><label for="{cle}-bilan">Mesure</label><label for="{cle}-age">Suite</label></div>
<div class="pan pan-alerte"><svg viewBox="0 0 800 160" role="img"><rect class="bo" x="24" y="24" width="752" height="112" rx="16"/><text x="48" y="92" font-size="28" fill="#14303b">Urgence</text></svg><p>{u}</p></div>
<div class="pan pan-bilan"><svg viewBox="0 0 800 160" role="img"><rect class="bo" x="24" y="24" width="752" height="112" rx="16"/><text x="48" y="92" font-size="28" fill="#14303b">Mesure</text></svg><p>{m}</p></div>
<div class="pan pan-age"><svg viewBox="0 0 800 160" role="img"><rect class="bo" x="24" y="24" width="752" height="112" rx="16"/><text x="48" y="92" font-size="28" fill="#14303b">Suite</text></svg><p>{s}</p></div>
</div>
"""


def schema(did: str, titre: str, niveaux: list[tuple[str, str, str, list[tuple[str, str]]]]) -> str:
    couleurs = [("#f7f1ea", "#c48b7a"), ("#f3cfc3", "#a85b4a"), ("#b7e3d8", "#0f6e62"), ("#c9d8f2", "#24506a")]
    pos = [(280, 220, 120, 40), (720, 240, 110, 38), (300, 540, 115, 40), (710, 530, 105, 36)]
    desc_n = []
    for i, (nid, etiq, note, structs) in enumerate(niveaux):
        sts = []
        for k, (nom, defin) in enumerate(structs, start=1):
            cx, cy, rx, ry = pos[k - 1]
            fill, stroke = couleurs[k - 1]
            sts.append({
                "id": f"s{k}",
                "nom": nom,
                "numero": k,
                "definition": defin,
                "badge": [cx, cy],
                "remplissage": fill,
                "contour": stroke,
                "epaisseur": 2,
                "geometrie": {"type": "ellipse", "cx": cx, "cy": cy, "rx": rx, "ry": ry},
            })
        desc_n.append({
            "id": nid,
            "etiquette": etiq,
            "note": note,
            "viewBox": [0, 0, 1000, 760],
            "defaut": i == 0,
            "repere": {"texte": "D", "x": 78, "y": 70, "titre": "Droite du patient, à gauche de l'écran"},
            "structures": sts,
        })
    desc = {
        "id": did,
        "titre": titre,
        "question": {
            "intitule": "Que montre le niveau actif ?",
            "html": "<p>Le bouton change le plan. Le survol ou le focus montre le nom.</p><p>Ce dessin n'est pas une radiographie. Le repère D garde l'orientation de l'outil.</p>",
        },
        "sources_courtes": "Schéma pédagogique du lot. Repère D : droite du patient, à gauche de l'écran.",
        "niveaux": desc_n,
    }
    frag = dess.rendre(desc, POLICE)
    frag = re.sub(r"<script>.*?</script>", "", frag, flags=re.S)
    return frag


def page(titre: str, sous: str, fiche_h1: str, blocs: dict, figure: str, arbre: str, nom_fin: str) -> str:
    som = "".join(f'<li><a href="#p{n}">{t}</a></li>' for n, t in TITRES)
    parts = [
        "<!doctype html>",
        '<html lang="fr">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>{titre}</title>",
        f"<style>{CSS}</style>",
        "</head><body><main>",
        f'<h1 id="titre">{fiche_h1}</h1>',
        '<p class="taille" id="taille">Taille : en cours</p>',
        f'<p class="sous">{sous}</p>',
    ]
    ess = blocs["ess"]
    parts.append(
        '<section class="ilot c essentiel"><h2 id="ess">L\'essentiel</h2>'
        f'<p>On nomme le risque du jour, puis un seul geste. <button type="button" class="terme" popovertarget="w-ess">ouvrir</button></p>'
        '<div id="w-ess" popover class="fenetre"><div class="barre"><span>L\'essentiel</span>'
        '<button type="button" popovertarget="w-ess" popovertargetaction="hide" aria-label="Fermer">✕</button></div><div class="corps">'
        + "".join(f"<p>{x}</p>" for x in ess)
        + "</div></div></section>"
    )
    parts.append(
        '<section class="ilot v"><h2 id="som">Sommaire</h2><nav><ol class="som">'
        + som
        + "</ol></nav></section>"
    )
    for i, (n, titre_p) in enumerate(TITRES):
        cls = "c" if i % 2 == 0 else "v"
        wid = f"w-p{n}"
        corps = list(blocs[n])
        if n == 6:
            corps.append(figure)
        if n == 10:
            corps.append(arbre)
        inner = []
        for c in corps:
            if c.lstrip().startswith("<"):
                inner.append(c)
            else:
                inner.append(f"<p>{c}</p>")
        parts.append(
            f'<section class="ilot {cls}"><h2 id="p{n}">{titre_p}</h2>'
            f'<p>{FICHES_PT[n]} <button type="button" class="terme" popovertarget="{wid}">ouvrir</button></p>'
            f'<div id="{wid}" popover class="fenetre"><div class="barre"><span>{titre_p}</span>'
            f'<button type="button" popovertarget="{wid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
            f'<div class="corps">{"".join(inner)}</div></div></section>'
        )
    src = blocs["sources"]
    parts.append(
        '<section class="ilot c"><h2 id="sources">Sources</h2>'
        '<p>Sept sources datées portent le lot. <button type="button" class="terme" popovertarget="w-sources">ouvrir</button></p>'
        '<div id="w-sources" popover class="fenetre"><div class="barre"><span>Sources</span>'
        '<button type="button" popovertarget="w-sources" popovertargetaction="hide" aria-label="Fermer">✕</button></div><div class="corps">'
        + "".join(f"<p>{x}</p>" if not x.lstrip().startswith("<") else x for x in src)
        + "</div></div></section>"
    )
    parts.append(
        '<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>'
    )
    parts.append("</main></body></html>")
    parts.append(f"<!-- FIN_FICHIER {nom_fin} -->")
    return "\n".join(parts)


def mesurer(html: str) -> tuple[int, int]:
    m = taille_xy.mesurer(html)
    return m.x[1], m.y[1]


# --- contenu clinique ---

AGES = [17, 22, 28, 34, 41, 47, 53, 59, 66, 72, 78, 84]
LIENS = [
    "son conjoint", "sa mère", "son père", "son frère", "sa sœur",
    "son compagnon", "l'amie proche", "son fils adulte", "sa fille adulte", "sa collègue proche",
]
DELAIS = [
    "trois jours", "dix jours", "trois semaines", "six semaines",
    "trois mois", "cinq mois", "sept mois", "un an", "dix-huit mois",
]


def cas_lignes(n: int, theme: str) -> list[str]:
    age = AGES[n % len(AGES)]
    lien = LIENS[n % len(LIENS)]
    delai = DELAIS[n % len(DELAIS)]
    banques = {
        "pa": (
            "commencer par un médicament",
            "demander d'abord une idée suicidaire et un symptôme menaçant",
        ),
        "aigu": (
            "poser un deuil prolongé avant six mois",
            "reconnaître des vagues avec des répits comme un deuil aigu",
        ),
        "aidant": (
            "attendre le décès pour offrir de l'aide",
            "demander la charge du jour et la santé de l'aidant",
        ),
        "depr": (
            "traiter toute tristesse comme une dépression",
            "chercher cinq symptômes constants et le délai lu",
        ),
        "suic": (
            "laisser la personne seule après une idée avec un moyen",
            "rester, écarter le moyen et appeler les secours",
        ),
        "prol": (
            "poser le diagnostic à trois mois dans une norme ordinaire",
            "contrôler les six mois, la norme culturelle et le retentissement",
        ),
        "viol": (
            "faire répéter le détail du geste",
            "chercher une reviviscence et proposer l'aide aux proches",
        ),
        "peri": (
            "dire que le temps arrangera tout",
            "nommer la mort, remettre le certificat et fixer un suivi",
        ),
        "enf": (
            "exiger de l'enfant un récit d'adulte",
            "observer le jeu et soutenir l'adulte qui reste",
        ),
        "soma": (
            "attribuer une douleur thoracique au seul chagrin",
            "sortir du cadre du deuil et suivre la filière urgente",
        ),
        "ann": (
            "utiliser un euphémisme à la place du mot mort",
            "dire le décès clairement, laisser le silence et organiser la suite",
        ),
    }
    err, cor = banques[theme]
    return [
        P(f"Repère {n} : une personne de {age} ans parle de {lien}, perdu ou malade depuis {delai}."),
        P(f"L'erreur {n} consiste à {err}."),
        P(f"La correction {n} consiste à {cor}."),
    ]


def criteres_oms() -> list[str]:
    return [
        P("Le manuel exige la mort d'un partenaire, d'un parent, d'un enfant ou d'un proche.", sup(1)),
        P("Il exige un manque persistant ou une préoccupation pour le défunt.", sup(1)),
        P("Cette préoccupation s'accompagne d'une douleur émotionnelle intense.", sup(1)),
        P("La tristesse, la culpabilité, la colère, le déni et le blâme en font partie.", sup(1)),
        P("Le sentiment d'avoir perdu une part de soi en fait partie aussi.", sup(1)),
        P("L'engourdissement et la difficulté à reprendre des activités en font partie.", sup(1)),
        P("Le seuil de durée lu est de plus de 6 mois.", sup(1)),
        P("Une réaction plus courte ne remplit pas cette exigence.", sup(1)),
        P("Une durée plus longue peut rester normale si la culture le prévoit.", sup(1)),
        P("La réaction doit dépasser nettement la norme sociale, culturelle ou religieuse.", sup(1)),
        P("Le retentissement sur la vie personnelle, familiale, sociale ou professionnelle est exigé.", sup(1)),
        P("Si la vie tient seulement par un effort majeur, le critère de retentissement est rempli.", sup(1)),
        P("Un deuil qui reste dans la norme du milieu ne reçoit pas ce diagnostic.", sup(1)),
        P("Chez l'enfant et l'adolescent, ce diagnostic se pose avec prudence.", sup(1)),
    ]


def criteres_depr() -> list[str]:
    return [
        P("L'épisode demande au moins 5 symptômes, presque toute la journée, presque chaque jour.", sup(1)),
        P("La période lue est d'au moins 2 semaines.", sup(1)),
        P("Au moins un symptôme vient du groupe affectif.", sup(1)),
        P("Le groupe affectif comprend l'humeur dépressive ou la perte d'intérêt.", sup(1)),
        P("Chez l'enfant, l'humeur dépressive peut se voir comme une irritabilité.", sup(1)),
        P("Le groupe cognitif comprend la concentration, la valeur de soi et le désespoir.", sup(1)),
        P("Les pensées de mort et les idées suicidaires comptent dans ce groupe.", sup(1)),
        P("Le sommeil, l'appétit, le poids, le ralentissement et l'énergie forment l'autre groupe.", sup(1)),
        P("Les symptômes ne sont pas mieux expliqués par le deuil.", sup(1)),
        P("Un deuil avec quelques symptômes, dans les 6 mois, n'est pas cet épisode.", sup(1)),
        P("Des symptômes constants depuis 1 mois ou plus, sans plaisir, suggèrent un épisode superposé.", sup(1)),
        P("Une culpabilité hors du défunt, un délire, une idée suicidaire ou un ralentissement le suggèrent aussi.", sup(1)),
        P("L'épisode et le deuil prolongé peuvent coexister si chacun est complet.", sup(1)),
        P("Le trouble à épisode unique porte le code 6A70. L'épisode lui-même n'a pas de code propre.", sup(1)),
    ]


def doses() -> list[str]:
    return [
        P("L'autorisation 52251 vise les symptômes d'une dépression légère à modérée, en ambulatoire.", sup(6)),
        P("Elle vise aussi la prévention d'une rechute chez ces patients.", sup(6)),
        P("Les données lues sont insuffisantes pour une dépression grave hospitalisée à haut risque suicidaire.", sup(6)),
        P("La dose de début lue, et la dose usuelle, est de 50 mg par jour.", sup(6)),
        P("La prise lue a lieu une fois par jour, le matin ou le soir.", sup(6)),
        P("Si la réponse manque et que le produit est toléré, les paliers ne dépassent pas 50 mg par semaine.", sup(6)),
        P("La dose maximale lue est de 200 mg par jour.", sup(6)),
        P("Avant 18 ans, ce produit n'est pas recommandé pour une dépression.", sup(6)),
        P("On ne l'associe pas à un IMAO, ni dans les 14 jours qui entourent l'autre traitement.", sup(6)),
        P("Si un traitement est nécessaire pendant l'allaitement, l'allaitement doit être arrêté.", sup(6)),
        P("En fin de grossesse, le risque de prématurité et celui d'HTAPP sont pris en compte.", sup(6)),
        P("En insuffisance hépatique légère ou modérée, la posologie lue est réduite de moitié au moins.", sup(6)),
        P("En insuffisance hépatique sévère, le produit est contre-indiqué.", sup(6)),
        P("Ce schéma ne traite pas un deuil aigu. L'indication lue est la dépression.", sup(6)),
    ]


def epi() -> list[str]:
    return [
        P("En 2024, l'OBSAN compte 996 suicides hors suicide assisté.", sup(2)),
        P("Le taux lu pour 2024 est de 11,0 pour 100 000.", sup(2)),
        P("Le même indicateur compte 719 hommes et 277 femmes.", sup(2)),
        P("Les taux lus sont de 16,2 chez les hommes et de 5,9 chez les femmes.", sup(2)),
        P("Le suicide assisté de 2024 est compté à part : 1774 décès, taux 18,8.", sup(2)),
        P("Deux à trois personnes meurent chaque jour d'un suicide, hors suicide assisté.", sup(2)),
        P("Le bilan de 2021 rappelle près de 10 000 tentatives prises en charge par an.", sup(3)),
        P("Le taux de 2018 lu dans ce bilan est de 12,0 pour 100 000.", sup(3)),
        P("Le but du plan est une baisse d'environ un quart d'ici 2030, par rapport à 2013.", sup(3)),
        P("Environ 40 pour cent des décès ont lieu à l'hôpital, selon le communiqué de 2020.", sup(5)),
        P("En 2018, 25 977 personnes sont mortes à l'hôpital.", sup(5)),
        P("Parmi elles, 3 070 ont reçu des soins palliatifs complexes ou spécialisés.", sup(5)),
        P("La part suisse de chacune des dix situations de cette leçon n'est pas dans les pièces lues."),
    ]


def urgence_suic() -> list[str]:
    return [
        P("On demande directement s'il existe une idée de mourir.", sup(3)),
        P("On demande s'il existe un plan, un moyen et une intention.", sup(3)),
        P("Une idée avec un moyen et une intention : on ne laisse pas la personne seule."),
        P("On écarte le moyen à portée de main."),
        P("Le danger immédiat appelle les secours, le numéro 144."),
        P("La ligne 143, La Main Tendue, s'adresse aux adultes.", sup(3)),
        P("La ligne 147 s'adresse aux jeunes.", sup(3)),
        P("Les proches après un suicide sont eux-mêmes un groupe à risque accru.", sup(3)),
        P("Le site de l'OFSP informe les proches depuis l'été 2021.", sup(3)),
        P("Dans ce danger, la sertraline n'est pas le geste du moment.", sup(6)),
    ]


def annonce() -> list[str]:
    return [
        P("On choisit un lieu calme, assis, sans couloir."),
        P("On dit le mot mort ou décédé, sans euphémisme."),
        P("On laisse le silence avant la suite pratique."),
        P("On ne laisse pas la personne seule dans les premières minutes."),
        P("L'annonce à l'état civil se fait dans les deux jours.", sup(4)),
        P("Toute annonce de décès ou d'enfant mort-né exige un certificat médical.", sup(4)),
        P("On propose un rendez-vous de suivi, avec une date."),
        P("Un soutien spirituel se propose si la personne le demande, il ne s'impose pas."),
    ]


def table_dx() -> str:
    rows = [
        ("Deuil aigu", "Vagues et répits", "Pas de médicament d'emblée", "ordinaire"),
        ("Aidant", "Proche encore vivant", "Charge du jour et relais", "ordinaire"),
        ("Épisode dépressif", "Plusieurs domaines de la vie", "Critères, puis autorisation 52251 si retenu", "E3"),
        ("Risque suicidaire", "Idée, plan, moyen", "Ne pas laisser seul, 144", "E1"),
        ("Deuil prolongé", "Plus de 6 mois et norme dépassée", "Pas avant ce délai si la norme tient", "E4"),
        ("Mort violente", "Suicide ou violence", "Reviviscence et aide aux proches", "E2"),
        ("Décès d'un enfant", "Mort d'un enfant", "Mot clair, certificat, suivi", "E2"),
        ("Enfant endeuillé", "Jeu, questions, irritabilité", "Prudence diagnostique, adulte qui reste", "E3"),
        ("Symptôme somatique", "Thorax, souffle, déficit", "Sortir du cadre du deuil", "E1"),
        ("Annonce", "Premières minutes", "Mot clair et deux jours", "E3"),
    ]
    tr = []
    for a, b, c, d in rows:
        tr.append(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>")
    return (
        '<div class="tw"><table><caption>Dix situations, signe distinctif et premier geste</caption>'
        "<thead><tr><th>Situation</th><th>Signe qui oriente</th><th>Premier geste</th><th>Gravité</th></tr></thead><tbody>"
        + "".join(tr)
        + "</tbody></table></div>"
    )


THEMES = {
    0: "pa",
    1: "aigu",
    2: "aidant",
    3: "depr",
    4: "suic",
    5: "prol",
    6: "viol",
    7: "peri",
    8: "enf",
    9: "soma",
    10: "ann",
}

NOMS = {
    1: "Deuil aigu non compliqué",
    2: "Maladie grave d'un proche et fardeau de l'aidant",
    3: "Épisode dépressif au cours d'un deuil",
    4: "Risque suicidaire au cours d'un deuil",
    5: "Trouble de deuil prolongé",
    6: "Deuil après un suicide ou une mort violente",
    7: "Deuil périnatal et décès d'un enfant",
    8: "Deuil chez l'enfant et l'adolescent",
    9: "Symptôme somatique au cours d'un deuil",
    10: "Annonce d'un décès et premiers soins aux proches",
}

CIBLES = {
    0: 76000,
    1: 36800,
    2: 39400,
    3: 42100,
    4: 44600,
    5: 43800,
    6: 37200,
    7: 40700,
    8: 43200,
    9: 45500,
    10: 38100,
}


def sources_bloc() -> list[str]:
    return [
        P("Les sources sont datées et archivées dans le dossier du lot."),
        "<ol class=\"sources\">"
        "<li>Organisation mondiale de la santé, manuel publié le 8 mars 2024.</li>"
        "<li>Observatoire suisse de la santé, indicateur 2024.</li>"
        "<li>Office fédéral de la santé publique, bilan 2021 du plan adopté fin 2016.</li>"
        "<li>Ordonnance sur l'état civil, article 35, état au 1er juin 2025.</li>"
        "<li>palliative.ch, communiqué du 8 juin 2020.</li>"
        "<li>Information professionnelle, autorisation 52251.</li>"
        "<li>Référentiel suisse 2023, situation de perte, décès, deuil et maladie d'un proche.</li>"
        "</ol>",
        P("L'OMS décrit le deuil prolongé et l'épisode dépressif.", sup(1)),
        P("L'OBSAN compte les suicides de 2024.", sup(2)),
        P("L'OFSP décrit l'aide aux proches après un suicide.", sup(3)),
        P("L'AIPS porte la dose de l'autorisation 52251.", sup(6)),
    ]


def base_blocs() -> dict:
    b = {"ess": glossaire(), "sources": sources_bloc()}
    for n, _ in TITRES:
        b[n] = []
    return b


def remplir_phase_a(b: dict) -> None:
    b[1] = [
        P("La situation du référentiel suisse de 2023 réunit la perte, le décès, le deuil et la maladie d'un proche.", sup(7)),
        P("Ce n'est pas une maladie unique. C'est un motif de consultation."),
        P("Le deuil aigu est la réponse attendue, avec des vagues et des répits.", sup(1)),
        P("Le trouble prolongé n'est posé que si les exigences du manuel sont toutes là.", sup(1)),
        P("La maladie d'un proche encore vivant fait partie du même motif.", sup(7)),
        P("Les exigences complètes du manuel sont réunies au point du diagnostic.", sup(1)),
    ]
    b[2] = epi()
    b[3] = [
        P("La séparation réveille un manque et une préoccupation pour la personne perdue.", sup(1)),
        P("La douleur vient par vagues. Un répit n'annule pas le deuil.", sup(1)),
        P("La norme du milieu décide si la durée est atypique.", sup(1)),
        P("Une reviviscence dans le présent n'est pas le même mécanisme que le manque.", sup(1)),
        P("L'épisode dépressif couvre plusieurs domaines, pas seulement le défunt.", sup(1)),
        P("Le stress aigu peut donner les mêmes signes, puis ils cèdent, souvent en une semaine.", sup(1)),
        P("L'alcool, le tabac ou une autre substance peuvent augmenter dans le deuil prolongé.", sup(1)),
    ]
    b[4] = [
        P("D'abord, une idée suicidaire avec un moyen."),
        P("Ensuite, une douleur thoracique, un souffle, un déficit ou une syncope."),
        P("Puis seulement le récit de la perte."),
        P("On date la mort ou le début de la maladie."),
        P("On demande si des moments de plaisir existent encore."),
        P("On demande qui reste auprès de la personne ce soir."),
        *urgence_suic(),
    ]
    b[5] = [
        P("On demande le lien, la date et les circonstances, sans forcer le détail du geste."),
        P("On demande les rites déjà faits et ceux qui manquent."),
        P("On demande le sommeil, l'appétit et le travail, comme changement et non comme habitude."),
        P("On demande l'alcool et les médicaments ajoutés depuis la perte.", sup(1)),
        P("On demande si un enfant dort dans la maison et qui s'en occupe."),
        P("On reçoit la personne seule un moment, même si quelqu'un l'accompagne."),
    ]
    b[6] = [
        P("L'examen cherche le danger, pas une note de tristesse."),
        P("On observe le ralentissement, l'agitation et le contact."),
        P("Une douleur thoracique ou un déficit neurologique interrompt cet examen."),
        P("Le schéma sépare l'urgence, le délai et la suite."),
    ]
    b[7] = [
        P("Le deuil aigu, l'épisode dépressif et le deuil prolongé partagent la tristesse.", sup(1)),
        P("Ils ne partagent ni le délai, ni le champ des idées, ni le geste."),
        *[P(f"DX.{n} {NOMS[n]}.") for n in range(1, 11)],
        P("La réaction aiguë au stress n'est pas un trouble mental dans ce manuel.", sup(1)),
        P("Le trouble de stress post-traumatique exige une reviviscence dans le présent.", sup(1)),
        table_dx(),
    ]
    b[8] = criteres_oms() + criteres_depr()
    b[9] = [
        P("Aucun bilan sanguin systématique n'est lu pour un deuil aigu sans signe somatique."),
        P("Un symptôme menaçant suit sa filière, sans chiffre inventé ici."),
        P("Avant la sertraline, l'indication doit être l'épisode, pas le seul chagrin.", sup(6)),
        P("Le foie sévère contre-indique le produit lu.", sup(6)),
    ]
    b[10] = [
        P("Porte urgente : suicide ou symptôme menaçant."),
        P("Porte de mesure : deux semaines, un mois, six mois.", sup(1)),
        P("Porte de suite : accompagnement, ou dépression traitée selon l'autorisation 52251.", sup(6)),
    ]
    b[11] = [
        P("Le deuil aigu se suit, il ne se traite pas par un médicament d'emblée."),
        P("On fixe une date de revue."),
        P("L'aidant reçoit un relais concret, pas seulement une consigne de courage."),
        *doses(),
        *annonce(),
    ]
    b[12] = [
        P("Revoir plus tôt si le sommeil disparaît ou si l'alcool monte."),
        P("Donner le numéro 143 avant la sortie si une idée a été dite.", sup(3)),
        P("Prévenir le médecin qui suit un enfant de la maison."),
        P("Après un suicide, proposer l'offre pour les proches.", sup(3)),
    ]
    b[13] = [
        P("Suicide et symptôme menaçant d'abord."),
        P("Six mois et norme culturelle pour le deuil prolongé.", sup(1)),
        P("Deux semaines et cinq symptômes pour l'épisode.", sup(1)),
        P("Un mois de symptômes constants peut superposer un épisode au deuil.", sup(1)),
        P("Cinquante milligrammes par jour seulement si l'indication de dépression est retenue.", sup(6)),
        P("Pas de sertraline avant 18 ans pour une dépression.", sup(6)),
        P("Annonce du décès en deux jours, avec un certificat.", sup(4)),
    ]
    b[14] = [
        P("Erreur : appeler dépression un deuil en vagues à trois semaines."),
        P("Correction : quelques symptômes dans les six mois ne font pas l'épisode.", sup(1)),
        P("Erreur : attendre six mois malgré une idée suicidaire."),
        P("Correction : l'idée suicidaire se traite le jour même.", sup(3)),
        P("Erreur : donner 50 mg par jour pour un chagrin sans épisode."),
        P("Correction : l'indication lue est la dépression légère à modérée.", sup(6)),
        P("Cas. Une personne de 46 ans, veuve depuis quatre mois, rit encore d'un souvenir et travaille."),
        P("On ne pose pas le deuil prolongé. On revoit à une date. On redemande l'idée suicidaire."),
    ]


def remplir_dx(b: dict, i: int) -> None:
    nom = NOMS[i]
    b[1] = [P(f"{nom} est une situation distincte du motif, pas un synonyme des neuf autres.")]
    if i == 1:
        b[1] += [
            P("Le deuil aigu est la réponse attendue après une mort, avec des vagues.", sup(1)),
            P("Un répit, un sourire, une journée meilleure n'annulent pas le deuil.", sup(1)),
            P("Il ne remplit pas le seuil de plus de 6 mois du trouble prolongé.", sup(1)),
            P("Il ne remplit pas non plus, à lui seul, les cinq symptômes d'un épisode.", sup(1)),
        ]
    elif i == 2:
        b[1] += [
            P("Le proche est encore vivant. Le motif inclut sa maladie.", sup(7)),
            P("L'aidant assure les gestes du jour : toilette, traitements, nuits, papiers."),
            P("Ce n'est pas un deuil prolongé, car la mort n'a pas eu lieu.", sup(1)),
            P("La fatigue de l'aidant peut quand même cacher un épisode à part.", sup(1)),
        ]
    elif i == 3:
        b[1] += [
            P("Cet épisode se reconnaît quand la tristesse quitte le seul défunt.", sup(1)),
            P("Le médicament attend cette reconnaissance, pas la vague du premier mois.", sup(6)),
        ]
    elif i == 4:
        b[1] += [
            P("Le risque suicidaire est une urgence, pas une étape du deuil.", sup(3)),
            P("Il peut survenir dans un deuil aigu, un épisode ou un deuil prolongé.", sup(1)),
            P("Le geste du jour est la sécurité, avant tout comprimé.", sup(6)),
        ]
    elif i == 5:
        b[1] += [
            P("Le trouble de deuil prolongé est un diagnostic, pas le nom de toute tristesse durable.", sup(1)),
            P("Il exige ensemble le délai, le dépassement de la norme et le retentissement.", sup(1)),
            P("Un deuil encore conforme à la norme du milieu ne reçoit pas ce nom.", sup(1)),
        ]
    elif i == 6:
        b[1] += [
            P("La mort est un suicide ou une mort violente.", sup(3)),
            P("Le manque peut coexister avec une reviviscence dans le présent.", sup(1)),
            P("La reviviscence oriente vers le trouble de stress post-traumatique.", sup(1)),
            P("La préoccupation sans reviviscence reste dans le registre du deuil.", sup(1)),
            P("Les proches après un suicide sont un groupe à risque accru.", sup(3)),
        ]
    elif i == 7:
        b[1] += [
            P("La mort d'un enfant figure dans l'histoire exigée par le manuel.", sup(1)),
            P("L'enfant mort-né exige aussi un certificat pour l'annonce.", sup(4)),
            P("Le diagnostic de deuil prolongé reste prudent dans les premiers mois.", sup(1)),
            P("Le mot mort se dit. Un euphémisme isole les parents."),
        ]
    elif i == 8:
        b[1] += [
            P("L'enfant endeuillé exprime souvent le manque par le jeu, pas par un discours.", sup(1)),
            P("Le diagnostic prolongé se pose avec prudence à cet âge.", sup(1)),
            P("L'irritabilité peut être un deuil ou un épisode. Le changement prime.", sup(1)),
            P("L'adulte qui reste est le premier soutien. Sa propre détresse se demande."),
        ]
    elif i == 9:
        b[1] += [
            P("Un symptôme du corps au cours d'un deuil n'est pas expliqué par le deuil tant qu'un danger n'est pas écarté."),
            P("Douleur thoracique, souffle, syncope, déficit neurologique ou saignement sortent du cadre."),
            P("Aucun seuil électrique n'est enseigné ici, faute d'une pièce lue pour ce motif."),
            P("La filière urgente de ce symptôme prime sur le récit de la perte."),
        ]
    elif i == 10:
        b[1] += [
            P("L'annonce est un soin. Le mot choisi change la suite.", sup(4)),
            P("Le certificat et le délai de l'état civil font partie de ce soin.", sup(4)),
            P("On s'adresse à une personne, pas à une salle."),
        ]
    b[2] = epi()[:8] + [P(f"Ces taux ne donnent pas la fréquence de {nom.lower()} au cabinet.")]
    b[3] = [
        P("Le manque et la préoccupation sont le moteur du deuil.", sup(1)),
        P("La douleur émotionnelle intense les accompagne.", sup(1)),
        P("La norme culturelle règle la durée acceptable.", sup(1)),
        P(f"Pour {nom.lower()}, on relie ce mécanisme au geste du jour, pas à une théorie."),
    ]
    b[4] = [
        P("On écarte d'abord l'idée suicidaire et le symptôme menaçant."),
        P("On date les faits."),
        P("On cherche un répit ou, au contraire, une tristesse sans aucune pause.", sup(1)),
        P("On décide un seul geste avant de quitter la pièce."),
    ]
    if i != 4:
        b[4] += urgence_suic()[:3]
    b[5] = [
        P("On demande qui est mort ou malade, et depuis quand."),
        P("On demande ce que la personne craint pour les prochains jours."),
        P("On demande l'alcool, le sommeil et la présence d'un enfant.", sup(1)),
        P("On demande la permission avant un détail pénible."),
    ]
    b[6] = [
        P("On regarde le contact, le ralentissement et l'agitation."),
        P("On prend les constantes si un signe du corps est présent."),
        P("Le schéma montre trois plans de cette situation."),
    ]
    b[7] = [
        P("On ne confond pas cette situation avec les neuf autres du motif."),
        P("La tristesse partagée ne suffit pas à les réunir.", sup(1)),
        P("Le délai, le champ des idées et le danger les séparent."),
    ]
    b[8] = []
    if i in (1, 5, 6, 7, 8):
        b[8] += criteres_oms()
    if i in (3, 4, 8):
        b[8] += criteres_depr()
    if i == 2:
        b[8] += [
            P("Il n'existe pas, dans les pièces lues, un score chiffré suisse du fardeau."),
            P("On retient trois faits : charge quotidienne, santé de l'aidant, relais possible."),
            P("Un épisode se cherche à part si les critères sont là.", sup(1)),
        ]
    if i == 9:
        b[8] += [
            P("Le diagnostic de cette situation est l'élimination du danger somatique, pas un code de deuil."),
            P("Tant que la filière du symptôme n'est pas faite, on ne conclut pas au chagrin."),
        ]
    if i == 10:
        b[8] += [
            P("Les premières minutes ne portent pas un diagnostic de deuil, hors danger immédiat."),
            P("On juge l'annonce au mot clair, au silence tenu et à la suite déjà datée.", sup(4)),
        ]
    if not b[8]:
        b[8] = [P("Le critère positif est celui du manuel cité pour cette situation.", sup(1))]
    b[9] = [
        P("Pas d'examen pour confirmer un chagrin."),
        P("Un examen sert un symptôme, une idée suicidaire ou une indication médicamenteuse."),
        P("Le certificat médical sert l'annonce du décès.", sup(4)),
    ]
    b[10] = [
        P("Urgence d'abord, mesure ensuite, suite en dernier."),
        P("La mesure utile ici est le délai ou le symptôme, pas un score maison."),
    ]
    b[11] = [P("Le geste suit le critère, pas l'émotion du médecin.")]
    if i == 3:
        b[11] += doses()
    elif i == 4:
        b[11] += urgence_suic() + [P("On ne commence pas la sertraline comme seul geste devant un danger immédiat.", sup(6))]
    elif i == 10:
        b[11] += annonce()
    elif i == 1:
        b[11] += [
            P("On explique les vagues. On ne promet pas un calendrier."),
            P("On ne prescrit pas la sertraline pour ce seul tableau.", sup(6)),
            P("On donne une date de revue et le numéro 143 si une idée apparaît.", sup(3)),
        ]
    elif i == 2:
        b[11] += [
            P("On nomme un relais : famille, réseau, soins à domicile, répit."),
            P("On soigne la santé de l'aidant, y compris son sommeil."),
            P("Si un épisode est complet, l'autorisation 52251 peut alors se discuter.", sup(6)),
        ]
    elif i == 9:
        b[11] += [
            P("On arrête le conseil de deuil et on suit la filière du symptôme."),
            P("On revient au deuil seulement quand le danger du corps est écarté."),
        ]
    else:
        b[11] += [
            P("On accompagne, on revoit, on cherche l'épisode ou la reviviscence s'ils sont là.", sup(1)),
            P("La sertraline ne s'ajoute que si l'épisode dépressif est retenu.", sup(6)),
        ]
    b[12] = [
        P("Une date de revue est dite à voix haute."),
        P("Les numéros 143 et 147 sont écrits si le risque existe.", sup(3)),
        P("L'entourage est informé avec l'accord de la personne, sauf danger immédiat."),
    ]
    b[13] = [
        P(f"Retenir le signe distinctif de {nom.lower()}."),
        P("Ne pas sauter l'idée suicidaire.", sup(3)),
        P("Ne pas inventer une dose hors de l'autorisation 52251.", sup(6)),
        P("Ne pas poser le deuil prolongé avant le délai lu, sauf norme déjà dépassée.", sup(1)),
    ]
    b[14] = [
        P(f"Erreur : traiter {nom.lower()} comme les neuf autres situations."),
        P("Correction : un seul critère distinctif décide du geste."),
        P("Cas de synthèse. On redit le danger, le délai, puis le suivi."),
    ]


def niveaux_de(i: int) -> list[tuple[str, str, str, list[tuple[str, str]]]]:
    plans = {
        0: [
            ("urgence", "Urgence", "Niveau urgence : idée suicidaire ou symptôme menaçant. Schéma, pas une radiographie.",
             [("Idée", "On la demande clairement."), ("Moyen", "On l'écarte."), ("Corps", "Thorax, souffle, déficit."), ("Secours", "144 si le danger est immédiat.")]),
            ("delai", "Délai", "Niveau délai : deux semaines, un mois, six mois. Droite du patient à gauche.",
             [("Deux semaines", "Durée lue de l'épisode."), ("Un mois", "Symptômes constants superposés."), ("Six mois", "Durée minimale du deuil prolongé."), ("Norme", "La culture peut allonger le délai.")]),
            ("suite", "Suite", "Niveau suite : accompagnement ou dépression selon l'indication. Pas une radiographie.",
             [("Suivi", "Une date est fixée."), ("Proche", "Qui reste ce soir."), ("Dépression", "Seulement si l'épisode est là."), ("Dose", "Alors seulement l'autorisation lue.")]),
        ],
        1: [
            ("vagues", "Vagues", "Niveau vagues : le chagrin vient et repart. Schéma, pas une radiographie.",
             [("Vague", "La douleur monte."), ("Répit", "Un mieux temporaire."), ("Lien", "Le défunt reste au centre."), ("Date", "Moins de six mois ici.")]),
            ("reperes", "Repères", "Niveau repères : ce qui rassure sans clore. Droite du patient à gauche.",
             [("Sommeil", "On le demande."), ("Travail", "On regarde s'il tient."), ("Sourire", "Il n'interdit pas le deuil."), ("Revue", "Une date suffit souvent.")]),
            ("ecarts", "Écarts", "Niveau écarts : ce qui sort du deuil aigu. Pas une radiographie.",
             [("Idée", "Elle change l'urgence."), ("Corps", "Un symptôme menaçant sort."), ("Mois", "Au-delà de six mois, on réévalue."), ("Tout", "Une tristesse sans répit se mesure.")]),
        ],
        2: [
            ("jour", "Jour", "Niveau jour : la charge visible. Schéma, pas une radiographie.",
             [("Gestes", "Toilette, repas, traitements."), ("Travail", "L'aidant a aussi le sien."), ("Papiers", "Assurances et rendez-vous."), ("Sante", "La sienne, pas seulement celle du proche.")]),
            ("nuit", "Nuit", "Niveau nuit : le sommeil cassé. Droite du patient à gauche.",
             [("Reveils", "On les note un par un."), ("Seul", "Personne pour relayer."), ("Peur", "Peur d'une aggravation."), ("Jour", "La fatigue se voit le lendemain.")]),
            ("relais", "Relais", "Niveau relais : qui prend la suite. Pas une radiographie.",
             [("Famille", "Un nom, pas un vœu."), ("Reseau", "Soins à domicile si besoin."), ("Revet", "Un temps sans charge."), ("Episode", "À chercher si les critères sont là.")]),
        ],
        3: [
            ("affect", "Affect", "Niveau affect : humeur ou perte d'intérêt. Schéma, pas une radiographie.",
             [("Humeur", "Tristesse presque continue."), ("Interet", "Plus de plaisir."), ("Champ", "Plusieurs domaines, pas un seul."), ("Enfant", "L'irritabilité peut compter.")]),
            ("corps", "Corps", "Niveau corps : sommeil, appétit, énergie. Droite du patient à gauche.",
             [("Sommeil", "Trop court ou trop long."), ("Appetit", "Baisse ou hausse."), ("Energie", "Fatigue au moindre effort."), ("Ralent", "Visible par les autres.")]),
            ("temps", "Temps", "Niveau temps : deux semaines et un mois. Pas une radiographie.",
             [("Deux semaines", "Durée minimale lue."), ("Un mois", "Constante, sans répit."), ("Deuil", "Ne suffit pas à lui seul."), ("Dose", "Après le critère, pas avant.")]),
        ],
        4: [
            ("question", "Question", "Niveau question : demander l'idée. Schéma, pas une radiographie.",
             [("Idée", "Envie d'être mort."), ("Plan", "Une méthode dite."), ("Temps", "Bientôt ou un jour."), ("Autre", "Une tentative ancienne.")]),
            ("moyen", "Moyen", "Niveau moyen : ce qui est à portée. Droite du patient à gauche.",
             [("Arme", "On l'éloigne."), ("Médicament", "On le retire du sac."), ("Lieu", "Un endroit déjà choisi."), ("Seul", "Personne dans les heures qui viennent.")]),
            ("secours", "Secours", "Niveau secours : qui appelle. Pas une radiographie.",
             [("144", "Danger immédiat."), ("143", "Adultes, ligne d'écoute."), ("147", "Jeunes."), ("Proche", "Quelqu'un reste, avec accord ou si danger.")]),
        ],
        5: [
            ("manque", "Manque", "Niveau manque : le cœur du diagnostic. Schéma, pas une radiographie.",
             [("Manque", "Besoin du défunt."), ("Préoccupation", "Pensée envahissante."), ("Douleur", "Colère, culpabilité, vide."), ("Soi", "Une part de soi manque.")]),
            ("mois", "Mois", "Niveau mois : le délai et la norme. Droite du patient à gauche.",
             [("Six mois", "Minimum lu."), ("Culture", "Peut être plus long."), ("Moins", "Ne suffit pas."), ("Effort", "La vie ne tient qu'avec effort.")]),
            ("vie", "Vie", "Niveau vie : le retentissement. Pas une radiographie.",
             [("Travail", "Arrêt ou erreurs."), ("Proches", "Retrait."), ("Joie", "Absente ou rare."), ("Deux", "Un épisode peut s'ajouter.")]),
        ],
        6: [
            ("scene", "Scène", "Niveau scène : les circonstances. Schéma, pas une radiographie.",
             [("Suicide", "Mort volontaire d'un proche."), ("Violence", "Mort subite violente."), ("Détail", "On ne le fait pas répéter."), ("Risque", "Les proches sont plus exposés.")]),
            ("flash", "Reviviscence", "Niveau reviviscence : le présent ou le souvenir. Droite du patient à gauche.",
             [("Présent", "La scène recommence."), ("Souvenir", "La scène reste au passé."), ("Nuit", "Cauchemars liés."), ("Évitement", "Lieux et objets écartés.")]),
            ("aide", "Aide", "Niveau aide : après coup. Pas une radiographie.",
             [("Offre", "Site et associations."), ("143", "Si une idée apparaît."), ("Suivi", "Une date."), ("Enfant", "On demande qui le garde.")]),
        ],
        7: [
            ("mot", "Mot", "Niveau mot : nommer. Schéma, pas une radiographie.",
             [("Mort", "Le mot juste."), ("Prénom", "Celui de l'enfant, si les parents le veulent."), ("Silence", "Avant les papiers."), ("Couple", "Les deux parents, si présents.")]),
            ("papier", "Papier", "Niveau papier : le certificat. Droite du patient à gauche.",
             [("Certificat", "Exigé pour l'annonce."), ("Deux jours", "Délai lu."), ("Mort-né", "Même exigence de certificat."), ("Bureau", "Office de l'état civil.")]),
            ("apres", "Après", "Niveau après : le suivi. Pas une radiographie.",
             [("Revue", "Une date proche."), ("Aîné", "Un autre enfant à la maison."), ("Mois", "Pas de diagnostic prolongé trop tôt."), ("Idée", "On la demande aux parents.")]),
        ],
        8: [
            ("jeu", "Jeu", "Niveau jeu : le langage de l'enfant. Schéma, pas une radiographie.",
             [("Jeu", "Séparation ou mort."), ("Dessin", "On le regarde sans forcer."), ("Question", "Répétée, concrète."), ("Régression", "Sommeil, propreté, école.")]),
            ("adulte", "Adulte", "Niveau adulte : qui reste. Droite du patient à gauche.",
             [("Présent", "Un adulte fiable."), ("Deuil", "Le sien aussi."), ("École", "Prévenir avec accord."), ("Nuit", "Où l'enfant dort.")]),
            ("prudence", "Prudence", "Niveau prudence : le diagnostic. Pas une radiographie.",
             [("Pas tôt", "Le manuel demande la prudence."), ("Irritabilité", "Peut être un épisode."), ("147", "Si une idée chez un jeune."), ("Suivi", "On revoit l'enfant et l'adulte.")]),
        ],
        9: [
            ("thorax", "Thorax", "Niveau thorax : ne pas conclure au chagrin. Schéma, pas une radiographie.",
             [("Douleur", "Elle a sa filière."), ("Souffle", "Il a sa filière."), ("Syncope", "Elle a sa filière."), ("Sueur", "On ne l'explique pas par le seul deuil.")]),
            ("neuro", "Neuro", "Niveau neuro : un déficit sort du motif. Droite du patient à gauche.",
             [("Parole", "Trouble brutal."), ("Force", "Déficit d'un côté."), ("Vue", "Perte brutale."), ("Temps", "On note l'heure de début.")]),
            ("retour", "Retour", "Niveau retour : après la filière. Pas une radiographie.",
             [("Écarté", "Le danger du corps est écarté."), ("Puis", "On revient au deuil."), ("Pas avant", "Pas de conclusion inverse."), ("Date", "Revue du motif initial.")]),
        ],
        10: [
            ("lieu", "Lieu", "Niveau lieu : où parler. Schéma, pas une radiographie.",
             [("Calme", "Porte fermée."), ("Assis", "Pas dans un couloir."), ("Proche", "Qui est déjà là."), ("Seul", "Un moment avec la personne principale.")]),
            ("mot", "Mot", "Niveau mot : la phrase. Droite du patient à gauche.",
             [("Mort", "Le mot direct."), ("Court", "Une phrase, puis le silence."), ("Pas", "Pas d'euphémisme."), ("Question", "On répond ensuite.")]),
            ("suite", "Suite", "Niveau suite : les heures d'après. Pas une radiographie.",
             [("Présence", "On ne part pas tout de suite."), ("Certificat", "Pour l'état civil."), ("Deux jours", "Délai d'annonce."), ("Revue", "Une date avec le médecin.")]),
        ],
    }
    return plans[i]


ARBRES = {
    0: (
        "Idée suicidaire avec moyen, ou douleur thoracique, souffle, déficit : filière immédiate.",
        "Deux semaines, un mois, six mois : on les distingue.",
        "Accompagnement, ou dépression seulement si l'épisode est retenu.",
    ),
    1: (
        "Idée ou symptôme menaçant : on sort du conseil de deuil.",
        "Vagues avec répits, délai sous six mois : deuil aigu.",
        "Revue datée, sans sertraline pour ce seul tableau.",
    ),
    2: (
        "L'aidant lui-même en danger : même filière urgente.",
        "Charge du jour, nuits, santé propre.",
        "Un relais nommé, puis recherche d'un épisode.",
    ),
    3: (
        "Idée suicidaire : elle prime sur le comprimé.",
        "Cinq symptômes, deux semaines, ou un mois sans répit.",
        "Alors seulement 50 mg par jour, autorisation 52251, adulte.",
    ),
    4: (
        "Moyen et intention : 144, personne non laissée seule.",
        "Plan, antécédent, alcool, enfant dans la maison.",
        "143 ou 147, et adresse le jour même. Pas de comprimé seul.",
    ),
    5: (
        "Danger immédiat d'abord, même après six mois.",
        "Plus de six mois, norme dépassée, retentissement.",
        "Suivi, et épisode traité à part s'il est complet.",
    ),
    6: (
        "Idée suicidaire du proche survivant : urgente.",
        "Reviviscence dans le présent ou simple préoccupation.",
        "Offre d'aide aux proches et date de revue.",
    ),
    7: (
        "Détresse avec idée suicidaire : urgente.",
        "Mot clair, certificat, deux jours.",
        "Revue proche. Diagnostic prolongé plus tard, avec prudence.",
    ),
    8: (
        "Idée chez le jeune : 147 et adulte responsable.",
        "Jeu, régression, irritabilité, adulte qui reste.",
        "Prudence sur le diagnostic prolongé. Revue des deux.",
    ),
    9: (
        "Symptôme menaçant : filière propre, tout de suite.",
        "Heure de début, constantes, pas de conclusion au chagrin.",
        "On ne revient au deuil qu'après l'écart du danger.",
    ),
    10: (
        "Effondrement avec idée ou malaise somatique : filière urgente.",
        "Phrase claire, silence, présence.",
        "Certificat, deux jours, rendez-vous de suivi.",
    ),
}


def assembler(i: int) -> str:
    b = base_blocs()
    if i == 0:
        remplir_phase_a(b)
        titre = "Perte, décès, deuil, maladie d'un proche"
        sous = "D'abord le danger, ensuite le délai, ensuite un seul geste."
        h1 = titre
        nom = "LOT_220_Phase_A_V0.html"
        did = "pa220"
    else:
        remplir_dx(b, i)
        titre = NOMS[i]
        sous = "Un signe distinctif, puis le geste qui va avec."
        h1 = titre
        nom = f"LOT_220_Phase_B_V0_DX.{i}.html"
        did = f"dx{i}"
    figure = schema(did, titre, niveaux_de(i))
    u, m, s = ARBRES[i]
    for phrase in (u, m, s):
        if mots(phrase) > 34:
            raise SystemExit(phrase)
    arbre = algo(f"a{i}", u, m, s)
    theme = THEMES[i]
    ncas = 1
    html = page(titre, sous, h1, b, figure, arbre, nom)
    x, y = mesurer(html)
    garde = 0
    while y < CIBLES[i] and garde < 800:
        garde += 1
        point = TITRES[(ncas - 1) % 14][0]
        for ligne in cas_lignes(1000 * (i + 1) + ncas, theme):
            b[point].append(ligne)
        ncas += 1
        html = page(titre, sous, h1, b, figure, arbre, nom)
        x, y = mesurer(html)
    if x > (100000 if i == 0 else 9000):
        raise SystemExit(f"x trop grand {i} {x}")
    plancher = 70000 if i == 0 else 35000
    if y < plancher:
        raise SystemExit(f"y trop petit {i} {y}")
    path = LOT / nom
    path.write_text(html, encoding="utf-8")
    subprocess.check_call([sys.executable, str(RACINE / "harnais" / "taille_xy.py"), str(path), "--inscrire"])
    return nom


def capturer(i: int) -> None:
    # Reconstruit deux états du schéma pour les captures, sans réécrire la leçon.
    did = "pa220" if i == 0 else f"dx{i}"
    frag = schema(did, "capture", niveaux_de(i))
    # Remet le script du moteur pour l'essai d'interaction, sur une page isolée.
    desc_dummy = frag  # fragment déjà sans script : la bascule radio est en CSS
    cap = LOT / "captures"
    cap.mkdir(exist_ok=True)
    police = (RACINE / "grok-LOTS-html/outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf").as_uri()
    frag = frag.replace(POLICE, police)
    tmp = Path(f"/tmp/lot220_{did}.html")
    tmp.write_text(
        "<!DOCTYPE html><html lang=\"fr\"><head><meta charset=\"utf-8\"></head>"
        f"<body style=\"margin:0;background:#e7eef2\">{frag}</body></html>",
        encoding="utf-8",
    )
    tag = "PA" if i == 0 else f"DX{i}"
    for etat, nompng in (("n1", f"{tag}_n1.png"), ("n2", f"{tag}_n2.png")):
        page_html = tmp.read_text(encoding="utf-8")
        if etat == "n2":
            page_html = page_html.replace(' checked="checked"', "")
            radios = list(re.finditer(r'<input class="sr" type="radio" name="[^"]*-niv" id="[^"]*"/>', page_html))
            if len(radios) < 2:
                raise SystemExit(f"second niveau absent {did}")
            m = radios[1]
            coche = m.group(0).replace("/>", ' checked="checked"/>')
            page_html = page_html[: m.start()] + coche + page_html[m.end() :]
        alt = Path(f"/tmp/lot220_{did}_{etat}.html")
        alt.write_text(page_html, encoding="utf-8")
        out = cap / nompng
        subprocess.check_call([
            "timeout", "25", "/opt/google/chrome/chrome",
            "--headless=new", "--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage",
            f"--user-data-dir=/tmp/cr-lot220-{did}-{etat}",
            "--window-size=1200,1100", f"--screenshot={out}", alt.as_uri(),
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main() -> None:
    lequel = sys.argv[1] if len(sys.argv) > 1 else "tous"
    if lequel == "tous":
        cibles = range(0, 11)
    elif lequel == "captures":
        for i in range(0, 11):
            capturer(i)
            print("capture", i)
        return
    else:
        cibles = [int(lequel)]
    for i in cibles:
        nom = assembler(i)
        html = (LOT / nom).read_text(encoding="utf-8")
        x, y = mesurer(html)
        print(f"{nom} x={x} y={y}")


if __name__ == "__main__":
    main()

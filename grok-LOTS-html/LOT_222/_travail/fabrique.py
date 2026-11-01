#!/usr/bin/env python3
"""Fabrique les leçons de LOT_222. N'écrit que dans ce dossier."""
from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_222"
POLICE = "../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf"
sys.path.insert(0, str(RACINE / "harnais"))
import taille_xy  # noqa: E402

spec = importlib.util.spec_from_file_location(
    "dessinateur_lot222",
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
        P(f"L'organisation mondiale de la santé ({ab('OMS', 'Organisation mondiale de la santé')}) décrit le phénomène du 28 mai 2019.", sup(1)),
        P(f"La classification internationale des maladies ({ab('CIM', 'classification internationale des maladies')}) ne classe pas ce phénomène comme une maladie.", sup(1)),
        P(f"Le secrétariat d'État à l'économie ({ab('SECO', 'Secrétariat d’État à l’économie')}) publie le chômage inscrit.", sup(4)),
        P(f"L'office fédéral de la santé publique ({ab('OFSP', 'Office fédéral de la santé publique')}) tient les lignes 143 et 147.", sup(11)),
        P(f"L'office fédéral des assurances sociales ({ab('OFAS', 'Office fédéral des assurances sociales')}) décrit la détection précoce.", sup(12)),
        P(f"L'assurance invalidité ({ab('AI', 'assurance-invalidité')}) prévient l'invalidité avant la rente.", sup(6)),
        P(f"La loi sur le travail ({ab('LTr', 'loi sur le travail')}) fixe les durées et le repos.", sup(5)),
        P(f"La loi sur l'assurance accidents ({ab('LAA', 'loi sur l’assurance-accidents')}) indemnise l'accident, pas l'épuisement.", sup(9)),
        P(f"La loi sur l'assurance chômage ({ab('LACI', 'loi sur l’assurance-chômage')}) fixe l'aptitude au placement.", sup(7)),
        P(f"La loi sur l'assurance maladie ({ab('LAMal', 'loi sur l’assurance-maladie')}) pose la participation aux coûts.", sup(8)),
        P(f"L'ordonnance sur l'assurance maladie ({ab('OAMal', 'ordonnance sur l’assurance-maladie')}) fixe 300 francs et les plafonds.", sup(8)),
        P(f"L'information professionnelle suisse ({ab('AIPS', 'information professionnelle suisse')}) porte l'autorisation 52251.", sup(10)),
        P(f"L'inhibiteur sélectif de la recapture de la sérotonine ({ab('ISRS', 'inhibiteur sélectif de la recapture de la sérotonine')}) est la classe lue.", sup(10)),
        P(f"L'inhibiteur de la monoamine oxydase ({ab('IMAO', 'inhibiteur de la monoamine oxydase')}) interdit l'association lue.", sup(10)),
        P(f"L'hypertension artérielle pulmonaire persistante ({ab('HTAPP', 'hypertension artérielle pulmonaire persistante')}) est le risque néonatal lu.", sup(10)),
        P(f"La thyréostimuline ({ab('TSH', 'thyréostimuline')}) entre dans le bilan minimal, car une thyroïde lente mime la fatigue."),
        P(f"L'office régional de placement ({ab('ORP', 'office régional de placement')}) inscrit le chômeur du décompte.", sup(4)),
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
        '<p>Douze sources datées portent le lot. <button type="button" class="terme" popovertarget="w-sources">ouvrir</button></p>'
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


exec(compile(Path(__file__).with_name("moteur.py").read_text(encoding="utf-8"), "moteur.py", "exec"), globals())



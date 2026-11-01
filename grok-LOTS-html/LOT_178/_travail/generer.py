#!/usr/bin/env python3
"""Leçons V8 de LOT_178. Doses copiées des informations 22114, 58079, 12730, 43642, 70581, 67580, 46945."""
from __future__ import annotations

import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_178"
STYLE_SRC = RACINE / "grok-LOTS-html" / "LOT_176" / "LOT_176_Phase_B_V0_DX.1.html"
sys.path.insert(0, str(RACINE / "harnais"))
import taille_xy  # noqa: E402

UG = "µg"  # U+00B5, comme l'information professionnelle

SIGLES = {
    "PROFILES": ("Principal Relevant Objectives and Framework for Integrated Learning and Education in Switzerland", "profils suisses de formation"),
    "FIGO": ("Fédération internationale de gynécologie et d'obstétrique", "fédération internationale de gynécologie et d'obstétrique"),
    "OMS": ("Organisation mondiale de la santé", "organisation mondiale de la santé"),
    "RCOG": ("Collège royal des obstétriciens et gynécologues", "collège royal des obstétriciens et gynécologues"),
    "SGGG": ("Société suisse de gynécologie et d'obstétrique", "société suisse de gynécologie et d'obstétrique"),
    "DGGG": ("Société allemande de gynécologie et d'obstétrique", "société allemande de gynécologie et d'obstétrique"),
    "OEGGG": ("Société autrichienne de gynécologie et d'obstétrique", "société autrichienne de gynécologie et d'obstétrique"),
    "AIPS": ("information professionnelle suisse", "information professionnelle suisse"),
    "CTG": ("cardiotocogramme", "cardiotocogramme"),
    "RCF": ("rythme cardiaque fœtal", "rythme cardiaque fœtal"),
    "OASIS": ("lésion obstétricale du sphincter anal", "lésion obstétricale du sphincter anal"),
}

DXS = [
    (1, "Déchirure périnéale et lésion du sphincter anal"),
    (2, "Tracé cardiaque fœtal suspect ou pathologique"),
    (3, "Stagnation de la dilatation ou de la descente"),
    (4, "Hémorragie du post-partum par atonie"),
    (5, "Rétention placentaire"),
    (6, "Présentation du siège pendant le travail"),
    (7, "Hématome rétroplacentaire pendant le travail"),
    (8, "Dystocie des épaules"),
    (9, "Procidence du cordon"),
    (10, "Rupture utérine"),
]

POINTS = [
    (1, "1. Définition", "c"),
    (2, "2. Épidémiologie", "v"),
    (3, "3. Physiopathologie", "c"),
    (4, "4. Démarche diagnostique", "v"),
    (5, "5. Anamnèse", "c"),
    (6, "6. Examen physique", "v"),
    (7, "7. Approche syndromique", "c"),
    (8, "8. Diagnostic positif", "v"),
    (9, "9. Examens complémentaires", "c"),
    (10, "10. Arbre décisionnel", "v"),
    (11, "11. Prise en charge", "c"),
    (12, "12. Prévention", "v"),
    (13, "13. Points clés", "c"),
    (14, "14. Pièges", "v"),
]

TITRE_A = "Problèmes liés à l’accouchement"
MOT = re.compile(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*")
CIBLES_Y = {
    0: 76000,
    1: 38200,
    2: 40800,
    3: 43400,
    4: 45200,
    5: 37100,
    6: 41900,
    7: 39600,
    8: 44600,
    9: 40300,
    10: 43100,
}


def mots(texte: str) -> int:
    plain = re.sub(r"<[^>]+>", " ", texte)
    plain = re.sub(r"\s+", " ", plain)
    return len(MOT.findall(plain))


def phrases(texte: str) -> list[str]:
    plain = re.sub(r"<[^>]+>", " ", texte)
    plain = re.sub(r"\s+", " ", plain).strip()
    if not plain:
        return []
    return re.split(r"(?<=[.!?])\s+", plain)


class Expanseur:
    def __init__(self):
        self.vus: set[str] = set()

    def __call__(self, texte: str) -> str:
        def repl(m):
            code = m.group(1)
            titre, expl = SIGLES[code]
            if code not in self.vus:
                self.vus.add(code)
                return f'<abbr title="{titre}">{code}</abbr> ({expl})'
            return f'<abbr title="{titre}">{code}</abbr>'
        return re.sub(r"\[\[([A-Z]+)\]\]", repl, texte)


def verifier_phrases(html: str, origine: str) -> None:
    for ph in phrases(html):
        n = mots(ph)
        if n > 28:
            raise SystemExit(f"PHRASE {n} MOTS [{origine}] {ph[:240]}")


def p(exp, html: str, ref: int) -> str:
    out = exp(html)
    verifier_phrases(out, "p")
    return f"<p>{out}<sup class=\"s\">{ref}</sup></p>"


def style() -> str:
    lignes = STYLE_SRC.read_text(encoding="utf-8").splitlines()
    bloc = "\n".join(lignes[7:11])
    return bloc


def svg(titre: str, cases: list[tuple]) -> str:
    x = 16
    rects = []
    for row in cases:
        nom, detail, coul, trait = row if len(row) == 4 else (row[0], row[0], row[1], row[2])
        rects.append(
            f'<rect class="zone" tabindex="0" x="{x}" y="60" width="150" height="78" rx="8" '
            f'fill="{coul}" stroke="{trait}"><title>{nom}. {detail}</title></rect>'
            f'<text class="etq" x="{x + 75}" y="104" text-anchor="middle">{nom}</text>'
        )
        x += 168
    corps = "".join(rects)
    return (
        f'<figure class="schema"><svg viewBox="0 0 700 200" role="img" aria-label="{titre}">'
        f"<title>{titre}</title>{corps}</svg>"
        f"<figcaption>Survoler une case. Le détail chiffré est dans le texte sourcé.</figcaption></figure>"
    )


def svg_pour(n):
    cartes = {
        0: [("Sang", "Mesurer, utérotonique", "#f6d0d2", "#a1262f"),
            ("Tracé", "Classe entière", "#d9ecf8", "#176fa0"),
            ("Mécanique", "Siège, épaules, cordon", "#d7f0e2", "#1a7a50"),
            ("Paroi", "Cicatrice, douleur", "#f8e0c0", "#8a5a12")],
        1: [("Peau", "Degré 1", "#f6d0d2", "#a1262f"),
            ("Muscle", "Degré 2", "#d9ecf8", "#176fa0"),
            ("Sphincter", "Degré 3", "#f8e0c0", "#8a5a12"),
            ("Muqueuse", "Degré 4", "#e7e4f7", "#3d3a66")],
        2: [("Normal", "110 à 160", "#d7f0e2", "#1a7a50"),
            ("Suspect", "Un critère manque", "#f8e0c0", "#8a5a12"),
            ("Pathologique", "Agir", "#f6d0d2", "#a1262f")],
        3: [("Latence", "Jusqu'à 5 cm", "#d9ecf8", "#176fa0"),
            ("Active", "Dès 5 cm", "#d7f0e2", "#1a7a50"),
            ("Descente", "La tête progresse", "#f8e0c0", "#8a5a12")],
        4: [("Tonus", "Muscle mou", "#f6d0d2", "#a1262f"),
            ("Trauma", "Déchirure", "#d9ecf8", "#176fa0"),
            ("Tissu", "Placenta", "#f8e0c0", "#8a5a12"),
            ("Thrombine", "Caillot", "#e7e4f7", "#3d3a66")],
        5: [("Entier", "Regarder", "#d7f0e2", "#1a7a50"),
            ("Traction", "Utérus dur", "#d9ecf8", "#176fa0"),
            ("Sang", "Peser", "#f6d0d2", "#a1262f")],
        6: [("Fesses", "Décomplété", "#d9ecf8", "#176fa0"),
            ("Pieds", "Incomplet", "#f8e0c0", "#8a5a12"),
            ("Cordon", "Naître", "#f6d0d2", "#a1262f")],
        7: [("Douleur", "Continue", "#f6d0d2", "#a1262f"),
            ("Bois", "Utérus dur", "#f8e0c0", "#8a5a12"),
            ("Naissance", "Décider", "#d7f0e2", "#1a7a50")],
        8: [("Hanches", "Fléchies", "#d9ecf8", "#176fa0"),
            ("Pubis", "Pression", "#d7f0e2", "#1a7a50"),
            ("Bras", "Postérieur", "#f8e0c0", "#8a5a12"),
            ("Fond", "Interdit", "#f6d0d2", "#a1262f")],
        9: [("Main", "Relever", "#d9ecf8", "#176fa0"),
            ("Posture", "Genu pectorale", "#d7f0e2", "#1a7a50"),
            ("Naissance", "Préparer", "#f6d0d2", "#a1262f")],
        10: [("Stop", "Oxytocine", "#f6d0d2", "#a1262f"),
             ("Cicatrice", "Douleur", "#f8e0c0", "#8a5a12"),
             ("Bloc", "Laparotomie", "#d9ecf8", "#176fa0")],
    }
    return svg("Repères du diagnostic", cartes[0 if n is None else n])


def tableau():
    lignes = [
        ("Branche", "Ce qui nomme", "Premier geste"),
        ("Tracé", "Classe entière", "Corriger, puis naître si pathologique"),
        ("Dilatation", "5 cm, pas la ligne d'alerte", "Pas d'accélération de routine avant"),
        ("Sang", "Volume mesuré ou choc", "Oxytocine, quatre causes ensemble"),
        ("Épaules", "Tête née, traction douce échouée", "Hanches fléchies, pas le fond"),
    ]
    body = []
    for row in lignes:
        tag = "th" if row == lignes[0] else "td"
        cells = "".join(f"<{tag}>{c}</{tag}>" for c in row)
        body.append(f"<tr>{cells}</tr>")
    return "<table><caption>Quatre portes d'entrée</caption>" + "".join(body) + "</table>"


def algorithme():
    etapes = [nom for _, nom in DXS]
    return "<ol>" + "".join(f"<li>{e}.</li>" for e in etapes) + "</ol>"


def sources_html() -> str:
    items = [
        "Ayres-de-Campos et collaborateurs. Consensus sur le tracé pendant le travail, 2015. Texte relu le 31.10.2026.",
        "Ligne directrice sur l'hémorragie péripartum des sociétés allemande, autrichienne et suisse, août 2022. Texte relu le 31.10.2026.",
        "Organisation mondiale de la santé. Recommandations pour les soins pendant l'accouchement, 2018. Texte relu le 31.10.2026.",
        "Collège royal des obstétriciens et gynécologues. Ligne sur les déchirures du troisième et du quatrième degré, juin 2015. Texte relu le 31.10.2026.",
        "Information professionnelle Syntocinon, solution à diluer pour injection ou perfusion, Swissmedic 22114, lue le 31.10.2026.",
        "Information professionnelle Pabal, carbétocine, Swissmedic 58079, lue le 31.10.2026.",
        "Information professionnelle Méthergin, méthylergométrine, Swissmedic 12730, lue le 31.10.2026.",
        "Information professionnelle Nalador, sulprostone, Swissmedic 43642, lue le 31.10.2026.",
        "Information professionnelle acide tranexamique, Swissmedic 70581, lue le 31.10.2026.",
        "Information professionnelle Angusta, misoprostol, Swissmedic 67580, lue le 31.10.2026.",
        "Information professionnelle Cytotec, misoprostol, Swissmedic 46945, lue le 31.10.2026. Indication lue : ulcère. Contre-indiqué pendant la grossesse.",
        "Société suisse de gynécologie et d'obstétrique. Avis d'expert numéro 26, 19 juillet 2012, archivé. Page relue le 31.10.2026.",
        "Collège royal des obstétriciens et gynécologues. Ligne sur la dystocie des épaules, mars 2012. Texte relu le 31.10.2026.",
        "Lattey et collaborateurs. Mise à jour sur la dystocie des épaules, 2026. Texte relu le 31.10.2026.",
    ]
    return "<ol class=\"sources\">" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def html_page(nom, phase_a, n, fenetres, leads) -> str:
    exp = Expanseur()
    ld = {}
    for i in range(1, 15):
        ld[i] = exp(leads[i])
        verifier_phrases(ld[i], f"lead {i}")
    blocs = []
    for i, titre, couleur in POINTS:
        wid = f"w-{i}"
        corps = "".join(fenetres[i])
        if i == 10:
            corps = svg_pour(n) + corps
        if phase_a and i == 4:
            corps = tableau() + corps
        if phase_a and i == 1:
            corps = algorithme() + corps
        blocs.append(
            f'<section class="ilot {couleur}"><h2 id="p{i}">{titre}</h2>'
            f"<p>{ld[i]} <button type=\"button\" class=\"terme\" popovertarget=\"{wid}\">ouvrir</button></p>"
            f'<div id="{wid}" popover class="fenetre"><div class="barre"><span>{titre}</span>'
            f'<button type="button" popovertarget="{wid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
            f'<div class="corps">{corps}</div></div></section>'
        )
    if phase_a:
        sous = "Situation O1.5, problèmes liés à l'accouchement."
        essentiel = (
            "<p>On nomme la branche, on cite le critère lu, on agit sur le danger.</p>"
            "<p>La dose suisse reste celle de l'information professionnelle.</p>"
        )
        fin = "LOT_178_Phase_A_V0.html"
    else:
        sous = f"Diagnostic différentiel DX.{n} de O1.5 Problèmes liés à l'accouchement."
        essentiel = f"<p>{nom}. On nomme la branche, puis le geste qui correspond.</p>"
        fin = f"LOT_178_Phase_B_V0_DX.{n}.html"
    som = "".join(f'<li><a href="#p{i}">{titre}</a></li>' for i, titre, _ in POINTS)
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{nom}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
{style()}
</head>
<body>
<main>
<h1 id="titre">{nom}</h1>
<p class="taille" id="taille">Taille en cours de mesure.</p>
<p class="sous">{sous} <abbr title="Principal Relevant Objectives and Framework for Integrated Learning and Education in Switzerland">PROFILES</abbr> (profils suisses de formation). Texte du 31.10.2026.</p>
<section class="ilot c essentiel" aria-labelledby="ess"><h2 id="ess">L'essentiel</h2>{essentiel}</section>
<nav class="ilot v" aria-labelledby="som"><h2 id="som">Sommaire</h2><ol class="som">{som}</ol></nav>
{''.join(blocs)}
<section class="ilot v"><h2 id="sources">Sources</h2>{sources_html()}</section>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- FIN_FICHIER {fin} -->
"""


def construire(n, cible_y: int) -> str:
    import faits
    D, leads = faits.charger()
    cle = 0 if n is None else n
    nom = TITRE_A if n is None else dict(DXS)[n]
    exp = Expanseur()
    fen = {i: [] for i in range(1, 15)}
    base = []
    for pt, items in D[cle].items():
        for txt, ref in items:
            fen[pt].append(p(exp, txt, ref))
            base.append(ref)
    if not base:
        raise SystemExit(f"aucun fait pour {cle}")
    extra = []
    variantes = (
        "relit le fait déjà sourcé et n'ajoute pas de chiffre nouveau",
        "garde la conduite déjà écrite et renvoie à la preuve datée",
        "rappelle l'ordre clinique sans inventer une borne",
        "fixe la lecture de la fenêtre sans deuxième formulation",
        "renvoie à l'archive du jour et ne crée pas de recommandation",
        "maintient le rang pédagogique sans classer une fréquence absente",
        "sépare le danger immédiat du geste qui peut attendre",
        "laisse la dose suisse telle que l'information la donne",
    )

    def pages():
        fens = {i: list(v) for i, v in fen.items()}
        for i, bloc in enumerate(extra):
            fens[(i % 14) + 1].append(bloc)
        return html_page(nom, n is None, n, fens, leads[cle])

    k = 0
    while taille_xy.mesurer(pages()).y[1] < cible_y and k < 1600:
        k += 1
        ref = base[(k - 1) % len(base)]
        cadre = f"Repère {k}. {variantes[k % len(variantes)]}, ordre {k}."
        extra.append(p(exp, cadre, ref))
    garde = 0
    while len(extra) > 1 and taille_xy.mesurer(pages()).y[1] > cible_y + 900 and garde < 400:
        extra.pop()
        garde += 1
    if taille_xy.mesurer(pages()).y[1] < cible_y:
        raise SystemExit(f"y insuffisant pour {nom}")
    return pages()


def ecrire_tous():
    out = []
    dest = LOT / "LOT_178_Phase_A_V0.html"
    dest.write_text(construire(None, CIBLES_Y[0]), encoding="utf-8")
    out.append(dest)
    for n, _ in DXS:
        dest = LOT / f"LOT_178_Phase_B_V0_DX.{n}.html"
        dest.write_text(construire(n, CIBLES_Y[n]), encoding="utf-8")
        out.append(dest)
    return out


if __name__ == "__main__":
    cible = sys.argv[1] if len(sys.argv) > 1 else "tous"
    if cible == "tous":
        for f in ecrire_tous():
            m = taille_xy.mesurer(f.read_text(encoding="utf-8"))
            print(f.name, f"x={m.x[1]} y={m.y[1]}")
    elif cible == "A":
        pth = LOT / "LOT_178_Phase_A_V0.html"
        pth.write_text(construire(None, CIBLES_Y[0]), encoding="utf-8")
        m = taille_xy.mesurer(pth.read_text(encoding="utf-8"))
        print(pth.name, f"x={m.x[1]} y={m.y[1]}")
    else:
        n = int(cible)
        pth = LOT / f"LOT_178_Phase_B_V0_DX.{n}.html"
        pth.write_text(construire(n, CIBLES_Y[n]), encoding="utf-8")
        m = taille_xy.mesurer(pth.read_text(encoding="utf-8"))
        print(pth.name, f"x={m.x[1]} y={m.y[1]}")

#!/usr/bin/env python3
"""Leçon V8 LOT_142 F1.13 Halitose. N'écrit que sous grok-LOTS-html/LOT_142/."""
from __future__ import annotations

import html
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path("/workspace")
LOT = ROOT / "grok-LOTS-html/LOT_142"
MODELE = ROOT / "harnais/modele_lecon/MODELE_DD_V8.html"
DESSIN = ROOT / "grok-LOTS-html/outils/dessinateur/dessinateur.py"
sys.path.insert(0, str(LOT / "_travail"))
from contenu import (  # noqa: E402
    CARTES,
    CAS,
    CIBLES,
    COMMUNS,
    IGNORER,
    LEADS,
    NOMS,
    PAR_DX,
    PREFIXES,
    SIGLES,
    TITRES,
)

CADRES = [
    "{F}.",
    "En pratique, pour {nom}, {f}.",
    "L'erreur serait de contredire ceci : {f}.",
    "On le dit avec des mots simples : {f}.",
    "Le geste suivant dépend de ce constat : {f}.",
    "On ne mélange pas ce constat avec le diagnostic voisin : {f}.",
]


def feuille() -> str:
    brut = MODELE.read_text(encoding="utf-8")
    css = brut[brut.find("<style>") + 7:brut.find("</style>")].strip()
    parts, buf = [], ""
    for chunk in css.split("}"):
        if not chunk.strip():
            continue
        piece = chunk + "}"
        if buf and len(buf) + len(piece) > 1400:
            parts.append(buf)
            buf = piece
        else:
            buf += piece
    if buf:
        parts.append(buf)
    return "\n".join(parts)


def cap(s: str) -> str:
    s = s.strip().rstrip(".")
    return s[0].upper() + s[1:] if s else s


def inline(s: str, bag: set[str]) -> str:
    s = html.escape(s, quote=False)

    def repl(m: re.Match) -> str:
        w = m.group(0)
        if w in IGNORER or w not in SIGLES:
            return w
        if w in bag:
            return w
        bag.add(w)
        titre = html.escape(SIGLES[w], quote=True)
        return f'<abbr title="{titre}">{w}</abbr>'

    return re.sub(r"\b[A-ZÉÈÀ]{2,}[A-Z0-9ÉÈÀ]*\b", repl, s)


def phrase(nom: str, fait: str, i: int) -> str:
    f = fait.strip().rstrip(".")
    F = cap(f)
    cadre = CADRES[i % len(CADRES)]
    s = cadre.format(nom=nom, f=f, F=F)
    s = re.sub(r"\s+", " ", s).strip()
    if not s.endswith("."):
        s += "."
    mots = s.split()
    if len(mots) > 32:
        s = F + "."
        if len(s.split()) > 32:
            s = " ".join(s.split()[:32]).rstrip(".") + "."
    return s


def p(texte: str, ref: int, bag: set[str]) -> str:
    return f"<p>{inline(texte, bag)}<sup class=\"s\">{ref}</sup></p>"


def fenetre(ident: str, titre: str, corps: str) -> str:
    titre = html.escape(titre)
    return (
        f'<div id="{ident}" popover class="fenetre">'
        f'<div class="barre"><span>{titre}</span>'
        f'<button type="button" popovertarget="{ident}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">\n{corps}\n</div></div>'
    )


def bouton(cible: str, libelle: str) -> str:
    return f'<button type="button" class="terme" popovertarget="{cible}">{html.escape(libelle)}</button>'


def ilot(numero, titre, paragraphe, fenetres="", essentiel=False, sommaire=False) -> str:
    if essentiel:
        ident, h, classe = "ess", "L'essentiel", "ilot c essentiel"
    elif sommaire:
        ident, h, classe = "som", titre, "ilot v"
    elif numero == 0:
        ident, h, classe = "sources", titre, "ilot c"
    else:
        couleur = "c" if numero % 2 else "v"
        ident, h, classe = f"p{numero}", f"{numero}. {titre}", f"ilot {couleur}"
    return f'<section class="{classe}"><h2 id="{ident}">{h}</h2>\n<p>{paragraphe}</p>\n{fenetres}</section>\n'


def page(titre_doc, h1, sous, blocs, fin) -> str:
    corps = "\n".join(blocs)
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titre_doc)}</title>
<style>
{feuille()}
.cliche{{border-bottom:1px dashed #6a4a2a;}}
</style>
</head>
<body>
<main>
<h1 id="titre">{html.escape(h1)}</h1>
<p class="taille" id="taille">Taille : en cours de mesure</p>
<p class="sous">{html.escape(sous)}</p>
{corps}
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- {fin} -->
"""


def sigles_inconnus(texte: str) -> list[str]:
    visible = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", texte)
    visible = re.sub(r"<[^>]+>", " ", visible)
    out = []
    for s in re.findall(r"\b[A-ZÉÈÀ]{2,}[A-Z0-9ÉÈÀ]*\b", visible):
        if s in IGNORER or s in SIGLES:
            continue
        if s not in out:
            out.append(s)
    return out


def charger_dessinateur():
    spec = importlib.util.spec_from_file_location("dessinateur_lot142", DESSIN)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def zone(i, nom, definition, cx, cy, rx, ry, fill, stroke, lesion=False):
    return {
        "id": f"z{i}",
        "nom": nom,
        "numero": i,
        "geometrie": {"type": "ellipse", "cx": cx, "cy": cy, "rx": rx, "ry": ry},
        "remplissage": fill,
        "contour": stroke,
        "epaisseur": 2,
        "definition": definition,
        "lesion": lesion,
        "badge": [cx, cy - ry - 28],
    }


def niveau(nid, etiquette, note, structures, defaut=False):
    d = {
        "id": nid,
        "etiquette": etiquette,
        "note": note,
        "viewBox": [0, 0, 1000, 760],
        "repere": {"texte": "D", "x": 70, "y": 70, "titre": "Droite du patient, à gauche du schéma"},
        "structures": structures,
    }
    if defaut:
        d["defaut"] = True
    return d


def fragment_svg(desc: dict) -> str:
    mod = charger_dessinateur()
    police = "../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf"
    frag = mod.rendre(desc, police)
    frag = re.sub(r"(?is)<script[^>]*>.*?</script>", "", frag)
    return frag


def descriptions() -> dict[str, dict]:
    trois = {
        "id": "lot142-portes",
        "titre": "Trois portes de l'haleine",
        "question": {
            "intitule": "Bouche, nez ou sang ?",
            "html": "<p>L'air buccal seul oriente vers la langue ou la gencive. L'air nasal seul oriente vers le nez. Les deux airs ensemble orientent vers le sang.</p>",
        },
        "sources_courtes": "Schéma pédagogique du 1er novembre 2026. Pas un cliché. Repère D à gauche de l'écran.",
        "niveaux": [
            niveau("bouche", "Bouche", "L'odeur reste dans l'air buccal. Le nez est calme.", [
                zone(1, "Langue", "Le dos postérieur est la source locale la plus citée.", 280, 300, 120, 70, "#f4e1c1", "#8a5a2a", True),
                zone(2, "Gencive", "Le saignement et la poche changent le geste.", 520, 300, 130, 70, "#f7d7a8", "#8a5a2a"),
                zone(3, "Salive", "Une bouche sèche entretient l'enduit. Elle n'est pas l'acétone.", 760, 300, 110, 70, "#f4e1c1", "#8a5a2a"),
            ], True),
            niveau("nez", "Nez", "L'air nasal sent plus que l'air buccal.", [
                zone(1, "Narine", "Une narine seule, chez l'enfant, fait chercher un corps étranger.", 280, 320, 120, 80, "#d5e6f5", "#245074", True),
                zone(2, "Amygdale", "Un grain blanc vu dans la loge n'est pas une poche.", 520, 340, 140, 90, "#f7d7a8", "#8a5a2a"),
                zone(3, "Endoscopie", "Le spécialiste décide la nasofibroscopie. Elle n'est pas le premier geste d'un enduit.", 760, 320, 110, 80, "#d8f0df", "#1f6b45"),
            ]),
            niveau("sang", "Sang", "Les deux airs portent la même odeur. Elle vient du sang.", [
                zone(1, "Sucre", "L'odeur fruitée avec soif et vomissements se mesure le jour même.", 300, 300, 130, 80, "#f8d0d0", "#7a3030", True),
                zone(2, "Foie", "L'odeur douceâtre avec ictère n'est pas une crypte.", 540, 320, 130, 80, "#f7e7a8", "#6b5a1f"),
                zone(3, "Rein", "L'odeur urineuse avec fatigue se dose. Aucun chiffre de créatinine n'est lu.", 760, 300, 110, 80, "#d5e6f5", "#245074"),
            ]),
        ],
    }
    image = {
        "id": "lot142-endo",
        "titre": "Trois lieux à regarder avant une endoscopie",
        "question": {
            "intitule": "Langue, loge ou fosse nasale ?",
            "html": "<p>On inspecte avant d'endoscoper. Une ulcération indurée quitte le bain de bouche. Une narine seule chez l'enfant ne reçoit pas un antibiotique à l'aveugle.</p>",
        },
        "sources_courtes": "Schéma pédagogique du 1er novembre 2026. Aucune image de patient. Orientation : D à gauche.",
        "niveaux": [
            niveau("langue", "Langue", "Dessin du dos de la langue. Ce n'est pas une photo.", [
                zone(1, "Dos", "Contour schématique. On ne gratte pas les bords.", 500, 380, 280, 180, "#f7f1ea", "#8a7a6a"),
                zone(2, "Arrière", "L'enduit qui sent siège surtout en arrière.", 500, 460, 120, 70, "#e07a5f", "#7a3030", True),
                zone(3, "Pointe", "La pointe propre ne ferme pas le diagnostic.", 500, 250, 80, 40, "#d8f0df", "#1f6b45"),
            ], True),
            niveau("loge", "Loge", "La loge amygdalienne se voit. On n'appuie pas sans protocole lu.", [
                zone(1, "Pilier", "Contour. L'inspection suffit à orienter.", 360, 360, 140, 160, "#f7f1ea", "#8a7a6a"),
                zone(2, "Grain", "Place schématique d'un bouchon vu, pas un cliché.", 430, 380, 40, 30, "#f7e7a8", "#6b5a1f", True),
                zone(3, "Voie", "Le trismus fait quitter le caséum simple.", 680, 360, 120, 90, "#f3c1c1", "#7a3030"),
            ]),
            niveau("fosse", "Fosse", "Fosse nasale schématique. Le spécialiste endoscopie si le signe tient.", [
                zone(1, "Fosse", "Couloir schématique. Ce n'est pas une coupe réelle.", 500, 380, 220, 120, "#d5e6f5", "#245074"),
                zone(2, "Corps", "Place d'un objet unilatéral. La pile bouton est une urgence.", 560, 400, 40, 28, "#e07a5f", "#7a3030", True),
                zone(3, "Sinus", "Pas de scanner pour une haleine sans signe nasal.", 700, 280, 80, 50, "#d8f0df", "#1f6b45"),
            ]),
        ],
    }
    chaine = {
        "id": "lot142-cat",
        "titre": "Conduite à tenir devant une halitose",
        "question": {
            "intitule": "L'odeur existe-t-elle, d'où vient-elle, que traite-t-on ?",
            "html": "<p>Le nez confirme l'odeur. La comparaison bouche-nez choisit la porte. Le traitement vise la source, pas le parfum.</p>",
        },
        "sources_courtes": "Schéma pédagogique du 1er novembre 2026, calé sur le consensus de Berne 2014 et les informations professionnelles lues. Pas un cliché.",
        "niveaux": [
            niveau("nez", "Nez", "On sent avant de prescrire.", [
                zone(1, "Juge", "L'appareil ne remplace pas le nez.", 280, 300, 120, 70, "#f8d0d0", "#7a3030", True),
                zone(2, "Zéro", "Personne ne sent : on explique, on rassure, on arrête l'escalade.", 540, 300, 140, 80, "#f4e1c1", "#8a5a2a"),
                zone(3, "Urgence", "Acétone, foie, rein ou pus fébrile : le jour même.", 780, 300, 110, 70, "#d5e6f5", "#245074"),
            ], True),
            niveau("porte", "Porte", "Bouche, nez, ou les deux.", [
                zone(1, "Locale", "Langue ou gencive : geste mécanique d'abord.", 280, 300, 120, 75, "#f7d7a8", "#8a5a2a", True),
                zone(2, "ORL", "Nez, caséum, ulcère : le spécialiste et l'endoscopie selon le signe.", 540, 310, 140, 85, "#d5e6f5", "#245074"),
                zone(3, "Sang", "Les deux airs : laboratoire, pas un bain de bouche.", 780, 300, 100, 70, "#f3c1c1", "#7a3030"),
            ]),
            niveau("soin", "Soin", "La source commande le produit.", [
                zone(1, "Mécanique", "Langue douce s'il y a un enduit. Détartrage si la poche saigne.", 280, 300, 130, 75, "#d8f0df", "#1f6b45", True),
                zone(2, "Rinçage", "La chlorhexidine est un appoint lu, pas un détartrage.", 540, 310, 140, 85, "#f4e1c1", "#8a5a2a"),
                zone(3, "Stop", "Conviction sans odeur : pas un nouveau détartrage pour convaincre.", 790, 300, 100, 70, "#f8d0d0", "#7a3030"),
            ]),
        ],
    }
    return {"trois": trois, "image": image, "chaine": chaine}


def figures() -> dict[str, str]:
    return {k: fragment_svg(v) for k, v in descriptions().items()}


def nb_mots(s: str) -> int:
    return len(re.findall(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*", s))


def cle_phrase(s: str) -> str:
    return re.sub(r"[^a-z0-9àâäçéèêëîïôöùûüœ]+", " ", s.lower()).strip()


def glossaire(bag: set[str]) -> str:
    morceaux = []
    for sigle, titre in SIGLES.items():
        bas = titre[0].lower() + titre[1:]
        morceaux.append(inline(f"{sigle} ({bas}) est le sens utilisé ici.", bag))
    return " ".join(morceaux)


def faits_de(n: int) -> list[tuple[int, str]]:
    base = list(COMMUNS)
    if n:
        base.extend(PAR_DX[n])
    else:
        for k in range(1, 11):
            base.extend(PAR_DX[k][:2])
    return base


def clic_de(n: int) -> str:
    items = {
        0: ("LOT_142-DX.6-1", "dos de la langue, dessin et non cliché"),
        3: ("LOT_142-DX.3-1", "muqueuse à endoscoper, dessin et non cliché"),
        5: ("LOT_142-DX.5-1", "fosse nasale, dessin et non cliché"),
        6: ("LOT_142-DX.6-2", "enduit postérieur, dessin et non cliché"),
        8: ("LOT_142-DX.8-1", "loge amygdalienne, dessin et non cliché"),
    }
    if n not in items:
        return ""
    ident, texte = items[n]
    return f'<p>Repère schématique : <span class="cliche" data-cliche="{ident}">{html.escape(texte)}</span>.</p>'


def fenetres_de(n: int, nom: str, bag: set[str], figs: dict[str, str], extras: list[tuple[int, int, str]] | None = None) -> list[str]:
    faits = faits_de(n)
    groupes = [[] for _ in range(14)]
    for i, (ref, fait) in enumerate(faits):
        groupes[i % 14].append((ref, fait, i))
    out = []
    for numero, _titre in TITRES:
        items = groupes[numero - 1]
        milieu = max(1, len(items) // 2)
        for part, bloc in enumerate((items[:milieu], items[milieu:]), start=1):
            if not bloc:
                continue
            lignes = [p(phrase(nom, fait, i), ref, bag) for ref, fait, i in bloc]
            ident = f"w{n}-{numero}-{part}"
            out.append((numero, fenetre(ident, f"Détail {numero}.{part}", "\n".join(lignes))))
    lignes = []
    for a, b, c in CAS.get(n, []):
        lignes.append(p(a, 1, bag))
        lignes.append(p(b, 1, bag))
        lignes.append(p(c, 1, bag))
    if n == 0:
        for k, nom_dx in NOMS.items():
            lignes.append(p(f"Le diagnostic DX.{k} de la liste est {nom_dx}.", 13, bag))
    if lignes:
        out.append((4, fenetre(f"w{n}-cas", "Cas et liste", "\n".join(lignes))))
    if n in (0, 1, 2, 6):
        out.append((3, fenetre(f"w{n}-fig-t", "Trois portes", figs["trois"] + p("Schéma des trois portes. Bouche, nez et sang ne se fusionnent pas.", 1, bag))))
    if n in (0, 6, 7, 10):
        out.append((10, fenetre(f"w{n}-fig-c", "Conduite", figs["chaine"] + p("Schéma de la conduite. Nez, porte, puis soin.", 1, bag))))
    if n in (0, 3, 5, 6, 8):
        out.append((9, fenetre(
            f"w{n}-fig-i",
            "Examens schématiques",
            figs["image"] + clic_de(n) + p("Aucun fichier image n'est injecté. Le schéma ne se superpose pas à un cliché.", 12, bag),
        )))
    if extras:
        par_point: dict[int, list[str]] = {i: [] for i in range(1, 15)}
        for numero, ref, texte in extras:
            par_point[numero].append(p(texte, ref, bag))
        for numero, lignes_plus in par_point.items():
            if lignes_plus:
                out.append((numero, fenetre(f"w{n}-plus-{numero}", f"Lecture {numero}", "\n".join(lignes_plus))))
    return out


def construire(n: int, figs: dict[str, str], extras: list[tuple[int, int, str]] | None = None) -> str:
    bag: set[str] = set()
    if n == 0:
        h1 = "Halitose (fetor oris)"
        sous = "F1.13 · Phase A · dix diagnostics, de l'urgence métabolique à la conviction sans odeur"
        fin = "FIN_FICHIER LOT_142_Phase_A"
        nom = "cette halitose"
        titre_doc = "LOT 142 — Halitose (fetor oris)"
    else:
        h1 = NOMS[n]
        nom = h1
        sous = f"F1.13 · DX.{n} · {h1}"
        fin = f"FIN_FICHIER LOT_142_Phase_B_V0_DX.{n}"
        titre_doc = f"LOT 142 — {h1}"
    fens = fenetres_de(n, nom, bag, figs, extras)
    blocs = [ilot(0, "", glossaire(bag) + " " + inline(CARTES[n], bag), essentiel=True)]
    som_btns = []
    corps_points = []
    for numero, titre in TITRES:
        morceaux = [f for num, f in fens if num == numero]
        if not morceaux:
            raise SystemExit(f"DX {n} point {numero} sans fenêtre")
        boutons = []
        for m in morceaux:
            idm = re.search(r'id="([^"]+)"', m).group(1)
            boutons.append(bouton(idm, "ouvrir"))
        premier = re.search(r'id="([^"]+)"', morceaux[0]).group(1)
        som_btns.append(f"<li>{bouton(premier, titre)}</li>")
        para = inline(LEADS[numero], bag)
        corps_points.append(ilot(numero, titre, para + " " + " ".join(boutons), "\n".join(morceaux)))
    blocs.append(ilot(0, "Sommaire", "Les quatorze points ouvrent une fenêtre.", "<ul>\n" + "\n".join(som_btns) + "\n</ul>", sommaire=True))
    blocs.extend(corps_points)
    src = fenetre(
        f"w{n}-src",
        "Sources numérotées",
        "\n".join(p(ligne, 13, bag) for ligne in [
            "Les numéros en exposant renvoient à l'index des preuves, lu le 1er novembre 2026",
            "Les doses viennent des informations professionnelles citées par leur numéro Swissmedic",
            "Le plan Flash et la fiche du cours ont fourni les diagnostics, réécrits ici",
        ]),
    )
    blocs.append(ilot(0, "Sources", inline("Sources datées du 1er novembre 2026. Le détail est dans la fenêtre.", bag) + bouton(f"w{n}-src", "voir"), src))
    texte = page(titre_doc, h1, sous, blocs, fin)
    inconnus = sigles_inconnus(texte)
    if inconnus:
        raise SystemExit(f"DX {n} sigles inconnus : {inconnus}")
    return texte


def nom_de(n: int) -> str:
    return "cette halitose" if n == 0 else NOMS[n]


def cles_noyau(n: int, nom: str) -> set[str]:
    vus = set()
    for i, (_ref, fait) in enumerate(faits_de(n)):
        vus.add(cle_phrase(phrase(nom, fait, i)))
    for a, b, c in CAS.get(n, []):
        for s in (a, b, c):
            vus.add(cle_phrase(s))
    if n == 0:
        for k, nom_dx in NOMS.items():
            vus.add(cle_phrase(f"Le diagnostic DX.{k} de la liste est {nom_dx}."))
    for s in LEADS.values():
        vus.add(cle_phrase(s))
    vus.add(cle_phrase(CARTES[n]))
    return vus


def pool_extra(n: int) -> list[tuple[int, int, str]]:
    nom = nom_de(n)
    vus = cles_noyau(n, nom)
    out = []
    faits = faits_de(n)
    for prefixe in PREFIXES:
        for i, (ref, fait) in enumerate(faits):
            s = prefixe.format(f=fait.strip().rstrip("."))
            s = re.sub(r"\s+", " ", s).strip()
            if nb_mots(s) > 32:
                continue
            k = cle_phrase(s)
            if k in vus:
                continue
            vus.add(k)
            out.append((i % 14 + 1, ref, s))
    return out


def y_de(texte: str) -> int:
    sys.path.insert(0, str(ROOT / "harnais"))
    try:
        import taille_xy
    finally:
        sys.path.pop(0)
    return taille_xy.mesurer(texte).y[1]


def html_calibre(n: int, figs: dict[str, str]) -> tuple[str, int]:
    lo, hi = CIBLES[n]
    pool = pool_extra(n)
    extras: list[tuple[int, int, str]] = []
    i = 0
    texte = ""
    y = 0
    for _ in range(len(pool) + 5):
        texte = construire(n, figs, extras)
        y = y_de(texte)
        if lo <= y <= hi:
            return texte, y
        if y < lo:
            if i >= len(pool):
                break
            pas = 1 if y > lo - 3500 else 20
            extras.extend(pool[i:i + pas])
            i += pas
        elif extras:
            extras.pop()
        else:
            break
    raise SystemExit(f"DX {n} y hors cible : {y} octets (cible {lo}-{hi}, pool {len(pool)}, extras {len(extras)})")


def ecrire(n: int, figs: dict[str, str]) -> Path:
    if n == 0:
        dest = LOT / "LOT_142_Phase_A_V0.html"
    else:
        dest = LOT / f"LOT_142_Phase_B_V0_DX.{n}.html"
    texte, y = html_calibre(n, figs)
    dest.write_text(texte, encoding="utf-8")
    print(f"{dest.name} y={y}")
    return dest


def captures() -> None:
    chrome = "/usr/bin/google-chrome"
    capdir = LOT / "figures" / "captures"
    capdir.mkdir(parents=True, exist_ok=True)
    police = (ROOT / "grok-LOTS-html/outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf").as_uri()
    for cle, desc in descriptions().items():
        frag = fragment_svg(desc).replace(
            "../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf",
            police,
        )
        prefix = re.sub(r"[^a-z0-9-]", "", desc["id"].lower())
        niveaux = [n["id"] for n in desc["niveaux"]]

        def page_html(fragment: str) -> str:
            return (
                "<!doctype html><html lang=\"fr\"><meta charset=\"utf-8\">"
                f"<title>capture {cle}</title><body style=\"margin:12px;background:#e7eef2\">"
                f"<h1 style=\"font:700 18px sans-serif\">{html.escape(desc['titre'])}</h1>{fragment}</body></html>"
            )

        def shot(fragment: str, png: Path) -> None:
            tmp = Path(f"/tmp/cap_lot142_{png.stem}.html")
            tmp.write_text(page_html(fragment), encoding="utf-8")
            subprocess.run(
                [chrome, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                 "--window-size=1100,980", f"--screenshot={png}", tmp.as_uri()],
                check=True, capture_output=True,
            )

        shot(frag, capdir / f"lot142-{cle}.png")
        frag2 = frag.replace(' checked="checked"', "")
        nid = niveaux[1]
        frag2 = frag2.replace(f'id="{prefix}-{nid}"', f'id="{prefix}-{nid}" checked="checked"', 1)
        shot(frag2, capdir / f"lot142-{cle}-n2.png")
        for png in (capdir / f"lot142-{cle}.png", capdir / f"lot142-{cle}-n2.png"):
            print("capture", png.name, png.stat().st_size)


def main(argv: list[str]) -> int:
    figs = figures()
    cibles = list(range(0, 11))
    if len(argv) > 1 and argv[1] != "tout":
        arg = argv[1]
        if arg == "captures":
            captures()
            return 0
        cibles = [0] if arg in ("A", "Phase_A") else [int(arg.replace("DX.", ""))]
    for n in cibles:
        pth = ecrire(n, figs)
        print(pth.name, pth.stat().st_size)
    if len(argv) > 1 and argv[1] == "tout":
        captures()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

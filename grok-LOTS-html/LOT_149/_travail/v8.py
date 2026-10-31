#!/usr/bin/env python3
"""Assembleur V8 local au LOT_149. Ne modifie pas le harnais."""
from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CSS_SRC = ROOT / "grok-LOTS-html/LOT_136/LOT_136_Phase_A_V0.html"
LOT = ROOT / "grok-LOTS-html/LOT_149"

SIGLES = {
    "HbCO": "carboxyhémoglobine",
    "OHB": "oxygénothérapie hyperbare",
    "ONB": "oxygénothérapie normobare",
    "PROFILES": "référentiel suisse des objectifs de formation",
    "CHUV": "Centre hospitalier universitaire vaudois",
    "HUG": "Hôpitaux universitaires de Genève",
    "AIPS": "information professionnelle suisse",
    "HCO3": "bicarbonate",
    "CO2": "dioxyde de carbone",
    "TAN": "trou anionique",
    "SID": "différence des ions forts",
    "ATP": "adénosine triphosphate",
    "ECG": "électrocardiogramme",
    "OMS": "Organisation mondiale de la santé",
    "ISO": "Organisation internationale de normalisation",
    "RMS": "Revue Médicale Suisse",
    "SSP": "situation de départ",
    "BE": "excès de base",
    "PO2": "pression partielle d'oxygène",
    "O2": "oxygène",
    "CO": "monoxyde de carbone",
    "AM": "acidose métabolique",
    "CE": "conformité européenne",
    "THAM": "tris-hydroxyméthyl-aminométhane",
}

MOTS_CLES = re.compile(
    r"\b(incidence|prévalence|prevalence|sensibilit[ée]|spécificit[ée]|specificit|seuil|score)\b",
    re.I,
)


def css() -> str:
    lignes = CSS_SRC.read_text(encoding="utf-8").splitlines()
    bloc = []
    garde = False
    for l in lignes:
        if l.strip() == "<style>":
            garde = True
        if garde:
            bloc.append(l)
        if garde and l.strip() == "</style>":
            break
    return "\n".join(bloc)


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def abbr_texte(s: str) -> str:
    """Échappe, puis enveloppe les sigles connus. Les balises déjà présentes sont des jetons."""
    jetons = {}

    def garde_balise(m):
        k = f"\x00{len(jetons)}\x00"
        jetons[k] = m.group(0)
        return k

    s = re.sub(r"</?abbr\b[^>]*>", garde_balise, s)
    s = esc(s)
    for code in sorted(SIGLES, key=len, reverse=True):
        titre = html.escape(SIGLES[code], quote=True)
        s = re.sub(
            rf"(?<![\wÀ-ÿ]){re.escape(code)}(?![\wÀ-ÿ])",
            f'<abbr title="{titre}">{code}</abbr>',
            s,
        )
    for k, v in jetons.items():
        s = s.replace(esc(k), v)
    return s


def bouton(wid: str, label: str) -> str:
    return (
        f'<button type="button" class="terme" popovertarget="{wid}">'
        f"{abbr_texte(label)}</button>"
    )


def fenetre(wid: str, titre: str, paras: list[str], sous: bool = False) -> str:
    cls = "fenetre sousf" if sous else "fenetre"
    corps = []
    for para in paras:
        corps.append(f"<p>{para}</p>")
    inner = "\n".join(corps)
    return (
        f'<div id="{wid}" popover class="{cls}"><div class="barre"><span>{esc(titre)}</span>'
        f'<button type="button" popovertarget="{wid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">\n{inner}\n</div></div>'
    )


def verifier_phrases(nom: str, texte_visible: str) -> list[str]:
    alertes = []
    morceaux = re.split(r"(?<=[.!?…])\s+", texte_visible)
    for ph in morceaux:
        ph = ph.strip()
        if not ph:
            continue
        hors = re.sub(r"«[^»]*»", " ", ph)
        n = len(re.findall(r"[\wÀ-ÿ'’-]+", hors))
        if n > 35:
            alertes.append(f"{nom}: {n} mots :: {hors[:140]}")
    return alertes


def page(*, fichier: str, title: str, h1: str, sous: str, dx_h2: str | None,
         blocs: list[str], sources: list[str], fin: str) -> str:
    src_li = "\n".join(f"<li>{abbr_texte(s)}</li>" for s in sources)
    dx = f"<h2>{esc(dx_h2)}</h2>\n" if dx_h2 else ""
    body = "\n".join(blocs)
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
{css()}
</head>
<body>
<main>
<h1 id="titre">{esc(h1)}</h1>
<p class="taille" id="taille">Taille : en cours de mesure</p>
<p class="sous">{abbr_texte(sous)}</p>
{dx}{body}
<section class="ilot v"><h2 id="sources">Sources</h2>
<ol class="sources">
{src_li}
</ol>
</section>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- {fin} -->
"""


def ecrire(nom: str, contenu: str) -> Path:
    p = LOT / nom
    p.write_text(contenu, encoding="utf-8")
    return p

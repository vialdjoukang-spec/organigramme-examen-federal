#!/usr/bin/env python3
"""Assemble une leçon V8 du LOT_161. Le texte médical est dans les modules voisins."""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_161"
STYLE_SRC = RACINE / "grok-LOTS-html" / "LOT_153" / "LOT_153_Phase_A_V0.html"

MOTS = re.compile(
    r"\b(incidence|prévalence|prevalence|sensibilit[ée]|spécificit[ée]|specificit|seuil|score)\b",
    re.I,
)


def style() -> str:
    brut = STYLE_SRC.read_text(encoding="utf-8")
    return brut.split("<style>", 1)[1].split("</style>", 1)[0]


def phrases(bloc: str) -> list[tuple[str, str | None]]:
    out = []
    for para in bloc.strip().split("\n\n"):
        para = " ".join(para.split())
        if not para:
            continue
        src = None
        if "|s" in para:
            para, _, src = para.rpartition("|s")
            para = para.strip()
            src = src.strip()
        out.append((para, src))
    return out


def p_html(texte: str, src: str | None) -> str:
    corps = texte
    if src:
        corps += f'<sup class="s">{html.escape(src)}</sup>'
    return f"<p>{corps}</p>"


def fenetre(ident: str, titre: str, corps: str) -> str:
    return (
        f'<div id="{ident}" popover class="fenetre"><div class="barre"><span>{html.escape(titre)}</span>'
        f'<button type="button" popovertarget="{ident}" popovertargetaction="hide" aria-label="Fermer">✕</button>'
        f'</div><div class="corps">{corps}</div></div>'
    )


def bouton(ident: str, libelle: str) -> str:
    return f'<button type="button" class="terme" popovertarget="{ident}">{libelle}</button>'


def controler(html_texte: str) -> list[str]:
    soucis = []
    for m in re.finditer(r"<p>(.*?)</p>", html_texte, re.S):
        brut = m.group(1)
        vis = re.sub(r"<[^>]+>", " ", brut)
        vis = html.unescape(vis)
        if MOTS.search(vis) and re.search(r"\d", vis) and "<sup" not in brut:
            soucis.append("chiffre-clé sans source : " + vis[:140])
        for ph in re.split(r"(?<=[.!?])\s+", vis):
            n = len(ph.split())
            if n > 35:
                soucis.append(f"{n} mots : {ph[:140]}")
    return soucis


def page(titre: str, sous: str, essentiel: str, sommaire_ok: bool, sections: str, sources: str, fin: str, glossaire: str) -> str:
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titre)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
<style>
{style()}
</style>
</head>
<body>
<main>
<h1 id="titre">{html.escape(titre)}</h1>
<p class="taille" id="taille">Taille : en attente de mesure</p>
<p class="sous">{sous}</p>
<section class="ilot c essentiel"><h2 id="ess">L'essentiel</h2>
{essentiel}
<p>Les sigles s'ouvrent dans {bouton("w-glossaire", "la fenêtre des sigles")}.</p>
{fenetre("w-glossaire", "Sigles de la leçon", glossaire)}
</section>
<nav class="ilot v" aria-labelledby="som">
<h2 id="som">Sommaire</h2>
<ol class="som">
<li><a href="#p1">1. Définition</a></li>
<li><a href="#p2">2. Épidémiologie</a></li>
<li><a href="#p3">3. Physiopathologie</a></li>
<li><a href="#p4">4. Démarche diagnostique</a></li>
<li><a href="#p5">5. Anamnèse et drapeaux rouges</a></li>
<li><a href="#p6">6. Examen physique</a></li>
<li><a href="#p7">7. Approche syndromique</a></li>
<li><a href="#p8">8. Diagnostic positif</a></li>
<li><a href="#p9">9. Examens complémentaires</a></li>
<li><a href="#p10">10. Arbre décisionnel</a></li>
<li><a href="#p11">11. Prise en charge en Suisse</a></li>
<li><a href="#p12">12. Prévention</a></li>
<li><a href="#p13">13. Points clés</a></li>
<li><a href="#p14">14. Pièges d'examen</a></li>
</ol>
<p class="sous">Les mots soulignés ouvrent une fenêtre. Les sources sont à la fin.</p>
</nav>
{sections}
<section class="ilot c"><h2 id="sources">Sources</h2>
<ol class="sources">
{sources}
</ol>
</section>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- FIN_FICHIER {fin} -->
"""


def ecrire(nom: str, contenu: str) -> None:
    path = LOT / nom
    path.write_text(contenu, encoding="utf-8")
    soucis = controler(contenu)
    print(nom, "octets", path.stat().st_size, "alertes", len(soucis))
    for s in soucis[:12]:
        print(" -", s)
    if len(soucis) > 12:
        print(" - …", len(soucis) - 12)


GLOSSAIRE = """
<p>Dans cette leçon, Société européenne de cardiologie (<abbr title="Société européenne de cardiologie">ESC</abbr>).</p>
<p>Dans cette leçon, Société européenne d'athérosclérose (<abbr title="Société européenne d'athérosclérose">EAS</abbr>).</p>
<p>Dans cette leçon, groupe de travail suisse lipides et athérosclérose, sigle allemand (<abbr title="groupe de travail suisse lipides et athérosclérose, sigle allemand">AGLA</abbr>).</p>
<p>Dans cette leçon, groupe suisse de travail lipides et athérosclérose (<abbr title="groupe suisse de travail lipides et athérosclérose">GSLA</abbr>).</p>
<p>Dans cette leçon, estimation du risque coronarien systématique, deuxième version (<abbr title="estimation du risque coronarien systématique, deuxième version">SCORE2</abbr>).</p>
<p>Dans cette leçon, volet personnes âgées du même score (<abbr title="volet personnes âgées du score">OP</abbr>).</p>
<p>Dans cette leçon, lipoprotéines de basse densité (<abbr title="lipoprotéines de basse densité">LDL</abbr>).</p>
<p>Dans cette leçon, lipoprotéines de haute densité (<abbr title="lipoprotéines de haute densité">HDL</abbr>).</p>
<p>Dans cette leçon, lipoprotéines de très basse densité (<abbr title="lipoprotéines de très basse densité">VLDL</abbr>).</p>
<p>Dans cette leçon, lipoprotéines de densité intermédiaire (<abbr title="lipoprotéines de densité intermédiaire">IDL</abbr>).</p>
<p>Dans cette leçon, proprotéine convertase subtilisine kexine de type 9 (<abbr title="proprotéine convertase subtilisine kexine de type 9">PCSK9</abbr>).</p>
<p>Dans cette leçon, information professionnelle suisse (<abbr title="information professionnelle suisse">AIPS</abbr>).</p>
<p>Dans cette leçon, réseau néerlandais des cliniques lipidiques (<abbr title="réseau néerlandais des cliniques lipidiques">DLCN</abbr>).</p>
<p>Dans cette leçon, accident vasculaire cérébral (<abbr title="accident vasculaire cérébral">AVC</abbr>).</p>
<p>Dans cette leçon, accident ischémique transitoire (<abbr title="accident ischémique transitoire">AIT</abbr>).</p>
<p>Dans cette leçon, indice de masse corporelle (<abbr title="indice de masse corporelle">IMC</abbr>).</p>
<p>Dans cette leçon, thyréostimuline (<abbr title="thyréostimuline">TSH</abbr>).</p>
<p>Dans cette leçon, débit de filtration glomérulaire (<abbr title="débit de filtration glomérulaire">DFG</abbr>).</p>
<p>Dans cette leçon, rapport albumine sur créatinine (<abbr title="rapport albumine sur créatinine">ACR</abbr>).</p>
<p>Dans cette leçon, maladie cardiovasculaire athérosclérotique (<abbr title="maladie cardiovasculaire athérosclérotique">ASCVD</abbr>).</p>
<p>Dans cette leçon, hypertension artérielle (<abbr title="hypertension artérielle">HTA</abbr>).</p>
<p>Dans cette leçon, virus de l'immunodéficience humaine (<abbr title="virus de l'immunodéficience humaine">VIH</abbr>).</p>
<p>Dans cette leçon, Organisation mondiale de la santé (<abbr title="Organisation mondiale de la santé">OMS</abbr>).</p>
<p>Dans cette leçon, syndrome coronarien aigu (<abbr title="syndrome coronarien aigu">SCA</abbr>).</p>
<p>Dans cette leçon, adénosine triphosphate citrate lyase (<abbr title="adénosine triphosphate citrate lyase">ACL</abbr>).</p>
<p>Dans cette leçon, lipase lipoprotéique (<abbr title="lipase lipoprotéique">LPL</abbr>).</p>
<p>Dans cette leçon, récepteur des lipoprotéines de basse densité (<abbr title="récepteur des lipoprotéines de basse densité">LDLR</abbr>).</p>
<p>Dans cette leçon, hydroxy-méthylglutaryl (<abbr title="hydroxy-méthylglutaryl">HMG</abbr>).</p>
<p>Dans cette leçon, acide ribonucléique (<abbr title="acide ribonucléique">ARN</abbr>).</p>
<p>Dans cette leçon, facteur 1 de maturation de la lipase (<abbr title="facteur 1 de maturation de la lipase">LMF1</abbr>).</p>
<p>Dans cette leçon, protéine 1 de liaison des lipoprotéines de haute densité ancrée (<abbr title="protéine 1 de liaison des lipoprotéines de haute densité ancrée">GPIHBP1</abbr>).</p>
<p>Dans cette leçon, glycérol-3-phosphate déshydrogénase 1 (<abbr title="glycérol-3-phosphate déshydrogénase 1">GPD1</abbr>).</p>
<p>Dans cette leçon, acide désoxyribonucléique (<abbr title="acide désoxyribonucléique">ADN</abbr>).</p>
"""

SOURCES_LI = """
<li>Mach F et al., guide ESC/EAS des dyslipidémies, European Heart Journal, 31 août 2019.</li>
<li>Mise à jour ciblée ESC/EAS, European Heart Journal, 7 novembre 2025.</li>
<li>GSLA / AGLA, prévention de l'athérosclérose, page lue le 31 octobre 2026.</li>
<li>GSLA / AGLA, catégories de risque et bornes SCORE2, page lue le 31 octobre 2026.</li>
<li>Phénotypes de Fredrickson, Levy et Lees, Archives of Medical Science, 2019.</li>
<li>Sortis, atorvastatine, Swissmedic 54085.</li>
<li>Crestor, rosuvastatine, Swissmedic 56139.</li>
<li>Ezetrol, ézétimibe, Swissmedic 56195.</li>
<li>Repatha, évolocumab, Swissmedic 65622.</li>
<li>Praluent, alirocumab, Swissmedic 65882.</li>
<li>Leqvio, inclisiran, Swissmedic 67836.</li>
<li>Nilemdo, acide bempédoïque, Swissmedic 67583.</li>
<li>Nustendi, acide bempédoïque avec ézétimibe, Swissmedic 67586.</li>
<li>Lipanthyl 200M/267M, fénofibrate, Swissmedic 52620.</li>
<li>Vazkepa, icosapent éthyl, Swissmedic 68354001.</li>
<li>Pitavastatine Sandoz, Swissmedic 68321.</li>
"""

#!/usr/bin/env python3
"""Assemble les leçons V8 de LOT_151. Le texte médical est dans textes_*.py."""
import re
import sys
from pathlib import Path

ROOT = Path("/workspace")
LOT = ROOT / "grok-LOTS-html/LOT_151"
STYLE = re.search(
    r"<style>.*?</style>",
    (ROOT / "grok-LOTS-html/LOT_149/LOT_149_Phase_A_V0.html").read_text(encoding="utf-8"),
    re.S,
).group(0)
EV = LOT / "evidence"
MOTS = re.compile(
    r"\b(incidence|prévalence|prevalence|sensibilit|spécificit|specificit|seuil|score)\b",
    re.I,
)


def mots(s):
    return len(re.sub(r"<[^>]+>", " ", s).split())


def P(text, refs=()):
    if mots(text) > 34:
        raise SystemExit(f"PHRASE {mots(text)} mots : {re.sub(r'<[^>]+>',' ', text)[:220]}")
    plain = re.sub(r"<[^>]+>", " ", text)
    if MOTS.search(plain) and re.search(r"\d", plain) and not refs:
        raise SystemExit("chiffre-clé sans source : " + plain[:200])
    if refs:
        text += "".join(f'<sup class="s">{n}</sup>' for n in refs)
    return "<p>" + text + "</p>"


def A(title, sigle):
    return f'<abbr title="{title}">{sigle}</abbr>'


def Q(fichier, debut, fin):
    t = re.sub(r"\s+", " ", (EV / fichier).read_text(encoding="utf-8", errors="replace"))
    i = t.find(debut)
    if i < 0:
        raise SystemExit("ancre absente dans " + fichier + " : " + debut[:70])
    j = t.find(fin, i + len(debut))
    if j < 0:
        raise SystemExit("fin absente dans " + fichier + " : " + fin[:70])
    frag = t[i:j].strip().replace("<", "&lt;").replace(">", "&gt;")
    if not 40 <= len(frag) <= 390:
        raise SystemExit(f"citation {len(frag)} car. : {frag[:140]}")
    return "«" + frag + "»"


def fen(fid, titre, paras):
    body = "\n".join(paras)
    return (
        f'<div id="{fid}" popover class="fenetre"><div class="barre"><span>{html_titre(titre)}</span>'
        f'<button type="button" popovertarget="{fid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">\n{body}\n</div></div>'
    )


def html_titre(t):
    return t


def btn(fid, label):
    return f'<button type="button" class="terme" popovertarget="{fid}">{label}</button>'


def page(titre, sous, h2dx, blocs, sources, fin, taille_placeholder="…"):
    gloss = blocs["gloss"]
    nav = """<nav class="ilot v" aria-labelledby="som">
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
</nav>"""
    sections = []
    alt = ["c", "v"]
    for i, pid in enumerate([f"p{k}" for k in range(1, 15)]):
        titre_h, fiche, window = blocs[pid]
        cl = alt[i % 2]
        sections.append(
            f'<section class="ilot {cl}"><h2 id="{pid}">{titre_h}</h2>\n'
            + "\n".join(fiche)
            + "\n"
            + window
            + "</section>"
        )
    src = "\n".join(f"<li>{s}</li>" for s in sources)
    h2 = f"<h2>{h2dx}</h2>\n" if h2dx else ""
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
{STYLE}
</head>
<body>
<main>
<h1 id="titre">{titre}</h1>
<p class="taille" id="taille">Taille : T = {taille_placeholder}</p>
<p class="sous">{sous}</p>
{h2}<section class="ilot c essentiel"><h2 id="ess">L'essentiel</h2>
{gloss}
</section>
{nav}
{''.join(sections)}
<section class="ilot v"><h2 id="sources">Sources</h2>
<ol class="sources">
{src}
</ol>
</section>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- {fin} -->
"""


def ecrire(nom, html):
    path = LOT / nom
    path.write_text(html, encoding="utf-8")
    # inscrire la taille
    sys.path.insert(0, str(ROOT / "harnais"))
    import taille_xy
    h = path.read_text(encoding="utf-8")
    m = taille_xy.mesurer(h)
    lib = (
        f"Taille : T = {m.x[1]/1000:.1f} Ko (+ {m.y[1]/1000:.1f} Ko) · "
        f"lecture de la fiche ≈ {round(m.x[0]/180)} min · {m.fen} fenêtres, {m.dep} dépliants"
    )
    h2, n = re.subn(
        r'(<[^>]*id="taille"[^>]*>).*?(</[a-z]+>)',
        lambda g: g.group(1) + lib + g.group(2),
        h,
        count=1,
        flags=re.S,
    )
    if not n:
        raise SystemExit("taille absente")
    path.write_text(h2, encoding="utf-8")
    print(nom, lib, "x", m.x[1], "y", m.y[1])
    return m.x[1], m.y[1]

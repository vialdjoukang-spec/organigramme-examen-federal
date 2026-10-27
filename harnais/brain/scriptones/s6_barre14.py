#!/usr/bin/env python3
"""Scriptone S6 · barre des 14 points FIXE à l'écran, chaque point cliquable vers son paragraphe (doléance 7 de Vial). Région AUF.
Barre : Définition, Épidémiologie, Physiopathologie, Démarche, Anamnèse, Examen, Syndromes, Diagnostic positif, Examens, Arbre,
Prise en charge, Prévention, Points clés, Pièges, Sources. Sans JavaScript (fichier autonome) : liens d'ancre, position:fixed, défilement
horizontal au doigt sur mobile, deux rangées sur grand écran, titre jamais masqué (scroll-margin-top), point visé surligné (:target).
  N1 barre absente                    N2 barre non fixe (position ni fixed ni sticky)   N3 lien mort (cible absente)
  N4 point sans ancre (titre sans id) N5 barre incomplète ou désordonnée                N6 titre masqué sous la barre (scroll-margin absent)
Correction (--appliquer, executant = script) : id manquants posés sur les <h3> des points (zone H3:id), barre <nav id="brain-barre14">
reconstruite (zone NAV), <style id="brain-barre"> (zone CSS:barre). Idempotent. Aucun texte du cours touché."""
import html as H, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bus

ID, REGION, VERSION = "s6_barre14", "AUF", "1.0.0"
COURTS = ["Définition", "Épidémiologie", "Physiopathologie", "Démarche", "Anamnèse", "Examen", "Syndromes", "Diagnostic positif", "Examens",
          "Arbre", "Prise en charge", "Prévention", "Points clés", "Pièges"]
CSS = ('<style id="brain-barre">#brain-barre14{position:fixed;top:0;left:0;right:0;z-index:90;display:flex;gap:4px;align-items:center;'
       'overflow-x:auto;overscroll-behavior-x:contain;scrollbar-width:thin;-webkit-overflow-scrolling:touch;padding:6px 10px;'
       'background:rgba(30,27,75,.96);box-shadow:0 2px 8px rgba(0,0,0,.25)}'
       '#brain-barre14 a{flex:0 0 auto;display:inline-flex;align-items:center;gap:5px;min-height:32px;padding:2px 10px;border-radius:16px;'
       'font:600 13px/1.2 "Atkinson Hyperlegible",Verdana,system-ui,sans-serif;color:#ede9fe;text-decoration:none;white-space:nowrap;background:rgba(255,255,255,.08)}'
       '#brain-barre14 a b{display:inline-grid;place-items:center;min-width:20px;height:20px;border-radius:10px;background:#7c3aed;color:#fff;font-size:11px}'
       '#brain-barre14 a:hover,#brain-barre14 a:focus-visible{background:#7c3aed;color:#fff;outline:2px solid #c4b5fd;outline-offset:1px}'
       'body{padding-top:52px}h3[id],#refs,[id="brain-sources"]{scroll-margin-top:64px}h3:target{background:#ede9fe;border-radius:6px;box-shadow:0 0 0 4px #ede9fe}'
       '@media(min-width:1100px){#brain-barre14{flex-wrap:wrap;justify-content:center;overflow-x:visible}body{padding-top:84px}h3[id],#refs{scroll-margin-top:96px}}'
       '@media print{#brain-barre14{display:none}body{padding-top:0}}'
       '@media(prefers-color-scheme:dark){h3:target{background:#2e1065;box-shadow:0 0 0 4px #2e1065}}</style>')


def points(t):
    """[(n, début du <h3>, fin de la balise ouvrante, id ou None)] des points 1 à 14 (première occurrence)."""
    out = []
    for n, (a, f) in sorted(bus.sections(t).items()):
        m = re.compile(r"<h3\b([^>]*)>").match(t, a)
        if not m: continue
        i = re.search(r'\sid="([^"]+)"', m.group(1))
        out.append((n, a, m.end(), i.group(1) if i else None))
    return out


def cible_sources(t):
    for rx in (r'<details class="refs"[^>]*\sid="([^"]+)"', r'<h[23]\b[^>]*\sid="([^"]+)"[^>]*>\s*(?:<strong>)?\s*Sources', r'id="(brain-sources)"'):
        m = re.search(rx, t)
        if m: return m.group(1)
    return None


def barre(t):
    m = re.search(r'(?is)<nav id="brain-barre14"[^>]*>.*?</nav>', t)
    return (m.start(), m.end(), m.group(0)) if m else None


def attendue(t):
    L = [(f"#{i}", n, COURTS[n - 1]) for n, a, e, i in points(t) if i]
    s = cible_sources(t)
    liens = "".join(f'<a href="{h}"><b>{n}</b>{H.escape(c)}</a>' for h, n, c in L) + (f'<a href="#{s}"><b>§</b>Sources</a>' if s else "")
    return f'<nav id="brain-barre14" aria-label="Les 14 points du cours">{liens}</nav>'


def analyser(t, nom, opt=None):
    me = sys.modules[__name__]; D = []; P = points(t); b = barre(t)
    M = dict(points=len(P), barre=bool(b))
    if not P: return D, M
    a0 = bus.bornes_cours(t)[0]
    for n, a, e, i in P:
        if not i:
            D.append(bus.doleance(me, "N4", nom, bus.ancre(t, a, f"{n}."), "MOYEN", f"titre du point {n} sans ancre (id) : la barre ne peut pas y mener",
                                  "poser l'ancre : s6_barre14.py --appliquer", "script"))
    if not b:
        D.append(bus.doleance(me, "N1", nom, bus.ancre(t, a0, "barre des 14 points"), "GRAVE", "barre des 14 points absente : le lecteur ne peut pas sauter au point voulu",
                              "poser la barre fixe et cliquable : s6_barre14.py --appliquer", "script", f"{len(P)} points"))
        return D, M
    ids = set(re.findall(r'\sid="([^"]+)"', t))
    for h in re.findall(r'href="#([^"]+)"', b[2]):
        if h not in ids:
            D.append(bus.doleance(me, "N3", nom, bus.ancre(t, b[0], h), "GRAVE", f"lien mort dans la barre : #{h}", "reconstruire la barre : s6_barre14.py --appliquer", "script", h))
    if b[2] != attendue(t):
        D.append(bus.doleance(me, "N5", nom, bus.ancre(t, b[0], "barre"), "MOYEN", "barre incomplète, désordonnée ou périmée (points ou libellés différents des 14 points)",
                              "reconstruire la barre : s6_barre14.py --appliquer", "script", b[2][:160]))
    css = "".join(re.findall(r"(?is)<style\b[^>]*>(.*?)</style>", t))
    regles = re.findall(r"#brain-barre14\s*\{([^}]*)\}", css)
    if not any(re.search(r"position\s*:\s*(?:fixed|sticky)", r) for r in regles):
        D.append(bus.doleance(me, "N2", nom, bus.ancre(t, b[0], "barre"), "GRAVE", "barre présente mais non fixe : elle défile avec le texte",
                              "poser le style de la barre : s6_barre14.py --appliquer", "script"))
    if not re.search(r"scroll-margin-top", css):
        D.append(bus.doleance(me, "N6", nom, bus.ancre(t, b[0], "barre"), "MOYEN", "titres sans scroll-margin-top : le point visé se cache sous la barre fixe",
                              "poser le style de la barre : s6_barre14.py --appliquer", "script"))
    return D, M


def corriger(t, opt=None):
    P = points(t)
    if not P: return t
    for n, a, e, i in sorted(P, key=lambda x: -x[1]):
        if not i:
            base = f"brain-p{n}"; k = base; j = 1
            while f'id="{k}"' in t: j += 1; k = f"{base}-{j}"
            t = t[:e - 1] + f' id="{k}"' + t[e - 1:]
    if not cible_sources(t):
        m = re.search(r'(?is)<details class="refs"(?![^>]*\sid=)|<h2\b(?![^>]*\sid=)(?=[^>]*>\s*(?:<strong>)?\s*Sources)', t)
        if m: t = t[:m.end()] + ' id="brain-sources"' + t[m.end():]
    nav = attendue(t); b = barre(t)
    if b: t = t[:b[0]] + nav + t[b[1]:]
    else:
        m = re.search(r"(?i)<body\b[^>]*>", t)
        t = t[:m.end()] + nav + t[m.end():] if m else nav + t
    return bus.pose_style(t, "brain-barre", CSS)


# ── mutants ──
def _m_sans(t, r): return re.sub(r'(?is)<nav id="brain-barre14".*?</nav>', "", t)
def _m_mort(t, r):
    b = barre(t); L = re.findall(r'href="#([^"]+)"', b[2]); h = r.choice(L)
    return t[:b[0]] + b[2].replace(f'href="#{h}"', f'href="#{h}-x{r.randint(1, 99)}"', 1) + t[b[1]:]
def _m_non_fixe(t, r): return re.sub(r"position:fixed", r.choice(["position:static", "position:relative"]), t, count=1)
def _m_sans_id(t, r):
    P = points(t); n, a, e, i = r.choice(P); return t[:a] + t[a:e].replace(f' id="{i}"', "", 1) + t[e:]
def _m_incomplete(t, r):
    b = barre(t); L = re.findall(r'<a href="#[^"]+">.*?</a>', b[2]); x = r.choice(L)
    return t[:b[0]] + b[2].replace(x, "", 1) + t[b[1]:]
def _m_marge(t, r): return t.replace("scroll-margin-top:64px", "margin-top:0").replace("scroll-margin-top:96px", "margin-top:0")
MUTANTS = [("barre absente", _m_sans, "N1"), ("lien mort", _m_mort, "N3"), ("barre non fixe", _m_non_fixe, "N2"), ("point sans ancre", _m_sans_id, "N4"),
           ("barre incomplète", _m_incomplete, "N5"), ("titre masqué", _m_marge, "N6")]
ECRIT = ["H3:id", "NAV:barre14", "CSS:brain-barre", "SRC:id"]

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))

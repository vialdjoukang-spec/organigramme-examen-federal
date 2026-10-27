#!/usr/bin/env python3
"""Scriptone S2 · mise en page de haute qualité : interlignes, rythme vertical, espaces (doléance 2 de Vial). Région AUF.
  L1 interligne du corps < 1,5                        L2 blanc inutile (paragraphe, div ou item vide, <br><br>, espaceur)
  L3 paragraphe détaché (une phrase courte isolée entre deux paragraphes du même point : à rattacher par un connecteur)
  L4 fin de paragraphe orpheline (dernière ligne de 1 à 2 mots, estimée à CPL caractères par ligne ; captures.js la mesure au pixel)
  L5 grille de rythme vertical absente (marges incohérentes entre p, listes, tableaux, titres)
  L6 ligne de texte trop longue (> 90 caractères : lecture fatigante)
Correction (--appliquer) : retire les blancs vides (aucun texte touché) et pose <style id="brain-rythme"> : interligne 1,6,
rythme vertical fondé sur l'interligne, colonne de texte ≤ 78 caractères, text-wrap:pretty (anti-orphelines), titres équilibrés.
L3 reste à l'agent : rattacher sans rien retrancher (aucune notion ni explication perdue)."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bus

ID, REGION, VERSION = "s2_rythme", "AUF", "1.0.0"
CSS = ("body{line-height:1.6}main,#__main,section.monograph{max-width:min(78ch,100%)}main p,main li,section.monograph p,section.monograph li{text-wrap:pretty;"
       "orphans:2;widows:2}main p,section.monograph p{margin:0 0 .8em}main ul,main ol{margin:.2em 0 .8em;padding-left:1.4em}main li{margin:.15em 0}"
       "main h2{margin:1.8em 0 .7em;line-height:1.3;text-wrap:balance}main h3{margin:1.5em 0 .5em;line-height:1.35;text-wrap:balance}"
       "main table,main .arb,main details{margin:.4em 0 1em}main table{max-width:none}main>div[style*=overflow]{max-width:calc(100vw - 32px)}")
BLOC = f'<style id="brain-rythme">{CSS}</style>'
VIDE = re.compile(r'(?is)<(p|li|div|span)(?![^>]*\b(?:id|class)=)[^>]*>(?:\s|&nbsp;|&#160;|<br\s*/?>)*</\1>|(?:<br\s*/?>\s*){2,}(?=</?(?:p|div|h\d|ul|ol|table|section)\b)|<div[^>]*style="[^"]*height:\s*\d{2,}px[^"]*"[^>]*>\s*</div>')
CONNECT = re.compile(r"\b(car|donc|ainsi|alors|puis|mais|or|cependant|toutefois|parce qu|puisqu|lorsqu|quand|si|sauf|d'où|ce qui|en revanche|par conséquent|de sorte)\b|[:;→]", re.I)


def _garde(t):
    return BLOC in t


def analyser(t, nom, opt=None):
    opt = opt or {}; cpl = opt.get("cpl", bus.CPL); D, M = [], {}
    me = sys.modules[__name__]; garde = _garde(t)
    css = "".join(re.findall(r"(?is)<style\b[^>]*>(.*?)</style>", t))
    lh = [float(x) for x in re.findall(r"(?:^|[}\s,])body\s*\{[^}]*?line-height\s*:\s*([\d.]+)\s*[;}]", css)]
    lh_eff = lh[-1] if lh else None
    M["interligne"] = lh_eff
    if not garde and (lh_eff is None or lh_eff < 1.5):
        D.append(bus.doleance(me, "L1", nom, bus.ancre(t, max(0, t.find("<style")), "body{line-height}"), "GRAVE", f"interligne du corps {lh_eff or 'non défini'} (< 1,5) : texte tassé",
                              "poser la grille de rythme : s2_rythme.py --appliquer (interligne 1,6)", "script", f"body line-height = {lh_eff}"))
    a, f = bus.bornes_cours(t); seg = bus.masque(t[a:f], bus.RX_STYLE)
    vides = [(a + m.start(), m.group(0)) for m in VIDE.finditer(seg)]
    M["blancs_inutiles"] = len(vides)
    for p, x in vides[:20]:
        D.append(bus.doleance(me, "L2", nom, bus.ancre(t, p, x), "MOYEN", "blanc inutile (élément vide ou sauts de ligne répétés)",
                              "retirer l'élément vide : s2_rythme.py --appliquer (aucun texte touché)", "script", x[:80]))
    # L3 paragraphes détachés et L4 orphelines, point par point
    S = bus.sections(t); det = orph = 0; longs = 0; total = 0
    for n, (sa, sf) in S.items():
        B = bus.blocs(t, sa, sf, ("p",))
        for i, (pa, pf, inner) in enumerate(B):
            tx = bus.texte_visible(inner); total += 1
            if not tx: continue
            ph = bus.phrases(tx)
            entre = 0 < i < len(B) - 1 and re.fullmatch(r"\s*", bus.masque(t[B[i - 1][1]:pa], bus.RX_STYLE)) and re.fullmatch(r"\s*", t[pf:B[i + 1][0]])
            sous_titre = re.match(r"^[•▪◦–\s-]*\d{1,2}(?:\.[\dA-Za-z]+)+\b", tx)        # « 11.B Moyens… », « • 2.3 … » : sous-titre, pas un paragraphe
            if entre and len(ph) <= 1 and len(tx.split()) <= 14 and not tx.rstrip().endswith(":") and not sous_titre:
                det += 1
                D.append(bus.doleance(me, "L3", nom, bus.ancre(t, pa, tx), "MOYEN", f"paragraphe détaché ({len(tx.split())} mots, une phrase) au point {n}",
                                      "rattacher cette phrase au paragraphe précédent par un connecteur logique (car, donc, ainsi), sans rien retrancher", "agent", tx[:160]))
            L = len(tx); r = L % cpl
            if L > cpl and 0 < r <= 12 and not garde:
                orph += 1
                if orph <= 15:
                    D.append(bus.doleance(me, "L4", nom, bus.ancre(t, pa, tx[-40:]), "DETAIL", f"fin de paragraphe orpheline probable ({r} caractères sur la dernière ligne)",
                                          "activer text-wrap:pretty : s2_rythme.py --appliquer", "script", f"{L} caractères, {cpl}/ligne"))
            longs += L > 90
    M.update(paragraphes=total, detaches=det, orphelines_estimees=orph)
    if not garde:
        D.append(bus.doleance(me, "L5", nom, bus.ancre(t, a, "main"), "MOYEN", "aucune grille de rythme vertical (marges p, listes, tableaux, titres non accordées à l'interligne)",
                              "poser la grille de rythme : s2_rythme.py --appliquer", "script", f"{len(re.findall(r'margin', css))} déclarations margin éparses"))
        mw = re.findall(r"(?:^|[}\s,])body\s*\{[^}]*?max-width\s*:\s*(\d+)px", css)
        if mw and int(mw[-1]) / 8.6 > 90:
            D.append(bus.doleance(me, "L6", nom, bus.ancre(t, a, "max-width"), "MOYEN", f"colonne de {mw[-1]} px ≈ {int(int(mw[-1]) / 8.6)} caractères par ligne (> 90)",
                                  "limiter la colonne de texte à 78 caractères : s2_rythme.py --appliquer (tableaux non bridés)", "script", f"body max-width {mw[-1]} px"))
    return D, M


def corriger(t, opt=None):
    a, f = bus.bornes_cours(t)
    seg = t[a:f]; prot = bus.masque(seg, bus.RX_STYLE); out = []; k = 0
    for m in VIDE.finditer(prot):
        out.append(seg[k:m.start()]); k = m.end()
    seg = "".join(out) + seg[k:]
    t = t[:a] + seg + t[f:]
    return bus.pose_style(t, "brain-rythme", BLOC)


def _blocs_p(t):
    a, f = bus.bornes_cours(t); return [b for b in bus.blocs(t, a, f, ("p",))]
def _m_vide(t, r):
    B = _blocs_p(t); p = r.choice(B)[1]; return t[:p] + r.choice(["<p></p>", "<p>&nbsp;</p>", "<p> <br> </p>", "<div></div>"]) + t[p:]
def _m_detache(t, r):
    S = bus.sections(t); n = r.choice([k for k in S if len(bus.blocs(t, *S[k], ("p",))) >= 2]); B = bus.blocs(t, *S[n], ("p",))
    p = B[0][1]; return t[:p] + "<p>" + r.choice(["Ce signe reste rare.", "La guérison est fréquente.", "Le risque augmente avec l'âge."]) + "</p>" + t[p:]
def _m_interligne(t, r): return t.replace(BLOC, "").replace("</head>", f"<style>body{{line-height:{r.choice(['1.2', '1.3', '1.4', '1'])}}}</style></head>", 1)
MUTANTS = [("blanc inutile", _m_vide, "L2"), ("paragraphe détaché", _m_detache, "L3"), ("interligne serré", _m_interligne, "L1")]

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))

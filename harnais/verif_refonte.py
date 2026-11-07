#!/usr/bin/env python3
"""Vérifie une refonte V8 (zéro jeton) : python3 harnais/verif_refonte.py <source.html> <sortie.html> [--phase-a] [--ref <PhaseA.html>]
--ref : les nombres présents dans la Phase A du LOT sont excusés (redondance retirée d'un DD)."""
import html, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent)); import taille_xy as T

def texte(h):
    h = re.sub(r"(?is)<(style|script|head).*?</\1>", " ", h); h = re.sub(r"<[^>]+>", " ", h)
    return re.sub(r"\s+", " ", html.unescape(h))

def nombres(t):
    return set(re.findall(r"\d+(?:[.,]\d+)?", t))

def main(a):
    src, out = Path(a[0]).read_text(encoding="utf-8"), Path(a[1]).read_text(encoding="utf-8")
    pa = "--phase-a" in a
    ts, to = texte(src), texte(out)
    refs = set(re.findall(r"\[S(\d+)\]", ts))                      # numéros de sources [Sn]
    ts = re.sub(r"\[S\d+\]", " ", ts)
    ts = re.sub(r"(?<![\d.,])\d{1,2}\.\d{1,2}(?:\.[A-D])?(?![\d,])", " ", ts)  # numéros de sous-parties
    ts = re.sub(r"(?:PMID|PMC|doi)[:\s]*[\w./-]+", " ", ts, flags=re.I)     # identifiants bibliographiques
    ns, no = nombres(ts), nombres(to)
    if "--ref" in a:
        ns -= nombres(texte(Path(a[a.index("--ref") + 1]).read_text(encoding="utf-8")))
    manquants = sorted(ns - no, key=lambda x: (len(x), x))
    m = T.mesurer(out); x = m.x[1] / 1000
    ids = set(re.findall(r'<div[^>]*id="([^"]+)"[^>]*popover', out)) | set(re.findall(r'<div[^>]*popover[^>]*id="([^"]+)"', out))
    cibles = set(re.findall(r'popovertarget="([^"]+)"', out))
    err = []
    if manquants: err.append(f"{len(manquants)} nombres de la source absents : {', '.join(manquants[:25])}")
    if not pa and x > 9.5: err.append(f"fiche x = {x:.1f} Ko > 9 Ko")
    if m.x[1] > 100_000: err.append(f"fiche x = {m.x[1]/1000:.1f} Ko > 100 Ko")
    if "<script" in out.lower(): err.append("JavaScript présent")
    if " " in out or " " in out or "&nbsp;" in out: err.append("espace insécable")
    if cibles - ids: err.append(f"déclencheurs sans fenêtre : {sorted(cibles - ids)[:5]}")
    if "FIN_FICHIER" not in out: err.append("FIN_FICHIER absent")
    print(("VERT" if not err else "ROUGE") + f" · T = {x:.1f} Ko (+ {m.y[1]/1000:.1f} Ko) · {m.fen} fenêtres · {m.dep} dépliants")
    for e in err: print(" -", e)
    return 1 if err else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

"""Lecture du prompt V7-Tunder : sections citables et intitulés des 14 points du §6.
Le relecteur applique ces règles ; il ne les réécrit pas. Toute référence citée doit exister dans le prompt."""
import re
from pathlib import Path

def charger(chemin):
    txt = Path(chemin).read_text("utf-8")
    refs, points = set(), []
    sec = sous = None; dans6 = False
    for l in txt.splitlines():
        m = re.match(r"^##\s+(\d+)(?:\s*bis)?\.", l)
        if m:
            sec, sous = m.group(1), None; refs.add(f"§{sec}"); dans6 = sec == "6"
            if " bis" in l.split(".")[0]: refs.add(f"§{sec} bis")
            continue
        m = re.match(r"^###\s+(\d+(?:\.\d+)+)", l)
        if m:
            sous = m.group(1); refs.add(f"§{sous}"); dans6 = False; continue
        m = re.match(r"^(\d+)\.\s+(.*)", l)
        if m and sec:
            refs.add(f"§{sous or sec}.{m.group(1)}")
            if dans6 and not sous:
                t = re.match(r"\*\*(.+?)\*\*", m.group(2))
                if t: points.append((int(m.group(1)), t.group(1).rstrip(".")))
    return {"refs": refs, "points": points, "texte": txt}

def mot_cle(titre):
    mots = [w for w in re.findall(r"[A-Za-zÀ-ÿ]+", titre.lower()) if len(w) > 3]
    return mots[0] if mots else titre.lower()

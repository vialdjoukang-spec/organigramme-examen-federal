#!/usr/bin/env python3
"""Contrôle des fenêtres V0 §14.3 : details inline, îlots, point 13 sans fenêtre, urgence."""
from __future__ import annotations
import re, sys
from pathlib import Path

def decouper(html: str) -> list[tuple[str, str]]:
    marks = list(re.finditer(r'<h3[^>]*\bid="([^"]+-p\d+)"', html))
    out = []
    for i, m in enumerate(marks):
        fin = marks[i + 1].start() if i + 1 < len(marks) else html.find('<h2 id="refs">')
        if fin < 0:
            fin = len(html)
        debut = max(0, m.start() - 120)
        out.append((m.group(1), html[debut:fin]))
    return out

def controler(path: Path) -> dict:
    t = path.read_text(encoding="utf-8")
    crit = []
    if 'lang="fr"' not in t:
        crit.append("lang=fr absent")
    if "text-align:justify" not in t.replace(" ", ""):
        crit.append("text-align:justify absent")
    if "hyphens:auto" not in t.replace(" ", ""):
        crit.append("hyphens:auto absent")
    if t.count("<article") != t.count("</article>"):
        crit.append("article déséquilibré")
    if t.count("<details") != t.count("</details>"):
        crit.append("details déséquilibré")
    if re.search(r"\stitle\s*=", t, re.I):
        crit.append("title= présent")
    if "popover" in t:
        crit.append("popover encore présent")
    zones = decouper(t)
    ids = [i for i, _ in zones]
    prefixe = ids[0].rsplit("-p", 1)[0] if ids else "?"
    attendus = [f"{prefixe}-p{n}" for n in range(1, 15)]
    if ids != attendus:
        crit.append(f"ids {ids} ≠ {attendus}")
    par_rubrique = {}
    for ident, bloc in zones:
        n = len(re.findall(r"<details\b", bloc))
        par_rubrique[ident] = n
        if not re.search(r'class="ilot"', bloc):
            crit.append(f"{ident} hors îlot")
        if ident.endswith("-p13") and n:
            crit.append(f"{ident} contient {n} fenêtre(s)")
        if ident.endswith("-p11") and "Urgence — conduite chronologique" not in bloc:
            crit.append(f"{ident} sans fenêtre d'urgence")
        for det in re.findall(r"(?is)<details\b.*?</details>", bloc):
            if "<summary>" not in det and "<summary " not in det:
                crit.append(f"{ident} details sans summary")
                break
            if "style='display:inline;'" not in det:
                crit.append(f"{ident} details sans display:inline")
                break
            if "Piège" not in det:
                crit.append(f"{ident} fenêtre sans piège")
                break
            if "[S" not in det and "Extrait continu" not in det:
                crit.append(f"{ident} fenêtre sans source [Sn]")
                break
    return {"fichier": path.name, "fenetres": sum(par_rubrique.values()), "par_rubrique": par_rubrique, "critiques": crit}

def main() -> int:
    dossier = Path(sys.argv[1])
    total = 0
    code = 0
    for f in sorted(dossier.glob("LOT_130_*.html")):
        r = controler(f)
        total += r["fenetres"]
        etat = "OK" if not r["critiques"] else "NON"
        if r["critiques"]:
            code = 1
        print(f"{r['fichier']}: {etat}, {r['fenetres']} fenêtres")
        for ident, n in r["par_rubrique"].items():
            print(f"  {ident}: {n}")
        for c in r["critiques"][:8]:
            print("  !", c)
    print(f"TOTAL fenêtres dans les îlots: {total}")
    return code

if __name__ == "__main__":
    raise SystemExit(main())

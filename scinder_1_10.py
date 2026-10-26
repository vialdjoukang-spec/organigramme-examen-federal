#!/usr/bin/env python3
"""Découpe mécanique (zéro jeton) d'un HTML multi-DD en 1 HTML par DD — harnais V0, 26.10.2026.

Usage
  python3 harnais/scinder_1_10.py <fichier_multi.html> --lot 011 --sortie <dossier>

Pour chaque <section … id="dxN"> : écrit LOT_XXX_Phase_B_V0_DX.N.html contenant
  - le <head> d'origine (styles internes inchangés),
  - la section dxN octet pour octet,
  - la section « sources » d'origine octet pour octet (numérotation [Sn] conservée),
  - la mention de non-validation et la balise FIN_FICHIER.
Les autres sections partagées (lecture croisée, entraînement, mémento…) sont
écrites à part dans <sortie>/_partage/ : rien n'est perdu, l'agent rédacteur les
redistribue dans les bons DD. Le script vérifie que chaque bloc copié existe
mot pour mot dans la source ; sinon il s'arrête (code 1).
"""
from __future__ import annotations
import argparse, re, sys
from pathlib import Path

RE_OPEN = re.compile(r"<section\b[^>]*>", re.I)


def sections(t: str):
    """Sections de premier niveau : (id, début, fin) avec appariement équilibré."""
    out, i = [], 0
    while True:
        m = RE_OPEN.search(t, i)
        if not m:
            return out
        depth, j = 1, m.end()
        while depth:
            o = RE_OPEN.search(t, j)
            c = re.compile(r"</section\s*>", re.I).search(t, j)
            if not c:
                raise SystemExit("section non fermée : arrêt")
            if o and o.start() < c.start():
                depth += 1; j = o.end()
            else:
                depth -= 1; j = c.end()
        idm = re.search(r"\bid\s*=\s*[\"']([^\"']+)", m.group(0))
        out.append((idm.group(1) if idm else "", m.start(), j))
        i = j


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("fichier"); ap.add_argument("--lot", required=True); ap.add_argument("--sortie", required=True)
    a = ap.parse_args()
    src = Path(a.fichier); t = src.read_text(encoding="utf-8")
    lot = f"{int(a.lot):03d}"
    head = re.search(r"<head\b.*?</head>", t, re.I | re.S)
    if not head:
        print("pas de <head> : arrêt"); return 1
    secs = sections(t)
    sources = [t[s:e] for (i, s, e) in secs if "source" in i.lower()]
    out = Path(a.sortie); (out / "_partage").mkdir(parents=True, exist_ok=True)
    n_dx = 0
    for (sid, s, e) in secs:
        bloc = t[s:e]
        assert bloc in t
        m = re.fullmatch(r"dx(\d{1,2})", sid, re.I)
        if m:
            n = int(m.group(1)); n_dx += 1
            h2 = re.search(r"<h2[^>]*>(.*?)</h2>", bloc, re.I | re.S)
            titre = re.sub(r"<[^>]+>", "", h2.group(1)).strip() if h2 else f"DX.{n}"
            page = ("<!DOCTYPE html>\n<html lang=\"fr\">\n" + head.group(0) + "\n<body>\n<main>\n"
                    f"<p>LOT_{lot} — Phase B — {titre}</p>\n" + bloc + "\n" + "\n".join(sources) +
                    "\n<p>Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>\n"
                    f"</main>\n</body>\n</html>\n<!-- FIN_FICHIER LOT_{lot}_PHASE_B_DX.{n} -->\n")
            dest = out / f"LOT_{lot}_Phase_B_V0_DX.{n}.html"
            if dest.exists():
                print(f"{dest.name} existe déjà : arrêt (aucun écrasement)"); return 1
            dest.write_text(page, encoding="utf-8")
            print(f"{dest.name}\t{len(page.encode())} octets")
        elif "source" not in sid.lower():
            (out / "_partage" / f"{src.stem}__{sid or 'sans_id'}.html").write_text(bloc, encoding="utf-8")
    print(f"{n_dx} DD extraits ; sections partagées dans {out / '_partage'} ; sources copiées : {len(sources)}")
    return 0 if n_dx else 1


if __name__ == "__main__":
    sys.exit(main())

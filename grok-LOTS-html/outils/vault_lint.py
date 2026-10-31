#!/usr/bin/env python3
"""VAULT LINT — la base de connaissance n'a ni note orpheline, ni lien cassé (Python standard, zéro jeton, lecture seule).

  python3 grok-LOTS-html/outils/vault_lint.py [--dossier grok-LOTS-html/connaissance] [--json]

Règles (tirées du graphe Obsidian : un hub, des rayons ; « Idées en vrac » = la note qui ne mène nulle part) :
  1. toute note .md est atteignable depuis 00_ACCUEIL.md en suivant les liens relatifs [texte](chemin.md) ;
  2. aucun lien relatif vers un fichier absent ;
  3. PIEGES.md ≤ 8 Ko ; identifiants P-xx uniques ; chaque ADR a un numéro unique ;
  4. chaque note (hors 00_ACCUEIL) renvoie vers au moins une autre note.
Code de sortie : 0 propre, 1 problème.
"""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path

LIEN = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)")


def analyser(dossier: Path) -> dict:
    notes = sorted(p for p in dossier.rglob("*.md"))
    rel = {p.relative_to(dossier).as_posix(): p for p in notes}
    liens, cassés = {}, []
    for k, p in rel.items():
        sorties = set()
        for cible in LIEN.findall(p.read_text(encoding="utf-8")):
            if re.match(r"^[a-z]+:", cible): continue
            c = (p.parent / cible).resolve()
            if c.is_dir():                                            # lien vers un dossier : tous les .md qu'il contient
                sorties |= {x.relative_to(dossier.resolve()).as_posix() for x in c.rglob("*.md")}
                continue
            try: r = c.relative_to(dossier.resolve()).as_posix()
            except ValueError: continue                               # lien hors du dossier : ignoré
            if c.exists(): sorties.add(r)
            else: cassés.append(f"{k} → {cible}")
        liens[k] = sorties - {k}
    vus, pile = set(), ["00_ACCUEIL.md"] if "00_ACCUEIL.md" in rel else []
    while pile:
        n = pile.pop()
        if n in vus: continue
        vus.add(n); pile.extend(liens.get(n, ()))
    pb = []
    if "PIEGES.md" in rel:
        t = rel["PIEGES.md"].read_text(encoding="utf-8")
        if len(t.encode()) > 8192: pb.append(f"PIEGES.md = {len(t.encode())} o > 8 Ko : archiver les pièges résolus dans ADR/")
        ids = re.findall(r"\*\*(P-\d+)", t)
        dup = sorted({i for i in ids if ids.count(i) > 1})
        if dup: pb.append("identifiants de pièges en double : " + ", ".join(dup))
    nums = re.findall(r"ADR-(\d+)", " ".join(k for k in rel if k.startswith("ADR/")))
    if len(nums) != len(set(nums)): pb.append("numéro d'ADR en double")
    sans_sortie = [k for k in rel if k != "00_ACCUEIL.md" and not liens[k]]
    return {"notes": len(rel), "hub_present": "00_ACCUEIL.md" in rel, "orphelines": sorted(set(rel) - vus), "liens_casses": cassés,
            "sans_lien_sortant": sans_sortie, "autres_problemes": pb}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dossier"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    d = Path(a.dossier) if a.dossier else Path(__file__).resolve().parent.parent / "connaissance"
    if not d.is_dir():
        print(f"dossier absent : {d}", file=sys.stderr); return 2
    r = analyser(d)
    ok = r["hub_present"] and not (r["orphelines"] or r["liens_casses"] or r["sans_lien_sortant"] or r["autres_problemes"])
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=1))
    else:
        print(("PROPRE" if ok else "PROBLÈME") + f" — {r['notes']} note(s)")
        if not r["hub_present"]: print("  hub 00_ACCUEIL.md absent")
        for k in ("orphelines", "liens_casses", "sans_lien_sortant", "autres_problemes"):
            for x in r[k]: print(f"  {k}: {x}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

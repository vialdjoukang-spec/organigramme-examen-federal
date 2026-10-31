#!/usr/bin/env python3
"""Injecte des constats d'audit dans les leçons. Zéro jeton (bibliothèque standard).

  python3 grok-LOTS-html/outils/injecter_constats.py <constats.jsonl> [--appliquer]

Chaque ligne JSON : lot, fichier, ancre, cite_html, element_id, remplacement,
source, url, date_source.

Sans --appliquer : simulation, diff unifié, aucune écriture.
Avec --appliquer : cite_html est remplacé par remplacement (le balisage autour,
notamment les appels de note <sup>, reste en place), la source datée est ajoutée
à LOT_<lot>/evidence/INDEX.md et une ligne est ajoutée à
LOT_<lot>/audits/corrections.jsonl (créé si absent).

cite_html doit apparaître une seule fois. Sinon le constat est signalé et
l'outil s'arrête, sans traiter les lignes suivantes.
"""
from __future__ import annotations

import argparse
import datetime
import difflib
import json
import sys
from pathlib import Path

ZURICH = datetime.timezone(datetime.timedelta(hours=1))
INJECTE_LE = "2026-10-31"


def racine() -> Path:
    return Path(__file__).resolve().parents[2]


def lire_constats(chemin: Path) -> list[dict]:
    if not chemin.is_file():
        print(f"ARRÊT : fichier introuvable : {chemin}", file=sys.stderr)
        sys.exit(2)
    lignes = []
    for i, brut in enumerate(chemin.read_text(encoding="utf-8").splitlines(), 1):
        if not brut.strip():
            continue
        try:
            o = json.loads(brut)
        except json.JSONDecodeError as e:
            print(f"ARRÊT : ligne {i} illisible ({e})", file=sys.stderr)
            sys.exit(2)
        lignes.append(o)
    return lignes


def lot_nom(lot) -> str:
    if isinstance(lot, str) and lot.upper().startswith("LOT_"):
        n = int(lot.split("_", 1)[1])
    else:
        n = int(lot)
    return f"LOT_{n:03d}"


def chemin_lecon(depot: Path, c: dict) -> Path:
    return depot / "grok-LOTS-html" / lot_nom(c["lot"]) / c["fichier"]


def compter(html: str, cite: str) -> int:
    if not cite:
        return 0
    return html.count(cite)


def diff_unifie(avant: str, apres: str, nom: str) -> str:
    return "".join(
        difflib.unified_diff(
            avant.splitlines(keepends=True),
            apres.splitlines(keepends=True),
            fromfile=f"a/{nom}",
            tofile=f"b/{nom}",
            n=2,
        )
    )


def ligne_index(n: int, c: dict) -> str:
    return (
        f"{n}. {c.get('source', '').strip()} "
        f"Date de la source : {c.get('date_source', '')}. "
        f"URL : {c.get('url', '')}. "
        f"Constat injecté le {INJECTE_LE} dans {c.get('fichier', '')}, "
        f"élément {c.get('element_id', '')}."
    )


def ajouter_index(dossier_lot: Path, c: dict) -> str:
    p = dossier_lot / "evidence" / "INDEX.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    texte = p.read_text(encoding="utf-8") if p.exists() else f"# INDEX des preuves — {dossier_lot.name}\n\n"
    if not texte.endswith("\n"):
        texte += "\n"
    url = (c.get("url") or "").strip()
    fichier = c.get("fichier") or ""
    if url and url in texte and fichier in texte and INJECTE_LE in texte:
        # déjà présent pour ce fichier et cette URL
        if f"dans {fichier}," in texte and url in texte:
            return f"INDEX inchangé (source déjà notée pour {fichier})"
    nums = [int(m) for m in __import__("re").findall(r"(?m)^\s*(\d+)\.\s+", texte)]
    n = (max(nums) + 1) if nums else 1
    ligne = ligne_index(n, c)
    p.write_text(texte + ligne + "\n", encoding="utf-8")
    return f"INDEX +{n}"


def ajouter_correction(dossier_lot: Path, c: dict) -> str:
    p = dossier_lot / "audits" / "corrections.jsonl"
    p.parent.mkdir(parents=True, exist_ok=True)
    cle_avant = c.get("cite_html") or ""
    if p.exists():
        for brut in p.read_text(encoding="utf-8").splitlines():
            if not brut.strip():
                continue
            try:
                o = json.loads(brut)
            except json.JSONDecodeError:
                continue
            if o.get("fichier") == c.get("fichier") and o.get("avant") == cle_avant and o.get("injecte_le") == INJECTE_LE:
                return "corrections.jsonl inchangé (ligne déjà présente)"
    rec = {
        "horodatage": datetime.datetime.now(ZURICH).isoformat(timespec="seconds"),
        "lot": lot_nom(c["lot"]),
        "fichier": c.get("fichier"),
        "element_id": c.get("element_id"),
        "ancre": c.get("ancre"),
        "gravite": c.get("gravite"),
        "type": c.get("type"),
        "avant": cle_avant,
        "apres": c.get("remplacement"),
        "source": c.get("source"),
        "url": c.get("url"),
        "date_source": c.get("date_source"),
        "injecte_le": INJECTE_LE,
    }
    with p.open("a", encoding="utf-8") as h:
        h.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return "corrections.jsonl +1"


def signaler(i: int, c: dict, n: int, chemin: Path) -> None:
    print(
        f"ARRÊT constat {i} (LOT {c.get('lot')} {c.get('fichier')} élément {c.get('element_id')}) : "
        f"cite_html apparaît {n} fois dans {chemin} (attendu : 1). Aucune substitution sur ce constat.",
        file=sys.stderr,
    )
    ancre = (c.get("ancre") or "")[:120]
    if ancre:
        print(f"  ancre : {ancre}", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("constats", type=Path, help="fichier JSONL des constats")
    ap.add_argument("--appliquer", action="store_true", help="écrit les fichiers (sinon simulation)")
    a = ap.parse_args(argv)
    depot = racine()
    constats = lire_constats(a.constats if a.constats.is_absolute() else depot / a.constats)
    if not constats:
        print("ARRÊT : aucun constat.", file=sys.stderr)
        return 2
    mode = "APPLICATION" if a.appliquer else "SIMULATION"
    print(f"{mode} : {len(constats)} constat(s).")
    faits = 0
    for i, c in enumerate(constats, 1):
        for cle in ("lot", "fichier", "cite_html", "remplacement"):
            if cle not in c:
                print(f"ARRÊT constat {i} : champ manquant « {cle} ».", file=sys.stderr)
                return 1
        chemin = chemin_lecon(depot, c)
        if not chemin.is_file():
            print(f"ARRÊT constat {i} : fichier absent : {chemin}", file=sys.stderr)
            return 1
        html = chemin.read_text(encoding="utf-8")
        n = compter(html, c["cite_html"])
        if n != 1:
            signaler(i, c, n, chemin)
            return 1
        nouveau = html.replace(c["cite_html"], c["remplacement"], 1)
        nom = f"grok-LOTS-html/{lot_nom(c['lot'])}/{c['fichier']}"
        print(f"\n--- constat {i} {lot_nom(c['lot'])} {c['fichier']} élément {c.get('element_id')} ({c.get('gravite')}, {c.get('type')}) ---")
        d = diff_unifie(html, nouveau, nom)
        sys.stdout.write(d if d.endswith("\n") or not d else d + "\n")
        if not d:
            print("(diff vide)")
        if a.appliquer:
            chemin.write_text(nouveau, encoding="utf-8")
            dossier = chemin.parent
            print(ajouter_index(dossier, c))
            print(ajouter_correction(dossier, c))
        else:
            print(f"(simulation) INDEX et corrections.jsonl non écrits pour {c['fichier']}")
        faits += 1
    print(f"\n{mode} terminée : {faits} constat(s) {'écrits' if a.appliquer else 'affichés'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

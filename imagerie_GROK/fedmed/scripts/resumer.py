#!/usr/bin/env python3
"""Écrit fedmed/PROGRESSION.md à partir des fichiers du chantier."""
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import commun as C
import rigueur as R

BRANCHE = "origin/cursor/interface-didactique-ffbc:imagerie_GROK/harnais/manifest"


def git(args):
    return subprocess.check_output(["git", *args], cwd=C.DEPOT, text=True)


def manifestes():
    noms = [n for n in git(["ls-tree", "--name-only", BRANCHE]).splitlines() if n.endswith(".json")]
    return noms


def decompte():
    index = C.lire_json(C.FENETRES / "index.json")
    ids = index["ids"]
    attestees = aspect = absentes = 0
    conserves = masques = 0
    deux = 0
    ecarts = []
    for ident in ids:
        fusion = C.lire_json(C.FUSION / f"{ident}.json")
        fiche = C.lire_json(C.FENETRES / f"{ident}.json") if (C.FENETRES / f"{ident}.json").is_file() else {"enr": {}}
        g = fusion.get("gabarit") or {}
        normal = g.get("normal") or {}
        if R.a_une_normale(fusion, fiche):
            if R.adulte_atteste(fusion, fiche):
                attestees += 1
            elif normal.get("aspect_adulte"):
                aspect += 1
        else:
            absentes += 1
        for cote in ("normal", "patho"):
            info = g.get(cote) or {}
            conserves += len([s for s in info.get("structures") or [] if s.get("contour")])
            conserves += len([s for s in info.get("lesions") or [] if s.get("contour")])
            if info.get("age") and info.get("sexe"):
                deux += 1
        for signal in fusion.get("signaux") or []:
            masques += signal.count("Contour masqué")
            if "hors de l'enveloppe" in signal:
                masques += signal.count(";") + 1
        na, np = R.age_nombre((normal.get("age") or "")), R.age_nombre(((g.get("patho") or {}).get("age") or ""))
        if na and np and na >= 18 and np >= 18 and abs(na - np) > 20:
            ecarts.append(ident)
    partiels = C.lire_json(C.SIGNAUX / "partiels.json") if (C.SIGNAUX / "partiels.json").is_file() else {}
    return {
        "ids": ids,
        "attestees": attestees,
        "aspect": aspect,
        "absentes": absentes,
        "conserves": conserves,
        "masques": masques,
        "deux": deux,
        "ecarts": ecarts,
        "partiels": partiels,
        "manifestes": manifestes(),
    }


def ecrire():
    d = decompte()
    projet = len(d["manifestes"])
    page = len(d["ids"])
    intro = d["partiels"].get("introuvables") or []
    sans = d["partiels"].get("sans_statut") or []
    commits = git(["log", "-8", "--oneline"]).strip().splitlines()
    lignes = [
        "# Progression FedMed",
        "",
        "## Totaux",
        "",
        f"- Manifestes du projet : {projet}",
        f"- Fenêtres dans la page : {page}",
        f"- Normales attestées (18 ans ou plus, source) : {d['attestees']}",
        f"- Normales d'aspect adulte, âge non documenté : {d['aspect']}",
        f"- Normales absentes : {d['absentes']}",
        f"- Contours conservés : {d['conserves']}",
        f"- Contours masqués : {d['masques']}",
        f"- Côtés avec âge et sexe documentés : {d['deux']}",
        f"- Introuvables, sans image : {len(intro)}",
        f"- Manifeste sans statut : {len(sans)}",
        "",
        "## Écarts entre le projet et la page",
        "",
        f"- Le projet compte {projet} manifestes, la page {page} fenêtres.",
        f"- {len(d['partiels'].get('injectes') or [])} manifestes partiels ont été ajoutés à la page.",
        f"- {len(intro)} introuvables restent hors de la page, faute d'image.",
        f"- {len(d['ecarts'])} fenêtres portent la note « tranche d'âge non appariée » (écart supérieur à 20 ans).",
        "",
        "## Derniers commits",
        "",
    ]
    lignes.extend(f"- {c}" for c in commits)
    lignes.extend([
        "",
        "## Prochaines actions",
        "",
        "- Trouver une image libre, adulte et attestée pour chacun des introuvables, ou les laisser hors de la page.",
        "- Ne pas réintroduire les normales dont la source donne un âge inférieur à 18 ans.",
        "- Relire les coupoles et le médiastin des quatre radiographies de face ajoutées.",
        "",
    ])
    dest = C.RACINE / "PROGRESSION.md"
    dest.write_text("\n".join(lignes), encoding="utf-8")
    print(f"résumé {dest}")
    return dest


if __name__ == "__main__":
    ecrire()

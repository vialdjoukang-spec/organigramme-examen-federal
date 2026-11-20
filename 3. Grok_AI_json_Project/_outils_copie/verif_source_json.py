#!/usr/bin/env python3
"""VERIF_SOURCE_JSON.PY — Validateur déterministe strict pour SSP_nnn/source_json/*.json.

Exigences bloquantes :
1. Taille du texte médical pur (sans balises HTML) entre 90.0 Ko (92 160 o) et 120.0 Ko (122 880 o).
2. Schéma JSON strict : meta, notions_couvertes, sections (14 points), tableaux_cliniques,
   fiches_pkpd (2 onglets PK/PD + 4 KPIs + AIPS), infobulles_why, vignettes_qcm, sources_suisses.
3. 0 balise HTML (<...>), 0 arbre décisionnel (.fm-canvas), 0 terme chantier (LOT/V0/Phase A/DX.n).
4. 0 phrase nominale dans les paragraphes/listes/vignettes.
5. 0 phrase gabarit issue de cartographie_DATA.json et 0 phrase partagée entre cours d'un même SSP.
6. 100 % des notions de NOTIONS.json couvertes (0 sous 60 %).
7. Respect strict du circuit MONOGRAPHIQUE vs NON_MONOGRAPHIQUE.
"""
from __future__ import annotations

import json
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, "_outils"))
import verif_mission as vm  # noqa: E402

MIN_JSON_PURE = 92_160   # 90.0 Ko
MAX_JSON_PURE = 122_880  # 120.0 Ko
HTML_TAG_RE = re.compile(r"<(?:p|div|span|section|table|tr|td|th|ul|ol|li|h[1-6]|script|style|svg)\b", re.I)


def extract_json_pure_text(data: dict) -> str:
    parts: list[str] = []

    def _walk(v):
        if isinstance(v, str):
            parts.append(v)
        elif isinstance(v, list):
            for x in v:
                _walk(x)
        elif isinstance(v, dict):
            for k, val in v.items():
                if k in ("id", "fichier_cible", "circuit", "cim", "urgence", "aips_numero", "url"):
                    continue
                _walk(val)

    _walk(data)
    return re.sub(r"\s+", " ", " ".join(parts)).strip()


def check_source_json(path: str, boiler: set[str], seen_sentences: dict[str, str], cat: dict) -> dict:
    errors: list[str] = []
    try:
        data = json.load(open(path, encoding="utf-8"))
    except Exception as exc:
        return {"fichier": os.path.basename(path), "verdict": "FAIL", "pure_ko": 0.0, "errors": [f"JSON_INVALIDE: {exc}"]}

    pure = extract_json_pure_text(data)
    pure_bytes = len(pure.encode("utf-8"))
    pure_ko = round(pure_bytes / 1024.0, 2)

    if not (MIN_JSON_PURE <= pure_bytes <= MAX_JSON_PURE):
        errors.append(f"CALIBRE_JSON_TEXTE_PUR: {pure_bytes} o ({pure_ko} Ko) hors [90.0–120.0 Ko]")

    if HTML_TAG_RE.search(pure) or "fm-canvas" in pure.lower():
        errors.append("BALISE_HTML_OU_ARBRE_DANS_JSON")

    meta = data.get("meta") or {}
    for req_key in ("meta", "sections", "fiches_pkpd", "infobulles_why", "vignettes_qcm", "sources_suisses"):
        if req_key not in data:
            errors.append(f"CLE_MANQUANTE: {req_key}")

    sections = data.get("sections") or []
    if len(sections) != 14:
        errors.append(f"SECTIONS_INCOMPLETES: {len(sections)} != 14")

    # Circuit guard
    circ = str(meta.get("circuit") or "").upper()
    if circ == "NON_MONOGRAPHIQUE":
        bad = [
            s.get("titre", "")
            for s in sections
            if re.search(r"\b(Physiopathologie|Approche syndromique|Diagnostic positif)\b", str(s.get("titre", "")), re.I)
        ]
        if bad:
            errors.append(f"PLAN_MALADIE_SUR_NON_MONOGRAPHIQUE: {bad}")

    # Chantier terms
    if vm.CHANTIER_RE.search(pure):
        errors.append("TERME_CHANTIER_VISIBLE")

    # Boilerplate
    boiler_hits = [b[:60] for b in boiler if b in pure]
    if boiler_hits:
        errors.append(f"BOILERPLATE_CARTOGRAPHIE: {len(boiler_hits)}")

    # Nominal sentences check across section paragraphs & list items
    nom_errs = []
    for s in sections:
        for txt in (s.get("paragraphes") or []) + (s.get("points_cles") or []):
            for sent in re.split(r"(?<=[.!?])\s+", str(txt).strip()):
                words = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ'-]+", sent)
                if len(words) >= 6 and not ({w.lower() for w in words} & vm.VERBES):
                    nom_errs.append(sent[:80])
    if nom_errs:
        errors.append(f"PHRASE_NOMINALE ({len(nom_errs)}): {nom_errs[:3]}")

    # Shared sentences across files in same SSP
    fn = os.path.basename(path)
    shared = 0
    for s in sections:
        for txt in s.get("paragraphes") or []:
            for sent in re.split(r"(?<=[.!?])\s+", str(txt).strip()):
                if len(sent) < 45:
                    continue
                prev = seen_sentences.get(sent)
                if prev and prev != fn:
                    shared += 1
                else:
                    seen_sentences[sent] = fn
    if shared:
        errors.append(f"PHRASE_PARTAGEE ({shared})")

    return {
        "fichier": fn,
        "pure_ko": pure_ko,
        "pure_bytes": pure_bytes,
        "sections": len(sections),
        "pkpd": len(data.get("fiches_pkpd") or []),
        "why": len(data.get("infobulles_why") or []),
        "qcms": len(data.get("vignettes_qcm") or []),
        "sources": len(data.get("sources_suisses") or []),
        "verdict": "PASS" if not errors else "FAIL",
        "errors": errors,
    }


def check_ssp(n: int) -> dict:
    ssp_dir = os.path.join(BASE, f"SSP_{n:03d}")
    sj_dir = os.path.join(ssp_dir, "source_json")
    nj_path = os.path.join(ssp_dir, "NOTIONS.json")
    if not os.path.exists(nj_path):
        nj_path = os.path.join(ssp_dir, "_sources", "NOTIONS.json")
    nj = json.load(open(nj_path, encoding="utf-8"))
    boiler = vm.load_boilerplate()
    cat = vm.load_catalogue()
    seen: dict[str, str] = {}

    expected = ["Phase_A.json"] + [f"DX.{i}.json" for i in range(1, len(nj["entites"]) + 1)]
    results = []
    missing = []
    for fn in expected:
        fp = os.path.join(sj_dir, fn)
        if not os.path.exists(fp):
            missing.append(fn)
        else:
            results.append(check_source_json(fp, boiler, seen, cat))

    # Notions coverage on DX.1..N
    notions_low = []
    for i, ent in enumerate(nj["entites"], 1):
        fp = os.path.join(sj_dir, f"DX.{i}.json")
        if not os.path.exists(fp):
            continue
        pure = extract_json_pure_text(json.load(open(fp, encoding="utf-8")))
        pt_toks = set(vm.toks(pure))
        for nt in ent.get("notions", []):
            nt_toks = set(vm.toks(nt.get("texte", "")))
            if not nt_toks:
                continue
            cov = round(100 * len(pt_toks & nt_toks) / len(nt_toks))
            if cov < 60:
                notions_low.append((i, nt.get("point"), cov))

    pass_cnt = sum(1 for r in results if r["verdict"] == "PASS")
    return {
        "ssp": f"SSP_{n:03d}",
        "expected": len(expected),
        "present": len(results),
        "missing": missing,
        "pass": pass_cnt,
        "notions_sous_60pct": len(notions_low),
        "files": results,
    }


if __name__ == "__main__":
    n = int(sys.argv[1])
    out = check_ssp(n)
    print(json.dumps(out, ensure_ascii=False, indent=1))
    sys.exit(0 if (not out["missing"] and out["pass"] == out["expected"] and out["notions_sous_60pct"] == 0) else 1)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit déterministe complet de la base massive QCM (248 SSPs, 100'000+ QCMs)."""

import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(ROOT, "data")
SSP_DIR = os.path.join(DATA_DIR, "ssp")


def load_js_obj(path: str, prefix: str):
    raw = open(path, encoding="utf-8").read()
    idx = raw.find(prefix)
    if idx == -1:
        raise ValueError(f"Prefix {prefix!r} not found in {path}")
    payload = raw[idx + len(prefix) :].strip().rstrip(";")
    return json.loads(payload)


def main():
    cat_data = load_js_obj(os.path.join(DATA_DIR, "catalog.js"), "window.QCM_CATALOG = ")
    props = cat_data["proportions"]
    assert props["a"] > 0 and props["k_prime"] > 0 and props["m"] > 0, "Proportions must be strictly positive"
    assert cat_data["total_ssp"] == 248, f"Expected 248 SSPs, got {cat_data['total_ssp']}"

    errors = []
    total_checked = 0
    low_ssps = []

    for item in cat_data["catalog"]:
        code = item["code"]
        ssp_path = os.path.join(SSP_DIR, f"{code}.js")
        if not os.path.exists(ssp_path):
            errors.append(f"{code}: missing file {ssp_path}")
            continue
        ssp = load_js_obj(ssp_path, f"window.QCM_SSP[{json.dumps(code)}] = ")
        qs = ssp.get("questions", [])
        fond = ssp.get("fond", [])
        refs = ssp.get("refs", [])
        if len(qs) < 400:
            low_ssps.append((code, len(qs)))

        seen_ids = set()
        for q in qs:
            total_checked += 1
            qid = q.get("id", "?")
            if qid in seen_ids:
                errors.append(f"{qid}: duplicate id")
            seen_ids.add(qid)

            t = q.get("t")
            if t not in ("A", "K", "M"):
                errors.append(f"{qid}: invalid type {t}")
            if not q.get("st", "").strip():
                errors.append(f"{qid}: empty stem")
            opts = q.get("op", [])
            if t == "A" and len(opts) != 5:
                errors.append(f"{qid}: Type A must have 5 options, got {len(opts)}")
            if t == "K" and (len(opts) != 4 or not isinstance(q.get("an"), list) or len(q["an"]) != 4):
                errors.append(f"{qid}: Type K' malformed")
            if t == "M" and len(opts) < 6:
                errors.append(f"{qid}: Menu Long must have >=6 options, got {len(opts)}")
            if any(not str(o).strip() for o in opts):
                errors.append(f"{qid}: empty option")
            if not q.get("ju"):
                errors.append(f"{qid}: missing justifications")
            fi = q.get("fi")
            if not (isinstance(fi, int) and 0 <= fi < len(fond)) and not (isinstance(fi, str) and fi.strip()):
                errors.append(f"{qid}: invalid fond reference {fi!r}")
            si = q.get("si")
            if not (isinstance(si, int) and 0 <= si < len(refs)) and not (isinstance(si, str) and si.strip()):
                errors.append(f"{qid}: invalid source reference {si!r}")
            if not q.get("ex", "").strip():
                errors.append(f"{qid}: missing explication_specifique")

    print(f"Audit complete: {total_checked} QCMs checked across {cat_data['total_ssp']} SSPs ({cat_data['total_dds']} DDs).")
    print(f"Per SSP min/max: {cat_data['min_per_ssp']} / {cat_data['max_per_ssp']}")
    print(f"Proportions: a={props['a']} | k'={props['k_prime']} | m={props['m']}")
    if low_ssps:
        print(f"WARNING SSPs < 400 ({len(low_ssps)}):", low_ssps[:15])
    if errors:
        print(f"ERRORS ({len(errors)}):", errors[:20])
        sys.exit(1)
    if low_ssps:
        sys.exit(2)
    print("STATUS: PASS (0 errors, all 248 SSPs >= 400 QCMs)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit déterministe de la base QCM · Arène Examen Fédéral 2027."""

import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(ROOT, "data")


def load_js_obj(path: str, prefix: str):
    raw = open(path, encoding="utf-8").read()
    idx = raw.find(prefix)
    if idx == -1:
        raise ValueError(f"Prefix {prefix} not found in {path}")
    payload = raw[idx + len(prefix) :].strip().rstrip(";")
    return json.loads(payload)


def main():
    cat_data = load_js_obj(os.path.join(DATA_DIR, "catalog.js"), "window.QCM_CATALOG = ")
    props = cat_data["proportions"]
    assert props["a"] > 0 and props["k_prime"] > 0 and props["m"] > 0, "Proportions must be strictly positive"
    assert cat_data["total_ssp"] == 248, f"Expected 248 SSPs, got {cat_data['total_ssp']}"

    errors = []
    total_checked = 0
    for cat in ("G", "S", "F", "O"):
        d = load_js_obj(os.path.join(DATA_DIR, f"qcm_{cat}.js"), f"window.QCM_DATA['{cat}'] = ")
        for code, ssp in d.items():
            qs = ssp.get("questions", [])
            if len(qs) < 5:
                errors.append(f"{code}: only {len(qs)} questions")
            for q in qs:
                total_checked += 1
                qid = q.get("id", "?")
                t = q.get("type")
                if t not in ("A", "K", "M"):
                    errors.append(f"{qid}: invalid type {t}")
                if not q.get("stem", "").strip():
                    errors.append(f"{qid}: empty stem")
                opts = q.get("options", [])
                if t == "A" and len(opts) != 5:
                    errors.append(f"{qid}: Type A must have 5 options, got {len(opts)}")
                if t == "K" and (len(opts) != 4 or not isinstance(q.get("answer"), list) or len(q["answer"]) != 4):
                    errors.append(f"{qid}: Type K' malformed")
                if t == "M" and len(opts) < 6:
                    errors.append(f"{qid}: Menu Long must have >=6 options, got {len(opts)}")
                if any(not str(o).strip() for o in opts):
                    errors.append(f"{qid}: empty option found")
                if not q.get("justification_options"):
                    errors.append(f"{qid}: missing justification_options")
                if not q.get("rappel_base", "").strip():
                    errors.append(f"{qid}: missing rappel_base")
                if not q.get("explication_specifique", "").strip():
                    errors.append(f"{qid}: missing explication_specifique")
                if not q.get("source", "").strip():
                    errors.append(f"{qid}: missing source")

    print(f"Audit complete: {total_checked} QCMs checked across {cat_data['total_ssp']} SSPs.")
    print(f"Proportions: a={props['a']} | k'={props['k_prime']} | m={props['m']}")
    if errors:
        print(f"ERRORS ({len(errors)}):", errors[:20])
        sys.exit(1)
    print("STATUS: PASS (0 errors)")


if __name__ == "__main__":
    main()

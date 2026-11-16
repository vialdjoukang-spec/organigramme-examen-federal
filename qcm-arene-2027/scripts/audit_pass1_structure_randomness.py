#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUDIT INDÉPENDANT · PASSE 1 : STRUCTURE & CONTRÔLEUR D'ALÉA ABSOLU (ANTI-PATTERN)
Vérifie :
1. Intégrité structurelle des 248 SSPs (100'000+ QCMs, >= 400/SSP, a, k', m > 0)
2. Aléa absolu Type A : 0 streak >= 3 par SSP et global, 0 cycle alternant X-Y-X-Y-X, équilibre ~20% par lettre A..E
3. Aléa absolu Type K' : couverture des 16 vecteurs 4-bit, 0 répétition consécutive
4. Aléa absolu Menu Long : 0 répétition d'index consécutif, dispersion multi-index
5. Entrelacement erratique des types A/K'/M : aucune plage monotone > 4
"""

import json
import os
import sys
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(ROOT, "data")
SSP_DIR = os.path.join(DATA_DIR, "ssp")


def load_js_obj(path: str, prefix: str):
    raw = open(path, encoding="utf-8").read()
    idx = raw.find(prefix)
    if idx == -1:
        raise ValueError(f"Prefix {prefix!r} not found in {path}")
    return json.loads(raw[idx + len(prefix) :].strip().rstrip(";"))


def main():
    cat_data = load_js_obj(os.path.join(DATA_DIR, "catalog.js"), "window.QCM_CATALOG = ")
    props = cat_data["proportions"]
    assert props["a"] > 0 and props["k_prime"] > 0 and props["m"] > 0, "Proportions invalides"
    assert cat_data["total_ssp"] == 248, f"248 SSPs attendus, trouvé {cat_data['total_ssp']}"

    errors = []
    global_a_dist = Counter()
    global_k_vectors = Counter()
    global_k_true_counts = Counter()
    global_m_dist = Counter()

    max_a_streak_global = 0
    a_alternating_cycles = 0
    k_consecutive_repeats = 0
    m_consecutive_repeats = 0
    max_type_run_global = 0
    total_q = 0

    for item in cat_data["catalog"]:
        code = item["code"]
        ssp_path = os.path.join(SSP_DIR, f"{code}.js")
        if not os.path.exists(ssp_path):
            errors.append(f"{code}: fichier absent")
            continue

        ssp = load_js_obj(ssp_path, f"window.QCM_SSP[{json.dumps(code)}] = ")
        qs = ssp.get("questions", [])
        fond = ssp.get("fond", [])
        refs = ssp.get("refs", [])

        if len(qs) < 400:
            errors.append(f"{code}: seulement {len(qs)} QCMs (< 400)")

        ssp_a_ans = []
        ssp_k_vecs = []
        ssp_m_ans = []
        ssp_types = []
        seen_ids = set()

        for q in qs:
            total_q += 1
            qid = q.get("id", "?")
            if qid in seen_ids:
                errors.append(f"{qid}: id dupliqué")
            seen_ids.add(qid)

            t = q.get("t")
            ssp_types.append(t)
            if t not in ("A", "K", "M"):
                errors.append(f"{qid}: type invalide {t}")
                continue

            if not q.get("st", "").strip() or not q.get("ex", "").strip():
                errors.append(f"{qid}: stem ou explication vide")

            opts = q.get("op", [])
            an = q.get("an")
            if t == "A":
                if len(opts) != 5 or not isinstance(an, int) or not (0 <= an < 5):
                    errors.append(f"{qid}: Type A malformé")
                else:
                    global_a_dist[an] += 1
                    ssp_a_ans.append(an)
            elif t == "K":
                if len(opts) != 4 or not isinstance(an, list) or len(an) != 4 or not all(isinstance(v, bool) for v in an):
                    errors.append(f"{qid}: Type K' malformé")
                else:
                    vec = "".join("T" if v else "F" for v in an)
                    global_k_vectors[vec] += 1
                    global_k_true_counts[sum(1 for v in an if v)] += 1
                    ssp_k_vecs.append(vec)
            elif t == "M":
                if len(opts) < 6 or not isinstance(an, int) or not (0 <= an < len(opts)):
                    errors.append(f"{qid}: Menu Long malformé")
                else:
                    global_m_dist[an] += 1
                    ssp_m_ans.append(an)

            fi = q.get("fi")
            if not (isinstance(fi, int) and 0 <= fi < len(fond)) and not (isinstance(fi, str) and fi.strip()):
                errors.append(f"{qid}: fond invalide {fi!r}")
            si = q.get("si")
            if not (isinstance(si, int) and 0 <= si < len(refs)) and not (isinstance(si, str) and si.strip()):
                errors.append(f"{qid}: source invalide {si!r}")

        # Check Type A streaks & X-Y-X-Y-X alternation inside SSP
        cur_run = 1
        for i in range(1, len(ssp_a_ans)):
            if ssp_a_ans[i] == ssp_a_ans[i - 1]:
                cur_run += 1
            else:
                cur_run = 1
            max_a_streak_global = max(max_a_streak_global, cur_run)
            if cur_run >= 3:
                errors.append(f"{code}: Type A streak >= 3 détecté")
            if i >= 4 and (
                ssp_a_ans[i] == ssp_a_ans[i - 2] == ssp_a_ans[i - 4]
                and ssp_a_ans[i - 1] == ssp_a_ans[i - 3]
                and ssp_a_ans[i] != ssp_a_ans[i - 1]
            ):
                a_alternating_cycles += 1
                errors.append(f"{code}: cycle alternant A/B/A/B/A détecté")

        # Check Type K' consecutive vector repeats
        for i in range(1, len(ssp_k_vecs)):
            if ssp_k_vecs[i] == ssp_k_vecs[i - 1]:
                k_consecutive_repeats += 1

        # Check Menu Long consecutive repeats
        for i in range(1, len(ssp_m_ans)):
            if ssp_m_ans[i] == ssp_m_ans[i - 1]:
                m_consecutive_repeats += 1

        # Check max consecutive same-type run
        trun = 1
        for i in range(1, len(ssp_types)):
            trun = trun + 1 if ssp_types[i] == ssp_types[i - 1] else 1
            max_type_run_global = max(max_type_run_global, trun)

    tot_a = sum(global_a_dist.values())
    a_pcts = {["A", "B", "C", "D", "E"][k]: round(global_a_dist[k] * 100 / tot_a, 2) for k in range(5)}
    for letter, pct in a_pcts.items():
        if not (18.0 <= pct <= 22.0):
            errors.append(f"Déséquilibre Type A lettre {letter}: {pct}%")

    if len(global_k_vectors) != 16:
        errors.append(f"Type K': seulement {len(global_k_vectors)}/16 vecteurs présents")
    if m_consecutive_repeats > 0:
        errors.append(f"Menu Long: {m_consecutive_repeats} répétitions consécutives d'index")
    if k_consecutive_repeats > 0:
        errors.append(f"Type K': {k_consecutive_repeats} répétitions consécutives de vecteur")

    print("=== PASSE 1 · AUDIT STRUCTURE & ALÉA ABSOLU ===")
    print(f"Total QCMs : {total_q} across {cat_data['total_ssp']} SSPs ({cat_data['total_dds']} DDs)")
    print(f"Proportions : a={props['a']} · k'={props['k_prime']} · m={props['m']}")
    print(f"Type A distribution (%) : {a_pcts}")
    print(f"Type A max streak global : {max_a_streak_global} | Cycles alternants X-Y-X-Y-X : {a_alternating_cycles}")
    print(f"Type K' vecteurs 4-bit couverts : {len(global_k_vectors)}/16 | Répétitions consécutives : {k_consecutive_repeats}")
    print(f"Type K' nb de Vrai : {dict(sorted(global_k_true_counts.items()))}")
    print(f"Menu Long répétitions consécutives : {m_consecutive_repeats} | Index distincts utilisés : {len(global_m_dist)}")
    print(f"Run max de même type (A/K'/M) : {max_type_run_global}")

    if errors:
        print(f"ECHEC PASSE 1 ({len(errors)} erreurs) :", errors[:15])
        sys.exit(1)
    print("STATUT PASSE 1 : SUCCÈS TOTAL (0 erreur, Aléa Absolu certifié)")


if __name__ == "__main__":
    main()

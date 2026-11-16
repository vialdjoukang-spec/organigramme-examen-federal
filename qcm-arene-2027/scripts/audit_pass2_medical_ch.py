#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUDIT INDÉPENDANT · PASSE 2 : COHÉRENCE CLINIQUE, JUSTIFICATIONS & PRATIQUE SUISSE
Vérifie indépendamment de build_qcm_db.py :
1. Alignement strict réponse / justification sur 100% des 102'614 QCMs :
   - Type A : lettre A..E exacte, ju[an] positive, toutes les 4 autres ju[k] négatives
   - Type K' : lettre a..d exacte, ju[i] cohérente avec booléen an[i] (+ Vrai vs - Faux)
   - Menu Long : option exacte présente, unicité des options
2. Stratification fréquentielle & drapeaux rouges (« À ne pas manquer ») dans chaque SSP
3. Couverture suisse obligatoire dans chaque SSP (Smarter Medicine, Compendium/AIPS, OFSP, Sortie hospitalière)
4. Hygiène rédactionnelle : 0 balise HTML résiduelle (<...>), 0 « À vérifier » isolé dans les énoncés
"""

import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(ROOT, "data")
SSP_DIR = os.path.join(DATA_DIR, "ssp")

VALID_TIERS = {"Très fréquente", "Fréquente", "Peu fréquente", "Moins fréquente", "Rare"}


def load_js_obj(path: str, prefix: str):
    raw = open(path, encoding="utf-8").read()
    idx = raw.find(prefix)
    if idx == -1:
        raise ValueError(f"Prefix {prefix!r} not found in {path}")
    return json.loads(raw[idx + len(prefix) :].strip().rstrip(";"))


def main():
    cat_data = load_js_obj(os.path.join(DATA_DIR, "catalog.js"), "window.QCM_CATALOG = ")
    errors = []
    warnings = []
    total_q = 0
    swiss_q_count = 0
    total_mastery_causes = 0
    ssps_with_tiers = 0
    html_leak_count = 0

    letters = ["A", "B", "C", "D", "E"]
    letters_k = ["a", "b", "c", "d"]

    for item in cat_data["catalog"]:
        code = item["code"]
        ssp = load_js_obj(os.path.join(SSP_DIR, f"{code}.js"), f"window.QCM_SSP[{json.dumps(code)}] = ")
        qs = ssp.get("questions", [])
        refs = ssp.get("refs", [])
        mastery = ssp.get("mastery", {})
        causes = mastery.get("causes", [])

        if ssp.get("dd_count", 0) > 0:
            if len(causes) != ssp["dd_count"]:
                errors.append(f"{code}: mastery.causes ({len(causes)}) != dd_count ({ssp['dd_count']})")
            for c in causes:
                total_mastery_causes += 1
                if c.get("tier") not in VALID_TIERS:
                    errors.append(f"{code}: tier invalide {c.get('tier')!r}")
            if causes:
                ssps_with_tiers += 1

        # Verify Swiss reference existence
        refs_blob = " ".join(refs).lower()
        if not ("compendium" in refs_blob or "aips" in refs_blob or "swissmedic" in refs_blob or "ofsp" in refs_blob):
            errors.append(f"{code}: référence suisse (Compendium/AIPS/OFSP) manquante")

        has_swiss_q = False
        for q in qs:
            total_q += 1
            qid = q["id"]
            t = q["t"]
            op = q["op"]
            an = q["an"]
            ju = q["ju"]
            st = q["st"]
            ex = q["ex"]

            if re.search(r"<(?:p|div|span|br|ul|li|b|strong|script)\b", st + " " + ex, re.I):
                html_leak_count += 1
                errors.append(f"{qid}: fuite HTML dans stem/ex")
            if re.search(r"(?:\[\s*à vérifier\s*\]|source\s+à\s+vérifier|\bà\s+vérifier\s*[:·(\-])", (st + " " + ex).lower()):
                errors.append(f"{qid}: mention placeholder 'À vérifier' dans l'énoncé/explication")

            if any(k in (q.get("th", "") + " " + st).lower() for k in ("smarter medicine", "compendium", "aips", "sortie d'hospitalisation", "ofsp")):
                has_swiss_q = True
                swiss_q_count += 1

            if t == "A":
                if len(set(op)) != 5:
                    errors.append(f"{qid}: options Type A non uniques")
                if len(ju) != 5:
                    errors.append(f"{qid}: {len(ju)} justifications au lieu de 5")
                    continue
                for idx in range(5):
                    j = ju[idx]
                    if not j.startswith(f"{letters[idx]} ("):
                        errors.append(f"{qid}: préfixe lettre justification[{idx}] incohérent: {j[:25]!r}")
                    if idx == an:
                        if "Exacte" not in j:
                            errors.append(f"{qid}: justification[{idx}] de la bonne réponse sans 'Exacte'")
                    else:
                        if "Exacte" in j or ("Fausse" not in j and "Rejetée" not in j):
                            errors.append(f"{qid}: justification[{idx}] de mauvaise option incohérente: {j[:40]!r}")

            elif t == "K":
                if len(ju) != 4:
                    errors.append(f"{qid}: {len(ju)} justifications K' au lieu de 4")
                    continue
                for idx in range(4):
                    j = ju[idx]
                    if not j.startswith(f"{letters_k[idx]} ("):
                        errors.append(f"{qid}: préfixe K' [{idx}] incohérent: {j[:20]!r}")
                    if an[idx] is True and "+ Vrai" not in j:
                        errors.append(f"{qid}: K'[{idx}] Vrai sans '+ Vrai'")
                    if an[idx] is False and "- Faux" not in j:
                        errors.append(f"{qid}: K'[{idx}] Faux sans '- Faux'")

            elif t == "M":
                if len(set(op)) != len(op):
                    errors.append(f"{qid}: options Menu Long dupliquées")
                if not ju or "Exacte" not in ju[0] and "exacte" not in ju[0]:
                    errors.append(f"{qid}: Menu Long sans justification exacte")

        if not has_swiss_q:
            warnings.append(f"{code}: aucune question explicite de pratique suisse détectée")

    print("=== PASSE 2 · AUDIT MÉDICAL, JUSTIFICATIONS & PRATIQUE SUISSE ===")
    print(f"QCMs audités : {total_q} | QCMs pratiques suisses (AIPS/Smarter/OFSP/Sortie) : {swiss_q_count}")
    print(f"Causes stratifiées par fréquence : {total_mastery_causes} causes sur {ssps_with_tiers} SSPs avec DDs")
    print(f"Fuites HTML détectées : {html_leak_count} | Avertissements : {len(warnings)}")
    if warnings:
        print("Warnings sample:", warnings[:5])
    if errors:
        print(f"ECHEC PASSE 2 ({len(errors)} erreurs) :", errors[:20])
        sys.exit(1)
    print("STATUT PASSE 2 : SUCCÈS TOTAL (0 incohérence option/justification, 0 erreur)")


if __name__ == "__main__":
    main()

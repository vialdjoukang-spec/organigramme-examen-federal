#!/usr/bin/env python3
"""Fusionne les audits médical et linguistique d'un lot puis produit sa liste Word.

Usage : fusion_audit.py N "Titre" CODE_SSP DOSSIER_AUDITS
Contrôle que chaque extrait cité existe bien dans le fichier visé (texte sans balises).
"""
import html, json, os, re, subprocess, sys

N, TITRE, SSP, AUD = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
HERE = os.path.dirname(os.path.abspath(__file__))
LOTDIR = os.path.dirname(HERE)
ORDER = {"Critique": 0, "Grave": 1, "Moyen": 2, "Léger": 3}


def norm(s):
    s = html.unescape(re.sub(r"<[^>]+>", " ", s))
    return re.sub(r"\s+", " ", s.replace(" ", " ").replace(" ", " ")).strip().lower()


texts = {}
for f in os.listdir(LOTDIR):
    if f.startswith(f"LOT_{N}_") and f.endswith(".html"):
        texts[f] = norm(open(os.path.join(LOTDIR, f), encoding="utf-8", errors="replace").read())

man = json.load(open(os.path.join(LOTDIR, f"LOT_{N}_MANIFESTE_CLONE.json"), encoding="utf-8"))
fichiers = [{"nom": m["localName"], "drive_id": m["fileId"], "taille": m["localSize"],
             "statut": "export Google Doc" if m["kind"] == "doc" else "HTML"} for m in man]

constats, rm, rl, syn, introuvables = [], [], [], [], []
for code, target in (("MEDICAL", rm), ("LINGUISTIQUE", rl)):
    d = json.load(open(os.path.join(AUD, f"LOT_{N}_{code}.json"), encoding="utf-8"))
    target.extend(d.get("rapport", []))
    syn.extend(d.get("synthese", []))
    for c in d["constats"]:
        f = c.get("fichier", "")
        ex = norm(c.get("extrait", ""))
        if ex and f in texts and ex not in texts[f]:
            introuvables.append(c["id"])
            c["emplacement"] += " (extrait à rechercher par mots-clés : citation non littérale)"
        constats.append(c)
constats.sort(key=lambda c: (ORDER.get(c["gravite"], 9), c["id"]))
a = {"lot": int(N), "titre": TITRE, "ssp": SSP, "date": "2026-10-22",
     "auditeur": "Claude — audits médical et linguistique indépendants",
     "fichiers": fichiers, "synthese": syn, "constats": constats,
     "rapport_medical": rm, "rapport_linguistique": rl}
out_json = os.path.join(AUD, f"LOT_{N}_AUDIT_FUSION.json")
json.dump(a, open(out_json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
docx = os.path.join(LOTDIR, f"LOT_{N}_Liste_Corrections_Audit.docx")
subprocess.run([sys.executable, os.path.join(HERE, "gen_checklist_docx.py"), out_json, docx], check=True,
               stdout=subprocess.DEVNULL)
cnt = {g: sum(c["gravite"] == g for c in constats) for g in ORDER}
print(json.dumps({"lot": N, "docx": docx, "taille": os.path.getsize(docx), "constats": cnt,
                  "extraits_non_litteraux": introuvables}, ensure_ascii=False))

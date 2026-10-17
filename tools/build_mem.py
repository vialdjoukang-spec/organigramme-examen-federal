#!/usr/bin/env python3
"""Mnémosyne · construit data/MEM.json mot pour mot à partir de research_memorisation.md.
Usage : python3 tools/build_mem.py <research_memorisation.md> [data/MEM.json]"""
import re, json, sys
t = open(sys.argv[1], encoding='utf-8').read()
dest = sys.argv[2] if len(sys.argv) > 2 else 'data/MEM.json'
secs = re.split(r'\n## (\d+)\. ', t.split('## Tableau de synthèse')[0])[1:]
IDS = ["recuperation", "rappel-libre", "pratique-espacee", "reapprentissage", "cartes-anki", "entrelacement",
       "auto-explication", "interrogation-elaborative", "reflexion-structuree", "double-codage", "enseigner", "faible-utilite"]
def bloc(body, label):
    m = re.search(r'\*\*' + re.escape(label) + r'([^*]*)\*\*(.*?)(?=\n\n\*\*|\Z)', body, re.S)
    return (m.group(1).strip(' .:'), m.group(2).strip()) if m else None
full = {}
for line in t.split('## Références complètes')[1].split('## Sources')[0].splitlines():
    m = re.match(r'\d+\. (.*) https://doi.org/(\S+)$', line.strip())
    if m: full[m.group(2)] = m.group(1).strip()
syn = []
for line in t.split('## Tableau de synthèse')[1].split('## Références')[0].splitlines()[3:]:
    if line.startswith('|'): syn.append([x.strip() for x in line.strip('|').split('|')])
out = []
for i in range(0, len(secs), 2):
    n = int(secs[i]); head, _, body = secs[i + 1].partition('\n')
    body = body.split("\n---")[0]
    m = {"id": IDS[n - 1], "n": n, "nom": head.strip(), "texte": bloc(body, "Texte à coller")[1]}
    g = bloc(body, "Preuves générales"); m["preuves_generales"] = g[1] if g else None
    c = bloc(body, "Conséquence pour l’application")
    if c: m["consequence_application"] = c[1]
    pm = bloc(body, "Preuves en médecine")
    if pm:
        statut, texte = pm
        if texte.startswith("dans cette"): texte = f"{statut[0].upper()}{statut[1:]} {texte}"
        m["preuves_medecine"] = {"statut": statut, "texte": texte}
    else:
        m["preuves_medecine"] = None  # la note de recherche ne donne pas ce bloc
    refs = bloc(body, "Références")[1].split(" · ")
    m["references"] = [{"cite": r.split(", doi:")[0].strip(), "doi": r.split("doi:")[1].strip(),
                        "url": "https://doi.org/" + r.split("doi:")[1].strip(), "complete": full.get(r.split("doi:")[1].strip())} for r in refs]
    s = syn[n - 1]; m["synthese"] = {"ligne": s[0], "preuve_generale": s[1], "preuve_medecine": s[2]}
    out.append(m)
doc = {"_source": "research_memorisation.md du 17.10.2026, repris mot pour mot ; références M1 à M24 vérifiées dans Crossref.",
       "_lecture": t.split('## Comment lire ces notes')[1].split('---')[0].strip(),
       "references": [{"m": f"M{i + 1}", "doi": d, "url": "https://doi.org/" + d, "complete": c} for i, (d, c) in enumerate(full.items())],
       "methodes": out}
assert len(out) == 12 and len(full) == 24 and all(r["complete"] for x in out for r in x["references"])
json.dump(doc, open(dest, 'w', encoding='utf-8'), ensure_ascii=False, indent=1); open(dest, 'a').write('\n')
for x in out: print(x["n"], x["id"], "|", (x["preuves_medecine"] or {}).get("statut"), "|", len(x["references"]))

#!/usr/bin/env python3
"""Régénère LOT_Claude_Finaux/PROGRESSION.html : file active (10 LOTS) depuis ETAT_FILE.json + CATALOGUE_248.csv."""
import csv, html, json, sys
D = "LOT_Claude_Finaux/"
debut = int(sys.argv[1]) if len(sys.argv) > 1 else 1
cat = {r["lot"]: r for r in csv.DictReader(open(D + "CATALOGUE_248.csv", encoding="utf-8"))}
et = {l["lot"]: l for l in json.load(open(D + "ETAT_FILE.json"))["lots"]}
sc = lambda v: "—" if v is None else f"{v} %"
rows = ""
for n in range(debut, debut + 10):
    k, e = f"{n:03d}", et[f"{n:03d}"]
    rows += (f"<tr><td>{k}</td><td>{html.escape(cat[k]['ssp_profiles_2023_fr_en'])}</td>"
             f"<td>{(e['etat_source'] or '—').replace('_', ' ')}</td><td>{sc(e['score_A'])}</td>"
             f"<td>{sc(e['score_B'])}</td><td>{e['verdict'] or e['statut_audit']}</td></tr>\n")
open(D + "PROGRESSION.html", "w", encoding="utf-8").write(f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><title>Progression — LOT_Claude_Finaux</title>
<style>body{{font:14px system-ui;margin:2rem}}table{{border-collapse:collapse;width:100%}}td,th{{border:1px solid #ccc;padding:.3rem .5rem;text-align:left}}</style></head><body>
<h1>Catalogue = 248 SSP (PROFILES 2023)</h1>
<p>File active : LOT_{debut:03d} → LOT_{debut+9:03d}. Scores inconnus = « — ».</p>
<table><tr><th>LOT</th><th>SSP</th><th>État</th><th>Phase A</th><th>Phase B</th><th>Verdict</th></tr>
{rows}</table></body></html>
""")

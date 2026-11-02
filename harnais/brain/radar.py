#!/usr/bin/env python3
"""Radar gratuit (Vial, 28.10.2026) : un coup d'œil sur tout le circuit, sans appel de modèle.
  python3 harnais/brain/radar.py [--json]
Affiche : redémarrage du conteneur, circuits vivants, avancement par LOT (leçons finies, fragments rendus, refus notifiés),
bande Ko, porte médicale (AIPS présent), disque, état git. Code 2 si un circuit est mort sans bilan (à relancer avec --reprendre)."""
import json, shutil, subprocess, sys, time
from pathlib import Path
R = Path(__file__).resolve().parents[2]
sh = lambda c: subprocess.run(c, shell=True, capture_output=True, text=True, cwd=R).stdout.strip()
def lots():
    out = []
    for d in sorted(R.glob("essai_lot*")):
        j = d / "journal"; html = sorted(d.glob("*.html"))
        fait = list(j.glob("*.fait.json")) if j.exists() else []
        notif = j / "notifications.md"
        ko = [round(f.stat().st_size / 1000) for f in html]
        out.append(dict(lot=d.name, lecons=len(html), finies=len(fait), bilan=(j / "bilan.json").exists(),
                        refus=len(notif.read_text().splitlines()) if notif.exists() else 0,
                        ko_min=min(ko, default=0), ko_max=max(ko, default=0), hors_bande=sum(1 for k in ko if k > 150 or k < 80)))
    return out
def main(a):
    vivants = [l for l in sh("ps -eo args").splitlines() if "lancer_parallele" in l or "lancer_circuit" in l]
    vivants = [l for l in vivants if "grep" not in l and "bash -c" not in l]
    e = dict(heure=time.strftime("%H:%M:%S"), demarrage_conteneur=sh("uptime -s"), circuits_vivants=len(vivants),
             aips="OK" if (R / ".cache/aips/AipsDownload_20261008.xml").exists() else "MANQUANT", disque_libre_go=round(shutil.disk_usage(R).free / 1e9, 1),
             git_non_suivis=len(sh("git status --short").splitlines()), lots=lots())
    mort = [l["lot"] for l in e["lots"] if l["lecons"] and not l["bilan"] and l["finies"] < l["lecons"] and not vivants]
    e["a_relancer"] = mort
    if "--json" in a: print(json.dumps(e, ensure_ascii=False, indent=1))
    else:
        print(f"{e['heure']} · conteneur démarré {e['demarrage_conteneur']} · circuits vivants {e['circuits_vivants']} · AIPS {e['aips']} · disque {e['disque_libre_go']} Go · non suivis {e['git_non_suivis']}")
        for l in e["lots"]: print(f"  {l['lot']} : {l['finies']}/{l['lecons']} leçons finies · bilan {'oui' if l['bilan'] else 'non'} · refus notifiés {l['refus']} · Ko {l['ko_min']}–{l['ko_max']} · hors bande {l['hors_bande']}")
        if mort: print("  ⚠ circuit mort sans bilan :", ", ".join(mort), "→ relancer avec --reprendre")
    return 2 if mort else 0
if __name__ == "__main__": sys.exit(main(sys.argv[1:]))

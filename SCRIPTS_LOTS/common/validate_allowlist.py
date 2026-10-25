#!/usr/bin/env python3
"""Valide la liste des domaines agréés : chaque domaine est vérifié par curl (HTTPS, redirections suivies).
Produit allowlist.json. Aucune IA ; résultat entièrement déterministe et horodaté."""
import json, subprocess, sys, datetime, re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlparse

ICI = Path(__file__).resolve().parent
UA = "scripts_lots/1.3 (+projet organigramme-examen-federal; validation des domaines)"

DEFIS = ("just a moment", "one moment, please", "checking your browser", "access denied", "request not authorized")

def verifier(niveau, domaine, organisme, sonde="/"):
    cmd = ["curl", "-s", "-L", "-m", "20", "-A", UA, "-H", "Accept: " + ("text/html" if sonde == "/" else "application/json, */*"),
           "-o", "-", "-w", "\n%{http_code} %{url_effective}", f"https://{domaine}{sonde}"]
    try:
        out = subprocess.run(cmd, capture_output=True, timeout=30).stdout.decode("utf-8", "replace")
    except Exception as e:
        out = f"\n000 erreur:{e}"
    corps, _, fin = out.rpartition("\n")
    code, _, finale = fin.partition(" ")
    m = re.search(r"<title[^>]*>(.*?)</title>", corps, re.S | re.I)
    titre = re.sub(r"\s+", " ", m.group(1)).strip()[:120] if m else ""
    hote_final = urlparse(finale).hostname or ""
    rejet_attendu = organisme.startswith("REJET")
    if rejet_attendu:
        statut = "rejete"
    elif code == "200" and any(d in titre.lower() for d in DEFIS):
        statut = "joignable_bloque_robots"
    elif code == "200":
        statut = "valide"
    elif code in ("401", "403", "412", "415", "429"):
        statut = "joignable_bloque_robots"
    else:
        statut = "injoignable"
    return {"niveau": int(niveau), "domaine": domaine, "organisme": organisme, "http": code,
            "url_finale": finale, "hote_final": hote_final, "titre": titre, "statut": statut,
            "auto_fetch": statut == "valide"}

def main():
    cand = json.loads((ICI / "allowlist_candidates.json").read_text("utf-8"))
    taches = [(n, *x) for n, l in cand.items() for x in l]
    with ThreadPoolExecutor(16) as ex:
        res = list(ex.map(lambda t: verifier(*t), taches))
    res.sort(key=lambda r: (r["niveau"], r["domaine"]))
    doc = {"valide_le": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
           "methode": "curl -L https://<domaine><sonde> ; 200 sans page de défi anti-robot = valide ; 401/403/412/415/429 = joignable mais bloque l'accès automatisé (usage manuel seulement)",
           "domaines": res}
    (ICI / "allowlist.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1), "utf-8")
    for r in res:
        print(f'{r["niveau"]} {r["statut"]:<24} {r["http"]} {r["domaine"]:<28} -> {r["hote_final"]} | {r["titre"][:60]}')
    return 0

if __name__ == "__main__":
    sys.exit(main())

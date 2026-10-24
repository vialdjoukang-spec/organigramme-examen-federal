#!/usr/bin/env python3
"""Génère agent_1 … agent_8 (config.json + enveloppes minces) pour l'organisation à 8 agents / 2 équipes (v1.4).
Déterministe, bibliothèque standard. Relancer après toute modification de ORGANISATION ou des débits.

Loi d'indépendance absolue : chaque agent a ses propres cache, retours, compteur ET état des seaux
(~/.scripts_lots/agent_N/etat) ; le dossier ~/.scripts_lots/partage n'est plus utilisé par aucune configuration.

Partage des budgets externes (les 8 agents ensemble restent sous les anciennes limites globales) :
  LanguageTool : 10 req/min et 60 000 o/min au total  → 10 // 8 = 1 req/min et 60 000 // 8 = 7 500 o/min par agent
                 (8 req/min au total) ; requête ≤ 6 000 o (capacité 7 200 o, rafale cumulée 57,6 Ko ≤ 60 Ko) ; 1 requête par passage.
  NCBI E-utilities : 3 req/s sans clé → 0,375 req/s par agent ; 10 req/s avec clé → 1,25 req/s par agent (capacité 1 jeton).
  Par domaine : 1 req/s → 0,125 req/s par agent et par domaine (une requête toutes les 8 s ; capacité 1 jeton).
"""
import json
from pathlib import Path

ICI = Path(__file__).resolve().parent
NB_AGENTS = 8
TOUT = ["A", "P1", "P2", "P3", "P4"]
CHAPITRES = {"A+P1": ("Appel A + Partie 1 (DX.1–DX.2)", ["A", "P1"]),
             "P2": ("Partie 2 (DX.3–DX.5)", ["P2"]),
             "P3": ("Partie 3 (DX.6–DX.7)", ["P3"]),
             "P4": ("Partie 4 (DX.8–DX.10)", ["P4"])}
# agent: (équipe, chapitre, premier LOT, dernier LOT, LOT entiers déjà rédigés seul, dossiers de travail)
ORGANISATION = {
    1: (1, "A+P1", 227, 237, [227, 228], ["/workspace/agent1"]),
    3: (1, "P2", 229, 237, [], ["/workspace/agent3"]),
    5: (1, "P3", 229, 237, [], ["/workspace/agent5"]),
    7: (1, "P4", 229, 237, [], ["/workspace/agent7"]),
    2: (2, "A+P1", 238, 248, [238, 239], ["/workspace/agent2", "/workspace/lots"]),
    4: (2, "P2", 240, 248, [], ["/workspace/agent4"]),
    6: (2, "P3", 240, 248, [], ["/workspace/agent6"]),
    8: (2, "P4", 240, 248, [], ["/workspace/agent8"]),
}
LT = {"budget_req_per_min": 10 // NB_AGENTS, "budget_bytes_per_min": 60000 // NB_AGENTS,
      "max_bytes_per_request": 6000, "max_requests_per_pass": 1}
PUBMED = {"rate_per_s_without_key": 3 / NB_AGENTS, "rate_per_s_with_key": 10 / NB_AGENTS, "mcp_url": ""}
HTTP = {"per_domain_per_s": 1.0 / NB_AGENTS}

ENVELOPPE = '''#!/usr/bin/env python3
"""Agent {n} — {titre} — point d'entrée mince vers common/{mod}.py avec la configuration de CET agent uniquement."""
import sys
from pathlib import Path
ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent / "common"))
import {mod}
sys.exit({mod}.main(ICI / "config.json", sys.argv[1:]))
'''

def config(n):
    eq, ch, a, b, entiers, dossiers = ORGANISATION[n]
    libelle, parties = CHAPITRES[ch]
    pa = {**{str(x): TOUT for x in entiers}, "*": parties} if entiers else parties
    r = f"~/.scripts_lots/agent_{n}"
    return {
        "_commentaire": (f"Agent {n} — équipe {eq} — {libelle} — LOT_{a}–{b}"
                         + (f" (LOT_{', LOT_'.join(map(str, entiers))} rédigés entiers)" if entiers else "")
                         + ". Indépendance absolue : tous les chemins inscriptibles, y compris l'état des seaux, sont propres à cet agent."),
        "agent": n, "equipe": eq, "chapitre": libelle,
        "lot_min": a, "lot_max": b, "lots": list(range(a, b + 1)),
        "parties_autorisees": pa, "dossier_travail": dossiers if len(dossiers) > 1 else dossiers[0],
        "lots_root": None,
        "cache_dir": f"{r}/cache", "output_dir": f"{r}/retours", "shared_state_dir": f"{r}/etat",
        "prompt_path": "/workspace/v7_tunder/PROMPT_ULTIME_PRODUCTION_LOTS_V7-Tunder.md",
        "enforce_os_readonly": False,
        "languagetool": dict(LT), "pubmed": dict(PUBMED), "http": dict(HTTP),
        "compteur": {"csv": f"{r}/COMPTEUR_TOKENS_AGENT_{n}.csv"},
    }

def main():
    for n in sorted(ORGANISATION):
        d = ICI / f"agent_{n}"; d.mkdir(exist_ok=True)
        eq, ch, a, b, _, _ = ORGANISATION[n]
        titre = f"équipe {eq}, {CHAPITRES[ch][0]}, LOT_{a}–{b}"
        (d / "config.json").write_text(json.dumps(config(n), ensure_ascii=False, indent=1) + "\n", "utf-8")
        for f, mod in (("script_source.py", "source_engine"), ("script_synchrone.py", "sync_reviewer")):
            (d / f).write_text(ENVELOPPE.format(n=n, titre=titre, mod=mod), "utf-8"); (d / f).chmod(0o755)
        print(f"agent_{n} : {titre}")

if __name__ == "__main__":
    main()

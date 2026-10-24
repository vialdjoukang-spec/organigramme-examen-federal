#!/usr/bin/env python3
"""COMPTEUR DE JETONS — mesure l'économie due à la règle de protection des jetons (règle n° 1). Aucune IA.

  log    --config C --lot LOT_X --cas 1|2|3 --message "…"   journalise un message AUTORISÉ à l'utilisateur (≤ 15 mots, une ligne)
  tunder --config C --lot LOT_X --resume "…"               journalise une information routée vers Tunder au lieu de l'utilisateur
  rapport --config C [--config C2] [--format md|json]       synthèse Markdown pour Tunder

Mesuré : messages réellement envoyés (cas 1 LOT terminé, 2 série terminée, 3 urgence ou difficulté) et informations routées vers Tunder.
ESTIMÉ (jamais présenté comme mesuré) : messages qu'un agent aurait envoyés sans la règle, selon un scénario de référence
configurable, car les agents n'ont aucun historique antérieur. Jetons ≈ ceil(caractères / car_par_jeton)."""
import argparse, csv, datetime, json, math, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import config as cfgmod

SCENARIO_DEFAUT = {
    "_nature": "ESTIMATION — scénario de référence sans règle n° 1 ; aucune donnée historique n'existe",
    "messages_par_lot": {"debut_lot": 1, "recherche_sources": 6, "appel_a_termine": 1, "parties_terminees": 4,
                          "corrections_annoncees": 4, "questions_a_l_utilisateur": 2, "resume_fin_lot": 1},
    "messages_fin_serie": 2,
    "caracteres_par_message_type": 480,
    "car_par_jeton": 4,
    "cout_relecture_contexte_par_message": 120,
}
CAS = {"1": "LOT terminé", "2": "série terminée", "3": "urgence ou difficulté", "T": "routé vers Tunder"}
ENTETE = ["horodatage", "agent", "lot", "cas", "mots", "caracteres", "jetons_estimes", "message"]

def jetons(txt, cpj):
    return math.ceil(len(txt) / cpj) if txt else 0

def scenario(cfg):
    s = json.loads(json.dumps(SCENARIO_DEFAUT)); s.update({k: v for k, v in cfg.get("compteur", {}).items() if k in s and k != "messages_par_lot"})
    s["messages_par_lot"].update(cfg.get("compteur", {}).get("messages_par_lot", {}))
    return s

def chemin_csv(cfg):
    return Path(cfg.get("compteur", {}).get("csv") or Path(cfg["cache_dir"]).parent / f"COMPTEUR_TOKENS_AGENT_{cfg['agent']}.csv").expanduser()

def ajouter(cfg, lot, cas, message):
    message = message.strip()
    if cas in "123":
        if "\n" in message or len(message.split()) > 15:
            raise ValueError("règle n° 1 : une seule ligne de 15 mots au maximum")
    elif cas != "T":
        raise ValueError("cas autorisés : 1, 2, 3 (utilisateur) ou T (Tunder)")
    num = int(lot.replace("LOT_", "")) if lot not in ("", "-") else None
    if num is not None and not cfgmod.lot_autorise(cfg, num):
        raise ValueError(f"{lot} hors de la série de l'agent {cfg['agent']}")
    p = chemin_csv(cfg); p.parent.mkdir(parents=True, exist_ok=True); neuf = not p.exists()
    with open(p, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if neuf: w.writerow(ENTETE)
        w.writerow([datetime.datetime.now().astimezone().isoformat(timespec="seconds"), cfg["agent"], lot, cas,
                    len(message.split()), len(message), jetons(message, scenario(cfg)["car_par_jeton"]), message])
    return p

def calculer(cfg):
    s = scenario(cfg); p = chemin_csv(cfg)
    lignes = []
    if p.exists():
        with open(p, encoding="utf-8") as f: lignes = list(csv.DictReader(f))
    envoyes = [l for l in lignes if l["cas"] in ("1", "2", "3")]; tunder = [l for l in lignes if l["cas"] == "T"]
    lots_finis = sorted({l["lot"] for l in envoyes if l["cas"] == "1"})
    serie_finie = any(l["cas"] == "2" for l in envoyes)
    par_lot = sum(s["messages_par_lot"].values())
    base_msgs = len(lots_finis) * par_lot + (s["messages_fin_serie"] if serie_finie else 0)
    jetons_type = jetons("x" * s["caracteres_par_message_type"], s["car_par_jeton"])
    cout_msg = jetons_type + s["cout_relecture_contexte_par_message"]
    reels = len(envoyes); jetons_reels = sum(int(l["jetons_estimes"]) for l in envoyes)
    economie = max(0, base_msgs - reels) * cout_msg
    return {"agent": cfg["agent"], "serie": f"LOT_{cfg['lot_min']}–{cfg['lot_max']}", "csv": str(p),
            "mesure": {"messages_envoyes": reels, "par_cas": {c: sum(1 for l in envoyes if l["cas"] == c) for c in "123"},
                       "jetons_messages_envoyes_estimes": jetons_reels, "informations_routees_vers_tunder": len(tunder), "lots_termines": len(lots_finis)},
            "estimation": {"nature": s["_nature"], "messages_par_lot_sans_regle": par_lot, "detail_par_lot": s["messages_par_lot"],
                           "messages_sans_regle": base_msgs, "jetons_par_message_type": jetons_type,
                           "cout_relecture_contexte": s["cout_relecture_contexte_par_message"], "cout_par_message_evite": cout_msg,
                           "messages_evites": max(0, base_msgs - reels), "jetons_economises": economie,
                           "formule": "(messages_sans_regle − messages_envoyes) × (ceil(caracteres_par_message_type / car_par_jeton) + cout_relecture_contexte)"}}

def rendu(rs):
    l = ["# Compteur de jetons — règle n° 1 (protection des jetons)", "",
         "> Les colonnes « mesuré » proviennent des journaux CSV. Les colonnes « ESTIMATION » proviennent d'un scénario de référence configurable : aucun historique n'existe, rien n'y est mesuré.", "",
         "| Agent | Série | LOT terminés (mesuré) | Messages envoyés (mesuré) | Routés vers Tunder (mesuré) | Messages sans règle (ESTIMATION) | Messages évités (ESTIMATION) | Jetons économisés (ESTIMATION) |",
         "|---|---|---|---|---|---|---|---|"]
    for r in rs:
        m, e = r["mesure"], r["estimation"]
        l.append(f"| {r['agent']} | {r['serie']} | {m['lots_termines']} | {m['messages_envoyes']} (cas 1 : {m['par_cas']['1']}, 2 : {m['par_cas']['2']}, 3 : {m['par_cas']['3']}) | {m['informations_routees_vers_tunder']} | {e['messages_sans_regle']} | {e['messages_evites']} | ≈ {e['jetons_economises']} |")
    e = rs[0]["estimation"]
    l += ["", "Hypothèses du scénario (modifiables dans `config.json`, clé `compteur`) :",
          f"- messages par LOT sans la règle : {e['messages_par_lot_sans_regle']} ({', '.join(f'{k} {v}' for k, v in e['detail_par_lot'].items())}) ;",
          f"- message type ≈ {e['jetons_par_message_type']} jetons ; coût de relecture du contexte ≈ {e['cout_relecture_contexte']} jetons par message ;",
          f"- formule : {e['formule']}."]
    return "\n".join(l) + "\n"

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    a1 = sp.add_parser("log"); a1.add_argument("--config", required=True); a1.add_argument("--lot", required=True); a1.add_argument("--cas", required=True, choices=["1", "2", "3"]); a1.add_argument("--message", required=True)
    a2 = sp.add_parser("tunder"); a2.add_argument("--config", required=True); a2.add_argument("--lot", required=True); a2.add_argument("--resume", required=True)
    a3 = sp.add_parser("rapport"); a3.add_argument("--config", action="append", required=True); a3.add_argument("--format", default="md")
    a = ap.parse_args(argv)
    try:
        if a.cmd == "log":
            print(ajouter(cfgmod.charger(a.config), a.lot, a.cas, a.message)); return 0
        if a.cmd == "tunder":
            print(ajouter(cfgmod.charger(a.config), a.lot, "T", a.resume)); return 0
        rs = [calculer(cfgmod.charger(c)) for c in a.config]
        print(json.dumps(rs, ensure_ascii=False, indent=1) if a.format == "json" else rendu(rs)); return 0
    except ValueError as e:
        print(f"REFUS : {e}", file=sys.stderr); return 2

if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Scriptone S16 · économie de jetons par étage (mesure, plafonds). Région ECO.
Estimation constante : 4 caractères par jeton (texte français UTF-8) ; elle sert aux comparaisons avant/après, pas à la facturation.
  W1 paquet d'un point au-dessus du plafond d'un nœud (6 000 jetons) : à découper avant transmission
  W2 relecture intégrale au-dessus de 60 000 jetons (fichier trop lourd pour une boucle de correction)
  W3 fichier au-dessus de 200 Ko (bande indicative de Vial : avertissement, jamais bloquant)
Mesures : relecture intégrale, texte du cours, paquets par point, doléances [agent] compactes (si fournies), gain de la boucle."""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bus

ID, REGION, VERSION = "s16_economie", "ECO", "1.0.0"
PLAFOND_PAQUET, PLAFOND_FICHIER, BANDE_KO = 6000, 60000, 200


def mesures(t, doleances=None):
    a, f = bus.bornes_cours(t); S = bus.sections(t)
    paq = {n: bus.estime_jetons(bus.texte(bus.masque(t[x:y], bus.RX_STYLE))) for n, (x, y) in S.items()}
    M = dict(jetons_relecture_integrale=bus.estime_jetons(t), jetons_texte_cours=bus.estime_jetons(bus.texte_visible(t[a:f])), jetons_paquets=paq,
             octets=len(t.encode("utf-8", "surrogatepass")))
    if doleances is not None:
        ag = [d for d in doleances if d["executant"] == "agent"]
        compact = "\n".join(f"- {d['severite']} {d['code']} {d['ancre']} : {d['constat']} → {d['correction_prescrite']}" for d in ag)
        pts = sorted({int(m.group(1)) for d in ag for m in [re.search(r"point (\d{1,2})", d["constat"])] if m})
        M.update(jetons_doleances=bus.estime_jetons(compact), jetons_paquets_concernes=sum(paq.get(n, 0) for n in pts),
                 gain_boucle_pct=round(100 * (1 - (bus.estime_jetons(compact) + sum(paq.get(n, 0) for n in pts)) / max(1, M["jetons_relecture_integrale"])), 1))
    return M


def analyser(t, nom, opt=None):
    opt = opt or {}; me = sys.modules[__name__]; D = []; M = mesures(t, opt.get("doleances"))
    for n, j in sorted(M["jetons_paquets"].items()):
        if j > PLAFOND_PAQUET:
            D.append(bus.doleance(me, "W1", nom, bus.ancre(t, bus.sections(t)[n][0], f"{n}."), "MOYEN", f"paquet du point {n} : {j} jetons (plafond d'un nœud {PLAFOND_PAQUET})",
                                  f"transmettre le point {n} en sous-paquets (sous-titres) ; ne jamais le résumer", "agent", f"{j} jetons"))
    if M["jetons_relecture_integrale"] > PLAFOND_FICHIER:
        D.append(bus.doleance(me, "W2", nom, "#haut", "MOYEN", f"relecture intégrale : {M['jetons_relecture_integrale']} jetons (plafond {PLAFOND_FICHIER})",
                              "ne jamais relire le fichier entier : passer par les paquets du collecteur et les doléances", "agent"))
    if M["octets"] > BANDE_KO * 1000:
        D.append(bus.doleance(me, "W3", nom, "#haut", "DETAIL", f"fichier de {M['octets'] // 1000} Ko (bande indicative 80–200 Ko, non bloquante)",
                              "vérifier l'absence de redites et d'habillage dupliqué ; ne rien retrancher d'utile", "agent"))
    return D, M


def _gonfle(t, n, k):
    S = bus.sections(t); a, f = S[n]; i = t.rindex("</p>", a, f)
    return t[:i] + (" Le patient reste sous surveillance continue jusqu'à la stabilisation de son état clinique." * k) + t[i:]
MUTANTS = [("paquet trop lourd", lambda t, r: _gonfle(t, r.choice([3, 9, 11]), r.randint(300, 400)), "W1"),
           ("fichier trop lourd", lambda t, r: _gonfle(t, 12, r.randint(2700, 3000)), "W2"),
           ("fichier hors bande", lambda t, r: t.replace("</main>", "<!--" + "x" * r.randint(200000, 220000) + "--></main>", 1), "W3")]
ECRIT = []
COUT_MUTATION = 10

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))

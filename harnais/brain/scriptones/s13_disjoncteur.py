#!/usr/bin/env python3
"""Scriptone S13 · disjoncteurs, ré-routage, repli et escalade (auto-adaptation en cas de panne). Région SEC.
Fait passer les 140 synapses α et β du fichier par leurs disjoncteurs (reseau.Disjoncteur) et rend compte de chaque panne :
  Z1 panne d'une synapse (exception, contrat rompu, altération) : disjoncteur ouvert, exigence couverte par son jumeau (autre zone, autre méthode)
  Z2 panne sans jumeau valide : escalade au nœud auditeur du point, le fichier ne sort pas sans relecture humaine de la zone
  Z3 stagnation : mêmes doléances (mêmes id) deux passages de suite → fichier BLOQUÉ, retour au chef de production
  Z4 lenteur : budget de temps dépassé, disjoncteur ouvert pour les fichiers suivants (résultat courant conservé)
Options (tests et pannes injectées) : pannes {id: exception|contrat|lenteur}, historique [[id…], [id…]] (passages précédents)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bus, reseau

ID, REGION, VERSION = "s13_disjoncteur", "SEC", "1.0.0"
DEPEND = ["reseau.py", "registre.json"]
NOEUDS_SONNET = {1: "S1", 2: "S1", 3: "S1", 4: "S2", 5: "S2", 6: "S2", 7: "S3", 8: "S3", 9: "S3", 10: "S4", 11: "S4", 12: "S5", 13: "S5", 14: "S5"}


def synapses():
    return [e["id"] for e in reseau.registre()["scriptones"] if e["zone"] in ("alpha", "beta")]


def analyser(t, nom, opt=None):
    opt = opt or {}; me = sys.modules[__name__]; D = []; dj = reseau.Disjoncteur(budget_ms=opt.get("budget_ms", 4000))
    pannes = opt.get("pannes") or {}; ids = opt.get("ids") or synapses(); couverts = 0; vus = set()
    for i in ids:
        s, eff, nature = reseau.executer_protege(i, t, nom, dj, pannes)
        if s:
            for d in s["doleances"]: vus.add(d["id"])
        if nature is None: continue
        e = reseau.entree(i); n = e.get("point")
        if nature == "lenteur":
            D.append(bus.doleance(me, "Z4", nom, f"#haut · {i}", "MOYEN", f"{i} : budget de temps dépassé ; disjoncteur ouvert pour les fichiers suivants",
                                  f"profiler {i} ; en attendant, son jumeau {reseau.jumeau(i) or '—'} couvre l'exigence", "agent", nature)); continue
        if eff:
            couverts += 1
            D.append(bus.doleance(me, "Z1", nom, f"#haut · {i}", "GRAVE", f"panne de {i} ({nature}) : disjoncteur ouvert, exigence couverte par {eff}",
                                  f"réparer {i} (gardien : empreinte, contrat) ; le nœud {NOEUDS_SONNET.get(n, 'Opus')} relit le point {n or '—'} pour cette famille", "agent", nature))
        else:
            D.append(bus.doleance(me, "Z2", nom, f"#haut · {i}", "CRITIQUE", f"panne de {i} ({nature}) sans jumeau valide : exigence non couverte",
                                  f"escalade : le nœud Opus du domaine relit la zone de {i} ; le fichier ne sort pas avant", "agent", nature))
    H = opt.get("historique") or []
    if len(H) >= 2 and H[-1] and set(H[-1]) == set(H[-2]):
        D.append(bus.doleance(me, "Z3", nom, "#haut · passages", "GRAVE", f"stagnation : les {len(H[-1])} mêmes doléances deux passages de suite",
                              "fichier BLOQUÉ : retour au chef de production (aucune relance en boucle d'un agent)", "agent", ",".join(sorted(H[-1]))[:300]))
    return D, dict(synapses=len(ids), pannes=len(dj.journal), reroutees=couverts, ouverts=sorted(dj.ouverts), doleances_vues=len(vus))


def _ids(): return synapses()
def _m_exc(t, r): i = r.choice(_ids()); return t, {"pannes": {i: "exception"}, "ids": [i]}
def _m_contrat(t, r): i = r.choice(_ids()); return t, {"pannes": {i: "contrat"}, "ids": [i]}
def _m_sans(t, r):
    i = r.choice(_ids()); j = reseau.jumeau(i); return t, {"pannes": {i: "exception", j: "exception"}, "ids": [j, i]}
def _m_lent(t, r): i = r.choice(_ids()); return t, {"pannes": {i: "lenteur"}, "ids": [i]}
def _m_stag(t, r): h = [f"{r.getrandbits(48):012x}" for _ in range(r.randint(1, 5))]; return t, {"historique": [h, list(reversed(h))], "ids": []}
MUTANTS = [("panne (exception)", _m_exc, "Z1"), ("contrat rompu", _m_contrat, "Z1"), ("panne sans jumeau", _m_sans, "Z2"), ("lenteur", _m_lent, "Z4"), ("stagnation", _m_stag, "Z3")]
ECRIT = []
COUT_MUTATION = 8

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))

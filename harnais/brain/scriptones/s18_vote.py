#!/usr/bin/env python3
"""Scriptone S18 · nœud de vote α/β (comparateur) : routage des désaccords vers les auditeurs. Région BUS.
Pour chaque point n, verdict α (zone α : forme et concision) et verdict β (zone β : fond et exhaustivité) ; KO = au moins une doléance GRAVE ou CRITIQUE.
  X1 β KO, α OK : β rattrape ce qu'α n'a pas vu → nœud Opus du domaine (5 nœuds O1–O5, routés par type de signal)
  X2 α KO, β OK : correction de forme seulement → nœud Sonnet du territoire (5 nœuds S1–S5) ; β confirme le fond
Les accords (OK/OK, KO/KO) ne produisent rien : le bus porte déjà les doléances. Mesures : verdicts et table de routage."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bus, familles as F

ID, REGION, VERSION = "s18_vote", "BUS", "1.0.0"
DEPEND = ["familles.py", "synapses.json"]
SONNET = {1: "S1", 2: "S1", 3: "S1", 4: "S2", 5: "S2", 6: "S2", 7: "S3", 8: "S3", 9: "S3", 10: "S4", 11: "S4", 12: "S5", 13: "S5", 14: "S5"}
OPUS = {"medical": "O1 fond médical (doses, critères, conduite)", "doleance": "O2 sources et épidémiologie", "langue": "O4 langue et concision", "forme": "O5 forme et pédagogie"}
OPUS_POINT = {2: "O2 sources et épidémiologie", 12: "O2 sources et épidémiologie", 3: "O1 fond médical (doses, critères, conduite)", 8: "O1 fond médical (doses, critères, conduite)",
              11: "O1 fond médical (doses, critères, conduite)", 4: "O3 démarche diagnostique", 5: "O3 démarche diagnostique", 6: "O3 démarche diagnostique",
              7: "O3 démarche diagnostique", 9: "O3 démarche diagnostique", 10: "O3 démarche diagnostique"}


def verdicts(t, nom):
    V = {}
    for n in range(1, 15):
        if not F.zone(t, n): continue
        ka = [d for f in F.FAM_A for d in F.analyseur("A", f, n)(t, nom, {})[0] if d["severite"] in ("GRAVE", "CRITIQUE")]
        kb = [d for f in F.FAM_B if f != "M" for d in F.analyseur("B", f, n)(t, nom, {})[0] if d["severite"] in ("GRAVE", "CRITIQUE")]
        V[n] = (ka, kb)
    return V


def analyser(t, nom, opt=None):
    me = sys.modules[__name__]; D = []; V = verdicts(t, nom); route = {}
    for n, (ka, kb) in V.items():
        if kb and not ka:
            o = OPUS_POINT.get(n) or OPUS.get(F.signal("B", kb[0]["scriptone"][-1]), "O5 forme et pédagogie"); route[n] = o
            D.append(bus.doleance(me, "X1", nom, bus.ancre(t, F.zone(t, n)[0], f"{n}."), "MOYEN", f"désaccord au point {n} : β voit {len(kb)} faute(s) grave(s) qu'α ne voit pas ({', '.join(sorted({d['code'] for d in kb}))})",
                                  f"router vers le nœud {o} avec les doléances β du point {n} et son seul paquet", "agent", "; ".join(d["constat"][:60] for d in kb[:3])))
        elif ka and not kb:
            route[n] = SONNET[n]
            D.append(bus.doleance(me, "X2", nom, bus.ancre(t, F.zone(t, n)[0], f"{n}."), "DETAIL", f"point {n} : faute(s) de forme α seulement ({', '.join(sorted({d['code'] for d in ka}))}), fond confirmé par β",
                                  f"router vers le nœud Sonnet {SONNET[n]} (correction de forme ciblée)", "agent", "; ".join(d["constat"][:60] for d in ka[:3])))
    return D, dict(points=len(V), accords=sum(bool(a) == bool(b) for a, b in V.values()), desaccords=len(route), routage=route)


MUTANTS = [("faute vue par β seul", lambda t, r: F.inserer(t, r.choice([3, 5, 7, 9]), f'La règle s\'applique à tous.<sup class="r"><a href="#sb-{r.randint(90, 99)}">9</a></sup>', r), "X1"),
           ("faute vue par α seul", lambda t, r: F.inserer(t, r.choice([3, 5, 7, 9, 12]), r.choice(F.NEG_PURES), r), "X2")]
ECRIT = []
COUT_MUTATION = 10

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))

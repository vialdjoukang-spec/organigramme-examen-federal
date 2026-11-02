#!/usr/bin/env python3
"""Scriptone S17 · compilateur de brief : ce que l'agent reçoit, et rien d'autre (consignes minimales, doléances [agent], paquets concernés). Région ENT.
compiler(t, nom, doleances) → brief Markdown : règle absolue, interdits, puis, point par point, les doléances à appliquer telles quelles.
L'analyse porte sur le TEXTE d'un brief (contrat de sortie du compilateur) :
  F1 règle absolue de la contraction absente     F2 interdiction d'inventer (chiffre, dose, source) absente
  F3 brief au-dessus de son plafond (3 000 jetons) F4 ligne de doléance mal formée (sans ancre ni correction « → »)"""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bus

ID, REGION, VERSION = "s17_brief", "ENT", "1.0.0"
PLAFOND = 3000
REGLE = "RÈGLE ABSOLUE : la contraction ne touche ni les notions, ni le sens, ni les explications ; reformuler plus concis est permis, résumer jamais."
INTERDIT = "JAMAIS : inventer un chiffre, une dose, une source ou une référence ; une absence se tait (aucun « à vérifier », « non chiffré », « non lu »)."
DORE = Path(__file__).resolve().parent.parent / "dore/brief_dore.md"
O = {k: i for i, k in enumerate(bus.SEVERITES)}


def compiler(t, nom, doleances, plafond=PLAFOND):
    ag = sorted([d for d in doleances if d["executant"] == "agent"], key=lambda d: (O[d["severite"]], d["code"]))
    par = {}
    for d in ag:
        m = re.search(r"point (\d{1,2})", d["constat"]); par.setdefault(int(m.group(1)) if m else 0, []).append(d)
    L = [f"# Brief de correction · {nom}", REGLE, INTERDIT, "Applique chaque correction telle quelle, à l'ancre donnée ; ne relis pas le fichier entier."]
    S = bus.sections(t) if t else {}
    for n in sorted(par):
        L.append(f"## Point {n}" if n else "## Ensemble du cours")
        for d in par[n]:
            l = f"- {d['severite']} {d['code']} {d['ancre']} : {d['constat']} → {d['correction_prescrite']}"
            if bus.estime_jetons("\n".join(L + [l])) > plafond - 60:
                L.append(f"- … {sum(len(v) for v in par.values()) - sum(1 for x in L if x.startswith('- '))} doléances suivantes au prochain passage (plafond du brief)"); return "\n".join(L) + "\n"
            L.append(l)
    return "\n".join(L) + "\n"


def analyser(t, nom, opt=None):
    me = sys.modules[__name__]; D = []
    if REGLE not in t:
        D.append(bus.doleance(me, "F1", nom, "#brief", "CRITIQUE", "règle absolue de la contraction absente du brief", "recompiler le brief (s17_brief.compiler)", "script"))
    if INTERDIT not in t:
        D.append(bus.doleance(me, "F2", nom, "#brief", "CRITIQUE", "interdiction d'inventer absente du brief", "recompiler le brief (s17_brief.compiler)", "script"))
    j = bus.estime_jetons(t)
    if j > PLAFOND:
        D.append(bus.doleance(me, "F3", nom, "#brief", "MOYEN", f"brief de {j} jetons (plafond {PLAFOND})", "découper le brief par point ; envoyer le reste au passage suivant", "script"))
    mal = [l for l in t.splitlines() if l.startswith("- ") and not l.startswith("- …") and not re.match(r"- (?:CRITIQUE|GRAVE|MOYEN|DETAIL) [A-Z]{1,2}\d .+ : .+ → .+", l)]
    for l in mal[:3]:
        D.append(bus.doleance(me, "F4", nom, "#brief", "MOYEN", "ligne de doléance mal formée (sans sévérité, code, ancre ou correction)", "recompiler le brief", "script", l[:160]))
    return D, dict(jetons=j, lignes=len(t.splitlines()), doleances=sum(l.startswith("- ") for l in t.splitlines()))


MUTANTS = [("règle absolue retirée", lambda t, r: t.replace(REGLE + "\n", ""), "F1"), ("interdit retiré", lambda t, r: t.replace(INTERDIT + "\n", ""), "F2"),
           ("brief trop long", lambda t, r: t + "\n".join(f"- MOYEN AH1 #p{i} · l.{i} : phrase nominale au point {i % 14 + 1} → réécrire en phrase verbale" for i in range(r.randint(300, 400))) + "\n", "F3"),
           ("ligne mal formée", lambda t, r: t + r.choice(["- corriger le point 3\n", "- GRAVE : sans code ni flèche\n"]), "F4")]
ECRIT = []

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))

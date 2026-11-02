#!/usr/bin/env python3
"""Scriptone S10 · mémoire tentaculaire des fautes déjà corrigées (anti-récidive). Région MEM.
Chaque entrée de memoire_fautes.json est une correction réelle (relecture externe, auditeurs, Prompt §4 bis) : motifs requis dans une même
phrase, motif d'exclusion, constat, correction prescrite et tentacule (région qui traite : AUM fond médical, AUL langue, AUF forme).
  M1 prétraitement P2Y12 systématique · M2 anaphylaxie assise · M3 C4 « hors crise » · M4 C4 normal « exclut » · M5 NaCl 3 % sans durée
  M6 indication FDA · M7 rang de fréquence sans source · M8 infobulle title=
Lecture seule : un script ne juge pas la clinique, il empêche la RÉCIDIVE d'une faute déjà jugée par un humain ou un auditeur."""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bus

ID, REGION, VERSION = "s10_memoire", "MEM", "1.0.0"
DEPEND = ["memoire_fautes.json"]
F = json.loads((Path(__file__).resolve().parent / "memoire_fautes.json").read_text(encoding="utf-8"))["fautes"]


def phrases_cours(t):
    a, f = bus.bornes_cours(t); out = []
    for pa, pf, inner in bus.blocs(t, a, f, ("p", "li", "td")):
        if re.search(r"(?i)<(?:p|li)\b", inner): continue
        for ph in bus.phrases(bus.texte(inner)) or [bus.texte(inner)]: out.append((pa, ph, inner))
    return out


def analyser(t, nom, opt=None):
    me = sys.modules[__name__]; D = []; P = phrases_cours(t); a, f = bus.bornes_cours(t); k = {}
    for e in F:
        if e.get("html"):
            for m in list(re.finditer(e["tous"][0], t[a:f]))[:3]:
                k[e["code"]] = k.get(e["code"], 0) + 1
                D.append(bus.doleance(me, e["code"], nom, bus.ancre(t, a + m.start(), m.group(0)), e["severite"], f"{e['constat']} (mémoire : {e['origine']})",
                                      e["correction"], "agent", f"tentacule {e['region']} · {m.group(0)[:120]}"))
            continue
        for pa, ph, inner in P:
            dans_bloc = e["code"] == "M7" and re.search(e["sauf"], inner)          # rang : la source peut suivre la phrase dans son bloc
            if all(re.search(x, ph) for x in e["tous"]) and not re.search(e["sauf"], ph) and not dans_bloc:
                k[e["code"]] = k.get(e["code"], 0) + 1
                D.append(bus.doleance(me, e["code"], nom, bus.ancre(t, pa, ph), e["severite"], f"{e['constat']} (mémoire : {e['origine']})",
                                      e["correction"], "agent", f"tentacule {e['region']} · {ph[:160]}"))
    return D, dict(entrees=len(F), recidives=k)


def _inj(e):
    def fn(t, r):
        S = bus.sections(t); n = r.choice(sorted(S)); B = [b for b in bus.blocs(t, *S[n], ("p",))]
        pa, pf, inner = r.choice(B); return t[:pf] + "<p>" + e["mutant"] + "</p>" + t[pf:]
    return fn
MUTANTS = [(f"récidive {e['code']}", _inj(e), e["code"]) for e in F]
ECRIT = []

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))

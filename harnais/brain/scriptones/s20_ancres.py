#!/usr/bin/env python3
"""Scriptone S20 · ancres et liens internes (barre des 14 points, exposants de source, bandes de médicaments, arbre). Région AUF.
  Y1 lien interne mort : href="#x" sans élément id="x" (un clic qui ne mène nulle part)
  Y2 cible ambiguë : id visé par un lien et présent plusieurs fois (le navigateur saute au premier)
  Y3 lien externe non sûr : http:// en clair ou javascript:
Lecture seule : la cible manquante relève du rédacteur (ou du convertisseur s'il l'a produite)."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bus

ID, REGION, VERSION = "s20_ancres", "AUF", "1.0.0"


def analyser(t, nom, opt=None):
    me = sys.modules[__name__]; D = []; prot = bus.masque(t, bus.RX_STYLE)
    ids = {}
    for m in re.finditer(r'\sid="([^"]+)"', prot): ids[m.group(1)] = ids.get(m.group(1), 0) + 1
    vises = {}
    for m in re.finditer(r'href="#([^"]*)"', prot): vises.setdefault(m.group(1), m.start())
    morts = [(h, p) for h, p in vises.items() if h and h not in ids]
    for h, p in morts[:10]:
        D.append(bus.doleance(me, "Y1", nom, bus.ancre(t, p, h), "GRAVE", f"lien interne mort : #{h}", f"créer la cible id=\"{h}\" ou corriger le lien", "agent", h))
    for h, p in vises.items():
        if ids.get(h, 0) > 1:
            D.append(bus.doleance(me, "Y2", nom, bus.ancre(t, p, h), "MOYEN", f"cible #{h} présente {ids[h]} fois : le lien saute à la première",
                                  "rendre l'id unique (la cible visée garde l'id, les autres prennent une classe)", "agent", h))
    for m in list(re.finditer(r'href="(http://[^"]+|javascript:[^"]*)"', prot))[:5]:
        D.append(bus.doleance(me, "Y3", nom, bus.ancre(t, m.start(), m.group(1)), "MOYEN", f"lien non sûr : {m.group(1)[:60]}", "écrire l'URL en https:// réellement ouverte ; jamais de javascript:", "agent", m.group(1)[:120]))
    return D, dict(ids=len(ids), liens_internes=len(vises), morts=len(morts))


def _m_mort(t, r):
    a, f = bus.bornes_cours(t); i = t.index("</p>", (a + f) // 2)
    return t[:i] + f' <a href="#cible-absente-{r.randint(1, 999)}">voir</a>' + t[i:]
def _m_double(t, r):
    h = r.choice(re.findall(r'href="#(sb-\d+)"', t)); i = t.index("</main>") if "</main>" in t else len(t)
    return t[:i] + f'<div id="{h}">copie</div>' + t[i:]
def _m_http(t, r):
    a, f = bus.bornes_cours(t); i = t.index("</p>", (a + f) // 2)
    return t[:i] + r.choice([' <a href="http://example.invalid/page">page</a>', ' <a href="javascript:void(0)">lien</a>']) + t[i:]
MUTANTS = [("lien mort", _m_mort, "Y1"), ("cible en double", _m_double, "Y2"), ("lien non sûr", _m_http, "Y3")]
ECRIT = []

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))

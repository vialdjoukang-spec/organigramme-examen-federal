#!/usr/bin/env python3
"""Scriptone S12 · ordonnanceur anti-conflit (un seul écrivain par zone ; ordre ; idempotence). Région BUS.
Preuve statique + contre-épreuve dynamique, sur CHAQUE fichier :
  O1 zone revendiquée par deux écrivains dans le registre (refus de démarrer : pigeonnier, conflit certain)
  O2 non-confluence : le résultat dépend de l'ordre des écrivains (K ordres aléatoires, chacun jusqu'au point fixe)
  O3 non-idempotence de la chaîne : corriger(corriger(x)) ≠ corriger(x)
  O4 écriture hors zone : un écrivain modifie une partie du fichier qu'il n'a pas déclarée
Options : ordres (défaut 3), graine ; injecter = duel | bavard | intrus (écrivains de test, pour la mutation) ; registre (registre de test)."""
import difflib, json, random, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bus, reseau

ID, REGION, VERSION = "s12_ordonnanceur", "BUS", "1.0.0"
DEPEND = ["reseau.py", "registre.json"]


def portees(t, zones):
    """Intervalles autorisés pour un ensemble de zones déclarées (évaluées sur le texte AVANT écriture)."""
    out = []; S = bus.sections(t); a, f = bus.bornes_cours(t); body = re.search(r"(?i)<body\b[^>]*>", t); b0 = body.end() if body else 0
    for z in zones:
        k = z.split(":")[0]
        if k.startswith("P") and k[1:].isdigit():
            n = int(k[1:])
            if n in S: out.append(S[n])
        elif k == "CSS": out.append((0, b0 + 1))
        elif k == "NAV": out += [(b0 - 1, b0 + 1)] + [(m.start(), m.end()) for m in re.finditer(r'(?is)<nav id="brain-barre14".*?</nav>', t)]
        elif k == "H3": out += [(m.start(), m.end()) for m in re.finditer(r"<h3\b[^>]*>", t)]
        elif k == "SRC": out.append((f, len(t)))
        elif k in ("BLANCS", "TEXTE", "TABLE"): out.append((a, f))
    return out


def changements(t, u):
    """Fenêtres [début, fin) du texte d'origine modifiées par l'écriture (diff par lignes, puis par caractères dans la ligne)."""
    A, B = t.splitlines(True), u.splitlines(True); pos = [0]
    for l in A: pos.append(pos[-1] + len(l))
    out = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, A, B, autojunk=False).get_opcodes():
        if tag == "equal": continue
        x, y = "".join(A[i1:i2]), "".join(B[j1:j2]); p = 0
        while p < min(len(x), len(y)) and x[p] == y[p]: p += 1
        s = 0
        while s < min(len(x), len(y)) - p and x[-1 - s] == y[-1 - s]: s += 1
        out.append((pos[i1] + p, max(pos[i1] + p + 1, pos[i2] - s)))
    return out


# écrivains de test (mutation de l'ordonnanceur lui-même)
def _duel_a(t, o=None): return t.replace("froid", "FROID")
def _duel_b(t, o=None): return t.replace("FROID", "froid").replace("Le froid", "Le grand froid") if "FROID" in t else t
def _bavard(t, o=None): return t.replace("</main>", "<!-- passage -->" + "</main>", 1)
def _intrus(t, o=None):
    S = bus.sections(t); a, f = S[5]; i = t.index("</p>", a); return t[:i] + " (note)" + t[i:]
TEST = {"duel": [("test_duel_a", ["P3:test"], _duel_a), ("test_duel_b", ["P3:test2"], _duel_b)],
        "bavard": [("test_bavard", ["TEXTE:test"], _bavard)], "intrus": [("test_intrus", ["P3:test"], _intrus)]}


def analyser(t, nom, opt=None):
    opt = opt or {}; me = sys.modules[__name__]; D = []
    reg = opt.get("registre") or reseau.registre()
    for z, ids in reseau.conflits_statiques(reg).items():
        D.append(bus.doleance(me, "O1", nom, "#haut · registre", "CRITIQUE", f"zone {z} revendiquée par {len(ids)} écrivains : {', '.join(ids)}",
                              "donner la zone à un seul écrivain ; les autres émettent des doléances (règle anti-conflit)", "agent", json.dumps(ids)))
    W = [(i, z, (lambda m: lambda x, o=None: m.corriger(x, {}))(reseau.module(i))) for i, z in reseau.ecrivains()] + TEST.get(opt.get("injecter"), [])
    r = random.Random(opt.get("graine", nom)); K = int(opt.get("ordres", 3))
    def chaine(x, ordre):
        for _ in range(4):
            y = x
            for i, z, fn in ordre: y = fn(y)
            if y == x: return y
            x = y
        return x
    ref = chaine(t, W); ordres = 0
    for k in range(K):
        o = W[:]; r.shuffle(o); ordres += 1
        if chaine(t, o) != ref:
            D.append(bus.doleance(me, "O2", nom, "#haut · ordre", "GRAVE", f"résultat dépendant de l'ordre des écrivains (ordre aléatoire n° {k + 1})",
                                  "séparer les zones des écrivains en conflit, ou fixer leur ordre dans reseau.ORDRE", "agent", " → ".join(i for i, _, _ in o)[:380])); break
    if chaine(ref, W) != ref:
        D.append(bus.doleance(me, "O3", nom, "#haut · idempotence", "GRAVE", "chaîne de correction non idempotente", "rendre chaque écrivain idempotent (pose_style, remplacements stables)", "agent"))
    hors = 0
    for i, z, fn in W:
        u = fn(t)
        if u == t: continue
        P = portees(t, z)
        for a, b in changements(t, u):
            if not any(x <= a and b <= y + 1 for x, y in P):
                hors += 1
                D.append(bus.doleance(me, "O4", nom, bus.ancre(t, a, t[a:a + 40]), "GRAVE", f"{i} écrit hors de ses zones {z}",
                                      f"restreindre {i} à ses zones déclarées, ou déclarer la zone (si elle n'a pas d'autre écrivain)", "agent", f"{a}–{b}")); break
    return D, dict(ecrivains=len(W), zones=sorted({x for _, z, _ in W for x in z}), ordres_testes=ordres, hors_zone=hors, conflits_statiques=len(reseau.conflits_statiques(reg)))


def _m_reg(t, r):
    reg = json.loads(json.dumps(reseau.registre())); e = r.choice([x for x in reg["scriptones"] if not x["ecrit"]]); e["ecrit"] = [r.choice(reseau.ecrivains())[1][0]]
    return t, {"registre": reg, "ordres": 1}
MUTANTS = [("deux écrivains sur une zone", _m_reg, "O1"), ("duel d'écrivains", lambda t, r: (t, {"injecter": "duel", "ordres": 6, "graine": r.random()}), "O2"),
           ("écrivain non idempotent", lambda t, r: (t, {"injecter": "bavard", "ordres": 1}), "O3"), ("écrivain intrus", lambda t, r: (t, {"injecter": "intrus", "ordres": 1}), "O4")]
ECRIT = []
COUT_MUTATION = 2       # graines par mutant (chaîne complète × K ordres : coûteux)

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))

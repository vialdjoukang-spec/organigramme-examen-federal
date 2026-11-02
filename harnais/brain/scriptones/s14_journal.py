#!/usr/bin/env python3
"""Scriptone S14 · journal de circulation (JSONL, schéma evenements.schema.json) : intégrité sous concurrence. Région BUS.
Entrée : le TEXTE du journal (.cache/brain/evenements.jsonl), pas un cours. C'est ce journal que la vue 3D rejoue.
  J1 ligne illisible (JSON tronqué : écriture interrompue)     J2 champ obligatoire absent (v, ts, run, seq, type, de, vers)
  J3 type de signal inconnu                                     J4 rang (seq) dupliqué ou décroissant dans un passage (écritures concurrentes)
Correction (--appliquer, executant = script) : J1, J2 et J3 sont retirées du journal (quarantaine comptée en mesure) ; J4 reste signalée."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bus

ID, REGION, VERSION = "s14_journal", "BUS", "1.0.0"
DEPEND = ["evenements.schema.json"]
OBLIG = ("v", "ts", "run", "seq", "type", "de", "vers")
DORE = Path(__file__).resolve().parent.parent / "dore/journal_dore.jsonl"


def lignes(t):
    out = []
    for k, l in enumerate(t.splitlines(), 1):
        if not l.strip(): continue
        try: e = json.loads(l); out.append((k, l, e if isinstance(e, dict) else None, None if isinstance(e, dict) else "objet attendu"))
        except ValueError as x: out.append((k, l, None, str(x)[:80]))
    return out


def defaut(e):
    if e is None: return "J1"
    if any(c not in e for c in OBLIG) or not isinstance(e.get("seq"), int): return "J2"
    if e.get("type") not in bus.TYPES: return "J3"
    return None


def analyser(t, nom, opt=None):
    me = sys.modules[__name__]; D = []; L = lignes(t); k = {"J1": 0, "J2": 0, "J3": 0, "J4": 0}; dern = {}
    for n, l, e, err in L:
        c = defaut(e)
        if c:
            k[c] += 1
            if k[c] <= 5:
                D.append(bus.doleance(me, c, nom, f"#journal · l.{n}", "GRAVE" if c == "J1" else "MOYEN",
                                      {"J1": f"ligne illisible ({err})", "J2": "champ obligatoire absent", "J3": f"type de signal inconnu : {e.get('type') if e else '?'}"}[c],
                                      "mettre la ligne en quarantaine : s14_journal.py --appliquer (le passage reste lisible)", "script", l[:200]))
            continue
        r, s = str(e["run"]), e["seq"]
        if r in dern and s <= dern[r]:
            k["J4"] += 1
            if k["J4"] <= 5:
                D.append(bus.doleance(me, "J4", nom, f"#journal · l.{n}", "MOYEN", f"rang {s} non croissant dans le passage {r[:24]} (écritures concurrentes)",
                                      "écrire chaque passage depuis un seul processus (orchestre.py numérote) ; vérifier le verrou du journal", "agent", l[:200]))
        dern[r] = max(dern.get(r, -1), s)
    return D, dict(lignes=len(L), quarantaine=k["J1"] + k["J2"] + k["J3"], **k)


def corriger(t, opt=None):
    L = lignes(t)
    if all(defaut(e) is None for _, _, e, _ in L): return t
    return "".join(l + "\n" for _, l, e, _ in L if defaut(e) is None)


def _m_tronque(t, r):
    L = t.splitlines(); i = r.randrange(len(L)); L[i] = L[i][:r.randint(5, max(6, len(L[i]) - 5))]; return "\n".join(L) + "\n"
def _m_champ(t, r):
    L = t.splitlines(); i = r.randrange(len(L)); e = json.loads(L[i]); e.pop(r.choice(OBLIG)); L[i] = json.dumps(e, ensure_ascii=False); return "\n".join(L) + "\n"
def _m_type(t, r):
    L = t.splitlines(); i = r.randrange(len(L)); e = json.loads(L[i]); e["type"] = r.choice(["audio", "inconnu", "Medical"]); L[i] = json.dumps(e, ensure_ascii=False); return "\n".join(L) + "\n"
def _m_seq(t, r):
    L = t.splitlines(); i = r.randrange(1, len(L)); e = json.loads(L[i]); p = json.loads(L[i - 1]); e["run"] = p["run"]; e["seq"] = p["seq"]
    L[i] = json.dumps(e, ensure_ascii=False); return "\n".join(L) + "\n"
MUTANTS = [("ligne tronquée", _m_tronque, "J1"), ("champ absent", _m_champ, "J2"), ("type inconnu", _m_type, "J3"), ("rang dupliqué", _m_seq, "J4")]
ECRIT = ["JOURNAL:quarantaine"]

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))

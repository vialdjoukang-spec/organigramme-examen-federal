#!/usr/bin/env python3
"""Scriptone S15 · gardien d'intégrité des 160 scriptones (empreintes SHA-256 et registre). Région SEC.
Entrée : le TEXTE de SHA256SUMS (liste « empreinte  chemin »), comparé aux fichiers réels du dossier et au registre.
  G1 altération (empreinte différente du fichier)      G2 fichier listé introuvable
  G3 scriptone ou donnée présent mais non listé        G4 registre incohérent (fichier absent, empreinte du registre périmée)
Toute altération arrête le scriptone concerné (bus.executer, code 3) ; le gardien en fait la revue d'ensemble."""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bus

ID, REGION, VERSION = "s15_gardien", "SEC", "1.0.0"
D_ = Path(__file__).resolve().parent
DORE = D_ / "SHA256SUMS"


def analyser(t, nom, opt=None):
    opt = opt or {}; me = sys.modules[__name__]; D = []; listes = {}
    for k, l in enumerate(t.splitlines(), 1):
        m = re.match(r"^([0-9a-f]{64})\s+(\S.*)$", l.strip())
        if not m:
            if l.strip(): D.append(bus.doleance(me, "G1", nom, f"#SHA256SUMS · l.{k}", "CRITIQUE", "ligne d'empreinte illisible", "régénérer : python3 harnais/brain/cerveau.py empreintes --ecrire (après revue)", "agent", l[:120]))
            continue
        h, n = m.group(1), m.group(2).strip(); listes[n] = h; p = (D_ / n).resolve()
        if D_.resolve() not in p.parents or not p.is_file():      # introuvable, dossier, ou chemin hors du dossier (../) : jamais lu
            D.append(bus.doleance(me, "G2", nom, f"#SHA256SUMS · l.{k}", "CRITIQUE", f"fichier listé introuvable : {n}", "restaurer le fichier ou le retirer de la liste après revue", "agent", n))
        elif bus.sha(p.read_bytes()) != h:
            D.append(bus.doleance(me, "G1", nom, f"#SHA256SUMS · l.{k}", "CRITIQUE", f"altération : {n} ne correspond plus à son empreinte",
                                  "revoir la modification (git diff) ; si elle est voulue, régénérer les empreintes ; sinon restaurer le fichier", "agent", n))
    for n in bus.fichiers_empreintes():
        if n not in listes:
            D.append(bus.doleance(me, "G3", nom, "#SHA256SUMS", "GRAVE", f"{n} n'est pas protégé par une empreinte", "régénérer les empreintes après revue", "agent", n))
    reg = opt.get("registre")
    if reg is None and (D_ / "registre.json").exists(): reg = json.loads((D_ / "registre.json").read_text(encoding="utf-8"))
    for e in (reg or {}).get("scriptones", []):
        if e.get("langage", "python") != "python": continue
        p = D_ / e["fichier"]
        if not p.exists() or (e.get("sha256") and bus.sha(p.read_bytes()) != e["sha256"]):
            D.append(bus.doleance(me, "G4", nom, f"#registre · {e['id']}", "GRAVE", f"registre incohérent pour {e['id']} ({'absent' if not p.exists() else 'empreinte périmée'})",
                                  "régénérer le registre : python3 harnais/brain/outils/gabarit.py", "agent", e["fichier"]))
    return D, dict(listes=len(listes), registre=len((reg or {}).get("scriptones", [])))


def _lignes(t): return [l for l in t.splitlines() if l.strip()]
def _m_alt(t, r):
    L = _lignes(t); i = r.randrange(len(L)); h = L[i][:64]; c = r.randrange(64); x = "0" if h[c] != "0" else "1"
    L[i] = h[:c] + x + h[c + 1:] + L[i][64:]; return "\n".join(L) + "\n"
def _m_fantome(t, r): return t + f"{'%064x' % r.getrandbits(256)}  fantome_{r.randint(1, 99)}.py\n"
def _m_retire(t, r): L = _lignes(t); L.pop(r.randrange(len(L))); return "\n".join(L) + "\n"
def _m_reg(t, r):
    reg = json.loads((D_ / "registre.json").read_text(encoding="utf-8")); e = r.choice([x for x in reg["scriptones"] if x.get("langage", "python") == "python"])
    e["sha256"] = "%064x" % r.getrandbits(256); return t, {"registre": reg}
MUTANTS = [("empreinte altérée", _m_alt, "G1"), ("fichier fantôme", _m_fantome, "G2"), ("fichier non listé", _m_retire, "G3"), ("registre périmé", _m_reg, "G4")]
ECRIT = []

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))

#!/usr/bin/env python3
"""Audit d'un LOT par scripts (0 token) : contrôle médical + contrôle de langue + forme, sur tous les fichiers écrits.
  python3 harnais/audit_lot.py <LOT> [--dossier <chemin>]     (défaut : .cache/travail/LOT_<LOT>, cycle lu dans taches.json)
Écrit audits/MED_<f>_C<c>.md et audits/CONF_<f>_C<c>.md, met à jour le tableau de tâches, affiche le bilan. Code 0 si ≥90 %, 0 critique partout."""
import concurrent.futures as cf, json, re, subprocess, sys
from pathlib import Path
R = Path(__file__).resolve().parent.parent; lot = sys.argv[1]
D = Path(sys.argv[sys.argv.index("--dossier") + 1]) if "--dossier" in sys.argv else R / ".cache/travail" / f"LOT_{lot}"
T = D / "taches.json"; c = json.loads(T.read_text())["cycle"] if T.exists() else 1; (D / "audits").mkdir(exist_ok=True)
fs = sorted(D.glob("LOT_*_Phase_*.html"))
def run(args): return subprocess.run([sys.executable, *args], capture_output=True, text=True, timeout=1800, cwd=R)
def un(f):
    m = D / "audits" / f"MED_{f.name}_C{c}.md"; l = D / "audits" / f"CONF_{f.name}_C{c}.md"
    if not m.exists(): run(["harnais/controle_medical.py", str(f), "--rapport", str(m)])
    if not l.exists(): run(["harnais/controle_langue.py", str(f), "--rapport", str(l)])
    g = lambda p: (lambda x: dict(score=float(x.group(1)), crit=int(x.group(2)), q=x.group(3)) if x else None)(re.search(r"RESULTAT score=([\d.]+) critiques=(\d+) question=(\w+)", p.read_text())) if p.exists() else None
    return f.name, g(m), g(l)
with cf.ThreadPoolExecutor(3) as ex: res = list(ex.map(un, fs))
ko = []; L = []
for n, m, l in res:
    ok = bool(m and l and all(x["score"] >= 90 and x["crit"] == 0 for x in (m, l))); L.append(f"| {n} | {m['score'] if m else '—'} / {m['crit'] if m else '—'} | {l['score'] if l else '—'} / {l['crit'] if l else '—'} | {'OUI' if ok else 'NON'} |")
    if not ok: ko.append(n)
    if T.exists():
        i = "A" if "Phase_A" in n else re.search(r"DX\.(\d+)", n).group(1); d = json.loads(T.read_text())
        for k in ("med", "conf"): d[k][i] = "fait"
        T.write_text(json.dumps(d, ensure_ascii=False, indent=1))
B = "| Fichier | Médical score/crit | Langue score/crit | Conforme |\n|---|---|---|---|\n" + "\n".join(L)
(D / "audits" / f"BILAN_SCRIPTS_C{c}.md").write_text(f"# Bilan audit par scripts — LOT_{lot} cycle {c}\n\n{B}\n", encoding="utf-8")
print(B); print(f"\nBILAN cycle {c} : {len(res)-len(ko)}/{len(res)} conformes" + (f" · à corriger : {len(ko)}" if ko else "")); sys.exit(1 if ko else 0)

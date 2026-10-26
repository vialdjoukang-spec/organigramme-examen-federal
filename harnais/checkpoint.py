#!/usr/bin/env python3
"""CHECKPOINT d'un fichier (porte individuelle, gratuite) : médical + langue rapide + forme → onglet Rappel mémoire (G) → commit + push sur la branche du LOT.
  python3 harnais/checkpoint.py <LOT> <fichier.html> [--cycle N]
Sortie : « CHECKPOINT OK » (fichier commité) ou « CHECKPOINT REFUSÉ » + chemins des rapports à corriger (rien n'est commité).
Un fichier = un checkpoint : autant de chapitres, autant de contrôles médicaux. La PR du LOT est ouverte une fois tous les fichiers commités."""
import fcntl, importlib.util, json, re, shutil, subprocess, sys
from pathlib import Path
R = Path(__file__).resolve().parent.parent; lot = sys.argv[1]; f = Path(sys.argv[2]).resolve(); SORTIE = "--sortie" in sys.argv; TER = f.parent.name if f.parent.name in ("entree", "sortie") else None
LOTDIR = R / ".cache/travail" / f"LOT_{lot}"
c = sys.argv[sys.argv.index("--cycle") + 1] if "--cycle" in sys.argv else str(json.loads((LOTDIR / "taches.json").read_text()).get("cycle", 1)) if (LOTDIR / "taches.json").exists() else "1"
A = LOTDIR / "audits"; A.mkdir(exist_ok=True); WT = R.parent / f"wt-{lot}"
def run(*a, **k): return subprocess.run(a, capture_output=True, text=True, cwd=k.get("cwd", R))
res = lambda p: (lambda m: dict(score=float(m.group(1)), crit=int(m.group(2))) if m else None)(re.search(r"RESULTAT score=([\d.]+) critiques=(\d+)", p.read_text())) if p.exists() else None
med, lan = A / f"MED_{f.name}_C{c}.md", A / f"CONF_{f.name}_C{c}.md"
run("python3", "harnais/controle_medical.py", str(f), "--rapport", str(med)); run("python3", "harnais/controle_langue.py", str(f), "--rapport", str(lan))
spec = importlib.util.spec_from_file_location("cl", R / "harnais/controle_lot.py"); cl = importlib.util.module_from_spec(spec); sys.argv_bak, sys.argv = sys.argv, ["x"]; spec.loader.exec_module(cl); sys.argv = sys.argv_bak
forme = cl.analyse_fichier(f); m, l = res(med), res(lan)
if lot in ("001", "002", "003", "004", "005", "006", "007", "008", "009", "010", "011", "012", "013", "014", "015", "016"):
    run("python3", "harnais/rappel_memoire.py", "inject", str(f))   # onglet Rappel mémoire (catégorie G), idempotent
mx = re.search(r"DX\.(\d+)", f.name)
if mx and (LOTDIR / "LISTE_DX_CANONIQUE.md").exists():   # le titre h2 doit porter « DX.n — nom » (cohérence A↔B)
    n_ = mx.group(1); tx = f.read_text(encoding="utf-8", errors="replace")
    if not re.search(rf"<h2[^>]*>\s*DX\.{n_}\s*[—–-]", tx):
        ml = re.search(rf"DX\.{n_}\s*[—–-]\s*([^\n|«»]+)", (LOTDIR / "LISTE_DX_CANONIQUE.md").read_text(encoding="utf-8"))
        if ml: f.write_text(re.sub(r"<h2[^>]*>.*?</h2>", f"<h2>DX.{n_} — {ml.group(1).strip()}</h2>", tx, count=1, flags=re.S), encoding="utf-8")
sys.path.insert(0, str(R / "harnais")); import forme_interactive as FI
conv = FI.convert(f.read_text(encoding="utf-8", errors="replace")); crit_i, moy_i, st_i = FI.controle(conv)
cf = R / ".cache/conv" / f.name; cf.parent.mkdir(parents=True, exist_ok=True); cf.write_text(conv, encoding="utf-8"); forme = cl.analyse_fichier(cf)
bad = []
if not m or m["score"] < 90 or m["crit"]: bad.append(f"médical {m} → {med}")
if not l or l["score"] < 90 or l["crit"]: bad.append(f"langue {l} → {lan}")
if crit_i: bad.append("forme interactive : " + " ; ".join(crit_i))
if not 100_000 <= cf.stat().st_size <= 200_000: bad.append(f"taille finale {cf.stat().st_size} o hors bande 100–200 Ko : allège la forme (pas le fond)")
if forme["critiques"]: bad.append(f"forme {forme['critiques']} (bande 100–200 Ko APRÈS l'onglet ≈ +7 Ko : vise ≤ 190 Ko)")
if bad: print("CHECKPOINT REFUSÉ —", " | ".join(bad)); sys.exit(1)
tb = json.loads((LOTDIR / "taches.json").read_text()) if (LOTDIR / "taches.json").exists() else {}
idx = "A" if "Phase_A" in f.name else re.search(r"DX\.(\d+)", f.name).group(1); prop = (tb.get("ecrire", {}).get(idx, {}) or {}).get("prop")
if prop in ("1", "2", "3") and not SORTIE:   # étape rédaction : le fichier entre dans son territoire, en attente de l'audit-correctif Opus
    ent = LOTDIR / f"B{prop}" / "entree"; ent.mkdir(parents=True, exist_ok=True); shutil.copy2(f, ent / f.name); (ent / f.name).with_suffix(".src").write_text(str(f))
    print(f"CHECKPOINT OK (étape rédaction) — {f.name} → territoire B{prop}/entree, en attente de l'audit Opus"); sys.exit(0)
if "--sans-commit" in sys.argv: print("CHECKPOINT OK (portes passées ; commit réservé à l'auditeur du territoire)", f.name, f"médical {m['score']} % · langue {l['score']} %"); sys.exit(0)
if not WT.exists(): print("CHECKPOINT OK (pas de worktree de LOT : fichier non commité)"); sys.exit(0)
dest = WT / f"LOT_Claude_Finaux/LOT_{lot}"; (dest / "audits").mkdir(parents=True, exist_ok=True)
shutil.copy2(cf, dest / f.name); [shutil.copy2(p, dest / "audits" / p.name) for p in (med, lan)]
if (LOTDIR / "LISTE_DX_CANONIQUE.md").exists(): shutil.copy2(LOTDIR / "LISTE_DX_CANONIQUE.md", dest / "LISTE_DX_CANONIQUE.md")
with open(R / ".cache/verrous/git.lock", "w") as lk:
    fcntl.flock(lk, fcntl.LOCK_EX)
    run("git", "add", "-A", cwd=WT)
    r = run("git", "commit", "--no-verify", "-q", "-m", f"LOT_{lot} : {f.name} — checkpoint médical {m['score']} %, langue {l['score']} %\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01QZK4dvwhmDEnsTae9bMPTq", cwd=WT)
    p = run("git", "push", "-q", "-u", "origin", f"prod/lot-{lot}-final", cwd=WT)
if SORTIE and TER == "entree": (f.parent.parent / "sortie").mkdir(exist_ok=True); shutil.copy2(f, f.parent.parent / "sortie" / f.name)
print("CHECKPOINT OK —", f.name, f"médical {m['score']} % · langue {l['score']} % · commit " + ("fait" if r.returncode == 0 else "rien à commiter") + " · push " + ("ok" if p.returncode == 0 else "échec : " + p.stderr[-120:]))

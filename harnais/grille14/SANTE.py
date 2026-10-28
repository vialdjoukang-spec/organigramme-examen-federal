#!/usr/bin/env python3
"""Santé du circuit « Grille des 14 points » : une commande, une ligne par rubrique, lecture seule.
  python3 harnais/grille14/SANTE.py [--lot 001]      (G14_TEST=1 : lit le bac de test)
Rubriques : verrous (orphelins = > 20 min sans modification du fichier), bloqués, prêts non audités (> 20 min),
essais par fichier, pannes d'outil, commits du worktree vs origin, empreintes des scripts en lecture seule.
Code 0 = tout vert ; 1 = au moins une alerte (✗)."""
import hashlib, json, os, re, subprocess, sys, time
from pathlib import Path
R = Path(__file__).resolve().parents[2]; TEST = bool(os.environ.get("G14_TEST"))
lot = sys.argv[sys.argv.index("--lot") + 1] if "--lot" in sys.argv and sys.argv.index("--lot") + 1 < len(sys.argv) else "001"
WK = R / ".cache/test_g14" if TEST else R / ".cache/travail" / f"LOT_{lot}"
MEM = R / (".cache/test_g14/memoire" if TEST else ".cache/memoire")
WT = (R / ".cache/test_g14" if TEST else R.parent) / f"wt-{lot}"
SEUIL = 1200; now = time.time(); alerte = False
court = lambda n: re.sub(rf"^LOT_{lot}_(Phase_B_V0_)?|\.html$", "", n)
mn = lambda s: f"{int(s // 60)} min"
def ligne(ok, rub, det):
    global alerte
    alerte |= not ok; print(f"{'✓' if ok else '✗'} {rub:<22} {det}")
def jl(p):
    try: return json.loads(p.read_text())
    except (OSError, ValueError): return None

# 1. verrous
vs = []
for p in (R / ".cache/verrous").glob("*.lock"):
    d = jl(p)
    if not isinstance(d, dict) or "fichier" not in d or f"LOT_{lot}_" not in Path(d["fichier"]).name: continue
    try: af = now - os.path.getmtime(d["fichier"])
    except OSError: af = float("inf")
    vs.append((d.get("agent", "?"), court(Path(d["fichier"]).name), now - d.get("t", now), af))
orph = [v for v in vs if v[2] > SEUIL and v[3] > SEUIL]
ligne(not orph, "verrous", f"{len(vs)} actif(s)" + (" : " + ", ".join(f"{a}→{n} ({mn(t)})" for a, n, t, _ in sorted(vs)) if vs else "")
      + (" · ORPHELINS : " + ", ".join(f"{a}→{n} (verrou {mn(t)}, fichier {mn(min(f, 1e9))})" for a, n, t, f in orph) if orph else " · aucun orphelin"))
# 2. bloqués
bl = []
for p in sorted((WK / "bloque").glob("*.md")) if (WK / "bloque").exists() else []:
    t = p.read_text(encoding="utf-8", errors="replace"); ag = re.search(r"agent : (\S+)", t); ra = re.search(r"raison : (.+)", t)
    bl.append(f"{court(p.name[:-3])} ({ag.group(1) if ag else '?'} : {ra.group(1)[:40] if ra else '?'})")
ligne(not bl, "bloqués", f"{len(bl)}" + (" : " + " · ".join(bl) if bl else ""))
# 3. prêts non audités
pn = []; pret = sorted((WK / "pret").glob("*")) if (WK / "pret").exists() else []
for p in pret:
    auds = list((WK / "audits").glob(f"AUD_B*_{p.name}.md")) if (WK / "audits").exists() else []
    if not any(a.stat().st_mtime >= p.stat().st_mtime for a in auds) and now - p.stat().st_mtime > SEUIL: pn.append(f"{court(p.name)} ({mn(now - p.stat().st_mtime)})")
audites = sum(1 for p in pret if any(a.stat().st_mtime >= p.stat().st_mtime for a in (WK / "audits").glob(f"AUD_B*_{p.name}.md"))) if (WK / "audits").exists() else 0
ligne(not pn, "prêts non audités", f"{len(pret)} prêt(s), {audites} audité(s)" + (" · EN SOUFFRANCE > 20 min : " + ", ".join(pn) if pn else ""))
# 4. essais
es = jl(MEM / f"essais_{lot}{'_test' if TEST else ''}.json") or {}
lst = sorted(((k.split(":", 1) + [""])[:2] + [v] for k, v in es.items() if isinstance(v, dict)), key=lambda x: -x[2].get("n", 0))
haut = [x for x in lst if x[2].get("n", 0) >= 2]
ligne(not haut, "essais", f"{len(lst)} fichier(s) en cours de refus" + (" : " + ", ".join(f"{court(n)} {a} {e.get('n', 0)}/3" + (" (sans modif.)" if e.get("noop") else "") for a, n, e in lst[:16]) if lst else ""))
# 5. pannes d'outil
inc = sorted((WK / "incidents").glob("*.md")) if (WK / "incidents").exists() else []
err = MEM / "erreurs_moteur.log"; ne = err.read_text(errors="replace").count("Traceback") if err.exists() else 0
ligne(not inc, "pannes d'outil", f"{len(inc)} incident(s)" + (" : " + ", ".join(court(p.name[:-3]) for p in inc) if inc else "") + f" · erreurs internes du moteur : {ne}")
# 6. commits du worktree
if WT.exists():
    g = lambda *a: subprocess.run(["git", "-C", str(WT), *a], capture_output=True, text=True, timeout=30).stdout.strip()
    br = g("rev-parse", "--abbrev-ref", "HEAD"); av = g("rev-list", "--count", f"origin/{br}..HEAD") or "?"; ar = g("rev-list", "--count", f"HEAD..origin/{br}") or "?"
    sale = len([l for l in g("status", "--porcelain").splitlines() if l.strip()])
    ligne(av == "0" and ar == "0", "commits", f"{WT.name} {br} : {av} en avance, {ar} en retard sur origin, {sale} fichier(s) non commité(s) · dernier : {g('log', '-1', '--format=%cr · %s')[:90]}")
else: ligne(True, "commits", f"pas de worktree {WT.name}")
# 7. empreintes
sums = {}; f = R / "harnais/agents/SHA256SUMS"
for l in f.read_text().splitlines() if f.exists() else []:
    x = l.split(None, 1)
    if len(x) == 2: sums[x[1].strip()] = x[0]
faux = [n for n, h in sums.items() if not (R / n).exists() or hashlib.sha256((R / n).read_bytes()).hexdigest() != h]
inscr = [n for n in sums if (R / n).exists() and (R / n).stat().st_mode & 0o222]
ligne(sums and not faux and not inscr, "empreintes", f"{len(sums)} scripts suivis" + (f" · FAUSSES : {faux}" if faux else " · toutes justes") + (f" · INSCRIPTIBLES : {inscr}" if inscr else " · tous en lecture seule"))
sys.exit(1 if alerte else 0)

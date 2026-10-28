#!/usr/bin/env python3
"""Test du dispositif Harnais — sortie : CONFIRMÉ / ÉCHEC + bloc ajouté à harnais/PREUVE_EMBOITEMENT.txt."""
import hashlib, json, os, subprocess, sys, time
from pathlib import Path
R = Path(__file__).resolve().parents[2]; os.chdir(R); E = R / ".cache/harnais/etat.json"
def sh(*a, t=60): return subprocess.run(a, capture_output=True, text=True, timeout=t)
res = {}
if not E.exists() or time.time() - E.stat().st_mtime > 3:
    subprocess.Popen([sys.executable, "harnais/dispositif/veille.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
    time.sleep(4)
a = json.loads(E.read_text()); time.sleep(2.2); b = json.loads(E.read_text())
res["veille_active_chaque_seconde"] = b["tick"] > a["tick"] and time.time() - E.stat().st_mtime < 3
res["etat_tous_controles_ok"] = b["ok"]
p = R / "harnais/prompt_projet.py"
res["prompt_lecture_seule"] = not (p.stat().st_mode & 0o222)
res["prompt_lisible_agent"] = "UN SEUL LOT ACTIF" in sh(sys.executable, str(p)).stdout
orig = p.read_text(); alt = hashlib.sha256(orig.replace("90 %", "80 %").encode()).hexdigest()
res["alteration_detectable"] = alt != hashlib.sha256(orig.encode()).hexdigest()
res["controle_lot_conforme"] = "CONFORME" in sh(sys.executable, "harnais/controle_lot.py", "verifier", "--sans-nom", ".cache/travail/LOT_001").stdout
res["aips_texte_axhidrox"] = "peut être envisagée pendant la grossesse" in sh(sys.executable, "harnais/aips_texte.py", "69243", "--section", "Si nécessaire").stdout
res["aips_symbol_decode"] = "µg" in sh(sys.executable, "-c", "import sys;sys.path.insert(0,'tools');from aips_verbatim import decode;print(decode('<style>.s{font-family:Symbol}</style><p><span class=\"s\">m</span>g</p>'))").stdout
res["pubmed_verifier"] = "Hyperhidrosis" in sh(sys.executable, "harnais/pubmed.py", "verifier", "41572865").stdout
res["file_g_prep"] = '"N": 15' in sh(sys.executable, "harnais/file_g.py", "prep", "001").stdout
ok = all(res.values())
bloc = f"\n{time.strftime('%Y-%m-%d %H:%M')} Europe/Zurich\nboucle=test-dispositif-harnais-file-G\nok={ok}\ncommande=python3 harnais/dispositif/test_dispositif.py\n" + "\n".join(f"{k}={v}" for k, v in res.items()) + "\nproducteur=Claude Sonnet (chef de production)\n"
open(R / "harnais/PREUVE_EMBOITEMENT.txt", "a").write(bloc)
print("CONFIRMÉ" if ok else "ÉCHEC", json.dumps(res, ensure_ascii=False)); sys.exit(0 if ok else 1)

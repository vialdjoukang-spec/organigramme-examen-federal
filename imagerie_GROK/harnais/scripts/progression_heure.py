#!/usr/bin/env python3
"""Toutes les heures : validate.py, build_app.py, screenshot.py, puis le décompte archivé.
Usage : python3 scripts/progression_heure.py
N'écrit que sous harnais/progression/<horodatage>/ et relance bilan_nuit.py.
Ne pousse rien et n'écrit pas au chat.
"""
import glob, json, os, shutil, subprocess, sys
from datetime import datetime
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable

def checkouts():
    found = [("coordinateur", ROOT)]
    for i in range(1, 5):
        for name, path in (
            (f"lot{i}", f"/tmp/imagerie-lot{i}"),
            (f"audit{i}", f"/tmp/imagerie-audit{i}"),
        ):
            if os.path.isdir(os.path.join(path, "scripts", "validate.py")):
                found.append((name, path))
    return found

def run(cwd, args):
    p = subprocess.run([PY, *args], cwd=cwd, text=True, capture_output=True)
    return p.returncode, (p.stdout or "") + (p.stderr or "")

def counts_from_report(path):
    if not os.path.isfile(path):
        return {}
    try:
        return json.load(open(path, encoding="utf-8")).get("summary", {})
    except Exception as e:
        return {"erreur_lecture": str(e)}

def main():
    now = datetime.now(ZoneInfo("Europe/Zurich"))
    stamp = now.strftime("%Y%m%d-%H%M")
    dest = os.path.join(ROOT, "progression", stamp)
    os.makedirs(dest, exist_ok=True)
    archive = {"horodatage": now.strftime("%d.%m.%Y %H:%M Europe/Zurich"), "checkouts": []}
    for name, cwd in checkouts():
        entry = {"nom": name, "chemin": cwd, "commandes": []}
        code, out = run(cwd, [os.path.join(cwd, "scripts", "validate.py")])
        entry["commandes"].append({"cmd": "validate.py", "code": code})
        open(os.path.join(dest, f"{name}-validate.txt"), "w", encoding="utf-8").write(out)
        rep = os.path.join(cwd, "validate_report.json")
        if os.path.isfile(rep):
            shutil.copy2(rep, os.path.join(dest, f"{name}-validate_report.json"))
        entry["decompte"] = counts_from_report(rep)
        built = os.path.join(dest, f"{name}-Radio_Paires.html")
        code, out = run(cwd, [os.path.join(cwd, "scripts", "build_app.py"), "--external", "--out", built])
        entry["commandes"].append({"cmd": "build_app.py --external", "code": code})
        open(os.path.join(dest, f"{name}-build.txt"), "w", encoding="utf-8").write(out)
        tag = f"{stamp}-{name}"
        code, out = run(cwd, [os.path.join(cwd, "scripts", "screenshot.py"), "--html", built, "--tag", tag])
        entry["commandes"].append({"cmd": "screenshot.py", "code": code})
        open(os.path.join(dest, f"{name}-screenshot.txt"), "w", encoding="utf-8").write(out)
        shot_dir = os.path.join(cwd, "shots")
        kept = os.path.join(dest, "shots", name)
        os.makedirs(kept, exist_ok=True)
        for f in glob.glob(os.path.join(shot_dir, tag + "*.png")):
            shutil.copy2(f, os.path.join(kept, os.path.basename(f)))
        archive["checkouts"].append(entry)
        print(name, entry["decompte"], [(c["cmd"], c["code"]) for c in entry["commandes"]])
    json.dump(archive, open(os.path.join(dest, "decompte.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    bilan = os.path.join(SCRIPTS, "bilan_nuit.py")
    subprocess.run([PY, bilan], cwd=ROOT, check=False)
    print("archivé", dest)

if __name__ == "__main__":
    main()

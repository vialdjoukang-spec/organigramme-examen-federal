#!/usr/bin/env python3
"""Veille du Harnais : contrôle fonctionnel chaque seconde (local) ; réseau toutes les 30 s.
  python3 harnais/dispositif/veille.py            boucle (Ctrl-C) → .cache/harnais/etat.json + veille.log
  python3 harnais/dispositif/veille.py --once     un passage complet (réseau inclus), code 0 si tout est OK"""
import hashlib, json, os, py_compile, stat, subprocess, sys, time, urllib.request
from pathlib import Path
R = Path(__file__).resolve().parents[2]; C = R / ".cache" / "harnais"; C.mkdir(parents=True, exist_ok=True)
FICHIERS = ["harnais/prompt_projet.py", "harnais/controle_lot.py", "harnais/aips_texte.py", "harnais/pubmed.py", "harnais/scinder_1_10.py",
            "harnais/HARNAIS_OBLIGATOIRE.md", "harnais/SOURCES_AUTORISEES.md", "harnais/ROUTAGE_MODELES.md", "harnais/dispositif/prompt.sha256", "harnais/verrou.py", "harnais/controle_medical.py", "harnais/controle_langue.py", "harnais/audit_lot.py", "harnais/audit_sortie.py",
            ".claude/agents/redacteur.md", ".claude/agents/redacteur-phase-a.md", ".claude/agents/auditeur-medical.md",
            ".claude/agents/auditeur-conformite.md", ".claude/agents/mecanique.md", ".cache/aips/AipsDownload_20261008.xml", ".cache/g_in/g_tables.json"]
SCRIPTS = ["harnais/prompt_projet.py", "harnais/controle_lot.py", "harnais/aips_texte.py", "harnais/pubmed.py", "harnais/dispositif/veille.py"]
URLS = {"aips_refdata": "https://files.refdata.ch/simis-public-prod/MedicinalDocuments/8b471836624c4402a592ec8fe64c736f-fr.html",
        "pubmed": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi?retmode=json"}
_cc = {}
def local():
    c = {}
    c["fichiers"] = all((R / f).exists() for f in FICHIERS)
    p = R / "harnais/prompt_projet.py"
    c["prompt_lecture_seule"] = p.exists() and not (p.stat().st_mode & (stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH))
    try:
        sha = hashlib.sha256(subprocess.run([sys.executable, str(p), "--sha"], capture_output=True, text=True, timeout=5).stdout.strip().encode()).hexdigest()
        c["prompt_intact"] = subprocess.run([sys.executable, str(p), "--sha"], capture_output=True, text=True, timeout=5).stdout.strip() == (R / "harnais/dispositif/prompt.sha256").read_text().strip()
    except Exception: c["prompt_intact"] = False
    ok = True
    for s in SCRIPTS:
        f = R / s; k = (s, f.stat().st_mtime if f.exists() else 0)
        if k not in _cc:
            try: py_compile.compile(str(f), doraise=True, cfile=str(C / "x.pyc")); _cc[k] = True
            except Exception: _cc[k] = False
        ok &= _cc[k]
    c["scripts_compilent"] = ok
    import re
    c["lecons_max5"] = all(len(re.findall(r"^\s*(?:\d+\.|-)\s+\*\*", (R / "harnais/LECONS" / f).read_text(), re.M)) <= 5 for f in os.listdir(R / "harnais/LECONS")) if (R / "harnais/LECONS").exists() else False
    c["agents_modeles"] = all("model:" in (R / f".claude/agents/{a}.md").read_text() for a in ("redacteur", "redacteur-phase-a", "auditeur-medical", "auditeur-conformite", "mecanique"))
    return c
def reseau():
    c = {}
    for n, u in URLS.items():
        try: c["reseau_" + n] = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=10).status == 200
        except Exception: c["reseau_" + n] = False
    return c
def passage(avec_reseau, prec):
    c = local(); c.update(reseau() if avec_reseau else {k: v for k, v in prec.items() if k.startswith("reseau_")})
    return c
if __name__ == "__main__":
    once = "--once" in sys.argv; prec = {}; n = 0
    while True:
        c = passage(once or n % 30 == 0, prec); prec = c; n += 1
        e = {"t": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "tick": n, "ok": all(c.values()), "controles": c}
        (C / "etat.json").write_text(json.dumps(e, ensure_ascii=False))
        if not e["ok"]: open(C / "veille.log", "a").write(json.dumps(e, ensure_ascii=False) + "\n")
        if once: print(json.dumps(e, ensure_ascii=False)); sys.exit(0 if e["ok"] else 1)
        time.sleep(1)

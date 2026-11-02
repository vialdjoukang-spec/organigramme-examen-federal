#!/usr/bin/env python3
"""Macrophage — éboueur de fichiers inutiles (Vial, 28.10.2026). Contrat interne ultra bref :
  1. DÉTECTE seulement les fichiers répondant aux CRITÈRES D'INUTILITÉ (injectés ci-dessous par l'orchestrateur).
  2. NE DÉTRUIT QUE ce que le SIGNAL nomme (.cache/brain/macrophage_signal.json, écrit par l'orchestrateur, expire).
  3. S'ARRÊTE et se désactive (.cache/brain/macrophage.off) dès qu'une cible touche ou contient une ZONE UTILE.
  python3 harnais/brain/macrophage.py             patrouille : rapport des cibles (aucune destruction)
  python3 harnais/brain/macrophage.py --signal    l'orchestrateur signe : toutes les cibles détectées ce jour (heures de validité : --h 2)
  python3 harnais/brain/macrophage.py --detruire  détruit les cibles détectées ET signées ; jamais une zone utile
  python3 harnais/brain/macrophage.py --reveiller lève la désactivation après revue humaine"""
import json, shutil, subprocess, sys, time
from pathlib import Path
R = Path(__file__).resolve().parents[2]
SIG, OFF = R / ".cache/brain/macrophage_signal.json", R / ".cache/brain/macrophage.off"
# ZONES UTILES (circonscrites par l'orchestrateur) : rien dedans, rien qui les contienne, ne se détruit jamais.
ZONES_UTILES = ["LOT_Claude_Finaux", "harnais", "tools", "data", "audit", "docs", "tests", "assets", "skills", "qa", "gestes", "journal",
                "PROMPT_Casern", "veille", "nc", "orig", "lot en cours de production", ".github", ".claude", ".cursor",
                "essai_flash", "essai_parallele", "essai_lot001", "essai_lot002", "essai_lot003", "essai_lot004", ".cache/aips"]
RACINE_UTILE = {"AGENTS.md", "CATALOGUE.md", "CLAUDE.md", "CONTINUATION.md", "ETAT.json", "ETAT.md", "HANDOFF.md", "MESSAGE_CHAT_CLAUDE_CODE.md",
                "NETTOYAGE.md", "PROCHAINE_ACTION.md", "README.md", "app_v2.html", "progres.html"}
# CRITÈRES D'INUTILITÉ : (nom, test sur le chemin relatif)
BROUILLONS = (".pyc", ".tmp", ".bak", ".orig", ".whl", ".swp")
CRITERES = [
    ("bytecode", lambda p: "__pycache__" in p.parts),
    ("brouillon", lambda p: p.suffix in BROUILLONS or p.name.endswith("~") or p.name == ".DS_Store" or p.name.lower().startswith(("brouillon", "draft"))),
    ("journal_perime", lambda p: p.parts[:3] == (".cache", "brain", "circuit") and time.time() - p.stat().st_mtime > 24 * 3600),
    ("scratch_g14", lambda p: p.parts[:2] == (".cache", "test_g14")),
]
def dans_zone(rel):
    """Vrai si la cible est dans une zone utile OU si elle en contient une (parent) : proximité interdite."""
    for z in ZONES_UTILES:
        zp = Path(z)
        if rel == zp or zp in rel.parents or rel in zp.parents: return True
    return rel.parent == Path(".") and rel.name in RACINE_UTILE
def cibles():
    sortie, proches = [], []
    for p in R.rglob("*"):
        if ".git" in p.parts or not (p.is_file() or p.is_dir()): continue
        rel = p.relative_to(R)
        for nom, test in CRITERES:
            try: ok = test(rel)
            except OSError: ok = False
            if ok:
                # un __pycache__ est inutile même dans une zone utile (bytecode régénérable) ; tout le reste respecte les zones
                (sortie if nom == "bytecode" or not dans_zone(rel) else proches).append((str(rel), nom)); break
    return sorted(set(sortie)), sorted(set(proches))
def main(a):
    if "--reveiller" in a: OFF.unlink(missing_ok=True); print("macrophage réveillé"); return 0
    if OFF.exists(): print("macrophage DÉSACTIVÉ (proximité des zones utiles) : revue humaine puis --reveiller"); return 3
    cs, proches = cibles()
    for rel, nom in cs[:60]: print(f"cible [{nom}] {rel}")
    if len(cs) > 60: print(f"… {len(cs) - 60} autres")
    for rel, nom in proches[:10]: print(f"zone utile (épargnée) [{nom}] {rel}")
    print(f"# {len(cs)} cible(s) · {len(proches)} épargnée(s) en zone utile")
    if "--signal" in a:
        h = float(a[a.index("--h") + 1]) if "--h" in a else 2.0
        SIG.parent.mkdir(parents=True, exist_ok=True)
        SIG.write_text(json.dumps(dict(expire=time.time() + h * 3600, detruire=[r for r, _ in cs]), ensure_ascii=False)); print(f"signal signé pour {h} h : {len(cs)} cible(s)")
    if "--detruire" in a:
        if not SIG.exists(): print("aucun signal : rien n'est détruit"); return 0
        s = json.loads(SIG.read_text())
        if time.time() > s["expire"]: print("signal expiré : rien n'est détruit"); return 0
        autorise, n = set(s["detruire"]), 0
        for rel, nom in cs:
            if rel not in autorise: continue
            r = Path(rel)
            if nom != "bytecode" and dans_zone(r):                       # garde finale (ceinture et bretelles) : désactivation
                OFF.parent.mkdir(parents=True, exist_ok=True); OFF.write_text(rel); print("PROXIMITÉ zone utile :", rel, "→ macrophage désactivé"); return 3
            p = R / rel
            if p.is_dir(): shutil.rmtree(p, ignore_errors=True)
            elif p.exists(): p.unlink()
            n += 1
        SIG.unlink(missing_ok=True); print(f"# {n} fichier(s) détruit(s) ; signal consommé")
    return 0
if __name__ == "__main__": sys.exit(main(sys.argv[1:]))

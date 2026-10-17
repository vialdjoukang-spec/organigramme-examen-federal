#!/usr/bin/env python3
"""Génère CATALOGUE.md : scripts et automates gratuits, workflows, skills du dépôt, MCP et droits.

  catalogue.py [--dry-run]

Les sections que seul Codex connaît (ses serveurs MCP, ses skills, ses connecteurs) portent la marque
« À COMPLÉTER PAR CODEX » si l'outil ne peut pas les lire lui-même ; tools/porte.py refuse l'Étape 1
tant qu'une marque reste. Codex remplace la marque par la liste réelle, puis la présente à Vial
(ou dans PROCHAINE_ACTION.md) avant de commencer.
"""
import glob, os, re, shutil, subprocess, sys

RACINE = os.environ.get("OEF_REPO") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARQUE = "À COMPLÉTER PAR CODEX"


def premiere_ligne(f):
    try:
        t = open(f, encoding="utf-8", errors="replace").read(4000)
    except OSError:
        return ""
    m = re.search(r'"""\s*(.+)', t) or re.search(r"^#\s+(?!!)(.+)$", t, re.M)
    return (m.group(1).strip() if m else "").replace("|", "/")[:140]


def sortie(cmd):
    if not shutil.which(cmd[0]):
        return None
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return (r.stdout or r.stderr).strip() or None
    except (OSError, subprocess.TimeoutExpired):
        return None


def main():
    L = ["# CATALOGUE · outils gratuits, automates, MCP et skills (Étape 0)", "",
         "Généré par `python3 tools/catalogue.py`, puis complété par Codex. À présenter avant toute étape de contenu.", "",
         "## 1. Scripts du dépôt (gratuits, déterministes)", "", "| Script | Rôle |", "|---|---|"]
    for f in sorted(glob.glob(os.path.join(RACINE, "tools", "**", "*.py"), recursive=True) +
                    glob.glob(os.path.join(RACINE, "tools", "**", "*.sh"), recursive=True)):
        r = os.path.relpath(f, RACINE)
        if "/patches/" in r or "__pycache__" in r:
            continue
        L.append(f"| `{r}` | {premiere_ligne(f)} |")
    L += ["", f"Patches rejouables : {len(glob.glob(os.path.join(RACINE, 'tools', 'patches', '*.py')))} dans `tools/patches/` (skill ssp-patch).", "",
          "## 2. Automates GitHub Actions (gratuits, dépôt public)", "", "| Workflow | Rôle |", "|---|---|"]
    for f in sorted(glob.glob(os.path.join(RACINE, ".github", "workflows", "*.yml"))):
        L.append(f"| `{os.path.relpath(f, RACINE)}` | {premiere_ligne(f)} |")
    L += ["", "## 3. Outils système gratuits", ""]
    for c in ("git", "gh", "python3", "node", "npx", "jq", "flock", "pdftotext", "curl", "codex", "crontab"):
        L.append(f"- `{c}` : {'présent' if shutil.which(c) else 'absent'}")
    L += ["", "## 4. Skills du dépôt (`docs/skills/`)", ""]
    for f in sorted(glob.glob(os.path.join(RACINE, "docs", "skills", "*", "SKILL.md"))):
        t = open(f, encoding="utf-8", errors="replace").read(1500)
        m = re.search(r"^description:\s*(?:>-?|\|-?)?\s*\n?((?:[ \t]+.+\n?)+|.+)", t, re.M)
        d = re.sub(r"\s+", " ", m.group(1)).strip() if m else premiere_ligne(f)
        L.append(f"- `{os.path.basename(os.path.dirname(f))}` : {d[:160]}")
    L += ["- Propositions automatiques : `docs/skills/PROPOSITIONS.md` (`python3 tools/propose_skills.py`).", "",
          "## 5. Serveurs MCP et connecteurs de Codex", ""]
    mcp = sortie(["codex", "mcp", "list"])
    L += (["```", mcp, "```"] if mcp else [f"{MARQUE} : lancer `codex mcp list` (ou lire `~/.codex/config.toml`, section `[mcp_servers]`) et lister chaque serveur avec son usage ici."])
    L += ["", "## 6. Skills et outils propres à Codex", "",
          f"{MARQUE} : lister les skills/outils intégrés de Codex (recherche web, navigateur, exécution, images…) et dire lesquels servent à quelle étape.", "",
          "## 7. Droits de fusion-publication", ""]
    droits = sortie(["bash", os.path.join(RACINE, "tools", "file_fusion.sh"), "--droits"])
    L += (["```", droits, "```", "Attendu : admin=true, auto_merge=true, merge_commit=true ; protection : garde, html, tests, visuel, strict."]
          if droits and '"admin"' in droits else [f"{MARQUE} : `bash tools/file_fusion.sh --droits` a échoué ; configurer gh (voir Étape 0.d)."])
    L += ["", "## 8. Modèle des tâches répétitives", "",
          "Ordre de Vial : toute tâche répétitive utilise **GPT 6 Luna** (`gpt-6-luna`). Sinon : le modèle le moins cher disponible, noté dans ETAT.md.", ""]
    out = "\n".join(L)
    if "--dry-run" in sys.argv:
        print(out)
    else:
        open(os.path.join(RACINE, "CATALOGUE.md"), "w", encoding="utf-8").write(out)
        print(f"CATALOGUE.md écrit ({out.count(MARQUE)} section(s) à compléter par Codex)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

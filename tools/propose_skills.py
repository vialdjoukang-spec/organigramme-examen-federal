#!/usr/bin/env python3
"""Proposition automatique de skills (gratuit, déterministe).

Repère les commandes et les tâches répétitives dans journal/*.md, HANDOFF.md, CONTINUATION.md,
.etat_local/*.log (veille, Codex) et `git log`, puis écrit les candidats non encore couverts
par un skill de docs/skills/ dans docs/skills/PROPOSITIONS.md (squelette prêt à compléter).

  propose_skills.py [--seuil 3] [--commits 400] [--dry-run]

Une commande « répétitive » = même forme normalisée (chiffres, SHA, numéros de PR, chemins
de lot remplacés) vue au moins --seuil fois. Une tâche répétitive = même début de sujet de
commit (3 premiers mots normalisés) vu au moins --seuil fois.
"""
import collections, glob, os, re, subprocess, sys

RACINE = os.environ.get("OEF_REPO") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SORTIE = os.path.join(RACINE, "docs", "skills", "PROPOSITIONS.md")
CMD_RE = re.compile(r"`((?:python3|bash|gh|git|flock|node|npx|tools/)[^`]{3,160})`")
LIGNE_CMD_RE = re.compile(r"^\s*(?:\$ )?((?:python3|bash|gh|git|flock) [^\n]{3,160})$", re.M)


def arg(nom, defaut):
    if nom in sys.argv:
        i = sys.argv.index(nom)
        if i + 1 < len(sys.argv):
            return type(defaut)(sys.argv[i + 1])
    return defaut


def normaliser(c):
    c = c.strip().rstrip(";")
    c = re.sub(r"\b[0-9a-f]{7,40}\b", "<sha>", c)
    c = re.sub(r"#?\b\d+\b", "<n>", c)
    c = re.sub(r"\b[SGOF]\d+(?:\.\d+)*\b", "<ssp>", c)
    c = re.sub(r"(/workspace/)[\w.-]+", r"\1<wt>", c)
    c = re.sub(r"\"[^\"]*\"|'[^']*'", "<txt>", c)
    return re.sub(r"\s+", " ", c)


def textes():
    fichiers = glob.glob(os.path.join(RACINE, "journal", "*.md")) + [
        os.path.join(RACINE, "HANDOFF.md"), os.path.join(RACINE, "CONTINUATION.md")]
    fichiers += glob.glob(os.path.join(RACINE, ".etat_local", "*.log"))
    for f in fichiers:
        try:
            yield f, open(f, encoding="utf-8", errors="replace").read()
        except OSError:
            pass


def sujets_commits(n):
    r = subprocess.run(["git", "-C", RACINE, "log", f"-n{n}", "--no-merges", "--format=%s"],
                       capture_output=True, text=True)
    return [l for l in r.stdout.splitlines() if l.strip()]


def skills_existants():
    corpus = ""
    for f in glob.glob(os.path.join(RACINE, "docs", "skills", "*", "SKILL.md")) + \
             glob.glob(os.path.join(RACINE, "docs", "skills", "*.md")):
        if not f.endswith("PROPOSITIONS.md"):
            corpus += open(f, encoding="utf-8", errors="replace").read()
    return corpus


def main():
    seuil = arg("--seuil", 3)
    cmds, ou = collections.Counter(), collections.defaultdict(set)
    for f, t in textes():
        for m in list(CMD_RE.finditer(t)) + list(LIGNE_CMD_RE.finditer(t)):
            k = normaliser(m.group(1))
            cmds[k] += 1
            ou[k].add(os.path.relpath(f, RACINE))
    taches = collections.Counter()
    for s in sujets_commits(arg("--commits", 400)):
        mots = re.findall(r"[\wÀ-ÿ'’-]+", normaliser(s).lower())[:3]
        if len(mots) == 3:
            taches[" ".join(mots)] += 1
    corpus = skills_existants()
    prop_cmd = [(k, v) for k, v in cmds.most_common() if v >= seuil and k.split(" <")[0] not in corpus]
    prop_tache = [(k, v) for k, v in taches.most_common() if v >= seuil]
    lignes = ["# Propositions de skills (générées par tools/propose_skills.py)", "",
              "Relancer : `python3 tools/propose_skills.py`. Codex lit ce fichier à la fin de chaque étape : "
              "chaque candidat utile devient `docs/skills/<nom>/SKILL.md` (procédure courte, commandes exactes, pièges), "
              "les autres sont rayés avec leur motif.", "",
              f"Seuil : {seuil} occurrences. Corpus : journal/*.md, HANDOFF.md, CONTINUATION.md, .etat_local/*.log, git log.", "",
              "## Commandes répétitives non couvertes par un skill", ""]
    if prop_cmd:
        lignes += ["| Vu | Commande normalisée | Où | Skill proposé |", "|---|---|---|---|"]
        for k, v in prop_cmd[:40]:
            nom = "ssp-" + re.sub(r"[^a-z0-9]+", "-", k.split()[1 if len(k.split()) > 1 else 0].split("/")[-1].lower()).strip("-")[:30]
            kk = k.replace("|", "\\|")
            lignes.append(f"| {v} | `{kk}` | {', '.join(sorted(ou[k]))[:80]} | `{nom}` |")
    else:
        lignes.append("Aucune.")
    lignes += ["", "## Tâches répétitives (sujets de commit)", ""]
    if prop_tache:
        lignes += ["| Vu | Début de sujet | Action |", "|---|---|---|"]
        lignes += [f"| {v} | {k} | automatiser par script ou skill ; modèle GPT 6 Luna (ordre de Vial) |" for k, v in prop_tache[:30]]
    else:
        lignes.append("Aucune.")
    lignes += ["", "## Squelette d'un skill", "", "```markdown", "---", "name: ssp-<nom>",
               "description: <quand l'utiliser, en une phrase>", "---", "# <Titre>",
               "1. Préalable : <worktree, fichiers lus>", "2. Commandes : <exactes, rejouables>",
               "3. Contrôle : <tests, --check>", "4. Pièges : <liste>", "```", ""]
    out = "\n".join(lignes)
    if "--dry-run" in sys.argv:
        print(out)
        return 0
    os.makedirs(os.path.dirname(SORTIE), exist_ok=True)
    open(SORTIE, "w", encoding="utf-8").write(out)
    print(f"{len(prop_cmd)} commande(s), {len(prop_tache)} tâche(s) → {os.path.relpath(SORTIE, RACINE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

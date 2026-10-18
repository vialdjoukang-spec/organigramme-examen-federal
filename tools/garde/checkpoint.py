#!/usr/bin/env python3
"""Point de contrôle de chaque PR (R15) · .github/workflows/checkpoint.yml.

  checkpoint.py --inventaire                 affiche les automates actifs (début de chaque session Codex)
  checkpoint.py [--base REF] [--corps F]     contrôle la PR courante (CI : GITHUB_EVENT_PATH)

Échecs (avec la correction exacte) :
  A. corps de PR sans section « Automates actifs » listant scripts/skills/MCP existants ;
  B. ETAT.json déclare finie une étape en boucle (etapes.json boucle=true) sans aucun changement de données de contenu ;
  C. dose nouvelle dans data/ck/mono/*.json ou data/ck/prev.json sans dose_ref vers une ligne de
     data/ck/doses_ch.json qui la contient, ni « À vérifier ».
Exemptions : étiquette `infra`, branche infra/garde-fous.
"""
import argparse, glob, json, os, re, subprocess, sys

ICI = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, os.path.join(ROOT, "tools", "audit"))
CFG = json.load(open(os.path.join(ICI, "config.json"), encoding="utf-8"))


def git(*a):
    r = subprocess.run(["git", "-C", ROOT, *a], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


# ---------------------------------------------------------------- inventaire
def connus():
    noms = set()
    for p in glob.glob(os.path.join(ROOT, "tools", "**", "*"), recursive=True):
        if os.path.isfile(p):
            r = os.path.relpath(p, ROOT)
            noms |= {r, os.path.basename(r), os.path.splitext(os.path.basename(r))[0]}
    for p in glob.glob(os.path.join(ROOT, "docs", "skills", "*")) + glob.glob(os.path.join(ROOT, ".github", "workflows", "*.yml")):
        r = os.path.relpath(p, ROOT)
        noms |= {r, os.path.basename(r), os.path.splitext(os.path.basename(r))[0]}
    cat = open(os.path.join(ROOT, "CATALOGUE.md"), encoding="utf-8").read() if os.path.exists(os.path.join(ROOT, "CATALOGUE.md")) else ""
    noms |= set(re.findall(r"`([^`\s]+)`", cat))
    return {n.lower() for n in noms}, cat


def inventaire():
    print("# Automates actifs (R15) — à recopier dans la section « Automates actifs » de chaque PR\n")
    print("## Workflows GitHub Actions (permanents, gratuits, indépendants de tout PC)")
    for p in sorted(glob.glob(os.path.join(ROOT, ".github", "workflows", "*.yml"))):
        t = open(p, encoding="utf-8").read()
        cron = re.findall(r"cron:\s*'([^']+)'", t)
        print(f"- `{os.path.relpath(p, ROOT)}`" + (f" · cron {', '.join(cron)}" if cron else ""))
    print("\n## Garde-fous R15 (tools/garde/, seuils en minutes dans config.json)")
    for k, v in CFG.items():
        if k.endswith("_min") or k.endswith("_vial") or k.endswith("passage"):
            print(f"- {k} = {v}")
    print("\n## Skills (docs/skills/)")
    for p in sorted(glob.glob(os.path.join(ROOT, "docs", "skills", "*"))):
        if os.path.isdir(p):
            print(f"- `{os.path.basename(p)}`")
    print("\n## Scripts clés")
    for s in ("tools/porte.py", "tools/jauge/binomes.py", "tools/prev_build.py", "tools/mono_build.py", "tools/doses_check.py",
              "tools/aips_verbatim.py", "tools/lyncee.py", "tools/audit/niveau1.py", "tools/file_fusion.sh",
              "tools/garde/progres.py", "tools/garde/checkpoint.py", "tools/garde/recyclage.py", "tools/garde/appel.py",
              "tools/garde/fin.py"):
        if os.path.exists(os.path.join(ROOT, s)):
            print(f"- `{s}`")
    print("\n## MCP : voir CATALOGUE.md § MCP (n'en citer que ceux réellement branchés dans la session).")


# ---------------------------------------------------------------- A. section Automates actifs
def section_automates(corps):
    lignes = (corps or "").splitlines()
    for i, l in enumerate(lignes):
        if re.search(r"automates?\s+actifs?", l, re.I):
            bloc = []
            for x in lignes[i + 1:]:
                if re.match(r"\s*#{1,6}\s", x):
                    break
                bloc.append(x)
            return [x for x in bloc if re.match(r"\s*([-*+]|\d+[.)])\s+", x)]
    return None


def noms_puces(puces):
    out = []
    for p in puces:
        b = re.findall(r"`([^`]+)`", p)
        if b:
            out += [x.strip() for x in b]
        else:
            m = re.match(r"\s*(?:[-*+]|\d+[.)])\s+([^\s:—–,(]+)", p)
            if m:
                out.append(m.group(1))
    return out


def ctrl_automates(corps, F):
    puces = section_automates(corps)
    if puces is None or not puces:
        F.append("A · Section « Automates actifs » absente ou vide dans le corps de la PR.\n"
                 "  Correction : lance `python tools/garde/checkpoint.py --inventaire`, puis ajoute au corps de la PR :\n"
                 "    ## Automates actifs\n    - `tools/garde/progres.py`\n    - `ssp-audit-medical` (skill)\n"
                 "  (une puce par script/skill/MCP réellement utilisé, nom entre accents graves).")
        return
    ok, _ = connus()
    inconnus = [n for n in noms_puces(puces)
                if n.lower() not in ok and os.path.basename(n).lower() not in ok and not n.lower().startswith("mcp")]
    mcp = [n for n in noms_puces(puces) if n.lower().startswith("mcp")]
    cat = open(os.path.join(ROOT, "CATALOGUE.md"), encoding="utf-8").read().lower() if os.path.exists(os.path.join(ROOT, "CATALOGUE.md")) else ""
    inconnus += [n for n in mcp if n.lower().split(":", 1)[-1].strip() not in cat]
    if inconnus:
        F.append("A · Automates cités qui n'existent ni dans tools/, ni dans docs/skills/, ni dans CATALOGUE.md : "
                 + ", ".join(f"`{n}`" for n in inconnus) + ".\n"
                 "  Correction : corrige le nom (chemin exact, ex. `tools/prev_build.py`), ou ajoute l'outil au dépôt "
                 "et à CATALOGUE.md (`python3 tools/catalogue.py`), ou retire la puce. Pour un MCP : `MCP: <nom du CATALOGUE>`.")


# ---------------------------------------------------------------- B. fausse fin d'étape
def json_at(ref, path):
    try:
        return json.loads(git("show", f"{ref}:{path}") or "null")
    except json.JSONDecodeError:
        return None


def ctrl_etat(base, fichiers, F):
    if "ETAT.json" not in fichiers:
        return
    b, h = json_at(base, "ETAT.json") or {}, json_at("HEAD", "ETAT.json") or {}
    etapes = {e["n"]: e for e in (json_at("HEAD", "tools/etapes.json") or {}).get("etapes", [])}
    nb = b.get("etape_courante")
    if not isinstance(nb, int) or not etapes.get(nb, {}).get("boucle"):
        return
    finie = (h.get("etape_courante") == nb and h.get("statut") == "terminee") or (isinstance(h.get("etape_courante"), int) and h["etape_courante"] > nb)
    contenu = [f for f in fichiers if any(f.startswith(p) for p in CFG["chemins_contenu"])]
    if finie and not contenu:
        F.append(f"B · ETAT.json déclare finie l'étape {nb} (« {etapes[nb]['titre'][:60]} »), qui est une BOUCLE, "
                 f"sans aucun changement de données de contenu ({', '.join(CFG['chemins_contenu'])}).\n"
                 f"  Un relevé seul ne termine jamais une étape en boucle (R15). Correction : remets dans ETAT.json "
                 f"\"etape_courante\": {nb}, \"statut\": \"en_cours\" et rédige le lot suivant (prévalences/monographies) "
                 f"dans cette PR ou une PR de contenu ; la fin vient du critère automatique (`python3 tools/porte.py etat`).")


# ---------------------------------------------------------------- C. doses
def ctrl_doses(base, fichiers, F):
    try:
        from niveau1 import DOSE, STATUT_AV, dose_norm
        from ck_common import strip_tags
    except Exception:
        return
    table = {d["id"]: d for d in (json_at("HEAD", "data/ck/doses_ch.json") or []) if isinstance(d, dict)}

    def doses_entree(v):
        out = []
        for k, t in (v.items() if isinstance(v, dict) else []):
            if k in ("src", "lu", "id", "url", "dose_ref", "n") or not isinstance(t, str):
                continue
            if STATUT_AV.lower() in t.lower() or "à vérifier" in t.lower():
                continue
            out += [dose_norm(m.group(0)) for m in DOSE.finditer(strip_tags(t))]
        return out

    def entrees(ref, path):
        d = json_at(ref, path)
        if not isinstance(d, dict):
            return {}
        if path.endswith("prev.json"):
            return {f"{c}#{e.get('i')}": e for c, v in d.items() if isinstance(v, dict) for e in v.get("items", []) if isinstance(e, dict)}
        return {k: v for k, v in d.items() if not k.startswith("_")}

    for path in [f for f in fichiers if re.match(r"data/ck/(mono/[^/]+\.json|prev\.json)$", f)]:
        B, H = entrees(base, path), entrees("HEAD", path)
        for k, v in H.items():
            if isinstance(v, dict) and v.get("statut") == STATUT_AV:
                continue
            nouv = [d for d in doses_entree(v) if d not in doses_entree(B.get(k, {}))]
            if not nouv:
                continue
            refs = v.get("dose_ref")
            refs = refs if isinstance(refs, list) else [refs] if refs else []
            txt = " ".join(dose_norm(table[r]["dose"]) for r in refs if r in table)
            manq = [d for d in nouv if not re.search(r"(?<![\d.])" + re.escape(d) + r"(?![\d])", txt)]
            if manq:
                F.append(f"C · {path} « {k} » : dose(s) nouvelle(s) {', '.join(manq)} sans ligne correspondante dans "
                         f"data/ck/doses_ch.json.\n  Correction : ajoute la ligne AIPS verbatim (`python3 tools/aips_verbatim.py`, "
                         f"puis `python tools/doses_check.py`) et mets \"dose_ref\": \"<id>\" sur l'entrée ; sinon écris "
                         f"« À vérifier » à la place du chiffre. Jamais de dose hors AIPS suisse.")


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--inventaire", action="store_true")
    a.add_argument("--base", default=os.environ.get("CHECKPOINT_BASE", "origin/main"))
    a.add_argument("--corps", help="fichier contenant le corps de la PR (sinon GITHUB_EVENT_PATH)")
    x = a.parse_args()
    if x.inventaire:
        return inventaire()
    ev = {}
    if os.environ.get("GITHUB_EVENT_PATH") and os.path.exists(os.environ["GITHUB_EVENT_PATH"]):
        ev = json.load(open(os.environ["GITHUB_EVENT_PATH"], encoding="utf-8")).get("pull_request") or {}
    corps = open(x.corps, encoding="utf-8").read() if x.corps else (ev.get("body") or "")
    labels = {l["name"] for l in ev.get("labels", [])}
    branche = (ev.get("head") or {}).get("ref") or git("rev-parse", "--abbrev-ref", "HEAD").strip()
    if "infra" in labels or branche == "infra/garde-fous":
        print(f"Checkpoint R15 : PR exemptée (étiquette infra ou branche {branche}).")
        return 0
    mb = git("merge-base", x.base, "HEAD").strip() or x.base
    fichiers = [f for f in git("diff", "--name-only", f"{mb}...HEAD").splitlines() if f]
    F = []
    ctrl_automates(corps, F)
    ctrl_etat(mb, fichiers, F)
    ctrl_doses(mb, fichiers, F)
    if F:
        print("ÉCHEC du checkpoint R15 (garde-fous de Vial). Corrige puis pousse :\n")
        print("\n\n".join(F))
        return 1
    print(f"Checkpoint R15 vert : automates déclarés, aucune fausse fin d'étape, doses adossées à l'AIPS ({len(fichiers)} fichiers).")
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)

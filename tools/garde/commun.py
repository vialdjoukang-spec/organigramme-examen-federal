#!/usr/bin/env python3
"""Garde-fous R15 · fonctions communes (zéro jeton, gratuit : GitHub Actions + gh CLI).

Jetons (variables d'environnement) :
  GH_TOKEN_CODEX : jeton qui écrit les « @codex » (secrets.AUTO_FUSION_TOKEN = compte de Vial,
                   seul capable de déclencher l'intégration GitHub de Codex) ; défaut GH_TOKEN.
  GH_TOKEN_BOT   : jeton qui mentionne @vialdjoukang-spec (GITHUB_TOKEN = github-actions[bot]) :
                   GitHub n'envoie pas de courriel à quelqu'un qui se mentionne lui-même.
  GARDE_SEC=1    : n'écrit rien sur GitHub (essai local), affiche seulement.
"""
import datetime as dt, json, os, subprocess, sys

ICI = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(ICI))
CFG = json.load(open(os.path.join(ICI, "config.json"), encoding="utf-8"))
REPO = os.environ.get("GH_REPO") or os.environ.get("GITHUB_REPOSITORY") or "vialdjoukang-spec/organigramme-examen-federal"
SEC = os.environ.get("GARDE_SEC") == "1"


def now():
    return dt.datetime.now(dt.timezone.utc)


def iso(t):
    return t.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse(s):
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00")) if s else None


def minutes_depuis(s, t=None):
    p = parse(s)
    return 1e9 if p is None else ((t or now()) - p).total_seconds() / 60


def git(*a, ok=True):
    r = subprocess.run(["git", "-C", ROOT, *a], capture_output=True, text=True)
    if r.returncode and not ok:
        raise SystemExit(r.stderr)
    return r.stdout.strip() if r.returncode == 0 else ""


def gh(*a, token=None, data=None, ok=True):
    env = dict(os.environ)
    if token:
        env["GH_TOKEN"] = token
    r = subprocess.run(["gh", *a], capture_output=True, text=True, env=env, input=data)
    if r.returncode:
        if not ok:
            raise RuntimeError(r.stderr.strip())
        sys.stderr.write(f"gh {' '.join(a[:3])} : {r.stderr.strip()[:300]}\n")
        return None
    return r.stdout


def api(path, token=None, method="GET", body=None, ok=True):
    a = ["api", "-X", method, path, "-H", "Accept: application/vnd.github+json"]
    if method == "GET" and "per_page" not in path:
        a.insert(3, "--paginate")
    if body is not None:
        a += ["--input", "-"]
    out = gh(*a, token=token, data=json.dumps(body) if body is not None else None, ok=ok)
    if not out:
        return None
    try:
        return json.loads(out)
    except json.JSONDecodeError:  # --paginate concatène les pages
        return json.loads("[" + out.replace("][", "],[") + "]") if out.startswith("[") else None


def tok_codex():
    return os.environ.get("GH_TOKEN_CODEX") or os.environ.get("GH_TOKEN")


def tok_bot():
    return os.environ.get("GH_TOKEN_BOT") or os.environ.get("GH_TOKEN")


def classer(fichiers):
    """contenu | releve | autre, selon les chemins modifiés."""
    if any(f.startswith(p) for f in fichiers for p in CFG["chemins_contenu"]):
        return "contenu"
    if fichiers and all(any(f.startswith(p) for p in CFG["chemins_releve"]) for f in fichiers):
        return "releve"
    return "autre"


def fichiers_pr(n):
    r = api(f"repos/{REPO}/pulls/{n}/files?per_page=100") or []
    return [f["filename"] for f in r]


# ---------------------------------------------------------------- fil « Pilote Codex »
def pilote(creer=True):
    """Numéro de la PR brouillon « Pilote Codex » (les « @codex » ne marchent que sur une PR)."""
    titre, br = CFG["pilote_titre"], CFG["pilote_branche"]
    for p in api(f"repos/{REPO}/pulls?state=open&per_page=100") or []:
        if p["title"] == titre or p["head"]["ref"] == br:
            return p["number"]
    if not creer or SEC:
        return None
    main = api(f"repos/{REPO}/git/ref/heads/main")["object"]["sha"]
    for t in (tok_codex(), tok_bot()):
        if api(f"repos/{REPO}/git/ref/heads/{br}", token=t) is None:
            api(f"repos/{REPO}/git/refs", token=t, method="POST", body={"ref": f"refs/heads/{br}", "sha": main})
            import base64
            api(f"repos/{REPO}/contents/veille/PILOTE.md", token=t, method="PUT", body={
                "message": "Pilote Codex : fil de relance (ne pas fusionner)", "branch": br,
                "content": base64.b64encode(PILOTE_MD.encode()).decode()})
        p = api(f"repos/{REPO}/pulls", token=t, method="POST", body={
            "title": titre, "head": br, "base": "main", "draft": True, "body": PILOTE_MD})
        if p:
            api(f"repos/{REPO}/issues/{p['number']}/labels", token=t, method="POST", body={"labels": ["infra"]})
            return p["number"]
    return None


PILOTE_MD = """# Pilote Codex · fil de relance automatique (R15) — NE PAS FUSIONNER

Fil unique où `garde-progres.yml` (toutes les 10 min, GitHub Actions, gratuit) écrit :
- `@codex …` : ordre de Vial de reprendre la rédaction quand le contenu ne bouge plus ;
- `@vialdjoukang-spec …` : seulement quand Vial doit intervenir (courriel GitHub).

Ordre de Vial : « Codex doit être libre, indépendant de tout PC ». Seuils : `tools/garde/config.json`.
"""


def commenter(n, texte, token):
    if SEC or n is None:
        print(f"[essai] commentaire #{n} :\n{texte}\n")
        return True
    return api(f"repos/{REPO}/issues/{n}/comments", token=token, method="POST", body={"body": texte}) is not None


# ---------------------------------------------------------------- état (branche garde/etat)
def lire_etat():
    br, f = CFG["etat_branche"], CFG["etat_fichier"]
    git("fetch", "-q", "origin", br)
    raw = git("show", f"origin/{br}:{f}")
    try:
        return json.loads(raw) if raw else {}
    except json.JSONDecodeError:
        return {}


def ecrire_etat(e):
    import base64
    br, f = CFG["etat_branche"], CFG["etat_fichier"]
    txt = json.dumps(e, ensure_ascii=False, indent=1) + "\n"
    if SEC:
        print(f"[essai] état non écrit :\n{txt}")
        return
    t = tok_bot()
    if api(f"repos/{REPO}/git/ref/heads/{br}", token=t) is None:
        main = api(f"repos/{REPO}/git/ref/heads/main", token=t)["object"]["sha"]
        api(f"repos/{REPO}/git/refs", token=t, method="POST", body={"ref": f"refs/heads/{br}", "sha": main})
    cur = api(f"repos/{REPO}/contents/{f}?ref={br}", token=t)
    body = {"message": f"garde : état {e.get('maj', '')}", "branch": br,
            "content": base64.b64encode(txt.encode()).decode()}
    if isinstance(cur, dict) and cur.get("sha"):
        body["sha"] = cur["sha"]
    api(f"repos/{REPO}/contents/{f}", token=t, method="PUT", body=body)


def resume(txt):
    print(txt)
    p = os.environ.get("GITHUB_STEP_SUMMARY")
    if p:
        open(p, "a", encoding="utf-8").write(txt + "\n")

#!/usr/bin/env python3
"""Compteur de consommation d'une passe Grok. Python standard, zéro appel de modèle.

  python3 grok-LOTS-html/outils/compteur_conso.py debut <LOT> <fichier> <poste>
  python3 grok-LOTS-html/outils/compteur_conso.py lu <chemin>
  python3 grok-LOTS-html/outils/compteur_conso.py web <url>
  python3 grok-LOTS-html/outils/compteur_conso.py fin <LOT> <fichier> <poste>
  python3 grok-LOTS-html/outils/compteur_conso.py bilan [LOT]
  python3 grok-LOTS-html/outils/compteur_conso.py retroactif [LOT]

Entre debut et fin (processus distincts : l'état est dans /tmp, hors dépôt) :
durée murale, fichiers déclarés lus, diff git du fichier, fenêtres, T x+y,
dossier evidence/, URLs journalisées, instantané /proc, variables d'usage
numériques de l'environnement. Champ null si la mesure n'a pas été obtenue.
Jetons = octets / 3,12, proxy o200k, toujours marqués estimation.
Une ligne JSON par fin ou par rétroactif dans connaissance/CONSO.jsonl.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ZH = ZoneInfo("Europe/Zurich")
FACTEUR = 3.12  # octets par jeton, proxy tiktoken o200k mesuré le 31.10.2026 ; estimation
SESSION = Path("/tmp/conso_grok_session.json")
RACINE = Path(__file__).resolve().parents[2]
JOURNAL = RACINE / "grok-LOTS-html/connaissance/CONSO.jsonl"
USAGE_MOTS = ("USAGE", "TOKEN", "CURSOR", "MODEL", "GROK", "OPENAI", "ANTHROPIC", "XAI")
SECRET_MOTS = ("KEY", "SECRET", "PASSWORD", "TOKEN", "AUTH", "COOKIE")


def maintenant() -> str:
    return datetime.now(ZH).isoformat(timespec="seconds")


def estimation(octets):
    if octets is None:
        return None
    return round(octets / FACTEUR, 1)


def charger_session() -> dict:
    if not SESSION.exists():
        return {}
    try:
        return json.loads(SESSION.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def sauver_session(s: dict) -> None:
    SESSION.write_text(json.dumps(s, ensure_ascii=False, indent=1), encoding="utf-8")


def cle(lot, fichier, poste) -> str:
    return f"{lot}|{fichier}|{poste}"


def git(*args) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=RACINE, capture_output=True)


def chemin_lecon(lot: str, fichier: str) -> Path | None:
    if fichier.endswith(".html"):
        p = Path(fichier)
        return p if p.is_absolute() else RACINE / p
    d = RACINE / "grok-LOTS-html" / lot
    if fichier in ("Phase_A", "Phase A"):
        return d / f"{lot}_Phase_A_V0.html"
    m = re.fullmatch(r"DX\.(\d+)", fichier)
    if m:
        return d / f"{lot}_Phase_B_V0_DX.{m.group(1)}.html"
    return None


def modele(poste: str) -> tuple[str | None, str | None]:
    for nom in ("GROK_MODEL", "CURSOR_MODEL", "MODEL"):
        if os.environ.get(nom):
            return os.environ[nom], "env:" + nom
    conf = RACINE / "grok-LOTS-html/ROUTAGE_GROK.json"
    try:
        postes = json.loads(conf.read_text(encoding="utf-8")).get("postes", {})
        m = (postes.get(poste) or {}).get("modele")
        if m:
            return m, "routage_config"
    except (OSError, json.JSONDecodeError):
        pass
    return None, None


def compteurs_env() -> dict | None:
    """Valeurs numériques seulement. Un secret n'est jamais copié."""
    out = {}
    for k, v in os.environ.items():
        ku = k.upper()
        if not any(s in ku for s in USAGE_MOTS):
            continue
        if any(s in ku for s in SECRET_MOTS):
            continue
        if re.fullmatch(r"-?\d+(?:[.,]\d+)?", v.strip()):
            out[k] = v.strip().replace(",", ".")
    return out or None


def instantane_vm() -> dict | None:
    try:
        mem = {}
        for ligne in Path("/proc/meminfo").read_text(encoding="utf-8").splitlines():
            clef, _, reste = ligne.partition(":")
            if clef in ("MemTotal", "MemAvailable", "MemFree"):
                mem[clef] = int(reste.strip().split()[0])
        rss = None
        for ligne in Path("/proc/self/status").read_text(encoding="utf-8").splitlines():
            if ligne.startswith("VmRSS:"):
                rss = int(ligne.split()[1])
        charge = Path("/proc/loadavg").read_text(encoding="utf-8").split()
        uptime = float(Path("/proc/uptime").read_text(encoding="utf-8").split()[0])
        return {
            "mem_total_kib": mem.get("MemTotal"),
            "mem_available_kib": mem.get("MemAvailable"),
            "mem_free_kib": mem.get("MemFree"),
            "vmrss_kib": rss,
            "loadavg_1_5_15": charge[:3] if len(charge) >= 3 else None,
            "cpu_count": os.cpu_count(),
            "uptime_s": uptime,
        }
    except (OSError, ValueError, IndexError):
        return None


def mesurer_html(path: Path) -> dict:
    if not path.is_file():
        return {"fenetres": None, "depliants": None, "x_octets": None, "y_octets": None, "T": None}
    sys.path.insert(0, str(RACINE / "harnais"))
    try:
        import taille_xy
    finally:
        sys.path.pop(0)
    m = taille_xy.mesurer(path.read_text(encoding="utf-8", errors="replace"))
    return {
        "fenetres": m.fen,
        "depliants": m.dep,
        "x_octets": m.x[1],
        "y_octets": m.y[1],
        "T": f"{m.x[1]/1000:.1f} + {m.y[1]/1000:.1f} Ko",
    }


def mesurer_texte(texte: str) -> dict:
    sys.path.insert(0, str(RACINE / "harnais"))
    try:
        import taille_xy
    finally:
        sys.path.pop(0)
    m = taille_xy.mesurer(texte)
    return {
        "fenetres": m.fen,
        "depliants": m.dep,
        "x_octets": m.x[1],
        "y_octets": m.y[1],
        "T": f"{m.x[1]/1000:.1f} + {m.y[1]/1000:.1f} Ko",
    }


def diff_travail(path: Path) -> int | None:
    rel = str(path.relative_to(RACINE)) if path.is_absolute() else str(path)
    r = git("diff", "HEAD", "--", rel)
    if r.returncode != 0:
        return None
    if r.stdout:
        return len(r.stdout)
    suivi = git("ls-files", "--error-unmatch", rel)
    if suivi.returncode != 0 and path.is_file():
        return path.stat().st_size
    return 0


def evidence(lot: str) -> dict:
    d = RACINE / "grok-LOTS-html" / lot / "evidence"
    if not d.is_dir():
        return {"evidence_fichiers": None, "evidence_octets": None}
    fichiers = [p for p in d.iterdir() if p.is_file()]
    return {"evidence_fichiers": len(fichiers), "evidence_octets": sum(p.stat().st_size for p in fichiers)}


def lectures(chemins: list[str]) -> dict:
    details = []
    total = 0
    manquant = False
    for c in chemins:
        p = Path(c)
        if not p.is_absolute():
            p = RACINE / c
        if p.is_file():
            n = p.stat().st_size
            total += n
            details.append({"chemin": c, "octets": n})
        else:
            manquant = True
            details.append({"chemin": c, "octets": None})
    return {
        "lus": details,
        "octets_lus": None if manquant and not details else total if details else 0,
        "jetons_lus_est": estimation(total if details and not manquant else (total if details else 0)),
    }


def ecrire_ligne(obj: dict) -> None:
    JOURNAL.parent.mkdir(parents=True, exist_ok=True)
    with JOURNAL.open("a", encoding="utf-8") as f:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")


def cmd_debut(lot, fichier, poste) -> int:
    s = charger_session()
    s[cle(lot, fichier, poste)] = {
        "lot": lot,
        "fichier": fichier,
        "poste": poste,
        "debut": maintenant(),
        "lus": [],
        "webs": [],
        "vm_debut": instantane_vm(),
    }
    sauver_session(s)
    print("début", lot, fichier, poste, s[cle(lot, fichier, poste)]["debut"])
    return 0


def session_ouverte() -> tuple[str, dict] | None:
    s = charger_session()
    if len(s) == 1:
        k = next(iter(s))
        return k, s
    return None


def cmd_lu(chemin: str) -> int:
    trouve = session_ouverte()
    if not trouve:
        print("aucune passe ouverte, ou plusieurs : lancez debut d'abord", file=sys.stderr)
        return 2
    k, s = trouve
    s[k]["lus"].append(chemin)
    sauver_session(s)
    print("lu", chemin)
    return 0


def cmd_web(url: str) -> int:
    trouve = session_ouverte()
    if not trouve:
        print("aucune passe ouverte, ou plusieurs : lancez debut d'abord", file=sys.stderr)
        return 2
    k, s = trouve
    s[k]["webs"].append({"url": url, "horodatage": maintenant()})
    sauver_session(s)
    print("web", url)
    return 0


def cmd_fin(lot, fichier, poste) -> int:
    s = charger_session()
    k = cle(lot, fichier, poste)
    ouv = s.get(k)
    if not ouv:
        print("passe inconnue (debut manquant)", file=sys.stderr)
        return 2
    fin = maintenant()
    try:
        duree = (datetime.fromisoformat(fin) - datetime.fromisoformat(ouv["debut"])).total_seconds()
    except ValueError:
        duree = None
    path = chemin_lecon(lot, fichier)
    html = mesurer_html(path) if path else {"fenetres": None, "depliants": None, "x_octets": None, "y_octets": None, "T": None}
    diff = diff_travail(path) if path else None
    lus = lectures(ouv.get("lus") or [])
    ev = evidence(lot)
    mod, src = modele(poste)
    ligne = {
        "horodatage": fin,
        "retroactif": False,
        "lot": lot,
        "fichier": fichier,
        "poste": poste,
        "modele": mod,
        "modele_source": src,
        "debut": ouv["debut"],
        "fin": fin,
        "duree_s": duree,
        "octets_lus": lus["octets_lus"],
        "jetons_lus_est": lus["jetons_lus_est"],
        "facteur_octets_par_jeton": FACTEUR,
        "jetons_proxy": "o200k estimation octets/3.12",
        "lus": lus["lus"],
        "octets_diff_git": diff,
        "jetons_ecrits_est": estimation(diff),
        "octets_fichier": path.stat().st_size if path and path.is_file() else None,
        **html,
        **ev,
        "web": ouv.get("webs") or [],
        "web_n": len(ouv.get("webs") or []),
        "vm_fin": instantane_vm(),
        "vm_debut": ouv.get("vm_debut"),
        "compteurs_usage_env": compteurs_env(),
    }
    ecrire_ligne(ligne)
    del s[k]
    sauver_session(s)
    print(json.dumps({k: ligne[k] for k in ("fichier", "duree_s", "T", "fenetres", "octets_diff_git", "jetons_lus_est")}, ensure_ascii=False))
    return 0


def blob(commit: str, rel: str) -> str | None:
    r = git("show", f"{commit}:{rel}")
    if r.returncode != 0:
        return None
    return r.stdout.decode("utf-8", errors="replace")


def cmd_retroactif(lot: str, jusqua: int = 7) -> int:
    n = 0
    for i in range(1, jusqua + 1):
        nom = f"DX.{i}"
        rel = f"grok-LOTS-html/{lot}/{lot}_Phase_B_V0_{nom}.html"
        r = git("log", "-2", "--format=%H%x09%cI", "--", rel)
        if r.returncode != 0 or not r.stdout.strip():
            ecrire_ligne({
                "horodatage": maintenant(), "retroactif": True, "lot": lot, "fichier": nom,
                "poste": "redacteur", "modele": None, "modele_source": None,
                "erreur": "aucun commit", "duree_s": None, "octets_diff_git": None,
                "fenetres": None, "depliants": None, "x_octets": None, "y_octets": None, "T": None,
                "compteurs_usage_env": None, "vm_fin": None, "web": None, "lus": None,
                "octets_lus": None, "jetons_lus_est": None, "jetons_ecrits_est": None,
            })
            continue
        lignes = r.stdout.decode().strip().splitlines()
        dernier, date_dernier = lignes[0].split("\t", 1)
        duree = None
        parent = None
        if len(lignes) > 1:
            parent, date_parent = lignes[1].split("\t", 1)
            try:
                duree = (datetime.fromisoformat(date_dernier) - datetime.fromisoformat(date_parent)).total_seconds()
            except ValueError:
                duree = None
        diff = None
        if parent:
            d = git("diff", parent, dernier, "--", rel)
            diff = len(d.stdout) if d.returncode == 0 else None
        texte = blob(dernier, rel)
        html = mesurer_texte(texte) if texte is not None else {
            "fenetres": None, "depliants": None, "x_octets": None, "y_octets": None, "T": None}
        mod, src = modele("redacteur")
        ecrire_ligne({
            "horodatage": maintenant(),
            "retroactif": True,
            "lot": lot,
            "fichier": nom,
            "poste": "redacteur",
            "modele": mod,
            "modele_source": src,
            "commit": dernier,
            "commit_precedent": parent,
            "commit_horodatage": date_dernier,
            "duree_s": duree,
            "duree_source": "ecart_entre_les_deux_derniers_commits_du_fichier" if parent else None,
            "octets_lus": None,
            "jetons_lus_est": None,
            "lus": None,
            "facteur_octets_par_jeton": FACTEUR,
            "jetons_proxy": "o200k estimation octets/3.12",
            "octets_diff_git": diff,
            "jetons_ecrits_est": estimation(diff),
            "octets_fichier": len(texte.encode("utf-8")) if texte is not None else None,
            **html,
            "evidence_fichiers": None,
            "evidence_octets": None,
            "web": None,
            "web_n": None,
            "vm_fin": None,
            "vm_debut": None,
            "compteurs_usage_env": None,
        })
        n += 1
        print("rétroactif", nom, html.get("T"), "fen", html.get("fenetres"), "duree_s", duree)
    return 0 if n else 1


def cmd_bilan(lot: str | None) -> int:
    if not JOURNAL.exists():
        print("journal absent")
        return 1
    lignes = []
    for brut in JOURNAL.read_text(encoding="utf-8").splitlines():
        if not brut.strip():
            continue
        o = json.loads(brut)
        if lot and o.get("lot") != lot:
            continue
        lignes.append(o)
    print(f"{'fichier':<12} {'poste':<22} {'duree_s':>8} {'T':<22} {'fen':>4} {'diff_o':>8} {'retro':<5}")
    for o in lignes:
        print(f"{str(o.get('fichier')):<12} {str(o.get('poste')):<22} {str(o.get('duree_s')):>8} "
              f"{str(o.get('T')):<22} {str(o.get('fenetres')):>4} {str(o.get('octets_diff_git')):>8} "
              f"{'oui' if o.get('retroactif') else 'non':<5}")
    print(f"{len(lignes)} ligne(s)")
    return 0


def main(argv=None) -> int:
    a = list(sys.argv[1:] if argv is None else argv)
    if not a:
        print(__doc__)
        return 2
    cmd, *rest = a
    if cmd == "debut" and len(rest) == 3:
        return cmd_debut(*rest)
    if cmd == "lu" and len(rest) == 1:
        return cmd_lu(rest[0])
    if cmd == "web" and len(rest) >= 1:
        return cmd_web(" ".join(rest))
    if cmd == "fin" and len(rest) == 3:
        return cmd_fin(*rest)
    if cmd == "bilan":
        return cmd_bilan(rest[0] if rest else None)
    if cmd == "retroactif":
        lot = "LOT_134"
        jusqua = 7
        if rest:
            lot = rest[0]
        if len(rest) > 1:
            jusqua = int(rest[1])
        return cmd_retroactif(lot, jusqua)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())

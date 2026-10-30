#!/usr/bin/env python3
"""GARDE TEMPS RÉEL DE CODEX — couple [Harnais + Routage], progression, puis audit Astra en boucle (zéro jeton, Python standard).

Déposé par Claude sur ordre de Vial (31.10.2026). Codex l'exécute en permanence ; GitHub Actions l'exécute aussi depuis GitHub.

  python3 codex-LOTS-html/outils/garde_temps_reel.py boucle [--intervalle 60]   garde permanente : contrôle, corrige ce qui peut l'être, dit la prochaine action
  python3 codex-LOTS-html/outils/garde_temps_reel.py controle                   un passage ; code 1 si le couple est rompu (BLOQUANT)
  python3 codex-LOTS-html/outils/garde_temps_reel.py prochaine                  la prochaine action exacte (production, puis audit Astra)
  python3 codex-LOTS-html/outils/garde_temps_reel.py audite <fichier.html>      consigne l'audit Astra d'une leçon (cycle en cours)
  python3 codex-LOTS-html/outils/garde_temps_reel.py installer                  ajoute la garde au crochet pre-commit (sans retirer celui du registre)

Règles appliquées (PROMPT_CODEX.md § 9, PROMPT_PRODUCTION_V2.md L5bis) :
  H1  harnais identique : chaque fichier de harnais/HARNAIS_MANIFESTE.json a l'empreinte du manifeste de production-v2 (le plus récent)
  R1  table de routage valide : routage_codex.py autotest = 0
  R2  veille du routage vivante : .veille_routage < 30 min ; sinon la garde relance « routage_codex.py veille » elle-même
  R3  chaque leçon de codex-LOTS-html/LOT_*/ a au moins une passe consignée dans ROUTAGE_CODEX.jsonl
  R4  aucune leçon auditée par le modèle qui l'a rédigée, sauf audit_croise_externe déclaré
  P   progression : LOTS de la plage IA_RESERVATIONS.json (codex) complets = 11 leçons avec FIN_FICHIER
  A   quand tout est complet : audit Astra (gpt-6-astra, passe indépendante, consignée « auditeur-medical ») de chaque leçon,
      puis nouveau cycle ; jamais d'arrêt.
Corrections automatiques (zéro jeton) : resynchronisation du harnais depuis origin/production-v2, relance de la veille du routage.
Tout le reste est BLOQUANT : la garde dit exactement quoi faire ; aucune production tant que le couple n'est pas vert.
"""
import datetime, hashlib, json, os, subprocess, sys, time
from pathlib import Path

D = Path(__file__).resolve().parents[1]          # codex-LOTS-html/
R = D.parent                                       # racine du dépôt
IA = "codex"
ZH = datetime.timezone(datetime.timedelta(hours=1))
ETAT = D / "GARDE_TEMPS_REEL.json"
LOG = D / "GARDE_TEMPS_REEL.log"
ASTRA = D / "AUDIT_ASTRA.json"
POULS_MAX = 30 * 60


def now():
    return datetime.datetime.now(ZH)


def git(*a):
    try:
        return subprocess.run(["git", *a], cwd=R, capture_output=True, text=True, timeout=120).stdout
    except Exception:
        return ""


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None


def manifeste_reference():
    """Manifeste de harnais le plus récent : celui de origin/production-v2, sinon le local."""
    git("fetch", "-q", "origin", "production-v2")
    t = git("show", "origin/production-v2:harnais/HARNAIS_MANIFESTE.json")
    try:
        return json.loads(t), "origin/production-v2"
    except Exception:
        p = R / "harnais/HARNAIS_MANIFESTE.json"
        return (json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}), "local"


def fichiers_manifeste(m):
    f = m.get("fichiers", m)
    return {k: (v.get("sha256") if isinstance(v, dict) else v) for k, v in f.items() if isinstance(v, (str, dict))}


def controle_harnais(corriger):
    m, src = manifeste_reference()
    ecarts = [k for k, h in fichiers_manifeste(m).items() if h and sha(R / k) != h]
    if ecarts and corriger and src == "origin/production-v2":
        git("checkout", "origin/production-v2", "--", *ecarts)
        ecarts = [k for k, h in fichiers_manifeste(m).items() if h and sha(R / k) != h]
        if not ecarts:
            return True, f"harnais resynchronisé depuis production-v2 (corrigé automatiquement)"
    return (not ecarts), ("harnais identique au manifeste (" + src + ")" if not ecarts else
                          f"harnais NON identique ({len(ecarts)} fichier(s) : {', '.join(ecarts[:5])}) → git checkout origin/production-v2 -- {' '.join(ecarts[:5])}")


def routage_conf():
    try:
        return json.loads((D / "ROUTAGE_CODEX.json").read_text(encoding="utf-8"))
    except Exception:
        return None


def controle_routage(corriger):
    res = []
    rc = subprocess.run([sys.executable, str(D / "routage_codex.py"), "autotest"], cwd=R, capture_output=True, text=True)
    res.append((rc.returncode == 0, "R1 table de routage valide" if rc.returncode == 0 else "R1 autotest du routage ROUGE → corriger ROUTAGE_CODEX.json"))
    pouls = D / ".veille_routage"
    age = None
    try:
        t = pouls.read_text(encoding="utf-8").strip()
        age = (now() - datetime.datetime.fromisoformat(t)).total_seconds()
    except Exception:
        pass
    if (age is None or age > POULS_MAX) and corriger:
        subprocess.Popen([sys.executable, str(D / "routage_codex.py"), "veille"], cwd=R, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
        time.sleep(3)
        try:
            age = (now() - datetime.datetime.fromisoformat(pouls.read_text(encoding="utf-8").strip())).total_seconds()
        except Exception:
            pass
    vivant = age is not None and age <= POULS_MAX
    res.append((vivant, f"R2 veille du routage vivante (pouls il y a {int(age // 60)} min)" if vivant else "R2 veille du routage MORTE → python3 codex-LOTS-html/routage_codex.py veille &"))
    passes = {}
    jl = D / "ROUTAGE_CODEX.jsonl"
    if jl.exists():
        for l in jl.read_text(encoding="utf-8").splitlines():
            try:
                o = json.loads(l)
            except Exception:
                continue
            passes.setdefault((o.get("lot"), str(o.get("fichier", "")).split(" ")[0]), []).append(o)
    sans = []
    for f in sorted(D.glob("LOT_[0-9][0-9][0-9]/LOT_*_Phase_*.html")):
        lot = f.parent.name
        cle = "Phase_A" if "Phase_A" in f.name else "DX." + f.stem.split("DX.")[-1]
        if not any(l == lot and (x == cle or x.startswith(cle) or x in (f.name, f.stem)) for (l, x) in passes):
            sans.append(f.relative_to(R).as_posix())
    res.append((not sans, "R3 chaque leçon a sa passe consignée" if not sans else
                f"R3 {len(sans)} leçon(s) sans passe consignée → routage_codex.py consigner … (ex. {sans[0]})"))
    conf = routage_conf() or {}
    red = (conf.get("postes", {}).get("redacteur") or {}).get("modele")
    externe = conf.get("audit_croise_externe")
    auto = [k for k, v in passes.items() if any(o.get("poste") == "auditeur-medical" and o.get("modele") == red for o in v)]
    res.append((externe or not auto, "R4 aucun auto-audit par le modèle rédacteur" if (externe or not auto) else
                f"R4 {len(auto)} audit(s) médical(aux) par le modèle rédacteur → déclarer audit_croise_externe ou faire auditer par un autre modèle"))
    return res


def plage():
    try:
        return tuple(json.loads((R / "IA_RESERVATIONS.json").read_text(encoding="utf-8"))[IA]["plage"])
    except Exception:
        return (18, 133)


def lot_complet(lot):
    d = D / lot
    fs = list(d.glob(f"{lot}_Phase_*.html")) if d.exists() else []
    liste = d / "LISTE_DX_CANONIQUE.md"
    n_dx = sum(1 for l in liste.read_text(encoding="utf-8").splitlines() if l.lstrip().startswith(("DX.", "| DX.", "- DX."))) if liste.exists() else 10
    attendu = 1 + max(n_dx, 10)
    finis = [f for f in fs if "FIN_FICHIER" in f.read_text(encoding="utf-8", errors="ignore")[-400:]]
    return len(finis) >= attendu, len(finis), attendu


def progression():
    a, b = plage()
    lots = [f"LOT_{k:03d}" for k in range(a, b + 1)]
    etat = {l: lot_complet(l) for l in lots}
    faits = [l for l, (ok, _, _) in etat.items() if ok]
    prochain = next((l for l in lots if not etat[l][0]), None)
    return lots, faits, prochain, etat


def astra_etat(lots):
    s = json.loads(ASTRA.read_text(encoding="utf-8")) if ASTRA.exists() else {"cycle": 1, "audites": []}
    tout = [f.relative_to(R).as_posix() for l in lots for f in sorted((D / l).glob(f"{l}_Phase_*.html"))]
    reste = [f for f in tout if f not in s["audites"]]
    if tout and not reste:
        s = {"cycle": s["cycle"] + 1, "audites": [], "cycle_precedent_fini": now().isoformat(timespec="seconds")}
        ASTRA.write_text(json.dumps(s, ensure_ascii=False, indent=1), encoding="utf-8")
        reste = tout
    return s, reste


def prochaine_action(couple_ok, lots, faits, prochain):
    if not couple_ok:
        return "BLOQUANT : rétablir le couple [Harnais + Routage] (voir les lignes ✗) ; aucune production avant."
    if prochain:
        ok, n, att = lot_complet(prochain)
        return f"PRODUIRE {prochain} : {n}/{att} leçons finies → poursuivre (PROMPT_CODEX.md, norme V8), consigner chaque passe, pousser codex/lots."
    s, reste = astra_etat(lots)
    return (f"AUDIT ASTRA cycle {s['cycle']} : {len(reste)} leçon(s) restante(s) → auditer {reste[0]} (gpt-6-astra, passe indépendante, "
            f"routage_codex.py consigner … auditeur-medical), corriger en place, verif_refonte VERT, puis : garde_temps_reel.py audite {reste[0]}")


def passage(corriger=True, sortie=True):
    h_ok, h_txt = controle_harnais(corriger)
    r = controle_routage(corriger)
    lignes = [(h_ok, "H1 " + h_txt)] + r
    couple_ok = all(ok for ok, _ in lignes)
    lots, faits, prochain, _ = progression()
    action = prochaine_action(couple_ok, lots, faits, prochain)
    etat = dict(horodatage=now().isoformat(timespec="seconds"), couple_harnais_routage="VERT" if couple_ok else "ROUGE",
                controles=[{"ok": ok, "detail": t} for ok, t in lignes], lots_complets=len(faits), lots_total=len(lots),
                phase="production" if prochain else "audit Astra", prochaine_action=action)
    ETAT.write_text(json.dumps(etat, ensure_ascii=False, indent=1), encoding="utf-8")
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"{etat['horodatage']} couple {etat['couple_harnais_routage']} · {len(faits)}/{len(lots)} LOTS · {action}\n")
    if sortie:
        print(f"[{etat['horodatage']}] COUPLE [Harnais + Routage] : {etat['couple_harnais_routage']}")
        for ok, t in lignes:
            print(("  ✓ " if ok else "  ✗ ") + t)
        print(f"  Progression : {len(faits)}/{len(lots)} LOTS complets ({'production' if prochain else 'audit Astra'})")
        print("  → " + action)
    return couple_ok


def main(a):
    cmd = a[0] if a else "controle"
    if cmd == "controle":
        return 0 if passage(corriger="--sans-correction" not in a) else 1
    if cmd == "prochaine":
        lots, faits, prochain, _ = progression()
        print(prochaine_action(True, lots, faits, prochain)); return 0
    if cmd == "audite" and len(a) > 1:
        lots, _, _, _ = progression(); s, _ = astra_etat(lots)
        f = Path(a[1]).resolve().relative_to(R).as_posix() if Path(a[1]).exists() else a[1]
        if f not in s["audites"]:
            s["audites"].append(f)
        ASTRA.write_text(json.dumps(s, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"audit Astra consigné (cycle {s['cycle']}) : {f}"); return 0
    if cmd == "boucle":
        pas = int(a[a.index("--intervalle") + 1]) if "--intervalle" in a else 60
        while True:
            try:
                passage()
            except Exception as x:
                print("garde : erreur", x, flush=True)
            sys.stdout.flush(); time.sleep(pas)
    if cmd == "installer":
        h = R / ".git/hooks/pre-commit"
        ligne = 'python3 "$(git rev-parse --show-toplevel)/codex-LOTS-html/outils/garde_temps_reel.py" controle --sans-correction || exit 1\n'
        t = h.read_text() if h.exists() else "#!/bin/sh\n"
        if ligne not in t:
            # la garde passe AVANT le exec du registre, sinon elle ne s'exécuterait jamais
            lignes = t.splitlines(keepends=True)
            i = next((k for k, l in enumerate(lignes) if l.startswith("exec ")), len(lignes))
            lignes.insert(i, ligne)
            h.write_text("".join(lignes)); os.chmod(h, 0o755)
        print("garde ajoutée au crochet pre-commit"); return 0
    print(__doc__); return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

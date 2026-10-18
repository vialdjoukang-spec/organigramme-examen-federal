#!/usr/bin/env python3
"""Porte des étapes et état de pilotage (Codex). Gratuit, déterministe, sans dépendance.

Fichiers : ETAT.json ({"etape_courante":N,"statut":"en_cours|terminee",...}),
ETAT.md (cases de l'Étape 0 entre les balises PORTE-ETAPE-0), tools/etapes.json.

  porte.py etat                 état courant + étape suivante
  porte.py verifier0            0 si l'Étape 0 est complète, sinon 1 et la liste des manques
  porte.py commencer N          refuse (code 2) de commencer N>=1 tant que l'Étape 0 n'est pas complète
  porte.py critere N            0 si le critère de fin automatique de N est atteint
  porte.py terminer [N]         marque l'étape courante terminée (fin de session de Codex)
  porte.py avancer              si terminée : passe à N+1 (ou au lot suivant d'une étape en boucle)
  porte.py ordre                imprime l'ordre de relance de Vial pour l'étape courante
Options : --dry-run (n'écrit rien), --sans-reseau (critères « chaine » non évalués).
"""
import datetime, json, os, re, subprocess, sys
from pathlib import Path

RACINE = os.environ.get("OEF_REPO") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ETAT_JSON = os.path.join(RACINE, "ETAT.json")
ETAT_MD = os.path.join(RACINE, "ETAT.md")
ETAPES = os.path.join(RACINE, "tools", "etapes.json")
DEPOT = os.environ.get("GH_REPO", "vialdjoukang-spec/organigramme-examen-federal")
FICHIERS_ETAPE0 = [
    "CATALOGUE.md", "tools/propose_skills.py", "docs/skills/PROPOSITIONS.md",
    "tools/veille_relance.sh", "tools/file_fusion.sh", "tools/porte.py",
    "PROCHAINE_ACTION.md", "journal/echecs_fusion.md",
]
MARQUE_A_REMPLIR = "À COMPLÉTER PAR CODEX"
DRY = "--dry-run" in sys.argv
SANS_RESEAU = "--sans-reseau" in sys.argv


def maintenant():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def lire_etat():
    try:
        with open(ETAT_JSON, encoding="utf-8") as f:
            e = json.load(f)
    except (OSError, ValueError):
        e = {}
    e.setdefault("etape_courante", 0)
    e.setdefault("statut", "en_cours")
    e.setdefault("lot", 1)
    return e


def ecrire_etat(e):
    e["maj"] = maintenant()
    if DRY:
        print("[dry-run] ETAT.json ←", json.dumps(e, ensure_ascii=False))
        return
    with open(ETAT_JSON, "w", encoding="utf-8") as f:
        json.dump(e, f, ensure_ascii=False, indent=1)
        f.write("\n")


def etapes():
    with open(ETAPES, encoding="utf-8") as f:
        return json.load(f)


def etape(n):
    for x in etapes()["etapes"]:
        if x["n"] == n:
            return x
    return None


def derniere():
    return max(x["n"] for x in etapes()["etapes"])


def verifier0(bavard=True):
    manques = []
    try:
        md = open(ETAT_MD, encoding="utf-8").read()
    except OSError:
        md = ""
    m = re.search(r"<!-- PORTE-ETAPE-0 -->(.*?)<!-- /PORTE-ETAPE-0 -->", md, re.S)
    if not m:
        manques.append("ETAT.md : section PORTE-ETAPE-0 absente")
    else:
        cases = re.findall(r"^\s*- \[( |x|X|~)\] (.+)$", m.group(1), re.M)
        if not cases:
            manques.append("ETAT.md : aucune case dans la porte")
        manques += [f"case non cochée : {t.strip()}" for c, t in cases if c.lower() != "x"]
    for p in FICHIERS_ETAPE0:
        if not os.path.exists(os.path.join(RACINE, p)):
            manques.append(f"fichier absent : {p}")
    cat = os.path.join(RACINE, "CATALOGUE.md")
    if os.path.exists(cat) and MARQUE_A_REMPLIR in open(cat, encoding="utf-8").read():
        manques.append("CATALOGUE.md : sections encore « À COMPLÉTER PAR CODEX » (MCP, skills, droits)")
    if bavard:
        print("Étape 0 complète." if not manques else "Étape 0 INCOMPLÈTE :\n- " + "\n- ".join(manques))
    return not manques


def etat_pr(n):
    r = subprocess.run(["gh", "pr", "view", str(n), "--repo", DEPOT, "--json", "state", "--jq", ".state"],
                       capture_output=True, text=True)
    return r.stdout.strip() or "INCONNU"


def critere(n, bavard=True):
    x = etape(n)
    if not x:
        return False
    c = x.get("critere")
    if not c:
        if bavard:
            print(f"Étape {n} : pas de critère automatique (fin déclarée par Codex : porte.py terminer).")
        return False
    if c["type"] == "porte0":
        return verifier0(bavard)
    if c["type"] == "chaine":
        if SANS_RESEAU:
            print("critère chaine non évalué (--sans-reseau)")
            return False
        noms = c["nom"] if isinstance(c["nom"], list) else [c["nom"]]
        ok = True
        for nom in noms:
            for pr in etapes()["chaines"].get(nom, []):
                s = etat_pr(pr)
                if bavard:
                    print(f"  #{pr} {s}")
                ok &= s in ("MERGED", "CLOSED")
        return ok
    if c["type"] == "jauge":
        r = subprocess.run([sys.executable, os.path.join(RACINE, "tools", "jauge", "binomes.py"), "--json"],
                           capture_output=True, text=True)
        try:
            metric = json.loads(r.stdout)[c["nom"]]
            pct = metric['pct']
        except (ValueError, KeyError):
            return False
        if bavard:
            print(f"  jauge {c['nom']} = {pct} % (seuil {c['seuil']} %)")
        if c['seuil'] == 100:
            exact = type(metric.get('ok')) is int and type(metric.get('total')) is int and metric['total'] > 0 and metric['ok'] == metric['total']
            if exact and n in (8,9):
                sys.path.insert(0, RACINE)
                from tools.coordination.calculer import calculer
                root = Path(RACINE)
                ledger = json.loads((root/'tools/coordination/relectures.json').read_text())
                exact = calculer(root=root,ledger=ledger)['mesure']['maturite_documentaire_complete']
            return exact
        return pct >= c["seuil"]
    return False


def ordre(e=None):
    e = e or lire_etat()
    n = e["etape_courante"]
    x = etape(n) or {"titre": "fin", "modele": "defaut"}
    mod = "GPT 6 Luna (gpt-6-luna)" if x.get("modele") == "luna" else "modèle par défaut"
    lot = f", lot {e.get('lot', 1)}" if x.get("boucle") else ""
    if n > derniere():
        return "Ordre de Vial : le projet est terminé. Vérifie l'Étape 17 puis arrête-toi."
    return (f"Ordre de Vial : continue avec l'étape suivante. Étape {n}{lot} : {x['titre']}. "
            f"Lis AGENTS.md, puis CONTINUATION.md section « Étape {n} », ETAT.md et PROCHAINE_ACTION.md ; "
            f"lance `python3 tools/porte.py commencer {n}` ; travaille ; à la fin `python3 tools/porte.py terminer`. "
            f"Modèle : {mod}. Ne t'arrête jamais devant un obstacle : consigne-le et passe à la suite.")


def main(a):
    a = [x for x in a if not x.startswith("--")]
    cmd = a[0] if a else "etat"
    e = lire_etat()
    if cmd == "etat":
        x = etape(e["etape_courante"]) or {}
        print(json.dumps(e, ensure_ascii=False))
        print(f"Étape {e['etape_courante']} : {x.get('titre', '?')} · statut {e['statut']}")
        return 0
    if cmd == "verifier0":
        return 0 if verifier0() else 1
    if cmd == "commencer":
        n = int(a[1]) if len(a) > 1 else e["etape_courante"]
        if n >= 1 and not verifier0():
            print(f"REFUS : l'Étape {n} ne peut pas commencer tant que l'Étape 0 n'est pas complète.")
            return 2
        if n != e["etape_courante"]:
            print(f"Avertissement : ETAT.json indique l'étape {e['etape_courante']} ; tu demandes {n}.")
        e.update(etape_courante=n, statut="en_cours")
        ecrire_etat(e)
        print(f"OK : Étape {n} commencée ({(etape(n) or {}).get('titre', '?')}).")
        return 0
    if cmd == "critere":
        n = int(a[1]) if len(a) > 1 else e["etape_courante"]
        return 0 if critere(n) else 1
    if cmd == "terminer":
        n = e["etape_courante"]
        if n == 0 and not verifier0():
            print("REFUS : l'Étape 0 n'est pas complète.")
            return 2
        e["statut"] = "terminee"
        ecrire_etat(e)
        print(f"Étape {n} marquée terminée.")
        return 0
    if cmd == "avancer":
        if e["statut"] != "terminee":
            print("Rien à faire : l'étape courante est en cours.")
            return 1
        n = e["etape_courante"]
        x = etape(n) or {}
        if n == 0 and not verifier0(bavard=False):
            e.update(statut="en_cours")  # la porte reste fermée : on reste à l'Étape 0
        elif x.get("boucle") and x.get("critere") and not critere(n, bavard=False):
            e.update(statut="en_cours", lot=e.get("lot", 1) + 1)
        elif x.get("boucle") and not x.get("critere") and "--fin-boucle" not in sys.argv and e.get("fin_boucle") != n:
            # Étape en boucle sans critère : Codex écrit "fin_boucle": N dans ETAT.json quand tout est fait.
            e.update(statut="en_cours", lot=e.get("lot", 1) + 1)
        else:
            e.update(etape_courante=n + 1, statut="en_cours", lot=1)
            e.pop("fin_boucle", None)
        ecrire_etat(e)
        print(ordre(e))
        return 0
    if cmd == "ordre":
        print(ordre(e))
        return 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

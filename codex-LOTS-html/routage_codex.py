#!/usr/bin/env python3
"""MODÈLE de script de routage pour une IA de relève (Codex, Grok). À COPIER puis ADAPTER par l'IA :
    cp harnais/modele_routage/routage_modele.py <ia>-LOTS-html/routage_<ia>.py   (puis remplacer IA = "...")
Le registre (registre_ia.py pret <ia>) refuse toute production tant que ce script n'existe pas, que son autotest
n'est pas vert et que sa veille ne tourne pas. Zéro jeton : Python standard, aucun appel à un modèle.

Commandes :
  python3 <ia>-LOTS-html/routage_<ia>.py choisir <poste>                       modèle et effort à utiliser pour ce poste
  python3 <ia>-LOTS-html/routage_<ia>.py consigner <LOT_XXX> <fichier> <poste> "<raison>"   une ligne dans ROUTAGE_<IA>.jsonl
  python3 <ia>-LOTS-html/routage_<ia>.py autotest                              vérifie la table de routage (code 0 si valide)
  python3 <ia>-LOTS-html/routage_<ia>.py veille [--intervalle 60]              surveillance en temps réel (pouls + contrôles)
Postes : redacteur-phase-a, redacteur, auditeur-medical, auditeur-conformite, transversale, mecanique.
"""
import datetime, json, sys, time
from pathlib import Path

IA = "codex"                       # ← à remplacer par "grok" dans la copie de Grok
D = Path(__file__).resolve().parent
R = D.parent
CONF = D / f"ROUTAGE_{IA.upper()}.json"
JOURNAL = D / f"ROUTAGE_{IA.upper()}.jsonl"
POULS = D / ".veille_routage"
ALERTES = D / f"VEILLE_{IA.upper()}.log"
POSTES = ("redacteur-phase-a", "redacteur", "auditeur-medical", "auditeur-conformite", "transversale", "mecanique")
ORDRE = {"redacteur-phase-a": 0, "redacteur": 0, "auditeur-medical": 1, "auditeur-conformite": 2, "transversale": 3,
         "relecture-interne": 1, "controle-v8": 2, "transversale-interne": 3}
ZH = datetime.timezone(datetime.timedelta(hours=1))


def maintenant():
    return datetime.datetime.now(ZH).isoformat(timespec="seconds")


def conf():
    return json.loads(CONF.read_text(encoding="utf-8"))


def autotest():
    erreurs = []
    try:
        c = conf()
    except Exception as e:
        print(f"ROUTAGE_{IA.upper()}.json illisible : {e}"); return 1
    p = c.get("postes", {})
    for poste in POSTES:
        if not (isinstance(p.get(poste), dict) and p[poste].get("modele") and p[poste].get("effort")):
            erreurs.append(f"poste {poste} : modele et effort obligatoires")
    if p.get("redacteur", {}).get("modele") == p.get("auditeur-medical", {}).get("modele") and not c.get("audit_croise_externe"):
        erreurs.append("l'auditeur médical doit être un autre modèle que le rédacteur (ou audit_croise_externe déclaré)")
    if not c.get("modeles_disponibles"):
        erreurs.append("modeles_disponibles : liste des modèles réellement accessibles à cette IA")
    for e in erreurs:
        print("ÉCHEC :", e)
    print("autotest VERT" if not erreurs else "autotest ROUGE")
    return 1 if erreurs else 0


def poste_actif(poste):
    x = conf()["postes"][poste]
    if x.get("execution") == "differee":
        raise SystemExit("BLOQUÉ : passe indépendante différée ; aucun audit ne peut être déclaré depuis la session de rédaction.")
    return x


def choisir(poste):
    x = poste_actif(poste)
    print(json.dumps({"poste": poste, **x}, ensure_ascii=False))


def consigner(lot, fichier, poste, raison):
    x = poste_actif(poste)
    l = {"horodatage": maintenant(), "lot": lot, "fichier": fichier, "poste": poste,
         "modele": x["modele"], "effort": x["effort"], "raison": raison}
    if "independant" in x:
        l["independant"] = x["independant"]
    with JOURNAL.open("a", encoding="utf-8") as f:
        f.write(json.dumps(l, ensure_ascii=False) + "\n")
    print("consigné :", lot, fichier, poste, x["modele"])


def controle():
    """Contrôles de la veille : ordre des postes, modèle de l'auditeur différent du rédacteur, fichiers sans passe."""
    alertes, passes = [], {}
    if JOURNAL.exists():
        for x in JOURNAL.read_text(encoding="utf-8").splitlines():
            try:
                o = json.loads(x); passes.setdefault((o["lot"], o["fichier"]), []).append(o)
            except Exception:
                alertes.append(f"ligne illisible dans {JOURNAL.name}")
    for (lot, f), L in passes.items():
        rangs = [ORDRE.get(o["poste"], 9) for o in L]
        if rangs != sorted(rangs):
            alertes.append(f"{lot} {f} : postes dans le désordre ({', '.join(o['poste'] for o in L)})")
        red = {o["modele"] for o in L if o["poste"].startswith("redacteur")}
        aud = {o["modele"] for o in L if o["poste"] == "auditeur-medical"}
        if red & aud and not conf().get("audit_croise_externe"):
            alertes.append(f"{lot} {f} : audit médical par le même modèle que la rédaction")
    for h in D.glob("LOT_[0-9][0-9][0-9]/*.html"):
        nom = "Phase_A" if "_Phase_A_" in h.name else h.stem.split("_V0_")[-1]
        if (h.parent.name, nom) not in passes:
            alertes.append(f"{h.parent.name} {nom} : fichier sans aucune passe consignée")
    return alertes


def veille(intervalle=60):
    print(f"veille du routage {IA} : pouls toutes les {intervalle} s (Ctrl+C pour arrêter)")
    while True:
        POULS.write_text(maintenant())
        a = controle()
        with ALERTES.open("a", encoding="utf-8") as f:
            f.write(f"{maintenant()} pouls actif ; {len(a)} alerte(s) ; surveillance mécanique seule, aucun audit médical effectué.\n")
        if a:
            with ALERTES.open("a", encoding="utf-8") as f:
                for x in a:
                    f.write(f"{maintenant()} {x}\n")
        time.sleep(intervalle)


def main(a):
    if a and a[0] == "autotest":
        return autotest()
    if len(a) == 2 and a[0] == "choisir":
        choisir(a[1]); return 0
    if len(a) == 5 and a[0] == "consigner":
        consigner(*a[1:]); return 0
    if a and a[0] == "veille":
        veille(int(a[a.index("--intervalle") + 1]) if "--intervalle" in a else 60); return 0
    print(__doc__); return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

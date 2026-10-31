#!/usr/bin/env python3
"""Autotest et backtest de la conscience. Zéro jeton. N'écrit pas dans les LOT.

  python3 grok-LOTS-html/outils/conscience/autotest.py
  python3 grok-LOTS-html/outils/conscience/autotest.py --backtest

Le backtest lit git (versions parentes des commits d'audit) et corrections.jsonl.
Il écrit grok-LOTS-html/outils/conscience/resultats_backtest.json (mesure).
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import time
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import conscience as C

RACINE = C.racine_depot()
FACTURE = 3.12


def page(corps: str, titre: str = "Essai", nom: str = "LOT_000_Phase_B_V0_DX.1.html") -> str:
    return (
        "<!doctype html><html><body><main>"
        f"<h1>{titre}</h1><section><h2 id=\"p1\">1. Définition</h2><p>{corps}</p></section>"
        "</main></body></html>"
    )


def a(**kw):
    html = kw.pop("html")
    return C.analyser(html, **kw)


def contient(res, mot: str, niveau: str | None = None) -> bool:
    for o in res.ordres:
        if mot.lower() in o.texte.lower() and (niveau is None or o.niveau == niveau):
            return True
    return False


def tests() -> int:
    ko = 0

    def attend(cond, msg):
        nonlocal ko
        if not cond:
            ko += 1
            print("ÉCHEC", msg)
        else:
            print("ok", msg)

    r = a(html=page("Un érysipèle simple ne explique pas une crépitation."), lot="LOT_134", ssp="F1.5", titre="Érysipèle")
    attend(contient(r, "n'explique", "SIGNAL"), "élision ne explique")

    r = a(html=page("Paracétamol : 8 000 mg par jour chez l'adulte."), lot="LOT_134", ssp="F1.5", titre="Dose")
    attend(contient(r, "8000", "BLOQUANT") or contient(r, "8", "BLOQUANT"), "paracétamol 8000 mg/j bloquant")

    r = a(html=page("Paracétamol : 500 à 1 000 mg par prise, plafond 4 000 mg par jour."), lot="LOT_134", ssp="F1.5")
    attend(not any(o.niveau == "BLOQUANT" for o in r.ordres), "posologie AIPS dans les plafonds : pas de BLOQUANT")

    r = a(html=page("La journée de paracétamol est limitée à 2 g dans la maladie hépatique chronique."), lot="LOT_134", ssp="F1.5")
    attend(not any(o.niveau == "BLOQUANT" and "paracétamol" in o.texte for o in r.ordres), "2 g journaliers : pas un dépassement de prise")

    r = a(html=page("On donne du paracétamol 500 µg par prise."), lot="LOT_134", ssp="F1.5")
    attend(contient(r, "µg", "BLOQUANT") or contient(r, "unité", "BLOQUANT"), "µg au lieu de mg : bloquant")

    r = a(html=page("La kaliémie est à 25 mmol/l."), lot="LOT_134", ssp="F1.5")
    attend(contient(r, "kaliémie", "BLOQUANT"), "kaliémie impossible")

    r = a(html=page("La kaliémie est à 5,2 mmol/l."), lot="LOT_134", ssp="F1.5")
    attend(not any(o.niveau == "BLOQUANT" for o in r.ordres), "kaliémie 5,2 plausible")

    r = a(html=page("Zorblatix 50 mg deux fois par jour."), lot="LOT_134", ssp="F1.5")
    attend(contient(r, "Zorblatix", "SIGNAL") or contient(r, "sans référence", "SIGNAL"), "molécule inconnue")

    corps = "Radiographie du squelette. Aucune règle nommée."
    r = a(html=page(corps, "Phase A"), lot="LOT_152", ssp="F2.4", titre="Radiographies",
          corps_lot=corps, inclure_lot=True)
    attend(contient(r, "Ottawa"), "Ottawa absent : SOURCER")
    attend(contient(r, "Fleischner"), "Fleischner absent : SOURCER")
    attend("plutôt que retirer" in " ".join(o.texte for o in r.ordres), "formule sourcer plutôt que retirer")

    r = a(html=page("Le score d'Alvarado oriente vers une stratégie opératoire."), lot="LOT_134", ssp="F1.5", titre="Appendicite")
    attend(contient(r, "Alvarado"), "Alvarado sans réserve")
    r = a(html=page("Alvarado : la stratégie opératoire ne se décide pas ainsi. Le score n'autorise pas à confirmer."), lot="LOT_134", ssp="F1.5", titre="Appendicite")
    attend(not contient(r, "Alvarado"), "Alvarado avec réserve : silence")

    r = a(html=page("Après 65 ans : 14/1 000 d'un côté et 14/100 de l'autre."), lot="LOT_135", ssp="F1.6")
    attend(contient(r, "14/100"), "deux dénominateurs")

    r = a(html=page("L'AIPS dit la dose. Le WSES est cité."), lot="LOT_134", ssp="F1.5")
    attend(contient(r, "AIPS") and contient(r, "WSES"), "sigles nus")

    # Plafond de lignes
    faux = [C.Ordre(3, "SIGNAL", "conscience linguistique", i, f"CORRIGER item {i}.", "mineure", f"k{i}") for i in range(40)]
    txt = C.formater(C.Resultat(faux, 0.01), "CONSCIENCE essai")
    attend(len(txt.splitlines()) <= 30, f"plafond 30 lignes ({len(txt.splitlines())})")

    attend(C.orthographe_disponible() != "hunspell-fr", "hunspell-fr non requis pour passer")

    # Vitesse sur un vrai fichier, lecture seule
    cible = RACINE / "grok-LOTS-html/LOT_134/LOT_134_Phase_A_V0.html"
    if cible.exists():
        t0 = time.perf_counter()
        html = cible.read_text(encoding="utf-8", errors="replace")
        C.analyser(html, lot="LOT_134", ssp="F1.5", titre=C.titre_de(html), inclure_lot=False)
        dt = time.perf_counter() - t0
        attend(dt < 5, f"Phase A LOT_134 en {dt:.2f} s (< 5 s)")
    print(f"autotest : {ko} échec(s)")
    return ko


def _git(args: list[str]) -> str:
    return subprocess.check_output(["git", *args], cwd=RACINE, text=True, stderr=subprocess.DEVNULL)


def parent_quand(path: str, aiguille: str) -> str | None:
    try:
        log = _git(["log", "--reverse", "--format=%H\t%s", "--", path])
    except subprocess.CalledProcessError:
        return None
    for line in log.splitlines():
        if "\t" not in line:
            continue
        h, s = line.split("\t", 1)
        if aiguille in s.lower():
            try:
                return _git(["rev-parse", h + "^"]).strip()
            except subprocess.CalledProcessError:
                return None
    return None


def montrer(parent: str, path: str) -> str | None:
    try:
        return _git(["show", f"{parent}:{path}"])
    except subprocess.CalledProcessError:
        return None


def classe_gold(g: dict) -> str:
    """Règle explicite. Les audits n'utilisent pas le mot critique.

    critique : aucune correction d'audit (0). On ne promeut pas « grave » en critique.
    grave    : gravité d'audit « grave ».
    mineure  : léger, moyen, ou type langue.
    """
    if g.get("gravite") == "grave" and g.get("type") != "langue":
        return "grave"
    return "mineure"


STOP = {
    "dans", "avec", "pour", "cette", "comme", "plus", "moins", "sont", "être", "etre",
    "corrig", "sourcer", "plutot", "plutôt", "retirer", "conscience", "medicale", "médicale",
    "phase", "point", "ajout", "sans", "chez", "tout", "tous", "leur", "alors", "aussi",
    "entre", "apres", "après", "avant", "texte", "ligne",
}


def tokens(s: str) -> set[str]:
    return {t for t in re.findall(r"[a-zà-ÿ0-9]{5,}", s.lower()) if t not in STOP}


def apparie(ordre: C.Ordre, gold: dict) -> bool:
    """Un ordre rappelle une correction si deux mots de 5 lettres ou plus coïncident
    (avant ou après), ou si un pont explicite relie une forme fautive à sa correction.
    """
    og = (gold.get("avant") or "") + " " + (gold.get("apres") or "")
    inter = tokens(ordre.texte) & tokens(og)
    if len(inter) >= 2:
        return True
    g = og.lower()
    o = ordre.texte.lower()
    ponts = (
        ("ne explique", "n'explique"),
        ("tirée de le", "tirée du"),
        ("tirée de les", "tirée des"),
        ("tiré de le", "tiré du"),
        ("le situation", "la situation"),
        ("14/100", "14/100"),
        ("alvarado", "alvarado"),
        ("qsofa", "qsofa"),
        ("30 mm", "30 mm"),
        ("0,7", "0,7"),
    )
    for a, b in ponts:
        if a in g and b in o:
            return True
    src = (gold.get("source") or "").lower()
    if "sigle" in src and "sigle" in o:
        return True
    if gold.get("type") == "dose" and ordre.conscience == "conscience posologique":
        if inter:
            return True
    return False


def lecon_vers_nom(lot: str, lecon: str) -> str | None:
    if not lecon:
        return None
    if "Phase_A" in lecon or lecon.startswith("Phase A"):
        return f"{lot}_Phase_A_V0.html"
    m = re.search(r"DX\.(\d+)", lecon)
    if m:
        return f"{lot}_Phase_B_V0_DX.{m.group(1)}.html"
    return None


def charger_gold(lot: str) -> list[dict]:
    p = RACINE / "grok-LOTS-html" / lot / "audits" / "corrections.jsonl"
    out = []
    if not p.exists():
        return out
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        g = json.loads(line)
        g["classe"] = classe_gold(g)
        g["fichier"] = lecon_vers_nom(lot, g.get("lecon") or "")
        out.append(g)
    return out


def backtest() -> dict:
    rapport = {"lots": {}, "methode": {
        "instantane": "git show <parent du premier commit dont le message contient l'aiguille>:fichier",
        "medical": "aiguille « audit médical » ; or utilisé pour les corrections de type ≠ langue",
        "langue": "aiguille « conformité » ; or utilisé pour type langue. À défaut, l'instantané médical.",
        "appariement": "≥ 2 jetons d'au moins 5 lettres en commun, ou pont (ne explique, sigle, Alvarado, 14/100, 30 mm)",
        "plafond_sortie": "les jetons lus par le rédacteur sont ceux de la sortie plafonnée à 30 lignes (commande fichier)",
        "facteur": FACTURE,
    }}
    for lot in ("LOT_134", "LOT_135"):
        gold = charger_gold(lot)
        ssp, _ = C.ssp_catalogue(lot)
        par_fichier: dict[str, dict] = {}
        for g in gold:
            if not g["fichier"]:
                continue
            par_fichier.setdefault(g["fichier"], {"gold": [], "ordres_med": [], "ordres_lang": []})
            par_fichier[g["fichier"]]["gold"].append(g)
        jetons_sortie = 0
        secondes = []
        for nom, bloc in par_fichier.items():
            path = f"grok-LOTS-html/{lot}/{nom}"
            p_med = parent_quand(path, "audit médical")
            p_lang = parent_quand(path, "conformité")
            html_med = montrer(p_med, path) if p_med else None
            html_lang = montrer(p_lang, path) if p_lang else None
            bloc["parent_medical"] = p_med
            bloc["parent_langue"] = p_lang
            if html_med:
                r = C.analyser(html_med, lot=lot, ssp=ssp, titre=C.titre_de(html_med), inclure_lot=False)
                bloc["ordres_med"] = [o for o in r.ordres]
                secondes.append(r.secondes)
                # Une passe : ce que le rédacteur lit sur le texte soumis à l'audit (sortie plafonnée).
                jetons_sortie += len(C.formater(r, f"CONSCIENCE {nom}").encode("utf-8")) / FACTURE
            if html_lang:
                r = C.analyser(html_lang, lot=lot, ssp=ssp, titre=C.titre_de(html_lang), inclure_lot=False)
                bloc["ordres_lang"] = list(r.ordres)
            elif html_med:
                bloc["ordres_lang"] = bloc["ordres_med"]
        # Rappel / précision
        stats = {k: {"gold": 0, "rappeles": 0} for k in ("grave", "mineure")}
        stats["critique"] = {"gold": 0, "rappeles": 0}
        tp_ordres = 0
        fp_ordres = 0
        ordres_vus = 0
        details_fn = []
        graves_ok = []
        octets_apres = 0
        for nom, bloc in par_fichier.items():
            ordres = bloc["ordres_med"] + [o for o in bloc["ordres_lang"] if o not in bloc["ordres_med"]]
            # dédoublonnage grossier par cle+texte
            uniq = []
            vu = set()
            for o in list(bloc["ordres_med"]) + list(bloc["ordres_lang"]):
                cle = (o.cle, o.texte)
                if cle in vu:
                    continue
                vu.add(cle)
                uniq.append(o)
            ordres_vus += len(uniq)
            for g in bloc["gold"]:
                stats[g["classe"]]["gold"] += 1
                pool = bloc["ordres_lang"] if g.get("type") == "langue" else bloc["ordres_med"]
                if any(apparie(o, g) for o in pool):
                    stats[g["classe"]]["rappeles"] += 1
                    g["rappel"] = True
                    if g["classe"] == "grave":
                        graves_ok.append((g.get("avant") or "")[:120])
                    octets_apres += len((g.get("apres") or "").encode("utf-8"))
                else:
                    g["rappel"] = False
                    if len(details_fn) < 12:
                        details_fn.append({"fichier": nom, "classe": g["classe"], "type": g.get("type"),
                                           "gravite_audit": g.get("gravite"), "avant": (g.get("avant") or "")[:140]})
            for o in uniq:
                pool = bloc["gold"]
                if any(apparie(o, g) for g in pool):
                    tp_ordres += 1
                else:
                    fp_ordres += 1
        prec = tp_ordres / ordres_vus if ordres_vus else None
        rapport["lots"][lot] = {
            "corrections": len(gold),
            "par_classe": {
                k: {**v, "rappel": (v["rappeles"] / v["gold"] if v["gold"] else None)}
                for k, v in stats.items()
            },
            "ordres": ordres_vus,
            "vrais_positifs_ordres": tp_ordres,
            "faux_positifs_ordres": fp_ordres,
            "precision": prec,
            "fichiers_avec_instantane_medical": sum(1 for b in par_fichier.values() if b["parent_medical"]),
            "fichiers": len(par_fichier),
            "jetons_sortie_plafonnee_est": round(jetons_sortie, 1),
            "jetons_corrections_induites_est": round(octets_apres / FACTURE, 1),
            "note_corrections": "octets du champ apres des corrections rappelées / 3,12. Estimation : le rédacteur réécrit à peu près la phrase d'audit. Les ordres non appariés ne sont pas comptés comme réécriture.",
            "secondes_max": round(max(secondes), 3) if secondes else None,
            "graves_rappeles": graves_ok,
            "faux_negatifs_exemples": details_fn,
            "gravite_native": {
                "grave": sum(1 for g in gold if g.get("gravite") == "grave"),
                "moyen": sum(1 for g in gold if g.get("gravite") == "moyen"),
                "léger": sum(1 for g in gold if g.get("gravite") == "léger"),
                "langue": sum(1 for g in gold if g.get("type") == "langue"),
                "medical": sum(1 for g in gold if g.get("type") != "langue"),
            },
        }
    # LOT 149-154, texte actuel, lecture seule
    actuels = {}
    for n in range(149, 155):
        lot = f"LOT_{n}"
        dossier = RACINE / "grok-LOTS-html" / lot
        if not dossier.is_dir():
            continue
        ssp, _ = C.ssp_catalogue(lot)
        freres = C.corps_freres(dossier)
        ordres = []
        t0 = time.perf_counter()
        for p in C.fichiers_lot(dossier):
            html = p.read_text(encoding="utf-8", errors="replace")
            r = C.analyser(html, lot=lot, ssp=ssp, titre=C.titre_de(html), inclure_lot=("Phase_A" in p.name), corps_lot=freres)
            for o in r.ordres:
                ordres.append({"fichier": p.name, "niveau": o.niveau, "conscience": o.conscience,
                               "gravite": o.gravite, "ligne": o.ligne, "texte": o.texte})
        # éléments de lot une fois
        rlot = C.analyser("<html><h1>lot</h1><p></p></html>", lot=lot, ssp=ssp, titre="lot",
                          corps_lot=freres, inclure_lot=True)
        deja = {o["texte"] for o in ordres}
        for o in rlot.ordres:
            if o.cle.startswith("elt:") and o.texte not in deja:
                ordres.append({"fichier": "LOT", "niveau": o.niveau, "conscience": o.conscience,
                               "gravite": o.gravite, "ligne": 0, "texte": o.texte})
        dt = time.perf_counter() - t0
        actuels[lot] = {"ordres": ordres, "n": len(ordres), "secondes": round(dt, 3),
                        "bloquants": sum(1 for o in ordres if o["niveau"] == "BLOQUANT")}
    rapport["lots_149_154"] = actuels
    dest = ICI / "resultats_backtest.json"
    dest.write_text(json.dumps(rapport, ensure_ascii=False, indent=1), encoding="utf-8")
    print("écrit", dest)
    return rapport


def main() -> int:
    ko = tests()
    if "--backtest" in sys.argv:
        backtest()
    return 1 if ko else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Catalogue de production et catalogue joueur du jeu INTERNAT.

La source de vérité est jeu-revision/docs/progression.json.
Ce script la lit, la met à jour, et régénère :
  - docs/CATALOGUE_PRODUCTION.md  (chantier, pour les agents)
  - catalogue.html                (pour Vial, publié sur GitHub Pages)

Commandes :
  status
  set <specialite> --statut ... [--couvertes N] [--total N] [--urgence N]
      [--consultation N] [--a-verifier X] [--commit H] [--planche chemin] [--notes TEXTE]
  next
  render

Sans dépendance externe. N'invente aucun total : une valeur absente s'affiche « à établir ».
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Europe/Amsterdam")
ROOT = Path(__file__).resolve().parents[1]  # jeu-revision/
JSON_PATH = ROOT / "docs" / "progression.json"
MD_PATH = ROOT / "docs" / "CATALOGUE_PRODUCTION.md"
HTML_PATH = ROOT / "catalogue.html"
DATA_DIR = ROOT / "data"

STATUTS = ("à faire", "en cours", "audité", "poussé")
STATUT_ALIAS = {
    "à faire": "à faire", "a faire": "à faire", "à-faire": "à faire", "a-faire": "à faire",
    "en cours": "en cours", "en-cours": "en cours",
    "audité": "audité", "audite": "audité",
    "poussé": "poussé", "pousse": "poussé",
}
JOUEUR_STATUTS = ("disponible", "à venir")

# Groupes du plan, dans l'ordre de PLAN_PRODUCTION.md.
# Les 63 entrées « dans_catalogue_joueur » sont les spécialités et disciplines
# des lots A–G, du paraclinique, des transversales et des sciences fondamentales.
# Le plan n'en compte pas 45 : il en compte 63 (détail dans CATALOGUE_PRODUCTION.md).
GROUPES = [
    ("veille", "0 · Veille", False),
    ("phase-0", "Phase 0 · Moteur", False),
    ("lot-a", "Lot A · Médecine interne", True),
    ("lot-b", "Lot B · Neurosciences et santé mentale", True),
    ("lot-c", "Lot C · Mère et enfant", True),
    ("lot-d", "Lot D · Chirurgie", True),
    ("lot-e", "Lot E · Organes des sens et peau", True),
    ("lot-f", "Lot F · Aigu et fin de vie", True),
    ("lot-g", "Lot G · Premier recours et société", True),
    ("paraclinique", "Phase 2 · Paraclinique", True),
    ("transversales", "Phase 3 · Disciplines transversales", True),
    ("fondamentales", "Phase 4 · Sciences fondamentales", True),
    ("examen-blanc", "Examen blanc PROFILES", False),
]

# (id, nom, groupe, data_systeme ou None)
CATALOGUE_ITEMS = [
    ("veille", "Veille (examen fédéral, santé publique, sociétés savantes)", "veille", None),
    ("moteur", "Moteur (règles, étoiles, modes, sons, traqueur, carte du parcours)", "phase-0", None),
    # Lot A
    ("cardiologie", "Cardiologie", "lot-a", "cardio"),
    ("angiologie", "Angiologie", "lot-a", None),
    ("pneumologie", "Pneumologie", "lot-a", "pneumo"),
    ("gastro-enterologie-hepatologie", "Gastro-entérologie et hépatologie", "lot-a", None),
    ("nephrologie", "Néphrologie", "lot-a", None),
    ("endocrinologie-diabetologie", "Endocrinologie et diabétologie", "lot-a", None),
    ("hematologie", "Hématologie", "lot-a", None),
    ("oncologie", "Oncologie", "lot-a", None),
    ("infectiologie", "Infectiologie", "lot-a", "infectieux"),
    ("rhumatologie", "Rhumatologie", "lot-a", None),
    ("immunologie-allergologie", "Immunologie et allergologie", "lot-a", None),
    ("geriatrie", "Gériatrie", "lot-a", None),
    # Lot B
    ("neurologie", "Neurologie", "lot-b", "neuro"),
    ("psychiatrie-psychotherapie", "Psychiatrie et psychothérapie", "lot-b", None),
    ("pedopsychiatrie", "Pédopsychiatrie", "lot-b", None),
    ("addictologie", "Addictologie", "lot-b", None),
    # Lot C
    ("pediatrie", "Pédiatrie", "lot-c", None),
    ("neonatologie", "Néonatologie", "lot-c", None),
    ("gynecologie", "Gynécologie", "lot-c", None),
    ("obstetrique", "Obstétrique", "lot-c", None),
    # Lot D
    ("chirurgie-viscerale", "Chirurgie viscérale", "lot-d", None),
    ("traumatologie-orthopedie", "Traumatologie et orthopédie", "lot-d", None),
    ("urologie", "Urologie", "lot-d", None),
    ("chirurgie-vasculaire", "Chirurgie vasculaire", "lot-d", None),
    ("chirurgie-thoracique-cardiaque", "Chirurgie thoracique et cardiaque", "lot-d", None),
    ("neurochirurgie", "Neurochirurgie", "lot-d", None),
    # Lot E
    ("orl", "ORL", "lot-e", None),
    ("ophtalmologie", "Ophtalmologie", "lot-e", None),
    ("dermatologie-venereologie", "Dermatologie et vénéréologie", "lot-e", None),
    # Lot F
    ("medecine-urgence", "Médecine d'urgence", "lot-f", None),
    ("anesthesiologie", "Anesthésiologie", "lot-f", None),
    ("medecine-intensive", "Médecine intensive", "lot-f", None),
    ("toxicologie", "Toxicologie", "lot-f", None),
    ("medecine-palliative", "Médecine palliative", "lot-f", None),
    # Lot G
    ("medecine-famille", "Médecine de famille", "lot-g", None),
    ("medecine-voyages-tropicale", "Médecine des voyages et tropicale", "lot-g", None),
    ("medecine-travail", "Médecine du travail", "lot-g", None),
    ("medecine-physique-readaptation", "Médecine physique et réadaptation", "lot-g", None),
    ("prevention-sante-publique", "Prévention et santé publique", "lot-g", None),
    ("medecine-legale", "Médecine légale", "lot-g", None),
    ("genetique-medicale", "Génétique médicale", "lot-g", None),
    # Paraclinique
    ("radiologie", "Radiologie", "paraclinique", None),
    ("medecine-nucleaire", "Médecine nucléaire", "paraclinique", None),
    ("laboratoire", "Laboratoire (chimie, hématologie, microbiologie)", "paraclinique", None),
    ("anatomopathologie", "Anatomopathologie", "paraclinique", None),
    ("ecg", "ECG", "paraclinique", None),
    ("efr-explorations-fonctionnelles", "EFR et explorations fonctionnelles", "paraclinique", None),
    # Transversales
    ("ethique", "Éthique", "transversales", None),
    ("droit-medical-suisse", "Droit médical suisse", "transversales", None),
    ("communication", "Communication", "transversales", None),
    ("ebm-statistiques", "EBM et statistiques", "transversales", None),
    ("systeme-sante-assurances", "Système de santé et assurances suisses (LAMal, LAA, AI)", "transversales", None),
    ("pharmacologie-clinique", "Pharmacologie clinique", "transversales", None),
    # Fondamentales
    ("anatomie", "Anatomie", "fondamentales", None),
    ("physiologie", "Physiologie", "fondamentales", None),
    ("physiopathologie", "Physiopathologie", "fondamentales", None),
    ("biochimie", "Biochimie", "fondamentales", None),
    ("pharmacologie", "Pharmacologie", "fondamentales", None),
    ("microbiologie", "Microbiologie", "fondamentales", None),
    ("immunologie", "Immunologie", "fondamentales", None),
    ("genetique", "Génétique", "fondamentales", None),
    ("histologie", "Histologie", "fondamentales", None),
    ("embryologie", "Embryologie", "fondamentales", None),
    # Hors catalogue joueur
    ("examen-blanc-profiles", "Examen blanc PROFILES", "examen-blanc", None),
]

GROUPE_JOUEUR = {g for g, _, flag in GROUPES if flag}


def maintenant():
    return dt.datetime.now(TZ).strftime("%Y-%m-%dT%H:%M:%S%z")


def maintenant_lisible():
    return dt.datetime.now(TZ).strftime("%d.%m.%Y %H:%M") + " (Europe/Amsterdam)"


def item_vierge(ident, nom, groupe, data_systeme):
    return {
        "id": ident,
        "nom": nom,
        "groupe": groupe,
        "dans_catalogue_joueur": groupe in GROUPE_JOUEUR,
        "statut": "à faire",
        "couvertes": None,
        "total": None,
        "urgence": None,
        "consultation": None,
        "a_verifier": None,
        "commit": None,
        "planche": None,
        "notes": "",
        "data_systeme": data_systeme,
    }


def etat_initial():
    items = [item_vierge(*row) for row in CATALOGUE_ITEMS]
    by_id = {i["id"]: i for i in items}

    by_id["moteur"]["statut"] = "poussé"
    by_id["moteur"]["commit"] = "8de11ee8762ac9e1250341a7f94d6c55509a497f"
    by_id["moteur"]["notes"] = (
        "La Phase 0 (moteur v2, confiance, traqueur, parcours, sons, outils de couverture et planche) "
        "a été poussée sur main le 17.11.2026 (commit 8de11ee)."
    )

    cardio = by_id["cardiologie"]
    cardio["statut"] = "à faire"
    cardio["couvertes"] = 0
    cardio["total"] = None
    cardio["urgence"] = 1
    cardio["consultation"] = 0
    cardio["a_verifier"] = "35/180"
    cardio["commit"] = "8de11ee8762ac9e1250341a7f94d6c55509a497f"
    cardio["planche"] = "planches/cardiologie.html"
    cardio["notes"] = (
        "Le prototype « urgences cardio » et la Phase 0 sont sur main (commit 8de11ee) : "
        "18 cartes, 1 cas Urgence, 4 duels, planche planches/cardiologie.html. "
        "Le rapport docs/couverture/cardiologie.md (lu le 17.11.2026) compte 6 pathologies dans le catalogue initial, "
        "dont 0 couverte, 3 partielles et 3 manquantes ; 35 affirmations « À vérifier » sur 180 (19,4 %). "
        "Le total visé pour la spécialité complète reste à établir."
    )

    by_id["veille"]["statut"] = "en cours"
    by_id["veille"]["notes"] = (
        "La veille réutilise veille/veille.py, veille/sources.yml et les workflows ve1/ve2, "
        "puis les étend. Les données quotidiennes s'écrivent sur la branche veille-etat, pas sur main."
    )

    return {
        "version": 1,
        "mis_a_jour": maintenant(),
        "consignes_reprise": (
            "Tu es un agent neuf. Lis d'abord jeu-revision/docs/PROMPT_PROJET.md, "
            "docs/PLAN_PRODUCTION.md, docs/PROGRESSION.md et docs/progression.json. "
            "N'ouvre aucun cours ni aucun LOT du dépôt. Ne modifie pas js/, css/, data/ ni index.html "
            "(Eta_Bot produit le jeu). Lance : python3 jeu-revision/tools/progression.py status "
            "puis python3 jeu-revision/tools/progression.py next. "
            "Après chaque spécialité auditee, exécute la commande set puis render, puis pousse "
            "depuis origin/main (fetch juste avant le push)."
        ),
        "items": items,
    }


def charger():
    if not JSON_PATH.exists():
        etat = etat_initial()
        enregistrer(etat)
        return etat
    etat = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    return etat


def enregistrer(etat):
    etat["mis_a_jour"] = maintenant()
    JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    JSON_PATH.write_text(
        json.dumps(etat, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def trouver(etat, ident):
    for it in etat["items"]:
        if it["id"] == ident:
            return it
    return None


def fmt_nb(val, suffix=""):
    if val is None or val == "":
        return "à établir"
    return f"{val}{suffix}"


def joueur_items(etat):
    return [i for i in etat["items"] if i.get("dans_catalogue_joueur")]


# ---------- extraction d'aperçu depuis data/ du jeu (contenu produit seulement) ----------

def _charger_specialite_json(*idents):
    """Lit data/specialites/<id>.js (JSON strict entre JEU.specialite(...))."""
    for ident in idents:
        if not ident:
            continue
        chemin = DATA_DIR / "specialites" / f"{ident}.js"
        if not chemin.is_file():
            continue
        texte = chemin.read_text(encoding="utf-8")
        m = re.search(r"JEU\.specialite\(\s*(\{.*\})\s*\)\s*;?\s*\Z", texte, re.S)
        brut = m.group(1) if m else None
        if brut is None:
            debut, fin = texte.find("{"), texte.rfind("}")
            if debut == -1 or fin == -1:
                continue
            brut = texte[debut:fin + 1]
        try:
            return json.loads(brut)
        except json.JSONDecodeError:
            continue
    return None


def _cartes_js():
    textes = []
    cards_dir = DATA_DIR / "cards"
    if cards_dir.is_dir():
        for p in sorted(cards_dir.glob("*.js")):
            textes.append(p.read_text(encoding="utf-8"))
    return "\n".join(textes)


def _services_js():
    textes = []
    svc = DATA_DIR / "services"
    if svc.is_dir():
        for p in sorted(svc.glob("*.js")):
            textes.append(p.read_text(encoding="utf-8"))
    return "\n".join(textes)


def _extraire_objet(texte, debut):
    """Retourne le littéral d'objet JS qui commence à texte[debut] == '{'."""
    niveau, dans_chaine, quote, i, n = 0, False, None, debut, len(texte)
    while i < n:
        ch = texte[i]
        if dans_chaine:
            if ch == "\\" and i + 1 < n:
                i += 2
                continue
            if ch == quote:
                dans_chaine = False
            i += 1
            continue
        if ch in ('"', "'", "`"):
            dans_chaine, quote = True, ch
            i += 1
            continue
        if ch == "{":
            niveau += 1
        elif ch == "}":
            niveau -= 1
            if niveau == 0:
                return texte[debut:i + 1]
        i += 1
    return None


def _blocs_objets(texte):
    """Découpe les objets JS qui portent un champ id (cartes ou services).

    On part de chaque `{ id:` plutôt que du premier `{` du fichier, pour ne pas
    avaler tout un IIFE (function () { ... }).
    """
    blocs = []
    for m in re.finditer(r"\{\s*id\s*:", texte):
        bloc = _extraire_objet(texte, m.start())
        if bloc:
            blocs.append(bloc)
    return blocs


def _champ_str(bloc, nom):
    m = re.search(rf'{nom}\s*:\s*"((?:\\.|[^"\\])*)"', bloc)
    return m.group(1).replace('\\"', '"').replace("\\n", " ") if m else None


def _affirmations(bloc, champ):
    """Lit les appels c("texte", "src", ...) d'un tableau nommé champ."""
    m = re.search(rf"{champ}\s*:\s*\[(.*?)\n    \],", bloc, re.S)
    if not m:
        return []
    corps = m.group(1)
    out = []
    for am in re.finditer(r'c\(\s*"((?:\\.|[^"\\])*)"([^)]*)\)', corps):
        texte = am.group(1).replace('\\"', '"')
        rest = am.group(2)
        sources = re.findall(r'"((?:\\.|[^"\\])*)"', rest)
        out.append({"t": texte, "s": sources})
    return out


def _apercu_depuis_json(data):
    pathologies, drapeaux, pieges_patho, pieges_action = [], [], [], []
    for p in data.get("pathologies") or []:
        nom = p.get("nom")
        if nom:
            pathologies.append(nom)
    for carte in data.get("cartes") or []:
        typ = carte.get("type")
        if typ == "pathologie":
            cle = carte.get("cle")
            if cle:
                drapeaux.append(cle)
            if not pathologies and carte.get("nom"):
                pathologies.append(carte["nom"])
            cible = pieges_patho
        else:
            cible = pieges_action
        for aff in carte.get("pieges") or []:
            if not isinstance(aff, dict):
                continue
            texte, sources = aff.get("t") or "", aff.get("s") or []
            if sources and "À vérifier" not in texte:
                cible.append(texte)
    pieges = list(pieges_patho)
    for cas in data.get("cas") or []:
        for etape in cas.get("etapes") or []:
            regles = etape.get("regles") or {}
            if isinstance(regles, dict):
                coups = regles.values()
            else:
                coups = regles
            for coup in coups:
                if not isinstance(coup, dict) or coup.get("verdict") != "erreur":
                    continue
                msg = coup.get("msg") or ""
                if msg.startswith("Erreur. "):
                    msg = msg[len("Erreur. "):]
                if msg and msg not in pieges:
                    pieges.append(msg)
    for msg in pieges_action:
        if msg not in pieges:
            pieges.append(msg)
    if not pathologies:
        return None

    def uniq(xs):
        seen, out = set(), []
        for x in xs:
            if x not in seen:
                seen.add(x); out.append(x)
        return out
    return {
        "pathologies": uniq(pathologies),
        "drapeaux_rouges": uniq(drapeaux),
        "pieges": uniq(pieges)[:8],
    }


def extraire_apercu(systeme, ident=None):
    """Construit l'aperçu d'une spécialité à partir des fichiers data/ uniquement.

    Ne retient que le contenu produit. Les pièges sans source (s vide) sont écartés.
    Retourne None s'il n'y a aucune pathologie produite pour ce système.
    """
    data = _charger_specialite_json(ident, systeme)
    if data:
        return _apercu_depuis_json(data)
    if not systeme:
        return None
    texte = _cartes_js()
    if not texte:
        return None
    pathologies, drapeaux, pieges_patho, pieges_action = [], [], [], []
    for bloc in _blocs_objets(texte):
        if _champ_str(bloc, "systeme") != systeme:
            continue
        typ = _champ_str(bloc, "type")
        if typ == "pathologie":
            nom = _champ_str(bloc, "nom")
            cle = _champ_str(bloc, "cle")
            if nom:
                pathologies.append(nom)
            if cle:
                drapeaux.append(cle)
            cible = pieges_patho
        else:
            cible = pieges_action
        for aff in _affirmations(bloc, "pieges"):
            if aff["s"] and "À vérifier" not in aff["t"]:
                cible.append(aff["t"])
    pieges = list(pieges_patho)

    # Pièges des duels : uniquement les messages des coups verdict « erreur ».
    svc = _services_js()
    for am in re.finditer(
        r'verdict\s*:\s*"erreur"\s*,\s*(?:pv\s*:\s*\d+\s*,\s*)?msg\s*:\s*"((?:\\.|[^"\\])*)"',
        svc,
    ):
        msg = am.group(1).replace('\\"', '"')
        if msg.startswith("Erreur. "):
            msg = msg[len("Erreur. "):]
        if msg and msg not in pieges:
            pieges.append(msg)
    for msg in pieges_action:
        if msg not in pieges:
            pieges.append(msg)

    if not pathologies:
        return None
    # Déduplique en conservant l'ordre
    def uniq(xs):
        seen, out = set(), []
        for x in xs:
            if x not in seen:
                seen.add(x); out.append(x)
        return out
    return {
        "pathologies": uniq(pathologies),
        "drapeaux_rouges": uniq(drapeaux),
        "pieges": uniq(pieges)[:8],
    }


def specialite_disponible(item, apercu):
    """Une spécialité est disponible dès qu'un contenu jouable a été produit."""
    if apercu and apercu.get("pathologies"):
        return True
    if item.get("statut") == "poussé" and (item.get("couvertes") or 0) not in (None, 0, "0"):
        return True
    return False


# ---------- commandes ----------

def cmd_status(etat):
    items = etat["items"]
    joueur = joueur_items(etat)
    n_dispo = 0
    lignes = []
    lignes.append(f"Mis à jour : {etat.get('mis_a_jour', '?')}")
    lignes.append(f"Entrées du chantier : {len(items)}.")
    lignes.append(
        f"Spécialités et disciplines du catalogue joueur : {len(joueur)} "
        "(le plan en compte 63, pas 45)."
    )
    par_statut = {}
    for it in items:
        par_statut.setdefault(it["statut"], 0)
        par_statut[it["statut"]] += 1
    lignes.append(
        "Statuts du chantier : "
        + ", ".join(f"{s} {par_statut.get(s, 0)}" for s in STATUTS)
        + "."
    )
    lignes.append("")
    groupe_lib = {g: lib for g, lib, _ in GROUPES}
    courant = None
    for it in items:
        if it["groupe"] != courant:
            courant = it["groupe"]
            lignes.append(f"## {groupe_lib.get(courant, courant)}")
        extra = ""
        if it.get("dans_catalogue_joueur"):
            apercu = extraire_apercu(it.get("data_systeme"), it.get("id"))
            dispo = specialite_disponible(it, apercu)
            if dispo:
                n_dispo += 1
            extra = " · joueur : " + ("disponible" if dispo else "à venir")
        cov = fmt_nb(it.get("couvertes"))
        tot = fmt_nb(it.get("total"))
        lignes.append(
            f"- {it['id']} — {it['nom']} : {it['statut']} "
            f"(couvertes {cov} / total {tot}, urgence {fmt_nb(it.get('urgence'))}, "
            f"consultation {fmt_nb(it.get('consultation'))}, "
            f"À vérifier {fmt_nb(it.get('a_verifier'))}, "
            f"commit {it.get('commit') or '—'}, "
            f"planche {it.get('planche') or '—'}){extra}"
        )
    lignes.append("")
    lignes.append(f"Catalogue joueur : {n_dispo} / {len(joueur)} disponible(s).")
    print("\n".join(lignes))
    return 0


def _parse_optional_int(raw, nom):
    if raw is None:
        return None, False  # unchanged
    if isinstance(raw, int):
        return raw, True
    s = str(raw).strip()
    if s in ("", "à établir", "a etablir", "null", "none", "-"):
        return None, True
    try:
        return int(s), True
    except ValueError:
        raise SystemExit(f"Valeur invalide pour {nom} : {raw!r} (nombre entier ou « à établir »).")


def cmd_set(etat, args):
    it = trouver(etat, args.specialite)
    if not it:
        connus = ", ".join(i["id"] for i in etat["items"])
        raise SystemExit(f"Spécialité inconnue : {args.specialite}. Identifiants : {connus}.")
    if args.statut:
        cle = args.statut.strip().lower()
        statut = STATUT_ALIAS.get(cle) or STATUT_ALIAS.get(args.statut.strip())
        if statut is None:
            raise SystemExit(
                f"Statut invalide : {args.statut}. "
                f"Choisis parmi : {', '.join(STATUTS)} (tu peux écrire à-faire, en-cours)."
            )
        it["statut"] = statut
    mapping = {
        "couvertes": args.couvertes,
        "total": args.total,
        "urgence": args.urgence,
        "consultation": args.consultation,
    }
    for champ, brut in mapping.items():
        val, changed = _parse_optional_int(brut, champ)
        if changed:
            it[champ] = val
    if args.a_verifier is not None:
        s = args.a_verifier.strip()
        it["a_verifier"] = None if s in ("", "à établir", "a etablir", "null", "none", "-") else s
    if args.commit is not None:
        it["commit"] = args.commit.strip() or None
    if args.planche is not None:
        it["planche"] = args.planche.strip() or None
    if args.notes is not None:
        it["notes"] = args.notes
    enregistrer(etat)
    render(etat)
    print(f"Mis à jour : {it['id']} ({it['nom']}), statut « {it['statut']} ».")
    return 0


def cmd_next(etat):
    """Affiche la prochaine entrée à produire et les consignes de reprise."""
    print("## REPRISE")
    print(etat.get("consignes_reprise", "").strip())
    print()
    # On poursuit d'abord ce qui est « en cours », sinon le premier « à faire »
    # dans l'ordre du plan (moteur, puis lots A–G, etc.).
    en_cours = [i for i in etat["items"] if i["statut"] == "en cours"]
    a_faire = [i for i in etat["items"] if i["statut"] == "à faire"]
    cible = en_cours[0] if en_cours else (a_faire[0] if a_faire else None)
    if not cible:
        print("Rien n'attend : toutes les entrées sont auditées ou poussées.")
        return 0
    print("## Prochaine entrée")
    print(f"Identifiant : {cible['id']}")
    print(f"Nom : {cible['nom']}")
    print(f"Groupe : {cible['groupe']}")
    print(f"Statut : {cible['statut']}")
    if cible.get("notes"):
        print(f"Notes : {cible['notes']}")
    print()
    print(
        "Consignes : n'ouvre aucun cours ni aucun LOT. Appuie-toi seulement sur les "
        "sociétés savantes, universités et facultés suisses. Couvre chaque pathologie "
        "retenue par PROFILES (liste publique), avec un cas Urgence et un cas Consultation "
        "pour les pathologies fréquentes ou graves. Marque « À vérifier » toute affirmation "
        "sans source lue et datée. N'invente aucun total. Quand l'audit est vert, lance :"
    )
    print(
        f"  python3 jeu-revision/tools/progression.py set {cible['id']} "
        "--statut audité --couvertes N --total N --urgence N --consultation N "
        "--a-verifier X --commit H --planche planches/<id>.html"
    )
    print("  python3 jeu-revision/tools/progression.py render")
    print("Puis attends le feu vert de Grok Bot avant de pousser sur main.")
    return 0


# ---------- rendus ----------

def render(etat):
    MD_PATH.write_text(rendre_markdown(etat), encoding="utf-8")
    HTML_PATH.write_text(rendre_catalogue_joueur(etat), encoding="utf-8")
    print(f"Régénéré : {MD_PATH.relative_to(ROOT.parent)}")
    print(f"Régénéré : {HTML_PATH.relative_to(ROOT.parent)}")
    joueur = joueur_items(etat)
    if len(joueur) != 63:
        print(
            f"ATTENTION : le catalogue joueur compte {len(joueur)} entrées, pas 63. "
            "Vérifie CATALOGUE_ITEMS.",
            file=sys.stderr,
        )
        return 1
    return 0


def rendre_markdown(etat):
    groupe_lib = {g: lib for g, lib, _ in GROUPES}
    joueur = joueur_items(etat)
    n_dispo = 0
    for it in joueur:
        if specialite_disponible(it, extraire_apercu(it.get("data_systeme"), it.get("id"))):
            n_dispo += 1
    lignes = []
    lignes.append("# Catalogue de production · INTERNAT")
    lignes.append("")
    lignes.append("## REPRISE")
    lignes.append("")
    lignes.append(etat.get("consignes_reprise", "").strip())
    lignes.append("")
    lignes.append(
        "Commandes du script : `python3 jeu-revision/tools/progression.py status` · "
        "`next` · `set <id> --statut …` · `render`. "
        "La source de vérité est `docs/progression.json` ; ce fichier Markdown est régénéré, "
        "ne l'édite pas à la main."
    )
    lignes.append("")
    lignes.append(f"Dernière mise à jour : {maintenant_lisible()}.")
    lignes.append("")
    lignes.append("## Dénombrement")
    lignes.append("")
    lignes.append(
        f"Le plan de production (lots A à G, paraclinique, transversales, sciences fondamentales) "
        f"compte **{len(joueur)}** spécialités et disciplines, **pas 45**. "
        "Le détail figure ci-dessous, groupé comme dans PLAN_PRODUCTION.md. "
        "La Phase 0, la veille et l'examen blanc s'ajoutent au chantier mais n'entrent pas "
        "dans le compteur joueur."
    )
    lignes.append("")
    lignes.append(
        f"Le catalogue joueur (`catalogue.html`) affiche aujourd'hui **{n_dispo} / {len(joueur)}** "
        "spécialité(s) disponible(s)."
    )
    lignes.append("")

    for gid, lib, _ in GROUPES:
        membres = [i for i in etat["items"] if i["groupe"] == gid]
        if not membres:
            continue
        lignes.append(f"## {lib}")
        lignes.append("")
        for it in membres:
            lignes.append(f"### {it['nom']}")
            lignes.append("")
            lignes.append(f"- Identifiant : `{it['id']}`.")
            lignes.append(f"- Statut : {it['statut']}.")
            lignes.append(
                f"- Pathologies couvertes : {fmt_nb(it.get('couvertes'))} "
                f"sur un total visé de {fmt_nb(it.get('total'))}."
            )
            lignes.append(
                f"- Cas Urgence : {fmt_nb(it.get('urgence'))}. "
                f"Cas Consultation : {fmt_nb(it.get('consultation'))}."
            )
            lignes.append(f"- Taux « À vérifier » : {fmt_nb(it.get('a_verifier'))}.")
            if it.get("commit"):
                sha = it["commit"]
                url = f"https://github.com/vialdjoukang-spec/organigramme-examen-federal/commit/{sha}"
                lignes.append(f"- Commit : [`{sha}`]({url}).")
            else:
                lignes.append("- Commit : aucun pour l'instant.")
            if it.get("planche"):
                lignes.append(f"- Planche : `{it['planche']}`.")
            else:
                lignes.append("- Planche : pas encore produite.")
            if it.get("notes"):
                lignes.append(f"- Notes : {it['notes']}")
            lignes.append("")
    return "\n".join(lignes) + "\n"


def _esc(s):
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def rendre_catalogue_joueur(etat):
    joueur = joueur_items(etat)
    total = len(joueur)
    apercus = {}
    n_dispo = 0
    for it in joueur:
        ap = extraire_apercu(it.get("data_systeme"), it.get("id"))
        apercus[it["id"]] = ap
        if specialite_disponible(it, ap):
            n_dispo += 1

    groupes_html = []
    for gid, lib, flag in GROUPES:
        if not flag:
            continue
        membres = [i for i in joueur if i["groupe"] == gid]
        cartes = []
        for it in membres:
            ap = apercus.get(it["id"])
            dispo = specialite_disponible(it, ap)
            if dispo and ap:
                pathos = "".join(f"<li>{_esc(p)}</li>" for p in ap["pathologies"])
                draps = "".join(f"<li>{_esc(d)}</li>" for d in ap["drapeaux_rouges"])
                pieges = "".join(f"<li>{_esc(p)}</li>" for p in ap["pieges"])
                apercu_html = f"""
        <div class="apercu">
          <h4>Pathologies couvertes</h4>
          <ul>{pathos}</ul>
          <h4>Drapeaux rouges</h4>
          <ul>{draps or '<li>Aucun drapeau rouge n’a encore été saisi dans les cartes produites.</li>'}</ul>
          <h4>Pièges</h4>
          <ul>{pieges or '<li>Aucun piège sourcé n’a encore été saisi dans les cartes produites.</li>'}</ul>
        </div>"""
                bouton = (
                    f'<a class="arene" href="index.html?specialite={_esc(it["id"])}">'
                    "Entrer dans l'Arène</a>"
                )
                statut = "disponible"
            else:
                apercu_html = (
                    '<p class="attente">Cette spécialité arrive bientôt. '
                    "L'aperçu restera vide tant qu'aucun cas sourcé n'est produit : "
                    "rien n'est inventé ici.</p>"
                )
                bouton = (
                    '<button class="arene arene-off" type="button" disabled>'
                    "L'Arène ouvrira ici</button>"
                )
                statut = "à venir"
            cartes.append(f"""
      <article class="carte statut-{statut}" id="{_esc(it['id'])}">
        <header>
          <h3>{_esc(it['nom'])}</h3>
          <p class="badge badge-{statut}">{_esc(statut)}</p>
        </header>
        {apercu_html}
        <p class="action">{bouton}</p>
      </article>""")
        groupes_html.append(
            f'<section class="lot" id="{_esc(gid)}">'
            f"<h2>{_esc(lib)}</h2>"
            f'<div class="grille">{"".join(cartes)}</div>'
            f"</section>"
        )

    css = """
:root {
  --fond: #f5f6f8; --papier: #fff; --encre: #101828; --encre-2: #344054; --encre-3: #5d6b82;
  --trait: #d9dee7; --urgence: #b42318; --calme: #1d4e89; --calme-fond: #eef4fb;
  --bon: #0e7a3b; --bon-fond: #ecfaf1; --attention: #a14a06; --attention-fond: #fff6ea;
  --police: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}
* { box-sizing: border-box; }
html { font-size: 18px; }
body { margin: 0; font-family: var(--police); color: var(--encre); background:
  radial-gradient(1200px 500px at 10% -10%, #e8eef8, transparent 60%),
  radial-gradient(800px 400px at 100% 0%, #f8efe8, transparent 50%), var(--fond);
  line-height: 1.5; }
header.haut { max-width: 1120px; margin: 0 auto; padding: 2rem 1.25rem 1rem; }
.marque { display: flex; align-items: baseline; gap: .6rem; flex-wrap: wrap; }
.marque-logo { display: inline-grid; place-items: center; width: 2rem; height: 2rem;
  border-radius: 8px; background: var(--calme); color: #fff; font-weight: 700; }
.marque-nom { font-weight: 700; font-size: 1.4rem; letter-spacing: -.02em; }
.marque-lien { color: var(--calme); }
h1 { font-size: clamp(1.8rem, 3vw, 2.4rem); margin: 1rem 0 .4rem; letter-spacing: -.03em; }
.accroche { color: var(--encre-2); max-width: 46rem; }
.compteur { display: inline-flex; align-items: baseline; gap: .35rem; margin: 1.2rem 0;
  padding: .55rem 1rem; background: var(--papier); border: 1px solid var(--trait);
  border-radius: 999px; box-shadow: 0 1px 3px rgba(16,24,40,.06); }
.compteur .n { font-size: 1.8rem; font-weight: 750; color: var(--calme); }
.compteur .sep { color: var(--encre-3); }
nav.ancres { display: flex; flex-wrap: wrap; gap: .4rem; margin: 1rem 0 0; }
nav.ancres a { font-size: .85rem; color: var(--calme); text-decoration: none;
  border: 1px solid var(--trait); background: var(--papier); padding: .25rem .6rem; border-radius: 999px; }
nav.ancres a:hover { border-color: var(--calme); }
main { max-width: 1120px; margin: 0 auto; padding: 0 1.25rem 3rem; }
section.lot { margin-top: 2.2rem; }
section.lot h2 { font-size: 1.15rem; margin: 0 0 .8rem; padding-bottom: .4rem;
  border-bottom: 2px solid var(--calme); }
.grille { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1rem; }
.carte { background: var(--papier); border: 1px solid var(--trait); border-radius: 14px;
  padding: 1rem 1rem .9rem; display: flex; flex-direction: column; gap: .6rem;
  box-shadow: 0 1px 2px rgba(16,24,40,.05); }
.carte header { display: flex; justify-content: space-between; gap: .6rem; align-items: start; }
.carte h3 { margin: 0; font-size: 1.05rem; }
.badge { margin: 0; font-size: .75rem; font-weight: 650; text-transform: uppercase;
  letter-spacing: .04em; padding: .15rem .5rem; border-radius: 999px; white-space: nowrap; }
.badge-disponible { background: var(--bon-fond); color: var(--bon); }
.badge-a { } /* placeholder */
.badge-à, .badge-à\\ venir, .badge-àvenir { background: var(--attention-fond); color: var(--attention); }
.badge-àvenir, .carte.statut-à\\ venir .badge, .carte[class*="venir"] .badge { background: var(--attention-fond); color: var(--attention); }
.apercu { font-size: .92rem; color: var(--encre-2); }
.apercu h4 { margin: .6rem 0 .2rem; font-size: .8rem; text-transform: uppercase;
  letter-spacing: .04em; color: var(--encre-3); }
.apercu ul { margin: 0; padding-left: 1.1rem; }
.apercu li { margin: .15rem 0; }
.attente { color: var(--encre-3); font-size: .95rem; margin: 0; flex: 1; }
.action { margin: auto 0 0; }
.arene { display: inline-block; text-decoration: none; background: var(--calme); color: #fff;
  font-weight: 650; padding: .5rem 0.9rem; border-radius: 10px; border: 0; font-size: .95rem; }
.arene:hover { filter: brightness(1.08); }
.arene-off { background: #98a2b3; color: #fff; cursor: not-allowed; }
pied, footer.pied { max-width: 1120px; margin: 0 auto; padding: 0 1.25rem 2.5rem;
  color: var(--encre-3); font-size: .9rem; }
footer.pied a { color: var(--calme); }
@media (prefers-reduced-motion: reduce) { * { transition: none !important; animation: none !important; } }
"""
    # Fix badge for "à venir" - use a class without special chars
    # I'll use statut-disponible / statut-avenir in the HTML instead

    # Wait I already used statut-{statut} with "à venir" and "disponible".
    # Let me fix: use statut-disponible and statut-avenir

    html_groupes = "\n".join(groupes_html)
    # post-process class names
    html_groupes = html_groupes.replace("statut-à venir", "statut-avenir")
    html_groupes = html_groupes.replace("badge-à venir", "badge-avenir")

    ancres = []
    for gid, lib, flag in GROUPES:
        if flag:
            court = lib.split("·", 1)[-1].strip()
            ancres.append(f'<a href="#{_esc(gid)}">{_esc(court)}</a>')

    page = f"""<!doctype html>
<html lang="fr-CH">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Catalogue · Internat — {n_dispo} / {total}</title>
  <meta name="description" content="Catalogue des spécialités du jeu de révision INTERNAT. Parcours chaque salle, lis l'aperçu d'une minute, puis entre dans l'Arène.">
  <style>{css}
  .badge-avenir {{ background: var(--attention-fond); color: var(--attention); }}
  </style>
</head>
<body>
  <header class="haut">
    <p class="marque">
      <span class="marque-logo" aria-hidden="true">+</span>
      <span class="marque-nom">Internat</span>
      <a class="marque-lien" href="index.html">Retour au jeu</a>
      ·
      <a class="marque-lien" href="https://vialdjoukang-spec.github.io/organigramme-examen-federal/veille/">Veille</a>
    </p>
    <h1>Le catalogue des salles</h1>
    <p class="accroche">Parcours les spécialités et les disciplines du plan. Pour chaque salle disponible, lis l'aperçu en une minute — pathologies couvertes, drapeaux rouges et pièges, tirés seulement du contenu déjà produit et sourcé — puis entre dans l'Arène.</p>
    <p class="compteur" aria-live="polite">
      <span class="n">{n_dispo}</span>
      <span class="sep">/</span>
      <span class="n">{total}</span>
      <span>salle{'' if total == 1 else 's'} — {n_dispo} ouverte{'' if n_dispo == 1 else 's'}</span>
    </p>
    <nav class="ancres" aria-label="Lots">{''.join(ancres)}</nav>
  </header>
  <main>
    {html_groupes}
  </main>
  <footer class="pied">
    <p>Ce catalogue compte les {total} spécialités et disciplines du plan (lots A à G, paraclinique, disciplines transversales, sciences fondamentales). Il n'en compte pas 45. La Phase 0, la veille et l'examen blanc restent dans le <a href="docs/CATALOGUE_PRODUCTION.md">catalogue de production</a>.</p>
    <p>L'aperçu d'une salle reste vide tant qu'aucun cas sourcé n'est produit. Rien n'est inventé. Prototype pédagogique : il ne remplace ni un protocole local ni l'avis d'un médecin.</p>
  </footer>
</body>
</html>
"""
    return page


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("status", help="Affiche l'état de toutes les spécialités.")
    sub.add_parser("next", help="Affiche la prochaine spécialité à produire et les consignes de reprise.")
    sub.add_parser("render", help="Régénère CATALOGUE_PRODUCTION.md et catalogue.html.")

    sp = sub.add_parser("set", help="Met à jour une spécialité, puis régénère les catalogues.")
    sp.add_argument("specialite", help="Identifiant (ex. cardiologie)")
    sp.add_argument("--statut", metavar="STATUT",
                    help="à-faire | en-cours | audité | poussé (tu peux aussi écrire « à faire » entre guillemets)")
    sp.add_argument("--couvertes", default=None)
    sp.add_argument("--total", default=None)
    sp.add_argument("--urgence", default=None)
    sp.add_argument("--consultation", default=None)
    sp.add_argument("--a-verifier", dest="a_verifier", default=None)
    sp.add_argument("--commit", default=None)
    sp.add_argument("--planche", default=None)
    sp.add_argument("--notes", default=None)

    args = p.parse_args(argv)
    etat = charger()
    # Garantit que les 63 + annexes existent (n'écrase pas l'état déjà saisi).
    connus = {i["id"] for i in etat["items"]}
    for row in CATALOGUE_ITEMS:
        if row[0] not in connus:
            etat["items"].append(item_vierge(*row))
            connus.add(row[0])
    if args.cmd == "status":
        return cmd_status(etat)
    if args.cmd == "next":
        return cmd_next(etat)
    if args.cmd == "render":
        return render(etat)
    if args.cmd == "set":
        return cmd_set(etat, args)
    return 1


if __name__ == "__main__":
    sys.exit(main())

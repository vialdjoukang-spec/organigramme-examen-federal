#!/usr/bin/env python3
"""Conscience embarquée du rédacteur — zéro jeton, déterministe, pas un audit.

Trois consciences, après chaque fichier (ou section), avant certitude_redaction.py
et avant porte_zero_jeton.py :

  conscience linguistique   formes, sigles, unités
  conscience médicale       cohérence, définitions, seuils, éléments centraux
  conscience posologique    doses lues contre le cache AIPS local

  python3 grok-LOTS-html/outils/conscience/conscience.py fichier <fichier.html>
  python3 grok-LOTS-html/outils/conscience/conscience.py lot <LOT_XXX>
  python3 grok-LOTS-html/outils/conscience/conscience.py fichier <fichier.html> --ancre p11

Code de sortie : 0 aucun BLOQUANT · 1 au moins un BLOQUANT · 2 usage.
N'écrit rien. Ne appelle aucun modèle. Sortie plafonnée à 30 lignes
(priorité aux BLOQUANT). --tout affiche tout, pour la mesure.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import subprocess
import sys
import time
import unicodedata
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path

ICI = Path(__file__).resolve().parent
DONNEES = ICI / "donnees"
PLAFOND_LIGNES = 30
FACTEUR = 3.12

_PAS_MOLECULE = {
    "prevention", "sommaire", "definition", "epidemiologie", "demarche", "pieges", "respecter",
    "femme", "douleur", "arbre", "instable", "physiologie", "physiopathologie", "anamnese",
    "diagnostic", "examen", "examens", "conduite", "indication", "intervalle", "plafond",
    "adulte", "chronique", "traitement", "sources", "points", "prise", "charge", "essentiel",
    "alerte", "urgence", "prevenir", "prevention", "philadelphie", "chromosome", "femme",
    "homme", "enfant", "enfants", "grossesse", "contre", "indication", "informations",
    "professionnelle", "comprime", "comprimes", "dose", "doses", "maximale", "quotidienne",
}

STOP_NOM = {
    "suisse", "revue", "information", "comprimé", "comprimés", "adulte", "enfant",
    "dose", "plafond", "intervalle", "clairance", "maladie", "points", "sources",
    "numéro", "swissmedic", "phase", "définition", "prise", "charge", "fenêtre",
    "texte", "lecture", "selon", "après", "avant", "cette", "dans", "pour", "avec",
    "sans", "plus", "moins", "comme", "entre", "toute", "tous", "leur", "leurs",
    "patient", "patiente", "patients", "médecin", "médicale", "médical",
}


@dataclass
class Ordre:
    priorite: int
    niveau: str
    conscience: str
    ligne: int
    texte: str
    gravite: str
    cle: str = ""


@dataclass
class Resultat:
    ordres: list[Ordre] = field(default_factory=list)
    secondes: float = 0.0
    orthographe_externe: str = "inactive"


def racine_depot() -> Path:
    for p in [ICI, *ICI.parents]:
        if (p / "LOT_Claude_Finaux" / "CATALOGUE_248.csv").exists():
            return p
    return ICI.parents[3]


def charger(nom: str):
    return json.loads((DONNEES / nom).read_text(encoding="utf-8"))


def ssp_catalogue(lot: str) -> tuple[str, str]:
    """Code SSP et intitulé, lus dans le catalogue (le brief de contexte_lot s'en sert)."""
    m = re.search(r"(\d+)", lot or "")
    if not m:
        return "", ""
    num = str(int(m.group(1)))
    chemin = racine_depot() / "LOT_Claude_Finaux" / "CATALOGUE_248.csv"
    if not chemin.exists():
        return "", ""
    with chemin.open(encoding="utf-8", errors="replace", newline="") as h:
        for r in csv.DictReader(h):
            cle = (r.get("lot") or "").strip()
            if cle == num or cle.lstrip("0") == num:
                return (r.get("code") or "").strip(), (r.get("ssp_profiles_2023_fr_en") or "").strip()
    return "", ""


class _Corps(HTMLParser):
    """Texte pédagogique. Les fenêtres popover (citations) sont sautées."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.abbr: list[str] = []
        self.skip = 0
        self._titre_abbr = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.skip:
            self.skip += 1
            return
        if tag == "div" and "popover" in a:
            self.skip = 1
            return
        if tag in ("style", "script", "svg"):
            self.skip = 1
            return
        if tag == "abbr":
            self._titre_abbr = a.get("title") or ""
        if tag in ("p", "li", "h1", "h2", "h3", "br", "tr"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if self.skip:
            self.skip -= 1
            return
        if tag == "abbr" and self._titre_abbr:
            self.abbr.append(self._titre_abbr)
            self._titre_abbr = ""

    def handle_data(self, data):
        if not self.skip and data:
            self.parts.append(data)


def decouper(html: str, ancre: str | None) -> str:
    if not ancre:
        return html
    m = re.search(rf'\bid\s*=\s*["\']{re.escape(ancre)}["\']', html)
    if not m:
        return html
    reste = html[m.start():]
    nxt = re.search(r"<section\b", reste[20:])
    return reste[: nxt.start() + 20] if nxt else reste


def corps_de(html: str, ancre: str | None = None) -> tuple[str, str]:
    frag = decouper(html, ancre)
    p = _Corps()
    try:
        p.feed(frag)
    except Exception:
        p.parts.append(re.sub(r"<[^>]+>", " ", frag))
    texte = re.sub(r"[ \t]+", " ", "".join(p.parts))
    texte = re.sub(r"\n{2,}", "\n", texte)
    return texte, "\n".join(p.abbr)


def titre_de(html: str) -> str:
    m = re.search(r"<h1\b[^>]*>(.*?)</h1>", html, re.I | re.S)
    if not m:
        return ""
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1))).strip()


def ligne_de(brut: str, extrait: str) -> int:
    e = re.sub(r"\s+", " ", extrait).strip()[:42]
    if len(e) < 4:
        return 0
    for i, lig in enumerate(brut.splitlines(), 1):
        plat = re.sub(r"<[^>]+>", "", lig)
        plat = re.sub(r"\s+", " ", plat)
        if e in lig or e in plat:
            return i
    return 0


def nombre(s: str) -> float:
    t = s.replace("\u00a0", "").replace(" ", "").replace("'", "").replace("’", "").replace(",", ".")
    return float(t)


def _ajouter(sac: list[Ordre], vus: set[str], o: Ordre) -> None:
    if o.cle in vus:
        return
    vus.add(o.cle)
    sac.append(o)


def conscience_linguistique(texte: str, abbr: str, brut: str, sac: list[Ordre], vus: set[str]) -> None:
    lex = charger("lexique_formes.json")
    for forme in lex["formes"]:
        flags = 0 if forme.get("casses") else re.I
        for m in re.finditer(forme["motif"], texte, flags):
            vu = m.group(0)
            _ajouter(sac, vus, Ordre(
                3, "SIGNAL", "conscience linguistique", ligne_de(brut, vu),
                f"CORRIGER « {vu} » → « {forme['correction']} » ({forme['pourquoi']}).",
                "mineure", f"lex:{forme['motif']}:{m.start()}",
            ))
            break
    # Unités : espace manquant, µg, mmol/l. Pas d'insécable exigé à chaque fois (bruit).
    colles = list(re.finditer(r"\d(?:mg|µg|μg|mcg|mmol|%)\b", texte))
    if colles:
        ex = colles[0].group(0)
        _ajouter(sac, vus, Ordre(
            3, "SIGNAL", "conscience linguistique", ligne_de(brut, ex),
            f"CORRIGER l'unité collée « {ex} » : espace avant l'unité ({len(colles)} fois dans le corps).",
            "mineure", "unite:collee",
        ))
    mcg = list(re.finditer(r"\d(?:[ \u00a0])?(?:mcg|ug)\b", texte, re.I))
    if mcg:
        _ajouter(sac, vus, Ordre(
            3, "SIGNAL", "conscience linguistique", ligne_de(brut, mcg[0].group(0)),
            f"CORRIGER « {mcg[0].group(0).strip()} » → µg ({len(mcg)} fois).",
            "mineure", "unite:mcg",
        ))
    if re.search(r"mmol/L", texte):
        _ajouter(sac, vus, Ordre(
            3, "SIGNAL", "conscience linguistique", ligne_de(brut, "mmol/L"),
            "CORRIGER mmol/L → mmol/l (symbole SI, litre minuscule).",
            "mineure", "unite:mmolL",
        ))
    sigles = charger("sigles.json")["sigles"]
    developpe = (texte + "\n" + abbr).lower()
    nus = []
    for s in sigles:
        sig = s["sigle"]
        if s.get("sauf_prefixe"):
            motif = rf"(?<!{s['sauf_prefixe']}){re.escape(sig)}\b"
        else:
            motif = rf"\b{re.escape(sig)}\b"
        if not re.search(motif, texte):
            continue
        if any(d.lower() in developpe for d in s["developpements"]):
            continue
        nus.append(sig)
    if nus:
        _ajouter(sac, vus, Ordre(
            3, "SIGNAL", "conscience linguistique", 0,
            "CORRIGER sigles non développés dans le corps ni dans un abbr : " + ", ".join(nus[:8]) + ".",
            "mineure", "sigles",
        ))
    for o in orthographe_externe(texte):
        _ajouter(sac, vus, o)


def orthographe_disponible() -> str:
    if not shutil.which("hunspell"):
        return "hunspell absent"
    if not Path("/usr/share/hunspell/fr_FR.dic").exists() and not Path("/usr/share/hunspell/fr.dic").exists():
        return "hunspell sans dictionnaire français (hunspell-fr non installé)"
    return "hunspell-fr"


def orthographe_externe(texte: str) -> list[Ordre]:
    """Option libre. Inactive si le dictionnaire français n'est pas là. Aucun appel réseau."""
    if orthographe_disponible() != "hunspell-fr":
        return []
    dic = "fr_FR" if Path("/usr/share/hunspell/fr_FR.dic").exists() else "fr"
    mots = sorted({m for m in re.findall(r"\b[A-Za-zÀ-ÿ]{5,}\b", texte) if m.lower() not in STOP_NOM})
    if not mots:
        return []
    try:
        r = subprocess.run(
            ["hunspell", "-d", dic, "-l"],
            input="\n".join(mots[:400]),
            capture_output=True, text=True, timeout=2,
        )
    except (subprocess.SubprocessError, OSError):
        return []
    inconnus = [l.strip() for l in r.stdout.splitlines() if l.strip()][:5]
    if not inconnus:
        return []
    return [Ordre(
        3, "SIGNAL", "conscience linguistique", 0,
        "CORRIGER orthographe à vérifier (hunspell-fr) : " + ", ".join(inconnus) + ".",
        "mineure", "hunspell",
    )]


def _valeur_hors(regle: dict, valeur: float) -> bool:
    return valeur < float(regle["min"]) or valeur > float(regle["max"])


def conscience_medicale(texte: str, titre: str, ssp: str, corps_lot: str, inclure_lot: bool,
                        brut: str, sac: list[Ordre], vus: set[str]) -> None:
    bornes = charger("bornes.json")
    for reg in bornes["regles"]:
        if "motif" in reg and "nombre_avant" not in reg and "motif_nombre" not in reg:
            for m in re.finditer(reg["motif"], texte, re.I):
                if reg.get("contexte"):
                    fen = texte[max(0, m.start() - 40): m.end() + 12]
                    if not re.search(reg["contexte"], fen, re.I):
                        continue
                try:
                    val = nombre(m.group(1))
                except ValueError:
                    continue
                if _valeur_hors(reg, val):
                    _ajouter(sac, vus, Ordre(
                        0, "BLOQUANT", "conscience médicale", ligne_de(brut, m.group(0)),
                        f"CORRIGER {reg['nom']} {m.group(0).strip()} hors plage de plausibilité "
                        f"{reg['min']}–{reg['max']} {reg.get('unite', '')} (À vérifier comme seuil clinique ; ici seulement l'impossible).".replace("  ", " "),
                        "critique", f"borne:{reg['id']}:{m.start()}",
                    ))
                    break
        elif "nombre_avant" in reg:
            for m in re.finditer(reg["nombre_avant"], texte, re.I):
                fen = texte[max(0, m.start() - 40): m.end() + 5]
                if not re.search(reg["contexte"], fen, re.I):
                    continue
                avant = texte[max(0, m.start() - 16): m.start()]
                nm = re.search(r"(\d+(?:[.,]\d+)?)\s*$", avant)
                if not nm:
                    continue
                try:
                    val = nombre(nm.group(1))
                except ValueError:
                    continue
                if _valeur_hors(reg, val):
                    _ajouter(sac, vus, Ordre(
                        0, "BLOQUANT", "conscience médicale", ligne_de(brut, nm.group(1)),
                        f"CORRIGER {reg['nom']} {nm.group(1)} hors plage de plausibilité {reg['min']}–{reg['max']} (À vérifier comme seuil clinique).",
                        "critique", f"borne:{reg['id']}:{m.start()}",
                    ))
                    break
        elif "motif_nombre" in reg:
            for m in re.finditer(reg["motif_nombre"], texte, re.I):
                fen = texte[max(0, m.start() - 40): m.end() + 5]
                if not re.search(reg["contexte"], fen, re.I):
                    continue
                try:
                    val = nombre(m.group(1))
                except ValueError:
                    continue
                if _valeur_hors(reg, val):
                    _ajouter(sac, vus, Ordre(
                        0, "BLOQUANT", "conscience médicale", ligne_de(brut, m.group(0)),
                        f"CORRIGER {reg['nom']} {m.group(0).strip()} hors plage {reg['min']}–{reg['max']}.",
                        "critique", f"borne:{reg['id']}:{m.start()}",
                    ))
                    break
    # Même dénominateur cité deux fois (14/100 et 14/1 000).
    mil = set(re.findall(r"\b(\d+)\s*/\s*(?:1[\s\u00a0'’]?000|1000)\b", texte))
    cen = set(re.findall(r"\b(\d+)\s*/\s*100(?!\d)(?![\s\u00a0'’]*000)\b", texte))
    for n in sorted(mil & cen):
        _ajouter(sac, vus, Ordre(
            1, "SIGNAL", "conscience médicale", 0,
            f"CORRIGER cohérence : {n}/100 et {n}/1 000 figurent tous les deux — un seul dénominateur, sourcé.",
            "grave", f"den:{n}",
        ))
    # Définitions minimales de deux scores souvent confondus. Pas un glossaire général.
    if re.search(r"(?<!q)\bSOFA\b", texte) and not re.search(r"défaillance|sequential organ", texte, re.I):
        _ajouter(sac, vus, Ordre(
            1, "SIGNAL", "conscience médicale", ligne_de(brut, "SOFA"),
            "CORRIGER définition : SOFA est utilisé sans dire que c'est un score de défaillance d'organes.",
            "grave", "def:SOFA",
        ))
    if re.search(r"\bqSOFA\b", texte) and not re.search(r"dépist|au lit|quick sequential", texte, re.I):
        _ajouter(sac, vus, Ordre(
            1, "SIGNAL", "conscience médicale", ligne_de(brut, "qSOFA"),
            "CORRIGER définition : qSOFA est utilisé sans dire que c'est un dépistage au lit.",
            "grave", "def:qSOFA",
        ))
    # Formulation qui fait opérer sur le seul Alvarado, sans la réserve.
    if re.search(r"Alvarado", texte) and re.search(r"stratégie opératoire|autorise à opérer", texte, re.I):
        if not re.search(r"n['’]autorise pas|déconseille|pas suffisamment spécifique|ne pas confirmer|suggest against", texte, re.I):
            _ajouter(sac, vus, Ordre(
                1, "SIGNAL", "conscience médicale", ligne_de(brut, "Alvarado"),
                "CORRIGER : Alvarado cité avec une stratégie opératoire sans la réserve (ne confirme pas chez l'adulte) — sourcer plutôt que laisser la phrase seule.",
                "grave", "alvarado",
            ))
    elements = charger("elements_centraux.json")["ssp"].get(ssp or "", [])
    titre_n = unicodedata.normalize("NFC", titre or "").lower()
    for el in elements:
        if el.get("ou") == "lot" and not inclure_lot:
            continue
        if el.get("ou") == "dx":
            mots = [m.lower() for m in el.get("titre", [])]
            if not any(m in titre_n for m in mots):
                continue
        if any(s.lower() in titre_n for s in el.get("titre_sauf", [])):
            continue
        cible = corps_lot if el.get("ou") == "lot" else texte
        def _present(p: str, cible: str) -> bool:
            return re.search(r"(?<!\d)" + re.escape(p), cible) is not None

        if el.get("presence_toutes"):
            ok = all(_present(p, cible) for p in el["presence_toutes"])
        elif el.get("presence_regex"):
            ok = any(re.search(p, cible, re.I | re.S) for p in el["presence_regex"])
        else:
            ok = any(_present(p, cible) for p in el.get("presence", []))
        if not ok:
            _ajouter(sac, vus, Ordre(
                1, "SIGNAL", "conscience médicale", 0,
                el["ordre"] + ".",
                "grave", f"elt:{el['id']}",
            ))


_DOSE = re.compile(
    r"(?P<a>\d{1,3}(?:[ \u00a0'’]\d{3})+|\d+(?:[.,]\d+)?)"
    r"(?:\s*(?:à|-|–|—)\s*(?P<b>\d{1,3}(?:[ \u00a0'’]\d{3})+|\d+(?:[.,]\d+)?))?"
    r"\s*(?P<unit>µg|μg|mcg|ug|mg|g|UI)\b",
    re.I,
)


def _unite(u: str) -> str:
    u = u.lower().replace("μ", "µ")
    if u in ("mcg", "ug"):
        return "µg"
    return u


def _en_mg(amount: float, unit: str) -> float | None:
    if unit == "g":
        return amount * 1000
    if unit == "mg":
        return amount
    if unit == "µg":
        return amount / 1000.0
    return None


def conscience_posologique(texte: str, brut: str, sac: list[Ordre], vus: set[str]) -> None:
    data = charger("doses.json")
    mols = data["molecules"]
    alias = sorted(
        ((a.lower(), m) for m in mols for a in m["noms"]),
        key=lambda x: -len(x[0]),
    )
    try:
        spec = charger("specialites.json")["noms"]
    except (OSError, json.JSONDecodeError, KeyError):
        spec = {}
    alias_tokens = {a.split()[0] for a, _ in alias}
    sans_plage: list[str] = []
    sans_ref: list[str] = []
    for m in _DOSE.finditer(texte):
        queue = texte[m.end(): m.end() + 8]
        if re.match(r"\s*/\s*(?:dl|l|ml)\b", queue, re.I):
            continue
        try:
            vals = [nombre(m.group("a"))]
            if m.group("b"):
                vals.append(nombre(m.group("b")))
        except ValueError:
            continue
        amount = max(vals)
        unit = _unite(m.group("unit"))
        fen = texte[max(0, m.start() - 70): m.end() + 55]
        avant = texte[max(0, m.start() - 70): m.start()].lower()
        if re.search(r"n['’]écrit pas|ne pas enseigner|pas recopié|on n['’]écrit pas", avant):
            continue
        bas = fen.lower()
        mol = next((mo for al, mo in alias if al in bas), None)
        per_kg = bool(re.search(r"/\s*kg|par kilogramme|par kg", fen, re.I))
        apres = texte[m.end(): m.end() + 36]
        voisins = texte[max(0, m.start() - 48): m.end() + 36]
        prefixe = texte[max(0, m.start() - 14): m.start()]
        mult = 1
        mx = re.search(r"(\d+)\s*[x×]\s*$", prefixe, re.I)
        if mx:
            mult = int(mx.group(1))
        fx = re.search(r"\b(une|un|deux|trois|quatre|\d+)\s+fois", apres, re.I)
        if fx:
            mot = fx.group(1).lower()
            mult = {"une": 1, "un": 1, "deux": 2, "trois": 3, "quatre": 4}.get(mot, int(mot) if mot.isdigit() else 1)
        quotidien = bool(re.search(r"par jour|/j\b|journali|quotidien|journée|par 24|plafond", voisins, re.I)) or (
            mult > 1 and bool(re.search(r"par jour|fois", apres, re.I))
        )
        if mol is None:
            # Nom juste devant la dose. Un titre qui suit (« Prévention ») n'est pas une molécule.
            avant_nom = texte[max(0, m.start() - 32): m.start()]
            caps = re.findall(r"\b[A-ZÉÈÊÀÂÎÔÛ][a-zà-ÿœ-]{5,}\b", avant_nom)
            mot = ""
            if caps:
                t = caps[-1].lower()
                nu = "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn")
                if t not in STOP_NOM and t not in alias_tokens and nu not in _PAS_MOLECULE:
                    mot = t
            if mot and mot in spec and mot not in sans_plage:
                sans_plage.append(mot)
            elif mot and mot not in spec and mot not in sans_ref:
                sans_ref.append(mot)
            continue
        if unit.lower() == "ui" and (mol.get("unite") or "").lower() != "ui":
            continue
        if mol.get("plage_extraite") is False:
            etiquette = mol["noms"][0] + " (AIPS " + mol["aips"] + ", plage non extraite)"
            if etiquette not in sans_plage:
                sans_plage.append(etiquette)
            continue
        cite = f"AIPS {mol['aips']} {mol['specialite']}, corpus {data['meta']['date_corpus']}"
        if per_kg:
            if unit == "µg" and mol.get("par_kg_max_ug") is not None and amount > float(mol["par_kg_max_ug"]):
                _bloquer_dose(sac, vus, brut, m.group(0), mol, amount, unit, "par kg", mol["par_kg_max_ug"], "µg/kg", cite)
            elif mol.get("par_kg_max_mg") is not None:
                val = _en_mg(amount, unit)
                if val is not None and val > float(mol["par_kg_max_mg"]):
                    _bloquer_dose(sac, vus, brut, m.group(0), mol, amount, unit, "par kg", mol["par_kg_max_mg"], "mg/kg", cite)
            continue
        # Unité ×1000 : 500 µg de paracétamol alors que l'AIPS est en mg.
        if mol.get("unite") == "mg" and unit == "µg" and amount >= 50:
            _ajouter(sac, vus, Ordre(
                0, "BLOQUANT", "conscience posologique", ligne_de(brut, m.group(0)),
                f"CORRIGER unité : {m.group(0).strip()} pour {mol['noms'][0]}, l'AIPS {mol['aips']} est en mg — vérifier µg/mg.",
                "critique", f"unit:{mol['aips']}:{m.start()}",
            ))
            continue
        val = _en_mg(amount, unit) if mol.get("unite") == "mg" else None
        if val is None:
            if mol.get("unite") != unit:
                _ajouter(sac, vus, Ordre(
                    0, "BLOQUANT", "conscience posologique", ligne_de(brut, m.group(0)),
                    f"CORRIGER unité incohérente : {m.group(0).strip()} ({unit}) pour {mol['noms'][0]}, cache en {mol['unite']} ({cite}).",
                    "critique", f"unit2:{mol['aips']}:{m.start()}",
                ))
            continue
        total = val * (mult if quotidien and mult > 1 else 1)
        prise = mol.get("prise_max_mg")
        jour = mol.get("jour_max_mg")
        if quotidien and jour is not None and total > float(jour):
            _bloquer_dose(sac, vus, brut, m.group(0), mol, total, "mg", "par jour", jour, "mg/j", cite)
        elif not quotidien and jour is not None and val > float(jour):
            _bloquer_dose(sac, vus, brut, m.group(0), mol, val, "mg", "au-dessus du plafond journalier", jour, "mg/j", cite)
        elif not quotidien and prise is not None and val > float(prise):
            # Un total journalier écrit « 4 g » sans les mots « par jour » ne doit pas
            # être jugé comme une prise. On ne bloque que si la phrase dit « par prise »
            # ou si le nombre dépasse aussi le plafond du jour (cas précédent).
            if re.search(r"par prise", voisins, re.I) or jour is None:
                _bloquer_dose(sac, vus, brut, m.group(0), mol, val, "mg", "par prise", prise, "mg", cite)
    if sans_ref:
        _ajouter(sac, vus, Ordre(
            2, "SIGNAL", "conscience posologique", 0,
            "SIGNAL molécule dosée sans référence AIPS dans le cache : " + ", ".join(sans_ref[:4]) + ".",
            "grave", "sans-ref",
        ))
    if sans_plage:
        _ajouter(sac, vus, Ordre(
            2, "SIGNAL", "conscience posologique", 0,
            "SIGNAL spécialité dosée, plage AIPS non comparée : " + ", ".join(sans_plage[:4]) + ".",
            "grave", "sans-plage",
        ))


def _bloquer_dose(sac, vus, brut, extrait, mol, valeur, _unit, portee, plafond, uplaf, cite) -> None:
    _ajouter(sac, vus, Ordre(
        0, "BLOQUANT", "conscience posologique", ligne_de(brut, extrait.strip()[:24]),
        f"CORRIGER {mol['noms'][0]} {valeur:g} {uplaf} ({portee}) > plafond {plafond:g} {uplaf} ({cite}).",
        "critique", f"dose:{mol['aips']}:{extrait}:{portee}",
    ))


def analyser(html: str, *, lot: str = "", ssp: str = "", titre: str = "",
             chemin: str = "", corps_lot: str | None = None, inclure_lot: bool = False,
             ancre: str | None = None) -> Resultat:
    t0 = time.perf_counter()
    if not ssp and lot:
        ssp, _ = ssp_catalogue(lot)
    if not titre:
        titre = titre_de(html)
    texte, abbr = corps_de(html, None)
    texte_section = texte
    if ancre:
        texte_section, abbr_s = corps_de(html, ancre)
        abbr = abbr + "\n" + abbr_s
    if corps_lot is None:
        corps_lot = texte
    sac: list[Ordre] = []
    vus: set[str] = set()
    conscience_linguistique(texte_section, abbr, html, sac, vus)
    conscience_medicale(texte, titre, ssp, corps_lot, inclure_lot, html, sac, vus)
    conscience_posologique(texte_section, html, sac, vus)
    sac.sort(key=lambda o: (o.priorite, o.ligne or 10**9, o.cle))
    return Resultat(sac, time.perf_counter() - t0, orthographe_disponible())


def fichiers_lot(dossier: Path) -> list[Path]:
    return sorted(p for p in dossier.glob("*.html") if p.is_file())


def corps_freres(dossier: Path) -> str:
    bouts = []
    for p in fichiers_lot(dossier):
        try:
            bouts.append(corps_de(p.read_text(encoding="utf-8", errors="replace"))[0])
        except OSError:
            continue
    return "\n".join(bouts)


def formater(resultat: Resultat, entete: str, tout: bool = False) -> str:
    n_b = sum(1 for o in resultat.ordres if o.niveau == "BLOQUANT")
    n_s = len(resultat.ordres) - n_b
    lignes = [f"{entete} — {len(resultat.ordres)} ordre{'s' if len(resultat.ordres) != 1 else ''} "
              f"({n_b} BLOQUANT, {n_s} SIGNAL) — {resultat.secondes:.2f} s"]
    montre = resultat.ordres if tout else resultat.ordres[: PLAFOND_LIGNES - 2]
    for o in montre:
        ou = f" L{o.ligne}" if o.ligne else ""
        lignes.append(f"{o.niveau} {o.conscience}{ou} : {o.texte}")
    reste = len(resultat.ordres) - len(montre)
    if reste > 0:
        lignes.append(f"… {reste} ordres masqués (priorité aux BLOQUANT). Relancer avec --tout.")
    return "\n".join(lignes[: PLAFOND_LIGNES if not tout else 10**6])


def _lot_dir(lot: str) -> Path:
    nom = lot if lot.startswith("LOT_") else f"LOT_{int(lot):03d}"
    return racine_depot() / "grok-LOTS-html" / nom


def commande_fichier(chemin: Path, ancre: str | None, tout: bool) -> int:
    html = chemin.read_text(encoding="utf-8", errors="replace")
    lot = ""
    m = re.search(r"(LOT_\d+)", str(chemin))
    if m:
        lot = m.group(1)
    ssp, _ = ssp_catalogue(lot)
    titre = titre_de(html)
    inclure = "Phase_A" in chemin.name
    lot_txt = corps_freres(chemin.parent) if inclure else None
    r = analyser(html, lot=lot, ssp=ssp, titre=titre, chemin=str(chemin),
                 corps_lot=lot_txt, inclure_lot=inclure, ancre=ancre)
    print(formater(r, f"CONSCIENCE {chemin.name}", tout))
    return 1 if any(o.niveau == "BLOQUANT" for o in r.ordres) else 0


def commande_lot(lot: str, tout: bool) -> int:
    dossier = _lot_dir(lot)
    if not dossier.is_dir():
        print(f"Dossier introuvable : {dossier}", file=sys.stderr)
        return 2
    ssp, _ = ssp_catalogue(dossier.name)
    freres = corps_freres(dossier)
    tous: list[Ordre] = []
    vus: set[str] = set()
    t0 = time.perf_counter()
    for p in fichiers_lot(dossier):
        html = p.read_text(encoding="utf-8", errors="replace")
        r = analyser(html, lot=dossier.name, ssp=ssp, titre=titre_de(html),
                     corps_lot=freres, inclure_lot=False)
        for o in r.ordres:
            o.texte = f"[{p.name}] {o.texte}"
            o.cle = p.name + ":" + o.cle
            if o.cle not in vus:
                vus.add(o.cle)
                tous.append(o)
    # Éléments de niveau LOT une seule fois (Ottawa, Fleischner, seuils 0/1 h…).
    rlot = analyser("<html><h1>lot</h1><p></p></html>", lot=dossier.name, ssp=ssp,
                    titre="lot", corps_lot=freres, inclure_lot=True)
    for o in rlot.ordres:
        if o.cle.startswith("elt:"):
            o.cle = "lot:" + o.cle
            if o.cle not in vus:
                vus.add(o.cle)
                tous.append(o)
    tous.sort(key=lambda o: (o.priorite, o.ligne or 10**9, o.cle))
    res = Resultat(tous, time.perf_counter() - t0, orthographe_disponible())
    print(formater(res, f"CONSCIENCE {dossier.name}", tout))
    return 1 if any(o.niveau == "BLOQUANT" for o in tous) else 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Conscience embarquée du rédacteur (zéro jeton).")
    sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fichier")
    f.add_argument("chemin")
    f.add_argument("--ancre", default=None, help="Limite linguistique et posologie à cette ancre (p11). La conscience médicale d'absence reste sur le fichier.")
    f.add_argument("--tout", action="store_true")
    g = sub.add_parser("lot")
    g.add_argument("lot")
    g.add_argument("--tout", action="store_true")
    a = ap.parse_args(argv)
    if a.cmd == "fichier":
        p = Path(a.chemin)
        if not p.is_file():
            print(f"Fichier introuvable : {p}", file=sys.stderr)
            return 2
        return commande_fichier(p, a.ancre, a.tout)
    return commande_lot(a.lot, a.tout)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

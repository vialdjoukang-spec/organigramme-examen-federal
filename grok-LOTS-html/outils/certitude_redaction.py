#!/usr/bin/env python3
"""CERTITUDE DU RÉDACTEUR — contrôles gratuits, zéro jeton, bibliothèque standard.

Remplace la boucle d'audit dans la production (ordre de Vial, 31.10.2026) : le rédacteur
ne livre un fichier que s'il est certain de ce qu'il écrit, au vu des prompts de base
(PROMPT_PRODUCTION_V2 §2 et §12, Prompt V0 §11–14, PIEGES P-01).

  python3 grok-LOTS-html/outils/certitude_redaction.py <fichier.html> --preuves <dossier> [--lot LOT_XXX]
  python3 grok-LOTS-html/outils/certitude_redaction.py --autotest

Verdict : VERT (rien) · ORANGE (à lire, ne bloque pas) · ROUGE (ne pas livrer).
Code de sortie : 0 VERT/ORANGE · 1 ROUGE · 2 usage.
Lecture seule : n'écrit rien dans le dépôt (le piège d'autotest vit dans un dossier temporaire).

P-01 : les critiques V0 du harnais (title=, bande 80–150 Ko, feuille externe, h2, h3_14,
section Sources au sens V0) ne sont PAS des anomalies. Le format jugé ici est le V8
(îlots h2 id=p1…p14, abbr title voulu, taille x/y via harnais/taille_xy.py).
"""
from __future__ import annotations

import argparse
import html
import re
import sys
import tempfile
import unicodedata
from pathlib import Path

# Règle de Vial (PROMPT_PRODUCTION_V2 §12) : x = texte de la fiche.
X_MAX_DD, X_MAX_A = 9_000, 100_000
# Le marqueur « À vérifier » reste dans les leçons 134/135 déjà auditées (ils nomment le trou).
# À partir de LOT_137, ordre du 31.10.2026 : le trou sort du cours (INCERTITUDES.md), le marqueur est ROUGE.
LOT_REGLE_INCERTITUDE = 137

POINTS = {
    1: "définition",
    2: "épidémiologie",
    3: "physiopathologie",
    4: "démarche",
    5: "anamnèse",
    6: "examen",
    7: "syndrom",
    8: "diagnostic",
    9: "examen",
    10: "arbre",
    11: "prise en charge",
    12: "prévention",
    13: "points clés",
    14: "piège",
}

# Posologie médicamenteuse. Hors champ : mg/dl, g/dl, g/l (biologie), « g of salt » / « g de sel ».
DOSE = re.compile(
    r"\b(\d+(?:[.,]\d+)?)\s*"
    r"(µg|μg|mcg|mg|UI|IU|ml/h|mL/h)"
    r"(?:\s*/\s*(?:kg|j|jour|h|24\s*h))?"
    r"(?!\s*/\s*(?:dl|dL|l|ml)\b)",
    re.I,
)
DOSE_G = re.compile(
    r"\b(\d+(?:[.,]\d+)?)\s*g\b"
    r"(?!\s*/\s*(?:dl|dL|l)\b)"
    r"(?!\s+of\s+salt\b)"
    r"(?!\s+de\s+sel\b)",
    re.I,
)
MOTS_CLES = re.compile(
    r"\b(incidence|prévalence|prevalence|sensibilit[ée]|spécificit[ée]|specificit|"
    r"seuil|score)\b",
    re.I,
)
CHIFFRE = re.compile(r"\d+(?:[.,]\d+)?\s*(?:%|‰|pour\s+100|/\s*1?\s*000|/\s*100\b)?")
MARQUEUR_DURE = re.compile(r"\b(TODO|FIXME)\b|\(\?\)|À\s+vérifier|A\s+vérifier", re.I)
SIGLE = re.compile(r"\b([A-ZÉÈÀ]{2,}[A-Z0-9ÉÈÀ]*)\b")
# Sigles typographiques ou unités, pas des abréviations à développer.
SIGLES_IGNORÉS = {
    "HTML", "CSS", "UTF", "DOI", "URL", "PDF", "SI", "DX", "LOT", "OK", "CI",
    "II", "III", "IV", "VI", "VII", "VIII", "IX", "XI", "XII",
}


def racine_depot() -> Path:
    ici = Path(__file__).resolve()
    for p in (ici.parents[2], ici.parents[1]):
        if (p / "harnais" / "taille_xy.py").exists():
            return p
    return ici.parents[2]


def lot_de(nom: str, explicite: str | None) -> tuple[str | None, int | None]:
    if explicite:
        m = re.search(r"LOT_(\d+)", explicite, re.I)
        if m:
            return f"LOT_{int(m.group(1)):03d}" if False else f"LOT_{m.group(1)}", int(m.group(1))
        return explicite, None
    m = re.search(r"LOT_(\d+)", nom)
    if not m:
        return None, None
    return f"LOT_{m.group(1)}", int(m.group(1))


def phase_a(nom: str) -> bool:
    return "Phase_A" in nom or "Phase A" in nom


def norm_espace(s: str) -> str:
    s = html.unescape(s).replace("\u00a0", " ").replace("\u202f", " ").replace("μ", "µ")
    s = unicodedata.normalize("NFKC", s)
    return re.sub(r"\s+", " ", s)


def texte_visible(fragment: str) -> str:
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", fragment)
    t = re.sub(r"(?i)<br\s*/?>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    return norm_espace(t)


def hors_guillemets(t: str) -> str:
    """Retire les citations « » : une phrase source recopiée n'est pas l'affirmation de la fiche."""
    return re.sub(r"«[^»]*»", " ", t)


def mesurer_xy(racine: Path, html_texte: str) -> tuple[int, int]:
    sys.path.insert(0, str(racine / "harnais"))
    try:
        import taille_xy
    finally:
        sys.path.pop(0)
    m = taille_xy.mesurer(html_texte)
    return m.x[1], m.y[1]


def lire_preuves(dossier: Path | None) -> tuple[str, dict[int, str], list[tuple[str, str]]]:
    """Retourne (corpus normalisé, entrées INDEX, fichiers (nom, texte normalisé))."""
    if dossier is None or not dossier.is_dir():
        return "", {}, []
    fichiers = []
    index = {}
    morceaux = []
    for p in sorted(dossier.rglob("*")):
        if not p.is_file():
            continue
        if p.suffix.lower() not in {".txt", ".md", ".html", ".csv"}:
            continue
        try:
            brut = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        nt = norm_espace(brut).lower()
        fichiers.append((p.name, nt))
        morceaux.append(nt)
        if p.name.upper() == "INDEX.MD":
            for m in re.finditer(r"(?m)^\s*(\d+)\.\s+(.+)$", brut):
                index[int(m.group(1))] = m.group(2).strip()
    return "\n".join(morceaux), index, fichiers


def variantes_dose(nombre: str, unite: str) -> list[str]:
    u = unite.lower().replace("μg", "µg").replace("mcg", "µg")
    nums = {nombre}
    if "," in nombre:
        nums.add(nombre.replace(",", "."))
    elif "." in nombre:
        nums.add(nombre.replace(".", ","))
    out = []
    for n in nums:
        out.append(norm_espace(f"{n} {u}").lower())
        out.append(norm_espace(f"{n}{u}").lower())
    return out


def fichier_aips(nom: str, texte: str) -> bool:
    n = nom.lower()
    return (
        "aips" in n
        or "swissmedic" in n
        or "aips" in texte
        or "swissmedic" in texte
        or "information professionnelle" in texte
    )


def numeros(texte: str) -> set[str]:
    return set(re.findall(r"\b\d{5}\b", texte))


def dose_adossee(variantes: list[str], html_brut: str, fichiers: list[tuple[str, str]]) -> bool:
    """La dose est mot pour mot dans un extrait AIPS/Swissmedic du dossier,
    et la fiche cite un n° d'autorisation présent dans ces preuves.

    Le numéro et la phrase de dose ne sont pas toujours dans le même fichier
    (INDEX d'un côté, extrait de l'autre) : les deux doivent exister dans le dossier.
    """
    cites = numeros(html_brut)
    dose_dans_aips = False
    nums_aips: set[str] = set()
    for nom, texte in fichiers:
        if not fichier_aips(nom, texte):
            continue
        nums_aips |= numeros(texte) | numeros(nom)
        if any(v in texte for v in variantes):
            dose_dans_aips = True
    return dose_dans_aips and bool(cites & nums_aips)


def annee_dans(s: str) -> bool:
    return re.search(r"\b(?:19|20)\d{2}\b", s) is not None


def controles_herites(plain_hors_citations: str) -> list[str]:
    """Erreurs récurrentes corrigées dans les audits LOT_134 et LOT_135.

    On lit le texte hors citations « » : recopier la phrase fautive d'une source
    n'est pas la réécrire comme conduite. La fiche corrigée porte la négation.
    """
    t = plain_hors_citations
    rouge = []
    # Alvarado ≥ 7 ≠ chirurgie systématique (WSES Jérusalem 2020 ; audit LOT_134 DX.4).
    for m in re.finditer(r"Alvarado.{0,160}", t, re.I):
        w = t[m.start():m.start() + 220]
        if re.search(r"(\b7\b|sept).{0,80}(chirurg|opér)", w, re.I) or re.search(
            r"(chirurg|opér).{0,80}(\b7\b|sept)", w, re.I
        ):
            if not re.search(
                r"n['’]autorise pas|déconseill|ne suffit pas|refuse|pas confirmer|"
                r"ne confirme pas|\bAIR\b|\bAAS\b|n['’]est pas une indication",
                w,
                re.I,
            ):
                rouge.append(
                    "Alvarado : un score ≥ 7 n'autorise pas la chirurgie chez l'adulte "
                    "(WSES 2020 ; audit LOT_134). La fiche affirme encore l'opération."
                )
                break
    # qSOFA dépiste au lit ; SOFA ≥ 2 est un autre usage (SFR 2020 rec. 2 et 9 ; LOT_134 DX.7).
    if re.search(r"(?<![qQ])SOFA\s+(au lit|dépiste|de dépistage)", t):
        rouge.append("SOFA n'est pas l'outil de dépistage au lit : c'est le qSOFA (audit LOT_134, SFR 2020 rec. 2).")
    if re.search(r"recommandation\s+2.{0,60}(?<![qQ])SOFA", t, re.I) and not re.search(
        r"recommandation\s+2.{0,40}qSOFA", t, re.I
    ):
        rouge.append("La recommandation 2 (dépistage au lit) vise le qSOFA, pas le SOFA (audit LOT_134).")
    # 500 ml = intervalle de clampage, pas un seuil diagnostique de rétention (EAU 2024 ; LOT_135 DX.5).
    for m in re.finditer(r"500\s*ml", t, re.I):
        w = t[max(0, m.start() - 140):m.end() + 140]
        if re.search(r"rétention|vessie", w, re.I) and re.search(r"diagnos|seuil|définit", w, re.I):
            if not re.search(r"clamp|pas un seuil|n['’]est pas", w, re.I):
                rouge.append(
                    "500 ml n'est pas un seuil diagnostique de rétention (intervalle de clampage ; audit LOT_135)."
                )
                break
    # 14/100 après 65 ans est un écart de traduction ; le chiffre retenu est 14/1 000 (LOT_135).
    if re.search(r"14\s*/\s*100\b", t) and re.search(r"pneumon|65\s*ans|personnes", t, re.I):
        if not re.search(r"traduction|écart|1[\s\u00a0]?000|14\s*/\s*1", t, re.I):
            rouge.append("14/100 (pneumonie, ≥ 65 ans) est un écart de traduction ; retenir 14/1 000 (audit LOT_135).")
    # « Artérite mésentérique » n'est pas le nom de l'ischémie aiguë (ESVS 2017 ; LOT_134).
    if re.search(r"artérite mésentérique", t, re.I):
        if not re.search(r"pas une artérite|n['’]est pas une artérite|ischémie mésentérique", t, re.I):
            rouge.append("Dire « artérite mésentérique » pour l'ischémie aiguë est faux (audit LOT_134, ESVS 2017).")
    # Le stade C3 décrit un godet, pas une étiologie veineuse prouvée (Bonn ; LOT_134 DX.1).
    # La phrase corrigée (« n'égale pas ») contient les mêmes mots : on n'alerte que l'affirmation.
    m_c3 = re.search(
        r"stade\s+C3(.{0,140})(étiologie veineuse prouvée|insuffisance veineuse documentée|diagnostic veineux certain)",
        t,
        re.I,
    )
    if m_c3 and not re.search(r"\bpas\b|n['’]|aucun", m_c3.group(1), re.I):
        rouge.append("Le stade C3 n'égale pas une insuffisance veineuse documentée (audit LOT_134, Bonn Vein Study).")
    # Aucune sensibilité chiffrée lue pour la disparition de la matité hépatique (LOT_135 DX.10).
    if re.search(r"disparition de la matité hépatique.{0,100}sensibilit[ée].{0,30}\d", t, re.I):
        rouge.append(
            "Aucune sensibilité chiffrée n'a été lue pour la disparition de la matité hépatique (audit LOT_135)."
        )
    return rouge


def verifier(fichier: Path, preuves: Path | None, lot: str | None, racine: Path) -> dict:
    rouge, orange = [], []
    if not fichier.is_file():
        return {"verdict": "ROUGE", "rouge": [f"fichier absent : {fichier}"], "orange": [], "info": {}}
    brut = fichier.read_text(encoding="utf-8", errors="replace")
    nom = fichier.name
    lot_nom, lot_n = lot_de(nom, lot)
    strict = lot_n is None or lot_n >= LOT_REGLE_INCERTITUDE
    info = {
        "fichier": nom,
        "lot": lot_nom,
        "ignores_v0_P01": ["title", "bande_80_150", "externe", "h2", "h3_14", "sources_v0"],
    }

    # (g) tailles V8
    try:
        x, y = mesurer_xy(racine, brut)
    except Exception as e:
        x, y = -1, -1
        rouge.append(f"taille_xy illisible : {e}")
    xmax = X_MAX_A if phase_a(nom) else X_MAX_DD
    info.update({"x": x, "y": y, "x_max": xmax, "type": "Phase A" if phase_a(nom) else "DD"})
    if x > xmax:
        rouge.append(f"fiche x = {x/1000:.1f} Ko > {xmax/1000:.0f} Ko (PROMPT_PRODUCTION_V2 §12)")
    elif x > 0.95 * xmax:
        orange.append(f"fiche x = {x/1000:.1f} Ko, au-dessus de 95 % du plafond {xmax/1000:.0f} Ko")

    # (a) 14 points présents et non vides
    titres = {}
    for m in re.finditer(r'<h2([^>]*)>(.*?)</h2>', brut, re.S | re.I):
        attrs, corps = m.group(1), m.group(2)
        idm = re.search(r'id="([^"]+)"', attrs)
        if not idm:
            continue
        titres[idm.group(1)] = texte_visible(corps)
    heads = [(m.start(), m.group(1)) for m in re.finditer(r'<h2[^>]*\bid="(p\d+|sources|ess|som)"', brut)]
    segments = {}
    for i, (pos, ident) in enumerate(heads):
        fin = heads[i + 1][0] if i + 1 < len(heads) else len(brut)
        fin_section = brut.find("</section>", pos)
        if fin_section != -1 and fin_section < fin:
            fin = fin_section
        segments[ident] = brut[pos:fin]
    for n, mot in POINTS.items():
        ident = f"p{n}"
        if ident not in segments:
            rouge.append(f"point {n} absent (id {ident} ; plan §11)")
            continue
        visible = texte_visible(segments[ident])
        if len(visible) < 40:
            rouge.append(f"point {n} vide ou trop court ({len(visible)} caractères)")
        titre = titres.get(ident, "")
        if mot not in titre.lower():
            orange.append(f"point {n} : le titre « {titre} » ne contient pas « {mot} »")

    # (f) sigles développés par <abbr title>
    developpes = set(re.findall(r'<abbr\s+title="[^"]*"\s*>([^<]+)</abbr>', brut, re.I))
    developpes |= set(re.findall(r"<abbr\s+title='[^']*'\s*>([^<]+)</abbr>", brut, re.I))
    developpes = {s.strip() for s in developpes}
    visible_total = texte_visible(brut)
    sigles = []
    for s in SIGLE.findall(visible_total):
        if s in SIGLES_IGNORÉS or s.isdigit() or len(s) < 2:
            continue
        if s not in developpes and s not in sigles:
            sigles.append(s)
    if sigles:
        montre = ", ".join(sigles[:8])
        orange.append(f"sigles sans <abbr title> : {montre}" + ("…" if len(sigles) > 8 else ""))

    # (e) incertitude non résolue
    visible_pour_marqueurs = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", brut)
    visible_pour_marqueurs = re.sub(r"<[^>]+>", " ", visible_pour_marqueurs)
    marqueurs = MARQUEUR_DURE.findall(visible_pour_marqueurs)
    if marqueurs:
        n = len(marqueurs)
        msg = f"{n} marqueur(s) d'incertitude (À vérifier, TODO, FIXME ou (?))"
        if strict:
            rouge.append(msg + " — les retirer du cours ou les noter dans INCERTITUDES.md")
        else:
            orange.append(msg + f" — toléré en ORANGE sur {lot_nom} (leçon auditée avant la règle du 31.10.2026)")

    # (b) (c) (d) preuves
    corpus, index, fichiers = lire_preuves(preuves)
    info["preuves"] = str(preuves) if preuves else None
    info["index"] = len(index)
    if preuves is None or not preuves.is_dir():
        rouge.append("dossier de preuves absent : passez --preuves")
    else:
        if not index:
            orange.append("evidence/INDEX.md sans entrée numérotée « 1. … »")
        sups = set()
        for bloc in re.findall(r"<sup[^>]*>(.*?)</sup>", brut, re.S | re.I):
            for n in re.findall(r"\d+", re.sub(r"<[^>]+>", "", bloc)):
                sups.add(int(n))
        absents = sorted(n for n in sups if n not in index)
        if absents:
            rouge.append(
                "référence citée absente de evidence/INDEX.md : "
                + ", ".join(str(n) for n in absents[:12])
            )
        # (b) doses
        plain = visible_total
        doses = []
        for m in DOSE.finditer(plain):
            doses.append((m.group(1), m.group(2), m.group(0)))
        for m in DOSE_G.finditer(plain):
            doses.append((m.group(1), "g", m.group(0)))
        vues = set()
        orphelines = []
        for nombre, unite, brut_dose in doses:
            cle = norm_espace(brut_dose).lower()
            if cle in vues:
                continue
            vues.add(cle)
            if not dose_adossee(variantes_dose(nombre, unite), brut, fichiers):
                orphelines.append(norm_espace(brut_dose))
        if orphelines:
            rouge.append(
                "dose sans citation AIPS/Swissmedic mot pour mot (n° d'autorisation cité dans la fiche) : "
                + ", ".join(orphelines[:10])
            )
        # (c) chiffres-clés : incidence, sensibilité, spécificité, seuil, score
        sans_date = 0
        for m in re.finditer(r"<p[^>]*>(.*?)</p>|<li[^>]*>(.*?)</li>", brut, re.S | re.I):
            bloc = m.group(1) or m.group(2) or ""
            vis = texte_visible(bloc)
            if not MOTS_CLES.search(vis) or not re.search(r"\d", vis):
                continue
            sup_bloc = [int(n) for n in re.findall(r"\d+", " ".join(re.findall(r"<sup[^>]*>(.*?)</sup>", bloc, re.S | re.I)))]
            date_ok = False
            for n in sup_bloc:
                if n in index and annee_dans(index[n]):
                    date_ok = True
                    break
            if not date_ok and annee_dans(vis):
                # l'année doit exister dans l'INDEX (pas une année inventée hors preuves)
                annees = set(re.findall(r"\b(?:19|20)\d{2}\b", vis))
                idx_annees = set(re.findall(r"\b(?:19|20)\d{2}\b", " ".join(index.values())))
                if annees & idx_annees:
                    date_ok = True
            if not date_ok and "«" in bloc:
                citation = re.search(r"«([^»]{25,400})»", vis)
                if citation and norm_espace(citation.group(1)).lower()[:80] in corpus:
                    # la citation est dans les preuves ; l'INDEX du dossier doit porter une année quelque part
                    if any(annee_dans(v) for v in index.values()):
                        date_ok = True
            if not date_ok:
                sans_date += 1
        if sans_date:
            msg = f"{sans_date} chiffre(s)-clé (incidence, sensibilité, spécificité, seuil, score) sans référence datée dans evidence/INDEX.md"
            if strict:
                rouge.append(msg)
            else:
                orange.append(msg + f" — ORANGE sur {lot_nom} (leçon déjà auditée)")

    # (h) liste DX
    if lot_nom and preuves is not None:
        liste = preuves.parent / "LISTE_DX_CANONIQUE.md"
        if not liste.is_file():
            orange.append("LISTE_DX_CANONIQUE.md absente à côté du dossier de preuves")
        else:
            noms = {}
            for ligne in liste.read_text(encoding="utf-8", errors="replace").splitlines():
                mm = re.match(r"DX\.(\d+)\s*[—–\-]\s*(.+)", ligne.strip())
                if mm:
                    noms[int(mm.group(1))] = mm.group(2).strip()
            h1m = re.search(r"<h1[^>]*>(.*?)</h1>", brut, re.S | re.I)
            h1 = texte_visible(h1m.group(1)) if h1m else ""
            dxm = re.search(r"DX\.(\d+)", nom)
            if dxm and noms:
                n = int(dxm.group(1))
                attendu = noms.get(n, "")
                if attendu and norm_espace(attendu).lower() not in norm_espace(h1).lower():
                    rouge.append(f"titre DX.{n} « {h1} » ≠ liste canonique « {attendu} »")
            if phase_a(nom) and noms:
                manquants = [f"DX.{n} {lib}" for n, lib in noms.items() if norm_espace(lib).lower() not in norm_espace(brut).lower()]
                if manquants:
                    rouge.append("Phase A : noms absents de la liste canonique : " + " ; ".join(manquants[:6]))

    # (i) règles héritées des audits
    hors = hors_guillemets(visible_total)
    for msg in controles_herites(hors):
        rouge.append(msg)

    # (j) P-01 déjà consigné dans info : aucune de ces critiques n'entre dans rouge/orange.
    verdict = "ROUGE" if rouge else ("ORANGE" if orange else "VERT")
    return {"verdict": verdict, "rouge": rouge, "orange": orange, "info": info}


def afficher(r: dict) -> None:
    i = r.get("info") or {}
    print(
        f"{r['verdict']}  {i.get('fichier','')}  "
        f"[{i.get('type','?')}, x = {i.get('x','?')} o, lot {i.get('lot')}]"
    )
    for m in r["rouge"]:
        print("  ROUGE  ", m)
    for m in r["orange"]:
        print("  ORANGE ", m)


def _page(titre, points: dict[int, str], extra="", fin="FIN_FICHIER LOT_999_Phase_B_V0_DX.1") -> str:
    ilots = []
    for n in range(1, 15):
        corps = points.get(n, f"Le point {n} énonce une conduite claire, datée et sans dose inventée.")
        ilots.append(f'<section class="ilot"><h2 id="p{n}">{n}. {POINTS[n].capitalize()}</h2><p>{corps}</p></section>')
    return f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>{titre}</title></head><body>
<main>
<h1 id="titre">{titre}</h1>
<p id="taille">Taille</p>
<section class="ilot"><h2 id="ess">L'essentiel</h2><p>Essentiel de démonstration.</p></section>
<section class="ilot"><h2 id="som">Sommaire</h2><p>Sommaire court.</p></section>
{''.join(ilots)}
{extra}
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
<section><h2 id="sources">Sources</h2><p>Voir l'index des preuves.</p></section>
</main></body></html>
<!-- {fin} -->
"""


def autotest() -> int:
    """Deux fichiers synthétiques : un sain (pas ROUGE), un piégé (ROUGE)."""
    racine = racine_depot()
    echecs = []
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        ev = base / "evidence"
        ev.mkdir()
        (ev / "INDEX.md").write_text(
            "1. ESPEN, Clinical Nutrition, 2019, critères GLIM. extrait_espen.txt\n"
            "2. AIPS Benerva n° 12345, lu le 31.10.2026. aips_12345.txt\n",
            encoding="utf-8",
        )
        (ev / "aips_12345.txt").write_text(
            "Information professionnelle AIPS Swissmedic. Autorisation 12345. "
            "La dose usuelle est de 100 mg par jour.\n",
            encoding="utf-8",
        )
        (ev / "extrait_espen.txt").write_text(
            "GLIM 2019 : un critère phénotypique et un critère étiologique.\n",
            encoding="utf-8",
        )
        (base / "LISTE_DX_CANONIQUE.md").write_text(
            "DX.1 — Cachexie cancéreuse\n",
            encoding="utf-8",
        )
        sain_points = {
            2: 'L\'<abbr title="indice de masse corporelle">IMC</abbr> bas entre dans le phénotype. '
               'Prévalence hospitalière suisse citée en 2019<sup class="s">1</sup>.',
            11: 'La spécialité lue porte le numéro 12345. La dose usuelle est de 100 mg par jour, '
                'selon l\'<abbr title="information professionnelle suisse">AIPS</abbr>.',
        }
        sain = base / "LOT_137_Phase_B_V0_DX.1.html"
        sain.write_text(
            _page("Cachexie cancéreuse", sain_points, fin="FIN_FICHIER LOT_137_Phase_B_V0_DX.1"),
            encoding="utf-8",
        )
        rs = verifier(sain, ev, "LOT_137", racine)
        afficher(rs)
        if rs["verdict"] == "ROUGE":
            echecs.append("fixture saine ROUGE")

        piege_points = {
            1: "Définition À vérifier, avec un TODO et un (?).",
            2: "Incidence de 12 % sans année et sans exposant.",
            4: "Un score d'Alvarado d'au moins 7 impose la chirurgie immédiate.",
            8: "Seuil diagnostique de rétention : 500 ml de volume vésical.",
            11: "On donne 999 mg trois fois par jour, sans numéro d'autorisation.",
            14: "",
        }
        piege = base / "LOT_137_Phase_B_V0_DX.1.html"
        # point 14 vide + marqueurs + dose inventée + règles héritées + exposant 9 absent
        corps = _page("Mauvais titre", piege_points, extra='<p>Source <sup class="s">9</sup>.</p>')
        corps = corps.replace(
            '<h2 id="p14">14. Piège</h2><p></p>',
            '<h2 id="p14">14. Piège</h2><p></p>',
        )
        # forcer le point 14 vide : le défaut de _page met une phrase si la chaîne est vide... 
        # piege_points[14] = "" tombe sur le défaut de _page. On écrase.
        corps = re.sub(
            r'(<h2 id="p14">14\. Piège</h2><p>).*?(</p>)',
            r"\1 \2",
            corps,
            count=1,
        )
        piege.write_text(corps, encoding="utf-8")
        rp = verifier(piege, ev, "LOT_137", racine)
        afficher(rp)
        if rp["verdict"] != "ROUGE":
            echecs.append("fixture piégée non ROUGE")
        else:
            attendus = ("incertitude", "Alvarado", "500 ml", "999 mg", "INDEX", "point 14", "chiffre")
            blob = " ".join(rp["rouge"]).lower()
            # 999 mg peut être rendu « 999 mg »
            manquent = []
            for a in ("vérifier", "alvarado", "500 ml", "999 mg", "index", "point 14", "chiffre"):
                if a not in blob:
                    manquent.append(a)
            if manquent:
                echecs.append("piège incomplet : " + ", ".join(manquent))
    if echecs:
        print("AUTOTEST ROUGE  " + " ; ".join(echecs))
        return 1
    print("AUTOTEST VERT  fixture saine non ROUGE ; fixture piégée ROUGE")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fichier", nargs="?")
    ap.add_argument("--preuves", help="dossier evidence du LOT")
    ap.add_argument("--lot", help="LOT_XXX si le nom de fichier ne le porte pas")
    ap.add_argument("--autotest", action="store_true")
    a = ap.parse_args(argv)
    if a.autotest:
        return autotest()
    if not a.fichier:
        ap.print_usage(sys.stderr)
        return 2
    r = verifier(Path(a.fichier), Path(a.preuves) if a.preuves else None, a.lot, racine_depot())
    afficher(r)
    return 1 if r["verdict"] == "ROUGE" else 0


if __name__ == "__main__":
    sys.exit(main())

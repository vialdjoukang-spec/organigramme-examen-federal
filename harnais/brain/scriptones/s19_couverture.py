#!/usr/bin/env python3
"""Scriptone S19 · couverture des fautes récurrentes (le cumul des corrections → les scriptones qui en empêchent la reproduction). Région MEM.
Entrée : le TEXTE du cumul (DOSSIER_INGENIEUR/04_CUMUL_CORRECTIONS_AUDITEURS.md, 262 rapports, ou tout journal de corrections).
Classe chaque ligne dans une famille de fautes (motifs), compte les occurrences et vérifie qu'un scriptone (ou un contrôle existant) la couvre.
  U1 famille de fautes récurrente sans aucune couverture     U2 lignes non classées au-dessus de 60 % (classification à enrichir)
Option : retirer = nom de famille (test : couverture retirée)."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bus

ID, REGION, VERSION = "s19_couverture", "MEM", "1.0.0"
DORE = Path(__file__).resolve().parent.parent / "DOSSIER_INGENIEUR/04_CUMUL_CORRECTIONS_AUDITEURS.md"
CLASSES = [
 ("récit négatif et « À vérifier »", r"À vérifier|non chiffr|non lu|non quantifi|non trouvé", ["αn·R (AR1–AR4)", "βn·X (lacune devenue doléance)"]),
 ("doses et AIPS", r"AIPS|posolog|\bdoses?\b", ["controle_medical (existant)", "αn·R (AR3)", "β11·S (BS3)", "s9_sources (I1)", "s10_memoire"]),
 ("abréviations et sigles", r"abréviation|sigle", ["forme_interactive (existant, critique)"]),
 ("médicaments et termes cliquables", r"cliquable|®|fenêtre|ATC", ["forme_interactive (existant)", "αn·D (AD2–AD4)"]),
 ("phrases nominales et longueur", r"nominale|sans verbe|phrases? longues?|> ?25 mots|mots par phrase", ["αn·H (AH1, AH2)", "controle_langue (existant)"]),
 ("mentions de conception", r"conception|ce fichier|Phase [AB]|autre IA|cycle \d|rédacteur", ["αn·D (AD1)"]),
 ("références, PMID et sources", r"PMID|référence|\[S\d+\]|grappe", ["controle_medical (existant)", "βn·S (BS1, BS2)", "s9_sources", "s20_ancres"]),
 ("chiffres sans source ou non retrouvés", r"chiffre|sans source|retrouv", ["s4_budget (B2)", "βn·S (BS1)", "βn·C"]),
 ("point médian et typographie des nombres", r"·\d|\d·|point médian", ["βn·C (BC1, BC2, BC6)"]),
 ("rangs, ordre canonique, fréquences", r"canonique|\brang|fréquence", ["s10_memoire (M7)", "αn·R"]),
 ("taille et lignes longues", r"\d+ ?Ko|taille|3 000|ligne", ["controle_lot (existant)", "s16_economie (W3)", "s11_collecteur"]),
 ("arbre de classification", r"arbre|arborescence|classification", ["s5_arbre (A1–A6)", "α1·S (AS4)"]),
 ("tableaux et en-têtes", r"tableau|caption|en-tête|colonne", ["s8_tableaux (T1–T7)", "α3·S", "α9·S"]),
 ("épidémiologie et budgets", r"épidémiolog|prévalence|incidence", ["s4_budget (B1–B4)", "α2·Q (AQ1, AQ2)", "β2·X"]),
 ("police et rendu", r"Atkinson|police|rendu", ["s1_police (P1–P7)", "s7_captures (V1)"]),
 ("verrous, blocages, stagnation", r"verrou|BLOQU|stagnation|bloqué", ["grille_agent (existant)", "s13_disjoncteur (Z3)"]),
 ("numéros Swissmedic et spécialités", r"Swissmedic|spécialité|n° \d{5}", ["s9_sources", "s10_memoire"]),
 ("title= et infobulles", r"title=|infobulle|survol", ["s10_memoire (M8)", "forme_interactive (existant)"]),
]


def analyser(t, nom, opt=None):
    opt = opt or {}; me = sys.modules[__name__]; D = []
    L = [l for l in t.splitlines() if l.startswith("- ")]; occ = {c: 0 for c, _, _ in CLASSES}; nc = 0
    for l in L:
        hit = False
        for c, rx, _ in CLASSES:
            if re.search(rx, l): occ[c] += 1; hit = True
        nc += not hit
    cov = {c: ([] if c == opt.get("retirer") else s) for c, _, s in CLASSES}
    for c, n in occ.items():
        if n and not cov[c]:
            D.append(bus.doleance(me, "U1", nom, f"#cumul · {c}", "GRAVE", f"faute récurrente « {c} » ({n} rapports) sans scriptone qui en empêche la reproduction",
                                  "écrire un scriptone (ou une entrée de memoire_fautes.json) et son mutant, puis l'ajouter au registre", "agent", f"{n} occurrences"))
    if L and nc / len(L) > 0.6:
        D.append(bus.doleance(me, "U2", nom, "#cumul", "MOYEN", f"{nc} lignes sur {len(L)} non classées", "enrichir CLASSES de s19_couverture.py", "agent"))
    return D, dict(rapports=len(L), non_classes=nc, occurrences=occ, couverture={c: s for c, s in cov.items()})


MUTANTS = [("couverture retirée", (lambda t, r: (t, {"retirer": r.choice([c for c, _, _ in CLASSES[:8]])})), "U1"),
           ("cumul inconnu", (lambda t, r: "\n".join(f"- rapport {i} : opération de maintenance sans rapport" for i in range(r.randint(20, 40)))), "U2")]
ECRIT = []

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))

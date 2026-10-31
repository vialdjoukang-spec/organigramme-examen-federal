#!/usr/bin/env python3
"""DX.7 approfondi : arthrite septique.

Texte lu le 31.10.2026 : recommandations françaises 2020, Couderc et al.,
DOI 10.1016/j.jbspin.2020.07.012 (page ouverte). Le PDF HAL n'était pas un PDF.
Aucune dose en milligrammes : À vérifier (AIPS).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import profond_lib as L

NOM = "Arthrite septique"
FICHIER = "LOT_134_Phase_B_V0_DX.7.html"
SRC = Path("/home/ubuntu/.cursor/projects/workspace/agent-tools/d4ed48ee-9992-485e-b010-7de240a0a799.txt")
L.GLOSS.update({
    "SA": "arthrite septique",
    "SOFA": "score séquentiel d'évaluation des défaillances d'organe",
    "SFR": "société française de rhumatologie",
    "SPILF": "société de pathologie infectieuse de langue française",
    "SOFCOT": "société française de chirurgie orthopédique et traumatologique",
    "HAS": "haute autorité de santé",
    "US": "échographie",
    "CRP": "protéine C réactive",
    "MRI": "imagerie par résonance magnétique",
    "CT": "tomodensitométrie",
    "PCR": "amplification génique",
    "IV": "voie intraveineuse",
    "PO": "voie orale",
})
DOSE = re.compile(r"\b\d+(?:[.,]\d+)?\s?(?:mg|µg|mcg|g|UI|IU|ml|mL)\b")
MOTS = re.compile(r"\b(septic|arthritis|synovial|aspirat|antibiotic|joint|fever|crystal|drainage)\b", re.I)


def cliniques(texte, mots, n, deja):
    pris = []
    for p in L.phrases_source(texte):
        if p in deja or not MOTS.search(p):
            continue
        if mots and not any(m.lower() in p.lower() for m in mots):
            continue
        if DOSE.search(p) or "h-index" in p or "http" in p or p.count(",") > 7:
            continue
        deja.add(p)
        pris.append(p)
        if len(pris) >= n:
            break
    return pris


def paquet(c, xs, prefix, theme):
    preuves = L.preuves(c, "SFR", prefix, theme, "les recommandations françaises de 2020", xs)
    lignes = [f"Les boutons ouvrent des phrases des recommandations de 2020 sur {theme}."]
    for i in range(1, len(xs) + 1):
        lignes.append(f"Phrase citée numéro {i} sur {theme}. " + L.B(f"{prefix}-q{i}", f"citation {i}"))
    return L.W(f"{prefix}-index", f"Citations : {theme}", lignes) + "\n" + preuves


def construire():
    brut = " ".join(SRC.read_text(encoding="utf-8", errors="replace").split())
    c = L.Corpus()
    c.texts["SFR"] = brut
    deja = set()
    themes = [
        ("w-dx7d", "le diagnostic", ["monoarthritis", "aspiration", "synovial"], 12),
        ("w-dx7a", "l'antibiotique sans dose", ["antibiotic", "probabilistic", "severity"], 10),
        ("w-dx7c", "le cœur et les cristaux", ["endocarditis", "crystal", "ultrasound"], 8),
        ("w-dx7z", "le texte", ["arthritis", "joint", "synovial"], 60),
    ]
    blocs = {}
    for prefix, theme, mots, n in themes:
        xs = cliniques(brut, mots, n, deja)
        print(theme, len(xs))
        if len(xs) < 3:
            raise SystemExit("peu " + theme)
        blocs[prefix] = paquet(c, xs, prefix, theme)
    wins = [""] * 14
    wins[0] = L.W("w-dx7-def", "Articulation native", [
        "C'est l'infection bactérienne pyogène d'une articulation native de l'adulte.",
        "Une prothèse n'est pas le sujet de ce texte.",
        "Le texte exclut aussi les mycobactéries, Lyme, les virus, les parasites, les champignons, le pied diabétique, Whipple et l'arthrite réactionnelle.",
        "La ponction documente. La main seule ne nomme pas.",
    ]) + "\n" + blocs["w-dx7d"]
    wins[1] = L.W("w-dx7-epi", "Pas de taux suisse", [
        "Aucun taux suisse ou européen n'a été lu dans ces pages : À vérifier.",
        "Le rang DX.7 vient de cette absence de dénominateur, pas d'un calcul.",
        "Le rang d'exclusion E5 rappelle que c'est une urgence, même si le chiffre manque.",
        "Le texte dit la maladie rare, mais grave par le dégât articulaire.",
    ])
    wins[2] = L.W("w-dx7-phys", "Du germe au liquide", [
        "Le germe atteint la synoviale, le liquide devient inflammatoire, puis purulent.",
        "La douleur au moindre mouvement vient de cette synoviale.",
        "Les cristaux peuvent imiter le tableau : on les cherche dans le même liquide.",
        "L'antibiotique vise le germe, mais seulement après le prélèvement, sauf gravité immédiate.",
    ])
    wins[3] = L.W("w-dx7-dem", "E5", [
        "Ce diagnostic est DX.7, rang d'exclusion E5.",
        "Une fasciite ou une péritonite peuvent passer avant si la peau ou tout l'abdomen dominent.",
        "Toute monoarthrite aiguë fait quand même évoquer l'infection, avec ou sans fièvre.",
    ])
    wins[4] = L.W("w-dx7-ana", "Fièvre non exigée", [
        "On demande le début, la fièvre, une porte d'entrée, un antibiotique déjà pris.",
        "L'absence de fièvre n'écarte pas le diagnostic.",
        "Une oligoarthrite ou une polyarthrite ne l'écartent pas non plus.",
        "Un score de gravité immédiat, SOFA d'au moins 2, change l'heure de l'antibiotique.",
    ])
    wins[5] = L.W("w-dx7-exam", "Comparer, puis ponctionner proprement", [
        "On compare à l'autre côté, on cherche un épanchement et une douleur au moindre mouvement.",
        "La peau autour se regarde : une crépitation n'est plus une arthrite simple.",
        "On ne ponctionne pas à travers une peau infectée si une autre voie existe : cette précision opératoire reste À vérifier dans un protocole suisse.",
        "L'échographie guide la ponction quand le liquide est peu abondant.",
    ])
    wins[6] = L.W("w-dx7-synd", "Trois tableaux", [
        "Monoarthrite aiguë fébrile ou non : évoquer l'infection.",
        "Liquide purulent sans cristal : le texte permet alors un antibiotique probabiliste.",
        "Gravité immédiate, SOFA d'au moins 2 : ne pas attendre le résultat pour traiter, après avoir prélevé si c'est possible.",
        "Crépitation sous-cutanée : sortir de l'arthrite simple.",
    ])
    wins[7] = L.W("w-dx7-pos", "Le liquide", [
        "Le diagnostic positif est le liquide synovial, avec culture et examen direct.",
        "On ensemence aussi des flacons d'hémoculture, surtout si un antibiotique a déjà été donné ou si l'attente est longue.",
        "Un liquide clairement purulent, sans cristal, peut faire démarrer l'antibiotique probabiliste, recommandation 9.",
        "Ce n'est pas le cas habituel : en principe, on attend le prélèvement et son résultat.",
        "Les hémocultures font partie de la documentation, avant l'antibiotique.",
    ])
    wins[8] = L.W("w-dx7-ex", "Avant l'image de luxe", [
        "La radiographie de référence est indiquée.",
        "L'échographie guide la ponction.",
        "L'échographie cardiaque n'est pas systématique.",
        "Elle est indiquée pour le staphylocoque doré, les streptocoques buccaux, Streptococcus gallolyticus, Enterococcus faecalis, ou une suspicion clinique d'endocardite.",
        "La biologie seule ne remplace pas le liquide.",
    ]) + "\n" + blocs["w-dx7c"]
    wins[9] = L.W("w-dx7-arbre", "Si, alors", [
        "Si l'articulation est aiguë, on évoque l'infection, même sans fièvre.",
        "Si l'on peut ponctionner, on le fait avant l'antibiotique.",
        "Si le score SOFA atteint 2, la gravité immédiate autorise à ne pas attendre le résultat, le prélèvement restant la règle.",
        "Si le liquide est clairement purulent et sans cristal, l'antibiotique probabiliste est discuté.",
        "Si le patient a moins de 70 ans, le texte français conseille la céfazoline injectable.",
        "S'il a plus de 70 ans, il privilégie la ceftriaxone ou le céfotaxime.",
        "Aucune de ces phrases n'est une dose suisse.",
    ]) + "\n" + blocs["w-dx7a"]
    wins[10] = L.W("w-dx7-pec", "Noms sans milligrammes", [
        "Sous 70 ans, le texte français conseille une céphalosporine injectable de première génération, la céfazoline.",
        "Au-dessus de 70 ans, il privilégie la ceftriaxone ou le céfotaxime.",
        "Aucune dose en milligrammes n'est recopiée.",
        "Elle se lit dans l'information professionnelle suisse du produit : À vérifier (AIPS).",
        "Le drainage et la rééducation précoce sont recommandés par le texte, sans protocole suisse recopié.",
        "La surveillance cherche la fièvre, l'autre articulation et les signes de gravité.",
    ]) + "\n" + blocs["w-dx7z"]
    wins[11] = L.W("w-dx7-prev", "Pas de vaccin lu", [
        "Aucun programme de prévention chiffré n'a été lu.",
        "La prévention utile est de ponctionner avant de traiter.",
    ])
    wins[13] = L.quiz("w-dx7-pieges", [
        ("Faut-il de la fièvre ?",
         "Non. Toute monoarthrite aiguë fait évoquer l'infection."),
        ("Une polyarthrite exclut-elle ?",
         "Non."),
        ("Quand ponctionne-t-on ?",
         "Avant l'antibiotique, sauf si la gravité immédiate empêche d'attendre."),
        ("Que veut dire SOFA d'au moins 2 ?",
         "Un signe de gravité immédiate dans la recommandation 2."),
        ("Liquide purulent sans cristal ?",
         "Le texte permet alors un antibiotique probabiliste. Ce n'est pas la voie habituelle."),
        ("Quelle molécule sous 70 ans ?",
         "Céfazoline, dans le texte français. La dose suisse est À vérifier (AIPS)."),
        ("Et au-dessus de 70 ans ?",
         "Ceftriaxone ou céfotaxime, sans milligramme ici."),
        ("L'échographie cardiaque est-elle systématique ?",
         "Non. Seulement pour certains germes ou une suspicion d'endocardite."),
        ("Une prothèse est-elle incluse ?",
         "Non."),
        ("E5 est-il le premier rang du lot ?",
         "Non. Il rappelle l'urgence sans être E1."),
        ("Le taux suisse est-il connu ici ?",
         "Non. À vérifier."),
        ("Peut-on ponctionner à travers une peau infectée ?",
         "La leçon ne l'affirme pas. La précision opératoire suisse est À vérifier."),
        ("Les cristaux se cherchent-ils ?",
         "Oui, dans le même liquide, comme diagnostic différentiel."),
        ("Qui a écrit le texte ?",
         "Sociétés françaises de rhumatologie, d'infectiologie et de chirurgie orthopédique, méthode de la Haute Autorité de santé, 2020."),
    ])
    paras = [
        "C'est l'infection bactérienne d'une articulation native de l'adulte. Les recommandations françaises de 2020 exigent la ponction. Une prothèse n'est pas le sujet. "
        + L.B("w-dx7-def", "périmètre"),
        "L'incidence en Suisse ou en Europe n'est pas dans les pages lues : À vérifier. Le rang DX.7 vient de cette absence. E5 rappelle l'urgence. "
        + L.B("w-dx7-epi", "rang"),
        "Le germe infecte la synoviale. Les cristaux peuvent imiter. " + L.B("w-dx7-phys", "liquide"),
        "DX.7, rang d'exclusion E5. Toute monoarthrite aiguë fait évoquer ce diagnostic. " + L.B("w-dx7-dem", "urgence"),
        "Début, porte d'entrée, antibiotique déjà pris. La fièvre n'est pas exigée. " + L.B("w-dx7-ana", "questions"),
        "On compare à l'autre côté. Douleur au moindre mouvement. Crépitation : ce n'est plus une arthrite simple. " + L.B("w-dx7-exam", "geste"),
        "Monoarthrite, liquide purulent, gravité immédiate : trois conduites. " + L.B("w-dx7-synd", "tableaux"),
        "Le diagnostic positif est le liquide, culture et examen direct. La recommandation 9 parle du liquide purulent sans cristal. " + L.B("w-dx7-pos", "preuve"),
        "Radiographie de référence, échographie pour guider, cœur seulement dans des cas lus. " + L.B("w-dx7-ex", "examens"),
        "Ponction d'abord. Antibiotique après, sauf gravité ou liquide purulent sans cristal. " + L.B("w-dx7-arbre", "arbre"),
        "Sous 70 ans, céfazoline. Au-dessus, ceftriaxone ou céfotaxime. Aucun milligramme : À vérifier (AIPS). " + L.B("w-dx7-pec", "noms"),
        "Pas de programme de prévention lu. Ponctionner avant de traiter. " + L.B("w-dx7-prev", "prévention"),
        "Pas de fièvre exigée. Ponction avant l'antibiotique. Pas de milligramme. Prothèse exclue.",
        "Quatorze questions. " + L.B("w-dx7-pieges", "pièges") + " Répondez avant d'ouvrir.",
    ]
    sources = L.sources_section([
        "<sup class=\"s\">7</sup> Couderc M, Bart G, Coiffier G et al. Recommandations françaises 2020, arthrite septique sur articulation native de l'adulte. DOI 10.1016/j.jbspin.2020.07.012. Page ouverte lue le 31.10.2026.",
        "<sup class=\"s\">2</sup> Piqueres S, Staeger P, Pasche O. Revue Médicale Suisse 2016;537.",
        "<sup class=\"s\">8</sup> Swissmedic, Dafalgan comprimés, numéro 69266. Non utilisé ici comme traitement de l'arthrite.",
    ], "Les noms de céphalosporines viennent du texte français. Les milligrammes suisses ne sont pas affirmés : À vérifier (AIPS).")
    html = L.assembler(
        f"DX.7 — {NOM}", NOM,
        "DX.7 du cours F1.5. Le rang d'exclusion n'est pas le numéro DX. Texte du 31.10.2026.",
        f"<h2>DX.7 — {NOM}</h2>",
        "L'arthrite septique de l'adulte, sur articulation native, se documente par la ponction avant l'antibiotique. La fièvre n'est pas exigée. Aucun milligramme n'est écrit.",
        list(zip(paras, wins)),
        sources,
        "FIN_FICHIER LOT_134_Phase_B_DX.7",
        FICHIER,
        32000,
    )
    L.ecrire(FICHIER, html)
    (L.EVID / "sfr2020_arthrite.txt").write_text(
        "===== Recommandations françaises 2020, DOI 10.1016/j.jbspin.2020.07.012, phrases citées, lues le 31.10.2026 =====\n"
        + "\n".join(c.cites) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    construire()

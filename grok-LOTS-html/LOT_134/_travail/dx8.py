#!/usr/bin/env python3
"""DX.8 approfondi : péritonite aiguë généralisée.

Sources lues le 31.10.2026 :
- Revue Médicale Suisse 2016 (preuve déjà en extraits)
- WSES, consensus 2016 sur les infections intra-abdominales, PMC5418731,
  DOI 10.1186/s13017-017-0132-7. Aucun milligramme.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import profond_lib as L

NOM = "Péritonite aiguë généralisée"
FICHIER = "LOT_134_Phase_B_V0_DX.8.html"
SRC = Path("/tmp/wses_iai.txt")
L.GLOSS.update({
    "IAI": "infection intra-abdominale",
    "CIAI": "infection intra-abdominale compliquée",
    "CT": "tomodensitométrie",
    "SOFA": "score séquentiel d'évaluation des défaillances d'organe",
    "ICU": "soins intensifs",
    "RCT": "essai contrôlé randomisé",
    "WSES": "société mondiale de chirurgie d'urgence",
})
DOSE = re.compile(r"\b\d+(?:[.,]\d+)?\s?(?:mg|µg|mcg|g|UI|IU|ml|mL)\b")
MOTS = re.compile(r"\b(periton|source control|abdomen|sepsis|antibiotic|laparotom|contamination|resuscitation)\b", re.I)


def cliniques(texte, mots, n, deja):
    pris = []
    for p in L.phrases_source(texte):
        if p in deja or not MOTS.search(p):
            continue
        if mots and not any(m.lower() in p.lower() for m in mots):
            continue
        if DOSE.search(p) or "h-index" in p or p.count(",") > 7 or len(p) < 80:
            continue
        deja.add(p)
        pris.append(p)
        if len(pris) >= n:
            break
    return pris


def paquet(c, xs, prefix, theme):
    preuves = L.preuves(c, "WSES", prefix, theme, "le consensus de 2016", xs)
    lignes = [f"Les boutons ouvrent des phrases du consensus sur {theme}."]
    for i in range(1, len(xs) + 1):
        lignes.append(f"Phrase citée numéro {i} sur {theme}. " + L.B(f"{prefix}-q{i}", f"citation {i}"))
    return L.W(f"{prefix}-index", f"Citations : {theme}", lignes) + "\n" + preuves


def construire():
    brut = " ".join(SRC.read_text(encoding="utf-8", errors="replace").split())
    c = L.Corpus()
    c.texts["WSES"] = brut
    deja = set()
    themes = [
        ("w-dx8d", "la définition", ["periton", "contamination"], 10),
        ("w-dx8c", "le contrôle de la source", ["source control", "laparotom", "resuscitation"], 12),
        ("w-dx8i", "l'image", ["computed", "free air", "periton"], 8),
        ("w-dx8z", "le consensus", ["periton", "abdomen", "sepsis", "antibiotic"], 60),
    ]
    blocs = {}
    for prefix, theme, mots, n in themes:
        xs = cliniques(brut, mots, n, deja)
        print(theme, len(xs))
        if len(xs) < 3:
            raise SystemExit("peu " + theme)
        blocs[prefix] = paquet(c, xs, prefix, theme)
    rms = (
        "<p>«Il faut également rechercher des signes de péritonite localisée ou généralisée : "
        "signes de défense, de détente ou l’absence de bruits digestifs qui peuvent annoncer "
        "une pathologie grave telle qu’une perforation digestive.»</p>"
    )
    wins = [""] * 14
    wins[0] = L.W("w-dx8-def", "Localisée ou généralisée", [
        "Le mot désigne ici l'inflammation aiguë de toute la cavité, pas d'un seul foyer.",
        "L'article suisse la relie à une perforation digestive quand la défense, la détente ou le silence sont là.",
        "Une définition histologique séparée n'a pas été ouverte : À vérifier.",
        "Le consensus distingue une péritonite limitée à une zone et une péritonite diffuse, quand l'infection quitte l'organe.",
        "Les deux textes ne se contredisent pas : l'un décrit le signe, l'autre le passage hors de l'organe.",
    ]) + "\n" + L.fenetre("w-dx8-rms", "Phrase de la revue suisse", rms) + "\n" + blocs["w-dx8d"]
    wins[1] = L.W("w-dx8-epi", "Pas de taux pour 100 000", [
        "Pas de taux pour 100 000 dans les sources de ce diagnostic.",
        "Le rang DX.8 ne classe donc pas une fréquence mesurée.",
        "Le rang d'exclusion E2 la place juste après la fasciite, parce que le ventre de bois n'attend pas.",
        "Le consensus rappelle la morbidité et la mortalité, sans donner un pourcentage suisse.",
    ])
    wins[2] = L.W("w-dx8-phys", "Contamination puis inflammation", [
        "Une perforation ou une infection d'organe contamine le péritoine.",
        "La défense involontaire est la contraction que le patient ne commande pas.",
        "La détente est la douleur au relâchement.",
        "Le silence auscultatoire accompagne l'iléus.",
        "Le contrôle de la source arrête la contamination. L'antibiotique limite la diffusion. La réanimation soutient le malade grave.",
        "Aucun de ces trois gestes n'est dosé ici.",
    ]) + "\n" + blocs["w-dx8c"]
    wins[3] = L.W("w-dx8-dem", "E2", [
        "Ce diagnostic est DX.8. Son rang d'exclusion est E2.",
        "Seul E1, la fasciite, se cherche encore plus tôt sur la peau.",
        "Un ventre de bois passe avant l'anévrisme stable, l'appendice et la vésicule.",
        "On ne finit pas la liste des diagnostics fréquents avant d'avoir écarté ce tableau.",
    ])
    wins[4] = L.W("w-dx8-ana", "Début brutal", [
        "On demande l'heure du début, un ulcère, un diverticule, une chirurgie récente, une fièvre.",
        "Une douleur qui devient maximale d'emblée oriente vers la perforation.",
        "Le malaise et la chute de tension sont des drapeaux de gravité, pas un motif d'attendre.",
    ])
    wins[5] = L.W("w-dx8-exam", "Du superficiel au profond", [
        "La main part de la surface et n'enfonce qu'ensuite, les yeux sur le visage.",
        "La défense involontaire, la détente et le silence se cherchent.",
        "Aucun comprimé ne lève une contracture de tout l'abdomen.",
        "On distingue une défense locale, qui peut rester un foyer, d'une contracture de tout l'abdomen.",
    ])
    wins[6] = L.W("w-dx8-synd", "Deux étendues", [
        "Syndrome localisé : défense d'un quadrant, bruits encore présents ou non.",
        "Syndrome généralisé : contracture diffuse, silence, visage souffrant.",
        "Le second n'attend pas le scanner pour appeler le chirurgien.",
        "Le premier peut encore avoir une image si l'état le permet.",
    ]) + "\n" + blocs["w-dx8i"]
    wins[7] = L.W("w-dx8-pos", "Le tableau commande", [
        "Le diagnostic positif, devant la contracture généralisée, est chirurgical.",
        "L'imagerie ne doit pas retarder l'appel si la contracture est déjà généralisée.",
        "Une règle suisse qui interdirait toute image n'a pas été lue : À vérifier.",
        "Le consensus rappelle qu'un pneumopéritoine à distance, dans la diverticulite perforée, n'oblige pas toujours à opérer.",
        "Cette nuance ne s'applique pas au ventre de bois.",
    ])
    wins[8] = L.W("w-dx8-ex", "Image si l'état le permet", [
        "Le scanner précise la cause quand le malade peut le passer.",
        "Il ne remplace pas l'appel devant une contracture généralisée.",
        "La biologie ne nomme pas la perforation.",
        "Le lactate, s'il est pris, ne se substitue pas à l'examen.",
    ])
    wins[9] = L.W("w-dx8-arbre", "Si, alors", [
        "Si le ventre est de bois, on appelle le chirurgien et on réanime, sans attendre une image de confort.",
        "Si la défense est locale et l'état stable, l'image peut chercher la cause.",
        "Si le scanner montre de l'air libre à distance dans une diverticulite, le consensus dit que la chirurgie n'est pas automatique.",
        "Si la source continue de contaminer, le contrôle de la source est le geste lu.",
        "L'antibiotique accompagne, il ne remplace pas ce geste.",
    ])
    wins[10] = L.W("w-dx8-pec", "Sans milligramme", [
        "Pas de milligramme d'antibiotique ni d'antalgique propre à cette leçon.",
        "L'antalgique cité en Phase A ne ferme pas une perforation.",
        "L'antibiothérapie péri-opératoire se lit dans l'information professionnelle du produit choisi : À vérifier (AIPS).",
        "Les quatre piliers lus sont le diagnostic tôt, le contrôle de la source, l'antimicrobien adapté au risque, et la réanimation du malade grave.",
        "La surveillance cherche la tension, la diurèse, la contracture qui s'étend et le silence.",
    ]) + "\n" + blocs["w-dx8z"]
    wins[11] = L.W("w-dx8-prev", "Pas de dépistage", [
        "Aucun programme de prévention de la perforation n'a été lu.",
        "La prévention utile est de ne pas rassurer un ventre de bois avec un comprimé.",
    ])
    wins[13] = L.quiz("w-dx8-pieges", [
        ("Que cherche-t-on à la palpation ?",
         "Défense, détente, silence abdominal. La revue suisse les relie à une perforation possible."),
        ("Le ventre de bois attend-il le scanner ?",
         "Non. L'appel chirurgical ne se retarde pas."),
        ("Toute image est-elle interdite ?",
         "Une règle suisse qui l'interdirait n'a pas été lue. L'image se discute si l'état le permet."),
        ("L'air libre à distance oblige-t-il toujours à opérer ?",
         "Pas dans la diverticulite perforée, dit le consensus. Cela ne rassure pas un ventre de bois."),
        ("E2 veut-il dire le premier geste du lot ?",
         "Non. E1 est la fasciite. E2 vient juste après."),
        ("Y a-t-il un taux pour 100 000 ?",
         "Non dans les sources de ce diagnostic."),
        ("Le paracétamol traite-t-il la perforation ?",
         "Non."),
        ("Où est la dose d'antibiotique ?",
         "Absente. À vérifier (AIPS)."),
        ("Que sont les quatre piliers lus ?",
         "Diagnostic tôt, contrôle de la source, antimicrobien adapté, réanimation."),
        ("Défense locale et contracture diffuse sont-elles le même syndrome ?",
         "Non."),
        ("Une définition histologique a-t-elle été ouverte ?",
         "Non. À vérifier."),
        ("DX.8 classe-t-il une fréquence mesurée ?",
         "Non. Le dénominateur manque."),
        ("Le silence abdominal veut dire quoi ?",
         "L'absence de bruits, signe d'iléus dans le tableau grave."),
        ("Qui a écrit le consensus ?",
         "La société mondiale de chirurgie d'urgence, conférence de 2016, texte PMC5418731."),
    ])
    paras = [
        "C'est l'inflammation aiguë de l'ensemble de la cavité péritonéale. L'article suisse la relie à une perforation quand la défense, la détente ou le silence sont là. "
        + L.B("w-dx8-def", "étendue"),
        "Pas de taux pour 100 000. Le rang DX.8 ne mesure donc pas une fréquence. E2 vient juste après la fasciite. " + L.B("w-dx8-epi", "rang"),
        "La contamination du péritoine explique la défense. Le contrôle de la source l'arrête. " + L.B("w-dx8-phys", "piliers"),
        "DX.8, rang d'exclusion E2. Le ventre de bois n'attend pas la fin de la liste. " + L.B("w-dx8-dem", "urgence"),
        "Heure du début, ulcère, diverticule, chirurgie récente. " + L.B("w-dx8-ana", "histoire"),
        "On palpe du superficiel au profond, en regardant le visage. Un ventre de bois ne se rend pas par un comprimé. " + L.B("w-dx8-exam", "geste"),
        "Défense d'un quadrant n'est pas contracture de tout l'abdomen. " + L.B("w-dx8-synd", "syndromes"),
        "Devant la contracture généralisée, le diagnostic est chirurgical. L'image ne retarde pas l'appel. " + L.B("w-dx8-pos", "décision"),
        "Le scanner cherche la cause si l'état le permet. La biologie ne nomme pas la perforation. " + L.B("w-dx8-ex", "examens"),
        "Ventre de bois : chirurgien et réanimation. Défense locale stable : l'image peut aider. " + L.B("w-dx8-arbre", "arbre"),
        "Pas de milligramme. Le paracétamol de la Phase A ne traite pas une perforation. À vérifier (AIPS). " + L.B("w-dx8-pec", "moyens"),
        "Pas de dépistage lu. Ne pas rassurer un ventre de bois. " + L.B("w-dx8-prev", "prévention"),
        "Défense, détente, silence. E2. Pas de comprimé. Pas de milligramme.",
        "Quatorze questions. " + L.B("w-dx8-pieges", "pièges") + " Répondez avant d'ouvrir.",
    ]
    sources = L.sources_section([
        "<sup class=\"s\">2</sup> Piqueres S, Staeger P, Pasche O. Revue Médicale Suisse 2016;537, 2 novembre 2016.",
        "<sup class=\"s\">6</sup> Sartelli M et al. Consensus WSES 2016 sur les infections intra-abdominales. PMC5418731. DOI 10.1186/s13017-017-0132-7. Texte intégral lu le 31.10.2026.",
    ], "Aucune dose n'est affirmée. À vérifier (AIPS) pour l'antibiotique choisi.")
    html = L.assembler(
        f"DX.8 — {NOM}", NOM,
        "DX.8 du cours F1.5. Le rang d'exclusion n'est pas le numéro DX. Texte du 31.10.2026.",
        f"<h2>DX.8 — {NOM}</h2>",
        "La péritonite aiguë généralisée est un ventre de bois. La revue suisse y joint la défense, la détente et le silence, annonce possible d'une perforation. Le contrôle de la source ne s'écrit pas en milligrammes.",
        list(zip(paras, wins)),
        sources,
        "FIN_FICHIER LOT_134_Phase_B_DX.8",
        FICHIER,
        30000,
    )
    L.ecrire(FICHIER, html)
    (L.EVID / "wses2016_peritonite.txt").write_text(
        "===== WSES infections intra-abdominales, PMC5418731, phrases citées, lues le 31.10.2026 =====\n"
        + "\n".join(c.cites) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    construire()

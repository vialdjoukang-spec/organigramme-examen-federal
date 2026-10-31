#!/usr/bin/env python3
"""DX.5 approfondi : cirrhose hépatique.

Sources lues le 31.10.2026 :
- Revue Médicale Suisse 2016 et information professionnelle Dafalgan, n° 69266 (déjà en preuves)
- brouillon final du panel EASL déposé à l'UCL (eprint 10053258), même définition
  que le texte publié J Hepatol 2018, DOI 10.1016/j.jhep.2018.03.024.
  Le PDF du journal a renvoyé 403 : les phrases viennent de ce brouillon, pas d'une dose.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import profond_lib as L

NOM = "Cirrhose hépatique"
FICHIER = "LOT_134_Phase_B_V0_DX.5.html"
SRC = Path("/home/ubuntu/.cursor/projects/workspace/agent-tools/9a0562e9-fceb-4085-b308-1ef2fa0ee6da.txt")
L.GLOSS.update({
    "EASL": "association européenne pour l'étude du foie",
    "SBP": "péritonite bactérienne spontanée",
    "HRS": "syndrome hépatorénal",
    "AKI": "atteinte rénale aiguë",
    "ACLF": "défaillance aiguë sur chronique",
    "LT": "transplantation hépatique",
    "GI": "gastro-intestinal",
    "HPS": "syndrome hépatopulmonaire",
    "CCM": "cardiomyopathie cirrhotique",
    "PPHT": "hypertension portopulmonaire",
    "NSBB": "bêtabloquant non cardiosélectif",
    "LVP": "paracentèse évacuatrice",
    "SAAG": "gradient d'albumine sérum-ascite",
    "PMN": "polynucléaires neutrophiles",
    "TIPS": "shunt intrahépatique portosystémique",
    "MDRO": "bactérie multirésistante",
    "RCT": "essai contrôlé randomisé",
    "AASLD": "association américaine pour l'étude des maladies du foie",
})
DOSE = re.compile(r"\b\d+(?:[.,]\d+)?\s?(?:mg|µg|mcg|g|UI|IU|ml|mL)\b")
MOTS = re.compile(r"\b(ascites|cirrhosis|paracentesis|encephalopathy|bleeding|jaundice|decompensat|spleen|albumin|infection)\b", re.I)


def cliniques(texte, mots, n, deja):
    pris = []
    for p in L.phrases_source(texte):
        if p in deja or "typesetter" in p or not MOTS.search(p):
            continue
        if mots and not any(m.lower() in p.lower() for m in mots):
            continue
        if p.count(",") > 6 or DOSE.search(p) or "AASLD" in p:
            continue
        deja.add(p)
        pris.append(p)
        if len(pris) >= n:
            break
    return pris


def paquet(c, xs, prefix, theme):
    preuves = L.preuves(c, "EASL", prefix, theme, "le brouillon final du panel européen, 2018", xs)
    lignes = [f"Les boutons ouvrent des phrases du texte européen sur {theme}."]
    for i in range(1, len(xs) + 1):
        lignes.append(f"Phrase citée numéro {i} sur {theme}. " + L.B(f"{prefix}-q{i}", f"citation {i}"))
    return L.W(f"{prefix}-index", f"Citations : {theme}", lignes) + "\n" + preuves


def construire():
    brut = " ".join(SRC.read_text(encoding="utf-8", errors="replace").split())
    c = L.Corpus()
    c.texts["EASL"] = brut
    deja = set()
    themes = [
        ("w-dx5d", "la décompensation", ["decompensat", "ascites", "encephalopathy", "jaundice"], 12),
        ("w-dx5a", "l'ascite", ["ascites", "paracentesis"], 14),
        ("w-dx5i", "l'infection", ["infection", "paracentesis"], 10),
        ("w-dx5z", "le texte", ["cirrhosis", "ascites", "bleeding", "encephalopathy"], 55),
    ]
    blocs = {}
    for prefix, theme, mots, n in themes:
        xs = cliniques(brut, mots, n, deja)
        print(theme, len(xs))
        if len(xs) < 4:
            raise SystemExit("peu " + theme)
        blocs[prefix] = paquet(c, xs, prefix, theme)
    aips = (
        "<p>«Troubles fonctionnels hépatiques graves (cirrhose hépatique et ascite)/hépatite aiguë ou maladie hépatique décompensée active.»</p>"
        "<p>«La dose quotidienne ne doit pas dépasser 2 g»</p>"
    )
    wins = [""] * 14
    wins[0] = L.W("w-dx5-def", "Deux mots à ne pas confondre", [
        "La cirrhose est le stade où la fibrose remplace l'architecture du foie.",
        "Une définition histologique de société, pour le seul mot cirrhose, n'a pas été ouverte : À vérifier.",
        "Le texte européen de 2018 définit la phase décompensée, pas la lame d'histologie.",
        "Cette phase est marquée par l'ascite, le saignement, l'encéphalopathie ou l'ictère.",
        "Le signe palpé n'est qu'un bord, une rate ou un flot, pas le diagnostic histologique.",
    ]) + "\n" + blocs["w-dx5d"]
    wins[1] = L.W("w-dx5-epi", "Ne pas mélanger les dénominateurs", [
        "Le taux de cirrhose dans la population, lui, n'a pas été lu : À vérifier.",
        "L'article suisse estime à 5 % la prévalence de l'ascite en médecine de premier recours.",
        "Ce 5 % n'est pas la prévalence de la cirrhose.",
        "Il sert à chercher l'ascite, pas à classer la cirrhose parmi les maladies rares.",
    ])
    wins[2] = L.W("w-dx5-phys", "Pression portale et signes", [
        "La pression portale monte, la fonction baisse, puis les signes apparaissent.",
        "L'ascite est du liquide dans le péritoine, pas un simple bord dur.",
        "Le saignement, l'encéphalopathie et l'ictère sont les autres marques lues de la décompensation.",
        "Une infection ou un carcinome peuvent accélérer l'évolution, dit le texte, sans pourcentage recopié.",
        "Le paracétamol n'est pas le traitement de cette cascade : il est limité, voire contre-indiqué.",
    ])
    wins[3] = L.W("w-dx5-dem", "E9, pas une urgence de tête", [
        "Ce diagnostic est DX.5. Son rang d'exclusion est E9.",
        "Une défense généralisée, une ischémie ou une rupture vasculaire passent avant le bord hépatique.",
        "Un flot d'ascite ne ferme pas le diagnostic de cirrhose.",
    ])
    wins[4] = L.W("w-dx5-ana", "Ce qui change la main", [
        "On demande l'alcool, les virus, le gonflement, le saignement, la confusion et l'ictère.",
        "Une ascite nouvelle de grade 2 ou 3, dans le texte européen, appelle une ponction diagnostique.",
        "Ce grade n'est pas une règle suisse séparée relue ailleurs.",
        "La fièvre ou le choc avec ascite font chercher l'infection du liquide, sans attendre.",
    ]) + "\n" + blocs["w-dx5a"]
    wins[5] = L.W("w-dx5-exam", "Bord, rate, flot", [
        "On cherche le bord du foie, la rate et le flot d'ascite.",
        "La revue suisse rappelle qu'un foie palpé corrèle mal avec une vraie hépatomégalie.",
        "L'absence de foie palpé n'exclut pas l'hépatomégalie.",
        "On ne transforme pas ces rapports de vraisemblance en diagnostic de cirrhose.",
    ])
    wins[6] = L.W("w-dx5-synd", "Syndromes", [
        "Syndrome compensé : pas d'ascite, pas de saignement, pas d'encéphalopathie, pas d'ictère, selon la description lue.",
        "Syndrome décompensé : au moins un de ces quatre signes.",
        "Syndrome infectieux sur ascite : fièvre ou choc, ponction.",
        "On ne palpe pas le premier comme s'il était le troisième.",
    ]) + "\n" + blocs["w-dx5i"]
    wins[7] = L.W("w-dx5-pos", "Ce qui ne suffit pas", [
        "Le diagnostic positif de la cirrhose n'est pas le bord palpé.",
        "L'échographie et, si besoin, une évaluation spécialisée viennent ensuite.",
        "Les critères non invasifs suisses exacts sont À vérifier.",
        "La décompensation, elle, se reconnaît aux signes cliniques lus, puis se documente.",
    ])
    wins[8] = L.W("w-dx5-ex", "Ponction et image", [
        "L'échographie voit le foie, la rate et l'ascite.",
        "Une ascite nouvelle de grade 2 ou 3 justifie une ponction diagnostique dans le texte européen.",
        "À l'admission, la même famille de recommandations demande la ponction sans délai pour écarter l'infection du liquide.",
        "Le seuil suisse de cette ponction, s'il diffère, est À vérifier.",
        "On ne dose pas l'albumine du liquide de mémoire.",
    ])
    wins[9] = L.W("w-dx5-arbre", "Si, alors", [
        "Si l'on palpe seulement un bord, on n'écrit pas cirrhose.",
        "Si l'ascite est nouvelle et au moins modérée, le texte européen recommande la ponction.",
        "Si la fièvre ou le choc s'y ajoute, la ponction cherche l'infection du liquide.",
        "Si la cirrhose avec ascite est connue, le paracétamol de Dafalgan est contre-indiqué.",
        "Si une autre spécialité est choisie, sa dose est À vérifier (AIPS).",
    ])
    wins[10] = L.W("w-dx5-pec", "Le seul milligramme lu", [
        "Le paracétamol de Dafalgan comprimés, numéro 69266, est contre-indiqué dans la cirrhose avec ascite.",
        "La maladie hépatique chronique limite la journée à 2 g, phrase lue dans la même information professionnelle.",
        "Cette phrase suit l'énumération de la maladie hépatique chronique, de l'alcoolisme, de la dénutrition, de la déshydratation et de la cachexie.",
        "Aucun autre milligramme, diurétique compris, n'est écrit ici.",
        "Le but est de traiter la cause et la complication, pas d'ajouter un antalgique interdit.",
        "La surveillance cherche l'ictère, la confusion, le saignement et la fièvre.",
    ]) + "\n" + L.fenetre("w-dx5-aips", "Phrases de l'information professionnelle", aips) + "\n" + blocs["w-dx5z"]
    wins[11] = L.W("w-dx5-prev", "Cause tôt", [
        "Le panel insiste pour traiter la cause le plus tôt possible, à tout degré de maladie.",
        "Aucun programme suisse de dépistage chiffré n'a été lu pour cette leçon : À vérifier.",
        "Éviter le paracétamol au-delà de la phrase lue est déjà une prévention de l'aggravation.",
    ])
    wins[13] = L.quiz("w-dx5-pieges", [
        ("Palper le foie, est-ce la cirrhose ?",
         "Non. Le bord n'est pas l'histologie."),
        ("Que marque la décompensation dans le texte européen ?",
         "L'ascite, le saignement, l'encéphalopathie ou l'ictère."),
        ("Le 5 % suisse est-il la prévalence de la cirrhose ?",
         "Non. C'est l'ascite en médecine de premier recours. La prévalence de la cirrhose est À vérifier."),
        ("Dafalgan et cirrhose avec ascite ?",
         "Contre-indiqué, information professionnelle, numéro 69266."),
        ("Quelle dose maximale est écrite dans la maladie hépatique chronique ?",
         "2 g par jour, dans la même information, avec d'autres situations."),
        ("Un diurétique est-il dosé ici ?",
         "Non. À vérifier (AIPS)."),
        ("Quand le texte européen demande-t-il une ponction ?",
         "Ascite nouvelle de grade 2 ou 3, ou aggravation, et sans délai à l'admission pour écarter l'infection du liquide."),
        ("Ce grade est-il une règle suisse séparée ?",
         "Non. Il est dans le texte européen lu. L'écart suisse est À vérifier."),
        ("E9 est-il l'urgence maximale ?",
         "Non. Plusieurs diagnostics du lot s'excluent avant."),
        ("L'absence de foie palpé exclut-elle l'hépatomégalie ?",
         "Non, dit la revue suisse."),
        ("Peut-on écrire un pourcentage de mortalité ?",
         "Non. Il n'a pas été recopié."),
        ("La phase compensée a-t-elle déjà ces quatre signes ?",
         "Non, selon la description lue."),
        ("D'où viennent les phrases sur 2 g ?",
         "De l'information professionnelle suisse, pas du texte européen."),
        ("Le brouillon et le journal sont-ils la même page ?",
         "Le PDF du journal a renvoyé 403. Les phrases viennent du brouillon final du panel, déposé, dont la définition recoupe le résumé publié."),
    ])
    paras = [
        "La cirrhose est le stade d'une maladie chronique du foie où la fibrose remplace l'architecture. Le signe palpé n'est qu'un bord, une rate ou un flot. "
        + L.B("w-dx5-def", "décompensation"),
        "La prévalence de la cirrhose elle-même est À vérifier. L'article suisse estime à 5 % la prévalence de l'ascite en médecine de premier recours, ce qui n'est pas le même dénominateur. "
        + L.B("w-dx5-epi", "5 %"),
        "La pression portale et la fonction expliquent les signes, pas le seul bord. " + L.B("w-dx5-phys", "cascade"),
        "Ce diagnostic est DX.5, rang d'exclusion E9. Les urgences abdominales du lot passent avant. " + L.B("w-dx5-dem", "rang"),
        "Alcool, virus, ascite, saignement, confusion, ictère. " + L.B("w-dx5-ana", "questions"),
        "On palpe le bord, la rate et le flot. La corrélation avec l'hépatomégalie est mauvaise. " + L.B("w-dx5-exam", "main"),
        "Compensé, décompensé, infectieux : trois tableaux. " + L.B("w-dx5-synd", "syndromes"),
        "Le diagnostic positif n'est pas le bord palpé. Les critères non invasifs suisses sont À vérifier. " + L.B("w-dx5-pos", "preuve"),
        "L'échographie précède. La ponction diagnostique est dans le texte européen pour l'ascite nouvelle. " + L.B("w-dx5-ex", "examens"),
        "Bord seul : pas de cirrhose. Ascite nouvelle : ponction selon le texte lu. Cirrhose avec ascite : pas ce paracétamol. " + L.B("w-dx5-arbre", "arbre"),
        "Dafalgan, numéro 69266, est contre-indiqué dans la cirrhose avec ascite. Plafond lu : 2 g par jour dans la maladie hépatique chronique. "
        + L.B("w-dx5-pec", "information professionnelle"),
        "Traiter la cause tôt. Le dépistage suisse chiffré est À vérifier. " + L.B("w-dx5-prev", "prévention"),
        "Le bord n'est pas la cirrhose. L'ascite à 5 % n'est pas la prévalence de la maladie. Deux grammes, pas plus, et contre-indiqué si ascite.",
        "Quatorze questions. " + L.B("w-dx5-pieges", "pièges") + " Répondez avant d'ouvrir.",
    ]
    sources = L.sources_section([
        "<sup class=\"s\">2</sup> Piqueres S, Staeger P, Pasche O. Revue Médicale Suisse 2016;537, 2 novembre 2016.",
        "<sup class=\"s\">8</sup> Swissmedic, Dafalgan comprimés, numéro 69266. Information professionnelle lue le 31.10.2026.",
        "<sup class=\"s\">4</sup> Association européenne pour l'étude du foie. Cirrhose décompensée, 2018. Brouillon final du panel, UCL eprint 10053258, lu le 31.10.2026. DOI publié 10.1016/j.jhep.2018.03.024. Le PDF du journal a renvoyé 403.",
    ], "Seule la phrase sur 2 g est une dose, et elle vient de l'information professionnelle. Aucun diurétique n'est dosé.")
    html = L.assembler(
        f"DX.5 — {NOM}", NOM,
        "DX.5 du cours F1.5. Le rang d'exclusion n'est pas le numéro DX. Texte du 31.10.2026.",
        f"<h2>DX.5 — {NOM}</h2>",
        "La cirrhose ne se palpe pas comme une preuve. L'ascite, le saignement, l'encéphalopathie et l'ictère marquent la décompensation dans le texte européen lu. Le paracétamol de Dafalgan est contre-indiqué s'il y a une ascite.",
        list(zip(paras, wins)),
        sources,
        "FIN_FICHIER LOT_134_Phase_B_DX.5",
        FICHIER,
        38000,
    )
    L.ecrire(FICHIER, html)
    (L.EVID / "easl2018_cirrhose.txt").write_text(
        "===== EASL cirrhose décompensée, brouillon final UCL eprint 10053258, phrases citées, lues le 31.10.2026 =====\n"
        + "\n".join(c.cites) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    construire()

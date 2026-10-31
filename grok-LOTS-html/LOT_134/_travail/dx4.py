#!/usr/bin/env python3
"""DX.4 approfondi : appendicite aiguë. RMS 2016 et WSES Jérusalem 2020 (PMC7386163), lus le 31.10.2026."""
from __future__ import annotations

import html as htmlmod
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import profond_lib as L

NOM = "Appendicite aiguë"
FICHIER = "LOT_134_Phase_B_V0_DX.4.html"
SRC = Path("/tmp/wses_app.txt")
L.GLOSS.update({
    "AA": "appendicite aiguë",
    "RCT": "essai contrôlé randomisé",
    "NOM": "traitement non opératoire",
    "US": "échographie",
})
DOSE = re.compile(r"\b\d+(?:[.,]\d+)?\s?(?:mg|µg|mcg|g|UI|IU|ml|mL)\b")
MOTS = re.compile(r"\b(appendic|Alvarado|ultrasound|laparoscop|antibiotic|pregnant|score|diagnosis|delay|abscess)\b", re.I)


def cliniques(texte, mots, n, deja):
    pris = []
    for p in L.phrases_source(texte):
        if p in deja or not MOTS.search(p) or (mots and not any(m.lower() in p.lower() for m in mots)):
            continue
        if p.count(",") > 6 or DOSE.search(p) or "http" in p:
            continue
        deja.add(p)
        pris.append(p)
        if len(pris) >= n:
            break
    return pris


def paquet(c, xs, prefix, theme):
    preuves = L.preuves(c, "WSES", prefix, theme, "le consensus de Jérusalem 2020", xs)
    lignes = [f"Les boutons ouvrent des phrases du consensus de 2020 sur {theme}."]
    for i in range(1, len(xs) + 1):
        lignes.append(f"Phrase citée numéro {i} sur {theme}. " + L.B(f"{prefix}-q{i}", f"citation {i}"))
    return L.W(f"{prefix}-index", f"Citations : {theme}", lignes) + "\n" + preuves


def construire():
    brut = " ".join(htmlmod.unescape(SRC.read_text(encoding="utf-8", errors="replace")).split())
    c = L.Corpus()
    c.texts["WSES"] = brut
    deja = set()
    themes = [
        ("w-dx4d", "le score", ["Alvarado", "score"], 12),
        ("w-dx4c", "la chirurgie", ["appendectomy", "delay", "24"], 12),
        ("w-dx4i", "l'image", ["ultrasound", "CT", "imaging", "pregnant"], 10),
        ("w-dx4n", "le non opératoire", ["non-operative", "antibiotic", "abscess"], 10),
        ("w-dx4z", "le consensus", ["appendic"], 52),
    ]
    blocs = {}
    for prefix, theme, mots, n in themes:
        xs = cliniques(brut, mots, n, deja)
        print(theme, len(xs))
        if len(xs) < 3:
            raise SystemExit("peu de phrases " + theme)
        blocs[prefix] = paquet(c, xs, prefix, theme)
    rms = (
        "<p>«La prévalence des appendicites parmi les consultations ambulatoires pour douleurs abdominales aiguës en MPR "
        "est estimée à 1 % alors que l’incidence dans la population générale est de 9 cas pour 100 000 personnes par année.»</p>"
        "<p>«Un score &lt; 4 permet en principe d’éviter une intervention chirurgicale.»</p>"
        "<p>«Un score ≥ 7 est fortement évocateur d’une appendicite et devrait orienter vers une stratégie opératoire (RV+ 3,1 ; RV- 0,26).»</p>"
    )
    wins = [""] * 14
    wins[0] = L.W("w-dx4-def", "Nom et point", [
        "C'est l'inflammation aiguë de l'appendice iléo-cæcal.",
        "L'article suisse de 2016 ne cite pas une définition d'une société mondiale unique.",
        "Un point de McBurney, seul, ne porte pas le nom.",
        "Le consensus de 2020 demande une démarche adaptée à l'âge, au sexe et aux signes, pas un seul point.",
    ])
    wins[1] = L.W("w-dx4-rms", "Deux dénominateurs", [
        "La part lue en médecine de premier recours est d'environ un pour cent des douleurs abdominales aiguës.",
        "Le second chiffre lu est neuf cas pour 100 000 personnes chaque année.",
        "Ces deux dénominateurs ne doivent pas être additionnés.",
        "Le rapport de vraisemblance positif lu pour un score d'au moins 7 est 3,1.",
        "Le rapport de vraisemblance négatif lu pour ce seuil est 0,26.",
    ]) + "\n" + L.fenetre("w-dx4-citrms", "Phrases de la revue suisse", rms) + "\n" + blocs["w-dx4d"]
    wins[2] = L.W("w-dx4-phys", "De la lumière à la défense", [
        "La lumière se bouche, la paroi s'infecte, la douleur migre vers la fosse iliaque droite.",
        "La perforation ou l'abcès changent le tableau et la voie.",
        "Le score ne montre pas cette cascade : il trie seulement.",
        "Aucun antibiotique de cette leçon n'est dosé en milligrammes.",
    ])
    wins[3] = L.W("w-dx4-dem", "E6 dans le lot", [
        "Ce diagnostic est DX.4. Son rang d'exclusion est E6.",
        "Une défense généralisée ou une instabilité vasculaire passe avant la fosse iliaque.",
        "On ne rassure pas sur un score bas si l'abdomen se contracte partout.",
    ])
    wins[4] = L.W("w-dx4-ana", "Ce que l'histoire change", [
        "L'histoire utile porte sur la migration de la douleur, la fièvre, les vomissements, l'anorexie et la toux qui réveille la douleur.",
        "Une grossesse extra-utérine reste à écarter chez la femme avant de fermer le diagnostic.",
        "La règle suisse du dosage avant l'image est À vérifier.",
        "Le consensus de 2020 dit de ne pas décider chez la femme enceinte sur les seuls symptômes.",
    ]) + "\n" + blocs["w-dx4i"]
    wins[5] = L.W("w-dx4-exam", "Fosse iliaque, pas un point magique", [
        "On palpe la fosse iliaque droite et on cherche une défense locale.",
        "Le point de McBurney isolé ne fait pas le diagnostic.",
        "La toux douloureuse est un signe d'irritation, pas une preuve.",
        "On compare à l'aine et à l'hypocondre droit pour ne pas nommer une autre douleur.",
    ])
    wins[6] = L.W("w-dx4-synd", "Trois tableaux", [
        "Syndrome simple : migration, fièvre modérée, défense locale.",
        "Syndrome compliqué : abcès ou phlegmon, masse, fièvre plus marquée.",
        "Syndrome de péritonite : la défense dépasse la fosse.",
        "Le score d'Alvarado aide le premier, il ne classe pas le troisième à lui seul.",
    ])
    wins[7] = L.W("w-dx4-pos", "Revue suisse et consensus, les deux", [
        "La revue de 2016 : un score sous 4 évite en principe la chirurgie.",
        "La même revue : un score d'au moins 7 oriente vers une stratégie opératoire.",
        "Le consensus de 2020 : le score d'Alvarado n'est pas assez spécifique chez l'adulte pour porter seul le diagnostic.",
        "On ne cache pas cette tension : le score trie, il ne remplace pas l'image.",
        "Le diagnostic positif combine la clinique et l'imagerie.",
    ])
    wins[8] = L.W("w-dx4-ex", "Image après le tri", [
        "L'échographie est souvent la première image, surtout chez le jeune et la femme enceinte, selon les chapitres lus.",
        "Le scanner se discute quand l'échographie ne tranche pas : le seuil suisse exact est À vérifier.",
        "Le consensus refuse de conclure chez la femme enceinte sur les signes seuls.",
        "La biologie seule ne nomme pas l'appendice.",
    ])
    wins[9] = L.W("w-dx4-arbre", "Si, alors", [
        "Si le score est sous 4 et l'examen est rassurant, la revue suisse évite en principe l'opération.",
        "Si le score atteint 7, la même revue oriente vers une stratégie opératoire, sans sauter l'image.",
        "Si l'appendicite simple est retenue, le consensus de 2020 vise l'opération dans les 24 heures, en réduisant l'attente.",
        "Le même texte dit qu'attendre jusqu'à 24 heures après l'admission ne paraît pas augmenter le risque de forme compliquée.",
        "Ces 24 heures sont celles du consensus mondial, pas un règlement d'hôpital suisse relu à part.",
        "Si l'abdomen est contracté partout, on ne reste pas sur le score.",
    ]) + "\n" + blocs["w-dx4c"]
    wins[10] = L.W("w-dx4-pec", "Sans milligramme", [
        "Pas de milligramme d'antibiotique dans cette leçon.",
        "Le paracétamol, s'il est utilisé, reste celui de la Phase A.",
        "Le traitement non opératoire est discuté dans le consensus, sans dose suisse : À vérifier (AIPS).",
        "L'heure suisse de l'appendicectomie n'est pas dans la revue de 2016.",
        "La surveillance après une décision d'attente cherche la fièvre, la défense qui s'étend et le vomissement.",
    ]) + "\n" + blocs["w-dx4n"] + "\n" + blocs["w-dx4z"]
    wins[11] = L.W("w-dx4-prev", "Pas de programme lu", [
        "Aucun dépistage de l'appendicite n'a été lu.",
        "La prévention utile ici est de ne pas rassurer sur un seul point douloureux.",
    ])
    wins[13] = L.quiz("w-dx4-pieges", [
        ("Quelle part en premier recours ?",
         "Environ 1 % des douleurs abdominales aiguës. L'incidence lue est 9 pour 100 000 et par an. On n'additionne pas."),
        ("Que fait un score sous 4 selon la revue suisse ?",
         "Il permet en principe d'éviter la chirurgie."),
        ("Que fait un score d'au moins 7 ?",
         "Il est fortement évocateur et oriente vers une stratégie opératoire. RV+ 3,1 et RV- 0,26."),
        ("Le consensus de 2020 se contente-t-il d'Alvarado chez l'adulte ?",
         "Non. Il le dit pas assez spécifique pour le diagnostic adulte."),
        ("Le point de McBurney suffit-il ?",
         "Non."),
        ("Quel délai opératoire est écrit pour la forme simple ?",
         "Dans les 24 heures, consensus de 2020, pas un règlement suisse séparé."),
        ("Attendre 24 heures après l'admission aggrave-t-il forcément ?",
         "Le même texte dit que cela ne paraît pas être un facteur de forme compliquée."),
        ("Où est la dose d'antibiotique ?",
         "Absente. À vérifier (AIPS)."),
        ("La femme enceinte se décide-t-elle sur les signes seuls ?",
         "Non, dit le consensus. Le dosage suisse avant l'image reste À vérifier."),
        ("E6 est-il la première urgence du lot ?",
         "Non. Plusieurs rangs d'exclusion passent avant."),
        ("Peut-on ajouter 1 % et 9 pour 100 000 ?",
         "Non. Les dénominateurs diffèrent."),
        ("L'image est-elle facultative si le score est haut ?",
         "Non dans cette leçon : le score trie, il ne remplace pas l'image."),
        ("Le paracétamol est-il redosé ?",
         "Non. Il reste celui de la Phase A."),
        ("Une défense de tout l'abdomen reste-t-elle une appendicite simple ?",
         "Non. On sort du score et on pense péritonite."),
    ])
    paras = [
        "C'est l'inflammation aiguë de l'appendice iléo-cæcal. Le diagnostic ne repose pas sur un seul point de McBurney. " + L.B("w-dx4-def", "nom"),
        "En médecine de premier recours, environ 1 % des douleurs abdominales aiguës sont une appendicite. L'incidence lue est de 9 cas pour 100 000 personnes et par année. "
        + L.B("w-dx4-rms", "chiffres"),
        "La lumière se bouche, puis la douleur migre. " + L.B("w-dx4-phys", "cascade") + " Le score ne photographie pas la paroi.",
        "Ce diagnostic est DX.4, rang d'exclusion E6. Une péritonite ou une instabilité passe avant. " + L.B("w-dx4-dem", "rang"),
        "On cherche la migration, la fièvre, les vomissements, l'anorexie et la toux douloureuse. Chez la femme, une grossesse extra-utérine reste un drapeau. "
        + L.B("w-dx4-ana", "histoire"),
        "On palpe la fosse iliaque droite. Le point isolé ne suffit pas. " + L.B("w-dx4-exam", "geste"),
        "Le syndrome simple n'est pas l'abcès, ni la contracture de tout l'abdomen. " + L.B("w-dx4-synd", "tableaux"),
        "Le score d'Alvarado aide à trier, il ne remplace pas l'image. Un score d'au moins 7 oriente vers une stratégie opératoire. Un score sous 4 évite en principe la chirurgie. "
        + L.B("w-dx4-pos", "tension des sources"),
        "La clinique et l'image se complètent. Le seuil suisse du scanner est À vérifier. " + L.B("w-dx4-ex", "image"),
        "Forme simple retenue : le consensus de 2020 vise l'opération dans les 24 heures. Ce n'est pas un règlement suisse séparé. " + L.B("w-dx4-arbre", "délai"),
        "Pas de milligramme d'antibiotique. Le paracétamol reste celui de la Phase A. À vérifier (AIPS) pour le reste. " + L.B("w-dx4-pec", "moyens"),
        "Pas de dépistage lu. " + L.B("w-dx4-prev", "prévention"),
        "Un pour cent en premier recours, neuf pour 100 000 en population. Le score trie. L'image confirme. Pas de milligramme.",
        "Quatorze questions. " + L.B("w-dx4-pieges", "pièges") + " Répondez avant d'ouvrir.",
    ]
    sources = L.sources_section([
        "<sup class=\"s\">2</sup> Piqueres S, Staeger P, Pasche O. Revue Médicale Suisse 2016;537, 2 novembre 2016.",
        "<sup class=\"s\">6</sup> Di Saverio S et al. Mise à jour 2020 des recommandations de Jérusalem sur l'appendicite aiguë. Texte intégral lu le 31.10.2026, PMC7386163.",
        "<sup class=\"s\">4</sup> Wanhainen A et al. Société européenne de chirurgie vasculaire, 2024.",
        "<sup class=\"s\">5</sup> Björck M et al. Maladies des artères et veines mésentériques. Publié le 29.3.2017.",
        "<sup class=\"s\">7</sup> Couderc M et al. Recommandations françaises, 3 août 2020.",
        "<sup class=\"s\">8</sup> Swissmedic, Dafalgan comprimés, numéro 69266.",
    ], "Les seuils 4 et 7 viennent de la revue suisse. Les 24 heures viennent du consensus de 2020. Aucune dose n'est affirmée.")
    html = L.assembler(
        f"DX.4 — {NOM}", NOM,
        "DX.4 du cours F1.5. Le rang d'exclusion n'est pas le numéro DX. Texte du 31.10.2026.",
        f"<h2>DX.4 — {NOM}</h2>",
        "L'appendicite aiguë est l'inflammation de l'appendice. En premier recours, environ 1 % des douleurs abdominales aiguës. Le score aide, il ne remplace pas l'image, et aucun milligramme n'est écrit.",
        list(zip(paras, wins)),
        sources,
        "FIN_FICHIER LOT_134_Phase_B_DX.4",
        FICHIER,
        40000,
    )
    L.ecrire(FICHIER, html)
    (L.EVID / "wses2020_appendicite.txt").write_text(
        "===== WSES Jérusalem 2020, PMC7386163, phrases citées, lues le 31.10.2026 =====\n" + "\n".join(c.cites) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    construire()

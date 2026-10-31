#!/usr/bin/env python3
"""DX.10 approfondi : fasciite nécrosante.

Texte lu le 31.10.2026 : consensus WSES/SIS-E 2018, PMC6295010,
DOI 10.1186/s13017-018-0219-9. Aucun milligramme suisse.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import profond_lib as L

NOM = "Fasciite nécrosante"
FICHIER = "LOT_134_Phase_B_V0_DX.10.html"
SRC = Path("/tmp/wses_ssti.txt")
L.GLOSS.update({
    "NSTI": "infection nécrosante des tissus mous",
    "SSTI": "infection de la peau et des tissus mous",
    "LRINEC": "score de laboratoire du risque d'infection nécrosante",
    "CT": "tomodensitométrie",
    "MRI": "imagerie par résonance magnétique",
    "WSES": "société mondiale de chirurgie d'urgence",
    "ICU": "soins intensifs",
    "SOFA": "score séquentiel d'évaluation des défaillances d'organe",
})
DOSE = re.compile(r"\b\d+(?:[.,]\d+)?\s?(?:mg|µg|mcg|g|UI|IU|ml|mL)\b")
MOTS = re.compile(r"\b(necrot|fasci|NSTI|LRINEC|surgical|soft tissue|crepit|debrid)\b", re.I)


def cliniques(texte, mots, n, deja):
    pris = []
    for p in L.phrases_source(texte):
        if p in deja or not MOTS.search(p):
            continue
        if mots and not any(m.lower() in p.lower() for m in mots):
            continue
        if DOSE.search(p) or "IDSA" in p or "h-index" in p or p.count(",") > 7:
            continue
        deja.add(p)
        pris.append(p)
        if len(pris) >= n:
            break
    return pris


def paquet(c, xs, prefix, theme):
    preuves = L.preuves(c, "WSES", prefix, theme, "le consensus de 2018", xs)
    lignes = [f"Les boutons ouvrent des phrases de 2018 sur {theme}."]
    for i in range(1, len(xs) + 1):
        lignes.append(f"Phrase citée numéro {i} sur {theme}. " + L.B(f"{prefix}-q{i}", f"citation {i}"))
    return L.W(f"{prefix}-index", f"Citations : {theme}", lignes) + "\n" + preuves


def construire():
    brut = " ".join(SRC.read_text(encoding="utf-8", errors="replace").split())
    c = L.Corpus()
    c.texts["WSES"] = brut
    deja = set()
    themes = [
        ("w-dx10d", "la définition", ["necrotizing fasciitis", "fascia", "soft tissue"], 8),
        ("w-dx10s", "le score", ["LRINEC", "sensitivity", "rule-out"], 6),
        ("w-dx10c", "la chirurgie", ["surgical", "debridement", "exploration"], 10),
        ("w-dx10z", "le consensus", ["surgical", "soft tissue", "debridement", "necrot"], 70),
    ]
    blocs = {}
    for prefix, theme, mots, n in themes:
        xs = cliniques(brut, mots, n, deja)
        print(theme, len(xs))
        if len(xs) < 2:
            raise SystemExit("peu " + theme)
        blocs[prefix] = paquet(c, xs, prefix, theme)
    score = (
        "<p>«LRINEC ≥ 6 had sensitivity of 68.2% and specificity of 84.8%, while LRINEC ≥ 8 had sensitivity of 40.8% and specificity of 94.9%.</p>"
        "<p>The authors concluded that due to poor sensitivity, LRINEC should not be used to rule-out NSTIs.»</p>"
    )
    # La citation doit rester dans des guillemets fermés, phrase par phrase.
    score = (
        "<p>«LRINEC ≥ 6 had sensitivity of 68.2% and specificity of 84.8%, while LRINEC ≥ 8 had sensitivity of 40.8% and specificity of 94.9%.»</p>"
        "<p>«The authors concluded that due to poor sensitivity, LRINEC should not be used to rule-out NSTIs.»</p>"
    )
    wins = [""] * 14
    wins[0] = L.W("w-dx10-def", "Fascia, pas un érysipèle", [
        "L'infection nécrose la peau et les tissus mous, et elle progresse le long des fascias.",
        "Le consensus mondial de 2018 la traite comme une urgence chirurgicale.",
        "Une définition histologique séparée n'est pas recopiée : À vérifier.",
        "L'érysipèle et la cellulite restent dans la peau. Ici, le plan du fascia est atteint.",
    ]) + "\n" + blocs["w-dx10d"]
    wins[1] = L.W("w-dx10-epi", "Rang et taux", [
        "L'incidence pour 100 000 n'est pas dans les extraits lus : À vérifier.",
        "Ce diagnostic est DX.10, le dernier de la liste de fréquence, et ce rang de fréquence reste À vérifier.",
        "Son rang d'exclusion est E1 : c'est celui qu'on écarte en premier.",
        "La rareté possible ne ralentit pas le geste.",
    ])
    wins[2] = L.W("w-dx10-phys", "Le long du fascia", [
        "Les germes nécrosent le fascia et avancent plus loin que la rougeur.",
        "La crépitation, quand elle est là, vient de gaz dans les tissus.",
        "Son absence n'exclut pas.",
        "La chirurgie enlève le tissu mort. L'antibiotique couvre le reste, sans dose écrite ici.",
    ])
    wins[3] = L.W("w-dx10-dem", "E1", [
        "E1 se cherche avant la péritonite, l'ischémie et l'anévrisme.",
        "Une peau tendue, douloureuse au-delà de la rougeur, fait passer ce diagnostic en tête.",
        "On ne finit pas l'examen de l'abdomen pendant que le fascia avance.",
    ])
    wins[4] = L.W("w-dx10-ana", "Douleur disproportionnée à la peau", [
        "Douleur très forte pour une rougeur modeste, progression en heures, porte d'entrée, immunodépression.",
        "La fièvre peut manquer au début.",
        "Un antibiotique oral déjà pris ne rassure pas.",
    ])
    wins[5] = L.W("w-dx10-exam", "Au-delà de la rougeur", [
        "On palpe au-delà de la rougeur, on cherche la crépitation et la tension des tissus.",
        "On marque la peau pour voir l'avance.",
        "On ne rassure pas parce que la rougeur paraît limitée.",
        "La douleur à distance de l'érythème est un drapeau.",
    ])
    wins[6] = L.W("w-dx10-synd", "Peau simple ou fascia", [
        "Syndrome de cellulite : rougeur, chaleur, limite assez nette, malade stable.",
        "Syndrome nécrosant : douleur majeure, tension, avance rapide, parfois crépitation, état qui se dégrade.",
        "Le second ne se surveille pas quelques heures pour voir.",
    ])
    wins[7] = L.W("w-dx10-pos", "Le fascia vu, pas le score", [
        "Le diagnostic positif est opératoire : le fascia est nécrotique.",
        "Aucun score n'exclut la maladie.",
        "À 6 ou plus, le score de laboratoire a une sensibilité de 68,2 % et une spécificité de 84,8 %.",
        "À 8 ou plus, la sensibilité tombe à 40,8 % et la spécificité monte à 94,9 %.",
        "Le consensus conclut qu'on ne s'en sert pas pour écarter l'infection nécrosante.",
        "Un score de 8 ou plus était décrit, dans le texte de 2004 cité, avec un risque de 75 % : ce n'est pas une sensibilité.",
    ]) + "\n" + L.fenetre("w-dx10-cit", "Phrases du score", score) + "\n" + blocs["w-dx10s"]
    wins[8] = L.W("w-dx10-ex", "L'image n'exclut pas", [
        "Le scanner peut aider, il ne doit pas retarder le bloc si le tableau est clair.",
        "Une étude citée par le consensus, 58 explorations, trouve une sensibilité du scanner de 100 % dans ce petit groupe : ce n'est pas une règle universelle.",
        "La biologie entre dans le score, elle ne remplace pas l'exploration.",
    ])
    wins[9] = L.W("w-dx10-arbre", "Si, alors", [
        "Si la douleur dépasse la rougeur et les tissus sont tendus, on appelle le chirurgien.",
        "Si le score est bas, on n'écarte pas.",
        "Si l'on explore et que le fascia est nécrotique, on excise.",
        "L'antibiotique part en même temps que la chirurgie, sans milligramme suisse ici.",
        "Si la rougeur est limitée mais la douleur est majeure, on ne rassure pas.",
    ]) + "\n" + blocs["w-dx10c"]
    wins[10] = L.W("w-dx10-pec", "Chirurgie et antibiotique, sans dose", [
        "Pas de milligramme ici.",
        "Le consensus demande un antibiotique en même temps que la chirurgie, sans donner la dose suisse.",
        "Le choix de molécule selon le terrain suisse est À vérifier (AIPS).",
        "Le but immédiat est d'enlever le fascia mort et de soutenir le malade.",
        "On remarque la peau pour voir si la limite avance après le premier geste.",
        "Le pronostic chiffré suisse n'a pas été lu.",
    ]) + "\n" + blocs["w-dx10z"]
    wins[11] = L.W("w-dx10-prev", "Pas de score de tri négatif", [
        "Aucun dépistage de population n'a été lu.",
        "La prévention de l'erreur est de ne pas utiliser le score pour dire non.",
    ])
    wins[13] = L.quiz("w-dx10-pieges", [
        ("E1 veut-il dire le plus fréquent ?",
         "Non. E1 est le premier à écarter. DX.10 est le dernier rang de fréquence, et ce rang de fréquence reste À vérifier."),
        ("Le score à 6 ou plus exclut-il si l'on est en dessous ?",
         "Non. Sensibilité 68,2 % seulement. On ne l'utilise pas pour écarter."),
        ("Que veut 40,8 % ?",
         "La sensibilité du score à 8 ou plus, dans la revue citée. La spécificité est alors 94,9 %."),
        ("75 % est-il une sensibilité ?",
         "Non. C'est le risque décrit pour un score de 8 ou plus dans le texte de 2004 cité par le consensus."),
        ("Qui fait le diagnostic positif ?",
         "Le chirurgien qui voit le fascia nécrotique."),
        ("Une rougeur limitée rassure-t-elle ?",
         "Non. On palpe au-delà et on marque la peau."),
        ("Où est la dose ?",
         "Absente. À vérifier (AIPS)."),
        ("L'antibiotique remplace-t-il l'excision ?",
         "Non. Il part en même temps."),
        ("L'incidence pour 100 000 est-elle écrite ?",
         "Non. À vérifier."),
        ("Une définition histologique séparée est-elle recopiée ?",
         "Non. À vérifier."),
        ("Le scanner de l'étude à 58 patients est-il une loi ?",
         "Non. C'est un groupe cité. Il ne retarde pas le bloc si le tableau est clair."),
        ("La crépitation absente exclut-elle ?",
         "Non."),
        ("Quelle année a le consensus ?",
         "2018, société mondiale de chirurgie d'urgence."),
        ("DX.10 se palpe-t-il après les neuf autres ?",
         "Non. E1 passe devant."),
    ])
    paras = [
        "C'est une infection nécrosante de la peau et des tissus mous, qui avance le long des fascias. Le consensus de 2018 en fait une urgence chirurgicale. "
        + L.B("w-dx10-def", "plan"),
        "L'incidence pour 100 000 n'est pas lue : À vérifier. DX.10 est le dernier rang de fréquence, lui aussi À vérifier. E1 est le premier à écarter. "
        + L.B("w-dx10-epi", "rangs"),
        "La nécrose suit le fascia, au-delà de la rougeur. " + L.B("w-dx10-phys", "avance"),
        "E1 avant le ventre de bois et avant l'ischémie. " + L.B("w-dx10-dem", "urgence"),
        "Douleur majeure, progression en heures, porte d'entrée. " + L.B("w-dx10-ana", "histoire"),
        "On palpe au-delà de la rougeur, on cherche la crépitation et la tension, on marque la peau. " + L.B("w-dx10-exam", "geste"),
        "Cellulite stable n'est pas fascia qui avance. " + L.B("w-dx10-synd", "syndromes"),
        "Le fascia nécrotique fait le diagnostic. Le score à 6 ou plus n'a que 68,2 % de sensibilité. " + L.B("w-dx10-pos", "score"),
        "L'image ne retarde pas le bloc si le tableau est clair. " + L.B("w-dx10-ex", "examens"),
        "Douleur au-delà de la rougeur : chirurgien. Score bas : on n'écarte pas. " + L.B("w-dx10-arbre", "arbre"),
        "Antibiotique en même temps que la chirurgie. Pas de milligramme : À vérifier (AIPS). " + L.B("w-dx10-pec", "moyens"),
        "Pas de dépistage lu. Ne pas utiliser le score pour dire non. " + L.B("w-dx10-prev", "prévention"),
        "E1. Fascia. 68,2 % seulement. Pas de dose. On marque la peau.",
        "Quatorze questions. " + L.B("w-dx10-pieges", "pièges") + " Répondez avant d'ouvrir.",
    ]
    sources = L.sources_section([
        "<sup class=\"s\">6</sup> Sartelli M et al. Consensus du 14 décembre 2018 sur les infections de la peau et des parties molles. PMC6295010. DOI 10.1186/s13017-018-0219-9. Texte intégral lu le 31.10.2026.",
    ], "68,2 %, 84,8 %, 40,8 %, 94,9 % et le risque de 75 % à un score de 8 viennent de ce texte. Aucune dose suisse n'est affirmée.")
    html = L.assembler(
        f"DX.10 — {NOM}", NOM,
        "DX.10 du cours F1.5. Le rang d'exclusion n'est pas le numéro DX. Texte du 31.10.2026.",
        f"<h2>DX.10 — {NOM}</h2>",
        "La fasciite nécrosante avance sous la peau, au-delà de la rougeur. C'est l'urgence E1. Le score de laboratoire ne l'exclut pas : à 6 ou plus, la sensibilité n'est que de 68,2 %. Aucun milligramme n'est écrit.",
        list(zip(paras, wins)),
        sources,
        "FIN_FICHIER LOT_134_Phase_B_DX.10",
        FICHIER,
        25000,
    )
    L.ecrire(FICHIER, html)
    (L.EVID / "wses2018_fasciite.txt").write_text(
        "===== WSES 2018 infections de la peau, PMC6295010, phrases citées, lues le 31.10.2026 =====\n"
        + "\n".join(c.cites) + "\n" + score + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    construire()

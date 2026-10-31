#!/usr/bin/env python3
"""DX.2 approfondi : anévrisme de l'aorte abdominale. Source lue le 31.10.2026.

Texte intégral : ESVS 2024, Eur J Vasc Endovasc Surg, Wanhainen et al.,
https://www.ejves.com/article/S1078-5884(23)00889-4/fulltext
Ne réécrit pas evidence/corpus_v8.txt (preuves de DX.1).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import profond_lib as L

NOM = "Anévrisme de l'aorte abdominale"
FICHIER = "LOT_134_Phase_B_V0_DX.2.html"
SRC = Path("/home/ubuntu/.cursor/projects/workspace/agent-tools/1a593a1a-354f-491c-b307-902beaf1cf50.txt")

L.GLOSS["UK"] = "Royaume-Uni"
L.GLOSS["BP"] = "pression artérielle"
L.GLOSS["US"] = "échographie"
L.GLOSS["OSR"] = "réparation ouverte"
L.GLOSS["RCT"] = "essai contrôlé randomisé"
L.GLOSS["IFU"] = "notice d'utilisation du fabricant"
L.GLOSS["ACS"] = "syndrome du compartiment abdominal"
L.GLOSS["MAP"] = "pression artérielle moyenne"

MOTS_CLIN = re.compile(
    r"\b(aneurysm|aortic|aorta|palpation|ultrasound|rupture|screening|diameter|"
    r"repair|hypotension|endovascular|surveillance|mortality|smoking|iliac|"
    r"retroperitoneal|tomography|duplex|threshold|haemorrhage|unstable|systolic)\b",
    re.I,
)


def cliniques(texte: str, mots: list[str], n: int, deja: set[str]) -> list[str]:
    pris = []
    for p in L.phrases_source(texte):
        if p in deja:
            continue
        if not MOTS_CLIN.search(p):
            continue
        if mots and not any(m.lower() in p.lower() for m in mots):
            continue
        if p.count(",") > 5:
            continue
        if re.search(r"\b[A-Z][a-z]+ [a-z],", p):
            continue
        if "in the US" in p or "the USA" in p:
            continue
        if "http" in p or "doi" in p.lower():
            continue
        deja.add(p)
        pris.append(p)
        if len(pris) >= n:
            break
    return pris


def index_et_preuves(c: L.Corpus, extraits: list[str], prefix: str, theme: str) -> str:
    preuves = L.preuves(c, "ESVS", prefix, theme, "la recommandation européenne de 2024", extraits)
    lignes = [f"Les boutons ouvrent des phrases de la recommandation sur {theme}, sans ajouter un chiffre."]
    for i in range(1, len(extraits) + 1):
        lignes.append(f"Phrase citée numéro {i} sur {theme}. " + L.B(f"{prefix}-q{i}", f"citation {i}"))
    return L.W(f"{prefix}-index", f"Citations : {theme}", lignes) + "\n" + preuves


def construire():
    brut = " ".join(SRC.read_text(encoding="utf-8", errors="replace").split())
    c = L.Corpus()
    c.texts["ESVS"] = brut
    deja: set[str] = set()
    themes = [
        ("w-dx2d", "la définition", ["30 mm", "define an AAA", "dilatation"], 8),
        ("w-dx2p", "la palpation", ["palpation", "pulsatile mass"], 6),
        ("w-dx2e", "la prévalence", ["prevalence", "screening", "65 year"], 12),
        ("w-dx2i", "l'image", ["ultrasound", "duplex", "computed tomography", "retroperitoneal"], 10),
        ("w-dx2r", "la rupture", ["rupture", "unstable", "hypotension", "80 mmHg"], 12),
        ("w-dx2f", "la réparation", ["55 mm", "50 mm", "indication", "endovascular"], 14),
        ("w-dx2s", "la surveillance", ["surveillance", "follow up", "interval"], 10),
        ("w-dx2v", "le risque vasculaire", ["smoking", "statin", "antiplatelet"], 8),
        ("w-dx2u", "le suivi", ["endoleak", "graft", "iliac aneurysm"], 10),
    ]
    blocs = {}
    for prefix, theme, mots, n in themes:
        extraits = cliniques(brut, mots, n, deja)
        if not extraits:
            raise SystemExit(f"aucune phrase pour {theme}")
        blocs[prefix] = index_et_preuves(c, extraits, prefix, theme)
        print(theme, len(extraits))

    wins = [""] * 14
    wins[0] = L.W("w-dx2-def", "Deux seuils, pas un slogan", [
        "La définition générale lue est une dilatation focale et permanente d'au moins la moitié du diamètre attendu.",
        "En pratique, le même chapitre fixe 30 mm ou plus pour nommer l'anévrisme de l'aorte abdominale.",
        "Ce second seuil dépasse en général de plus de deux écarts types le diamètre moyen des hommes, dit le texte.",
        "Un seuil plus bas pourrait mieux convenir aux femmes et à certaines populations d'Asie : le texte le dit au conditionnel.",
        "Une aorte battante chez une personne maigre peut rester normale : la palpation ne tranche pas.",
        "Le détail des phrases est dans les citations de la définition, pas dans une paraphrase plus large.",
    ]) + "\n" + blocs["w-dx2d"]
    wins[1] = L.W("w-dx2-epi", "Ce qui est chiffré, et ce qui ne l'est pas", [
        "La prévalence lue chez les hommes de 65 ans en Suède, de 2006 à 2009, est 1,7 %, plus 0,5 % déjà connus.",
        "Le programme du Royaume-Uni, de 2009 à 2013, rapporte 1,3 % chez les hommes du même âge.",
        "En 2020 et 2021, les deux programmes nationaux lus passent sous 1 %.",
        "Le texte attribue la baisse sur vingt ans au recul du tabac et à la prise en charge du risque cardiovasculaire.",
        "Avant 55 à 60 ans, la prévalence est dite négligeable, puis elle augmente avec l'âge.",
        "Le chiffre suisse de population n'est pas dans cette recommandation : il reste À vérifier.",
        "Un programme limité aux fumeurs, cité pour les États-Unis d'Amérique, dépasse 5 % : ce n'est pas un taux suisse.",
        "On ne convertit pas ces pourcentages en risque de rupture de l'année pour le patient du jour.",
    ]) + "\n" + blocs["w-dx2e"]
    wins[2] = L.W("w-dx2-physio", "De la paroi à la rupture", [
        "La paroi se dilate de façon focale, le plus souvent en fuseau, selon la définition lue.",
        "La rupture se fait vers le rétro-péritoine : l'échographie d'urgence voit mal ce sang.",
        "Le risque de rupture augmente avec le diamètre : le texte maintient 55 mm chez l'homme et 50 mm chez la femme pour envisager la réparation.",
        "Ces deux seuils de réparation ont été abaissés en force de recommandation, faute de preuve de haute qualité.",
        "Le seuil de réparation doit de préférence reposer sur la mesure échographique, dit la mise à jour.",
        "Les pourcentages annuels de rupture par tranche de diamètre ne sont pas recopiés ici : À vérifier dans le tableau source si on doit les citer un par un.",
        "Aucun médicament de cette leçon ne prétend refermer la paroi : la classe lue vise le risque cardiovasculaire, sans milligramme.",
    ]) + "\n" + L.W("w-dx2-corr", "Lésion, examen, geste", [
        "Dilatation focale d'au moins 30 mm : l'échographie la mesure, la surveillance ou la réparation dépend du diamètre.",
        "Rupture suspectée chez un patient instable : l'anévrisme vu à l'échographie est très évocateur, le sang rétropéritonéal l'est mal.",
        "Anatomie de réparation endovasculaire : l'échographie ne la donne pas, l'angioscanner thoraco-abdominal et des axes d'accès la donne si l'état le permet.",
        "Risque cardiovasculaire associé : arrêt du tabac, pression, statine et antiagrégant sont recommandés, sans dose suisse relue.",
    ]) + "\n" + blocs["w-dx2f"]
    wins[3] = L.W("w-dx2-dem", "E4 n'est pas le premier geste", [
        "Le numéro DX.2 ne dit pas l'urgence : le rang d'exclusion lu pour cette lésion est E4.",
        "Une douleur avec une instabilité le fait passer avant les signes fréquents du lot.",
        "Sans douleur, un battement seul ne se nomme pas rupture.",
        "Les urgences du lot qui précèdent E4 restent la fasciite, la péritonite et l'ischémie mésentérique.",
        "On ne rassure pas sur une main seule quand la douleur et la tension changent.",
    ])
    wins[4] = L.W("w-dx2-ana", "Douleur, syncope, tension", [
        "Douleur abdominale ou lombaire, malaise, syncope et chute de tension sont les drapeaux déjà retenus.",
        "L'instabilité hémodynamique lue est une perte ou une baisse de conscience, ou une pression systolique sous 80 mmHg.",
        "Ce seuil est dans le chapitre de la rupture, pas dans la palpation de routine.",
        "Le texte ajoute que l'instabilité est relative et que l'angioscanner reste souvent possible.",
        "Une masse douloureuse sans brèche de la paroi est un anévrisme symptomatique non rompu, définition variable dans le chapitre.",
        "Emboles périphériques sans autre source entrent dans cette définition variable, pas dans la rupture.",
    ]) + "\n" + blocs["w-dx2r"]
    wins[5] = L.W("w-dx2-exam", "Ce que la main peut et ne peut pas", [
        "On cherche une masse pulsatile, en sachant que la sensibilité lue va de 33 à 100 %.",
        "La spécificité lue va de 75 à 100 %, et la valeur prédictive positive de 14 à 100 %.",
        "Le taux de détection dépend du diamètre, de l'expérience et du morphotype.",
        "La même recommandation conclut que la palpation n'est pas fiable pour le diagnostic.",
        "La chaleur, les limites et la mobilité à la respiration restent des caractères de la palpation du cours, sans devenir un diamètre.",
    ]) + "\n" + blocs["w-dx2p"]
    wins[6] = L.W("w-dx2-synd", "Trois tableaux à ne pas mélanger", [
        "Le syndrome de base est une masse battante, pas un godet et pas une défense.",
        "Dès que la douleur s'accompagne d'instabilité, la palpation cesse d'être un geste de réassurance.",
        "On passe à l'image et à l'équipe vasculaire.",
        "Un anévrisme symptomatique non rompu a mal, ou une masse sensible, ou des emboles, sans brèche de paroi.",
        "La rupture ajoute la brèche et le risque de collapsus.",
        "Le godet bilatéral chronique du diagnostic précédent ne se palpe pas comme cette masse.",
    ])
    wins[7] = L.W("w-dx2-pos", "Qui affirme le diagnostic", [
        "On affirme le petit anévrisme par l'image, pas par le seul battement sous les doigts.",
        "Pour le petit anévrisme, la sensibilité et la spécificité lues de l'échographie et du duplex dépassent 97 %.",
        "La mesure se fait dans un plan perpendiculaire à l'axe de l'aorte.",
        "Quand l'état le permet, c'est l'angioscanner qui confirme la brèche.",
        "Sentir l'aorte ne suffit jamais à écrire le diagnostic.",
    ])
    wins[8] = L.W("w-dx2-ex", "Ordre des images", [
        "L'échographie et le duplex sont les outils de première ligne pour le petit anévrisme.",
        "L'échographie d'urgence voit l'anévrisme, pas le saignement rétropéritonéal : sa sensibilité pour cette hémorragie est basse.",
        "Elle ne dit pas si l'anatomie convient à une réparation endovasculaire.",
        "Chez le patient instable, voir l'anévrisme suggère fortement la rupture.",
        "L'angioscanner thoraco-abdominal et des axes iliaques est l'examen clé si le patient peut le passer.",
        "La mesure du diamètre au scanner se fait avec un logiciel dédié, dans un plan orthogonal, recommandation relevée en classe I.",
        "Le texte ne choisit pas un placement de calibre unique pour l'échographie.",
    ]) + "\n" + blocs["w-dx2i"]
    wins[9] = L.W("w-dx2-arbre", "Si, alors", [
        "Si le patient est instable et que l'échographie voit l'anévrisme, la rupture est très probable.",
        "S'il peut passer au scanner, l'angioscanner thoraco-abdominal et des accès est l'examen clé.",
        "S'il ne le peut pas, la voie lue est le bloc, selon l'état et l'équipe.",
        "Si le diamètre est sous le seuil de réparation, on surveille et on traite le risque cardiovasculaire.",
        "Si l'homme atteint 55 mm ou la femme 50 mm à l'échographie, la réparation peut être envisagée, avec une recommandation moins forte qu'avant.",
        "Si la main seule sent un battement sans douleur, on ne conclut pas.",
        "Un battement douloureux et instable ne retourne pas à la fin de la liste des diagnostics fréquents.",
    ])
    wins[10] = L.W("w-dx2-pec", "But, moyens, surveillance, suite", [
        "Le but immédiat d'une rupture est d'arrêter le saignement au bloc, pas de finir la palpation.",
        "Le but d'un petit anévrisme est d'éviter la rupture et l'événement cardiovasculaire.",
        "Les moyens lus pour le risque sont l'arrêt du tabac, le contrôle de la pression, une statine, un antiagrégant et le mode de vie.",
        "Aucune dose en milligrammes n'est écrite ici.",
        "L'anticoagulation peropératoire et l'hypotension permissive ont des recommandations propres : les milligrammes et la cible tensionnelle précise ne sont pas recopiés.",
        "Le produit suisse, s'il est choisi, se lit dans son information professionnelle : À vérifier (AIPS) pour la spécialité retenue.",
        "La surveillance du petit anévrisme repose d'abord sur l'échographie.",
        "Après réparation, le suivi à long terme cherche les fuites, l'infection de prothèse et la rupture secondaire : le calendrier suisse n'a pas été lu.",
        "Le pronostic dépend de la rupture, du terrain et de la voie : on ne donne pas un pourcentage de survie suisse non lu.",
    ]) + "\n" + blocs["w-dx2v"] + "\n" + blocs["w-dx2u"]
    wins[11] = L.W("w-dx2-prev", "Dépister sans la main", [
        "Le dépistage échographique des groupes à haut risque reste de classe I, niveau A, dans la mise à jour de 2024.",
        "La cible n'est plus fixée dans la recommandation : elle dépend de la prévalence locale, de l'espérance de vie et de l'organisation des soins.",
        "La palpation n'est pas l'outil de ce dépistage.",
        "Le programme suisse, son âge et son sexe cibles, sont À vérifier.",
        "Le recul du tabac est le facteur de baisse de prévalence le plus cité, pas un médicament dosé ici.",
    ]) + "\n" + blocs["w-dx2s"]
    wins[12] = (
        "Trente millimètres définissent l'anévrisme en pratique. La main ne suffit pas. "
        "Instabilité plus anévrisme à l'échographie : penser rupture, sans attendre de voir le sang. "
        "Cinquante-cinq millimètres chez l'homme et cinquante chez la femme ouvrent la discussion de réparation, avec une preuve jugée moins forte."
    )
    # Le point 13 est une phrase de fiche, pas une fenêtre : le plan demande des phrases intactes.
    wins[12] = ""
    wins[13] = L.quiz("w-dx2-pieges", [
        ("Sentir l'aorte, est-ce l'anévrisme ?",
         "Pas à soi seul. La sensibilité de la palpation va de 33 à 100 %. L'échographie dépasse 97 % pour le petit anévrisme."),
        ("L'échographie voit-elle le saignement ?",
         "Mal. Sa sensibilité pour l'hémorragie rétropéritonéale est basse. Elle voit l'anévrisme."),
        ("Quel seuil d'instabilité est écrit ?",
         "Perte ou baisse de conscience, ou pression systolique sous 80 mmHg, dans le chapitre de la rupture."),
        ("Le dépistage vise-t-il un âge unique ?",
         "La classe I vise les groupes à haut risque. La cible locale n'est plus fixée dans la recommandation de 2024."),
        ("Quel diamètre nomme l'anévrisme en pratique ?",
         "30 mm ou plus. La définition générale, elle, est une augmentation d'au moins la moitié du diamètre attendu."),
        ("À partir de quand discute-t-on la réparation ?",
         "55 mm chez l'homme et 50 mm chez la femme, de préférence sur la mesure échographique. La force de la recommandation a été abaissée."),
        ("Une aorte battante chez une personne maigre suffit-elle ?",
         "Non. La palpation n'est pas fiable, et le morphotype change le taux de détection."),
        ("Le chiffre suisse de prévalence est-il dans la recommandation ?",
         "Non. Les taux lus sont suédois et britanniques. Le taux suisse reste À vérifier."),
        ("Peut-on écrire une dose de statine ou d'héparine ?",
         "Non. Aucun milligramme n'a été relu dans une information professionnelle suisse pour cette leçon."),
        ("L'anévrisme symptomatique est-il déjà rompu ?",
         "Pas selon la définition lue : douleur, masse sensible ou embole, sans brèche de la paroi."),
        ("E4 veut-il dire qu'on palpe avant la fasciite ?",
         "Non. E4 vient après la fasciite, la péritonite et l'ischémie mésentérique."),
        ("L'angioscanner est-il inutile si l'échographie a vu l'anévrisme ?",
         "Non quand l'état le permet. Il confirme et dit si l'anatomie convient à la voie endovasculaire."),
        ("La baisse de prévalence est-elle une invention ?",
         "Non. Le texte l'attribue au recul du tabac et au contrôle du risque, sur vingt ans."),
        ("Où est la phrase sur les 30 mm ?",
         "Dans le chapitre d'épidémiologie et de diagnostic de la recommandation de 2024, citation à ouvrir."),
    ])

    paras = [
        "En pratique clinique, le seuil lu est un diamètre de 30 mm ou plus. Une aorte battante chez une personne maigre peut être normale. "
        + L.B("w-dx2-def", "seuils") + " La recommandation européenne de 2024 sépare la définition générale et ce seuil fixe.",
        "Chez les hommes de 65 ans, la Suède rapportait 1,7 % entre 2006 et 2009, plus 0,5 % déjà connus. Le Royaume-Uni rapportait 1,3 % entre 2009 et 2013. "
        "Les deux programmes nationaux sont sous 1 % en 2020-2021. Le chiffre suisse est À vérifier. " + L.B("w-dx2-epi", "chiffres"),
        "La paroi se dilate et peut se rompre vers le rétro-péritoine. Le risque augmente avec le diamètre. "
        + L.B("w-dx2-physio", "paroi") + " Les pourcentages annuels par taille ne sont pas recopiés : À vérifier pour un tableau complet.",
        "Ce diagnostic est DX.2, avec le rang d'exclusion E4. Une douleur et une instabilité le font passer avant les signes fréquents. Un battement isolé, sans douleur, n'est pas une rupture. "
        + L.B("w-dx2-dem", "rang"),
        "Douleur abdominale ou lombaire, malaise, syncope et chute de tension sont les drapeaux. "
        + L.B("w-dx2-ana", "instabilité") + " Le seuil de 80 mmHg se lit dans le chapitre de la rupture.",
        "On cherche une masse pulsatile, en sachant que la sensibilité va de 33 à 100 %. La spécificité va de 75 à 100 %, et la valeur prédictive positive de 14 à 100 %. "
        "La même recommandation conclut que la palpation n'est pas fiable. " + L.B("w-dx2-exam", "main"),
        "Le syndrome est celui d'une masse battante, pas d'un godet ni d'une défense. La douleur avec instabilité change le syndrome : on ne palpe plus pour rassurer. "
        + L.B("w-dx2-synd", "tableaux"),
        "Le diagnostic positif du petit anévrisme est l'échographie, pas la main. La sensibilité et la spécificité dépassent 97 % pour le petit anévrisme. "
        "La rupture se confirme par l'angioscanner dès que l'état le permet. " + L.B("w-dx2-pos", "preuve"),
        "L'échographie d'urgence voit l'anévrisme, pas le saignement rétropéritonéal. Sa sensibilité pour cette hémorragie est basse. Elle ne dit pas si l'anatomie convient à un traitement endovasculaire. "
        + L.B("w-dx2-ex", "examens"),
        "Patient instable et anévrisme vu : la rupture est très probable. S'il peut passer au scanner, l'angioscanner thoraco-abdominal et des axes d'accès est l'examen clé. "
        "S'il ne le peut pas, la voie est le bloc. " + L.B("w-dx2-arbre", "arbre"),
        "Aucune dose médicamenteuse n'est écrite. L'hypotension permissive et l'héparine peropératoire ont des chapitres propres, sans milligramme recopié. "
        "Le produit suisse se lit dans son information professionnelle : À vérifier (AIPS). " + L.B("w-dx2-pec", "conduite"),
        "Le dépistage échographique des populations à haut risque est de classe I. La cible dépend des conditions locales. La palpation n'est pas l'outil. Le programme suisse est À vérifier. "
        + L.B("w-dx2-prev", "dépistage"),
        "Trente millimètres définissent l'anévrisme en pratique. La main ne suffit pas. Instabilité plus anévrisme à l'échographie : penser rupture, sans attendre de voir le sang.",
        "Quatorze questions ferment la leçon. " + L.B("w-dx2-pieges", "pièges") + " Répondez avant d'ouvrir.",
    ]
    sources = L.sources_section([
        "<sup class=\"s\">2</sup> Piqueres S, Staeger P, Pasche O. Revue Médicale Suisse 2016;537, 2 novembre 2016.",
        "<sup class=\"s\">4</sup> Wanhainen A et al. Société européenne de chirurgie vasculaire, anévrismes aorto-iliaques, 2024. Texte intégral lu le 31.10.2026. Eur J Vasc Endovasc Surg.",
        "<sup class=\"s\">5</sup> Björck M et al. Maladies des artères et veines mésentériques. Publié le 29.3.2017.",
        "<sup class=\"s\">6</sup> Sartelli M et al. Consensus du 14 décembre 2018 sur les infections de la peau et des parties molles.",
        "<sup class=\"s\">7</sup> Couderc M, Bart G, Coiffier G et al. Recommandations françaises, arthrite septique native de l'adulte, 3 août 2020.",
        "<sup class=\"s\">8</sup> Swissmedic, Dafalgan comprimés, numéro 69266. Texte hors ligne lu le 31.10.2026.",
    ], "La Phase A porte la ligne du catalogue et les adresses complètes. Ce diagnostic ne les recopie pas. Aucune dose n'est affirmée.")
    html = L.assembler(
        f"DX.2 — {NOM}", NOM,
        "DX.2 du cours F1.5. Le rang d'exclusion n'est pas le numéro DX. Texte du 31.10.2026.",
        f"<h2>DX.2 — {NOM}</h2>",
        "L'anévrisme de l'aorte abdominale est une dilatation focale, fixée en pratique à 30 mm ou plus. La main peut sentir un battement, mais elle ne fait pas le diagnostic. Chez un patient instable, voir l'anévrisme à l'échographie suggère fortement la rupture.",
        list(zip(paras, wins)),
        sources,
        "FIN_FICHIER LOT_134_Phase_B_DX.2",
        FICHIER,
        40000,
    )
    L.ecrire(FICHIER, html)
    # Extraits cités seulement : ne pas verser le texte intégral dans le dépôt, ne pas écraser DX.1.
    entete = "===== ESVS 2024, anévrismes aorto-iliaques, phrases citées, lues le 31.10.2026 =====\n"
    (L.EVID / "esvs2024_aaa.txt").write_text(entete + "\n".join(c.cites) + "\n", encoding="utf-8")


if __name__ == "__main__":
    construire()

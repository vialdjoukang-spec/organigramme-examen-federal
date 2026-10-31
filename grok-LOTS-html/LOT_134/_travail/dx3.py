#!/usr/bin/env python3
"""DX.3 approfondi : cholécystite aiguë. Sources lues le 31.10.2026.

Revue Médicale Suisse 2016 (déjà en preuves) et WSES 2020, PMC7643471,
texte intégral Europe PMC. Pas une société suisse : le calendrier suisse
et les milligrammes restent À vérifier (AIPS).
"""
from __future__ import annotations

import html as htmlmod
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import profond_lib as L

NOM = "Cholécystite aiguë"
FICHIER = "LOT_134_Phase_B_V0_DX.3.html"
SRC = Path("/tmp/wses_chol.txt")

L.GLOSS.update({
    "DLC": "cholécystectomie laparoscopique différée",
    "ILC": "cholécystectomie laparoscopique intermédiaire",
    "RCT": "essai contrôlé randomisé",
    "QoE": "qualité de la preuve",
    "SoR": "force de la recommandation",
    "TG13": "recommandations de Tokyo 2013",
    "TG18": "recommandations de Tokyo 2018",
})
DOSE = re.compile(r"\b\d+(?:[.,]\d+)?\s?(?:mg|µg|mcg|g|UI|IU|ml|mL)\b")
MOTS = re.compile(
    r"\b(cholecyst|gallbladder|Murphy|ultrasound|antibiotic|laparoscopic|severity|"
    r"percutaneous|diagnosis|fever|symptom|admission|bile)\b",
    re.I,
)


def cliniques(texte, mots, n, deja):
    pris = []
    for p in L.phrases_source(texte):
        if p in deja or not MOTS.search(p):
            continue
        if mots and not any(m.lower() in p.lower() for m in mots):
            continue
        if p.count(",") > 6 or DOSE.search(p):
            continue
        if re.search(r"\b[A-Z][a-z]+ [a-z],", p):
            continue
        if "http" in p or "doi" in p.lower():
            continue
        deja.add(p)
        pris.append(p)
        if len(pris) >= n:
            break
    return pris


def paquet(c, extraits, prefix, theme):
    preuves = L.preuves(c, "WSES", prefix, theme, "le consensus mondial de 2020", extraits)
    lignes = [f"Les boutons ouvrent des phrases du consensus de 2020 sur {theme}."]
    for i in range(1, len(extraits) + 1):
        lignes.append(f"Phrase citée numéro {i} sur {theme}. " + L.B(f"{prefix}-q{i}", f"citation {i}"))
    return L.W(f"{prefix}-index", f"Citations : {theme}", lignes) + "\n" + preuves


def construire():
    brut = htmlmod.unescape(SRC.read_text(encoding="utf-8", errors="replace"))
    brut = " ".join(brut.split())
    c = L.Corpus()
    c.texts["WSES"] = brut
    deja = set()
    themes = [
        ("w-dx3d", "le diagnostic", ["diagnosis", "Murphy", "fever", "criteria"], 10),
        ("w-dx3i", "l'image", ["ultrasound", "imaging", "computed"], 8),
        ("w-dx3c", "la chirurgie", ["laparoscopic", "7 days", "early", "admission"], 12),
        ("w-dx3g", "la gravité", ["severity", "grade", "percutaneous", "high-risk"], 10),
        ("w-dx3a", "l'antibiotique sans dose", ["antibiotic", "source control"], 8),
        ("w-dx3z", "le consensus", ["cholecyst", "gallbladder", "bile", "laparoscopic"], 50),
    ]
    blocs = {}
    for prefix, theme, mots, n in themes:
        xs = cliniques(brut, mots, n, deja)
        print(theme, len(xs))
        if not xs:
            raise SystemExit("vide " + theme)
        blocs[prefix] = paquet(c, xs, prefix, theme)
    wins = [""] * 14
    wins[0] = L.W("w-dx3-def", "Ce que le consensus retient", [
        "Le consensus mondial de 2020 n'est pas une société suisse.",
        "Il retient la fièvre, la douleur ou la sensibilité de l'hypocondre droit, le vomissement ou l'intolérance alimentaire.",
        "Il retient aussi le signe de Murphy, la protéine C réactive, les leucocytes et des signes d'inflammation à l'image.",
        "La revue suisse de 2016 dit qu'aucune combinaison de symptômes et de signes ne permet le diagnostic avec certitude.",
        "Les deux phrases ne se contredisent pas : une liste n'est pas une certitude clinique.",
        "Le terme à éviter est de conclure sur le seul Murphy.",
    ]) + "\n" + blocs["w-dx3d"]
    wins[1] = L.W("w-dx3-epi", "Le seul pourcentage lu", [
        "Environ 5 % des patients vus aux urgences pour une douleur abdominale aiguë ont une cholécystite, selon la revue suisse de 2016.",
        "Le taux dans la population générale, hors urgences, n'a pas été lu dans la revue : À vérifier.",
        "Ce n'est pas le motif le plus rare, ni le plus fréquent, des dix diagnostics du lot.",
        "On ne transforme pas ces 5 % en risque individuel de complication.",
    ])
    wins[2] = L.W("w-dx3-phys", "Calcul, paroi, douleur", [
        "Le calcul obstrue le canal cystique, la paroi s'inflamme, la douleur siège sous les côtes droites.",
        "Le Murphy est la douleur qui bloque l'inspiration quand la main est sur l'hypocondre droit.",
        "La revue suisse le juge peu discriminatif : il ne prouve pas la vésicule à lui seul.",
        "Un ictère ou une chute de tension élargit vers une complication biliaire, pas vers le diagnostic simple.",
        "Le lien avec l'antibiotique est le contrôle de l'infection, sans milligramme écrit ici.",
        "Le lien avec la chirurgie est d'enlever la vésicule malade quand l'expertise est là.",
    ])
    wins[3] = L.W("w-dx3-dem", "Place dans le lot", [
        "Ce diagnostic est DX.3. Son rang d'exclusion est E7.",
        "Une défense de tout l'abdomen fait passer la péritonite avant cette vésicule.",
        "Une instabilité avec masse battante fait passer l'anévrisme avant.",
        "On ne range pas une douleur de l'hypocondre droit derrière les diagnostics bénins si la tension tombe.",
    ])
    wins[4] = L.W("w-dx3-ana", "Questions qui changent la conduite", [
        "Où est la douleur, depuis quand, avec fièvre, vomissement ou refus alimentaire.",
        "Un ictère oriente vers la voie biliaire, pas vers une vésicule simple.",
        "Une chute de tension élargit vers la complication.",
        "La femme en âge de procréer : le dosage de grossesse reste À vérifier dans une règle suisse non lue.",
        "La durée des symptômes sert au délai opératoire du consensus, pas à rassurer.",
    ])
    wins[5] = L.W("w-dx3-exam", "Main et inspiration", [
        "On palpe l'hypocondre droit en inspiration.",
        "Le signe de Murphy est peu discriminatif, dit la revue suisse.",
        "On cherche une défense locale, sans la confondre avec une contracture de tout l'abdomen.",
        "La chaleur et les limites de la zone douloureuse se décrivent, sans devenir un score.",
    ])
    wins[6] = L.W("w-dx3-synd", "Syndromes à séparer", [
        "Syndrome vésiculaire : douleur de l'hypocondre droit, fièvre possible, Murphy inconstant.",
        "Syndrome de complication : ictère ou tension qui tombe.",
        "Syndrome péritonéal : défense ou contracture qui dépasse l'hypocondre.",
        "On ne nomme pas le troisième avec les mots du premier.",
    ]) + "\n" + blocs["w-dx3g"]
    wins[7] = L.W("w-dx3-pos", "Ce qui suffit, ce qui ne suffit pas", [
        "Le Murphy seul ne suffit pas.",
        "Un chiffre de laboratoire, seul, ne désigne pas la vésicule.",
        "L'image doit montrer des signes d'inflammation de la vésicule, selon le consensus.",
        "Les critères échographiques exacts d'une recommandation suisse restent À vérifier.",
        "La revue suisse refuse la certitude clinique sans l'image et l'ensemble.",
    ]) + "\n" + blocs["w-dx3i"]
    wins[8] = L.W("w-dx3-ex", "Ordre des examens", [
        "L'échographie est l'examen de première ligne dans l'enseignement suisse de la revue de 2016.",
        "Le consensus mondial demande des signes d'inflammation à l'image, sans fixer ici le protocole suisse.",
        "Si l'échographie ne répond pas, le passage au scanner n'a pas de seuil suisse lu : À vérifier.",
        "La protéine C réactive et les leucocytes font partie des éléments du consensus, pas d'un diagnostic isolé.",
    ])
    wins[9] = L.W("w-dx3-arbre", "Si, alors", [
        "Si la douleur est de l'hypocondre droit avec fièvre ou vomissement, on cherche la vésicule à l'échographie.",
        "Si le Murphy est seul et l'image est normale, on ne ferme pas le diagnostic.",
        "Si l'abdomen est contracté partout, on traite d'abord comme une péritonite.",
        "Si l'expertise chirurgicale est là, le consensus recommande la cholécystectomie laparoscopique précoce.",
        "Ce délai lu est dès que possible, dans les 7 jours de l'admission et dans les 10 jours du début des symptômes.",
        "Ce délai est celui du consensus mondial de 2020, pas une règle suisse relue à part.",
        "Si le patient est à très haut risque opératoire, le drainage percutané est discuté dans le même texte, sans consigne suisse recopiée.",
    ]) + "\n" + blocs["w-dx3c"]
    wins[10] = L.W("w-dx3-pec", "But et moyens, sans milligramme", [
        "Le but est de calmer la douleur, traiter l'infection et enlever la cause quand c'est possible.",
        "L'antalgie, si le paracétamol est choisi, suit l'information professionnelle suisse déjà citée en Phase A.",
        "Elle n'est pas répétée ici.",
        "L'antibiotique du consensus n'est pas recopié en milligrammes : À vérifier (AIPS) pour la spécialité suisse.",
        "L'heure de la cholécystectomie dans un hôpital suisse n'est pas dans la revue de 2016.",
        "Le consensus de 2020, lui, place la voie laparoscopique précoce dans les bornes déjà dites, si l'expertise est présente.",
        "La surveillance cherche l'ictère, la chute de tension et l'extension de la défense.",
        "Le pronostic suisse chiffré n'a pas été lu.",
    ]) + "\n" + blocs["w-dx3a"] + "\n" + blocs["w-dx3z"]
    wins[11] = L.W("w-dx3-prev", "Prévention non lue", [
        "La prévention des calculs n'est pas un programme lu ici : À vérifier.",
        "Reconnaître tôt la douleur de l'hypocondre droit évite de rassurer sur un Murphy isolé.",
        "Aucun chiffre de prévention suisse n'est écrit.",
    ])
    wins[13] = L.quiz("w-dx3-pieges", [
        ("Quelle part aux urgences ?",
         "Environ 5 % des douleurs abdominales aiguës, revue suisse de 2016. L'incidence en population est À vérifier."),
        ("Le Murphy suffit-il ?",
         "Non. La même revue le dit peu discriminatif, et aucune combinaison clinique n'est certaine."),
        ("Que liste le consensus de 2020 ?",
         "Fièvre, hypocondre droit, vomissement ou intolérance, Murphy, protéine C réactive, leucocytes, image."),
        ("Quel délai opératoire est écrit ?",
         "Dès que possible, dans les 7 jours de l'admission et les 10 jours des symptômes, si l'expertise est là. C'est le consensus mondial, pas une règle suisse séparée."),
        ("Où est la dose d'antibiotique ?",
         "Nulle part dans cette leçon. À vérifier (AIPS) pour le produit suisse."),
        ("L'ictère est-il une cholécystite simple ?",
         "Non. Il élargit vers une complication biliaire."),
        ("La biologie seule nomme-t-elle la vésicule ?",
         "Non."),
        ("Que fait-on si tout l'abdomen se défend ?",
         "On ne reste pas sur la vésicule. La péritonite passe avant, rang d'exclusion plus haut."),
        ("Le paracétamol est-il redosé ici ?",
         "Non. L'information professionnelle est citée en Phase A et n'est pas répétée."),
        ("Le scanner est-il obligatoire d'emblée ?",
         "Non d'après la revue, qui place l'échographie en premier. Le passage au scanner n'a pas de borne suisse lue."),
        ("E7 veut-il dire urgence maximale ?",
         "Non. Plusieurs urgences du lot se excluent avant."),
        ("Peut-on promettre une certitude clinique ?",
         "Non. La revue de 2016 l'écrit."),
        ("Le drainage percutané remplace-t-il toujours la chirurgie ?",
         "Non. Le consensus le discute chez le patient à haut risque, sans en faire la voie de tous."),
        ("La grossesse est-elle tranchée ?",
         "Non. La démarche du dosage est À vérifier dans une règle suisse non lue."),
    ])
    paras = [
        "La cholécystite aiguë est une inflammation de la vésicule, en pratique presque toujours lithiasique dans ce cours. "
        + L.B("w-dx3-def", "critères") + " Aucune combinaison clinique ne la certifie, dit la revue suisse de 2016.",
        "Environ 5 % des patients vus aux urgences pour une douleur abdominale aiguë ont une cholécystite. L'incidence en population générale n'est pas dans cet article : À vérifier. "
        + L.B("w-dx3-epi", "part"),
        "Le calcul bloque le cystique, la paroi gonfle, la douleur est sous les côtes droites. " + L.B("w-dx3-phys", "mécanisme")
        + " Le Murphy ne prouve pas cette cascade à lui seul.",
        "Ce diagnostic est DX.3, avec le rang d'exclusion E7. Une péritonite généralisée ou une instabilité vasculaire passe avant. "
        + L.B("w-dx3-dem", "rang"),
        "Douleur de l'hypocondre droit, fièvre, vomissement et intolérance alimentaire ouvrent l'histoire. Un ictère ou une chute de tension élargit vers une complication. "
        + L.B("w-dx3-ana", "questions") + " La grossesse : À vérifier.",
        "On palpe l'hypocondre droit en inspiration. Le signe de Murphy est peu discriminatif. On cherche aussi une défense locale. "
        + L.B("w-dx3-exam", "geste"),
        "Le syndrome est celui de l'hypocondre droit, pas du godet ni de la masse battante. " + L.B("w-dx3-synd", "syndromes"),
        "Le diagnostic positif n'est pas le Murphy. L'image cherche l'inflammation de la vésicule. Les critères suisses exacts sont À vérifier. "
        + L.B("w-dx3-pos", "certitude"),
        "L'échographie est la première ligne de la revue suisse. La biologie seule ne nomme pas la vésicule. Le seuil suisse du scanner est À vérifier. "
        + L.B("w-dx3-ex", "examens"),
        "Si l'expertise est là, le consensus de 2020 place la cholécystectomie laparoscopique tôt : dans les 7 jours de l'admission et les 10 jours des symptômes. "
        + L.B("w-dx3-arbre", "délai") + " Ce n'est pas une règle suisse séparée.",
        "Aucune dose n'est affirmée. Le paracétamol, s'il est choisi, reste celui de la Phase A. L'antibiotique suisse est À vérifier (AIPS). "
        + L.B("w-dx3-pec", "moyens"),
        "Aucun programme de prévention des calculs n'a été lu : À vérifier. " + L.B("w-dx3-prev", "prévention"),
        "Cinq pour cent aux urgences, pas une certitude clinique. Le Murphy ne suffit pas. Le délai lu est mondial, pas suisse, et sans milligramme.",
        "Quatorze questions. " + L.B("w-dx3-pieges", "pièges") + " Répondez avant d'ouvrir.",
    ]
    sources = L.sources_section([
        "<sup class=\"s\">2</sup> Piqueres S, Staeger P, Pasche O. Revue Médicale Suisse 2016;537, 2 novembre 2016.",
        "<sup class=\"s\">6</sup> Sartelli M et al. Consensus mondial mis à jour en 2020 sur la cholécystite aiguë lithiasique. Texte intégral lu le 31.10.2026, PMC7643471.",
        "<sup class=\"s\">4</sup> Wanhainen A et al. Société européenne de chirurgie vasculaire, 2024.",
        "<sup class=\"s\">5</sup> Björck M et al. Maladies des artères et veines mésentériques. Publié le 29.3.2017.",
        "<sup class=\"s\">7</sup> Couderc M, Bart G, Coiffier G et al. Recommandations françaises, 3 août 2020.",
        "<sup class=\"s\">8</sup> Swissmedic, Dafalgan comprimés, numéro 69266. Texte hors ligne lu le 31.10.2026.",
    ], "Les milligrammes et le calendrier opératoire suisse ne sont pas affirmés. À vérifier (AIPS) pour toute spécialité.")
    html = L.assembler(
        f"DX.3 — {NOM}", NOM,
        "DX.3 du cours F1.5. Le rang d'exclusion n'est pas le numéro DX. Texte du 31.10.2026.",
        f"<h2>DX.3 — {NOM}</h2>",
        "La cholécystite aiguë se palpe sous les côtes droites, mais le signe de Murphy ne la certifie pas. Environ 5 % des douleurs abdominales aiguës aux urgences, dans la revue suisse lue. Ni la dose d'antibiotique ni le calendrier suisse ne sont affirmés.",
        list(zip(paras, wins)),
        sources,
        "FIN_FICHIER LOT_134_Phase_B_DX.3",
        FICHIER,
        40000,
    )
    L.ecrire(FICHIER, html)
    entete = "===== WSES 2020 cholécystite aiguë lithiasique, PMC7643471, phrases citées, lues le 31.10.2026 =====\n"
    (L.EVID / "wses2020_cholecystite.txt").write_text(entete + "\n".join(c.cites) + "\n", encoding="utf-8")


if __name__ == "__main__":
    construire()

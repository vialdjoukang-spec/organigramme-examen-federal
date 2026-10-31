#!/usr/bin/env python3
"""DX.6 approfondi : adénopathie périphérique maligne.

Source lue le 31.10.2026 : Richli et al. n'est pas le titre exact du fichier.
Swiss Medical Weekly, DOI 10.57187/s.3549, « Peripheral lymphadenopathy of unknown origin
in adults », texte ouvert. Revue Médicale Suisse 2016 pour les caractères de la masse.
Pas de recommandation américaine comme référence. Pas de milligramme.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import profond_lib as L

NOM = "Adénopathie périphérique maligne"
FICHIER = "LOT_134_Phase_B_V0_DX.6.html"
SRC = Path("/home/ubuntu/.cursor/projects/workspace/agent-tools/bc12bf3f-f899-4705-927c-74bd19278607.txt")
L.GLOSS.update({
    "CT": "tomodensitométrie",
    "MRI": "imagerie par résonance magnétique",
    "PET": "tomographie par émission de positons",
    "FDG": "fluorodésoxyglucose",
    "ESMO": "société européenne d'oncologie médicale",
    "NGS": "séquençage de nouvelle génération",
    "HIV": "virus de l'immunodéficience humaine",
    "FNAC": "cytologie à l'aiguille fine",
    "CNB": "biopsie au trocart",
    "US": "échographie",
    "LDH": "lactate déshydrogénase",
})
DOSE = re.compile(r"\b\d+(?:[.,]\d+)?\s?(?:mg|µg|mcg|g|UI|IU|ml|mL)\b")
MOTS = re.compile(r"\b(lymph|biopsy|malign|ultrasound|node|Hodgkin|cervical|supraclavicular)\b", re.I)
CASSURE = re.compile(r"[a-zàâé]{3,}-[a-z]")


def cliniques(texte, mots, n, deja):
    pris = []
    for p in L.phrases_source(texte):
        if p in deja or not MOTS.search(p):
            continue
        if mots and not any(m.lower() in p.lower() for m in mots):
            continue
        if CASSURE.search(p) or DOSE.search(p) or "American College" in p or "http" in p:
            continue
        if p.count(",") > 7:
            continue
        deja.add(p)
        pris.append(p)
        if len(pris) >= n:
            break
    return pris


def paquet(c, xs, prefix, theme):
    preuves = L.preuves(c, "SMW", prefix, theme, "la revue médicale suisse hebdomadaire", xs)
    lignes = [f"Les boutons ouvrent des phrases de la revue suisse sur {theme}."]
    for i in range(1, len(xs) + 1):
        lignes.append(f"Phrase citée numéro {i} sur {theme}. " + L.B(f"{prefix}-q{i}", f"citation {i}"))
    return L.W(f"{prefix}-index", f"Citations : {theme}", lignes) + "\n" + preuves


def construire():
    brut = " ".join(SRC.read_text(encoding="utf-8", errors="replace").split())
    c = L.Corpus()
    c.texts["SMW"] = brut
    deja = set()
    themes = [
        ("w-dx6d", "la définition", ["lymphadenopathy", "size", "consistency"], 8),
        ("w-dx6e", "les chiffres cités", ["malignancy", "incidence", "Hodgkin"], 10),
        ("w-dx6b", "la biopsie", ["biopsy", "needle", "histolog"], 10),
        ("w-dx6z", "la revue", ["lymph", "node", "biopsy"], 55),
    ]
    blocs = {}
    for prefix, theme, mots, n in themes:
        xs = cliniques(brut, mots, n, deja)
        print(theme, len(xs))
        if len(xs) < 3:
            raise SystemExit("peu " + theme)
        blocs[prefix] = paquet(c, xs, prefix, theme)
    wins = [""] * 14
    wins[0] = L.W("w-dx6-def", "Ganglion et malignité", [
        "La revue suisse hebdomadaire définit l'adénopathie comme une anomalie de taille, de consistance ou d'aspect d'un ou de plusieurs ganglions.",
        "Le diagnostic de cette leçon ajoute l'origine maligne, locale ou métastatique.",
        "Cette origine se prouve par l'histologie, pas par la main.",
        "Le signe palpé reste une masse : localisation, dimension, forme, consistance, sensibilité et mobilité.",
    ]) + "\n" + blocs["w-dx6d"]
    wins[1] = L.W("w-dx6-epi", "Ce que la revue rapporte, et ce qu'elle ne dit pas", [
        "La proportion suisse de cancers parmi les ganglions palpés en premier recours n'est pas un registre national : À vérifier.",
        "La revue cite, dans les études qu'elle rassemble, 1,1 à 8,1 % de malignité parmi les patients avec adénopathie.",
        "Elle cite aussi 0,5 à 0,6 % par an dans des cabinets de médecine de famille, en 1981 et 1984, pas en Suisse d'aujourd'hui.",
        "Ce diagnostic est DX.6 faute d'un dénominateur commun avec les autres du lot.",
        "Ce rang n'est pas une méta-analyse.",
        "Parmi les maladies lymphoprolifératives confirmées de l'adulte, la revue rapporte le lymphome de Hodgkin à 31 %, le lymphome B diffus à grandes cellules à 29 % et le folliculaire à 16 %.",
        "Ces trois parts ne sont pas des incidences suisses.",
    ]) + "\n" + blocs["w-dx6e"]
    wins[2] = L.W("w-dx6-phys", "Pourquoi le ganglion grossit", [
        "Un ganglion réactif est souvent mou, mobile et bien limité, dit la revue.",
        "Un ganglion ferme, fixé, ou sus-claviculaire fait chercher une malignité.",
        "La persistance au-delà de deux semaines est un motif d'enquête, pas une preuve de cancer.",
        "La main décrit. L'histologie nomme.",
    ])
    wins[3] = L.W("w-dx6-dem", "E8", [
        "Ce diagnostic est DX.6. Son rang d'exclusion est E8.",
        "Une infection nécrosante, une péritonite ou une ischémie passent avant un ganglion isolé stable.",
        "Un ganglion sus-claviculaire ne se range pas parmi les signes banals.",
    ])
    wins[4] = L.W("w-dx6-ana", "Histoire qui oriente", [
        "On cherche une infection récente, un voyage, un animal, un médicament et un cancer déjà connu.",
        "La fièvre, l'amaigrissement et la sueur ouvrent vers une maladie générale.",
        "Deux semaines ou plus : la revue demande d'investiguer.",
        "Un essai d'antibiotique répété sans diagnostic n'est pas une conduite lue comme règle suisse écrite : À vérifier.",
    ])
    wins[5] = L.W("w-dx6-exam", "Caractères de la masse", [
        "On note la localisation, la dimension, la forme, la consistance, la sensibilité et la mobilité.",
        "Mou, mobile et bien limité oriente plutôt vers une réaction, sans l'exclure du lymphome.",
        "Ferme, peu mobile, ulcéré ou sus-claviculaire oriente vers la malignité.",
        "On palpe les autres aires et la rate, pas seulement le ganglion montré.",
    ])
    wins[6] = L.W("w-dx6-synd", "Local ou diffus", [
        "Syndrome local : un territoire, souvent le cou.",
        "La revue situe la répartition des formes localisées surtout au cou, puis à l'aine, puis au creux sus-claviculaire et axillaire, dans les séries citées.",
        "Syndrome diffus : plusieurs territoires, maladie générale à ne pas manquer.",
        "Syndrome de malignité : persistance, consistance ferme, âge plus élevé, histologie.",
    ])
    wins[7] = L.W("w-dx6-pos", "L'histologie, pas l'essai médicamenteux", [
        "Le diagnostic positif n'est pas l'antibiotique d'épreuve.",
        "Il vient de l'histologie, décidée avec le spécialiste.",
        "La revue dit qu'en dehors de la tête et du cou, la biopsie ouverte reste le meilleur choix si l'on suspecte un lymphome.",
        "Au cou, la cytologie ou le trocart précèdent souvent l'imagerie, selon le même texte.",
        "Répéter une antibiothérapie sans diagnostic n'est pas une conduite écrite ici.",
    ]) + "\n" + blocs["w-dx6b"]
    wins[8] = L.W("w-dx6-ex", "Image puis tissu", [
        "L'échographie est la première image dans la revue.",
        "Le scanner ou la résonance viennent ensuite pour l'extension, surtout au cou.",
        "La numération et le lactate déshydrogénase ne prouvent pas la malignité : la revue dit la preuve faible.",
        "Le tissu tranche.",
    ])
    wins[9] = L.W("w-dx6-arbre", "Si, alors", [
        "Si le ganglion a moins de deux semaines et un contexte infectieux clair, on surveille de près.",
        "Si cela dure plus de deux semaines, on examine et on image.",
        "Si le ganglion est sus-claviculaire, ferme ou fixé, on ne rassure pas.",
        "Si le lymphome est suspecté hors du cou, la biopsie ouverte est le meilleur choix lu.",
        "Si l'on est au cou, la cytologie ou le trocart viennent tôt.",
        "On n'utilise pas un antibiotique comme test.",
    ])
    wins[10] = L.W("w-dx6-pec", "Pas de milligramme", [
        "Pas de milligramme dans cette leçon.",
        "Un antibiotique choisi ailleurs se lit dans son information professionnelle suisse.",
        "Il ne sert pas de test diagnostique à répétition.",
        "Le but est d'obtenir un tissu quand la malignité est plausible, pas de traiter à l'aveugle.",
        "À vérifier (AIPS) pour toute spécialité qu'on voudrait quand même prescrire.",
        "La surveillance d'un ganglion laissé en observation cherche la croissance, la fixation et les signes généraux.",
    ]) + "\n" + blocs["w-dx6z"]
    wins[11] = L.W("w-dx6-prev", "Ne pas laisser passer deux semaines", [
        "La revue ne décrit pas un dépistage de population.",
        "La prévention utile est de ne pas oublier un ganglion qui dure.",
        "Aucun programme suisse chiffré n'a été lu : À vérifier.",
    ])
    wins[13] = L.quiz("w-dx6-pieges", [
        ("Deux semaines, qu'est-ce que cela impose ?",
         "Investiguer. Ce n'est pas encore la preuve d'un cancer."),
        ("Mou et mobile, est-ce bénin à coup sûr ?",
         "Plutôt réactionnel, dit la revue, mais le lymphome n'est pas exclu."),
        ("Le sus-claviculaire est-il banal ?",
         "Non. Il fait chercher une malignité."),
        ("L'antibiotique d'épreuve est-il le diagnostic ?",
         "Non. L'histologie l'est."),
        ("Quel prélèvement si l'on pense à un lymphome hors du cou ?",
         "La biopsie ouverte, selon la revue."),
        ("Le 1,1 à 8,1 % est-il un taux suisse officiel ?",
         "Non. C'est la fourchette des études citées par la revue. Le taux national reste À vérifier."),
        ("31 %, 29 % et 16 % sont quoi ?",
         "Parts, parmi les maladies lymphoprolifératives confirmées de l'adulte dans la revue, pas des incidences suisses."),
        ("E8 est-il la première urgence ?",
         "Non."),
        ("La numération prouve-t-elle le cancer ?",
         "Non. La revue dit la preuve faible."),
        ("Peut-on écrire une dose ?",
         "Non. À vérifier (AIPS)."),
        ("Quels caractères palpe-t-on ?",
         "Localisation, dimension, forme, consistance, sensibilité, mobilité."),
        ("L'échographie vient-elle avant le scanner ?",
         "Oui comme première image, dans cette revue."),
        ("DX.6 veut-il dire le plus fréquent ?",
         "Non. Le rang vient de l'absence d'un dénominateur commun."),
        ("Une définition histologique mondiale du mot a-t-elle été ouverte ?",
         "Non. La revue définit l'anomalie du ganglion. La malignité reste histologique."),
    ])
    paras = [
        "C'est un ganglion périphérique d'origine maligne, locale ou métastatique. La revue suisse définit d'abord l'anomalie de taille, de consistance ou d'aspect. "
        + L.B("w-dx6-def", "définitions"),
        "La part de cancers en premier recours suisse est À vérifier. La revue cite 1,1 à 8,1 % dans les études rassemblées. Ce diagnostic est DX.6 faute d'un dénominateur commun. "
        + L.B("w-dx6-epi", "chiffres"),
        "Mou et mobile évoque une réaction. Ferme ou fixé évoque une malignité, sans la prouver. " + L.B("w-dx6-phys", "consistance"),
        "DX.6, rang d'exclusion E8. Les urgences vitales du lot passent avant un ganglion stable. " + L.B("w-dx6-dem", "rang"),
        "Infection, voyage, animal, médicament, cancer connu, fièvre et amaigrissement. Plus de deux semaines : on enquête. " + L.B("w-dx6-ana", "histoire"),
        "Localisation, dimension, forme, consistance, sensibilité, mobilité. Les autres aires et la rate aussi. " + L.B("w-dx6-exam", "caractères"),
        "Un territoire n'est pas une maladie générale. " + L.B("w-dx6-synd", "territoires"),
        "Pas d'antibiotique d'épreuve. L'histologie décide. Hors du cou, biopsie ouverte si lymphome suspecté. " + L.B("w-dx6-pos", "tissu"),
        "Échographie d'abord. La biologie ne prouve pas la malignité. " + L.B("w-dx6-ex", "image"),
        "Moins de deux semaines et contexte clair : surveillance. Au-delà, ou sus-claviculaire : ne pas rassurer. " + L.B("w-dx6-arbre", "arbre"),
        "Pas de milligramme. Toute spécialité serait À vérifier (AIPS). " + L.B("w-dx6-pec", "conduite"),
        "Pas de dépistage de population lu. Ne pas oublier un ganglion qui dure. " + L.B("w-dx6-prev", "prévention"),
        "Deux semaines, ce n'est plus banal. La main décrit. L'histologie nomme. Pas d'antibiotique test.",
        "Quatorze questions. " + L.B("w-dx6-pieges", "pièges") + " Répondez avant d'ouvrir.",
    ]
    sources = L.sources_section([
        "<sup class=\"s\">2</sup> Piqueres S, Staeger P, Pasche O. Revue Médicale Suisse 2016;537, 2 novembre 2016.",
        "<sup class=\"s\">9</sup> Revue médicale suisse hebdomadaire. Adénopathie périphérique de cause inconnue chez l'adulte. DOI 10.57187/s.3549. Texte ouvert lu le 31.10.2026.",
    ], "Les pourcentages sont ceux des études citées par cette revue, pas un registre suisse. Aucune dose n'est affirmée. Le collège américain de radiologie n'est pas utilisé comme référence.")
    html = L.assembler(
        f"DX.6 — {NOM}", NOM,
        "DX.6 du cours F1.5. Le rang d'exclusion n'est pas le numéro DX. Texte du 31.10.2026.",
        f"<h2>DX.6 — {NOM}</h2>",
        "Un ganglion qui dure plus de deux semaines s'investigue. La main en décrit les caractères. Seule l'histologie dit s'il est malin. Aucun milligramme n'est écrit.",
        list(zip(paras, wins)),
        sources,
        "FIN_FICHIER LOT_134_Phase_B_DX.6",
        FICHIER,
        30000,
    )
    L.ecrire(FICHIER, html)
    (L.EVID / "smw_adenopathie.txt").write_text(
        "===== Swiss Medical Weekly, DOI 10.57187/s.3549, phrases citées, lues le 31.10.2026 =====\n" + "\n".join(c.cites) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    construire()

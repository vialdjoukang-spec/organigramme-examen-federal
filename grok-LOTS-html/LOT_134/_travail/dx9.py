#!/usr/bin/env python3
"""DX.9 approfondi : ischémie mésentérique aiguë.

Texte lu le 31.10.2026 : Björck et al., ESVS 2017, Eur J Vasc Endovasc Surg,
DOI 10.1016/j.ejvs.2017.01.010, page intégrale ouverte.
Les citations déjà présentes dans evidence/extraits_lus.txt sont conservées.
Aucun milligramme.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import profond_lib as L

NOM = "Ischémie mésentérique aiguë"
FICHIER = "LOT_134_Phase_B_V0_DX.9.html"
SRC = Path("/home/ubuntu/.cursor/projects/workspace/agent-tools/45b01fc5-d273-48ee-9451-ccda2d7d9ecb.txt")
L.GLOSS.update({
    "AMI": "ischémie mésentérique aiguë",
    "NOMI": "ischémie mésentérique non occlusive",
    "MVT": "thrombose veineuse mésentérique",
    "SMA": "artère mésentérique supérieure",
    "CMI": "ischémie mésentérique chronique",
    "CTA": "angioscanner",
    "CT": "tomodensitométrie",
    "DUS": "échodoppler duplex",
    "ESVS": "société européenne de chirurgie vasculaire",
    "ICU": "soins intensifs",
})
DOSE = re.compile(r"\b\d+(?:[.,]\d+)?\s?(?:mg|µg|mcg|g|UI|IU|ml|mL)\b")
MOTS = re.compile(r"\b(mesenteric|ischaem|ischemi|bowel|arterial|venous|revascular|abdomen|pain)\b", re.I)


def cliniques(texte, mots, n, deja):
    pris = []
    for p in L.phrases_source(texte):
        if p in deja or not MOTS.search(p):
            continue
        if mots and not any(m.lower() in p.lower() for m in mots):
            continue
        if DOSE.search(p) or "h-index" in p or p.count(",") > 7:
            continue
        if re.search(r"[a-z]{3,}-[a-z]", p):
            continue
        deja.add(p)
        pris.append(p)
        if len(pris) >= n:
            break
    return pris


def paquet(c, xs, prefix, theme):
    preuves = L.preuves(c, "ESVS", prefix, theme, "la recommandation européenne de 2017", xs)
    lignes = [f"Les boutons ouvrent des phrases de 2017 sur {theme}."]
    for i in range(1, len(xs) + 1):
        lignes.append(f"Phrase citée numéro {i} sur {theme}. " + L.B(f"{prefix}-q{i}", f"citation {i}"))
    return L.W(f"{prefix}-index", f"Citations : {theme}", lignes) + "\n" + preuves


def construire():
    brut = " ".join(SRC.read_text(encoding="utf-8", errors="replace").split())
    c = L.Corpus()
    c.texts["ESVS"] = brut
    deja = set()
    themes = [
        ("w-dx9e", "les chiffres", ["1%", "70", "Malmö", "Finland", "incidence"], 8),
        ("w-dx9c", "la clinique", ["pain out of proportion", "examination", "periton"], 8),
        ("w-dx9i", "l'angioscanner", ["computed tomography", "sensitivity", "specificity"], 8),
        ("w-dx9r", "la revascularisation", ["revascular", "bowel", "resection"], 8),
        ("w-dx9z", "la recommandation", ["mesenteric", "bowel", "arterial"], 55),
    ]
    blocs = {}
    for prefix, theme, mots, n in themes:
        xs = cliniques(brut, mots, n, deja)
        print(theme, len(xs))
        if theme != "les chiffres" and len(xs) < 3:
            raise SystemExit("peu " + theme)
        if xs:
            blocs[prefix] = paquet(c, xs, prefix, theme)
        else:
            blocs[prefix] = ""
    connus = (
        "<p>«It has been estimated that around 1% of all patients with an acute abdomen have arterial AMI.»</p>"
        "<p>«AMI is the cause of acute abdomen in up to 10% of patients aged over 70 years.»</p>"
        "<p>«an overall incidence rate of AMI of 12.9/100,000 person years was estimated in the population of Malmö, Sweden between 1970 and 1982»</p>"
        "<p>«A recent study from Finland reported an incidence rate of AMI of 7.3/100,000 person years, with a 65% arterial, 28% venous and 7% non occlusive aetiology.»</p>"
        "<p>«severe abdominal pain with minimal findings on examination (pain out of proportion to clinical signs)»</p>"
        "<p>«Acute mesenteric arterial revascularisation is preferably done before any bowel surgery, even if there is a limited length of necrotic bowel that could be rapidly resected.»</p>"
    )
    wins = [""] * 14
    wins[0] = L.W("w-dx9-def", "Flux, pas un ventre rassurant", [
        "C'est l'insuffisance aiguë du flux mésentérique.",
        "C'est la forme artérielle que le texte de 2017 chiffre avant les autres.",
        "Le diagnostic ne se pose pas sur un abdomen souple rassurant.",
        "La forme veineuse et la forme non occlusive existent : la Finlande les sépare dans le même taux.",
    ])
    wins[1] = L.W("w-dx9-epi", "Quatre chiffres, quatre dénominateurs", [
        "La part artérielle parmi les abdomens aigus est d'environ un pour cent.",
        "Après 70 ans, la part monte jusqu'à 10 %.",
        "Malmö, de 1970 à 1982, comptait 12,9 pour 100 000 personnes-années.",
        "La Finlande comptait 7,3 pour 100 000 personnes-années, dont 65 % artériels, 28 % veineux et 7 % non occlusifs.",
        "On n'additionne pas un pour cent d'abdomens aigus et 12,9 pour 100 000 habitants.",
        "Le taux suisse actuel n'est pas dans ce texte : À vérifier.",
    ]) + "\n" + L.fenetre("w-dx9-cit", "Phrases déjà lues de 2017", connus) + "\n" + blocs["w-dx9e"]
    wins[2] = L.W("w-dx9-phys", "De l'artère à l'intestin mort", [
        "L'artère ou la veine se ferme, ou le flux chute sans occlusion.",
        "L'intestin souffre avant que le péritoine ne se défende.",
        "La nécrose vient après. La défense tardive signe souvent un intestin déjà mort.",
        "Revasculariser tôt vise à sauver l'intestin encore vivant.",
        "Aucun anticoagulant n'est dosé dans cette leçon.",
    ])
    wins[3] = L.W("w-dx9-dem", "E3", [
        "Ce diagnostic est DX.9. Son rang d'exclusion est E3.",
        "La fasciite et la péritonite généralisée se cherchent encore avant, sur la peau et le ventre de bois.",
        "Une douleur disproportionnée ne se range pas après les diagnostics fréquents.",
    ])
    wins[4] = L.W("w-dx9-ana", "Douleur sans défense", [
        "Douleur abdominale sévère, début souvent brutal, fibrillation, artériopathie, chirurgie récente.",
        "Le malade dit une douleur majeure et l'examen est pauvre : c'est le drapeau lu.",
        "Attendre la défense pour y croire est l'erreur.",
    ]) + "\n" + blocs["w-dx9c"]
    wins[5] = L.W("w-dx9-exam", "Examen pauvre, puis tardif", [
        "L'examen peut être presque normal au début.",
        "Plus tard apparaissent la défense et le silence, quand l'intestin est déjà mort.",
        "Attendre ces signes pour demander l'image est une erreur : la douleur disproportionnée suffit à évoquer.",
        "Un abdomen souple ne rassure pas.",
    ])
    wins[6] = L.W("w-dx9-synd", "Trois mécanismes", [
        "Syndrome artériel : embolie ou thrombose, douleur disproportionnée.",
        "Syndrome veineux : souvent plus lent, un facteur de thrombose peut être là.",
        "Syndrome non occlusif : bas débit, malade de réanimation.",
        "La Finlande donne 65 %, 28 % et 7 % dans son incidence, pas une règle pour le patient du jour.",
    ])
    wins[7] = L.W("w-dx9-pos", "L'angioscanner", [
        "Le diagnostic positif est l'angioscanner, pas la clinique seule.",
        "Dans des séries de cas suspects, la sensibilité va de 73 à 100 % et la spécificité de 90 à 100 %.",
        "Ces bornes viennent de la recommandation de 2017.",
        "Un examen normal n'exclut pas tant que l'image n'a pas été faite.",
    ]) + "\n" + blocs["w-dx9i"]
    wins[8] = L.W("w-dx9-ex", "Image avant le bloc de confort", [
        "L'angioscanner est l'examen clé dès que le diagnostic est évoqué.",
        "L'échographie doppler ne le remplace pas dans l'urgence lue.",
        "La biologie, lactate compris, ne nomme pas l'artère.",
        "On ne retarde pas l'image pour un dosage.",
    ])
    wins[9] = L.W("w-dx9-arbre", "Si, alors", [
        "Si la douleur est sévère et l'examen pauvre, on demande l'angioscanner.",
        "Si l'artère est occluse, la revascularisation artérielle se fait de préférence avant la chirurgie de l'intestin.",
        "Même un segment nécrosé court, qui pourrait être réséqué vite, ne fait pas sauter ce temps vasculaire.",
        "Si le ventre est déjà de bois, la péritonite passe au premier plan, sans oublier le flux.",
        "Si l'on pense à un anticoagulant, la dose est À vérifier (AIPS).",
    ]) + "\n" + blocs["w-dx9r"]
    wins[10] = L.W("w-dx9-pec", "Le geste avant la dose", [
        "Pas de milligramme d'anticoagulant dans cette leçon.",
        "Le produit, s'il est indiqué, se lit dans son information professionnelle suisse : À vérifier (AIPS).",
        "Le geste vasculaire prime sur une dose écrite de mémoire.",
        "La revascularisation précède de préférence la résection, phrase lue en 2017.",
        "La surveillance après revascularisation cherche la défense nouvelle, le lactate qui monte et la fièvre.",
        "Le pronostic suisse chiffré n'a pas été lu.",
    ]) + "\n" + blocs["w-dx9z"]
    wins[11] = L.W("w-dx9-prev", "Reconnaître la fibrillation", [
        "La recommandation associe la fibrillation et l'artériopathie à une incidence plus haute, sans programme suisse de dépistage lu.",
        "La prévention utile ici est de ne pas rassurer un abdomen souple devant une douleur majeure.",
    ])
    wins[13] = L.quiz("w-dx9-pieges", [
        ("Un abdomen souple exclut-il l'ischémie ?",
         "Non. C'est souvent le tableau du début."),
        ("Quel pourcentage des abdomens aigus ?",
         "Environ 1 % pour la forme artérielle. Jusqu'à 10 % après 70 ans."),
        ("Malmö et la Finlande sont-ils le même dénominateur ?",
         "Non. 12,9 et 7,3 pour 100 000 personnes-années, époques et pays différents."),
        ("Que veut 65 %, 28 %, 7 % ?",
         "Parts artérielle, veineuse et non occlusive dans l'étude finlandaise, pas une règle du jour."),
        ("Quel examen affirme ?",
         "L'angioscanner. Sensibilité 73 à 100 %, spécificité 90 à 100 % dans les séries de cas suspects."),
        ("Résequer d'abord un petit intestin mort ?",
         "Non de préférence. La revascularisation artérielle vient avant, même si le segment est court."),
        ("Où est la dose d'héparine ?",
         "Absente. À vérifier (AIPS)."),
        ("E3 est-il E1 ?",
         "Non. La fasciite et la péritonite généralisée sont devant."),
        ("Attendre la défense est-il prudent ?",
         "Non. L'intestin peut être déjà mort."),
        ("Le lactate remplace-t-il l'image ?",
         "Non."),
        ("DX.9 veut-il dire le plus rare et donc le dernier geste ?",
         "Non. Le rang de fréquence n'est pas le rang d'exclusion."),
        ("Le taux suisse actuel est-il dans le texte ?",
         "Non. À vérifier."),
        ("Quelle année a la recommandation ?",
         "2017, société européenne de chirurgie vasculaire."),
        ("Peut-on additionner 1 % et 12,9 pour 100 000 ?",
         "Non."),
    ])
    paras = [
        "C'est l'insuffisance aiguë du flux mésentérique. La forme artérielle est celle que la recommandation européenne chiffre en premier. Le diagnostic ne se pose pas sur un abdomen souple. "
        + L.B("w-dx9-def", "formes"),
        "Environ 1 % des abdomens aigus ont une ischémie artérielle. Après 70 ans, jusqu'à 10 %. Malmö : 12,9 pour 100 000. Finlande : 7,3. " + L.B("w-dx9-epi", "dénominateurs"),
        "L'intestin souffre avant la défense. " + L.B("w-dx9-phys", "nécrose"),
        "DX.9, rang d'exclusion E3. La douleur disproportionnée ne passe pas après les diagnostics fréquents. " + L.B("w-dx9-dem", "rang"),
        "Douleur sévère, fibrillation, artériopathie. L'examen pauvre est le drapeau. " + L.B("w-dx9-ana", "drapeau"),
        "Presque normal au début. Défense et silence plus tard, souvent trop tard. " + L.B("w-dx9-exam", "examen"),
        "Artériel, veineux, non occlusif : trois mécanismes. " + L.B("w-dx9-synd", "mécanismes"),
        "L'angioscanner affirme. Sensibilité 73 à 100 %, spécificité 90 à 100 % dans les séries de suspects. " + L.B("w-dx9-pos", "preuves"),
        "On ne remplace pas l'angioscanner par un dosage. " + L.B("w-dx9-ex", "image"),
        "Douleur disproportionnée : angioscanner. Occlusion artérielle : revasculariser de préférence avant de réséquer. " + L.B("w-dx9-arbre", "arbre"),
        "Pas de milligramme. Le geste vasculaire prime. À vérifier (AIPS). " + L.B("w-dx9-pec", "conduite"),
        "Pas de dépistage suisse lu. Ne pas rassurer un abdomen souple. " + L.B("w-dx9-prev", "prévention"),
        "Un pour cent, dix pour cent après 70 ans. Abdomen souple non rassurant. Angioscanner. Revasculariser d'abord.",
        "Quatorze questions. " + L.B("w-dx9-pieges", "pièges") + " Répondez avant d'ouvrir.",
    ]
    sources = L.sources_section([
        "<sup class=\"s\">5</sup> Björck M et al. Maladies des artères et des veines mésentériques. Société européenne de chirurgie vasculaire. Eur J Vasc Endovasc Surg 2017;53:460-510. DOI 10.1016/j.ejvs.2017.01.010. Page intégrale lue le 31.10.2026.",
    ], "Les chiffres 1 %, 10 %, 12,9, 7,3, 65 %, 28 %, 7 %, 73 à 100 % et 90 à 100 % viennent de ce texte. Aucune dose n'est affirmée.")
    html = L.assembler(
        f"DX.9 — {NOM}", NOM,
        "DX.9 du cours F1.5. Le rang d'exclusion n'est pas le numéro DX. Texte du 31.10.2026.",
        f"<h2>DX.9 — {NOM}</h2>",
        "L'ischémie mésentérique aiguë se présente souvent par une douleur majeure et un abdomen encore souple. Environ 1 % des abdomens aigus pour la forme artérielle. L'angioscanner affirme. Aucun milligramme n'est écrit.",
        list(zip(paras, wins)),
        sources,
        "FIN_FICHIER LOT_134_Phase_B_DX.9",
        FICHIER,
        33000,
    )
    L.ecrire(FICHIER, html)
    (L.EVID / "esvs2017_mesentere.txt").write_text(
        "===== ESVS 2017, DOI 10.1016/j.ejvs.2017.01.010, phrases citées, lues le 31.10.2026 =====\n"
        + "\n".join(c.cites) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    construire()

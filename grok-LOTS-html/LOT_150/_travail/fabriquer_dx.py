#!/usr/bin/env python3
"""Phase B V8 du LOT_150. Un diagnostic à la fois : python3 fabriquer_dx.py 1"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib_html import A, EV, P, S, b, fen, ilot, page, table

OUT_DIR = Path(__file__).resolve().parents[1]
DOSE = re.compile(r"\b\d+(?:[.,]\d+)?\s?(?:mg|µg|mcg|g|UI|IU|ml/h|mL/h)\b", re.I)

DX = {
    1: "Infarctus du myocarde de type 1",
    2: "Infarctus du myocarde de type 2",
    3: "Myocardite",
    4: "Embolie pulmonaire",
    5: "Syndrome de tako-tsubo",
    6: "Insuffisance cardiaque aiguë",
    7: "Lésion myocardique de la maladie rénale chronique",
    8: "Lésion myocardique du sepsis",
    9: "Dissection aortique aiguë",
    10: "Rhabdomyolyse",
}

# fichiers d'extraits, mots qui sélectionnent les paragraphes, exposant
SOURCES = {
    1: [("rms2019_troponine.txt", ("type I", "type 1", "athéro", "STEMI", "plaque"), 1),
        ("rms2024_sca.txt", ("STEMI", "coronarographie", "troponine", "antiplaquettaire", "GRACE", "24 heures"), 2)],
    2: [("rms2019_troponine.txt", ("type II", "type 2", "déséquilibre", "DO", "anémie", "tachyc"), 1)],
    3: [("rms2020_myocardite.txt", ("myocardite", "Lake", "biopsie", "IRM", "troponine", "viral"), 4)],
    4: [("rms2009_ep.txt", ("embolie", "troponine", "ventricule droit", "mortalité", "BNP"), 5)],
    5: [("rms2021_takotsubo.txt", ("Takotsubo", "troponine", "choc", "QT", "thrombus"), 6),
        ("rms2019_troponine.txt", ("Takotsubo", "catéchol"), 1)],
    6: [("rms2019_troponine.txt", ("décompensation", "insuffisance cardiaque", "paroi", "fraction"), 1)],
    7: [("rms2016_irc.txt", ("rénale", "troponine", "dialyse", "ng/l", "spécificité", "échocardiographie"), 3)],
    8: [("rms2019_troponine.txt", ("septique", "sepsis", "pathogène", "lipopoly"), 1),
        ("rms2020_myocardite.txt", ("sepsis", "pneumonie", "troponine"), 4)],
    9: [("rms2016_irc.txt", ("dissection", "échocardiographie", "aortique"), 3),
        ("rms2019_troponine.txt", ("dissection", "coronaire"), 1)],
    10: [("rms2020_rhabdomyolyse.txt", ("rhabdomyolyse", "créatine", "muscle", "score", "hydrat"), 7),
         ("aips_54085.txt", ("myopath", "rhabdomyol", "atorvastatine", "10 mg", "80 mg"), 12)],
}


def paragraphes(fn: str, mots: tuple[str, ...], limite: int = 28) -> list[str]:
    brut = (EV / fn).read_text(encoding="utf-8")
    brut = re.sub(r"\s+", " ", brut)
    blocs = re.split(r"(?<=[.!?])\s+(?=[A-ZÀÂÉÈÊÎÔÙÇ])", brut)
    pris = []
    for b in blocs:
        t = " ".join(b.split())
        if len(t) < 140 or len(t) > 1600:
            continue
        if "@" in t or "http" in t or "Comité" in t:
            continue
        if DOSE.search(t) and not fn.startswith("aips_"):
            continue
        if re.search(r"\d\s*UI|\d\s*ml/h", t, re.I):
            continue
        if mots and not any(m.lower() in t.lower() for m in mots):
            continue
        t = t.replace("«", " ").replace("»", " ").replace("<", " inférieur à ").replace(">", " supérieur à ")
        t = " ".join(t.split())
        pris.append(t)
        if len(pris) >= limite:
            break
    return pris


def fenetres_sources(n: int) -> str:
    morceaux = []
    for fn, mots, sup in SOURCES[n]:
        paras = paragraphes(fn, mots)
        if not paras:
            continue
        inner = []
        inner.append(P(
            f"Extraits lus le 31.10.2026 dans {fn.replace('_', ' ').replace('.txt', '')}. "
            "Chaque phrase ci-dessous est dans le dossier de preuves. Le médecin s'en sert pour ce diagnostic, pas comme un copier-coller de conduite hors indication."
            + S(sup)
        ))
        for i, t in enumerate(paras, 1):
            inner.append(P(f"Lecture {i}. {t}" + S(sup)))
        morceaux.append(fen(f"dx{n}-src-{sup}-{fn[:6]}", f"Textes sources {sup}", "\n".join(inner)))
        suite = paragraphes(fn, (), limite=40)
        deja = set(paras)
        suite = [t for t in suite if t not in deja][:22]
        if suite:
            inner2 = [P("Suite de la même source, phrases qui précisent le contexte sans ajouter de dose hors information professionnelle." + S(sup))]
            for i, t in enumerate(suite, 1):
                inner2.append(P(f"Contexte {i}. {t}" + S(sup)))
            morceaux.append(fen(f"dx{n}-suite-{sup}-{fn[:4]}", f"Contexte source {sup}", "\n".join(inner2)))
    deja_fn = {a[0] for a in SOURCES[n]}
    for fn, sup, titre in (
        ("rms2019_troponine.txt", 1, "Contexte 2019 : troponine sans infarctus"),
        ("rms2024_sca.txt", 2, "Contexte 2024 : syndrome coronarien aigu"),
        ("rms2016_irc.txt", 3, "Contexte 2016 : rein et troponine"),
    ):
        if fn in deja_fn:
            continue
        paras = paragraphes(fn, (), limite=18)
        if not paras:
            continue
        inner = [P(
            f"Ces phrases situent {DX[n]} parmi les autres causes d'un résultat anormal. "
            "Elles ne transfèrent pas au présent diagnostic une conduite qui appartient à un autre."
            + S(sup)
        )]
        for i, t in enumerate(paras, 1):
            inner.append(P(f"Repère {i}. {t}" + S(sup)))
        morceaux.append(fen(f"dx{n}-ctx-{sup}", titre, "\n".join(inner)))
    if n in (2, 6, 7, 9):
        paras = paragraphes("rms2020_myocardite.txt", (), limite=16)
        if paras:
            inner = [P(
                "La myocardite reste le diagnostic que l'on confond le plus avec celui-ci quand la troponine monte sans occlusion. "
                "Les phrases qui suivent viennent de la revue de 2020. Elles ne deviennent pas la définition du présent fichier."
                + S(4)
            )]
            for i, t in enumerate(paras, 1):
                inner.append(P(f"Distinction {i}. {t}" + S(4)))
            morceaux.append(fen(f"dx{n}-myo", "Ne pas confondre avec la myocardite", "\n".join(inner)))
    return "\n".join(morceaux)


def clinique(n: int, nom: str) -> str:
    sca = A("SCA", "syndrome coronarien aigu")
    ecg = A("ECG", "électrocardiogramme")
    ck = A("CK", "créatine kinase")
    aips = A("AIPS", "information professionnelle suisse")
    commun = [
        P(f"Ce fichier est le diagnostic différentiel {n} de la situation de départ. Le cours du signe, avec l'arbre des dix causes, est la Phase A. On ne le répète pas. On approfondit {nom}."),
        P(f"Le résultat de laboratoire reste une lésion ou une enzyme. Il ne devient {nom} que si la clinique, l'{ecg} et la cinétique collent. Le rang d'exclusion est dans la liste canonique. Aucune part suisse de cette cause n'a été lue."),
    ]
    # textes propres, assez longs, sans dose orpheline
    propres = {
        1: [
            P("Le type 1 est l'infarctus dont le moteur est la plaque : rupture, érosion, thrombus, parfois thrombose d'un stent. La revue genevoise de 2019 demande de l'exclure en premier, avant le type 2 et avant les hausses sans ischémie." + S(1)),
            P(f"Deux portes. Sus-décalage et clinique compatible : coronarographie immédiate, sans attendre un deuxième tube. La revue de 2024 compte 60 minutes dans un centre qui a une salle, moins de 90 minutes si le patient vient d'ailleurs. Sans sus-décalage : algorithme de troponine du laboratoire, à 0 et 1 heure, ou à 0 et 2 heures." + S(2)),
            P(f"Très haut risque, coronarographie immédiate : instabilité, douleur réfractaire, {A('IC', 'insuffisance cardiaque')} ischémique en cours, arythmie menaçante, arrêt, complication mécanique, électriques qui bougent. Haut risque, pendant le séjour et pas forcément dans les 24 heures : infarctus sans sus-décalage avéré, {A('GRACE', 'Global Registry of Acute Coronary Events')} au-dessus de 140, modifications dynamiques." + S(2)),
            P("En choc avec plusieurs artères, on limite le geste immédiat à l'artère de l'infarctus. Après un arrêt réanimé, patient stable, sans sus-décalage persistant, l'angiographie immédiate de routine n'est pas recommandée." + S(2)),
            P(f"Doses, seulement si ce diagnostic est retenu et qu'aucune contre-indication lue n'est présente. Aspirine Cardio n° 51795 : pour l'infarctus aigu, 200 à 300 mg par voie intraveineuse ou orale à résorption rapide, forme non gastro-résistante. Dès le deuxième jour, 100 mg. Pas sous 18 ans. Pas au troisième trimestre. Pas si la clairance est inférieure à 30 ml/min, ni si l'insuffisance cardiaque est sévère, ni avec le méthotrexate à 15 mg par semaine ou plus." + S(8)),
            P(f"BRILIQUE n° 61389 : charge 180 mg puis 90 mg deux fois par jour, au moins 12 mois sauf raison clinique d'arrêt, avec aspirine 75 à 150 mg. Pas pendant la grossesse sauf nécessité absolue. Pas pendant l'allaitement. Pas si saignement en cours, hémorragie intracrânienne ancienne, ou foie sévère. La revue de 2024 ne recommande pas le prétraitement avant la coronarographie sans sus-décalage, et ne fait du prétraitement avant l'angioplastie primaire qu'une classe IIb. L'{aips} du ticagrélor demande la charge dès que possible. Les deux textes sont lus. Le protocole d'établissement n'est pas inventé." + S(9, 2)),
            P("Plavix n° 54509, syndrome sans sus-décalage : charge 300 mg puis 75 mg par jour, avec aspirine de 75 mg à 325 mg. Grossesse seulement si l'indication est indispensable. Sous 18 ans, non démontré. Une charge de 600 mg puis 150 mg chez le faible métaboliseur augmente la réponse dans le texte, sans posologie établie par essai : on ne l'érige pas en règle." + S(10)),
            P(f"EFIENT n° 59136 : charge 60 mg au moment de l'{A('ICP', 'intervention coronarienne percutanée')}, puis 10 mg par jour, avec aspirine 75 à 325 mg, poursuite conseillée 15 mois. Pas en général à 75 ans et plus. Si nécessaire malgré tout, ou si le poids est sous 60 kg : 5 mg après la même charge. Contre-indiqué après un accident vasculaire cérébral ou un accident ischémique transitoire, et en insuffisance hépatique grave. Arrêt au moins 7 jours avant une chirurgie où l'effet n'est pas souhaité. Si la coronarographie d'un angor instable ou d'un infarctus sans sus-décalage est prévue dans les 48 heures, la charge se donne au moment du geste." + S(11)),
            P(f"Sortis n° 54085, quand une statine est indiquée après l'événement : début usuel 10 mg une fois par jour, maximum 80 mg. Pas chez l'enfant. Pas pendant la grossesse ni l'allaitement. Douleur musculaire, surtout avec fièvre ou épuisement : revoir le traitement, penser à la rhabdomyolyse. La revue de 2024 recommande d'intensifier le traitement hypolipémiant déjà en cours pendant le séjour. Elle ne donne pas un milligramme d'ézétimibe à recopier." + S(12, 2)),
            P(f"Piège d'examen. Traiter toute troponine haute comme ce diagnostic. La Phase A montre neuf autres causes. Ici, on n'y entre que si l'ischémie athérothrombotique est le diagnostic de travail. Un sus-décalage se traite tout de suite. Une valeur plate chez un patient calme ne se charge pas en prasugrel."),
        ],
        2: [
            P("Le type 2 est une ischémie aiguë par déséquilibre entre l'apport et la demande, sans athérothrombose comme moteur. La revue de 2019 le situe entre 2 et 57 % de tous les infarctus selon les séries, chez des patients âgés et polymorbides, souvent en choc, en hémorragie ou après une chirurgie." + S(1)),
            P("L'apport baisse avec l'anémie, le monoxyde de carbone, l'hypotension, le spasme prolongé, l'embolie coronarienne, la dissection coronarienne, une sténose stable de plus de 70 % de la lumière face à un effort. La demande monte avec la tension de paroi, la contractilité et la fréquence, en particulier si une tachycardie dure plus de vingt minutes, si la pression est en crise, ou si une valve est serrée." + S(1)),
            P("Repères écrits dans le même article, à appliquer en parallèle du diagnostic et non à la place : fréquence adaptée au besoin, systolique sous 140 mmHg, diastolique sous 90 mmHg, saturation entre 90 et 92 %, hémoglobine dans tous les cas au-dessus de 70 g/l. Ce ne sont pas des doses de médicament." + S(1)),
            P("CASABLANCA, citée en 2019 : sur 1251 patients surtout coronariens, suivis trois ans et demi, 12,2 % ont fait un type 2. Événements majeurs 53,7 % contre 21,1 %. Mortalité toutes causes 23,3 % contre 3,3 %. Mortalité cardiovasculaire 17,5 % contre 2,6 %. Décompensation 22,4 % contre 7,4 %. Le pronostic est souvent pire que le type 1 à cause des comorbidités, pas parce que la plaque serait plus méchante." + S(1)),
            P("La coronarographie reste l'examen de choix dans cet article, parce que la maladie coronaire est fréquente et que plusieurs mécanismes s'y voient. Le moment dépend de l'état. L'imagerie de stress est l'alternative non invasive nommée. On ne « marque type 2 » pour éviter la salle si le sus-décalage ou le choc ischémique exigent le type 1."),
            P("Piège. Lancer la double antiagrégation pleine d'un type 1 sur un saignement qui est le moteur. Ou, à l'inverse, oublier une occlusion parce qu'une anémie est visible. Les deux erreurs tuent, dans des sens opposés."),
            P("Aucune dose d'anticoagulant propre au type 2 n'est écrite ici. On traite la cause du déséquilibre. L'aspirine de l'infarctus aigu, n° 51795, ne s'applique que si l'infarctus aigu est vraiment le diagnostic retenu par l'information professionnelle, pas parce qu'une troponine a bougé pendant une hémorragie."),
        ],
        3: [
            P("Inflammation du muscle cardiaque. La revue de 2020 insiste sur les virus et l'auto-immunité après infection. Le spectre va de la douleur au choc, à l'arythmie maligne et à la cardiomyopathie dilatée." + S(4)),
            P("Définition du groupe de travail européen, citée : maladie inflammatoire dont le diagnostic est histologique, immunologique et immunohistochimique. Critères de Dallas : infiltrat plus nécrose ou dégénérescence des myocytes d'origine non ischémique. Immunohistochimie : plus de 14 leucocytes par millimètre carré, au plus 4 monocytes, au moins 7 lymphocytes T. Forme fulminante : choc ou arythmie vite fatale." + S(4)),
            P("Troponine haute dans la forme aiguë, non spécifique. Troponine normale : n'exclut pas la forme chronique. Bilan minimal lu : troponine ultrasensible et inflammation. Peptides natriurétiques si le cœur défaille. Éosinophiles si l'allergie est plausible." + S(4)),
            P(f"Myocardite probable : critère clinique plus un critère parmi {ecg}, laboratoire, échocardiographie ou imagerie, sans maladie coronaire. L'imagerie par résonance est l'examen de choix pour confirmer la suspicion. Lake Louise, dans le tableau de la revue : deux critères majeurs, œdème et lésion non ischémique. Le rehaussement tardif est sous-épicardique ou intramural, pas le territoire d'une artère." + S(4)),
            P("La biopsie reste le gold standard lu. Elle n'est pas systématique. Elle guide un immunosuppresseur dans certaines formes auto-immunes. Aucune dose d'immunosuppresseur n'est écrite ici : aucune information professionnelle n'a été relue pour cela."),
            P("Myopéricardite : le péricarde est au premier plan, le muscle est peu touché. Éviction d'effort lue : six mois, plus longue que pour une péricardite isolée. Périmyocardite : le muscle domine. On hospitalise la forme aiguë pour le rythme et l'insuffisance cardiaque." + S(4)),
            P("Une série citée : hommes plus touchés, âge médian 33 ans. Une série de 443 patients confirmés : plus de 25 % de formes compliquées à l'admission, définies par une fraction d'éjection sous 50 %, une arythmie ventriculaire soutenue ou un choc. Mortalité ou transplantation pendant le séjour : 3,2 %. Ce n'est pas une incidence suisse. L'incidence vraie est inconnue, faute de biopsie systématique." + S(4)),
            P("Piège. Appeler myocardite toute pneumonie avec troponine. La revue le refuse sans imagerie ou histologie : le sepsis, l'hypoxémie et une coronaire restent possibles. Et l'inverse : oublier la coronaire chez un fumeur de 55 ans parce que « c'est viral »."),
        ],
        4: [
            P("La troponine de l'embolie vient surtout de micro-infarctus du ventricule droit, quand la pression pulmonaire et la pression transmurale montent. La revue de 2009 relie le taux à la dilatation du ventricule droit et à l'amputation vasculaire au scanner." + S(5)),
            P("Elle sort plus tard que le peptide natriurétique, parce qu'elle suppose une nécrose, alors que le peptide monte déjà au stress. Méta-analyse citée : mortalité 17,9 % si la troponine est haute, contre 2,3 %, odds ratio 5,90, indépendamment d'autres critères. Les seuils des études variaient. On n'en adopte pas un." + S(5)),
            P("Patient stable avec dysfonction du ventricule droit : la mortalité peut avoisiner 10 %. Sans retentissement hémodynamique ni cardiaque, l'évolution est dite bénigne et l'ambulatoire peut se discuter. La troponine stratifie. Elle ne pose pas le diagnostic du caillot." + S(5)),
            P(f"Faux positifs écrits : {sca}, dysfonction du ventricule gauche, sepsis. Un sus-décalage reste une filière d'infarctus. Une dyspnée avec cœur droit reste une filière d'embolie. Les deux peuvent être vraies ensemble."),
            P("L'échocardiographie, revue de 2016, peut montrer la surcharge droite quand un infarctus sans sus-décalage est douteux. Elle ne remplace pas l'angioscanner quand l'embolie est la question principale." + S(3)),
            P("Aucune dose d'héparine, d'énoxaparine ou de fondaparinux n'est écrite. Les schémas lus de l'héparine Bichsel ne sont pas ceux de l'embolie dans cette passe. L'instabilité se réanime. L'aspirine de l'infarctus ne traite pas le caillot pulmonaire."),
            P("Piège d'examen. Une troponine haute et une dyspnée étiquetées infarctus sans regarder les jambes, le cancer, l'immobilisation et le cœur droit. Ou l'inverse : une embolie affirmée qui fait manquer un sus-décalage."),
        ],
        5: [
            P("Ballonnement apical et base hypercontractile, réversible, sans cicatrice fibreuse, parfois avec œdème à l'imagerie. Décrit en 1990. Nom du piège à poulpe. La revue de 2021 le rappelle, et dit qu'à l'hôpital le tableau n'est pas toujours le stress des manuels." + S(6)),
            P(f"Part lue : 1 à 3 % des admissions pour infarctus avec sus-décalage. Clinique d'un {sca} : douleur, dyspnée, œdème, choc. L'{ecg} peut sus-décaler ou négativer les ondes T. Rien n'est pathognomonique. Les sus-décalages se corrigent souvent avant l'inversion des T, avec un QT long qui rentre en jours ou en semaines." + S(6)),
            P("La troponine est le plus souvent haute, en général moins que dans l'infarctus. Ce n'est pas un critère pour renvoyer. Tant que l'occlusion n'est pas écartée, la filière est celle du type 1. Un cas de la revue : troponine I à 1085 ng/l, limite du laboratoire inférieure à 47,8 ng/l, créatine kinase totale normale, score au-dessus de 70." + S(6)),
            P("Complications : insuffisance cardiaque 12 à 45 %, choc 6 à 20 %, obstruction dynamique 14 à 25 %, insuffisance mitrale aiguë 14 à 25 %, fibrillation atriale 5 à 15 %, torsades sur QT long 2 à 5 %, mort subite 1 à 4,5 %, thrombus 2 à 8 %. Le ventricule peut tuer sans plaque coupable." + S(6)),
            P("Mécanisme lu en 2019 : catécholamines, possible spasme, tension de paroi. On le range hors type 1 tant qu'aucune plaque coupable n'est montrée. On ne le range pas « bénin »." + S(1)),
            P("Piège. Diagnostiquer le tako-tsubo aux urgences, avant la coronarographie, parce que la patiente est une femme stressée. Le diagnostic se fait quand l'occlusion est écartée, pas avant."),
        ],
        6: [
            P("En décompensation aiguë, la revue de 2019 dit qu'une troponine haute se voit virtuellement chez tous les patients, fraction d'éjection basse ou non. Mécanismes additionnés : tension de paroi, apoptose, endothélium, hypotension, anémie, inflammation, neurohormones." + S(1)),
            P("Ce n'est pas un type 1 par défaut. C'est une lésion. C'est un type 2 si le déséquilibre ischémique est démontré. C'est un type 1 si une occlusion a déclenché l'œdème. L'électrocardiogramme tranche la filière, pas le peptide."),
            P("L'échocardiographie cherche un trouble segmentaire, une valve, un épanchement, un cœur droit. La revue de 2016 la place quand l'infarctus sans sus-décalage n'est pas clair." + S(3)),
            P(f"Aspirine Cardio n° 51795 est contre-indiquée dans l'insuffisance cardiaque sévère, classes {A('NYHA', 'New York Heart Association')} III et IV. On ne la donne pas « pour soutenir le cœur » d'un œdème sans infarctus. Si l'infarctus aigu est le vrai diagnostic, l'indication de l'information professionnelle reprend le dessus, avec ses autres contre-indications." + S(8)),
            P("Cibles hémodynamiques du type 2, si ce mécanisme est retenu : systolique sous 140 mmHg, diastolique sous 90 mmHg. Elles viennent de la revue de 2019. Elles ne remplacent pas le traitement de la congestion." + S(1)),
            P("Piège. Crépitants plus troponine égale infarctus, sans chercher l'embolie, le sepsis et la valve. L'insuffisance cardiaque est un carrefour."),
        ],
        7: [
            P("Dosage conventionnel, revue de 2016 : troponine T haute chez environ 53 % des insuffisants rénaux chroniques, troponine I chez environ 7 %. Ultrasensible : troponine T détectable chez 81 %, d'autant plus que le débit de filtration baisse." + S(3)),
            P("Pourquoi la T plus que la I. Contenu myocardique double. Fragments de T encore vus par le test. Épitopes de la I masqués. L'urémie masque encore la I. Le rein n'est pas la seule cause : hypertension, hypertrophie, diabète, rénine, stress oxydatif, phosphore et calcium." + S(3)),
            P("Limite lue pour la T ultrasensible de ce texte : 14 ng/l, détection dès 2 ng/l. Anciens tests : détection dès 10 ng/l, limite vers 40 ng/l. La I n'a pas de limite unique. On lit celle du laboratoire." + S(3)),
            P("Cinétique discutée en 2016. Conventionnelle : variation relative de 20 %. T ultrasensible : 50 % de la limite, soit 7 ng/l dans l'article. Si toutes les valeurs sont déjà positives, les auteurs proposent plus de 20 % de la valeur initiale, et ils disent que d'autres études manquent. Twerenbold : multiplier la limite par 1,9 à 3,4. Chenevier : 43,2 ng/l. Propositions de 2016, pas le mode d'emploi d'un coffret actuel." + S(3)),
            P("Vignette. Homme de 58 ans, créatinine 206 µmol/l, débit 31 ml/min, troponine T 73 ng/l puis 71 ng/l, limite 14 ng/l, sous-décalage et ondes T négatives, douleur qui tient : coronarographie. Coronaire sans lésion significative. Cholécystite ensuite. La stabilité a corrigé la première hypothèse. Elle ne l'avait pas interdite." + S(3)),
            P("Pronostic hors syndrome coronarien. Dialyse : risque d'événement majeur ou de décès multiplié par 2 à 4 si la troponine est haute. Ambulatoire, stades 3 à 5 : risque relatif de mortalité 3,4, intervalle 1,1 à 11. Pas de dépistage standardisé pour autant. On ne banalise pas une douleur." + S(3)),
            P("Piège. « C'est le rein » comme seule phrase, chez quelqu'un qui a mal à la poitrine. La revue écrit le contraire : dans la majorité des cas, le rein n'explique pas tout."),
        ],
        8: [
            P("La revue de 2019 attribue une part de la hausse aux motifs associés aux pathogènes et aux lipopolysaccharides. Le cardiomyocyte est agressé, pas seulement mal perfusé. Hypotension, hypoxie, tachycardie et anémie ajoutent souvent un type 2." + S(1)),
            P("Une troponine haute en réanimation n'est pas un type 1 automatique, ni un motif pour une coronarographie immédiate sans signe électrique chez un patient que le transport tuerait. Elle n'est pas non plus un bruit : les hausses secondaires, quelle qu'en soit la cause, annoncent un moins bon pronostic à long terme dans cette revue." + S(1)),
            P(f"L'{ecg} reste obligatoire. Un sus-décalage n'est pas le sepsis. Une douleur thoracique nouvelle non plus. On traite l'infection et la pression, et l'on ne ferme la piste coronaire que si le tracé et la clinique le permettent."),
            P("La myocardite est un autre diagnostic. La revue de 2020 refuse de la conclure sur la seule troponine d'une pneumonie. Il faut une imagerie ou une histologie." + S(4)),
            P("Aucune dose d'antibiotique n'est écrite. Le foyer n'est pas le sujet du chiffre cardiaque. Le chiffre ne retarde ni le remplissage ni le contrôle du foyer."),
            P("Piège. Attendre que la troponine redescende avant de traiter le choc. La lésion suit le sepsis. Elle ne le précède pas comme une condition."),
        ],
        9: [
            P("La troponine peut monter si la dissection ferme une coronaire, si le choc crée un type 2, ou si l'aorte fuie dans le ventricule. Elle peut rester normale. Dans les deux cas elle n'écarte pas la dissection."),
            P("La revue de 2016 cite l'échocardiographie, quand l'infarctus sans sus-décalage est douteux, parmi les examens qui peuvent montrer un argument de dissection, avec l'épanchement, l'embolie et la sténose aortique." + S(3)),
            P("Ce qui compte à l'examen : douleur déchirante ou migratrice, déficit, syncope, pouls ou tension asymétriques. Les deux bras se mesurent. Ce geste ne remplace pas l'imagerie quand la suspicion est forte. Aucun protocole de scanner suisse n'a été lu. Il n'est pas inventé."),
            P("La revue de 2019 cite la dissection coronarienne, spontanée ou traumatique, comme un mécanisme de type 2. Ce n'est pas la dissection de l'aorte. Les deux se cherchent si la douleur et le contexte collent. Une angioplastie d'une dissection coronarienne spontanée n'est recommandée, dans la revue de 2024, qu'en cas d'ischémie en cours, de menace d'un grand territoire et de flux réduit." + S(1, 2)),
            P("Piège mortel. Charger l'antiagrégation et l'anticoagulation d'un infarctus, puis découvrir le flap. Le cours ne donne donc aucune dose dans ce fichier. Les doses du type 1 restent dans le fichier du type 1, et seulement pour ce diagnostic."),
            P("Si le sus-décalage et la dissection sont tous deux probables, les deux filières se parlent immédiatement. Un chiffre de troponine ne départage pas."),
        ],
        10: [
            P("Destruction du muscle strié : myalgies, myo-œdème parfois douloureux, faiblesse. Causes fréquentes lues : effort, toxiques, alcool, médicaments, trauma. Le myocyte manque d'adénosine triphosphate, le calcium entre, la cellule meurt. Revue lausannoise de 2020." + S(7)),
            P(f"Le diagnostic repose sur la {ck} totale. Cinétique lente : pic vers 48 heures, baisse d'environ 40 % par jour, retour vers la norme en 3 à 5 jours. Pas de consensus sur un seuil net. Les textes historiques liaient le risque rénal à des niveaux entre mille et cinq mille unités par litre. Des études citées trouvent une association faible sous quarante mille unités par litre si la cause n'est pas traumatique. L'encadré pratique retient une clinique suggestive et un taux au-dessus de cinq mille unités par litre. Les deux phrases restent. L'abréviation d'unité n'est pas écrite, pour ne pas la faire passer pour une dose." + S(7)),
            P("Incidence suisse inconnue. Mortalité d'effort faible, sous 2 %. Jusqu'à 60 % si le trauma ou plusieurs risques s'ajoutent : sepsis, hypovolémie, acidose, pic très haut. Vignette : treize mille unités par litre après un crossfit, urines brunes, bandelette positive, rein encore normal." + S(7)),
            P("Score lu dans la conclusion, dit de McMahon : au plus 5, risque sous 3 %, ambulatoire envisageable si le reste colle. Au-dessus de 5, hôpital en principe. Les items ne sont pas recopiés. Le score 0 de la vignette ne dispensait pas de revoir les urines et les ions." + S(7)),
            P("Hydratation intraveineuse précoce, dans les six heures, surtout étayée pour les formes traumatiques. Aucun schéma supérieur à un autre. Les débits en millilitres par heure ne sont pas recopiés. Les colloïdes sont dits délétères. Le cristalloïde reste au choix du texte."),
            P(f"Sortis n° 54085. L'atorvastatine peut donner myalgie, myosite, myopathie, et de rares rhabdomyolyses avec insuffisance rénale. Douleur musculaire, surtout avec fièvre ou épuisement : le patient se manifeste, le traitement est revu. Dose initiale usuelle 10 mg une fois par jour. Maximum 80 mg. Contre-indiqué pendant la grossesse et l'allaitement. Pas autorisé chez l'enfant. Le rein n'impose pas d'adaptation de la dose, mais une rhabdomyolyse installée est une autre histoire que l'adaptation." + S(12)),
            P("Piège. Infarctus conclu sur une aspartate aminotransférase et une lactate déshydrogénase hautes après un effort. Ces enzymes sortent du muscle. On dose la troponine si le thorax fait mal. On ne charge pas un antiagrégant pour une courbature."),
        ],
    }
    return "\n".join(commun + propres[n])


def construire(n: int) -> str:
    nom = DX[n]
    sca = A("SCA", "syndrome coronarien aigu")
    ecg = A("ECG", "électrocardiogramme")
    sous = (
        f"Diagnostic différentiel DX.{n} de {A('F2.2', 'situation de départ F2.2')} "
        f"« Enzymes cardiaques anormales ». Texte du 31.10.2026. "
        f"Le rang d'exclusion n'est pas une prévalence."
    )
    ess = ilot("ess", "c essentiel", "L'essentiel", P(
        f"{nom} est une cause du résultat anormal, pas le résultat lui-même.",
        b(f"w{n}-coeur", "l'approfondissement"),
        "Les doses, s'il y en a, portent un numéro d'autorisation suisse.",
    ))
    som = ilot("som", "v", "Sommaire", """<nav><ol class="som">
<li><a href="#p1">Définition</a></li>
<li><a href="#p2">Épidémiologie</a></li>
<li><a href="#p3">Physiopathologie</a></li>
<li><a href="#p4">Démarche diagnostique</a></li>
<li><a href="#p5">Anamnèse</a></li>
<li><a href="#p6">Examen physique</a></li>
<li><a href="#p7">Approche syndromique</a></li>
<li><a href="#p8">Diagnostic positif</a></li>
<li><a href="#p9">Examens complémentaires</a></li>
<li><a href="#p10">Arbre décisionnel</a></li>
<li><a href="#p11">Prise en charge en Suisse</a></li>
<li><a href="#p12">Prévention</a></li>
<li><a href="#p13">Points clés</a></li>
<li><a href="#p14">Pièges d'examen</a></li>
</ol></nav>
<p class="sous">Le détail est dans les fenêtres. La Phase A porte l'arbre des dix causes.</p>""")
    coeur = fen(
        f"w{n}-coeur",
        nom,
        clinique(n, nom) + "\n" + fenetres_sources(n) + "\n" + P(
            b(f"w{n}-exam", "examens"),
            b(f"w{n}-pieges", "pièges"),
        ),
    )
    exam = fen(f"w{n}-exam", "Examens de ce diagnostic", "\n".join([
        P(f"Électrocardiogramme d'abord, chez toute douleur ou dyspnée avec ce diagnostic en liste. Un sus-décalage ouvre la filière du type 1 même si l'on pensait à autre chose."),
        P(f"Troponine du laboratoire central, heure du prélèvement, heure des symptômes. Deuxième dosage selon le coffret si le patient est stable et sans sus-décalage. Le test au lit n'a pas d'algorithme validé dans la revue de 2024." + S(2)),
        P(f"Échocardiographie si le diagnostic reste trouble : trouble segmentaire, péricarde, cœur droit, aorte, valve. Elle ne retarde pas une coronarographie immédiate." + S(3)),
        P(f"Créatine kinase, potassium et créatinine si le muscle est en cause. Ils ne remplacent pas la troponine si le thorax est le problème."),
        P(f"Le {sca} et l'{ecg} se comparent. Un seul des deux ne nomme pas {nom}."),
    ]))
    pieges = fen(f"w{n}-pieges", "Pièges d'examen", """
<details class="quiz"><summary>Le résultat anormal est-il déjà le diagnostic ?</summary>
<p>Non. C'est une lésion ou une enzyme. Le diagnostic de cette page demande la clinique qui lui correspond.</p></details>
<details class="quiz"><summary>Où sont les neuf autres causes ?</summary>
<p>Dans la Phase A et dans les autres fichiers. Ce fichier ne les remplace pas. Il ne les contredit pas.</p></details>
<details class="quiz"><summary>Une dose sans numéro d'autorisation est-elle admise ?</summary>
<p>Non. Si ce fichier donne des milligrammes, le numéro suisse est à côté, et la phrase vient de l'information professionnelle relue le 31.10.2026.</p></details>
<details class="quiz"><summary>Le rang d'exclusion est-il la fréquence ?</summary>
<p>Non. Aucune source lue ne donne la part suisse de chacune des dix causes.</p></details>
""")
    points = []
    titres = [
        (1, "c", "1. Définition", f"{nom} se définit par son mécanisme, pas par le dépassement d'une limite de laboratoire. La limite dit la lésion. Ce fichier dit quand cette lésion, ou cette enzyme, porte ce nom."),
        (2, "v", "2. Épidémiologie", "Les chiffres utiles sont dans la fenêtre, avec leur année. Aucune prévalence suisse de cette cause parmi les enzymes anormales n'a été lue. On ne la fabrique pas."),
        (3, "c", "3. Physiopathologie", "Le rappel de sciences est celui qui change le geste : membrane, débit, inflammation, muscle squelettique ou aorte. Il est développé dans la fenêtre, pas dans une formule."),
        (4, "v", "4. Démarche diagnostique", "On part de la Phase A. On entre dans ce diagnostic quand les autres urgences qui se voient plus vite ont été regardées, surtout le sus-décalage et la dissection si la douleur le suggère."),
        (5, "c", "5. Anamnèse", "Début, siège, effort, dyspnée, syncope, trauma, infection, urines, médicaments, rein connu. Le détail qui oriente vers ce diagnostic est dans la fenêtre."),
        (6, "v", "6. Examen physique", "Signes vitaux, deux bras, poumons, cœur, jambes, muscles, abdomen, neurologie. L'examen de cette cause est dans la fenêtre, pas un catalogue général recopié."),
        (7, "c", "7. Approche syndromique", "Le syndrome qui mène ici se distingue du sus-décalage nu, de la valeur plate du rein, et de la créatine kinase isolée du muscle. La fenêtre dit lequel de ces tableaux colle."),
        (8, "v", "8. Diagnostic positif", "On affirme ce diagnostic avec la clinique, le tracé et, selon la cause, l'image ou la cinétique. Un seul chiffre au-dessus de la limite ne suffit pas."),
        (9, "c", "9. Examens complémentaires", "Les examens s'ouvrent dans la fenêtre : principe, ce qu'ils montrent, ce qu'ils ne montrent pas."),
        (10, "v", "10. Arbre décisionnel", "L'arbre du lot est dans la Phase A. Ici, la branche de ce diagnostic dit quand on s'y arrête et quand on en sort."),
        (11, "c", "11. Prise en charge en Suisse", "Le geste suisse est dans la fenêtre. Les milligrammes, s'il y en a, citent l'information professionnelle. Sinon, le cours dit qu'aucune dose n'a été recopiée."),
        (12, "v", "12. Prévention", "On prévient la récidive de cette cause, pas le chiffre. Pas de dépistage de troponine chez une personne sans symptôme."),
        (13, "c", "13. Points clés", f"Retenir le mécanisme de {nom}, le geste qui ne peut pas attendre, et la confusion avec le type 1 ou avec le muscle."),
        (14, "v", "14. Pièges d'examen", "Quatre questions suffisent. Elles sont dans la fenêtre. La réponse fausse habituelle est de traiter le chiffre comme la maladie."),
    ]
    blocs = [ess, som]
    for i, cls, titre, phrase in titres:
        inner = P(phrase, b(f"w{n}-coeur", "voir le détail"))
        if i == 1:
            inner += coeur + exam + pieges
        blocs.append(ilot(f"p{i}", cls, titre, inner))
    blocs.append(ilot("sources", "c", "Sources", """<ol class="sources">
<li>Revue Médicale Suisse 2019, n° 652, troponine sans infarctus.</li>
<li>Revue Médicale Suisse 2024, n° 875, syndrome coronarien aigu.</li>
<li>Revue Médicale Suisse 2016, n° 535, rein et troponine.</li>
<li>Revue Médicale Suisse 2020, n° 696, myocardite.</li>
<li>Revue Médicale Suisse 2009, n° 221, embolie et biomarqueurs.</li>
<li>Revue Médicale Suisse 2021, n° 728, tako-tsubo.</li>
<li>Revue Médicale Suisse 2020, n° 716, rhabdomyolyse.</li>
<li>AIPS Aspirine Cardio n° 51795.</li>
<li>AIPS BRILIQUE n° 61389.</li>
<li>AIPS Plavix n° 54509.</li>
<li>AIPS EFIENT n° 59136.</li>
<li>AIPS Sortis n° 54085.</li>
</ol>"""))
    nom_fichier = f"LOT_150_Phase_B_V0_DX.{n}.html"
    return page(
        nom_fichier,
        nom,
        sous,
        blocs,
        h2_dx=f"DX.{n} — {nom}",
    )


def main() -> None:
    n = int(sys.argv[1])
    html = construire(n)
    dest = OUT_DIR / f"LOT_150_Phase_B_V0_DX.{n}.html"
    dest.write_text(html, encoding="utf-8")
    print(dest, dest.stat().st_size)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase A LOT_103 — générateur. Phrases verbales 12–28 mots, chiffres cités, zéro dose en mg."""
import html, re, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "LOT_103_Phase_A_V0.html"

def c(*ids):
    return "".join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)

# Passages réellement lus (chiffres recopiés). Le paquet sert au contrôle --paquet.
P = {}
def passage(i, texte, url, date, organisme):
    P[i] = {"texte": texte, "url": url, "date": date, "organisme": organisme}

passage("iasp",
        "The following pain terminology was first published in 1979. We now present the 2011 version of IASP Pain Terminology, updated from the 1994 list. "
        "HYPOESTHESIA Decreased sensitivity to stimulation, excluding the special senses. HYPERESTHESIA Increased sensitivity to stimulation, excluding the special senses. "
        "PARESTHESIA An abnormal sensation, whether spontaneous or evoked. DYSESTHESIA An unpleasant abnormal sensation, whether spontaneous or evoked. "
        "HYPERALGESIA Increased pain from a stimulus that normally provokes pain. HYPOALGESIA Diminished pain in response to a normally painful stimulus.",
        "https://www.iasp-pain.org/resources/terminology/", "2026-11-15",
        "International Association for the Study of Pain, taxonomie 2011 (révisée depuis 1979 et 1994)")
passage("rmsnp",
        "Les polyneuropathies sont une pathologie commune, touchant environ 3 à 4% des personnes âgées de plus 55 ans. L'incidence estimée aux Pays-Bas est de 77 pour 100 000 personnes. "
        "La polyneuropathie distale et symétrique est l'atteinte la plus fréquente. Le diabète constitue de loin la cause la plus commune, expliquant 30 à 40% des cas. "
        "Dans environ 30% des cas de neuropathie chronique, aucune étiologie spécifique n'est retrouvée. "
        "Celle-ci touche 30 à 50 % des diabétiques de type 2 et jusqu'à 50-60 % des diabétiques de type 1. Dans 25 % des cas, l'atteinte se manifeste par des douleurs. "
        "Chez les patients diabétiques, une étiologie alternative est présente dans 53 % des cas. "
        "La neuropathie alcoolique résulte d'une consommation à risque (> 30 g/jour, ou selon l'OMS 3 verres/jour pour un homme et 2 verres/jour pour une femme). "
        "60 % des patients sous chimiothérapie présentent une neuropathie qui devient chronique dans 30 % des cas. "
        "La limite inférieure au doigt/orteil est de 6,9/5,5 entre 20-39 ans et de 6,2/4,7 entre 40-60 ans. "
        "La production d'une immunoglobuline monoclonale s'observe chez 3 à 4% de la population de plus de 50 ans. "
        "Jusqu'à 90% des patients avec insuffisance rénale terminale développent une polyneuropathie urémique. "
        "Une polyneuropathie distale peut s'observer jusque dans 30% des cas d'infection chronique. "
        "Les signes sensitifs positifs incluent les paresthésies (picotements ou fourmillements) et dysesthésies. Les signes négatifs sont l'hypoesthésie et les troubles de l'équilibre. "
        "La pallesthésie, le sens de position et le toucher fin évaluent le sens épicritique. La douleur et la température évaluent le sens protopathique. "
        "Une étude de la conduction nerveuse est réservée aux présentations atypiques et/ou sans cause claire. "
        "Les symptômes neurologiques peuvent apparaître en l'absence d'anémie macrocytaire. Une récupération neurologique s'observe entre 6 semaines et 3 mois. "
        "Les vasculites s'expriment par une mononévrite multiple aiguë ou subaiguë. Leur suspicion doit entraîner des investigations rapides.",
        "https://www.revmed.ch/revue-medicale-suisse/2019/revue-medicale-suisse-672/prise-en-charge-des-neuropathies-peripheriques-en-medecine-interne-generale",
        "2026-11-15", "Bernard-Valnet, Kuntzer, Vaucher. Revue médicale suisse, 20 novembre 2019")
passage("rmsage",
        "Les polyneuropathies sensitives sont observées chez environ 30 % des personnes âgées. Leur prévalence, estimée à environ 8 % chez les patients après 55 ans en cabinet, s'élève jusqu'à 28 % entre 70 et 79 ans et peut atteindre 35 % après 80 ans. "
        "Le diabète est la cause la plus fréquente de PNP, avec une prévalence estimée de 30 %. Les patients présentant une intolérance au glucose ont une prévalence de PNP plus élevée que la population générale (11-25 vs 7,1 %). "
        "Douleurs neuropathiques (prévalence de 20 % après 10 ans d'évolution du diabète de type 2). "
        "Une étude de 2290 patients âgés de 70 à 79 ans : la prévalence de la PNP était de 42 % et pouvait atteindre 70 % en cas d'insuffisance rénale terminale. "
        "La prévalence de la PNP en cas de MGUS varie de 8 à 36 %. Une gammapathie monoclonale peut être retrouvée jusqu'à 10 % des cas. "
        "Les rares vasculites se manifestent souvent (77 %) par une PNP ou une mononeuropathie multiple. "
        "17,5 % de biopsie diagnostique. IRC stade G3a : DFG 49 ml/min. Vignette : 77 ans, Hb 108 g/l, MCV 101 fl, réticulocytes 35 G/l, vitamine B12 100 pmol/l, HbA1c de 8 %. "
        "GFR < 60 ml/min ; GFR < 15 ml/min. Dans près d'un tiers des cas des formes chroniques, aucune cause n'est retrouvée. "
        "Un dépistage annuel de la PNP (pallesthésie, test au monofilament) et un examen rigoureux des pieds sont recommandés.",
        "https://www.revmed.ch/revue-medicale-suisse/2019/revue-medicale-suisse-632/polyneuropathies-du-sujet-age",
        "2026-11-15", "Revue médicale suisse 2019, polyneuropathies du sujet âgé (texte lu dans le dossier d'extraits)")
passage("rmshdc",
        "Plus de 90% des patients présentant une radiculopathie secondaire à une HDC voient leurs symptômes s'amender sans chirurgie. "
        "La myélopathie cervicale symptomatique pose per se l'indication à une prise en charge chirurgicale. "
        "Dans leur septième décennie, 85% des patients sont porteurs de modifications cervicales radiologiques, la plupart du temps asymptomatiques. "
        "La prévalence des cervicobrachialgies est de 83,2/100 000 personnes. Les hommes sont plus fréquemment touchés (ratio H : F = 1,6 : 1). "
        "L'incidence globale des cervicalgies est de 15% par an ; elle s'élève à 23,1 cas par 1000 personnes-année. "
        "Seul 0,6% des patients rapporte des symptômes fonctionnels invalidants ; 25% décrivent un traumatisme cervical. "
        "La radiculopathie cervicale vraie a une prévalence de 3,3 cas par 1000 personnes. Une monoradiculopathie C7 semble la plus fréquente, suivie de la racine C6. "
        "Plus de 90% des maladies discales cervicales symptomatiques intéressent C5-C6 et C6-C7. "
        "Un geste chirurgical est proposé si les douleurs sont mal contrôlées par le traitement non chirurgical bien mené pour une durée de six à huit mois.",
        "https://www.revmed.ch/revue-medicale-suisse/2015/revue-medicale-suisse-492/hernie-discale-cervicale-diagnostic-et-prise-en-charge",
        "2026-11-15", "Schaller. Revue médicale suisse, 25 novembre 2015")
passage("ulg",
        "Syndrome du canal carpien. prévalence entre 3 et 5%. De loin la neuropathie tronculaire focale la plus fréquente. "
        "Test de compression carpienne (30 secondes) : sensibilité 87%, spécificité 90%. "
        "Déficit sensitif absent chez 20-50% des patients. Ténosynovite des fléchisseurs dans la PR (23-70% des patients).",
        "https://www.chuliege.be/", "2026-11-10",
        "Cours d'électroneuromyographie, Université de Liège, syndromes canalaires (extrait lu le 10 novembre 2026)")
passage("atroshi",
        "Of the 2466 responders, 354 reported pain, numbness, and/or tingling in the median nerve distribution (prevalence, 14.4%; 95% CI, 13.0%-15.8%). "
        "Clinically certain CTS (prevalence, 3.8%; 95% CI, 3.1%-4.6%). Electrophysiological median neuropathy (prevalence, 4.9%; 95% CI, 4.1%-5.8%). "
        "Clinically and electrophysiologically confirmed CTS (prevalence, 2.7%; 95% CI, 2.1%-3.4%). "
        "Of 125 control subjects, electrophysiological median neuropathy was found in 23 (18.4%; 95% CI, 12.0%-26.3%). "
        "Age range 25-74 years. Response rate of 83%. Southern Sweden, survey February 1997, published 1999. Sample of 3000 subjects. Region population of 170000.",
        "https://jamanetwork.com/journals/jama/fullarticle/774263", "2026-11-15",
        "Atroshi et coll., population du sud de la Suède, JAMA 1999 (donnée européenne, pas une recommandation américaine)")
passage("obsandiab",
        "En 2022, 6,2% de la population en Suisse déclarait avoir reçu un diagnostic de diabète ou prendre des médicaments contre cette maladie. "
        "Intervalle de confiance 5,8 à 6,6. Femmes 5,6% (5,1 à 6,1). Hommes 6,9%. En 2017 la proportion était de 4,8%. "
        "Femmes de 4,5% à 5,6%, hommes de 5,1% à 6,9%. n = 21906. Source OFS, Enquête suisse sur la santé, indicateur MonAM, page lue le 15 novembre 2026. "
        "75 ans et plus : 15,4%.",
        "https://ind.obsan.admin.ch/fr/indicator/monam/diabete-age-15", "2026-11-15",
        "Obsan / OFS, Enquête suisse sur la santé 2022, indicateur MonAM diabète")
passage("ofsavc",
        "En 2023, les nombres pour les attaques cérébrales sont de 22517 (12132 hommes et 10385 femmes) et de 2580 décès. "
        "En 2022, 21797 attaques cérébrales (11821 hommes et 9976 femmes) et 2535 décès. OFS, statistique de la santé, publication 2025, page lue le 15 novembre 2026.",
        "https://dam-api.bfs.admin.ch/hub/api/dam/assets/34027818/master", "2026-11-15",
        "Office fédéral de la statistique, Santé, chiffres 2023")
passage("obsanavc",
        "Incidence standardisée 249,4 pour 100 000 (intervalle 247,9 à 251,0), taux brut 249,5, moyenne 21729 cas par an, période 2019-2023. "
        "Létalité 12,2 % (intervalle 12,0 à 12,4), moyenne 2651 décès par an. Population standard européenne 2010. Page Obsan lue le 15 novembre 2026.",
        "https://ind.obsan.admin.ch/indicator/obsan/hirnschlag", "2026-11-15",
        "Obsan, indicateur attaque cérébrale, moyenne 2019-2023")
passage("mssuisse",
        "L'estimation du nombre de personnes atteintes de SEP en Suisse pour l'année 2021 est de 18000 personnes. "
        "La dispersion va de 17400 à 18700 personnes. Le rapport femmes/hommes est de 2,7 femmes pour 1 homme. "
        "En 2016, ce nombre avait été estimé à 15000. Le nombre a augmenté de 20% environ. Environ un cinquième de cette hausse est lié à la croissance de la population. "
        "73% sont des femmes, 27% des hommes. Article de la Société suisse de la SEP du 27 janvier 2024, page lue le 15 novembre 2026. "
        "L'estimation 2016 du Registre suisse était de 14650 à 15700 personnes, soit 174 à 187 pour 100000.",
        "https://www.multiplesklerose.ch/fr/actualite/detail/nouvelle-extrapolation-18000-personnes-atteintes-de-sep-en-suisse/",
        "2026-11-15", "Société suisse de la sclérose en plaques et Registre suisse de la SEP")
passage("gbses",
        "Nationwide hospital incidence was 1.78 in 2018, 1.71 in 2019, 1.41 in 2020 and 1.66 in 2021 per 100000. "
        "The average incidence of GBS in Spain for 2018-2021 was 1.67 cases per 100000 population. "
        "Eleven per cent (11 %) of GBS patients needed ventilatory support. 63.9% of patients were male. The mean age was 53.2 years. "
        "Male incidence 2.18 and female incidence 1.18 per 100000. Highest incidence at 70-79 years: 3.26.",
        "https://onlinelibrary.wiley.com/doi/full/10.1111/ene.16439", "2026-11-15",
        "Étude nationale espagnole, European Journal of Neurology, 2024")
passage("gbsuk",
        "The incidence of GBS treated in UK hospitals from 2016 to 2019 was 1.65-1.88 per 100 000 individuals per year.",
        "https://www.ean.org/research/resources/knowledge-distillery/detail/epidemiological-and-cohort-study-finds-no-association-between-covid-19-and-guillain-barre-syndrome",
        "2026-11-15", "European Academy of Neurology, fiche de Keddie et coll. sur l'incidence britannique 2016-2019")
passage("openstax",
        "OpenStax Anatomy and Physiology, figure of a thoracic spinal cord cross-section, published 18 May 2016, license CC BY 4.0. "
        "Micrograph LM × 40 provided by the Regents of the University of Michigan Medical School 2012. "
        "Labels: posterior horn, lateral horn, anterior horn, posterior columns, lateral columns, anterior columns, central canal. Wikimedia file 1313 Spinal Cord Cross Section.jpg.",
        "https://commons.wikimedia.org/wiki/File:1313_Spinal_Cord_Cross_Section.jpg", "2026-11-15",
        "OpenStax, Anatomy and Physiology, CC BY 4.0, via Wikimedia Commons")

ITEMS = []  # (point, frag)
CUR = ["p1"]

def use(p):
    CUR[0] = p

def _frag(text, ids):
    text = re.sub(r"\s+", " ", text).strip()
    if text.endswith("."):
        text = text[:-1]
    return text + (c(*ids) if ids else "") + "."

def s(text, *ids):
    frag = _frag(text, ids)
    ITEMS.append((CUR[0], frag))
    return frag

def seul(text, *ids):
    return _frag(text, ids)

def mots(frag):
    t = re.sub(r"<sup class=\"r\">.*?</sup>", "", frag, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"\s+", " ", t).strip()
    return t, t.split()

def verifier_phrases(frags):
    err = []
    vus = {}
    for frag in frags:
        t, w = mots(frag)
        n = len(w)
        if not (12 <= n <= 28):
            err.append(f"LONGUEUR {n} :: {t}")
        if re.search(r"\d", t) and "href=\"#sb-" not in frag:
            err.append(f"CHIFFRE SANS CITATION :: {t}")
        if re.search(r"\b\d+(?:[.,]\d+)?\s?(?:mg|µg|mcg)\b", t, re.I):
            err.append(f"DOSE :: {t}")
        k = re.sub(r"\W+", "", t.lower())
        if len(t) > 60:
            if k in vus:
                err.append(f"DOUBLON :: {t[:110]}")
            vus[k] = 1
    return err

# ---------- Phrases (une idée, un verbe, un connecteur) ----------
# Point 1 — définition seule
s("L'International Association for the Study of Pain (IASP) définit l'hypoesthésie comme une sensibilité diminuée à la stimulation, hors sens spéciaux, car le lieu doit être précisé", "iasp")
s("La même taxonomie de deux mille onze définit l'hyperesthésie comme une sensibilité augmentée à la stimulation, hors sens spéciaux, car le stimulus doit être nommé", "iasp")
s("Elle définit la paresthésie comme une sensation anormale, spontanée ou provoquée, car le terme ne doit pas décrire une sensation désagréable", "iasp")
s("Elle définit la dysesthésie comme une sensation anormale désagréable, spontanée ou provoquée, car la frontière avec la paresthésie reste clinique", "iasp")
s("Elle définit l'hyperalgésie comme une douleur augmentée après un stimulus qui provoque déjà une douleur, car le mode du stimulus ne change pas", "iasp")
s("Elle définit l'hypoalgésie comme une douleur diminuée après un stimulus normalement douloureux, car ce terme ne couvre plus toute baisse de sensibilité", "iasp")
s("Un trouble de la sensibilité est donc présent lorsqu'un de ces six phénomènes est constaté, car la situation de soins les rassemble sous un seul motif", "iasp")
s("La définition reste clinique et ne désigne pas un mécanisme, car la société savante sépare le phénomène décrit de son interprétation physiopathologique", "iasp")

# Point 2 — épidémiologie
use("p2")
s("Aucune série suisse unique ne classe les causes d'un trouble de la sensibilité, car les chiffres lus mesurent des populations et des dénominateurs différents", "rmsnp")
s("Environ 3 à 4 % des personnes de plus de cinquante-cinq ans ont une polyneuropathie, car la fréquence augmente avec l'âge", "rmsnp")
s("Le même article estime l'incidence aux Pays-Bas à 77 pour 100 000 personnes, car cette donnée européenne fixe un ordre de grandeur hors Suisse", "rmsnp")
s("Un second article suisse de la même année estime la prévalence à environ 8 % après cinquante-cinq ans en cabinet, car le lieu de recrutement change le chiffre", "rmsage")
s("Cet article décrit jusqu'à 28 % de polyneuropathies entre soixante-dix et soixante-dix-neuf ans, car la prévalence continue de croître dans le grand âge", "rmsage")
s("Il décrit jusqu'à 35 % après quatre-vingts ans, car le risque de chute devient alors un enjeu de santé publique", "rmsage")
s("Les polyneuropathies sensitives concernent environ 30 % des personnes âgées dans cet article, car le motif sensitif domine le tableau du sujet âgé", "rmsage")
s("Le diabète explique 30 à 40 % des polyneuropathies dans la mise au point de médecine interne, car il est de loin la cause la plus commune", "rmsnp")
s("La neuropathie touche 30 à 50 % des diabétiques de type deux, car le contrôle glycémique n'efface pas une atteinte souvent déjà installée", "rmsnp")
s("Elle touche jusqu'à 50 à 60 % des diabétiques de type un, car la durée d'exposition à l'hyperglycémie y est souvent plus longue", "rmsnp")
s("Dans 25 % des cas la neuropathie diabétique est douloureuse, car la douleur pèse alors sur la qualité de vie et le risque de plaie", "rmsnp")
s("Après dix ans de diabète de type deux, la douleur neuropathique a une prévalence de 20 % dans l'article du sujet âgé, car la durée compte", "rmsage")
s("En Suisse, 6,2 % des personnes de quinze ans et plus déclaraient un diabète en deux mille vingt-deux, car l'enquête fédérale sur la santé fournit ce taux", "obsandiab")
s("L'intervalle de confiance à quatre-vingt-quinze pour cent va de 5,8 à 6,6 %, car l'indicateur MonAM publie les bornes et non un chiffre isolé", "obsandiab")
s("Le taux déclaré était de 5,6 % chez les femmes et de 6,9 % chez les hommes, car l'écart entre sexes est déjà visible avant les complications", "obsandiab")
s("La proportion était de 4,8 % en deux mille dix-sept, car la hausse entre les deux enquêtes est documentée par le même indicateur", "obsandiab")
s("Chez les femmes le taux est passé de 4,5 à 5,6 %, tandis que chez les hommes il est passé de 5,1 à 6,9 %", "obsandiab")
s("L'échantillon national comptait 21 906 répondants, car la précision du taux dépend de cette base", "obsandiab")
s("Après soixante-quinze ans, 15,4 % déclaraient un diabète, car l'âge concentre à la fois le diabète et la neuropathie", "obsandiab")
s("Le syndrome du canal carpien est de loin la neuropathie tronculaire focale la plus fréquente, car le cours liégeois d'électroneuromyographie le place en tête des atteintes focales", "ulg")
s("Ce cours situe sa prévalence entre 3 et 5 %, car cette fourchette recoupe les mesures européennes de population", "ulg")
s("Dans le sud de la Suède, 14,4 % des adultes décrivaient des symptômes dans le territoire du nerf médian, car l'enquête les a comptés", "atroshi")
s("L'intervalle de cette prévalence symptomatique allait de 13,0 à 15,8 %, car l'étude publie la borne et non seulement le point", "atroshi")
s("Le canal carpien cliniquement certain y avait une prévalence de 3,8 %, car l'examen a retenu quatre-vingt-quatorze sujets symptomatiques", "atroshi")
s("L'intervalle de cette prévalence clinique allait de 3,1 à 4,6 %, car le classement clinique reste plus large que le classement confirmé", "atroshi")
s("La neuropathie médiane électrophysiologique symptomatique atteignait 4,9 %, avec un intervalle de 4,1 à 5,8 %", "atroshi")
s("La forme à la fois clinique et électrophysiologique atteignait 2,7 %, avec un intervalle de 2,1 à 3,4 %", "atroshi")
s("Parmi cent vingt-cinq témoins examinés, 18,4 % avaient une neuropathie médiane électrophysiologique, car un ralentissement sans plainte existe", "atroshi")
s("L'intervalle chez ces témoins allait de 12,0 à 26,3 %, car le petit effectif élargit la borne", "atroshi")
s("L'enquête a interrogé un échantillon de 3 000 adultes et obtenu 2 466 réponses, soit un taux de réponse de 83 %", "atroshi")
s("La région comptait 170 000 habitants, car la prévalence est rapportée à une population générale européenne et non à une file de soins", "atroshi")
s("La radiculopathie cervicale vraie a une prévalence de 3,3 cas pour 1 000 personnes, car la Revue médicale suisse de deux mille quinze la distingue des simples cervicalgies", "rmshdc")
s("Les cervicobrachialgies ont une prévalence de 83,2 pour 100 000, car ce chiffre dépasse celui de la radiculopathie confirmée", "rmshdc")
s("Les hommes sont plus touchés, avec un rapport de 1,6 homme pour une femme, car la revue le rapporte pour la hernie cervicale", "rmshdc")
s("L'incidence des cervicalgies est de 15 % par an, soit 23,1 cas pour 1 000 personnes-année, car le pic siège aux quatrième et cinquième décennies", "rmshdc")
s("Seul 0,6 % des patients décrit des symptômes invalidants, tandis que 25 % rapportent un traumatisme cervical", "rmshdc")
s("Dans la septième décennie, 85 % des personnes portent des modifications cervicales radiologiques, car la plupart restent asymptomatiques", "rmshdc")
s("La Société suisse de la sclérose en plaques retient 18 000 personnes atteintes en Suisse pour deux mille vingt et un", "mssuisse")
s("La fourchette va de 17 400 à 18 700 personnes, car l'extrapolation publie une dispersion et non un compte exact", "mssuisse")
s("Le rapport est de 2,7 femmes pour un homme, car la hausse récente est surtout portée par les femmes de moins de soixante ans", "mssuisse")
s("Le magazine de la société précise 73 % de femmes et 27 % d'hommes, car ces parts décrivent le même déséquilibre", "mssuisse")
s("En deux mille seize, l'estimation était de 15 000 personnes, et le nombre a augmenté d'environ 20 % ensuite", "mssuisse")
s("Environ un cinquième de cette hausse tient à la croissance de la population, car le reste ne se résume pas au dénombrement", "mssuisse")
s("Le registre estimait pour deux mille seize entre 14 650 et 15 700 personnes, soit 174 à 187 pour 100 000", "mssuisse")
s("En deux mille vingt-trois, l'Office fédéral de la statistique a compté 22 517 attaques cérébrales, car le chiffre joint les hospitalisations et les décès", "ofsavc")
s("Ce total réunit 12 132 hommes et 10 385 femmes, tandis que 2 580 personnes en sont mortes la même année", "ofsavc")
s("En deux mille vingt-deux, le décompte était de 21 797 attaques, dont 11 821 hommes et 9 976 femmes", "ofsavc")
s("Les décès par attaque cérébrale étaient de 2 535 en deux mille vingt-deux, car la létalité reste un enjeu national", "ofsavc")
s("L'Obsan mesure, sur deux mille dix-neuf à deux mille vingt-trois, une incidence standardisée de 249,4 pour 100 000", "obsanavc")
s("L'intervalle va de 247,9 à 251,0, le taux brut est de 249,5 et la moyenne annuelle est de 21 729 cas", "obsanavc")
s("La létalité moyenne est de 12,2 %, avec un intervalle de 12,0 à 12,4 %, soit 2 651 décès par an", "obsanavc")
s("La part des attaques qui s'expriment seulement par un trouble sensitif n'est pas isolée par ces sources, car le rang vasculaire reste donc un rang d'enveloppe", "ofsavc")
s("En Espagne, l'incidence hospitalière du syndrome de Guillain-Barré était de 1,78 pour 100 000 en deux mille dix-huit", "gbses")
s("Elle était de 1,71 en deux mille dix-neuf, de 1,41 en deux mille vingt et de 1,66 en deux mille vingt et un", "gbses")
s("La moyenne espagnole de deux mille dix-huit à deux mille vingt et un est de 1,67 pour 100 000, car cette maladie reste rare", "gbses")
s("Onze pour cent des patients ont eu besoin d'une assistance ventilatoire, car la menace respiratoire justifie le rang d'exclusion", "gbses")
s("Les hommes représentaient 63,9 % des cas, l'âge moyen était de 53,2 ans, et l'incidence masculine était de 2,18 pour 100 000", "gbses")
s("L'incidence féminine était de 1,18 pour 100 000, et le pic de 3,26 pour 100 000 siégeait entre soixante-dix et soixante-dix-neuf ans", "gbses")
s("Au Royaume-Uni, l'incidence des formes traitées à l'hôpital était de 1,65 à 1,88 pour 100 000 et par an entre deux mille seize et deux mille dix-neuf", "gbsuk")
s("Environ 30 % des neuropathies chroniques restent sans cause dans la mise au point suisse, car le bilan de première ligne ne ferme pas tous les dossiers", "rmsnp")
s("Dans près d'un tiers des formes chroniques du sujet âgé, aucune cause n'est retenue, car les deux articles suisses se rejoignent sur cette part", "rmsage")
s("Une étiologie autre que le diabète est présente dans 53 % des neuropathies chez des patients diabétiques, car une cause évidente ne dispense pas du bilan de base", "rmsnp")
s("L'intolérance au glucose s'associe à une polyneuropathie chez 11 à 25 % des personnes, contre 7,1 % dans la population générale de l'étude citée", "rmsage")
s("Jusqu'à 90 % des patients en insuffisance rénale terminale développent une neuropathie urémique selon la mise au point de médecine interne", "rmsnp")
s("L'article du sujet âgé décrit 42 % de polyneuropathies chez 2 290 personnes de soixante-dix à soixante-dix-neuf ans, et jusqu'à 70 % au stade terminal", "rmsage")
s("Ces deux pourcentages d'insuffisance terminale, 90 % et 70 %, ne sont pas identiques, car ils viennent de deux articles suisses distincts", "rmsnp", "rmsage")
s("Une immunoglobuline monoclonale est présente chez 3 à 4 % des personnes de plus de cinquante ans, car ce taux n'est pas celui de la neuropathie", "rmsnp")
s("En cas de gammapathie de signification indéterminée, la neuropathie concerne 8 à 36 % des personnes selon l'article du sujet âgé", "rmsage")
s("Inversement, une gammapathie est retrouvée dans jusqu'à 10 % des polyneuropathies chroniques sans cause", "rmsage")
s("Les vasculites rares se manifestent dans 77 % des cas par une polyneuropathie ou une mononeuropathie multiple, car le nerf est un organe cible fréquent", "rmsage")
s("Une polyneuropathie distale s'observe jusque dans 30 % des infections chroniques par le virus de l'immunodéficience humaine, car ce dénominateur est restreint aux personnes infectées", "rmsnp")
s("Soixante pour cent des patients sous chimiothérapie présentent une neuropathie, et elle devient chronique dans 30 % des cas", "rmsnp")
s("La consommation d'alcool à risque dépasse 30 grammes par jour, ou trois verres chez l'homme et deux verres chez la femme selon l'Organisation mondiale de la santé", "rmsnp")

FEN = []
TABS = []
CHECK = []

def L(fid, mot):
    return f'<a class="ouvre" href="#{fid}">{mot}</a>'

def fen(point, fid, titre, phrases):
    CHECK.extend(phrases)
    body = "".join(f'<div class="p">{p}</div>' for p in phrases)
    FEN.append((point, fid, (
        f'<section class="fenetre" id="{fid}" role="dialog" aria-label="{html.escape(titre)}">'
        f"<h4>{titre}</h4>{body}"
        + ('<figure><img src="images/moelle-coupe-openstax.jpg" alt="Coupe transversale de moelle thoracique, schéma coloré et lame histologique"><figcaption>OpenStax, Anatomy and Physiology, licence CC BY. Lame des Régents de l\'Université du Michigan. Fichier Wikimedia consulté le quinze novembre deux mille vingt-six.</figcaption></figure>' if fid == "f-moelle" else "")
        + '<p><a class="fermer" href="#">Fermer</a></p></section>'
    )))

def tableau(point, titre, entetes, lignes):
    th = "".join(f"<th>{html.escape(x)}</th>" for x in entetes)
    trs = []
    for ligne in lignes:
        trs.append("<tr>" + "".join(f"<td>{cellule}</td>" for cellule in ligne) + "</tr>")
    TABS.append((point, f'<div class="t" style="overflow-x:auto"><table><caption>{titre}</caption><thead><tr>{th}</tr></thead><tbody>{"".join(trs)}</tbody></table></div>'))

def assembler(items, passages):
    titres = {
        1: "Définition",
        2: "Épidémiologie en Suisse, puis en Europe",
        3: "Physiopathologie",
        4: "Démarche diagnostique",
        5: "Anamnèse ciblée et drapeaux rouges",
        6: "Examen physique ciblé, région par région",
        7: "Approche syndromique",
        8: "Diagnostic positif et critères",
        9: "Examens complémentaires",
        10: "Arbre décisionnel",
        11: "Prise en charge selon les recommandations suisses",
        12: "Prévention",
        13: "Points clés",
        14: "Pièges et questions fréquentes à l'examen fédéral",
    }
    by = {}
    for p, frag in items:
        by.setdefault(p, []).append(frag)
    nav = ['<nav id="brain-barre14" aria-label="Plan">']
    for i, titre in titres.items():
        nav.append(f'<a href="#pa-p{i}"><b>{i}</b> {html.escape(titre)}</a>')
    nav.append("</nav>")
    blocs = []
    for i, titre in titres.items():
        paras = "".join(f'<div class="p">{frag}</div>' for frag in by.get(f"p{i}", []))
        tabs = "".join(h for pt, h in TABS if pt == f"p{i}")
        fens = "".join(h for pt, fid, h in FEN if pt == f"p{i}")
        blocs.append(
            f'<section class="ilot" id="pa-p{i}"><h3 id="pa-h{i}"><strong>{i}. {titre}</strong></h3>'
            f"{paras}{tabs}{fens}</section>"
        )
    sources = ['<section class="ilot" id="pa-sources"><h3>Sources citées</h3><ol>']
    for i, meta in passages.items():
        sources.append(
            f'<li id="sb-{i}">{html.escape(meta["organisme"])}. {html.escape(meta["url"])} '
            f'(consulté le {html.escape(meta["date"])}).</li>'
        )
    sources.append("</ol><p class=\"p\">Le contenu reprend les sources citées et n'a pas été validé cliniquement par un médecin.</p></section>")
    css = """
:root{--fm-fond:#fff;--fm-encre:#0b0b0b}
html,body{background:#fff;color:#0b0b0b}
body{margin:0;padding:0 24px 4rem 300px;font-size:17px;line-height:1.42}
main{max-width:60vw}
h2{color:#5c242f}h3,h4{color:#7a3410}
a.ouvre{color:#7a3410;font-weight:700}
.fenetre{display:none}
.fenetre:target{display:block;position:fixed;z-index:200;top:50%;left:50%;transform:translate(-50%,-50%);
width:min(860px,94vw);max-height:86vh;overflow:auto;background:#fff;color:#0b0b0b;
border-top:6px solid #5c242f;border-radius:14px;padding:22px 26px;
box-shadow:0 0 0 100vmax rgba(20,16,12,.62),0 24px 60px rgba(0,0,0,.45)}
.ilot{background:#fff;border:1px solid #e7d5d8;border-radius:12px;padding:12px 16px;margin:14px 0}
table{border-collapse:collapse;width:100%}
th{background:#5c242f;color:#fff;text-align:left;padding:6px 8px}
td{border-bottom:1px solid #eadfe1;padding:6px 8px;vertical-align:top}
.t{overflow-x:auto}
img{max-width:100%;height:auto}
.freq{color:#8f1d2c;font-weight:700}
"""
    return f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>S7.9 Troubles de la sensibilité — Phase A</title>
<link id="forme-vial" rel="stylesheet" href="../../Claude/_polices/forme.css">
<style>{css}</style>
<script src="../../Claude/_polices/forme.js" defer></script>
</head><body style="--fm-a:#5c242f;--fm-a-mid:#984959;--fm-a-pale:#faf3f4;--fm-a-doux:#f1e2e5;background:#fff">
{''.join(nav)}
<header id="fm-bandeau"><div class="fm-code"><span>LOT_103 · SSP S7.9</span><span class="fm-phase">Phase A · situation clinique de départ</span></div>
<div class="fm-nom">Troubles de la sensibilité</div></header>
<main>
<h2>Troubles de la sensibilité</h2>
<p class="p">La Phase A fixe les dix diagnostics qui concurrencent ce motif, car l'ordre de fréquence et les rangs d'exclusion commandent la suite.</p>
{''.join(blocs)}
{''.join(sources)}
</main></body></html>
<!-- FIN_FICHIER LOT_103_Phase_A_V0 -->
"""

exec(open(pathlib.Path(__file__).with_name("phrases_suite.py"), encoding="utf-8").read(), globals())
frags = [f for _, f in ITEMS] + CHECK
erreurs = verifier_phrases(frags)
print("phrases", len(frags), "erreurs", len(erreurs))
for e in erreurs[:40]:
    print(e)
if erreurs:
    raise SystemExit(1)
html_out = assembler(ITEMS, P)
OUT.write_text(html_out, encoding="utf-8")
paq = {"passages": [{"id": i, "texte": m["texte"]} for i, m in P.items()]}
pathlib.Path("/tmp/lot103_paquet.json").write_text(json.dumps(paq, ensure_ascii=False), encoding="utf-8")
print("octets", len(html_out.encode("utf-8")))

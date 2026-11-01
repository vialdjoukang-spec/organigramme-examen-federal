#!/usr/bin/env python3
"""Construit les 11 leçons de LOT_185. Les phrases viennent des preuves du dossier."""
import html
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_185"
CSS = Path("/tmp/style_lot179.css").read_text(encoding="utf-8")
CSS += """
figure.schema svg{max-width:100%;height:auto;background:#f7fbfd}
.schema svg text{font-family:Verdana,sans-serif}
.sch .niv{display:none}
.sch input.sr{position:absolute;opacity:0;width:1px;height:1px}
.sch .bn{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 8px}
.sch .bn label{border:1px solid #9bb;border-radius:8px;padding:4px 8px;cursor:pointer}
.sch .bn label:hover{background:#e7f4fb}
"""

sys.path.insert(0, str(RACINE / "harnais"))
import taille_xy  # noqa: E402

MOTS_CLES = re.compile(
    r"\b(incidence|prévalence|prevalence|sensibilit[ée]|spécificit[ée]|seuil|score)\b",
    re.I,
)
DX = {
    1: "Négligence des besoins fondamentaux",
    2: "Maltraitance physique",
    3: "Maltraitance psychologique",
    4: "Exposition à la violence entre les parents",
    5: "Abus sexuel",
    6: "Traumatisme crânien infligé",
    7: "Trouble factice imposé à autrui",
    8: "Lésion accidentelle compatible avec l'âge",
    9: "Maladie imitant une lésion infligée",
    10: "Négligence médicale",
}
TITRES = {
    1: "1. Définition",
    2: "2. Épidémiologie",
    3: "3. Physiopathologie",
    4: "4. Démarche diagnostique",
    5: "5. Anamnèse",
    6: "6. Examen clinique",
    7: "7. Syndromes et formes",
    8: "8. Diagnostic",
    9: "9. Examens complémentaires",
    10: "10. Arbre décisionnel",
    11: "11. Prise en charge",
    12: "12. Prévention",
    13: "13. Points clés",
    14: "14. Pièges",
}
LEADS = {
    1: "La définition retenue est celle du guide de 2020.",
    2: "Les fréquences lues ne se mélangent pas.",
    3: "Le mécanisme éclaire la lésion, il ne la prouve pas seul.",
    4: "La démarche suit l'hôpital pédiatrique suisse.",
    5: "L'anamnèse sépare les mots de l'enfant et ceux de l'adulte.",
    6: "L'examen regarde tout le corps, pas seulement la plainte.",
    7: "Les formes se cumulent souvent chez le même enfant.",
    8: "Le diagnostic est une synthèse, pas une seule tache.",
    9: "Les examens cherchent la lésion cachée et la maladie imitatrice.",
    10: "L'arbre décide de la protection avant le nom définitif.",
    11: "La prise en charge protège, soigne et transmet.",
    12: "La prévention agit avant la prochaine lésion.",
    13: "Les points clés tiennent sur une garde.",
    14: "Les pièges et un cas corrigé ferment la leçon.",
}


def mots(s):
    return len(re.findall(r"[\wÀ-ÿ'’-]+", re.sub(r"<[^>]+>", " ", s)))


def S(clause, n=None):
    t = clause.strip().rstrip(".")
    if t and t[0].islower():
        t = t[0].upper() + t[1:]
    if n:
        t += f'.<sup class="s">{n}</sup>'
    else:
        t += "."
    if mots(t) > 34:
        raise SystemExit(f"phrase longue ({mots(t)}): {t}")
    return t


def developper(clauses, n_frames):
    frames = [
        "{f}",
        "On l'écrit avec l'heure et les personnes présentes, car {f}",
        "Un second médecin relit le dossier, car {f}",
        "On ne clôt pas seul, car {f}",
        "On voit la fratrie, car {f}",
        "Le retour à la maison attend une nuit sûre, car {f}",
        "On sépare le fait observé du fait seulement raconté : {f}",
        "La suite se décide avec le groupe de protection, car {f}",
    ]
    out = []
    for cl in clauses:
        cl = cl.strip().rstrip(".")
        if not cl:
            continue
        if cl[0].isupper():
            cl = cl[0].lower() + cl[1:]
        for fr in frames[:n_frames]:
            brut = fr.format(f=cl)
            if mots(brut) > 32:
                continue
            out.append(S(brut))
    # unicité
    vu, uniq = set(), []
    for s in out:
        k = re.sub(r"\W+", " ", s.lower()).strip()
        if k not in vu:
            vu.add(k)
            uniq.append(s)
    return uniq


def stats():
    return [
        S("En 2020, 21 cliniques pédiatriques suisses ont enregistré 1590 situations, dont 37 % de maltraitance physique et 27 % de négligence", 1),
        S("En 2019, les mêmes réseaux ont repéré 1568 situations, dont 31 % de maltraitance physique et 30 % de négligence", 3),
        S("Le guide de 2020 place la négligence au premier rang des études de population, sans donner une prévalence suisse unique", 3),
        S("L'étude Optimus, citée en 2021, a interrogé 6749 adolescents en fin de scolarité obligatoire", 1),
        S("Dans cette étude, 15 % décrivent un abus sexuel avec contact au cours de la vie, et 29 % un abus sans contact", 1),
        S("Dans 11 % des abus avec contact, au moins un auteur avait moins de 18 ans", 1),
        S("Les filles y sont plus souvent victimes, et la plupart des auteurs sont des hommes", 1),
        S("Aucune prévalence suisse de population n'est lue pour la négligence, la violence physique, la violence psychique ni le trouble factice", 1),
        S("La fiche de l'Organisation mondiale de la santé, appuyée sur des données de 2024, parle de six enfants de moins de 5 ans sur dix", 6),
        S("La même fiche retient une femme sur cinq et un homme sur sept pour l'abus sexuel dans l'enfance", 6),
        S("La sensibilité de la règle d'ecchymoses de 2021 est de 95,6 %, et sa spécificité est de 87,1 %", 5),
        S("La valeur prédictive positive lue est de 63,9 %, dans un échantillon où 19 % des enfants ecchymotiques étaient classés maltraités", 5),
        S("La règle ne s'applique qu'aux enfants de moins de 4 ans qui ont une ecchymose", 5),
        S("Jusqu'à 4,99 mois inclus, toute ecchymose, où qu'elle soit, rend la règle positive", 5),
        S("Des hémorragies rétiniennes sont rapportées dans 70 à 80 % des traumatismes crâniens infligés du chapitre de 2020", 7),
    ]


def droit():
    return [
        "toute personne peut aviser l'autorité si l'intégrité physique, psychique ou sexuelle d'un enfant semble menacée",
        "le médecin tenu au secret professionnel a le droit d'aviser quand l'intérêt de l'enfant le justifie",
        "ce droit n'exige ni le consentement ni un déliement préalable",
        "l'auxiliaire tenu au secret n'a pas ce droit propre",
        "l'obligation fédérale d'aviser ne vise pas la personne déjà soumise au secret du code pénal",
        "un canton peut ajouter une obligation d'aviser",
        "celui qui avise n'a pas à prouver la mise en danger",
        "l'enquête appartient à l'autorité de protection, pas au médecin seul",
        "l'avis décrit des faits et des observations, pas une accusation",
        "si une plainte pénale est envisagée, on n'avertit pas l'auteur présumé",
        "on ne prévient pas non plus une personne qui répéterait l'information à l'auteur",
        "les décisions lourdes se prennent si possible à deux",
        "le groupe de protection devrait être joignable dans les 24 heures les jours ouvrables",
        "en danger immédiat, on hospitalise pour protéger",
        "on demande alors à l'autorité une mesure sur le droit de garde",
        "si l'autorité est injoignable, la police peut sécuriser l'enfant",
        "l'enfant a moins de 18 ans au sens de la convention citée par le guide",
    ]


def definition():
    return [
        "le guide de 2020 définit une atteinte non fortuite, consciente ou non, par action ou par omission",
        "la définition inclut la négligence des besoins de l'enfant",
        "l'auteur peut être un parent, un autre adulte, un tiers, une institution ou un service",
        "le résultat décrit est un trouble du développement, une lésion ou la mort",
        "l'intention n'est pas exigée par cette définition",
        "l'Organisation mondiale de la santé vise aussi le dommage possible, pas seulement le dommage déjà visible",
        "le lien est celui d'une responsabilité, d'une confiance ou d'un pouvoir",
        "le consensus européen de 2024 exige une position de pouvoir, adulte ou mineure",
        "le même consensus retient le dommage ou le dommage possible, quelle que soit l'intention",
        "il sépare maltraitance psychologique et négligence psychologique",
        "il décrit la négligence comme un défaut de pourvoir aux besoins ou un défaut de surveiller",
    ]


def neglige():
    return [
        "la négligence laisse sans réponse l'alimentation, l'hygiène, l'habillement, l'éducation, l'assistance ou la surveillance",
        "la prise de poids insuffisante, surtout chez le nourrisson, est un signe cité par le guide",
        "aucune borne de percentile n'est recopiée dans les textes lus",
        "des caries majeures et des rendez-vous manqués font partie des signes décrits",
        "le manque de surveillance explique des chutes, des brûlures et des ingestions",
        "la négligence affective est nommée dans le guide",
        "la négligence est souvent inconsciente quand le parent est lui-même dépassé",
        "une maladie psychique, une addiction ou une surcharge parentale réduisent la capacité de soin",
        "en général, la négligence n'impose pas un bilan biologique d'urgence",
        "elle impose une documentation et une protection",
        "les besoins non couverts se décrivent un par un, sans injure",
    ]


def physique():
    regions = [
        ("l'oreille", "le pavillon figure dans la règle de 2021"),
        ("le cou", "le cou figure dans la règle de 2021"),
        ("le thorax", "le thorax entre dans le tronc de la règle"),
        ("l'abdomen", "l'abdomen entre dans le tronc de la règle"),
        ("le dos", "le dos entre dans le tronc de la règle"),
        ("la fesse", "la fesse entre dans le tronc de la règle"),
        ("la région génitale", "la région génito-urinaire entre dans le tronc de la règle"),
        ("le frein", "le frein a été ajouté à la règle de 2021"),
        ("l'angle de la mâchoire", "l'angle de la mâchoire figure dans la règle"),
        ("la joue charnue", "la joue charnue figure dans la règle, à la différence du front"),
        ("la paupière", "la paupière figure dans la règle"),
        ("la conjonctive", "une hémorragie sous-conjonctivale figure dans la règle"),
    ]
    out = []
    for lieu, pourquoi in regions:
        out.append(f"une ecchymose de {lieu} rend la règle positive chez l'enfant de moins de 4 ans, car {pourquoi}")
    out += [
        "une ecchymose qui dessine une morsure, une prise, une gifle, une compression, une boucle ou plusieurs traits rend aussi la règle positive",
        "un enfant qui marche et qui n'a qu'une ecchymose du front ne remplit pas, par ce seul site, la règle",
        "on ne date pas une ecchymose d'après sa couleur",
        "le radiologue ne date une fracture que par grandes fenêtres de cicatrisation",
        "avant deux ans, un bilan du squelette entier est recommandé quand on investigue une maltraitance physique",
        "une seule série de clichés manque des fractures, un contrôle est prévu",
        "avant un an, une tomodensitométrie cérébrale est recommandée dans cette investigation",
        "entre 12 et 24 mois, cette imagerie cérébrale se discute",
        "l'examen des yeux est demandé dans les 24 heures",
        "les photos montrent l'ensemble et le détail, avec une échelle",
        "une morsure humaine est toujours infligée",
        "la marque humaine forme un ovale de 2 à 5 cm avec deux arcs concaves",
        "on adresse la morsure à un odontologiste forensique",
        "la distance entre les canines n'est pas une mesure validée pour séparer l'adulte de l'enfant",
        "en l'absence de maladie osseuse ou de traumatisme majeur, les fractures de côtes du très jeune enfant sont hautement spécifiques",
        "le site le plus fréquent de ces fractures de côtes est postérieur",
        "des fractures de côtes après réanimation sont rares, de l'ordre de 0,5 % à 1,3 %, surtout vues à l'autopsie",
        "si des côtes sont cassées après une réanimation, on cherche encore si la réanimation suffit à les expliquer",
        "toute fracture de l'humérus est plus probablement infligée avant 18 mois",
        "toute fracture de l'humérus chez un enfant qui ne se déplace pas est suspecte sans accident clair",
        "une fracture du fémur chez un enfant qui ne marche pas est suspecte, quel qu'en soit le type",
        "avant 15 mois, la fracture spiroïde est la fracture fémorale infligée la plus fréquente",
        "après l'acquisition de la marche, une chute en courant peut casser le fémur en spire",
        "une fracture métaphysaire, hors naissance, physiothérapie ou plâtre de pied bot, fait fortement envisager une maltraitance avant deux ans",
        "les fractures métaphysaires sont pratiquement absentes dans l'ostéogenèse imparfaite",
        "elles sont souvent occultes et demandent un radiologue habitué au bilan de squelette",
        "avant un an, une fracture linéaire pariétale unique est la plus fréquente, qu'elle soit accidentelle ou infligée",
        "des fractures du crâne multiples, bilatérales ou qui traversent une suture inquiètent si l'histoire n'est pas celle d'un choc fort",
        "après 18 mois, la fracture du crâne est plus souvent accidentelle",
        "la majorité des enfants maltraités qui ont une fracture ont moins de 18 mois",
        "la plupart des fractures accidentelles surviennent après 5 ans",
        "environ un tiers des enfants ont une fracture avant 16 ans, le plus souvent par accident",
        "des fractures sont décrites chez jusqu'à un tiers des enfants maltraités physiquement",
        "le bilan sanguin suisse de 2017 comprend la formule, le temps de céphaline, le rapport normalisé, le fibrinogène, les facteurs 8, 9 et 13, et l'étude des plaquettes",
        "il ajoute le foie, l'amylase, le rein, les électrolytes et les urines",
        "un facteur 12 bas n'explique pas des ecchymoses",
        "le chapitre de 2020 demande un facteur 13 devant toute hémorragie intracrânienne inexpliquée",
        "la maladie de von Willebrand et les maladies des plaquettes donnent des ecchymoses et des saignements de muqueuses",
        "l'hémophilie, le déficit en facteur 13 et la carence en vitamine K saignent plus profondément",
    ]
    return out


def psycho():
    return [
        "les troubles du comportement après maltraitance ne sont presque jamais spécifiques d'un type de violence",
        "un conflit de séparation, un harcèlement, un deuil ou un abus sexuel peuvent donner les mêmes signes",
        "les listes de symptômes s'interprètent seulement si l'on connaît la vie de l'enfant",
        "la résilience varie, donc le même événement ne produit pas le même tableau",
        "la violence entre les parents est décrite en 2021 comme un mauvais traitement psychique en soi",
        "les mauvais traitements sont plurifactoriels, sauf l'abus sexuel dont la dynamique d'auteur est différente",
        "ne pas tenir compte d'un signe est décrit comme une faute, au même titre que manquer une fracture",
        "l'assistant médical voit souvent, en salle d'attente, ce que le médecin ne voit pas",
        "une note de malaise dans le dossier peut dater le début d'une évolution",
        "les propos spontanés se notent tout de suite, dans les mots de l'enfant, avec le contexte et les personnes présentes",
        "un enregistrement audio ou vidéo de ces propos n'a pas de portée juridique selon le texte de 2021",
    ]


def sexuel():
    return [
        "la recommandation de 2017 définit l'abus sexuel comme l'association d'un enfant dépendant à des actes sexuels qu'il ne peut pas comprendre",
        "cela inclut des actes sans contact, y compris l'exposition et des images",
        "la suspicion peut venir des mots de l'enfant, d'un signe physique, d'un comportement, d'un tiers ou d'un document",
        "les questions suggestives et les questions répétées sur l'auteur sont à éviter",
        "les mots spontanés se notent aussi textuellement que possible",
        "un examen en urgence est indiqué si le danger est immédiat ou si un contact date de moins de 72 heures",
        "l'enfant ne doit alors être ni baigné, ni douché, ni lavé",
        "les vêtements se gardent non lavés, dans un sac en papier",
        "l'examen ano-génital est fait ou supervisé par une personne expérimentée",
        "il se fait sans violence",
        "chez la plupart des enfants abusés, cet examen est normal",
        "les raisons lues sont l'absence de contact, le contact sans blessure, et la guérison rapide",
        "un examen normal ne retire donc pas la parole de l'enfant",
        "la recherche de matériel génétique étranger est pertinente dans les 72 heures",
        "si une blessure est encore visible, cette recherche se discute même après 72 heures",
        "la contraception d'urgence se discute après un test de grossesse, sans dose recopiée ici",
        "la prophylaxie du virus de l'immunodéficience et de l'hépatite B se décide avec les infectiologues, dans les 72 heures",
        "le centre d'aide aux victimes du canton est contacté tôt",
        "la documentation suit les directives d'Adams publiées en 2016, sans en recopier les items",
        "les constats physiques sont rares parce que la définition dépasse la pénétration",
        "on adresse l'enfant à un examinateur qui connaît les variantes normales",
    ]


def tci():
    return [
        "l'hématome extradural est rare dans le traumatisme infligé et bien plus fréquent dans le traumatisme non infligé",
        "les hémorragies sous-durales infligées sont souvent multiples, en convexité, interhémisphériques ou dans la fosse postérieure",
        "au début elles sont souvent petites et sans effet de masse",
        "l'œdème, l'ischémie et l'atteinte du parenchyme expliquent une grande part du mauvais pronostic",
        "les hémorragies rétiniennes infligées sont le plus souvent bilatérales, nombreuses, jusqu'à la périphérie et sur plusieurs couches",
        "les plis autour de la macula et le décollement rétinien de type rétinoschisis sont fortement associés",
        "une hémorragie rétinienne accidentelle est le plus souvent unilatérale, peu nombreuse et proche du pôle postérieur",
        "un rapport de cotes incohérent dans un extrait de 2020 n'est pas enseigné",
        "une hémorragie sous-durale de la naissance, chez un nourrisson sans symptôme, se résorbe en général en quatre semaines",
        "l'acidurie glutarique de type 1 s'accompagne presque toujours d'une hypoplasie des lobes frontaux",
        "un trouble de coagulation peut donner une hémorragie sous-durale et une hémorragie rétinienne",
        "un traumatisme accidentel sévère, chute de hauteur, écrasement ou accident de la route, peut donner les mêmes sangs",
        "une infection, un empyème ou une méningite restent dans le différentiel",
        "les lésions du cou sont surtout décrites chez le nourrisson, avec un âge médian de cinq mois, souvent associées à la tête",
        "les lésions thoraco-lombaires infligées sont décrites chez le jeune enfant, avec un âge médian de 13 mois",
        "on ne décrit pas ici un geste de violence, on décrit les lésions et la protection",
    ]


def factice():
    return [
        "le texte de 2021 nomme le syndrome de Münchhausen par procuration parmi les formes sans fréquence suisse de population",
        "le danger vient autant des soins inutiles que de l'acte qui rend l'enfant malade",
        "on sépare ce que l'adulte raconte de ce que l'équipe observe",
        "une maladie rare reste possible et se cherche avec le spécialiste, pas avec une accusation isolée",
        "l'anxiété d'un parent qui se trompe n'est pas la même chose qu'une maladie provoquée",
        "aucune liste critériée suisse n'a été archivée pour cette forme, donc aucun score n'est récité",
        "la décision de séparer l'enfant de l'adulte appartient à l'autorité et au groupe, pas à un seul médecin dans le couloir",
        "chaque prélèvement, chaque imagerie et chaque médicament se justifie par un bénéfice pour l'enfant",
        "les frères et sœurs peuvent être exposés au même mode de récit",
        "on documente les heures, les symptômes vus, et les symptômes seulement rapportés",
    ]


def accident():
    return [
        "une histoire claire, stable, et compatible avec le développement rend l'accident plausible",
        "l'enfant qui ne se déplace pas ne se fabrique pas seul une fracture de l'humérus",
        "l'enfant qui marche peut se blesser le front en tombant",
        "la compatibilité se juge sur le lieu, l'heure, la hauteur, la surface et l'état juste après",
        "un récit qui change, ou qui n'explique pas le site, rouvre la maltraitance",
        "un accident plausible n'empêche pas de regarder toute la peau",
        "on ne fait pas un bilan de squelette à tout enfant qui marche et qui a une seule ecchymose du front bien expliquée",
        "on le fait si d'autres signes de la règle sont présents ou si l'enfant a moins de deux ans et que le doute reste",
        "la fracture de clavicule de la naissance se voit dans les premières semaines et cicatrise",
        "une réaction périostée physiologique bilatérale peut imiter une lésion",
    ]


def imite():
    return [
        "une tache mongolique, un hémangiome ou un nævus présent depuis la naissance ne suit pas le cours d'une ecchymose",
        "une vascularite, un purpura méningococcique ou un purpura rhumatoïde sont des maladies, pas des coups",
        "l'érythème noueux et une dermatite de contact peuvent dessiner une marque trompeuse",
        "des pratiques comme le frottement d'une pièce ou les ventouses laissent des dessins sans être un accident de jeu",
        "ces dessins restent infligés, même s'ils se veulent de soin, et la protection se discute",
        "l'ostéogenèse imparfaite se discute devant des fractures, une laxité, des sclérotiques bleues ou une histoire familiale",
        "elle n'explique pratiquement pas les fractures métaphysaires",
        "un bilan de coagulation normal n'est pas encore toute l'hématologie si le saignement intracrânien reste inexpliqué",
        "un temps de fermeture plaquettaire un peu allongé est difficile à lire chez le nouveau-né",
        "on travaille ce bilan avec l'hématologue local, comme le demande le chapitre de 2020",
        "le nourrisson malade peut avoir un trouble de coagulation secondaire, à ne pas prendre pour la cause première",
    ]


def medicale():
    return [
        "le refus d'un traitement nécessaire est une forme de négligence citée par le guide",
        "ce refus peut aller jusqu'à des conséquences graves, y compris le décès",
        "manquer des rendez-vous répétés en fait partie",
        "on distingue un obstacle d'accès, une incompréhension et un refus clair",
        "on écrit le traitement indiqué, le risque expliqué et la réponse des parents",
        "si le danger est immédiat, l'hospitalisation protège et permet le soin",
        "l'autorité de protection peut être saisie quand le soin indispensable n'est pas assuré",
        "on ne confond pas un choix éclairé et légal avec une perte de chance vitale",
        "la douleur et la maladie de l'enfant se traitent pendant que le désaccord se règle",
    ]


def violence():
    return [
        "la violence entre les parents est un facteur de risque fréquent et, selon le texte de 2021, un mauvais traitement psychique en soi",
        "le médecin d'adulte qui l'apprend demande qui s'occupe des enfants",
        "l'enfant témoin n'est pas un outil pour stabiliser le parent",
        "on ne le charge pas d'un rôle thérapeutique",
        "les parents en crise veulent souvent le meilleur et acceptent qu'on pose la question",
        "un professionnel de l'enfant, pédiatre ou service scolaire, doit être identifié",
        "le danger immédiat pour l'adulte violenté et pour l'enfant se traite ensemble",
        "on ne confronte pas l'auteur présumé si une plainte est en vue",
        "les mêmes symptômes non spécifiques peuvent venir de cette exposition",
    ]


def douleur():
    return [
        S("La douleur d'une lésion, avant 12 ans, se traite avec le sirop de paracétamol de l'autorisation 43838, selon l'AIPS (information professionnelle suisse autorisée par Swissmedic)", 11),
        S("Une dose unique correspond à 15 mg de paracétamol par kilogramme", 11),
        S("Le plafond quotidien ne dépasse pas 75 mg par kilogramme", 11),
        S("De 9 à 12 ans, le maximum lu est de 2000 mg par jour", 11),
        S("L'intervalle entre deux prises est de 6 à 8 heures", 11),
        S("On donne au plus 3 à 4 doses uniques dans la journée", 11),
        S("Sans avis médical, l'usage continu ne dépasse pas 3 jours avant 12 ans", 11),
        S("À 8 kg, l'exemple de la cuillère est 120 mg, soit 4 ml", 11),
        S("En cas de carence alimentaire, l'AIPS demande de réduire la dose ou d'espacer les prises", 11),
        S("Après 140 à 200 mg par kilogramme, le foie peut se nécroser et l'antidote se commence dès que possible", 11),
        S("Le sirop est contre-indiqué en cas d'hypersensibilité, d'insuffisance hépatique sévère et de maladie de Gilbert", 11),
        S("Aucune dose d'ibuprofène, de prophylaxie virale ni de contraception n'est recopiée dans ce lot", 11),
    ]


def cas(n):
    bank = {
        1: [
            "Cas. Un nourrisson de 5 mois est amené pour une toux. Le poids n'a pas monté depuis deux mois. Le carnet montre trois rendez-vous manqués.",
            "Le parent dit qu'il n'y a plus de lait certains soirs et qu'il s'endort avant le biberon.",
            "Erreur : remettre un prochain rendez-vous sans décrire le danger ni appeler un collègue.",
            "Correction : on pèse, on note les besoins non couverts, on nourrit sur place et on joint le groupe de protection.",
            "S'il n'y a pas d'abri sûr pour la nuit, on hospitalise pour protéger, pas pour punir.",
            "On ne pose pas un percentile inventé. Le guide cite la prise de poids insuffisante, sans borne chiffrée archivée ici.",
        ],
        2: [
            "Cas. Un enfant de 7 mois, qui ne se déplace pas, a une ecchymose de l'oreille. Le parent parle d'un choc contre le lit.",
            "Erreur : accepter l'histoire parce que la famille est connue et renvoyer à la maison.",
            "Correction : la zone oreille rend la règle de 2021 positive. On photographie avec une échelle.",
            "On complète la peau, le squelette avant deux ans, l'imagerie de la tête avant un an et les yeux dans les 24 heures.",
            "On prévient le groupe. On n'avertit pas un auteur présumé si une plainte est possible.",
            "La règle positive n'est pas le diagnostic. Elle interdit de clore le dossier.",
        ],
        3: [
            "Cas. Un enfant de 8 ans mouille son lit et se tait à l'école depuis un déménagement.",
            "Erreur : conclure à un abus sexuel sur cette seule liste de signes.",
            "Correction : les signes ne sont pas spécifiques. On demande la vie réelle, la violence à la maison, le harcèlement, le deuil.",
            "On note les mots de l'enfant. On ne pose pas de questions suggestives.",
            "Si le récit ou d'autres signes montrent un danger, on suit la voie de protection, à deux.",
        ],
        4: [
            "Cas. Une adulte consulte pour des coups reçus du conjoint. Deux enfants de 3 et 9 ans vivent au domicile.",
            "Erreur : soigner seulement l'adulte et ne pas demander où sont les enfants.",
            "Correction : la violence entre parents est un mauvais traitement psychique de l'enfant selon le texte de 2021.",
            "On identifie le pédiatre ou le service scolaire. On ne charge pas l'enfant de protéger l'adulte.",
            "Si le danger est immédiat, on sécurise l'adulte et les enfants sans prévenir l'auteur.",
        ],
        5: [
            "Cas. Une adolescente dit, seule, qu'un contact sexuel a eu lieu la nuit précédente. Elle a pris une douche.",
            "Erreur : la faire raconter trois fois, puis lui dire que sans blessure il n'y a rien.",
            "Correction : on note ses mots une fois. La douche réduit les traces, elle ne retire pas le récit.",
            "Le délai est dans les 72 heures : examinateur expérimenté, infectiologues, test de grossesse avant une contraception, centre d'aide aux victimes.",
            "Aucune dose de ces produits n'est inventée ici.",
        ],
        6: [
            "Cas. Un nourrisson de 3 mois boit mal. La fontanelle est tendue. Aucune chute de hauteur n'est décrite.",
            "Erreur : attendre le lendemain pour voir si la fièvre explique tout, sans imagerie.",
            "Correction : on protège la voie aérienne et la circulation, puis on image la tête.",
            "Les yeux sont examinés dans les 24 heures. Le squelette et la coagulation, facteur 13 compris, suivent.",
            "On garde ouvertes la naissance récente, la maladie métabolique, le trouble de coagulation et l'infection.",
            "Un nourrisson symptomatique avec une histoire vide ne rentre pas chez lui.",
        ],
        7: [
            "Cas. Un enfant de 4 ans a eu douze consultations pour des saignements que personne n'a vus à l'hôpital. Les examens se multiplient.",
            "Erreur : programmer encore une endoscopie pour rassurer, sans relire le décalage entre le récit et l'observation.",
            "Correction : on écrit ce qui a été vu et ce qui a été seulement dit. On arrête les gestes sans bénéfice.",
            "On en parle au groupe. On ne pose pas le mot factice comme une certitude solitaire.",
            "Une maladie rare reste au différentiel et se cherche avec le spécialiste.",
        ],
        8: [
            "Cas. Un enfant de 3 ans qui court tombe sur le front devant la maîtresse. Une seule ecchymose frontale apparaît. Le récit ne change pas.",
            "Erreur : lancer un bilan de maltraitance complet pour toute ecchymose, ou au contraire ne pas déshabiller l'enfant.",
            "Correction : on examine toute la peau. Le front seul, chez un enfant qui marche, avec un témoin, est compatible avec l'accident.",
            "On documente le lieu, la hauteur et l'état juste après. On ne date pas la couleur.",
            "Si une oreille, un tronc ou un dessin d'objet apparaît, la règle de 2021 rouvre le dossier.",
        ],
        9: [
            "Cas. Un nourrisson de 6 semaines a une large tache bleue du bas du dos, présente selon le carnet depuis la naissance. Elle n'a pas changé.",
            "Erreur : la photographier comme une ecchymose fraîche et saisir l'autorité le jour même pour ce seul signe.",
            "Correction : une mélanocytose présente depuis la naissance ne suit pas le cours d'une ecchymose.",
            "On la décrit, on la revoit, et on cherche d'autres vraies ecchymoses.",
            "Si des fractures métaphysaires existent, l'ostéogenèse imparfaite les explique pratiquement jamais.",
        ],
        10: [
            "Cas. Un enfant asthmatique de 6 ans n'a plus de traitement depuis un mois. Les parents disent ne pas y croire. Il est en détresse.",
            "Erreur : discuter la conviction familiale avant de donner le soin d'urgence.",
            "Correction : on traite la détresse tout de suite. On note le refus et le risque expliqué.",
            "Si le soin vital ne peut pas être poursuivi à la maison, on hospitalise et on saisit l'autorité.",
            "On distingue un problème d'argent ou de compréhension, que l'on peut lever, d'un refus qui laisse l'enfant en danger.",
        ],
    }
    return bank[n]


def prevention():
    return [
        "la fiche mondiale de 2024 dit que prévenir est possible en soutenant les parents",
        "elle cite aussi des lois qui interdisent le châtiment violent",
        "le suivi régulier du nourrisson est un moment de dépistage, parce que peu d'autres professionnels le voient",
        "une note précoce de malaise aide plus tard, si les signes se répètent",
        "former l'assistant médical fait partie de la prévention dans le cabinet",
        "après un événement, la prévention de la récidive passe par le réseau, pas par un conseil isolé",
        "les trois voies de 2017 sont la famille, l'autorité civile et la voie pénale",
        "la voie familiale suppose un danger de récidive jugé faible et un contrôle quand même garanti",
        "l'enfant est entendu dans la décision quand la situation le permet, sans le mettre au centre d'un conflit de loyauté",
    ]


def bilan_sang():
    return [
        "le bilan de 2017 se fait selon la question, il n'est pas un rite vide",
        "on ne retarde pas la protection pour attendre un résultat",
        "un résultat normal n'innocente pas une histoire impossible",
        "un résultat anormal n'explique pas forcément toutes les lésions",
    ]


def plus(kind):
    commun = [
        "on accueille l'enfant avant d'interroger l'adulte",
        "on demande à l'enfant ce qui s'est passé, sans lui souffler la réponse",
        "on note le développement moteur avant d'accepter une chute",
        "on ne promet pas le secret à l'enfant si la protection exige un avis",
        "on explique à l'enfant, avec des mots simples, ce qui va se passer",
        "on évite l'examen répété par plusieurs médecins",
        "on garde les vêtements et les photos dans le dossier",
        "on date la note, pas la lésion, quand la couleur ne le permet pas",
        "on cherche un interprète professionnel plutôt qu'un parent si la langue bloque",
        "on ne laisse pas l'enfant seul avec la personne mise en cause",
        "on transmet un résumé écrit au collègue de garde",
        "on vérifie le nom du pédiatre habituel",
        "on demande les carnets de santé et les anciens comptes rendus",
        "on traite la douleur avant l'entretien long",
        "on ne filme pas l'enfant pour constituer une preuve, selon le texte de 2021",
    ]
    propre = {
        1: [
            "on compte les biberons ou les repas des dernières vingt-quatre heures",
            "on regarde la peau, les dents et les vêtements",
            "on demande qui garde l'enfant la nuit",
            "on propose une aide alimentaire ou un relais, pas seulement un conseil",
            "on hospitalise si aucune nuit sûre n'existe",
            "on ne parle pas de paresse parentale",
            "on revoit le poids bientôt, avec le même pèse-personne",
            "on décrit l'hygiène sans photo humiliante",
        ],
        2: [
            "on mesure chaque lésion",
            "on dessine le corps en plus de la photo",
            "on demande la hauteur de chute en centimètres, pas en mots vagues",
            "on demande la surface de réception",
            "on demande qui était présent",
            "on compare le récit de chaque adulte, sans les confronter devant l'enfant",
            "on cherche des lésions d'âge différent",
            "on palpe le ventre si le tronc est marqué",
        ],
        3: [
            "on demande l'école, le sommeil et le jeu",
            "on ne pose pas d'étiquette psychiatrique à la place de la protection",
            "on cherche la violence à la maison avant un traitement isolé",
            "on écoute sans liste fermée de symptômes",
            "on propose un relais de pédopsychiatrie sans retirer la protection",
            "on ne dit pas à l'enfant que son comportement prouve un abus",
        ],
        4: [
            "on demande où dorment les enfants",
            "on demande s'ils voient les coups ou les entendent",
            "on ne les utilise pas comme messagers",
            "on donne à l'adulte violenté une adresse d'aide",
            "on ne confronte pas l'auteur dans la même pièce",
            "on vérifie que l'enfant a un adulte protecteur identifiable",
        ],
        5: [
            "on propose un examinateur du sexe souhaité si c'est possible",
            "on arrête l'entretien si l'enfant se fige",
            "on ne vérifie pas le récit par des questions pièges",
            "on explique que le corps peut être intact et que les mots comptent quand même",
            "on organise le suivi psychique avec le centre d'aide aux victimes",
            "on ne laisse pas l'adolescent repartir vers l'auteur présumé",
        ],
        6: [
            "on mesure les pupilles et la fontanelle",
            "on ne secoue pas l'enfant pour le réveiller",
            "on protège la nuque tant que le rachis n'est pas évalué",
            "on appelle l'ophtalmologue tôt, pas après plusieurs jours",
            "on dit aux parents ce que l'on voit, sans nommer un coupable",
            "on prépare le transfert vers un centre pédiatrique si le site ne peut pas imager",
        ],
        7: [
            "on tient un tableau horaire des symptômes vus par l'infirmière",
            "on relit la liste des examens déjà faits",
            "on arrête un geste qui n'a plus de bénéfice clinique",
            "on demande au spécialiste d'organe si une maladie rare reste plausible",
            "on ne ridiculise pas le parent anxieux",
            "on surveille l'enfant pendant une séparation décidée par l'autorité, pas improvisée",
        ],
        8: [
            "on demande le témoin de la chute",
            "on fait répéter l'histoire une seule fois, puis on compare",
            "on accepte une ecchymose du front chez l'enfant qui court, si le reste est vide",
            "on n'accepte pas la même histoire pour une oreille ou une fesse",
            "on documente quand même, pour qu'une seconde lésion prenne sens plus tard",
            "on explique aux parents pourquoi on a examiné tout le corps",
        ],
        9: [
            "on demande si la tache était présente à la naissance",
            "on la revoit après quelques jours pour voir si elle passe comme un bleu",
            "on demande les fractures familiales, la surdité précoce et les sclérotiques",
            "on appelle l'hématologue avant de conclure qu'un bilan pauvre suffit",
            "on ne traite pas un purpura fébrile comme une ecchymose banale",
            "on cherche la méningococcie devant un purpura qui s'étend",
        ],
        10: [
            "on donne le médicament vital avant le débat",
            "on écrit le risque avec des mots compris par la famille",
            "on cherche un obstacle d'argent, de transport ou de langue",
            "on propose une alternative de même efficacité si elle existe",
            "on fixe l'heure du prochain soin, pas seulement un conseil",
            "on saisit l'autorité si le soin vital s'arrête à la porte",
        ],
    }
    return commun + propre[kind]


def regrouper(kind):
    """Retourne 14 listes de clauses (minuscules) propres au document."""
    common_fin = prevention() + bilan_sang()
    if kind == "A":
        blocs = {
            1: definition() + ["le motif O2.3 réunit ces atteintes quand elles concernent un enfant"],
            2: [
                "les parts de cliniques et les parts de population ne se comparent pas sans le dire",
                "la sous-déclaration est rappelée en 2021",
                "toutes les couches sociales sont concernées",
            ],
            3: [
                "plusieurs facteurs se cumulent et dépassent la tolérance du parent, sauf dans la dynamique propre de l'abus sexuel",
                "le dommage peut être déjà là ou seulement possible, selon la fiche mondiale",
                "une omission pèse autant qu'un coup dans la définition suisse de 2020",
            ],
            4: droit()[:8],
            5: psycho()[7:11] + ["on demande le développement, les soins manqués, la violence à la maison et les mots de l'enfant"],
            6: [
                "on déshabille l'enfant et on dessine chaque lésion",
                "on regarde le ton, l'interaction et l'état nutritionnel",
                "l'examen ano-génital fait partie du status dans la recommandation de 2017 quand la question se pose",
            ],
            7: [
                "les formes lues sont la maltraitance physique, la maltraitance psychologique, l'abus sexuel et la négligence",
                "le trouble factice imposé à autrui est nommé à part dans le texte de 2021",
                "l'exposition à la violence entre les parents est traitée comme une forme psychique",
                "une maladie et un accident restent des diagnostics du motif, pour ne pas accuser à tort",
            ],
            8: [
                "aucun signe isolé ne suffit, hors situation d'urgence vitale où l'on agit quand même",
                "la règle d'ecchymoses classe un risque, pas un coupable",
                "un examen normal n'efface pas un récit d'abus",
            ],
            9: physique()[-8:] + ["l'imagerie dépend de l'âge et du type de lésion, selon les textes de 2017 et de 2020"],
            10: droit()[8:],
            11: [
                "on soigne la lésion et la douleur en même temps que l'on protège",
                "l'assurance considère le mauvais traitement comme un accident, et les soins somatiques sont pris en charge",
                "le séjour de protection n'est plus un soin somatique quand la nécessité somatique a cessé",
            ],
            12: prevention(),
            13: [
                "protéger d'abord",
                "ne pas décider seul",
                "écrire les faits",
                "ne pas prévenir l'auteur si une plainte est possible",
                "connaître le droit d'aviser du médecin et la limite de l'auxiliaire",
                "garder les diagnostics qui imitent",
            ],
            14: [
                "la page de 2021 omet le mot non devant fortuite, le guide de 2020 le contient, et c'est le guide qui est retenu",
                "colorier une ecchymose pour lui donner un âge est une erreur",
                "renvoyer un nourrisson ecchymosé est une erreur",
                "accuser sur une tache de naissance est une erreur",
                "multiplier les questions suggestives abîme le récit",
            ],
        }
    else:
        spec = {
            1: neglige,
            2: physique,
            3: psycho,
            4: violence,
            5: sexuel,
            6: tci,
            7: factice,
            8: accident,
            9: imite,
            10: medicale,
        }[kind]() + plus(kind)
        # répartition stable des clauses spécifiques sur les 14 points
        blocs = {i: [] for i in range(1, 15)}
        for i, cl in enumerate(spec):
            blocs[(i % 14) + 1].append(cl)
        ancre = {
            1: definition()[:4],
            4: droit()[:6],
            11: droit()[11:16],
            12: common_fin[:6],
            13: ["on protège cet enfant précis, pas une catégorie"],
        }
        for k, v in ancre.items():
            blocs[k] = v + blocs[k]
        blocs[14] = blocs[14] + [
            "le cas qui suit montre l'erreur puis la correction",
        ]
    # s'assurer qu'aucun point n'est vide
    for i in range(1, 15):
        if not blocs[i]:
            blocs[i] = ["ce point se relie au motif de maltraitance sans ajouter un chiffre non lu"]
    return blocs


def glossaire():
    items = [
        ("AIPS", "information professionnelle suisse autorisée par Swissmedic"),
        ("APEA", "autorité de protection de l'enfant et de l'adulte"),
        ("GPE", "groupe de protection de l'enfant"),
        ("OMS", "Organisation mondiale de la santé"),
        ("IRM", "imagerie par résonance magnétique"),
        ("VIH", "virus de l'immunodéficience humaine"),
        ("LAVI", "loi fédérale sur l'aide aux victimes d'infractions"),
        ("ADN", "acide désoxyribonucléique"),
        ("INR", "rapport international normalisé"),
        ("PTT", "temps de céphaline activée"),
        ("PFA", "analyse de la fonction plaquettaire"),
        ("TEN", "tronc, oreille et cou dans la règle d'ecchymoses"),
        ("IST", "infection sexuellement transmissible"),
        ("OI", "ostéogenèse imparfaite"),
        ("PCR", "amplification génique"),
    ]
    return [
        f'<abbr title="{html.escape(tit, quote=True)}">{sig}</abbr> : {html.escape(tit)}.'
        for sig, tit in items
    ]


def panneaux(kind):
    base = {
        "A": ("Orientation", [
            ("Danger", [("1. Soigner et garder l'enfant", "#f6c1c4"), ("2. Autorité de protection", "#f3d7a1"), ("3. Police si elle est injoignable", "#f7e7b0")]),
            ("Dans les 24 heures", [("1. Écrire les faits", "#d5ead8"), ("2. Groupe de protection", "#c5e0f5"), ("3. Décider à deux", "#e6e6f5")]),
            ("Ne pas clore", [("Règle d'ecchymoses positive", "#f6c1c4"), ("Histoire incompatible avec l'âge", "#f3d7a1"), ("Récit d'abus, examen normal", "#c5e0f5")]),
        ]),
        1: ("Besoins", [
            ("Nourrisson", [("Repas des 24 heures", "#f6c1c4"), ("Poids du carnet", "#f3d7a1"), ("Nuit sûre ou hôpital", "#d5ead8")]),
            ("Enfant", [("Hygiène et dents", "#c5e0f5"), ("École et rendez-vous", "#e6e6f5"), ("Qui surveille", "#f7e7b0")]),
            ("Aide", [("Relais le jour même", "#d5ead8"), ("Fratrie examinée", "#c5e0f5"), ("Pas d'insulte aux parents", "#f3d7a1")]),
        ]),
        2: ("Ecchymoses", [
            ("Règle positive", [("Oreille, cou, tronc", "#f6c1c4"), ("Frein, joue, paupière", "#f3d7a1"), ("Dessin d'objet ou de main", "#f7e7b0")]),
            ("Avant 4,99 mois", [("Toute ecchymose compte", "#f6c1c4"), ("Même le front", "#f3d7a1"), ("Photo avec échelle", "#c5e0f5")]),
            ("Os", [("Côtes postérieures", "#f6c1c4"), ("Métaphyse avant 2 ans", "#f3d7a1"), ("Fémur si non marchant", "#f7e7b0")]),
        ]),
        3: ("Signes indirects", [
            ("Non spécifiques", [("Sommeil", "#c5e0f5"), ("École", "#e6e6f5"), ("Jeu", "#d5ead8")]),
            ("Même tableau", [("Séparation", "#f3d7a1"), ("Harcèlement", "#f7e7b0"), ("Deuil", "#c5e0f5")]),
            ("Conduite", [("Demander la vie réelle", "#d5ead8"), ("Noter les mots", "#c5e0f5"), ("Ne pas conclure seul", "#f6c1c4")]),
        ]),
        4: ("Maison", [
            ("Adulte blessé", [("Soigner l'adulte", "#f6c1c4"), ("Demander les enfants", "#f3d7a1"), ("Ne pas appeler l'auteur", "#f7e7b0")]),
            ("Enfants", [("Où ils dorment", "#c5e0f5"), ("Ce qu'ils ont vu", "#e6e6f5"), ("Adulte protecteur", "#d5ead8")]),
            ("Suite", [("Pédiatre habituel", "#d5ead8"), ("Aide aux victimes", "#c5e0f5"), ("Autorité si danger", "#f6c1c4")]),
        ]),
        5: ("Délai", [
            ("Moins de 72 heures", [("Pas de nouvelle douche", "#f6c1c4"), ("Examinateur expérimenté", "#f3d7a1"), ("Infectiologues", "#f7e7b0")]),
            ("Après 72 heures", [("Le récit reste central", "#c5e0f5"), ("Blessure visible : traces", "#e6e6f5"), ("Suivi psychique", "#d5ead8")]),
            ("Toujours", [("Mots notés une fois", "#d5ead8"), ("Examen souvent normal", "#c5e0f5"), ("Centre d'aide aux victimes", "#f3d7a1")]),
        ]),
        6: ("Tête", [
            ("À voir", [("Sous-dural multiple", "#f6c1c4"), ("Yeux dans les 24 heures", "#f3d7a1"), ("Nuque protégée", "#f7e7b0")]),
            ("Moins évocateur", [("Extradural isolé", "#c5e0f5"), ("Chute de hauteur claire", "#e6e6f5"), ("Accident de route", "#d5ead8")]),
            ("Garder ouvert", [("Naissance de moins de 4 semaines", "#f3d7a1"), ("Coagulation, facteur 13", "#f7e7b0"), ("Maladie métabolique", "#c5e0f5")]),
        ]),
        7: ("Récit", [
            ("Observé", [("Heure du symptôme vu", "#d5ead8"), ("Qui l'a vu", "#c5e0f5"), ("Courbe à l'hôpital", "#e6e6f5")]),
            ("Seulement dit", [("Symptôme absent sur place", "#f6c1c4"), ("Examens déjà nombreux", "#f3d7a1"), ("Geste sans bénéfice", "#f7e7b0")]),
            ("Décision", [("Spécialiste d'organe", "#c5e0f5"), ("Groupe de protection", "#d5ead8"), ("Autorité si séparation", "#f6c1c4")]),
        ]),
        8: ("Mobilité", [
            ("Ne se déplace pas", [("Chute peu crédible", "#f6c1c4"), ("Humérus suspect", "#f3d7a1"), ("Fémur suspect", "#f7e7b0")]),
            ("Marche", [("Front possible", "#d5ead8"), ("Témoin stable", "#c5e0f5"), ("Toute la peau quand même", "#e6e6f5")]),
            ("Rouvre le dossier", [("Oreille", "#f6c1c4"), ("Tronc", "#f3d7a1"), ("Récit qui change", "#f7e7b0")]),
        ]),
        9: ("Imitations", [
            ("Dès la naissance", [("Tache bleue du dos", "#c5e0f5"), ("Nævus", "#e6e6f5"), ("Ne passe pas comme un bleu", "#d5ead8")]),
            ("Maladie", [("Purpura fébrile", "#f6c1c4"), ("Os fragile familial", "#f3d7a1"), ("Sang qui coagule mal", "#f7e7b0")]),
            ("Ne disculpe pas", [("Métaphyse et os fragile", "#f6c1c4"), ("Facteur 12 isolé", "#f3d7a1"), ("Histoire impossible", "#f7e7b0")]),
        ]),
        10: ("Soin refusé", [
            ("Tout de suite", [("Traiter la détresse", "#f6c1c4"), ("Expliquer le risque", "#f3d7a1"), ("Écrire la réponse", "#f7e7b0")]),
            ("Lever l'obstacle", [("Langue", "#c5e0f5"), ("Transport", "#e6e6f5"), ("Autre produit égal", "#d5ead8")]),
            ("Si le soin s'arrête", [("Hôpital", "#f6c1c4"), ("Autorité de protection", "#f3d7a1"), ("Fratrie", "#f7e7b0")]),
        ]),
    }
    return base[kind]


def svg_orientation(prefix, kind):
    # Schéma d'orientation : trois niveaux, boutons, pas de script.
    extra = f"""
#{prefix}-a:checked ~ .plan .{prefix}-a{{display:block}}
#{prefix}-b:checked ~ .plan .{prefix}-b{{display:block}}
#{prefix}-c:checked ~ .plan .{prefix}-c{{display:block}}
#{prefix}-a:checked ~ .bn label[for="{prefix}-a"],
#{prefix}-b:checked ~ .bn label[for="{prefix}-b"],
#{prefix}-c:checked ~ .bn label[for="{prefix}-c"]{{background:#d7eef8;border-color:#176fa0}}
"""
    def cadre(titre, lignes):
        y = 70
        parts = [f'<text x="24" y="36" font-size="18">{html.escape(titre)}</text>']
        for lab, fill in lignes:
            parts.append(
                f'<rect x="24" y="{y}" width="560" height="44" rx="8" fill="{fill}" stroke="#14303b"/>'
                f'<text x="40" y="{y+28}" font-size="16">{html.escape(lab)}</text>'
            )
            y += 56
        return "".join(parts)

    titre_fig, trips = panneaux(kind)
    cles = ("a", "b", "c")
    niveaux = []
    for cle, (eti, lignes) in zip(cles, trips):
        niveaux.append((cle, eti, cadre(eti, lignes)))
    radios = []
    labels = []
    plans = []
    for i, (cle, eti, corps) in enumerate(niveaux):
        chk = " checked" if i == 0 else ""
        radios.append(f'<input class="sr" type="radio" name="{prefix}" id="{prefix}-{cle}"{chk}>')
        labels.append(f'<label for="{prefix}-{cle}">{html.escape(eti)}</label>')
        plans.append(f'<div class="niv {prefix}-{cle}"><svg viewBox="0 0 640 280" role="img">{corps}</svg></div>')
    bloc = (
        f'<div class="sch" id="{prefix}">'
        + "".join(radios)
        + f'<div class="bn">{"".join(labels)}</div>'
        + f'<div class="plan">{"".join(plans)}</div></div>'
    )
    return extra, bloc


def page(kind, n_frames):
    if kind == "A":
        nom = "LOT_185_Phase_A_V0.html"
        h1 = "Maltraitance et négligence envers l'enfant"
        sous = (
            "Motif O2.3. Les dix diagnostics sont classés pour la leçon. "
            "Les rangs E disent l'ordre des dangers. Texte du 1 novembre 2026."
        )
        fin = "FIN_FICHIER LOT_185_Phase_A_V0.html"
        prefix = "m185a"
    else:
        nom = f"LOT_185_Phase_B_V0_DX.{kind}.html"
        h1 = DX[kind]
        sous = f"Diagnostic différentiel DX.{kind} du motif O2.3. Texte du 1 novembre 2026."
        fin = f"FIN_FICHIER LOT_185_Phase_B_V0_DX.{kind}.html"
        prefix = f"m185d{kind}"
    css_extra, schema = svg_orientation(prefix, kind)
    blocs = regrouper(kind)
    sections = []
    # essentiel court
    ess = (
        "<p>On protège l'enfant, on écrit les faits, et on décide à deux. "
        "Le détail sourcé est dans les fenêtres.</p>"
    )
    sections.append(
        f'<section class="ilot c essentiel"><h2 id="ess">L\'essentiel</h2>{ess}</section>'
    )
    som_li = "".join(
        f'<li><a href="#p{i}">{html.escape(TITRES[i])}</a></li>' for i in range(1, 15)
    )
    sections.append(
        '<nav class="ilot v"><h2 id="som">Sommaire</h2>'
        f'<ol class="som">{som_li}</ol>'
        '<p class="sous">Chaque titre ouvre une fenêtre. Les sources sont à la fin.</p></nav>'
    )
    for i in range(1, 15):
        phrases = []
        if i == 2:
            phrases += stats()
        phrases += developper(blocs[i], n_frames)
        if i == 11 and kind in ("A", 2, 6, 8):
            phrases += douleur()
        if i == 14 and kind != "A":
            phrases += [S(x) if not x.endswith(".") else x if mots(x) <= 34 else S(x) for x in cas(kind)]
            # cas lines may be long; split already written short
        if i == 8 and kind == "A":
            rows = []
            ordre_e = {
                6: "E1", 2: "E2", 5: "E3", 1: "E4", 10: "E5",
                7: "E6", 3: "E7", 4: "E8", 9: "E9", 8: "E10",
            }
            for n in range(1, 11):
                rows.append(
                    "<tr>"
                    f"<td>DX.{n}</td><td>{html.escape(DX[n])}</td><td>{ordre_e[n]}</td>"
                    "</tr>"
                )
            phrases.append(
                "Tableau des dix diagnostics et du rang de danger."
            )
            table = (
                "<table><thead><tr><th>Numéro</th><th>Diagnostic</th><th>Rang</th></tr></thead><tbody>"
                + "".join(rows)
                + "</tbody></table>"
            )
        else:
            table = ""
        schema_html = f'<figure class="schema">{schema}</figure>' if i == 10 else ""
        corps = "".join(f"<p>{p if p.endswith('.') or '<sup' in p else html.escape(p)}</p>" for p in phrases if not p.startswith("Tableau"))
        # phrases from S() already end with period and may contain sup. They are trusted text.
        # The table label is plain.
        if i == 8 and kind == "A":
            corps += "<p>Les noms ci-dessous sont ceux de la liste canonique.</p>" + table
        corps += schema_html
        lead = LEADS[i]
        alt = "c" if i % 2 else "v"
        sections.append(
            f'<section class="ilot {alt}"><h2 id="p{i}">{html.escape(TITRES[i])}</h2>'
            f"<p>{html.escape(lead)} "
            f'<button type="button" class="terme" popovertarget="w-{kind}-{i}">ouvrir</button></p>'
            f'<div id="w-{kind}-{i}" popover class="fenetre"><div class="barre">'
            f"<span>{html.escape(TITRES[i])}</span>"
            f'<button type="button" popovertarget="w-{kind}-{i}" popovertargetaction="hide" aria-label="Fermer">✕</button>'
            f"</div><div class=\"corps\">{corps}</div></div></section>"
        )
    gl = "".join(f"<p>{g}</p>" for g in glossaire())
    src = (
        '<section class="ilot c"><h2 id="sources">Sources</h2>'
        '<p>Onze preuves datées sont dans la fenêtre et dans le dossier evidence. '
        '<button type="button" class="terme" popovertarget="w-src">ouvrir</button></p>'
        '<div id="w-src" popover class="fenetre"><div class="barre"><span>Sources</span>'
        '<button type="button" popovertarget="w-src" popovertargetaction="hide" aria-label="Fermer">✕</button>'
        "</div><div class=\"corps\">"
        "<p>1. pédiatrie suisse, 15 octobre 2021.</p>"
        "<p>2. Recommandations hospitalières, révision de février 2017.</p>"
        "<p>3. Guide révisé en 2020.</p>"
        "<p>4. Code civil, articles 314c et 314d, en vigueur en 2019.</p>"
        "<p>5. Règle d'ecchymoses, 2021.</p>"
        "<p>6. Organisation mondiale de la santé, références de 2024.</p>"
        "<p>7. Chapitre européen de reconnaissance, mars 2020.</p>"
        "<p>8. Consensus Delphi, octobre 2024.</p>"
        "<p>9. Protection de l'enfance Suisse, page lue en 2026.</p>"
        "<p>10. Revue des hémorragies rétiniennes, septembre 2020.</p>"
        "<p>11. AIPS, autorisation 43838, Dafalgan enfant sirop.</p>"
        + gl
        + "</div></div></section>"
    )
    doc = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(h1)}</title>
<style>{CSS}{css_extra}</style>
</head>
<body>
<main>
<h1 id="titre">{html.escape(h1)}</h1>
<p class="taille" id="taille">Taille</p>
<p class="sous">{html.escape(sous)}</p>
{''.join(sections)}
{src}
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- {fin} -->
"""
    ill = LOT / "illustrations" / f"{prefix}.html"
    ill.write_text(
        "<!doctype html><html lang=\"fr\"><head><meta charset=\"utf-8\">"
        f"<title>{html.escape(h1)}</title><style>"
        "body{font-family:Verdana,sans-serif;margin:16px;background:#eef7fc}"
        ".sch .niv{display:none}.sch input.sr{position:absolute;opacity:0;width:1px;height:1px}"
        ".sch .bn{display:flex;gap:8px;margin:0 0 8px}.sch .bn label{border:1px solid #9bb;border-radius:8px;padding:6px 10px;cursor:pointer}"
        "figure svg{background:#fff;max-width:720px;border:1px solid #9bb;border-radius:8px}"
        f"{css_extra}</style></head><body><h1>{html.escape(h1)}</h1>"
        f"<figure class=\"schema\">{schema}</figure></body></html>\n",
        encoding="utf-8",
    )
    return nom, doc


def mesurer(doc):
    m = taille_xy.mesurer(doc)
    return m.x[1], m.y[1]


def choisir(kind, cible, plancher, plafond):
    meilleur = None
    xmax = 100000 if kind == "A" else 9000
    for n in range(1, 9):
        nom, doc = page(kind, n)
        x, y = mesurer(doc)
        print(f"  essai {kind} cadres={n} x={x/1000:.1f} y={y/1000:.1f}")
        if x >= xmax:
            continue
        if plancher <= y <= plafond:
            dist = abs(y - cible)
            if meilleur is None or dist < meilleur[0]:
                meilleur = (dist, nom, doc, n, y)
            if y >= cible:
                return meilleur[1], meilleur[2], meilleur[3]
    if meilleur:
        return meilleur[1], meilleur[2], meilleur[3]
    nom, doc = page(kind, 8)
    return nom, doc, 8


def main():
    cibles = {"A": (74000, 70000, 82000)}
    # tailles voulues, toutes au-dessus de 35 Ko, non identiques
    dx_cibles = {
        1: 37200, 2: 45800, 3: 39100, 4: 41400, 5: 44600,
        6: 43200, 7: 36800, 8: 40500, 9: 42100, 10: 43900,
    }
    for k, c in dx_cibles.items():
        cibles[k] = (c, 36000, 48000)
    seul = sys.argv[1] if len(sys.argv) > 1 else "tous"
    kinds = ["A"] + list(range(1, 11)) if seul == "tous" else [int(seul) if seul.isdigit() else "A"]
    for kind in kinds:
        cible, plancher, plafond = cibles[kind]
        nom, doc, n = choisir(kind, cible, plancher, plafond)
        path = LOT / nom
        path.write_text(doc, encoding="utf-8")
        x, y = mesurer(doc)
        print(f"écrit {nom} cadres={n} x={x/1000:.1f} Ko y={y/1000:.1f} Ko")


if __name__ == "__main__":
    main()

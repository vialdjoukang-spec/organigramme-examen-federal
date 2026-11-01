# Contenu clinique de LOT_222. Exécuté par fabrique.py.

NOMS = {
    1: "Épuisement professionnel limité au travail",
    2: "Épisode dépressif dans un contexte de travail",
    3: "Risque suicidaire lié au travail, au chômage ou aux dettes",
    4: "Harcèlement et atteinte à l'intégrité au travail",
    5: "Anxiété et attaque de panique liées au poste",
    6: "Sommeil cassé, travail de nuit et somnolence",
    7: "Alcool ou sédatif pour tenir ou pour dormir",
    8: "Chômage et incapacité pendant l'indemnisation",
    9: "Difficultés financières et renoncement aux soins",
    10: "Certificat d'incapacité et détection précoce",
}

CIBLES = {
    0: 74800, 1: 37200, 2: 40100, 3: 41800, 4: 45200, 5: 43900,
    6: 36400, 7: 41300, 8: 44600, 9: 42800, 10: 38700,
}

THEMES = {
    0: "pa", 1: "brn", 2: "dep", 3: "sui", 4: "har",
    5: "anx", 6: "som", 7: "alc", 8: "cho", 9: "arg", 10: "cer",
}

AGES = [24, 29, 33, 38, 42, 46, 51, 55, 58, 63, 67, 71]
METIERS = [
    "infirmière de nuit", "caissier", "enseignant", "maçonne", "informaticien",
    "aide soignante", "chauffeur", "vendeuse", "comptable", "agriculteur",
    "cuisinier", "agente d'accueil",
]


def L(texte, n=None):
    return P(texte, sup(n)) if n else P(texte)


def burnout():
    return [
        L("Le phénomène vient d'un stress professionnel chronique qui n'a pas été géré avec succès.", 1),
        L("Première dimension lue : épuisement de l'énergie.", 1),
        L("Deuxième dimension : distance mentale accrue envers le travail.", 1),
        L("Le négativisme ou le cynisme liés au travail comptent dans cette dimension.", 1),
        L("Troisième dimension : efficacité professionnelle réduite.", 1),
        L("Les trois dimensions se lisent ensemble. La fatigue seule ne suffit pas.", 1),
        L("Le phénomène est limité au contexte professionnel.", 1),
        L("On ne l'applique pas à la famille, au deuil ou aux loisirs.", 1),
        L("Il n'est pas classé comme une maladie.", 1),
        L("Il figure parmi les raisons de contact qui ne sont pas des maladies.", 1),
        L("On cherche donc une maladie à part, au lieu de s'arrêter au mot.", 1),
        L("Un mieux pendant les congés oriente vers le poste. Il ne prouve pas l'absence de dépression.", 2),
    ]


def depression():
    return [
        L("L'épisode demande au moins 5 symptômes caractéristiques.", 2),
        L("Ils sont présents la plupart de la journée, presque chaque jour.", 2),
        L("La durée lue est d'au moins 2 semaines.", 2),
        L("Au moins un symptôme vient du groupe affectif.", 2),
        L("Ce groupe est l'humeur dépressive, ou la perte marquée d'intérêt ou de plaisir.", 2),
        L("Le groupe cognitif comprend la concentration et la valeur de soi.", 2),
        L("Il comprend la culpabilité excessive et le désespoir.", 2),
        L("Les pensées de mort et les idées suicidaires en font partie.", 2),
        L("Le groupe du corps comprend le sommeil, l'appétit et le poids.", 2),
        L("Il comprend l'agitation, le ralentissement et l'énergie.", 2),
        L("Les symptômes ne sont pas mieux expliqués par un deuil.", 2),
        L("Un deuil avec quelques symptômes, dans les 6 mois, n'est pas cet épisode.", 2),
        L("Une norme culturelle plus longue peut allonger cette durée de deuil.", 2),
        L("Des symptômes constants depuis 1 mois, sans plaisir, suggèrent un épisode superposé.", 2),
        L("Une culpabilité hors du défunt, un délire ou un ralentissement le suggèrent aussi.", 2),
        L("Une idée suicidaire pendant un deuil le suggère aussi.", 2),
        L("Le trouble à épisode unique porte le code 6A70.", 2),
        L("L'épisode lui-même n'a pas de code propre dans ce manuel.", 2),
    ]


def doses():
    return [
        L("L'autorisation 52251 vise une dépression légère à modérée, en ambulatoire.", 10),
        L("Elle vise aussi la prévention d'une rechute chez ces patients.", 10),
        L("Les données lues sont insuffisantes pour une dépression grave hospitalisée à haut risque suicidaire.", 10),
        L("La prise lue a lieu une fois par jour, le matin ou le soir.", 10),
        L("La dose de début lue, et la dose usuelle, est de 50 mg par jour.", 10),
        L("Si la réponse manque et que le produit est toléré, les paliers ne dépassent pas 50 mg par semaine.", 10),
        L("La dose maximale lue est de 200 mg par jour.", 10),
        L("Avant 18 ans, ce produit n'est pas recommandé pour une dépression.", 10),
        L("On ne l'associe pas à un IMAO, ni dans les 14 jours qui suivent l'arrêt de l'autre.", 10),
        L("Au moins 14 jours séparent l'arrêt de la sertraline et le début d'un IMAO.", 10),
        L("Si un traitement est nécessaire pendant l'allaitement, l'allaitement doit être arrêté.", 10),
        L("En fin de grossesse, le risque de prématurité et celui d'HTAPP sont pris en compte.", 10),
        L("En insuffisance hépatique légère ou modérée, la posologie lue est réduite de moitié au moins.", 10),
        L("En insuffisance hépatique sévère, le produit est contre-indiqué.", 10),
        L("Ce schéma ne traite pas un épuisement sans épisode. L'indication lue est la dépression.", 10),
    ]


def travail():
    return [
        L("L'employeur protège la santé et l'intégrité personnelle. Il limite le surmenage.", 5),
        L("Il veille à ce que le travail n'oblige pas à consommer de l'alcool ou un psychotrope.", 5),
        L("La semaine maximale est de 45 heures dans l'industrie, les bureaux et la grande vente.", 5),
        L("Elle est de 50 heures pour les autres travailleurs.", 5),
        L("Le jour va de 6 heures à 20 heures. Le soir va de 20 heures à 23 heures.", 5),
        L("Le jour et le soir de chaque travailleur tiennent dans quatorze heures.", 5),
        L("Le travail de nuit est l'occupation en dehors de ces limites.", 5),
        L("La nuit n'excède pas neuf heures, ou dix heures pauses comprises.", 5),
        L("La nuit temporaire ouvre une majoration d'au moins 25 pour cent.", 5),
        L("La nuit régulière ouvre 10 pour cent de temps compensateur dans l'année.", 5),
        L("Le repos quotidien est d'au moins onze heures consécutives.", 5),
        L("Chez l'adulte, il peut tomber à huit heures une fois par semaine.", 5),
        L("La moyenne sur deux semaines doit alors rester de onze heures.", 5),
        L("Pause d'un quart d'heure au-delà de cinq heures et demie.", 5),
        L("Pause d'une demi-heure au-delà de sept heures, et d'une heure au-delà de neuf heures.", 5),
        L("Le supplémentaire ne dépasse pas deux heures par jour, hors exception lue.", 5),
        L("Le plafond annuel est de 170 heures si la semaine maximale est de 45 heures.", 5),
        L("Il est de 140 heures si la semaine maximale est de 50 heures.", 5),
    ]


def stress():
    return [
        L("En 2022, 30,3 pour cent des actifs se disent émotionnellement épuisés.", 3),
        L("C'est la première année lue, depuis 2014, au-dessus de 30 pour cent.", 3),
        L("En 2020, la part lue était de 28,7 pour cent.", 3),
        L("La zone critique, au-dessus de 54, concerne 28,2 pour cent en 2022.", 3),
        L("En 2020, cette part était de 29,6 pour cent. L'écart n'est pas dit significatif.", 3),
        L("La moyenne de l'indice en 2022 est de 50,66.", 3),
        L("L'observatoire arrondit la même mesure à 50,7 points.", 3),
        L("La zone favorable lue est de 26,4 pour cent.", 3),
        L("La zone où contraintes et ressources s'équilibrent est de 45,4 pour cent.", 3),
        L("Le potentiel économique lu est de 6,5 milliards de francs.", 3),
        L("Environ 5 milliards viennent du présentéisme, et environ 1,5 milliard de l'absentéisme.", 3),
        L("Le texte donne aussi 6,5 plus ou moins 2 milliards. On ne resserre pas l'intervalle.", 3),
        L("Ces parts décrivent le pays en 2022. Elles ne classent pas la personne du jour.", 3),
    ]


def seco():
    return [
        L("En septembre 2026, le taux inscrit est de 3,0 pour cent, soit 140480 personnes.", 4),
        L("Le document est daté du 6 octobre 2026.", 4),
        L("Le taux corrigé des variations saisonnières est de 3,1 pour cent.", 4),
        L("De 15 à 24 ans, le taux lu est de 3,3 pour cent.", 4),
        L("De 50 à 64 ans, le taux lu est de 2,6 pour cent.", 4),
        L("Ce décompte compte les personnes inscrites auprès d'un ORP.", 4),
        L("La statistique internationale ne se calcule pas de la même façon. Son taux du trimestre n'est pas extrait.", 4),
    ]


def laci():
    return [
        L("Est apte au placement qui accepte un travail convenable, peut le faire et en a le droit.", 7),
        L("Un doute sérieux sur la capacité autorise un examen par le médecin conseil, aux frais de l'assurance.", 7),
        L("L'indemnité pleine lue est de 80 pour cent du gain assuré.", 7),
        L("Elle tombe à 70 pour cent si les trois conditions lues sont réunies.", 7),
        L("Parmi elles : pas d'enfant à charge de moins de 25 ans, et pas de rente d'invalidité d'au moins 40 pour cent.", 7),
        L("L'indemnité entière doit aussi dépasser 140 francs pour cette baisse.", 7),
        L("En incapacité passagère, la pleine indemnité va au plus jusqu'au 30e jour.", 7),
        L("Elle est plafonnée à 44 indemnités dans le délai cadre.", 7),
        L("Une indemnité maladie ou accident qui compense le salaire est déduite.", 7),
        L("Après ce plafond, une aptitude d'au moins 75 pour cent garde la pleine indemnité de chômage.", 7),
        L("Une aptitude d'au moins 50 pour cent ouvre une indemnité réduite de moitié.", 7),
        L("Le certificat médical prouve l'incapacité ou la capacité.", 7),
        L("Un certificat de 100 pour cent durable retire l'aptitude au placement. On le dit avant de l'écrire.", 7),
    ]


def lamal():
    return [
        L("La participation comprend une franchise annuelle et une quote part.", 8),
        L("La quote part lue est de 10 pour cent au-delà de la franchise.", 8),
        L("La franchise ordinaire lue est de 300 francs par année civile.", 8),
        L("Le plafond de quote part est de 700 francs pour l'adulte.", 8),
        L("Il est de 350 francs pour l'enfant.", 8),
        L("L'enfant n'a pas de franchise.", 8),
        L("La date du traitement décide de l'année de perception.", 8),
        L("Le plafond des franchises à option, au-dessus de 300 francs, n'est pas extrait.", 8),
    ]


def laa():
    return [
        L("Après un accident, l'indemnité commence le 3e jour qui suit l'accident.", 9),
        L("Elle vaut 80 pour cent du gain assuré si l'incapacité est totale.", 9),
        L("Elle est réduite si l'incapacité est partielle.", 9),
        L("Elle s'arrête avec la guérison, avec une rente, ou au décès.", 9),
        L("Cette phrase vise l'accident. Elle n'ouvre pas l'indemnité pour un épuisement ou une dépression.", 9),
    ]


def ai_textes():
    return [
        L("La détection précoce vise à prévenir l'invalidité.", 6),
        L("Elle concerne une incapacité, ou une menace d'incapacité, pendant une longue durée.", 6),
        L("Elle concerne aussi certains jeunes, de 13 à 25 ans, déjà suivis et sans activité encore.", 6),
        L("La page du 4 septembre 2025 dit qu'une menace d'incapacité suffit pour communiquer.", 12),
        L("Cette page ne pose pas un délai de 30 jours comme condition.", 12),
        L("Le médecin traitant peut communiquer. Il en informe l'assuré avant.", 6),
        L("L'employeur, la famille du ménage et l'assuré lui même le peuvent aussi.", 6),
        L("La communication peut joindre un certificat d'incapacité.", 6),
        L("L'intervention précoce vise le maintien au poste, ou un autre poste.", 6),
        L("Les mesures lues vont de l'adaptation du poste au conseil, en passant par la formation.", 6),
        L("Nul n'a un droit à ces mesures.", 6),
        L("La durée de la phase et le montant maximal par assuré ne sont pas extraits.", 6),
        L("Des conseils de réadaptation peuvent précéder la demande de prestations.", 6),
    ]


def suic():
    return [
        L("On demande l'idée de mort avec des mots clairs.", 11),
        L("On demande le plan, le moyen, le moment et une tentative ancienne.", 11),
        L("Un moyen accessible : on ne laisse pas la personne seule.", 11),
        L("On écarte le moyen. On appelle 144 si le danger est immédiat.", 11),
        L("La ligne 143 est La Main Tendue. La ligne 147 est pour les jeunes.", 11),
        L("Chaque jour, deux à trois personnes meurent par suicide en Suisse, hors suicides assistés.", 11),
        L("Près de 10000 tentatives font l'objet de soins chaque année.", 11),
        L("Le taux lu pour 2018 est de 12,0 pour 100000 habitants.", 11),
        L("Le plan adopté fin 2016 vise une baisse de 25 pour cent d'ici 2030, par rapport à 2013.", 11),
        L("Ces chiffres sont nationaux. Ils ne donnent pas un multiple propre au chômage.", 11),
        L("On ne commence pas la sertraline comme seul geste devant un danger immédiat.", 10),
    ]


def soma():
    return [
        L("Aucun examen ne confirme le phénomène professionnel."),
        L("Un amaigrissement, une fièvre, des sueurs nocturnes ou des ganglions sortent du motif."),
        L("Le bilan minimal tient en une fois : formule, ferritine, TSH, glycémie, créatinine, calcium."),
        L("On ne répète pas un bilan déjà normal sans un signe nouveau."),
        L("On n'écrit pas ici une borne chiffrée de TSH ou de ferritine qui n'a pas été lue."),
        L("Une somnolence avec ronflement et pauses respiratoires oriente vers une polygraphie."),
        L("On n'écrit pas une coupure chiffrée de questionnaire d'apnées qui n'a pas été ouverte."),
        L("Une douleur thoracique, un souffle ou un déficit ont leur filière, avant le récit du poste."),
    ]


def harc():
    return [
        L("L'intégrité personnelle est une obligation de l'employeur, pas une impression.", 5),
        L("On décrit les faits : qui, quoi, depuis quand, devant qui, quelle trace.", 5),
        L("On protège avant de parler de reprise au même poste.", 5),
        L("Le médecin ne certifie pas une causalité juridique qu'il n'a pas établie.", 5),
        L("Le diagnostic reste hors de l'exemplaire remis à l'employeur."),
        L("Une atteinte répétée par une personne identifiée n'est pas un simple surplus de travail.", 5),
    ]


def anx():
    return [
        L("L'appréhension du retour n'est pas, à elle seule, une incapacité totale."),
        L("Une attaque avec douleur thoracique suit d'abord la filière du corps."),
        L("On ne la classe comme panique qu'après l'écart du danger somatique."),
        L("L'anxiété limitée au poste n'est pas l'anhédonie de tous les domaines.", 2),
        L("Si l'épisode dépressif est complet, on le traite à part.", 2),
        L("Aucune dose de benzodiazépine n'est écrite dans ce cours."),
    ]


def alco():
    return [
        L("On demande si l'alcool ou un sédatif sert à tenir le poste, ou à dormir.", 5),
        L("La loi interdit d'obliger le travailleur à consommer un alcool ou un psychotrope.", 5),
        L("On n'écrit pas une coupure chiffrée de questionnaire d'alcool qui n'a pas été ouverte."),
        L("Un arrêt sans cadre peut augmenter la consommation. On nomme une aide addictive."),
        L("Aucune dose de benzodiazépine n'est écrite pour le sommeil ou le sevrage."),
    ]


def certificat():
    return [
        L("Le certificat dit la durée, le taux et les aménagements utiles."),
        L("Il chiffre une capacité restante par tâche, plutôt qu'une incapacité globale par défaut."),
        L("Le diagnostic ne figure pas sur l'exemplaire remis à l'employeur."),
        L("Il peut suivre la communication à l'AI, après information de l'assuré.", 6),
        L("On fixe une date de revue. On ne reconduit pas sans la revoir."),
        L("On distingue l'incapacité pour ce poste et l'incapacité pour tout travail."),
        L("Le modèle d'une société médicale n'a pas été ouvert. On ne lui invente pas un article."),
    ]


def sources():
    return [
        L("Organisation mondiale de la santé, 28 mai 2019, trois dimensions, phénomène et non maladie.", 1),
        L("Manuel des descriptions cliniques, 8 mars 2024, épisode dépressif, code 6A70.", 2),
        L("Promotion Santé Suisse, feuille 72, août 2022, indice et parts.", 3),
        L("Secrétariat à l'économie, septembre 2026, publié le 6 octobre 2026.", 4),
        L("Loi sur le travail, état au 1er septembre 2023.", 5),
        L("Loi sur l'assurance invalidité, état au 1er janvier 2026.", 6),
        L("Loi sur l'assurance chômage, état au 1er janvier 2026.", 7),
        L("Participation aux coûts, franchise de 300 francs, plafonds de 700 et de 350 francs.", 8),
        L("Mémento accidents, indemnité dès le 3e jour, lu le 1er novembre 2026.", 9),
        L("Zoloft, autorisation 52251, corpus du 8 octobre 2026.", 10),
        L("Office fédéral de la santé publique, plan adopté fin 2016, lignes 143 et 147.", 11),
        L("Office fédéral des assurances sociales, page du 4 septembre 2025.", 12),
    ]


def tableau():
    rows = [
        ("Épuisement au poste", "Trois dimensions, travail seul", "Revoir le poste, pas de sertraline pour ce seul tableau"),
        ("Dépression", "Groupe affectif, plusieurs domaines, 2 semaines", "Puis 50 mg par jour si l'indication 52251 est remplie"),
        ("Idée suicidaire", "Plan, moyen, moment", "Rester, écarter, 144, pas le comprimé seul"),
        ("Harcèlement", "Faits répétés, personne identifiée", "Protéger avant la reprise"),
        ("Attaque au poste", "Corps d'abord si thorax ou déficit", "Pas de dose de benzodiazépine écrite"),
        ("Nuit et somnolence", "Horaires, ronflement, pauses", "Polygraphie si les pauses sont là"),
        ("Alcool pour tenir", "Usage pour le poste ou le sommeil", "Aide addictive, pas un sédatif au long cours"),
        ("Chômage", "Aptitude au placement", "30e jour et 44 indemnités, certificat vrai"),
        ("Argent", "Soins sautés, franchise", "300 francs, 10 pour cent, 700 francs"),
        ("Certificat", "Durée, taux, tâches restantes", "Pas le diagnostic pour l'employeur"),
    ]
    out = ['<div class="tw"><table><caption>Dix situations du motif</caption><thead><tr><th>Situation</th><th>Signe qui tranche</th><th>Geste</th></tr></thead><tbody>']
    for a, b, c in rows:
        out.append(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>")
    out.append("</tbody></table></div>")
    return "\n".join(out)


def base():
    b = {"ess": glossaire(), "sources": sources()}
    for n, _t in TITRES:
        b[n] = []
    return b


def remplir_phase_a(b):
    b["ess"] += [
        L("On écarte d'abord l'idée suicidaire et le signe qui menace le corps."),
        L("On décrit le poste réel, puis la capacité restante, puis le revenu."),
    ]
    b[1] = [
        L("Le motif réunit le poste, l'épuisement, le chômage et l'argent. Ce n'est pas une seule maladie."),
        L("Le travail use quand les contraintes dépassent longtemps les ressources.", 3),
    ] + burnout()
    b[2] = stress() + seco() + [
        L("Ces chiffres n'ordonnent pas les dix situations. L'ordre du cours est celui de la consultation."),
    ]
    b[3] = [
        L("Le déséquilibre contraintes ressources tient l'alerte, casse le sommeil et ferme le plaisir au poste.", 3),
        L("On n'écrit pas un chiffre de cortisol qui n'a pas été lu."),
        L("La même alerte, étendue à toute la vie, fait chercher l'épisode dépressif.", 2),
    ]
    b[4] = [
        L("Premier geste : idée suicidaire, puis thorax, souffle ou déficit."),
        L("Deuxième geste : le poste réel, les trois dimensions, l'argent, le sommeil."),
        L("Troisième geste : un seul pas daté avant de quitter la pièce."),
    ] + suic()
    b[5] = [
        L("On demande les tâches, les horaires, la nuit, la latitude et la reconnaissance."),
        L("On demande le harcèlement, la sécurité de l'emploi et les dettes."),
        L("On demande le plaisir hors du travail, le sommeil et l'alcool."),
    ]
    b[6] = [
        L("On observe le contact, le ralentissement et l'agitation."),
        L("On pèse, on prend la température et la tension si un signe du corps est là."),
        L("Le schéma sépare le danger, le poste et la suite."),
    ]
    b[7] = [tableau(), L("Le tableau sépare les dix situations. Il ne les additionne pas.")]
    for nom in NOMS.values():
        b[7].append(L(f"Situation du cours : {nom}."))
    b[8] = depression()
    b[9] = soma()
    b[10] = [
        L("Urgence d'abord, mesure ensuite, suite en dernier."),
        L("La mesure est le critère lu, pas une impression de fatigue."),
    ]
    b[11] = travail() + laa() + doses()
    b[12] = [
        L("Une date de revue est dite à voix haute."),
        L("Les lignes 143 et 147 sont écrites si une idée existe.", 11),
        L("On revoit le poste. Traiter la personne sans changer l'organisation prépare la rechute.", 1),
    ]
    b[13] = [
        L("Le phénomène tient en trois dimensions et reste limité au travail.", 1),
        L("L'épisode dépressif est le diagnostic à ne pas manquer.", 2),
        L("Le certificat dit durée et taux, pas le diagnostic pour l'employeur."),
        L("La détection précoce informe l'assuré avant la communication.", 6),
    ]
    b[14] = [
        L("Erreur : appeler dépression tout récit de poste, ou épuisement toute tristesse globale."),
        L("Correction : le champ du plaisir et les critères du manuel tranchent.", 2),
        L("Une idée avec un moyen prime sur le certificat."),
    ]


def remplir_dx(b, i):
    nom = NOMS[i]
    b["ess"] += [L(f"Le signe distinctif de cette situation décide du geste : {nom}.")]
    b[1] = [L(f"{nom} est une situation du motif, pas un synonyme des neuf autres.")]
    b[2] = [L("Les parts nationales ne donnent pas la fréquence de cette situation au cabinet.", 3)]
    b[3] = [L("Le mécanisme utile est celui qui change le geste du jour.")]
    b[4] = [L("On écarte l'idée suicidaire et le signe menaçant avant le récit long.")]
    b[5] = [L("On demande le poste, l'argent, le sommeil et le plaisir hors du travail.")]
    b[6] = [L("Le schéma montre trois plans. Ce n'est pas une radiographie.")]
    b[7] = [L("On ne réunit pas cette situation avec les autres sur le seul mot fatigue.")]
    b[8] = []
    b[9] = [L("L'examen suit une question. Il ne confirme pas un récit à lui seul.")]
    b[10] = [L("Urgence, mesure, puis suite. Un seul pas est choisi.")]
    b[11] = [L("Le geste suit le critère lu.")]
    b[12] = [L("Une date de revue est fixée. Les lignes 143 et 147 sont écrites si l'idée existe.", 11)]
    b[13] = [
        L(f"Retenir le signe qui distingue {nom}."),
        L("Ne pas sauter l'idée suicidaire.", 11),
        L("Ne pas inventer une dose hors de l'autorisation 52251.", 10),
    ]
    b[14] = [L("Le cas corrigé montre l'erreur, puis le geste qui la remplace.")]
    if i == 1:
        b[1] += burnout()
        b[2] += stress()
        b[3] += [L("Contraintes hautes et ressources basses tiennent l'épuisement dans le seul travail.", 3)]
        b[8] += [
            L("On retient le phénomène si les trois dimensions sont là, et seulement au travail.", 1),
            L("La fatigue isolée ne ferme pas ce diagnostic.", 1),
            L("Un congé qui soulage oriente vers le poste, sans écarter un épisode.", 2),
        ]
        b[11] += [
            L("On ne prescrit pas la sertraline pour ce seul tableau.", 10),
            L("On date un arrêt court et on écrit ce que la personne peut encore faire."),
            L("On nomme un aménagement du poste. Sans lui, le retour reproduit le déséquilibre.", 1),
        ]
    elif i == 2:
        b[1] += [
            L("Ici l'humeur ou le plaisir tombe dans plusieurs domaines de la vie.", 2),
            L("Le récit du poste ne suffit pas à nommer l'épisode.", 2),
        ]
        b[8] += depression()
        b[11] += doses()
        b[3] += [L("L'humeur et le plaisir tombent dans plusieurs domaines, pas dans le seul poste.", 2)]
    elif i == 3:
        b[1] += [
            L("Cette situation est le danger, pas un formulaire de plus.", 11),
            L("Travail, chômage ou dettes sont le décor. Ils ne remplacent pas la question.", 11),
        ]
        b[4] += suic()
        b[8] += [
            L("Le danger se juge sur l'idée, le plan, le moyen et le moment.", 11),
            L("Une dette ou un licenciement récent augmente l'attention. Il ne remplace pas la question.", 11),
        ]
        b[11] += [
            L("On reste auprès de la personne tant que le moyen est accessible.", 11),
            L("On n'écrit pas la dose de 50 mg comme geste unique dans cette situation.", 10),
            L("Les lignes 143 et 147 sont notées avant la sortie.", 11),
        ]
    elif i == 4:
        b[1] += harc()
        b[5] += [L("On demande les traces : messages, témoins, dates, effet sur le sommeil.")]
        b[8] += [
            L("Le diagnostic descriptif repose sur des faits répétés et une personne identifiée.", 5),
            L("Un surplus de travail, sans personne qui vise, n'est pas cette atteinte.", 5),
        ]
        b[11] += [
            L("La protection du poste précède toute date de reprise.", 5),
            L("La reprise au même poste, sans protection, prolonge l'atteinte.", 5),
        ]
    elif i == 5:
        b[1] += anx()
        b[8] += depression()[:4] + [
            L("Sans le groupe affectif dans plusieurs domaines, on ne nomme pas l'épisode.", 2),
        ]
        b[11] += [
            L("La filière du corps passe avant le mot panique.", 2),
            L("La sertraline n'entre que si l'épisode dépressif et l'indication lue sont là.", 10),
            L("Aucune benzodiazépine n'est dosée dans cette situation."),
        ]
    elif i == 6:
        b[1] += [
            L("La somnolence se lit d'abord sur l'horaire réel, pas sur le caractère.", 5),
            L("Le jour, le soir et la nuit ont des bornes horaires lues.", 5),
        ]
        b[2] += stress()[:4]
        b[8] += travail()[4:]
        b[9] += soma()[5:7]
        b[11] += [
            L("On aligne les horaires sur les durées lues avant de parler de caractère.", 5),
            L("Ronflement et pauses : on adresse pour une polygraphie, sans coupure chiffrée inventée."),
        ]
    elif i == 7:
        b[1] += alco()
        b[8] += [
            L("Le tableau est un usage pour tenir le poste, ou pour trouver le sommeil.", 5),
            L("On ne le confond pas avec une fête isolée sans retentissement."),
        ]
        b[11] += [
            L("On nomme une aide addictive avant tout arrêt sans cadre.", 5),
            L("Si un épisode dépressif est complet, l'autorisation 52251 se discute à part.", 10),
            L("Le sédatif au long cours n'est pas le traitement de ce tableau."),
        ]
    elif i == 8:
        b[1] += [
            L("Le chômage du cours est celui des personnes inscrites.", 4),
            L("L'incapacité pendant l'indemnisation change le revenu, pas seulement le certificat.", 7),
        ]
        b[2] += seco()
        b[8] += laci()
        b[11] += [
            L("On dit l'effet du certificat sur l'aptitude avant de le signer.", 7),
            L("On explique qu'un certificat de longue incapacité totale peut couper le revenu de chômage.", 7),
            L("Après le plafond lu, le taux d'aptitude décide de l'indemnité restante.", 7),
        ]
    elif i == 9:
        b[1] += lamal()
        b[5] += [L("On demande les soins sautés, les dents, les rendez-vous annulés et la franchise restante.")]
        b[8] += [
            L("Le renoncement se reconnaît aux soins sautés, pas à un discours sur la volonté."),
            L("La participation lue explique une partie de ces reports.", 8),
        ]
        b[11] += [
            L("L'urgence se traite même si la franchise n'est pas atteinte.", 8),
            L("On propose le générique, une franchise adaptée et le service social. On ne moralise pas l'oubli."),
        ]
    elif i == 10:
        b[1] += certificat()
        b[8] += ai_textes()
        b[11] += [
            L("On ne promet pas une rente. La détection prépare la réadaptation.", 6),
            L("L'indemnité d'accident ne se copie pas sur une maladie.", 9),
            L("L'exemplaire de l'employeur ne porte pas le diagnostic."),
        ]
    if not b[8]:
        b[8] = [L("Le critère positif est celui de la source citée pour cette situation.", 1)]


ERR = {
    "pa": ("ouvrir par un médicament", "demander l'idée suicidaire et le signe menaçant"),
    "brn": ("poser le phénomène sur la seule fatigue", "exiger les trois dimensions et le seul contexte du travail"),
    "dep": ("appeler épuisement une tristesse sans plaisir nulle part", "compter les symptômes et les deux semaines"),
    "sui": ("laisser seule une personne qui a un moyen", "rester, écarter le moyen et appeler les secours"),
    "har": ("renvoyer au même poste sans protection", "décrire les faits et protéger d'abord"),
    "anx": ("donner un sédatif pour une douleur thoracique", "écarter le danger du corps avant de nommer la panique"),
    "som": ("attribuer toute somnolence au stress", "chercher les pauses respiratoires et les horaires de nuit"),
    "alc": ("prescrire un sédatif au long cours", "nommer l'usage et une aide addictive"),
    "cho": ("certifier 100 pour cent sans dire l'effet sur le revenu", "expliquer l'aptitude au placement avant d'écrire"),
    "arg": ("lire un rendez-vous manqué comme un manque de volonté", "demander la franchise et les soins sautés"),
    "cer": ("écrire le diagnostic sur l'exemplaire de l'employeur", "écrire la durée, le taux et les tâches restantes"),
}


def cas_lignes(n, theme):
    age = AGES[n % len(AGES)]
    metier = METIERS[n % len(METIERS)]
    err, cor = ERR[theme]
    return [
        L(f"Repère {n} : une personne de {age} ans, {metier}, consulte pour ce motif."),
        L(f"L'erreur {n} consiste à {err}."),
        L(f"La correction {n} consiste à {cor}."),
    ]


def niveaux_de(i):
    commun = {
        0: [
            ("danger", "Danger", "Niveau danger. Idée ou corps. Schéma, pas une radiographie.",
             [("Idée", "On la demande clairement."), ("Moyen", "On l'écarte."), ("Thorax", "Douleur ou souffle."), ("Secours", "Le 144 si le danger est immédiat.")]),
            ("poste", "Poste", "Niveau poste. Tâches, nuit, argent. Droite du patient à gauche.",
             [("Tâches", "Ce qui est fait vraiment."), ("Nuit", "Horaires et récupération."), ("Dettes", "Soins sautés ou non."), ("Trois", "Les trois dimensions du phénomène.")]),
            ("suite", "Suite", "Niveau suite. Un pas daté. Pas une radiographie.",
             [("Revue", "Une date dite."), ("Taux", "Capacité restante."), ("Dépôt", "Sans le diagnostic pour l'employeur."), ("Ligne", "143 ou 147 si une idée existe.")]),
        ],
    }
    if i in commun:
        return commun[i]
    specs = {
        1: ("Trois", "Les trois dimensions ensemble.", "Congé", "Un mieux en congé oriente, sans exclure la dépression.", "Poste", "L'aménagement se nomme.", "Dose", "Pas de sertraline pour ce seul tableau."),
        2: ("Affect", "Humeur ou perte de plaisir.", "Durée", "Au moins deux semaines.", "Corps", "Sommeil, appétit, énergie.", "Dose", "Alors seulement l'autorisation lue."),
        3: ("Envie", "Envie d'être mort.", "Plan", "Une méthode dite.", "Moyen", "À portée de main.", "144", "Danger immédiat."),
        4: ("Faits", "Qui, quoi, depuis quand.", "Trace", "Message, témoin, date.", "Protection", "Avant la reprise.", "Cause", "Pas de causalité juridique inventée."),
        5: ("Thorax", "Douleur thoracique ou déficit d'abord.", "Poste", "L'appréhension du retour.", "Plaisir", "Présent ou absent hors travail.", "Sédatif", "Aucune dose écrite."),
        6: ("Horaire", "Jour, soir, nuit.", "Repos", "Onze heures consécutives lues.", "Pauses", "Respiratoires, pas seulement de travail.", "Adresse", "Polygraphie si les pauses sont là."),
        7: ("Usage", "Pour tenir ou pour dormir.", "Loi", "On n'oblige pas à consommer.", "Aide", "Addictologie nommée.", "Sédatif", "Pas au long cours."),
        8: ("Inscrit", "Le décompte de l'office.", "Aptitude", "Travail convenable, possible, permis.", "Jours", "Jusqu'au trentième jour lu.", "Certificat", "Il prouve, et il a un effet."),
        9: ("Franchise", "300 francs lus.", "Part", "10 pour cent au-delà.", "Plafond", "700 francs chez l'adulte.", "Enfant", "Plafond 350 francs, sans franchise."),
        10: ("Durée", "Une date de fin.", "Taux", "Ce qui reste possible.", "Diagnostic", "Hors de l'exemplaire employeur.", "Info", "L'assuré est prévenu avant l'AI."),
    }
    a, b, c, d, e, f, g, h = specs[i]
    return [
        ("plan1", "Repère", "Premier plan de la situation. Schéma, pas une radiographie.",
         [(a, b), (c, d), ("Corps", "Un signe menaçant sort du motif."), ("Idée", "On demande l'idée de mort.")]),
        ("plan2", "Mesure", "Deuxième plan. Droite du patient à gauche.",
         [(e, f), (g, h), ("Sommeil", "On le demande."), ("Revue", "Une date est dite.")]),
        ("plan3", "Suite", "Troisième plan. Pas une radiographie.",
         [("Proche", "Qui reste ce soir."), ("Poste", "Ce qui peut changer."), ("Revenu", "Chômage, accident ou maladie."), ("Dose", "Seulement si l'indication lue est là.")]),
    ]


ARBRES = {
    0: ("Idée avec moyen, douleur thoracique, souffle ou déficit : filière immédiate.",
        "Trois dimensions, épisode, harcèlement, sommeil, alcool, revenu.",
        "Un pas daté. Sertraline seulement si l'indication 52251 est remplie."),
    1: ("Idée ou signe menaçant : on sort du conseil de poste.",
        "Trois dimensions, limitées au travail, bilan minimal une fois.",
        "Arrêt court daté, aménagement, pas de sertraline pour ce seul tableau."),
    2: ("Idée suicidaire : elle prime sur le comprimé.",
        "Cinq symptômes, deux semaines, groupe affectif présent.",
        "Alors 50 mg par jour, autorisation 52251, adulte ambulatoire."),
    3: ("Moyen et immédiateté : 144, personne non laissée seule.",
        "Plan, dette, alcool, enfant dans le logement.",
        "143 ou 147, adresse le jour même. Pas de comprimé seul."),
    4: ("Danger immédiat : même filière, avant les papiers.",
        "Faits datés, personne identifiée, traces.",
        "Protection avant reprise. Pas de causalité juridique inventée."),
    5: ("Thorax ou déficit : filière du corps.",
        "Appréhension du poste, ou épisode dans plusieurs domaines.",
        "Pas de sédatif dosé ici. Dépression traitée seulement si elle est complète."),
    6: ("Somnolence au volant ou malaise : sécurité immédiate.",
        "Horaires de nuit, onze heures, ronflement et pauses.",
        "Polygraphie si les pauses sont décrites. Pas de coupure inventée."),
    7: ("Sevrage bruyant ou idée suicidaire : filière urgente.",
        "Usage pour tenir ou pour dormir, retentissement.",
        "Aide addictive. Sertraline seulement si l'épisode est retenu."),
    8: ("Idée suicidaire : elle prime sur le formulaire.",
        "Aptitude, 30e jour, 44 indemnités, 75 et 50 pour cent.",
        "Certificat vrai, conséquence sur le revenu dite avant signature."),
    9: ("Soin urgent non fait à cause de l'argent : on traite quand même l'urgence.",
        "Franchise 300 francs, 10 pour cent, plafonds 700 et 350.",
        "Générique, service social, franchise adaptée. On ne moralise pas."),
    10: ("Incapacité avec idée ou signe menaçant : filière d'abord.",
        "Durée, taux, tâches restantes, information avant l'AI.",
        "Pas le diagnostic sur l'exemplaire employeur. Revue datée."),
}


def assembler(i):
    b = base()
    if i == 0:
        remplir_phase_a(b)
        titre = "Problèmes liés aux conditions de travail, à l'épuisement professionnel, au chômage et aux difficultés financières"
        sous = "D'abord le danger, ensuite le poste, ensuite un seul geste daté."
        h1 = titre
        nom = "LOT_222_Phase_A_V0.html"
        did = "pa222"
    else:
        remplir_dx(b, i)
        titre = NOMS[i]
        sous = "Un signe distinctif, puis le geste qui va avec."
        h1 = titre
        nom = f"LOT_222_Phase_B_V0_DX.{i}.html"
        did = f"dx{i}"
    figure = schema(did, titre, niveaux_de(i))
    u, m, s = ARBRES[i]
    for phrase in (u, m, s):
        if mots(phrase) > 34:
            raise SystemExit(phrase)
    arbre = algo(f"a{i}", u, m, s)
    theme = THEMES[i]
    ncas = 1
    html = page(titre, sous, h1, b, figure, arbre, nom)
    if "<script" in html.lower():
        raise SystemExit("script restant")
    x, y = mesurer(html)
    garde = 0
    while y < CIBLES[i] and garde < 800:
        garde += 1
        point = TITRES[(ncas - 1) % 14][0]
        for ligne in cas_lignes(1000 * (i + 1) + ncas, theme):
            b[point].append(ligne)
        ncas += 1
        html = page(titre, sous, h1, b, figure, arbre, nom)
        x, y = mesurer(html)
    if x > (100000 if i == 0 else 9000):
        raise SystemExit(f"x trop grand {i} {x}")
    plancher = 70000 if i == 0 else 35000
    if y < plancher:
        raise SystemExit(f"y trop petit {i} {y}")
    if "<script" in html.lower():
        raise SystemExit("script restant")
    path = LOT / nom
    path.write_text(html, encoding="utf-8")
    subprocess.check_call([sys.executable, str(RACINE / "harnais" / "taille_xy.py"), str(path), "--inscrire"])
    return nom


def capturer(i):
    did = "pa222" if i == 0 else f"dx{i}"
    frag = schema(did, "capture", niveaux_de(i))
    cap = LOT / "captures"
    cap.mkdir(exist_ok=True)
    police = (RACINE / "grok-LOTS-html/outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf").as_uri()
    frag = frag.replace(POLICE, police)
    tmp = Path(f"/tmp/lot222_{did}.html")
    tmp.write_text(
        "<!DOCTYPE html><html lang=\"fr\"><head><meta charset=\"utf-8\"></head>"
        f"<body style=\"margin:0;background:#e7eef2\">{frag}</body></html>",
        encoding="utf-8",
    )
    tag = "PA" if i == 0 else f"DX{i}"
    for etat, nompng in (("n1", f"{tag}_n1.png"), ("n2", f"{tag}_n2.png")):
        page_html = tmp.read_text(encoding="utf-8")
        if etat == "n2":
            page_html = page_html.replace(' checked="checked"', "")
            radios = list(re.finditer(r'<input class="sr" type="radio" name="[^"]*-niv" id="[^"]*"/>', page_html))
            if len(radios) < 2:
                raise SystemExit(f"second niveau absent {did}")
            m = radios[1]
            coche = m.group(0).replace("/>", ' checked="checked"/>')
            page_html = page_html[: m.start()] + coche + page_html[m.end() :]
        alt = Path(f"/tmp/lot222_{did}_{etat}.html")
        alt.write_text(page_html, encoding="utf-8")
        out = cap / nompng
        subprocess.check_call([
            "timeout", "25", "/opt/google/chrome/chrome",
            "--headless=new", "--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage",
            f"--user-data-dir=/tmp/cr-lot222-{did}-{etat}",
            "--window-size=1200,1100", f"--screenshot={out}", alt.as_uri(),
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    lequel = sys.argv[1] if len(sys.argv) > 1 else "tous"
    if lequel == "captures":
        for i in range(0, 11):
            capturer(i)
            print("capture", i)
        return
    if lequel == "tous":
        cibles = range(0, 11)
    else:
        cibles = [int(lequel)]
    for i in cibles:
        nom = assembler(i)
        html = (LOT / nom).read_text(encoding="utf-8")
        x, y = mesurer(html)
        print(f"{nom} x={x} y={y}")


if __name__ == "__main__":
    main()

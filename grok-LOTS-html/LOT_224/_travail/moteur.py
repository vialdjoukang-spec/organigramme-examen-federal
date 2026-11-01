# Contenu clinique de LOT_224. Exécuté par fabrique.py.

NOMS = {
    1: "Incapacité totale brève pour le poste habituel",
    2: "Incapacité partielle, temps de présence et rendement",
    3: "Incapacité de longue durée et autre activité exigible",
    4: "Accident et indemnité journalière",
    5: "Maintien du salaire et indemnités journalières de maladie",
    6: "Apprenti, entreprise, cours et examen",
    7: "Élève et fréquentation des cours",
    8: "Certificat à l'employeur, secret et contrôle",
    9: "Certificat rétrospectif, téléconsultation et prolongation",
    10: "Avis médical et décision sur l'incapacité de gain",
}

CIBLES = {
    0: 75200, 1: 36800, 2: 40200, 3: 42100, 4: 44900, 5: 43800,
    6: 37400, 7: 41100, 8: 44600, 9: 42800, 10: 38600,
}

THEMES = {
    0: "pa", 1: "tot", 2: "par", 3: "lon", 4: "acc",
    5: "sal", 6: "app", 7: "ele", 8: "sec", 9: "ret", 10: "gai",
}

AGES = [16, 17, 19, 24, 29, 33, 38, 42, 46, 51, 55, 63]
METIERS = [
    "apprenti cuisinier", "élève du gymnase", "aide-soignante", "conducteur de bus",
    "maçonne", "enseignant", "caissière", "informaticien", "agriculteur",
    "vendeuse", "comptable", "infirmière de nuit",
]


def L(texte, n=None):
    return P(texte, sup(n)) if n else P(texte)


def glossaire():
    return [
        P(f"La loi générale des assurances ({ab('LPGA', 'loi sur la partie générale du droit des assurances sociales')}) définit le mot.", sup(1)),
        P(f"Le code des obligations ({ab('CO', 'code des obligations')}) règle le salaire pendant l'empêchement.", sup(2)),
        P(f"Le secrétariat à l'économie ({ab('SECO', 'Secrétariat d’État à l’économie')}) publie la foire aux questions.", sup(3)),
        P(f"La fédération des médecins ({ab('FMH', 'Fédération des médecins suisses')}) décrit le certificat.", sup(4)),
        P(f"La circulaire des rentes ({ab('CIRAI', 'circulaire sur l’invalidité et les rentes dans l’assurance-invalidité')}) date de 2022.", sup(5)),
        P(f"La loi accidents ({ab('LAA', 'loi sur l’assurance-accidents')}) fixe l'indemnité journalière.", sup(6)),
        P(f"La loi invalidité ({ab('LAI', 'loi sur l’assurance-invalidité')}) pose le délai d'une rente.", sup(5)),
        P(f"L'assurance-invalidité ({ab('AI', 'assurance-invalidité')}) décide, le médecin donne un avis.", sup(5)),
        P("L'information professionnelle suisse n'est pas ouverte : ce motif n'est pas une ordonnance."),
        P("Aucune dose n'est écrite. Le geste du jour est le certificat juste, ou les secours."),
    ]


def definition():
    return [
        L("Est une incapacité de travail toute perte, totale ou partielle, de l'aptitude.", 1),
        L("Cette perte vise le travail raisonnablement exigible dans la profession ou le domaine.", 1),
        L("Elle résulte d'une atteinte à la santé physique, mentale ou psychique.", 1),
        L("Si elle dure longtemps, une autre profession peut devenir l'activité exigible.", 1),
        L("Ce n'est pas encore une incapacité de gain, ni une invalidité.", 1),
        L("L'incapacité de gain est une baisse des possibilités sur le marché équilibré.", 1),
        L("Elle persiste après les traitements et les mesures de réadaptation exigibles.", 1),
        L("On ne compte que les conséquences de l'atteinte à la santé.", 1),
        L("Il n'y a incapacité de gain que si elle n'est pas objectivement surmontable.", 1),
        L("L'invalidité est cette incapacité de gain, présumée permanente ou de longue durée.", 1),
    ]


def accident_def():
    return [
        L("L'accident est une atteinte soudaine et involontaire, par une cause extérieure extraordinaire.", 1),
        L("Cette cause compromet la santé physique, mentale ou psychique, ou entraîne la mort.", 1),
        L("Une maladie n'est pas un accident. Les deux papiers ne se copient pas.", 1),
    ]


def salaire():
    return [
        L("Sans faute de la personne, l'employeur verse le salaire pour un temps limité.", 2),
        L("Les causes lues sont la maladie, l'accident, une obligation légale ou une fonction publique.", 2),
        L("Les rapports doivent avoir duré plus de trois mois, ou avoir été conclus pour plus de trois mois.", 2),
        L("Le salaire en nature perdu ouvre une indemnité équitable.", 2),
        L("La première année, la loi fixe au moins trois semaines.", 2),
        L("Ensuite, la durée plus longue se fixe équitablement, selon l'ancienneté et les circonstances.", 2),
        L("En cas de grossesse, l'employeur verse le salaire dans la même mesure.", 2),
        L("Un écrit, un contrat-type ou une convention collective peut déroger, si l'équivalent est tenu.", 2),
    ]


def echelles():
    return [
        L("Sans assurance perte de gain, le plein salaire est dû dès le premier jour. Aucun jour de carence.", 3),
        L("La première année, les trois échelles lues donnent trois semaines.", 3),
        L("La deuxième année, Bâle donne deux mois, l'échelle bernoise un mois, Zurich huit semaines.", 3),
        L("L'échelle bernoise vaut pour Berne, Argovie, Obwald, Saint-Gall et la Suisse romande.", 3),
        L("Zurich et les Grisons suivent l'échelle zurichoise.", 3),
        L("La troisième année, Bâle et l'échelle bernoise donnent deux mois, Zurich neuf semaines.", 3),
        L("Le crédit est annuel. Plusieurs empêchements de la même année s'additionnent.", 3),
        L("Une nouvelle maladie, la même année, n'ouvre pas un second crédit entier.", 3),
        L("Le tableau officiel continue. Les années masquées par des points de suspension ne sont pas inventées.", 3),
        L("L'obligation légale ne se supprime pas par un simple contrat.", 3),
    ]


def ij():
    return [
        L("Beaucoup de polices versent 80 pour cent pendant 720 ou 730 jours, sur 900 jours.", 3),
        L("La police et ses conditions priment sur ce schéma.", 3),
        L("Une police peut prévoir 100 pour cent. On la lit avant de l'affirmer.", 3),
        L("80 pour cent pendant 720 jours sont réputés équivalents au salaire légal, plus court mais entier.", 3),
        L("L'employeur paie au moins la moitié de la prime pour cette équivalence.", 3),
        L("L'équivalence se juge globalement, pas sur le seul dossier du jour.", 3),
        L("Un à trois jours de carence peuvent être convenus, selon le tribunal.", 3),
    ]


def certificat():
    return [
        L("Le certificat à l'employeur porte sur la capacité, pas sur le diagnostic.", 4),
        L("Il est clair, daté, signé, et conforme à la vérité.", 4),
        L("On y met les noms du médecin, de la personne et du destinataire.", 4),
        L("On y met le début, et la fin ou la date de la prochaine consultation.", 4),
        L("On y met le degré, complet ou partiel, et la nature : accident, maladie ou grossesse.", 4),
        L("Ni le diagnostic ni le traitement ne figurent sur l'exemplaire de l'employeur.", 4),
        L("La capacité a deux parts : le temps de présence et le rendement.", 4),
        L("Sans précision, un pourcentage veut dire une baisse du temps, pas du rendement.", 4),
        L("Cette lecture se fait par rapport à un plein temps.", 4),
        L("Exemple lu : trois demi-journées par semaine, rendement entier.", 4),
        L("Autre exemple lu : cinq jours par semaine, rendement de moitié.", 4),
        L("En principe, on ne dépasse pas un mois. Sinon, on borne à la prochaine visite.", 4),
        L("On n'écrit pas jusqu'à nouvel avis. On ne renouvelle pas machinalement en fin de mois.", 4),
    ]


def retro():
    return [
        L("Un certificat rétrospectif devrait être évité.", 4),
        L("Il arrive, si l'employeur ne le demande qu'à partir du quatrième jour.", 4),
        L("On sépare ce que le médecin a vu et ce que la personne a dit.", 4),
        L("On écrit la date de début, la date du certificat et la date de la première consultation.", 4),
        L("On n'antidate jamais. Antidater ferait un faux certificat.", 4),
        L("La rétroactivité ne devrait pas excéder quelques jours.", 4),
        L("Après une vraie téléconsultation, seule une incapacité totale brève se certifie ainsi.", 4),
        L("Une incapacité partielle ne s'évalue ni au téléphone ni en vidéo.", 4),
        L("On documente ce qui a été observé à distance.", 4),
    ]


def controle():
    return [
        L("L'employeur peut demander un examen de contrôle, à ses frais.", 4),
        L("Le médecin-conseil reste tenu au secret.", 4),
        L("Il parle de l'aptitude aux tâches, de la reprise et d'une occupation temporaire.", 4),
        L("Il ne donne ni le diagnostic ni le traitement à l'employeur.", 4),
        L("Il peut dire que la personne ne s'est pas présentée.", 4),
        L("Le travailleur prouve l'empêchement. Le certificat dit le degré, pas le diagnostic.", 3),
        L("L'employeur peut exiger le papier dès le premier jour.", 3),
        L("Beaucoup de contrats attendent le troisième ou le quatrième jour.", 3),
    ]


def laa():
    return [
        L("Après un accident, l'indemnité journalière naît le troisième jour qui suit l'accident.", 6),
        L("Elle cesse avec la pleine capacité, avec une rente, ou au décès.", 6),
        L("Si l'incapacité est totale, elle vaut 80 pour cent du gain assuré.", 6),
        L("Si l'incapacité est partielle, elle est réduite en conséquence.", 6),
        L("Elle ne se verse pas en même temps qu'une indemnité journalière d'invalidité.", 6),
        L("Elle ne double pas une allocation de maternité, de l'autre parent, de prise en charge ou d'adoption.", 6),
        L("Cette voie est celle de l'accident. Elle ne s'ouvre pas pour une maladie.", 6),
    ]


def cirai():
    return [
        L("Le médecin donne un avis. Il ne tranche pas seul la capacité pour l'office.", 5),
        L("L'office décide, en s'appuyant sur cet avis. L'arrêt cité est 140 V 193.", 5),
        L("Sauf mention contraire, l'avis médical vise un temps plein. L'arrêt cité est 9C_648/2010.", 5),
        L("Le médecin traitant ne fixe ni l'incapacité de gain ni le taux d'invalidité.", 5),
        L("L'arrêt cité pour cette limite est 144 V 50.", 5),
        L("La rente suppose, en moyenne, au moins 40 pour cent d'incapacité de travail pendant une année.", 5),
        L("Cette année est sans interruption notable. L'arrêt cité est 9C_882/2009.", 5),
        L("À l'échéance, il faut encore une incapacité de gain durable d'au moins 40 pour cent.", 5),
        L("Ces deux conditions sont celles de l'article 28, alinéa 1, de la loi sur l'invalidité.", 5),
        L("La moyenne sur l'année divise la somme des taux fois les jours par 365 jours.", 5),
        L("Les exemples chiffrés de l'annexe ne sont pas recopiés.", 5),
        L("Le droit à la rente ne naît pas avant six mois après la demande.", 5),
        L("L'arrêt cité est 8C_544/2016. Une demande tardive perd les mois de retard.", 5),
        L("Avant la rente, l'office examine la réadaptation.", 5),
    ]


def apprenti():
    return [
        L("La personne en formation annonce tout de suite l'empêchement à l'entreprise.", 7),
        L("En règle générale, le certificat vient dès le troisième jour.", 7),
        L("Il peut être demandé dès le premier jour, si l'assurance ou l'éducation l'exige.", 7),
        L("On ne fait pas rattraper les heures manquées pour maladie ou accident.", 7),
        L("Si les cours professionnels sont impossibles, on avertit l'école selon son règlement.", 7),
        L("L'examen final manqué se justifie par un certificat à l'autorité d'examen.", 7),
        L("En règle générale, l'examen se passe après la guérison. Les modalités sont celles de l'autorité.", 7),
        L("Les trois premiers jours d'accident, y compris le jour même, restent au moins aux quatre cinquièmes.", 7),
        L("Cette phrase de la notice vise le salaire de l'employeur, pas l'indemnité d'assurance.", 7),
        L("La notice décrit une solution répandue : 80 pour cent pendant 30 jours, puis 730 jours sur 900.", 7),
        L("L'employeur y paie la moitié des primes. L'équivalence demande au moins cette moitié.", 7),
        L("La plupart du temps, trois jours d'absence se justifient aussi auprès des cours interentreprises.", 8),
        L("Avant le contrat, une visite peut vérifier que le métier envisagé est tenable.", 8),
        L("Sous l'âge minimum, en règle générale 15 ans, un certificat est exigé.", 8),
        L("Le travail de nuit régulier ou périodique des jeunes appelle un examen et un conseil.", 8),
    ]


def mineur():
    return [
        L("Un mineur sans activité lucrative n'est pas jugé comme un salarié du jour.", 1),
        L("Il est réputé invalide si l'atteinte provoquera probablement une incapacité de gain.", 1),
        L("Cette phrase vise l'avenir, pas la dispense de cours de cette semaine.", 1),
        L("Le certificat de cours dit si la classe, le sport ou l'examen sont tenables.", 7),
        L("Il ne décide pas une rente. L'office le fera plus tard, s'il est saisi.", 5),
        L("Le règlement cantonal de l'école obligatoire n'a pas été extrait. On n'invente pas son délai.", 7),
        L("Pour l'apprenti, l'école professionnelle est avertie à part de l'entreprise.", 7),
    ]


def proche():
    return [
        L("Soigner un enfant ou un conjoint n'est pas l'incapacité de travail de soi-même.", 3),
        L("Le congé lu est limité au temps nécessaire, au plus trois jours par cas.", 3),
        L("Pour le cercle étroit hors enfants, le plafond lu est de dix jours par année.", 3),
        L("La limite de dix jours ne s'applique pas à la prise en charge des enfants, selon la page lue.", 3),
        L("On ne transforme pas ce congé en un taux d'incapacité de la personne soignante.", 3),
    ]


def urgence():
    return [
        L("Avant le certificat, on cherche l'idée de mort, le plan et le moyen."),
        L("Un moyen accessible : on ne laisse pas la personne seule, on appelle les secours."),
        L("Douleur thoracique, souffle brutal ou déficit neurologique : filière d'urgence d'abord."),
        L("Conduire, garder un enfant ou tenir une machine dangereuse : on le dit avant le taux."),
        L("Le certificat ne remplace pas ce geste. Il vient après, s'il a encore un sens."),
    ]


def tableau():
    lignes = [
        "<div class=\"tw\"><table>",
        "<caption>Dix situations, dans l'ordre de la consultation</caption>",
        "<thead><tr><th>Place</th><th>Situation</th><th>Signe qui tranche</th></tr></thead>",
        "<tbody>",
    ]
    signes = {
        1: "Tout le poste habituel est intenable, pour une durée brève datée.",
        2: "Une part du temps ou du rendement reste possible.",
        3: "La durée longue ouvre une autre activité exigible.",
        4: "La cause est un accident, pas une maladie.",
        5: "La question est le salaire ou l'indemnité de maladie.",
        6: "Il y a un contrat d'apprentissage, une école et parfois un examen.",
        7: "Il y a des cours, sans le poste d'un salarié.",
        8: "Le destinataire est l'employeur : pas de diagnostic.",
        9: "La date du papier et la date du début ne coïncident pas.",
        10: "On passe de l'avis médical à la décision de l'office.",
    }
    for i, nom in NOMS.items():
        lignes.append(f"<tr><td>{i}</td><td>{nom}</td><td>{signes[i]}</td></tr>")
    lignes.append("</tbody></table></div>")
    return "\n".join(lignes)


def base():
    b = {}
    b["ess"] = glossaire()
    b["sources"] = [
        L("Loi générale, articles 4, 6, 7 et 8, lue le 1er novembre 2026.", 1),
        L("Code des obligations, article 324a, en vigueur au 1er octobre 2026.", 2),
        L("Foire aux questions sur l'empêchement, lue le 1er novembre 2026.", 3),
        L("Guide des médecins, chapitre 7.6, lu le 1er novembre 2026.", 4),
        L("Circulaire des rentes, état au 1er janvier 2022.", 5),
        L("Loi accidents, articles 16 et 17, article 16 en vigueur au 1er janvier 2026.", 6),
        L("Notice apprentissage, maladie et accident, lue le 1er novembre 2026.", 7),
        L("Notice apprentissage, certificat médical, lue le 1er novembre 2026.", 8),
    ]
    return b


def remplir_phase_a(b):
    b["ess"] += [
        L("On sépare le poste habituel, les cours, l'accident et la maladie."),
        L("On écrit une date de fin. On ne promet pas une rente."),
    ]
    b[1] = [
        L("Le motif est une détermination, pas le nom d'une maladie."),
        L("Deux questions arrivent ensemble : le travail, et la fréquentation des cours."),
    ] + definition() + accident_def()
    b[2] = [
        L("Aucune fréquence suisse de ces dix situations au cabinet n'a été lue."),
        L("Les durées légales ne sont pas des fréquences. Elles ne classent pas la personne.", 2),
        L("L'ordre du cours est celui de la consultation, pas celui d'une gravité."),
    ]
    b[3] = [
        L("Le mécanisme utile est la tâche qui devient inexigible à cause de la santé.", 1),
        L("Douleur, souffle, contagion, ralentissement ou danger pour autrui changent le taux."),
        L("La faute morale n'entre pas dans la définition lue.", 1),
        L("Une baisse de gain qui resterait après réadaptation est un autre concept.", 1),
    ]
    b[4] = urgence() + [
        L("Ensuite seulement : poste réel, cours, accident ou maladie, durée, taux."),
        L("Dernier geste du jour : un certificat daté, ou l'adresse des secours."),
    ]
    b[5] = [
        L("On demande le métier, les tâches, les horaires et ce qui met autrui en danger."),
        L("On demande si la personne est apprentie, élève, salariée, ou sans activité."),
        L("On demande la date de début réelle, et ce qui a déjà été constaté."),
        L("On demande le revenu en jeu : salaire, accident, ou indemnité de maladie."),
    ]
    b[6] = [
        L("On observe ce qui se voit aujourd'hui. On le sépare du récit."),
        L("Le schéma a trois plans : danger, mesure, suite. Ce n'est pas une radiographie."),
    ]
    b[7] = [tableau(), L("Le tableau ne donne pas une fréquence. Il évite de tout nommer du même mot.")]
    for nom in NOMS.values():
        b[7].append(L(f"Situation du cours : {nom}."))
    b[8] = [
        L("Le certificat décrit la capacité restante. Il ne pose pas le taux d'invalidité.", 5),
        L("Totale ou partielle se dit sur le poste exigible, pas sur un souhait.", 1),
        L("La longue durée est le seul moment où un autre métier entre dans l'exigibilité.", 1),
    ]
    b[9] = [
        L("L'examen suit la question clinique. Il ne prouve pas à lui seul un taux."),
        L("Un contrôle par le médecin-conseil répond à un doute de l'employeur, à ses frais.", 4),
        L("Aucune biologie systématique n'est exigée par les textes lus pour écrire le taux."),
    ]
    b[10] = [
        L("Urgence, puis mesure, puis suite."),
        L("La mesure est le texte lu, pas l'habitude du cabinet."),
    ]
    b[11] = certificat() + laa()[:4] + salaire()[:4] + [
        L("Aucune dose n'accompagne cette détermination."),
    ]
    b[12] = [
        L("Une date de revue est dite. Le papier ne vit pas sans elle.", 4),
        L("Après 30 jours consécutifs, une annonce à l'office est possible.", 4),
        L("Cette possibilité n'est pas une rente, ni une obligation d'en promettre une.", 5),
    ]
    b[13] = [
        L("Définition d'abord : poste exigible, santé, totale ou partielle.", 1),
        L("L'employeur reçoit le degré et les dates, pas le diagnostic.", 4),
        L("L'accident et la maladie n'ouvrent pas la même indemnité.", 6),
        L("L'office, pas le médecin traitant, fixe l'incapacité de gain.", 5),
    ]
    b[14] = [
        L("Erreur : écrire 100 pour cent parce que la personne le demande."),
        L("Correction : décrire les tâches encore possibles, ou dire qu'aucune ne l'est.", 4),
        L("Erreur : mettre le diagnostic sur l'exemplaire de l'employeur.", 4),
        L("Erreur : copier l'indemnité d'accident sur une maladie.", 6),
    ]


def remplir_dx(b, i):
    nom = NOMS[i]
    b["ess"] += [L(f"Le signe distinctif décide du geste : {nom}.")]
    b[1] = [L(f"{nom} est une situation du motif, pas un synonyme des neuf autres.")]
    b[2] = [L("Aucune part nationale lue ne donne la fréquence de cette situation au cabinet.")]
    b[3] = [L("Le mécanisme utile est celui qui change le certificat du jour.")]
    b[4] = [L("On écarte le danger immédiat avant d'écrire un taux.")] + urgence()[:2]
    b[5] = [L("On demande le poste, les cours, la date réelle et le revenu en jeu.")]
    b[6] = [L("Le schéma montre trois plans. Ce n'est pas une radiographie.")]
    b[7] = [L("On ne colle pas cette situation aux autres sur le seul mot arrêt.")]
    b[8] = []
    b[9] = [L("L'examen suit une question. Il ne remplace pas le texte qui définit le taux.")]
    b[10] = [L("Urgence, mesure, puis suite. Un seul pas est choisi.")]
    b[11] = [L("Le geste suit le texte lu. Aucune dose n'est ajoutée.")]
    b[12] = [L("Une date de revue est fixée avant de quitter la pièce.", 4)]
    b[13] = [
        L(f"Retenir le signe qui distingue {nom}."),
        L("Ne pas sauter l'idée de mort ni le signe qui menace."),
        L("Ne pas inventer une dose. Ce motif n'ouvre pas d'ordonnance."),
    ]
    b[14] = [L("Le cas corrigé montre l'erreur, puis le geste qui la remplace.")]
    if i == 1:
        b[1] += [
            L("Ici, aucune tâche du poste habituel n'est exigible, et la durée reste brève.", 1),
            L("On nomme la fin, ou la prochaine consultation, dans le mois en principe.", 4),
        ]
        b[3] += [L("Le corps ou le psychisme rend tout le poste intenable, pour peu de jours.", 1)]
        b[8] += definition()[:4] + [
            L("On ne parle pas encore d'une autre profession. La durée n'est pas longue.", 1),
        ]
        b[11] += [
            L("On écrit une incapacité totale, une date de fin, et la nature maladie ou accident.", 4),
            L("On ne laisse pas le papier ouvert jusqu'à nouvel avis.", 4),
        ]
    elif i == 2:
        b[1] += [
            L("Une part du travail reste exigible. Le taux doit dire laquelle.", 1),
            L("Temps de présence et rendement sont deux phrases, pas un seul nombre vague.", 4),
        ]
        b[8] += certificat()[6:11]
        b[11] += [
            L("On écrit les heures encore possibles, ou le rendement sur le temps présent.", 4),
            L("Faute de cette phrase, le lecteur croira une simple baisse du temps.", 4),
            L("Une incapacité partielle ne se certifie pas après un seul appel vidéo.", 4),
        ]
    elif i == 3:
        b[1] += [
            L("La durée est longue. L'activité exigible peut quitter le métier d'origine.", 1),
            L("Ce glissement ne se fait pas dès le premier certificat bref.", 1),
        ]
        b[8] += definition()[3:4] + cirai()[:5]
        b[11] += [
            L("On décrit ce qui reste possible, y compris hors du poste d'origine si la durée le commande.", 1),
            L("On ne transforme pas cet avis en taux d'invalidité.", 5),
            L("On propose l'annonce à l'office si 30 jours consécutifs sont déjà là.", 4),
        ]
    elif i == 4:
        b[1] += accident_def()
        b[8] += laa()
        b[11] += [
            L("On coche accident, pas maladie, si la définition de l'accident est tenue.", 1),
            L("On ne promet pas 80 pour cent dès le premier jour : le droit naît le troisième jour suivant.", 6),
            L("Les trois premiers jours de l'apprenti suivent la notice, à part.", 7),
        ]
    elif i == 5:
        b[1] += [
            L("La question ici est le revenu pendant la maladie, pas le nom de la maladie.", 2),
            L("Sans assurance, le plein salaire a une durée. Avec assurance, la police décide.", 3),
        ]
        b[2] += [L("Les échelles lues ne sont pas une fréquence de consultation.", 3)]
        b[8] += salaire() + echelles() + ij()
        b[11] += [
            L("On dit si une assurance perte de gain existe. Sans elle, le plein salaire a ses durées.", 3),
            L("On ne garantit pas 720 jours sans avoir lu la police.", 3),
            L("La grossesse ouvre le même maintien de salaire, dans la mesure lue.", 2),
        ]
        b[7] += proche()
    elif i == 6:
        b[1] += [
            L("Trois lieux : l'entreprise, les cours professionnels, l'examen.", 7),
            L("Une incapacité dans l'un ne se copie pas sans phrase sur les autres.", 7),
        ]
        b[8] += apprenti()
        b[11] += [
            L("On écrit à part l'entreprise, les cours et, s'il approche, l'examen.", 7),
            L("On n'exige pas le rattrapage des heures de maladie.", 7),
            L("Le médecin-conseil, s'il est nommé, est payé par l'entreprise.", 8),
        ]
    elif i == 7:
        b[1] += [
            L("Ici il n'y a pas de poste de salarié. Il y a une classe.", 1),
            L("La dispense de cours n'est pas une décision de rente.", 5),
        ]
        b[8] += mineur() + [
            L("Pour l'élève sans contrat, on n'invente pas le délai du canton.", 7),
            L("On dit ce qui est tenable en classe, au sport et à l'examen, avec des dates.", 4),
        ]
        b[11] += [
            L("On ne délivre pas un certificat de salarié à un élève sans poste.", 1),
            L("On n'annonce pas une rente sur la seule dispense de cours de la semaine.", 5),
            L("Si un apprentissage existe, on revient à la situation de l'apprenti.", 7),
        ]
    elif i == 8:
        b[1] += [
            L("Le destinataire est l'employeur. Le secret borne ce qu'il peut lire.", 4),
            L("Le degré et les dates suffisent à réorganiser le travail.", 4),
        ]
        b[8] += certificat() + controle()
        b[11] += [
            L("L'exemplaire de l'employeur ne porte pas le diagnostic.", 4),
            L("Le dossier médical le garde. L'assureur maladie n'est pas l'employeur.", 4),
            L("Si l'employeur paie un contrôle, on l'explique sans le vivre comme une offense.", 4),
        ]
    elif i == 9:
        b[1] += [
            L("Le papier arrive après le début réel. On ne réécrit pas le calendrier.", 4),
            L("La vidéo ne voit pas un rendement partiel.", 4),
        ]
        b[8] += retro()
        b[11] += [
            L("On refuse d'antidater. On écrit les trois dates lues.", 4),
            L("Au-delà de quelques jours en arrière, on ne couvre pas la période non vue.", 4),
            L("Une prolongation se revoit. Elle ne se reconduit pas jusqu'à nouvel avis.", 4),
            L("Le partiel attend une consultation où le rendement se voit.", 4),
        ]
    elif i == 10:
        b[1] += definition()[4:]
        b[8] += cirai()
        b[3] += [
            L("L'incapacité de gain ne se juge qu'après les traitements et la réadaptation exigibles.", 1),
            L("Seules les suites de la santé comptent. Le surmontable objectif reste dehors.", 1),
        ]
        b[11] += [
            L("On rédige un avis, avec le temps plein sauf mention contraire.", 5),
            L("On ne signe pas un taux d'invalidité à la place de l'office.", 5),
            L("On rappelle les 40 pour cent sur une année, puis la capacité de gain durable.", 5),
            L("On rappelle les six mois après la demande, sans promettre la date de la rente.", 5),
        ]
    if not b[8]:
        b[8] = [L("Le critère positif est celui de la source citée pour cette situation.", 1)]


ERR = {
    "pa": ("ouvrir par le pourcentage demandé", "chercher le danger, puis le poste et les cours"),
    "tot": ("laisser le certificat sans date de fin", "écrire une fin ou la prochaine consultation"),
    "par": ("mettre un pourcentage sans dire le temps ni le rendement", "écrire les heures restantes et le rendement"),
    "lon": ("geler la personne dans le seul métier d'origine", "dire si une autre activité devient exigible"),
    "acc": ("appliquer l'indemnité de maladie à un accident", "dater le troisième jour suivant et le taux de 80 pour cent"),
    "sal": ("promettre 720 jours sans lire la police", "distinguer le salaire légal et la police réelle"),
    "app": ("un seul papier pour l'entreprise, les cours et l'examen", "écrire chaque lieu à part"),
    "ele": ("traiter l'élève comme un salarié invalide", "décrire la classe et laisser la rente à l'office"),
    "sec": ("écrire le diagnostic pour l'employeur", "écrire le degré, les dates et la nature"),
    "ret": ("antidater le certificat", "séparer les trois dates et ne pas couvrir l'invu"),
    "gai": ("fixer soi-même le taux d'invalidité", "donner un avis et laisser la décision à l'office"),
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
    if i == 0:
        return [
            ("danger", "Danger", "Niveau danger. Idée ou corps. Schéma, pas une radiographie.",
             [("Idée", "On demande le plan et le moyen."), ("Souffle", "Douleur ou essoufflement brutal."), ("Déficit", "Un déficit sort du certificat."), ("Secours", "Les secours passent avant le papier.")]),
            ("mesure", "Mesure", "Niveau mesure. Poste, cours, taux. Droite du patient à gauche.",
             [("Poste", "Tâches réellement exigibles."), ("Cours", "Classe, sport, examen."), ("Taux", "Temps et rendement."), ("Nature", "Accident, maladie ou grossesse.")]),
            ("suite", "Suite", "Niveau suite. Une date. Pas une radiographie.",
             [("Fin", "Une date de fin ou de revue."), ("Secret", "Pas de diagnostic à l'employeur."), ("Revenu", "Salaire, accident ou maladie."), ("Office", "Avis seulement, pas la rente.")]),
        ]
    specs = {
        1: ("Tout", "Aucune tâche du poste n'est tenable.", "Fin", "Une date dans le mois, en principe.", "Nature", "Maladie ou accident, sans diagnostic.", "Revue", "Pas jusqu'à nouvel avis."),
        2: ("Temps", "Heures ou demi-journées restantes.", "Rendement", "Ce qui est fait pendant ce temps.", "Vidéo", "Le partiel ne se juge pas à distance.", "Plein", "Sans phrase, on lit une baisse du temps."),
        3: ("Durée", "Longue : autre métier possible.", "Avis", "Le médecin ne fixe pas l'invalidité.", "Plein", "Temps plein, sauf mention contraire.", "Annonce", "Possible après 30 jours consécutifs."),
        4: ("Cause", "Soudaine, involontaire, extérieure.", "Jour", "Droit dès le troisième jour suivant.", "Taux", "80 pour cent si totale, réduit sinon.", "Maladie", "Ne pas copier cette indemnité."),
        5: ("Semaines", "Au moins trois la première année.", "Crédit", "Les arrêts de l'année s'ajoutent.", "Police", "Elle prime sur le schéma de 720 jours.", "Moitié", "L'employeur paie au moins la moitié."),
        6: ("Entreprise", "Annonce immédiate.", "Cours", "L'école est avertie à part.", "Examen", "Certificat à l'autorité, rattrapage après.", "Heures", "Pas de rattrapage des heures malades."),
        7: ("Classe", "Ce qui est tenable en cours.", "Sport", "À dire à part.", "Avenir", "Le mineur se juge sur le gain probable.", "Canton", "Délai cantonal non inventé."),
        8: ("Degré", "Complet ou partiel, compréhensible.", "Dates", "Début, fin, signature.", "Secret", "Ni diagnostic ni traitement.", "Contrôle", "Médecin-conseil aux frais de l'employeur."),
        9: ("Trois", "Début, établissement, première visite.", "Faux", "Ne jamais antidater.", "Quelques", "Quelques jours en arrière, pas des semaines.", "Distance", "Seul le total bref, après vraie téléconsultation."),
        10: ("Avis", "Pas une décision d'office.", "Année", "40 pour cent en moyenne sur un an.", "Gain", "Puis incapacité de gain durable.", "Six", "Pas avant six mois après la demande."),
    }
    a, b, c, d, e, f, g, h = specs[i]
    return [
        ("plan1", "Repère", "Premier plan. Schéma, pas une radiographie.",
         [(a, b), (c, d), ("Corps", "Un signe menaçant sort du motif."), ("Idée", "On demande l'idée de mort.")]),
        ("plan2", "Mesure", "Deuxième plan. Droite du patient à gauche.",
         [(e, f), (g, h), ("Cours", "Classe ou entreprise, à part."), ("Revue", "Une date est dite.")]),
        ("plan3", "Suite", "Troisième plan. Pas une radiographie.",
         [("Revenu", "Salaire, accident ou maladie."), ("Secret", "Diagnostic hors de l'employeur."), ("Office", "Avis, pas le taux d'invalidité."), ("Dose", "Aucune dose dans ce motif.")]),
    ]


ARBRES = {
    0: ("Idée avec moyen, douleur thoracique, souffle ou déficit : secours d'abord.",
        "Poste, cours, accident ou maladie, temps et rendement.",
        "Certificat daté sans diagnostic pour l'employeur, ou annonce sans promettre une rente."),
    1: ("Danger immédiat : on ne commence pas par le formulaire.",
        "Tout le poste habituel est intenable, durée encore brève.",
        "Incapacité totale datée, dans le mois ou jusqu'à la prochaine visite."),
    2: ("Danger d'abord. Le pourcentage vient ensuite.",
        "Heures restantes et rendement, deux phrases.",
        "Pas de partiel au téléphone. Revue datée."),
    3: ("Le danger du jour prime sur le débat de métier.",
        "Durée longue : dire si une autre activité est exigible.",
        "Avis médical. L'office fixe l'incapacité de gain."),
    4: ("Le corps menaçant passe avant la case accident.",
        "Définition d'accident tenue, troisième jour suivant, 80 pour cent si totale.",
        "Ne pas copier cette indemnité sur une maladie."),
    5: ("L'urgence clinique se traite même si le crédit de salaire est flou.",
        "Trois semaines au moins la première année, ou police lue.",
        "Ne pas promettre 720 jours sans la police. Moitié de prime pour l'équivalence."),
    6: ("Danger d'abord, y compris à l'atelier.",
        "Entreprise, cours et examen sont trois phrases.",
        "Pas de rattrapage des heures. Examen après la guérison, selon l'autorité."),
    7: ("Danger d'abord, y compris le retour seul au domicile.",
        "Classe, sport, examen. Pas un taux de salarié.",
        "Le mineur et la rente future restent à l'office. Délai cantonal non inventé."),
    8: ("Danger d'abord. Le secret ne retarde pas les secours.",
        "Degré, dates, nature. Pas de diagnostic à l'employeur.",
        "Contrôle possible aux frais de l'employeur, sans livrer le diagnostic."),
    9: ("On ne couvre pas un danger passé par un papier antidaté.",
        "Trois dates. Quelques jours au plus. Pas de partiel à distance.",
        "Prolongation revue. Jamais jusqu'à nouvel avis."),
    10: ("Le danger clinique prime sur le dossier de rente.",
        "Avis sur temps plein, 40 pour cent sur un an, puis gain durable.",
        "Décision de l'office. Pas avant six mois après la demande."),
}


def assembler(i):
    b = base()
    if i == 0:
        remplir_phase_a(b)
        titre = "Détermination de l'incapacité de travail ou de fréquentation des cours"
        sous = "D'abord le danger, ensuite le poste ou les cours, ensuite un papier daté."
        h1 = titre
        nom = "LOT_224_Phase_A_V0.html"
        did = "pa224"
    else:
        remplir_dx(b, i)
        titre = NOMS[i]
        sous = "Un signe distinctif, puis le geste qui va avec."
        h1 = titre
        nom = f"LOT_224_Phase_B_V0_DX.{i}.html"
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
    did = "pa224" if i == 0 else f"dx{i}"
    frag = schema(did, "capture", niveaux_de(i))
    cap = LOT / "captures"
    cap.mkdir(exist_ok=True)
    police = (RACINE / "grok-LOTS-html/outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf").as_uri()
    frag = frag.replace(POLICE, police)
    tmp = Path(f"/tmp/lot224_{did}.html")
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
        alt = Path(f"/tmp/lot224_{did}_{etat}.html")
        alt.write_text(page_html, encoding="utf-8")
        out = cap / nompng
        subprocess.check_call([
            "timeout", "25", "/opt/google/chrome/chrome",
            "--headless=new", "--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage",
            f"--user-data-dir=/tmp/cr-lot224-{did}-{etat}",
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

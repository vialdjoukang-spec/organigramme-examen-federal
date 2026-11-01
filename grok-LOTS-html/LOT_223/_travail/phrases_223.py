# -*- coding: utf-8 -*-
"""Phrases cliniques de LOT_223. Chaque phrase fait au plus 30 mots."""
from __future__ import annotations

DXS_NOMS = [
    "Préparation du voyage et protection contre les piqûres",
    "Vaccinations du voyageur",
    "Diarrhée du voyageur",
    "Chimioprophylaxie du paludisme",
    "Dengue, chikungunya et infection à virus Zika",
    "Fièvre au retour et paludisme",
    "Mal des montagnes",
    "Thrombose veineuse après un long trajet",
    "Rage après exposition animale",
    "Infection à Chlamydia trachomatis au retour",
]

DOSE_CLES = {"a", "3", "4", "5", "6", "7", "8", "9", "10"}

SPEC: dict[str, dict[int, tuple[str, ...]]] = {}
DETAILS: dict[str, list[str]] = {}
TEASERS: dict[str, list[str]] = {}


def _k(cle: str, rows: list[tuple[str, ...]]) -> None:
    if len(rows) != 14:
        raise SystemExit(f"{cle} n'a pas 14 points ({len(rows)})")
    SPEC[cle] = {i + 1: rows[i] for i in range(14)}


def _t(cle: str, lines: list[str]) -> None:
    if len(lines) != 14:
        raise SystemExit(f"teasers {cle}")
    TEASERS[cle] = lines


# --- Phase A ---
_k("a", [
    (
        "O7.1 est la consultation avant ou après un voyage à l'étranger, surtout en pays tropical.",
        "Ce n'est pas le nom d'une seule infection.",
        "L'office demande de s'informer auprès du médecin quatre à six semaines avant un départ à risque. [[1]]",
        "Depuis le 18 juillet 2022, l'office renvoie vers le site des conseils aux voyageurs. [[1]]",
    ),
    (
        "En 2024, la Suisse a déclaré 429 dengue, 19 chikungunya, 9 infections Zika, un Nil occidental et zéro fièvre jaune. [[2]]",
        "Le document de janvier 2016 compte 150 à 450 paludismes déclarés par an, et un à trois décès de voyageurs non immuns. [[4]]",
        "Ces deux sources ne classent pas à elles seules les dix lectures.",
        "On ne transforme pas une inconnue en zéro.",
    ),
    (
        "L'anophèle pique le soir et la nuit, puis le parasite passe par le foie avant les globules rouges. [[1]]",
        "L'aède de la dengue pique le jour et au crépuscule. [[18]]",
        "L'atovaquone bloque une étape mitochondriale du parasite et le proguanil agit sur les folates. [[5]]",
        "Le lopéramide se lie aux récepteurs mu de la paroi intestinale. [[13]]",
    ),
    (
        "On date le voyage, la destination, la grossesse, les vaccins et les médicaments avant de choisir une mesure.",
        "Toute fièvre pendant ou après une zone d'endémie fait suspecter le paludisme jusqu'à preuve du contraire. [[1]]",
        "On ne rassure pas tant que le sang n'a pas été examiné.",
        "La branche de préparation reste ouverte si la personne part et n'a pas de fièvre.",
    ),
    (
        "On demande les dates, l'altitude, l'eau douce, les animaux, les rapports sexuels et la durée assise en avion ou en car.",
        "On demande une fièvre, des selles, un saignement, une plaie et un antécédent psychiatrique avant une méfloquine.",
        "On demande la clairance rénale connue avant l'atovaquone avec proguanil.",
        "On demande si un vaccin vivant est possible, notamment la fièvre jaune et le vaccin oral de la typhoïde.",
    ),
    (
        "On cherche la fièvre, la conscience, un saignement, un ictère, une détresse respiratoire et un mollet augmenté.",
        "On regarde la plaie, la muqueuse et le siège de la morsure, surtout la tête, le cou et les mains. [[12]]",
        "Le schéma sépare le danger, la maladie et la préparation.",
        "Un examen normal n'écarte pas un paludisme débutant.",
    ),
    (
        "Les lectures voisines sont la diarrhée, la dengue, le paludisme, le mal des montagnes, la thrombose et la rage.",
        "La préparation et les vaccins occupent la plupart des consultations avant le départ.",
        "La fièvre au retour est la lecture qu'on ne remet pas au lendemain. [[1]]",
        "Une même personne peut cumuler une diarrhée et une fièvre, et les deux se lisent.",
    ),
    (
        "Le diagnostic de la situation est le voyage plus le problème dominant, pas un seul microbe.",
        "Le paludisme se confirme par l'examen du sang, pas par le récit seul. [[1]]",
        "La dengue sévère se reconnaît à l'aggravation, souvent quand la fièvre tombe. [[18]]",
        "La rage se classe en trois catégories d'exposition, lues en entier dans la lecture dédiée. [[12]]",
    ),
    (
        "Aucun bilan biologique systématique n'est exigé pour toute consultation de voyage.",
        "La fièvre au retour d'une zone d'endémie justifie un examen du sang pour le paludisme, sans délai. [[1]]",
        "Les seuils d'un laboratoire suisse pour les plaquettes ou le parasite n'ont pas été extraits pour ce lot.",
        "On n'attend pas un résultat pour hospitaliser une personne confuse, qui saigne ou qui est en choc.",
    ),
    (
        "La branche d'alerte s'ouvre devant la fièvre au retour, le choc, la détresse ou une plaie de catégorie trois.",
        "La branche de la maladie s'ouvre quand le tableau lu est réuni, par exemple la diarrhée ou la dengue.",
        "La branche de préparation reste ouverte avant le départ, sans symptôme grave.",
        "On peut ouvrir deux branches si la diarrhée s'accompagne de fièvre.",
    ),
    (
        "Les milligrammes de cette page portent le numéro d'autorisation lu à côté, et l'information professionnelle les désigne.",
        "Le paracétamol de la fièvre, autorisation 69266, va de 500 à 1'000 mg par prise, sans dépasser 4'000 mg par jour. [[16]]",
        "L'artéméther avec luméfantrine, autorisation 54594, est réservé à l'accès non compliqué, pas à la forme grave. [[8]]",
        "On ne recopie pas un schéma d'un autre pays quand l'information professionnelle suisse a déjà une phrase.",
    ),
    (
        "La protection contre les piqûres concerne toutes les zones à paludisme, même si le risque est bas. [[3]]",
        "Les vêtements clairs et couvrants, le répulsif et la moustiquaire imprégnée sont les mesures lues. [[1]]",
        "La vaccination de l'hépatite A est recommandée vers les pays tropicaux ou subtropicaux. [[18]]",
        "On revoit le projet si la personne est enceinte et que la destination est à haut risque de paludisme. [[4]]",
    ),
    (
        "On nomme la lecture, on protège le danger vital, et on ne médicalise pas un voyage sans exposition.",
        "Les catégories de rage, les schémas vaccinaux lus et les doses avec numéro restent entiers.",
        "Deux textes donnent deux seuils de fièvre, 38 degrés sur la page de l'office et 37,5 degrés sur le feuillet de 2024. [[1]] [[3]]",
        "On attribue chaque chiffre à sa source, sans les fondre.",
    ),
    (
        "Le piège vital est de remettre au lendemain une fièvre au retour d'une zone d'endémie. [[1]]",
        "Le piège digestif est de donner le lopéramide en premier lors d'une dysenterie fébrile et sanglante. [[13]]",
        "Le piège du vaccin vivant est de l'injecter à une personne immunodéprimée. [[9]]",
        "Le cas juste de cette page est de séparer préparation, maladie et urgence avant de choisir le comprimé.",
    ),
])

_k("1", [
    (
        "Cette lecture est le conseil avant le départ, quand aucune maladie du voyage n'est encore là.",
        "Elle couvre l'itinéraire, les dates, le type de séjour et la protection contre les piqûres.",
        "L'office recommande ce temps de conseil quatre à six semaines avant une zone à risque. [[1]]",
        "Un départ dans moins d'une semaine ne supprime pas le conseil, il le concentre.",
    ),
    (
        "La plupart des consultations de voyage commencent par cette lecture, sans qu'une proportion suisse unique ait été lue.",
        "On ne lui donne pas le rang d'une incidence inventée.",
        "Le bulletin de 2025 rappelle que les voyageurs protègent aussi la Suisse en évitant de ramener un virus. [[2]]",
        "Aucune transmission locale de dengue n'avait été déclarée en Suisse dans ce bulletin. [[2]]",
    ),
    (
        "L'anophèle pique du crépuscule à l'aube, l'aède pique le jour. [[1]] [[18]]",
        "Au-dessus de 1500 mètres, le document de 2016 juge le risque palustre en général plus faible. [[4]]",
        "La transmission peut encore survenir presque jusqu'à 3000 mètres selon le même document. [[4]]",
        "La protection mécanique baisse le contact avant même le comprimé.",
    ),
    (
        "On écrit la destination, les escales, la saison, le logement et le fait de dormir dehors ou climatisé.",
        "On repère la grossesse, le nourrisson, l'immunodépression et une maladie chronique.",
        "On décide ensuite si une prophylaxie, un vaccin ou un simple conseil suffit.",
        "On ne prescrit pas une chimio prophylaxie pour un séjour sans exposition lue.",
    ),
    (
        "On demande les voyages antérieurs, les vaccins déjà faits et les intolérances.",
        "On demande l'eau douce, l'altitude prévue et les animaux probables.",
        "On demande si la personne peut consulter sur place dans les 24 heures en cas de fièvre. [[4]]",
        "On demande une assurance et un accès aux soins, sans inventer une obligation chiffrée.",
    ),
    (
        "L'examen est court si la personne est asymptomatique.",
        "On note un ictère, une grossesse visible, une plaie ou un déficit qui changerait un vaccin vivant.",
        "Le schéma de cette lecture place la piqûre, le logement, le calendrier et le sac.",
        "On n'ouvre pas un bilan parce que le motif est un voyage.",
    ),
    (
        "On distingue cette lecture de la prophylaxie du paludisme, qui s'ajoute seulement en zone à haut risque. [[3]]",
        "On la distingue des vaccins, qui ont leur propre lecture.",
        "On la distingue de la fièvre au retour, qui est une urgence. [[1]]",
        "Un conseil incomplet laisse partir sans répulsif ni calendrier.",
    ),
    (
        "Il n'y a pas de critère biologique pour dire que le conseil est complet.",
        "Le conseil est complet quand l'itinéraire, les piqûres, les vaccins utiles et le plan en cas de fièvre ont été dits.",
        "Le feuillet de 2024 rappelle qu'un thermomètre qui fonctionne fait partie du voyage en zone palustre. [[3]]",
        "On note par écrit ce qui a été choisi et ce qui a été écarté.",
    ),
    (
        "Aucun examen complémentaire n'est systématique dans cette lecture.",
        "Un test n'est utile que s'il change un vaccin ou une contre-indication, par exemple une grossesse.",
        "On ne demande pas un bilan parasitaire avant un départ chez une personne sans symptôme.",
        "Les seuils de laboratoire ne sont pas enseignés ici, faute d'extrait suisse pour cette question.",
    ),
    (
        "Si la destination est à haut risque de falciparum, on quitte cette lecture vers la prophylaxie. [[3]]",
        "Si un vaccin est exigé ou fortement recommandé, on ouvre la lecture des vaccins.",
        "Si la personne a déjà de la fièvre, on n'est plus dans la préparation.",
        "Si le séjour est court en Europe sans exposition particulière, on reste sur le conseil.",
    ),
    (
        "Cette lecture ne porte aucun milligramme.",
        "Le traitement d'une maladie déjà là est dans les autres lectures.",
        "On explique comment faire baisser une fièvre future sans retarder l'avis médical. [[4]]",
        "Le cas juste est un itinéraire écrit, un répulsif, et la phrase sur la fièvre au retour.",
    ),
    (
        "Vêtements longs et clairs, répulsif sur la peau découverte, moustiquaire ou chambre traitée. [[1]] [[4]]",
        "La protection nocturne vise l'anophèle, la protection diurne vise l'aède. [[18]]",
        "On évite l'eau stagnante autour du logement, site de ponte des aèdes. [[18]]",
        "On répète le répulsif dans la journée selon le produit, sans inventer un intervalle non lu.",
    ),
    (
        "Le conseil tient en quatre gestes lus en 2016 : savoir le risque, éviter les piqûres, prendre le médicament s'il est indiqué, consulter vite si fièvre. [[4]]",
        "Le feuillet de 2024 garde la protection dans toutes les zones, et réserve la prophylaxie au haut risque. [[3]]",
        "On dit les deux textes, avec leur date.",
        "On ne promet pas un risque nul.",
    ),
    (
        "Le piège est de tout résumer à un comprimé et d'oublier la piqûre.",
        "Le piège inverse est de refuser tout médicament dans une zone à haut risque de falciparum. [[3]]",
        "Le piège du délai est de dire qu'il est trop tard pour conseiller.",
        "Cas corrigé : on écrit quand même le plan de fièvre, même si le départ est dans trois jours.",
    ),
])

_k("2", [
    (
        "Cette lecture réunit les vaccins du voyage, en plus du calendrier habituel.",
        "La fièvre jaune, l'hépatite A, la typhoïde orale et la rage avant exposition en sont les pièces lues.",
        "Chaque produit garde son autorisation, sans mélanger les schémas.",
        "Un vaccin vivant ne se décide pas comme un vaccin inactivé.",
    ),
    (
        "La fièvre jaune n'a pas été déclarée en Suisse en 2024. [[2]]",
        "Cela ne dispense pas le voyageur qui entre dans une zone où le virus circule. [[18]]",
        "L'hépatite A reste recommandée vers les pays tropicaux ou subtropicaux. [[18]]",
        "Aucune couverture vaccinale suisse du voyage n'a été lue pour classer cette lecture.",
    ),
    (
        "Stamaril est un virus vivant atténué. [[9]]",
        "Vivotif est une immunisation orale vivante contre Salmonella enterica sérovar Typhi. [[11]]",
        "Havrix est un vaccin inactivé de l'hépatite A. [[10]]",
        "La protection de la fièvre jaune, chez la personne immunocompétente, commence dix jours après la première dose. [[9]] [[18]]",
    ),
    (
        "On vérifie l'âge, la grossesse, l'immunodépression, un thymus malade et l'allergie avant un vaccin vivant. [[9]]",
        "On vérifie le pays qui exige un certificat et le pays où le virus circule vraiment. [[18]]",
        "On ne vaccine pas pour un cachet de passeport si le risque médical est disproportionné, surtout après 60 ans. [[9]]",
        "On sépare l'obligation administrative et l'indication médicale, puis on dit les deux.",
    ),
    (
        "On demande les doses déjà reçues, les dates et le carnet international.",
        "On demande une immunodépression, une corticothérapie générale, une radiothérapie ou un cytostatique. [[9]]",
        "On demande une grossesse en cours ou prévue dans le mois qui suit la fièvre jaune. [[9]]",
        "On demande l'âge exact de l'enfant, parce que les bornes changent avec le produit.",
    ),
    (
        "L'examen cherche une contre-indication visible, pas un syndrome vaccinal.",
        "Une fièvre aiguë sévère fait reporter, sans qu'un degré précis ait été extrait de ces autorisations.",
        "Le schéma montre le vivant, l'inactivé, le certificat et l'âge.",
        "On n'injecte pas dans une consultation pressée sans ces questions.",
    ),
    (
        "On ne confond pas la fièvre jaune et la dengue, qui n'ont pas le même vaccin.",
        "Le bulletin limite le vaccin dengue aux voyageurs déjà infectés et exposés à une forte transmission. [[2]]",
        "On ne confond pas le certificat à vie et la phrase sur la durée de protection. [[9]]",
        "HealthyTravel recommande en outre un rappel unique de fièvre jaune après dix ans s'il n'y a pas d'immunosuppression. [[18]]",
    ),
    (
        "Stamaril, autorisation 00520, se donne en une dose de 0,5 ml à partir de neuf mois révolus. [[9]]",
        "Il est contre-indiqué avant six mois révolus. [[9]]",
        "Entre six et neuf mois, il n'est pas recommandé sauf circonstance particulière et recommandation officielle. [[9]]",
        "Havrix 1440, autorisation 00558, est la dose adulte de 1,0 ml dès le dix-neuvième anniversaire, avec un rappel entre six et douze mois. [[10]]",
    ),
    (
        "Dans les études lues, 99 pour cent des personnes étaient séropositives trente jours après la première dose de Havrix. [[10]]",
        "Cette phrase n'est pas une efficacité de terrain pour chaque pays.",
        "Vivotif, autorisation 00467, est une gélule aux jours un, trois et cinq, à jeun depuis une heure, avec une eau qui ne dépasse pas 37 degrés. [[11]]",
        "Il est indiqué à partir de cinq ans révolus, et la protection devient effective environ dix jours après la dernière gélule. [[11]]",
    ),
    (
        "Si le pays exige le certificat, on vaccine assez tôt pour les dix jours de la fièvre jaune. [[9]]",
        "Si la personne a plus de 60 ans, on ne vaccine que si le risque de fièvre jaune est significatif et inévitable. [[9]]",
        "Si elle est immunodéprimée, Stamaril et Vivotif sont contre-indiqués. [[9]] [[11]]",
        "Si seule l'hépatite A est en jeu, on reste sur Havrix.",
    ),
    (
        "Cette lecture ne porte pas de milligramme d'un médicament.",
        "Les volumes lus sont 0,5 ml pour Stamaril et 1,0 ml pour Havrix 1440. [[9]] [[10]]",
        "L'enfant et l'adolescent jusqu'au dix-neuvième anniversaire reçoivent Havrix 720, soit 0,5 ml. [[10]]",
        "Cas corrigé : on n'écrit pas un rappel systématique tous les dix ans comme si l'information professionnelle l'avait démontré pour la vie entière.",
    ),
    (
        "Le certificat de fièvre jaune, selon le règlement sanitaire international cité par l'autorisation, vaut pour la vie. [[9]]",
        "La même autorisation dit qu'aucune étude prospective n'a démontré une protection toute la vie après une seule dose. [[9]]",
        "Un rappel de 0,5 ml peut être nécessaire si la réponse a été insuffisante et que le risque demeure. [[9]]",
        "On évite de débuter une grossesse pendant un mois après Stamaril. [[9]]",
    ),
    (
        "On dit le certificat, la limite des études, et le rappel possible, sans en choisir un seul.",
        "Après 60 ans, le risque de maladie grave liée au vaccin augmente. [[9]]",
        "Une vaccination faite par erreur pendant la grossesse ne justifie pas, dans le texte lu, une interruption. [[9]]",
        "Stamaril reste contre-indiqué pendant la grossesse, sauf nécessité absolue. [[9]]",
    ),
    (
        "Le piège est de promettre une protection à vie alors que l'étude prospective manque. [[9]]",
        "Le piège inverse est de refuser le certificat à vie écrit dans le règlement cité. [[9]]",
        "Le piège pédiatrique est de vacciner un nourrisson de moins de six mois. [[9]]",
        "Cas corrigé : on reporte Stamaril chez la personne greffée, et on explique pourquoi.",
    ),
])
from phrases_223_suite import (  # noqa: E402
    algo_de,
    commun,
    ess_de,
    niveaux_de,
    question_de,
    remplir,
    sources_items,
)

remplir(_k, _t, DETAILS)

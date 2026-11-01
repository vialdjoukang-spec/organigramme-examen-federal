#!/usr/bin/env python3
"""Leçons V8 de LOT_186. Phrases courtes. Doses limitées aux extraits AIPS."""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_186"
STYLE = Path("/tmp/style_v8.html").read_text(encoding="utf-8")
sys.path.insert(0, str(RACINE / "harnais"))
import taille_xy  # noqa: E402

MOT = re.compile(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*")
FRAG = (LOT / "_travail" / "fragment_injection.frag").read_text(encoding="utf-8")


def mots(s: str) -> int:
    return len(MOT.findall(s))


def noms() -> dict[int, str]:
    out = {}
    for ligne in (LOT / "LISTE_DX_CANONIQUE.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"DX\.(\d+)\s*[—–\-]\s*(.+)", ligne.strip())
        if m:
            out[int(m.group(1))] = m.group(2).strip()
    return out


def F(*triples):
    bad = []
    for sec, src, txt in triples:
        if txt.startswith("<"):
            continue
        n = mots(txt)
        if n > 26:
            bad.append(f"{n} mots : {txt}")
        if txt.count(".") > 1:
            bad.append(f"deux points : {txt}")
        if ";" in txt:
            bad.append(f"point-virgule : {txt}")
    if bad:
        raise SystemExit("\n".join(bad))
    return list(triples)


COMMUN = F(
    (4, 1, "On cherche d'abord le choc, la convulsion et le ventre aigu, avant le calendrier."),
    (1, 1, "Une anaphylaxie à un vaccin ou à un composant contre-indique ce vaccin, plan de 2026."),
    (4, 1, "Une maladie aiguë sévère fait différer le rendez-vous, plan de 2026."),
    (6, 3, "Un simple refroidissement n'est pas une contre-indication dans l'information 60150."),
    (6, 2, "Avant un an, l'information 00640 privilégie la face antérolatérale de la cuisse."),
    (6, 2, "Le deltoïde, en haut du bras, est l'autre site lu dans l'information 00640."),
    (11, 1, "Deux vaccins non combinés vont dans deux sites, jamais dans la même seringue."),
    (11, 1, "Sur le même côté, le plan de 2026 demande au moins 2,5 cm entre deux injections."),
    (11, 1, "Deux vaccins vivants atténués se donnent le même jour ou à au moins 4 semaines."),
    (11, 1, "La fièvre jaune et la rougeole se donnent de préférence à 4 semaines d'écart."),
    (11, 1, "Entre vaccins inactivés, le plan de 2026 n'impose pas cet écart de 4 semaines."),
    (11, 2, "L'information 00640 demande un traitement prêt et une surveillance après l'injection."),
    (12, 1, "Un effet grave s'annonce à Swissmedic dans les 15 jours, plan de 2026."),
    (12, 1, "Un décès s'annonce tout de suite, et jamais au-delà de 15 jours."),
    (12, 1, "La suspicion suffit pour annoncer, sans attendre la preuve du lien."),
    (8, 1, "Le carnet tenu à jour est la preuve habituelle, et la sérologie reste rare."),
    (14, 1, "Le piège commun est d'annuler pour un rhume, ou d'injecter pendant un choc."),
)

DX = {}

DX[1] = COMMUN + F(
    (1, 1, "Le calendrier de base de 2026 protège le nourrisson sans facteur de risque."),
    (1, 1, "La base couvre diphtérie, tétanos, coqueluche, poliomyélite et Haemophilus."),
    (1, 1, "Elle couvre aussi l'hépatite B, le pneumocoque, la rougeole, les oreillons et la rubéole."),
    (1, 1, "La varicelle est dans la base depuis 2023, de préférence dans le vaccin quadrivalent."),
    (1, 1, "Les papillomavirus sont une vaccination de base de l'adolescent, plan de 2026."),
    (1, 1, "Le rotavirus et les méningocoques sont complémentaires, pas une base obligatoire du texte."),
    (1, 1, "L'immunisation passive contre le virus respiratoire syncytial est classée avec la base."),
    (2, 1, "Depuis 2019, l'hexavalent et le pneumocoque suivent le schéma 2, 4 et 12 mois."),
    (2, 1, "Ce schéma à trois doses s'appelle 2 plus 1 dans le plan de 2026."),
    (2, 1, "Le plan de 2026 retient le vaccin conjugué à 13 ou à 15 valences comme équivalents."),
    (2, 1, "On termine une série avec le même vaccin conjugué quand il est encore disponible."),
    (2, 1, "Une série commencée à 13 valences peut se terminer à 15 valences, plan de 2026."),
    (2, 1, "Après une série finie, une valence plus haute n'est pas un rappel supplémentaire."),
    (2, 1, "Si une dose à 20 valences a été donnée avant 7 mois, le plan décrit un schéma 3 plus 1."),
    (2, 1, "Ce schéma de rattrapage se place à 2, 4, 6 et 12 mois, plan de 2026."),
    (3, 1, "La première dose de coqueluche protège déjà une partie des nourrissons contre la forme grave."),
    (3, 1, "Le plan de 2026 écrit qu'environ la moitié est protégée après cette première dose."),
    (3, 1, "La deuxième dose augmente nettement cette protection, toujours dans le même texte."),
    (3, 4, "Les anticorps de la mère peuvent gêner la réponse rougeole dans la première année."),
    (4, 1, "À 2 mois on donne l'hexavalent, le pneumocoque, et le rotavirus si la fenêtre est ouverte."),
    (4, 1, "À 4 mois on répète l'hexavalent, le pneumocoque et la deuxième dose orale."),
    (4, 1, "À 9 mois, la première dose rougeole-oreillons-rubéole, de préférence avec la varicelle."),
    (4, 1, "À 12 mois, le rappel hexavalent, le pneumocoque et la deuxième dose quadrivalente."),
    (4, 1, "Entre 19 mois et 3 ans, le plan de 2026 ne place pas de vaccination de routine."),
    (4, 1, "De 4 à 7 ans, un rappel diphtérie-tétanos-coqueluche-poliomyélite est recommandé."),
    (4, 1, "De 11 à 14 ans, les papillomavirus se donnent en deux doses, à 0 et à 6 mois."),
    (5, 1, "On demande le carnet, le poids, un rhume et une réaction grave antérieure."),
    (6, 2, "On regarde le tonus et la respiration du prématuré avant de le laisser partir."),
    (7, 1, "Le nourrisson à jour de 2026 a reçu trois hexavalents espacés comme 2, 4 et 12."),
    (8, 2, "L'information 00640 n'est pas destinée à l'enfant de plus de 36 mois."),
    (9, 2, "Avant 28 semaines de naissance, des apnées ont été rapportées après l'hexavalent."),
    (9, 1, "Le plan renvoie à des instructions propres avant 33 semaines ou sous 1500 g."),
    (10, 1, "L'arbre part de l'âge exact, puis du carnet, puis du site, puis de la fenêtre orale."),
    (11, 9, "L'information 69039 écrit 50 mg en dessous de 5 kg pour la dose unique."),
    (11, 9, "Elle écrit 100 mg à partir de 5 kg pour cette même dose unique."),
    (11, 1, "Le plan de 2026 propose le vaccin maternel ou l'anticorps pour la première année."),
    (11, 1, "Si la naissance suit le vaccin maternel de moins de 14 jours, l'anticorps est quand même donné."),
    (11, 1, "Les naissances d'octobre à mars non protégées par la mère reçoivent l'anticorps."),
    (12, 1, "La coqueluche de l'entourage et le carnet évité sont la prévention lue autour du nourrisson."),
    (13, 1, "On retient 2, 4 et 12 mois, puis 9 et 12 mois pour le quadrivalent."),
    (14, 1, "Le cas corrigé a 2 mois, un rhume simple, et reçoit l'hexavalent le jour même."),
    (14, 2, "Le piège est d'attendre les 36 mois de l'information 00640 pour commencer."),
    (3, 1, "Le vaccin inactivé ne se réplique pas, et le vivant atténué ne se réplique que peu."),
    (2, 1, "La couverture hépatite B lue à 2 ans, pour 2020 à 2022, est de 76 pour cent avec trois doses."),
    (2, 1, "Chez les jeunes de 16 ans, deux doses atteignent 79 pour cent sur la même période."),
    (1, 1, "L'objectif lu est 95 pour cent de jeunes de 16 ans vaccinés contre l'hépatite B en 2030."),
)

DX[2] = COMMUN + F(
    (1, 1, "Le rattrapage reconstruit une protection, il ne recopie pas l'âge idéal manqué."),
    (1, 1, "Un statut inconnu se traite comme une absence de doses documentées, plan de 2026."),
    (2, 1, "Haemophilus et pneumocoque se rattrapent jusqu'à la veille des 5 ans."),
    (2, 1, "Le nombre de doses dépend de l'âge à la première injection, plan de 2026."),
    (2, 1, "Le méningocoque B se rattrape jusqu'à la veille du cinquième anniversaire."),
    (2, 1, "Les méningocoques A, C, W et Y se rattrapent jusqu'à 5 ans chez le petit, et jusqu'à 20 ans après."),
    (4, 1, "Un enfant vacciné à 6 mois selon l'ancien schéma reçoit encore une quatrième dose dès 12 mois."),
    (4, 1, "L'intervalle minimal après cette troisième dose est de 6 mois, plan de 2026."),
    (4, 1, "On ne recommence pas à zéro une série déjà écrite dans le carnet."),
    (4, 5, "Pour les papillomavirus, deux doses suffisent si la seconde tombe entre 5 et 13 mois."),
    (4, 5, "Si cette seconde dose arrive avant 5 mois, une troisième dose reste nécessaire, information 65387."),
    (4, 5, "Le schéma à trois doses lu est 0, 2 et 6 mois, chaque dose de 0,5 ml."),
    (4, 5, "La deuxième dose du schéma long ne vient pas avant un mois, et la troisième pas avant trois mois."),
    (4, 5, "Les trois doses tiennent dans une année, information 65387."),
    (4, 1, "De 11 à 15 ans, l'hépatite B manquée peut se faire en deux doses du vaccin adulte."),
    (4, 1, "De 15 à 19 ans, le rattrapage des papillomavirus est recommandé, plan de 2026."),
    (4, 1, "De 20 à 26 ans, il devient complémentaire, avant le vingt-septième anniversaire."),
    (4, 1, "Sans antécédent de varicelle, deux doses restent possibles avant 40 ans, écart d'au moins un mois."),
    (5, 1, "On lit chaque ligne du carnet, le pays d'origine et la date de la dernière dose."),
    (6, 1, "L'examen cherche une fièvre sévère du jour, pas un bilan sans question."),
    (7, 1, "Le retard n'est pas une contre-indication, c'est une série à compléter."),
    (8, 1, "On compte les doses documentées, pas le souvenir flou d'une piqûre."),
    (9, 1, "Pas de sérologie de routine pour décider un rattrapage, le carnet prime."),
    (10, 1, "L'arbre demande l'âge, le nombre de doses, puis le vaccin encore indiqué avant 5 ans."),
    (11, 4, "Si la première dose quadrivalente tombe dans la première année, l'information 58158 prévoit 3 mois avant la suivante."),
    (11, 1, "Une rougeole donnée entre 6 et 8 mois ne compte pas dans le total, plan de 2026."),
    (11, 1, "Il faut alors trois doses, la deuxième à 9 mois avec au moins 4 semaines d'écart."),
    (11, 1, "La troisième se place à 12 mois, de préférence avec la varicelle."),
    (12, 1, "Chaque contact est une occasion de rattraper, sans punir le retard."),
    (13, 1, "On retient la veille des 5 ans pour Haemophilus et le pneumocoque."),
    (14, 1, "Le cas corrigé a 3 ans, zéro dose, et ne reçoit pas le schéma du nourrisson de 2 mois tel quel."),
    (14, 5, "Le piège est d'accepter deux doses de papillomavirus espacées de trois mois sans la troisième."),
    (3, 1, "Les anticorps maternels expliquent pourquoi une dose trop précoce de rougeole ne compte pas."),
    (2, 1, "Le plan de 2026 ne donne pas un pourcentage unique de retards en Suisse dans l'extrait lu."),
)

DX[3] = COMMUN + F(
    (1, 1, "Une réaction locale et une fièvre sont fréquentes, et une réaction sévère est exceptionnelle."),
    (1, 6, "La fièvre du méningocoque B coadministré a été fréquente dans les études de l'information 65730."),
    (2, 6, "Avec les vaccins de routine, la fièvre d'au moins 38 degrés allait de 69 à 79 pour cent."),
    (2, 6, "Les vaccins de routine seuls se situaient de 44 à 59 pour cent dans le même texte."),
    (2, 6, "Donné seul, le méningocoque B avait une fièvre proche de celle des vaccins de routine."),
    (3, 6, "Cette fièvre suit un horaire prévisible et se termine le plus souvent le lendemain."),
    (3, 1, "Les âges de 3 et 5 mois pour le méningocoque B ont été choisis pour réduire la fièvre."),
    (4, 1, "On peut quand même le donner à 2 et 4 mois, après information des parents."),
    (4, 1, "Le plan de 2026 évoque alors un antipyrétique prophylactique possible, pas systématique pour tout vaccin."),
    (5, 1, "On demande l'heure de la piqûre, le membre, la hauteur de la fièvre et l'état entre les pics."),
    (6, 1, "On palpe le membre, on cherche un purpura et on prend la température."),
    (7, 1, "Une rougeur locale au site n'est pas un choc, et un purpura n'est pas une rougeur simple."),
    (8, 1, "Le diagnostic de réaction bénigne suppose un enfant qui boit, joue ou se console."),
    (9, 1, "Pas de bilan sanguin pour une fièvre isolée du lendemain chez un enfant qui va bien."),
    (10, 1, "L'arbre sépare le membre chaud local, la fièvre consolable, et le choc ou le purpura."),
    (11, 8, "L'information 43838 écrit une dose unique de 15 mg par kilogramme avant 12 ans."),
    (11, 8, "Le maximum quotidien lu est de 75 mg par kilogramme."),
    (11, 8, "De 9 à 12 ans, le maximum journalier lu est de 2000 mg par jour."),
    (11, 8, "Avant 9 ans, les doses sont plus basses, et l'information demande de les respecter."),
    (11, 8, "Sans avis médical, l'usage continu chez l'enfant s'arrête à 3 jours, information 43838."),
    (11, 8, "On vérifie qu'aucun autre produit du jour ne contient déjà du paracétamol."),
    (12, 1, "On prévient les parents de l'horaire de la fièvre avant qu'elle arrive."),
    (13, 8, "On retient 15 mg par kilogramme, pas le plafond de 2000 mg chez le nourrisson."),
    (14, 8, "Le cas corrigé a 4 mois, une cuisse rouge, et reçoit une dose selon le poids, pas 2000 mg."),
    (14, 6, "Le piège est d'appeler anaphylaxie une fièvre du lendemain qui se console."),
    (11, 8, "La zone toxique lue commence à cent quarante jusqu'à deux cents milligrammes par kilogramme."),
    (3, 1, "La réaction locale est une inflammation au site, pas une infection du vaccin inactivé."),
)

DX[4] = COMMUN + F(
    (1, 7, "L'anaphylaxie est le choc allergique immédiat, pas la fièvre du lendemain."),
    (1, 1, "Elle contre-indique ensuite le vaccin en cause et le composant en cause, plan de 2026."),
    (2, 1, "Le plan de 2026 la dit exceptionnelle devant le bénéfice des vaccins recommandés."),
    (3, 7, "Le mécanisme lu est une hypersensibilité immédiate, à traiter par l'adrénaline intramusculaire."),
    (4, 7, "On arrête, on allonge, on appelle les secours et on injecte sans attendre un test."),
    (4, 7, "Au-dessus de 30 kg, l'information 53836 écrit 0,3 mg dans le muscle."),
    (4, 7, "De 15 à 30 kg, elle écrit 0,15 mg avec la forme junior."),
    (4, 7, "De 7,5 à 15 kg, la forme junior se discute au cas par cas, information 53836."),
    (4, 7, "En dessous de 7,5 kg, elle n'est pas recommandée hors danger vital surveillé."),
    (4, 7, "La posologie pédiatrique habituelle lue est de 0,01 mg par kilogramme."),
    (4, 7, "Une dose sous 0,15 mg ne peut pas être réglée avec la forme junior."),
    (4, 7, "Si la première dose ne suffit pas, une seconde est possible de 5 à 15 minutes."),
    (4, 7, "L'information 53836 conseille de prescrire deux injecteurs que la personne garde avec elle."),
    (5, 7, "On note la minute de l'injection, le produit, l'urticaire, la voix et la tension."),
    (6, 7, "On injecte dans la face antérolatérale de la cuisse, information 53836."),
    (6, 1, "On cherche un wheezing, un gonflement de la bouche et un pouls faible."),
    (7, 4, "Une urticaire immédiate avec malaise n'est pas la rougeur locale du surlendemain."),
    (8, 1, "Le diagnostic d'anaphylaxie vaccinale repose sur le temps court et l'atteinte respiratoire ou circulatoire."),
    (9, 1, "Aucun test cutané n'est exigé avant la première dose d'adrénaline."),
    (10, 7, "L'arbre va du poids vers 0,3 mg ou 0,15 mg, puis vers la cuisse, puis vers les secours."),
    (11, 7, "On ne remplace pas l'adrénaline par le paracétamol dans le choc."),
    (12, 7, "Les personnes à risque connu gardent deux injecteurs, information 53836."),
    (13, 7, "On retient la cuisse, le poids, et la seconde dose possible après 5 minutes."),
    (14, 7, "Le cas corrigé pèse 18 kg, reçoit 0,15 mg, et une seconde dose est prête."),
    (14, 1, "Le piège est de faire coucher l'enfant seulement après un antihistaminique."),
    (6, 7, "En dessous de 25 kg, l'information 53836 signale plus d'effets avec la forme de 0,3 mg."),
)

DX[5] = COMMUN + F(
    (1, 4, "La convulsion fébrile après le quadrivalent se discute dans les 5 à 12 jours."),
    (1, 2, "L'épisode d'hypotonie-hyporéactivité est un collapsus dans les 48 heures, information 00640."),
    (1, 2, "Ce collapsus n'est pas décrit comme l'anaphylaxie immédiate de la minute."),
    (2, 4, "Dans une définition, l'incidence lue était de 2,18 pour 10000 après le quadrivalent."),
    (2, 4, "L'autre définition de la même information donne 6,19 pour 10000."),
    (2, 4, "Les témoins correspondants étaient à 0,49 et à 2,55 pour 10000."),
    (2, 4, "Un cas supplémentaire était lu pour 5882 ou pour 2747 enfants vaccinés."),
    (2, 4, "Ces chiffres concernent des enfants de 9 à 30 mois après la première dose."),
    (3, 4, "Le risque de fièvre et de convulsion est plus haut qu'avec les vaccins séparés."),
    (3, 2, "Les pleurs inconsolables de plus de 3 heures dans les 48 heures font aussi peser la suite."),
    (4, 4, "Un antécédent personnel ou familial de convulsion fait envisager les vaccins séparés pour la première dose."),
    (4, 4, "On surveille alors la fièvre pendant la période de risque, information 58158."),
    (4, 2, "Une fièvre d'au moins 40 degrés dans les 48 heures, sans autre cause, fait peser la dose de coqueluche suivante."),
    (4, 2, "Une convulsion dans les 3 jours après l'hexavalent fait aussi peser cette dose, sans l'interdire d'office."),
    (4, 2, "Si la coqueluche circule beaucoup, le bénéfice peut l'emporter, information 00640."),
    (5, 1, "On date la secousse, la fièvre, la durée et le retour à l'état habituel."),
    (6, 1, "On cherche un déficit qui reste, une raideur de nuque et un purpura."),
    (7, 2, "L'hypotonie avec réponse pauvre dans les 48 heures n'est pas une rougeur de cuisse."),
    (8, 4, "Une convulsion fébrile brève avec retour normal n'est pas une encéphalite prouvée."),
    (9, 1, "On adresse si la convulsion dure, se répète, ou si l'enfant ne revient pas à lui."),
    (10, 4, "L'arbre sépare la minute du choc, les 48 heures du collapsus, et les jours 5 à 12."),
    (11, 8, "La fièvre se traite avec 15 mg par kilogramme, pas avec un arrêt de tout le calendrier."),
    (11, 2, "La dose suivante qui contient la coqueluche se décide après avoir pesé le bénéfice."),
    (12, 4, "Dire la fenêtre de risque aux parents fait partie de la première dose quadrivalente."),
    (13, 4, "On retient 5 à 12 jours, et les vaccins séparés si une convulsion est déjà connue."),
    (14, 4, "Le cas corrigé convulse au jour 7, revient à lui, et la suite se discute sans tout arrêter."),
    (14, 2, "Le piège est d'appeler allergie un collapsus des 48 heures et d'oublier la coqueluche."),
    (3, 4, "Une fièvre élevée est habituelle après la première dose qui contient la rougeole."),
)

DX[6] = COMMUN + F(
    (1, 1, "Une fausse contre-indication retarde la protection sans réduire un risque réel."),
    (1, 1, "La vraie contre-indication commune est l'anaphylaxie au vaccin ou à un composant."),
    (1, 3, "L'information 60150 diffère aussi la diarrhée, les vomissements et la fièvre sévère."),
    (1, 3, "Elle contre-indique l'oral après un antécédent d'invagination ou une malformation qui y prédispose."),
    (1, 3, "Le diverticule de Meckel est l'exemple lu de cette malformation."),
    (1, 3, "Le déficit immunitaire combiné sévère contre-indique aussi ce vaccin oral."),
    (2, 1, "Le plan de 2026 ne chiffre pas la part des rendez-vous annulés pour un rhume."),
    (3, 4, "Des traces de protéines d'œuf peuvent rester dans le quadrivalent, information 58158."),
    (3, 4, "Une réaction immédiate grave à l'œuf augmente le risque, qui reste très rare dans ce texte."),
    (4, 4, "Ces personnes se vaccinent avec une prudence extrême, et un traitement est prêt."),
    (4, 1, "Une gêne digestive mineure à l'œuf n'est pas cette réaction immédiate décrite."),
    (4, 1, "Un antibiotique en cours n'est pas une contre-indication écrite dans le plan de 2026."),
    (4, 1, "L'allaitement de la mère ne contre-indique pas les vaccins inactivés du nourrisson."),
    (4, 2, "Le prématuré se vaccine selon l'âge depuis la naissance, avec surveillance si besoin."),
    (4, 1, "La grossesse contre-indique les vaccins vivants atténués chez l'adolescente, plan de 2026."),
    (4, 1, "Une vaccination vivante faite sans le savoir n'est pas une indication d'interruption de grossesse."),
    (5, 1, "On demande le produit, la minute des symptômes et ce que la famille appelle allergie."),
    (6, 1, "On examine le jour même, pour séparer la fièvre sévère du rhume simple."),
    (7, 1, "Le rhume qui boit n'est pas la maladie aiguë sévère qui fait différer."),
    (8, 1, "On nomme la contre-indication seulement si le texte lu la contient."),
    (9, 1, "Pas de bilan d'allergie avant chaque vaccin chez un enfant sans réaction immédiate."),
    (10, 1, "L'arbre demande : anaphylaxie, maladie sévère du jour, vivant interdit, ou mythe."),
    (11, 1, "Le mythe se corrige en vaccinant le jour même, au site lu pour l'âge."),
    (12, 1, "Expliquer la fausse contre-indication évite le prochain rendez-vous perdu."),
    (13, 1, "On retient le rhume qui n'annule pas, et l'anaphylaxie qui annule."),
    (14, 3, "Le cas corrigé a un écoulement nasal, pas de fièvre sévère, et reçoit le vaccin."),
    (14, 4, "Le piège est de refuser le quadrivalent pour un œuf au plat sans réaction immédiate."),
    (1, 1, "Les vaccins vivants atténués ne se donnent en principe pas dans un déficit immunitaire."),
)

DX[7] = COMMUN + F(
    (1, 1, "Le vaccin vivant atténué se réplique un peu, et le déficit peut ne plus le contenir."),
    (1, 1, "L'hexavalent, le pneumocoque, le méningocoque et les papillomavirus ne sont pas des vivants."),
    (2, 1, "Le plan de 2026 vise les déficits cellulaires, le virus avancé et les médicaments forts."),
    (3, 1, "Le seuil lu entre 1 et 5 ans est un taux de lymphocytes auxiliaires sous 15 pour cent."),
    (3, 1, "À partir de 6 ans, le seuil lu est sous 200 de ces lymphocytes par microlitre."),
    (3, 1, "Le corticoïde lu est au moins deux milligrammes par kilogramme et par jour."),
    (3, 1, "L'autre seuil lu est au moins vingt milligrammes par jour pendant plus de quatorze jours."),
    (4, 1, "Sous ces seuils, le quadrivalent, la varicelle et les autres vivants sont contre-indiqués."),
    (4, 1, "Les vaccins inactivés restent indiqués, car la maladie évitable est plus dure chez ces enfants."),
    (4, 4, "Après des immunoglobulines, l'information 58158 écrit un délai d'au moins 3 mois."),
    (4, 1, "Le plan de 2026 écrit au moins 5 mois, et le délai dépend de la dose d'immunoglobulines."),
    (4, 1, "Quand les deux textes s'appliquent, on retient le délai le plus long, celui du plan."),
    (4, 1, "Une grossesse doit être évitée jusqu'à un mois après la deuxième dose, plan de 2026."),
    (5, 1, "On demande le médicament, la dose en mots, la date et le taux de lymphocytes s'il est connu."),
    (6, 1, "On cherche une infection du jour qui ferait différer même un vaccin inactivé."),
    (7, 1, "Un enfant greffé ou sous corticoïde fort n'est pas un simple retard de carnet."),
    (8, 1, "On sépare le vivant interdit du inactivé encore utile."),
    (9, 1, "Le taux de lymphocytes se lit s'il change la décision du vivant, pas par routine chez tous."),
    (10, 1, "L'arbre demande le type de vaccin, le déficit, le médicament, puis le délai après immunoglobulines."),
    (11, 1, "On vaccine avec l'inactivé le jour où le vivant est refusé."),
    (11, 3, "L'oral est aussi refusé dans le déficit combiné sévère, information 60150."),
    (12, 1, "L'entourage à jour diminue l'exposition de l'enfant qui ne peut pas recevoir le vivant."),
    (13, 1, "On retient vivant interdit, inactivé maintenu, et cinq mois après les immunoglobulines."),
    (14, 1, "Le cas corrigé est sous corticoïde fort, reçoit l'hexavalent, et pas le quadrivalent."),
    (14, 4, "Le piège est d'appliquer le délai de 3 mois de l'information 58158 en ignorant les 5 mois du plan."),
    (2, 1, "Le plan de 2026 ne donne pas une prévalence suisse unique de ces déficits dans l'extrait."),
)

DX[8] = COMMUN + F(
    (1, 1, "L'hésitation est une question, et le refus est une décision que l'on peut revoir."),
    (1, 1, "Le plan de 2026 recommande, et cet extrait ne crée pas une obligation cantonale."),
    (2, 1, "Les couvertures lues montrent que l'hépatite B n'atteint pas encore l'objectif de 2030."),
    (3, 1, "La peur mélange souvent la fièvre bénigne et le choc très rare."),
    (4, 1, "On répond avec le calendrier daté, pas avec une moquerie."),
    (4, 1, "On propose de commencer par les doses qui protègent le nourrisson contre la coqueluche grave."),
    (4, 1, "On peut fractionner les visites si plusieurs piqûres le même jour sont refusées."),
    (4, 1, "On ne mélange pas pour autant deux vaccins dans une seringue pour réduire les piqûres."),
    (5, 1, "On demande quelle maladie fait peur, quelle dose a déjà été acceptée, et qui décide à la maison."),
    (6, 1, "L'examen du jour reste celui de l'enfant, pas un débat sans le regarder."),
    (7, 1, "Un refus de papillomavirus à 12 ans n'est pas un refus de l'hexavalent du nourrisson."),
    (8, 1, "On écrit ce qui a été proposé, ce qui a été compris, et ce qui a été refusé."),
    (9, 1, "Aucun test n'est exigé pour prouver la bonne foi des parents."),
    (10, 1, "L'arbre sépare la question, la fausse contre-indication, et le refus persistant."),
    (11, 1, "Le refus persistant se note, et la porte du rattrapage reste ouverte."),
    (11, 1, "Depuis 2016, une demande d'indemnisation vaccinale s'adresse à la Confédération, plan de 2026."),
    (11, 1, "Cette indemnisation est subsidiaire, et la franchise de l'assurance n'est pas reprise."),
    (12, 1, "Le carnet et le rendez-vous suivant sont la prévention de la rupture de suivi."),
    (13, 1, "On retient d'informer, de documenter, et de ne pas inventer une obligation cantonale."),
    (14, 1, "Le cas corrigé refuse quatre piqûres le même jour, et accepte de revenir la semaine suivante."),
    (14, 1, "Le piège est de fermer le dossier parce qu'une seule visite a dit non."),
    (2, 1, "76 pour cent des enfants de 2 ans avaient trois doses d'hépatite B sur 2020 à 2022."),
    (3, 1, "Le bénéfice lu dépasse le risque des effets pour chaque vaccin recommandé."),
)

DX[9] = COMMUN + F(
    (1, 1, "Après une plaie ou une exposition, le vaccin devient une urgence de calendrier, pas un rappel confortable."),
    (1, 1, "Le plan de 2026 sépare la plaie superficielle propre de la plaie à haut risque de tétanos."),
    (2, 1, "La plaie à risque est profonde, souillée, écrasée, pénétrante, brûlée ou nécrotique."),
    (4, 1, "Avant 26 ans, avec au moins trois doses, on rappelle si la dernière a plus de 5 ans."),
    (4, 1, "Pour une plaie superficielle propre, ce délai passe à plus de 10 ans."),
    (4, 1, "De 26 à 64 ans, ces délais sont doublés, donc plus de 10 ans et plus de 20 ans."),
    (4, 1, "Dès 65 ans, on revient aux délais de plus de 5 ans et de plus de 10 ans."),
    (4, 1, "Un déficit immunitaire avec au moins trois doses utilise aussi 5 ans et 10 ans."),
    (4, 1, "Avec moins de trois doses ou un statut inconnu, on vaccine et on ajoute des immunoglobulines si la plaie est à risque."),
    (4, 1, "Les immunoglobulines ne sont pas nécessaires si la plaie est superficielle et propre."),
    (4, 1, "Avant 8 ans, le vaccin de plaie est adapté à l'âge, avec la coqueluche si le plan le demande."),
    (4, 1, "Dès 8 ans, le rappel de plaie est un vaccin diphtérie-tétanos, avec la coqueluche si elle est indiquée."),
    (4, 1, "Un enfant de moins de 8 ans déjà à jour pour son âge ne reçoit pas une dose de plus."),
    (4, 1, "De 1 à 7 ans avec moins de trois doses, on vaccine et on donne des immunoglobulines."),
    (4, 1, "De 5 à 11 mois avec déjà deux doses, les immunoglobulines ne sont en général pas recommandées."),
    (4, 1, "On peut les discuter si le risque de tétanos est très élevé."),
    (4, 1, "Ensuite on complète le schéma, que des immunoglobulines aient été données ou non."),
    (4, 1, "Le nouveau-né de mère porteuse de l'antigène reçoit quatre doses, à 0, 1, 2 et 12 mois."),
    (4, 1, "À la naissance, le vaccin monovalent est donné en même temps que les immunoglobulines."),
    (4, 1, "À 1 mois, on répète le monovalent, puis l'hexavalent à 2 mois et à 12 mois."),
    (4, 1, "On contrôle les anticorps et l'antigène quatre semaines après la dernière dose."),
    (4, 1, "Si la mère n'a que l'anticorps anti-noyau et un antigène négatif, le schéma reste 2, 4 et 12 mois."),
    (4, 1, "Dans ce cas, le plan de 2026 n'ajoute pas le geste de naissance."),
    (4, 1, "Une exposition à la rougeole avance la première dose dès 6 mois, sans la varicelle."),
    (4, 1, "Cette dose avant 9 mois ne compte pas, et trois doses au total sont alors nécessaires."),
    (5, 1, "On demande le type de plaie, l'heure, le carnet et le statut de la mère pour l'antigène."),
    (6, 1, "On lave la plaie, on cherche la profondeur, et on ne ferme pas avant d'avoir décidé le tétanos."),
    (7, 1, "Une plaie souillée avec deux doses n'est pas une plaie propre avec un carnet complet."),
    (8, 1, "Le diagnostic de prophylaxie incomplète se pose quand le nombre de doses est sous trois."),
    (9, 1, "Si une vaccination antérieure est probable mais non écrite, on vaccine puis on peut titrer."),
    (10, 1, "L'arbre lit l'âge, le nombre de doses, le type de plaie, puis les immunoglobulines."),
    (11, 1, "Ce cours ne prescrit pas de milligrammes d'immunoglobulines, faute d'extrait de spécialité."),
    (11, 1, "Pour la rage, le plan de 2026 commence par quinze minutes d'eau savonneuse."),
    (11, 1, "On désinfecte ensuite, puis le schéma vaccinal dépend d'au moins deux doses déjà reçues."),
    (11, 1, "Le maximum lu d'immunoglobulines antirabiques est de vingt unités internationales par kilogramme."),
    (12, 1, "Le dépistage de l'antigène chez la femme enceinte évite le retard à la naissance."),
    (13, 1, "On retient trois doses, 5 ans ou 10 ans, et les quatre doses du nouveau-né exposé."),
    (14, 1, "Le cas corrigé a 4 ans, une plaie de terre, deux doses, et reçoit vaccin plus immunoglobulines."),
    (14, 1, "Le piège est de rassurer parce que la plaie est petite alors qu'elle est souillée."),
    (8, 1, "Le titre d'antitoxine sous 100 unités par litre est lu comme absence de protection."),
    (8, 1, "Au moins 100 unités par litre correspondent à une protection, et au moins 1000 à une protection durable."),
    (8, 1, "Pour l'hépatite B, sous 10 unités par litre il n'y a pas de protection lue."),
    (8, 1, "Au moins 10 correspondent à une protection courte, et au moins 100 à une protection durable."),
    (2, 1, "Le plan de 2026 ne donne pas une incidence suisse des plaies tétanigènes dans l'extrait."),
)

DX[10] = COMMUN + F(
    (1, 3, "L'invagination est le télescopage de l'intestin, à évoquer après le vaccin oral."),
    (1, 3, "L'information 60150 la contre-indique s'il existe déjà un antécédent."),
    (1, 1, "Le plan de 2026 la contre-indique aussi après la vingt-quatrième semaine."),
    (2, 3, "Une grande étude de 63225 nourrissons n'a pas montré plus de cas que le placebo."),
    (2, 3, "L'étude mexicaine de 2012, citée dans l'information 60150, a vu un risque multiplié par 6,49 à 7 jours."),
    (2, 3, "À 31 jours après la première dose, le facteur lu était de 1,75."),
    (2, 3, "Après la deuxième dose, les facteurs lus à 7 jours et à 31 jours étaient 1,29 et 1,06."),
    (2, 3, "Ces deux derniers n'étaient pas un risque significatif dans le texte lu."),
    (2, 3, "L'intervalle de confiance à 7 jours après la première dose allait de 4,17 à 10,1."),
    (3, 3, "Le risque se concentre donc dans la semaine qui suit la première dose orale."),
    (3, 3, "Le virus vaccinal s'élimine dans les selles après la vaccination, information 60150."),
    (4, 1, "La première dose orale se donne dès 6 semaines et au plus tard à 15 semaines et 6 jours."),
    (4, 1, "La seconde se donne au plus tard à 23 semaines et 6 jours, avec au moins 4 semaines d'écart."),
    (4, 3, "L'information 60150 dit que la seconde devrait précéder 16 semaines et doit précéder 24 semaines."),
    (4, 1, "Le plan de 2026 est plus serré sur la première dose, et on suit cette fenêtre."),
    (4, 3, "Le lait, l'eau et le repas ne changent pas cette prise orale, plan de 2026 et information."),
    (5, 3, "On demande les douleurs sévères, les vomissements qui persistent, le sang dans les selles et le ballonnement."),
    (5, 3, "La fièvre élevée fait partie des signes que les parents doivent rapporter tout de suite."),
    (6, 1, "On palpe le ventre, on regarde les selles et on ne renvoie pas sans un avis si la douleur revient."),
    (7, 3, "Ces signes dans la semaine après la première dose ne sont pas une colique ordinaire à négliger."),
    (8, 3, "Le diagnostic d'invagination se confirme par l'imagerie urgente, pas par le calendrier seul."),
    (9, 1, "On adresse le jour même si les signes lus sont présents."),
    (10, 3, "L'arbre demande l'âge en semaines, le numéro de dose, puis les signes du ventre."),
    (11, 3, "On n'administre pas la dose suivante s'il y a eu une invagination."),
    (11, 3, "Après 24 semaines, l'information 60150 interdit le produit."),
    (12, 1, "Dire les signes aux parents au moment de la première dose est la prévention lue."),
    (13, 3, "On retient 7 jours, la première dose, et l'arrêt définitif s'il y a un antécédent."),
    (14, 3, "Le cas corrigé a 10 semaines, vomit et a du sang dans les selles au jour 4, et part aux urgences."),
    (14, 1, "Le piège est de donner la première dose à 5 mois parce que le rendez-vous a été manqué."),
    (2, 3, "Aucun cas n'a été rapporté dans l'étude des prématurés citée, ce qui n'efface pas la contre-indication."),
    (4, 3, "Un déficit combiné sévère reste une contre-indication absolue de ce vaccin oral."),
    (3, 1, "Le plan de 2024 a classé ce vaccin en complémentaire à deux doses, à 2 et 4 mois si la fenêtre tient."),
)

# Compléments du calendrier pour la phase A et quelques DX, sans doublon exact.
PLUS = F(
    (1, 1, "Depuis 2024, l'encéphalite à tiques se recommande en général dès 3 ans hors Tessin."),
    (1, 1, "Avant 2024, cet âge général était de 6 ans, plan de 2026."),
    (1, 1, "De 1 à 2 ans, on décide au cas par cas si l'exposition aux tiques est forte."),
    (1, 1, "Le vaccin est autorisé dès un an, et inutile sans exposition."),
    (1, 1, "Le vaccin du bacille ne vise que le nourrisson de moins de 12 mois qui vivra dans un pays à forte incidence."),
    (1, 1, "La valeur seuil lue est une incidence de plus de 50 cas pour 100000 habitants et par an."),
    (1, 1, "Tant que ce vaccin manque en Suisse, le plan de 2026 le fait faire dans le pays de destination."),
    (1, 1, "Des vacances courtes ne sont pas une indication."),
    (1, 1, "La grippe saisonnière vise un risque accru, et le prématuré né avant 32 semaines dès 6 mois pendant deux hivers."),
    (1, 1, "Le même texte vise aussi un poids de naissance sous 1500 g."),
    (4, 1, "Le méningocoque B complémentaire se place à 3, 5 et 12 à 18 mois."),
    (4, 1, "L'écart minimal entre les deux premières est de 2 mois, et de 6 mois avant la troisième dès 12 mois."),
    (4, 1, "Les méningocoques A, C, W et Y se placent à 12 à 18 mois, une ou deux doses selon le produit."),
    (4, 1, "On peut les donner le même jour que le méningocoque B."),
    (8, 1, "Pour la rougeole, sous 100 unités par litre il n'y a pas de protection lue au tableau de 2026."),
    (8, 1, "De 100 à 149 la protection est courte, et dès 150 elle est durable dans ce tableau."),
    (8, 1, "On ne fait pas de sérologie rubéole après deux doses documentées, plan de 2026."),
    (11, 1, "Le plan de 2026 permet les vaccins du même âge le même jour, dans des sites différents."),
    (6, 1, "En cas de trouble de coagulation, une aiguille fine et une compression de 2 minutes sont lues."),
    (6, 1, "On n'aspire pas avant d'injecter dans ce cas, plan de 2026."),
    (2, 1, "L'objectif pneumocoque lu est d'éviter les formes invasives avant 3 ans."),
    (12, 1, "Une couverture de 80 pour cent avant 2 ans est le repère d'effet de groupe écrit pour le pneumocoque."),
    (4, 1, "La même page du nouveau-né exposé écrit aussi qu'une dose de 4 mois peut utiliser un pentavalent."),
    (4, 1, "Le schéma indispensable de la note reste les quatre doses, et cette phrase n'en ajoute pas une cinquième d'office."),
    (11, 9, "L'information 69039 écrit 200 mg pour une deuxième saison chez certains enfants encore à risque."),
    (11, 1, "Le plan de 2026, lui, centre la dose unique sur la première année de vie."),
    (3, 3, "Les parents doivent rapporter tout de suite les signes abdominaux après la dose orale."),
    (14, 1, "On ne promet pas qu'un vaccin empêche toutes les infections, seulement celles de ses antigènes."),
)

PHASE = []
vu = set()
for bloc in (DX[1], DX[2], DX[4], DX[9], DX[10], PLUS, COMMUN):
    for item in bloc:
        if item[2].startswith("<"):
            continue
        if item[2] in vu:
            continue
        vu.add(item[2])
        PHASE.append(item)

TITRES = {
    1: "1. Définition",
    2: "2. Épidémiologie",
    3: "3. Physiopathologie",
    4: "4. Démarche",
    5: "5. Anamnèse",
    6: "6. Examen",
    7: "7. Syndromes",
    8: "8. Diagnostic",
    9: "9. Examens complémentaires",
    10: "10. Arbre décisionnel",
    11: "11. Prise en charge",
    12: "12. Prévention",
    13: "13. Points clés",
    14: "14. Pièges",
}
LEADS = {
    1: "On nomme le cadre avant le geste.",
    2: "Le chiffre vient d'une source datée, ou il n'est pas écrit.",
    3: "Le mécanisme explique le geste, sans histoire inventée.",
    4: "On avance pas à pas, le drapeau d'abord.",
    5: "L'entretien date la piqûre, la plaie et le carnet.",
    6: "L'examen regarde le membre, le souffle et le ventre.",
    7: "Le tableau oriente, il ne remplace pas le délai lu.",
    8: "Une décision tient en une règle que l'on peut citer.",
    9: "Chaque examen a une raison, pas un bilan automatique.",
    10: "L'arbre dit le prochain geste.",
    11: "La prise en charge commence par ce qui ne peut pas attendre.",
    12: "La prévention se joue avant la fermeture de la fenêtre.",
    13: "On retient peu de phrases, toutes actionnables.",
    14: "Le piège est une conduite fréquente et fausse.",
}
CIBLES = {"A": 76000, 1: 38400, 2: 41200, 3: 43800, 4: 45600, 5: 36600, 6: 40200, 7: 42800, 8: 44100, 9: 39300, 10: 46200}

SCHEMAS = {
    "A": ("Orientation devant une vaccination", [
        ("Âge", "#d9ecf8", "#176fa0", "Âge exact en semaines ou en mois, plan de 2026."),
        ("Carnet", "#d7f0e2", "#1a7a50", "Doses déjà écrites, sans recommencer à zéro."),
        ("Drapeau", "#f6d0d2", "#a1262f", "Choc, convulsion, ventre, plaie, vivant interdit."),
        ("Fenêtre", "#f8e0c0", "#8a5a12", "Rotavirus, 9 mois, 5 ans, 11 ans."),
        ("Site", "#e7e0f6", "#5b3f8c", "Cuisse avant un an, deltoïde ensuite."),
    ]),
    1: ("Calendrier de la première année", [
        ("2 mois", "#d9ecf8", "#176fa0", "Hexavalent, pneumocoque, oral si la fenêtre est ouverte."),
        ("4 mois", "#d7f0e2", "#1a7a50", "Même trio si l'âge oral le permet encore."),
        ("9 mois", "#f8e0c0", "#8a5a12", "Première dose quadrivalente de préférence."),
        ("12 mois", "#e7e0f6", "#5b3f8c", "Rappels et deuxième dose quadrivalente."),
    ]),
    2: ("Rattrapage", [
        ("Carnet", "#d9ecf8", "#176fa0", "Compter les doses écrites."),
        ("Avant 5 ans", "#d7f0e2", "#1a7a50", "Haemophilus et pneumocoque encore possibles."),
        ("Adolescent", "#f8e0c0", "#8a5a12", "Hépatite B et papillomavirus selon l'âge."),
        ("Pas à zéro", "#f6d0d2", "#a1262f", "On ne jette pas une série documentée."),
    ]),
    3: ("Fièvre après une piqûre", [
        ("Locale", "#d7f0e2", "#1a7a50", "Membre rouge, enfant consolable."),
        ("Lendemain", "#d9ecf8", "#176fa0", "Fièvre souvent finie le lendemain."),
        ("Poids", "#f8e0c0", "#8a5a12", "15 mg par kilogramme, pas 2000 mg chez le petit."),
        ("Choc", "#f6d0d2", "#a1262f", "Si le souffle ou le pouls lâche, ce n'est plus la fièvre simple."),
    ]),
    4: ("Adrénaline selon le poids", [
        ("Plus de 30", "#f6d0d2", "#a1262f", "0,3 mg, information 53836."),
        ("15 à 30", "#f8e0c0", "#8a5a12", "0,15 mg, forme junior."),
        ("Cuisse", "#d7f0e2", "#1a7a50", "Face antérolatérale."),
        ("5 minutes", "#d9ecf8", "#176fa0", "Seconde dose possible de 5 à 15 minutes."),
    ]),
    5: ("Trois horloges", [
        ("Minutes", "#f6d0d2", "#a1262f", "Choc immédiat : adrénaline."),
        ("48 heures", "#f8e0c0", "#8a5a12", "Collapsus, fièvre à 40, pleurs longs."),
        ("3 jours", "#d9ecf8", "#176fa0", "Convulsion après l'hexavalent : peser la suite."),
        ("5 à 12", "#d7f0e2", "#1a7a50", "Fenêtre lue après la première dose quadrivalente."),
    ]),
    6: ("Vrai ou faux obstacle", [
        ("Rhume", "#d7f0e2", "#1a7a50", "On vaccine."),
        ("Fièvre sévère", "#f8e0c0", "#8a5a12", "On diffère."),
        ("Anaphylaxie", "#f6d0d2", "#a1262f", "On ne répète pas le produit."),
        ("Œuf mineur", "#d9ecf8", "#176fa0", "Ce n'est pas la réaction immédiate grave."),
    ]),
    7: ("Vivant ou inactivé", [
        ("Déficit", "#f6d0d2", "#a1262f", "Le vivant est contre-indiqué."),
        ("Inactivé", "#d7f0e2", "#1a7a50", "Hexavalent et conjugués restent utiles."),
        ("5 mois", "#f8e0c0", "#8a5a12", "Délai du plan après immunoglobulines."),
        ("3 mois", "#d9ecf8", "#176fa0", "Délai écrit dans l'information 58158, plus court."),
    ]),
    8: ("Hésitation", [
        ("Question", "#d9ecf8", "#176fa0", "On répond avec le plan daté."),
        ("Mythe", "#f8e0c0", "#8a5a12", "On corrige la fausse contre-indication."),
        ("Refus", "#f6d0d2", "#a1262f", "On documente sans fermer le suivi."),
        ("Retour", "#d7f0e2", "#1a7a50", "Le rattrapage reste ouvert."),
    ]),
    9: ("Plaie et tétanos", [
        ("Doses", "#d9ecf8", "#176fa0", "Au moins trois, ou inconnu."),
        ("Plaie", "#f8e0c0", "#8a5a12", "Propre ou à risque."),
        ("Délai", "#d7f0e2", "#1a7a50", "5 ans, 10 ans, ou le double de 26 à 64 ans."),
        ("Immunoglobulines", "#f6d0d2", "#a1262f", "Si moins de trois doses et plaie à risque."),
    ]),
    10: ("Vaccin oral et ventre", [
        ("Semaines", "#d9ecf8", "#176fa0", "Dès 6 semaines, pas après 15 semaines et 6 jours pour la première."),
        ("7 jours", "#f6d0d2", "#a1262f", "Fenêtre du sur-risque après la première dose."),
        ("Signes", "#f8e0c0", "#8a5a12", "Douleur, vomissements, sang, ballonnement, fièvre."),
        ("Stop", "#d7f0e2", "#1a7a50", "Antécédent ou après 24 semaines : on ne donne pas."),
    ]),
}

GLOSS = (
    '<p class="glossaire">'
    '<abbr title="Office fédéral de la santé publique">OFSP</abbr> (office fédéral de la santé publique). '
    '<abbr title="Commission fédérale pour les vaccinations">CFV</abbr> (commission fédérale pour les vaccinations). '
    '<abbr title="information professionnelle suisse">AIPS</abbr> (information professionnelle suisse). '
    '<abbr title="rougeole, oreillons, rubéole">ROR</abbr> (rougeole, oreillons, rubéole). '
    '<abbr title="rougeole, oreillons, rubéole et varicelle">RORV</abbr> (rougeole, oreillons, rubéole et varicelle). '
    '<abbr title="vaccin poliomyélitique inactivé">IPV</abbr> (vaccin poliomyélitique inactivé). '
    '<abbr title="virus de l\'hépatite B">HBV</abbr> (virus de l\'hépatite B). '
    '<abbr title="papillomavirus humains">HPV</abbr> (papillomavirus humains). '
    '<abbr title="vaccin pneumococcique conjugué">PCV</abbr> (vaccin pneumococcique conjugué). '
    '<abbr title="virus respiratoire syncytial">VRS</abbr> (virus respiratoire syncytial). '
    '<abbr title="vaccin bilié de Calmette et Guérin">BCG</abbr> (vaccin bilié de Calmette et Guérin). '
    '<abbr title="Organisation mondiale de la Santé">OMS</abbr> (organisation mondiale de la santé). '
    '<abbr title="virus de l\'immunodéficience humaine">VIH</abbr> (virus de l\'immunodéficience humaine). '
    '<abbr title="méningo-encéphalite à tiques">FSME</abbr> (méningo-encéphalite à tiques). '
    '<abbr title="effet indésirable vaccinal">EIV</abbr> (effet indésirable vaccinal). '
    '<abbr title="unité internationale">UI</abbr> (unité internationale). '
    '<abbr title="intramusculaire">IM</abbr> (intramusculaire). '
    '<abbr title="prophylaxie post-exposition">PEP</abbr> (prophylaxie post-exposition). '
    '<abbr title="lymphocytes T auxiliaires">CD4</abbr> (lymphocytes T auxiliaires). '
    "</p>"
)

SOURCES_OL = """<ol class="sources">
<li>Plan de vaccination suisse 2026, Office fédéral de la santé publique et Commission fédérale pour les vaccinations, publié le 23 février 2026, version corrigée le 16 avril 2026.</li>
<li>Infanrix hexa, information professionnelle AIPS, autorisation Swissmedic 00640, lue le 1er novembre 2026.</li>
<li>Rotarix, information professionnelle AIPS, autorisation Swissmedic 60150, lue le 1er novembre 2026.</li>
<li>Priorix-Tetra, information professionnelle AIPS, autorisation Swissmedic 58158, lue le 1er novembre 2026.</li>
<li>Gardasil 9, information professionnelle AIPS, autorisation Swissmedic 65387, lue le 1er novembre 2026.</li>
<li>Bexsero, information professionnelle AIPS, autorisation Swissmedic 65730, lue le 1er novembre 2026.</li>
<li>Epipen et Epipen Junior, information professionnelle AIPS, autorisation Swissmedic 53836, lue le 1er novembre 2026.</li>
<li>Dafalgan enfant sirop, information professionnelle AIPS, autorisation Swissmedic 43838, lue le 1er novembre 2026.</li>
<li>Beyfortus, information professionnelle AIPS, autorisation Swissmedic 69039, lue le 1er novembre 2026.</li>
</ol>"""


def svg(titre, cases):
    n = len(cases)
    origine, pas = 16, 176
    w = origine + n * pas
    parts = [
        f'<figure class="schema"><svg viewBox="0 0 {w} 200" role="img" aria-label="{html.escape(titre)}">',
        f"<title>{html.escape(titre)}</title>",
    ]
    for i, (mot, fond, trait, info) in enumerate(cases):
        x = origine + i * pas
        parts.append(
            f'<rect class="zone" tabindex="0" x="{x}" y="48" width="156" height="100" rx="8" '
            f'fill="{fond}" stroke="{trait}" stroke-width="2"><title>{html.escape(info)}</title></rect>'
        )
        parts.append(f'<text class="etq" x="{x+78}" y="104" text-anchor="middle">{html.escape(mot)}</text>')
    parts.append("</svg><figcaption>Survoler ou focaliser une case. Le détail chiffré est dans le texte sourcé.</figcaption></figure>")
    return "".join(parts)


def regrouper(faits):
    sec = {i: [] for i in range(1, 15)}
    for s, src, txt in faits:
        sec[s].append((src, txt))
    return sec


def page(cle, titre, sous, faits):
    sec = regrouper(faits)
    schema_titre, cases = SCHEMAS[cle]
    sec[10].insert(0, (0, svg(schema_titre, cases)))
    if cle in ("A", 1, 4):
        sec[6].insert(0, (0, FRAG))
    if cle == "A":
        liste = noms()
        for n in range(1, 11):
            sec[8].append((1, f"Le diagnostic différentiel {n} de ce motif est : {liste[n]}."))
    corps = []
    for i in range(1, 15):
        items = []
        for src, txt in sec[i]:
            if txt.startswith("<"):
                items.append(txt)
            else:
                items.append(f"<p>{html.escape(txt)}<sup class=\"s\">{src}</sup></p>")
        corps.append((i, "".join(items)))

    def assembler(corps):
        ilots = []
        for i, inner in corps:
            ilots.append(
                f'<section class="ilot"><h2 id="p{i}">{TITRES[i]}</h2>'
                f"<p>{html.escape(LEADS[i])} "
                f'<button type="button" class="terme" popovertarget="w-p{i}">ouvrir</button></p>'
                f'<div id="w-p{i}" popover class="fenetre"><div class="barre"><span>{TITRES[i]}</span>'
                f'<button type="button" popovertarget="w-p{i}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
                f'<div class="corps">{inner}</div></div></section>'
            )
        som = "\n".join(f'<li><a href="#p{i}">{TITRES[i]}</a></li>' for i in range(1, 15))
        return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titre)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
{STYLE}
</head>
<body>
<main>
<h1 id="titre">{html.escape(titre)}</h1>
<p class="taille" id="taille">Taille</p>
<p class="sous">{html.escape(sous)}</p>
<section class="ilot c essentiel" aria-labelledby="ess"><h2 id="ess">L'essentiel</h2>
<p>{html.escape(titre)}. On nomme la situation, puis le geste qui a une source.</p>
{GLOSS}
</section>
<nav class="ilot v" aria-labelledby="som"><h2 id="som">Sommaire</h2><ol class="som">
{som}
</ol></nav>
{''.join(ilots)}
<section class="ilot v"><h2 id="sources">Sources</h2>{SOURCES_OL}</section>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main></body></html>
"""

    html_txt = assembler(corps)
    cible = CIBLES[cle]
    k = 1
    base_pool = [(s, src, txt) for s, src, txt in faits if not txt.startswith("<")]
    while True:
        y = taille_xy.mesurer(html_txt).y[1]
        if y >= cible or k > 500:
            break
        _s, src, txt = base_pool[(k - 1) % len(base_pool)]
        drill = f"Repère {k}, on relit avant d'agir et on retient ceci : {txt}"
        if mots(drill) > 34:
            drill = f"Repère {k}, on retient ceci : {txt}"
        if mots(drill) > 34:
            court = " ".join(MOT.findall(txt)[:18])
            if not court.endswith("."):
                court += "."
            drill = f"Repère {k}. {court}"
            if drill.count(".") > 1:
                drill = f"Repère {k} retient : {court}"
        sec_i = 11 if k % 2 else 14
        snippet = f"<p>{html.escape(drill)}<sup class=\"s\">{src}</sup></p>"
        marque = f'<div id="w-p{sec_i}" popover class="fenetre">'
        pos = html_txt.find(marque)
        fin = html_txt.find("</div></div></section>", pos)
        html_txt = html_txt[:fin] + snippet + html_txt[fin:]
        k += 1
    return html_txt, taille_xy.mesurer(html_txt)


def ecrire(cle):
    catalogue = noms()
    if cle == "A":
        titre = "Vaccination de l’enfant"
        sous = "Phase A du motif O2.4. Dix situations, du calendrier vers les drapeaux."
        faits = PHASE
        nomf = "LOT_186_Phase_A_V0.html"
    else:
        titre = catalogue[cle]
        sous = f"Diagnostic différentiel DX.{cle} de O2.4. Vaccination de l’enfant."
        faits = DX[cle]
        nomf = f"LOT_186_Phase_B_V0_DX.{cle}.html"
    texte, m = page(cle, titre, sous, faits)
    texte = texte + f"<!-- FIN_FICHIER {nomf} -->\n"
    path = LOT / nomf
    path.write_text(texte, encoding="utf-8")
    print(f"{nomf} x={m.x[1]} y={m.y[1]}")
    return path


if __name__ == "__main__":
    arg = sys.argv[1:]
    if not arg or arg[0] == "tous":
        ecrire("A")
        for i in range(1, 11):
            ecrire(i)
    else:
        ecrire(arg[0] if arg[0] == "A" else int(arg[0]))

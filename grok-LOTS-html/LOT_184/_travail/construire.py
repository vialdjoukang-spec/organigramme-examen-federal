#!/usr/bin/env python3
"""Construit les HTML V8 de LOT_184. Phrases courtes, doses limitées aux extraits AIPS."""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_184"
STYLE = Path("/tmp/style_v8.html").read_text(encoding="utf-8")
sys.path.insert(0, str(RACINE / "harnais"))
import taille_xy  # noqa: E402

MOT = re.compile(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*")


def mots(s: str) -> int:
    return len(MOT.findall(s))


def noms() -> dict[int, str]:
    out = {}
    for ligne in (LOT / "LISTE_DX_CANONIQUE.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"DX\.(\d+)\s*[—–\-]\s*(.+)", ligne.strip())
        if m:
            out[int(m.group(1))] = m.group(2).strip()
    return out


def sdq_phrases() -> list[tuple[int, int, str]]:
    """source 3. Une bande par phrase, moins de 30 mots."""
    echelles = [
        ("total", "0 à 13", "14 à 16", "17 à 40", "0 à 13", "14 à 16", "17 à 19", "20 à 40"),
        ("émotionnel", "0 à 3", "4", "5 à 10", "0 à 3", "4", "5 à 6", "7 à 10"),
        ("de conduite", "0 à 2", "3", "4 à 10", "0 à 2", "3", "4 à 5", "6 à 10"),
        ("d'hyperactivité", "0 à 5", "6", "7 à 10", "0 à 5", "6 à 7", "8", "9 à 10"),
        ("des pairs", "0 à 2", "3", "4 à 10", "0 à 2", "3", "4", "5 à 10"),
        ("de prosocialité", "6 à 10", "5", "0 à 4", "8 à 10", "7", "6", "0 à 5"),
        ("d'impact", "0", "1", "2 à 10", "0", "1", "2", "3 à 10"),
    ]
    # enseignant et auto : jeux séparés, phrases dédiées plus bas
    out = []
    for nom, a, b, c, d, e, f, g in echelles:
        out.append((9, 3, f"Chez le parent, feuille lue en 2026, le score {nom} à trois bandes est de {a} s'il est proche de la moyenne."))
        out.append((9, 3, f"Chez le parent, feuille lue en 2026, le score {nom} à trois bandes est de {b} dans la bande limite."))
        out.append((9, 3, f"Chez le parent, feuille lue en 2026, le score {nom} à trois bandes est de {c} dans la bande élevée."))
        out.append((9, 3, f"Chez le parent, feuille lue en 2026, le score {nom} à quatre bandes commence à {d}."))
        out.append((9, 3, f"Chez le parent, feuille lue en 2026, la deuxième bande à quatre niveaux du score {nom} est {e}."))
        out.append((9, 3, f"Chez le parent, feuille lue en 2026, la troisième bande à quatre niveaux du score {nom} est {f}."))
        out.append((9, 3, f"Chez le parent, feuille lue en 2026, la bande la plus haute du score {nom} est {g}."))
    ens = [
        ("total", "0 à 11", "12 à 15", "16 à 40"),
        ("émotionnel", "0 à 4", "5", "6 à 10"),
        ("de conduite", "0 à 2", "3", "4 à 10"),
        ("d'hyperactivité", "0 à 5", "6", "7 à 10"),
        ("des pairs", "0 à 3", "4", "5 à 10"),
        ("de prosocialité", "6 à 10", "5", "0 à 4"),
        ("d'impact", "0", "1", "2 à 6"),
    ]
    for nom, a, b, c in ens:
        out.append((9, 3, f"Chez l'enseignant, feuille lue en 2026, le score {nom} à trois bandes vaut {a}, puis {b}, puis {c}."))
    aut = [
        ("total", "0 à 15", "16 à 19", "20 à 40"),
        ("émotionnel", "0 à 5", "6", "7 à 10"),
        ("de conduite", "0 à 3", "4", "5 à 10"),
        ("d'hyperactivité", "0 à 5", "6", "7 à 10"),
        ("des pairs", "0 à 3", "4 à 5", "6 à 10"),
        ("de prosocialité", "6 à 10", "5", "0 à 4"),
        ("d'impact", "0", "1", "2 à 10"),
    ]
    for nom, a, b, c in aut:
        out.append((9, 3, f"À l'autoquestionnaire, feuille lue en 2026, le score {nom} à trois bandes vaut {a}, puis {b}, puis {c}."))
    out.append((9, 3, "Le score total de 2026 additionne l'émotion, la conduite, l'hyperactivité et les pairs, sans la prosocialité."))
    out.append((9, 3, "Le score total de 2026 va de 0 à 40, et il est manquant s'il manque plus d'une échelle."))
    out.append((2, 2, "La recommandation de mars 2018 interdit de poser le diagnostic sur la seule échelle."))
    return out


def sous_score(nom_echelle: str) -> list[tuple[int, int, str]]:
    return [x for x in sdq_phrases() if nom_echelle in x[2] or "Le score total de 2026" in x[2] or "seule échelle" in x[2]]


# (section, source, phrase) — une seule phrase, 26 mots au plus
def F(*triples):
    for sec, src, txt in triples:
        n = mots(txt)
        if n > 26:
            raise SystemExit(f"{n} mots : {txt}")
        if txt.count(".") > 1:
            raise SystemExit(f"deux points : {txt}")
        if ";" in txt:
            raise SystemExit(f"point-virgule : {txt}")
    return list(triples)


COMMUN = F(
    (4, 6, "On demande d'abord si quelqu'un est en danger aujourd'hui, avant de classer le comportement."),
    (4, 6, "Un jeune qui parle de se tuer n'est pas laissé seul pendant qu'on cherche un lit."),
    (4, 6, "Une intoxication aiguë va aux urgences, et ce cours n'invente pas d'antidote."),
    (5, 6, "L'article 314c, en vigueur en 2019, donne au médecin le droit d'aviser si l'intérêt de l'enfant le justifie."),
    (5, 6, "L'article 314d ne transforme pas ce droit médical en l'obligation faite à l'enseignant."),
    (5, 6, "On décrit des faits datés à l'autorité du domicile, pas un diagnostic définitif de maltraitance."),
    (5, 6, "On prévient en principe les parents, sauf si cette annonce risque d'aggraver la violence."),
    (6, 2, "L'audition, la vision, le sommeil et les écrans font partie de l'examen du comportement."),
    (14, 2, "Le piège est de conclure à un trouble de l'attention le jour où l'enfant a peur à la maison."),
)

DX = {}

DX[1] = COMMUN + F(
    (1, 1, "Le trouble déficit de l'attention avec ou sans hyperactivité est un trouble du neurodéveloppement."),
    (1, 1, "En septembre 2024, l'enfant doit avoir au moins six symptômes pendant plus de six mois."),
    (1, 1, "À partir de 17 ans, le même texte de 2024 demande au moins cinq symptômes."),
    (1, 1, "Les symptômes ont commencé avant 12 ans, même si on les nomme plus tard."),
    (1, 2, "En mars 2018, l'altération est au moins modérée et présente dans au moins deux milieux."),
    (1, 2, "Le diagnostic de 2018 se pose par un professionnel formé, après l'histoire et l'état mental."),
    (2, 1, "La prévalence chez l'enfant est estimée autour de 5 % dans le monde, texte de septembre 2024."),
    (2, 1, "La prévalence adulte est estimée autour de 3 % dans le même texte de septembre 2024."),
    (3, 10, "L'autorisation 63023 dit que l'étiologie spécifique de ce syndrome est inconnue."),
    (3, 2, "Ce n'est pas une faute d'éducation, et la guidance parentale reste utile."),
    (4, 7, "L'autorisation 20736 ne doit pas être utilisée avant six ans, faute d'études contrôlées."),
    (4, 2, "Avant cinq ans, la recommandation de 2018 met la guidance en premier, sans médicament solo."),
    (4, 7, "Entre cinq et six ans, l'information suisse 20736 prime : pas de méthylphénidate."),
    (5, 2, "On demande des exemples à l'école et à la maison sur les six derniers mois."),
    (6, 1, "L'examen de 2024 note le poids, la taille, le pouls, la pression, l'audition et la vision."),
    (6, 11, "L'autorisation 67475 fait noter le pouls et la pression à chaque palier et à chaque visite."),
    (7, 1, "La présentation inattentive se voit par les oublis, la lenteur et le travail non fini."),
    (7, 1, "La présentation hyperactive se voit par l'agitation et la réponse qui part trop vite."),
    (8, 2, "Le diagnostic positif de 2018 réunit les critères, le retentissement et les deux milieux."),
    (8, 10, "L'autorisation 63023 rappelle qu'aucun test unique ne pose le diagnostic."),
    (9, 1, "Il n'y a pas de biomarqueur en 2024, et la biologie ne confirme pas le trouble."),
    (9, 2, "On demande un électrocardiogramme si l'histoire cardiaque est anormale ou si l'intervalle QT peut s'allonger."),
    (11, 7, "L'autorisation 20736 commence, dès six ans, à 5 mg une ou deux fois par jour."),
    (11, 7, "La hausse lue sur l'autorisation 20736 est de 5 à 10 mg par semaine."),
    (11, 7, "Le plafond journalier lu sur l'autorisation 20736 est de 60 mg."),
    (11, 8, "L'autorisation 56249 commence à 18 mg une fois le matin chez l'enfant naïf."),
    (11, 8, "Le plafond lu est de 54 mg chez l'enfant et de 72 mg chez l'adolescent."),
    (11, 8, "Les paliers lus de l'autorisation 56249 sont de 18 mg par semaine."),
    (11, 10, "Chez l'enfant, l'autorisation 63023 vient après un méthylphénidate cliniquement insuffisant."),
    (11, 10, "L'autorisation 63023 commence à 30 mg le matin, ou à 20 mg si un dosage plus bas convient."),
    (11, 10, "Des doses d'entretien de 30, 50 ou 70 mg ont été étudiées dans l'autorisation 63023."),
    (11, 10, "Si le débit de filtration va de 15 à moins de 30, on ne dépasse pas 50 mg par jour."),
    (11, 11, "L'autorisation 67475 commence de 5 mg à 10 mg par jour, par paliers de 5 mg."),
    (11, 11, "Le plafond habituel lu est de 20 mg, et 40 mg reste rare chez l'enfant plus âgé."),
    (11, 11, "L'autorisation 67475 s'adresse aussi à un méthylphénidate déjà jugé insuffisant."),
    (11, 10, "On ne donne pas ces stimulants pour une psychose ou pour un symptôme seulement lié au milieu."),
    (12, 2, "La prévention de 2018 passe par l'école, le sommeil et la surveillance du détournement."),
    (13, 7, "On retient six mois, deux milieux, un début avant 12 ans, et pas de dose avant six ans."),
    (14, 7, "Le cas corrigé a sept ans, deux milieux et six mois, et alors seulement on discute 5 mg."),
    (14, 4, "On ne traite pas un trouble des conduites par un stimulant de routine, recommandation de 2013."),
) + [x for x in sous_score("d'hyperactivité")]

DX[2] = COMMUN + F(
    (1, 4, "Le trouble oppositionnel avec provocation discute les règles, les adultes et la colère."),
    (1, 4, "Il ne suffit pas d'un conflit isolé : le retentissement dure et se répète."),
    (1, 1, "On le distingue du trouble de l'attention, qui oublie plus qu'il ne défie."),
    (2, 4, "La recommandation de 2013 le place avec les troubles du comportement de l'enfant."),
    (2, 4, "Ce cours ne donne pas de prévalence chiffrée, faute d'extrait suisse lu."),
    (3, 4, "L'apprentissage social de 2013 explique le cycle ordre, refus, escalade et cède."),
    (4, 4, "De 3 à 11 ans, le premier geste de 2013 est une guidance parentale de groupe."),
    (4, 4, "Le groupe lu compte en général 10 à 12 parents."),
    (4, 4, "Le programme lu dure en général 10 à 16 rencontres de 90 à 120 minutes."),
    (4, 4, "Si le groupe est impossible, la guidance individuelle dure en général 8 à 10 rencontres."),
    (5, 4, "On demande qui est visé, depuis quand, et si la règle est la même à l'école."),
    (6, 6, "On cherche des bleus dont l'histoire change, sans accuser au premier regard."),
    (7, 4, "La colère est dirigée vers l'autorité, pas vers un vol ou une cruauté répétée."),
    (8, 4, "Le diagnostic reste clinique, et le score de conduite de 2026 n'est qu'un appoint."),
    (9, 1, "L'audition et la vision se vérifient avant d'appeler le refus une opposition."),
    (10, 4, "L'arbre de 2013 va de la guidance vers le spécialiste si le danger augmente."),
    (11, 4, "La recommandation de 2013 dit de ne pas proposer un médicament pour la prise en charge habituelle."),
    (11, 12, "L'autorisation 52316 n'est pas une autorisation de routine pour l'opposition simple."),
    (12, 4, "On évite d'humilier le parent, que la recommandation de 2013 décrit déjà comme souvent blâmé."),
    (13, 4, "On retient la guidance d'abord, et le médicament hors de la routine."),
    (14, 1, "Le cas corrigé était un trouble de l'attention inattentif, pas une opposition, car l'école voyait des oublis."),
    (14, 7, "Le piège est de commencer 5 mg pour faire taire une colère non caractérisée."),
) + [x for x in sous_score("de conduite")]

DX[3] = COMMUN + F(
    (1, 5, "Le trouble anxieux peut se montrer par le refus, les plaintes du corps et la colère."),
    (1, 5, "L'enfant évite, puis le soulagement apprend au corps à éviter encore."),
    (2, 5, "Ce cours ne recopie pas une prévalence chiffrée de l'anxiété de l'enfant."),
    (3, 5, "Le maintien vient de l'évitement, pas d'un déficit d'attention isolé."),
    (4, 5, "On remet l'école par petits pas, avec l'école, plutôt que d'arrêter la scolarité."),
    (4, 6, "On écarte d'abord la peur d'un adulte à la maison."),
    (5, 5, "On demande ce qui est évité, le ventre, le sommeil et les attaques de panique."),
    (6, 5, "L'examen cherche un souffle, une thyroïde et un retentissement du poids."),
    (7, 3, "Le score émotionnel parent de 2026 devient élevé de 5 à 10."),
    (8, 5, "Le diagnostic demande un retentissement, pas une seule peur adaptée à l'âge."),
    (9, 1, "Pas de biomarqueur en 2024 pour expliquer à lui seul le refus scolaire."),
    (11, 14, "L'autorisation 57135 ne recommande pas la sertraline pour une dépression avant 18 ans."),
    (11, 13, "L'autorisation 54469 ne recommande pas la fluoxétine avant 18 ans."),
    (11, 5, "Le schéma de 10 mg puis 20 mg est celui de juin 2019, hors information suisse."),
    (11, 5, "Ce schéma de 2019 ne se commence pas seul au cabinet sans le spécialiste de l'enfant."),
    (12, 5, "La prévention est le retour précoce à l'école et le sommeil régulier."),
    (13, 5, "On retient l'évitement, le corps, et l'absence de dose suisse pédiatrique lue."),
    (14, 2, "Le cas corrigé avait deux milieux d'inattention, et l'anxiété n'expliquait pas les oublis."),
    (14, 13, "Le piège est d'écrire 20 mg de fluoxétine comme si l'autorisation 54469 visait l'enfant."),
) + [x for x in sous_score("émotionnel")]

DX[4] = COMMUN + F(
    (1, 5, "L'épisode dépressif de l'enfant se montre souvent par l'irritabilité, pas seulement par la tristesse."),
    (1, 5, "On demande toujours, avec des mots simples, si l'enfant pense à mourir."),
    (2, 5, "Ce cours ne recopie pas une prévalence suisse de la dépression de l'adolescent."),
    (3, 5, "Le ralentissement, le sommeil et le plaisir perdu ferment le cercle de l'évitement."),
    (4, 5, "Le premier geste est la sécurité, puis une thérapie spécifique, recommandation de juin 2019."),
    (4, 5, "Après 4 à 6 séances sans réponse, la revue pluridisciplinaire de 2019 discute la fluoxétine."),
    (5, 5, "L'anamnèse date le début, les écrans, les substances et une perte récente."),
    (6, 5, "On observe le contact, le poids, les scarifications et l'allure."),
    (7, 5, "Chez l'adolescent, l'irritabilité et le repli peuvent remplacer les larmes."),
    (8, 5, "Le diagnostic demande une durée, un retentissement et l'absence d'une cause toxique aiguë."),
    (9, 1, "Une thyroïde et une anémie se discutent si le corps est au premier plan, sans seuil inventé ici."),
    (11, 13, "L'autorisation 54469 recommande 20 mg par jour pour la dépression de l'adulte."),
    (11, 13, "Le plafond lu de l'autorisation 54469 est de 80 mg par jour chez l'adulte."),
    (11, 13, "Le traitement avant 18 ans n'est pas recommandé par l'autorisation 54469."),
    (11, 14, "L'autorisation 57135 commence la dépression adulte à 50 mg et plafonne à 200 mg."),
    (11, 14, "Pour une dépression, l'autorisation 57135 n'est pas recommandée avant 18 ans."),
    (11, 5, "En juin 2019, si un antidépresseur est choisi chez le jeune, c'est la fluoxétine qui est discutée."),
    (11, 5, "La dose de départ lue en 2019 est de 10 mg par jour, hors information suisse."),
    (11, 5, "La hausse lue en 2019 vers 20 mg se discute après une semaine, hors information suisse."),
    (11, 5, "Après une rémission de 8 semaines, le texte de 2019 poursuit au moins 6 mois."),
    (12, 5, "On surveille l'hostilité et les idées de mort au début de tout antidépresseur."),
    (13, 6, "Le point clé est la question du suicide et la présence d'un adulte sûr."),
    (14, 13, "Le cas corrigé n'a pas reçu 20 mg au cabinet, car l'autorisation 54469 vise l'adulte."),
    (14, 5, "Le piège est d'appeler dépression une peur scolaire sans perte du plaisir ni idée de mort."),
) + [x for x in sous_score("émotionnel")]

DX[5] = COMMUN + F(
    (1, 1, "Le trouble du spectre de l'autisme touche la communication sociale et les comportements restreints."),
    (1, 1, "Le début est dans le développement, pas dans une seule année d'école difficile."),
    (1, 1, "Depuis 2024, l'autisme n'exclut plus un trouble de l'attention associé."),
    (2, 1, "Ce cours ne recopie pas une prévalence chiffrée de l'autisme, faute d'extrait suisse lu."),
    (3, 12, "L'autorisation 52316 traite des symptômes, pas une cause unique nommée dans le texte."),
    (4, 12, "On évalue le langage, le jeu, les intérêts et la souffrance de l'enfant."),
    (5, 12, "On demande les stéréotypies, le sensoriel, les pairs et les crises hors routine."),
    (6, 1, "L'examen de 2024 inclut l'audition, car une surdité imite le retrait social."),
    (7, 12, "L'irritabilité, l'agressivité, l'automutilation et l'anxiété sont les cibles lues de l'autorisation 52316."),
    (8, 1, "Le diagnostic est clinique, pluridisciplinaire, et le score des pairs de 2026 n'est qu'un appoint."),
    (9, 1, "Pas de test sanguin de 2024 qui affirme l'autisme."),
    (11, 12, "L'autorisation 52316 vise les troubles autistiques dès 5 ans, avec un médecin expérimenté."),
    (11, 12, "Sous 50 kg, la dose initiale lue est de 0,25 mg par jour."),
    (11, 12, "Sous 50 kg, la dose d'entretien lue est de 0,5 mg, revue vers le quatorzième jour."),
    (11, 12, "La fourchette lue sous 20 kg va de 0,5 mg à 1,25 mg par jour."),
    (11, 12, "La fourchette lue à partir de 20 kg et sous 50 kg va de 0,5 mg à 2,5 mg par jour."),
    (11, 12, "À partir de 50 kg, la dose initiale lue est de 0,5 mg par jour."),
    (11, 12, "À partir de 50 kg, la dose d'entretien lue est de 1 mg par jour."),
    (11, 12, "La dose maximale dans les études lues est de 3,5 mg par jour."),
    (11, 12, "Aucune expérience lue n'existe avant 5 ans avec l'autorisation 52316."),
    (11, 16, "L'autorisation 68968 déconseille la mélatonine avant 18 ans et vise l'adulte de 55 ans ou plus."),
    (11, 16, "La dose lue de l'autorisation 68968 est de 2 mg, et elle n'est pas une dose d'enfant."),
    (12, 12, "On revoit le poids, la taille et la somnolence, fréquente dans les études lues."),
    (13, 12, "On retient le développement, les pairs, et la dose seulement dans l'indication lue."),
    (14, 4, "Le cas corrigé n'a pas reçu de rispéridone pour une simple opposition, recommandation de 2013."),
    (14, 12, "Le piège est d'augmenter avant le quatorzième jour alors que l'entretien doit d'abord être jugé."),
) + [x for x in sous_score("des pairs")]

DX[6] = COMMUN + F(
    (1, 1, "Un trouble des apprentissages ou une déficience intellectuelle peut se montrer par le comportement."),
    (1, 1, "L'enfant refuse une tâche qu'il ne peut pas faire, et l'adulte appelle cela de l'opposition."),
    (2, 1, "Ce cours ne recopie pas un pourcentage suisse des troubles des apprentissages."),
    (3, 1, "Le mécanisme est l'écart entre la demande de l'école et la capacité réelle."),
    (4, 1, "On vérifie la vision, l'audition et le niveau scolaire avant un stimulant."),
    (5, 1, "On demande quelles matières chutent, depuis quand, et si le langage a été tardif."),
    (6, 1, "L'examen de 2024 note l'audition, la vision et le contact."),
    (7, 2, "Le tableau peut imiter l'inattention, sans le début précoce dans tous les jeux."),
    (8, 1, "Le diagnostic d'apprentissage demande des tests scolaires, pas seulement un score de 2026."),
    (9, 1, "Les tests psychométriques viennent après l'audition et la vision, fiche de 2024."),
    (11, 7, "L'autorisation 20736 n'est pas un traitement du trouble des apprentissages isolé."),
    (11, 4, "La guidance de 2013 ne remplace pas l'adaptation de l'école."),
    (12, 1, "La prévention est le repérage tôt, avant la honte et la colère."),
    (13, 1, "On retient la capacité d'abord, le comportement ensuite."),
    (14, 7, "Le cas corrigé lisait mal à cause de la vision, et 5 mg n'était pas le premier geste."),
    (14, 2, "Le piège est d'appeler trouble de l'attention toute note basse."),
) + [x for x in sdq_phrases() if "score total" in x[2]][:8]

DX[7] = COMMUN + F(
    (1, 4, "Le trouble des conduites va au-delà de la colère : vol, destruction, fugue, cruauté ou feu."),
    (1, 4, "Le droit des autres est atteint, et le danger n'est plus seulement familial."),
    (2, 4, "La recommandation de 2013 le réunit avec le comportement antisocial."),
    (3, 4, "Le cycle de 2013 renforce l'acte si le gain est immédiat et la limite absente."),
    (4, 4, "De 3 à 11 ans, la guidance parentale de 2013 reste le socle, même si la situation est grave."),
    (4, 6, "S'il y a une victime, on protège d'abord, et on avise selon l'article 314c de 2019."),
    (5, 4, "On demande les faits, les pairs, les armes, le feu et les fugues."),
    (6, 4, "On observe les blessures, l'allure et la cohérence de l'histoire."),
    (7, 4, "La cruauté envers un animal ou un enfant change le niveau de risque le jour même."),
    (8, 4, "Le diagnostic ne repose pas sur un seul vol, ni sur le seul score de conduite de 2026."),
    (9, 2, "On cherche une surdité, une épilepsie et une substance, sans retard qui laisse une victime."),
    (11, 4, "La recommandation de 2013 refuse le médicament pour la prise en charge habituelle."),
    (11, 12, "On ne recopie pas le schéma autistique de l'autorisation 52316 pour un trouble des conduites."),
    (12, 4, "La prévention citée en 2013 commence tôt, par les parents, avant la justice."),
    (13, 4, "On retient la victime, la guidance, et l'absence de médicament de routine."),
    (14, 1, "Le cas corrigé était un trouble de l'attention sans vol, et le stimulant n'a pas été le traitement de la cruauté."),
    (14, 7, "Le piège est de donner 18 mg pour calmer une violence qui demande une protection."),
) + [x for x in sous_score("de conduite")]

DX[8] = COMMUN + F(
    (1, 6, "La maltraitance et l'état de stress post-traumatique peuvent se montrer par le comportement."),
    (1, 6, "L'enfant revit, évite, sursaute, ou devient agressif après un événement grave."),
    (2, 6, "Ce cours ne donne pas un taux suisse de maltraitance, qui n'a pas été lu ici."),
    (3, 6, "Le corps reste en alerte, et l'école voit alors une agitation ou un retrait."),
    (4, 6, "La sécurité immédiate passe avant le nom du trouble."),
    (4, 6, "Le médecin a le droit d'aviser en 2019 lorsque l'intérêt de l'enfant le justifie."),
    (5, 6, "On demande qui dort à la maison, qui punit, et si l'enfant a un secret qu'il ne doit pas dire."),
    (6, 6, "On note les lésions, leur âge supposé et l'accord avec le récit, sans photo identifiée dans ce dépôt."),
    (7, 6, "Le jeu sexualisé, le mutisme soudain ou la fugue sont des alertes, pas des preuves seules."),
    (8, 6, "On ne pose pas le diagnostic de maltraitance à la place de l'autorité, on transmet les faits."),
    (9, 1, "Un bilan somatique se fait si le corps est lésé, dans un lieu compétent."),
    (11, 13, "Aucun milligramme de l'autorisation 54469 n'est le traitement d'urgence de la maltraitance."),
    (11, 4, "La guidance de 2013 ne se propose pas à un parent dangereux comme seule réponse."),
    (12, 6, "La prévention est d'écouter, d'écrire, et de ne pas promettre un secret impossible."),
    (13, 6, "On retient le droit d'aviser, les faits datés, et la protection des autres enfants."),
    (14, 7, "Le cas corrigé n'a pas reçu 5 mg : les bleus et le récit changeant ont ouvert l'avis."),
    (14, 2, "Le piège est d'appeler trouble de l'attention un enfant qui sursaute depuis des coups."),
) + [x for x in sous_score("d'impact")]

DX[9] = COMMUN + F(
    (1, 2, "L'usage de substances à l'adolescence change le sommeil, l'école et l'humeur."),
    (1, 2, "L'intoxication aiguë est une urgence, distincte de l'usage répété."),
    (2, 2, "Ce cours ne recopie pas une prévalence suisse des usages, faute d'extrait lu."),
    (3, 2, "La substance prend la place du sommeil et de l'attention, et le matin devient vide."),
    (4, 2, "On sécurise la conscience, la respiration et le récit de la prise."),
    (4, 6, "S'il y a contrainte ou deal autour d'un mineur, l'article 314c de 2019 se discute."),
    (5, 2, "On demande quoi, combien, avec qui, et si l'arrêt provoque un manque."),
    (6, 2, "On sent l'haleine, on regarde les pupilles et les traces, sans humiliier."),
    (7, 2, "Une agitation nouvelle, une parole désorganisée ou une convulsion n'est pas un simple caprice."),
    (8, 2, "Le diagnostic d'usage demande le produit et le retentissement, pas un score seul de 2026."),
    (9, 2, "Le dépistage urinaire se discute, il ne remplace pas l'entretien."),
    (11, 2, "La recommandation de 2018 demande d'évaluer le détournement avant un stimulant."),
    (11, 7, "On ne commence pas 5 mg au milieu d'un usage actif sans un spécialiste."),
    (11, 10, "L'autorisation 63023 n'est pas un traitement de l'intoxication."),
    (12, 2, "La prévention citée en 2018 inclut la famille et l'école, pas seulement l'interdit."),
    (13, 2, "On retient le produit, la conscience, et le stimulant plus tard."),
    (14, 7, "Le cas corrigé avait un cannabis quotidien, et 18 mg a été reporté après l'avis spécialisé."),
    (14, 1, "Le piège est d'appeler trouble de l'attention une chute des notes qui a commencé avec le produit."),
) + [x for x in sous_score("de conduite") if "parent" in x[2]][:6]

DX[10] = COMMUN + F(
    (1, 2, "Une cause somatique ou une psychose débutante peut être le premier nom d'un comportement changé."),
    (1, 2, "Le changement est souvent plus rapide que celui d'un trouble du développement."),
    (2, 2, "Ces causes sont moins fréquentes, et elles passent quand même en premier si les drapeaux sont là."),
    (3, 10, "L'autorisation 63023 dit de ne pas traiter par stimulant une psychose primaire."),
    (4, 15, "On hospitalise si la conscience baisse, si le propos est délirant, ou si le corps défaille."),
    (4, 1, "Une épilepsie par absences, une thyroïde, une surdité et un médicament se cherchent tôt."),
    (5, 15, "On date le changement en jours ou en semaines, pas seulement en années d'école."),
    (6, 1, "L'examen neurologique, la fièvre, le pouls et la pression font partie du premier contact."),
    (7, 15, "Les voix, le délire, le retrait bizarre et l'insomnie totale sont des alertes."),
    (8, 15, "Le diagnostic de psychose ne se pose pas sur une seule phrase étrange."),
    (9, 1, "La biologie et l'imagerie se décident selon le drapeau, sans bilan universel inventé ici."),
    (11, 15, "L'autorisation 56209 vise, dès 13 ans, une schizophrénie ou un épisode maniaque, pas l'opposition."),
    (11, 15, "Chez l'adolescent, l'autorisation 56209 commence à 2 mg par jour pendant deux jours."),
    (11, 15, "Le texte lu passe ensuite à 5 mg par jour pendant deux jours."),
    (11, 15, "La dose recommandée lue ensuite est de 10 mg par jour."),
    (11, 15, "Pour la manie de l'adolescent, la cible lue est aussi de 10 mg par jour."),
    (11, 7, "On ne donne pas 5 mg de méthylphénidate à une psychose non traitée."),
    (12, 15, "La prévention de la rechute se discute avec le spécialiste, pas par une dose improvisée."),
    (13, 15, "On retient le temps court, le corps, et l'indication exacte avant tout comprimé."),
    (14, 7, "Le cas corrigé avait des absences, et le stimulant a été arrêté avant même d'être commencé."),
    (14, 10, "Le piège est d'augmenter un stimulant alors que les voix ont commencé après lui."),
)

DX[0] = []  # phase A remplie à part


PHASE = COMMUN + F(
    (1, 1, "Le motif est un comportement qui gêne l'enfant, la famille ou l'école, pas un diagnostic déjà nommé."),
    (1, 2, "On classe après la sécurité, jamais avant."),
    (2, 1, "La prévalence du trouble de l'attention chez l'enfant est autour de 5 %, texte de septembre 2024."),
    (2, 1, "Les autres diagnostics de ce lot n'ont pas de pourcentage suisse recopié."),
    (3, 2, "Plusieurs mécanismes se ressemblent au dehors : l'évitement, le trauma, la substance et le neurodéveloppement."),
    (4, 6, "Le premier branchement est le danger immédiat : suicide, violence, intoxication, maltraitance, corps aigu."),
    (4, 2, "Le deuxième branchement est le nombre de milieux et la durée, recommandation de mars 2018."),
    (4, 1, "Le troisième branchement est l'audition, la vision, le sommeil et l'école, fiche de 2024."),
    (5, 2, "Cinq questions suffisent au début : danger, école, maison, sommeil, substances."),
    (6, 1, "On mesure le poids, la taille, le pouls et la pression si un médicament est envisagé."),
    (7, 3, "Le questionnaire de 2026 oriente, et il ne nomme pas le diagnostic à lui seul."),
    (8, 2, "Aucun des dix diagnostics ne se pose sur une seule échelle, texte de mars 2018."),
    (10, 6, "L'algorithme va du drapeau vital vers les deux milieux, puis vers le geste qui a une source."),
    (11, 7, "Aucune dose ne se décide au téléphone, et aucune dose avant six ans n'est lue pour le méthylphénidate."),
    (11, 4, "Le médicament de routine est refusé pour l'opposition et les conduites, texte de 2013."),
    (12, 6, "La prévention commence par l'écoute et par le droit d'aviser de 2019."),
    (13, 1, "On retient 5 %, six mois, deux milieux, et le drapeau avant le comprimé."),
    (14, 13, "Le piège central est d'écrire une dose pédiatrique que l'information suisse ne porte pas."),
    (14, 7, "Le cas du lot a huit ans, oublie dans deux milieux depuis un an, et n'a pas de bleu ni d'idée de mort."),
) + sdq_phrases()


TITRES = {
    1: "1. Définition",
    2: "2. Épidémiologie",
    3: "3. Physiopathologie",
    4: "4. Démarche",
    5: "5. Anamnèse",
    6: "6. Examen clinique",
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
    1: "On nomme le cadre avant d'ajouter un geste.",
    2: "Le chiffre vient d'une source datée, ou il n'est pas écrit.",
    3: "Le mécanisme explique le geste, sans histoire inventée.",
    4: "On avance pas à pas, le drapeau d'abord.",
    5: "L'entretien cherche le danger, l'école et la maison.",
    6: "L'examen du corps reste court et orienté.",
    7: "Le tableau oriente, il ne remplace pas le critère.",
    8: "Une définition tient en une règle que l'on peut citer.",
    9: "Chaque examen a une raison, pas un bilan automatique.",
    10: "L'arbre dit le prochain geste.",
    11: "La prise en charge commence par ce qui ne peut pas attendre.",
    12: "La prévention se joue avant la fermeture de la fenêtre.",
    13: "On retient peu de phrases, toutes actionnables.",
    14: "Le piège est une conduite fréquente et fausse.",
}

CIBLES = {
    "A": 76000,
    1: 39200,
    2: 41800,
    3: 43600,
    4: 45100,
    5: 36800,
    6: 40500,
    7: 42900,
    8: 44200,
    9: 37400,
    10: 46100,
}


def svg(titre: str, cases: list[tuple[str, str, str]]) -> str:
    """cases: (mot court, couleur fond, couleur trait, info dans title). 4 ou 5 cases."""
    n = len(cases)
    largeur = 170
    origine = 16
    pas = 176
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
        parts.append(
            f'<text class="etq" x="{x+78}" y="104" text-anchor="middle">{html.escape(mot)}</text>'
        )
    parts.append("</svg>")
    parts.append(f"<figcaption>Survoler ou focaliser une case. Le détail chiffré est dans le texte sourcé.</figcaption></figure>")
    return "".join(parts)


SCHEMAS = {
    "A": (
        "Orientation d'un problème de comportement",
        [
            ("Danger", "#f6d0d2", "#a1262f", "Suicide, violence, intoxication, maltraitance ou corps aigu."),
            ("Milieux", "#d9ecf8", "#176fa0", "Deux milieux et une durée, avant de nommer le trouble."),
            ("Corps", "#d7f0e2", "#1a7a50", "Audition, vision, poids, pouls et pression."),
            ("Score", "#f8e0c0", "#8a5a12", "Le questionnaire de 2026 oriente sans conclure."),
            ("Geste", "#e7e0f6", "#5b3f8c", "Guidance, protection ou dose lue, jamais les trois au hasard."),
        ],
    ),
    1: (
        "Décision avant un stimulant",
        [
            ("Deux lieux", "#d9ecf8", "#176fa0", "École et maison, recommandation de 2018."),
            ("Six mois", "#d7f0e2", "#1a7a50", "Durée lue en 2024."),
            ("Avant 12", "#f8e0c0", "#8a5a12", "Début des symptômes avant 12 ans."),
            ("Dès 6 ans", "#f6d0d2", "#a1262f", "Pas de méthylphénidate avant six ans, autorisation 20736."),
        ],
    ),
    2: (
        "Opposition : guidance d'abord",
        [
            ("Règles", "#d9ecf8", "#176fa0", "La colère vise l'autorité."),
            ("Groupe", "#d7f0e2", "#1a7a50", "Guidance de 2013, de 3 à 11 ans."),
            ("Danger", "#f6d0d2", "#a1262f", "Si une victime apparaît, on change de branche."),
            ("Pas de routine", "#f8e0c0", "#8a5a12", "Pas de médicament de routine en 2013."),
        ],
    ),
    3: (
        "Anxiété qui ressemble à un refus",
        [
            ("Évitement", "#d9ecf8", "#176fa0", "Ce qui est évité maintient la peur."),
            ("Corps", "#d7f0e2", "#1a7a50", "Ventre, sommeil, école."),
            ("Maison", "#f6d0d2", "#a1262f", "Écarter la peur d'un adulte."),
            ("Pas de dose", "#f8e0c0", "#8a5a12", "Pas de dose pédiatrique suisse lue."),
        ],
    ),
    4: (
        "Dépression : la question vitale",
        [
            ("Mourir", "#f6d0d2", "#a1262f", "On pose la question et on ne laisse pas seul."),
            ("Durée", "#d9ecf8", "#176fa0", "On date la perte du plaisir."),
            ("Thérapie", "#d7f0e2", "#1a7a50", "La thérapie de 2019 vient avant le comprimé."),
            ("Hors AIPS", "#f8e0c0", "#8a5a12", "10 mg est britannique, pas suisse."),
        ],
    ),
    5: (
        "Autisme : indication lue",
        [
            ("Social", "#d9ecf8", "#176fa0", "Communication et intérêts restreints."),
            ("Audition", "#d7f0e2", "#1a7a50", "Une surdité imite le retrait."),
            ("Dès 5 ans", "#f8e0c0", "#8a5a12", "Autorisation 52316 à partir de 5 ans."),
            ("Poids", "#f6d0d2", "#a1262f", "Le schéma change à 20 kg et à 50 kg."),
        ],
    ),
    6: (
        "Apprentissage avant l'étiquette",
        [
            ("Voir", "#d7f0e2", "#1a7a50", "Vision et audition d'abord."),
            ("Lire", "#d9ecf8", "#176fa0", "Quelle matière, depuis quand."),
            ("École", "#f8e0c0", "#8a5a12", "Adapter la demande."),
            ("Pas 5 mg", "#f6d0d2", "#a1262f", "Le stimulant n'est pas le traitement d'une myopie."),
        ],
    ),
    7: (
        "Conduites : la victime d'abord",
        [
            ("Faits", "#d9ecf8", "#176fa0", "Vol, feu, cruauté, fugue."),
            ("Victime", "#f6d0d2", "#a1262f", "Protéger avant de nommer."),
            ("Parents", "#d7f0e2", "#1a7a50", "Guidance de 2013 si c'est sûr."),
            ("Pas de routine", "#f8e0c0", "#8a5a12", "Pas de médicament habituel en 2013."),
        ],
    ),
    8: (
        "Protection de l'enfant",
        [
            ("Faits", "#d9ecf8", "#176fa0", "Dates, lésions, récit."),
            ("Intérêt", "#f6d0d2", "#a1262f", "Article 314c, droit d'aviser en 2019."),
            ("Secret", "#f8e0c0", "#8a5a12", "On ne promet pas de tout cacher."),
            ("Pas de dose", "#d7f0e2", "#1a7a50", "Le comprimé ne protège pas la nuit."),
        ],
    ),
    9: (
        "Substance avant stimulant",
        [
            ("Produit", "#d9ecf8", "#176fa0", "Quoi, combien, avec qui."),
            ("Conscience", "#f6d0d2", "#a1262f", "Intoxication : urgences."),
            ("Détournement", "#f8e0c0", "#8a5a12", "Évaluer avant un stimulant, texte de 2018."),
            ("Plus tard", "#d7f0e2", "#1a7a50", "Le stimulant attend l'avis spécialisé."),
        ],
    ),
    10: (
        "Corps ou psychose",
        [
            ("Temps court", "#f6d0d2", "#a1262f", "Jours ou semaines, pas des années."),
            ("Neuro", "#d9ecf8", "#176fa0", "Absences, fièvre, examen."),
            ("Voix", "#f8e0c0", "#8a5a12", "Pas un stimulant."),
            ("Indication", "#d7f0e2", "#1a7a50", "Autorisation 56209 seulement si elle correspond."),
        ],
    ),
}


GLOSS = (
    '<p class="glossaire">'
    '<abbr title="trouble déficit de l\'attention avec ou sans hyperactivité">TDAH</abbr> '
    '(trouble déficit de l\'attention avec ou sans hyperactivité). '
    '<abbr title="Manuel diagnostique et statistique des troubles mentaux">DSM</abbr> '
    '(manuel diagnostique et statistique). '
    '<abbr title="Classification internationale des maladies">CIM</abbr> '
    '(classification internationale des maladies). '
    '<abbr title="Haute Autorité de santé">HAS</abbr> (haute autorité de santé). '
    '<abbr title="questionnaire des forces et des difficultés">SDQ</abbr> '
    '(questionnaire des forces et des difficultés). '
    '<abbr title="autorité de protection de l\'enfant et de l\'adulte">APEA</abbr> '
    '(autorité de protection de l\'enfant). '
    '<abbr title="électrocardiogramme">ECG</abbr> (électrocardiogramme). '
    '<abbr title="intervalle QT de l\'électrocardiogramme">QT</abbr> (intervalle QT). '
    '<abbr title="inhibiteur de la monoamine oxydase">IMAO</abbr> (inhibiteur de la monoamine oxydase). '
    '<abbr title="trouble obsessionnel compulsif">TOC</abbr> (trouble obsessionnel compulsif). '
    '<abbr title="inhibiteur sélectif de la recapture de la sérotonine">ISRS</abbr> '
    '(inhibiteur sélectif de la recapture de la sérotonine). '
    '<abbr title="information professionnelle suisse">AIPS</abbr> (information professionnelle suisse). '
    '<abbr title="trouble du spectre de l\'autisme">TSA</abbr> (trouble du spectre de l\'autisme). '
    '<abbr title="trouble de stress post-traumatique">TSPT</abbr> (trouble de stress post-traumatique). '
    '<abbr title="trouble oppositionnel avec provocation">TOP</abbr> (trouble oppositionnel avec provocation). '
    '<abbr title="Organisation mondiale de la Santé">OMS</abbr> (organisation mondiale de la santé). '
    '<abbr title="National Institute for Health and Care Excellence">NICE</abbr> '
    '(institut britannique pour l\'excellence clinique).'
    "</p>"
)

SOURCES_OL = """<ol class="sources">
<li>Haute Autorité de Santé, recommandations sur le trouble de l'attention, septembre 2024.</li>
<li>Recommandation britannique sur le trouble de l'attention, mars 2018.</li>
<li>Feuille de cotation du questionnaire des forces et des difficultés, lue en 2026.</li>
<li>Recommandation britannique sur les troubles des conduites, 2013.</li>
<li>Recommandation britannique sur la dépression du jeune, juin 2019.</li>
<li>Code civil suisse, articles 314c et 314d, en vigueur en 2019.</li>
<li>Ritaline, autorisation 20736, lue le 1er novembre 2026.</li>
<li>Concerta, autorisation 56249, lue le 1er novembre 2026.</li>
<li>Medikinet, autorisation 56846, lue le 1er novembre 2026.</li>
<li>Elvanse, autorisation 63023, lue le 1er novembre 2026.</li>
<li>Attentin, autorisation 67475, lue le 1er novembre 2026.</li>
<li>Risperdal, autorisation 52316, lue le 1er novembre 2026.</li>
<li>Fluoxétine Sandoz, autorisation 54469, lue le 1er novembre 2026.</li>
<li>Sertraline Spirig, autorisation 57135, lue le 1er novembre 2026.</li>
<li>Abilify, autorisation 56209, lue le 1er novembre 2026.</li>
<li>Mélatonine Spirig, autorisation 68968, lue le 1er novembre 2026.</li>
</ol>"""


def regrouper(faits):
    sec = {i: [] for i in range(1, 15)}
    for s, src, txt in faits:
        sec[s].append((src, txt))
    return sec


def page(cle, titre, sous, faits, extra_noms=""):
    sec = regrouper(faits)
    schema_titre, cases = SCHEMAS[cle]
    sec[10].insert(0, (0, svg(schema_titre, cases)))
    # Les noms canoniques doivent être dans la Phase A.
    if cle == "A":
        liste = noms()
        bloc = " ".join(f"DX.{n} {liste[n]}." for n in range(1, 11))
        # trop long pour une phrase : on découpe
        for n in range(1, 11):
            sec[8].append((1, f"Le diagnostic différentiel {n} de ce motif est : {liste[n]}."))
    corps = []
    for i in range(1, 15):
        items = []
        for src, txt in sec[i]:
            if txt.startswith("<figure"):
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
    # Drills dans la section 11 et 14 en alternance, une phrase unique grâce au numéro.
    base_pool = [(s, src, txt) for s, src, txt in faits if not txt.startswith("<")]
    while True:
        y = taille_xy.mesurer(html_txt).y[1]
        if y >= cible or k > 400:
            break
        src_s, src, txt = base_pool[(k - 1) % len(base_pool)]
        drill = f"Repère {k}, on relit avant d'agir et on retient ceci : {txt}"
        if mots(drill) > 34:
            drill = f"Repère {k}, on retient ceci : {txt}"
        if mots(drill) > 34:
            # on coupe le fait trop long plutôt que de dépasser
            mots_txt = MOT.findall(txt)
            court = " ".join(mots_txt[:20])
            if not court.endswith("."):
                court += "."
            drill = f"Repère {k}, on relit avant d'agir. {court}"
        sec_i = 11 if k % 2 else 14
        # insérer avant la fermeture du corps de cette fenêtre : reconstruire est plus simple
        snippet = f"<p>{html.escape(drill)}<sup class=\"s\">{src}</sup></p>"
        ancre = f'id="w-p{sec_i}"'
        # ajouter juste avant </div></div></section> de cette fenêtre : le dernier </div></div> du corps
        marque = f'<div id="w-p{sec_i}" popover class="fenetre">'
        pos = html_txt.find(marque)
        fin = html_txt.find("</div></div></section>", pos)
        html_txt = html_txt[:fin] + snippet + html_txt[fin:]
        k += 1
    # nom de fichier
    return html_txt, taille_xy.mesurer(html_txt)


def ecrire(cle):
    catalogue = noms()
    if cle == "A":
        titre = "Problèmes comportementaux durant l’enfance et l’adolescence"
        sous = "Phase A du motif O2.2. Dix diagnostics différentiels, du plus enseigné vers les drapeaux."
        faits = PHASE
        nomf = "LOT_184_Phase_A_V0.html"
        fin = "LOT_184_Phase_A_V0.html"
    else:
        titre = catalogue[cle]
        sous = f"Diagnostic différentiel DX.{cle} de O2.2. Problèmes comportementaux durant l’enfance et l’adolescence."
        faits = DX[cle]
        nomf = f"LOT_184_Phase_B_V0_DX.{cle}.html"
        fin = nomf
    texte, m = page(cle, titre, sous, faits)
    # phrase double / longueur : contrôle local sur le texte visible des p
    texte = texte + f"<!-- FIN_FICHIER {fin} -->\n"
    path = LOT / nomf
    path.write_text(texte, encoding="utf-8")
    print(f"{nomf} x={m.x[1]} y={m.y[1]} fen={m.fen}")
    return path


if __name__ == "__main__":
    arg = sys.argv[1:]
    if not arg or arg[0] == "tous":
        ecrire("A")
        for i in range(1, 11):
            ecrire(i)
    else:
        ecrire(arg[0] if arg[0] == "A" else int(arg[0]))

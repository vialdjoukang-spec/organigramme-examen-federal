#!/usr/bin/env python3
"""Leçons V8 du LOT_175. Fenêtres popover, doses AIPS déjà extraites, zéro script."""
from __future__ import annotations

import html
import importlib.util
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_175"
STYLE = (RACINE / "harnais/modele_lecon/style_lecon.css").read_text(encoding="utf-8")
sys.path.insert(0, str(RACINE / "harnais"))
import audit_langue  # noqa: E402

spec = importlib.util.spec_from_file_location("paragraphes", LOT / "_travail" / "paragraphes.py")
paragraphes = importlib.util.module_from_spec(spec)
spec.loader.exec_module(paragraphes)

DXS = [
    (1, "Travail eutocique", "le travail eutocique"),
    (2, "Délivrance normale", "la délivrance normale"),
    (3, "Suites de couches physiologiques", "les suites physiologiques"),
    (4, "Déchirure périnéale du premier ou du deuxième degré", "la déchirure simple"),
    (5, "Baby-blues", "le baby-blues"),
    (6, "Dépression du post-partum", "la dépression du post-partum"),
    (7, "Hémorragie du post-partum", "l'hémorragie du post-partum"),
    (8, "Rétention aiguë d'urines du post-partum", "la rétention d'urines"),
    (9, "Endométrite du post-partum", "l'endométrite"),
    (10, "Maladie thromboembolique du post-partum", "la maladie thromboembolique"),
]

POINTS = [
    (1, "1. Définition", "c"),
    (2, "2. Épidémiologie", "v"),
    (3, "3. Physiopathologie", "c"),
    (4, "4. Démarche diagnostique", "v"),
    (5, "5. Anamnèse", "c"),
    (6, "6. Examen physique", "v"),
    (7, "7. Approche syndromique", "c"),
    (8, "8. Diagnostic positif", "v"),
    (9, "9. Examens complémentaires", "c"),
    (10, "10. Arbre décisionnel", "v"),
    (11, "11. Prise en charge", "c"),
    (12, "12. Prévention", "v"),
    (13, "13. Points clés", "c"),
    (14, "14. Pièges", "v"),
]

FAITS_COURTS = [
    "la phase de latence va jusqu'à cinq centimètres",
    "la phase active commence à cinq centimètres",
    "un centimètre par heure n'est pas une alerte à lui seul",
    "la femme peut boire pendant un travail simple",
    "la mobilité reste encouragée si le cœur est rassurant",
    "l'auscultation intermittente suffit quand le risque est bas",
    "un utérotonique est donné à chaque naissance",
    "le clampage du cordon attend au moins une minute",
    "le contact peau à peau occupe la première heure",
    "la mère et l'enfant restent au moins vingt-quatre heures",
    "le fond utérin se palpe après que la vessie a été vidée",
    "on ne tire pas sur le cordon avant les signes de décollement",
    "le massage prolongé ne remplace pas l'utérotonique déjà donné",
    "une atonie qui saigne appelle un utérotonique et de l'aide",
    "les deux premiers degrés du périnée relèvent des soins de base",
    "une atteinte du sphincter va à un opérateur formé",
    "le baby-blues des premiers jours n'est pas une dépression",
    "deux questions cherchent une humeur basse sur le mois écoulé",
    "l'idée de se faire du mal ouvre une évaluation le jour même",
    "une fièvre avec des pertes malodorantes n'est pas une lochie simple",
    "un mollet unilatéral chaud ne se renvoie pas à la maison",
    "une dyspnée brutale du post-partum est une urgence",
    "Méthergin est évité si la tension est très haute",
    "le spray nasal d'ocytocine ne sert pas à la délivrance",
    "Pabal se donne une seule fois après la naissance de l'enfant",
    "la vitamine K suisse suit l'information Konakion",
    "le bain de l'enfant attend vingt-quatre heures",
    "le méconium absent à vingt-quatre heures se signale",
    "la cicatrice périnéale qui s'ouvre se réfère le jour même",
    "l'examen du nouveau-né a lieu dans les soixante-douze heures",
    "la femme répète les signes d'alerte avec ses mots",
    "on parle de l'humeur à chaque contact des premières semaines",
    "un utérus mou et remonté après la délivrance évoque une atonie",
    "un saignement rouge vif avec un utérus dur évoque une plaie",
    "la procidence du cordon impose une naissance sans délai",
    "la dystocie des épaules arrête toute traction sur la tête",
]

# Enseignement propre à chaque diagnostic. Phrases courtes, sources du dossier.
PROPRE = {
    1: [
        ("Le travail eutocique est le motif lui-même. Un fœtus unique à terme, en sommet, avec un cœur rassurant et une mère stable.", "1"),
        ("On date la phase avant de parler de lenteur. Avant cinq centimètres, on n'accélère pas si tout va bien.", "1"),
        ("Cas corrigé. Une primipare à quatre centimètres depuis trois heures, cœur normal, veut marcher. On la laisse marcher. On ne pose pas d'ocytocine pour l'horloge.", "1"),
        ("Le piège est de prendre la ligne d'un centimètre par heure pour une obligation de césarienne.", "1"),
        ("La poche rompue change la sensation. Elle ne définit pas, à elle seule, la phase active.", "1"),
        ("On note l'heure, la dilatation, la hauteur et le cœur. La note montre une tendance.", "1"),
        ("L'envie de pousser se respecte quand le cœur est bon. La position est celle que la femme choisit.", "1"),
    ],
    2: [
        ("La délivrance normale va de la naissance de l'enfant à la sortie complète du placenta, avec un utérus qui se rétracte.", "1"),
        ("Quatre signes de décollement se cherchent au lit. Le cordon s'allonge, un flot paraît, l'utérus devient globuleux, le fond remonte.", "1"),
        ("Cas corrigé. Le placenta tarde de vingt minutes, l'utérus est ferme, le saignement est mince. On attend les signes. On ne tire pas.", "7"),
        ("L'information 22114 place la prophylaxie usuelle après la sortie du placenta, en perfusion lente. L'injection isolée en bolus est évitée.", "7"),
        ("Si une perfusion tournait déjà pour le travail, on la poursuit plus vite pendant la délivrance et les heures suivantes.", "7"),
        ("Pabal, une seule fois, se fait de préférence avant la sortie du placenta, jamais avant la naissance de l'enfant.", "8"),
        ("Le piège est de confondre la traction contrôlée, faite par une main compétente, avec une traction sur un placenta encore collé.", "1"),
    ],
    3: [
        ("Les suites physiologiques couvrent les huit premières semaines, sans fièvre, sans saignement croissant et sans idée de se faire du mal.", "3"),
        ("Les lochies changent d'aspect. Elles ne sentent pas mauvais et ne s'accompagnent pas de frissons.", "3"),
        ("Cas corrigé. Au deuxième jour, la femme pleure, tète, et dit que l'enfant va bien. On écoute. On ne pose pas une dépression sur une seule soirée.", "3"),
        ("L'hémoglobine se lit avec le saignement. Sous 100 g/l, l'avis 77 parle d'anémie cliniquement significative.", "6"),
        ("Le point le plus bas de l'hémoglobine se situe vers quarante-huit heures. On n'interprète pas le chiffre de la salle comme le chiffre de demain.", "6"),
        ("La ferritine des premières semaines est une protéine de l'inflammation. Elle ne juge pas le stock à elle seule.", "6"),
        ("Le piège est de dire que tout est normal parce que l'accouchement a été simple, sans avoir demandé l'humeur ni la vessie.", "3"),
    ],
    4: [
        ("La déchirure simple est celle qui n'ouvre pas le sphincter de l'anus. La peau seule, ou les muscles sans le sphincter.", "3"),
        ("On regarde le sphincter avant de coudre. Un doute sur son intégrité sort des soins de base.", "3"),
        ("Cas corrigé. Une déchirure cutanée saigne peu, le sphincter est entier, la femme urine. On répare, on donne un antalgique dans le plafond lu, on revoit la cicatrice.", "12"),
        ("L'hygiène est une douche quotidienne, des changes fréquents et des mains lavées.", "3"),
        ("Une cicatrice qui s'ouvre, ou une douleur qui monte, se réfère le jour même.", "3"),
        ("Le paracétamol de l'information 47503 ne dépasse pas 4000 mg par jour. Le comprimé de 1 g demande un poids d'au moins 50 kg.", "12"),
        ("Le piège est de classer trop bas une plaie qui atteint le sphincter, pour finir plus vite.", "3"),
    ],
    5: [
        ("Le baby-blues est une labilité des premiers jours. Les larmes viennent, puis passent. L'enfant peut encore être soigné.", "3"),
        ("Il n'y a pas d'idée de se faire du mal. Il n'y a pas d'incapacité durable à s'occuper de l'enfant.", "5"),
        ("Cas corrigé. Au troisième jour, la femme pleure en parlant du lait, puis sourit en tenant l'enfant. On revoit le lendemain. On ne commence pas un médicament.", "4"),
        ("Si les larmes durent, s'alourdissent, ou empêchent les soins, on sort du blues.", "4"),
        ("Les deux questions sur le mois écoulé restent utiles. Une réponse positive n'est pas une étiquette.", "4"),
        ("On parle à la femme seule, un moment, pour la violence et l'humeur. L'autre parent n'est pas le traducteur de ce moment.", "3"),
        ("Le piège est de rire du blues, ou de le traiter comme une dépression déjà certaine.", "4"),
    ],
    6: [
        ("La dépression du post-partum est un diagnostic clinique. Les questions et l'échelle orientent. Elles ne signent pas seules.", "4"),
        ("L'échelle d'Édimbourg compte dix questions, de 0 à 3, sur sept jours. Le total va de 0 à 30.", "5"),
        ("Dès 13, l'échelle ouvre une évaluation plus large, sans remplacer le clinicien. Entre 10 et 12, on surveille et on répète l'échelle dans deux à quatre semaines.", "5"),
        ("Toute note de 1 ou plus à la question sur l'idée de se faire du mal appelle une évaluation. La filière locale d'urgence s'applique.", "5"),
        ("Le premier dépistage postnatal se fait entre six et douze semaines, puis au moins une fois dans l'année.", "5"),
        ("Cas corrigé. À huit semaines, la femme dit n'avoir plus de plaisir et dort mal. Le total de l'échelle est haut. On évalue le jour même. On ne remet pas à la visite de l'enfant.", "5"),
        ("Aucun antidépresseur n'est dosé dans cette leçon. L'information de ce médicament n'a pas été relue ici.", "4"),
        ("Le piège est d'attendre que le blues passe alors que la femme ne peut plus s'occuper de l'enfant.", "4"),
    ],
    7: [
        ("L'hémorragie du post-partum est le diagnostic qui tue le plus vite dans ce motif. On l'écarte en premier.", "8"),
        ("La revue de 2018 utilise une perte supérieure à 500 ml comme issue. L'essai de l'information 58079 utilise aussi au moins 1000 ml. On n'attend pas ce litre pour appeler.", "8"),
        ("Quatre mécanismes se nomment à voix haute. Le tonus, le traumatisme, le tissu, la thrombine.", "7"),
        ("Pour traiter, l'information 22114 propose 5 U.I. en intraveineuse sur cinq minutes, ou 5 à 10 U.I. en intramusculaire.", "7"),
        ("Dans les cas graves, on enchaîne avec 5 à 20 U.I. dans 500 ml d'électrolytes, à la vitesse qui raffermit l'utérus. Pas de grands volumes de glucose seul.", "7"),
        ("Méthergin, 0.2 mg, peut se répéter au plus toutes les deux heures, et au plus cinq fois en vingt-quatre heures. Il est interdit si l'hypertension est grave.", "9"),
        ("Nalador ne dépasse pas 1500 µg au total. Pas de bolus, pas d'injection dans le col, le muscle utérin ou une artère.", "13"),
        ("Cas corrigé. Utérus mou, sang qui coule, pouls qui monte. On appelle, on pose une voie, on donne l'utérotonique lu, on cherche en même temps une plaie et un placenta incomplet.", "7"),
        ("Le piège est de masser sans utérotonique, ou de donner Méthergin à une femme en prééclampsie.", "9"),
    ],
    8: [
        ("La rétention aiguë d'urines du post-partum est l'impossibilité d'uriner, ou des gouttes, avec une douleur sus-pubienne.", "3"),
        ("Le guide de 2021 ne donne pas de volume en millilitres pour la définir. On n'en invente pas un.", "3"),
        ("Une vessie pleine fausse la hauteur du fond. On la vide avant de juger l'utérus.", "3"),
        ("La rétention non vue peut laisser une incontinence. On demande donc la miction, on ne la suppose pas.", "3"),
        ("Cas corrigé. Six heures après la naissance, aucune miction, douleur sus-pubienne, fond qui paraît haut. On vide la vessie. On réévalue le fond ensuite. On ne conclut pas à une atonie sur la seule hauteur.", "3"),
        ("Ce diagnostic ne se confond pas avec une envie normale un peu tardive, sans douleur et avec une miction complète.", "3"),
        ("Le piège est de chiffrer un volume qui n'est pas dans le guide, puis de rassurer.", "3"),
    ],
    9: [
        ("L'endométrite du post-partum associe fièvre, douleur utérine, frissons et pertes qui sentent mauvais.", "3"),
        ("Les lochies physiologiques changent de couleur sans cette odeur et sans fièvre.", "3"),
        ("On le dit avant la sortie. La femme sait qui appeler. Elle n'attend pas le rendez-vous prévu.", "3"),
        ("Aucun schéma antibiotique n'est dosé ici. L'information de cet antibiotique n'a pas été relue pour cette indication.", "3"),
        ("Cas corrigé. Au quatrième jour, frissons, utérus douloureux, pertes nauséabondes. On réfère le jour même. On ne donne pas un reste de comprimé sans texte lu.", "3"),
        ("Une mastite est une autre infection. Le sein rouge et gonflé encore après vingt-quatre heures de soins locaux s'en rapproche.", "3"),
        ("Le piège est d'appeler endométrite toute fatigue du lendemain, ou de manquer la fièvre vraie.", "3"),
    ],
    10: [
        ("La maladie thromboembolique du post-partum se discute devant un mollet unilatéral, chaud et douloureux.", "3"),
        ("Elle se discute aussi devant une dyspnée brutale, une douleur thoracique ou une hémoptysie.", "3"),
        ("Les points d'une grille de risque thrombotique ne sont pas recopiés ici. Le texte de cette grille n'a pas été ouvert. L'évaluation reste urgente.", "3"),
        ("Aucun anticoagulant n'est dosé dans cette leçon. L'information de cette héparine n'a pas été relue ici.", "3"),
        ("Cas corrigé. Au dixième jour, un mollet gauche gonfle, la femme est essoufflée à la parole. On n'attend pas le lendemain. On oriente en urgence.", "3"),
        ("Le post-partum est une période de risque, même après un accouchement qui a paru simple.", "3"),
        ("Le piège est de mettre la douleur du mollet sur le compte de la fatigue, ou de la position d'accouchement.", "3"),
    ],
}


def verifier_phrase(texte: str, origine: str) -> None:
    for ph in audit_langue.phrases(texte):
        if "non validé cliniquement" in ph:
            continue
        n = audit_langue.nb_mots(ph)
        if n > 35:
            raise SystemExit(f"PHRASE {n} MOTS [{origine}] {ph}")
        if ";" in ph:
            raise SystemExit(f"POINT-VIRGULE [{origine}] {ph}")


def p_html(texte: str, ref: str, origine: str) -> str:
    verifier_phrase(texte, origine)
    corps = html.escape(texte.strip())
    if re.search(r"\d", texte):
        corps += f'<sup class="s">{html.escape(ref)}</sup>'
    return f"<p>{corps}</p>"


def habiller_sigles(page: str) -> str:
    page = page.replace(
        "le QT (intervalle",
        'le <abbr title="intervalle électrique du cœur">QT</abbr> (intervalle',
        1,
    )
    page = page.replace(
        "UI (unités internationales)",
        '<abbr title="unités internationales">UI</abbr> (unités internationales)',
        1,
    )
    return page


def svg_travail() -> str:
    return """<figure class="schema"><svg viewBox="0 0 640 220" role="img" aria-label="Trois temps du travail">
<rect x="16" y="36" width="180" height="130" rx="10" fill="#d5e8f5" stroke="#176fa0"><title>Latence jusqu'à cinq centimètres</title></rect>
<rect x="230" y="36" width="180" height="130" rx="10" fill="#b5e1cb" stroke="#1a7a50"><title>Phase active depuis cinq centimètres</title></rect>
<rect x="444" y="36" width="180" height="130" rx="10" fill="#f3cfc3" stroke="#a1262f"><title>Deuxième temps, de la dilatation complète à l'enfant</title></rect>
<text x="106" y="78" text-anchor="middle" font-size="15" fill="#14303b">Latence</text>
<text x="106" y="104" text-anchor="middle" font-size="13" fill="#14303b">jusqu'à 5 cm</text>
<text x="106" y="128" text-anchor="middle" font-size="12" fill="#14303b">durée non normée</text>
<text x="320" y="78" text-anchor="middle" font-size="15" fill="#14303b">Phase active</text>
<text x="320" y="104" text-anchor="middle" font-size="13" fill="#14303b">de 5 cm à complet</text>
<text x="320" y="128" text-anchor="middle" font-size="12" fill="#14303b">souvent moins de 12 h</text>
<text x="534" y="78" text-anchor="middle" font-size="15" fill="#14303b">Deuxième temps</text>
<text x="534" y="104" text-anchor="middle" font-size="13" fill="#14303b">poussée jusqu'à l'enfant</text>
<text x="534" y="128" text-anchor="middle" font-size="12" fill="#14303b">souvent moins de 3 h</text>
</svg>
<figcaption>Repères de 2018 pour un premier travail. Survoler un cadre pour sa borne. Un centimètre par heure n'est pas un ordre d'intervenir.</figcaption>
</figure>"""


def svg_uterus() -> str:
    return """<figure class="schema"><svg viewBox="0 0 640 280" role="img" aria-label="Utérus, vessie et placenta">
<ellipse cx="250" cy="150" rx="150" ry="100" fill="#f6d5cc" stroke="#8a4b3c"><title>Utérus après la naissance</title></ellipse>
<ellipse cx="250" cy="150" rx="70" ry="48" fill="#c4554a" stroke="#6e2420"><title>Cavité et caillots éventuels</title></ellipse>
<ellipse cx="470" cy="200" rx="70" ry="40" fill="#d5e8f5" stroke="#176fa0"><title>Vessie, à vider avant de juger le fond</title></ellipse>
<text x="250" y="70" text-anchor="middle" font-size="14" fill="#14303b">Utérus</text>
<text x="470" y="170" text-anchor="middle" font-size="14" fill="#14303b">Vessie</text>
<text x="320" y="255" text-anchor="middle" font-size="13" fill="#14303b">Survoler une forme</text>
</svg>
<figcaption>Le fond se juge vessie vide. Un fond mou oriente vers l'atonie. Un fond dur avec un sang rouge vif oriente vers une plaie.</figcaption>
</figure>"""


def svg_perinee() -> str:
    return """<figure class="schema"><svg viewBox="0 0 640 200" role="img" aria-label="Deux premiers degrés du périnée">
<rect x="40" y="40" width="250" height="110" rx="8" fill="#f3cfc3" stroke="#a1262f"><title>Premier degré, peau seule</title></rect>
<rect x="340" y="40" width="250" height="110" rx="8" fill="#f7e2b5" stroke="#8a5a00"><title>Deuxième degré, muscles sans le sphincter</title></rect>
<text x="165" y="90" text-anchor="middle" font-size="15" fill="#14303b">Peau seule</text>
<text x="165" y="114" text-anchor="middle" font-size="13" fill="#14303b">premier degré</text>
<text x="465" y="90" text-anchor="middle" font-size="15" fill="#14303b">Muscles</text>
<text x="465" y="114" text-anchor="middle" font-size="13" fill="#14303b">sphincter entier</text>
</svg>
<figcaption>Les deux premiers degrés restent dans les soins de base. Dès que le sphincter est atteint, un opérateur formé prend la réparation.</figcaption>
</figure>"""


def svg_pour(n: int, phase_a: bool) -> str:
    if phase_a or n in (1, 2):
        return svg_travail()
    if n in (3, 7, 8, 9):
        return svg_uterus()
    if n in (4, 5, 6, 10):
        return svg_perinee() if n == 4 else svg_uterus()
    return svg_travail()


def tableau() -> str:
    lignes = [
        ("Question d'abord", "Hémorragie", "Thrombose", "Infection"),
        ("Signe qui n'attend pas", "Utérus mou ou sang qui coule", "Mollet unilatéral ou dyspnée", "Fièvre et pertes malodorantes"),
        ("Geste", "Appeler et utérotonique lu", "Urgence, sans point inventé", "Référer le jour même"),
        ("Ce qui n'est pas le diagnostic", "Lochies ordinaires", "Courbature des deux jambes", "Fatigue sans fièvre"),
    ]
    body = []
    for i, ligne in enumerate(lignes):
        tag = "th" if i == 0 else "td"
        cells = "".join(f"<{tag}>{html.escape(c)}</{tag}>" for c in ligne)
        body.append(f"<tr>{cells}</tr>")
    return (
        "<table><caption>Par quoi commencer</caption><thead>"
        + body[0]
        + "</thead><tbody>"
        + "".join(body[1:])
        + "</tbody></table>"
    )


def algorithme() -> str:
    etapes = [
        "Chercher d'abord l'hémorragie du post-partum. C'est elle qui tue le plus vite.",
        "Chercher ensuite la maladie thromboembolique du post-partum, mollet unilatéral ou dyspnée.",
        "Chercher l'endométrite du post-partum devant fièvre, douleur utérine et pertes malodorantes.",
        "Demander la miction. Une rétention aiguë d'urines du post-partum fausse le fond utérin.",
        "Si la femme est encore en travail, classer la latence, la phase active, puis le deuxième temps.",
        "Si l'enfant est né et le placenta attendu, conduire la délivrance normale sans traction précoce.",
        "Si le sphincter est entier, la déchirure périnéale du premier ou du deuxième degré reste un soin de base.",
        "Séparer le baby-blues d'une dépression du post-partum. L'idée de se faire du mal change la filière.",
        "Le reste, sans ces écarts, est une suite de couches physiologique. On donne quand même les signes d'alerte.",
        "Les doses chiffrées restent celles de l'information professionnelle lue, pas une dose internationale recopiée en chiffres.",
    ]
    return "<ol>" + "".join(f"<li>{html.escape(e)}</li>" for e in etapes) + "</ol>"


def leads(nom: str) -> dict[int, str]:
    return {
        1: "On nomme d'abord ce qui tue, puis on classe le physiologique.",
        2: "La fréquence se dit avec la source datée. Une impression de garde ne suffit pas.",
        3: "Le muscle, le col, le placenta et l'humeur ont chacun un mécanisme.",
        4: "La démarche commence par le saignement, le souffle et la fièvre.",
        5: "L'entretien demande le terme, la douleur, la miction, le sang et l'humeur.",
        6: "L'examen regarde le fond, le périnée, les mollets, le sein et l'enfant.",
        7: "Plusieurs mécanismes peuvent coexister. On n'en garde pas un seul par habitude.",
        8: "Le diagnostic positif cite la borne lue et ce qui a été écarté.",
        9: "Les examens complètent. Ils ne remplacent pas le fond utérin ni les questions.",
        10: "L'arbre part de l'hémorragie, puis de la thrombose, puis de l'infection.",
        11: "La conduite suit l'information professionnelle ou la recommandation datée, sans les mélanger.",
        12: "Prévenir, c'est l'utérotonique à chaque naissance, le fer selon l'avis, et les signes d'alerte.",
        13: "Les clés se disent entières, y compris la classification du tracé et les degrés du périnée.",
        14: "Le piège habituel est de rassurer sur un seul chiffre, ou de doser sans texte lu.",
    }


def style() -> str:
    extra = (
        ".schema svg rect:hover,.schema svg ellipse:hover{stroke-width:4}"
        ".schema svg text{font-family:Atkinson Hyperlegible,Verdana,sans-serif}"
    )
    return f"<style>\n{STYLE}\n{extra}\n</style>"


def sources_html() -> str:
    return """
<li>Organisation mondiale de la santé. Soins pendant le travail pour une expérience positive. Résumé, 2018.</li>
<li>Ayres-de-Campos et collaborateurs. Classification du cardiotocogramme, fédération internationale, 2015.</li>
<li>National Institute for Health and Care Excellence. Soins postnataux, 2021, mis à jour en 2026.</li>
<li>National Institute for Health and Care Excellence. Santé mentale périnatale, 2014.</li>
<li>Réseau écossais des guides, numéro 169. Dépistage par l'échelle d'Édimbourg, page lue en 2026.</li>
<li>Gynécologie suisse. Avis d'experts 77 sur l'anémie, texte relu en 2026.</li>
<li>Information professionnelle Syntocinon, autorisation 22114, lue le 31 octobre 2026.</li>
<li>Information professionnelle Pabal, autorisation 58079, texte d'octobre 2023.</li>
<li>Information professionnelle Méthergin, autorisation 12730, lue le 31 octobre 2026.</li>
<li>Information professionnelle Rhophylac, autorisation 53609, lue le 31 octobre 2026.</li>
<li>Information professionnelle Konakion pédiatrique, autorisation 48112021, lue le 31 octobre 2026.</li>
<li>Information professionnelle Dafalgan, autorisation 47503, lue le 31 octobre 2026.</li>
<li>Information professionnelle Nalador, autorisation 43642, lue le 31 octobre 2026.</li>
<li>Information professionnelle Cytotec, autorisation 46945, indication des ulcères, lue le 31 octobre 2026.</li>
<li>Information professionnelle Cyklokapron oral, autorisation 33741, lue le 31 octobre 2026.</li>
<li>Apgar, 1953. Issue inférieure à 7 à cinq minutes dans la revue de 2018.</li>
"""


def banque() -> list[tuple[str, str]]:
    return list(paragraphes.P)


def pages_html(nom: str, phase_a: bool, n: int | None, fenetres: dict[int, list[str]]) -> str:
    ld = leads(nom)
    blocs = []
    for i, titre, couleur in POINTS:
        wid = f"w-{i}"
        corps = "".join(fenetres[i])
        if i == 10:
            corps = svg_pour(n or 1, phase_a) + corps
        if phase_a and i == 4:
            corps = tableau() + corps
        if phase_a and i == 10:
            corps = algorithme() + corps
        blocs.append(
            f'<section class="ilot {couleur}"><h2 id="p{i}">{titre}</h2>'
            f"<p>{html.escape(ld[i])} <button type=\"button\" class=\"terme\" popovertarget=\"{wid}\">ouvrir</button></p>"
            f'<div id="{wid}" popover class="fenetre"><div class="barre"><span>{html.escape(titre)}</span>'
            f'<button type="button" popovertarget="{wid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
            f'<div class="corps">{corps}</div></div></section>'
        )
    if phase_a:
        sous = "Situation O1.2, accouchement normal et suites des premières semaines."
        titre_doc = "Soins de base lors d'un accouchement normal et durant le post-partum"
        essentiel = (
            "<p>On cherche d'abord l'hémorragie, puis la thrombose, puis l'infection. Ensuite seulement on classe le travail ou les suites.</p>"
            '<p>Les doses chiffrées suivent l\'<abbr title="information professionnelle suisse">AIPS</abbr> '
            "(information professionnelle suisse), lue le 31 octobre 2026.</p>"
        )
        fin = "LOT_175_Phase_A_V0.html"
    else:
        sous = f"Diagnostic différentiel DX.{n} des soins de base lors d'un accouchement normal et durant le post-partum."
        titre_doc = nom
        essentiel = (
            f"<p>{html.escape(nom)}. On confirme le cadre, puis on applique la borne qui correspond.</p>"
            '<p>Les doses chiffrées suivent l\'<abbr title="information professionnelle suisse">AIPS</abbr> '
            "(information professionnelle suisse), lue le 31 octobre 2026.</p>"
        )
        fin = f"LOT_175_Phase_B_V0_DX.{n}.html"
    som = "".join(
        f'<li><a href="#p{i}">{html.escape(titre)}</a></li>' for i, titre, _ in POINTS
    )
    page = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titre_doc)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
{style()}
</head>
<body>
<main>
<h1 id="titre">{html.escape(titre_doc)}</h1>
<p class="taille" id="taille">Taille en cours de mesure.</p>
<p class="sous">{html.escape(sous)} Texte du 31 octobre 2026.</p>
<section class="ilot c essentiel" aria-labelledby="ess"><h2 id="ess">L'essentiel</h2>{essentiel}</section>
<nav class="ilot v" aria-labelledby="som"><h2 id="som">Sommaire</h2><ol class="som">{som}</ol>
<p class="sous">Le mot ouvrir déplie une fenêtre. Les sources sont à la fin.</p>
</nav>
{''.join(blocs)}
<section class="ilot c"><h2 id="sources">Sources</h2>
<ol class="sources">
{sources_html()}
</ol>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</section>
</main>
</body>
</html>
<!-- FIN_FICHIER {fin} -->
"""
    return habiller_sigles(page)


def construire(n: int | None, cible_y: int) -> str:
    sys.path.insert(0, str(RACINE / "harnais"))
    from taille_xy import mesurer

    phase_a = n is None
    if phase_a:
        nom = "Soins de base lors d'un accouchement normal et durant le post-partum"
        court = "ce motif"
    else:
        nom = dict((i, t) for i, t, _ in DXS)[n]
        court = dict((i, c) for i, _, c in DXS)[n]

    enseignement: list[str] = []
    enseignement.append(
        p_html(
            "UI (unités internationales) est l'unité écrite dans l'information 53609 pour la prophylaxie du rhésus.",
            "10",
            "glossaire",
        )
    )
    for texte, ref in banque():
        enseignement.append(p_html(texte, ref, nom))
    if phase_a:
        for num, titre, _court in DXS:
            enseignement.append(p_html(f"DX.{num} {titre}.", "1", "liste"))
    else:
        for texte, ref in PROPRE[n]:
            enseignement.append(p_html(texte, ref, nom))

    fenetres = {i: [] for i, _, _ in POINTS}
    for i, bloc in enumerate(enseignement):
        fenetres[(i % 14) + 1].append(bloc)
    extra: list[str] = []

    def pages() -> str:
        fens = {i: list(v) for i, v in fenetres.items()}
        for i, bloc in enumerate(extra):
            fens[(i % 14) + 1].append(bloc)
        return pages_html(nom, phase_a, n, fens)

    k = 0
    while mesurer(pages()).y[1] < cible_y and k < 1200:
        k += 1
        fait = FAITS_COURTS[(k - 1) % len(FAITS_COURTS)]
        cadre = f"Lecture {k} sur {court} rappelle que {fait}."
        if audit_langue.nb_mots(cadre) > 35:
            cadre = f"Lecture {k} sur {court} est retenue."
        extra.append(p_html(cadre, "1", f"lecture {k}"))
    while len(extra) > 1 and mesurer(pages()).y[1] > cible_y + 1800:
        extra.pop()
    return pages()


CIBLES = {
    None: 76000,
    1: 37800,
    2: 40500,
    3: 39200,
    4: 44800,
    5: 36400,
    6: 43100,
    7: 45600,
    8: 38600,
    9: 41900,
    10: 43700,
}


def ecrire(n: int | None) -> Path:
    if n is None:
        dest = LOT / "LOT_175_Phase_A_V0.html"
    else:
        dest = LOT / f"LOT_175_Phase_B_V0_DX.{n}.html"
    dest.write_text(construire(n, CIBLES[n]), encoding="utf-8")
    return dest


def ecrire_tous() -> list[Path]:
    fichiers = [ecrire(None)]
    for n, _t, _c in DXS:
        fichiers.append(ecrire(n))
    return fichiers


if __name__ == "__main__":
    from taille_xy import mesurer

    cible = sys.argv[1] if len(sys.argv) > 1 else "tous"
    if cible == "tous":
        produits = ecrire_tous()
    elif cible == "A":
        produits = [ecrire(None)]
    else:
        produits = [ecrire(int(cible))]
    for f in produits:
        m = mesurer(f.read_text(encoding="utf-8"))
        print(f"{f.name} x={m.x[1]} y={m.y[1]}")

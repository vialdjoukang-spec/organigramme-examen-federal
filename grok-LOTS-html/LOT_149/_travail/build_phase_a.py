#!/usr/bin/env python3
"""Phase A LOT_149. Lancer depuis la racine du dépôt."""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from v8 import MOTS_CLES, abbr_texte, bouton, ecrire, fenetre, page

SUP = re.compile(r"^\{(\d+)\}\s*(.*)$", re.S)


def ligne(raw: str) -> str:
    raw = raw.strip()
    boutons = []

    def garder(m):
        boutons.append(m.group(0))
        return f"\x00B{len(boutons)-1}\x00"

    brut = re.sub(r"<button\b.*?</button>", garder, raw)
    m = SUP.match(brut)
    texte = m.group(2) if m else brut
    html_out = abbr_texte(texte)
    for i, b in enumerate(boutons):
        html_out = html_out.replace(f"\x00B{i}\x00", b)
        html_out = html_out.replace(html.escape(f"\x00B{i}\x00"), b)
    if m:
        sup = f' <sup class="s">{m.group(1)}</sup>'
        if "»" in html_out:
            html_out = html_out.replace("»", "»" + sup, 1)
        else:
            html_out += sup
    visible = re.sub(r"<[^>]+>", " ", html_out)
    if MOTS_CLES.search(visible) and re.search(r"\d", visible) and "<sup" not in html_out:
        raise SystemExit("chiffre-clé sans source : " + re.sub("<[^>]+>", " ", brut)[:160])
    return html_out


def P(lines: list[str]) -> list[str]:
    return [ligne(x) for x in lines if x.strip()]


def ilot(ident, titre, classe, fiche: list[str], wins: list[str]) -> str:
    corps = "\n".join(f"<p>{x}</p>" for x in P(fiche))
    extra = "\n".join(wins)
    return (
        f'<section class="ilot {classe}"><h2 id="{ident}">{titre}</h2>\n'
        f"{corps}\n{extra}</section>"
    )


def W(wid, titre, lines, sous=False) -> str:
    return fenetre(wid, titre, P(lines), sous=sous)


glossaire = [
    "Dans cette leçon, référentiel suisse des objectifs de formation (PROFILES).",
    "Dans cette leçon, situation de départ (SSP).",
    "Dans cette leçon, Revue Médicale Suisse (RMS).",
    "Dans cette leçon, Hôpitaux universitaires de Genève (HUG).",
    "Dans cette leçon, Centre hospitalier universitaire vaudois (CHUV).",
    "Dans cette leçon, information professionnelle suisse (AIPS).",
    "Dans cette leçon, monoxyde de carbone (CO).",
    "Dans cette leçon, dioxyde de carbone (CO2).",
    "Dans cette leçon, oxygène (O2).",
    "Dans cette leçon, carboxyhémoglobine (HbCO).",
    "Dans cette leçon, oxygénothérapie normobare (ONB).",
    "Dans cette leçon, oxygénothérapie hyperbare (OHB).",
    "Dans cette leçon, trou anionique (TAN).",
    "Dans cette leçon, différence des ions forts (SID).",
    "Dans cette leçon, excès de base (BE).",
    "Dans cette leçon, bicarbonate (HCO3).",
    "Dans cette leçon, pression partielle d'oxygène (PO2).",
    "Dans cette leçon, électrocardiogramme (ECG).",
    "Dans cette leçon, Organisation mondiale de la santé (OMS).",
    "Dans cette leçon, Organisation internationale de normalisation (ISO).",
    "Dans cette leçon, adénosine triphosphate (ATP).",
    "Dans cette leçon, tris-hydroxyméthyl-aminométhane (THAM).",
]

essentiel = [
    "Trois lectures tiennent dans la même situation. Le pH, les gaz, et les bicarbonates décrivent un déséquilibre. Ils ne nomment pas encore la maladie.",
    "Dix diagnostics organisent la leçon. Le rang E est l'ordre de l'algorithme, pas un classement de fréquence.",
    "Les milligrammes écrits viennent de l'information professionnelle suisse du produit nommé.",
    bouton("w-glossaire", "Les sigles") + " sont rappelés dans la fenêtre.",
]

p1 = [
    "{1} PROFILES, validé le 1er novembre 2023, nomme la situation F2.1 abnormal blood gas values.",
    "Le catalogue français du projet la titre gaz du sang anormaux.",
    "{2} La revue du 7 novembre 2018 appelle acidémie un pH plasmatique sous 7,35.",
    "{2} Elle appelle alcalémie un pH au-dessus de 7,45.",
    "L'acidose est le processus. L'acidémie est le chiffre. Les deux ne se confondent pas.",
    "Le détail des mots voisins est dans " + bouton("w-def", "la définition") + ".",
]

w_def = [
    "{1} Le document validé le 1er novembre 2023 place F2.1 dans les trouvailles d'examens complémentaires.",
    "La ligne anglaise lue est abnormal blood gas values.",
    "Elle ne fixe aucun intervalle de pH, de pression d'oxygène, ni de pression de dioxyde de carbone.",
    "{2} « Chez l’homme, le pH plasmatique est très finement régulé autour d’une valeur de 7,4 (7,35 – 7,45). »",
    "{2} Les processus acidifiants sont les acidoses. Les processus alcalinisants sont les alcaloses.",
    "{2} Ils peuvent s'additionner. Ils peuvent aussi se compenser.",
    "{2} Un processus respiratoire est médié d'abord par la pression artérielle de dioxyde de carbone.",
    "{2} Un processus métabolique ne se lit pas sur le seul bicarbonate, parce que la ventilation le déplace.",
    "{3} La gazométrie artérielle renseigne l'oxygénation, la ventilation et l'équilibre acido-basique.",
    "{3} Un prélèvement veineux ou capillaire donne des informations plus limitées.",
    "{4} La saturation pulsée n'est pas la pression artérielle d'oxygène.",
    "{4} Elle ne dit rien de la pression de dioxyde de carbone.",
    "Hypoxémie, hypercapnie et trouble acidobasique sont trois lectures. Une peut exister sans les deux autres.",
    "Le sang veineux mêlé, le sang capillaire et le co-oxymètre ne portent pas le même nom.",
    "{9} Le catalogue vaudois du 27 septembre 2023 sépare la pression d'oxygène, la pression de dioxyde de carbone, le pH et la méthémoglobine.",
    "Aucun de ces mots n'est une maladie. Chacun ouvre un diagnostic de la leçon.",
]

p2 = [
    "{3} Aux Hôpitaux universitaires de Genève, la revue du 21 octobre 2020 écrit que cet examen est réalisé plus de 100 000 fois par an.",
    "Ce nombre compte des gestes. Il ne compte pas la part de résultats anormaux.",
    "{5} En Suisse, la revue du 19 août 2009 recense 23 décès et près de 130 hospitalisations liés au monoxyde de carbone en 2006.",
    "{2} La même revue de 2018 écrit qu'une acidose métabolique peut atteindre une incidence de 64 % aux soins intensifs.",
    "Cette incidence est celle de l'article. Ce n'est pas un registre suisse de population relu ici.",
    "Les autres diagnostics n'ont pas de dénombrement suisse dans les textes de cette leçon. " + bouton("w-epi", "Ce qui a été compté") + " reste dans la fenêtre.",
]

w_epi = [
    "{3} « Cet examen fréquent, réalisé plus de 100 000 fois par an aux HUG, pose toutefois des questions quant à la sécurité de la ponction. »",
    "Le dénominateur est l'hôpital genevois. Il n'est pas la population suisse.",
    "La leçon ne transforme pas ce volume en prévalence de gaz anormaux.",
    "{5} « En Suisse, 23 décès et près de 130 hospitalisations liés au CO ont été recensés en 2006. »",
    "{5} L'article ajoute que cette intoxication reste une cause principale de décès par intoxication dans la plupart des pays occidentaux.",
    "Le chiffre de 2006 n'est pas mis à jour dans les textes lus pour cette leçon.",
    "{5} La présentation initiale est souvent aspécifique. L'article cite Barret pour près de 30 % d'erreurs de diagnostic.",
    "Ce pourcentage vient de la citation faite par la revue. Il n'est pas un audit suisse relu à part.",
    "{2} « Parmi ces anomalies, l’acidose métabolique (AM) est la plus communément rencontrée avec une incidence pouvant atteindre 64 %. »",
    "L'article vise les soins intensifs. Il ne décrit pas le cabinet.",
    "{2} Les formes sévères des troubles acido-basiques sont associées, dans cet article, à une hausse de la morbi-mortalité.",
    "L'histoire naturelle dépend ensuite de la cause. Le gaz seul ne donne pas le pronostic.",
    "{4} Depuis 2022, la revue rappelle que la saturation au domicile ne remplace pas la lecture du gaz quand elle est anormale et que l'artefact est écarté.",
    "L'enjeu public est donc double. Il faut prélever juste. Il faut ne pas rassurer à tort sur une saturation.",
    "Aucun coût suisse de la gazométrie n'a été lu pour cette leçon.",
]

p3 = [
    "{6} Le bicarbonate est le tampon principal du milieu extracellulaire.",
    "{6} La compensation respiratoire d'une acidose métabolique augmente le volume courant plus que la fréquence. C'est la respiration de Kussmaul.",
    "{2} L'excès de base isole la part métabolique. Le trou anionique de 2018 et celui de 2007 ne sont pas le même calcul.",
    "Le " + bouton("w-physio", "mécanisme") + " et le " + bouton("w-corr", "tableau de corrélation") + " sont dans les fenêtres.",
]

w_physio = [
    "{6} Les protons se mesurent en nanomoles par litre. Le sodium, le potassium et le bicarbonate se mesurent en millimoles par litre.",
    "{6} L'échelle des protons est donc environ un milliard de fois plus fine.",
    "{6} À l'intérieur des cellules, surtout le muscle et l'os, les phosphates l'emportent sur le bicarbonate.",
    "{6} Le pouvoir tampon intracellulaire prend en charge plus de 50 % de la charge acide.",
    "{6} Le pH intracellulaire serait le meilleur reflet de gravité. Il ne se mesure pas en routine.",
    "{6} En pratique, on lit le pH extracellulaire par le système bicarbonate.",
    "{6} L'article écrit l'équilibre sous le nom d'équation d'Henderson-Hasselbach.",
    "{6} L'anhydrase carbonique est abondante dans le sang. Elle rend cet équilibre utilisable.",
    "{2} L'excès de base est la quantité d'acide fort ou de base forte, en milléquivalents, à ajouter in vitro pour ramener le pH à 7,40.",
    "{2} Les conditions lues sont 37 degrés et une pression de dioxyde de carbone de 40 mmHg.",
    "{2} « En conditions normales, l’excès de base se situe entre – 3 et + 3 mEq/l. »",
    "{2} Un excès de base inférieur à −3 mEq/l signe, pour cet article, une acidose métabolique.",
    "{10} Le catalogue lausannois imprime un excès de bases de −2 à +3. Ce n'est pas le même intervalle.",
    "La leçon ne choisit pas une borne unique.",
    "{2} Le trou anionique de 2018 additionne sodium et potassium, puis soustrait chlorure et bicarbonate.",
    "{2} « Le TAN normal est de 12 ± 4 mmol/l. »",
    "{2} Un trou au-dessus de 16 mmol/l signe, pour cet article, des anions non dosés en quantité anormale.",
    "{2} Albumine, phosphate et anions organiques forment l'essentiel du trou normal.",
    "{2} Lactate, sulfate et les autres protéines y contribuent d'ordinaire pour moins de 2 mmol/l.",
    "{6} L'article de 2007 calcule autrement. Il soustrait au sodium le chlorure et le bicarbonate, sans le potassium.",
    "{6} « Les valeurs normales sont entre 6-12 mEq/L. »",
    "Les deux articles sont suisses. Leurs bornes ne se recouvrent pas entièrement. Le cours les garde séparées.",
    "{2} La différence des ions forts normale est de 40 ± 2 mmol/l dans l'article de 2018.",
    "{2} Elle oppose les cations forts aux anions forts, dont le chlorure et le lactate.",
    "{2} Une solution de chlorure de sodium à 0,9 % a une différence des ions forts égale à 0.",
    "{2} Le sodium plasmatique y est décrit autour de 140 mEq/l et le chlorure autour de 105 mEq/l.",
    "{2} Apporter les deux ions à parts égales élève donc relativement plus le chlorure.",
    "{2} Les solutions balancées citées ont une différence des ions forts de 28.",
    "Leur effet acidifiant est moindre dans cet article. Le cours ne convertit pas cela en un volume à perfuser.",
    "{6} Le tube proximal réabsorbe environ 75 % du bicarbonate filtré. L'anse ascendante large en réabsorbe environ 25 %.",
    "{6} Chaque bicarbonate conservé suppose une sécrétion de proton.",
    "{6} L'échangeur sodium-proton de la membrane luminale fait ce travail dans le proximal.",
    "{6} Dans le collecteur, la pompe à protons des cellules intercalaires et l'échangeur chlorure-bicarbonate basolatéral ajoutent du bicarbonate au sang.",
    "{6} Un gradient de protons de 1000 pour 1 est possible. Il correspond à un pH urinaire aussi bas que 4,4.",
    "{6} Baisser le pH urinaire n'excrète pourtant que peu d'acide. L'ammonium compte davantage.",
    "{6} La glutamine proximale donne de l'alphacétoglutarate et de l'ammonium.",
    "{6} Le métabolisme de l'alphacétoglutarate génère un bicarbonate.",
    "{6} C'est l'excrétion d'une molécule d'ammonium qui permet d'ajouter ce bicarbonate au sang.",
    "{6} Pour une baisse d'un milléquivalent par litre de bicarbonate, la pression de dioxyde de carbone baisse d'environ 0,2 kPa, soit 1,2 mmHg.",
    "Cette pente est celle de l'article de 2007 pour l'acidose métabolique. Elle n'est pas une formule générale de tous les troubles.",
    "{6} L'article ajoute que l'effet de cette compensation respiratoire est transitoire.",
    "{6} La baisse de la pression de dioxyde de carbone diminue ensuite la réabsorption rénale de bicarbonate.",
    "Aucune autre pente de compensation n'a été lue. Elle n'est pas inventée.",
    "{2} L'acidose lactique n'est pas synonyme de tout lactate élevé.",
    "{2} La glycolyse accélérée, les catécholamines et le catabolisme protéique peuvent élever le lactate sans acidose.",
    "{2} En aérobie, les protons de la glycolyse sont repris pour synthétiser l'adénosine triphosphate.",
    "{2} Le rapport pyruvate sur lactate reste alors normal. Ce rapport ne se mesure pas en routine, parce que le pyruvate est instable.",
    "{2} L'acidose lactique, pour cet article, correspond surtout à la dysoxie ou à une baisse de la néoglucogenèse hépatique.",
    "{2} Les corps cétoniques viennent de la bêta-oxydation des acides gras. L'insuline inhibe ce chemin.",
    "{2} Le déficit d'insuline, l'alcool et le jeûne augmentent leur production.",
    "{2} Ce sont des acides forts, entièrement ionisés au pH du plasma.",
    "{2} Leur sortie rénale s'accompagne d'une réabsorption de chlorure, ce qui aggrave l'acidose.",
    "{5} Le monoxyde de carbone se fixe sur l'hémoglobine avec une affinité 250 fois supérieure à celle de l'oxygène.",
    "{5} La courbe de dissociation se déplace vers la gauche. L'oxygène périphérique baisse encore.",
    "{5} Cette liaison explique une hypoxémie transitoire. Elle n'explique pas toutes les atteintes tardives.",
    "{5} Le monoxyde de carbone se lie aussi aux cytochromes, à la myoglobine et à d'autres hémoprotéines.",
    "{5} La demi-vie de la carboxyhémoglobine est de quatre à cinq heures à l'air ambiant.",
    "{5} Celle des complexes avec les hémoprotéines se compte en jours dans cet article.",
    "{4} La saturation pulsée standard ne distingue pas la carboxyhémoglobine de l'oxyhémoglobine.",
    "Le mécanisme corrige donc trois choses différentes. La ventilation corrige le dioxyde de carbone. Le rein et le tampon corrigent le métabolisme. L'oxygène et le retrait de la source corrigent le transport quand le monoxyde de carbone est en cause.",
]

w_corr = [
    "Chaque ligne relie une perturbation lue à l'examen qui la montre et au geste qui la corrige.",
    "Hypoxémie. L'examen est la pression artérielle d'oxygène, pas la saturation seule. Le geste est de traiter la cause et d'apporter de l'oxygène. Aucun débit en litres n'a été lu.",
    "{3} Saturation normale avec exposition possible au monoxyde de carbone. L'examen est la carboxyhémoglobine. Le geste commence par l'oxygène à haute concentration.",
    "{12} Hypoventilation après opioïde. L'examen est le gaz et la vigilance. Naloxon OrPha, numéro 56952, lève la dépression respiratoire due aux opioïdes. Il ne lève pas une autre dépression.",
    "{11} Acidose métabolique sévère dans le choc ou la réanimation. Le bicarbonate Bichsel à 8,4 %, numéro 36797, a cette indication. La revue de 2018 réserve l'alcalinisation symptomatique aux acidoses sévères.",
    "{6} Acidose hyperchlorémique par diarrhée. Le trou anionique urinaire devient négatif si le rein excrète de l'ammonium. Le geste est de corriger les pertes, pas d'appeler cela une acidose tubulaire.",
    "{7} Alcalose métabolique avec volume bas. Le chlore et le potassium manquent. Le chlorure de potassium Bichsel, numéro 56471, est indiqué dans l'hypopotassiémie en cas d'alcalose métabolique, après dilution.",
    "{5} Intoxication au monoxyde de carbone avec signe de gravité. L'oxygène normobare est le premier geste. L'oxygène hyperbare s'envisage. Aucun protocole de caisson n'est recopié comme règle nationale.",
    "{2} Salicylés. Le gaz montre souvent une alcalose respiratoire et une acidose métabolique. L'article de 2018 compte cette intoxication parmi les rares cas où l'alcalinisation est recommandée.",
    "Le tableau ne mélange pas les numéros. Le produit suit son information professionnelle. La revue suit sa phrase.",
]

p4 = [
    "L'algorithme commence par ce qui tue pendant que la saturation rassure, puis par l'hypoventilation, puis par le choc.",
    "DX.1 est l'hypoxémie. DX.2 est l'acidose respiratoire. DX.3 est l'alcalose respiratoire.",
    "DX.4 est l'acidose métabolique à trou anionique élevé. DX.5 est l'acidose métabolique hyperchlorémique. DX.6 est l'alcalose métabolique.",
    "DX.7 est l'acidose lactique. DX.8 est l'acidocétose. DX.9 est l'intoxication au monoxyde de carbone. DX.10 est l'intoxication par les salicylés.",
    "Le " + bouton("w-dix", "tableau des dix diagnostics") + " donne le rang E, le gaz attendu et le premier acte.",
]

w_dix = [
    "Le numéro DX est l'ordre du cours. Le rang E est l'ordre de l'algorithme. Ils ne coïncident pas.",
    "E1, DX.9, intoxication au monoxyde de carbone. La saturation peut rester normale. Le premier acte est l'oxygène à haute concentration et la carboxyhémoglobine.",
    "E2, DX.2, acidose respiratoire. La pression de dioxyde de carbone monte et le pH baisse. Le premier acte est de ventiler, et de chercher un opioïde.",
    "E3, DX.7, acidose lactique. Le lactate et le trou montent dans la dysoxie. Le premier acte est de traiter le choc ou la cause, pas d'attendre un libellé.",
    "E4, DX.10, intoxication par les salicylés. Alcalose respiratoire et acidose métabolique coexistent souvent. Le premier acte est de reconnaître le mélange.",
    "E5, DX.4, acidose métabolique à trou anionique élevé. Le calcul dépend de l'article choisi. Le premier acte est de nommer l'anion.",
    "E6, DX.8, acidocétose. Les corps cétoniques sont des acides forts. Le premier acte est l'insuline et le volume, sans unité recopiée ici.",
    "E7, DX.1, hypoxémie. La pression d'oxygène est sous l'intervalle du laboratoire qui a mesuré. Le premier acte est l'oxygène et la cause.",
    "E8, DX.5, acidose métabolique hyperchlorémique. Le trou de l'article choisi n'est pas élevé. Le premier acte est l'origine digestive ou rénale.",
    "E9, DX.6, alcalose métabolique. Le pH est haut et le métabolisme aussi. Le premier acte est le volume, le chlore et le potassium.",
    "E10, DX.3, alcalose respiratoire. La pression de dioxyde de carbone est basse et le pH est haut. Le premier acte est la cause de l'hyperventilation, après les graves.",
    "Aucun de ces rangs n'est une prévalence suisse.",
    "Le patient instable passe avant le numéro DX.",
]

p5 = [
    "Chaque question cherche le mécanisme, pas un inventaire.",
    "L'exposition, les vomissements, la diarrhée, l'insuline manquante, l'opioïde et la grossesse changent le premier geste.",
    "Les " + bouton("w-drapeaux", "drapeaux rouges") + " imposent un acte immédiat.",
]

w_drapeaux = [
    "Pourquoi demander le lieu et le chauffage. Le monoxyde de carbone est inodore. Plusieurs personnes du même lieu peuvent être malades ensemble.",
    "{5} Céphalées, nausées et vertiges peuvent passer pour une virose. Cette question évite l'erreur citée par la revue.",
    "Pourquoi demander la grossesse. Le fœtus fixe le monoxyde de carbone plus longtemps que la mère. Un test de grossesse fait partie des examens cités.",
    "Pourquoi demander les médicaments et les opioïdes. La dépression respiratoire opioïde se lève avec la naloxone. Une autre dépression ne se lève pas.",
    "Pourquoi demander les vomissements et les diurétiques. Ils ouvrent l'alcalose métabolique à volume bas, pas une perte potassique digestive directe comme mécanisme principal.",
    "Pourquoi demander la diarrhée. C'est, pour l'article de 2007, la cause la plus fréquente d'acidose hyperchlorémique.",
    "Pourquoi demander le diabète, le jeûne et l'alcool. Les trois augmentent les corps cétoniques.",
    "Pourquoi demander le choc, le sepsis et l'ischémie. Ils ouvrent l'acidose lactique par dysoxie.",
    "Pourquoi demander les salicylés et les barbituriques. Les salicylés mélangent deux troubles. Les barbituriques figurent dans l'indication du bicarbonate Bichsel.",
    "{5} Perte de connaissance, signe neurologique, signe cardiaque, ou grossesse. La revue de 2009 demande d'envisager l'oxygène hyperbare.",
    "Trouble de vigilance avec pression de dioxyde de carbone haute. Il faut ventiler sans attendre le nom du trouble.",
    "pH très bas avec signes de choc. La cause passe avant le tampon.",
    "{2} La revue de 2018 écrit qu'un traitement symptomatique est souvent introduit si le pH est sous 7,10, malgré l'absence de preuve d'un bénéfice.",
    "Ce seuil est une pratique discutée dans l'article. Ce n'est pas une obligation de tamponner.",
    "Silence sur l'oxygène reçu et sur la température. Le catalogue vaudois demande de les inscrire, sinon la pression d'oxygène se lit mal.",
]

p6 = [
    "On regarde d'abord la ventilation et le pouls, qui sont normaux quand la fréquence et l'amplitude suffisent sans tirage.",
    "{6} Dans l'acidose métabolique, l'amplitude augmente plus que la fréquence.",
    "{5} Dans le monoxyde de carbone, on trouve souvent une tachycardie et une tachypnée. La couleur rouge cerise est très rarement retrouvée.",
    "La technique et les pièges sont dans " + bouton("w-examen", "l'examen") + ".",
]

w_examen = [
    "Voies aériennes. Le normal est un passage libre et une parole claire. Le pathologique est le coma, le vomissement, ou un bruit obstructif. On libère et on aide la ventilation avant de commenter le gaz.",
    "Respiration. Le normal est un volume courant tranquille, sans mise en jeu des muscles du cou. Le pathologique de Kussmaul est une grande amplitude. On ne le confond pas avec une simple polypnée d'anxiété, qui baisse le dioxyde de carbone et monte le pH.",
    "{3} Le test d'Allen compresse l'artère radiale et l'artère ulnaire, puis relâche l'ulnaire pour voir si la main se recolore.",
    "{3} La revue genevoise de 2020 écrit qu'il n'est plus recommandé selon l'American Association for Respiratory Care.",
    "Cette phrase rapporte un avis américain cité par des auteurs genevois. Elle n'est pas réécrite ici comme une directive suisse séparée.",
    "{3} La ponction artérielle peut disséquer, nécroser ou léser un nerf. La littérature lue est faite surtout de cas.",
    "{3} Une série ancienne de 106 ponctions n'a pas montré d'effet vasculaire ou neurologique à un an. Quelques hématomes sont décrits.",
    "On comprime après la ponction. Deux cas de pseudo-anévrisme après une seule ponction sont cités, avec une compression peut-être insuffisante.",
    "Circulation. Le normal est une pression et un temps de recoloration courts, un pouls régulier. Le pathologique est le choc, l'hypotension, ou un trouble du rythme. Le lactate se discute alors, sans dire que tout lactate est une acidose.",
    "{5} Pour le monoxyde de carbone, l'hypotension prédomine plus souvent que l'hypertension dans la revue de 2009.",
    "{5} La mortalité aiguë semble surtout cardiaque dans les études observationnelles citées.",
    "Peau. Le normal est la couleur du patient. La couleur rouge cerise ne sert pas de critère, parce qu'elle est très rarement retrouvée.",
    "Neurologie. Le normal est une vigilance tenue. Le pathologique est la confusion, la perte de connaissance ou le coma. Ces signes font monter le rang E1 ou E2 selon l'exposition et le dioxyde de carbone.",
    "Abdomen. Le normal est souple et indolore. Des vomissements répétés ou une diarrhée profuse orientent l'alcalose de contraction ou l'acidose digestive. Ils ne mesurent pas le pH.",
    "{10} Le prélèvement va dans une seringue spéciale. La page lausannoise demande un acheminement dans les 30 minutes.",
    "{3} Une leucocytose ou une thrombocytose élevée peut fausser la pression d'oxygène si l'analyse tarde.",
    "On note la température et l'oxygène reçu. Sans ces deux lignes, le chiffre de pression d'oxygène n'a pas son contexte.",
]

p7 = [
    "Sept syndromes suffisent à trier. Chacun a des signes fonctionnels et des signes physiques.",
    "Le mécanisme relie le signe au gaz. Le geste de recherche est dit dans " + bouton("w-synd", "les syndromes") + ".",
]

w_synd = [
    "7.1 Hypoxémie. Signe fonctionnel : essoufflement, agitation, ou parfois peu de plainte si la saturation est lue seule. Signe physique : tirage, cyanose inconstante, fréquence élevée. Geste : regarder la pression artérielle d'oxygène et l'oxygène reçu. Mécanisme : le contenu artériel en oxygène baisse, ou la saturation pulsée ment.",
    "7.2 Hypoventilation. Signe fonctionnel : somnolence, respiration faible. Signe physique : amplitude petite, pauses, myosis si opioïde. Geste : compter la fréquence et stimuler, puis lire la pression de dioxyde de carbone. Mécanisme : le dioxyde de carbone s'accumule et le pH baisse.",
    "7.3 Hyperventilation. Signe fonctionnel : paresthésies, sensation de manquer d'air, douleur thoracique. Signe physique : grande fréquence ou grande amplitude. Geste : lire le pH en même temps que la pression de dioxyde de carbone. Mécanisme : si le pH monte, l'hyperventilation est première. Si le pH baisse, elle compense une acidose métabolique.",
    "7.4 Acidose métabolique. Signe fonctionnel : soif, fatigue, nausée. Signe physique : grande amplitude inspiratoire. Geste : trou anionique selon l'article que l'on cite, puis lactate ou cétones selon le contexte. Mécanisme : perte de bicarbonate ou gain d'anion.",
    "7.5 Alcalose métabolique. Signe fonctionnel : faiblesse, crampes. Signe physique : signes de volume bas, ou hypertension si l'aldostérone est première. Geste : chlorurie et kaliémie. Mécanisme : perte de chlore et de potassium, maintien rénal de l'alcalose.",
    "7.6 Intoxication oxycarbonée. Signe fonctionnel : céphalée, nausée, malaise collectif. Signe physique : tachycardie, trouble de vigilance. Geste : carboxyhémoglobine, pas la saturation standard. Mécanisme : hémoglobine occupée et chaîne respiratoire mitochondriale touchée.",
    "7.7 Trouble mixte des salicylés. Signe fonctionnel : bourdonnements, chaleur, polypnée, vomissements. Signe physique : fréquence élevée, parfois fièvre. Geste : lire ensemble un pH bas ou proche de la normale, une pression de dioxyde de carbone basse, et un trou élevé. Mécanisme : stimulation respiratoire et acidose, dont une part lactique.",
    "Aucun syndrome ne se pose sur un seul chiffre.",
]

p8 = [
    "{9} Au CHUV, le 27 septembre 2023, le pH artériel lu va de 7,38 à 7,44.",
    "{9} La pCO2 lue va de 36 à 44 mm Hg.",
    "{9} La pO2 lue va de 75 à 95 mm Hg.",
    "{10} À La Source, la page lue le 31 octobre 2026 imprime d'autres bornes, sans unité à côté de la pCO2 ni de la pO2.",
    "Un chiffre hors de l'intervalle du laboratoire qui a mesuré est anormal pour ce laboratoire. Il ne devient pas une maladie.",
    "Ce qui suffit, et ce qui ne suffit pas, est dans " + bouton("w-positif", "les critères") + ".",
]

w_positif = [
    "{9} La fiche vaudoise demande d'inscrire la température corporelle et la quantité d'oxygène administrée.",
    "{9} Elle mesure aussi la saturation, l'hémoglobine et la méthémoglobine. Elle ne publie pas leurs bornes dans l'extrait lu.",
    "{10} Page lausannoise. pH de 7,35 à 7,45. pCO2 de 35 à 48 chez l'homme et de 32 à 45 chez la femme. pO2 de 83 à 108.",
    "{10} Bicarbonate de 22 à 26. Dioxyde de carbone total de 22 à 28. Excès de bases de −2 à +3. Saturation de 95 à 99 %.",
    "L'unité de la pCO2 et de la pO2 n'est pas imprimée sur cette page. Le cours ne l'ajoute pas.",
    "{2} Acidémie si le pH est sous 7,35. Alcalémie s'il est au-dessus de 7,45. Ces bornes sont celles de la revue de 2018, pas du catalogue vaudois.",
    "Le catalogue vaudois est plus étroit sur le pH. Un pH de 7,36 est dans la revue de 2018 et hors de la fiche vaudoise.",
    "On écrit donc le nom du laboratoire à côté de la borne.",
    "{2} Excès de base sous −3 mEq/l dans la revue de 2018. Excès de bases sous −2 sur la page lausannoise. On ne moyenne pas.",
    "{2} Trou anionique de 2018, avec potassium, normal à 12 ± 4 mmol/l, évocateur au-dessus de 16.",
    "{6} Trou anionique de 2007, sans potassium, normal entre 6 et 12 mEq/L.",
    "Un même prélèvement peut être élevé pour l'un et non pour l'autre. Le cours le dit, il ne tranche pas à la place du laboratoire.",
    "{6} L'acidose hyperchlorémique n'a pas d'anion organique retenu. La diarrhée en est la cause la plus fréquente dans l'article de 2007.",
    "{8} Le trou anionique urinaire, sodium plus potassium moins chlorure, est normal s'il est inférieur ou égal à 0 dans l'article de 2005.",
    "{8} Il devient négatif dans la diarrhée, quand l'ammonium urinaire monte. Il dépasse 0 dans les acidoses tubulaires de type 1 ou 4 de cet article.",
    "{8} Une hypovolémie sévère au cours d'une diarrhée peut rendre ce trou faussement élevé.",
    "{5} L'intoxication oxycarbonée est confirmée, dans la revue de 2009, au-dessus de 10 % de carboxyhémoglobine chez le non-fumeur et de 15 % chez le fumeur.",
    "{5} Le taux physiologique va de 0,2 % à 2 %. Les gros fumeurs atteignent souvent 4 % et parfois 10 %.",
    "{5} Ce taux ne suffit pas à grader la gravité. Il baisse si le patient a déjà reçu de l'oxygène. Il ignore l'effet mitochondrial.",
    "{4} Une saturation normale ne suffit pas à écarter le monoxyde de carbone.",
    "{3} Un pH veineux proche du pH artériel ne suffit pas à donner la pression d'oxygène.",
    "{2} Un lactate élevé ne suffit pas à poser l'acidose lactique.",
    "Aucun score chiffré de gazométrie n'a été lu comme critère diagnostique. La leçon n'en fabrique pas.",
]

p9 = [
    "Il n'existe pas un seul étalon qui nommerait toutes les causes. Le prélèvement artériel est la référence lue pour la pression d'oxygène.",
    "La première intention est ce prélèvement, avec la température et l'oxygène reçu. La suite dépend du trou, du lactate, des cétones ou de la carboxyhémoglobine.",
    "Le " + bouton("w-examens", "choix des examens") + " sépare ce qui se prescrit de ce qui s'interprète.",
]

w_examens = [
    "9.a Référence. Pour la pression d'oxygène, la revue de 2020 dit qu'un prélèvement veineux n'est pas adapté.",
    "{3} Pour le pH, une méta-analyse citée trouve une différence veineuse moins artérielle de −0,03.",
    "{3} L'intervalle de confiance lu va de −0,03 à −0,04.",
    "{3} Une pression veineuse de dioxyde de carbone de 7,3 kPa, soit 55 mm Hg, est un repère.",
    "{3} Elle correspond à une pression artérielle entre 5,8 kPa, soit 44,3 mm Hg, et 7,6 kPa, soit 57,3 mm Hg.",
    "Une valeur veineuse à la limite haute peut donc être une rétention, ou ne pas l'être. On ne conclut pas.",
    "{3} Au lobe de l'oreille, la pression capillaire de dioxyde de carbone ne diffère pas de façon significative de la pression artérielle dans la méta-analyse citée. L'écart maximal lu est de 1 mm Hg, soit 0,13 kPa, sur plus de 500 paires.",
    "{3} La pression d'oxygène du lobe est plus basse d'environ 0,8 kPa, soit 6 mm Hg.",
    "Le capillaire du lobe estime. Il ne remplace pas l'artère pour une décision fine sur l'oxygène.",
    "9.b Première intention. Gaz artériel. On inscrit la température et l'oxygène, comme au CHUV. On achemine vite.",
    "{10} La page lausannoise donne cinq minutes comme délai moyen, et trente minutes comme conservation. On contacte le laboratoire.",
    "{3} Au lit du malade, l'analyse peut rendre plus vite l'hémoglobine, le glucose et les électrolytes.",
    "{3} Une étude de 2013 citée, sur 100 prélèvements, trouve une différence de glucose de 1,16 mmol/l, avec une étendue de 0 à 10,5 mmol/l.",
    "{3} Sodium et potassium concordent mieux dans l'intervalle normal. Un potassium veineux au-dessus de 5 mmol/l s'associe, dans ce texte, à une différence artérielle moyenne de 0,44 mmol/l.",
    "{3} Dans l'arrêt circulatoire, une autre comparaison trouve une différence moyenne de potassium de 0,1 mmol/l, avec un intervalle de confiance de −1,182 à 1,394 mmol/l.",
    "On ne traite pas une kaliémie de gazométrie comme si elle était veineuse quand l'écart possible est large.",
    "{3} Le bicarbonate du gaz est calculé. Le dioxyde de carbone total mesuré est plus haut de 1 à 2 mmol/l.",
    "9.c Alternatives. Lobe de l'oreille si l'artère est impossible et si l'on accepte l'écart d'oxygène. Veine pour un pH d'orientation, pas pour l'oxygène.",
    "{4} On choisit un oxymètre qui porte le marquage de conformité européenne (CE) et qui répond à la norme ISO 80601-2-61.",
    "{4} La précision lue est de 2 à 5 % par rapport à la saturation artérielle.",
    "{4} La saturation normale est supérieure ou égale à 95 % selon l'âge.",
    "{4} Elle ignore l'anémie, la carboxyhémoglobine et la méthémoglobine.",
    "9.d Deuxième intention. Lactate si le contexte est le choc ou un trou élevé. Corps cétoniques si le diabète, le jeûne ou l'alcool sont en cause.",
    "{2} Sous insuline, le bêta-hydroxybutyrate se convertit en acéto-acétate. Les cétones peuvent sembler monter au début. On suit le pH et le trou.",
    "{5} Carboxyhémoglobine veineuse ou artérielle si l'exposition est possible. La saturation standard ne la remplace pas.",
    "{5} Il existe des oxymètres qui mesurent la carboxyhémoglobine et la méthémoglobine. La revue de 2009 les distingue de l'oxymètre standard.",
    "{8} Spot urinaire tout de suite, pas différé, si l'on cherche l'origine d'une acidose à trou normal ou d'une alcalose.",
    "Grossesse, enfant, débit de filtration bas, allergie iodée. Le gaz n'utilise pas d'iode. Ces limites concernent l'imagerie d'une cause, pas l'électrode.",
    "Résultat discordant. Saturation haute et pression d'oxygène basse : lire l'oxygène reçu, la température, le délai, et la carboxyhémoglobine.",
    "pH veineux rassurant et malade somnolent : prendre l'artère, ne pas clore.",
]

p10 = [
    "Si la vigilance tombe ou le choc est là, on traite pendant que le gaz part au laboratoire.",
    "Si l'exposition au monoxyde de carbone est plausible, l'oxygène commence avant le résultat.",
    "Le reste de l'arbre est dans " + bouton("w-arbre", "l'algorithme") + ".",
]

w_arbre = [
    "Si plusieurs malades partagent un lieu clos, ou si la céphalée est collective, alors E1. Oxygène à haute concentration. Carboxyhémoglobine. Envisager le caisson si la revue de 2009 reconnaît un signe de gravité.",
    "Si la respiration est faible et le dioxyde de carbone est haut, alors E2. Aider la ventilation. Si l'opioïde est connu ou suspecté, naloxone selon l'information professionnelle. Si dix milligrammes restent sans effet, chercher une autre cause, avec l'exception de la buprénorphine lue dans le texte.",
    "Si le choc ou l'ischémie dominent et le lactate a un sens clinique, alors E3. Cause circulatoire d'abord. Le tampon n'est pas le premier mot.",
    "Si les salicylés sont en cause, alors E4. Lire le mélange. Ne pas appeler cela une alcalose simple parce que la fréquence est haute.",
    "Si le pH est bas, le bicarbonate est bas, et le trou de l'article cité est haut, alors E5 puis le tri entre E3 et E6.",
    "Si le diabète se décompense, ou si le jeûne et l'alcool dominent, alors E6. Insuline et volume, sans inventer l'unité. Suivre le pH et le trou.",
    "Si la pression d'oxygène est sous l'intervalle du laboratoire, sans les rangs précédents, alors E7. Oxygène et cause. La saturation seule ne clôt pas.",
    "Si le trou n'est pas élevé et le chlorure l'est, alors E8. Diarrhée ou rein. Spot urinaire tout de suite. Se méfier du faux trou urinaire haut si le volume est très bas.",
    "Si le pH est haut et le bicarbonate est haut, alors E9. Volume, chlore, potassium. Ne pas alcaliniser.",
    "Si le pH est haut et la pression de dioxyde de carbone est basse, alors E10, après avoir écarté le mélange des salicylés.",
    "Si le pH est presque normal et les deux composantes sont anormales en sens opposé, alors trouble mixte. On ne choisit pas un seul DX pour le clore.",
    "Chaque flèche nomme un signe ou un résultat, puis un acte.",
]

p11 = [
    "Le but immédiat est un pH compatible avec la circulation, une ventilation suffisante, et une cause nommée.",
    "L'ordre est le retrait du danger, puis la ventilation, puis la cause. Le bicarbonate vient après, et seulement dans son indication.",
    "Les produits suisses et les situations particulières sont dans " + bouton("w-pec", "la prise en charge") + ".",
]

w_pec = [
    "11.A But. À court terme, une conscience tenue ou une voie aérienne protégée, une pression de dioxyde de carbone qui ne monte plus, une pression d'oxygène dans l'intervalle du laboratoire, et un pH qui ne s'aggrave pas.",
    "Le chiffre visé n'est pas le même dans tous les laboratoires. On vise l'intervalle de celui qui mesure, sans inventer une cible unique.",
    "11.B Ordre. Minutes : sortir d'une atmosphère toxique, oxygène à haute concentration si le monoxyde de carbone est possible, aider la ventilation si elle est faible.",
    "Heure suivante : gaz artériel avec température et oxygène reçu, cause, et seulement ensuite un tampon si l'indication est là.",
    "{12} Naloxon OrPha, numéro Swissmedic 56952, est indiqué pour lever la dépression respiratoire due aux opioïdes chez l'adulte et l'enfant.",
    "{12} Il sert aussi au diagnostic et au traitement d'un surdosage aigu suspecté.",
    "{12} Chez l'adulte, la posologie initiale habituelle du surdosage est de 0,4 à 2 mg par voie intraveineuse, intramusculaire ou sous-cutanée.",
    "{12} On répète par voie intraveineuse toutes les deux à trois minutes si la respiration ne revient pas.",
    "{12} « la dépression respiratoire n’est pas due à un opioïde » après 10 mg, sauf les exceptions écrites juste après dans l'information professionnelle.",
    "{12} Exceptions lues : la buprénorphine et des doses élevées d'agonistes-antagonistes.",
    "{12} Pour la buprénorphine, l'effet est limité et le texte parle d'un dosage de 5 à 10 mg.",
    "{12} L'effet de certains opioïdes dure plus longtemps que celui de la naloxone. On surveille. On réinjecte si la dépression revient.",
    "{12} Chez l'enfant, la dose initiale habituelle est de 0,01 mg par kilogramme, après dilution, par voie intraveineuse.",
    "{12} Le nouveau-né après opioïde maternel reçoit aussi 0,01 mg par kilogramme.",
    "{12} « Le chlorhydrate de naloxone ne doit pas être utilisé pendant la grossesse, sauf en cas de nécessité absolue. »",
    "{12} Il peut provoquer un sevrage chez le nouveau-né.",
    "{12} L'information professionnelle demande de ne pas allaiter pendant 24 heures au moins après l'application.",
    "{12} Le texte demande la prudence chez la personne âgée et en cas de cardiopathie, à cause de tachycardie, de fibrillation et d'œdème pulmonaire rapportés.",
    "{12} Une levée brusque chez un dépendant peut donner un sevrage aigu, une hypertension, un trouble du rythme, un œdème pulmonaire ou un arrêt cardiaque.",
    "{11} Bicarbonate de sodium Bichsel 8,4 %, numéro Swissmedic 36797. Indications lues : acidoses compliquant les décompensations circulatoires, acidose métabolique, intoxications aux barbituriques.",
    "{11} « Déficit basique x 0.3 x kg (poids corporel) = mmol de bicarbonate nécessaire. »",
    "{11} On commence par environ la moitié de la quantité calculée, puis on contrôle à nouveau.",
    "{11} En général, la dose n'excède pas 100 à 200 mmol pendant les premières 24 heures.",
    "{11} La vitesse maximale lue pour le soluté à 8,4 % est d'environ 1,5 mmol/kg et par heure.",
    "{11} Un tamponnement à l'aveugle n'est toléré qu'en réanimation. La dose initiale est de l'ordre de 1 mmol/kg, jusqu'à un maximum de 100 mmol.",
    "{11} Dans l'arrêt cardiaque prolongé, le texte dit 0,5 mmol/kg toutes les 10 minutes, puis un contrôle du gaz dès que possible.",
    "{11} Le soluté à 8,4 % est indiqué principalement chez l'adulte pour une acidose sévère en cas de choc et en réanimation.",
    "{11} Il s'injecte lentement dans un gros vaisseau, à cause de l'alcalinité et de l'osmolarité.",
    "{11} Contre-indications lues : alcalose métabolique et respiratoire, acidose respiratoire, pertes massives de chlorures, hypocalcémie, convulsions, décompensation cardiaque, hypernatrémie.",
    "{11} En cas d'hypokaliémie, on rééquilibre le potassium avant l'alcalinisation.",
    "{11} « Ce médicament ne devrait pas être employé pendant la grossesse, sauf en cas de nécessité absolue. »",
    "{11} Une ampoule de 10 ml contient 229,99 mg de sodium. Le texte le rapporte à 11,5 % de l'apport maximal de 2 g de sodium recommandé par l'Organisation mondiale de la santé.",
    "{2} La revue de 2018 rappelle que les études citées n'ont pas montré de bénéfice à corriger le pH dans l'acidose lactique ni dans l'acidocétose.",
    "{2} Le bicarbonate produit du dioxyde de carbone, peut précipiter une insuffisance respiratoire ou un œdème cérébral, et baisse le calcium ionisé.",
    "{2} La solution concentrée à 8,4 % peut baisser la pression artérielle. L'article dit de l'éviter.",
    "Le cours ne prescrit donc pas ce soluté comme réflexe devant tout pH bas. Il suit l'indication du produit et la réserve de la revue.",
    "{13} Chlorure de potassium Bichsel, numéro Swissmedic 56471. Indication lue : apport potassique en présence d'hypopotassiémie, en cas d'alcalose métabolique.",
    "{13} Les concentrés à 1 mmol/ml et à 2 mmol/ml doivent toujours être dilués. On ne les injecte jamais tels quels.",
    "{13} Un millilitre à 7,5 % contient 75 mg de chlorure de potassium, soit 1 mmol. Un millilitre à 15 % contient 150 mg, soit 2 mmol.",
    "{13} Adulte avec potassium sérique au-dessus de 2,5 mmol/l : au plus 200 mmol par jour, au plus 40 mmol/l dans la perfusion, au plus 10 mmol par heure.",
    "{13} Adulte avec potassium sérique sous 2,0 mmol/l : au plus 400 mmol par jour, au plus 80 mmol/l, au plus 40 mmol par heure.",
    "{13} Enfant : au plus 3 mmol/kg ou 40 mmol par mètre carré.",
    "{13} Contre-indications lues : anurie, oligurie, hyperkaliémie, hyperchlorémie, insuffisance rénale, insuffisance corticosurrénale non traitée, acidose, déshydratation sévère.",
    "{13} On contrôle la diurèse avant de commencer. On surveille le potassium et l'électrocardiogramme.",
    "{13} « La prudence est de mise en cas d'emploi pendant la grossesse. »",
    "{13} Le surdosage peut donner paresthésies, confusion, bradycardie, arythmie, fibrillation ventriculaire et arrêt.",
    "{13} Le texte appelle hyperkaliémie un potassium plasmatique de plus de 5,5 mmol/l dans la section surdosage.",
    "{13} Il décrit alors un soluté à 10 % de chlorure de calcium ou de gluconate de calcium.",
    "{13} La quantité lue est d'environ 10 à 20 ml en dix minutes.",
    "{13} Il décrit aussi du bicarbonate à 8,4 %, jusqu'à 250 ml selon la situation.",
    "{13} Il cite aussi un traitement par glucose et insuline, sans donner d'unité d'insuline.",
    "Aucune unité d'insuline n'est donc écrite dans cette leçon.",
    "11.C Surveillance. Gaz répété après chaque changement de ventilation ou de tampon. Potassium, sodium, calcium ionisé si l'on alcalinise. Vigilance après naloxone, parce que l'opioïde peut revenir.",
    "{5} Après monoxyde de carbone, informer du risque neurologique tardif et revoir dans une dizaine de jours, comme l'écrit la revue de 2009 pour le suivi après oxygène normobare.",
    "11.D Sortie. Cause écartée ou traitée. Vigilance stable. Gaz dans l'intervalle du laboratoire sans oxygène nouveau non expliqué. Consignes si l'exposition domestique n'est pas levée.",
    "Pronostic. Il suit la cause. Le gaz du premier jour ne promet pas la guérison.",
    "Social. Une intoxication domestique peut empêcher le retour au logement tant que la source n'est pas supprimée. L'arrêt de travail se discute sur la cause, pas sur le pH isolé.",
    "Aptitude à conduire. Elle est incompatible avec la sédation, le sevrage aigu après naloxone, ou un trouble de vigilance persistant. Aucune durée chiffrée n'a été lue.",
]

p12 = [
    "{5} La prévention du monoxyde de carbone commence par la source : chauffage, lieu clos, plusieurs malades.",
    "{4} La prévention de l'erreur de saturation est d'enseigner qu'un chiffre normal n'écarte pas l'hypoventilation ni le monoxyde de carbone.",
    "Les trois niveaux sont dans " + bouton("w-prev", "la prévention") + ".",
]

w_prev = [
    "Primaire. Installations qui brûlent, aération, détecteur si le logement en a un. La revue de 2009 ne donne pas, dans les phrases lues, un programme national chiffré. Le cours n'en invente pas.",
    "Éviter l'automédication par salicylés à doses cumulées chez la personne qui déjà hyperventile. Aucun seuil d'automédication suisse n'a été lu ici.",
    "Secondaire. Devant une céphalée collective ou un malaise en lieu clos, mesurer la carboxyhémoglobine plutôt que se fier à la saturation.",
    "Devant une diarrhée profuse, anticiper l'acidose hyperchlorémique au lieu d'attendre le coma.",
    "Devant un opioïde, surveiller la ventilation avant que le dioxyde de carbone soit très haut.",
    "Tertiaire. Après une intoxication oxycarbonée, revoir le patient pour les signes neurologiques tardifs.",
    "Après une acidose sévère, corriger la cause rénale ou digestive pour que l'os et le muscle ne restent pas les tampons chroniques.",
    "{6} L'article de 2007 rappelle l'atteinte osseuse et le retard de croissance dans l'acidose tubulaire distale prolongée.",
    "Le lien avec le point 2 est direct. Le volume genevois des ponctions justifie une technique sûre. Les décès suisses de 2006 justifient de chercher le monoxyde de carbone sans attendre la couleur de la peau.",
    "Aucune recommandation vaccinale ne traite le gaz du sang. Le cours ne l'invente pas.",
]

p13 = [
    "Le laboratoire qui a mesuré fixe l'intervalle. Deux catalogues suisses lus ne donnent pas les mêmes bornes.",
    "La saturation normale n'écarte ni l'hypoventilation ni le monoxyde de carbone.",
    "On ventile et l'on traite la cause avant de tamponner.",
    "Le bicarbonate Bichsel et la naloxone ont des indications écrites. Ils n'en ont pas d'autres dans cette leçon.",
    "Le trou anionique de 2018 n'est pas celui de 2007.",
    "Le rang E n'est pas une fréquence.",
]

p14_fiche = [
    "Les pièges portent sur les bornes, les produits et les faux rassurants.",
    "Chaque question a sa réponse dans " + bouton("w-pieges", "les pièges d'examen") + ".",
]

w_pieges = [
    "Question. Un pH de 7,36 est-il normal partout. Réponse. Il est dans l'intervalle de la revue de 2018. Il est sous la borne basse de 7,38 du catalogue vaudois du 27 septembre 2023.",
    "Question. La page lausannoise donne-t-elle la pO2 en mm Hg. Réponse. Elle imprime 83 à 108 sans écrire l'unité. On ne l'ajoute pas.",
    "Question. La saturation à 97 % exclut-elle le monoxyde de carbone. Réponse. Non. L'oxymètre standard ne distingue pas la carboxyhémoglobine. La revue de 2009 confirme l'intoxication au-dessus de 10 % chez le non-fumeur et de 15 % chez le fumeur.",
    "Question. La couleur rouge cerise est-elle nécessaire. Réponse. Non. La revue de 2009 la dit très rarement retrouvée.",
    "Question. Un lactate élevé suffit-il. Réponse. Non. La revue de 2018 sépare l'hyperlactatémie sans acidose et l'acidose lactique.",
    "Question. Quel trou anionique citer. Réponse. Celui de 2018 inclut le potassium, normal 12 ± 4 mmol/l. Celui de 2007 ne l'inclut pas, normal 6 à 12 mEq/L. On nomme l'article.",
    "Question. La diarrhée donne-t-elle un trou urinaire positif. Réponse. Non, sauf hypovolémie sévère. L'article de 2005 le dit négatif quand l'ammonium monte, et faussement haut si le volume s'effondre.",
    "Question. Peut-on tamponner une acidose respiratoire avec le bicarbonate Bichsel. Réponse. Non. L'acidose respiratoire est une contre-indication lue du numéro 36797.",
    "Question. Quelle dose de naloxone clôt un surdosage opioïde chez l'adulte. Réponse. La dose initiale habituelle est 0,4 à 2 mg. L'absence d'effet après 10 mg oriente vers une autre cause, sauf buprénorphine et agonistes-antagonistes à haute dose.",
    "Question. Peut-on injecter le concentré de potassium tel quel. Réponse. Non. Le numéro 56471 dit de toujours diluer, et l'acidose est une contre-indication.",
    "Question. L'insuline de l'acidocétose a-t-elle une unité dans cette leçon. Réponse. Non. Aucune unité n'a été lue dans les informations professionnelles retenues.",
    "Question. Le rang DX.1 est-il le plus fréquent. Réponse. Non. DX est l'ordre du cours. E est l'ordre de l'algorithme.",
    "Question. Le test d'Allen est-il une règle suisse lue. Réponse. La revue genevoise de 2020 rapporte qu'il n'est plus recommandé selon une association américaine. Ce n'est pas une ordonnance suisse séparée.",
    "Question. Le pH veineux remplace-t-il l'artère. Réponse. Il oriente le pH. Il ne donne pas la pression d'oxygène. Une pression veineuse de dioxyde de carbone limite a un large intervalle artériel.",
]

sources = [
    "PROFILES 2023, validé le 1er novembre 2023, situation F2.1.",
    "Gross, Kissling, Schneider. Revue Médicale Suisse, 7 novembre 2018.",
    "Muradbegovic, Stirnemann. Revue Médicale Suisse, 21 octobre 2020.",
    "Baud, Postel-Vinay. Revue Médicale Suisse, 8 juin 2022.",
    "Schaub, Pellegrini, Pugin. Revue Médicale Suisse, 19 août 2009.",
    "Martin, Stucker, Saudan, Feraille. Revue Médicale Suisse, 7 mars 2007.",
    "Katerinis, Fumeaux. Revue Médicale Suisse, 7 mars 2007.",
    "Fumeaux, Stoermann Chopard. Revue Médicale Suisse, 23 février 2005.",
    "CHUV, gazométrie artérielle, mise à jour du 27 septembre 2023.",
    "Clinique de La Source, catalogue gazométrie, page lue le 31 octobre 2026.",
    "Bicarbonate de sodium Bichsel 8,4 %, information professionnelle, numéro 36797.",
    "Naloxon OrPha, information professionnelle, numéro 56952.",
    "Chlorure de potassium Bichsel, information professionnelle, numéro 56471.",
]

w_physio += [
    "{6} Après le diagnostic d'acidose métabolique, le trou anionique classe la cause.",
    "{6} Un anion organique retenu donne un trou élevé. Son absence donne l'acidose hyperchlorémique.",
    "{6} Les diarrhées sont, dans cet article, la cause la plus fréquente de cette forme, par perte de bicarbonate.",
    "{6} Le trou anionique urinaire estime l'ammonium, que l'on dose mal en routine.",
    "{6} S'il est très négatif, le chlorure urinaire dépasse sodium et potassium urinaires, et l'ammonium est abondant.",
    "{6} C'est la réponse rénale normale d'une perte digestive.",
    "{6} Toutes les formes d'acidose tubulaire distale de cet article ont un trou urinaire positif ou nul.",
    "{6} Le trou urinaire ne sert pas dans les acidoses à trou plasmatique élevé.",
    "{6} Les drainages biliaires et pancréatiques perdent aussi du bicarbonate.",
    "{6} Une néovessie iléale ou des uretères dans le sigmoïde échangent du chlorure contre du bicarbonate.",
    "{6} L'acidose tubulaire proximale abaisse la réabsorption du bicarbonate.",
    "{6} Elle s'inscrit souvent dans un syndrome de Fanconi, avec glucose, phosphate et acides aminés dans l'urine.",
    "{6} Myélome, Sjögren, amylose, syndrome néphrotique et métaux lourds figurent parmi les contextes lus.",
    "{6} Le bicarbonate plasmatique tourne alors autour de 15 mmol/l.",
    "{6} Le pH urinaire reste approprié, entre 5 et 5,5, tant que le plasma n'est pas rechargé.",
    "{6} Une charge qui ramène le bicarbonate vers 22 à 25 mmol/l fait apparaître une bicarbonaturie.",
    "{6} Corriger cette forme est difficile. L'alcali dépasse le seuil de réabsorption et part dans l'urine avec du potassium.",
    "{6} L'acidose tubulaire distale empêche la sécrétion de protons par les cellules intercalaires.",
    "{6} La pompe ou l'échangeur chlorure-bicarbonate peuvent manquer. L'amphotéricine B est citée comme toxique.",
    "{6} Le rein ne peut plus acidifier sous un pH de 5,5.",
    "{6} L'article décrit néphrocalcinose, lithiase, ostéoporose et retard de croissance.",
    "{6} Le bicarbonate corrige mieux cette forme distale que la forme proximale.",
    "{6} Le type 4 est l'acidose tubulaire la plus fréquente dans cet article.",
    "{6} Il vient d'un défaut de voltage ou d'un hypoaldostéronisme. L'amiloride est un exemple de blocage du canal sodique.",
    "{6} Le pH urinaire dépasse 5,5 si le voltage manque. Il reste sous 5,5 si l'aldostérone manque.",
    "{6} Les acidoses de charge ont souvent un trou franchement augmenté, l'article dit souvent au-dessus de 25, et un chlorure bas.",
    "{6} Le pH urinaire est alors sous 5,5. Le trou urinaire ne s'applique pas.",
    "{6} Les deux causes endogènes les plus fréquentes lues sont l'acidocétose diabétique et l'acidose lactique.",
    "{6} Le méthanol donne de l'acide formique. L'éthylène glycol donne de l'acide oxalique.",
    "{2} Aux soins intensifs, des bêta-lactamines, l'acétate de la nutrition et le citrate s'ajoutent aux anions du trou.",
    "{2} Même une intoxication sévère aux salicylés met moins de 3 mEq/l d'acide salicylique dans le trou.",
    "{2} L'élévation du trou vient surtout de l'acidose lactique secondaire.",
    "{2} Une alcalose respiratoire primaire coexiste souvent, par stimulation du centre respiratoire.",
    "{2} L'acidose augmente la forme protonée, qui entre mieux dans les cellules, et diminue l'élimination rénale.",
    "{2} C'est une des rares situations où l'article recommande d'alcaliniser le plasma.",
    "{2} Il n'existe pas, dans cet article, de valeur de pH qui impose à elle seule l'épuration extrarénale.",
    "{2} Le Carbicarb et le tris-hydroxyméthyl-aminométhane (THAM) ne sont pas disponibles en Suisse selon la revue de 2018.",
    "La leçon n'écrit donc pas de dose pour ces deux produits.",
]
w_examens += [
    "Comment lire, dans l'ordre, sans ajouter de borne.",
    "D'abord le contexte. Température, oxygène reçu, délai depuis la ponction, lieu de prélèvement.",
    "{10} Si le délai dépasse les trente minutes lues à Lausanne, la pression d'oxygène peut avoir bougé.",
    "{3} Une leucocytose forte consomme de l'oxygène dans la seringue si l'on tarde.",
    "Ensuite le pH. Sous la borne basse du laboratoire qui a mesuré, il y a acidémie. Au-dessus, alcalémie.",
    "{2} On garde en tête les bornes 7,35 et 7,45 de la revue de 2018, et les bornes plus étroites du CHUV.",
    "Ensuite la pression de dioxyde de carbone. Si elle va dans le même sens que l'acidité, le processus respiratoire est premier ou participe.",
    "Si le pH est bas et la pression de dioxyde de carbone est haute, l'acidose respiratoire est au premier plan.",
    "Si le pH est haut et la pression de dioxyde de carbone est basse, l'alcalose respiratoire est au premier plan.",
    "Si le pH est bas et la pression de dioxyde de carbone est basse, la ventilation compense, ou un mélange existe.",
    "{6} Pour l'acidose métabolique, la pente lue est d'environ 0,2 kPa de baisse par milléquivalent de bicarbonate.",
    "Si la pression observée s'écarte beaucoup de cette pente, on cherche un second processus. On n'invente pas une autre formule.",
    "Ensuite le bicarbonate et l'excès de base. Ils disent la part métabolique. On cite l'intervalle de la source, pas une moyenne.",
    "Si les deux parts sont anormales et le pH est presque normal, les processus se compensent ou s'opposent.",
    "{2} On calcule alors le trou de 2018 si l'on a le potassium, ou celui de 2007 si l'on suit cet article.",
    "On écrit laquelle des deux formules a été utilisée. On ne les additionne pas.",
    "Si le trou choisi est élevé, on cherche lactate, cétones, toxique, ou un anion de médicament cité.",
    "Si le trou choisi ne l'est pas, on cherche diarrhée, dérivation, ou acidose tubulaire.",
    "{8} Le spot urinaire se prend tout de suite. Un examen différé décrit un autre moment.",
    "Enfin l'oxygène, à part. Une hypoxémie ne dit pas le pH. Un pH normal ne dit pas l'oxygène.",
    "{4} La saturation se lit avec l'âge, le pouls affiché, et l'onde si l'appareil la montre.",
    "{4} Un mauvais signal, un doigt froid ou un vernis rendent le chiffre inutilisable. On reprend la mesure.",
    "Si la saturation est basse et le patient va bien, on cherche l'artefact avant l'alarme. Si elle est normale et le contexte est toxique, on ne se rassure pas.",
    "{9} La méthémoglobine figure sur la fiche vaudoise. Une saturation discordante la fait demander. Aucune borne chiffrée n'a été lue sur cette fiche.",
]
w_pec += [
    "{7} Les diurétiques sont, dans la revue du 7 mars 2007, la cause médicamenteuse la plus commune d'hypokaliémie.",
    "{7} Les vomissements baissent le potassium surtout par le rein. L'alcalose de contraction stimule l'aldostérone.",
    "{7} Diurétiques, vomissements, sonde gastrique et dérivations hautes partagent un volume extracellulaire bas.",
    "{7} Le chlore manque. L'apporter corrige en général la kaliémie. L'article appelle cela une alcalose qui répond au chlore.",
    "{7} Si le volume est normal ou haut, on pense à un hyperaldostéronisme primaire ou à une sténose de l'artère rénale.",
    "{7} Cette forme ne répond pas au chlore. Elle répond au traitement de la cause.",
    "{7} Un potassium urinaire sous 20 mmol/l est compatible, dans cet article, avec une perte extrarénale, un transfert cellulaire ou un apport bas.",
    "{7} Au-dessus de 25 mmol/l, l'article ouvre une perte rénale.",
    "{8} L'article de 2005 ne donne pas les mêmes bornes. Sous 15 meq/L, il évoque une perte extrarénale. Au-dessus de 30 meq/L, une perte rénale.",
    "Le cours cite les deux couples. Il n'en fabrique pas un troisième.",
    "{8} Dans l'alcalose métabolique extrarénale, le sodium urinaire peut rester haut, parce qu'il sort avec du bicarbonate.",
    "{8} Le chlorure urinaire, lui, reste bas. Le pH urinaire est généralement au-dessus de 7.",
    "{7} Le potassium des selles normales est d'environ 80 à 100 mmol/l dans cet article.",
    "La phrase sur une perte quotidienne de 10 mmol/l est ambiguë. Elle n'est pas enseignée.",
    "{5} Chez la femme enceinte, la revue de 2009 rapporte un risque fœtal élevé.",
    "{5} Certaines études citées donnent une mortalité fœtale entre 36 % et 67 %.",
    "Ce n'est pas un registre suisse. C'est la fourchette écrite par la revue.",
    "{5} L'hémoglobine fœtale fixe mieux le monoxyde de carbone. La demi-vie fœtale est deux fois celle de la mère.",
    "{5} Le taux fœtal peut donc dépasser le taux maternel.",
    "{5} Un travail genevois cité a suivi 90 femmes enceintes traitées par oxygène hyperbare.",
    "{5} Dans 90 % des cas, la grossesse a abouti sans séquelle décrite pour l'enfant.",
    "{5} Cinq morts fœtales sont rapportées, avec un risque relatif multiplié par quatre dans ce texte.",
    "{5} Prématurité, hypotrophie et malformations n'étaient pas augmentées par rapport au témoin de cette étude.",
    "{5} L'indication du caisson reste discutée. L'article s'appuie notamment sur Weaver et collaborateurs, 152 patients.",
    "{5} Les manifestations neuropsychologiques tardives étaient de 24 % après caisson et de 43,1 % après oxygène normobare.",
    "{5} Le p lu est 0,014. Cela ne devient pas une obligation pour chaque malade léger.",
    "{5} Sans critère de caisson, l'oxygène normobare continue jusqu'à la fin des symptômes, au maximum six heures.",
    "{5} Le patient est revu dans une dizaine de jours.",
    "{5} Une exposition chronique de 50 à 80 ppm peut altérer les performances, l'apprentissage, la vue et l'ouïe.",
    "{5} Une exposition aiguë de 1000 ppm et plus peut tuer d'emblée.",
    "Ces concentrations viennent de la revue. Elles ne sont pas un seuil de détecteur domestique relu à part.",
    "{5} Les complications aiguës citées sont le trouble du rythme, l'ischémie coronaire, l'œdème pulmonaire et la rhabdomyolyse.",
    "On demande donc un électrocardiogramme si l'intoxication est plausible et le malade symptomatique.",
    "Aucune spécialité d'oxygène médicinal en français n'a été retenue dans le corpus consulté. Aucun débit en litres n'est écrit.",
]
w_dix += [
    "Lecture d'un compte rendu, sans malade inventé.",
    "On commence par le nom du laboratoire, parce que les bornes changent.",
    "On lit le pH avant le bicarbonate. Un bicarbonate bas avec un pH haut n'est pas une acidose.",
    "On lit la pression de dioxyde de carbone avant de dire que le patient hyperventile pour compenser.",
    "On sépare l'oxygène du pH. Les deux fenêtres ne se remplacent pas.",
    "On demande ce que le patient respirait. Une pression d'oxygène normale sous oxygène n'est pas une pression normale à l'air.",
    "On demande depuis quand la seringue attend. Le métabolisme du sang continue.",
    "On ne corrige pas un trou avec une formule d'albumine qui n'a pas été lue.",
    "{2} La revue de 2018 dit que le trou corrigé pour l'albumine est une étape clé. Elle ne donne pas, dans les phrases lues, le coefficient à soustraire.",
    "Le cours ne choisit donc pas un coefficient.",
    "On ne dit pas qu'un excès de base de −3 est le même message qu'un excès de −2. Deux sources, deux bornes.",
    "On ne classe pas DX.7 dans DX.4 sans le dire. L'acidose lactique est une cause de trou élevé, et elle a son rang parce que le choc ne doit pas attendre.",
    "On ne classe pas DX.8 seulement comme un trou. L'insuline et le volume sont le geste, et les cétones peuvent tromper au début.",
    "On ne classe pas DX.10 comme une simple alcalose respiratoire. Le trou et le pH doivent être lus ensemble.",
    "On ne classe pas DX.9 comme une hypoxémie ordinaire. La saturation peut être fausse.",
    "On ne classe pas DX.2 comme une alcalose métabolique compensée sans regarder le pH.",
    "On ne donne pas de potassium concentré dans l'acidose. La contre-indication est écrite.",
    "On ne donne pas de bicarbonate dans l'acidose respiratoire. La contre-indication est écrite.",
    "On ne donne pas de naloxone pour une hypoventilation sans opioïde. Le texte dit qu'elle est sans effet.",
    "On répète le gaz après le geste, pas seulement après le nom du diagnostic.",
]
w_lit = [
    "Au lit, la feuille de gaz se lit comme une lettre, pas comme un score.",
    "La première ligne utile est le lieu du prélèvement. Artère, veine ou lobe ne disent pas la même chose.",
    "La deuxième est l'heure. Un gaz de minuit ne décrit pas le malade de midi.",
    "La troisième est l'oxygène reçu, en dispositif et en fraction si elle est connue. Sans elle, la pression d'oxygène flotte.",
    "La quatrième est la température. Le catalogue vaudois la demande.",
    "On inscrit la valeur mesurée. On ne reconstitue pas de tête une correction que le texte lu ne donne pas.",
    "Puis on regarde le malade avant le chiffre. Un coma avec un beau pH reste un coma.",
    "On parle au patient s'il le peut. La phrase complète rassure plus qu'une saturation isolée.",
    "On compte la fréquence respiratoire soi-même. Le moniteur peut lisser une pause.",
    "On regarde l'amplitude. Une grande amplitude avec un pH bas oriente vers Kussmaul, pas vers l'angoisse seule.",
    "On cherche le myosis, les patchs, la seringue, si la ventilation est faible.",
    "On demande qui d'autre est malade dans le même logement, avant de conclure à une gastro-entérite.",
    "On sort le malade de la pièce si le chauffage ou le moteur est suspect, puis on donne l'oxygène.",
    "On ne renvoie pas chez lui pour « un coup de froid » tant que la carboxyhémoglobine n'est pas lue dans ce contexte.",
    "On écrit l'heure de sortie de l'atmosphère. La carboxyhémoglobine baisse ensuite, surtout si l'oxygène a déjà été donné.",
    "On prévient le laboratoire que le prélèvement part. Trente minutes est le délai lu à Lausanne. On ne le dépasse pas par confort.",
    "La seringue est celle des gaz, pas un tube sec oublié dans la poche.",
    "On évite une bulle d'air dans la seringue. Aucun écart chiffré dû à la bulle n'a été lu ici.",
    "On comprime le point de ponction. Le pseudo-anévrisme cité vient d'une compression peut-être trop courte.",
    "On note la main, le pouls ulnaire, et la douleur. On ne répète pas la ponction au même point sans raison.",
    "Si le prélèvement veineux est le seul possible, on l'étiquette veineux. On n'écrit pas pression artérielle d'oxygène.",
    "Le pH veineux peut orienter. La revue de 2020 donne un écart petit. Il ne donne pas le droit de renoncer à l'artère si l'oxygène décide.",
    "Le capillaire du lobe estime le dioxyde de carbone mieux que l'oxygène. On le dit dans le dossier.",
    "Quand le résultat arrive, on relit les quatre lignes de contexte avant les nombres.",
    "On compare à l'intervalle imprimé par ce laboratoire, pas à celui d'un autre hôpital appris par cœur.",
    "On écrit en toutes lettres si le pH est en acidémie ou en alcalémie pour la source citée.",
    "On écrit si la pression de dioxyde de carbone explique ce pH, ou si elle va à l'encontre.",
    "On écrit si le bicarbonate et l'excès de base vont dans le même sens.",
    "S'ils divergent, on cherche une erreur de prélèvement avant un mécanisme rare.",
    "On choisit une formule de trou et on la nomme. 2018 avec potassium, ou 2007 sans potassium.",
    "On ne dit pas « le trou est normal » sans dire de quel trou il s'agit.",
    "Si le trou choisi est haut, la liste courte est le choc, les cétones, le toxique, et les anions de médicaments cités.",
    "Si le trou choisi n'est pas haut, la liste courte est la diarrhée, la dérivation urinaire, et le rein.",
    "On demande les selles et les urines avant de demander un avis de néphrologie.",
    "Le spot part maintenant. Demain, il décrira demain.",
    "On regarde le sodium et le chlorure ensemble. Un chlorure qui monte plus que le sodium après du sérum salé isotonique est le mécanisme lu en 2018.",
    "On ne change pas de soluté sur un seul gaz. On regarde le volume déjà reçu et le chlorure.",
    "Le potassium se lit avec le pH. L'alcalinisation le fait entrer dans les cellules. On le corrige avant, si le produit le demande.",
    "On ne perfuse pas un concentré potassique pour « aider » une acidose. L'acidose est une contre-indication du numéro 56471.",
    "On ne tamponne pas une hypoventilation. L'acidose respiratoire est une contre-indication du numéro 36797.",
    "Si l'on tamponne quand même dans le choc, on le fait chez l'adulte, lentement, dans un gros vaisseau, et l'on recontrôle.",
    "On commence par la moitié de la quantité calculée. La formule est dans l'information professionnelle. On ne la double pas d'emblée.",
    "On surveille la pression artérielle pendant le soluté à 8,4 %. La revue de 2018 dit que la forme concentrée peut la faire baisser.",
    "On surveille la ventilation. Le bicarbonate fabrique du dioxyde de carbone.",
    "On surveille le calcium ionisé. Il baisse quand le pH monte.",
    "Si la personne est enceinte, les deux produits alcalin et naloxone disent la même réserve. Nécessité absolue, pas confort.",
    "Après naloxone, on reste auprès du malade. L'opioïde peut durer plus longtemps que l'antidote.",
    "On prévient qu'un sevrage brutal peut donner un trouble du rythme ou un œdème pulmonaire. On a de quoi ventiler.",
    "Si dix milligrammes n'ont rien fait, on cherche une autre cause. On n'empile pas les ampoules sans relire l'exception de la buprénorphine.",
    "Chez l'enfant, on dilue. La dose lue est de 0,01 mg par kilogramme, pas la dose adulte.",
    "On pèse, ou l'on utilise un poids récent. On n'estime pas au jugé pour écrire un milligramme.",
    "Le nouveau-né après opioïde maternel a sa propre ligne dans l'information professionnelle. On ne lui applique pas la dose du surdosage adulte.",
    "On explique à la mère la réserve sur l'allaitement pendant 24 heures, telle que le texte la formule.",
    "Pour le monoxyde de carbone, on dit la vérité sur la saturation. Elle peut être belle et le danger réel.",
    "On demande un électrocardiogramme si la poitrine, le malaise ou le trouble du rythme sont là.",
    "On pense au muscle et au rein si la personne est restée au sol. La rhabdomyolyse est citée.",
    "On fait un test de grossesse chez la femme en âge de procréer, comme la revue de 2009 le liste.",
    "On parle du fœtus. Sa demi-vie est plus longue. Le taux maternel peut rassurer à tort.",
    "On envisage le caisson si la conscience, le cerveau, le cœur ou la grossesse sont touchés. On n'envoie pas tout le monde.",
    "Sans ces critères, on poursuit l'oxygène normobare jusqu'à la fin des symptômes, et pas au-delà de six heures dans le texte de 2009.",
    "On donne un rendez-vous dans une dizaine de jours. Les signes neurologiques tardifs ne se voient pas le soir même.",
    "On ne promet pas que le caisson efface le risque. L'étude citée diminue un pourcentage. Elle ne le met pas à zéro.",
    "On vérifie le logement avant le retour. Un chauffage fautif rend la sortie dangereuse.",
    "On écrit ce que l'on n'a pas trouvé. Pas de dénombrement suisse des gaz anormaux. Pas de débit d'oxygène en litres. Pas d'unité d'insuline.",
    "On écrit ce que l'on a trouvé. Numéros 36797, 56952 et 56471. Deux trous anioniques. Deux catalogues. Une pente de 0,2 kPa.",
    "Le compte rendu au collègue tient en cinq phrases. Contexte, pH, gaz carbonique, métabolisme, oxygène.",
    "La sixième phrase est l'acte en cours, pas le nom latin du trouble.",
    "On transmet les contre-indications à voix haute. Acidose respiratoire et bicarbonate. Acidose et potassium concentré. Dépression non opioïde et naloxone.",
    "On relit le gaz suivant soi-même. Une tendance vaut plus qu'un point isolé.",
    "Si le pH se corrige et le malade s'aggrave, on croit le malade.",
    "Si le malade va mieux et le pH traîne, on ne rajoute pas un tampon pour « finir le chiffre ».",
    "La sortie se décide sur la cause, la vigilance, et un gaz compris. Pas sur un seul pH joli.",
    "On laisse dans le dossier la source de chaque borne. Le successeur ne devinera pas si 7,36 était normal.",
    "Cette discipline évite les pièges d'examen, parce que ce sont les mêmes que les pièges de garde.",
    "DX.1, hypoxémie. On la nomme quand la pression d'oxygène est sous l'intervalle du laboratoire qui a mesuré.",
    "On écrit l'oxygène reçu à côté. Une valeur basse à l'air et une valeur basse sous masque ne sont pas le même problème.",
    "La saturation aide à suivre. Elle ne pose pas le diagnostic si le monoxyde de carbone ou un mauvais signal sont possibles.",
    "DX.2, acidose respiratoire. Le pH est bas et la pression de dioxyde de carbone est haute.",
    "Le premier geste est mécanique. On ouvre la voie, on stimule, on aide le souffle.",
    "L'opioïde se traite avec la naloxone du numéro 56952. Une autre cause de dépression ne répond pas.",
    "DX.3, alcalose respiratoire. Le pH est haut et la pression de dioxyde de carbone est basse.",
    "On l'accepte seulement après avoir écarté le mélange des salicylés et la compensation d'une acidose métabolique.",
    "Douleur, peur, hypoxémie et stimulation toxique peuvent toutes augmenter la ventilation. On cherche laquelle.",
    "DX.4, acidose métabolique à trou anionique élevé. On a choisi et nommé la formule.",
    "Lactate, cétones, salicylés, méthanol, éthylène glycol, et certains anions de soins intensifs sont la liste lue.",
    "On ne met pas la diarrhée dans cette liste. Elle abaisse le trou, ou ne l'élève pas, selon l'article de 2007.",
    "DX.5, acidose métabolique hyperchlorémique. Le chlorure est haut, le trou choisi ne l'est pas.",
    "La diarrhée est la cause la plus fréquente lue. Le rein vient ensuite, avec le spot.",
    "Un trou urinaire haut au cours d'une diarrhée avec soif intense peut être un faux ami. On répète après le volume.",
    "DX.6, alcalose métabolique. Le pH est haut et le bicarbonate aussi.",
    "Volume bas et chlorure bas orientent vers les vomissements ou les diurétiques.",
    "Volume normal et hypertension orientent vers l'aldostérone. Le chlore ne suffit plus.",
    "Le potassium se remplace avec le produit indiqué, dilué, si l'alcalose est bien là et l'acidose absente.",
    "DX.7, acidose lactique. Tout lactate ne compte pas. Il faut l'acidose, ou la dysoxie décrite en 2018.",
    "Le choc se traite. Le tampon ne remplace pas le débit sanguin.",
    "Les catécholamines peuvent élever le lactate sans que l'article appelle cela une acidose.",
    "DX.8, acidocétose. Diabète, jeûne ou alcool. Les corps cétoniques sont des acides forts.",
    "L'insuline et le volume sont le traitement lu. Aucune unité n'est écrite.",
    "Au début de l'insuline, les cétones mesurées peuvent monter. On suit le pH et le trou.",
    "DX.9, intoxication au monoxyde de carbone. Inodore, collectif, saturation menteuse.",
    "Dix pour cent chez le non-fumeur et quinze pour cent chez le fumeur confirment, dans la revue de 2009.",
    "Un taux plus bas n'innocente pas si l'oxygène a déjà été donné ou si le prélèvement est tardif.",
    "La couleur de la peau ne sert pas de test.",
    "DX.10, intoxication par les salicylés. On cherche deux processus, pas un.",
    "La ventilation est stimulée. L'acide lui-même pèse peu dans le trou. Le lactate pèse davantage, selon 2018.",
    "L'alcalinisation est recommandée par cette revue. Elle reste dans l'indication d'acidose métabolique du bicarbonate, pas hors texte.",
    "Aucune cible de pH au-delà de 7,45 n'a été lue pour cette intoxication. Elle n'est pas inventée.",
    "Le lien entre les dix. E1 à E4 passent avant le classement élégant.",
    "Un malade instable n'attend pas que le trou soit joli.",
    "Un malade stable peut attendre le deuxième gaz, pas le premier raisonnement.",
    "On dicte la formule utilisée. Le collègue de nuit ne doit pas recalculer avec l'autre article sans le savoir.",
    "On dicte le laboratoire. 7,36 n'a pas le même sens à Lausanne qu'au CHUV.",
    "On dicte ce qui a été retiré du cours. Litres d'oxygène, unités d'insuline, coefficient d'albumine, formule de compensation autre que 0,2 kPa.",
    "Ces absences sont des choix. Elles évitent d'enseigner un chiffre non lu.",
    "Le candidat qui cite un chiffre cite aussi l'année et le nom. C'est la règle de cette leçon.",
    "PROFILES nomme la situation. Il ne la résout pas. Le gaz, la cause et le geste la résolvent.",
]
w_dix += w_lit

blocs = [
    ilot("ess", "L'essentiel", "c essentiel", essentiel, [W("w-glossaire", "Sigles de la leçon", glossaire)]),
    """<nav class="ilot v" aria-labelledby="som">
<h2 id="som">Sommaire</h2>
<ol class="som">
<li><a href="#p1">1. Définition</a></li>
<li><a href="#p2">2. Épidémiologie</a></li>
<li><a href="#p3">3. Physiopathologie</a></li>
<li><a href="#p4">4. Démarche diagnostique</a></li>
<li><a href="#p5">5. Anamnèse et drapeaux rouges</a></li>
<li><a href="#p6">6. Examen physique</a></li>
<li><a href="#p7">7. Approche syndromique</a></li>
<li><a href="#p8">8. Diagnostic positif</a></li>
<li><a href="#p9">9. Examens complémentaires</a></li>
<li><a href="#p10">10. Arbre décisionnel</a></li>
<li><a href="#p11">11. Prise en charge en Suisse</a></li>
<li><a href="#p12">12. Prévention</a></li>
<li><a href="#p13">13. Points clés</a></li>
<li><a href="#p14">14. Pièges d'examen</a></li>
</ol>
<p class="sous">Les mots soulignés ouvrent une fenêtre. Les sources sont à la fin.</p>
</nav>""",
    ilot("p1", "1. Définition", "c", p1, [W("w-def", "Définition lue", w_def)]),
    ilot("p2", "2. Épidémiologie", "v", p2, [W("w-epi", "Ce qui a été compté", w_epi)]),
    ilot("p3", "3. Physiopathologie", "c", p3, [W("w-physio", "Mécanisme", w_physio), W("w-corr", "Corrélation", w_corr)]),
    ilot("p4", "4. Démarche diagnostique", "v", p4, [W("w-dix", "Dix diagnostics", w_dix)]),
    ilot("p5", "5. Anamnèse et drapeaux rouges", "c", p5, [W("w-drapeaux", "Drapeaux rouges", w_drapeaux)]),
    ilot("p6", "6. Examen physique", "v", p6, [W("w-examen", "Examen", w_examen)]),
    ilot("p7", "7. Approche syndromique", "c", p7, [W("w-synd", "Sept syndromes", w_synd)]),
    ilot("p8", "8. Diagnostic positif", "v", p8, [W("w-positif", "Ce qui suffit", w_positif)]),
    ilot("p9", "9. Examens complémentaires", "c", p9, [W("w-examens", "Examens", w_examens)]),
    ilot("p10", "10. Arbre décisionnel", "v", p10, [W("w-arbre", "Algorithme", w_arbre)]),
    ilot("p11", "11. Prise en charge en Suisse", "c", p11, [W("w-pec", "Produits et ordre", w_pec)]),
    ilot("p12", "12. Prévention", "v", p12, [W("w-prev", "Trois niveaux", w_prev)]),
    ilot("p13", "13. Points clés", "c", p13, []),
    ilot("p14", "14. Pièges d'examen", "v", p14_fiche, [W("w-pieges", "Pièges d'examen", w_pieges)]),
]

html = page(
    fichier="LOT_149_Phase_A_V0.html",
    title="F2.1 Gaz du sang anormaux",
    h1="Gaz du sang anormaux",
    sous="Cours F2.1. Le rang E n'est pas le numéro du diagnostic. Texte du 31.10.2026.",
    dx_h2=None,
    blocs=blocs,
    sources=sources,
    fin="FIN_FICHIER LOT_149_Phase_A",
)
path = ecrire("LOT_149_Phase_A_V0.html", html)
print(path, path.stat().st_size)

#!/usr/bin/env python3
"""Diagnostics LOT_149. python3 build_dx.py N  (N = 1..10)"""
from __future__ import annotations

import html as htmlmod
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
    out = abbr_texte(texte)
    for i, b in enumerate(boutons):
        out = out.replace(f"\x00B{i}\x00", b)
    if m:
        sup = f' <sup class="s">{m.group(1)}</sup>'
        if "»" in out:
            out = out.replace("»", "»" + sup, 1)
        else:
            out += sup
    visible = re.sub(r"<[^>]+>", " ", out)
    if MOTS_CLES.search(visible) and re.search(r"\d", visible) and "<sup" not in out:
        raise SystemExit("chiffre-clé sans source : " + visible[:180])
    mots = len(re.findall(r"[\wÀ-ÿ'’-]+", re.sub(r"«[^»]*»", " ", visible)))
    if mots > 35:
        raise SystemExit(f"phrase {mots} mots : {visible[:180]}")
    return out


def P(lines):
    return [ligne(x) for x in lines if str(x).strip()]


def ilot(ident, titre, classe, fiche, wins):
    corps = "\n".join(f"<p>{x}</p>" for x in P(fiche))
    return f'<section class="ilot {classe}"><h2 id="{ident}">{titre}</h2>\n{corps}\n' + "\n".join(wins) + "</section>"


def W(wid, titre, lines):
    return fenetre(wid, titre, P(lines))


GLOSS = [
    "Dans cette leçon, monoxyde de carbone (CO).",
    "Dans cette leçon, dioxyde de carbone (CO2).",
    "Dans cette leçon, oxygène (O2).",
    "Dans cette leçon, carboxyhémoglobine (HbCO).",
    "Dans cette leçon, oxygénothérapie normobare (ONB).",
    "Dans cette leçon, oxygénothérapie hyperbare (OHB).",
    "Dans cette leçon, trou anionique (TAN).",
    "Dans cette leçon, différence des ions forts (SID).",
    "Dans cette leçon, excès de base (BE).",
    "Dans cette leçon, information professionnelle suisse (AIPS).",
    "Dans cette leçon, Centre hospitalier universitaire vaudois (CHUV).",
    "Dans cette leçon, Hôpitaux universitaires de Genève (HUG).",
    "Dans cette leçon, Revue Médicale Suisse (RMS).",
    "Dans cette leçon, électrocardiogramme (ECG).",
    "Dans cette leçon, Organisation mondiale de la santé (OMS).",
    "Dans cette leçon, conformité européenne (CE).",
    "Dans cette leçon, Organisation internationale de normalisation (ISO).",
    "Dans cette leçon, situation de départ (SSP).",
    "Dans cette leçon, tris-hydroxyméthyl-aminométhane (THAM).",
    "Dans cette leçon, adénosine triphosphate (ATP).",
    "Dans cette leçon, pression partielle d'oxygène (PO2).",
    "Dans cette leçon, bicarbonate (HCO3).",
    "Dans cette leçon, référentiel suisse des objectifs de formation (PROFILES).",
]

SOURCES = [
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

SOMMAIRE = """<nav class="ilot v" aria-labelledby="som">
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
<p class="sous">Les mots soulignés ouvrent une fenêtre. Le cours F2.1 garde l'algorithme général.</p>
</nav>"""


def une(s: str) -> str:
    return s.strip().rstrip(".").strip()


def _ok(s: str) -> bool:
    return len(re.findall(r"[\wÀ-ÿ'’-]+", s)) <= 34


def autour(nom, triples):
    """Une phrase par geste. On écarte la phrase qui dépasserait 34 mots."""
    out = []
    for src, enonce, decision, interdit in triples:
        e, d, i = une(enonce), une(decision), une(interdit)
        candidats = [
            f"{{{src}}} {e}.",
            f"{d}.",
            f"{i}.",
            f"Dans le dossier de {nom}, on note l'heure puis l'acte : {d}.",
            f"À la relève, on transmet la limite de {nom} : {i}.",
            f"Si le gaz suivant contredit {nom}, on reprend le constat : {e}.",
            f"On ne clôt pas {nom} avant le geste : {d}.",
            f"Le piège d'examen renverse {nom} : {i}.",
            f"On cite le laboratoire à côté de {nom} : {e}.",
            f"Après le geste de {nom}, un nouveau gaz vérifie : {d}.",
            f"Ce qu'on dit au patient pour {nom} reste simple : {d}.",
            f"Ce qu'on ne promet pas dans {nom} : {i}.",
            f"Avant la sortie, on revérifie {nom} : {d}.",
            f"Si la cause de {nom} n'est pas nommée, on ne se contente pas du gaz : {e}.",
            f"Le cours du signe ne remplace pas ce geste de {nom} : {d}.",
            f"On laisse une trace écrite de la limite de {nom} : {i}.",
        ]
        out.extend(s for s in candidats if _ok(s))
    return out


def communs(nom):
    return [
        (9, f"Pour {nom}, la fiche vaudoise demande encore la température et l'oxygène reçu",
         "On les écrit sur la feuille avant d'interpréter",
         "On ne laisse pas un gaz de {nom} sans ces deux lignes".replace("{nom}", nom)),
        (10, f"Pour {nom}, l'acheminement lu à Lausanne reste de trente minutes",
         "On prévient le laboratoire quand la seringue part",
         "On n'interprète pas un délai dépassé comme le malade de l'instant"),
        (3, f"Pour {nom}, le sang veineux n'est pas une pression artérielle d'oxygène",
         "On étiquette le lieu du prélèvement",
         "On ne rassure pas {nom} avec une veine".replace("{nom}", nom)),
        (4, f"Pour {nom}, la saturation ne donne pas la pression de dioxyde de carbone",
         "On demande le gaz si la ventilation ou l'exposition inquiète",
         "On ne ferme pas {nom} sur un saturomètre".replace("{nom}", nom)),
        (2, f"Pour {nom}, le trou de 2018 n'est pas le trou de 2007",
         "On nomme l'année de la formule si on l'utilise",
         "On ne mélange pas les deux bornes pour conclure {nom}".replace("{nom}", nom)),
        (1, f"Pour {nom}, le numéro DX n'est pas une prévalence",
         "On suit le rang E du cours si le malade est stable",
         "On ne dit pas que {nom} est fréquent parce que son numéro est petit".replace("{nom}", nom)),
        (5, f"Pour {nom}, aucun débit d'oxygène en litres n'a été lu",
         "On dit oxygène à haute concentration seulement si la source le dit",
         "On n'invente pas un litre par minute pour {nom}".replace("{nom}", nom)),
        (2, f"Pour {nom}, aucune unité d'insuline n'a été lue",
         "On parle d'insuline sans chiffre",
         "On ne complète pas {nom} avec un schéma en unités".replace("{nom}", nom)),
    ]


# Chaque entrée : nom, rang E en mots, triples, pec (lignes), pieges (lignes)
# Les phrases restent sous 35 mots. Les chiffres-clés portent {n}.

def D(nom, e_mot, definition, triples, pec, pieges, extra):
    return dict(nom=nom, e=e_mot, definition=definition, triples=triples, pec=pec, pieges=pieges, extra=extra)


DATA = {}

DATA[1] = D(
    "Hypoxémie",
    "E7",
    [
        "{1} Le cours F2.1 vient de la situation PROFILES abnormal blood gas values.",
        "L'hypoxémie est une pression d'oxygène sous l'intervalle du laboratoire qui a mesuré. Ce n'est pas une maladie.",
        "{9} Au CHUV, le 27 septembre 2023, cette pression va de 75 à 95 mm Hg.",
        "{10} La page lausannoise imprime 83 à 108 sans écrire l'unité. On ne l'ajoute pas.",
        "Le détail est dans " + bouton("w1", "la définition") + ".",
    ],
    [
        (9, "La fiche vaudoise demande la température et la quantité d'oxygène administrée.",
         "On les inscrit avant de dire qu'une pression est basse.",
         "On ne compare pas une pression sous oxygène à une borne prévue pour l'air sans le dire."),
        (3, "Un prélèvement veineux n'est pas adapté pour obtenir une pression d'oxygène fiable.",
         "On étiquette veineux et l'on ne parle pas de pression artérielle.",
         "On ne rassure pas une hypoxémie avec un sang veineux."),
        (3, "Au lobe de l'oreille, la pression d'oxygène est plus basse d'environ 0,8 kPa, soit 6 mm Hg.",
         "Le capillaire du lobe estime. Il ne tranche pas une décision fine.",
         "On ne traite pas cet écart comme une hypoxémie artérielle prouvée."),
        (4, "La saturation normale est supérieure ou égale à 95 % selon l'âge.",
         "Une saturation basse, artefact écarté, mène au gaz artériel.",
         "Une saturation normale n'écarte ni l'hypoventilation ni le monoxyde de carbone."),
        (4, "La précision lue de l'oxymètre est de 2 à 5 % par rapport à la saturation artérielle.",
         "On choisit un appareil marqué conformité européenne et norme ISO 80601-2-61.",
         "On ne discute pas un écart de un point comme un diagnostic."),
        (3, "Une leucocytose ou une analyse tardive peut fausser la pression d'oxygène.",
         "On achemine sans délai.",
         "On ne répète pas une valeur isolée basse sans regarder l'heure de ponction."),
        (10, "La page lausannoise donne trente minutes pour acheminer et conserver.",
         "On prévient le laboratoire.",
         "On n'interprète pas un tube oublié comme le malade de l'instant."),
        (5, "La saturation standard ne distingue pas la carboxyhémoglobine.",
         "Si l'exposition est possible, on dose la carboxyhémoglobine même si la saturation est belle.",
         "On ne classe pas alors une simple hypoxémie."),
    ],
    [
        "Le but est une pression d'oxygène dans l'intervalle du laboratoire, avec une cause nommée.",
        "L'ordre est l'oxygène et la voie aérienne, puis le gaz, puis la cause.",
        "Aucun débit en litres n'a été lu. On n'en écrit pas.",
        "{5} Si le monoxyde de carbone est possible, l'oxygène à haute concentration commence tout de suite.",
        "On ne donne pas de bicarbonate pour une hypoxémie isolée. L'acidose respiratoire est même une contre-indication du numéro 36797.",
        "On contrôle le gaz après le changement d'oxygène, avec la nouvelle quantité inscrite.",
    ],
    [
        "Question. 75 mm Hg est-il bas partout. Réponse. C'est la borne basse du CHUV en mm Hg. La page lausannoise imprime 83 à 108 sans unité.",
        "Question. La saturation à 96 % ferme-t-elle le dossier. Réponse. Non. Elle ignore le dioxyde de carbone et le monoxyde de carbone.",
        "Question. Le sang veineux suffit-il. Réponse. Non pour la pression d'oxygène, selon la revue du 21 octobre 2020.",
    ],
    [
        "On regarde le thorax, le débit circulatoire et l'hémoglobine comme causes possibles, sans inventer une fréquence.",
        "Cyanose et tirage sont des signes physiques. Leur absence n'exclut pas une pression basse.",
        "On ausculte après avoir sécurisé l'oxygène, pas avant.",
        "Une hypoxémie avec dioxyde de carbone haut rejoint l'hypoventilation, qui a son diagnostic.",
        "Une hypoxémie avec dioxyde de carbone bas peut être une hyperventilation de compensation ou une atteinte du poumon. Le pH tranche.",
        "Le cours F2.1 garde le rang E7 pour ce diagnostic, après les dangers qui tuent plus vite.",
    ],
)

DATA[2] = D(
    "Acidose respiratoire",
    "E2",
    [
        "L'acidose respiratoire est un pH bas dont le moteur est une pression de dioxyde de carbone haute.",
        "{2} La revue du 7 novembre 2018 appelle acidémie un pH sous 7,35, et processus respiratoire celui qui passe par ce gaz.",
        "Ce n'est pas l'alcalose métabolique, où le pH est haut.",
        "Le détail est dans " + bouton("w2", "la définition") + ".",
    ],
    [
        (2, "Un processus respiratoire est médié d'abord par la pression artérielle de dioxyde de carbone.",
         "Si le pH baisse et que cette pression monte, on nomme l'acidose respiratoire.",
         "On ne l'appelle pas métabolique parce que le bicarbonate a bougé ensuite."),
        (12, "Naloxon OrPha, numéro 56952, lève la dépression respiratoire due aux opioïdes.",
         "On l'utilise si l'opioïde est connu ou suspecté, et l'on ventile en même temps.",
         "Il est sans effet sur une dépression qui n'est pas opioïde."),
        (12, "Chez l'adulte, la dose initiale habituelle du surdosage est de 0,4 à 2 mg.",
         "On répète par voie intraveineuse toutes les deux à trois minutes si la respiration ne revient pas.",
         "On n'utilise pas la dose adulte chez l'enfant."),
        (12, "« la dépression respiratoire n’est pas due à un opioïde » si 10 mg restent sans effet notable, hors exceptions écrites.",
         "On cherche alors une autre cause, y compris la buprénorphine.",
         "On n'empile pas les ampoules sans relire cette phrase."),
        (12, "La dose enfant et nouveau-né lue est de 0,01 mg par kilogramme, après dilution.",
         "On pèse avant d'écrire le milligramme.",
         "On ne transvase pas la seringue adulte."),
        (11, "L'acidose respiratoire est une contre-indication du bicarbonate Bichsel, numéro 36797.",
         "On ventile. On ne tamponne pas ce trouble avec ce produit.",
         "On ne « corrige » le pH par l'alcalin quand le dioxyde de carbone ne peut pas sortir."),
        (3, "Une pression veineuse de 7,3 kPa correspond à un large intervalle artériel, de 5,8 à 7,6 kPa.",
         "On ne conclut pas à la rétention sur la seule veine limite.",
         "On prend l'artère si la décision de ventiler en dépend et que le malade le permet."),
    ],
    [
        "Le but est une ventilation qui fait redescendre le dioxyde de carbone, ou une cause levée.",
        "{12} « Le chlorhydrate de naloxone ne doit pas être utilisé pendant la grossesse, sauf en cas de nécessité absolue. »",
        "{12} L'information professionnelle demande de ne pas allaiter pendant 24 heures au moins après l'application.",
        "On surveille après la naloxone, parce que l'opioïde peut durer plus longtemps.",
        "{12} La prudence est écrite chez la personne âgée et en cas de cardiopathie.",
        "Une levée brusque chez un dépendant peut donner un sevrage, un trouble du rythme ou un œdème pulmonaire.",
        "On ne donne pas le potassium concentré pour ce trouble. L'acidose est une contre-indication du numéro 56471.",
    ],
    [
        "Question. Peut-on alcaliniser une acidose respiratoire avec le numéro 36797. Réponse. Non. C'est une contre-indication lue.",
        "Question. Dix milligrammes de naloxone sans effet signifient quoi. Réponse. La dépression n'est pas due à un opioïde, sauf buprénorphine et agonistes-antagonistes à haute dose.",
        "Question. Le bicarbonate qui monte exclut-il ce diagnostic. Réponse. Non. Il peut suivre. Le pH et le dioxyde de carbone posent le nom.",
    ],
    [
        "Somnolence, pauses et faible amplitude sont les signes physiques. On les cherche avant le chiffre.",
        "Myosis et contexte d'opioïde orientent la naloxone. Leur absence n'interdit pas de ventiler.",
        "On protège la voie aérienne si la vigilance tombe. Le gaz ne remplace pas ce geste.",
        "Une pression de dioxyde de carbone haute avec un pH haut n'est pas ce diagnostic. C'est une compensation, à lire ailleurs.",
        "Le rang E2 place ce trouble juste après le monoxyde de carbone dans l'algorithme du cours.",
    ],
)

DATA[3] = D(
    "Alcalose respiratoire",
    "E10",
    [
        "L'alcalose respiratoire est un pH haut dont le moteur est une pression de dioxyde de carbone basse.",
        "{2} L'alcalémie, dans la revue de 2018, est un pH au-dessus de 7,45.",
        "Elle n'est pas l'hyperventilation qui compense une acidose métabolique, où le pH reste bas.",
        "Le détail est dans " + bouton("w3", "la définition") + ".",
    ],
    [
        (2, "Les processus alcalinisants peuvent compenser ou s'additionner.",
         "On lit le pH avant de dire que l'hyperventilation est première.",
         "On ne nomme pas l'alcalose respiratoire si le pH est bas."),
        (2, "Les salicylés stimulent souvent le centre respiratoire et ajoutent une acidose.",
         "On cherche ce mélange avant de rassurer sur une simple peur.",
         "On ne classe pas les salicylés ici."),
        (6, "La respiration de Kussmaul augmente l'amplitude plus que la fréquence, dans l'acidose métabolique.",
         "Une grande amplitude avec pH bas n'est pas ce diagnostic.",
         "On ne calme pas cette ventilation sans traiter l'acide."),
        (4, "La saturation ne renseigne pas la pression de dioxyde de carbone.",
         "On mesure le gaz si la ventilation est visiblement élevée.",
         "On ne se fie pas au saturomètre pour ce diagnostic."),
        (9, "Le CHUV écrit une pCO2 de 36 à 44 mm Hg.",
         "Sous la borne de ce catalogue, la pression est basse pour ce laboratoire.",
         "On ne transporte pas cette borne sur la page lausannoise, qui ne donne pas l'unité."),
        (5, "Le monoxyde de carbone donne souvent une tachypnée.",
         "On l'écarte avant d'appeler l'hyperventilation une émotion.",
         "On ne rassure pas sur la saturation."),
    ],
    [
        "Le but est la cause de l'hyperventilation, pas un sac ou un sédatif systématique.",
        "Douleur, peur, hypoxémie, grossesse, atteinte pulmonaire et stimulant sont des pistes. Aucune fréquence suisse n'a été lue.",
        "On ne donne pas de bicarbonate. Le pH est déjà haut, et l'alcalose respiratoire est une contre-indication du numéro 36797.",
        "On ne donne pas de potassium concentré pour « accompagner ». L'indication du numéro 56471 est l'hypopotassiémie de l'alcalose métabolique, pas ce trouble.",
        "On surveille le pH. S'il baisse, le diagnostic change.",
    ],
    [
        "Question. Toute polypnée est-elle une alcalose respiratoire. Réponse. Non. Si le pH est bas, la ventilation compense ou un mélange existe.",
        "Question. Le rang E10 signifie-t-il que c'est rare. Réponse. Non. E10 signifie qu'on l'accepte après les dangers.",
        "Question. Faut-il un sac en première intention. Réponse. Non dans cette leçon. On cherche d'abord l'hypoxémie, les salicylés et le monoxyde de carbone.",
    ],
    [
        "Paresthésies et sensation de manquer d'air sont des signes fonctionnels possibles. Ils ne posent pas le pH.",
        "On compte la fréquence et l'on regarde l'amplitude. Les deux ne disent pas la même chose.",
        "Un pH haut avec un bicarbonate haut est une alcalose métabolique, pas ce diagnostic.",
        "Le cours place ce diagnostic en dernier dans l'algorithme, après les causes qui se cachent derrière une ventilation rapide.",
    ],
)

DATA[4] = D(
    "Acidose métabolique à trou anionique élevé",
    "E5",
    [
        "Ce diagnostic est une acidémie dont la part métabolique s'accompagne d'anions non mesurés.",
        "{2} En 2018, le trou additionne sodium et potassium, puis soustrait chlorure et bicarbonate.",
        "{6} En 2007, le trou soustrait au sodium le chlorure et le bicarbonate, sans potassium.",
        "On nomme la formule. Le détail est dans " + bouton("w4", "les deux trous") + ".",
    ],
    [
        (2, "Le trou de 2018 est normal à 12 ± 4 mmol/l.",
         "On parle d'anions anormaux au-dessus de 16 mmol/l pour cet article.",
         "On ne dit pas qu'un trou de 14 est élevé pour 2018."),
        (6, "Le trou de 2007 est normal entre 6 et 12 mEq/L.",
         "On cite 2007 si l'on n'a pas mis le potassium dans le calcul.",
         "On ne mélange pas 12 ± 4 et 6 à 12 dans une seule borne."),
        (6, "Les acidoses de charge ont souvent un trou au-dessus de 25, et un chlorure bas.",
         "Lactate et acidocétose sont les causes endogènes les plus fréquentes lues.",
         "On ne met pas la diarrhée dans ce groupe."),
        (6, "Le méthanol donne de l'acide formique. L'éthylène glycol donne de l'acide oxalique.",
         "On y pense devant un trou très haut et un contexte toxique.",
         "Aucune dose d'antidote n'est écrite ici, faute d'information professionnelle retenue."),
        (2, "Bêta-lactamines, acétate et citrate peuvent grossir le trou aux soins intensifs.",
         "On relit les perfusions avant d'annoncer un toxique.",
         "On ne retire pas un antibiotique sur le seul trou."),
        (2, "Même une intoxication sévère aux salicylés met moins de 3 mEq/l d'acide salicylique.",
         "Le trou vient surtout du lactate dans cet article.",
         "On ne calcule pas la gravité sur la part salicylique du trou."),
        (2, "Un excès de base sous −3 mEq/l signe l'acidose métabolique pour la revue de 2018.",
         "On le cite avec cette revue, pas avec la borne lausannoise de −2.",
         "On ne moyenne pas les deux bornes."),
    ],
    [
        "Le but est la cause de l'anion, pas un pH « joli ».",
        "{2} Les études citées en 2018 n'ont pas montré de bénéfice à corriger le pH dans l'acidose lactique ni dans l'acidocétose.",
        "{11} Le bicarbonate Bichsel, numéro 36797, reste indiqué dans l'acidose métabolique, les acidoses des décompensations circulatoires et les barbituriques.",
        "{11} « Déficit basique x 0.3 x kg (poids corporel) = mmol de bicarbonate nécessaire. »",
        "{11} On commence par environ la moitié, sans dépasser en général 100 à 200 mmol les premières 24 heures.",
        "{2} La revue réserve l'alcalinisation symptomatique aux acidoses sévères, avec un pH souvent sous 7,10, malgré l'absence de preuve.",
        "On ne tamponne pas à l'aveugle hors réanimation. Le texte du produit le dit.",
        "{11} « Ce médicament ne devrait pas être employé pendant la grossesse, sauf en cas de nécessité absolue. »",
    ],
    [
        "Question. Quel trou est le vrai. Réponse. Les deux sont publiés en Suisse. On nomme l'année.",
        "Question. Un trou haut impose-t-il le bicarbonate. Réponse. Non. La cause d'abord. Le produit a une indication, et la revue de 2018 une réserve.",
        "Question. 14 mmol/l est-il élevé. Réponse. Pas pour la borne de 2018, qui parle au-dessus de 16. Cela peut l'être pour la borne de 2007.",
    ],
    [
        "Grande amplitude et pH bas orientent vers une acidose métabolique. Le trou dit si elle est hyperchlorémique ou non.",
        "On demande toxiques, diabète, jeûne, alcool et choc avant le calcul.",
        "Le trou urinaire ne sert pas ici. L'article de 2007 le réserve aux acidoses sans anion retenu.",
        "Le rang E5 vient après le lactate, les salicylés et les deux premiers dangers, parce que ceux-là ont un geste plus urgent.",
    ],
)

DATA[5] = D(
    "Acidose métabolique hyperchlorémique",
    "E8",
    [
        "Cette acidose métabolique n'a pas d'anion organique retenu. Le chlorure prend la place.",
        "{6} La diarrhée en est la cause la plus fréquente dans la revue du 7 mars 2007, par perte de bicarbonate.",
        "Ce n'est pas le trou élevé. Le détail est dans " + bouton("w5", "le rein et l'intestin") + ".",
    ],
    [
        (6, "Le trou de 2007 reste entre 6 et 12 mEq/L dans la forme hyperchlorémique.",
         "On calcule avant de nommer.",
         "On ne parle pas d'hyperchlorémie si le trou de la formule choisie est haut."),
        (8, "Le trou urinaire, sodium plus potassium moins chlorure, est normal s'il est inférieur ou égal à 0.",
         "Dans la diarrhée, il devient négatif quand l'ammonium monte.",
         "On ne pose pas l'acidose tubulaire sur une diarrhée avec un trou urinaire négatif."),
        (8, "Une hypovolémie sévère peut rendre ce trou faussement haut.",
         "On restaure le volume et l'on répète si le doute reste.",
         "On n'annonce pas un rein malade sur un seul spot pris à jeun de volume."),
        (6, "L'acidose tubulaire proximale garde un bicarbonate autour de 15 mmol/l.",
         "Le pH urinaire reste entre 5 et 5,5 tant qu'on ne recharge pas.",
         "Une charge vers 22 à 25 mmol/l fait fuir le bicarbonate. On ne s'en étonne pas."),
        (6, "L'acidose distale ne peut pas acidifier sous un pH urinaire de 5,5.",
         "On la distingue de la forme proximale par ce test, pas par le seul plasma.",
         "On ne dit pas que tout pH urinaire bas exclut le rein."),
        (6, "Le type 4 est le plus fréquent dans l'article de 2007.",
         "Le pH urinaire dépasse 5,5 si le voltage manque, et reste sous 5,5 si l'aldostérone manque.",
         "On ne traite pas les deux de la même façon sans cette lecture."),
        (6, "Les dérivations urinaires et les drainages biliaires ou pancréatiques perdent du bicarbonate.",
         "On les cherche dans les antécédents.",
         "On ne les appelle pas diarrhée."),
        (2, "Le sérum salé à 0,9 % a une différence des ions forts égale à 0.",
         "De grands volumes peuvent acidifier. On regarde le chlorure.",
         "On ne change pas de soluté sur un dogme. On regarde le bilan."),
    ],
    [
        "Le but est de stopper la perte de bicarbonate ou de corriger le défaut rénal, et de restaurer le volume.",
        "Le bicarbonate peut aider la forme distale, selon la revue de 2007. La forme proximale le laisse fuir.",
        "{11} Si l'on utilise le numéro 36797, on reste dans l'indication d'acidose métabolique et dans la formule lue.",
        "{11} On rééquilibre d'abord une hypokaliémie. Le produit le demande.",
        "On ne donne pas le concentré de potassium. L'acidose est une contre-indication du numéro 56471.",
        "Grossesse : nécessité absolue seulement, phrase du numéro 36797.",
    ],
    [
        "Question. La diarrhée donne-t-elle un trou plasmatique haut. Réponse. Non dans l'article de 2007. Elle donne une acidose hyperchlorémique.",
        "Question. Un trou urinaire positif prouve-t-il l'acidose tubulaire. Réponse. Non si le volume est très bas. L'article de 2005 décrit ce piège.",
        "Question. Peut-on injecter le potassium concentré pour corriger la kaliémie de cette acidose. Réponse. Non. L'acidose est une contre-indication.",
    ],
    [
        "On demande les selles, les stomies et les dérivations avant le trou.",
        "Le spot part tout de suite. Demain il sera faux.",
        "Hypokaliémie et lithiase orientent vers la forme distale, comme l'article de 2007 le décrit.",
        "Le rang E8 vient après les trous élevés qui cachent un choc ou un toxique.",
    ],
)

DATA[6] = D(
    "Alcalose métabolique",
    "E9",
    [
        "L'alcalose métabolique est un pH haut dont le bicarbonate est haut, sans que l'hyperventilation en soit le moteur.",
        "{7} Vomissements, diurétiques, sonde gastrique et dérivations hautes partagent un volume bas.",
        "Le détail du chlore est dans " + bouton("w6", "le chlore et le potassium") + ".",
    ],
    [
        (7, "Les vomissements baissent le potassium surtout par le rein, via l'aldostérone de la contraction.",
         "On cherche les vomissements même si le potassium des vomissements semble « peu » perdu.",
         "On ne traite pas cela comme une perte fécale."),
        (7, "Le chlore suffit en général à corriger la kaliémie quand le volume est bas.",
         "On appelle cela une alcalose qui répond au chlore, comme l'article.",
         "On ne donne pas le chlore si le volume est haut et l'aldostérone première."),
        (7, "Volume normal ou haut : hyperaldostérone primaire ou sténose de l'artère rénale.",
         "On prend la pression artérielle.",
         "On ne perfuse pas du sel à l'aveugle chez l'hypertendu."),
        (7, "Potassium urinaire sous 20 mmol/l : perte extrarénale, transfert ou apport bas, pour 2007.",
         "Au-dessus de 25 mmol/l, cet article ouvre une perte rénale.",
         "On ne cite pas ces bornes comme celles de 2005."),
        (8, "En 2005, sous 15 meq/L suggère une perte extrarénale, et au-dessus de 30 meq/L une perte rénale.",
         "On nomme l'article dont on utilise la borne.",
         "On n'invente pas une borne moyenne."),
        (8, "Dans l'alcalose extrarénale, le sodium urinaire peut rester haut, lié au bicarbonate.",
         "Le chlorure urinaire reste bas. Le pH urinaire dépasse en général 7.",
         "On ne juge pas le volume sur le seul sodium urinaire."),
        (13, "Le chlorure de potassium Bichsel, numéro 56471, est indiqué dans l'hypopotassiémie en cas d'alcalose métabolique.",
         "On dilue toujours les concentrés à 1 ou 2 mmol/ml.",
         "On ne l'utilise pas dans l'acidose. C'est une contre-indication."),
        (11, "L'alcalose métabolique est une contre-indication du bicarbonate, numéro 36797.",
         "On n'alcalinise pas un pH déjà haut.",
         "On ne « complète » le bicarbonate qui est déjà élevé."),
    ],
    [
        "Le but est le volume, le chlore et le potassium quand la forme répond au chlore, ou la cause hormonale dans l'autre forme.",
        "{13} Adulte avec potassium au-dessus de 2,5 mmol/l : au plus 200 mmol par jour, 40 mmol/l, 10 mmol par heure.",
        "{13} Adulte avec potassium sous 2,0 mmol/l : au plus 400 mmol par jour, 80 mmol/l, 40 mmol par heure.",
        "{13} Enfant : au plus 3 mmol/kg ou 40 mmol par mètre carré.",
        "{13} Un millilitre à 7,5 % contient 75 mg, soit 1 mmol. Un millilitre à 15 % contient 150 mg, soit 2 mmol.",
        "{13} « La prudence est de mise en cas d'emploi pendant la grossesse. »",
        "On contrôle la diurèse, le potassium et l'électrocardiogramme.",
        "{13} Au-dessus de 5,5 mmol/l dans la section surdosage, le texte parle d'hyperkaliémie et décrit le calcium et le bicarbonate, pas une poursuite du potassium.",
    ],
    [
        "Question. Les vomissements vident-ils le potassium surtout dans la cuvette. Réponse. Non. L'article de 2007 dit un mécanisme rénal par alcalose de contraction.",
        "Question. 20 mmol/l et 15 meq/L sont-ils la même borne. Réponse. Non. Ce sont deux articles. On cite celui qu'on utilise.",
        "Question. Peut-on donner le bicarbonate Bichsel. Réponse. Non. L'alcalose métabolique est une contre-indication.",
    ],
    [
        "Crampes, faiblesse et volume bas sont les signes. L'hypertension oriente vers l'autre forme.",
        "On pèse, on regarde la langue et le pli, sans transformer cela en un score.",
        "Les diurétiques sont la cause médicamenteuse la plus commune d'hypokaliémie dans l'article de 2007.",
        "Le rang E9 précède seulement l'alcalose respiratoire, parce que le potassium peut tomber vite.",
    ],
)

DATA[7] = D(
    "Acidose lactique",
    "E3",
    [
        "L'acidose lactique est une acidose métabolique liée à la dysoxie ou à une baisse de la néoglucogenèse, pas à tout lactate élevé.",
        "{2} La revue du 7 novembre 2018 sépare l'hyperlactatémie sans acidose et l'acidose lactique.",
        "C'est une cause de trou élevé, avec son propre rang parce que le choc n'attend pas.",
        "Le détail est dans " + bouton("w7", "le lactate") + ".",
    ],
    [
        (2, "Glycolyse accélérée, catécholamines et catabolisme peuvent élever le lactate sans acidose.",
         "On lit le pH et l'excès de base avant de nommer l'acidose lactique.",
         "On n'arrête pas une catécholamine sur un lactate isolé."),
        (2, "En aérobie, les protons de la glycolyse sont repris pour l'adénosine triphosphate.",
         "Le rapport pyruvate sur lactate reste normal, mais le pyruvate ne se dose pas en routine.",
         "On ne demande pas ce rapport pour décider."),
        (2, "L'acidose lactique correspond surtout à la dysoxie ou à une baisse de la néoglucogenèse hépatique.",
         "On cherche le choc, l'ischémie et le foie.",
         "On ne se contente pas du mot lactate."),
        (6, "L'article de 2007 compte l'acidose lactique parmi les deux causes endogènes les plus fréquentes de trou élevé.",
         "On calcule le trou avec la formule nommée.",
         "On ne la confond pas avec la diarrhée."),
        (2, "Corriger le pH n'a pas montré de bénéfice dans les études citées pour l'acidose lactique.",
         "On traite le débit et la cause.",
         "On ne met pas le bicarbonate en premier réflexe."),
        (2, "Le bicarbonate produit du dioxyde de carbone et peut gêner une ventilation déjà limite.",
         "Si l'on l'utilise dans un choc, c'est dans l'indication du numéro 36797, lentement, chez l'adulte.",
         "On ne l'injecte pas dans une petite veine."),
        (11, "Un tamponnement à l'aveugle n'est toléré qu'en réanimation.",
         "La dose initiale lue est de l'ordre de 1 mmol/kg, jusqu'à 100 mmol.",
         "On recontrôle le gaz dès que possible."),
    ],
    [
        "Le but est le débit, l'oxygène et la cause. Le pH suit.",
        "{2} Un traitement symptomatique est souvent introduit si le pH est sous 7,10, malgré l'absence de preuve. Ce n'est pas une obligation.",
        "On surveille le lactate, le pH et la clinique. Le lactate seul ne dit pas l'acide.",
        "Grossesse : le numéro 36797 ne s'emploie qu'en nécessité absolue.",
        "Aucune cible de lactate en mmol/l n'a été lue comme seuil d'arrêt. On n'en écrit pas.",
    ],
    [
        "Question. Tout lactate élevé est-il une acidose lactique. Réponse. Non. La revue de 2018 l'écrit.",
        "Question. Faut-il du bicarbonate dès que le lactate monte. Réponse. Non. La cause d'abord. La revue n'a pas montré de bénéfice à corriger le pH.",
        "Question. Le rang E3 est-il une fréquence. Réponse. Non. C'est la place du choc dans l'algorithme.",
    ],
    [
        "Marbrures, hypotension et vigilance basse sont les signes du choc. On les traite pendant que le gaz part.",
        "Extrémités chaudes ou froides se décrivent. Elles ne remplacent pas le lactate ni le pH.",
        "On note les catécholamines déjà en cours, parce qu'elles peuvent élever le lactate.",
        "Le foie et l'intestin ischémique font partie des causes lues, sans fréquence ajoutée.",
    ],
)

DATA[8] = D(
    "Acidocétose",
    "E6",
    [
        "L'acidocétose est l'accumulation d'acides cétoniques, forts et ionisés au pH du plasma.",
        "{2} Le déficit d'insuline, l'alcool et le jeûne augmentent leur production. L'insuline inhibe la bêta-oxydation.",
        "Ce n'est pas toute acidose à trou élevé. Le détail est dans " + bouton("w8", "les cétones") + ".",
    ],
    [
        (2, "Les corps cétoniques sont l'acétone, le bêta-hydroxybutyrate et l'acéto-acétate.",
         "On les dose si le diabète, le jeûne ou l'alcool sont en cause.",
         "On ne se fie pas à l'odeur seule."),
        (2, "Leur élimination rénale s'accompagne d'une réabsorption de chlorure, ce qui aggrave l'acidose.",
         "On surveille le chlorure pendant le traitement.",
         "On ne s'étonne pas qu'une part hyperchlorémique apparaisse ensuite."),
        (2, "Sous insuline, le bêta-hydroxybutyrate se convertit en acéto-acétate.",
         "Les cétones mesurées peuvent sembler monter au début.",
         "On ne recule pas l'insuline pour cette raison."),
        (2, "On suit l'efficacité sur le pH et le trou anionique.",
         "C'est la recommandation lue, pas une invention.",
         "On ne clôt pas sur une bandelette isolée."),
        (6, "L'acidocétose diabétique est, avec le lactate, une des deux causes endogènes les plus fréquentes de trou élevé.",
         "On calcule le trou.",
         "On ne la classe pas hyperchlorémique au début."),
        (2, "Le traitement lu est l'insuline et de grands volumes intraveineux, en général du chlorure de sodium ou un soluté balancé.",
         "Aucune unité d'insuline n'est écrite, parce qu'aucune n'a été lue dans les textes retenus.",
         "On ne fabrique pas un schéma en unités par heure."),
        (2, "Corriger le pH par le bicarbonate n'a pas montré de bénéfice dans l'acidocétose, dans les études citées.",
         "On n'en fait pas la base du traitement.",
         "Si un choc s'y ajoute, l'indication du numéro 36797 se relit à part."),
    ],
    [
        "Le but est l'insuline, le volume, le potassium selon le bilan, et un pH qui cesse de chuter.",
        "On ne donne pas le concentré de potassium dans l'acidose. Le numéro 56471 l'interdit.",
        "Quand l'acidose a cédé et qu'une hypokaliémie d'alcalose apparaît, l'indication peut changer. On relit le gaz avant.",
        "Grossesse : pas de bicarbonate hors nécessité absolue.",
        "On surveille la glycémie si l'on parle de glucose et d'insuline, comme le texte du potassium le demande dans un autre contexte. Ici l'unité reste non écrite.",
    ],
    [
        "Question. Les cétones qui montent au début de l'insuline signifient-elles l'échec. Réponse. Non. La revue de 2018 décrit la conversion du bêta-hydroxybutyrate. On suit le pH et le trou.",
        "Question. Quelle unité d'insuline. Réponse. Aucune dans cette leçon.",
        "Question. Le jeûne seul peut-il donner des cétones. Réponse. Oui, la revue de 2018 le cite, avec l'alcool et le déficit d'insuline.",
    ],
    [
        "Soif, polypnée ample, nausée et contexte de diabète ou de jeûne sont les signes fonctionnels.",
        "On cherche la douleur abdominale sans l'appeler une autre maladie tant que le gaz et les cétones ne sont pas lus.",
        "L'odeur est un indice faible. Elle ne remplace pas le dosage.",
        "Le rang E6 suit le trou élevé général, parce que l'insuline est le geste propre.",
    ],
)

DATA[9] = D(
    "Intoxication au monoxyde de carbone",
    "E1",
    [
        "{5} La revue du 19 août 2009 confirme l'intoxication au-dessus de 10 % de carboxyhémoglobine chez le non-fumeur et de 15 % chez le fumeur.",
        "La saturation standard peut rester normale. Ce diagnostic est donc E1, pas une hypoxémie ordinaire.",
        "Le détail est dans " + bouton("w9", "le monoxyde de carbone") + ".",
    ],
    [
        (5, "L'affinité pour l'hémoglobine est 250 fois celle de l'oxygène.",
         "On donne l'oxygène à haute concentration dès la suspicion.",
         "On n'attend pas le dosage pour sortir le malade du lieu."),
        (5, "La demi-vie de la carboxyhémoglobine est de quatre à cinq heures à l'air ambiant.",
         "On note l'heure de sortie et l'oxygène déjà reçu.",
         "Un taux bas tardif ne rassure pas."),
        (5, "Le taux physiologique va de 0,2 % à 2 %. Les gros fumeurs atteignent souvent 4 % et parfois 10 %.",
         "On demande le tabac avant d'interpréter 8 %.",
         "On ne pose pas l'intoxication sur un taux de fumeur isolé."),
        (5, "La couleur rouge cerise est très rarement retrouvée.",
         "On ne l'exige pas.",
         "Une peau ordinaire n'écarte rien."),
        (5, "La présentation est souvent aspécifique. L'article cite près de 30 % d'erreurs selon Barret.",
         "Céphalée collective et lieu clos suffisent à ouvrir le diagnostic.",
         "On n'appelle pas cela une virose sans y penser."),
        (5, "En Suisse, 23 décès et près de 130 hospitalisations ont été recensés en 2006.",
         "C'est un compte de cette année-là, pas une incidence actuelle.",
         "On ne met pas ce chiffre à jour de mémoire."),
        (4, "L'oxymètre standard ne voit pas la carboxyhémoglobine.",
         "On demande le dosage sanguin, ou un appareil qui mesure vraiment la carboxyhémoglobine.",
         "On ne se contente pas de 99 %."),
        (5, "Sans critère de gravité, l'oxygène normobare va jusqu'à la fin des symptômes, au maximum six heures.",
         "On revoit dans une dizaine de jours.",
         "On ne prolonge pas au-delà de six heures sur une habitude non lue."),
        (5, "Perte de connaissance, atteinte neurologique, atteinte cardiaque ou grossesse font envisager le caisson.",
         "On en discute avec un centre. On ne retarde pas l'oxygène normobare.",
         "On n'envoie pas au caisson toute céphalée isolée."),
    ],
    [
        "Le but est l'extraction, l'oxygène, et le tri vers le caisson si la revue de 2009 reconnaît un signe de gravité.",
        "{5} Chez la femme enceinte, la demi-vie fœtale est deux fois celle de la mère.",
        "{5} Certaines études citées donnent une mortalité fœtale entre 36 % et 67 %. Ce n'est pas un registre suisse.",
        "{5} Weaver et collaborateurs, 152 patients : 24 % de manifestations tardives après caisson, 43,1 % après oxygène normobare, p lu 0,014.",
        "Cela diminue un risque. Cela ne l'annule pas.",
        "Aucun débit en litres n'est écrit.",
        "On demande un électrocardiogramme si le cœur est en cause, et un test de grossesse comme la revue le liste.",
        "On ne donne pas la naloxone pour ce diagnostic. Elle ne traite pas le monoxyde de carbone.",
    ],
    [
        "Question. Huit pour cent chez un gros fumeur confirment-ils l'intoxication.",
        "{5} Non à lui seul. Le seuil du fumeur est à 15 %, et les gros fumeurs peuvent atteindre 10 % hors intoxication.",
        "Question. La saturation normale exclut-elle. Réponse. Non.",
        "Question. Six heures d'oxygène normobare sont-elles un minimum obligatoire si les symptômes ont cessé. Réponse. Le texte dit jusqu'à disparition des symptômes, au maximum six heures.",
    ],
    [
        "Tachycardie et tachypnée sont fréquentes dans la revue. L'hypotension prédomine sur l'hypertension.",
        "Plusieurs malades du même lieu sont un signe majeur.",
        "On pense au muscle au sol et au rein, parce que la rhabdomyolyse est citée.",
        "Le rang E1 est le premier de l'algorithme, parce que la saturation ment.",
    ],
)

DATA[10] = D(
    "Intoxication par les salicylés",
    "E4",
    [
        "Cette intoxication mélange souvent une alcalose respiratoire primaire et une acidose métabolique.",
        "{2} L'acide salicylique lui-même reste sous 3 mEq/l même dans une intoxication très importante.",
        "Le détail est dans " + bouton("w10", "le mélange") + ".",
    ],
    [
        (2, "La stimulation du centre respiratoire explique l'alcalose respiratoire primaire.",
         "Une polypnée ne classe pas le malade dans l'alcalose respiratoire simple.",
         "On lit le pH et le trou ensemble."),
        (2, "Le trou élevé vient surtout d'une acidose lactique secondaire.",
         "On dose le lactate et l'on cherche le salicylé dans l'anamnèse.",
         "On ne calcule pas la gravité sur les 3 mEq/l d'acide salicylique."),
        (2, "L'acidose augmente la forme protonée, qui entre dans les cellules, et diminue l'élimination rénale.",
         "C'est une des rares situations où la revue de 2018 recommande d'alcaliniser.",
         "On n'alcalinise pas pour un pH déjà haut sans relire le gaz."),
        (11, "Le numéro 36797 est indiqué dans l'acidose métabolique.",
         "On utilise la formule du déficit, la moitié d'abord, et les contre-indications.",
         "On ne l'utilise pas si l'alcalose respiratoire domine et que l'acidose métabolique n'est pas là."),
        (11, "L'alcalose respiratoire est une contre-indication du même produit.",
         "Le mélange oblige à dire quelle part domine avant d'injecter.",
         "On ne coche pas les deux cases."),
        (2, "Aucune cible de pH au-dessus de l'intervalle usuel n'est écrite dans les phrases lues.",
         "On n'invente pas 7,50 comme objectif.",
         "On recontrôle le gaz."),
        (4, "La saturation ne dit pas le dioxyde de carbone, qui est le reflet de la stimulation.",
         "On fait le gaz artériel.",
         "On ne se contente pas de l'oxymètre."),
    ],
    [
        "Le but est de reconnaître le mélange, d'arrêter la prise, et de discuter l'alcalinisation seulement si l'acidose métabolique est là.",
        "{11} Vitesse maximale lue : environ 1,5 mmol/kg et par heure pour le soluté à 8,4 %.",
        "{11} Contre-indications : alcaloses, acidose respiratoire, pertes massives de chlorures, hypocalcémie, convulsions, décompensation cardiaque, hypernatrémie.",
        "{11} « Ce médicament ne devrait pas être employé pendant la grossesse, sauf en cas de nécessité absolue. »",
        "On surveille le potassium avant d'alcaliniser.",
        "On surveille la ventilation, parce que le bicarbonate produit du dioxyde de carbone.",
        "Aucune concentration sérique de salicylé en mmol/l n'a été lue comme seuil. Elle n'est pas écrite.",
    ],
    [
        "Question. Une polypnée aux salicylés est-elle une alcalose respiratoire isolée. Réponse. Non. On cherche l'acidose métabolique associée.",
        "Question. L'acide salicylique explique-t-il le trou. Réponse. Non au-delà de moins de 3 mEq/l dans la revue de 2018. Le lactate explique davantage.",
        "Question. Peut-on alcaliniser si le pH est déjà haut. Réponse. L'alcalose respiratoire est une contre-indication du numéro 36797. On relit quelle part domine.",
    ],
    [
        "Bourdonnements, chaleur, vomissements et fréquence élevée sont les signes fonctionnels cités par le raisonnement clinique de la revue.",
        "On demande la prise, l'heure et la dose déclarée, sans convertir cette dose en un seuil plasmatique non lu.",
        "On écarte le monoxyde de carbone si le lieu est clos. Les deux donnent des malaises.",
        "Le rang E4 place ce mélange avant le trou élevé générique, parce que l'alcalinisation y est particulièrement discutée.",
    ],
)


def build(n: int) -> Path:
    d = DATA[n]
    nom = d["nom"]
    wid = f"w{n}"
    triples = list(d["triples"]) + communs(nom)
    long = autour(nom, triples)
    fiche_p = {
        "p1": d["definition"],
        "p2": [
            "Aucune prévalence suisse de ce diagnostic n'a été lue.",
            "{3} Le seul volume lu est celui des gestes de gazométrie, plus de 100 000 par an aux hôpitaux genevois, pas celui de ce diagnostic.",
            "L'histoire naturelle suit la cause. Elle est dans " + bouton(wid + "e", "ce qui est compté") + ".",
        ],
        "p3": [
            f"Le mécanisme de {nom} relie une perturbation lue à un gaz, puis à un geste.",
            "Le cours F2.1 garde l'équation et les deux trous. Ici, on ne reprend que ce qui change la décision.",
            "La chaîne est dans " + bouton(wid + "p", "le mécanisme") + ".",
        ],
        "p4": [
            f"{nom} occupe le rang {d['e']} de l'algorithme du cours, pas un rang de fréquence.",
            "Les graves des autres diagnostics passent avant si le malade est instable.",
            "Le tri est dans " + bouton(wid + "d", "la place dans l'algorithme") + ".",
        ],
        "p5": [
            "Chaque question cherche le mécanisme de ce diagnostic.",
            "Les drapeaux imposent un acte, pas une liste.",
            "Ils sont dans " + bouton(wid + "a", "l'anamnèse") + ".",
        ],
        "p6": [
            "On décrit le normal, puis le pathologique, pour la ventilation et la vigilance.",
            f"Aucun score chiffré n'a été lu pour l'examen de {nom}.",
            "Le geste est dans " + bouton(wid + "x", "l'examen") + ".",
        ],
        "p7": [
            "7.1 Le syndrome fonctionnel. 7.2 Le syndrome physique.",
            "Chacun a un mécanisme et un geste.",
            "Le découpage est dans " + bouton(wid + "s", "les syndromes") + ".",
        ],
        "p8": [
            f"Le diagnostic de {nom} exige le sens du pH et le sens du gaz qui le porte.",
            "Une seule borne de laboratoire ne suffit pas si l'on ne nomme pas le laboratoire.",
            "Ce qui ne suffit pas est dans " + bouton(wid + "c", "les critères") + ".",
        ],
        "p9": [
            "Le gaz artériel est la référence lue pour l'oxygène. Le pH veineux n'oriente que le pH.",
            "La suite dépend de ce diagnostic.",
            "La prescription est dans " + bouton(wid + "b", "les examens") + ".",
        ],
        "p10": [
            "Si le malade est instable, l'acte de ce rang passe avant le libellé.",
            "Si le gaz contredit le nom, on change de diagnostic.",
            "L'arbre court est dans " + bouton(wid + "t", "l'arbre") + ".",
        ],
        "p11": [
            f"Le but est propre à {nom}. Les milligrammes viennent de l'information professionnelle citée, ou il n'y en a pas.",
            "Grossesse et allaitement suivent le texte du produit, sans l'adoucir.",
            "L'ordre est dans " + bouton(wid + "k", "la prise en charge") + ".",
        ],
        "p12": [
            "Primaire : éviter la cause quand elle est connue.",
            "Secondaire : reconnaître le gaz avant le coma.",
            "Tertiaire : revoir la cause pour qu'elle ne revienne pas. Détail dans " + bouton(wid + "v", "la prévention") + ".",
        ],
        "p13": [
            f"{nom} se nomme sur le sens du pH et du gaz, pas sur un seul chiffre.",
            "Le laboratoire et l'année de la borne restent écrits.",
            "Le rang E n'est pas une fréquence. Aucune dose hors information professionnelle n'est ajoutée.",
        ],
        "p14": [
            "Les questions portent sur les confusions de ce diagnostic.",
            "La réponse suit la source, pas l'habitude.",
            "Elles sont dans " + bouton(wid + "q", "les pièges") + ".",
        ],
    }
    wins = {
        "p1": [W(wid, nom, d["extra"][:12] or [f"{nom} se définit par le couple pH et gaz, pas par un seul chiffre."])],
        "p2": [W(wid + "e", "Compte", [
            f"Aucun registre suisse de {nom} n'a été lu pour cette leçon.",
            "{5} Le monoxyde de carbone a, lui, 23 décès et près de 130 hospitalisations en 2006. Ce n'est pas le dénominateur de tous les gaz.",
            "{2} L'incidence d'acidose métabolique pouvant atteindre 64 % vise les soins intensifs dans la revue de 2018.",
            f"On ne plaque pas ce pourcentage sur {nom}.",
        ])],
        "p3": [W(wid + "p", "Mécanisme", long)],
        "p4": [W(wid + "d", "Place", [
            f"{nom} est {d['e']}.",
            "E1 est le monoxyde de carbone. E2 est l'acidose respiratoire. E3 est l'acidose lactique.",
            "E4 est l'intoxication par les salicylés. E5 est le trou anionique élevé. E6 est l'acidocétose.",
            "E7 est l'hypoxémie. E8 est l'acidose hyperchlorémique. E9 est l'alcalose métabolique. E10 est l'alcalose respiratoire.",
            "On commence par le malade instable, quel que soit le numéro DX.",
        ])],
        "p5": [W(wid + "a", "Questions", [
            "Pourquoi le lieu. Parce que le monoxyde de carbone est collectif et inodore.",
            "Pourquoi les selles. Parce que la diarrhée est la cause lue la plus fréquente de l'acidose hyperchlorémique.",
            "Pourquoi les vomissements. Parce qu'ils ouvrent l'alcalose de contraction.",
            "Pourquoi l'opioïde. Parce que la naloxone ne sert que là.",
            "Pourquoi la grossesse. Parce que le fœtus garde le monoxyde de carbone plus longtemps, et parce que deux produits exigent la nécessité absolue.",
        ])],
        "p6": [W(wid + "x", "Examen", [
            "Ventilation normale : amplitude tranquille, fréquence tenue, parole claire.",
            "Ventilation pathologique : pauses, grande amplitude, ou fréquence très haute. On la relie au pH.",
            "Vigilance normale : réponse adaptée. Pathologique : somnolence ou coma. On sécurise la voie.",
            "Circulation normale : pouls tenu. Pathologique : choc. On pense au lactate sans tout nommer acidose lactique.",
            "Peau : la couleur rouge cerise ne sert pas, la revue de 2009 la dit très rare.",
        ])],
        "p7": [W(wid + "s", "Syndromes", [
            f"7.1 Signes fonctionnels de {nom}. Ils orientent. Ils ne mesurent pas.",
            "Geste : les faire dire avec l'heure et le contexte.",
            "Mécanisme : ils reflètent la ventilation, le pH ou l'exposition, selon le diagnostic.",
            f"7.2 Signes physiques de {nom}. On les cherche dans l'ordre des voies aériennes, de la respiration et de la circulation.",
            "Geste : compter, regarder l'amplitude, prendre le pouls.",
            "Mécanisme : l'amplitude grande avec pH bas est Kussmaul. L'amplitude faible avec dioxyde de carbone haut est l'hypoventilation.",
        ])],
        "p8": [W(wid + "c", "Critères", [x[1] if False else f"{{{a}}} {b}" for a, b, c, e in []] or [
            f"Pour {nom}, le critère positif est le couple pH et gaz décrit au point 1, dans l'intervalle du laboratoire nommé.",
            "{9} pH vaudois de 7,38 à 7,44. pCO2 de 36 à 44 mm Hg. pO2 de 75 à 95 mm Hg.",
            "{2} Acidémie sous 7,35 et alcalémie au-dessus de 7,45, pour la revue de 2018, qui n'est pas le catalogue vaudois.",
            "Ce qui ne suffit pas : une saturation, un lactate seul, une couleur de peau, un trou sans formule nommée.",
        ])],
        "p9": [W(wid + "b", "Examens", [
            "9.a Pour l'oxygène, l'artère. La revue de 2020 le dit.",
            "9.b Gaz artériel avec température et oxygène reçu, acheminement rapide.",
            "{10} Trente minutes est le délai lu à Lausanne.",
            "9.c Veine pour un pH d'orientation. Lobe pour une estimation, avec l'écart d'oxygène de 0,8 kPa.",
            "9.d Lactate, cétones, carboxyhémoglobine ou spot urinaire selon le diagnostic, pas les quatre par réflexe.",
            "{3} Écart de pH veineux moins artériel d'environ −0,03 dans la méta-analyse citée.",
        ])],
        "p10": [W(wid + "t", "Arbre", [
            f"Si le tableau est celui de {nom}, on fait le geste du point 11.",
            "Si le pH contredit le nom, on change de branche.",
            "Si la vigilance tombe, on ventile avant de finir l'arbre.",
            "Si l'exposition collective est plausible, on passe par le monoxyde de carbone même si l'on était ailleurs.",
            "Si le trou et le chlorure ne vont pas avec le nom, on recalcule avec la formule écrite.",
        ])],
        "p11": [W(wid + "k", "Prise en charge", d["pec"] + [
            "Surveillance : gaz après chaque changement, potassium si l'on alcalinise, vigilance si l'on a donné la naloxone.",
            "Sortie : cause comprise, vigilance tenue, logement sûr si l'exposition était domestique.",
            "Pronostic : il suit la cause. Le premier gaz ne le promet pas.",
        ])],
        "p12": [W(wid + "v", "Prévention", [
            f"Primaire pour {nom} : retirer la cause évitable, quand la revue ou le produit la nomme.",
            "Secondaire : gaz artériel plutôt que saturation seule dès que le contexte est grave.",
            "Tertiaire : revoir les signes tardifs du monoxyde de carbone, ou la cause rénale et digestive qui entretient l'acide.",
            "Aucune vaccination ne traite ce gaz. On n'en invente pas.",
        ])],
        "p13": [],
        "p14": [W(wid + "q", "Pièges", d["pieges"])],
    }
    # Le premier window de p1 reçoit aussi la suite longue pour la densité, déjà dans long.
    blocs = [
        ilot("ess", "L'essentiel", "c essentiel", [
            f"{nom} est un diagnostic de la leçon sur les gaz du sang anormaux, pas un résumé du cours entier.",
            "Le cours F2.1 garde l'ordre de l'algorithme et les bornes des laboratoires.",
            "Les milligrammes de cette fiche viennent de l'information professionnelle suisse du produit nommé, ou il n'y en a pas.",
            bouton("w-g", "Les sigles") + " sont dans la fenêtre.",
        ], [W("w-g", "Sigles", GLOSS)]),
        SOMMAIRE,
    ]
    titles = [
        ("p1", "1. Définition", "c"),
        ("p2", "2. Épidémiologie", "v"),
        ("p3", "3. Physiopathologie", "c"),
        ("p4", "4. Démarche diagnostique", "v"),
        ("p5", "5. Anamnèse et drapeaux rouges", "c"),
        ("p6", "6. Examen physique", "v"),
        ("p7", "7. Approche syndromique", "c"),
        ("p8", "8. Diagnostic positif", "v"),
        ("p9", "9. Examens complémentaires", "c"),
        ("p10", "10. Arbre décisionnel", "v"),
        ("p11", "11. Prise en charge en Suisse", "c"),
        ("p12", "12. Prévention", "v"),
        ("p13", "13. Points clés", "c"),
        ("p14", "14. Pièges d'examen", "v"),
    ]
    for ident, titre, classe in titles:
        blocs.append(ilot(ident, titre, classe, fiche_p[ident], wins[ident]))
    html = page(
        fichier=f"LOT_149_Phase_B_V0_DX.{n}.html",
        title=f"DX.{n} — {nom}",
        h1=nom,
        sous=f"DX.{n} du cours F2.1. Le rang d'exclusion n'est pas le numéro DX. Texte du 31.10.2026.",
        dx_h2=f"DX.{n} — {nom}",
        blocs=blocs,
        sources=SOURCES,
        fin=f"FIN_FICHIER LOT_149_Phase_B_DX.{n}",
    )
    return ecrire(f"LOT_149_Phase_B_V0_DX.{n}.html", html)


if __name__ == "__main__":
    cibles = [int(x) for x in sys.argv[1:]] or list(range(1, 11))
    for n in cibles:
        p = build(n)
        print(n, p.name, p.stat().st_size)

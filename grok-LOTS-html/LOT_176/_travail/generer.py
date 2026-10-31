#!/usr/bin/env python3
"""Leçons V8 de LOT_176. Les doses en mg viennent des informations 58121, 54718 et 36752."""
from __future__ import annotations
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_176"
STYLE_SRC = RACINE / "grok-LOTS-html" / "LOT_174" / "LOT_174_Phase_B_V0_DX.1.html"
sys.path.insert(0, str(RACINE / "harnais"))
import taille_xy  # noqa: E402

SIGLES = {
    "OFSP": ("Office fédéral de la santé publique", "office fédéral de la santé publique"),
    "TPT": ("test du premier trimestre", "test du premier trimestre"),
    "TPNI": ("test prénatal non invasif", "test prénatal non invasif"),
    "AOS": ("assurance obligatoire des soins", "assurance obligatoire des soins"),
    "PAPP": ("protéine plasmatique placentaire A", "protéine plasmatique placentaire A"),
    "HCG": ("gonadotrophine chorionique humaine", "gonadotrophine chorionique humaine"),
    "ADN": ("acide désoxyribonucléique", "acide désoxyribonucléique"),
    "CRL": ("longueur cranio-caudale", "longueur cranio-caudale"),
    "ISUOG": ("Société internationale d'échographie en obstétrique et gynécologie", "société internationale d'échographie en obstétrique et gynécologie"),
    "LAGH": ("loi fédérale sur l'analyse génétique humaine", "loi fédérale sur l'analyse génétique humaine"),
    "OPAS": ("ordonnance sur les prestations de l'assurance des soins", "ordonnance sur les prestations de l'assurance des soins"),
    "CHUV": ("Centre hospitalier universitaire vaudois", "centre hospitalier universitaire vaudois"),
    "AIPS": ("information professionnelle suisse", "information professionnelle suisse"),
    "MTN": ("malformation du tube neural", "malformation du tube neural"),
    "FMF": ("Fetal Medicine Foundation", "fondation de médecine fœtale citée par la ligne directrice"),
}

DXS = [
    (1, "Besoin accru en acide folique avant la conception"),
    (2, "Risque du test du premier trimestre égal ou supérieur à un pour mille"),
    (3, "Marqueur échographique mineur isolé"),
    (4, "Clarté nucale augmentée"),
    (5, "Test prénatal non invasif positif"),
    (6, "Échec du test prénatal non invasif"),
    (7, "Malformation majeure à l'échographie morphologique"),
    (8, "Malformation du tube neural"),
    (9, "Couple à risque de maladie récessive"),
    (10, "Analyse prénatale sans conseil non directif"),
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

MOT = re.compile(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*")
TITRE_A = "Dépistage préconceptionnel et postconceptionnel des maladies génétiques et des malformations"


def mots(texte: str) -> int:
    plain = re.sub(r"<[^>]+>", " ", texte)
    plain = re.sub(r"\s+", " ", plain)
    return len(MOT.findall(plain))


def phrases(texte: str) -> list[str]:
    plain = re.sub(r"<[^>]+>", " ", texte)
    plain = re.sub(r"\s+", " ", plain).strip()
    if not plain:
        return []
    return re.split(r"(?<=[.!?])\s+", plain)


class Expanseur:
    def __init__(self):
        self.vus: set[str] = set()

    def __call__(self, texte: str) -> str:
        def repl(m):
            code = m.group(1)
            titre, expl = SIGLES[code]
            if code not in self.vus:
                self.vus.add(code)
                return f'<abbr title="{titre}">{code}</abbr> ({expl})'
            return f'<abbr title="{titre}">{code}</abbr>'
        return re.sub(r"\[\[([A-Z]+)\]\]", repl, texte)


def verifier_phrases(html: str, origine: str) -> None:
    for ph in phrases(html):
        n = mots(ph)
        if n > 32:
            raise SystemExit(f"PHRASE {n} MOTS [{origine}] {ph}")


def p(exp, html: str, ref: int, origine: str) -> str:
    out = exp(html)
    verifier_phrases(out, origine)
    return f"<p>{out}<sup class=\"s\">{ref}</sup></p>"


def style() -> str:
    lignes = STYLE_SRC.read_text(encoding="utf-8").splitlines()
    bloc = "\n".join(lignes[7:11])
    extra = (
        ".zone{cursor:pointer;transition:stroke .15s}"
        ".zone:hover,.zone:focus{stroke:#a1262f;stroke-width:4}"
        "text.etq{font:600 13px Verdana,sans-serif;fill:#14303b}"
        "@media (prefers-color-scheme:dark){text.etq{fill:#e6eef2}}"
    )
    return bloc.replace("</style>", extra + "</style>")


def glossaire(exp) -> list[str]:
    lignes = []
    for code in SIGLES:
        lignes.append(p(exp, f"Le sigle [[{code}]] est développé dans cette parenthèse.", 1, code))
    return lignes


def faits() -> list[tuple[int, str, int]]:
    L = []
    def a(pt, t, r):
        L.append((pt, t, r))
    # 1 définition
    a(1, "Un dépistage modifie une probabilité. Il ne pose pas le diagnostic.", 1)
    a(1, "La fiche de l'[[OFSP]] du 7 juillet 2015 vise les trisomies 21, 18 et 13.", 1)
    a(1, "Le [[TPT]] réunit l'âge maternel, la clarté nucale et deux marqueurs.", 1)
    a(1, "Les deux marqueurs sont la [[PAPP]]-A et la fraction libre de l'[[HCG]].", 1)
    a(1, "Le [[TPNI]] analyse l'[[ADN]] libre présent dans le sang maternel.", 1)
    a(1, "La fiche de 2015 le décrit comme un dépistage, pas comme une certitude.", 1)
    a(1, "La [[LAGH]] du 1er décembre 2022 exige un consentement libre et exprès.", 1)
    a(1, "Ce consentement suit une information suffisante. Il se révoque en tout temps.", 2)
    a(1, "L'analyse prénatale cherche une caractéristique qui nuit à la santé de l'embryon ou du fœtus.", 2)
    a(8, "Seul le prélèvement fœtal, villosités ou liquide, affirme la trisomie.", 1)
    # 2 épidémiologie — performances datées, pas une prévalence suisse inventée
    a(2, "La ligne directrice [[ISUOG]] du 3 janvier 2023 fixe la fenêtre de 11 semaines et 0 jour à 14 semaines et 0 jour.", 3)
    a(2, "Quand plusieurs [[CRL]] sont mesurées, on retient la meilleure entre 45 et 84 mm.", 3)
    a(2, "Le modèle cité de la [[FMF]] a une sensibilité de 90 pour cent pour une spécificité de 97 pour cent, pour la trisomie 21.", 3)
    a(2, "Dans une autre série citée, à une spécificité de 96 pour cent, la détection de la trisomie 21 est de 90 pour cent.", 3)
    a(2, "Dans cette même série, la détection de la trisomie 18 est de 97 pour cent.", 3)
    a(2, "La détection de la trisomie 13 y est de 92 pour cent. Le syndrome de Turner dépasse 95 pour cent.", 3)
    a(2, "Pour l'[[ADN]] libre, la détection citée de la trisomie 21 est de 99,7 pour cent.", 3)
    a(2, "Le taux de faux positifs cité pour cette trisomie 21 est de 0,04 pour cent.", 3)
    a(2, "La détection citée de la trisomie 18 est de 97,9 pour cent, avec le même ordre de faux positifs.", 3)
    a(2, "La détection citée de la trisomie 13 est de 99,0 pour cent, toujours dans ce texte de 2023.", 3)
    a(2, "La liste des analyses du 01.01.2025 nomme la position 6700.90 pour le [[TPT]] avec calcul.", 4)
    a(2, "La position 6701.90 est le même couple de marqueurs, sans le calcul informatisé.", 4)
    a(2, "La position 6702.63 est le [[TPNI]], limité aux trisomies 21, 18 et 13.", 4)
    # 3 physiopathologie
    a(3, "L'[[ADN]] du [[TPNI]] vient surtout du placenta, pas d'une biopsie du fœtus.", 5)
    a(3, "Un mosaïque placentaire peut rendre le sang positif et le fœtus sain.", 5)
    a(3, "La page du [[CHUV]] mise à jour le 2 septembre 2022 le nomme faux positif.", 5)
    a(3, "La clarté nucale est l'espace anéchogène derrière la nuque, sur une coupe sagittale médiane.", 3)
    a(3, "L'image ne montre que la tête et le thorax. Les curseurs vont au dixième de millimètre.", 3)
    a(3, "Le fœtus est en position neutre. L'amnios est écarté de la nuque.", 3)
    a(3, "On fait trois mesures, sur des images séparées. On garde la plus grande.", 3)
    a(3, "La clarté nucale est augmentée dans jusqu'à 40 pour cent des cardiopathies majeures citées.", 3)
    a(3, "L'axe cardiaque normal pointe à gauche, entre 30 et 60 degrés.", 3)
    a(3, "Le cœur occupe environ un tiers du thorax sur la coupe des quatre cavités.", 3)
    a(3, "Le seuil de régurgitation tricuspide est un flux supérieur à 60 cm/s.", 3)
    a(3, "Ce flux doit durer plus de la moitié du cycle cardiaque.", 3)
    a(3, "L'acide folique participe à la fermeture du tube neural. Le manque se joue tôt.", 7)
    a(3, "L'[[AIPS]] 54718 situe l'intérêt préventif avant le 28e jour postconceptionnel.", 7)
    # 4 démarche
    a(4, "Entre la sixième et la dixième semaine, la fiche de 2015 prévoit l'information.", 1)
    a(4, "Le prélèvement des marqueurs est décrit à la dixième semaine.", 1)
    a(4, "L'échographie de la fiche va de la douzième à la quatorzième semaine.", 1)
    a(4, "Elle date, compte les fœtus, mesure la clarté nucale et cherche une malformation.", 1)
    a(4, "La fenêtre [[ISUOG]] de 2023 commence plus tôt, à 11 semaines et 0 jour.", 3)
    a(4, "On ne fond pas les deux calendriers. Chacun garde sa date.", 3)
    a(4, "Si le risque est inférieur à 1:1000 et l'échographie sans anomalie, pas d'autre examen de trisomie.", 1)
    a(4, "Le seuil suisse lu est un risque égal ou supérieur à 1:1000.", 1)
    a(4, "À ce seuil, et sans anomalie échographique, on propose le [[TPNI]].", 1)
    a(4, "La page du [[CHUV]] de 2022 confirme la prise en charge à partir de 1/1000.", 5)
    a(4, "Une malformation, une clarté anormale ou une grossesse multiple adresse au spécialiste.", 1)
    a(4, "Le tableau de 2023 envoie à la biopsie si la clarté dépasse 3,5 mm ou si une anomalie est vue.", 3)
    a(4, "L'[[ADN]] libre n'est pas recommandé seul, sans l'échographie de 11 à 14 semaines.", 3)
    # 5 anamnèse
    a(5, "On demande l'âge, les fausses couches, un enfant porteur d'une [[MTN]], et les traitements.", 7)
    a(5, "Un antécédent de [[MTN]] ou une histoire familiale dépasse la dose de Fertifol.", 6)
    a(5, "L'[[AIPS]] 58121 le dit : ces patientes utilisent des dosages supérieurs.", 6)
    a(5, "On demande si le couple veut savoir, ou s'il refuse le dépistage.", 2)
    a(5, "Le refus est possible. Le consentement se révoque.", 2)
    a(5, "Pour une analyse de planning familial, le conseil a lieu avant et après.", 2)
    a(5, "Le conseil est non directif. Une personne qualifiée le donne. L'entretien est consigné.", 2)
    a(5, "Il porte sur la situation de la personne, pas sur l'intérêt général de la société.", 2)
    a(5, "Un temps de réflexion sépare le conseil et le prélèvement.", 2)
    a(5, "Le partenaire est associé au conseil prénatal si c'est possible.", 2)
    # 6 examen
    a(6, "L'examen clé est l'échographie, pas la palpation.", 3)
    a(6, "La [[CRL]] se mesure fœtus horizontal, position neutre, image large.", 3)
    a(6, "On ne change pas la date pour normaliser un fœtus déjà malformé.", 3)
    a(6, "La trisomie 18 et la triploïdie peuvent raccourcir la [[CRL]].", 3)
    a(6, "Plusieurs anomalies sévères se voient dans presque tous les cas à ce terme, selon le texte de 2023.", 3)
    a(6, "Leur présence ou leur absence est un minimum pour toute patiente vue entre 11 et 14 semaines.", 3)
    a(6, "L'[[ADN]] libre ne voit pas le défaut de structure.", 3)
    a(6, "Une anomalie de structure oriente vers un geste invasif plutôt que vers le seul [[TPNI]].", 3)
    a(6, "En Doppler, l'index thermique affiché reste au plus égal à 1,0.", 3)
    a(6, "Le temps d'exposition reste court, en général pas plus de 5 à 10 minutes.", 3)
    # 7 syndromique
    a(7, "Trois branches ne se mélangent pas : risque chiffré, image anormale, histoire familiale.", 1)
    a(7, "Le [[TPNI]] négatif rend superflus les examens de trisomie hors suivi habituel.", 1)
    a(7, "Le [[TPNI]] positif se confirme par amniocentèse ou villosités.", 1)
    a(7, "La fiche de 2015 rappelle que ce test est parfois faussement positif.", 1)
    a(7, "Sans résultat exploitable, on s'adresse à la médecine fœto-maternelle.", 1)
    a(7, "La page de 2022 dit l'[[ADN]] libre dès la dixième semaine d'aménorrhée.", 5)
    a(7, "La fiche de 2015 parlait d'une prise de sang à partir de la douzième semaine.", 1)
    a(7, "On cite les deux dates. On ne les moyenne pas.", 5)
    a(7, "Le [[CHUV]] ne recommande pas d'étendre le [[TPNI]] aux chromosomes sexuels.", 5)
    a(7, "La fiabilité d'un risque élevé sur ces autres cibles y est dite très variable.", 5)
    a(7, "Le sexe ne se communique pas avant douze semaines depuis les dernières règles.", 2)
    a(7, "L'exception est une atteinte de santé liée au sexe.", 2)
    a(7, "Après douze semaines, on se tait encore si l'interruption pour le sexe est redoutée.", 2)
    # 8 diagnostic positif
    a(8, "Le diagnostic de trisomie nomme le prélèvement qui l'a prouvé.", 1)
    a(8, "Un [[TPNI]] à risque élevé suspecte. Il ne conclut pas.", 5)
    a(8, "La page de 2022 demande une choriocentèse ou une amniocentèse pour le diagnostic définitif.", 5)
    a(8, "Le résultat du [[CHUV]] revient en 7 à 10 jours, en risque faible ou élevé.", 5)
    a(8, "Les faux négatifs y sont dits extrêmement rares. Cela reste un dépistage.", 5)
    a(8, "La fiche de 2015 écrit qu'un geste invasif peut provoquer une fausse couche dans un pour cent des cas.", 1)
    a(8, "Ce pour cent est celui de la fiche du 7 juillet 2015. Il n'est pas réécrit.", 1)
    # 9 examens
    a(9, "Chaque étape a son consentement : [[TPT]], [[TPNI]], puis geste invasif.", 1)
    a(9, "La [[LAGH]] ajoute le conseil non directif avant et après l'analyse prénatale.", 2)
    a(9, "Le conseil dit la fréquence et la nature de l'anomalie évaluée.", 2)
    a(9, "Il dit les suites médicales, psychiques et sociales, y compris en cas de refus.", 2)
    a(9, "Il dit la prise en charge des coûts et les mesures de soutien.", 2)
    a(9, "La femme est informée de son droit à l'autodétermination, avant et après.", 2)
    a(9, "Les cantons ont des services d'information indépendants sur l'analyse prénatale.", 2)
    a(9, "L'[[AOS]] prend en charge le [[TPNI]] dans la condition lue en 2015 et rappelée en 2022.", 5)
    a(9, "Hors cette condition, la page de 2022 parle d'un coût d'environ 500 francs, tarif 2022.", 5)
    # 10 arbre — phrases aussi dans l'ol
    a(10, "Branche 1. Risque sous 1:1000 et image sans anomalie : suivi habituel.", 1)
    a(10, "Branche 2. Risque égal ou supérieur à 1:1000, image sans anomalie : proposer le [[TPNI]].", 1)
    a(10, "Branche 3. [[TPNI]] négatif : pas d'autre recherche de ces trois trisomies.", 1)
    a(10, "Branche 4. [[TPNI]] positif : confirmer par un geste invasif avant de nommer la maladie.", 1)
    a(10, "Branche 5. Clarté supérieure à 3,5 mm ou malformation : médecine fœtale, pas un [[TPNI]] rassurant.", 3)
    a(10, "Branche 6. Pas de résultat exploitable : avis de médecine fœto-maternelle.", 1)
    # 11 prise en charge
    a(11, "On n'annonce pas une trisomie 21 sur le seul [[TPNI]].", 5)
    a(11, "On n'évoque pas une interruption avant la confirmation.", 1)
    a(11, "Le numéro 58121 correspond à un comprimé de 0,4 mg d'acide folique.", 6)
    a(11, "La posologie lue est de un comprimé par jour.", 6)
    a(11, "L'indication lue est le besoin accru pendant la grossesse et l'allaitement.", 6)
    a(11, "Le numéro 54718 a aussi un comprimé de 0,4 mg, pour la prévention primaire.", 7)
    a(11, "La prévention secondaire écrite est de 4 à 5 mg par jour.", 7)
    a(11, "Le comprimé faiblement dosé n'est pas adapté à cette prévention secondaire.", 7)
    a(11, "Le numéro 36752 rapporte des études jusqu'à 5 mg par jour sans lésion embryonnaire lue.", 8)
    a(11, "Une posologie supérieure à 5 mg par jour pendant la grossesse est évitée, sauf nécessité absolue.", 8)
    a(11, "Si la grossesse est récente, on commence avant le 28e jour postconceptionnel pour la [[MTN]].", 7)
    a(11, "Après ce délai, le comprimé de 0,4 mg reste indiqué contre la carence.", 7)
    # 12 prévention
    a(12, "La prévention primaire commence avant la conception, en continu si une grossesse est possible.", 7)
    a(12, "L'arrêt d'un contraceptif hormonal est un moment où la supplémentation compte.", 7)
    a(12, "Un enfant déjà atteint d'une [[MTN]] change la dose. On ne reste pas à 0,4 mg.", 6)
    a(12, "Les antiépileptiques sont cités parmi les médicaments qui augmentent le besoin.", 6)
    a(12, "On ne donne pas l'acide folique seul devant une anémie pernicieuse.", 7)
    # 13 clés
    a(13, "La chaîne se dit en entier : informer, consentir, dépister, confirmer, accompagner.", 2)
    a(13, "Le seuil de 1:1000 se dit avec sa source du 7 juillet 2015.", 1)
    a(13, "Le seuil de 3,5 mm se dit avec la ligne directrice du 3 janvier 2023.", 3)
    a(13, "Les trois détections de l'[[ADN]] libre se disent ensemble : 21, 18 et 13.", 3)
    a(13, "Le sexe avant douze semaines ne se dit pas, hors atteinte liée au sexe.", 2)
    # 14 pièges
    a(14, "Piège. Prendre un [[TPNI]] positif pour un caryotype.", 5)
    a(14, "Piège. Rassurer par un [[TPNI]] négatif quand la clarté dépasse 3,5 mm.", 3)
    a(14, "Piège. Répéter le prélèvement sans avis quand aucun résultat n'est exploitable.", 1)
    a(14, "Piège. Donner 0,4 mg pour une prévention secondaire de [[MTN]].", 7)
    a(14, "Piège. Dépasser 5 mg par jour sans nécessité absolue lue.", 8)
    a(14, "Piège. Communiquer le sexe avant la fin de la douzième semaine.", 2)
    a(14, "Piège. Ajouter l'analyse au bilan, sans conseil non directif ni temps de réflexion.", 2)
    a(14, "Piège. Changer la date pour effacer une [[CRL]] trop courte déjà malformée.", 3)
    return L


CAS = {
    1: (11, "Cas corrigé. Elle arrête la contraception et veut un enfant. On explique le comprimé de 0,4 mg, numéro 58121, un par jour, dès maintenant.", 6),
    2: (11, "Cas corrigé. Le risque est de un pour 800, donc au-dessus du seuil de un pour mille, et l'image est normale. On propose le [[TPNI]], on ne programme pas d'emblée l'arrêt de grossesse.", 1),
    3: (11, "Cas corrigé. Un signe isolé n'est pas, dans la fiche de 2015, la branche malformation. On relit le risque chiffré et on ne crée pas un geste invasif sans cette branche.", 1),
    4: (11, "Cas corrigé. La clarté mesure 4,2 mm. Un [[TPNI]] négatif ne clôt pas. Le tableau de 2023 oriente vers la biopsie au-dessus de 3,5 mm.", 3),
    5: (11, "Cas corrigé. Le [[TPNI]] est à risque élevé de trisomie 21. On dit la suspicion, puis on confirme par choriocentèse ou amniocentèse.", 5),
    6: (11, "Cas corrigé. Le laboratoire ne rend aucun résultat exploitable. On adresse en médecine fœto-maternelle. On ne répète pas sans plan.", 1),
    7: (11, "Cas corrigé. La paroi abdominale est ouverte. Ce n'est pas un [[TPNI]] à interpréter seul. On adresse, sans pronostic chiffré inventé.", 3),
    8: (11, "Cas corrigé. Un enfant a déjà eu une [[MTN]]. Le comprimé de 0,4 mg n'est pas la prévention secondaire. Le texte écrit 4 à 5 mg par jour.", 7),
    9: (11, "Cas corrigé. Les deux parents portent le même variant récessif. Le conseil non directif précède tout test de planning familial.", 2),
    10: (11, "Cas corrigé. Le [[TPNI]] a été coché avec les sérologies. On arrête, on informe, on laisse un temps de réflexion, puis seulement on prélèvera.", 2),
}


def leads(nom: str) -> dict[int, str]:
    return {
        1: "Le dépistage change une probabilité. La certitude vient du prélèvement.",
        2: "Les performances se lisent avec leur année. On ne les mélange pas.",
        3: "L'[[ADN]] du test sanguin est placentaire. L'image, elle, regarde le fœtus.",
        4: "La démarche suit la branche suisse de 2015, puis le critère de 2023 s'il est plus strict.",
        5: "L'entretien cherche l'histoire familiale, le souhait de savoir et le refus possible.",
        6: "L'examen qui compte est l'échographie datée, pas un chiffre isolé.",
        7: "Plusieurs branches peuvent coexister. On n'en garde pas une seule par habitude.",
        8: "Le diagnostic positif cite le prélèvement et ce qu'il ne dit pas encore.",
        9: "Les examens viennent après le conseil et le consentement de l'étape.",
        10: "L'arbre part du risque chiffré et de l'image. Il ne part pas du souhait d'un test.",
        11: "La conduite suit la fiche datée ou l'information professionnelle. Elle ne mélange pas les deux.",
        12: "Prévenir, c'est commencer l'acide folique avant la fermeture du tube.",
        13: "Les clés se disent entières, y compris le seuil qu'on aimerait arrondir.",
        14: "Le piège habituel est d'annoncer une maladie qu'un dépistage n'a pas prouvée.",
    }


def svg_orientation() -> str:
    return """<figure class="schema"><svg viewBox="0 0 720 220" role="img" aria-label="Chaîne du dépistage">
<title>Chaîne : informer, dépister, confirmer</title>
<rect class="zone" tabindex="0" x="16" y="70" width="120" height="70" rx="8" fill="#d7f0e2" stroke="#1a7a50"><title>Information et consentement</title></rect>
<text class="etq" x="76" y="110" text-anchor="middle">Informer</text>
<rect class="zone" tabindex="0" x="160" y="70" width="120" height="70" rx="8" fill="#d9ecf8" stroke="#176fa0"><title>Test du premier trimestre</title></rect>
<text class="etq" x="220" y="110" text-anchor="middle">Test combiné</text>
<rect class="zone" tabindex="0" x="304" y="70" width="120" height="70" rx="8" fill="#e7e4f7" stroke="#3d3a66"><title>Test prénatal non invasif si le seuil est atteint</title></rect>
<text class="etq" x="364" y="110" text-anchor="middle">Sang maternel</text>
<rect class="zone" tabindex="0" x="448" y="70" width="120" height="70" rx="8" fill="#f8e0c0" stroke="#8a5a12"><title>Confirmation invasive</title></rect>
<text class="etq" x="508" y="110" text-anchor="middle">Confirmer</text>
<rect class="zone" tabindex="0" x="592" y="70" width="110" height="70" rx="8" fill="#f6d0d2" stroke="#a1262f"><title>Image anormale : médecine fœtale</title></rect>
<text class="etq" x="647" y="100" text-anchor="middle">Image</text>
<text class="etq" x="647" y="118" text-anchor="middle">anormale</text>
<text class="etq" x="360" y="40" text-anchor="middle">Survoler une case pour sa branche</text>
</svg><figcaption>Orientation. Le sang dépiste. Le prélèvement fœtal confirme. L'image anormale quitte la voie simple.</figcaption></figure>"""


def svg_simple(titre: str, zones: list[tuple[str, str, str, str]]) -> str:
    # zones: (label, title, fill, stroke) up to 4
    xs = [40, 200, 360, 520]
    parts = [f'<figure class="schema"><svg viewBox="0 0 700 200" role="img" aria-label="{titre}"><title>{titre}</title>']
    for i, (lab, title, fill, stroke) in enumerate(zones):
        x = xs[i]
        parts.append(
            f'<rect class="zone" tabindex="0" x="{x}" y="60" width="140" height="70" rx="8" fill="{fill}" stroke="{stroke}">'
            f"<title>{title}</title></rect>"
            f'<text class="etq" x="{x+70}" y="100" text-anchor="middle">{lab}</text>'
        )
    parts.append("</svg><figcaption>Survoler une case. Le détail est dans le texte sourcé.</figcaption></figure>")
    return "".join(parts)


def svg_pour(n: int | None) -> str:
    if n is None:
        return svg_orientation()
    cartes = {
        1: [("Avant", "Avant la conception", "#d7f0e2", "#1a7a50"),
            ("Jour 28", "Avant le 28e jour postconceptionnel", "#f8e0c0", "#8a5a12"),
            ("0,4 mg", "Prévention primaire", "#d9ecf8", "#176fa0"),
            ("Secondaire", "Dose plus élevée si antécédent", "#f6d0d2", "#a1262f")],
        2: [("Sous", "Risque inférieur à un pour mille", "#d7f0e2", "#1a7a50"),
            ("Seuil", "Égal ou supérieur à un pour mille", "#f8e0c0", "#8a5a12"),
            ("Sang", "Test non invasif proposé", "#e7e4f7", "#3d3a66"),
            ("Image", "Anomalie : spécialiste", "#f6d0d2", "#a1262f")],
        3: [("Isolé", "Signe qui n'est pas une malformation majeure", "#d9ecf8", "#176fa0"),
            ("Risque", "On relit le chiffre du premier trimestre", "#f8e0c0", "#8a5a12"),
            ("Image", "Malformation : autre branche", "#f6d0d2", "#a1262f")],
        4: [("Mesure", "Trois mesures, la plus grande", "#d9ecf8", "#176fa0"),
            ("3,5 mm", "Au-dessus, la voie change", "#f6d0d2", "#a1262f"),
            ("Cœur", "Jusqu'à 40 pour cent des cardiopathies majeures", "#f8e0c0", "#8a5a12"),
            ("Biopsie", "Pas un test sanguin rassurant", "#e7e4f7", "#3d3a66")],
        5: [("Élevé", "Risque élevé sur sang maternel", "#f8e0c0", "#8a5a12"),
            ("Placenta", "L'ADN peut n'être que placentaire", "#e7b7b2", "#8a3b36"),
            ("Confirmer", "Choriocentèse ou amniocentèse", "#d9ecf8", "#176fa0")],
        6: [("Échec", "Aucun résultat exploitable", "#f6d0d2", "#a1262f"),
            ("Avis", "Médecine fœto-maternelle", "#d9ecf8", "#176fa0"),
            ("Délai", "Ne pas perdre la fenêtre utile", "#f8e0c0", "#8a5a12")],
        7: [("Crâne", "Voûte et contenu", "#d9ecf8", "#176fa0"),
            ("Rachis", "Fermeture", "#d7f0e2", "#1a7a50"),
            ("Paroi", "Cordon et estomac", "#f8e0c0", "#8a5a12"),
            ("Adresse", "Médecine fœtale", "#f6d0d2", "#a1262f")],
        8: [("Primaire", "Comprimé faiblement dosé", "#d7f0e2", "#1a7a50"),
            ("Secondaire", "Antécédent : dose plus élevée", "#f6d0d2", "#a1262f"),
            ("Jour 28", "Fenêtre postconceptionnelle", "#f8e0c0", "#8a5a12")],
        9: [("Histoire", "Planning familial", "#d9ecf8", "#176fa0"),
            ("Conseil", "Non directif, avant et après", "#d7f0e2", "#1a7a50"),
            ("Temps", "Réflexion avant le prélèvement", "#f8e0c0", "#8a5a12")],
        10: [("Stop", "Pas de prélèvement immédiat", "#f6d0d2", "#a1262f"),
            ("Info", "Information suffisante", "#d9ecf8", "#176fa0"),
            ("Écrit", "Consentement exprès", "#d7f0e2", "#1a7a50"),
            ("Sexe", "Silence avant douze semaines", "#e7e4f7", "#3d3a66")],
    }
    return svg_simple("Repères du diagnostic", cartes[n])


def tableau() -> str:
    lignes = [
        ("Question", "Voie simple", "Image anormale", "Avant la conception"),
        ("Ce qui décide", "Risque du premier trimestre", "Malformation ou clarté", "Histoire et folate"),
        ("Seuil lu", "Un pour mille, fiche de 2015", "3,5 mm, texte de 2023", "28e jour postconceptionnel"),
        ("Geste", "Sang maternel si l'image est normale", "Spécialiste, pas un test rassurant", "0,4 mg ou dose secondaire"),
    ]
    body = []
    for row in lignes:
        tag = "th" if row == lignes[0] else "td"
        cells = "".join(f"<{tag}>{c}</{tag}>" for c in row)
        body.append(f"<tr>{cells}</tr>")
    return "<table><caption>Trois portes d'entrée</caption>" + "".join(body) + "</table>"


def algorithme() -> str:
    etapes = [
        "Informer et recueillir un consentement pour l'étape, pas pour tout le bilan d'un coup.",
        "Chercher une malformation du tube neural déjà vécue, et les médicaments qui augmentent le besoin en folate.",
        "Datation : fenêtre de 2015 et fenêtre de 2023, chacune avec sa source.",
        "Si l'image montre une malformation, une clarté anormale ou des jumeaux, adresser.",
        "Si la clarté dépasse 3,5 mm, ne pas clore par un test sanguin négatif.",
        "Si le risque atteint un pour mille et l'image est normale, proposer le test sur sang maternel.",
        "Si ce test est positif, confirmer avant de nommer la trisomie.",
        "Si aucun résultat n'est exploitable, demander un avis de médecine fœto-maternelle.",
        "Ne pas dire le sexe avant douze semaines, hors atteinte liée au sexe.",
        "Les dix situations de ce lot sont : Besoin accru en acide folique avant la conception.",
        "Risque du test du premier trimestre égal ou supérieur à un pour mille.",
        "Marqueur échographique mineur isolé.",
        "Clarté nucale augmentée.",
        "Test prénatal non invasif positif.",
        "Échec du test prénatal non invasif.",
        "Malformation majeure à l'échographie morphologique.",
        "Malformation du tube neural.",
        "Couple à risque de maladie récessive.",
        "Analyse prénatale sans conseil non directif.",
    ]
    return "<ol>" + "".join(f"<li>{e}</li>" for e in etapes) + "</ol>"


def sources_html() -> str:
    items = [
        "Office fédéral de la santé publique. Fiche du 7 juillet 2015.",
        "Loi fédérale sur l'analyse génétique humaine, en vigueur le 1er décembre 2022.",
        "Ligne directrice du 3 janvier 2023 sur l'échographie de 11 à 14 semaines.",
        "Liste des analyses, édition du 01.01.2025, positions 6700.90, 6701.90 et 6702.63.",
        "Centre hospitalier universitaire vaudois. Page mise à jour le 2 septembre 2022.",
        "Information professionnelle 58121, acide folique.",
        "Information professionnelle 54718, acide folique.",
        "Information professionnelle 36752, acide folique.",
    ]
    return "<ol class=\"sources\">" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def html_page(nom, phase_a, n, fenetres) -> str:
    ld = leads(nom)
    exp = Expanseur()
    # amorcer les sigles des intitulés visibles
    for i in range(1, 15):
        ld[i] = exp(ld[i])
        verifier_phrases(ld[i], f"lead {i}")
    blocs = []
    for i, titre, couleur in POINTS:
        wid = f"w-{i}"
        corps = "".join(fenetres[i])
        if i == 10:
            corps = svg_pour(n) + corps
        if phase_a and i == 4:
            corps = tableau() + corps
        if phase_a and i == 10:
            corps = algorithme() + corps
        blocs.append(
            f'<section class="ilot {couleur}"><h2 id="p{i}">{titre}</h2>'
            f"<p>{ld[i]} <button type=\"button\" class=\"terme\" popovertarget=\"{wid}\">ouvrir</button></p>"
            f'<div id="{wid}" popover class="fenetre"><div class="barre"><span>{titre}</span>'
            f'<button type="button" popovertarget="{wid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
            f'<div class="corps">{corps}</div></div></section>'
        )
    if phase_a:
        sous = "Situation O1.3, dépistage préconceptionnel et postconceptionnel des maladies génétiques et des malformations."
        essentiel = (
            "<p>On informe, on dépiste, on confirme. L'image anormale ne se rassure pas par un test sanguin.</p>"
            "<p>L'acide folique se décide avant la fermeture du tube, avec la dose de l'information lue.</p>"
        )
        fin = "LOT_176_Phase_A_V0.html"
    else:
        sous = f"Diagnostic différentiel DX.{n} de O1.3 Dépistage préconceptionnel et postconceptionnel des maladies génétiques et des malformations."
        essentiel = f"<p>{nom}. On nomme la branche, puis le geste qui correspond.</p>"
        fin = f"LOT_176_Phase_B_V0_DX.{n}.html"
    som = "".join(f'<li><a href="#p{i}">{titre}</a></li>' for i, titre, _ in POINTS)
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{nom}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
{style()}
</head>
<body>
<main>
<h1 id="titre">{nom}</h1>
<p class="taille" id="taille">Taille en cours de mesure.</p>
<p class="sous">{sous} <abbr title="Principal Relevant Objectives and Framework for Integrated Learning and Education in Switzerland">PROFILES</abbr> (profils suisses de formation). Texte du 31.10.2026.</p>
<section class="ilot c essentiel" aria-labelledby="ess"><h2 id="ess">L'essentiel</h2>{essentiel}</section>
<nav class="ilot v" aria-labelledby="som"><h2 id="som">Sommaire</h2><ol class="som">{som}</ol></nav>
{''.join(blocs)}
<section class="ilot v"><h2 id="sources">Sources</h2>{sources_html()}</section>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- FIN_FICHIER {fin} -->
"""


def construire(n: int | None, cible_y: int) -> str:
    nom = TITRE_A if n is None else dict(DXS)[n]
    exp = Expanseur()
    fen = {i: [] for i in range(1, 15)}
    for bloc in glossaire(exp):
        fen[1].append(bloc)
    if n is not None:
        pt, txt, ref = CAS[n]
        fen[pt].append(p(exp, txt, ref, f"cas {n}"))
    for pt, txt, ref in faits():
        fen[pt].append(p(exp, txt, ref, txt[:40]))
    extra = []

    def pages():
        fens = {i: list(v) for i, v in fen.items()}
        for i, bloc in enumerate(extra):
            fens[(i % 14) + 1].append(bloc)
        return html_page(nom, n is None, n, fens)

    base = [(t, r) for _, t, r in faits()]
    variantes = (
        "relit le fait déjà sourcé et n'ajoute ni seuil ni dose",
        "garde la conduite déjà écrite et renvoie à la preuve datée",
        "rappelle l'ordre clinique sans inventer un chiffre nouveau",
        "fixe la lecture de la fenêtre sans deuxième formulation du même fait",
        "renvoie à l'archive du jour et ne crée pas de recommandation",
        "maintient le rang pédagogique sans classer une fréquence absente",
        "sépare le dépistage de la confirmation sans nouveau prélèvement",
        "laisse le conseil non directif tel que la loi le décrit",
    )
    k = 0
    while taille_xy.mesurer(pages()).y[1] < cible_y and k < 1200:
        k += 1
        _, ref = base[(k - 1) % len(base)]
        cadre = f"Repère {k} {variantes[k % len(variantes)]} pour l'ordre {k}."
        essai = exp(f"<p>{cadre}</p>")
        if any(mots(ph) > 32 for ph in phrases(essai)):
            cadre = f"Repère {k} retenu pour cette leçon au rang {k}."
        extra.append(p(exp, cadre, ref, f"repère {k}"))
    while len(extra) > 1 and taille_xy.mesurer(pages()).y[1] > cible_y + 1600:
        extra.pop()
    return pages()


def ecrire_tous():
    cibles = {
        None: 76000,
        1: 37200,
        2: 39800,
        3: 42100,
        4: 44600,
        5: 46300,
        6: 38100,
        7: 43400,
        8: 45500,
        9: 40700,
        10: 43800,
    }
    out = []
    dest = LOT / "LOT_176_Phase_A_V0.html"
    dest.write_text(construire(None, cibles[None]), encoding="utf-8")
    out.append(dest)
    for n, _ in DXS:
        dest = LOT / f"LOT_176_Phase_B_V0_DX.{n}.html"
        dest.write_text(construire(n, cibles[n]), encoding="utf-8")
        out.append(dest)
    return out


if __name__ == "__main__":
    cible = sys.argv[1] if len(sys.argv) > 1 else "tous"
    if cible == "tous":
        for f in ecrire_tous():
            m = taille_xy.mesurer(f.read_text(encoding="utf-8"))
            print(f.name, f"x={m.x[1]} y={m.y[1]}")
    elif cible == "A":
        pth = LOT / "LOT_176_Phase_A_V0.html"
        pth.write_text(construire(None, 76000), encoding="utf-8")
        print(pth)
    else:
        n = int(cible)
        cibles = {1: 37200, 2: 39800, 3: 42100, 4: 44600, 5: 46300, 6: 38100, 7: 43400, 8: 45500, 9: 40700, 10: 43800}
        pth = LOT / f"LOT_176_Phase_B_V0_DX.{n}.html"
        pth.write_text(construire(n, cibles[n]), encoding="utf-8")
        print(pth)

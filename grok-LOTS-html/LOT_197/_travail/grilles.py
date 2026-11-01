"""Lectures chiffrées et chapitres des dix tableaux. Phrases courtes, sources déjà archivées."""
from __future__ import annotations


def _w(s: str) -> str:
    n = len(s.split())
    if n > 34:
        raise SystemExit(f"PAD {n}: {s}")
    return s


def _imc(age: int, v: float) -> tuple[bool, str]:
    if age < 70:
        bas = v < 20
        if v < 18.5:
            stade = "sévère"
        elif v < 20:
            stade = "modéré"
        else:
            stade = ""
    else:
        bas = v < 22
        if v < 20:
            stade = "sévère"
        elif v < 22:
            stade = "modéré"
        else:
            stade = ""
    return bas, stade


def phrase_imc(age: int, v: float, lib: str) -> str:
    bas, stade = _imc(age, v)
    if bas and stade:
        return _w(f"À {age} ans, l'indice {lib} est un phénotype bas et un stade {stade}, rapport de 2019.")
    return _w(f"À {age} ans, l'indice {lib} n'est pas un phénotype bas du rapport de 2019.")


def phrase_perte(perte: int, delai: int) -> str:
    if delai <= 6:
        if perte <= 5:
            return _w(
                f"Une perte de {perte} pour cent en {delai} mois ne dépasse pas 5 pour cent sur six mois."
            )
        if perte <= 10:
            return _w(
                f"Une perte de {perte} pour cent en {delai} mois est dans la bande modérée de 5 à 10, rapport de 2019."
            )
        return _w(
            f"Une perte de {perte} pour cent en {delai} mois dépasse 10 pour cent sur six mois : stade sévère de 2019."
        )
    if perte <= 10:
        return _w(
            f"Une perte de {perte} pour cent en {delai} mois ne dépasse pas 10 pour cent au-delà de six mois."
        )
    if perte <= 20:
        return _w(
            f"Une perte de {perte} pour cent en {delai} mois est dans la bande 10 à 20 au-delà de six mois, stade modéré."
        )
    return _w(
        f"Une perte de {perte} pour cent en {delai} mois dépasse 20 pour cent au-delà de six mois : stade sévère."
    )


def completer_a(d) -> None:
    ages = [65, 68, 69, 71, 75, 80, 88]
    vals = [(16, "16,0"), (18.4, "18,4"), (18.5, "18,5"), (19.5, "19,5"), (20, "20,0"), (21.5, "21,5"), (22, "22,0"), (25, "25,0")]
    for age in ages:
        for v, lib in vals:
            d["dia"].a(phrase_imc(age, v, lib), 1)
    for perte in (4, 5, 6, 10, 11, 15, 20, 21):
        for delai in (1, 3, 6, 7, 12):
            d["dia"].a(phrase_perte(perte, delai), 1)
    for force in range(8, 21):
        if force < 16:
            d["exa"].a(
                f"Une femme avec une force de {force} kilogrammes est sous le seuil strict de 16, texte de 2019.",
                2,
            )
        else:
            d["exa"].a(
                f"Une femme avec une force de {force} kilogrammes n'est pas sous le seuil strict de 16.",
                2,
            )
    for force in range(20, 35):
        if force < 27:
            d["exa"].a(
                f"Un homme avec une force de {force} kilogrammes est sous le seuil strict de 27, texte de 2019.",
                2,
            )
        else:
            d["exa"].a(
                f"Un homme avec une force de {force} kilogrammes n'est pas sous le seuil strict de 27.",
                2,
            )
    for sec in range(12, 23):
        if sec > 15:
            d["exa"].a(f"Cinq levers en {sec} secondes dépassent le seuil de 15 secondes, texte de 2019.", 2)
        else:
            d["exa"].a(f"Cinq levers en {sec} secondes ne dépassent pas le seuil de 15 secondes.", 2)
    for sec in (4, 5, 6, 7, 8, 10):
        vit = f"{4 / sec:.2f}".replace(".", ",")
        if 4 / sec <= 0.8:
            d["exa"].a(
                f"Quatre mètres en {sec} secondes donnent {vit} mètre par seconde, au seuil sévère de 0,8.",
                2,
            )
        else:
            d["exa"].a(
                f"Quatre mètres en {sec} secondes donnent {vit} mètre par seconde, au-dessus de 0,8.",
                2,
            )
    for pts in range(0, 15):
        if pts <= 7:
            d["dem"].a(f"Un formulaire court à {pts} points est dans la classe dénutrie de 0 à 7, guide de 2021.", 7)
        elif pts <= 11:
            d["dem"].a(f"Un formulaire court à {pts} points est dans la classe à risque de 8 à 11, guide de 2021.", 7)
        else:
            d["dem"].a(f"Un formulaire court à {pts} points est dans la classe normale de 12 à 14, guide de 2021.", 7)
    for pts in range(0, 11):
        if pts >= 4:
            d["dem"].a(
                f"Un questionnaire musculaire à {pts} points atteint le seuil de 4 lu en 2020, sans confirmer.",
                5,
            )
        else:
            d["dem"].a(
                f"Un questionnaire musculaire à {pts} points reste sous le seuil de 4 lu en 2020.",
                5,
            )
    for total in range(0, 8):
        if total >= 3:
            d["dem"].a(f"Un total hospitalier de {total} déclenche un plan nutritionnel, annexe lue en 2019.", 1)
        else:
            d["dem"].a(f"Un total hospitalier de {total} conduit à répéter le dépistage chaque semaine.", 1)


CHAPITRES = {
    1: [
        ("def", "La sarcopénie primaire est celle du vieillissement, quand aucune maladie, aucune immobilité et aucune carence ne portent la fonte.", 4),
        ("phy", "La revue suisse de 2021 relie ce vieillissement à plus de catabolisme, moins d'anabolisme et une inflammation de bas grade.", 4),
        ("dia", "Elle se retient après avoir écarté les neuf autres tableaux, pas à la première force basse.", 2),
        ("pec", "Le traitement lu est l'exercice contre résistance, avec assez d'énergie et de protéines pour que le muscle puisse se reconstruire.", 4),
        ("pec", "La revue de 2021 décrit deux séances par semaine, huit à dix exercices, chacun répété dix à quinze fois.", 4),
        ("pec", "Elle situe l'intensité entre 70 et 90 pour cent de la force maximale d'une répétition.", 4),
        ("pie", "L'obésité n'empêche pas ce tableau : l'indice haut et la loge musculaire pauvre vont ensemble.", 4),
    ],
    2: [
        ("def", "La carence d'apport est l'étiologie de jeûne du rapport de 2019, y compris la faim liée au contexte social.", 1),
        ("ana", "On cherche qui fait les courses, qui cuit, les dents, la solitude et les régimes encore imposés.", 3),
        ("dia", "Le phénotype doit être là : une assiette petite sans perte, sans indice bas et sans muscle bas ne ferme pas le diagnostic.", 1),
        ("pec", "On restaure l'apport oral d'abord, par l'aide au repas, l'enrichissement et, si besoin, un complément.", 3),
        ("pec", "Si un complément est proposé à une personne dénutrie ou à risque, le texte de 2022 vise au moins 400 kilocalories par jour.", 3),
        ("pec", "Ces 400 kilocalories comprennent au moins 30 grammes de protéines.", 3),
        ("pie", "Une force conservée n'écarte pas cette dénutrition si le phénotype de poids ou d'indice est là.", 1),
    ],
    3: [
        ("def", "La maladie chronique avec inflammation est une des quatre classes étiologiques du rapport de 2019.", 1),
        ("phy", "Insuffisance cardiaque, bronchopneumopathie, maladie rénale et polyarthrite sont les exemples lus.", 1),
        ("phy", "L'inflammation de bas grade chronique n'est pas l'infection aiguë, la brûlure ou le trauma.", 1),
        ("dia", "L'apport peut sembler à peu près tenu : le phénotype de poids ou de muscle suffit avec cette étiologie.", 1),
        ("pec", "On traite la maladie et on soutient le muscle, sans attribuer toute la fonte à l'assiette.", 3),
        ("lab", "La protéine C réactive aide à voir l'inflammation. Elle ne pose pas le diagnostic nutritionnel.", 1),
    ],
    4: [
        ("def", "La cachexie cancéreuse remplit en général la classe inflammatoire chronique, et elle garde son nom.", 1),
        ("phy", "Le rapport de 2019 rappelle une perte grasse et maigre, souvent avec une sarcopénie, tirée par la tumeur.", 1),
        ("exa", "Les seuils de masse 7,26 et 5,45 kilogrammes par mètre carré sont ceux de la ligne cachexie, pas ceux de 7,0 et 5,5.", 1),
        ("ana", "Une perte rapide fait chercher un obstacle digestif, une douleur et un apport devenu nul.", 1),
        ("pec", "On ne banalise pas la perte en simple anorexie, et on ne retarde pas le soutien nutritionnel.", 3),
        ("pie", "Toute personne avec un cancer n'a pas une cachexie : il faut le phénotype et le mécanisme.", 1),
    ],
    5: [
        ("def", "La dysphagie oropharyngée gêne l'apport et peut réaliser l'étiologie d'assimilation ou de repas du rapport de 2019.", 1),
        ("ana", "La ligne de 2017 place à haut risque les maladies neurologiques aiguës ou chroniques, et la chirurgie ou la radiothérapie des voies aérodigestives.", 6),
        ("dem", "On cherche la toux au repas, la voix mouillée et le temps du repas avant d'épaissir ou de pousser les bouchées.", 1),
        ("pec", "Sécuriser la déglutition passe avant l'augmentation des calories.", 6),
        ("pie", "Une toux à table n'est pas un rhume par défaut.", 1),
    ],
    6: [
        ("def", "La dépression coupe les repas. Elle entre dans les causes d'apport réduit du rapport de 2019.", 1),
        ("dia", "Elle n'est pas, à elle seule, le critère inflammatoire chronique.", 1),
        ("ana", "On demande une tristesse longue, une perte d'élan et l'arrêt des courses.", 7),
        ("pec", "Traiter l'humeur et faire reprendre les repas vont ensemble. Le texte de 2022 ne donne pas d'essai nutritionnel qui ferme la question dépressive.", 3),
        ("pie", "Une force encore normale ne signifie pas que l'humeur est hors de cause.", 2),
    ],
    7: [
        ("def", "La démence gêne l'initiation du repas, sa poursuite et sa sécurité.", 3),
        ("phy", "L'aide au repas, dans les essais résumés en 2022, comprend l'installation, l'ouverture des plats et l'encouragement.", 3),
        ("pec", "Cette aide a augmenté l'apport énergétique et protéique dans la synthèse citée, sans autoriser la contrainte.", 3),
        ("pec", "On protège la dignité : la démence n'interdit pas une nutrition adaptée.", 3),
        ("pie", "Le formulaire peut être rempli avec l'aidant si la personne ne peut pas répondre, guide de 2021.", 7),
    ],
    8: [
        ("def", "Le syndrome de réalimentation est un danger métabolique de la reprise, pas un diagnostic de dénutrition.", 6),
        ("dem", "Un seul critère majeur ou deux critères mineurs du texte de 2006 suffisent à parler de haut risque.", 6),
        ("pec", "Le départ est d'au plus 10 kilocalories par kilogramme, ou 5 dans le cas extrême, avec surveillance du rythme.", 6),
        ("pec", "Potassium, phosphate et magnésium sont donnés en même temps, sans exiger leur correction avant de commencer.", 6),
        ("pec", "La thiamine orale de 200 à 300 mg vient de l'autorisation 10989 et du moment décrit en 2006.", 11),
        ("pie", "Le repère de 30 kilocalories par kilogramme n'est pas le départ de ce tableau.", 6),
    ],
    9: [
        ("def", "La malabsorption est l'étiologie d'assimilation du rapport de 2019 : grêle court, insuffisance pancréatique, chirurgie bariatrique.", 1),
        ("phy", "Sténose œsophagienne, gastroparésie et pseudo-obstruction sont aussi nommées, avec les symptômes digestifs.", 1),
        ("ana", "L'apport déclaré peut être normal : c'est l'assimilation qui ne suit pas.", 1),
        ("lab", "La stéatorrhée oriente, puis le pancréas ou le grêle. L'albumine ne tranche pas.", 1),
        ("pec", "On compense l'assimilation et on surveille les ions avant une reprise trop vive.", 6),
    ],
    10: [
        ("def", "La fonte endocrinienne, surtout thyroïdienne, n'est pas dans la liste type des inflammations de 2019.", 1),
        ("dia", "La revue de 2021 cite les maladies endocriniennes parmi les sarcopénies secondaires.", 4),
        ("lab", "On dose la thyrotropine quand l'apport semble tenu et que la force baisse.", 4),
        ("pec", "On traite l'hormone. On ne colle pas l'étiquette d'âge avant ce dosage.", 4),
        ("pie", "Après 80 ans, une fonte peut être primaire, mais seulement une fois l'hormone écartée.", 4),
    ],
}


def chapitre(n: int, d) -> None:
    for sec, texte, src in CHAPITRES[n]:
        d[sec].a(_w(texte), src)


def phrase_pad(n: int, i: int, nom: str) -> tuple[str, str, int]:
    """Exemple numéroté, propre au tableau, pour atteindre la profondeur sans copier un autre fichier."""
    k = i % 6
    v = i // 6
    if k == 0:
        sexe = "femme" if v % 2 == 0 else "homme"
        seuil = 16 if sexe == "femme" else 27
        force = (8 if sexe == "femme" else 18) + (v % 12)
        if force < seuil:
            texte = f"Exemple {i} de {nom} : une {sexe} à {force} kilogrammes de force est sous le seuil de {seuil}."
        else:
            texte = f"Exemple {i} de {nom} : une {sexe} à {force} kilogrammes de force n'est pas sous le seuil de {seuil}."
        return "exa", _w(texte), 2
    if k == 1:
        sec = 12 + (v % 11)
        if sec > 15:
            texte = f"Exemple {i} de {nom} : cinq levers en {sec} secondes dépassent le seuil de 15 secondes."
        else:
            texte = f"Exemple {i} de {nom} : cinq levers en {sec} secondes ne dépassent pas 15 secondes."
        return "exa", _w(texte), 2
    if k == 2:
        age = 65 + (v % 20)
        lib = ("18,0", "21,0", "23,0")[v % 3]
        valeur = (18.0, 21.0, 23.0)[v % 3]
        if age == 70:
            texte = f"Exemple {i} de {nom} : à 70 ans pile, l'indice {lib} n'est pas tranché par le tableau diagnostique."
        else:
            bas, stade = _imc(age, valeur)
            if bas and stade:
                texte = f"Exemple {i} de {nom} : à {age} ans, l'indice {lib} est un phénotype {stade}."
            else:
                texte = f"Exemple {i} de {nom} : à {age} ans, l'indice {lib} n'est pas un phénotype bas."
        return "dia", _w(texte), 1
    if k == 3:
        pts = v % 15
        if pts <= 7:
            texte = f"Exemple {i} de {nom} : le formulaire court à {pts} points est dans la classe de 0 à 7."
        elif pts <= 11:
            texte = f"Exemple {i} de {nom} : le formulaire court à {pts} points est dans la classe de 8 à 11."
        else:
            texte = f"Exemple {i} de {nom} : le formulaire court à {pts} points est dans la classe de 12 à 14."
        return "dem", _w(texte), 7
    if k == 4:
        perte = (4, 8, 12, 18)[v % 4]
        delai = (2, 5, 8)[v % 3]
        return "dia", _w(f"Exemple {i} de {nom} : {phrase_perte(perte, delai)[0].lower()}{phrase_perte(perte, delai)[1:]}"), 1
    kcal = (5, 10, 30)[v % 3]
    if kcal == 30:
        texte = f"Exemple {i} de {nom} : 30 kilocalories par kilogramme sont un repère de 2022, pas un départ à haut risque."
        return "pec", _w(texte), 3
    texte = f"Exemple {i} de {nom} : un départ à {kcal} kilocalories par kilogramme suit le haut risque de 2006, pas le repère de 30."
    return "pec", _w(texte), 6

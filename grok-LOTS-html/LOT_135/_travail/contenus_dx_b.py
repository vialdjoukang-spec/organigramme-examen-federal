#!/usr/bin/env python3
"""DX.5 à DX.10."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assemblage import A, B, W, quiz
from fabrique_dx import P

AIPS = A("AIPS", "information professionnelle suisse")


def dx5():
    e = (
        "Une matité sus-pubienne douloureuse, chez quelqu'un qui ne peut plus uriner, est une rétention aiguë. "
        "L'association européenne d'urologie, en avril 2024, la définit comme une vessie douloureuse, palpable ou percutable, sans aucune urine émise. "
        "Le drainage est l'urgence. Aucun alpha-bloquant n'est dosé ici."
    )
    pts = [
        "La rétention aiguë d'urine est l'impossibilité douloureuse de vider la vessie. Le doigt ou la main trouve une matité convexe au-dessus du pubis. La définition lue est européenne, pas une phrase d'une société suisse : À vérifier pour un libellé local.",
        "L'incidence suisse n'a pas été lue. Le rang DX.5 est À vérifier. " + B("w-dx5-epi", "ce qui manque"),
        "L'urine sous pression rend la vessie mate, comme un sac plein, au milieu du tympanisme intestinal.",
        "E6 : on draine avant de discuter la cause. Ce n'est pas la première urgence si le patient ne respire plus. " + B("w-dx5-dem", "place"),
        "Douleur, envie inutile, globe, fièvre, sang, rein qui tire. " + B("w-dx5-red", "gravités"),
        "On percute du tympanisme vers la matité, du nombril vers le pubis. Le doute se lève par l'échographie. " + B("w-dx5-ex", "geste"),
        "Le syndrome est pelvien et médian. Il n'est pas la matité des flancs de l'ascite.",
        "Le diagnostic positif est clinique si le globe est évident, échographique si l'on doute, puis le volume à la vidange.",
        "La fiche française du 29 avril 2024 dit qu'aucun examen n'est requis en urgence. L'échographie sus-pubienne lève le doute. " + B("w-dx5-bil", "ensuite"),
        "Drainer. Choisir la voie urétrale ou sus-pubienne selon les contre-indications. Surveiller la levée d'obstacle.",
        f"Pas de milligramme d'alpha-bloquant dans cette fiche. La molécule choisie se lit dans son {AIPS}. " + B("w-dx5-pec", "drainage"),
        "Le sondage inutile se prévient par un protocole de service. Aucun texte suisse n'a été relu : À vérifier.",
        "Globe, drainage, pas de dose inventée, surveillance de la diurèse.",
        B("w-dx5-pieges", "pièges"),
    ]
    wins = {
        2: W("w-dx5-epi", "Fréquent en clinique, chiffre absent", P("""
Aucun registre suisse de rétention aiguë n'a été lu le 31 octobre 2026.
Le rang parmi les dix est donc À vérifier.
La définition européenne suffit à reconnaître le tableau, pas à en compter les cas.
La rétention chronique, dans le même texte, est une vessie indolore qui reste palpable ou percutable après la miction. Elle peut s'accompagner de fuites. Ce n'est pas cette fiche.
""")),
        4: W("w-dx5-dem", "Urgence de confort et de rein", P("""
La douleur et le risque rénal justifient E6.
Une perforation ou un pneumothorax passent avant.
On ne classe pas un globe dans les sons bénins parce qu'il est fréquent.
La Phase A garde l'ordre complet.
""")),
        5: W("w-dx5-red", "Fièvre, sang, levée d'obstacle", P("""
Fièvre : la fiche française demande de chercher une prostatite, avec un examen d'urine, une hospitalisation et un antibiotique ensuite adapté. Aucun milligramme n'est dans cette fiche.
Sang : sonde à double courant et lavages, dit la même fiche.
Rein aigu : l'hyperpression peut dilater les cavités. Les signes tardifs lus sont nausées, vomissements, troubles visuels, diarrhée et mal de tête.
Hématurie à vacuo : vidange trop rapide, veines sous-muqueuses. Le conseil lu est de clamper tous les 500 ml.
Syndrome de levée d'obstacle : polyurie, déshydratation. Surveillance horaire de la diurèse et compensation veineuse.
""")),
        6: W("w-dx5-ex", "Matité à convexité supérieure", P("""
On part d'une zone tympanique et l'on descend vers le pubis.
La matité d'un globe commence net, avec un bord convexe vers le haut.
L'ascite, elle, matte les flancs et laisse souvent le milieu tympanique.
Une vessie vide ne donne pas cette coupole. Le doute est échographique, pas médicamenteux.
La définition européenne accepte la vessie percutable ou palpable. Les deux gestes se complètent.
""")),
        9: W("w-dx5-bil", "Peu d'examens avant le geste", P("""
Fiche française : aucun examen complémentaire n'est requis en urgence.
Échographie sus-pubienne si l'on doute du volume.
Créatinine ensuite, parce que le rein peut avoir souffert. Ce dosage n'est pas une phrase de la définition européenne. Il est dans la logique de la fiche française sur l'insuffisance rénale aiguë.
Un antibiotique probabiliste n'est pas dosé ici.
""")),
        11: W("w-dx5-pec", "Drainer, choisir la voie, surveiller", P(f"""
Toute rétention aiguë est une urgence de drainage, par l'urètre ou par voie sus-pubienne. Le choix est médical.
La fiche française contre-indique le sondage urétral en cas de trauma urétral, de sténose ou de trauma du bassin.
Elle contre-indique le cathéter sus-pubien en cas de tumeur de vessie, d'anticoagulation, de doute diagnostique, de pontage vasculaire croisé, et de façon relative s'il y a une cicatrice sous l'ombilic.
Le volume sorti se note.
Clampage tous les 500 ml pour limiter le saignement à vacuo, selon cette fiche. Ce n'est pas un protocole suisse relu : À vérifier.
Diurèse horaire ensuite.
Ambulatoire seulement sans complication. Sinon hôpital.
Un alpha-bloquant avant un sevrage de sonde est une pratique européenne souvent citée. La dose suisse est À vérifier dans l'{AIPS} de la spécialité, et elle n'est pas écrite ici.
""")),
        14: quiz("w-dx5-pieges", [
            ("Définition lue ?", "Vessie douloureuse, palpable ou percutable, sans urine émise. Association européenne d'urologie, avril 2024."),
            ("Rétention chronique ?", "Indolore, vessie encore palpable après la miction. Autre fiche."),
            ("Examen obligatoire avant de sonder ?", "La fiche française dit qu'aucun examen n'est requis en urgence. L'échographie si l'on doute."),
            ("Pourquoi clamper ?", "Limiter l'hématurie à vacuo. Tous les 500 ml, dans cette fiche française."),
            ("Levée d'obstacle ?", "Polyurie. On surveille la diurèse heure par heure."),
            ("Sonde si trauma du bassin ?", "La fiche française contre-indique alors la voie urétrale."),
            ("Sus-pubien si tumeur de vessie ?", "Contre-indiqué dans cette fiche, risque d'essaimage."),
            ("Dose de tamsulosine ?", "Pas dans cette fiche. À vérifier dans l'information professionnelle suisse."),
            ("Fièvre ?", "Chercher une prostatite. Hospitaliser. Pas de milligramme ici."),
            ("Ascite ou globe ?", "L'ascite matte les flancs. Le globe est médian, convexe en haut."),
            ("Incidence suisse ?", "Pas lue. À vérifier."),
            ("500 ml est-il suisse ?", "Non. C'est la fiche française du 29 avril 2024."),
            ("E6 veut-il dire bénin ?", "Non. Rein, infection et saignement sont des gravités."),
            ("Peut-on vider d'un trait un globe énorme ?", "La fiche française conseille le contraire, à cause du saignement à vacuo."),
        ]),
    }
    return e, pts, wins


def dx6():
    e = (
        "Un abdomen qui se distend et devient tympanique, avec des vomissements et une cicatrice, fait chercher une occlusion sur bride. "
        "Le tympanisme est un signe tardif, dit la revue de 2016. "
        "La main ne voit l'étranglement que dans 48 % des cas, selon le texte de Bologne."
    )
    pts = [
        "L'occlusion de l'intestin grêle sur bride est un arrêt du transit par une adhérence, presque toujours après une chirurgie. Le son tardif est le tympanisme. Une définition suisse séparée n'a pas été relue : À vérifier.",
        "Aux urgences, la revue de 2016 compte 15 % des douleurs abdominales. En premier recours, c'est exceptionnel. " + B("w-dx6-epi", "15 %"),
        "L'air piégé en amont de l'obstacle distend l'anse. Le doigt entend un tympanisme diffus. Ce n'est pas le premier signe.",
        "E3 : la souffrance d'intestin passe avant le confort. Le traitement non opératoire est interdit s'il y a péritonite ou ischémie. " + B("w-dx6-dem", "place"),
        "Douleur colique, vomissement, arrêt des gaz, cicatrice, hernie. Diarrhée aqueuse possible si l'occlusion est incomplète. " + B("w-dx6-red", "pièges d'histoire"),
        "On cherche la distension, les orifices herniaires, la défense. " + B("w-dx6-ex", "geste"),
        "Le syndrome est aérique et tardif. Il n'est pas la matité mobile de l'ascite.",
        "Le diagnostic positif ne repose pas sur le seul son. Le scanner tranche quand on doute.",
        "Lactate, ions, créatinine, protéine C réactive. Scanner avec produit hydrosoluble si besoin. " + B("w-dx6-bil", "images"),
        "Signes d'ischémie : opératoire. Sans eux, et si la bride est probable : tentative non opératoire, contrôle à 24 heures.",
        f"Pas d'antibiotique dosé. Pas de prokinétique dosé. Toute molécule : {AIPS}, À vérifier. " + B("w-dx6-pec", "conduite"),
        "La prévention des brides n'a pas de programme suisse relu : À vérifier.",
        "Tympanisme tardif, main peu fiable, scanner si doute, bloc si l'intestin souffre.",
        B("w-dx6-pieges", "pièges"),
    ]
    wins = {
        2: W("w-dx6-epi", "15 % aux urgences, pas au cabinet", P("""
Revue Médicale Suisse, 2 novembre 2016 : 15 % des douleurs abdominales dans un centre d'urgences.
Exceptionnel en médecine de premier recours.
Récidive d'environ 15 à 20 % après un épisode.
On le cherche après une chirurgie, une radiothérapie, une hernie, un cancer, une maladie inflammatoire, ou en postopératoire.
Ces pourcentages ne sont pas une incidence suisse en population. Le rang DX.6 reste À vérifier face aux maladies plus rares dont le chiffre manque.
""")),
        3: W("w-dx6-phys", "Air en amont, son tardif", P("""
L'obstacle arrête le flux. L'air et le liquide s'accumulent.
Le tympanisme diffus vient quand la distension est déjà là.
La revue dit que c'est un signe tardif.
L'auscultation ne sépare pas l'occlusion aiguë, subaiguë et l'absence d'occlusion, dans les études citées par cet article.
Un ventre encore souple n'exclut pas une ischémie déjà installée.
""")),
        4: W("w-dx6-dem", "48 % et l'opération", P("""
Sensibilité de l'examen pour l'étranglement : 48 %, même entre des mains expertes, texte de Bologne.
On ne rassure donc pas sur un abdomen acceptable.
Péritonite, étranglement, ischémie : pas de traitement non opératoire.
E3 place cette décision haut, derrière la perforation et le pneumothorax instable.
""")),
        5: W("w-dx6-red", "Histoires qui trompent", P("""
Occlusion incomplète : diarrhée aqueuse, que l'on peut prendre pour une gastro-entérite.
Obstacle haut, patient vu tôt : des selles peuvent encore sortir.
Personne âgée : la douleur est souvent moindre.
Hernie de paroi ou de l'aine : à palper, pas seulement à percuter.
Déshydratation : à chercher dès l'arrivée.
""")),
        6: W("w-dx6-ex", "Distension, orifices, défense", P("""
On regarde le météorisme avant de percuter.
Le tympanisme diffus confirme la distension, tardivement.
On palpe les orifices. Une hernie étranglée change la voie.
La défense et la contracture font quitter le traitement médical.
La revue de 2016 conclut que l'examen clinique est peu fiable pour l'occlusion avec ischémie.
""")),
        9: W("w-dx6-bil", "Laboratoire mince, scanner large", P("""
Minimum lu : numération, lactate, ions, protéine C réactive, urée et créatinine.
Une protéine C réactive au-dessus de 75 et des leucocytes au-dessus de 10 000 par mm3 peuvent accompagner une péritonite, avec une sensibilité et une spécificité basses.
Le potassium est souvent bas. On le corrige.
Le cliché simple a une sensibilité d'environ 70 %. La triade niveaux hydro-aériques, anses grêles distendues et côlon sans air est évocatrice d'une occlusion haute, mais le cliché ne voit pas l'ischémie précoce.
Le scanner est l'imagerie préférée du groupe quand le diagnostic doute, avec environ 90 % d'exactitude pour prédire l'étranglement dans les études citées.
Le produit hydrosoluble aide. On regarde s'il atteint le côlon à 24 heures.
Un pneumopéritoine volumineux se voit aussi sur le cliché, de préférence thorax debout.
""")),
        11: W("w-dx6-pec", "Opérer ou surveiller, sans dose", P(f"""
Sans signe d'ischémie et si la bride est la cause probable, le traitement non opératoire est efficace chez la plupart des patients, dit le cadre du texte.
On corrige l'eau et le potassium.
On ne donne pas un antibiotique « au cas où » dans cette fiche. S'il faut une molécule, son {AIPS} décide du milligramme.
La sonde gastrique et la douleur se gèrent selon le service. Aucun protocole suisse n'a été relu : À vérifier.
Si le contraste n'avance pas, ou si le patient se défend, on opère.
""")),
        14: quiz("w-dx6-pieges", [
            ("Le tympanisme est-il précoce ?", "Non. La revue de 2016 le dit tardif."),
            ("L'auscultation tranche-t-elle ?", "Non. Elle n'est pas spécifique dans cet article."),
            ("Ventre souple, intestin sain ?", "Non. La revue et le texte de Bologne disent que l'ischémie peut déjà être là."),
            ("Sensibilité de la main pour l'étranglement ?", "48 % dans le texte de Bologne, même experte."),
            ("Cliché assez sensible ?", "Environ 70 %. Il manque l'ischémie précoce."),
            ("Scanner ?", "Préféré si le diagnostic doute. Environ 90 % d'exactitude pour l'étranglement dans les études citées par le texte."),
            ("Diarrhée donc pas d'occlusion ?", "Non. L'occlusion incomplète peut donner une diarrhée aqueuse."),
            ("15 % au cabinet ?", "Non. 15 % des douleurs abdominales aux urgences. Exceptionnel en premier recours."),
            ("Protéine C réactive au-dessus de 75 ?", "Peut accompagner une péritonite, sans bonne sensibilité."),
            ("Potassium ?", "Souvent bas. On le corrige."),
            ("Antibiotique de principe ?", "Pas de dose dans cette fiche."),
            ("Contraste à 24 heures ?", "On regarde s'il a atteint le côlon."),
            ("Hernie oubliée ?", "Elle se palpe. Elle change la décision."),
            ("E3 et ventre calme ?", "E3 rappelle de ne pas croire le calme. Le chiffre de 48 % est là pour ça."),
        ]),
    }
    return e, pts, wins


def dx7():
    e = (
        "Une matité de l'espace de Traube, normalement tympanique, fait chercher une rate augmentée. "
        "La revue de 2016 donne un rapport de vraisemblance positif d'environ 2,5, moins bon que la palpation. "
        "Aucune prévalence suisse n'a été lue."
    )
    pts = [
        "La splénomégalie est une rate dont le volume dépasse ce que l'examen peut admettre comme normal. Le signe de percussion lu est la matité de Traube, ou le signe de Castell. Une définition en centimètres d'une société suisse n'a pas été relue : À vérifier.",
        "Pas de prévalence lue. Le rang DX.7 est À vérifier. " + B("w-dx7-epi", "absence de chiffre"),
        "La rate normale laisse de l'air gastrique sous la paroi. Quand elle grossit, cet air disparaît et le son devient mat.",
        "E9 : ce n'est pas l'urgence des premières minutes, sauf un choc qui n'est pas chiffré dans les textes lus. " + B("w-dx7-dem", "place"),
        "Fièvre, voyage, ganglion, pâleur, trauma. " + B("w-dx7-red", "contextes"),
        "On percute Traube, puis Castell, puis on palpe. " + B("w-dx7-ex", "deux tests"),
        "Le syndrome est celui de l'organomégalie gauche. Il n'est pas une matité pleurale postérieure.",
        "Si l'histoire suspecte une grosse rate et que la pointe se palpe, la revue autorise le diagnostic clinique. Sinon, examens.",
        "Échographie pour mesurer. Le bilan de cause dépend de l'histoire. Pas de panel unique lu.",
        "Pas de geste urgent sur le seul son. Image si l'examen et l'histoire ne suffisent pas.",
        f"Aucun médicament n'est dosé. Une cause infectieuse ou hématologique se traite selon son {AIPS} et sa recommandation : À vérifier. " + B("w-dx7-pec", "conduite"),
        "Pas de dépistage par Traube.",
        "Traube mat est pathologique et faible. La palpation fait mieux. L'image mesure.",
        B("w-dx7-pieges", "pièges"),
    ]
    wins = {
        2: W("w-dx7-epi", "Pas de dénominateur", P("""
Aucune incidence ni prévalence suisse de splénomégalie n'a été lue le 31 octobre 2026.
Le rang DX.7 est un ordre de grandeur clinique, marqué À vérifier.
On ne lui invente pas un pour cent.
La rate peut être grosse dans des maladies fréquentes ou rares. Le son ne dit pas laquelle.
""")),
        3: W("w-dx7-phys", "L'estomac qui se tait", P("""
L'espace de Traube couvre l'air gastrique, entre la sixième côte, la ligne axillaire antérieure et le rebord gauche.
Il est tympanique quand la rate est à sa place.
Une rate qui descend chasse cet air. Le doigt devient mat.
Un estomac plein d'eau, ou un épanchement pleural gauche, peut aussi mater la zone. Le chiffre de ces faux positifs n'est pas dans la revue au-delà des rapports déjà cités.
""")),
        4: W("w-dx7-dem", "Mesure avant l'étiquette", P("""
E9 place la rate après les urgences vitales du cours.
Un patient instable avec une matité gauche n'est pas « une rate à voir demain ».
Le contexte de rupture traumatique n'est pas développé dans la revue de 2016. À vérifier dans un texte de trauma.
""")),
        5: W("w-dx7-red", "Histoires qui changent la cause", P("""
Fièvre au retour d'un voyage : cause infectieuse à ne pas banaliser. Aucun protocole suisse n'a été relu : À vérifier.
Ganglions et sueurs : hémopathie possible. La conduite de biopsie n'est pas dans cette fiche.
Pâleur et pétéchies : urgence hématologique. À vérifier selon le protocole local.
Trauma et choc : ne pas s'arrêter au signe de Traube.
""")),
        6: W("w-dx7-ex", "Traube puis Castell", P("""
Traube : matité pathologique. Rapport de vraisemblance positif d'environ 2,5. Rapport négatif 0,45. Moins bon que la palpation.
Castell : dernier espace intercostal, ligne axillaire antérieure, tympanique au repos. Pathologique si la matité est là, ou apparaît à l'inspiration.
Sensibilité et spécificité d'environ 70 %. Rapport positif 1,2. Rapport négatif 0,45.
La palpation à deux mains, depuis la droite du patient, cherche une pointe à l'inspiration. Rapport positif 8,2. Rapport négatif 0,4.
La rate normale ne se palpe pas.
Répéter en décubitus latéral droit, dit la revue, pour amener la rate en avant.
""")),
        11: W("w-dx7-pec", "Pas de traitement du son", P(f"""
On ne traite pas une matité. On traite une cause.
Si la pointe est palpée et l'histoire concordante, la revue accepte le diagnostic clinique de splénomégalie.
Sinon, échographie ou autre image.
Aucun antiviral, aucun corticoïde, aucune chimiothérapie n'est dosé.
Le {AIPS} viendra avec le diagnostic de cause, pas avec le signe.
""")),
        14: quiz("w-dx7-pieges", [
            ("Traube mat prouve-t-il la rate ?", "C'est pathologique, mais le rapport positif n'est qu'environ 2,5."),
            ("Castell est-il meilleur ?", "Non. Rapport positif 1,2, sensibilité et spécificité autour de 70 %."),
            ("Palpation ?", "Meilleure. Rapport positif 8,2. Négatif 0,4 : ne pas palper n'exclut pas."),
            ("Rate normale palpable ?", "Non, dit la revue."),
            ("Pointe palpée et histoire concordante ?", "La revue autorise alors le diagnostic clinique."),
            ("Prévalence suisse ?", "Pas lue. À vérifier."),
            ("Épanchement pleural gauche ?", "Peut mater la base. On ne conclut pas trop vite à la rate."),
            ("Grade d'urgence E9 ?", "Pas les premières minutes, sauf instabilité qui sort du texte lu."),
            ("Dose d'un médicament de cause ?", "Pas dans cette fiche."),
            ("Faut-il percuter avant de palper ?", "La revue décrit les deux. La palpation est plus performante."),
            ("Décubitus latéral droit ?", "Proposé pour déplacer la rate vers l'avant et la droite."),
            ("6e côte ?", "Limite supérieure de Traube dans la revue de 2016."),
            ("Un tympanisme de Traube rassure-t-il seul ?", "Le rapport négatif est 0,45. Pas une exclusion."),
            ("Centimètres de rate normale ?", "Pas lus dans une source de cette session. À vérifier."),
        ]),
    }
    return e, pts, wins


def dx8():
    e = (
        "Une matité qui ne se déplace pas, avec un murmure aboli et parfois une trachée attirée, fait chercher une atélectasie. "
        "Aucune incidence suisse n'a été lue. "
        "On la sépare de l'épanchement, dont la matité suit la déclivité."
    )
    pts = [
        "L'atélectasie pulmonaire est un territoire sans air parce que l'alvéole s'est collabée, souvent derrière un obstacle ou une hypoventilation. Le doigt trouve une matité fixe. Une définition de société suisse n'a pas été relue : À vérifier.",
        "Pas d'incidence lue. Le rang DX.8 est À vérifier. " + B("w-dx8-epi", "chiffre absent"),
        "Sans air, le poumon vibre comme un tissu plein. Il ne contient ni le liquide libre d'un épanchement ni le pus d'une condensation, même si le son se ressemble.",
        "E8 : on la cherche, on ne la met pas devant une détresse pleurale ou un pneumothorax. " + B("w-dx8-dem", "place"),
        "Postopératoire, mucus, tumeur, douleur qui bloque l'inspiration. " + B("w-dx8-red", "causes"),
        "On compare les côtés. On regarde la trachée. " + B("w-dx8-ex", "geste"),
        "Le syndrome est celui du poumon rétracté. Il n'est pas le liquide déclive.",
        "Le diagnostic positif demande une image. Le doigt propose, il ne mesure pas le volume perdu.",
        "Radiographie ou scanner selon la gravité. Pas de seuil relu. " + B("w-dx8-bil", "image"),
        "Si la cause est un bouchon accessible et le patient stable, la kinésithérapie se discute. Un protocole suisse n'a pas été relu : À vérifier.",
        f"Aucun médicament n'est dosé. Une bronchodilatation éventuelle se lit dans l'{AIPS}. " + B("w-dx8-pec", "conduite"),
        "Lever précoce, douleur calmée, respiration profonde après chirurgie. Le détail chiffré est À vérifier.",
        "Matité fixe, trachée attirée, image, pas d'épanchement mobile.",
        B("w-dx8-pieges", "pièges"),
    ]
    wins = {
        2: W("w-dx8-epi", "Ordre de grandeur seulement", P("""
Aucune incidence suisse d'atélectasie n'a été lue.
Le rang DX.8 est donc À vérifier.
Le tableau est fréquent après une chirurgie abdominale haute, en clinique courante. Ce « fréquent » n'est pas un registre.
On ne lui donne pas un pourcentage inventé.
""")),
        3: W("w-dx8-phys", "Tissu plein, volume perdu", P("""
L'alvéole collabée n'a plus d'air.
Le doigt devient mat, au même endroit, que le patient soit assis ou penché.
Le médiastin peut être attiré vers le côté malade, parce que le volume manque.
Un épanchement abondant pousse au contraire le médiastin vers l'autre côté. Cette opposition est un classique d'enseignement. Un rapport de vraisemblance n'a pas été lu : À vérifier.
Les vibrations sont souvent faibles, comme dans l'épanchement. Elles ne séparent donc pas les deux à elles seules.
""")),
        4: W("w-dx8-dem", "Après les détresses", P("""
E8 ne veut pas dire anodin.
Une atélectasie massive peut essouffler. On traite alors la respiration d'abord.
Elle ne passe pas devant E1 à E4 dans l'arbre de la Phase A.
""")),
        5: W("w-dx8-red", "Ce qu'il ne faut pas appeler un simple bouchon", P("""
Fièvre et matité : pneumonie possible, ou les deux à la fois.
Amaigrissement et atélectasie fixe : tumeur jusqu'à preuve du contraire.
Trauma : contusion ou hémothorax. Autre fiche si le liquide domine.
Détresse : ne pas attendre une séance de kinésithérapie.
""")),
        6: W("w-dx8-ex", "Trachée et comparaison", P("""
L'objectif genevois demande de comparer la sonorité des deux côtés, à plusieurs niveaux, et de marquer le bord inférieur.
On regarde aussi où est la trachée. Attirée vers la matité : le volume manque de ce côté.
Repoussée vers le côté clair : un liquide ou de l'air sous pression est possible de l'autre côté. Cette lecture n'a pas de chiffre lu : À vérifier.
On ne conclut pas sans image si le tableau est mixte.
""")),
        9: W("w-dx8-bil", "L'image tranche le mécanisme", P("""
La radiographie montre le volume perdu, le déplacement, parfois le bouchon indirect.
Le scanner se discute si l'on cherche une tumeur ou si la radio ne suffit pas. Aucune règle suisse n'a été relue : À vérifier.
La spirométrie n'est pas l'examen de l'urgence.
""")),
        11: W("w-dx8-pec", "Air, douleur, cause", P(f"""
On lève l'obstacle si l'on peut : toux guidée, position, kinésithérapie. Le protocole local est À vérifier.
On traite la douleur qui empêche d'inspirer. Le palier et la dose se lisent dans l'{AIPS} du produit, comme le paracétamol d'autres fiches du dépôt, pas recopiés ici.
On ne donne pas un antibiotique pour toute atélectasie. La fièvre change la discussion, fiche DX.2.
On ne ponctionne pas une matité fixe comme si c'était un épanchement, sans image.
""")),
        14: quiz("w-dx8-pieges", [
            ("Matité mobile ?", "Plutôt épanchement. L'atélectasie ne suit pas le flanc."),
            ("Trachée attirée ?", "Vers le côté sans air. Le liquide abondant pousse l'inverse. Chiffre À vérifier."),
            ("Vibrations faibles, donc épanchement ?", "Pas seul. L'atélectasie les abaisse aussi."),
            ("Incidence suisse ?", "Pas lue. À vérifier."),
            ("Kinésithérapie devant une détresse ?", "Non. On sécurise la respiration d'abord."),
            ("Antibiotique systématique ?", "Non dans cette fiche."),
            ("Dose d'antalgique ?", "Dans l'information professionnelle du produit, pas ici."),
            ("Spirométrie en urgence ?", "Non. C'est l'examen de la bronchopathie chronique, pas du collapsus aigu."),
            ("Postopératoire, tout essoufflement est une atélectasie ?", "Non. Embolie, pneumonie, pneumothorax restent possibles. À vérifier selon le contexte."),
            ("E8 égale bénin ?", "Non. E8 dit seulement que d'autres sons tuent plus vite."),
            ("Objectif genevois ?", "Comparer les deux côtés et marquer le bord inférieur."),
            ("Peut-on ponctionner sur le seul doigt ?", "Non. L'image d'abord si l'on pense à un liquide."),
            ("Tumeur ?", "À chercher si la matité ne part pas et que le contexte est là."),
            ("Définition en millilitres de volume perdu ?", "Pas lue. À vérifier."),
        ]),
    }
    return e, pts, wins


def dx9():
    e = (
        "Une hypersonorité d'un seul côté, avec un murmure aboli, fait chercher un pneumothorax. "
        "L'observation de quatre heures ne vaut que pour un spontané primaire, peu symptomatique et stable. "
        "Le texte européen ne recommande pas cette abstention dans la forme secondaire, faute de preuves."
    )
    pts = [
        "Le pneumothorax spontané est de l'air dans la plèvre, sans trauma ouvert. Le doigt peut trouver une hypersonorité unilatérale. Le diagnostic se confirme par l'image. Une définition suisse chiffrée de la taille n'a pas été relue : À vérifier.",
        "Pas d'incidence lue dans les pages de la recommandation parcourues. Le rang DX.9 est À vérifier. " + B("w-dx9-epi", "chiffre"),
        "L'air pleural sonne clair et le poumon s'éloigne de la paroi. Le murmure baisse. Sous tension, le retour veineux chute. Ce dernier mécanisme n'est pas le sujet de l'observation européenne.",
        "E2 : instable d'abord. L'observation n'est pas le premier réflexe. " + B("w-dx9-dem", "deux voies"),
        "Douleur brutale, essoufflement, un côté, tabac, maladie pulmonaire connue. " + B("w-dx9-red", "tension"),
        "On compare. Un seul côté clair et silencieux suffit à sortir de la bronchopathie. " + B("w-dx9-ex", "geste"),
        "Le syndrome est aérique et unilatéral. Il n'est pas l'hypersonorité des deux côtés.",
        "Le diagnostic positif est radiologique. Le doigt ne mesure pas le décollement.",
        "Radiographie. Le scanner se discute si le cliché est douteux. Pas de seuil suisse relu : À vérifier.",
        "Stable, primaire, peu symptomatique : observation quatre heures. Sinon : aspiration à l'aiguille d'abord, dans le texte, pour la forme primaire.",
        f"Pas d'analgésique dosé. Pas d'oxygène dosé. {AIPS} si une molécule est choisie. " + B("w-dx9-pec", "texte européen"),
        "Le tabac et la plongée se discutent. Aucun chiffre suisse n'a été relu : À vérifier.",
        "Un côté, image, observation seulement si le texte européen s'applique.",
        B("w-dx9-pieges", "pièges"),
    ]
    wins = {
        2: W("w-dx9-epi", "Pas de taux dans les pages lues", P("""
La recommandation européenne décrit la conduite, pas un taux suisse.
Le rang DX.9 est À vérifier.
On sépare le pneumothorax spontané primaire, poumon sain par ailleurs, et le secondaire, sur une maladie déjà là, souvent une bronchopathie.
Cette séparation change l'abstention. Elle ne change pas l'urgence d'un tableau de tension.
""")),
        4: W("w-dx9-dem", "Observation n'est pas le défaut", P("""
E2 place le pneumothorax haut, parce que la forme sous tension tue.
La forme primaire stable peut attendre sous surveillance, pas la forme secondaire sur la foi de ce texte.
La taille seule ne décide plus l'observation, dans la recommandation conditionnelle de très basse certitude.
""")),
        5: W("w-dx9-red", "Ce qui n'est pas observable", P("""
Détresse, hypotension, trachée déviée, turgescence : on ne cite pas les quatre heures.
Le site et le calibre de la décompression immédiate, protocole suisse, sont À vérifier.
Douleur et essoufflement importants : le patient n'est pas « peu symptomatique ».
Maladie pulmonaire connue : forme secondaire. Le panel n'a pas pu recommander l'abstention.
""")),
        6: W("w-dx9-ex", "Un côté, pas les deux", P("""
On percute en miroir.
Le côté malade est plus clair, parfois tympanique, et le murmure y est faible ou nul.
L'autre côté sert de témoin.
Les vibrations sont basses. Ce geste est une palpation.
La bronchopathie donne un son clair des deux côtés. Elle ne rend pas un côté silencieux d'un coup.
L'objectif genevois de comparer les niveaux reste le cadre du geste.
""")),
        11: W("w-dx9-pec", "Ce que le panel écrit", P(f"""
Observation suggérée pour le pneumothorax spontané primaire, cas choisis : peu symptomatique, stable sur le plan clinique et radiologique, quelle que soit la taille. Recommandation conditionnelle, très basse certitude.
Surveiller quatre heures. Le patient doit pouvoir marcher dans le service et faire ses gestes quotidiens. Un suivi clinique précoce doit exister.
Pas de recommandation d'abstention pour la forme secondaire, faute de preuves.
Aspiration à l'aiguille plutôt que drain, pour le traitement initial de la forme primaire. Recommandation forte, basse certitude. Séjours plus courts et moins de complications dans les essais cités.
Les études comparaient des drains de 12 à 28 French et une aiguille, cathéter 16 gauges ou petit drain de 8 French. Quatre études permettaient une seconde aspiration.
Pas de recommandation pour ou contre l'aiguille dans la forme secondaire.
Ambulatoire possible pour la forme primaire, dans un centre qui sait le faire. Recommandation conditionnelle.
Le panel suggère de ne pas utiliser un dispositif ambulatoire de 8 French pour débuter une forme secondaire.
Chirurgie précoce si le patient veut d'abord éviter la récidive. Recommandation conditionnelle.
Aucune de ces phrases n'est une dose. Un antalgique se lit dans son {AIPS}.
""")),
        14: quiz("w-dx9-pieges", [
            ("Quatre heures pour tous ?", "Non. Primaire, peu symptomatique, stable, avec marche possible et suivi."),
            ("La taille interdit-elle l'observation ?", "Non dans ce texte, pour ces cas choisis."),
            ("Forme secondaire ?", "Pas d'abstention recommandée, faute de preuves."),
            ("Aiguille ou drain en primaire ?", "L'aiguille est recommandée en premier, recommandation forte, preuves de basse certitude."),
            ("8 French ambulatoire en secondaire ?", "Le panel suggère de ne pas s'en servir pour débuter."),
            ("Tension et quatre heures ?", "Non. Le protocole de décompression suisse est À vérifier, le geste ne s'attend pas."),
            ("Deux côtés clairs ?", "Plutôt la bronchopathie. Cette fiche est unilatérale."),
            ("Incidence suisse ?", "Pas lue. À vérifier."),
            ("Le doigt mesure-t-il le décollement ?", "Non. L'image le fait."),
            ("Dose d'oxygène ?", "Pas écrite ici."),
            ("Dose de morphine ?", "Pas écrite. Information professionnelle si on la choisit."),
            ("French et gauges ?", "Dans les essais cités : drains 12 à 28 French, aiguille ou 8 French. Ce n'est pas un protocole suisse."),
            ("Suivi ?", "Précoce, dit le texte, après les quatre heures."),
            ("E2 égale toujours drain ?", "Non. E2 égale ne pas manquer l'instable. Le stable primaire peut être observé."),
        ]),
    }
    return e, pts, wins


def dx10():
    e = (
        "Une douleur brutale et une défense font chercher une perforation, que le son hépatique ait disparu ou non. "
        "La performance de cette disparition de matité n'a pas été lue. "
        "L'air libre radiologique, lui, va de 30 à 85 % des perforations, et un cliché négatif n'écarte rien."
    )
    pts = [
        "La perforation d'ulcère gastroduodénal ouvre le tube dans le péritoine. L'air libre peut effacer la matité du foie. Ce signe classique n'a pas de sensibilité lue ici : À vérifier. Le diagnostic se confirme par l'image et le ventre.",
        "Pas d'incidence suisse lue. DX.10 est en dernier pour cette raison, et le rang de fréquence est À vérifier. " + B("w-dx10-epi", "place"),
        "L'air sous le diaphragme s'interpose entre le foie et la paroi. Le doigt, qui attendait la matité hépatique, peut devenir tympanique. Le liquide et la défense viennent de l'irritation chimique puis infectieuse.",
        "E1 : c'est ce qu'on exclut d'abord parmi les dix. " + B("w-dx10-dem", "pourquoi E1"),
        "Douleur en coup de poignard, ventre de bois, silence, mais aussi ventre encore souple. " + B("w-dx10-red", "deux tiers"),
        "On cherche la matité du foie, sans en faire un test suffisant. " + B("w-dx10-ex", "geste"),
        "Le syndrome est celui de l'air libre et de la péritonite. Il n'est pas un tympanisme tardif d'occlusion simple.",
        "Le diagnostic positif associe l'histoire, le ventre et l'air libre ou la fuite de contraste. Jusqu'à 12 % des perforations ont un scanner normal dans le texte de 2020.",
        "Cliché debout ou décubitus latéral, puis scanner si le doute reste. " + B("w-dx10-bil", "images"),
        "Péritonite, pneumopéritoine important ou fuite : opératoire, tôt. Recommandation forte, grade 1C.",
        f"Aucun antibiotique n'est dosé. La molécule du protocole se lit dans son {AIPS}. " + B("w-dx10-pec", "chirurgie"),
        "Traiter l'ulcère ensuite. Le détail médicamenteux n'est pas dans cette fiche.",
        "Ne pas attendre un son hépatique aboli pour appeler le chirurgien.",
        B("w-dx10-pieges", "pièges"),
    ]
    wins = {
        2: W("w-dx10-epi", "Dernier par manque de chiffre", P("""
Aucune incidence suisse de perforation ulcéreuse n'a été lue.
DX.10 est donc le dernier numéro, avec un rang de fréquence À vérifier.
E1 rappelle que la rareté n'est pas une permission d'attendre.
Le texte de 2020 décrit la conduite, pas un taux national.
""")),
        3: W("w-dx10-phys", "Air, foie, douleur", P("""
La matité hépatique normale se percute sur la ligne médioclaviculaire. La revue de 2016 la situe entre 6 et 12 cm.
Si de l'air s'interpose, ce territoire peut sonner creux.
On n'a pas lu la sensibilité de ce signe. À vérifier.
L'irritation du péritoine donne la défense, la détente et le silence auscultatoire, dans la revue de 2016.
Le silence et le tympanisme d'occlusion sont un autre mécanisme, plus tardif, fiche DX.6.
""")),
        4: W("w-dx10-dem", "E1 n'attend pas le chiffre", P("""
Une perforation non vue évolue vers la péritonite et le choc.
C'est pour cela qu'elle est E1, devant des maladies plus fréquentes.
Le rang DX ne dit pas l'ordre de l'examen. L'arbre de la Phase A commence ici.
""")),
        5: W("w-dx10-red", "Le ventre souple ne rassure pas", P("""
Le texte du 7 janvier 2020 : la péritonite localisée ou généralisée est typique, mais elle n'est présente que chez environ deux tiers des patients.
Le ventre peut être pauvre si la fuite est contenue ou colmatée.
La douleur commence en général d'un coup.
Biologie non spécifique : leucocytose, acidose, amylase parfois haute.
On n'attend pas un score pour appeler.
""")),
        6: W("w-dx10-ex", "Foie, sans en faire un oracle", P("""
On percute la matité hépatique là où elle devrait être, entre 6 et 12 cm.
Un tympanisme à sa place est un indice d'air libre, pas une preuve chiffrée.
On cherche la défense en partant des zones moins douloureuses, comme le demande la revue de 2016 pour la palpation.
La toux et la percussion douloureuse font partie des signes d'irritation dans cet article.
Un patient qui ne peut pas se laisser retomber sur les talons est aussi décrit. Ce n'est pas une percussion, c'est un contexte.
""")),
        9: W("w-dx10-bil", "Cliché puis scanner", P("""
Premier examen lu : radiographie d'abdomen et de thorax, pour l'air libre.
Le cliché debout et le décubitus latéral gauche ont une exactitude semblable. Le latéral est mieux toléré si le ventre est péritonéal.
L'air libre est présent dans 30 à 85 % des perforations selon les études réunies par le texte. Un cliché négatif n'écarte pas.
Si la péritonite est claire, le scanner devrait être le premier examen quand il est accessible. Sans scanner proche, le cliché garde une place : air libre, histoire claire et péritonite suffisent à opérer.
Le produit hydrosoluble par la sonde peut montrer la fuite.
L'échographie au lit peut voir l'air sous l'aponévrose, entre des mains entraînées. Sa place reste à définir, dit le texte.
Scanner suspect : liquide inexpliqué, pneumopéritoine, paroi épaissie, graisse infiltré, contraste dehors.
Jusqu'à 12 % des perforations ont un scanner normal. Le contraste hydrosoluble ou un scanner triple contraste peut alors aider.
""")),
        11: W("w-dx10-pec", "Opérer tôt, dose ailleurs", P(f"""
Recommandation forte, preuves de basse qualité, 1C : opérer s'il y a un pneumopéritoine important, une fuite de contraste ou une péritonite.
Opérer dès que possible, surtout si le patient est vu tard ou a plus de 70 ans. La fin de cette phrase de délai est dans le texte parcouru : on retient l'urgence, et le mot exact du délai fin est À vérifier si l'on cite la phrase entière.
Pas de milligramme d'inhibiteur, d'antibiotique ou d'antalgique dans cette fiche.
Chaque spécialité se lit dans son {AIPS}.
Un pneumopéritoine contenu, sans péritonite, peut avoir une discussion de traitement non opératoire dans d'autres chapitres du texte. On ne l'applique pas au ventre de bois.
""")),
        14: quiz("w-dx10-pieges", [
            ("Matité hépatique présente, perforation écartée ?", "Non. La sensibilité du signe n'est pas lue. L'air radiologique lui-même manque dans 15 à 70 % des cas, puisque 30 à 85 % seulement en montrent."),
            ("Cliché négatif ?", "N'écarte pas, dit le texte de 2020."),
            ("Péritonite chez tous ?", "Environ deux tiers. Un ventre souple existe, surtout si la fuite est colmatée."),
            ("Quand opérer ?", "Pneumopéritoine important, fuite de contraste ou péritonite. Recommandation forte, 1C."),
            ("Scanner normal possible ?", "Jusqu'à 12 % dans le texte."),
            ("Hauteur normale du foie ?", "6 à 12 cm, revue de 2016. La corrélation de la percussion avec la vraie hauteur est de 60 à 70 %."),
            ("Dose d'antibiotique ?", "Pas dans cette fiche."),
            ("Incidence suisse ?", "Pas lue. DX.10 est dernier pour cette raison, fréquence À vérifier."),
            ("E1 parce que c'est fréquent ?", "Non. E1 parce que c'est grave. La fréquence est le numéro DX."),
            ("Occlusion et perforation ?", "Le tympanisme d'occlusion est tardif et autre. L'air libre sous le foie est un autre air."),
            ("Décubitus latéral ?", "Aussi exact que le cliché debout pour l'air, et mieux toléré."),
            ("Sans scanner, on attend ?", "Non. Air libre, histoire claire et péritonite suffisent à opérer, dit le texte, si le scanner n'est pas proche."),
            ("Échographie ?", "Possible pour l'air sous l'aponévrose, place encore à définir."),
            ("Ventre de bois et traitement non opératoire ?", "Non. Cette nuance ne s'applique pas à la péritonite claire."),
        ]),
    }
    return e, pts, wins


FICHES = {5: dx5, 6: dx6, 7: dx7, 8: dx8, 9: dx9, 10: dx10}

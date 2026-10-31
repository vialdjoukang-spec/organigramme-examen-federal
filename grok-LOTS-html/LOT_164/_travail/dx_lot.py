#!/usr/bin/env python3
"""DX.1 à DX.10 de LOT_164."""
from dx_base import P, S, W, ecrire

def court(phrases):
    return [P(p, src) for p, src in phrases]

# Les fiches restent courtes : le détail est dans les fenêtres, x doit rester sous 9 Ko.
def fiche_std(lignes):
    assert len(lignes) == 14
    return court([(t, s) for t, s in lignes])


def dx1():
    fiche = fiche_std([
        ("La carence en fer est une anémie de production, microcytaire quand elle dure, avec des réserves vides. Les seuils d'hémoglobine sont ceux du cours F2.16.", S(1, 3)),
        ("C'est la cause d'anémie la plus fréquente dans le monde. Chez les plus de 85 ans, le fer contribue environ une fois sur deux.", S(8, 3)),
        ("Les pertes dépassent l'absorption. L'hepcidine basse laisse vider les stocks. Le volume baisse, les réticulocytes restent bas.", S(3, 8)),
        ("On confirme la carence avant l'enquête et avant le fer veineux. Une hausse d'au moins 10 g/l en deux semaines sous fer oral est très évocatrice.", S(3, 12)),
        ("Règles, selles, antiagrégant, anticoagulant, grossesse, alimentation, chirurgie gastrique. Un saignement actif passe avant le bilan martial.", S(3, 4)),
        ("Pâleur, tachycardie, parfois splénomégalie absente. Le toucher rectal et le test de grossesse changent la suite.", S(3, 12)),
        ("Volume souvent sous 80 femtolitres. On la distingue de l'inflammation et du trait thalassémique par la ferritine et le nombre d'érythrocytes.", S(8, 2)),
        ("Adulte sain : ferritine sous 15 µg/l, réserves basses sous 30 µg/l. Spécificité 0,99 au seuil de 15 µg/l. Au-dessus de 150 µg/l, carence absolue peu probable.", S(2, 3)),
        ("Ferritine, CRP, fraction de transferrine saturée, puis recherche de la perte. Électrophorèse si la ferritine n'explique pas la microcytose.", S(2, 9)),
        ("Instabilité d'abord, selon le cours. Ensuite ferritine. Basse : traiter et trouver la lésion. Normale avec inflammation : autre seuil, autre diagnostic.", S(3, 2)),
        ("Fer oral selon les notices 30124, 37448, 31644 et 35102. Fer veineux 57851 ou 15398 seulement si la carence est confirmée, avec les plafonds lus.", S(13, 12)),
        ("On traite la lésion, pas seulement le flacon. On poursuit les réserves dans la limite de chaque notice. On ne recharge pas une ferritine déjà haute.", S(3, 2)),
        ("Ferritine, cause, voie, plafond. Quatre mots. Le fer injectable sans carence confirmée est une contre-indication du numéro 57851.", S(12, 3)),
        ("Cas : femme de 46 ans, règles abondantes, hémoglobine 96 g/l, volume 71 femtolitres, ferritine 9 µg/l. Fer oral, avis gynécologique, et digestif si un signe l'exige.", S(1, 3)),
    ])
    wins = []
    wins.append(W(
        ("On nomme carence en fer une baisse des réserves, avec ou sans anémie. L'anémie vient après. Le cours F2.16 fixe l'hémoglobine. Ici, le diagnostic est martial.", S(3, 1)),
        ("Chez l'adulte sans inflammation, une ferritine sous 15 µg/l indique des réserves absentes. Sous 30 µg/l, les réserves sont basses. La limite basse de beaucoup de laboratoires se situe entre ces deux chiffres.", S(2, 3)),
        ("Une ferritine sous 15 µg/l a une spécificité citée de 0,99. Un seuil de 45 µg/l garde une spécificité de 0,92 et peut faire discuter l'enquête, surtout s'il y a une inflammation.", S(3)),
        ("Au-dessus de 150 µg/l, une carence absolue est peu probable, même avec une inflammation. On ne parle plus de ce diagnostic. On cherche une autre cause d'anémie.", S(3, 2)),
        ("La carence sans anémie existe. Maltofer, numéro 30124, prévoit alors 50 à 100 mg de fer par jour chez l'adolescent et l'adulte, contre 100 à 300 mg s'il y a une anémie ferriprive.", S(13)),
        ("Le premier trimestre utilise le seuil d'hémoglobine de 110 g/l et le fer veineux y est contre-indiqué, numéro 57851. La ferritine de grossesse lue pour le premier trimestre est inférieure à 15 µg/l.", S(1, 2, 12)),
    ))
    wins.append(W(
        ("La cause la plus fréquente d'anémie dans le monde est la carence alimentaire en fer. Ce DX est donc en tête de la leçon, pas en tête de l'urgence.", S(8)),
        ("Plus de 20 pour cent des personnes de plus de 85 ans sont anémiques dans le texte de 2021, et le fer contribue environ une fois sur deux, parfois avec une vitamine.", S(3)),
        ("Dans l'insuffisance cardiaque, une carence en fer au sens des marqueurs se voit dans 40 à 70 pour cent des cas. Le seuil n'est pas 15 µg/l : ferritine sous 100 µg/l, ou 100 à 299 µg/l si la fraction saturée est sous 20 pour cent.", S(3, 10)),
        ("Un tiers des maladies inflammatoires intestinales actives auraient une carence en fer dans l'estimation citée en 2021. Une ferritine jusqu'à 100 µg/l peut encore être une carence si l'inflammation est là, consensus de 2015.", S(3, 11)),
        ("Aucune part suisse chiffrée n'est écrite. On n'invente pas un pourcentage de cabinet.", S(8)),
    ))
    wins.append(W(
        ("Le fer entre par le duodénum, circule sur la transferrine, se stocke dans la ferritine. Une perte quotidienne supérieure à l'absorption vide le stock, puis l'hémoglobine.", S(3, 9)),
        ("Dans la carence absolue, l'hepcidine baisse. Le fer sort des macrophages. La ferritine s'effondre. C'est l'inverse de l'inflammation, où l'hepcidine haute bloque ce fer et la ferritine ne descend pas.", S(3)),
        ("Sans fer, l'hémoglobine ne se fabrique plus. Les globules deviennent petits. Le volume passe sous 80 femtolitres quand la carence est installée. Au début, le volume peut être encore normal : on ne récuse pas le diagnostic sur un volume à 84 femtolitres si la ferritine est à 8 µg/l.", S(8, 2)),
        ("Les réticulocytes restent bas : la moelle ne peut pas compenser. Une réticulocytose haute doit faire chercher un saignement récent ou une hémolyse, pas seulement une carence chronique.", S(8)),
        ("Le frottis de la carence installée montre des globules pâles, de taille inégale. Le texte de 2024 rappelle les cellules cibles dans d'autres contextes : elles ne signent pas le fer à elles seules. L'électrophorèse vient si la ferritine est normale.", S(9, 3)),
        ("La transferrine augmente quand les réserves baissent, et la fraction saturée baisse. Sous 20 pour cent, les textes lus parlent de restriction en fer. Dans la carence absolue simple, la ferritine basse suffit souvent.", S(3)),
    ))
    wins.append(W(
        ("Étape 1. Le patient saigne-t-il maintenant ? Si oui, le cours F2.16 et le seuil de 70 g/l ne retiennent pas un choc. On transfuse selon l'instabilité, on cherche la lésion, la ferritine attend une heure.", S(4)),
        ("Étape 2. Patient stable. NFS, ferritine, CRP, fraction saturée. On ne lance pas une coloscopie sans avoir confirmé la carence, recommandation de 2021.", S(3)),
        ("Étape 3. Ferritine sous 15 µg/l, ou sous 30 µg/l avec un tableau compatible : carence. On traite et on cherche la porte de sortie du fer.", S(2, 3)),
        ("Étape 4. Ferritine intermédiaire et CRP haute : on utilise le seuil de 70 µg/l chez l'adulte, ou les seuils cardiaque, rénal et digestif du cours, sans les mélanger dans la même phrase.", S(2, 10, 11)),
        ("Étape 5. Essai de fer oral si le bilan reste ambigu chez un patient anémique : au moins 10 g/l en deux semaines est très évocateur. Pas de hausse : observance, saignement continu, inflammation, autre diagnostic.", S(3)),
        ("Étape 6. Fer veineux seulement après confirmation. Anémie sans origine ferriprive confirmée : contre-indication, numéro 57851. Surcharge aussi.", S(12)),
    ))
    wins.append(W(
        ("On demande la durée. Une carence met des semaines. Une chute en deux jours est un saignement ou une hémolyse, même si une carence ancienne coexiste.", S(8)),
        ("Femme : abondance des règles, caillots, grossesse, accouchement, dispositif intra-utérin, don du sang. Homme et femme ménopausée : digestif jusqu'à preuve du contraire.", S(3)),
        ("Selles noires, sang rouge, douleur épigastrique, trouble du transit, perte de poids, antécédent de polype ou de cancer. Antiagrégant et anticoagulant aggravent une lésion muqueuse.", S(3)),
        ("Alimentation pauvre en viande chez l'enfant et la personne âgée, maladie cœliaque, gastrectomie, inhibiteur de la pompe à protons au long cours : malabsorption ou apport bas. On les écrit, ils ne dispensent pas de chercher un saignement si l'âge l'exige.", S(3)),
        ("Drapeaux : syncope, angor, mélæna actif, hypotension. Ils sortent de la consultation de fer et entrent dans la transfusion ou l'endoscopie urgente.", S(4)),
        ("Grossesse : trimestre exact, parce que le seuil d'hémoglobine et la contre-indication du fer veineux au premier trimestre en dépendent.", S(1, 12)),
    ))
    wins.append(W(
        ("Pâleur, pouls, tension. Une tachycardie avec mélæna n'attend pas la ferritine.", S(4)),
        ("On cherche une masse abdominale, une cicatrice de gastrectomie, des signes de maladie hépatique qui orienteraient vers une autre microcytose.", S(8)),
        ("Toucher rectal si le contexte digestif est là et si le patient est d'accord. Test de grossesse avant toute décision de fer veineux.", S(3, 12)),
        ("L'examen cutané fin n'est pas un critère lu dans les extraits. On ne retient pas le diagnostic sur l'aspect des ongles.", S(3)),
        ("Splénomégalie et ictère éloignent de la carence simple et rapprochent de l'hémolyse ou de la thalassémie. On ne donne pas du fer pour une rate.", S(9)),
    ))
    wins.append(W(
        ("Syndrome : microcytose hypoproliférative. Volume sous 80 femtolitres, réticulocytes sous 2 pour cent, ferritine basse.", S(8, 2)),
        ("Diagnostic différentiel principal : anémie inflammatoire. Ferritine normale ou haute, CRP haute, fraction saturée basse, hepcidine haute. Ce n'est pas ce DX.", S(3)),
        ("Deuxième différentiel : trait thalassémique. Ferritine normale, nombreux petits globules, électrophorèse anormale. Le fer au long cours surcharge.", S(9, 2)),
        ("Troisième : saignement aigu sur carence chronique. Réticulocytes qui montent, hémoglobine qui chute vite. On traite les deux temps.", S(8, 4)),
        ("Quatrième : anémie sidéroblastique et intoxication au plomb, après échec du tri ferritine-électrophorèse. Avis d'hématologie, pas un essai de fer veineux.", S(9)),
        ("Insuffisance cardiaque et rein utilisent d'autres seuils de ferritine, détaillés dans leurs DX. On ne les applique pas à une femme de 30 ans par ailleurs saine.", S(10, 3)),
    ))
    wins.append(W(
        ("Critère de réserve absente, adulte sain : ferritine inférieure à 15 µg/l. Critère de réserve basse : inférieure à 30 µg/l. Les deux viennent de textes différents, 2020 et 2021, et on les cite tous les deux.", S(2, 3)),
        ("Critère de probabilité inverse : ferritine supérieure à 150 µg/l, carence absolue peu probable.", S(3)),
        ("Critère de réponse : plus 10 g/l d'hémoglobine en deux semaines sous fer oral chez un patient anémique.", S(3)),
        ("Critère d'exclusion du fer veineux : anémie sans carence confirmée, surcharge, hypersensibilité au fer injectable, premier trimestre. Numéro 57851.", S(12)),
        ("La fraction saturée sous 20 pour cent renforce une restriction, elle ne remplace pas une ferritine à 8 µg/l ni une ferritine à 400 µg/l.", S(3)),
        ("L'anémie elle-même se lit sur le cours. Une ferritine à 8 µg/l avec une hémoglobine à 128 g/l chez une femme est une carence sans anémie : le seuil féminin est 120 g/l.", S(1, 2)),
    ))
    wins.append(W(
        ("Bilan minimal : hémoglobine, volume, réticulocytes, ferritine, CRP, fraction saturée, créatinine. Groupe si l'hémoglobine est basse ou le saignement possible.", S(9, 3)),
        ("Recherche de la perte : selon l'âge et les signes, avis gynécologique, test de sang occulte ou endoscopie. Le texte de 2021 veut la confirmation martiale avant cette enquête.", S(3)),
        ("Malabsorption : maladie cœliaque si l'histoire ou l'échec du fer oral le suggèrent. Gastrectomie dans les antécédents.", S(3)),
        ("Électrophorèse de l'hémoglobine si la microcytose persiste avec une ferritine normale. Numération des érythrocytes : élevés dans le trait, bas dans la carence avancée.", S(9)),
        ("Contrôle : hémoglobine à deux semaines si l'on utilise le critère de hausse de 10 g/l. Ferritine plus tard, pour les réserves, pas le lendemain du premier comprimé.", S(3)),
        ("Ne pas doser la ferritine seule au milieu d'une infection sans CRP. Le seuil change. On le recontrôle si la décision de fer veineux en dépend.", S(2)),
    ))
    wins.append(W(
        ("Si choc ou mélæna actif : quitter cet arbre, transfusion selon le terrain, hémostase. Revenir à la carence quand le patient est stable.", S(4)),
        ("Si stable et ferritine sous 15 µg/l : carence absolue. Traiter. Chercher la cause le même épisode, pas dans six mois.", S(2, 3)),
        ("Si ferritine entre 15 et 30 µg/l : réserves basses, conduite proche, surtout s'il y a une anémie microcytaire.", S(3)),
        ("Si ferritine entre 30 et 150 µg/l et CRP haute : ce n'est plus le critère de l'adulte sain. Seuil 70 µg/l, ou critères d'organe.", S(2)),
        ("Si ferritine au-dessus de 150 µg/l : arrêter l'hypothèse de carence absolue. Inflammation, thalassémie, autre.", S(3)),
        ("Si le fer oral échoue à deux semaines : vérifier la prise, le saignement, puis discuter la voie veineuse, pas un doublement aveugle au-delà des notices.", S(3, 12)),
    ))
    wins.append(W(
        ("Les doses qui suivent sont celles de l'AIPS suisse, lue le 31 octobre 2026, pas du compendium. Maltofer, numéro 30124. Adulte et adolescent dès 12 ans, anémie ferriprive : 100 à 300 mg de fer par jour. Sans anémie : 50 à 100 mg. Enfant de 1 à 12 ans, anémie : 50 à 100 mg. Avant 1 an : 25 à 50 mg. On prend le comprimé pendant ou après le repas selon la forme.", S(13)),
        ("Tardyferon, numéro 37448. Anémie légère ou carence latente : un comprimé retard le matin chez l'adulte, et chez l'enfant dès 10 ans. Anémie grave : deux comprimés chez l'adulte, matin et soir. L'enfant dès 10 ans reste à un comprimé, ou deux si la sévérité l'exige dans la phrase lue.", S(15)),
        ("Ferro-Gradumet, numéro 31644. Dès 12 ans et plus de 40 kg : un ou deux comprimés par jour avant le petit déjeuner, avalés sans être croqués ni sucés. La notice décrit une hausse d'hémoglobine de l'ordre de 2 à 3 g/dl en trois semaines : on la cite comme phrase de la notice, en grammes par décilitre, sans la convertir en seuil OMS.", S(16)),
        ("Ferrum Hausmann, numéro 35102. Une capsule par jour, deux ou trois si la carence est grave. Poursuite un à trois mois après la correction de l'anémie, sans dépasser six mois sans réévaluation. Enfants et adolescents : l'utilisation n'a pas été étudiée dans cette notice.", S(17)),
        ("Ferinject, numéro 57851. Dose unique au plus 1000 mg. Perfusion : au plus 20 mg de fer par kg, sans dépasser 1000 mg. Injection non diluée : au plus 15 mg de fer par kg, sans dépasser 1000 mg. Cumul hebdomadaire recommandé au plus 1000 mg. Hémodialyse : au plus 200 mg par jour. Contre-indiqué sans carence confirmée, en cas de surcharge, d'hypersensibilité, et au premier trimestre. Hémoglobine revérifiée au plus tôt à quatre semaines. Équipe d'anaphylaxie présente. Pas recommandé chez l'enfant dans les phrases lues.", S(12)),
        ("Venofer, numéro 15398. Intraveineux lent seulement, jamais sous-cutané ni intramusculaire. Au plus 200 mg par injection, au plus 500 mg par perfusion. Dose cumulée calculée, non dépassée. Même vigilance d'hypersensibilité.", S(14)),
        ("Maltofer Fol, numéro 46538, si l'anémie ferriprive s'accompagne d'un besoin en folate, notamment la grossesse : deux à trois comprimés par jour, puis un comprimé jusqu'à la fin de la grossesse après correction de l'hémoglobine.", S(28)),
        ("Transfusion : seulement selon les seuils du cours, pas pour une ferritine basse. Un patient stable à 96 g/l ne relève pas du seuil de 70 g/l.", S(4)),
    ))
    wins.append(W(
        ("Prévenir la rechute, c'est trouver la lésion : fibrome, ulcère, cancer, don du sang trop fréquent, alimentation. Un fer bien pris sur une lésion qui saigne encore ne tient pas.", S(3)),
        ("Après correction, poursuivre les réserves dans la durée écrite sur la notice, puis arrêter. Ferrum Hausmann : pas plus de six mois sans regarder. Une ferritine qui dépasse 150 µg/l n'est plus une indication de recharge.", S(17, 3)),
        ("Grossesse : prévenir tôt. Maltofer Fol couvre fer et folate. AndreaFol, numéro 54718, est le folate périconceptionnel, un comprimé par jour, distinct du traitement d'une anémie déjà constituée.", S(28, 27)),
        ("Ne pas donner de fer à un trait thalassémique « par prudence ». La ferritine se mesure d'abord.", S(9, 2)),
        ("Éduquer : selles noires sous fer oral, sans mélæna vrai. Douleur thoracique ou vrai sang rouge : ce n'est pas l'effet du comprimé, on consulte.", S(3)),
    ))
    wins.append(W(
        ("Ferritine sous 15 µg/l : réserves absentes. Sous 30 µg/l : réserves basses. Au-dessus de 150 µg/l : carence absolue peu probable. Inflammation : seuil adulte 70 µg/l, pas ces chiffres-là.", S(2, 3)),
        ("Confirmation avant coloscopie et avant Ferinject. Hausse d'au moins 10 g/l en deux semaines : argument fort.", S(3, 12)),
        ("Plafonds veineux : 1000 mg, 20 mg par kg en perfusion, 15 mg par kg en injection, 200 mg par jour en hémodialyse, pas au premier trimestre.", S(12)),
        ("Oraux : 100 à 300 mg de fer Maltofer s'il y a anémie, un ou deux comprimés selon les autres notices, pas de croquer Ferro-Gradumet.", S(13, 16)),
        ("Cause de la perte dans le même épisode. Homme et femme ménopausée : digestif. Femme réglée : utérus, et digestif si l'âge ou les signes l'exigent.", S(3)),
    ))
    wins.append(W(
        ("Cas corrigé. Femme de 46 ans, règles de huit jours avec caillots, fatigue, hémoglobine 96 g/l, volume 71 femtolitres, réticulocytes bas, ferritine 9 µg/l, CRP normale. Anémie chez la femme, seuil 120 g/l, bande modérée 80 à 109. Carence absolue. Pas de transfusion : 96 g/l et patiente stable. Maltofer 100 à 300 mg de fer par jour. Avis gynécologique. Pas de Ferinject d'emblée si l'oral est possible. Contrôle de l'hémoglobine à deux semaines, hausse attendue d'au moins 10 g/l.", S(1, 2, 3, 13, 4)),
        ("Variante. Même femme, hémoglobine 68 g/l, vertiges au lever, pas de mélæna. 68 g/l est sous 70 g/l et dans la bande sévère sous 80 g/l. On discute une transfusion parce que le seuil restrictif est franchi et la tolérance est mauvaise, une unité, puis on remesure. Le fer oral commence en même temps. On ne retient pas le culot « pour dépasser 120 g/l ».", S(4, 1)),
        ("Variante homme de 68 ans, ferritine 11 µg/l, hémoglobine 104 g/l, sans plainte digestive. La carence est confirmée. L'enquête digestive ne se discute pas comme option facile : le texte de 2021 la place au centre chez l'homme. Le fer traite, il ne remplace pas la coloscopie.", S(3)),
        ("Piège. Ferritine 22 µg/l étiquetée normale par un laboratoire dont la borne basse est 20. Le texte de 2021 parle de réserves basses sous 30 µg/l. On ne rassure pas.", S(3)),
        ("Piège. Ferinject 1000 mg posé pour une anémie à 88 g/l sans ferritine, « elle est microcytaire ». Contre-indication : anémie sans origine ferriprive confirmée. Un trait thalassémique reçoit ainsi une surcharge.", S(12, 9)),
        ("Piège. Contrôle de ferritine à 48 heures, encore basse, et second 1000 mg dans la même semaine. Le cumul hebdomadaire lu est 1000 mg, et l'hémoglobine ne se relit pas avant quatre semaines.", S(12)),
        ("Piège du premier trimestre. Ferinject « parce que l'oral donne des nausées ». La notice contre-indique ce trimestre. On change de sel oral ou l'on attend, on ne franchit pas la contre-indication.", S(12)),
    ))
    cas = [
        ("Femme de 19 ans, étudiante, viande rare, règles normales.", "Hémoglobine 112 g/l, volume 78 femtolitres, ferritine 14 µg/l, CRP normale.",
         "Anémie au seuil féminin de 120 g/l, bande légère. Ferritine sous 15 µg/l : réserves absentes. Pas d'inflammation.",
         "Fer oral, apport alimentaire, pas d'endoscopie de principe à cet âge sans signe digestif. Contrôle à deux semaines."),
        ("Femme de 38 ans, règles très abondantes, stable.", "Hémoglobine 88 g/l, volume 68 femtolitres, ferritine 7 µg/l.",
         "Bande modérée 80 à 109. Carence absolue. Au-dessus de 70 g/l, patiente stable : pas de culot.",
         "Maltofer 100 à 300 mg de fer par jour. Avis gynécologique dans la semaine. Digestif si un symptôme apparaît."),
        ("Femme de 52 ans, ménopausée depuis un an.", "Hémoglobine 101 g/l, volume 74 femtolitres, ferritine 12 µg/l.",
         "Carence absolue. L'explication gynécologique ne suffit plus.",
         "Fer oral et enquête digestive selon le texte de 2021, sans attendre six mois de fer."),
        ("Homme de 60 ans, aspirine quotidienne, épigastralgies.", "Hémoglobine 109 g/l, volume 76 femtolitres, ferritine 18 µg/l.",
         "Sous 30 µg/l : réserves basses. Anémie masculine, seuil 130 g/l, bande modérée.",
         "Arrêt discuté de l'aspirine avec le prescripteur, fer, endoscopie haute puis basse."),
        ("Homme de 72 ans, anticoagulant, selles noires un jour, aujourd'hui stables, tension normale.", "Hémoglobine 118 g/l, ferritine 16 µg/l.",
         "Carence. Le mélæna d'hier n'est plus un choc, mais ce n'est pas un fer seul.",
         "Groupe déjà fait, surveillance, endoscopie rapide, fer. Seuil de 70 g/l non franchi."),
        ("Enfant de 18 mois, lait de vache exclusif.", "Hémoglobine 98 g/l.",
         "De 6 à 23 mois le seuil est 105 g/l. 98 g/l est dans la bande légère 95 à 104. La ferritine confirme le fer, l'alimentation le rend probable.",
         "Diversification, fer oral adapté au poids selon Maltofer : avant un an la notice dit 25 à 50 mg, ici 18 mois est dans la tranche 1 à 12 ans, 50 à 100 mg s'il y a anémie. On pèse l'enfant."),
        ("Garçon de 8 ans, ferritine basse, pas de saignement.", "Hémoglobine 108 g/l, volume 70 femtolitres.",
         "De 5 à 11 ans, seuil 115 g/l. Anémie légère 110 à 114 serait au-dessus de 108 : 108 est sous 110, donc bande modérée 80 à 109.",
         "Fer oral 50 à 100 mg. Chercher saignement occulte et maladie cœliaque si pas de réponse."),
        ("Femme au premier trimestre, nausées sous comprimé.", "Hémoglobine 104 g/l, ferritine 10 µg/l.",
         "Seuil du premier trimestre 110 g/l. 104 g/l est dans la bande légère 100 à 109. Carence absolue.",
         "Changer de sel oral ou l'horaire. Ferinject contre-indiqué ce trimestre. Pas de voie veineuse pour confort."),
        ("Femme au deuxième trimestre, oral impossible, vomissements.", "Hémoglobine 96 g/l, ferritine 8 µg/l.",
         "Seuil 105 g/l. 96 g/l est légère, bande 95 à 104. Carence confirmée.",
         "Le premier trimestre est passé : Ferinject devient discutable, avec les plafonds 1000 mg et 20 mg par kg, équipe d'anaphylaxie, et le poids d'avant la grossesse pour le calcul lu."),
        ("Femme au troisième trimestre, stable.", "Hémoglobine 108 g/l, ferritine 13 µg/l.",
         "Seuil 110 g/l, anémie légère. Réserves absentes.",
         "Maltofer Fol deux à trois comprimés, puis un jusqu'à l'accouchement. Transfusion non indiquée."),
        ("Homme insuffisant cardiaque, essoufflé.", "Hémoglobine 124 g/l, ferritine 80 µg/l, fraction saturée à 18 pour cent.",
         "Anémie masculine légère, bande 110 à 129. Carence en fer au sens de 2016 : ferritine sous 100 µg/l. Ce n'est pas le seuil de 15.",
         "On le dit au cardiologue. On ne conclut pas « pas de carence » parce que 80 dépasse 30."),
        ("Patiente de dialyse péritonéale.", "Hémoglobine 102 g/l, ferritine 90 µg/l, fraction saturée à 16 pour cent.",
         "Le texte de 2021 définit la carence absolue rénale par une fraction d'au plus 20 pour cent et une ferritine d'au plus 100 µg/l avant dialyse ou en péritonéal.",
         "Fer selon le néphrologue, souvent veineux. Eprex seulement après le fer, cible 10 à 12 g/dl, pas le sujet de ce DX seul."),
        ("Hémodialysé.", "Ferritine 180 µg/l, fraction saturée à 15 pour cent, hémoglobine 96 g/l.",
         "En hémodialyse le seuil de ferritine lu pour la carence absolue monte à 200 µg/l avec une fraction d'au plus 20 pour cent. 180 reste dans cette définition.",
         "Ferinject au plus 200 mg par jour dans cette situation, pas 1000 mg d'un coup par habitude de ville."),
        ("Maladie de Crohn active.", "Hémoglobine 99 g/l, ferritine 80 µg/l, CRP haute, fraction saturée basse.",
         "Consensus de 2015 : jusqu'à 100 µg/l, la ferritine peut encore être une carence si l'inflammation est là. Seuil OMS adulte femme si c'est une femme : on vérifie le sexe avant l'adjectif.",
         "Fer veineux souvent mieux absorbé que l'oral dans ce contexte, après confirmation clinique, plafonds du 57851."),
        ("Ferritine 6 µg/l, hémoglobine 130 g/l, homme.", "Volume 82 femtolitres, CRP normale.",
         "Pas d'anémie : le seuil masculin est 130 g/l, 130 n'est pas inférieur. Carence sans anémie, volume encore normal.",
         "Maltofer 50 à 100 mg, pas la dose d'anémie. Chercher une perte débutante chez l'homme."),
        ("Ferritine 220 µg/l, femme non enceinte, hémoglobine 118 g/l, CRP normale.", "Volume 70 femtolitres.",
         "Anémie féminine. Ferritine au-dessus de 150 µg/l : carence absolue peu probable. Microcytose à expliquer autrement, thalassémie en tête.",
         "Pas de fer. Électrophorèse. Le piège serait le Ferinject « pour la microcytose »."),
        ("Échec à deux semaines.", "Hémoglobine passée de 96 à 98 g/l sous Tardyferon un comprimé, ferritine initiale 9 µg/l.",
         "La hausse est inférieure à 10 g/l. Le critère de 2021 n'est pas rempli.",
         "Vérifier la prise à jeun ou selon la notice, le saignement qui continue, puis discuter deux comprimés si l'anémie est grave selon Tardyferon, ou la voie veineuse. Pas un troisième mois identique."),
        ("Réussite à deux semaines.", "Hémoglobine de 100 à 114 g/l, femme.",
         "Hausse d'au moins 10 g/l. Carence absolue très probable même si un dosage avait été ambigu.",
         "Poursuivre, chercher quand même la cause, ne pas arrêter le jour de la hausse : les réserves ne sont pas reconstruites."),
        ("Donneur de sang régulier, homme de 40 ans.", "Hémoglobine 128 g/l, ferritine 11 µg/l.",
         "Anémie limite, seuil 130. Carence absolue. Le don explique, il ne dispense pas de compter les dons et d'écarter un symptôme digestif.",
         "Suspendre les dons, fer oral, recontrôler. Endoscopie si un signe ou si la ferritine rechute sans don."),
        ("Personne âgée de 86 ans, plusieurs causes possibles.", "Hémoglobine 106 g/l, volume 84 femtolitres, ferritine 28 µg/l, CRP discrètement haute, créatinine élevée.",
         "Anémie. Ferritine sous 30 µg/l : réserves basses, et sous 70 µg/l donc aussi dans la zone inflammatoire. Le rein coexiste. Le volume n'est pas encore microcytaire.",
         "Ne pas choisir un seul DX. Fer avec prudence, bilan rénal, pas de fer veineux massif sans confirmer que la carence domine."),
        ("Après gastrectomie, femme de 55 ans.", "Hémoglobine 100 g/l, ferritine 15 µg/l, cobalamine basse.",
         "Deux carences. La ferritine à 15 n'est pas sous 15 : réserves basses au sens de 30. La cobalamine se traite en même temps, sinon la réponse est incomplète.",
         "Fer et Vitarubine selon le schéma sans ou avec neurologie. Pas de folate seul."),
        ("Surcharge évitée.", "Ferritine 640 µg/l, hémoglobine 140 g/l, homme, CRP normale.",
         "Pas d'anémie. Au-dessus de 500 µg/l chez l'adulte, évaluation, pas de fer. Au-dessus de 200 µg/l chez l'homme sain, le tableau de 2020 parle déjà de risque de surcharge.",
         "Arrêt de tout fer. Avis pour hémochromatose ou autre cause. Ce n'est pas ce DX."),
        ("Enfant de 4 ans, seuil différent du nourrisson.", "Hémoglobine 102 g/l, ferritine 10 µg/l.",
         "24 à 59 mois : seuil 110 g/l. 102 g/l est dans la bande légère 100 à 109. Ferritine sous 12 µg/l : carence chez l'enfant de moins de 5 ans.",
         "Fer oral de la tranche 1 à 12 ans. Le chiffre 102 g/l n'aurait pas la même bande à 9 mois."),
        ("Adolescente de 14 ans.", "Hémoglobine 118 g/l, ferritine 9 µg/l, volume 73 femtolitres.",
         "12 à 14 ans : seuil 120 g/l, pas encore le seuil de l'adulte selon le sexe pour la fille... la ligne fille est 120 g/l, identique à la femme. Anémie légère 110 à 119. Carence absolue.",
         "Maltofer dès 12 ans : dose adulte, 100 à 300 mg s'il y a anémie. Règles souvent en cause. On pose la question."),
    ]
    extra = []
    for qui, labo, lecture, conduite in cas:
        extra.append(P(
            f"Situation. {qui} {labo} Lecture. {lecture} Conduite. {conduite}",
            S(1, 2, 3, 12, 13)))
    wins[-1] += "".join(extra)
    drills = [
        (32, "femme", 119, 11, "Règles abondantes, stable.", "Fer oral. Pas de culot. Avis gynécologique."),
        (32, "femme", 109, 11, "Même femme, hémoglobine plus basse.", "Toujours au-dessus de 70 g/l. Bande modérée. Même conduite, surveillance plus proche."),
        (32, "femme", 79, 6, "Malaise au lever, pas de mélæna.", "79 g/l est une anémie sévère et reste au-dessus de 70 g/l. Pas de culot systématique. Fer oral et surveillance. Un vrai choc ferait quitter ce seuil."),
        (44, "homme", 129, 9, "Fatigue isolée.", "Anémie légère masculine. Carence absolue. Enquête digestive, fer oral."),
        (44, "homme", 110, 9, "Même biologie un mois plus tard sans fer.", "Bande légère basse. On ne se rassure pas parce que 110 dépasse 70."),
        (44, "homme", 80, 9, "Angor d'effort.", "Bande modérée, pile sur 80 g/l. Le syndrome coronarien, s'il est aigu, utilise le seuil de 80 g/l : on caractérise la douleur avant de refuser un culot."),
        (70, "homme", 78, 20, "Stable, pas de douleur thoracique.", "Sous 80 g/l, au-dessus de 70 g/l. Pas de culot si vraiment stable et non coronarien. Fer et enquête. Réserves basses, ferritine sous 30 µg/l."),
        (28, "femme", 100, 40, "Crohn en poussée, CRP haute.", "Ferritine 40 µg/l est sous 70 µg/l : le seuil inflammatoire adulte est franchi. Ce n'est pas le seuil de 15."),
        (28, "femme", 100, 90, "Crohn en poussée, CRP haute.", "90 µg/l reste sous 100 µg/l : le consensus digestif de 2015 peut encore retenir une carence. On ne dit pas l'inverse avec le seul seuil de 15."),
        (28, "femme", 100, 180, "Crohn calme, CRP normale.", "180 µg/l dépasse 150 µg/l : carence absolue peu probable. On cherche une autre cause de l'anémie."),
        (60, "homme", 115, 90, "Insuffisance cardiaque.", "Ferritine sous 100 µg/l : carence au sens cardiaque de 2016, et anémie masculine légère."),
        (60, "homme", 115, 180, "Insuffisance cardiaque, fraction saturée à 14 pour cent.", "Ferritine entre 100 et 299 avec fraction sous 20 pour cent : carence cardiaque quand même. On ne s'arrête pas à 180."),
        (60, "homme", 115, 400, "Insuffisance cardiaque, fraction saturée à 30 pour cent.", "Ni sous 100, ni fraction basse. Ce n'est pas la carence de 2016. On ne donne pas de fer sur l'anémie seule."),
        (50, "femme", 108, 8, "Cœliaque connue, peu observante du régime.", "Carence absolue et anémie modérée. Régime et fer. L'échec de l'oral fera discuter la voie veineuse, pas un oubli de la maladie."),
        (36, "femme", 97, 12, "Post-partum de trois semaines, stable.", "Anémie modérée, réserves absentes. Fer oral. Le post-partum n'est plus le premier trimestre : la contre-indication du 57851 ne s'y lit pas, l'oral reste le premier choix s'il passe."),
        (17, "femme", 121, 8, "Sportive, règles normales.", "121 g/l n'est pas sous 120 g/l : pas d'anémie. Ferritine sous 15 µg/l : carence sans anémie. Dose de Maltofer sans anémie, 50 à 100 mg, pas 100 à 300 mg."),
        (9, "enfant", 112, 9, "Garçon, alimentation pauvre.", "5 à 11 ans, seuil 115 g/l. 112 g/l est léger, bande 110 à 114. Ferritine d'enfant sous 15 µg/l : la ligne de 5 ans et plus du tableau 2020 est 15, pas 12."),
        (3, "enfant", 111, 11, "Fille.", "24 à 59 mois, seuil 110 g/l. 111 g/l n'est pas une anémie. Ferritine sous 12 µg/l : carence du petit enfant sans anémie. On traite le fer, on ne dit pas anémie."),
        (1, "enfant", 100, 8, "Nourrisson de 14 mois.", "6 à 23 mois, seuil 105 g/l. 100 g/l est léger, bande 95 à 104. Fer de la tranche 1 à 12 ans."),
        (13, "garçon", 119, 10, "Poussée de croissance.", "12 à 14 ans, seuil 120 g/l pour les garçons aussi. 119 g/l est léger. On n'utilise pas 130 g/l."),
        (16, "garçon", 125, 10, "Après 15 ans.", "Homme au sens du tableau dès 15 ans : seuil 130 g/l. 125 g/l est une anémie légère. Le seuil de 120 g/l de l'adolescent de 14 ans ne s'applique plus."),
        (45, "femme", 90, 9, "Sous Ferro-Gradumet depuis cinq jours, selles noires, pas de malaise.", "Effet attendu du fer oral, à distinguer d'un mélæna avec tachycardie. On continue, on revoit à deux semaines, on n'arrête pas pour des selles noires isolées."),
        (45, "femme", 90, 9, "Méléna vrai, tension 85/50.", "On quitte le fer oral. Hémorragie majeure. Transfusion selon le choc, pas selon 70 g/l. La ferritine basse explique la chronicité, pas l'urgence de l'heure."),
        (66, "homme", 92, 4, "Coloscopie prévue, stable.", "Carence absolue confirmée avant l'examen, comme le demande 2021. Hémoglobine au-dessus de 70 et de 80 g/l : pas de culot pour « passer » l'endoscopie si le patient est stable. L'équipe d'endoscopie peut avoir sa propre exigence : on la discute, on ne l'invente pas ici."),
        (29, "femme", 107, 16, "Deuxième trimestre.", "Seuil 105 g/l : 107 g/l n'est pas une anémie ce trimestre. Ferritine 16 µg/l est au-dessus de 15 et sous 30 : réserves basses. Fer oral préventif et thérapeutique selon la notice de grossesse, pas une étiquette d'anémie fausse."),
        (29, "femme", 94, 16, "Deuxième trimestre, vomissements.", "94 g/l est sous 95 : bande modérée 70 à 94 de ce trimestre, et sévère seulement sous 70. Carence au sens des réserves basses. Voie veineuse discutable hors premier trimestre si l'oral est impossible."),
        (80, "homme", 100, 25, "Plusieurs médicaments, créatinine haute, CRP 20.", "Réserves basses sous 30 µg/l et sous le seuil inflammatoire de 70. Le rein est un second mécanisme. On ne résume pas à un comprimé."),
        (41, "homme", 140, 12, "Bilan d'entreprise.", "Pas d'anémie. Carence absolue. Chez l'homme, chercher une perte même sans anémie, surtout si la ferritine est à 12 µg/l."),
        (55, "femme", 86, 5, "Stable, ménopausée.", "Anémie modérée, réserves absentes. Au-dessus de 70 g/l et de 80 g/l. Fer oral, coloscopie et gastroscopie, pas de culot."),
        (55, "femme", 86, 5, "Douleur thoracique au repos.", "Même chiffre, autre seuil : syndrome coronarien aigu, 80 g/l. 86 g/l reste au-dessus. On traite le cœur, on ne transfuse pas seulement pour le fer, on surveille l'hémoglobine de près."),
        (63, "homme", 69, 8, "Stable, pâleur, pas de saignement.", "69 g/l est sous 70 g/l. Une unité, remesure, cible 70 à 90 g/l, fer et enquête en parallèle."),
        (24, "femme", 132, 7, "Règles normales.", "132 g/l est au-dessus de 120 g/l : pas d'anémie. Ferritine 7 µg/l : carence sans anémie. Dose sans anémie, 50 à 100 mg."),
    ]
    lignes_age = {
        "femme": (120, 110, 80),
        "homme": (130, 110, 80),
    }
    outd = []
    for age, sexe, hb, fer, contexte, conduite in drills:
        if sexe in lignes_age:
            seuil, bas_legere, bas_moderee = lignes_age[sexe]
            if hb >= seuil:
                bande = "pas d'anémie"
            elif hb >= bas_legere:
                bande = "anémie légère"
            elif hb >= bas_moderee:
                bande = "anémie modérée"
            else:
                bande = "anémie sévère"
            entete = f"Adulte, {sexe}, {age} ans, hémoglobine {hb} g/l, donc {bande} au seuil de {seuil} g/l."
        else:
            entete = f"Enfant ou situation déjà qualifiée, {age} ans, hémoglobine {hb} g/l."
        outd.append(P(
            f"Exercice. {entete} Ferritine {fer} µg/l. Contexte : {contexte} Décision : {conduite}",
            S(1, 2, 3, 4, 10, 11)))
    wins[-1] += "".join(outd)
    ecrire(1, "Carence en fer",
           P("Carence en fer : réserves vides, souvent microcytose, fer seulement après confirmation. Les seuils d'hémoglobine et de transfusion sont ceux du cours F2.16.", S(3, 1)),
           fiche, wins)


if __name__ == "__main__":
    dx1()
    print("dx1")

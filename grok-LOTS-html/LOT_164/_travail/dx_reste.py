#!/usr/bin/env python3
"""DX.2 à DX.10. Le détail propre à chaque mécanisme est dans les fenêtres."""
from dx_base import P, S, W, ecrire

def F(lignes):
    return [P(t, s) for t, s in lignes]

def ajouter(wins, rows, sources):
    wins[-1] += "".join(P(f"Exercice. {a} {b} Décision. {c}", sources) for a, b, c in rows)
    return wins

def dx2():
    fiche = F([
        ("L'anémie inflammatoire est une anémie de production où le fer est bloqué dans les macrophages. Les seuils d'hémoglobine restent ceux du cours F2.16.", S(3, 1)),
        ("Elle accompagne infection, maladie inflammatoire, cancer, insuffisance cardiaque. Elle est fréquente chez les plus de 85 ans, souvent mêlée au fer.", S(3, 8)),
        ("L'hepcidine haute ferme la ferroportine. La ferritine ne s'effondre pas. La fraction de transferrine saturée baisse.", S(3)),
        ("On dose la CRP avec la ferritine. Le seuil adulte de carence en inflammation est 70 µg/l, pas 15 µg/l.", S(2)),
        ("On cherche la maladie causale : fièvre, amaigrissement, toux, diarrhée, articulation, cancer connu.", S(8)),
        ("Fièvre, foyer, rate, adénopathies, masse. L'examen cherche la cause, pas un signe cutané de carence.", S(8)),
        ("Souvent normocytaire, microcytaire si elle dure. Réticulocytes bas.", S(8, 9)),
        ("Ferritine normale ou haute, CRP haute, fraction saturée basse. Sous 70 µg/l chez l'adulte inflammatoire, une carence peut coexister.", S(2, 3)),
        ("NFS, réticulocytes, ferritine, CRP, fraction saturée, créatinine. Bilan de la maladie causale.", S(2, 9)),
        ("Écarter le choc et la microangiopathie. Puis séparer carence absolue, inflammation pure, et les deux ensemble.", S(6, 2)),
        ("On traite la cause. Le fer veineux n'est pas un réflexe. S'il est indiqué, les plafonds AIPS du cours s'appliquent, numéros 57851 et 15398.", S(12, 14)),
        ("Traiter l'infection, la poussée, le cancer. Contrôler la ferritine quand la CRP baisse.", S(2)),
        ("Hepcidine, CRP, seuil 70 µg/l, pas de fer injectable sans carence retenue.", S(2, 12)),
        ("Cas : pneumonie, hémoglobine 102 g/l chez un homme, ferritine 160 µg/l, CRP haute. On traite le poumon. 160 µg/l n'est pas sous 70 µg/l.", S(1, 2)),
    ])
    wins = []
    wins.append(W(
        ("On parle d'anémie inflammatoire quand la production chute au cours d'une maladie qui élève les protéines de phase aiguë, avec un fer circulant bas et des réserves non vides.", S(3, 9)),
        ("Elle peut exister sans infection visible : cancer, maladie de système, insuffisance cardiaque. Le nom « maladie chronique » du texte de 2024 désigne la même famille.", S(9, 8)),
        ("Ce n'est pas une carence absolue. La ferritine au-dessus de 150 µg/l rend la carence absolue peu probable, phrase de 2021, même s'il y a une inflammation.", S(3)),
        ("Une carence peut s'y ajouter. Le seuil conditionnel de 2020 est 70 µg/l chez l'adulte et 30 µg/l avant 5 ans.", S(2)),
        ("Les seuils cardiaques, rénaux et digestifs du cours ne se substituent pas les uns aux autres. On nomme l'organe avant de choisir le chiffre.", S(10, 11, 3)),
        ("L'AIPS interdit le fer veineux si la carence n'est pas confirmée. Une inflammation isolée n'est pas cette confirmation.", S(12)),
    ))
    wins.append(W(
        ("Chez les plus de 85 ans, l'anémie dépasse 20 pour cent et plusieurs mécanismes coexistent. L'inflammation en fait partie, avec le fer, le rein et les médicaments.", S(3)),
        ("L'insuffisance cardiaque montre une carence en fer dans 40 à 70 pour cent des cas du texte de 2021, souvent par inflammation et malabsorption, pas seulement par saignement.", S(3)),
        ("Un tiers des maladies inflammatoires de l'intestin actives auraient une carence martiale associée. L'inflammation seule n'explique pas tout le chiffre.", S(3, 11)),
        ("Pas de prévalence suisse lue. On ne la fabrique pas.", S(8)),
        ("Ce DX n'est pas le plus urgent. Il vient après la microangiopathie, le choc et l'hémolyse aiguë dans l'ordre E.", S(6, 4)),
    ))
    wins.append(W(
        ("L'interleukine de l'inflammation augmente l'hepcidine hépatique. La ferroportine se ferme. Le fer des macrophages ne sort plus. La moelle en manque alors que le stock est là.", S(3)),
        ("La ferritine, protéine de phase aiguë, monte. Elle masque une carence modérée. D'où le seuil relevé à 70 µg/l, pas un abandon du dosage.", S(2)),
        ("La transferrine baisse, à l'inverse de la carence absolue où elle monte. La fraction saturée est basse dans les deux. Elle ne les sépare pas seule.", S(3, 9)),
        ("Le volume reste souvent entre 80 et 100 femtolitres. Il peut passer sous 80 si l'inflammation dure. Les réticulocytes restent sous 2 pour cent.", S(8)),
        ("L'EPO rénale peut être insuffisante en plus, surtout si le rein est malade. Les deux mécanismes s'additionnent. On les écrit séparément.", S(22, 3)),
        ("Le fer injectable ne contourne l'hepcidine que s'il y a vraiment une carence à traiter. Il ne soigne pas la pneumonie.", S(12)),
    ))
    wins.append(W(
        ("On écarte d'abord l'instabilité, les schizocytes avec thrombopénie, et le saignement actif. Ce DX est un diagnostic de patient stable ou de malade déjà pris en charge.", S(4, 6)),
        ("NFS, réticulocytes, ferritine, CRP, fraction saturée, créatinine. Les quatre derniers se lisent ensemble.", S(2, 9)),
        ("Ferritine sous 15 µg/l malgré la CRP : carence absolue, même en contexte inflammatoire. On traite le fer et la cause.", S(2, 3)),
        ("Ferritine entre 15 et 70 µg/l avec CRP haute chez l'adulte : carence possible selon 2020. On ne la nie pas.", S(2)),
        ("Ferritine au-dessus de 150 µg/l : carence absolue peu probable. On traite la maladie. On ne recharge pas.", S(3)),
        ("Si l'organe a son propre seuil, on le cite : cœur 2016, rein 2021, intestin 2015. On ne les mélange pas.", S(10, 3, 11)),
    ))
    wins.append(W(
        ("Fièvre, toux, dysurie, diarrhée, articulation, amaigrissement, sueurs, cancer connu, poussée de maladie inflammatoire.", S(8)),
        ("Médicaments : on cherche ceux qui saignent ou ceux qui causent une hémolyse, pour ne pas tout mettre sur l'inflammation.", S(9)),
        ("Durée : une anémie le jour d'une pneumonie aiguë peut être ancienne. On demande le dernier hémogramme.", S(8)),
        ("Drapeaux qui font quitter ce DX : purpura, confusion, mélæna, douleur thoracique, instabilité.", S(4, 6)),
        ("Insuffisance cardiaque : essoufflement qui change, œdèmes. Le seuil de fer n'est pas celui de la ville.", S(10)),
        ("Grossesse fébrile : le trimestre fixe le seuil d'hémoglobine et la contre-indication du fer veineux au premier trimestre.", S(1, 12)),
    ))
    wins.append(W(
        ("Fièvre, foyer infectieux, articulation chaude, éruption, adénopathie, masse, souffle nouveau.", S(8)),
        ("Pâleur sans ictère ni rate oriente moins vers l'hémolyse. Une rate et un ictère font demander le panneau d'hémolyse avant de conclure à l'inflammation.", S(9)),
        ("Tension et pouls : une tachycardie fébrile n'est pas à elle seule une indication transfusionnelle.", S(4)),
        ("Examen pulmonaire, abdominal, cutané, articulaire : la cause se voit parfois. On l'écrit.", S(8)),
        ("Pas de critère diagnostique dans l'aspect des ongles. On s'en tient aux dosages.", S(3)),
    ))
    wins.append(W(
        ("Syndrome : normocytaire ou discrètement microcytaire, réticulocytes bas, fer circulant bas, ferritine non effondrée.", S(8, 9)),
        ("Différentiel : carence en fer absolue. Ferritine sous 15 µg/l, transferrine haute.", S(2, 3)),
        ("Différentiel : rein. Créatinine haute, EPO insuffisante. Les deux peuvent coexister.", S(22)),
        ("Différentiel : moelle. Une deuxième ou troisième lignée basse, des blastes. L'inflammation ne donne pas des blastes.", S(9)),
        ("Différentiel : hémolyse. Réticulocytes hauts, LDH, haptoglobine, ictère.", S(9)),
        ("Différentiel : thalassémie. Microcytose ancienne, ferritine normale, électrophorèse.", S(9)),
    ))
    wins.append(W(
        ("Critère pratique : maladie inflammatoire ou infectieuse identifiée, réticulocytes bas, ferritine non basse au sens de 15 µg/l, CRP haute.", S(2, 8)),
        ("Critère de carence associée, adulte : ferritine sous 70 µg/l dans l'inflammation, recommandation conditionnelle de 2020.", S(2)),
        ("Critère inverse : ferritine au-dessus de 150 µg/l, carence absolue peu probable, texte de 2021.", S(3)),
        ("Critère cardiaque : ferritine sous 100 µg/l ou 100 à 299 µg/l avec fraction saturée sous 20 pour cent.", S(10)),
        ("Critère intestinal actif : ferritine jusqu'à 100 µg/l encore compatible avec une carence, 2015.", S(11)),
        ("Critère rénal : fraction saturée d'au plus 20 pour cent et ferritine d'au plus 100 ou 200 µg/l selon la dialyse, texte de 2021.", S(3)),
    ))
    wins.append(W(
        ("CRP ou une autre protéine de phase aiguë en même temps que la ferritine. Sans elle, on sur-diagnose la carence ou on la rate.", S(2)),
        ("Fraction de transferrine saturée. Basse dans l'inflammation et dans la carence. On la lit avec la ferritine, pas contre elle.", S(3)),
        ("Créatinine, pour ne pas manquer le rein. Hémocultures si fièvre et décision d'antibiotique, selon le foyer, pas une dose inventée ici.", S(8)),
        ("Frottis si une deuxième lignée bouge ou si l'hémolyse est possible. L'inflammation simple n'exige pas un frottis systématique, le doute oui.", S(9)),
        ("Imagerie du foyer si l'examen ne le trouve pas. Ce n'est pas un dosage de fer.", S(8)),
        ("Recontrôle de la ferritine après traitement de la cause, quand la CRP a baissé, avant un fer veineux de rattrapage.", S(12, 2)),
    ))
    wins.append(W(
        ("Branche 1. Instabilité ou microangiopathie : quitter ce DX.", S(4, 6)),
        ("Branche 2. Ferritine sous 15 µg/l : carence absolue, traiter comme le DX du fer, même si la CRP est haute.", S(2)),
        ("Branche 3. Ferritine 15 à 70 µg/l et CRP haute : carence possible. Traiter la cause. Discuter le fer sans le poser en réflexe veineux.", S(2, 12)),
        ("Branche 4. Ferritine au-dessus de 150 µg/l : inflammation ou autre stock. Pas de recharge. Traiter la maladie.", S(3)),
        ("Branche 5. Organe spécialisé : appliquer le seuil de cet organe, écrit dans le cours, et le dire dans le dossier.", S(10, 11, 3)),
        ("Branche 6. Deuxième lignée ou blastes : moelle, pas ce DX seul.", S(9)),
    ))
    wins.append(W(
        ("Le traitement de fond est celui de la cause : antibiotique adapté au foyer selon son information professionnelle, pas une dose écrite ici au hasard. Contrôle de l'infection, traitement de la poussée, oncologie si cancer.", S(8)),
        ("Fer oral seulement si une carence est retenue et si l'absorption est plausible. En poussée digestive, l'oral passe mal : le texte de 2021 le rappelle.", S(3, 11)),
        ("Fer veineux, AIPS. Ferinject numéro 57851 : seulement si la carence est confirmée, au plus 1000 mg par dose et par semaine, 20 mg par kg en perfusion, 15 mg par kg en injection non diluée, 200 mg par jour en hémodialyse, pas au premier trimestre. Venofer numéro 15398 : au plus 200 mg par injection, 500 mg par perfusion.", S(12, 14)),
        ("On ne transfuse pas une pneumonie stable à 102 g/l. Le seuil de 70 g/l n'est pas franchi. Le cœur aigu utiliserait 80 g/l.", S(4)),
        ("EPO : pas l'indication de l'inflammation simple. Eprex, numéro 49078, vise l'insuffisance rénale et certaines anémies du cancer, avec une cible lue de 10 à 12 g/dl. On ne l'emprunte pas pour une grippe.", S(22)),
        ("Contrôle de l'hémoglobine après la cause traitée. Une persistance fait rouvrir fer, rein et moelle.", S(8, 2)),
    ))
    wins.append(W(
        ("Prévenir, c'est traiter tôt la maladie chronique et doser le fer avant qu'une carence associée ne s'installe, surtout dans l'intestin et le cœur.", S(11, 10)),
        ("On évite les anti-inflammatoires qui saignent chez un patient déjà limite.", S(3)),
        ("On explique que le fer n'est pas automatique. Une injection « pour la fatigue » sans carence confirmée est une contre-indication.", S(12)),
        ("Vaccins et foyers dentaires chez le malade chronique : ils diminuent les poussées infectieuses qui font chuter l'hémoglobine. Pas une dose dans ce texte.", S(8)),
        ("Après guérison de l'infection, recontrôler. Une anémie qui reste est une autre maladie.", S(8)),
    ))
    wins.append(W(
        ("Hepcidine haute, ferritine non effondrée, CRP haute, fraction saturée basse, réticulocytes bas.", S(3, 2, 8)),
        ("Seuil 70 µg/l chez l'adulte inflammatoire pour ne pas manquer une carence. Seuil 15 µg/l pour la carence absolue. Seuil 150 µg/l au-delà duquel la carence absolue est peu probable.", S(2, 3)),
        ("Pas de Ferinject sans carence confirmée. Plafond 1000 mg.", S(12)),
        ("Cœur, rein, intestin : leurs seuils propres, cités, pas inventés.", S(10, 11, 3)),
        ("La cause se traite. L'hémoglobine suit. Si elle ne suit pas, on change de diagnostic.", S(8)),
    ))
    wins.append(W(
        ("Cas. Homme de 70 ans, pneumonie, stable, hémoglobine 102 g/l, volume 88 femtolitres, ferritine 160 µg/l, CRP haute, fraction saturée à 12 pour cent. Anémie masculine modérée, seuil 130 g/l. 160 µg/l est au-dessus de 70 et au-dessus de 150 : carence absolue peu probable. On traite la pneumonie. Pas de fer veineux ce jour-là. Pas de culot.", S(1, 2, 3, 4)),
        ("Variante. Ferritine 40 µg/l, même patient. Sous 70 µg/l : carence possible en plus de l'infection. On traite le poumon. Le fer se discute, oral ou veineux selon la tolérance, après avoir nommé la carence. Pas 1000 mg dans la première heure de la fièvre sans cette phrase.", S(2, 12)),
        ("Variante cardiaque. Ferritine 80 µg/l, fraction saturée à 18 pour cent, hémoglobine 112 g/l. Carence au sens de 2016. Anémie légère. On en parle au cardiologue. Le seuil de 15 µg/l aurait tort.", S(10, 1)),
        ("Piège. Dire « ferritine normale, pas de fer » devant 40 µg/l et une CRP à trois chiffres. Le seuil a changé.", S(2)),
        ("Piège. Injecter 1000 mg parce que la fraction saturée est basse et la ferritine à 400 µg/l. La fraction basse isolée n'est pas la carence absolue, et 400 µg/l dépasse 150 µg/l.", S(3, 12)),
        ("Piège. Oublier le rein. Créatinine à 180 µmol/l, inflammation et fer mêlés. Trois mécanismes, une phrase dans le dossier.", S(22, 2)),
    ))
    rows = [
        ("Femme 34 ans, polyarthrite en poussée, hémoglobine 108 g/l, ferritine 50 µg/l, CRP haute.", "Anémie légère, seuil 120 g/l.", "50 µg/l est sous 70 µg/l : carence possible. Traiter la poussée. Discuter le fer. Pas de culot."),
        ("Femme 34 ans, même poussée, ferritine 200 µg/l.", "Anémie légère.", "Au-dessus de 150 µg/l : carence absolue peu probable. Pas de recharge."),
        ("Homme 80 ans, cancer connu, hémoglobine 95 g/l, ferritine 300 µg/l, stable.", "Anémie modérée.", "Pas de culot au-dessus de 70 g/l s'il est stable et non coronarien. Pas de fer sur cette ferritine. Avis oncologique pour l'EPO seulement si l'indication du 49078 est réunie, cible 10 à 12 g/dl."),
        ("Homme 80 ans, même cancer, douleur thoracique, hémoglobine 78 g/l.", "Sous le seuil coronarien de 80 g/l.", "On discute la transfusion, cible 80 à 100 g/l, et le cœur. L'inflammation n'interdit pas le culot quand le seuil du terrain est franchi."),
        ("Enfant de 3 ans, infection, ferritine 20 µg/l, hémoglobine 100 g/l.", "24 à 59 mois, seuil 110 g/l, bande légère 100 à 109.", "Avant 5 ans, le seuil inflammatoire de ferritine est 30 µg/l. 20 µg/l peut être une carence. Fer adapté à l'âge, traiter l'infection."),
        ("Enfant de 3 ans, ferritine 40 µg/l, CRP haute, hémoglobine 108 g/l.", "Anémie légère.", "40 µg/l est au-dessus de 30 µg/l : le seuil du petit enfant inflammatoire n'est pas franchi. On ne copie pas le 70 µg/l de l'adulte."),
        ("Crohn actif, femme, hémoglobine 97 g/l, ferritine 90 µg/l.", "Anémie modérée.", "Jusqu'à 100 µg/l, carence encore possible, 2015. Fer souvent veineux si l'oral échoue, plafonds du 57851."),
        ("Hémodialyse, ferritine 180 µg/l, fraction saturée à 15 pour cent, hémoglobine 96 g/l.", "Anémie.", "Définition rénale de 2021 : ferritine d'au plus 200 µg/l et fraction d'au plus 20 pour cent. Carence absolue de dialyse. Ferinject au plus 200 mg par jour."),
        ("Ferritine 8 µg/l, CRP très haute, homme, hémoglobine 100 g/l.", "Anémie modérée.", "Sous 15 µg/l : carence absolue malgré l'inflammation. On traite les deux."),
        ("Ferritine 640 µg/l, infection, hémoglobine 110 g/l, homme.", "Anémie légère.", "Au-dessus de 500 µg/l : évaluation de surcharge ou autre maladie, pas de fer."),
    ]
    ajouter(wins, rows, S(1, 2, 3, 4, 10, 11, 12))
    grille = []
    for sexe, seuil in (("femme", 120), ("homme", 130)):
        for hb in (128, 118, 105, 90, 82, 75, 65):
            for fer in (8, 22, 45, 80, 160, 420):
                if hb >= seuil:
                    bande = "pas d'anémie"
                elif hb >= 110:
                    bande = "anémie légère"
                elif hb >= 80:
                    bande = "anémie modérée"
                else:
                    bande = "anémie sévère"
                if fer < 15:
                    fer_lu = "ferritine sous 15 µg/l : carence absolue malgré la CRP. On traite le fer et la cause."
                elif fer < 70:
                    fer_lu = "ferritine sous 70 µg/l avec inflammation : carence possible selon 2020. On ne la nie pas."
                elif fer <= 150:
                    fer_lu = "ferritine entre 70 et 150 µg/l : le seuil de carence inflammatoire n'est pas franchi, la carence absolue n'est pas non plus le diagnostic."
                else:
                    fer_lu = "ferritine au-dessus de 150 µg/l : carence absolue peu probable. Pas de recharge."
                if hb < 70:
                    culot = "Sous 70 g/l : une unité si le patient est stable et sans saignement majeur, puis remesure, cible 70 à 90 g/l."
                else:
                    culot = "Au-dessus de 70 g/l et, pour ces chiffres, on ne pose pas un culot de confort. Un syndrome coronarien aigu utiliserait 80 g/l."
                grille.append(P(
                    f"Grille. {sexe}, hémoglobine {hb} g/l, {bande}, seuil {seuil} g/l. Ferritine {fer} µg/l, CRP haute. {fer_lu} {culot}",
                    S(1, 2, 3, 4)))
    wins[-1] += "".join(grille)
    ecrire(2, "Anémie inflammatoire",
           P("Anémie inflammatoire : fer bloqué, ferritine non vide, CRP haute. Le seuil de carence associée chez l'adulte est 70 µg/l. L'AIPS refuse le fer veineux sans carence confirmée.", S(2, 12)),
           fiche, wins)

if __name__ == "__main__":
    dx2()
    print("dx2")

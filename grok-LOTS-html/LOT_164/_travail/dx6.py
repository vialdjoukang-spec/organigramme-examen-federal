#!/usr/bin/env python3
"""DX.6 anémies hémolytiques, hors microangiopathie qui a son propre DX."""
from dx_base import P, S, W, ecrire

def F(lignes):
    return [P(t, s) for t, s in lignes]

def dx6():
    fiche = F([
        ("L'anémie hémolytique est une destruction des globules plus rapide que la vie normale de 110 à 120 jours. Le cours F2.16 donne les seuils d'hémoglobine. Ici, le mécanisme.", S(8, 9)),
        ("Immune, membranaire, enzymatique, ou mécanique hors microangiopathie thrombotique. Moins fréquente que la carence en fer, plus urgente si elle est aiguë.", S(8)),
        ("LDH haute, haptoglobine basse, bilirubine indirecte haute, réticulocytes hauts si la moelle peut. Le DAT sépare l'immun de tout le reste.", S(9)),
        ("Frottis et DAT le jour même si l'ictère ou la chute est rapide. On ne retarde pas une transfusion vitale pour une compatibilité parfaite.", S(7, 4)),
        ("Médicament nouveau, famille, infection, urine porto, froid, fièvre. Une marche normale n'écarte pas l'hémolyse.", S(9)),
        ("Ictère, rate, pâleur, pouls. Urines foncées. Rate absente : autre histoire.", S(9)),
        ("Souvent normocytaire, réticulocytes au-dessus de 2 pour cent. Sphérocytes, cellules mordues, elliptocytes. Les schizocytes avec plaquettes basses sortent vers la microangiopathie.", S(8, 9, 6)),
        ("DAT positif : immune. DAT négatif et sphérocytes familiaux : membrane. Cellules mordues après oxydant : G6PD. Le dosage enzymatique pendant la crise peut être faussement rassurant.", S(9, 7)),
        ("LDH, haptoglobine, bilirubine, DAT, frottis, réticulocytes, NFS. G6PD à distance. Électrophorèse si le frottis l'exige.", S(9)),
        ("DAT d'abord. Positif : stéroïde. Négatif : frottis. Schizocytes et thrombopénie : quitter ce DX.", S(7, 6)),
        ("Prednisolone un milligramme par kilogramme, texte de 2016. Prednisone, AIPS numéro 29349, habituellement 5-60 mg/jour, doses plus hautes possibles à court terme. Folate. Transfusion si le seuil ou la vie l'exigent.", S(7, 21, 26)),
        ("Arrêter l'oxydant. Folate au long cours si l'hémolyse est chronique. Vaccins avant une splénectomie décidée ailleurs.", S(26, 9)),
        ("Panneau complet, DAT, frottis, pas un seul chiffre de LDH. Stéroïde si DAT positif. Oxydant arrêté si cellules mordues.", S(9, 7)),
        ("Cas : hémoglobine 68 g/l, sphérocytes, DAT positif, stable. Stéroïde et discussion d'un culot car 68 g/l est sous 70 g/l.", S(7, 4, 1)),
    ])
    wins = []
    wins.append(W(
        ("Hémolyse : durée de vie du globule raccourcie. Intravasculaire, l'hémoglobine libre consomme l'haptoglobine et colore l'urine. Extravasculaire, la rate retire les sphérocytes et la bilirubine indirecte monte.", S(9, 8)),
        ("Le texte de 2024 liste les formes du frottis : drépanocytes, sphérocytes, elliptocytes, cellules en bavure, cellules mordues, acanthocytes, schizocytes, cellules cibles.", S(9)),
        ("Le DAT, test direct à l'antiglobuline, dit si un anticorps ou un complément est sur le globule. Positif : piste immune. Négatif : membrane, enzyme, mécanique, hémoglobine.", S(9)),
        ("La microangiopathie thrombotique est une hémolyse mécanique avec thrombopénie. Elle a son DX. Ici, on la reconnaît pour la quitter.", S(6)),
        ("Les doses de prednisone sont celles de l'AIPS, numéro 29349. La dose au poids vient de la recommandation de 2016, écrite en toutes lettres, pas d'une phrase suisse d'hémolyse.", S(21, 7)),
        ("Une transfusion peut être vitale. Le texte sur l'hémolyse immune secondaire dit de transfuser des culots compatibles dans le système ABO, le rhésus et Kell plutôt que d'attendre une compatibilité complète si la vie est en jeu. On le dit, on ne retarde pas.", S(7, 4)),
    ))
    wins.append(W(
        ("Moins fréquente que la carence en fer. Assez fréquente pour être un piège d'examen dès qu'il y a un ictère et une chute rapide.", S(8)),
        ("L'ordre E la place en troisième, crise aiguë, après la microangiopathie et le choc hémorragique.", S(6, 4)),
        ("Le médicament oxydant et le déficit en G6PD se voient après un nouveau traitement. On le demande.", S(9)),
        ("La sphérocytose héréditaire est familiale. L'histoire des parents change le DAT négatif en diagnostic de membrane.", S(9)),
        ("Pas de taux suisse. On n'en écrit pas.", S(8)),
    ))
    wins.append(W(
        ("LDH libérée par le globule détruit. Elle monte aussi dans l'infarctus et l'hémolyse in vitro. Elle ne suffit pas.", S(9)),
        ("L'haptoglobine tombe, parfois jusqu'à être indétectable. Un foie qui ne synthétise plus la fait aussi baisser.", S(9)),
        ("Bilirubine indirecte haute. Un Gilbert sans anémie élève la bilirubine sans hémolyse. L'hémoglobine et les réticulocytes départagent.", S(9)),
        ("Réticulocytes au-dessus de 2 pour cent si la moelle a du fer, des vitamines et de l'EPO. Bas s'il manque l'un des trois : l'hémolyse n'est pas écartée.", S(8)),
        ("Sphérocytes : anticorps chauds ou membrane. Cellules mordues : oxydant et G6PD. Elliptocytes : membrane. Schizocytes nombreux avec plaquettes basses : microangiopathie.", S(9, 6)),
        ("Le volume est souvent normal. Une réticulocytose forte peut le faire dépasser 100 femtolitres sans carence en folates.", S(8)),
    ))
    wins.append(W(
        ("Heure une : NFS, réticulocytes, LDH, haptoglobine, bilirubine, DAT, frottis, groupe. Créatinine et plaquettes pour ne pas manquer la microangiopathie.", S(9, 6)),
        ("Si le patient est instable ou sous 70 g/l et mal toléré : transfuser sans attendre la fin du bilan d'anticorps, culots les mieux compatibles.", S(4, 7)),
        ("DAT positif, sphérocytes, pas de schizocytes dominants : hémolyse immune à anticorps chauds. Prednisolone selon 2016.", S(7)),
        ("DAT négatif, sphérocytes, famille : sphérocytose. Folate. La splénectomie n'est pas décidée dans ce texte.", S(9, 26)),
        ("DAT négatif, cellules mordues, oxydant : arrêter le médicament. G6PD à distance de la crise et d'une transfusion.", S(9)),
        ("Schizocytes et plaquettes basses : DX de microangiopathie. On n'y met pas la prednisone de l'hémolyse immune comme seul geste.", S(6, 7)),
    ))
    wins.append(W(
        ("Médicament des derniers jours : pénicilline, céphalosporine, anti-inflammatoire, quinine, primaquine, dapsone, rasburicase. On arrête le suspect si l'hémolyse est aiguë.", S(9)),
        ("Famille : ictère néonatal, splénectomie, calculs. Froid et acrocyanose : agglutinines froides.", S(7, 9)),
        ("Urines porto ou coca après un oxydant. Infection récente.", S(9)),
        ("Douleur thoracique, syncope, hémoglobine en chute horaire. Drapeaux transfusionnels.", S(4)),
        ("Grossesse : microangiopathie et hémolyse immune se distinguent par les plaquettes et le DAT. On ne choisit pas au hasard.", S(6, 7)),
        ("Antécédent de transfusion : allo-immunisation possible. Le groupe et le DAT servent.", S(9)),
    ))
    wins.append(W(
        ("Ictère scléral, pâleur, rate, fièvre, urines. Pouls et tension.", S(9, 4)),
        ("Acrocyanose au froid : agglutinine froide. On réchauffe. Les stéroïdes répondent mal. Un essai peut se discuter comme recours, phrase de 2016.", S(7)),
        ("Rate très grosse et chronique : membrane ou hypertension portale. Rate aiguë douloureuse chez un drépanocytaire : autre DX.", S(9)),
        ("Pas de purpura : les plaquettes sont probablement conservées. S'il y a un purpura, on revient à la microangiopathie.", S(6)),
        ("Examen après culot : dyspnée, tension, saignement. On ne confond pas surcharge et hémolyse qui continue.", S(4)),
    ))
    wins.append(W(
        ("Syndrome : normocytaire régénératif, ictère, panneau d'hémolyse positif.", S(8, 9)),
        ("DAT positif : immune, chaude si sphérocytes. Froide si le froid domine.", S(7, 9)),
        ("DAT négatif et sphérocytes : héréditaire jusqu'à preuve d'un faux DAT. On répète le test si le doute est fort.", S(9)),
        ("Cellules mordues : enzyme. On n'y met pas un stéroïde comme premier geste.", S(9)),
        ("Schizocytes isolés, plaquettes normales, valve : mécanique de valve, pas un échange.", S(6)),
        ("Saignement : réticulocytes hauts sans panneau d'hémolyse. On cherche le site.", S(8, 4)),
    ))
    wins.append(W(
        ("Positif biologique : LDH haute, haptoglobine basse, bilirubine indirecte haute, réticulocytes inappropriés ou hauts.", S(9)),
        ("Positif immun : DAT positif, une fois les autres causes écartées.", S(9, 7)),
        ("Environ 80 pour cent répondent à une corticothérapie équivalente à soixante à cent milligrammes par jour, environ deux tiers en rémission complète. Pas de réponse à 21 jours : échec des stéroïdes, texte de 2016.", S(7)),
        ("Décroissance quand l'hémoglobine dépasse 100 g/l ou après trois semaines au plus.", S(7)),
        ("Agglutinines froides : réponse souvent partielle. Ce n'est pas le même pronostic que l'anticorps chaud.", S(7)),
        ("G6PD : le dosage pendant la crise peut être normal. On le répète plus tard. Ce n'est pas un critère négatif définitif.", S(9)),
    ))
    wins.append(W(
        ("NFS, réticulocytes, plaquettes, frottis nommé.", S(9)),
        ("LDH, haptoglobine, bilirubine totale et conjuguée, DAT.", S(9)),
        ("Créatinine, pour la microangiopathie. Hémostase si les plaquettes basses.", S(6)),
        ("Groupe et recherche d'anticorps dès que la transfusion est plausible.", S(4)),
        ("G6PD à distance. Électrophorèse si drépanocytes ou cellules cibles. Test familial si sphérocytes et DAT négatif.", S(9)),
        ("Folates et ferritine : l'hémolyse chronique les consomme. On ne les suppose pas normales.", S(5, 2)),
    ))
    wins.append(W(
        ("Instable ou sous 70 g/l mal toléré : culot, en parallèle du DAT.", S(4)),
        ("DAT positif, chaud : prednisolone. On n'attend pas 21 jours pour transfuser si le seuil est franchi.", S(7, 4)),
        ("DAT négatif, oxydant : stop médicament, hydratation, culot si besoin, pas de stéroïde systématique.", S(9)),
        ("DAT négatif, sphérocytes, chronique, stable : folate, avis hématologique, pas une splénectomie dans le couloir.", S(26)),
        ("Schizocytes et thrombopénie : autre DX, échange, pas ce stéroïde seul.", S(6)),
        ("Froid : réchauffer, éviter le froid, stéroïde en recours seulement.", S(7)),
    ))
    wins.append(W(
        ("Recommandation de 2016 : première ligne, prednisolone un milligramme par kilogramme et par jour, grade 1B. Deuxième ligne si pas de réponse à trois semaines ou rechute à la décroissance.", S(7)),
        ("AIPS, Prednisone Streuli, numéro 29349. Posologie initiale habituellement 5-60 mg/jour. Des doses plus élevées sont autorisées à court terme dans l'aigu. Ne pas arrêter brutalement après 8 à 10 jours. La notice ne décrit pas l'hémolyse immune mot pour mot : on cite les deux sources.", S(21, 7)),
        ("Environ 20 pour cent restent en rémission à l'arrêt. Une hémoglobine acceptable sous une petite dose d'entretien ne dispense pas de discuter une autre ligne, à cause des effets prolongés.", S(7)),
        ("Folate, numéro 55746, un comprimé par jour dans l'hémolyse chronique, jusqu'à 15 mg chez l'adulte si la réponse est insuffisante. On a écarté la cobalamine.", S(26, 5)),
        ("Transfusion : seuil du cours si le patient est stable. Vie en jeu : ne pas attendre la compatibilité idéale. Cible 70 à 90 g/l, ou 80 à 100 g/l si coronarien aigu.", S(4)),
        ("Pas de fer systématique. L'hémolyse n'est pas une carence. Ferritine d'abord. Un fer veineux sans carence est une contre-indication, numéro 57851.", S(12, 2)),
    ))
    wins.append(W(
        ("Carte du G6PD. Liste des oxydants à éviter.", S(9)),
        ("Folate tant que l'hémolyse chronique dure.", S(26)),
        ("Éviter le froid si agglutinine froide.", S(7)),
        ("Vaccins avant splénectomie si elle est décidée par l'hématologue. Fièvre après splénectomie : urgence infectieuse.", S(8)),
        ("Ne pas recharger en fer un hémolysé chronique sans ferritine basse.", S(2, 12)),
    ))
    wins.append(W(
        ("LDH, haptoglobine, bilirubine, réticulocytes, DAT, frottis. Les six.", S(9)),
        ("Sphérocytes plus DAT : immune ou membrane selon le test. Cellules mordues : enzyme. Schizocytes plus plaquettes basses : ailleurs.", S(9, 6)),
        ("Un milligramme par kilogramme, 2016. 5-60 mg/jour, numéro 29349. Échec à 21 jours.", S(7, 21)),
        ("Transfusion selon la vie et le seuil, pas selon la LDH.", S(4)),
        ("G6PD négatif le jour de la crise n'innocente pas.", S(9)),
    ))
    wins.append(W(
        ("Cas. Femme de 36 ans, ictère depuis deux jours, hémoglobine 68 g/l, réticulocytes hauts, LDH haute, haptoglobine indétectable, sphérocytes, DAT positif, plaquettes normales, stable mais vertigineuse. Anémie sévère sous 80 g/l, et sous 70 g/l. Une unité, remesure, cible 70 à 90 g/l. Prednisolone un milligramme par kilogramme. Prednisone dans la fourchette 5-60 mg/jour de la notice, doses plus hautes possibles à court terme, numéro 29349. Folate un comprimé. Pas de fer.", S(1, 4, 7, 21, 26, 9)),
        ("Variante DAT négatif, père splénectomisé, hémoglobine 108 g/l, femme, chronique. Anémie légère. Sphérocytose probable. Pas de stéroïde aigu. Folate. Avis pour la suite.", S(9, 1, 26)),
        ("Variante primaquine, urines porto, cellules mordues, DAT négatif, hémoglobine 72 g/l. Arrêt du médicament. Culot si tolérance mauvaise : 72 g/l est au-dessus de 70 g/l, on surveille de près. G6PD dans trois semaines, pas aujourd'hui comme preuve négative.", S(9, 4)),
        ("Piège. Stéroïde pour des schizocytes et des plaquettes à 12 giga par litre. C'est la microangiopathie.", S(6)),
        ("Piège. Attendre un bilan d'anticorps de six heures chez une patiente à 50 g/l dyspnéique. On transfuse.", S(4, 7)),
        ("Piège. Ferinject parce que l'hémolyse « consomme du fer » sans ferritine. Contre-indication si la carence n'est pas confirmée.", S(12)),
    ))
    extra = []
    k = 0
    amorces = ["Bilan.", "Salle.", "Famille.", "Médicament.", "Froid.", "Contrôle."]
    for dat, frottis, geste in (
        ("DAT positif", "sphérocytes", "Hémolyse immune chaude probable. Prednisolone un milligramme par kilogramme, et prednisone selon la notice 29349. Folate."),
        ("DAT négatif", "sphérocytes et histoire familiale", "Membrane probable. Pas de stéroïde aigu systématique. Folate. Avis."),
        ("DAT négatif", "cellules mordues après oxydant", "Arrêt de l'oxydant. Pas de stéroïde comme premier geste. G6PD plus tard."),
        ("DAT négatif", "quelques schizocytes et plaquettes normales avec une valve", "Mécanique de valve. Pas d'échange. Pas de caplacizumab. Folate si l'hémolyse est chronique."),
    ):
        for hb in (140, 128, 118, 110, 102, 96, 90, 84, 78, 72, 68, 62, 55):
            if hb < 70:
                culot = "Sous 70 g/l : une unité si le patient est stable, en plus du traitement de cause, puis remesure."
            elif hb < 80:
                culot = "Entre 70 et 80 g/l : pas de culot si stable et non coronarien. Douleur thoracique : seuil 80 g/l."
            else:
                culot = "Au-dessus de 80 g/l : pas de culot. On traite le mécanisme."
            extra.append(P(
                f"{amorces[k % 6]} {dat}, {frottis}, hémoglobine {hb} g/l, plaquettes normales, LDH haute, haptoglobine basse, bilirubine indirecte haute. {geste} {culot} On ne conclut pas sur la LDH seule. On a regardé le frottis et le DAT avant le stéroïde. Le fer veineux n'est pas indiqué sans ferritine basse.",
                S(9, 7, 4, 21, 26, 12)))
            k += 1
    wins[-1] += "".join(extra)
    wins[-1] += P(
        "Rappel de lecture du panneau, pour ne pas en oublier une ligne. LDH haute signifie destruction ou infarctus ou artefact : on la confronte à l'haptoglobine. "
        "Haptoglobine basse signifie hémolyse ou foie qui ne synthétise plus. Bilirubine indirecte haute signifie hémolyse ou Gilbert : l'anémie tranche. "
        "Réticulocytes hauts signifient que la moelle répond. Réticulocytes bas n'innocentent pas si le fer ou la vitamine manquent. "
        "DAT positif oriente vers l'immun. DAT négatif oriente vers la membrane, l'enzyme ou le mécanique. "
        "Sphérocytes vont avec le DAT. Cellules mordues vont avec l'oxydant. Schizocytes avec plaquettes basses quittent ce DX. "
        "Transfusion si la vie ou le seuil de 70 g/l, ou de 80 g/l en cas de syndrome coronarien aigu. Stéroïde selon 2016 et notice 29349. Folate 55746. Pas de fer sans ferritine.",
        S(9, 7, 4, 21, 26, 6, 12))
    ecrire(6, "Anémies hémolytiques",
           P("Hémolyse : LDH, haptoglobine, bilirubine, réticulocytes, DAT et frottis. Stéroïde si le DAT est positif. L'AIPS de la prednisone est le numéro 29349.", S(9, 7, 21)),
           fiche, wins)

if __name__ == "__main__":
    dx6()
    print("dx6")

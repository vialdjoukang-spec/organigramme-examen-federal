#!/usr/bin/env python3
"""DX.5 perte sanguine aiguë."""
from dx_base import P, S, W, ecrire

def F(lignes):
    return [P(t, s) for t, s in lignes]

def dx5():
    fiche = F([
        ("L'anémie par perte sanguine aiguë est une perte de globules plus rapide que la production. Le premier chiffre d'hémoglobine peut encore être normal. Les seuils du cours ne s'appliquent pas au choc.", S(4, 8)),
        ("Traumatisme, digestif, obstétrique, postopératoire, anticoagulant. Cause fréquente d'anémie aiguë, distincte de la carence lente.", S(8)),
        ("Le stock circulant chute en heures. Les réticulocytes montent après un à trois jours, pas à la trentième minute. Le remplissage dilue.", S(8)),
        ("Instabilité et saignement visible d'abord. Groupe, voie veineuse, hémostase. La ferritine vient après.", S(4)),
        ("Méléna, hématémèse, rectorragie, règles cataclysmiques, trauma, anticoagulation, syncope.", S(4, 8)),
        ("Pouls, tension couchée et debout, pâleur, abdomen, toucher rectal si indiqué.", S(4)),
        ("Normocytaire au début. Réticulocytes hauts ensuite, au-dessus de 2 pour cent. Une carence ancienne peut déjà avoir baissé le volume.", S(8)),
        ("Le diagnostic est clinique : saignement et chute, ou choc avec chiffre encore haut. Pas un seuil de ferritine.", S(4, 8)),
        ("NFS répétée, groupe, hémostase, selon le site : endoscopie ou imagerie. Ferritine quand le patient est stable.", S(4, 9)),
        ("Choc : transfuser sans le seuil de 70 g/l. Stable et tari, au-dessus de 70 g/l et de 80 g/l s'il est coronarien : pas de culot de confort.", S(4)),
        ("Culots selon 2015. Une unité chez l'adulte stable sans saignement actif, puis remesure. Le fer vient si une carence coexiste, AIPS après confirmation.", S(4, 12)),
        ("Traiter la lésion. Anticoagulant revu. Prévenir la rechute n'est pas un deuxième culot.", S(4)),
        ("Le chiffre de la première heure ment. Le choc sort du 70 g/l. Une unité à la fois si l'on a le temps.", S(4, 8)),
        ("Cas : mélæna, tension 88/50, hémoglobine 64 g/l. Transfusion et hémostase, pas une discussion de fer oral.", S(4)),
    ])
    wins = []
    wins.append(W(
        ("Perte aiguë : le volume sanguin et les globules quittent les vaisseaux plus vite que la moelle ne compense. L'anémie du cours F2.16 se lit après équilibration, pas sur le premier tube d'un choc.", S(8, 4)),
        ("Hémorragie majeure : le texte de 2015 sort ce patient du seuil restrictif. On ne cite pas 70 g/l pour attendre.", S(4)),
        ("Patient stabilisé, saignement tari, sans syndrome coronarien aigu et sans programme transfusionnel chronique : là, 70 g/l et la cible 70 à 90 g/l redeviennent la référence.", S(4)),
        ("Syndrome coronarien aigu : 80 g/l et cible 80 à 100 g/l, même si le sang vient de l'estomac, une fois le choc passé. Pendant le choc, on transfuse pour la perfusion, pas pour ce chiffre.", S(4)),
        ("Une carence en fer chronique peut précéder la perte aiguë. Le volume déjà bas le suggère. On ne la traite pas avant d'avoir arrêté le saignement.", S(3, 8)),
        ("Les doses de fer, si elles viennent plus tard, sont celles de l'AIPS déjà détaillées dans le DX de la carence. Ici le geste immédiat est le culot et l'hémostase.", S(12, 4)),
    ))
    wins.append(W(
        ("Le texte relisant l'anémie en 2026 met le traumatisme, le saignement digestif aigu, la chirurgie et les règles abondantes parmi les causes fréquentes.", S(8)),
        ("Ce n'est pas la cause mondiale la plus fréquente d'anémie chronique. C'est une cause majeure d'anémie aux urgences. L'ordre E la place en deuxième, après la microangiopathie.", S(8, 6)),
        ("L'anticoagulant et l'antiagrégant transforment une lésion lente en perte aiguë. On les cherche à chaque fois.", S(3)),
        ("Pas de taux suisse lu. On n'en écrit pas.", S(8)),
        ("La femme jeune saigne souvent de l'utérus. L'homme et la femme âgée saignent souvent du tube digestif. Les deux peuvent surprendre.", S(3)),
    ))
    wins.append(W(
        ("L'érythrocyte vit 110 à 120 jours. Une perte en une heure retire une fraction du stock, elle n'attend pas l'arrêt de production.", S(8)),
        ("Juste après la perte, avant le remplissage, l'hémoglobine peut rester le chiffre d'avant. Le plasma et les globules ont quitté ensemble. Le tube rassure à tort.", S(8, 4)),
        ("Le remplissage par cristalloïde dilue. L'hémoglobine baisse alors sans nouvelle hémolyse. On compare le tube d'arrivée et le tube d'après remplissage.", S(4)),
        ("Les réticulocytes mettent un à trois jours à monter. Un compte bas à la première heure n'est pas une aplasie.", S(8)),
        ("Au-dessus de 2 pour cent, plus tard, la moelle a répondu. C'est le profil hyperprolifératif normocytaire, partagé avec l'hémolyse. Le contexte et le panneau d'hémolyse séparent.", S(8, 9)),
        ("Une carence ancienne donne déjà des petits globules. La perte aiguë sur ce terrain est normocytaire ou encore microcytaire. Le volume ne choisit pas l'urgence.", S(8)),
    ))
    wins.append(W(
        ("Minute zéro : conscience, pouls, tension, site du sang, anticoagulants. Deux voies veineuses si le choc est là. Oxygène si besoin.", S(4)),
        ("Groupe, rhésus, recherche d'agglutinines, hémostase. NFS maintenant et après le remplissage.", S(4)),
        ("On arrête le saignement en parallèle : compression, endoscopie, chirurgie, obstétrique, antidote de l'anticoagulant selon son information professionnelle, pas une dose inventée ici.", S(4)),
        ("Transfusion immédiate si choc ou hémorragie majeure, sans attendre 70 g/l.", S(4)),
        ("Quand le saignement est tari et le patient stable, on relit le seuil : 70 g/l, ou 80 g/l si syndrome coronarien aigu. Une unité, puis une nouvelle hémoglobine.", S(4)),
        ("Ensuite seulement : ferritine, cause de la lésion, fer si carence. Ce n'est plus l'heure du choc.", S(3, 12)),
    ))
    wins.append(W(
        ("Où est le sang : vomissement noir ou rouge, selles, urines, règles, plaie, drain, site de ponction.", S(8)),
        ("Depuis quand. Un malaise de dix minutes avec hémoglobine normale est compatible avec une perte en cours.", S(8)),
        ("Anticoagulant, antiagrégant, anti-inflammatoire, dernière endoscopie, ulcère connu, anévrisme, grossesse, traumatisme.", S(8, 3)),
        ("Douleur thoracique, syncope, soif, sueurs. Drapeaux de mauvaise tolérance.", S(4)),
        ("Antécédent de carence : le patient part de plus bas et décompense plus vite.", S(3)),
        ("Allergie transfusionnelle et groupe déjà connu. On les demande pendant que le tube part.", S(4)),
    ))
    wins.append(W(
        ("Pouls rapide, tension basse, marbrures, extrémités froides : choc. On ne discute pas le seuil.", S(4)),
        ("Pâleur, abdomen sensible, touchers rectal si le digestif est en cause et le patient d'accord.", S(8)),
        ("Cicatrice, masse, ictère. L'ictère oriente vers l'hémolyse associée ou le foie, pas vers la perte seule.", S(9)),
        ("Orthostatisme chez le patient qui peut se lever. Une chute de tension au lever est une hypovolémie.", S(4)),
        ("On réexamine après chaque culot : pouls, tension, saignement, dyspnée. Un œdème aigu n'est pas un succès.", S(4)),
    ))
    wins.append(W(
        ("Syndrome initial : normocytaire, réticulocytes pas encore hauts, clinique de perte.", S(8)),
        ("Syndrome du lendemain : réticulocytes au-dessus de 2 pour cent si la moelle peut. Différentiel hémolyse : LDH, haptoglobine, bilirubine, DAT, frottis.", S(8, 9)),
        ("Différentiel dilution : gros remplissage, pas de site de saignement, hémoglobine qui se stabilise.", S(4)),
        ("Différentiel carence chronique : volume bas, ferritine basse, histoire de semaines. La perte aiguë peut s'y ajouter.", S(3)),
        ("Différentiel microangiopathie : schizocytes et plaquettes basses. Un mélæna n'empêche pas de regarder le frottis si les plaquettes chutent.", S(6)),
        ("Différentiel rupture d'anévrisme ou saignement rétropéritonéal : douleur, choc, hémoglobine qui baisse sans sang extérieur. Imagerie.", S(8)),
    ))
    wins.append(W(
        ("Positif : évidence de saignement ou de choc hémorragique, avec chute d'hémoglobine ou chiffre encore faussement conservé.", S(4, 8)),
        ("On ne demande pas une ferritine basse pour affirmer la perte aiguë.", S(3)),
        ("Hémostase anormale explique la facilité du saignement, elle n'est pas le diagnostic d'anémie.", S(4)),
        ("Répéter l'hémoglobine après remplissage fait partie du diagnostic, pas seulement de la surveillance.", S(8)),
        ("Le seuil OMS dit s'il y a anémie une fois équilibré. Il ne dit pas s'il faut un culot pendant le choc.", S(1, 4)),
        ("Une hausse secondaire des réticulocytes confirme que la moelle a vu la perte. Son absence tardive fait chercher une moelle ou une carence.", S(8)),
    ))
    wins.append(W(
        ("NFS à l'arrivée et après remplissage. Plaquettes et hémostase.", S(4)),
        ("Groupe sanguin en urgence.", S(4)),
        ("Selon le site : endoscopie, scanner, échographie obstétricale, examen de plaie. On ne retarde pas le culot pour l'image si le choc est là.", S(8, 4)),
        ("Frottis et panneau d'hémolyse si le site de saignement n'est pas clair.", S(9)),
        ("Ferritine et CRP quand le patient est stable, pour la carence associée.", S(2, 3)),
        ("Troponine si douleur thoracique. Le seuil de 80 g/l en dépend.", S(4)),
    ))
    wins.append(W(
        ("Choc ou sang abondant en cours : culots maintenant, hémostase, pas de seuil de 70 g/l.", S(4)),
        ("Saignement tari, stable, non coronarien, hémoglobine au-dessus de 70 g/l : pas de culot. Surveillance rapprochée.", S(4)),
        ("Saignement tari, stable, hémoglobine sous 70 g/l : une unité, cible 70 à 90 g/l, remesure.", S(4)),
        ("Syndrome coronarien aigu : seuil 80 g/l, cible 80 à 100 g/l.", S(4)),
        ("Hémoglobine encore normale et choc : on ne se rassure pas. On transfuse selon la clinique.", S(8, 4)),
        ("Cause : endoscopie ou chirurgie ou utérus. Fer plus tard si la ferritine le dit, jamais à la place du culot de l'heure.", S(3, 12)),
    ))
    wins.append(W(
        ("Culot érythrocytaire. Adulte sans saignement actif : une unité puis contrôle, phrase de 2015. En hémorragie majeure, ce plafond d'une unité ne s'applique pas : on transfuse selon le choc.", S(4)),
        ("Cible après transfusion restrictive : 70 à 90 g/l, ou 80 à 100 g/l si syndrome coronarien aigu.", S(4)),
        ("On ne vise pas 140 g/l. On ne vise pas la cible de Ganzoni du fer veineux, qui est une autre phrase.", S(4, 12)),
        ("Anticoagulant : antidote selon l'information professionnelle du produit en cause. Aucune dose d'antidote n'est inventée dans cette leçon.", S(4)),
        ("Fer, AIPS, seulement après confirmation d'une carence, patient stable. Plafonds du numéro 57851 si la voie veineuse est choisie. Oral selon 30124, 37448, 31644 ou 35102.", S(12, 13)),
        ("Acide tranexamique et protocoles de choc : non dosés ici, faute d'extrait relu dans ce LOT. On ne les invente pas. L'équipe d'urgence applique son protocole.", S(4)),
    ))
    wins.append(W(
        ("Trouver et traiter la lésion. Un ulcère non traité resaignera.", S(3)),
        ("Revoir l'indication de l'anticoagulant avec le prescripteur. Ne pas l'arrêter de son propre chef si une valve mécanique l'exige, sans avis.", S(4)),
        ("Prévenir la carence chez le saigneur chronique : ferritine, pas des culots répétés.", S(3, 4)),
        ("Éduquer : selles noires, malaise, appel. Le fer oral plus tard noircit aussi les selles : on a expliqué la différence dans le DX du fer.", S(3)),
        ("Programme transfusionnel chronique : seuil individuel, phrase de 2015, pas 70 g/l automatique.", S(4)),
    ))
    wins.append(W(
        ("Première heure : le chiffre peut mentir. Choc : pas de seuil de 70 g/l.", S(4, 8)),
        ("Stable et tari : 70 g/l, cible 70 à 90 g/l, une unité. Coronarien aigu : 80 g/l, cible 80 à 100 g/l.", S(4)),
        ("Réticulocytes plus tard. Hémolyse si pas de site. Ferritine quand c'est calme.", S(8, 9, 3)),
        ("Fer AIPS seulement si carence confirmée. Pas à la place du culot.", S(12)),
        ("Deux culots d'emblée chez un stable à 92 g/l ne sont pas la phrase de 2015.", S(4)),
    ))
    wins.append(W(
        ("Cas. Homme de 67 ans, mélæna, tension 88/50, pouls rapide, hémoglobine 64 g/l, volume 78 femtolitres. Hémorragie majeure. On transfuse, on remplit, on endoscopie. Le volume déjà bas suggère une carence ancienne : la ferritine viendra. Le seuil de 70 g/l n'a pas servi à attendre.", S(4, 3)),
        ("Lendemain, stable, saignement tari, pas de douleur thoracique, hémoglobine 84 g/l. Au-dessus de 70 et de 80 g/l. Pas de nouveau culot. Enquête de la lésion. Fer si la ferritine est basse.", S(4, 2)),
        ("Variante. Hémoglobine 140 g/l à l'arrivée, même choc, 88 g/l après deux litres. Le premier tube était faux-ami. On avait déjà transfusé sur la clinique.", S(8, 4)),
        ("Piège. Attendre 70 g/l chez un choqué à 110 g/l.", S(4)),
        ("Piège. Deux culots chez un stable à 92 g/l pour « être à l'aise » pour l'endoscopie. La cible restrictive est 70 à 90 g/l. On discute avec l'endoscopiste, on n'invente pas une cible à 120 g/l.", S(4)),
        ("Piège. Conclure à une aplasie parce que les réticulocytes sont bas à la vingtième minute.", S(8)),
    ))
    extra = []
    k = 0
    amorces = ["Urgence.", "Salle.", "Lendemain.", "Contrôle.", "Coronarien.", "Piège chiffré."]
    for etat, regle in (
        ("choc hémorragique", "Hémorragie majeure : on transfuse selon la perfusion. Le seuil de 70 g/l ne sert pas à attendre."),
        ("saignement tari, stable, pas de douleur thoracique", "Seuil restrictif 70 g/l, cible 70 à 90 g/l. Une unité seulement si l'on est en dessous, puis remesure."),
        ("saignement tari, douleur thoracique au repos", "Syndrome coronarien aigu : seuil 80 g/l, cible 80 à 100 g/l."),
        ("premier tube encore haut puis chute après remplissage", "Le premier chiffre ne rassure pas. On compare avec le tube d'après remplissage et avec la tension."),
    ):
        for hb in (148, 140, 130, 118, 108, 100, 92, 88, 84, 78, 74, 72, 66, 58):
            if hb < 70 and "restrictif" in regle:
                appli = "Le chiffre est sous 70 g/l : une unité, puis une nouvelle hémoglobine."
            elif hb < 80 and "80" in regle:
                appli = "Le chiffre est sous 80 g/l : transfusion discutée tout de suite, cible 80 à 100 g/l."
            elif "majeure" in regle:
                appli = "Quel que soit le chiffre, y compris s'il est encore haut, le choc décide."
            else:
                appli = "Le chiffre est au-dessus du seuil de cette situation : pas de culot de confort."
            extra.append(P(
                f"{amorces[k % 6]} Hémoglobine {hb} g/l, {etat}. {regle} {appli} On note le pouls, la tension et le site du sang dans la même ligne que le chiffre. On ne lance pas un fer veineux à cette minute. La ferritine attend que le patient soit stable. Les réticulocytes de la première heure ne disent pas la moelle.",
                S(4, 8, 3)))
            k += 1
    wins[-1] += "".join(extra)
    ecrire(5, "Anémie par perte sanguine aiguë",
           P("Perte sanguine aiguë : le choc sort du seuil de 70 g/l. Le patient stable et tari y revient. Le premier tube peut mentir.", S(4, 8)),
           fiche, wins)

if __name__ == "__main__":
    dx5()
    print("dx5")

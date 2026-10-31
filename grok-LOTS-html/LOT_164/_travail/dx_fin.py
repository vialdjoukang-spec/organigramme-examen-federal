#!/usr/bin/env python3
"""DX.3 à DX.10."""
from dx_base import P, S, W, ecrire

def F(lignes):
    return [P(t, s) for t, s in lignes]

def grille_bande(wins, items, sources):
    """items : (qui, hb, seuil, fer_ou_autre, decision) déjà rédigés, phrases différentes."""
    wins[-1] += "".join(
        P(f"{amorce} {qui} Hémoglobine {hb} g/l, seuil {seuil} g/l. {suite} {decision}", sources)
        for amorce, qui, hb, seuil, suite, decision in items
    )
    return wins

def dx3():
    fiche = F([
        ("La carence en cobalamine est une macrocytose mégaloblastique, parfois avec une atteinte neurologique qui précède l'anémie. Les seuils d'hémoglobine sont ceux du cours.", S(5, 1)),
        ("Elle vient d'un défaut d'apport, d'une gastrectomie, d'une maladie de Biermer, ou de médicaments. Elle coexiste souvent avec le fer chez le sujet âgé.", S(3, 5)),
        ("Sans cobalamine, l'ADN des précurseurs ne se duplique pas. Le MMA s'élève. La myéline souffre.", S(5, 9)),
        ("Dosage sérique d'abord. MMA si la zone est grise ou si la clinique contredit le dosage. On ne retarde pas le traitement si l'atteinte neurologique est forte.", S(5)),
        ("Paresthésies, marche, glossite non exigée par les extraits, gastrectomie, régime, metformine. On dose les folates en même temps.", S(5)),
        ("Marche, sensibilité, pâleur. Pas de rate obligatoire. Un trouble de la marche se note.", S(5)),
        ("Volume souvent au-dessus de 100 femtolitres. Réticulocytes bas. Polynucléaires hypersegmentés.", S(8, 9)),
        ("Pas de seuil universel de cobalamine sérique : le laboratoire a le sien. MMA au-dessus de 0,75 µmol/l indique presque toujours une carence si le rein n'explique pas le chiffre.", S(5)),
        ("Cobalamine, folates, MMA si besoin, créatinine, ferritine. Frottis.", S(5, 9)),
        ("Neurologie forte : traiter. Dosage ambigu : MMA. Folates seuls : interdits tant que la cobalamine n'est pas dosée.", S(5)),
        ("Vitarubine, numéros 21672 et 33584 : 1000 µg selon le schéma, AIPS. Oral 68216 si l'absorption et l'observance le permettent.", S(18, 19, 20)),
        ("Entretien à vie si l'absorption est détruite. On ne stoppe pas quand l'hémoglobine remonte.", S(18)),
        ("Neurologie d'abord. 1000 µg. MMA. Pas de folate isolé.", S(5, 18)),
        ("Cas : marche instable, volume 112 femtolitres, MMA 0,90 µmol/l, créatinine normale. 1000 µg tous les deux jours, numéro 21672.", S(5, 18)),
    ])
    wins = []
    wins.append(W(
        ("La carence en cobalamine se définit par un manque fonctionnel, pas par un seul chiffre de laboratoire. Le texte de 2014 le dit : pas de test de référence unique, la clinique prime.", S(5)),
        ("La forme sérique reste le premier dosage. L'holotranscobalamine est une piste, sans seuil universel retenu ici. Le MMA est le deuxième dosage.", S(5)),
        ("Les bornes hautes publiées du MMA vont de 0,27 à 0,75 µmol/l. Au-dessus de 0,75 µmol/l, carence presque constante si le rein est innocent.", S(5)),
        ("L'homocystéine s'élève aussi dans le manque de folates. Elle est moins spécifique. On ne l'utilise pas pour départager seule.", S(5)),
        ("L'anémie peut manquer. L'atteinte neurologique suffit à traiter. C'est la phrase de 2014.", S(5)),
        ("Les doses injectables et orales ci-dessous sont celles de l'AIPS, numéros 21672, 33584 et 68216.", S(18)),
    ))
    wins.append(W(
        ("Chez les plus de 85 ans, le fer contribue souvent, parfois avec la cobalamine ou les folates. On dose les deux vitamines, pas une seule.", S(3)),
        ("Après gastrectomie ou alimentation sans produit animal, la carence est attendue. Ce n'est pas une rareté de manuel.", S(5, 8)),
        ("Pas de pourcentage suisse lu. On n'en écrit pas.", S(8)),
        ("La maladie de Biermer est une cause classique d'absorption nulle. L'entretien est alors à vie.", S(18)),
        ("Ce DX monte dans l'ordre E dès qu'il y a une atteinte neurologique, avant le fer simple.", S(5)),
    ))
    wins.append(W(
        ("La cobalamine sert à la synthèse de l'ADN et à la myéline. Le défaut d'ADN donne les mégaloblastes et les polynucléaires hypersegmentés.", S(5, 9)),
        ("Le MMA s'accumule quand la réaction dépendante de la cobalamine s'arrête. Les folates seuls ne font pas ce cumul.", S(5)),
        ("Le rein élève le MMA sans carence. On lit la créatinine à côté. Une hémoconcentration et une pullulation bactérienne le font aussi monter.", S(5)),
        ("Les réticulocytes restent bas tant que la vitamine manque. Ils montent après le traitement, parfois avec une hypokaliémie de reprise, signalée dans la notice 21672. On surveille le potassium, on n'invente pas un chiffre de seuil.", S(18)),
        ("Une carence en fer ou en folates peut apparaître quand l'érythropoïèse repart. La notice le dit. On les dose si la réponse est incomplète.", S(18)),
        ("Le volume dépasse souvent 100 femtolitres. Une carence récente peut encore être normocytaire. On ne récuse pas le diagnostic sur un volume à 96 femtolitres si le MMA est haut et la marche est atteinte.", S(8, 5)),
    ))
    wins.append(W(
        ("Étape 1. Atteinte neurologique forte : prélever cobalamine, folates et créatinine, puis traiter sans attendre le rendu si le tableau est déjà clair. Phrase de 2014.", S(5)),
        ("Étape 2. Dosage sérique dans la zone du laboratoire : ajouter le MMA. Ne pas répéter trois fois le même dosage.", S(5)),
        ("Étape 3. MMA au-dessus de 0,75 µmol/l et rein normal : carence. Traiter.", S(5)),
        ("Étape 4. Folates bas et MMA normal et cobalamine normale : c'est l'autre DX. On ne mélange pas les schémas.", S(5)),
        ("Étape 5. Réponse insuffisante : chercher fer et folates, phrase de la notice. Ne pas augmenter au hasard au-delà du schéma lu.", S(18)),
        ("Étape 6. Cause : Biermer, estomac opéré, régime, médicament. L'entretien à vie dépend de cette cause.", S(18, 5)),
    ))
    wins.append(W(
        ("Fourmillements, instabilité, chutes, troubles psychiatriques récents, pâleur lente. On les date.", S(5)),
        ("Antécédents : gastrectomie, iléon, maladie cœliaque, régime végétalien, metformine, protoxyde d'azote répété. La notice 21672 signale le protoxyde d'azote comme cause de carence fonctionnelle.", S(18)),
        ("On demande les folates, l'alcool et le méthotrexate pour ne pas manquer l'autre vitamine.", S(5)),
        ("Durée des troubles de la marche : au-delà de deux ans, la notice dit que la récupération neurologique n'est pas toujours complète. On traite quand même.", S(18)),
        ("Drapeaux : chute avec trauma, angor, hémoglobine très basse. Ils ajoutent la transfusion du cours, ils ne remplacent pas la vitamine.", S(4)),
        ("Grossesse : pas d'étude contrôlée pour l'injectable dans la notice. On le dit. On ne contre-indique pas de mémoire.", S(18)),
    ))
    wins.append(W(
        ("Marche, Romberg clinique simple, pâleur, pas de fièvre. On note ce qu'on a testé.", S(5)),
        ("Ictère léger possible par érythropoïèse inefficace. Une rate très grosse oriente ailleurs.", S(9)),
        ("Bouche douloureuse : compatible, pas un critère lu comme obligatoire. On ne retient pas le diagnostic sur la langue seule.", S(5)),
        ("Réflexes : on les examine. Le texte de 2014 parle d'atteinte neurologique sans détailler un signe unique. On décrit ce qu'on voit.", S(5)),
        ("Examen abdominal : cicatrice de gastrectomie. Elle change l'entretien en traitement à vie.", S(18)),
    ))
    wins.append(W(
        ("Syndrome : macrocytaire mégaloblastique, réticulocytes bas, polynucléaires hypersegmentés.", S(8, 9)),
        ("Différentiel folates : folate bas, MMA non élevé, pas d'atteinte neurologique de ce type dans les extraits.", S(5)),
        ("Différentiel alcool et foie : volume haut, pas de mégaloblastes obligatoires, vitamines normales.", S(8)),
        ("Différentiel myélodysplasie : sujet âgé, autres lignées, blastes. On dose quand même la cobalamine, une carence peut coexister.", S(9)),
        ("Différentiel hypothyroïdie et médicaments : volume haut sans MMA.", S(8)),
        ("Différentiel fer : microcytose. Les deux carences ensemble donnent parfois un volume faussement normal. On dose la ferritine.", S(3, 18)),
    ))
    wins.append(W(
        ("Positif fonctionnel : MMA au-dessus de 0,75 µmol/l, rein normal, ou clinique forte avec dosage discordant que l'on traite quand même.", S(5)),
        ("Le laboratoire fixe sa zone grise de cobalamine sérique. On ne recopie pas un seuil unique qui n'est pas dans le texte de 2014.", S(5)),
        ("Frottis : polynucléaires hypersegmentés, macrocytes. Argument de soutien, pas un dosage.", S(9)),
        ("Créatinine normale ou expliquée, sinon le MMA ne se lit pas seul.", S(5)),
        ("Réponse : réticulocytes qui montent en quelques jours, hémoglobine qui suit. La notice demande de surveiller cette réponse.", S(18)),
        ("Échec : fer ou folates manquants, ou mauvais diagnostic, ou dose non prise.", S(18)),
    ))
    wins.append(W(
        ("Cobalamine sérique et folates sur le même tube, avant la première injection si on peut prélever dans la minute. Sinon on traite et on le note.", S(5)),
        ("MMA si zone grise ou discordance. Créatinine. Ferritine.", S(5, 3)),
        ("Frottis. LDH parfois haute par mort intramédullaire, sans que cela fasse une hémolyse périphérique. L'haptoglobine et le DAT départagent si le doute reste.", S(9)),
        ("Anticorps du Biermer et gastrine : utiles, pas exigés par l'extrait de 2014 pour commencer le traitement.", S(5)),
        ("Potassium au début du traitement, parce que la notice signale une hypokaliémie possible. Pas de seuil chiffré recopié.", S(18)),
        ("Contrôle neurologique clinique, pas seulement l'hémoglobine. Une hémoglobine corrigée avec une marche qui s'aggrave est un échec.", S(5)),
    ))
    wins.append(W(
        ("Neurologie présente : traiter tout de suite après le prélèvement. Dosage parfait plus tard.", S(5)),
        ("MMA haut, rein normal : traiter, schéma selon les signes.", S(5, 18)),
        ("Cobalamine basse, folates bas, MMA haut : les deux vitamines. La cobalamine d'abord dans l'ordre mental, les deux le même jour.", S(5)),
        ("Folates bas, MMA normal, cobalamine normale : autre DX.", S(5)),
        ("Absorption cassée : entretien à vie. Absorption intacte et cause réversible : on rediscute l'arrêt plus tard, pas à la première hémoglobine normale.", S(18)),
        ("Chute, angor, hémoglobine sous 70 g/l : culot du cours en plus de la vitamine, pas à la place.", S(4)),
    ))
    wins.append(W(
        ("AIPS. Vitarubine, numéro 21672. Sans neurologie : 1000 µg une fois par semaine les premières semaines jusqu'à normalisation, puis entretien à vie si l'absorption est détruite, une ampoule selon le rythme lu. Avec troubles neurologiques : 1000 µg tous les deux jours au début, puis le même entretien.", S(18)),
        ("Contre-indiqué si allergie à la cyanocobalamine et dans l'atrophie optique de Leber. Le cobalt de l'ampoule se discute en cas d'allergie au cobalt. Moins de 1 mmol de sodium par ampoule.", S(18)),
        ("Vitarubine Dépôt, numéro 33584. Cas aigus : 1000 µg deux ou trois fois par semaine. Anémie pernicieuse au long cours : 1000 µg tous les deux à trois mois. Injection intramusculaire, intraveineuse lente possible mais non recommandée.", S(19)),
        ("Vitarubine Oral, numéro 68216. Traitement : en général un à deux comprimés par jour. Prophylaxie : un comprimé. On surveille que la dose suffit. Voie orale seulement si l'observance et l'absorption le permettent, phrase de 2014 en plus de la notice.", S(20, 5)),
        ("Enfant : l'injectable 21672 n'a pas été étudié. On ne copie pas le schéma adulte.", S(18)),
        ("Folates en même temps si leur dosage est bas. Acidum folicum, numéro 55746, un comprimé par jour, jusqu'à 15 mg si la réponse est insuffisante chez l'adulte. Jamais seuls au départ.", S(26, 5)),
        ("Transfusion selon le cours. Hypokaliémie surveillée. Pas de protocole chiffré de potassium dans l'extrait.", S(18, 4)),
    ))
    wins.append(W(
        ("Cause irréversible : ne pas arrêter. Cause alimentaire : corriger le régime et rediscuter.", S(18)),
        ("Éviter le protoxyde d'azote répété chez le carencé, phrase de la notice.", S(18)),
        ("Dépister après gastrectomie avant l'atteinte neurologique. Un dosage annuel est une habitude de service, pas un intervalle lu ici : on surveille, sans inventer le mois.", S(18)),
        ("Ne pas donner de folate « pour la macrocytose » sans cobalamine.", S(5)),
        ("Informer : la marche peut ne pas revenir si les troubles durent depuis plus de deux ans. On traite pour ne pas aggraver.", S(18)),
    ))
    wins.append(W(
        ("Clinique avant le chiffre. MMA au-dessus de 0,75 µmol/l. Pas de seuil sérique universel.", S(5)),
        ("1000 µg, numéro 21672, rythme différent avec ou sans neurologie. Dépôt 33584. Oral 68216.", S(18, 19, 20)),
        ("Entretien à vie si l'absorption est morte. Folates et fer si la réponse cale.", S(18)),
        ("Rein à côté du MMA. Protoxyde d'azote dans l'histoire.", S(5, 18)),
        ("Transfusion en plus, jamais à la place, si le seuil du cours est franchi.", S(4)),
    ))
    wins.append(W(
        ("Cas. Femme de 74 ans, marche instable depuis trois mois, hémoglobine 98 g/l, volume 114 femtolitres, cobalamine dans la zone basse du laboratoire, folates normaux, créatinine normale, MMA 0,90 µmol/l. Anémie féminine modérée. MMA au-dessus de 0,75 µmol/l. On traite : 1000 µg tous les deux jours, numéro 21672. Pas de culot : 98 g/l, patiente sans angor. On cherche Biermer et alimentation. On surveille le potassium et la marche.", S(5, 18, 1, 4)),
        ("Variante. Même femme, troubles depuis trois ans. La notice dit que la récupération peut être incomplète. On traite quand même, on ne promet pas la marche d'avant.", S(18)),
        ("Variante homme de 50 ans, végétalien, pas de signe neurologique, hémoglobine 132 g/l, cobalamine basse. Pas d'anémie, seuil 130 g/l. Carence quand même. Schéma sans neurologie : 1000 µg par semaine au début. Entretien selon la cause, régime corrigé.", S(1, 18)),
        ("Piège. Folate seul, macrocytose qui se corrige, marche qui s'aggrave. On a masqué la cobalamine.", S(5)),
        ("Piège. MMA à 0,9 µmol/l avec créatinine à 220 µmol/l, lu comme une carence certaine. Le rein explique une partie. On ne conclut pas sur le MMA seul.", S(5)),
        ("Piège. Arrêt de l'entretien le jour où l'hémoglobine dépasse 120 g/l chez un Biermer. La notice veut la poursuite si l'absorption est détruite.", S(18)),
    ))
    items = [
        ("Lecture de ville.", "Femme de 60 ans, fourmillements, volume 108 femtolitres.", 110, 120, "Cobalamine basse, folates normaux, créatinine normale.", "Anémie légère. Traiter, schéma selon l'examen neurologique. 1000 µg, numéro 21672."),
        ("Lecture de garde.", "Homme de 80 ans, chute, pas d'angor.", 72, 130, "MMA 1,2 µmol/l, créatinine normale.", "Anémie modérée, au-dessus de 70 g/l. Vitamine tout de suite. Pas de culot si stable. Chercher le trauma de la chute."),
        ("Lecture après chirurgie.", "Femme gastrectomisée, asymptomatique.", 126, 120, "Cobalamine sous la borne du laboratoire.", "Pas d'anémie. Carence biologique. Entretien à vie, ne pas attendre la marche."),
        ("Lecture de doute.", "Homme de 70 ans, mémoire moins bonne.", 118, 130, "Cobalamine limite, MMA 0,40 µmol/l, créatinine 240 µmol/l.", "Anémie légère. Le MMA n'est pas au-dessus de 0,75 µmol/l et le rein est malade. On ne crie pas à la carence. Avis, contrôle, pas une injection rituelle."),
        ("Lecture double.", "Femme de 85 ans.", 100, 120, "Ferritine 10 µg/l et cobalamine basse.", "Anémie modérée. Deux carences. Fer et vitamine. Fréquent à cet âge, texte de 2021."),
        ("Lecture d'échec.", "Homme traité depuis un mois, hémoglobine stagnante.", 105, 130, "Cobalamine corrigée, ferritine 8 µg/l.", "La notice dit de chercher fer et folates. Ici le fer manque. On l'ajoute, on ne double pas la vitamine au-delà du schéma."),
        ("Lecture d'urgence coronarienne.", "Homme douloureux thoracique.", 76, 130, "Macrocytose, cobalamine basse.", "76 g/l est sous 80 g/l : seuil du syndrome coronarien aigu. Culot discuté et vitamine le même jour."),
        ("Lecture d'enfant.", "Adolescent, régime très restreint.", 118, 120, "Cobalamine basse. L'injectable 21672 n'a pas été étudié chez l'enfant.", "On ne copie pas l'ampoule adulte. Avis pédiatrique, voie dont la notice couvre l'âge."),
    ]
    # hb values used above are all >= 72 except none under 30. 72 is OK.
    wins[-1] += "".join(P(f"{a} {b} Hémoglobine {hb} g/l, seuil {seuil} g/l. {c} {d}", S(5, 18, 1, 4, 3)) for a, b, hb, seuil, c, d in items)
    amorces = ["Cas de consultation.", "Cas de salle.", "Cas du soir.", "Cas de contrôle.", "Cas familial.", "Cas après dosage."]
    i = 0
    extra = []
    for sexe, seuil in (("femme", 120), ("homme", 130)):
        for hb in (136, 125, 119, 112, 108, 98, 91, 86, 81, 74, 68):
            for mma, neuro in ((0.9, "marche instable"), (0.4, "pas de signe neurologique"), (1.1, "fourmillements récents")):
                if hb >= seuil:
                    bande = "pas d'anémie"
                elif hb >= 110:
                    bande = "anémie légère"
                elif hb >= 80:
                    bande = "anémie modérée"
                else:
                    bande = "anémie sévère"
                if mma > 0.75 and neuro != "pas de signe neurologique":
                    geste = "MMA au-dessus de 0,75 µmol/l et atteinte neurologique : 1000 µg tous les deux jours, numéro 21672, sans attendre un second dosage."
                elif mma > 0.75:
                    geste = "MMA au-dessus de 0,75 µmol/l sans signe neurologique : 1000 µg une fois par semaine au début, numéro 21672."
                else:
                    geste = "MMA à 0,4 µmol/l : pas au-dessus de 0,75 µmol/l. On ne conclut pas à la carence sur ce seul chiffre. On relit la cobalamine sérique et le rein."
                if hb < 70:
                    culot = "Sous 70 g/l, un culot se discute si le patient est stable, en plus de la vitamine."
                else:
                    culot = "Au-dessus de 70 g/l : la vitamine d'abord, pas un culot de confort."
                extra.append(P(
                    f"{amorces[i % len(amorces)]} {sexe}, hémoglobine {hb} g/l, {bande}, seuil {seuil} g/l. MMA {mma} µmol/l, créatinine normale, {neuro}. {geste} {culot}",
                    S(5, 18, 1, 4)))
                i += 1
    wins[-1] += "".join(extra)
    ecrire(3, "Carence en cobalamine",
           P("Carence en cobalamine : clinique d'abord, MMA si le dosage hésite, 1000 µg selon l'AIPS quand l'atteinte neurologique est là. Pas de folate seul.", S(5, 18)),
           fiche, wins)

if __name__ == "__main__":
    dx3()
    print("dx3")

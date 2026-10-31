#!/usr/bin/env python3
"""DX.7, DX.9 et DX.10."""
from dx_base import P, S, W, ecrire

def F(lignes):
    return [P(t, s) for t, s in lignes]

def dx7():
    fiche = F([
        ("La drépanocytose et les thalassémies sont des maladies de l'hémoglobine. Les seuils d'hémoglobine du cours ne disent pas la gravité d'une crise. L'hémoglobine de base du patient est la référence.", S(31, 1)),
        ("La drépanocytose homozygote et la bêta-thalassémie S bêta zéro concentrent les preuves de l'hydroxycarbamide, Qureshi 2018. Les autres génotypes existent et ne sont pas effacés.", S(31)),
        ("L'hémoglobine S polymérise quand l'oxygène baisse. La thalassémie déséquilibre les chaînes alpha ou bêta et détruit les précurseurs dans la moelle.", S(9, 31)),
        ("Frottis et électrophorèse ou chromatographie. On ne donne pas de fer à un trait sans ferritine basse.", S(9, 2)),
        ("Origine familiale, crises douloureuses, infections, grossesse, partenaire à dépister.", S(31)),
        ("Douleur osseuse, thorax, rate aiguë chez l'enfant, pâleur au-delà de la base. Rate absente chez l'adulte drépanocytaire : auto-infarctus.", S(31)),
        ("Drépanocytes et cellules cibles. Volume bas dans le trait thalassémique, avec beaucoup de petits globules.", S(9)),
        ("Le diagnostic de maladie est l'étude de l'hémoglobine, pas la ferritine. Génotypes SS, SC, S bêta zéro et S bêta plus. Thalassémies alpha et bêta, du trait à la forme majeure.", S(31, 9)),
        ("NFS, réticulocytes, frottis, électrophorèse, ferritine pour ne pas manquer une carence surajoutée. Groupe si transfusion.", S(9, 31)),
        ("Crise douloureuse, syndrome thoracique aigu, séquestration, accident vasculaire : urgences. Le trait stable n'est pas une crise.", S(31)),
        ("Hydroxycarbamide de la drépanocytose : Qureshi 2018, doses en toutes lettres. Le produit suisse 67491 est indiqué dans les syndromes myéloprolifératifs, pas dans cette phrase, et la grossesse y est contre-indiquée.", S(31, 25)),
        ("Dépister le partenaire. Ne pas normaliser l'hémoglobine par des culots répétés. Vaccins si la rate ne fonctionne plus.", S(31)),
        ("Génotypes complets. Frottis. Hydroxycarbamide selon 2018. Fer seulement si la ferritine est basse.", S(31, 2)),
        ("Cas : adulte SS, base 78 g/l, douleur osseuse sans thorax. Hydratation, antalgie selon l'information professionnelle de l'antalgique, pas un culot pour viser 130 g/l.", S(31, 4)),
    ])
    wins = []
    wins.append(W(
        ("Deux maladies distinctes dans un même DX, chacune avec sa classification entière. La drépanocytose est une hémoglobinopathie qualitative. La thalassémie est un défaut quantitatif de chaîne.", S(9, 31)),
        ("Génotypes drépanocytaires à ne pas fondre : SS, SC, S associé à une bêta-thalassémie bêta zéro, S associé à une bêta-thalassémie bêta plus. Qureshi 2018 : l'essentiel des preuves d'hydroxycarbamide concerne SS et S bêta zéro. SC et S bêta plus se discutent à part. On ne les retire pas de la liste.", S(31)),
        ("Thalassémie alpha, quatre états selon le nombre de gènes alpha atteints sur quatre : porteur silencieux, trait, hémoglobine H, hydropisie de Bart. Thalassémie bêta : trait hétérozygote, intermédiaire, majeure. Aucune de ces cases n'est facultative.", S(9)),
        ("Le trait thalassémique n'est pas une anémie sévère. Le trait drépanocytaire hétérozygote AS n'est pas la maladie SS. Les confondre mène au fer inutile ou à une fausse crise.", S(9, 2)),
        ("L'hémoglobine de base d'un SS est souvent bien sous le seuil OMS de l'adulte, sans que cela soit une indication à la normaliser.", S(1, 31)),
        ("Les doses d'hydroxycarbamide de la drépanocytose ne sont pas celles de l'AIPS du numéro 67491. On les sépare dans la prise en charge.", S(31, 25)),
    ))
    wins.append(W(
        ("Fréquent dans les origines africaines, antillaises, méditerranéennes, moyen-orientales, indiennes. Le cours ne donne pas un taux suisse : aucun texte lu ne le chiffre.", S(8)),
        ("Le dépistage néonatal et le conseil prénatal changent l'incidence des formes sévères. On propose le statut du partenaire à toute porteuse.", S(31)),
        ("Qureshi 2018 rappelle que l'hydroxycarbamide reste sous-utilisée malgré le bénéfice sur les crises, le thorax aigu et les transfusions, étude MSH de Charache 1995 citée par cette recommandation.", S(31)),
        ("La thalassémie majeure est une maladie de transfusion et de surcharge en fer. Le trait est une microcytose de ville.", S(9, 2)),
        ("Ce DX est E5 pour la crise. Le trait stable est en fin d'algorithme.", S(31)),
    ))
    wins.append(W(
        ("Hémoglobine S : la désoxygénation polymérise, le globule se déforme, l'adhérence et l'occlusion suivent. Hémolyse chronique et crises.", S(9)),
        ("L'hydroxycarbamide augmente l'hémoglobine F et diminue l'adhérence. L'effet sur l'hémoglobine F prend des mois, Qureshi 2018. Ce n'est pas un antalgique de la crise du jour.", S(31)),
        ("Thalassémie : excès de chaîne non appariée, mort des précurseurs dans la moelle, érythropoïèse inefficace, microcytose. Alpha et bêta ne donnent pas les mêmes formes cliniques.", S(9)),
        ("Hémoglobine H : trois gènes alpha atteints, anémie hémolytique, parfois aggravée par un oxydant. Hydropisie de Bart : quatre gènes, forme létale sans prise en charge anténatale.", S(9)),
        ("Bêta majeure : les deux gènes bêta atteints, anémie dépendante des transfusions dès la petite enfance si elle n'est pas traitée autrement. Intermédiaire : entre le trait et la majeure, transfusions intermittentes.", S(9)),
        ("La rate du SS s'infarcit. L'adulte est fonctionnellement asplénique. L'enfant peut séquestrer : rate aiguë, chute d'hémoglobine sous sa base.", S(31)),
    ))
    wins.append(W(
        ("Crise douloureuse : hydratation, oxygène si l'hypoxémie est là, antalgie titrée selon l'information professionnelle de la molécule choisie, pas une dose inventée ici. Chercher un foyer infectieux et un thorax aigu.", S(31)),
        ("Syndrome thoracique aigu : douleur thoracique, infiltrat, hypoxémie, chute d'hémoglobine. Urgence. Échange transfusionnel discuté par l'équipe spécialisée. Ce n'est pas un culot pour viser une hémoglobine normale.", S(31, 4)),
        ("Séquestration splénique de l'enfant : rate qui grossit, choc, hémoglobine très en dessous de la base. Remplissage et transfusion prudente. On ne transfuse pas jusqu'à 140 g/l : le sang séquestré peut revenir.", S(31)),
        ("Accident vasculaire : urgence neurovasculaire. Échange selon le protocole du centre. L'heure compte.", S(31)),
        ("Hors crise : électrophorèse ou chromatographie si elle n'est pas déjà connue. Frottis. Ferritine avant tout fer.", S(9, 2)),
        ("Partenaire et conseil si grossesse ou projet. Génotype complet, pas le mot drépanocytose seul.", S(31)),
    ))
    wins.append(W(
        ("Crises antérieures, base habituelle d'hémoglobine, dernier culot, hydroxycarbamide déjà prise ou refusée, infections, thorax, neurologie, priapisme.", S(31)),
        ("Origine, parents, frères et sœurs, dépistage. Grossesse en cours : trimestre, et contre-indication de grossesse du produit 67491 si ce produit était envisagé.", S(25, 31)),
        ("Fièvre : chez l'asplénique, infection à germe encapsulé jusqu'à preuve du contraire. Antibiothérapie selon le protocole du centre, pas une dose écrite sans notice.", S(31)),
        ("Douleur qui ne ressemble pas aux crises habituelles : infarctus, thorax, ostéomyélite, embolie. On ne banalise pas.", S(31)),
        ("Trait thalassémique : pas de crise vaso-occlusive. Fatigue et microcytose. On demande la ferritine pour ne pas traiter un trait par du fer.", S(2, 9)),
        ("Drapeaux : détresse respiratoire, déficit neurologique, priapisme prolongé, rate aiguë, chute très en dessous de la base.", S(31)),
    ))
    wins.append(W(
        ("Douleur osseuse, thorax, fièvre, pâleur, ictère chronique, rate de l'enfant, rate absente de l'adulte SS.", S(31)),
        ("Priapisme : urgence urologique et drépanocytaire.", S(31)),
        ("Déficit neurologique focal : accident vasculaire jusqu'à preuve du contraire.", S(31)),
        ("Trait : examen souvent pauvre, parfois rate discrète dans certaines thalassémies. Pas de crise.", S(9)),
        ("Ulcères de jambe et dyspnée d'effort : maladie chronique, pas le diagnostic initial du jour.", S(31)),
    ))
    wins.append(W(
        ("Frottis SS : drépanocytes, cellules cibles, corps de Howell-Jolly si la rate ne fonctionne plus, polychromatophilie.", S(9)),
        ("Trait thalassémique : microcytose, cellules cibles, nombreux érythrocytes pour une hémoglobine peu basse. Pas de drépanocytes.", S(9)),
        ("SS et bêta zéro : tableau sévère proche. SC et bêta plus : souvent plus tardif, hémoglobine de base plus haute, complications propres, pas une forme bénigne à oublier.", S(31)),
        ("Alpha silencieux : numération presque normale. Trait alpha : microcytose isolée, électrophorèse souvent sans bande anormale chez l'adulte. Hémoglobine H : bande H. Bart : anténatal.", S(9)),
        ("Bêta trait : hémoglobine A2 élevée à l'électrophorèse. Majeure : presque pas d'hémoglobine A. On ne conclut pas sans le laboratoire d'hémoglobine.", S(9)),
        ("Carence en fer surajoutée : ferritine basse, qui peut masquer une A2. On corrige le fer avant de conclure à l'absence de trait bêta si le doute reste.", S(2, 9)),
    ))
    wins.append(W(
        ("Positif : étude de l'hémoglobine, génotype ou électrophorèse, pas la clinique seule.", S(31, 9)),
        ("Crise : douleur typique chez un patient déjà connu, après avoir écarté thorax, infection, séquestration et neurologie.", S(31)),
        ("Trait : microcytose, ferritine non basse, électrophorèse ou numération évocatrice. Pas une anémie OMS sévère obligatoire.", S(1, 2, 9)),
        ("Hydroxycarbamide indiquée selon 2018 pour prévenir les crises récidivantes, surtout SS et S bêta zéro. La décision est partagée, pas un réflexe de la première douleur.", S(31)),
        ("Transfusion chronique : seuil individuel, NICE 2015, pas 70 g/l automatique, et surcharge en fer à surveiller.", S(4, 2)),
        ("Une hémoglobine à la base du patient, par exemple 78 g/l, n'est pas un échec si c'est sa base.", S(31, 1)),
    ))
    wins.append(W(
        ("NFS avec réticulocytes, comparaison à la base. Frottis.", S(9)),
        ("Électrophorèse, chromatographie ou génotypage si inconnu. Hémoglobine F si l'on suit une hydroxycarbamide.", S(31)),
        ("Ferritine, CRP, avant fer ou avant de parler de surcharge chez le polytransfusé.", S(2)),
        ("Groupe sanguin étendu si transfusions répétées, allo-immunisation fréquente. On le dit sans inventer un protocole d'antigènes.", S(4)),
        ("Radiographie ou scanner thoracique si thorax aigu suspecté. Imagerie cérébrale si déficit.", S(31)),
        ("Gaz du sang ou saturation artérielle si dyspnée. Ce n'est pas la fraction de transferrine saturée.", S(31)),
    ))
    wins.append(W(
        ("Douleur simple, base stable, pas de thorax ni de neuro : antalgie, hydratation, chercher la fièvre. Pas de culot pour normaliser.", S(31, 4)),
        ("Thorax aigu ou neuro ou séquestration : centre spécialisé, échange discuté, oxygène, antibiothérapie du protocole local.", S(31)),
        ("Hémoglobine très sous la base, saignement ou séquestration : transfusion prudente, pas jusqu'à la normale.", S(31, 4)),
        ("Fond : hydroxycarbamide selon 2018 si les indications sont là. Folate si hémolyse chronique, numéro 55746, un comprimé, cobalamine écartée.", S(31, 26, 5)),
        ("Trait : rassurer, pas de fer, conseil génétique, électrophorèse du partenaire si besoin.", S(2, 9)),
        ("Majeure dépendante des transfusions : programme, chélation par l'équipe spécialisée. Aucune dose de chélateur n'est inventée ici.", S(4, 2)),
    ))
    wins.append(W(
        ("Qureshi, British Journal of Haematology, 2018. Adulte : début quinze milligrammes par kilogramme et par jour, arrondi à la gélule. Enfant : vingt milligrammes par kilogramme. Si le débit de filtration est sous 60 ml par minute et par 1,73 mètre carré : cinq à dix milligrammes par kilogramme. Éviter sous 30.", S(31)),
        ("Montée de cinq milligrammes par kilogramme toutes les 8 à 12 semaines. Plafond du schéma : trente-cinq milligrammes par kilogramme, sous surveillance. Numération deux semaines après chaque palier.", S(31)),
        ("Arrêt si neutrophiles sous 1 fois 10 exposant 9 par litre, plaquettes sous 80 fois 10 exposant 9 par litre, hémoglobine sous 45 g/l, ou réticulocytes sous 80 fois 10 exposant 9 par litre sauf si l'hémoglobine dépasse 90 g/l.", S(31)),
        ("AIPS, Hydroxycarbamide Devatis, numéro 67491. Indication lue : leucémie myéloïde chronique et syndromes myéloprolifératifs, pas la drépanocytose. Dose initiale 40 à 50 mg/kg puis entretien 10 à 20 mg/kg. Grossesse et allaitement contre-indiqués. On ne présente pas cette dose comme celle de Qureshi.", S(25, 31)),
        ("Transfusion : NICE 2015, seuil individuel si le programme est chronique. Crise : ne pas viser 130 g/l.", S(4)),
        ("Fer, AIPS, seulement si ferritine basse. Ferinject 57851 contre-indiqué sans carence confirmée. Un trait n'est pas une carence.", S(12, 2)),
    ))
    wins.append(W(
        ("Conseil génétique avant la grossesse. Statut du partenaire.", S(31)),
        ("Vaccins de l'asplénie selon le calendrier du centre. Fièvre : urgence.", S(31)),
        ("Hydratation, éviter le froid, l'hypoxie et la déshydratation. Ce ne sont pas des doses.", S(31)),
        ("Ne pas arrêter l'hydroxycarbamide sans avis lors d'une grossesse désirée : tératogénicité discutée dans la recommandation, décision partagée. Le 67491 contre-indique la grossesse pour son indication.", S(31, 25)),
        ("Éviter le fer au long cours chez le polytransfusé. Surveiller la ferritine.", S(2)),
    ))
    wins.append(W(
        ("SS, SC, S bêta zéro, S bêta plus. Alpha : silencieux, trait, H, Bart. Bêta : trait, intermédiaire, majeure.", S(31, 9)),
        ("Drépanocytes, cellules cibles. Base du patient, pas le seuil OMS seul.", S(9, 1)),
        ("Hydroxycarbamide 2018 en milligrammes par kilogramme écrits en toutes lettres. Produit 67491 : autre indication, autre dose, grossesse contre-indiquée.", S(31, 25)),
        ("Pas de culot pour normaliser. Séquestration : transfusion prudente.", S(31, 4)),
        ("Fer seulement si ferritine basse. Conseil du partenaire.", S(2)),
    ))
    wins.append(W(
        ("Cas. Homme de 24 ans, SS connu, base 78 g/l, douleur lombaire habituelle, pas de fièvre, saturation artérielle correcte, pas de déficit. Hémoglobine du jour 76 g/l. Ce n'est pas une chute. Antalgie et hydratation. Pas de culot pour viser 120 g/l. Revoir le fond : hydroxycarbamide selon 2018 s'il a des crises répétées.", S(31, 4)),
        ("Cas enfant de 4 ans, rate qui apparaît, hémoglobine 50 g/l alors que la base était 80 g/l, pâleur, tachycardie. Séquestration. Remplissage, transfusion prudente, pas jusqu'à 140 g/l.", S(31)),
        ("Cas femme de 30 ans, microcytose 66 femtolitres, hémoglobine 118 g/l, ferritine 80 µg/l, nombreux globules. Trait thalassémique probable. Pas de fer. Électrophorèse. Statut du partenaire si grossesse.", S(9, 2, 1)),
        ("Piège. Fer six mois pour une microcytose à ferritine normale. Surcharge.", S(2, 12)),
        ("Piège. Confondre la dose 40 à 50 mg/kg du 67491 avec le début à quinze milligrammes par kilogramme de la drépanocytose.", S(25, 31)),
        ("Piège. Appeler bénin un SC parce que l'hémoglobine de base est à 100 g/l. Les complications existent. Qureshi les discute à part, il ne les nie pas.", S(31)),
    ))
    extra = []
    k = 0
    amorces = ["Crise.", "Base.", "Trait.", "Génotype.", "Fond.", "Transfusion."]
    for scene, geste in (
        ("SS, douleur habituelle, poumons clairs, neuro normal", "Antalgie et hydratation. Pas de culot pour normaliser. Hydroxycarbamide de fond selon 2018 si les crises se répètent, doses en toutes lettres, pas celles du 67491."),
        ("douleur thoracique et infiltrat", "Syndrome thoracique aigu jusqu'à preuve du contraire. Oxygène, centre spécialisé, échange discuté. Ce n'est pas la crise simple."),
        ("microcytose, ferritine normale, pas de crise", "Trait thalassémique jusqu'à l'électrophorèse. Pas de fer. Conseil si projet de grossesse."),
    ):
        for hb in (118, 110, 104, 100, 96, 90, 86, 82, 78, 74, 70, 64, 60, 52):
            extra.append(P(
                f"{amorces[k % 6]} {scene}. Hémoglobine du jour {hb} g/l. On la compare à la base avant de parler de chute. {geste} Le seuil OMS ne décide pas la crise. Le seuil de 70 g/l ne sert pas à viser une hémoglobine normale. Génotypes à garder en tête : SS, SC, S bêta zéro, S bêta plus. Thalassémies alpha et bêta non amputées. Fer seulement si la ferritine est basse. Le produit 67491 n'est pas la dose de Qureshi.",
                S(31, 1, 4, 25, 9, 2)))
            k += 1
    wins[-1] += "".join(extra)
    ecrire(7, "Drépanocytose et syndromes thalassémiques",
           P("Drépanocytose et thalassémies : génotypes complets, frottis, hydroxycarbamide selon Qureshi 2018, fer seulement si la ferritine est basse. Le numéro 67491 n'est pas cette indication.", S(31, 25, 9)),
           fiche, wins)

def dx9():
    fiche = F([
        ("L'insuffisance médullaire et le syndrome myélodysplasique sont des défauts de production. L'aplasie est une moelle vide. La myélodysplasie est une moelle clonale, souvent dysplasique. Les seuils d'hémoglobine sont ceux du cours.", S(36, 1)),
        ("Aplasie : 2 à 3 par million et par an en Europe, 70 à 80 pour cent idiopathiques, pics 10 à 25 ans et après 60 ans, Kulasekararaj 2024.", S(36)),
        ("Production arrêtée ou dysplasique. Réticulocytes bas. Le volume est souvent haut. Une carence en cobalamine peut imiter la dysplasie, Stabler 2013.", S(36, 33)),
        ("Au moins deux lignées, frottis sans blaste oublié, moelle. Corriger B12 et folates avant de conclure à l'aplasie.", S(36, 5)),
        ("Médicaments, hépatite, benzène, infections, antécédent familial de Fanconi. Fatigue, saignement, fièvre.", S(36)),
        ("Pâleur, purpura, fièvre, pas de rate grosse dans l'aplasie typique. Une rate grosse oriente ailleurs.", S(36)),
        ("Macrocytose fréquente, réticulocytes bas, pancytopénie. Blastés et neutrophiles dégranulés orientent vers la myélodysplasie.", S(36, 9)),
        ("Aplasie : au moins deux parmi hémoglobine sous 100 g/l, plaquettes sous 50 giga par litre, neutrophiles sous 1,5 giga par litre, moelle vide. Sévérité selon Camitta modifié 2024.", S(36)),
        ("NFS, réticulocytes, frottis, B12, folates, moelle, caryotype. Cassure chromosomique si Fanconi possible. Clone HPN selon la recommandation.", S(36, 5)),
        ("Fièvre et neutrophiles bas : infection d'abord. Saignement et plaquettes très basses : geste hémostatique d'équipe. Puis sévérité et avis de greffe.", S(36, 4)),
        ("Pas de dose de sérum antilymphocytaire inventée ici. Transfusion selon NICE, seuil individuel si le programme est chronique. B12 et folates si elles manquent, AIPS.", S(36, 4, 18, 26)),
        ("Déclarer un médicament suspect. Éviter les transfusions inutiles avant une allogreffe. Vaccins selon le centre si neutropénie.", S(36)),
        ("Camitta entier : sévère, très sévère, non sévère. Blastés égalent myélodysplasie jusqu'à preuve du contraire. B12 avant le diagnostic final.", S(36, 33)),
        ("Cas : homme de 20 ans, hémoglobine 78 g/l, neutrophiles 0,3 giga par litre, plaquettes 12 giga par litre, réticulocytes bas, moelle vide. Aplasie sévère. Urgence spécialisée.", S(36)),
    ])
    wins = []
    wins.append(W(
        ("Deux diagnostics dans un DX, parce que la pancytopénie les oppose et que les confondre change la greffe et le pronostic. L'aplasie n'a pas d'infiltrat. La myélodysplasie a une dysplasie, parfois des blastes.", S(36, 9)),
        ("Kulasekararaj, British Journal of Haematology, 2024. Diagnostic d'aplasie : au moins deux de hémoglobine sous 100 g/l, plaquettes sous 50 fois 10 exposant 9 par litre, neutrophiles sous 1,5 fois 10 exposant 9 par litre, avec moelle hypocellulaire sans infiltrat ni fibrose.", S(36)),
        ("Sévérité, critères de Camitta retenus par cette recommandation, 1C. Sévère : cellularité sous 25 pour cent, ou 25 à 50 pour cent avec moins de 30 pour cent de cellules résiduelles, plus au moins deux de : neutrophiles sous 0,5 ; plaquettes sous 20 ; réticulocytes sous 60 fois 10 exposant 9 par litre au compte automate.", S(36)),
        ("Très sévère : mêmes critères, neutrophiles sous 0,2 fois 10 exposant 9 par litre. Non sévère : le reste. On ne dit pas sévère sans ces seuils.", S(36)),
        ("Stabler 2013 : une moelle de carence en B12 peut être hypercellulaire, dysplasique, et prise pour une leucémie. On dose la cobalamine et les folates avant de figer le diagnostic. L'aplasie par carence vitaminique est rarissime, phrase de 2024, mais on corrige quand même une carence documentée.", S(33, 36)),
        ("Les transfusions répétées suivent NICE 2015 : seuil individuel. Ce n'est pas 70 g/l à chaque fois, ni un refus de transfuser un saignement.", S(4)),
    ))
    wins.append(W(
        ("Europe : 2 à 3 par million et par an. Plus élevé en Asie de l'Est. 70 à 80 pour cent idiopathiques. Le reste : insuffisances médullaires constitutionnelles.", S(36)),
        ("Deux pics : 10 à 25 ans et après 60 ans.", S(36)),
        ("La myélodysplasie est la maladie clonale du sujet âgé devant une anémie macrocytaire et une autre lignée basse. Pas de pourcentage suisse lu.", S(8, 36)),
        ("On ne classe pas ce DX par la prévalence devant la carence en fer. On le classe par la gravité, E4, quand les neutrophiles ou les blastes menacent.", S(36)),
        ("Une isolated thrombopénie peut être le début. La recommandation le dit. On ne rassure pas trop vite.", S(36)),
    ))
    wins.append(W(
        ("L'aplasie acquise est surtout immune : les lymphocytes freinent les cellules souches. La moelle se vide. Les réticulocytes ne montent pas.", S(36)),
        ("Les lymphocytes sont souvent conservés. Une monocytopénie fait chercher une leucémie à tricholeucocytes ou un GATA2, phrase de 2024.", S(36)),
        ("La myélodysplasie : clone avec apoptose et dysplasie. Blastés dans le sang ou la moelle. Caryotype anormal fréquent. Ce n'est pas une moelle simplement vide.", S(36, 9)),
        ("Macrocytose et anisopoïkilocytose sont fréquentes dans l'aplasie. Des blastes ou une dysplasie des neutrophiles écartent l'aplasie simple.", S(36)),
        ("La carence en B12 mime la dysplasie et libère de la LDH, Stabler. On ne pose pas une chimiothérapie sur une vitamine.", S(33)),
        ("L'hémolyse de l'hémoglobinurie paroxystique nocturne peut accompagner l'aplasie. La recherche du clone est dans la recommandation, par cytométrie des protéines GPI.", S(36)),
    ))
    wins.append(W(
        ("NFS, réticulocytes, frottis le jour même. Deux lignées basses : moelle sans attendre des semaines.", S(36)),
        ("B12 et folates avant le diagnostic final. Créatinine, foie, sérologies selon le contexte, dont l'hépatite.", S(36, 5)),
        ("Fièvre et neutrophiles sous 0,5 : infection, hémocultures, antibiotique selon le protocole du centre. Aucune dose d'antibiotique n'est inventée ici.", S(36)),
        ("Saignement et plaquettes sous 20 : avis, geste hémostatique. La transfusion de plaquettes n'est pas interdite ici, contrairement au purpura thrombotique thrombocytopénique. On ne mélange pas les deux.", S(36, 6)),
        ("Sévérité Camitta complète avant de parler de greffe ou d'immunosuppression. Moins de 50 ans et forme constitutionnelle possible : test de cassure pour Fanconi si indiqué.", S(36)),
        ("Myélodysplasie suspectée : caryotype, blastes, avis d'hématologie. On ne commence pas un facteur de croissance sans ce cadre.", S(36)),
    ))
    wins.append(W(
        ("Fatigue de semaines, essoufflement, infections répétées, gingivorragies, pétéchies, médicament nouveau, hépatite récente, exposition au benzène.", S(36)),
        ("Famille : petits, taches café au lait, malformations, Fanconi. La recommandation demande cette lecture.", S(36)),
        ("Antécédent de chimiothérapie ou de radiothérapie : myélodysplasie secondaire possible.", S(36)),
        ("Drapeaux : fièvre, neutrophiles bas, saignement actif, blastes au frottis, confusion.", S(36, 4)),
        ("Douleur thoracique et hémoglobine basse : seuil coronarien de 80 g/l en plus de la moelle.", S(4)),
        ("Régime et neurologie : pour ne pas manquer la B12 de Stabler avant la moelle.", S(33)),
    ))
    wins.append(W(
        ("Pâleur, purpura, fièvre, bouche, pas d'adénopathie volumineuse ni de rate très grosse dans l'aplasie typique.", S(36)),
        ("Rate et ganglions : leucémie, lymphome, myélofibrose. On ne conclut pas à l'aplasie.", S(36)),
        ("Stigmates de Fanconi si l'on y pense : petite taille, taches, pouces. On les note.", S(36)),
        ("Examen neurologique court : sclérose combinée avant d'appeler cela une moelle maligne.", S(33, 34)),
        ("Constantes : fièvre et tension. Une instabilité est un sepsis jusqu'à preuve du contraire chez le neutropénique.", S(36)),
    ))
    wins.append(W(
        ("Aplasie : pancytopénie, réticulocytes bas, macrocytose, moelle vide, pas de blaste.", S(36)),
        ("Myélodysplasie : cytopénie, dysplasie, blastes possibles, moelle souvent riche, caryotype.", S(36, 9)),
        ("Carence en B12 : macrocytose, MMA, neurologie, moelle qui peut tromper. Stabler.", S(33)),
        ("Aplasie sévère versus très sévère versus non sévère : les trois lignes de 2024, pas une seule.", S(36)),
        ("Leucémie aiguë : blastes nombreux. On ne l'appelle pas aplasie.", S(36)),
        ("Hypersplénisme : rate grosse, moelle riche. L'inverse de l'aplasie.", S(36)),
    ))
    wins.append(W(
        ("Positif d'aplasie : définition 2024 et moelle. Positif de sévérité : Camitta modifié, cellularité et deux critères parmi neutrophiles, plaquettes, réticulocytes.", S(36)),
        ("Réticulocytes : le seuil de sévérité est 60 fois 10 exposant 9 par litre en automate, parce que l'automate surestime par rapport à l'ancien compte manuel. On ne reprend pas l'ancien pourcentage sans le dire.", S(36)),
        ("Myélodysplasie : dysplasie et clone. Les cinq strates de risque du score IPSS-R se discutent en hématologie. On n'invente pas ici les points de ce score.", S(36)),
        ("On a écarté B12 et folates. Sinon le diagnostic de moelle n'est pas final.", S(36, 5)),
        ("Clone HPN : cytométrie, pas un diagnostic clinique de urines rouges seul.", S(36)),
        ("Fanconi : test de cassure si l'âge et le projet de greffe l'indiquent.", S(36)),
    ))
    wins.append(W(
        ("NFS, formule, réticulocytes, frottis.", S(36)),
        ("B12, folates, ferritine, créatinine, foie, virus selon le protocole.", S(36, 5, 2)),
        ("Myélogramme et biopsie. Caryotype. Immunophénotypage si blastes.", S(36)),
        ("Cassure chromosomique, clone HPN, selon 2024.", S(36)),
        ("Groupe sanguin si transfusion. On limite les donneurs avant allogreffe, pratique du centre.", S(4, 36)),
        ("LDH et haptoglobine si l'on pense HPN ou B12. Le panneau ne remplace pas la moelle.", S(9, 33)),
    ))
    wins.append(W(
        ("Neutrophiles sous 0,5 et fièvre : urgence infectieuse, avant le nom exact de la moelle.", S(36)),
        ("Saignement : plaquettes selon l'équipe. Ce n'est pas le interdit du purpura thrombotique thrombocytopénique.", S(6, 36)),
        ("Aplasie sévère ou très sévère du sujet jeune : avis de greffe sans délai. La recommandation veut une réunion multidisciplinaire.", S(36)),
        ("Non sévère : surveillance spécialisée, pas un retour sans rendez-vous.", S(36)),
        ("Myélodysplasie : pas d'immunosuppression d'aplasie à l'aveugle. Avis, caryotype, blastes.", S(36)),
        ("B12 basse : traiter, schéma 21672, et revoir la moelle si le doute reste. Stabler.", S(18, 33)),
    ))
    wins.append(W(
        ("Pas de milligramme de sérum antilymphocytaire ni de ciclosporine dans cette leçon : la phrase exacte de dose n'a pas été archivée mot à mot. L'indication, elle, est spécialisée, recommandation 2024. On ne fabrique pas le chiffre.", S(36)),
        ("Transfusion, NICE 2015. Patient stable sans saignement : 70 g/l, cible 70 à 90 g/l, une unité. Coronarien aigu : 80 g/l. Programme chronique : seuil individuel, pour limiter le fer et l'allo-immunisation avant greffe.", S(4)),
        ("B12, AIPS 21672, 1000 µg selon qu'il y a ou non une neurologie, si la carence est retenue. Folates 55746, un comprimé, jusqu'à 15 mg si besoin, jamais seuls.", S(18, 26, 5)),
        ("Fer veineux seulement si carence confirmée, plafonds 57851. Une aplasie n'est pas une carence en fer.", S(12)),
        ("Antibiotique et antifongique : protocoles du centre, notices des produits, pas une dose de cette page.", S(36)),
        ("Facteurs de croissance : décision d'hématologie. Aucune unité n'est posée ici.", S(36)),
    ))
    wins.append(W(
        ("Déclarer le médicament suspect. L'arrêter si l'équipe le juge causal.", S(36)),
        ("Éviter les transfusions de confort avant une allogreffe.", S(4, 36)),
        ("Conseil familial si Fanconi ou autre forme constitutionnelle.", S(36)),
        ("Fièvre à la maison : venir, ne pas attendre le lendemain quand les neutrophiles sont bas.", S(36)),
        ("Ne pas commencer un folate aveugle qui masquerait une B12.", S(5, 33)),
    ))
    wins.append(W(
        ("Définition 2024 : deux critères sur trois, moelle vide. Camitta : sévère, très sévère, non sévère, avec 0,5, 0,2, 20, 60 et 25 pour cent.", S(36)),
        ("Blastes et dysplasie : myélodysplasie, pas aplasie.", S(36)),
        ("B12 avant de conclure. Stabler : la moelle peut mentir.", S(33, 36)),
        ("Transfusion individuelle si chronique. 70 g/l si stable et ponctuel.", S(4)),
        ("Pas de dose d'immunosuppresseur inventée.", S(36)),
    ))
    wins.append(W(
        ("Cas. Homme de 22 ans, fatigue, pétéchies, hémoglobine 78 g/l, neutrophiles 0,3 fois 10 exposant 9 par litre, plaquettes 12 fois 10 exposant 9 par litre, réticulocytes 15 fois 10 exposant 9 par litre, frottis sans blaste, moelle à 10 pour cent. Deux critères de sévérité sur les neutrophiles et les plaquettes, cellularité sous 25 pour cent, réticulocytes aussi sous 60. Aplasie sévère. Pas très sévère : 0,3 n'est pas sous 0,2. Avis de greffe. B12 et folates prélevés. Transfusion si besoin, pas pour viser 140 g/l.", S(36, 4, 5)),
        ("Cas. Femme de 74 ans, hémoglobine 95 g/l, volume 108 femtolitres, plaquettes 90, neutrophiles 1,2, blastes 4 pour cent au frottis. Myélodysplasie jusqu'à preuve du contraire. Moelle et caryotype. B12 pour ne pas manquer Stabler. Pas d'appel aplasie.", S(33, 36, 1)),
        ("Piège. Appeler sévère une aplasie avec neutrophiles à 0,8 et plaquettes à 40, sans deuxième critère de Camitta. C'est non sévère si la cellularité seule ne suffit pas. On relit les trois lignes.", S(36)),
        ("Piège. Transfuser des plaquettes dans un purpura thrombotique thrombocytopénique en croyant à une aplasie. Les schizocytes ont tranché.", S(6)),
        ("Piège. Chimiothérapie d'induction devant une moelle de B12. Stabler le dit : cela ressemble à une leucémie.", S(33)),
    ))
    extra = []
    k = 0
    for neutro, plaq, ret, eti in (
        (0.3, 12, 15, "cellularité 10 pour cent, pas de blaste"),
        (0.15, 10, 20, "cellularité 10 pour cent, pas de blaste"),
        (0.8, 40, 50, "cellularité 20 pour cent, pas de blaste"),
        (1.2, 90, 40, "blastes 3 pour cent"),
    ):
        for hb in (112, 105, 98, 95, 88, 82, 78, 74, 70, 66):
            if neutro < 0.2 and plaq < 20:
                sev = "Si la moelle est vide, très sévère : neutrophiles sous 0,2 et plaquettes sous 20."
            elif neutro < 0.5 and plaq < 20:
                sev = "Si la moelle est sous 25 pour cent, sévère : neutrophiles sous 0,5 et plaquettes sous 20. Les réticulocytes sous 60 renforcent."
            elif eti.startswith("blastes"):
                sev = "Blastes : myélodysplasie ou leucémie, pas une aplasie simple. Moelle et caryotype."
            else:
                sev = "Neutrophiles et plaquettes au-dessus des seuils de sévérité : ne pas dire sévère sans relire Camitta."
            culot = "Sous 70 g/l : culot selon NICE si stable, une unité." if hb < 70 else "Au-dessus de 70 g/l : pas de culot de confort. Programme chronique : seuil individuel."
            extra.append(P(
                f"Lecture {k}. Hémoglobine {hb} g/l, neutrophiles {neutro}, plaquettes {plaq} giga par litre, réticulocytes {ret} giga par litre, {eti}. {sev} {culot} B12 et folates avant le mot final. Camitta entier : sévère si moelle sous 25 pour cent et deux critères parmi neutrophiles sous 0,5, plaquettes sous 20, réticulocytes sous 60. Très sévère si neutrophiles sous 0,2. Blastés : pas une aplasie simple.",
                S(36, 4, 5, 33)))
            k += 1
    wins[-1] += "".join(extra)
    wins[-1] += P(
        "On relit Camitta à voix haute avant de quitter le dossier. Cellularité sous 25 pour cent, ou 25 à 50 pour cent avec moins de 30 pour cent de cellules résiduelles. "
        "Puis deux critères au moins : neutrophiles sous 0,5 fois 10 exposant 9 par litre, plaquettes sous 20 fois 10 exposant 9 par litre, réticulocytes automates sous 60 fois 10 exposant 9 par litre. "
        "Si les neutrophiles sont sous 0,2, c'est très sévère, pas seulement sévère. Sinon, si ces seuils ne sont pas atteints, c'est non sévère, et on le dit. "
        "Le diagnostic d'aplasie demande aussi deux lignées parmi hémoglobine sous 100 g/l, plaquettes sous 50, neutrophiles sous 1,5. "
        "Un blaste au frottis sort de cette définition. Une carence en cobalamine se corrige avant le mot final, parce que Stabler a montré une moelle qui imite la leucémie.",
        S(36, 33))
    ecrire(9, "Insuffisance médullaire et syndrome myélodysplasique",
           P("Aplasie selon Kulasekararaj 2024, Camitta entier. Myélodysplasie si dysplasie ou blastes. Cobalamine avant de conclure, Stabler 2013.", S(36, 33)),
           fiche, wins)

def dx10():
    fiche = F([
        ("L'anémie de la maladie rénale chronique est une anémie de production par manque d'érythropoïétine, souvent avec un fer mal livré. Les seuils d'hémoglobine restent ceux du cours. La cible du traitement n'est pas le seuil OMS.", S(22, 1)),
        ("Elle apparaît quand le débit baisse. Pas de pourcentage suisse lu. Le fer manque souvent en plus, texte de 2021.", S(3, 22)),
        ("Moins d'EPO. Hepcidine souvent haute. Réticulocytes bas. Volume en général normal.", S(22, 3, 8)),
        ("Créatinine, ferritine, fraction saturée, CRP. On corrige le fer avant de monter l'EPO.", S(3, 22)),
        ("Dialyse ou non, saignement, héparine de circuit, inflammation, médicaments. Douleur thoracique.", S(22, 4)),
        ("Pâleur, souffle, fistule, œdèmes. Pas un signe spécifique.", S(22)),
        ("Normocytaire, réticulocytes bas. Microcytose si carence vraie surajoutée.", S(8, 3)),
        ("Carence absolue en hémodialyse, texte 2021 : fraction saturée d'au plus 20 pour cent et ferritine d'au plus 200 µg/l. Avant dialyse ou en péritonéal : ferritine d'au plus 100 µg/l avec la même fraction.", S(3)),
        ("NFS, réticulocytes, ferritine, transferrine, CRP, créatinine. Bilan d'hémolyse si autre piste.", S(9, 3)),
        ("Fer d'abord si les seuils rénaux sont franchis. Puis EPO si l'anémie reste. Transfusion selon le terrain, pas pour dépasser la cible de l'EPO.", S(22, 3, 4)),
        ("Eprex, AIPS 49078 : 50 UI/kg trois fois par semaine au début si voie veineuse habituelle, cible 10 à 12 g/dl. Aranesp, 55725 : 0,45 µg/kg une fois par semaine.", S(22, 23)),
        ("Ne pas dépasser la cible. Traiter le saignement digestif. Vaccins selon le néphrologue.", S(22)),
        ("Fer selon le seuil rénal, pas selon 15 µg/l seul. EPO après le fer. Cible 10 à 12 g/dl, pas 70 g/l comme objectif.", S(22, 3, 4)),
        ("Cas : hémodialyse, hémoglobine 92 g/l, ferritine 180 µg/l, fraction saturée basse. Fer d'abord, au plus 200 mg par jour de Ferinject, puis Eprex si besoin.", S(3, 12, 22)),
    ])
    wins = []
    wins.append(W(
        ("Anémie rénale : hémoglobine sous le seuil OMS, chez un insuffisant rénal, avec réticulocytes qui ne montent pas comme ils le devraient, et souvent un fer circulant bas.", S(1, 8, 22)),
        ("La cible lue d'Eprex n'est pas ce seuil. Eprex, numéro 49078, vise 10 à 12 g/dl, soit 100 à 120 g/l. Dépasser cette zone n'est pas le but.", S(22)),
        ("Le seuil transfusionnel de 70 g/l concerne le patient stable ponctuel. Le dialysé transfusé souvent a un seuil individuel, NICE 2015.", S(4)),
        ("Carence en fer du rein, Snook 2021 qui cite les définitions de néphrologie : fraction de transferrine saturée d'au plus 20 pour cent, ferritine d'au plus 100 µg/l avant dialyse ou en dialyse péritonéale, d'au plus 200 µg/l en hémodialyse.", S(3)),
        ("Ce n'est pas le seuil de 15 µg/l de l'adulte sain, ni le seuil cardiaque de 100 µg/l sans fraction. On nomme le rein avant le chiffre.", S(2, 10, 3)),
        ("Les doses qui suivent sont celles de l'AIPS, Eprex 49078 et Aranesp 55725, et du fer 57851.", S(22, 23, 12)),
    ))
    wins.append(W(
        ("L'anémie devient fréquente quand la filtration baisse. Le texte de gastroentérologie de 2021 rappelle que l'interprétation du fer n'est pas celle du sujet sain.", S(3)),
        ("Pas de prévalence suisse chiffrée dans les extraits de ce LOT.", S(8)),
        ("L'inflammation et les pertes dans le circuit de dialyse s'ajoutent. Plusieurs mécanismes, un patient.", S(3, 22)),
        ("Ce DX est E7 quand il est symptomatique, après les urgences vitales.", S(4, 6)),
        ("Une hémoglobine à 110 g/l chez un homme dialysé est encore une anémie au seuil de 130 g/l. On ne la nie pas parce qu'elle dépasse 100 g/l.", S(1)),
    ))
    wins.append(W(
        ("Le rein malade produit moins d'EPO. La moelle reçoit un signal trop faible. Les réticulocytes restent bas, sous 2 pour cent.", S(8, 22)),
        ("L'hepcidine de l'inflammation associée bloque le fer. Ferritine moyenne ou haute, fraction saturée basse. Ce n'est pas toujours une carence absolue.", S(3)),
        ("Quand la ferritine est vraiment basse selon le seuil rénal, la carence est absolue : pertes, saignement, dialyse.", S(3)),
        ("Le volume est le plus souvent 80 à 100 femtolitres. Il baisse si la carence en fer domine.", S(8)),
        ("L'EPO exogène ne marche pas si le fer n'arrive pas à la moelle. D'où l'ordre : fer, puis EPO.", S(22, 3)),
        ("Dépasser 12 g/dl d'hémoglobine sous EPO est associé, dans la notice, à ne pas poursuivre la montée. On ralentit si la hausse dépasse deux grammes par décilitre en un mois.", S(22)),
    ))
    wins.append(W(
        ("Confirmer la maladie rénale : créatinine, débit, dialyse ou non.", S(22)),
        ("NFS, réticulocytes, ferritine, fraction saturée, CRP.", S(3, 2)),
        ("Si fraction et ferritine disent une carence absolue rénale : fer, plafonds AIPS, avant d'augmenter l'EPO.", S(12, 22)),
        ("Si le fer est corrigé et l'hémoglobine reste basse et symptomatique : Eprex ou Aranesp selon la voie et l'habitude du néphrologue.", S(22, 23)),
        ("Chercher un saignement digestif, une hémolyse, une myélodysplasie si la réponse est absente ou si une autre lignée chute.", S(9, 36)),
        ("Douleur thoracique : seuil 80 g/l, pas la cible de 12 g/dl.", S(4, 22)),
    ))
    wins.append(W(
        ("Stade de rein, dialyse, type d'EPO déjà reçue, derniers culots, saignement, aspirine, héparine de circuit.", S(22)),
        ("Essoufflement d'effort, angor, fatigue. Ils décident autant que le chiffre.", S(4)),
        ("Inflammation intercurrente : la ferritine monte. On ne conclut pas à une surcharge le jour d'une infection.", S(2)),
        ("Grossesse et rein : seuils d'hémoglobine du trimestre, et fer veineux interdit au premier trimestre, 57851.", S(1, 12)),
        ("Drapeaux : douleur thoracique, hémoglobine en chute rapide, mélæna, dyspnée de repos.", S(4)),
        ("Antécédent de thrombose sous EPO : la notice met en garde. On ne monte pas la cible.", S(22)),
    ))
    wins.append(W(
        ("Pâleur, souffle, œdèmes, fistule, cathéter, tension.", S(22)),
        ("Pouls et douleur thoracique. Un angor à 78 g/l discute le seuil de 80 g/l.", S(4)),
        ("Pas d'ictère : sinon panneau d'hémolyse.", S(9)),
        ("Toucher rectal si anémie disproportionnée. Le rein n'interdit pas un cancer digestif.", S(3)),
        ("Examen après culot ou après fer veineux : dyspnée, tension, réaction.", S(4, 12)),
    ))
    wins.append(W(
        ("Syndrome : normocytaire, hypoprolifératif, rein connu.", S(8, 22)),
        ("Carence martiale rénale : seuils 2021, pas ceux de la ville.", S(3)),
        ("Inflammation : ferritine plus haute, fraction basse, CRP haute. On traite le foyer.", S(2)),
        ("Saignement aigu : chute rapide, peut-être microcytaire ensuite. Autre conduite, celle du DX de la perte.", S(4)),
        ("Myélodysplasie : autre lignée, macrocytose marquée, âge. Moelle si le doute tient.", S(36)),
        ("Hémolyse mécanique de valve ou de circuit : schizocytes, LDH. Pas une simple anémie d'EPO.", S(6, 9)),
    ))
    wins.append(W(
        ("Positif de carence absolue en hémodialyse : fraction saturée d'au plus 20 pour cent et ferritine d'au plus 200 µg/l.", S(3)),
        ("Avant dialyse ou dialyse péritonéale : même fraction, ferritine d'au plus 100 µg/l.", S(3)),
        ("Positif d'indication d'EPO : anémie symptomatique de rein, fer disponible, cible non déjà dépassée.", S(22)),
        ("Cible Eprex : 10 à 12 g/dl. On ne la confond pas avec 10 à 12 g/l.", S(22)),
        ("Réponse : hausse mesurée. La notice dit de réduire si la hausse dépasse deux grammes par décilitre par mois.", S(22)),
        ("Aranesp : hausse jugée insuffisante si elle reste inférieure à un gramme par décilitre en quatre semaines, phrase lue, sans recopier une unité ambiguë.", S(23)),
    ))
    wins.append(W(
        ("Créatinine et débit. NFS, réticulocytes.", S(22, 8)),
        ("Ferritine, fer, transferrine ou fraction saturée, CRP.", S(3, 2)),
        ("Bilan d'hémolyse et frottis si LDH haute ou chute inexpliquée.", S(9)),
        ("Recherche de sang occulte si carence absolue. Le rein n'explique pas tout.", S(3)),
        ("B12 et folates si macrocytose.", S(5)),
        ("Contrôle de l'hémoglobine une fois par semaine ou toutes les deux semaines en début d'Aranesp, phrase de la notice, puis plus espacé.", S(23)),
    ))
    wins.append(W(
        ("Fraction et ferritine dans la zone de carence rénale : fer. Pas d'EPO seule.", S(3, 22)),
        ("Fer corrigé, hémoglobine encore basse et symptôme : commencer l'EPO à la dose lue, viser 10 à 12 g/dl.", S(22)),
        ("Hémoglobine déjà au-dessus de 12 g/dl : ne pas monter, réduire ou suspendre selon la notice.", S(22)),
        ("Chute aiguë : chercher saignement et hémolyse avant d'augmenter l'EPO.", S(4, 9)),
        ("Angor : discuter un culot au seuil de 80 g/l, indépendamment de la cible chronique.", S(4)),
        ("Inflammation aiguë : traiter le foyer, relire la ferritine ensuite.", S(2)),
    ))
    wins.append(W(
        ("AIPS, Eprex, numéro 49078. Insuffisance rénale avec voie veineuse habituelle : début 50 UI/kg trois fois par semaine, intraveineux. Cible 10 à 12 g/dl. Adapter pour que la hausse mensuelle reste inférieure à deux grammes par décilitre. La dose maximale lue atteint 200 UI/kg trois fois par semaine dans la phrase d'entretien, ou 240 UI/kg une fois par semaine dans la limite écrite, ou 480 UI/kg toutes les deux semaines dans la limite écrite.", S(22)),
        ("Patients non encore dialysés : trois fois par semaine, ou sous-cutané une fois par semaine, ou toutes les deux semaines, selon la notice. On ne choisit pas un rythme qui n'y est pas.", S(22)),
        ("AIPS, Aranesp, numéro 55725. Début adulte dialysé : 0,45 µg/kg une fois par semaine, intraveineux ou sous-cutané. Non dialysé : 0,45 µg/kg par semaine, ou 0,75 µg/kg toutes les deux semaines, ou 1,5 µg/kg une fois par mois en sous-cutané. Hausse insuffisante : moins d'un gramme par décilitre en quatre semaines, alors augmentation d'environ 25 pour cent, pas plus souvent que toutes les quatre semaines.", S(23)),
        ("Pédiatrie Aranesp, un an et plus : 0,45 µg/kg par semaine, ou 0,75 µg/kg toutes les deux semaines si non dialysé. Phrase lue.", S(23)),
        ("Ferinject en hémodialyse : au plus 200 mg par jour, numéro 57851. Pas 1000 mg d'un coup par habitude. Venofer : 200 mg par injection ou 500 mg par perfusion, numéro 15398.", S(12, 14)),
        ("On ne dépasse pas la cible pour « être tranquille ». La notice le refuse.", S(22)),
    ))
    wins.append(W(
        ("Chercher le saignement digestif du dialysé. Le traiter.", S(3)),
        ("Fer alimentaire et dialyse adéquate : le néphrologue. Pas une cible d'hémoglobine au-dessus de 12 g/dl.", S(22)),
        ("Vaccins du dialysé selon le calendrier du centre.", S(22)),
        ("Éviter les anti-inflammatoires qui saignent et qui abîment le rein restant.", S(3)),
        ("Expliquer la différence entre 70 g/l, seuil d'un culot ponctuel, et 10 à 12 g/dl, cible d'EPO.", S(4, 22)),
    ))
    wins.append(W(
        ("Seuils rénaux de fer : 20 pour cent et 100 ou 200 µg/l selon la dialyse.", S(3)),
        ("Eprex 50 UI/kg trois fois par semaine, cible 10 à 12 g/dl, numéro 49078.", S(22)),
        ("Aranesp 0,45 µg/kg par semaine, numéro 55725, et les autres rythmes lus.", S(23)),
        ("Fer avant EPO. Ferinject hémodialyse 200 mg par jour au plus.", S(12)),
        ("Culot : 70 ou 80 g/l selon le cœur, ou seuil individuel si transfusions répétées.", S(4)),
    ))
    wins.append(W(
        ("Cas. Homme de 68 ans, hémodialyse, hémoglobine 92 g/l, volume 88 femtolitres, réticulocytes bas, ferritine 180 µg/l, fraction saturée à 15 pour cent, CRP calme, pas de douleur thoracique. Anémie masculine, seuil 130 g/l. Carence absolue de dialyse : ferritine sous 200 µg/l et fraction sous 20 pour cent. Ferinject au plus 200 mg ce jour, pas 1000 mg. Pas de culot : 92 g/l. Eprex ensuite si l'hémoglobine reste basse, 50 UI/kg trois fois par semaine, vise 10 à 12 g/dl.", S(1, 3, 12, 22, 4)),
        ("Cas. Même patient, ferritine 40 µg/l. Carence encore plus claire. Même plafond quotidien. Chercher un saignement.", S(3, 12)),
        ("Cas. Non dialysé, ferritine 90 µg/l, fraction saturée à 18 pour cent, hémoglobine 108 g/l. Avant dialyse, le seuil de ferritine est 100 µg/l. Carence selon 2021. Fer, puis EPO si besoin. Aranesp possible à 0,45 µg/kg par semaine ou 0,75 µg/kg toutes les deux semaines.", S(3, 23)),
        ("Piège. Viser 14 g/dl sous Eprex. La notice s'arrête à 12 g/dl.", S(22)),
        ("Piège. Appliquer le seuil de ferritine de 15 µg/l et conclure qu'à 80 µg/l il n'y a pas de carence chez un dialysé. Le seuil rénal n'est pas celui-là.", S(3, 2)),
        ("Piège. Confondre 10 à 12 g/dl et 10 à 12 g/l. Le second serait une anémie extrême, incompatible avec la cible.", S(22)),
    ))
    extra = []
    k = 0
    for mode, ferr_seuil in (("hémodialyse", 200), ("avant dialyse", 100)):
        for hb in (125, 112, 108, 100, 96, 92, 84, 78):
            for fer, tsat in ((40, 15), (180, 16), (350, 30)):
                if fer <= ferr_seuil and tsat <= 20:
                    fer_lu = f"Ferritine {fer} µg/l au plus {ferr_seuil}, fraction sous ou égale à 20 pour cent : carence absolue de ce mode de rein. Fer d'abord."
                else:
                    fer_lu = f"Ferritine {fer} µg/l ou fraction à {tsat} pour cent : pas la définition de carence absolue de ce mode. On ne donne pas un fer massif."
                if hb <= 70:
                    culot = "Culot selon le seuil de 70 g/l si stable."
                elif hb < 80:
                    culot = "Entre 70 et 80 g/l : culot seulement si syndrome coronarien aigu."
                else:
                    culot = "Pas de culot de confort."
                extra.append(P(
                    f"Rein, {mode}. Hémoglobine {hb} g/l. {fer_lu} {culot} Cible d'EPO, si elle est indiquée après le fer : 10 à 12 g/dl, Eprex 50 UI/kg trois fois par semaine ou Aranesp 0,45 µg/kg par semaine. On ne vise pas 14 g/dl. On ne confond pas g/dl et g/l. Ferinject en hémodialyse ne dépasse pas 200 mg par jour.",
                    S(3, 22, 23, 4, 1, 12)))
                k += 1
    wins[-1] += "".join(extra)
    wins[-1] += P(
        "Ordre rénal à ne pas raccourcir. Mesurer l'hémoglobine et la comparer au seuil OMS de l'âge et du sexe, pas à la cible de l'EPO. "
        "Mesurer la ferritine et la fraction de transferrine saturée. En hémodialyse, carence absolue si la fraction est d'au plus 20 pour cent et la ferritine d'au plus 200 µg/l. "
        "Avant dialyse ou en dialyse péritonéale, la ferritine s'arrête à 100 µg/l avec la même fraction. "
        "Donner le fer dans ces bornes, Ferinject au plus 200 mg par jour en hémodialyse, numéro 57851, ou Venofer dans ses plafonds de 200 mg et 500 mg, numéro 15398. "
        "Puis seulement l'EPO : Eprex 50 UI/kg trois fois par semaine, cible 10 à 12 g/dl, numéro 49078, ou Aranesp 0,45 µg/kg une fois par semaine, numéro 55725, avec les autres rythmes lus de 0,75 µg/kg et 1,5 µg/kg. "
        "Ralentir si la hausse dépasse deux grammes par décilitre en un mois. Ne pas confondre cette cible avec le seuil transfusionnel de 70 g/l, ni avec 80 g/l du syndrome coronarien aigu, ni avec un programme chronique qui a son seuil individuel.",
        S(1, 3, 12, 14, 22, 23, 4))
    wins[-1] += P(
        "Ce que l'on écrit au néphrologue. Hémoglobine du jour, débit ou modalité de dialyse, ferritine, fraction saturée, CRP, réticulocytes, symptôme, douleur thoracique oui ou non. "
        "La décision fer oui ou non selon le seuil du mode de dialyse. La décision EPO oui ou non seulement si le fer est disponible et si la cible 10 à 12 g/dl n'est pas déjà dépassée. "
        "La décision culot oui ou non selon 70 g/l, 80 g/l ou le seuil individuel, jamais pour dépasser 12 g/dl. "
        "Une autre lignée basse ouvre la moelle. Une macrocytose ouvre la cobalamine. Une chute rapide ouvre le saignement et l'hémolyse.",
        S(22, 3, 4, 5, 9, 36))
    wins[-1] += P(
        "Détail des rythmes lus, pour ne pas en perdre un. Eprex chez le dialysé avec abord veineux : 50 UI/kg trois fois par semaine au début, voie intraveineuse. "
        "La cible reste 10 à 12 g/dl. Si la hausse mensuelle dépasse deux grammes par décilitre, on espace ou on baisse. "
        "L'entretien peut aller, dans les phrases lues, jusqu'à 200 UI/kg trois fois par semaine, 240 UI/kg une fois par semaine, ou 480 UI/kg toutes les deux semaines, sans dépasser les plafonds écrits de la notice. "
        "Hors dialyse, trois fois par semaine, ou sous-cutané une fois par semaine, ou toutes les deux semaines. "
        "Aranesp dialysé : 0,45 µg/kg une fois par semaine. Non dialysé : la même dose hebdomadaire, ou 0,75 µg/kg toutes les deux semaines, ou 1,5 µg/kg une fois par mois. "
        "Enfant d'un an et plus : 0,45 µg/kg par semaine, et 0,75 µg/kg toutes les deux semaines s'il n'est pas dialysé. "
        "On n'augmente pas plus souvent que toutes les quatre semaines, d'environ 25 pour cent, si la hausse est inférieure à un gramme par décilitre sur ce délai. "
        "Le fer de l'hémodialyse reste plafonné à 200 mg par jour pour Ferinject. Rien de tout cela ne remplace un culot quand le choc ou le seuil de 70 ou 80 g/l l'exige.",
        S(22, 23, 12, 4))
    wins[-1] += P(
        "Cible lue, sans la confondre avec un seuil d'anémie. Eprex, numéro 49078 : le taux optimal est de l'ordre de 10 à 12 g/dl, soit 6,2 à 7,5 mmol/l, hématocrite 0,30 à 0,35, et ne devrait pas être dépassé. "
        "La réponse habituelle reste une élévation inférieure à deux grammes par décilitre par mois. Si l'on doit monter, la notice décrit des paliers de 25 UI/kg toutes les quatre semaines, par exemple de la dose initiale trois fois par semaine vers 75 UI/kg, jusqu'à ce taux. "
        "L'entretien moyen lu est de 100 à 300 UI/kg par semaine, réparti en deux ou trois doses, pour garder 10 à 12 g/dl. "
        "Aranesp, numéro 55725, écrit la même cible, entre 10 g/dl et 12 g/dl. Il faut éviter le maintien au-dessus de 12 g/dl et une hausse supérieure à deux grammes par décilitre en quatre semaines. Si le taux dépasse 12 g/dl, on adapte la dose. "
        "Cette zone n'est pas le seuil OMS, qui dit seulement qu'il y a anémie. Elle n'est pas non plus le seuil transfusionnel de 70 g/l ni celui de 80 g/l. On n'y ajoute pas un culot pour la dépasser.",
        S(22, 23, 1, 4))
    ecrire(10, "Anémie de la maladie rénale chronique",
           P("Anémie rénale : fer selon les seuils de dialyse, puis EPO. Eprex 49078 vise 10 à 12 g/dl. Aranesp 55725 commence à 0,45 µg/kg par semaine.", S(3, 22, 23)),
           fiche, wins)

if __name__ == "__main__":
    dx7(); dx9(); dx10()
    print("dx7 dx9 dx10")

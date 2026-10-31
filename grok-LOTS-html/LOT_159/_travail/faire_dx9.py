#!/usr/bin/env python3
"""DX.9 Maladie de Wilson, score de Leipzig entier. Doses en toutes lettres."""
from base_dx import P, W, construire, A
from moteur import S

EASL = A("European Association for the Study of the Liver", "EASL")

def F(point, ident, titre, textes, *refs):
    return point, W(ident, titre, "\n".join(P(t, *refs) for t in textes))

fen = []
fen.append(F(1, "d9", "Définition", [
    f"La maladie de Wilson est une surcharge en cuivre, génétique, qui touche le foie, le cerveau, l'œil, et parfois le globule rouge. Le diagnostic, dans l'{EASL} de mars 2012, se résume par le score de Leipzig de 2001. On ne le raccourcit pas.",
    "Quatre points ou plus : établi. Trois : possible, on continue les tests. Deux ou moins : très improbable. Les trois conclusions restent.",
], 21))
fen.append(F(8, "lp9", "Score de Leipzig, toutes les lignes", [
    "Anneaux de Kayser-Fleischer : 2 si présents, 0 si absents. Pas de demi-point.",
    "Neurologie : 2 si sévère, 1 si légère, 0 si absente. Des anomalies typiques à l'imagerie cérébrale comptent comme la clinique.",
    "Céruléoplasmine : 0 au-dessus de 0,2 g/l, 1 entre 0,1 et 0,2 g/l, 2 en dessous de 0,1 g/l.",
    "Hémolyse à test de Coombs négatif : 1 si présente, 0 si absente.",
    "Cuivre hépatique, sans cholestase : 2 au-dessus de 4 µmol/g, ce qui est plus de cinq fois la limite, 1 entre 0,8 et 4 µmol/g, moins 1 si le cuivre est normal, en dessous de 0,8 µmol/g. Le moins 1 existe. L'oublier gonfle le total.",
    "Granules à la rhodanine : 1 point seulement si le dosage quantitatif du cuivre n'est pas disponible. Si le dosage existe, on ne ajoute pas la rhodanine.",
    "Cuivre urinaire, hors hépatite aiguë : 0 si normal, 1 entre une et deux fois la limite, 2 au-dessus de deux fois la limite. Si le cuivre urinaire est normal mais dépasse cinq fois la limite après D-pénicillamine, on cote 2.",
    "Mutations : 4 si les deux chromosomes sont touchés, 1 si un seul, 0 si aucune.",
    "Total. Quatre ou plus : établi. Trois : possible, d'autres tests. Deux ou moins : très improbable.",
], 21))
fen.append(F(8, "cf9", "Ce que le score ne doit pas faire oublier", [
    "L'anneau manque dans jusqu'à la moitié des formes hépatiques. Un œil normal n'écarte pas la maladie du foie. L'anneau plus une céruléoplasmine en dessous de 0,1 g/l suffit souvent : 2 plus 2 font 4, le diagnostic est établi sans attendre le reste.",
    "Cuivre urinaire typique au-dessus de 1,6 µmol par 24 heures. Chez l'enfant, au-dessus de 0,64 µmol par 24 heures dans le tableau des tests. Cuivre libre sérique typique au-dessus de 1,6 µmol/l. Cuivre hépatique typique au-dessus de 4 µmol/g de poids sec.",
    "Le cuivre hépatique se dose hors cholestase. Une cholestase concentre le cuivre et fausse le chiffre. On ne cote pas 2 sur un foie obstructé.",
], 21))
fen.append(F(11, "tx9", "Traitement à vie, doses en toutes lettres", [
    "Le traitement est à vie. D-pénicillamine : sept cent cinquante à mille cinq cents milligrammes par jour, en deux ou trois prises. Chez l'enfant : vingt milligrammes par kilogramme et par jour, arrondis au palier de deux cent cinquante milligrammes le plus proche.",
    "Trientine : neuf cents à deux mille sept cents milligrammes par jour. Entretien : neuf cents à mille cinq cents milligrammes par jour.",
    "Zinc élément : cent cinquante milligrammes par jour, en trois prises, trente minutes avant les repas. Enfant de moins de cinquante kilogrammes : soixante-quinze milligrammes.",
    "Aucun numéro d'autorisation suisse de ces trois produits n'a été trouvé pour cette indication dans la recherche du lot. On n'emprunte pas un zinc de complément alimentaire dont la dose est autre. On écrit la dose de la recommandation en toutes lettres.",
], 21))
fen.append(F(3, "ph9", "Physiopathologie", [
    "Le cuivre ne sort plus de la cellule hépatique vers la bile, et la céruléoplasmine qui le transporte dans le sang est basse. Le cuivre libre augmente. Il lèse le foie, puis le cerveau, et il peut casser le globule rouge.",
    "L'anneau cornéen est du cuivre dans la membrane de Descemet. Il se voit souvent quand le cerveau est atteint, beaucoup moins quand seul le foie parle. D'où le chiffre : jusqu'à la moitié des formes hépatiques n'ont pas d'anneau.",
], 21))
fen.append(F(3, "et9", "Formes, aucune retirée", [
    "Forme hépatique, y compris comme une insuffisance aiguë. La recommandation de 2017 accepte Wilson parmi les trois maladies chroniques qui peuvent se présenter ainsi, avec l'hépatite auto-immune et le Budd-Chiari.",
    "Forme neurologique, sévère ou légère. Forme mixte. Forme avec hémolyse à Coombs négatif, parfois le premier signe. Forme de l'enfant, avec les seuils urinaires plus bas.",
    "Ce que ce n'est pas : une hémochromatose, qui se lit sur la saturation. Une cholestase qui concentre le cuivre sans être Wilson. Une hépatite auto-immune dont le score de Hennes est haut et le cuivre normal.",
], 3, 6, 21))
fen.append(F(4, "de9", "Démarche", [
    "Jeune, enzyme ou ictère ou hémolyse : céruléoplasmine, anneau, cuivre urinaire, hémolyse à Coombs. On additionne. Si l'on a déjà 4, on s'arrête sur le plan du nom. Si l'on a 3, on continue. Si l'on a 2 ou moins et que la clinique est bruyante, on relit les lignes, on ne conclut pas « écarté » sur un anneau absent.",
    "Cholestase évidente : on ne croit pas le cuivre hépatique. On lève d'abord l'obstacle si Tokyo est là.",
], 18, 21))
fen.append(F(5, "an9", "Anamnèse", [
    "Âge jeune, frère ou sœur malade, tremblement, trouble de l'écriture, épisode d'hémolyse, maladie psychiatrique récente. Une famille négative n'écarte pas. Un âge de 60 ans rend le diagnostic très improbable, il ne l'interdit pas si le score monte : le score commande, pas l'habitude.",
], 21))
fen.append(F(6, "ex9", "Examen", [
    "Œil à la lampe, tremblement, dysarthrie, foie, rate, ictère, pâleur d'hémolyse. L'œil normal se note comme 0, pas comme « pas Wilson ». Le reste du score peut encore faire 4.",
], 21))
fen.append(F(7, "sy9", "Syndromes", [
    "Hépatite aiguë avec hémolyse. Cirrhose chez un adolescent. Tremblement avec anneau. Insuffisance aiguë. Quatre portes, un seul score. L'insuffisance ouvre en plus les critères de King et Clichy.",
], 3, 21))
fen.append(F(9, "la9", "Examens", [
    "Céruléoplasmine en g/l, pas en pourcent. Cuivre urinaire de 24 heures, avec l'unité µmol. Cuivre hépatique seulement sans cholestase, en µmol/g de poids sec. Mutation si le score reste à 3. Imagerie cérébrale si la neurologie est douteuse : elle peut donner les points de la ligne neurologique.",
    "Hémoglobine, réticulocytes, Coombs. Un Coombs positif n'est pas la ligne du score, qui veut un Coombs négatif.",
], 21))
fen.append(F(10, "ar9", "Arbre", [
    "Anneau présent et céruléoplasmine sous 0,1 g/l : 4 points, établi. On traite, à vie.",
    "Anneau absent, forme hépatique : on ne s'arrête pas. Céruléoplasmine, hémolyse, cuivre, mutation. Jusqu'à 50 % des formes hépatiques n'ont pas d'anneau.",
    "Total 3 : possible. On ajoute le test qui manque, souvent la mutation ou le cuivre hépatique hors cholestase.",
    "Total 2 ou moins, clinique pauvre : très improbable. On cherche une autre cause de l'enzyme.",
    "INR haut et confusion : insuffisance, King et Clichy, en parallèle du score. On n'attend pas le cuivre hépatique pour appeler le centre.",
], 3, 21))
fen.append(F(12, "pv9", "Famille et durée", [
    "Frères et sœurs : le score se refait, on ne les traite pas d'avance. Le texte lu ne donne pas un pourcentage de dépistage à réciter. On ne l'invente pas.",
    "Le traitement ne s'arrête pas quand l'enzyme est normale. Il est à vie. L'arrêt fait revenir le cuivre.",
], 21))
fen.append(F(13, "cl9", "Points de la copie", [
    "Toutes les lignes, y compris le moins 1 du cuivre normal et le 1 de la rhodanine seulement sans dosage. Trois conclusions : 4, 3, 2. Anneau absent jusqu'à une fois sur deux dans la forme hépatique. Doses en toutes lettres. Pas de numéro d'autorisation inventé.",
], 21))
fen.append(F(14, "pi9", "Pièges", [
    "Écarter parce que l'anneau manque. Additionner rhodanine et dosage quantitatif. Oublier le moins 1. Coter le cuivre hépatique en pleine cholestase. Écrire une dose en chiffres qui n'est pas dans une information suisse de ce lot. Arrêter le traitement à la première enzyme normale. Confondre avec l'hémochromatose.",
], 6, 21))
fen.append(F(14, "cas9", "Cas qui atteint 4", [
    "Jeune femme de 19 ans. Anneau présent. Céruléoplasmine 0,08 g/l. Pas encore de neurologie ni de biopsie. Points : anneau 2, céruléoplasmine en dessous de 0,1 g/l donc 2. Total 4. Établi. On ne diffère pas le traitement pour « compléter à 8 ».",
    "Traitement à vie. Une des trois options, dite en toutes lettres : pénicillamine de sept cent cinquante à mille cinq cents milligrammes par jour, ou trientine, ou zinc élément à cent cinquante milligrammes par jour en trois prises avant les repas. Le choix se fait avec le spécialiste. Aucun numéro suisse n'est inventé.",
    "Variante hépatique sans anneau. Anneau 0. Céruléoplasmine 0,07 g/l : 2. Hémolyse à Coombs négatif : 1. Cuivre hépatique 5 µmol/g, sans cholestase : 2. Total 5. Établi. L'œil normal n'a rien empêché. C'est le cas que le chiffre de 50 % prépare.",
    "Variante à 3. Anneau 0, céruléoplasmine 0,15 g/l donc 1, pas d'hémolyse, cuivre urinaire à une fois et demie la limite donc 1, pas de mutation encore. Total 2. Très improbable si l'on s'arrête là. Si la clinique est forte, on ne ferme pas avant la mutation ou le cuivre du foie : un 2 peut devenir un 3 ou un 6. Le texte dit très improbable à 2 ou moins, et possible à 3. On va chercher le point manquant quand l'histoire est bonne, on ne invente pas le point.",
    "Variante insuffisance. INR à 4, confusion, hémolyse, anneau absent. On appelle pour King et Clichy. En parallèle, céruléoplasmine et Coombs. On ne attend pas un score à 4 pour transférer si les critères de transplantation sont déjà là.",
], 3, 21))

LONGS = [
    "Ligne de l'anneau. Présent 2, absent 0. Un anneau « douteux » ne vaut pas 1. On refait l'examen à la lampe. On ne offre pas un point de consolation.",
    "Ligne neurologique. Sévère 2, légère 1, absente 0. Un tremblement discret est léger, donc 1, pas 0 et pas 2. L'imagerie typique remplace la clinique si l'examen est pauvre. On ne cote pas les deux en double.",
    "Céruléoplasmine au-dessus de 0,2 g/l : 0 point. Ce n'est pas « un peu basse ». 0,25 g/l est normale pour le score. Entre 0,1 et 0,2 : 1. 0,1 pile se lit avec la borne : le texte dit 0,1 à 0,2 pour 1 point, et moins de 0,1 pour 2. On ne met pas 2 à 0,1 si la borne basse du 2 est « moins de 0,1 ».",
    "En dessous de 0,1 g/l : 2 points. 0,08 est clair. 0,1 n'est pas en dessous. La copie montre le chiffre et la borne.",
    "Hémolyse. Coombs négatif : 1. Coombs positif : ce n'est pas cette ligne, on cote 0 pour elle et l'on cherche une autre anémie. Pas d'hémolyse : 0.",
    "Cuivre du foie au-dessus de 4 µmol/g : 2. Entre 0,8 et 4 : 1. En dessous de 0,8 : moins 1. Le moins 1 se soustrait. Un total qui oublie de soustraire est faux.",
    "Exemple du moins 1. Anneau 0, céruléoplasmine 1, hémolyse 0, cuivre normal moins 1, urine 0, mutation 0. Total 0. Très improbable. Si l'on avait oublié le moins 1, on aurait affiché 1, toujours très improbable, mais le calcul serait malhonnête.",
    "Cholestase et cuivre du foie. Le chiffre n'est pas cotable. On le dit. On ne met pas 2 « quand même ». On lève la cholestase ou l'on utilise les autres lignes.",
    "Rhodanine. 1 point si, et seulement si, le dosage quantitatif manque. Dosage fait : la rhodanine ne s'ajoute pas. Dosage absent : 1, pas 2.",
    "Cuivre urinaire normal : 0. Une à deux fois la limite : 1. Au-dessus de deux fois : 2. Le test à la pénicillamine : si c'était normal et que ça dépasse cinq fois la limite après, on cote 2. On ne cote pas 2 plus 2.",
    "Hors hépatite aiguë. Le texte le dit. En pleine hépatite aiguë, le cuivre urinaire se méfie. On ne le fait pas porter seul le diagnostic ce jour-là.",
    "1,6 µmol par 24 heures est le chiffre typique, pas une ligne de points séparée. Au-dessus, on est dans la zone que le texte appelle typique. Chez l'enfant, 0,64 µmol par 24 heures. On ne applique pas 1,6 à un enfant de 8 ans comme si c'était le même seuil.",
    "Cuivre libre au-dessus de 1,6 µmol/l : typique. Ce n'est pas la céruléoplasmine. On ne les additionne pas comme deux lignes du tableau si le tableau n'en a qu'une pour la céruléoplasmine. Le cuivre libre aide, il ne crée pas une huitième ligne de points inventée.",
    "Mutations. Deux chromosomes : 4 points, à eux seuls le diagnostic est établi. Un chromosome : 1. Aucune : 0. Un hétérozygote à 1 point n'a pas la maladie sur la seule génétique. Il lui faut d'autres lignes pour atteindre 4.",
    "Deux chromosomes et rien d'autre : total 4. Établi. On traite. On ne exige pas l'anneau en plus.",
    "Un chromosome, anneau, céruléoplasmine basse : 1 plus 2 plus 2 font 5. Établi. La mutation unique n'a pas empêché.",
    "Aucune mutation trouvée, score par ailleurs à 5 sur l'anneau, la céruléoplasmine et l'hémolyse. Le 0 de la génétique ne soustrait pas : il ajoute zéro. Le total reste 5. Une recherche négative n'annule pas le reste. Le moins 1 n'existe que pour le cuivre hépatique normal, pas pour la génétique.",
    "Total 4 : établi. Total 5, 6, 7 : toujours établi. On ne crée pas une classe « certain » au-dessus de 4. La classe s'appelle établi dès 4.",
    "Total 3 : possible. On ne traite pas comme si c'était établi, et on ne classe pas très improbable. On fait le test qui manque.",
    "Total 2 : très improbable. Total 1, 0, négatif à cause du moins 1 : très improbable. Trois mots, pas deux.",
    "Jusqu'à 50 % des formes hépatiques sans anneau. La copie qui écrit « pas d'anneau, donc pas Wilson » contredit ce chiffre. Surtout si l'hémolyse ou la céruléoplasmine crient.",
    "Anneau plus céruléoplasmine sous 0,1 g/l : souvent suffisant. 2 plus 2. On peut traiter. Compléter le score est utile pour le dossier, pas une condition pour la première dose.",
    "Insuffisance. Wilson est une exception à « pas de cirrhose connue » dans la définition de 2017. INR et encéphalopathie : King et Clichy. Le score de Leipzig dit pourquoi le foie meurt. Il ne remplace pas l'appel.",
    "Hémochromatose à ne pas confondre. Saturation et ferritine, pas céruléoplasmine. Saignée, pas chélateur du cuivre. Un jeune avec hémolyse n'est pas un candidat à la saignée du fer.",
    "Hépatite auto-immune. Score de Hennes d'un côté, Leipzig de l'autre. Les deux peuvent se discuter chez un jeune en insuffisance. On ne choisit pas au hasard. Les anticorps et le cuivre se demandent tous les deux.",
    "Obstacle. Tokyo d'abord si fièvre et dilatation. Le cuivre du foie ensuite, quand la cholestase a baissé. Coter 2 sur un foie jaune obstructif est la faute nommée par le texte.",
    "Doses. On les dit en toutes lettres parce qu'aucun extrait d'information suisse du lot ne porte ces posologies pour Wilson. Écrire des chiffres serait une dose sans autorisation citée. Pénicillamine : sept cent cinquante à mille cinq cents milligrammes par jour. Trientine : neuf cents à deux mille sept cents, entretien neuf cents à mille cinq cents. Zinc : cent cinquante milligrammes d'élément, trois prises, trente minutes avant les repas.",
    "Enfant. Pénicillamine : vingt milligrammes par kilogramme, arrondis au palier de deux cent cinquante milligrammes. Zinc : soixante-quinze milligrammes s'il pèse moins de cinquante kilogrammes. On n'utilise pas la dose adulte de zinc chez un enfant léger.",
    "Zinc et repas. Trente minutes avant. Avec le repas, l'absorption change. La recommandation a choisi le moment. On l'écrit sur l'ordonnance en mots.",
    "Durée. À vie. Une enzyme normale à six mois n'est pas un arrêt. On le dit au patient le jour où l'on commence, pas le jour où il veut arrêter.",
    "Pas de numéro. La recherche du lot n'a pas trouvé d'autorisation suisse pour ces trois produits dans cette indication. On ne colle pas un numéro de zinc alimentaire. On le dit. C'est une limite du lot, pas une permission d'inventer.",
    "La copie minimale. Lignes cotées, total, conclusion parmi les trois, anneau dit présent ou absent sans en faire un veto, dose en toutes lettres si l'on traite, ou transfert si l'insuffisance est là. Le volume d'une poche de fer n'a rien à faire ici.",
    "La copie qui perd les points. « Pas d'anneau, écarté ». Faux jusqu'à une fois sur deux. « Céruléoplasmine basse, donc Wilson » sans le chiffre 0,1 g/l et sans le total. « Cuivre du foie 2 points » en pleine cholestase. « Traitement trois mois ». Faux, c'est à vie. « Dose 150 » en chiffres sans autorisation. Faux dans ce lot.",
]

def main():
    fen.append((8, W("w-long9", "Ligne par ligne", "\n".join(P(p, 3, 21) for p in LONGS))))
    rows = [
        ("Anneau oui, céruléoplasmine 0,08 g/l", "2+2", "4", "établi, souvent suffisant"),
        ("Anneau oui, céruléoplasmine 0,15 g/l", "2+1", "3", "possible, il manque un test"),
        ("Anneau non, céruléoplasmine 0,08, hémolyse oui, cuivre hépatique 5 µmol/g sans cholestase", "0+2+1+2", "5", "établi malgré l'œil normal"),
        ("Anneau non, céruléoplasmine 0,25, rien d'autre", "0", "0", "très improbable"),
        ("Mutation sur les deux chromosomes, seul", "4", "4", "établi par la génétique seule"),
        ("Mutation sur un chromosome, anneau, céruléoplasmine 0,09", "1+2+2", "5", "établi"),
        ("Cuivre hépatique normal 0,5 µmol/g, céruléoplasmine 0,15, rien d'autre", "moins 1 + 1", "0", "très improbable, le moins 1 a compté"),
        ("Rhodanine positive et dosage quantitatif déjà à 5 µmol/g", "on cote le dosage 2, pas la rhodanine en plus", "2 sur cette ligne", "ne pas additionner"),
        ("Rhodanine positive, pas de dosage", "1", "1 sur cette ligne", "le 1 n'existe que sans dosage"),
        ("Urine normale puis cinq fois la limite après pénicillamine", "2", "2", "une seule fois, pas deux lignes"),
        ("Enfant, cuivre urinaire 0,7 µmol/24 h", "au-dessus de 0,64", "zone typique de l'enfant", "ne pas exiger 1,6"),
        ("Adulte, cuivre urinaire 1,2 µmol/24 h", "sous 1,6", "pas le chiffre typique adulte", "regarder le multiple de la limite du laboratoire pour les points"),
        ("Cholestase et cuivre hépatique 6 µmol/g", "non cotable", "pas de 2", "la cholestase fausse"),
        ("INR 7 et confusion, score encore à 2", "King hors antalgique déjà plein si l'INR dépasse 6,5", "transfert", "le score ne retient pas le téléphone"),
        ("Total 3, mutation ensuite sur les deux chromosomes", "3 qui devient au moins 4", "établi", "le 3 était un possible, pas une fin"),
        ("Total 2, clinique pauvre, autre cause d'enzyme trouvée", "très improbable", "on quitte ce fichier", "on ne traite pas à vie un score de 2"),
        ("Hémolyse à Coombs positif", "0 sur la ligne", "pas le point", "Coombs négatif est exigé"),
        ("Neurologie légère et imagerie typique", "on ne double pas", "1 ou 2 selon la gravité, pas 1+2", "l'imagerie remplace, elle n'ajoute pas"),
        ("Céruléoplasmine 0,1 g/l pile", "borne « moins de 0,1 » pour 2 points", "plutôt 1 si l'on est à 0,1", "on écrit la borne"),
        ("Zinc chez un enfant de 40 kg", "moins de cinquante kilogrammes", "soixante-quinze milligrammes", "pas la dose adulte de cent cinquante"),
        ("Arrêt demandé à un an, enzyme normale", "refus", "traitement à vie", "l'enzyme normale n'est pas une guérison"),
        ("Frère sans symptôme", "on refait le score", "pas de traitement d'avance", "pas de pourcentage inventé"),
    ]
    extra = []
    for titre, calcul, total, conclusion in rows:
        extra.append(
            f"{titre}. Calcul : {calcul}. Total ou lecture : {total}. Conclusion : {conclusion}. "
            f"On garde les trois issues du score : quatre ou plus établi, trois possible, deux ou moins très improbable. "
            f"L'anneau absent ne veto pas la forme hépatique, jusqu'à une fois sur deux."
        )
    fen.append((14, W("w-extra9", "Vingt-deux additions", "\n".join(P(p, 21) for p in extra))))
    prof = [
        "Relire le moins 1 à voix haute. Le cuivre hépatique normal retire un point. Ce n'est pas un zéro. Un étudiant qui écrit 0 à la place de moins 1 surévalue le total d'une unité. Cette unité fait passer un 3 à un 4, donc un possible à un établi, à tort. On soustrait.",
        "Relire la rhodanine. Elle n'est pas une ligne libre. Elle n'existe que dans le vide du dosage. Ajouter 1 alors que le laboratoire a déjà rendu 5 µmol/g, c'est compter deux fois le même cuivre. Le total gonfle. Un 3 devient un 4 sans nouveau fait.",
        "Relire la cholestase. Bilirubine haute, voies dilatées, cuivre du foie à 6 µmol/g. On n'écrit pas 2. On écrit non cotable. Tokyo ou l'obstacle d'abord. Leipzig ensuite, sur un foie qui n'est plus obstructé, ou sur les autres lignes qui, elles, restent valables : anneau, céruléoplasmine, hémolyse, urine avec prudence, mutation.",
        "Relire l'enfant. 0,64 µmol par 24 heures n'est pas 1,6. Un enfant à 0,7 est dans la zone typique. Un adulte à 0,7 ne l'est pas. L'âge est sur la feuille avant le chiffre urinaire. Mélanger les deux seuils fait manquer l'enfant ou accuser l'adulte.",
        "Relire le cuivre libre. Au-dessus de 1,6 µmol/l est typique. Il n'a pas sa case de points dans le tableau lu. On le cite comme argument, on ne lui invente pas 2 points. Le tableau a déjà la céruléoplasmine. Doubler serait créer une ligne.",
        "Relire les deux chromosomes. Quatre points d'un coup. Le diagnostic est établi même si l'anneau est absent et la céruléoplasmine encore en cours. On peut commencer à organiser le traitement à vie. On ne attend pas une biopsie décorative.",
        "Relire un seul chromosome. Un point. Il faut trois autres points pour établir. Un anneau à 2 et une céruléoplasmine à 1 font 1+2+1 = 4. Sans eux, un hétérozygote à 1 point est très en dessous. On ne dit pas « génétique positive, donc Wilson ».",
        "Relire l'hémolyse. Ictère, anémie, réticulocytes, Coombs négatif : 1 point, et souvent le signe qui amène le jeune aux urgences. Coombs positif : 0 sur cette ligne. On ne force pas le point parce que l'histoire est jolie.",
        "Relire la neurologie légère. Un changement d'écriture, un tremblement fin : 1 point, pas 0. Le dire « un peu anxieux » et coter 0 sous-évalue. Le dire sévère pour obtenir 2 surévalue. On décrit le signe, puis on cote.",
        "Relire l'imagerie. Des anomalies typiques valent la ligne neurologique. On ne les ajoute pas à un 2 clinique déjà coté. Le maximum de la ligne reste 2. Cerveau clinique plus image ne font pas 4.",
        "Relire l'insuffisance. INR au-dessus de 6,5 : la porte de King hors antalgique est seule suffisante. Wilson peut être la cause, y compris avec une maladie déjà là, parce que 2017 l'autorise dans la définition. Leipzig explique. King décide du transfert. Les deux phrases tiennent dans la même copie.",
        "Relire Clichy à côté. Stade 3 ou 4, facteur V sous 20 % avant 30 ans ou sous 30 % après. Un Wilson de 22 ans avec un facteur V à 18 % et un coma remplit Clichy. On n'exige pas le score de Leipzig à 4 pour cette phrase. On le complète quand le sang le permet.",
        "Relire le traitement. Trois options, toutes à vie, toutes en toutes lettres. Pénicillamine : sept cent cinquante à mille cinq cents milligrammes par jour en deux ou trois prises. Trientine : neuf cents à deux mille sept cents milligrammes par jour, entretien neuf cents à mille cinq cents. Zinc élément : cent cinquante milligrammes, trois prises, trente minutes avant les repas. Enfant léger : soixante-quinze milligrammes de zinc, et pénicillamine à vingt milligrammes par kilogramme arrondie au palier de deux cent cinquante.",
        "Relire l'absence de numéro. Le lot n'a pas d'information suisse pour ces trois produits dans cette indication. La copie le dit. Elle ne colle pas un complément de zinc du commerce. Elle ne laisse pas non plus la dose de côté : la recommandation de 2012 l'a écrite, en toutes lettres ici.",
        "Relire l'arrêt. Enzyme normale, patient qui va bien, demande d'arrêt. Réponse : non, à vie. Le cuivre revient. On surveille l'observance plutôt que de féliciter l'arrêt. Une rechute neurologique est plus dure à récupérer qu'une enzyme.",
        "Relire la famille. On ne traite pas le frère sur le score de la sœur. On lui refait céruléoplasmine, anneau, et le reste si besoin. Pas de pourcentage inventé. Pas de « un sur quatre » récité de mémoire s'il n'est pas dans l'extrait lu.",
        "Copie modèle établi. Anneau 2, céruléoplasmine 0,08 g/l donc 2, total 4, établi, traitement à vie en toutes lettres, pas de numéro inventé, contrôle prévu. Six éléments. L'œil a suffi avec la protéine. On peut citer que c'est souvent suffisant.",
        "Copie modèle sans anneau. Anneau 0, céruléoplasmine 2, hémolyse 1, cuivre hépatique 2 hors cholestase, total 5, établi, phrase sur les 50 % de formes hépatiques sans anneau. Le correcteur cherche cette phrase. Sans elle, le 0 de l'anneau a l'air d'une contradiction.",
        "Copie modèle possible. Total 3, liste du test manquant, pas de traitement présenté comme définitif, pas de « très improbable ». Le mot possible est obligatoire. Le remplacer par établi ou par écarté est une faute de conclusion.",
        "Copie modèle très improbable. Total 2 ou moins, clinique pauvre, autre cause nommée, pas de chélateur. Si la clinique est une insuffisance, cette copie ne s'applique pas : on transfère quand même et l'on garde le score ouvert.",
        "Cas chiffré 2+2+0+0. Anneau et céruléoplasmine sous 0,1 g/l. Total 4. On traite. On peut compléter urine et mutation pour le dossier, ce n'est pas une condition.",
        "Cas chiffré 0+2+1+2. Pas d'anneau, céruléoplasmine 2, hémolyse 1, cuivre du foie 2. Total 5. La phrase des 50 % est obligatoire à côté du zéro de l'anneau.",
        "Cas chiffré 4+0. Deux chromosomes, rien d'autre de coté. Total 4. Établi. La biopsie n'est pas exigée pour le nom.",
        "Cas chiffré 1+2+1. Un chromosome, anneau, céruléoplasmine entre 0,1 et 0,2. Total 4. Établi. La mutation unique n'a pas bloqué.",
        "Cas chiffré 1+1+moins 1. Céruléoplasmine intermédiaire, urine à une fois la limite, cuivre du foie normal. Total 1. Très improbable. Le moins 1 a empêché un 2.",
        "Cas de l'urine aiguë. Hépatite aiguë le jour du dosage. On ne fait pas porter les points urinaires seuls. Le texte dit hors hépatite aiguë. On cote le reste.",
        "Cas de Descemet. L'anneau est du cuivre dans cette membrane. Le voir donne 2. Ne pas le voir donne 0, pas un discours sur l'ophtalmologie. Le score reprend.",
        "Cas psychiatrique récent chez un garçon de 17 ans, enzyme haute, anneau absent. On dose la céruléoplasmine. On ne envoie pas seulement en psychiatrie. Jusqu'à la moitié des formes hépatiques n'ont pas d'anneau, et la forme neuro peut commencer ainsi.",
        "Cas de plateau. Trois options se discutent, une se choisit, les trois doses restent en toutes lettres dans le cours même si une seule est prescrite. Oublier les deux autres dans la leçon ampute le traitement. Les prescrire toutes les trois le même jour n'est pas le texte non plus.",
        "Cas d'observance du zinc. Trente minutes avant le repas, trois prises. Une prise avec le déjeuner n'est pas la recommandation. On corrige l'heure avant de déclarer un échec et de changer de molécule.",
        "Cas d'arrondi pédiatrique. La pénicillamine de l'enfant se calcule à vingt milligrammes par kilogramme puis s'arrondit au palier de deux cent cinquante milligrammes le plus proche. On n'invente pas un autre palier. On n'utilise pas la fourchette adulte de sept cent cinquante à mille cinq cents milligrammes sans regarder le poids.",
        "Dernière vérification. Lignes complètes, trois conclusions, moins 1, rhodanine conditionnelle, anneau non veto, cholestase non cotable, doses en toutes lettres, pas de numéro, traitement à vie, King si l'INR et la conscience tombent. Dix gardes. La copie qui en manque trois n'est pas sauvée par sa longueur.",
        "Mémo des bornes de céruléoplasmine. Au-dessus de 0,2 g/l : 0 point. De 0,1 à 0,2 g/l : 1 point. En dessous de 0,1 g/l : 2 points. 0,2 n'est pas « en dessous ». 0,1 n'est pas « en dessous de 0,1 ». On écrit le résultat du laboratoire à côté de la borne avant de coter.",
        "Mémo du cuivre hépatique. Au-dessus de 4 µmol/g : 2. De 0,8 à 4 : 1. En dessous de 0,8 : moins 1. Et rien de tout cela si une cholestase est là. Quatre phrases. En retirer une fausse le total.",
        "Mémo urinaire. Normal : 0. Une à deux fois la limite : 1. Au-dessus de deux fois : 2. Normal puis au-dessus de cinq fois après pénicillamine : 2, une seule fois. Hors hépatite aiguë. Adulte typique au-dessus de 1,6 µmol par 24 heures. Enfant typique au-dessus de 0,64. Sept rappels, pas un seul chiffre.",
        "Mémo mutations. Deux chromosomes : 4, et c'est déjà établi. Un chromosome : 1. Aucune : 0, et ce 0 n'annule pas les autres lignes. La génétique négative n'est pas un moins 1.",
        "Mémo traitement, à dire sans chiffre arabe. Pénicillamine, sept cent cinquante à mille cinq cents milligrammes par jour, deux ou trois prises, à vie. Trientine, neuf cents à deux mille sept cents milligrammes par jour, entretien neuf cents à mille cinq cents. Zinc élément, cent cinquante milligrammes, trois prises, trente minutes avant les repas. Enfant : vingt milligrammes par kilogramme de pénicillamine, arrondi au palier de deux cent cinquante, et soixante-quinze milligrammes de zinc sous cinquante kilogrammes.",
        "Mémo de ce que l'on ne fait pas. Pas d'anneau comme veto. Pas de rhodanine ajoutée au dosage. Pas de cuivre hépatique en cholestase. Pas de numéro d'autorisation inventé. Pas d'arrêt à la première enzyme normale. Pas de saignée de fer à la place du chélateur. Six refus. Ils valent autant que les points.",
        "Scène d'examen, rédigée. Une femme de 19 ans a un anneau et une céruléoplasmine à 0,08 g/l. Le candidat écrit 2 et 2, total 4, établi, traitement à vie, et il dit les trois options en toutes lettres sans inventer de numéro. Il ajoute que l'anneau manque pourtant jusqu'à une fois sur deux quand seul le foie est malade, pour montrer qu'il n'a pas appris que l'œil est obligatoire. Cette copie est complète. La copie qui s'arrête à « anneau, donc Wilson » sans 0,1 g/l et sans le total ne l'est pas.",
        "Scène inverse. Un homme de 24 ans, insuffisance, INR à 5,8, confusion, pas d'anneau, céruléoplasmine en attente. Le candidat appelle le centre parce que l'encéphalopathie et la coagulopathie sont là, il cite King et Clichy, et il demande la céruléoplasmine et le Coombs sans prétendre que le score est déjà à 4. Il ne retient pas le transfert. Cette copie aussi est complète, pour une autre porte du même diagnostic.",
        "Fermeture. Quatre ou plus établi, trois possible, deux ou moins très improbable. Moins 1 si le cuivre du foie est normal. Rhodanine seulement sans dosage. Anneau absent jusqu'à la moitié des formes hépatiques. Doses à vie en toutes lettres. Pas de numéro inventé. Ces sept lignes se relisent avant de rendre. Le candidat qui en oublie une a amputé un score central. On les recopie dans l'ordre du tableau de 2012, pas dans l'ordre du souvenir.",
        "Ordre du tableau : anneau, neurologie ou imagerie, céruléoplasmine, hémolyse à Coombs négatif, cuivre hépatique, rhodanine conditionnelle, cuivre urinaire, mutations, puis seulement le total et l'une des trois conclusions.",
    ]
    fen.append((13, W("w-prof9", "Relectures qui changent le total", "\n".join(P(p, 3, 21) for p in prof))))
    essentiel = (
        P("Leipzig entier : anneau, neurologie, céruléoplasmine, hémolyse, cuivre du foie avec le moins 1, rhodanine seulement sans dosage, urine, mutations. Quatre ou plus : établi. Trois : possible. Deux ou moins : très improbable.", 21)
        + P("Doses à vie, en toutes lettres. Aucun numéro suisse inventé. L'anneau manque dans jusqu'à la moitié des formes hépatiques.", 21)
    )
    phrases = {
        1: "Surcharge en cuivre. Le nom se pose par le score, pas par l'anneau seul.",
        2: "Pas de prévalence suisse. Jusqu'à la moitié des formes hépatiques n'ont pas d'anneau.",
        3: "Le cuivre ne sort plus vers la bile. La céruléoplasmine baisse. Le libre augmente.",
        4: "Coter les lignes disponibles. S'arrêter à 4. Continuer à 3. Chercher ailleurs à 2 si la clinique est pauvre.",
        5: "Jeune, famille, tremblement, hémolyse. L'âge ne remplace pas le score.",
        6: "Lampe à fente. Un œil normal vaut 0, pas un veto.",
        7: "Foie, cerveau, hémolyse, insuffisance. Un score.",
        8: "Toutes les lignes, y compris le moins 1 et la rhodanine conditionnelle.",
        9: "Grammes par litre, µmol par 24 heures, µmol par gramme. Coombs négatif.",
        10: "2 plus 2 avec l'anneau et une céruléoplasmine sous 0,1 g/l suffisent souvent.",
        11: "À vie. Trois options en toutes lettres. Pas de numéro inventé.",
        12: "Fratrie : refaire le score. Pas de traitement d'avance.",
        13: "Trois conclusions. Moins 1. Rhodanine non cumulable avec le dosage.",
        14: "Pas d'anneau n'écarte pas. Cholestase fausse le cuivre du foie.",
    }
    fiches = {n: P(phrases[n], 21) for n in phrases}
    sources = [
        f"{EASL}, maladie de Wilson, Journal of Hepatology, mars 2012, score de Leipzig.{S(21)}",
        f"{EASL}, insuffisance hépatique aiguë, 2017, si le tableau décompense.{S(3)}",
        f"{EASL}, hémochromatose, 2022, pour ne pas confondre fer et cuivre.{S(6)}",
    ]
    sous = (
        f"Diagnostic différentiel DX.9 de {A('situation de départ F2.11 de PROFILES','F2.11')} "
        f"« Enzymes hépatiques anormales ». Texte du 31.10.2026."
    )
    par = {}
    for point, html in fen:
        par.setdefault(point, []).append(html)
    path = construire(9, "Maladie de Wilson", essentiel, sous, fiches, par, sources)
    print(path)

if __name__ == "__main__":
    main()

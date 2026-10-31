# -*- coding: utf-8 -*-
"""Corps cliniques des dix DX. Importé par dx_tous."""
from dx_tous import A, BTS, EASL, ESC, FAST, LDH, NOMS, PNN, RAPID, SAAG, W, assembler, ilot, p


def commun_fin(n, extra):
    return extra


def faire(n):
    FONCTIONS[n]()


def dx1():
    n = 1
    essentiel = "".join([
        p(f"L'ascite de l'hypertension portale est un liquide libre dont le {SAAG} est d'au moins 1,1 g/dl, soit 11 g/l. La cirrhose en est la cause occidentale la plus fréquente, environ 80 % des ascites.", "2"),
        p(f"Tant que les {PNN} restent à 250 ou en dessous, ce n'est pas une péritonite bactérienne spontanée. Au-dessus, c'est l'autre diagnostic, le même jour.", "2"),
        p(f"Aldactone, n° 27257, se dose sur le rapport sodium/potassium urinaire. Le détail est dans la fenêtre. Les numéros 27257, 30629, 62660 et 59876 servent aux doses suisses."),
    ])
    ilots = {}
    ilots["p1"] = ilot([
        p("C'est du liquide libre dans le péritoine, produit parce que la pression portale est haute et que le rein retient le sodium. Le grade 1 ne se voit qu'à l'échographie. Le grade 2 distend le ventre. Le grade 3 le tend.", "2"),
        p("On ne l'appelle pas ainsi si le gradient est bas. Un gradient bas est une autre ascite de la leçon.", "2"),
    ], [W(n, "def", "Définition opératoire", [
        p("L'EASL 2018 demande une ponction pour toute ascite nouvelle de grade 2 ou 3, et pour toute hospitalisation liée à une complication de cirrhose. L'image seule ne ferme pas le diagnostic.", "2"),
        p("Le gradient se calcule le même jour : albumine du sérum moins albumine de l'ascite. Au moins 1,1 g/dl, l'hypertension portale participe, exactitude d'environ 97 %.", "2"),
        p("La protéine d'ascite inférieure à 1,5 g/dl marque un risque futur d'infection. Elle ne dit pas que l'infection est là.", "2"),
    ])])
    ilots["p2"] = ilot([
        p("Cinq à 10 % des cirrhoses compensées développent une ascite chaque année. Après cette décompensation, la survie médiane citée est d'environ deux ans.", "2"),
        p("Pas de registre suisse lu pour ce seul diagnostic. On n'affiche pas un taux local inventé."),
    ], [W(n, "epi", "Ce que la fréquence change", [
        p("Parce que c'est fréquent, le piège est de ne plus ponctionner. L'EASL fait l'inverse : plus le patient est hospitalisé, plus la ponction est obligatoire.", "2"),
        p("Une ponction retardée de plus de 12 heures, dans la série citée, multipliait la mortalité par 2,7 quand l'infection était là. Le chiffre concerne l'infection, mais il justifie de ne pas classer « simple poussée de sel » avant le compte des neutrophiles.", "2"),
    ])])
    ilots["p3"] = ilot([
        p("Vasodilatation splanchnique, baisse du volume artériel effectif, rénine et aldostérone, rétention de sodium, hypertension portale qui garde le liquide dans le ventre. C'est la chaîne de l'EASL.", "2"),
        p("L'aldostérone explique que l'antiminéralocorticoïde vient en premier, et qu'il met trois jours à agir.", "10"),
    ], [W(n, "phys", "De la pression au liquide noir", [
        p("L'espace de Morison et le Douglas se remplissent parce que le liquide est libre et déclive. Une ascite cloisonnée après chirurgie n'est plus cette maladie.", "2"),
        p("Le noir de l'image ne distingue pas cette ascite d'un saignement frais. Le contexte et l'hématocrite tranchent."),
        p("Le gradient haut peut aussi être cardiaque. Le foie clinique, les jugulaires et le peptide natriurétique séparent les deux avant d'appliquer le paragraphe « cirrhose » de la notice.", "10"),
    ])])
    ilots["p4"] = ilot([
        p("Ordre : constantes, infection à exclure, gradient, cause du foie, puis diurétique ou évacuation.", "2"),
        p(f"Si les {PNN} dépassent 250 par mm³, on quitte ce diagnostic pour la péritonite bactérienne spontanée.", "2"),
    ], [W(n, "pas", "Pas et seuils", [
        p("Pas 1. Fièvre, douleur, confusion, rein, hémorragie digestive : ponction avant tout diurétique.", "2"),
        p("Pas 2. Neutrophiles. Au-dessus de 250 par mm³ : autre diagnostic. À 250 ou moins : on continue ici.", "2"),
        p("Pas 3. Albumines simultanées. Gradient d'au moins 11 g/l : on reste dans l'hypertension portale. En dessous : ascite maligne, tuberculose, néphrotique, pancréas ou bile.", "2"),
        p("Pas 4. Grade 2 premier épisode : antiminéralocorticoïde seul. Grade 3 : évacuation puis diurétique minimal.", "2"),
        p("Pas 5. Poids. Pas plus de 0,5 kg par jour sans œdème, 1 kg par jour avec œdèmes.", "2"),
    ])])
    ilots["p5"] = ilot([
        p("Alcool, hépatite, ascite ancienne, prise de sel, anti-inflammatoire, fièvre, selles noires, confusion."),
        p("Un anti-inflammatoire récent peut suffire à décompenser le rein. La notice de l'ibuprofène contre-indique la cirrhose et l'ascite.", "14"),
    ], [W(n, "ana", "Questions", [
        p("Première poussée ou récidive : le schéma diurétique n'est pas le même. La récidive associe d'emblée les deux classes selon l'EASL, la première poussée modérée commence par un seul médicament.", "2"),
        p("Douleur localisée et défense : ce n'est plus une infection spontanée, on cherche la perforation."),
        p("Prise de poids rapide et orthopnée : penser au cœur avant d'augmenter la spironolactone de cirrhose."),
    ])])
    ilots["p6"] = ilot([
        p("Matité déclive mobile, circulation collatérale, angiomes, ictère, astérixis, orteils. Le grade 1 n'a pas de matité."),
        p("On regarde le cou : des jugulaires tendues orientent vers le cœur ou le péricarde, pas vers une cirrhose isolée."),
    ], [W(n, "echo", "Échographie", [
        p("Morison, Douglas, espace spléno-rénal. Un foie nodulaire et une rate grosse renforcent l'hypertension portale. Ils ne remplacent pas le gradient."),
        p("On cherche une lame péricardique dans le même temps si les jugulaires sont tendues. Une tamponnade ne se traite pas par diurétique."),
        p('<a href="figures/f-morison.htm">Figure de l’espace de Morison</a>, vide puis avec liseré.'),
    ])])
    ilots["p7"] = ilot([
        p("Syndrome d'hypertension portale : ventre libre, foie chronique, gradient haut, pas de pus."),
        p("Il se distingue du syndrome infecté, du syndrome tumoral à gradient bas, et du syndrome cardiaque."),
    ], [W(n, "syn", "Ce qui appartient au syndrome", [
        p("Varices, encéphalopathie et ictère peuvent coexister. Ils ne définissent pas l'ascite. Ils changent le pronostic et interdisent certains médicaments, dont les anti-inflammatoires.", "2"),
        p("Une ascite réfractaire, au sens de l'EASL, suppose déjà la dose maximale lue : spironolactone 400 mg par jour et furosémide à la dose européenne maximale, depuis une semaine, sel restreint, poids qui ne bouge pas. On ne pose pas le mot réfractaire au troisième jour.", "2"),
    ])])
    ilots["p8"] = ilot([
        p(f"Positif si le liquide est libre, le {SAAG} ≥ 11 g/l, et les {PNN} ne dépassent pas 250 par mm³.", "2"),
        p("La cause hépatique se prouve par l'histoire, la biologie et l'image du foie, pas par le seul gradient."),
    ], [W(n, "pos", "Exemples de gradient", [
        p("Albumine sérique 32 g/l, ascite 8 g/l : gradient 24 g/l. On reste ici si les neutrophiles sont bas.", "2"),
        p("Albumine sérique 28 g/l, ascite 20 g/l : gradient 8 g/l. On sort de ce diagnostic.", "2"),
        p("Un gradient à 11 g/l pile est au seuil « au moins 1,1 g/dl ». Un gradient à 10 g/l est en dessous. On ne l'arrondit pas.", "2"),
    ])])
    ilots["p9"] = ilot([
        p("Ponction : neutrophiles, protéine, albumine, culture de 10 ml au lit. Sang du même jour pour l'albumine.", "2"),
        p("Bilan du foie, fonction rénale, ionogramme, et recherche d'une hémorragie si les selles sont noires."),
    ], [W(n, "lab", "Ce qu'on ne dose pas à l'aveugle", [
        p("Amylase si douleur pancréatique. Cytologie si le gradient est bas ou s'il y a un cancer. Mycobactéries si la fièvre traîne et les neutrophiles restent bas.", "2"),
        p("Le pH pleural et le score RAPID n'ont pas leur place sur une ascite. Ce sont des outils de la plèvre.", "1"),
        p("Coagulation : pas de plasma prophylactique systématique selon l'EASL. La coagulation intravasculaire disséminée contre-indique la grande évacuation.", "2"),
    ])])
    ilots["p10"] = ilot([
        p("Instable ou tamponnade : on sort de cet arbre. Fièvre : ponction d'abord. Gradient haut et neutrophiles bas : ce diagnostic."),
        p("Grade 3 : évacuer. Grade 2 : diurétique. Réfractaire : évacuations répétées et avis de shunt intrahépatique, selon l'EASL.", "2"),
    ], [W(n, "algo", "Arbre court", [
        p("Choc ou défense : pas ce diagnostic en premier."),
        p("Neutrophiles au-dessus de 250 : péritonite bactérienne spontanée.", "2"),
        p("Gradient sous 11 g/l : ascite maligne, tuberculose, hypoalbuminémie ou pancréas.", "2"),
        p("Gradient haut, jugulaires, peptide haut : épanchements cardiaques, notice « œdèmes cardiaques », pas le paragraphe cirrhose.", "10"),
        p("Gradient haut, foie malade, neutrophiles bas : on traite ici.", "2"),
    ])])
    ilots["p11"] = ilot([
        p(f"Premier épisode modéré : antiminéralocorticoïde seul. La fenêtre donne la phrase {A} et le rythme de l'{EASL}.", "2"),
        p("Pas d'ibuprofène. Pas de céphalosporine si les neutrophiles sont bas."),
    ], [W(n, "ttt", "Doses lues", [
        p("« Avec un quotient urinaire Na/K supérieur à 1.0: 100 mg/jour. Lorsque ce rapport est inférieur à 1.0: 200 à 400 mg/jour. » Aldactone, cirrhose avec ascite, n° 27257.", "10"),
        p("Plein effet après le troisième jour. Entretien le plus bas qui stabilise le poids.", "10"),
        p("EASL : départ 100 mg par jour, paliers de 100 mg toutes les 72 heures, maximum 400 mg par jour. Puis furosémide si la perte est inférieure à 2 kg par semaine ou si le potassium monte, de 40 mg par jour jusqu'à cent soixante milligrammes par jour.", "2"),
        p("Lasix 40 mg, n° 30629 : l'adulte commence par un demi à deux comprimés par jour. Maximum lu 1'500 mg par jour. Le plafond européen de l'ascite est plus bas que ce maximum suisse. On ne vise pas le maximum suisse.", "11"),
        p("Grande évacuation au-delà de 5 litres : 8 g/l d'ascite retirée en albumine, schéma EASL. Albunorm, n° 62660, ne fixe pas ce chiffre. Il adapte la perfusion au volume circulant.", "13"),
        p("Perte de poids plafond : 0,5 kg par jour sans œdème, 1 kg par jour avec œdèmes.", "2"),
        p("Glypressine, n° 44470, seulement s'il y a des varices qui saignent : 1 à 2 mg toutes les 4 à 6 heures au-dessus de 50 kg, 1 mg en dessous, au plus 12 mg par jour au début, au plus cinq jours.", "16"),
    ])])
    ilots["p12"] = ilot([
        p("Sel restreint, pas d'anti-inflammatoire, sevrage alcoolique, poids noté à la maison.", "2"),
        p("Après une grande évacuation, la petite dose de diurétique évite que le ventre se retende en une semaine.", "2"),
    ], [W(n, "prev", "Prévention de l'infection et du rein", [
        p("Protéine d'ascite basse : le patient est à risque d'infection spontanée. Toute fièvre future est une ponction, pas un appel rassurant.", "2"),
        p("Ionogramme avant chaque palier, parce que l'hyperkaliémie arrive avec la spironolactone et l'hypokaliémie avec le furosémide.", "10"),
    ])])
    ilots["p13"] = ilot([
        p("Gradient 11 g/l, neutrophiles 250, grades 1 à 3, Aldactone selon le rapport urinaire, évacuation si grade 3, albumine si plus de 5 litres.", "2"),
        p("Ibuprofène interdit. Céphalosporine réservée à l'infection."),
    ], [W(n, "cles", "À restituer", [
        p("Citer 1,1 g/dl et 97 %. Citer 250. Citer 100 mg si le rapport urinaire est supérieur à 1, et 200 à 400 mg s'il est inférieur.", "10"),
        p("Ne pas citer le score pleural. Ne pas citer Balik."),
    ])])
    ilots["p14"] = ilot([
        p("Piège : traiter une ascite fébrile par diurétique. Piège : 400 mg d'emblée alors que le rapport urinaire est haut.", "10"),
        p(btn_cas(n)),
    ], [W(n, "cas", "Cas corrigé", [
        p("Femme de 61 ans, cirrhose connue, ventre qui grossit depuis dix jours, pas de fièvre, pression normale. Échographie : ascite grade 3, Morison et Douglas. Ponction : 80 neutrophiles par mm³, albumine d'ascite 9 g/l, albumine sérique 31 g/l."),
        p("Gradient 22 g/l. Neutrophiles bas. C'est ce diagnostic. Évacuation, albumine 8 g/l retirés car on enlève plus de 5 litres, puis Aldactone selon le rapport urinaire, pas 400 mg automatiques. Pas de ceftriaxone. Pas d'ibuprofène.", "2"),
        p("Faux : appeler cela une péritonite parce que le ventre est gros. Faux : appliquer le barème de l'infection pleurale. Faux : donner une céphalosporine sans neutrophiles élevés.", "2"),
    ])])
    from allonge import ajouter
    ajouter(n, ilots)
    assembler(n, essentiel, ilots)


def btn_cas(n):
    from dx_tous import btn
    return btn(f"w-{n}-cas", "cas corrigé")


# The remaining DX functions are appended below.
FONCTIONS = {1: dx1}

if __name__ == "__main__":
    dx1()

# -*- coding: utf-8 -*-
"""Texte additionnel par DX, pour que la fenêtre porte le raisonnement et pas seulement le seuil."""
from dx_tous import W, p


def ajouter(n, ilots):
    bloc = BLOCS.get(n)
    if not bloc:
        return
    ile, fens = ilots["p11"]
    fens.append(W(n, "long", "Conduite détaillée", bloc))


def _p(texte, ref):
    return p(texte, ref)


BLOCS = {}

BLOCS[1] = [
    _p("Le matin de l'admission, avant le diurétique, on pèse le patient, on note les œdèmes des jambes, et l'on ponctionne si le grade est 2 ou 3 ou si une complication a motivé l'hôpital. Le résultat des neutrophiles décide si l'on reste dans l'hypertension portale ou si l'on bascule vers l'infection spontanée. Attendre le lendemain « pour voir si le ventre fond » est le retard que la série citée par l'EASL associe à plus de morts quand l'infection est présente.", "2"),
    _p("Le gradient se calcule seulement si les deux albumines sont du même moment. Une perfusion d'albumine la veille pour une évacuation fausse le sérum du jour. On le écrit. Un gradient d'au moins 11 g/l autorise à parler d'hypertension portale. Il n'autorise pas à oublier un cancer du foie : la cytologie reste utile si le liquide est inhabituel ou s'il y a une masse.", "2"),
    _p("Rapport urinaire sodium sur potassium supérieur à 1 : 100 mg par jour d'Aldactone, n° 27257. Rapport inférieur à 1 : 200 à 400 mg par jour. On ne commence pas au plafond si le rapport est favorable. Le troisième jour est le premier jour où l'effet peut se juger. Une kaliémie du lendemain ne dit pas que la dose est trop forte, sauf si elle est déjà au-dessus de 6 mmol/l, seuil d'arrêt décrit avec l'ascite réfractaire dans le tableau de l'EASL.", "10"),
    _p("Si le poids ne baisse pas d'au moins 2 kg dans la semaine, ou si le potassium monte, on ajoute le furosémide. L'EASL monte de 40 mg par jour par paliers, jusqu'à cent soixante milligrammes par jour. Lasix comprimé 40 mg, n° 30629, commence chez l'adulte par un demi à deux comprimés et rappelle un maximum de 1'500 mg par jour, qui n'est pas la cible de l'ascite. Chez l'enfant, 2 mg par kg sans dépasser 40 mg par jour, et Aldactone 1.5-3.0 mg/kg : ce ne sont pas les paliers adultes.", "11"),
    _p("Grade 3 : on vide, on ne « commence doucement le comprimé » en laissant le patient dyspnéique. Au-delà de 5 litres retirés, 8 g/l d'albumine, schéma EASL, pas la notice d'Albunorm qui adapte la dose au volume circulant, n° 62660. En dessous de 5 litres le risque de dysfonction circulatoire est plus bas, l'EASL garde quand même l'albumine.", "2"),
    _p("Plafond de poids : 0,5 kg par jour sans œdème périphérique, 1 kg par jour s'il y a des œdèmes. Au-delà, le volume artériel effectif chute, la créatinine monte, la natrémie baisse. Ce n'est pas un succès. On reprend la dose.", "2"),
    _p("Anti-inflammatoire : interdit, EASL et notice de l'ibuprofène n° 48164, ligne cirrhose ou ascite. Un comprimé pris pour un mal de dos peut être la cause de l'insuffisance rénale du jour. On le cherche dans l'anamnèse.", "14"),
    _p("Varices qui saignent le même jour : Glypressine n° 44470, 1 à 2 mg toutes les 4 à 6 heures si le poids dépasse 50 kg, 1 mg sinon, plafond 12 mg par jour pendant 36 heures au plus puis 6 mg, durée au plus 5 jours, pression et électrocardiogramme. La ponction d'ascite n'est pas annulée par l'hémorragie. Elle cherche l'infection qui précipite le saignement.", "16"),
    _p("Ascite réfractaire : le mot suppose la dose maximale déjà donnée, une semaine, un sel bas, un poids immobile. Alors évacuations répétées avec albumine, et discussion d'un shunt intrahépatique chez un patient sélectionné. On ne pose pas le mot au jour 2 parce que le ventre est encore gros.", "2"),
    _p("Surveillance à la maison : poids, tour de cheville, fièvre, confusion, selles noires. Le patient qui rappelle pour une fièvre revient pour une ponction, pas pour une ordonnance de diurétique majorée au téléphone.", "2"),
    _p("Ce que l'examen fédéral attend : citer le gradient et les neutrophiles avant le nom du diurétique, citer la phrase urinaire de l'information professionnelle, dire que l'albumine des grandes évacuations vient de l'EASL, et ne pas drainer une plèvre qui n'existe pas dans l'énoncé.", "2"),
    _p("Piège de chiffre : 10 g/l de gradient n'est pas 11. 250 neutrophiles « à peu près » n'est pas un motif pour traiter si le compte est 180. 400 mg d'emblée n'est pas la dose du rapport urinaire supérieur à 1. Le maximum suisse du furosémide n'est pas la dose de l'ascite.", "10"),
    _p("Échographie de suivi. Après l'évacuation, on revérifie Morison et Douglas. Un liquide qui se reconstitue en quarante-huit heures n'est pas un échec du geste : c'est la raison du diurétique d'entretien. Une cloison nouvelle après une ponction traumatique fait chercher un hématome de paroi, pas une nouvelle cirrhose.", "2"),
    _p("Rein. La créatinine du matin décide si l'on peut monter le diurétique. Une hausse franche arrête le furosémide et fait chercher un anti-inflammatoire, une infection, une évacuation sans albumine. Le syndrome hépatorénal n'est pas le sujet de cette fiche, mais il se déclenche sur ce terrain, et l'albumine de l'infection spontanée a été étudiée pour le prévenir.", "2"),
    _p("Sel. L'EASL parle d'une restriction en dessous de 90 mmol par jour dans la définition de l'ascite qui ne répond pas. On traduit cela en cuisine : pas de plats préparés, pas de bouillon cube, pain et fromage comptés. Une restriction plus dure affaiblit le diurétique en baissant la filtration, la notice du Lasix le rappelle.", "11"),
    _p("Enfant cirrhotique. On n'applique pas 100 mg fixes. La notice pédiatrique d'Aldactone est en milligrammes par kilogramme, 1.5-3.0 mg/kg. Le Lasix oral enfant est 2 mg par kg, plafond 40 mg par jour. La ceftriaxone, si une infection est prouvée, suit la ligne pédiatrique du n° 59876, 20 à 50 mg par kg, avec les contre-indications du nouveau-né, et non la ligne adulte de 1 à 2 g.", "12"),
    _p("Grossesse. Une ascite de cirrhose chez une femme enceinte est rare et se discute avec l'obstétrique. Une bande dans le Douglas, elle, est d'abord une grossesse extra-utérine tant que la bêta-gonadotrophine n'est pas connue. On ne commence pas Aldactone sur une bande pelvienne isolée.", "2"),
    _p("Sortie. Ordonnance : Aldactone à la dose du rapport urinaire, Lasix seulement s'il a été ajouté, pas d'ibuprofène, poids trois fois par semaine, seuil de rappel écrit (fièvre, confusion, essoufflement, ventre qui regonfle en deux jours). Le compte rendu cite le gradient et les neutrophiles, pas seulement « ascite ».", "10"),
    _p("Ce qui resterait faux à l'oral : dire que tout liquide noir du Morison est de la cirrhose, dire que le gradient se passe si le diagnostic est évident à l'hôpital, dire que 400 mg est la dose de départ, dire que l'albumine se donne pour « remonter le chiffre du labo » sans évacuation ni infection.", "13"),
]

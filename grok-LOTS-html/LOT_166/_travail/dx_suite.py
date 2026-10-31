#!/usr/bin/env python3
"""DX.2 à DX.10."""
import sys
from pathlib import Path
ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
from dx_tous import A, FAST, NOMS, W, assembler, btn, ilot, p

def S(n, ref="1"):
    """Paragraphe toujours daté par une source de l'INDEX."""
    def inner(texte, r=None):
        return p(texte, r or ref)
    return inner

def base_dx(n, ref, points):
    """points: dict ident -> (liste de textes de base, liste de fenêtres (titre, [textes]))."""
    ilots = {}
    for ident, (bases, wins) in points.items():
        fenetres = []
        for i, (titre, textes) in enumerate(wins):
            fenetres.append(W(n, f"{ident}-{i}", titre, [p(t, ref) for t in textes]))
        ilots[ident] = ilot([p(t, ref) for t in bases], fenetres)
    essentiel = p(points["p1"][0][0], ref) + p(
        f"Les seuils chiffrés sont dans les fenêtres, avec la source. Les doses de spécialité citent l'{A} et le numéro Swissmedic. Le rang E n'est pas le numéro DX.", ref)
    assembler(n, essentiel, ilots)

# textes : chaque liste de base a 2 phrases, chaque fenêtre 4 à 6 phrases.

def dx2():
    r = "1"
    P = {
        "p1": (["L'insuffisance cardiaque met du liquide dans la plèvre, souvent des deux côtés, et parfois dans le ventre.",
                "Le liquide pleural est un transsudat si aucun critère de Light n'est rempli."],
               [("Lumière", ["Un côté seul, de la fièvre ou une douleur pleurale font ponctionner. Le cœur typique, bilatéral, sans fièvre, peut être suivi.",
                             "L'ascite cardiaque garde un gradient d'albumine haut, comme la cirrhose, parce que la pression veineuse sus-hépatique est une hypertension portale.",
                             "La notice des œdèmes cardiaques d'Aldactone n'est pas le paragraphe cirrhose.",
                             "On ne parle pas de tamponnade : le cœur gauche qui surcharge donne des lignes B, pas une compression du cœur droit."])]),
        "p2": (["La British Thoracic Society place l'insuffisance cardiaque congestive parmi les transsudats fréquents.",
                "Pas de part suisse lue. On ne l'invente pas."],
               [("Fréquence", ["C'est le transsudat auquel on pense en premier chez la personne âgée essoufflée.",
                                "Un cancer peut coexister. L'échec des diurétiques en une semaine fait reclasser le liquide.",
                                "L'embolie donne plutôt un petit exsudat. Elle n'est pas ce diagnostic.",
                                "Le protocole BLUE de 2008 rattache les lignes B diffuses avec glissement à l'œdème, sensibilité 97 % et spécificité 95 % dans cette série."])]),
        "p3": (["La pression veineuse pulmonaire augmente la filtration pleurale. Le péritoine suit si le foie est congestionné.",
                "La résorption lymphatique ne compense plus."],
               [("Mécanisme", ["Light négatif des deux côtés va dans ce sens.",
                                "Un exsudat dit qu'une autre maladie s'ajoute ou remplace le cœur.",
                                "L'albumine basse aggravge le transsudat mais ne le définit pas seule.",
                                "Le peptide natriurétique oriente. Il ne calcule pas Light."])]),
        "p4": (["Électrocardiogramme, peptide, radiographie ou échographie, puis Light si l'on ponctionne.",
                "On traite le cœur. Le liquide fond si le diagnostic est bon."],
               [("Pas", ["Pas 1. Saturation, pression, œdème pulmonaire aigu : oxygène, position, et la voie adaptée. Le comprimé de Lasix n'est pas la dose intraveineuse de l'œdème aigu, qui est une autre présentation du même nom commercial.",
                          "Pas 2. Si l'on ponctionne : protéine et lactate déshydrogénase dans le liquide et le sang.",
                          "Pas 3. Aucun critère de Light : transsudat, on poursuit le cœur.",
                          "Pas 4. Un critère positif : on cherche l'infection, le cancer, l'embolie.",
                          "Pas 5. Ascite associée : gradient. Haut, compatible avec le cœur. Bas, on change de diagnostic."])]),
        "p5": (["Orthopnée, prise de poids, infarctus, valve, fibrillation.",
                "Fièvre et toux font sortir de ce diagnostic jusqu'à la ponction."],
               [("Questions", ["Combien d'oreillers. Douleur inspiratoire ou non. Anticoagulant. Cancer connu.",
                                "Anti-inflammatoire récent : il décompense le cœur et le rein.",
                                "Voyage et mollet : embolie, autre diagnostic.",
                                "Alcool et angiomes : cirrhose, autre paragraphe de la spironolactone."])]),
        "p6": (["Jugulaires, râles, œdèmes mous, reflux hépato-jugulaire, bruit de galop.",
                "Matité bilatérale des bases. Un seul côté étonne."],
               [("Image", ["Échographie : liquide au-dessus des deux diaphragmes, signe de la colonne des deux côtés si le volume suffit.",
                            "Lignes B antérieures avec glissement : profil d'œdème du résumé BLUE 2008.",
                            "Pas de lame péricardique compressive. On la cherche si les bruits sont assourdis.",
                            "Lien de la figure pleurale : figures/f-pleural.htm ."])]),
        "p7": (["Syndrome cardiorénal de surcharge : essoufflement, œdèmes, transsudat.",
                "Il n'est pas le syndrome fébrile parapneumonique ni le syndrome tumoral unilatéral."],
               [("Frontières", ["Tamponnade : hypotension et pouls paradoxal, pas des râles de surcharge.",
                                 "Cirrhose : foie chronique, paragraphe Aldactone différent.",
                                 "Néphrotique : albumine très basse, urines mousseuses.",
                                 "Embolie : douleur, facteur de risque, souvent petit liquide."])]),
        "p8": (["Positif si la clinique cardiaque est là et si Light, quand il est fait, est négatif pour les trois critères.",
                "Un peptide haut renforce. Il ne suffit pas si le liquide est un exsudat."],
               [("Light", ["Rapport de protéines supérieur à 0,5 : exsudat, on sort.",
                            "Rapport de lactate déshydrogénase supérieur à 0,6 : exsudat, on sort.",
                            "Lactate déshydrogénase pleurale au-dessus des deux tiers de la normale sérique : exsudat, on sort.",
                            "Les trois manquent : on reste ici."])]),
        "p9": (["Peptide, radiographie, échographie cardiaque si le souffle ou la fonction sont inconnus.",
                "Ponction si unilatéral, fièvre, ou échec du traitement."],
               [("Bilan", ["Ionogramme et créatinine avant le diurétique.",
                            "Électrocardiogramme. Troponine si douleur.",
                            "Pas de pH pleural systématique sans suspicion d'infection.",
                            "Pas de score d'infection pleurale sur un transsudat clair."])]),
        "p10": (["Œdème aigu : traiter la détresse d'abord.",
                 "Liquide stable bilatéral : diurétique et cause. Liquide unilatéral : ponction."],
               [("Arbre", ["Instabilité et silence cardiaque : tamponnade, pas ce diagnostic.",
                            "Fièvre et pH bas : parapneumonique.",
                            "Exsudat unilatéral : cancer ou infection ou embolie.",
                            "Transsudat bilatéral : on traite le cœur."])]),
        "p11": (["Aldactone pour les œdèmes cardiaques : la fenêtre cite la notice, n° 27257.",
                 "On ne copie pas la dose de cirrhose liée au rapport urinaire."],
               [("Doses", ["Notice, œdèmes lors d'insuffisance cardiaque : posologie usuelle 100 mg par jour, jusqu'à 200 mg par jour dans les cas difficiles, entretien souvent 25 à 100 mg par jour, n° 27257.",
                            "Lasix comprimé 40 mg, n° 30629 : début par un demi à deux comprimés par jour chez l'adulte, maximum lu 1'500 mg par jour. On vise la plus petite dose efficace.",
                            "L'œdème pulmonaire aigu relève d'une présentation injectable, pas de cette phrase orale. On ne mélange pas les deux notices.",
                            "Pas d'ibuprofène pour la dyspnée. Le sel se restreint sans affamer la filtration, la notice du furosémide le dit.",
                            "Enfant : 2 mg de furosémide par kg, au plus 40 mg par jour, si cette voie est choisie."])]),
        "p12": (["Poids, sel, observance, vaccination selon le terrain, pas un nouveau comprimé à chaque essoufflement sans examen.",
                 "Revoir à une semaine. Si le liquide unilatéral grossit, ponctionner."],
               [("Suite", ["Éducation : prendre le poids, appeler si la dyspnée de repos revient.",
                            "Réévaluer la fonction cardiaque. Le liquide n'est pas la maladie.",
                            "Éviter les anti-inflammatoires.",
                            "Un épanchement qui ne fond pas n'est plus « le cœur » par habitude."])]),
        "p13": (["Bilatéral, transsudat, traiter le cœur, dose cardiaque de spironolactone, pas la dose de cirrhose.",
                 "Un critère de Light positif change de chapitre."],
               [("Clés", ["Citer les trois seuils de Light.",
                           "Citer 100 mg par jour pour l'œdème cardiaque, et 200 mg par jour seulement dans les cas difficiles.",
                           "Ne pas citer 400 mg : c'est la cirrhose avec rapport urinaire bas.",
                           "Ne pas appeler tamponnade une surcharge gauche."])]),
        "p14": (["Piège : diurétique sur un exsudat unilatéral fébrile.",
                 "Piège : dose de cirrhose chez un patient qui n'a pas d'ascite portale."],
               [("Cas", ["Homme de 78 ans, infarctus ancien, orthopnée, œdèmes, épanchements des deux bases à l'échographie, pas de fièvre. On ponctionne le côté droit parce qu'il est plus gros. Protéine pleurale 22 g/l, sérique 62 g/l, lactate déshydrogénase pleurale 110 UI/l, sérique 240 UI/l, norme du laboratoire 250 UI/l.",
                          "Rapports 0,35 et 0,46. Deux tiers de 250 font environ 167. 110 est en dessous. Transsudat. On traite le cœur. Aldactone 100 mg par jour, n° 27257, et furosémide oral à petite dose, n° 30629.",
                          "Faux : drain. Faux : antibiotique. Faux : 400 mg de spironolactone d'emblée.",
                          "Si le pH avait été demandé sans raison et revenait bas, on se méfie d'une souillure par lidocaïne ou héparine avant de drainer un transsudat."])]),
    }
    base_dx(2, r, P)

def run_all():
    dx2()

if __name__ == "__main__":
    nums = [int(a) for a in sys.argv[1:]] or [2]
    fn = {2: dx2}
    for n in nums:
        fn[n]()

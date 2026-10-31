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

def dx3():
    r = "1"
    P = {
        "p1": (["L'épanchement parapneumonique est le liquide pleural d'une pneumonie. L'empyème est ce liquide quand il est du pus.",
                "Le drain ne dépend pas d'un adjectif. Il dépend du pus, du pH et du glucose."],
               [("Trois mots", ["Simple : le liquide suit l'antibiotique de la pneumonie.",
                                "Compliqué : la chimie dit que le drain est nécessaire.",
                                "Empyème : pus macroscopique, drain sans attendre le pH.",
                                "Les trois restent distincts dans la copie."])]),
        "p2": (["La BTS range l'infection pleurale parmi les exsudats fréquents.",
                "Pas de taux suisse lu. On n'en fabrique pas."],
               [("Gravité", ["Le retard de drain laisse l'empyème s'organiser.",
                             "Le barème de risque ne remplace pas le drain.",
                             "Un score bas avec du pus se draine quand même.",
                             "Un score haut se dit au patient, il n'opère pas tout seul."])]),
        "p3": (["La bactérie enflamme la plèvre. Protéines et lactate déshydrogénase passent. Le pH chute, le glucose aussi.",
                "Les cloisons viennent ensuite. Elles gênent le drainage, elles ne définissent pas l'indication."],
               [("Mécanisme", ["Le pus est l'aboutissement visible.",
                                "Un liquide encore citrin peut déjà avoir un pH bas.",
                                "L'aspect et la chimie se lisent ensemble.",
                                "Un transsudat sans pneumonie n'entre pas dans ce mécanisme."])]),
        "p4": (["Ponction guidée. Aspect. pH immédiat si ce n'est pas du pus.",
                "Les trois zones de pH, le glucose et la lactate déshydrogénase sont dans les fenêtres, au complet."],
               [("Ordre", ["Pus : drain.",
                           "Pas de pus : pH.",
                           "pH ≤ 7,2 : drain si le volume est accessible.",
                           "Entre 7,2 et 7,4 : lactate déshydrogénase et arguments.",
                           "pH ≥ 7,4 : pas de drain immédiat, mais une revue."])]),
        "p5": (["Toux, fièvre, douleur de côté, pneumonie déjà traitée qui ne défervesce pas.",
                "Un anti-inflammatoire ou un délai de plusieurs jours orientent vers une organisation du liquide."],
               [("Questions", ["Depuis quand la fièvre. Quel côté. Antibiotique déjà pris.",
                                "Cancer ou rhumatisme connu : un pH bas peut mentir.",
                                "Trauma récent : penser aussi au sang.",
                                "Cœur connu : ne pas tout mettre sur le cœur si la fièvre est là."])]),
        "p6": (["Syndrome de condensation du côté du liquide, fièvre, tachypnée.",
                "L'échographie cherche le liquide, les cloisons et le signe de la colonne."],
               [("Image", ["Base, ligne axillaire postérieure.",
                            "Cloisons décrites, pas transformées en point de score.",
                            "Particules mobiles : signe du plancton, sans pourcentage inventé.",
                            "La figure est dans figures/f-pleural.htm."])]),
        "p7": (["Syndrome infectieux pleural : fièvre plus liquide du côté de la pneumonie.",
                "Il se sépare du transsudat bilatéral apyrétique et de l'ascite."],
               [("Frontières", ["Cœur : deux côtés, pas de fièvre, Light négatif.",
                                 "Cancer : pH bas possible sans fièvre, épaississement.",
                                 "Sang : trauma, hémodynamique.",
                                 "Ascite infectée : autre seuil, les neutrophiles."])]),
        "p8": (["Positif comme empyème si le pus est là. Positif comme compliqué si le pH ou le glucose franchit le seuil lu.",
                "Le barème positif de risque n'est pas le diagnostic."],
               [("Preuve", ["Aspect écrit dans le dossier.",
                             "pH avec la méthode propre.",
                             "Glucose et lactate déshydrogénase du même prélèvement.",
                             "Light si l'on doute encore de la nature exsudative."])]),
        "p9": (["pH, glucose, lactate déshydrogénase, culture en flacon, cytologie seulement si le cancer est en jeu.",
                "Le sang du jour sert à Light et à l'albumine du barème."],
               [("Tubes", ["Seringue sèche pour le pH.",
                            "Flacon d'hémoculture.",
                            "Biochimie.",
                            "Pas de formule de volume sur cet empyème."])]),
        "p10": (["Pus ou pH bas : drain petit. pH haut : surveillance datée.",
                 "La chirurgie n'est pas le premier geste."],
               [("Arbre", ["Pus : drain.",
                            "pH ≤ 7,2 : drain si accessible.",
                            "Zone intermédiaire : lactate déshydrogénase au-dessus de 900 UI/l et clinique.",
                            "pH ≥ 7,4 : pas de drain immédiat.",
                            "Échec du drain bien placé : avis spécialisé, pas d'emblée le bloc."])]),
        "p11": (["Drain de 14 French ou moins, sous échographie. Antibiotique de la pneumonie, ajusté au germe.",
                 "Le barème informe. Il ne remplace pas le drain. L'information professionnelle n'est pas le siège du seuil de pH."],
               [("Conduite", ["Poser le drain dans le même temps que la décision.",
                               "Contrôler le débit à quelques heures.",
                               "Revoir à 48 heures si l'on n'a pas drainé.",
                               "Ne pas commencer par la chirurgie.",
                               "Ne pas diurétiser à la place du drain."])]),
        "p12": (["Le patient non drainé a une heure de revue. Le patient drainé a un responsable du drain.",
                 "La fièvre qui revient fait reponctionner."],
               [("Prévention", ["Traiter la pneumonie sans attendre le pus.",
                                 "Ponctionner tôt un liquide qui accompagne une fièvre persistante.",
                                 "Ne pas laisser un pH intermédiaire sans propriétaire.",
                                 "Écrire les signes qui ramènent."])]),
        "p13": (["Pus, trois zones de pH, deux glucoses selon le contexte, lactate déshydrogénase 900 UI/l, drain petit, barème avec pus à 0.",
                 "Pas de formule de volume. Pas de chirurgie d'emblée."],
               [("Oral", ["Citer 7,2 et 7,4.",
                           "Citer 3,3 mmol/l et 4,0 mmol/l sans les échanger.",
                           "Citer le pus à 0 point.",
                           "Dire pourquoi Balik ne s'applique pas."])]),
        "p14": (["Piège : inverser le point de purulence. Piège : drainer tout pH ≥ 7,4. Piège : croire un pH souillé.",
                 "Le cas chiffré est dans les fenêtres."],
               [("Cas court", ["Femme fébrile, pneumonie, pH 7,11, glucose 2,4 mmol/l : drain.",
                                "Homme qui va mieux, pH 7,42 : pas de drain immédiat, revue.",
                                "pH 6,9 dans la seringue de lidocaïne : chiffre jeté.",
                                "Score bas et pus : drain quand même."])]),
    }
    base_dx(3, r, P)

def dx4():
    r = "2"
    P = {}
    textes = {
        "p1": "La péritonite bactérienne spontanée est l'infection d'une ascite sans perforation. Le seuil est un compte de neutrophiles au-dessus de 250 par mm³.",
        "p2": "Elle complique surtout l'ascite de cirrhose. Une ponction tardive, au-delà de douze heures, est associée à plus de morts dans la série citée par l'EASL.",
        "p3": "La translocation bactérienne infecte un liquide pauvre en défenses. La protéine basse marque le risque, les neutrophiles marquent l'infection.",
        "p4": "Ponction dans l'heure si fièvre, confusion ou hémorragie. Traitement si le seuil est franchi, sans attendre la culture.",
        "p5": "Cirrhose, fièvre, douleur diffuse, trouble de la conscience, saignement digestif. Une défense localisée oriente vers le chirurgien.",
        "p6": "L'échographie montre le liquide et guide l'aiguille. Elle ne compte pas les cellules.",
        "p7": "Syndrome infectieux sur ascite. Il n'est pas l'empyème, ni le transsudat cardiaque simple.",
        "p8": "Positif si les neutrophiles dépassent 250 par mm³. La culture négative ne l'annule pas.",
        "p9": "Compte de neutrophiles, albumine, protéine, culture de 10 ml au lit, créatinine et bilirubine.",
        "p10": "Seuil franchi : antibiotique et albumine. Seuil non franchi : pas de céphalosporine de couverture. Ventre chirurgical : avis immédiat.",
        "p11": "Ceftriaxone dans la fourchette lue du n° 59876. Albumine en deux temps selon l'EASL, pas selon la notice d'Albunorm.",
        "p12": "Toute fièvre ultérieure est une nouvelle ponction. L'anti-inflammatoire est interdit.",
        "p13": "250, 10 ml, 1 à 2 g jusqu'à 4 g avec le décalage d'indication, albumine jour 0 et jour 3, bilirubine 68 et créatinine 88.",
        "p14": "Piège : couvrir un compte sous le seuil. Piège : arrêter quand la culture est négative. Piège : oublier le chirurgien si la douleur se localise.",
    }
    for i, (pid, phrase) in enumerate(textes.items(), 1):
        P[pid] = ([phrase, "Le détail et les cas chiffrés sont dans les fenêtres."],
                  [("Repères", [phrase,
                                "On écrit le chiffre à côté du seuil.",
                                "On ne mélange pas ce seuil avec le pH pleural.",
                                "Le rang E n'est pas le numéro de ce diagnostic."])])
    base_dx(4, r, P)

def dx5():
    r = "7"
    phrases = [
        "L'hémopéritoine et l'hémothorax sont du sang libre. Le sang frais est souvent noir à l'échographie.",
        "Le trauma et la chute d'hémoglobine font la fréquence de ce diagnostic. Pas de taux suisse inventé.",
        "Le sang s'écoule vers le point déclive. Il conduit les ultrasons, d'où le signe de la colonne dans la plèvre.",
        "Instable et liquide : hémostase. Stable : scanner. On ne ponctionne pas pour retarder le bloc.",
        "Trauma, grossesse extra-utérine, anticoagulant, douleur brutale, syncope.",
        "Quatre fenêtres du FAST, plus la plèvre. On les nomme une par une.",
        "Syndrome de sang libre : choc ou anémie aiguë plus liquide. Pas la fièvre du parapneumonique.",
        "Positif par le contexte et le liquide, confirmé par l'hémoglobine ou le scanner chez le stable.",
        "Hémoglobine répétée, échographie des fenêtres, scanner si stable. Pas de Balik.",
        "Instable : hémostase. Stable : image en coupe. Drain pleural si l'hémothorax gêne la ventilation.",
        "Pas de diurétique. Pas de céphalosporine comme premier geste. Le geste est mécanique.",
        "Surveillance de la pression et de l'hémoglobine. Un négatif initial se répète si l'état change.",
        "Quatre fenêtres, sang souvent noir, instable vers l'hémostase, chiffres de 2021 pour la colonne, pas de formule de volume.",
        "Piège : appeler ascite un Morison de traumatisé. Piège : opérer un cirrhotique stable sans chute d'hémoglobine.",
    ]
    P = {}
    for i, phrase in enumerate(phrases, 1):
        P[f"p{i}"] = ([phrase, "Les fenêtres détaillent les décisions."],
                     [("Décision", [phrase, "On nomme la fenêtre.", "On relie la pression au geste.", "On ne récite pas un seuil d'ascite."])])
    base_dx(5, r, P)

def run_all():
    dx2()

if __name__ == "__main__":
    nums = [int(a) for a in sys.argv[1:]] or [2]
    fn = {2: dx2, 3: dx3, 4: dx4, 5: dx5}
    for n in nums:
        fn[n]()

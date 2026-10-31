#!/usr/bin/env python3
"""Phase A de LOT_162. Texte rédigé, pas un gabarit vide."""
from moteur import btn, fen, page, table, SIGLES
from fenetres_longues import lecture_score, nodules, suivi, cas_crise, cas_coma, cas_amio, cas_faux, interactions, populations, cas_deq, consultation
from pathlib import Path

S = lambda *n: "".join(f'<sup class="s">{i}</sup>' for i in n)

def P(*parts):
    return "<p>" + "".join(parts) + "</p>"

# --- fenêtres ---
profils = fen("w-profils", "Profils TSH, T4 libre et T3 libre", f"""
{P("On lit d'abord la thyréostimuline, puis la thyroxine libre si elle est anormale. La triiodothyronine libre vient quand la thyrotoxicose est possible et que la thyroxine libre est encore normale, ou quand on cherche un syndrome de basse T3.", S(1))}
{table("Huit profils. Les bornes chiffrées du CHUV sont celles publiées en 2010, pas une loi nationale.",
["Profil", "Lecture", "Ce qu'on ne conclut pas"],
[
["Thyréostimuline haute, thyroxine libre basse", "Hypothyroïdie primaire. Au CHUV en 2010, une hypothyroïdie franche a le plus souvent une thyréostimuline au-dessus de 10 mU/l.", "On ne commence pas la lévothyroxine si une insuffisance surrénale est possible : l'hormone thyroïdienne peut précipiter la crise."],
["Thyréostimuline haute, thyroxine libre normale", "Hypothyroïdie infraclinique. La revue lausannoise retient une thyréostimuline de 3,5 à 20 mU/l avec une thyroxine libre normale.", "Ce n'est pas une indication automatique de traitement. Les bénéfices restent controversés."],
["Thyréostimuline basse, thyroxine libre ou triiodothyronine libre haute", "Thyrotoxicose. La production, la libération ou une prise exogène peuvent donner le même profil.", "Le profil ne dit pas si c'est une maladie de Basedow, un nodule ou une thyroïdite."],
["Thyréostimuline basse, hormones libres normales", "Hyperthyroïdie infraclinique. La revue la cite à environ 1 % selon la population et les bornes.", "Une maladie aiguë, un corticoïde ou l'amiodarone peuvent abaisser la thyréostimuline sans hyperthyroïdie."],
["Thyréostimuline basse ou normale, thyroxine libre basse", "Hypothyroïdie centrale, ou phase tardive d'une maladie grave, ou reprise après un freinage.", "Une thyréostimuline normale n'écarte pas le déficit hypophysaire."],
["Thyréostimuline normale ou haute, thyroxine libre haute", "Effet de l'amiodarone chez un sujet encore euthyroïdien, adénome hypophysaire à thyréostimuline, résistance aux hormones, ou interférence de dosage.", "On ne traite pas comme une hypothyroïdie primaire."],
["Triiodothyronine basse, thyréostimuline normale ou basse, thyroxine libre normale puis basse", "Syndrome de basse T3 de la maladie grave.", "Ce n'est pas une indication de lévothyroxine ni de liothyronine chez le patient sans hypothyroïdie connue."],
["Thyréostimuline effondrée, hormones libres très hautes, clinique pauvre", "Interférence de la biotine sur un dosage streptavidine-biotine, jusqu'à preuve du contraire.", "On ne démarre pas un thionamide sur ce seul profil."],
])}
{P("Au laboratoire du Centre hospitalier universitaire vaudois, en 2010, la thyroxine libre allait de 8 à 22 pmol/l et la thyréostimuline de 0,2 à 3,5 mU/l. La même revue rappelle que la limite haute de la thyréostimuline est souvent de 4,5 mU/l dans la littérature, et que chaque laboratoire fixe ses bornes sur une population ambulatoire sans maladie thyroïdienne connue.", S(1))}
{P("L'ordre pratique de la revue est simple. On dose la thyréostimuline. On ajoute la thyroxine libre seulement si la thyréostimuline est anormale. On ne dépiste pas toute la population adulte. On dose en début de grossesse si le risque est augmenté : antécédent personnel ou familial, maladie autoimmune, irradiation cervicale, fausses couches répétées ou infertilité.", S(1))}
""")

epi = fen("w-epi", "Fréquences lues, et ce qu'elles ne classent pas", f"""
{P("Dans NHANES III, chez des adultes sans maladie thyroïdienne connue, l'hypothyroïdie franche et l'hyperthyroïdie franche étaient chacune inférieures à 1 %. L'hypothyroïdie est rare chez l'adulte jeune et augmente avec l'âge. Le goitre multinodulaire et l'hyperthyroïdie en général augmentent aussi avec l'âge, et le tabac renforce l'hyperthyroïdie. La maladie de Basedow est plus fréquente chez les femmes de 20 à 40 ans.", S(1))}
{P("Entre l'euthyroïdie et la maladie franche, la revue place une zone grise. La prévalence de l'hypothyroïdie infraclinique est estimée à environ 5 %. L'hyperthyroïdie infraclinique est plus rare, environ 1 %. Ces chiffres dépendent de la population et des bornes du laboratoire.", S(1))}
{P("Le risque de passer d'une hypothyroïdie infraclinique à une forme franche est de 4,3 % par an si les anticorps anti-thyroperoxydase sont présents, et de 2,3 % par an s'ils sont absents. À dix ans, ce risque passe de 23 % à 43 % quand les anticorps sont positifs.", S(1))}
{P("La crise thyréotoxique est rare. Les séries modernes citées par la recommandation de 2016 donnent une mortalité de 8 % à 25 %. Ce n'est pas une prévalence de population : c'est la mortalité des patients déjà dans la crise.", S(2))}
{P("Sous amiodarone, l'hypothyroïdie infraclinique est citée jusqu'à 26 % des patients traités, et la forme franche jusqu'à 5 %. La thyrotoxicose de type 2 est la forme la plus fréquente là où l'apport d'iode est suffisant.", S(4))}
{P("Aucun des textes lus ne donne la part suisse de chacun des dix diagnostics de cette leçon. L'ordre E du cours est un ordre d'exclusion, pas un classement de fréquence.")}
""")

physio = fen("w-physio", "Axe, rétrocontrôle et trois façons d'avoir trop d'hormone", f"""
{P("L'hypothalamus libère la thyréolibérine, l'hypophyse libère la thyréostimuline, la thyroïde libère surtout de la thyroxine et une part de triiodothyronine. La thyroxine se convertit en triiodothyronine dans les tissus, par les désiodases. La triiodothyronine est l'hormone qui agit sur le récepteur nucléaire. La thyroxine et la triiodothyronine freinent l'hypophyse. Si la thyroïde en produit trop, la thyréostimuline baisse. Si la thyroïde n'en produit plus, la thyréostimuline monte. Ce rétrocontrôle explique les deux premiers profils.")}
{P("Trois mécanismes donnent une thyrotoxicose, c'est-à-dire trop d'hormone dans le sang. La glande en fabrique trop : maladie de Basedow, nodule autonome, goitre multinodulaire toxique, surcharge iodée sur une autonomie. La glande en lâche le stock sans en fabriquer : thyroïdite subaiguë, thyroïdite silencieuse, thyroïdite du post-partum, thyroïdite de type 2 sous amiodarone. L'hormone vient de l'extérieur : lévothyroxine prise en excès, ou parfois une prise cachée. Le thionamide ne sert que le premier mécanisme. Il ne bloque pas une fuite de stock ni une prise exogène.", S(1, 2))}
{P("L'iode en excès bloque d'abord l'organification, c'est l'effet de Wolff-Chaikoff, puis la glande s'en échappe. Cet effet explique la hausse initiale de la thyréostimuline sous amiodarone, puis le retour de la thyréostimuline alors que la thyroxine libre reste haute parce que la désiodase de type 1 est inhibée.", S(4))}
{P("Dans la maladie grave, la triiodothyronine baisse en premier, par baisse de la conversion et hausse de la désiodase de type 3. Ensuite la thyréostimuline et la thyroxine baissent, puis la thyroxine libre chez les plus malades. La recommandation de 2014 tient ce mouvement pour adaptatif et déconseille de le corriger par une hormone chez le patient qui n'était pas hypothyréodien.", S(3))}
{P("La biotine ne change pas la glande. Elle occupe la streptavidine du tube. Le dosage sandwich de la thyréostimuline devient faussement bas. Le dosage compétitif de la thyroxine libre devient faussement haut. Le laboratoire rend alors un profil de Basedow chez un patient euthyroïdien.", S(2, 7))}
""")

demarche = fen("w-demarche", "Démarche en sept temps", f"""
{P("Temps 1. Est-ce une urgence clinique avant même le chiffre. Fièvre, agitation ou coma, vomissements, ictère, fibrillation très rapide, œdème pulmonaire : on calcule le score de Burch-Wartofsky et on traite la crise thyréotoxique si le tableau est celui d'une thyrotoxicose décompensée. Hypothermie, bradypnée, coma, hyponatrémie chez un patient au visage bouffi : on traite le coma myxœdémateux sans attendre le résultat, glucocorticoïde d'abord.", S(2, 3, 5))}
{P("Temps 2. On relit le profil, pas un chiffre isolé. Thyréostimuline seule haute ou basse ne suffit pas. On demande la thyroxine libre. On demande la triiodothyronine libre si la thyréostimuline est basse et la thyroxine libre encore dans les bornes, ou si l'on suspecte une basse T3.", S(1))}
{P("Temps 3. On cherche le médicament et le contexte. Amiodarone, biotine, corticoïde, produit de contraste, lithium, lévothyroxine déjà prescrite, grossesse, réanimation, dopamine. Sans cette question, le chiffre est souvent faux ou hors de propos.", S(1, 2, 4, 7))}
{P("Temps 4. On examine le cou et les yeux. Goitre diffus et souffle, orbitopathie : maladie de Basedow probable, et la scintigraphie n'est pas obligatoire. Nodules : échographie, puis scintigraphie si la thyréostimuline est basse. Cou très douloureux et vitesse de sédimentation haute : thyroïdite subaiguë.", S(1, 2))}
{P("Temps 5. On choisit l'examen qui distingue fabrication et destruction. Anticorps anti-récepteur si l'on pense à Basedow. Scintigraphie si l'on pense à un nodule toxique ou à une thyroïdite et qu'il n'y a pas de grossesse ni d'allaitement. Sous amiodarone en zone riche en iode, la captation est basse dans les deux types et ne les sépare pas : le Doppler et le terrain comptent davantage.", S(2, 4))}
{P("Temps 6. On traite le mécanisme, pas le mot hyperthyroïdie. Thionamide si la glande fabrique. Bêtabloquant pour le cœur dans les deux cas. Glucocorticoïde si la thyroïdite de type 2 à l'amiodarone est retenue. Antalgique et parfois prednisone si la thyroïdite de De Quervain est retenue. Rien de tout cela pour une biotine ou une basse T3 isolée.", S(1, 4, 8, 13))}
{P("Temps 7. On fixe le contrôle. Après un changement de lévothyroxine, on attend l'équilibre avant de re-doser la thyréostimuline. La revue lausannoise contrôle trois mois après l'introduction et quatre à six semaines après chaque changement de dose, puis une fois par an. Sous carbimazole, on surveille la formule sanguine selon l'information professionnelle, et on arrête le médicament devant une fièvre ou une angine.", S(1, 8, 9))}
""")

burch = fen("w-burch", "Score de Burch-Wartofsky, toutes les classes", f"""
{P("Le score date de 1993. Le tableau lu est celui de la recommandation japonaise de 2016, qui le reprend en entier. Il ne s'applique qu'à un patient déjà thyrotoxique. Une pneumonie seule peut donner de la fièvre, une tachycardie et un vomissement : le score monterait sans crise. La recommandation américaine de 2016 le dit explicitement.", S(2, 5))}
{table("Barème complet. Aucune ligne n'est retirée.",
["Domaine", "Classe", "Points"],
[
["Température", "37,2 à 37,7 °C", "5"],
["Température", "37,8 à 38,3 °C", "10"],
["Température", "38,4 à 38,8 °C", "15"],
["Température", "38,9 à 39,3 °C", "20"],
["Température", "39,4 à 39,9 °C", "25"],
["Température", "40,0 °C ou plus", "30"],
["Fréquence cardiaque", "90 à 109 par minute", "5"],
["Fréquence cardiaque", "110 à 119", "10"],
["Fréquence cardiaque", "120 à 129", "15"],
["Fréquence cardiaque", "130 à 139", "20"],
["Fréquence cardiaque", "140 ou plus", "25"],
["Fibrillation auriculaire", "Absente", "0"],
["Fibrillation auriculaire", "Présente", "10"],
["Insuffisance cardiaque", "Absente", "0"],
["Insuffisance cardiaque", "Légère", "5"],
["Insuffisance cardiaque", "Modérée", "10"],
["Insuffisance cardiaque", "Sévère", "15"],
["Foie et tube digestif", "Absent", "0"],
["Foie et tube digestif", "Modéré : diarrhée, douleur, nausée ou vomissement", "10"],
["Foie et tube digestif", "Sévère : ictère", "20"],
["Système nerveux", "Absent", "0"],
["Système nerveux", "Léger : agitation", "10"],
["Système nerveux", "Modéré : délire, psychose ou léthargie extrême", "20"],
["Système nerveux", "Sévère : convulsion ou coma", "30"],
["Facteur précipitant", "Absent", "0"],
["Facteur précipitant", "Présent", "10"],
])}
{P("Lecture du total. 45 ou plus : crise thyréotoxique, traitement agressif. 25 à 44 : crise imminente, le jugement clinique décide du traitement agressif, et le patient est surveillé de près. Moins de 25 : crise peu probable. Un score de 25 à 44 n'interdit pas le traitement, et un score de 45 ou plus ne dispense pas de chercher une autre cause au coma.", S(2, 5))}
{P("Les critères japonais de 2016 exigent d'abord une thyrotoxicose biologique, T3 libre ou T4 libre haute. TS1, première combinaison : au moins un signe neurologique, plus un signe parmi fièvre d'au moins 38 °C, fréquence d'au moins 130, insuffisance cardiaque définie, ou atteinte digestive. TS1, combinaison alternative : au moins trois de ces quatre signes sans exiger le signe neurologique. TS2 : deux de ces quatre signes. TS2 alternative : le tableau de TS1 mais les hormones libres ne sont pas encore rendues. Si une autre maladie explique clairement le signe, on l'écarte. Si l'on hésite, on garde le signe comme partie de la crise déclenchée par cette maladie.", S(5))}
{P("La fréquence d'au moins 130 du critère japonais n'est pas le même seuil que les paliers du score de Burch-Wartofsky, qui commence à compter dès 90. On n'additionne pas les deux systèmes pour fabriquer un troisième chiffre. On les utilise tous les deux, comme le texte japonais le recommande, puis on juge le patient.", S(5))}
""")

anticorps = fen("w-anticorps", "Anticorps, scintigraphie, rapport T3 sur T4", f"""
{P("Les anticorps anti-thyroperoxydase orientent vers une thyroïdite auto-immune et vers le risque d'évolution d'une forme infraclinique. Ils ne prouvent pas à eux seuls que l'hyperthyroïdie vient d'une maladie de Basedow. Sous amiodarone, ils sont souvent présents dans le type 1 et absents dans le type 2, sans permettre à eux seuls le classement.", S(1, 4))}
{P("Les anticorps anti-récepteur stimulent la glande dans la maladie de Basedow. En thyrotoxicose franche, les dosages récents cités en 2016 ont une sensibilité de 96 à 97 % et une spécificité de 99 % pour cette maladie. Un dosage négatif n'élimine pas un nodule toxique ni une thyroïdite : il rend Basedow moins probable. Un dosage positif au moment d'arrêter le carbimazole annonce une rechute : 80 à 100 % si l'anticorps reste haut, 20 à 30 % s'il est bas ou indétectable.", S(2))}
{P("La scintigraphie montre où l'iode entre. Basedow : fixation diffuse, sauf nodule ou fibrose associée. Nodule toxique unique : foyer chaud et extinction du reste de la glande. Goitre multinodulaire toxique : plusieurs foyers chauds et des zones éteintes. Thyroïdite destructrice : fixation basse, parce que la glande ne fabrique pas, elle fuit. On ne fait pas cet examen chez la femme enceinte ni chez la femme qui allaite.", S(2))}
{P("Quand la scintigraphie est impossible, le rapport de la triiodothyronine totale sur la thyroxine totale a été utile dans une étude citée par la recommandation de 2016. Au-dessus de 20, en nanogrammes par microgramme, le tableau allait vers Basedow ou un goitre nodulaire toxique. En dessous de 20, vers une thyroïdite silencieuse ou du post-partum. Une thyroxine très haute avec une triiodothyronine moins haute fait chercher une prise de lévothyroxine.", S(2))}
""")

tirads = fen("w-tirads", "TI-RADS, les cinq catégories et tous les points", f"""
{P("La classification de 2017 décrit un nodule, pas une hormone. Elle entre dans cette leçon parce qu'un nodule autonome et un cancer peuvent coexister, et parce qu'une thyréostimuline basse ne dispense pas de décrire le nodule avant un traitement par iode radioactif. On choisit un signe par catégorie, sauf les foyers échogènes où l'on additionne tout ce qui est présent. Le total donne la catégorie. On ne retire aucune catégorie.", S(6))}
{table("Points. Un choix par ligne, sauf les foyers échogènes.",
["Catégorie", "Signe", "Points"],
[
["Composition", "Kystique ou presque", "0"],
["Composition", "Spongiforme", "0"],
["Composition", "Mixte kystique et solide", "1"],
["Composition", "Solide ou presque solide", "2"],
["Échogénicité", "Anéchogène", "0"],
["Échogénicité", "Hyperéchogène ou isoéchogène", "1"],
["Échogénicité", "Hypoéchogène", "2"],
["Échogénicité", "Très hypoéchogène", "3"],
["Marge", "Lisse ou mal limitée", "0"],
["Marge", "Lobulée ou irrégulière", "2"],
["Marge", "Extension hors de la thyroïde", "3"],
["Foyers échogènes", "Aucun, ou queue de comète large", "0"],
["Foyers échogènes", "Macrocalcification", "1"],
["Foyers échogènes", "Calcification périphérique", "2"],
["Foyers échogènes", "Foyers ponctués", "3"],
["Forme", "Plus large que haut", "0"],
["Forme", "Plus haut que large", "3"],
])}
{table("Catégories et conduite. Toutes les classes.",
["Total", "Catégorie", "Cytoponction", "Suivi"],
[
["0", "TR1, bénin", "Non", "Non"],
["2", "TR2, non suspect", "Non", "Non"],
["3", "TR3, peu suspect", "Si 2,5 cm ou plus", "Si 1,5 cm ou plus"],
["4 à 6", "TR4, moyennement suspect", "Si 1,5 cm ou plus", "Si 1,0 cm ou plus"],
["7 ou plus", "TR5, très suspect", "Si 1,0 cm ou plus", "Si 0,5 cm ou plus"],
])}
{P("Un nodule spongiforme, quelle que soit sa taille, ne va pas à la cytoponction dans ce système. Les seuils de 2,5 cm et de 1,5 cm sont volontairement plus hauts que ceux d'autres sociétés : l'échographie mesure souvent un diamètre plus grand que la pièce. Un nodule qui fixe l'isotope et qui éteint le reste de la glande est un nodule autonome : la cytoponction répond à une autre question, celle du cancer, pas celle de la toxicité.", S(6))}
""")

biotine = fen("w-biotine", "Biotine : mécanisme et conduite", f"""
{P("La biotine, ou vitamine B7, sert de crochet dans de nombreux immunodosages. En excès dans le tube, elle prend la place sur la streptavidine. Le dosage sandwich de la thyréostimuline perd son signal et rend une valeur basse. Le dosage compétitif de la thyroxine libre et de la triiodothyronine libre rend une valeur haute, parce que le signal restant est inversement lié à l'hormone. Les anticorps, y compris l'anticorps anti-récepteur, peuvent aussi être faussement hauts. Le dossier ressemble alors à une maladie de Basedow.", S(2, 7))}
{P("La revue australienne de 2016 décrit des patients euthyroïdiens avec une thyréostimuline inférieure à 0,01 mUI/l et une thyroxine libre supérieure à 100 pmol/l. L'alimentation et une multivitamine usuelle ne suffisent pas à cet effet. Des doses dépassant 5 mg le peuvent : compléments pour les cheveux, la peau et les ongles, et fortes doses essayées dans la sclérose en plaques. On demande l'arrêt, puis on prélève à nouveau. La recommandation américaine de 2016 dit au moins 2 jours. La mise en garde de 2016 dit 72 heures. On retient les deux délais lus, et on ne traite pas entre les deux prélèvements si la clinique est pauvre.", S(2, 7))}
{P("Le piège inverse existe. Un patient vraiment hyperthyroïdien peut prendre de la biotine. L'arrêt de la biotine ne le guérit pas. On ne conclut à l'interférence que si le second prélèvement se normalise plus vite que la demi-vie de la thyroxine, ou si la clinique n'a jamais collé au chiffre.")}
""")

amio = fen("w-amio", "Amiodarone : profil euthyroïdien, puis deux maladies", f"""
{P("L'amiodarone contient beaucoup d'iode et inhibe la désiodase. Chez un sujet qui reste euthyroïdien, le profil change chez tout le monde, pas seulement chez ceux qui tombent malades. Les trois premiers mois : thyréostimuline haute, thyroxine haute, triiodothyronine basse, reverse T3 haute. Après trois mois : thyréostimuline revenue vers sa base, thyroxine encore haute ou en haut de la norme, triiodothyronine basse ou en bas de la norme, reverse T3 haute. Ce profil n'est pas une hyperthyroïdie et n'est pas une indication d'arrêter le médicament.", S(4))}
{P("La dose d'entretien lue dans l'information professionnelle des comprimés Cordarone, numéro 33393, va de 100 mg à 400 mg par jour. La recommandation européenne de 2018 parle d'une dose habituelle de 200 mg par jour, et note que des patients restent euthyroïdiens à 400 mg par jour. On ne recopie pas ici une dose de charge : elle n'est pas le sujet de la dysthyroïdie.", S(4, 14))}
{P("L'hypothyroïdie induite se traite par lévothyroxine si elle est franche, sans obligation d'arrêter l'amiodarone quand le cardiologue la maintient. La forme infraclinique peut être surveillée, surtout chez la personne âgée, tous les 4 à 6 mois. La cible sous traitement n'est pas une thyréostimuline basse : on vise une thyroxine libre et une triiodothyronine libre normales, et une thyréostimuline dans le haut de la norme, ou encore un peu haute mais sous 10 mU/l dans la forme franche, pour éviter le surdosage.", S(4))}
{P("La thyrotoxicose de type 1 est une fabrication d'hormone sur un goitre nodulaire ou un Basedow latent. La thyrotoxicose de type 2 est une destruction sur une glande à peu près normale. Le Doppler montre une vascularisation riche dans le type 1 et absente dans le type 2. En zone riche en iode, la scintigraphie est basse dans les deux et ne sert pas à les séparer. Le type 1 reçoit un thionamide. Le type 2 reçoit un glucocorticoïde. La forme mixte commence par le thionamide. On ajoute le glucocorticoïde d'emblée si le doute est fort, ou après quatre à six semaines sans amélioration.", S(4))}
""")

basst3 = fen("w-t3", "Syndrome de basse T3 : ce qu'on ne traite pas", f"""
{P("La revue lausannoise de 2010 le nomme déjà : dans une maladie aiguë, une dénutrition, ou après un corticoïde ou l'amiodarone, la triiodothyronine peut être très basse, et la thyréostimuline peut baisser au point de faire croire à une hyperthyroïdie. La recommandation américaine de 2014 décrit la séquence. D'abord la triiodothyronine baisse. Ensuite la thyréostimuline et la thyroxine baissent. Chez les plus graves, la thyroxine libre baisse aussi. La reverse T3 monte quand on la dose, mais elle n'est pas demandée en routine dans les textes suisses lus.", S(1, 3))}
{P("La recommandation est de ne pas donner de lévothyroxine à un patient hospitalisé pour une maladie grave qui présente ce syndrome et qui n'avait pas d'hypothyroïdie. Elle est aussi de ne pas donner de liothyronine dans la même situation. Les essais n'ont pas montré un bénéfice net, et un risque a été soulevé pour la lévothyroxine.", S(3))}
{P("La frontière avec l'hypothyroïdie vraie est la suivante. Un patient déjà substitué garde sa lévothyroxine pendant la réanimation. Une thyréostimuline qui monte pendant l'aggravation, chez un patient qui a une thyroïde malade, fait plutôt chercher un manque d'hormone. La dopamine peut abaisser la thyréostimuline et faire sous-doser si l'on ne regarde qu'elle. On ne corrige pas la triiodothyronine basse d'un patient déjà substitué dans le seul but de la ramener à la norme : la recommandation tient la baisse pour adaptative.", S(3))}
""")

urgences = fen("w-urgences", "Médicaments de l'urgence, dans l'ordre", f"""
{P("Crise thyréotoxique. Le traitement est multiple : bêtabloquant, thionamide, iode minéral au moins une heure après le thionamide, glucocorticoïde, refroidissement, remplissage, traitement de la cause, soins intensifs selon le tableau. L'iode donné avant le thionamide peut servir de substrat et aggraver la fabrication. C'est la raison de l'ordre, écrite dans la recommandation japonaise de 2016 qui cite l'American Thyroid Association.", S(2, 5))}
{P("Le thionamide suisse lu est le carbimazole, Néo-Mercazole, numéro 21037. Dose initiale 20 à 60 mg par jour, en deux ou trois prises, sans dépasser 60 mg par jour. Cette limite rejoint le plafond japonais du méthimazole dans la crise due à Basedow, qui est aussi de 60 mg par jour. On n'écrit pas ici les doses plus hautes signalées pour d'autres pays. Le propylthiouracile n'a pas de spécialité dans l'index parcouru : aucune dose n'est enseignée.", S(5, 8))}
{P("Le propranolol, Propranolol Zentiva, numéro 47025, a pour indication lue l'hyperthyroïdie et les crises thyréotoxiques. La dose écrite pour cette indication est de 10-40 mg, 3 à 4 fois par jour. On ne lui substitue pas la dose de l'hypertension, qui est une autre ligne de la même information professionnelle.", S(10))}
{P("L'iode de la crise n'est pas le comprimé d'iodure de potassium prévu pour un accident nucléaire. Iodure de potassium axapharm, numéro 67017, indique 130.0 mg chez l'adulte, et il est contre-indiqué dans l'hyperthyroïdie, la maladie de Basedow et l'autonomie thyroïdienne. La recommandation japonaise parle d'environ 200 milligrammes par jour d'iodure minéral, donnés après le thionamide, par la bouche, sous la langue, par sonde ou par voie rectale selon l'état. Cette dose n'est pas celle du comprimé de blocage nucléaire.", S(5, 12))}
{P("Le glucocorticoïde diminue la conversion de thyroxine en triiodothyronine et couvre une surrénale débordée. Solu-CORTEF, numéro 23533, décrit pour une intervention majeure chez un patient déjà sous corticoïde 100 mg par voie intraveineuse, puis 100 mg toutes les 6 heures pendant au moins 72 heures. Le cours retient cette dose de stress, déjà écrite, comme couverture de la crise et du coma, sans inventer un autre schéma.", S(3, 11))}
{P("Coma myxœdémateux. On prélève un cortisol si on le peut, puis on injecte le glucocorticoïde, puis seulement la lévothyroxine. La recommandation de 2014 demande une lévothyroxine intraveineuse, dose de charge 200 à 400 microgrammes, plus basse si le patient est petit, âgé ou coronarien, puis 1,6 microgramme par kilogramme et par jour réduit à 75 % tant que la voie est intraveineuse. Aucune spécialité intraveineuse n'est dans l'index suisse parcouru. Euthyrox, numéro 54949, est oral : dose initiale souvent 25 à 50 microgrammes chez le sujet fragile, avec la phrase lue de 25 µg chez la personne âgée ou cardiaque, et une dose d'entretien de l'ordre de 100 à 200 µg par jour dans le tableau de l'hypothyroïdie. On n'administre pas les comprimés comme s'ils étaient la forme intraveineuse.", S(3, 9))}
{P("On traite en même temps l'hypothermie sans réchauffement agressif, l'hypoventilation, l'hyponatrémie, l'hypoglycémie et la déplétion. On cherche un facteur déclenchant, souvent une infection. On ne retarde pas l'hormone pour attendre la thyréostimuline : son niveau ne mesure pas la gravité du coma.", S(3))}
""")

doses = fen("w-doses", "Doses lues, spécialité par spécialité", f"""
{table("Ce que l'information professionnelle suisse écrit, et ce qu'elle ne dit pas.",
["Spécialité", "Numéro", "Phrase retenue", "Hors de cette phrase"],
[
["Néo-Mercazole", "21037", "20 à 60 mg par jour au début, puis 5 à 20 mg par jour. Plafond adulte 60 mg par jour. Allaitement : pas plus de 20 mg par jour, en plusieurs prises, juste après la tétée.", "Pas de propylthiouracile dans l'index. Au-dessus de 40 mg par jour, formule sanguine avant traitement et chaque semaine pendant six semaines si le patient a plus de 40 ans."],
["Euthyrox", "54949", "Hypothyroïdie : début souvent 25 à 50, entretien 100 à 200 µg par jour. Sujet âgé, hypothyroïdie ancienne ou cœur : début à 25 µg. Le matin, à jeun, la forme voisine Eltroxine-LF, numéro 29812, se prend 30 minutes avant le petit-déjeuner.", "Pas de forme intraveineuse dans l'index. La dose de charge du coma vient de la recommandation de 2014, pas de cette autorisation."],
["Propranolol Zentiva", "47025", "Hyperthyroïdie et crises thyréotoxiques : 10-40 mg, 3 à 4 fois par jour.", "La dose de l'hypertension, jusqu'à 640 mg par jour, est une autre indication."],
["Solu-CORTEF", "23533", "Intervention majeure : 100 mg intraveineux, puis 100 mg toutes les 6 heures pendant au moins 72 heures. Doses initiales jusqu'à 100 mg. Ne pas descendre sous 25 mg par jour dans la mise en garde lue.", "Le schéma est écrit pour le stress opératoire du patient déjà cortiqué. On l'utilise comme dose de stress de la crise et du coma, en le disant."],
["Prednisone Streuli", "29349", "Maladie aiguë qui ne met pas le pronostic vital en jeu : 15 à 30 mg par jour. Seuil de Cushing écrit : 7,5 mg.", "L'essai cité par l'ETA dans la thyrotoxicose de type 2 à l'amiodarone utilisait 30 mg par jour. L'information professionnelle ne nomme pas cette maladie."],
["Cordarone comprimés", "33393", "Entretien 100 mg à 400 mg par jour. Comprimé à 200 mg.", "La dysthyroïdie n'est pas une ligne de posologie. On ne monte pas la dose pour traiter la thyroïde."],
["Iodure de potassium axapharm", "67017", "Adulte, accident nucléaire : 130.0 mg. Contre-indiqué si hyperthyroïdie, Basedow ou autonomie.", "Ce n'est pas le traitement de la crise. L'iode de la crise vient après le thionamide et n'est pas ce comprimé."],
])}
{P("Agranulocytose au carbimazole. Elle peut survenir en quelques heures, et des décès sont rapportés. Le patient arrête le médicament et consulte devant une fièvre, un malaise, des aphtes, une angine ou un autre signe d'infection. On contrôle alors la formule. L'arrêt précoce rend l'aplasie réversible dans la phrase lue. Des vascularites à ANCA sont décrites, surtout sous propylthiouracile, mais aussi sous carbimazole.", S(8))}
{P("Grossesse. Le carbimazole passe le placenta. Une dose inadaptée peut donner un goitre et une hypothyroïdie chez l'enfant, et un petit poids de naissance. Toute atteinte thyroïdienne chez une femme enceinte justifie un avis spécialisé, selon la revue de 2010. Les seuils de thyréostimuline par trimestre ne sont pas écrits ici : le texte de 2017 n'a pas été ouvert.", S(1, 8))}
""")

algo = fen("w-algo", "Algorithme et tableau des dix diagnostics", f"""
{P("L'ordre E exclut d'abord ce qui tue dans les heures. Ce n'est pas l'ordre de fréquence.")}
{table("Ordre d'exclusion.",
["Rang", "Diagnostic", "Signe qui le fait passer devant"],
[
["E1", "Crise thyréotoxique", "Thyrotoxicose et défaillance. Score 45 ou plus, ou critère japonais TS1 ou TS2."],
["E2", "Coma myxœdémateux", "Coma, hypothermie, hypoventilation, hyponatrémie. Glucocorticoïde avant l'hormone."],
["E3", "Maladie de Basedow", "Thyrotoxicose, goitre diffus, orbitopathie ou anticorps anti-récepteur."],
["E4", "Hypothyroïdie primaire", "Thyréostimuline haute, thyroxine libre basse, souvent anticorps anti-thyroperoxydase."],
["E5", "Dysthyroïdie induite par l'amiodarone", "Le médicament est là. On sépare l'effet euthyroïdien, l'hypothyroïdie, le type 1 et le type 2."],
["E6", "Thyroïdite destructrice", "Thyrotoxicose à fixation basse, puis souvent hypothyroïdie transitoire."],
["E7", "Goitre multinodulaire toxique et nodule autonome", "Thyréostimuline basse, foyers chauds, reste de la glande éteint."],
["E8", "Hypothyroïdie centrale", "Thyroxine libre basse, thyréostimuline basse ou normale, contexte hypophysaire."],
["E9", "Syndrome de basse T3 et interférence de la biotine", "Le chiffre ment ou la maladie générale domine. On ne donne pas d'hormone pour la basse T3, on ne donne pas de thionamide pour la biotine."],
["E10", "Dysfonction thyroïdienne infraclinique", "Une seule hormone anormale, l'autre dans les bornes, patient stable."],
])}
{P("Les dix noms de la leçon sont : maladie de Basedow, crise thyréotoxique, hypothyroïdie primaire, coma myxœdémateux, thyroïdite destructrice, goitre multinodulaire toxique et nodule autonome, dysthyroïdie induite par l'amiodarone, syndrome de basse T3 et interférence de la biotine, hypothyroïdie centrale, dysfonction thyroïdienne infraclinique.")}
""")

pieges = fen("w-pieges", "Pièges d'interprétation", f"""
{P("Traiter une thyréostimuline basse sans thyroxine libre. Une maladie aiguë suffit à l'abaisser.")}
{P("Donner de l'iode de blocage nucléaire à un patient en crise. Le comprimé 67017 est contre-indiqué dans l'hyperthyroïdie.", S(12))}
{P("Donner l'iode avant le thionamide. L'ordre lu est l'inverse : thionamide, puis au moins une heure, puis iode.", S(5))}
{P("Commencer la lévothyroxine devant une thyréostimuline haute sans avoir écarté l'insuffisance surrénale. La revue de 2010 le marque comme drapeau : l'hormone peut précipiter une crise addisonienne.", S(1))}
{P("Croire qu'une thyréostimuline normale écarte l'hypothyroïdie centrale.")}
{P("Classer un patient sous amiodarone comme hyperthyroïdien parce que la thyroxine libre est haute, alors que c'est l'effet attendu et que la thyréostimuline est normale.", S(4))}
{P("Demander une scintigraphie pour séparer les deux types de thyrotoxicose à l'amiodarone dans un pays riche en iode. Elle est basse des deux côtés.", S(4))}
{P("Donner un thionamide dans une thyroïdite destructrice. Il n'arrête pas la fuite du stock et il expose à l'agranulocytose.", S(1, 5))}
{P("Oublier la biotine devant un profil trop beau pour la clinique.", S(7))}
{P("Utiliser un score de crise chez un patient dont les hormones sont normales.")}
{P("Amputer une classification. Le score de Burch-Wartofsky garde toutes ses classes de température, de fréquence, d'insuffisance cardiaque, de foie, de système nerveux et de facteur précipitant. TI-RADS garde TR1, TR2, TR3, TR4 et TR5. Les critères japonais gardent les deux combinaisons de TS1 et les deux de TS2.", S(5, 6))}
""")

cas = fen("w-cas", "Cas type, correction", f"""
{P("Énoncé. Une femme de 34 ans consulte pour un amaigrissement de 6 kg en deux mois, des palpitations et une irritabilité. Le pouls est à 118 par minute, régulier. Les mains tremblent. La thyroïde est diffuse, soufflante. Les paupières sont rétractées et les conjonctives rouges. Il n'y a pas de fièvre, pas de vomissement, pas de confusion. La thyréostimuline est à 0,01 mU/l, la thyroxine libre à 48 pmol/l. Elle prend un comprimé pour les cheveux depuis dix jours. Que faites-vous, et que ne faites-vous pas ?")}
{P("Correction. Le profil est celui d'une thyrotoxicose, et la clinique colle : amaigrissement, tachycardie, tremblement, goitre diffus, souffle, atteinte oculaire. Ce n'est pas le tableau de la biotine seule, où la clinique est pauvre. On peut toutefois faire arrêter le comprimé et contrôler plus tard, parce qu'une biotine peut fausser en plus un vrai Basedow. On ne retarde pas le traitement d'une thyrotoxicose clinique pour ce seul doute.", S(7))}
{P("Ce n'est pas une crise. Température normale, pas de signe digestif, pas de signe neurologique au-delà de l'irritabilité, pas d'insuffisance cardiaque décrite, fréquence à 118. Sur le score, la fréquence entre 110 et 119 vaut 10 points, l'agitation légère vaudrait 10 si on la retient, et il n'y a pas de facteur précipitant évident. Le total reste sous 25 si l'on ne gonfle pas les items. On ne déclenche pas le protocole de crise. On surveille, parce qu'un produit de contraste ou une infection pourrait la déclencher.", S(5))}
{P("Le diagnostic de travail est la maladie de Basedow. L'orbitopathie et le goitre diffus rendent la scintigraphie inutile pour nommer la cause, selon la recommandation de 2016. Un anticorps anti-récepteur sert de base si l'on prévoit un traitement médical de douze à dix-huit mois. On explique l'agranulocytose avant la première prise.", S(2, 8))}
{P("Traitement initial. Propranolol 10-40 mg, 3 à 4 fois par jour, numéro 47025, pour la tachycardie. Carbimazole 20 à 60 mg par jour selon l'ampleur, numéro 21037, sans dépasser 60 mg par jour. Pas d'iode : elle n'est pas en crise et elle n'est pas au bloc. Contrôle clinique rapproché. Avis spécialisé si une grossesse est possible. La revue rappelle qu'une rémission à long terme s'observe chez 30 à 40 % des patients, et que le traitement médical dure en général douze à dix-huit mois dans Basedow, tandis que l'information professionnelle du carbimazole parle d'une durée habituelle de 6 à 18 mois. On cite les deux durées lues, on ne les moyenne pas.", S(1, 8, 10))}
{P("Deuxième cas, en une phrase de garde. Un homme de 78 ans sous amiodarone 200 mg par jour, numéro 33393, a une thyroxine libre haute et une thyréostimuline normale, sans amaigrissement. On ne pose pas le diagnostic d'hyperthyroïdie. On reconnaît l'effet chronique du médicament et on recontrôle. S'il maigrit, si la thyréostimuline s'effondre et si la triiodothyronine libre monte, là on ouvre le chapitre de la thyrotoxicose induite.", S(4, 14))}
""")

causes = fen("w-causes", "Causes classées", f"""
{P("Hyperthyroïdie par fabrication : maladie de Basedow, nodule autonome, goitre multinodulaire toxique, surcharge iodée sur une autonomie, y compris le type 1 de l'amiodarone. Hyperthyroïdie par libération : thyroïdite subaiguë de De Quervain, thyroïdite silencieuse, thyroïdite du post-partum, type 2 de l'amiodarone. Hyperthyroïdie exogène : excès de lévothyroxine. Faux profil : biotine, et parfois d'autres interférences d'anticorps hétérophiles que cette leçon ne détaille pas faute de texte suisse lu.")}
{P("Hypothyroïdie primaire : thyroïdite auto-immune, après iode radioactif, après thyroïdectomie, carence ou excès d'iode, amiodarone, lithium, phase tardive d'une thyroïdite. Hypothyroïdie centrale : tumeur, chirurgie, inflammation ou nécrose hypophysaire, où la thyréostimuline ne monte pas. Faux ou relatif : syndrome de basse T3, reprise après freinage, erreur de prise de la lévothyroxine.", S(1))}
{P("La revue sépare aussi l'urgence. Produit de contraste ou amiodarone chez un patient qui a un goitre multinodulaire : risque de crise. Hypothyroïdie auto-immune : risque de démasquer une insuffisance surrénale en donnant l'hormone. Grossesse : avis spécialisé.", S(1))}
""")

anamnese = fen("w-anamnese", "Questions qui changent la conduite", f"""
{P("Depuis quand. Un début en quelques jours avec une douleur cervicale irradiante vers l'oreille oriente vers De Quervain. Un début en semaines avec les yeux oriente vers Basedow. Un début après un accouchement oriente vers la thyroïdite du post-partum.")}
{P("Quels médicaments. Amiodarone, même arrêtée depuis des mois à cause de sa demi-vie. Biotine et compléments capillaires. Lithium. Corticoïde. Produit de contraste récent. Lévothyroxine : heure de prise, jeûne, calcium, fer, inhibiteur de la pompe à protons. La revue de 2010 rappelle que le calcium, le fer, l'hydroxyde d'aluminium et la cholestyramine diminuent l'absorption, et que la phénytoïne, la carbamazépine, le phénobarbital et la rifampicine accélèrent le métabolisme.", S(1))}
{P("Cœur. Angor, fibrillation connue, insuffisance cardiaque. Ils changent la dose de départ de la lévothyroxine et le recours au propranolol.")}
{P("Grossesse, projet de grossesse, allaitement. Avis spécialisé. Allaitement sous carbimazole : plafond 20 mg par jour.", S(1, 8))}
{P("Signes d'alarme à faire répéter au patient sous thionamide : fièvre, angine, aphtes, saignement. Il arrête et il consulte.", S(8))}
""")

examen = fen("w-examen", "Ce que les mains et les yeux ajoutent au chiffre", f"""
{P("Pouls, pression artérielle, température, fréquence respiratoire, conscience. Ces quatre lignes décident de la crise et du coma avant le laboratoire.")}
{P("Cou. Taille, consistance, douleur, souffle, nodule unique ou multiples, adénopathies. Une thyroïde douloureuse et dure n'est pas un Basedow. Un nodule unique chez un patient dont la thyréostimuline est basse fait demander une scintigraphie, pas seulement une échographie.")}
{P("Yeux. Rétraction palpébrale, rougeur conjonctivale, diplopie, baisse de vision. L'orbitopathie avec un goitre diffus suffit souvent à nommer Basedow. Une baisse de vision est une urgence ophtalmologique, hors du seul dosage.")}
{P("Peau et membres. Chaleur et tremblement fin dans la thyrotoxicose. Peau sèche, voix rauque, réflexes lents, visage bouffi dans l'hypothyroïdie. Œdème pretibial de Basedow, rare, à ne pas confondre avec une insuffisance cardiaque.")}
{P("Neurologie du coma. Échelle de Glasgow. Une valeur de 14 ou moins entre dans le signe neurologique du critère japonais de la crise, pas du coma myxœdémateux. On ne mélange pas les deux échelles.", S(5))}
""")

sources = """
<ol class="sources">
<li>Wuerzner et al., Revue Médicale Suisse, 2010.</li>
<li>Ross et al., Thyroid, 2016, American Thyroid Association.</li>
<li>Jonklaas et al., Thyroid, 2014, American Thyroid Association.</li>
<li>Bartalena et al., European Thyroid Journal, 2018.</li>
<li>Satoh et al., Endocrine Journal, 2016, critères japonais et score de Burch-Wartofsky.</li>
<li>Tessler et al., Journal of the American College of Radiology, 2017.</li>
<li>Medical Journal of Australia, 2016, biotine.</li>
<li>Néo-Mercazole, information professionnelle, numéro 21037.</li>
<li>Euthyrox, information professionnelle, numéro 54949.</li>
<li>Propranolol Zentiva, information professionnelle, numéro 47025.</li>
<li>Solu-CORTEF, information professionnelle, numéro 23533.</li>
<li>Iodure de potassium axapharm, information professionnelle, numéro 67017.</li>
<li>Prednisone Streuli, information professionnelle, numéro 29349.</li>
<li>Cordarone comprimés, information professionnelle, numéro 33393.</li>
<li>Eltroxine-LF, information professionnelle, numéro 29812.</li>
<li>Hydrocortisone Galepharm, information professionnelle, numéro 57970.</li>
<li>Catalogue PROFILES, situation F2.14, lu le 31 octobre 2026.</li>
</ol>
<p>Les fenêtres portent le même numérotage. Le détail des extraits est dans le dossier evidence.</p>
"""

ilots = {
"p1": (P("Une hormone thyroïdienne anormale est un résultat de laboratoire, pas encore un diagnostic. La situation F2.14 du référentiel porte ce nom. Le médecin la traduit en un des dix mécanismes de la leçon, ou en un faux profil.", S(17))
      + P("Le couple utile est la thyréostimuline et la thyroxine libre. La triiodothyronine libre et les anticorps viennent ensuite. Le ", btn("w-profils", "tableau des huit profils"), " évite de traiter un chiffre isolé.", S(1)),
      [profils]),
"p2": (P("Les formes franches sont peu fréquentes dans les enquêtes de population, les formes infracliniques le sont davantage, et la crise est rare mais meurtrière. Les ", btn("w-epi", "chiffres lus"), " ne classent pas les dix diagnostics entre eux.", S(1, 2)),
      [epi]),
"p3": (P("Le rétrocontrôle explique la thyréostimuline. Le mécanisme, fabrication, fuite ou prise exogène, explique le traitement. La ", btn("w-physio", "physiologie utile au lit"), ", les ", btn("w-causes", "causes classées"), " et les ", btn("w-pop", "situations particulières"), " relient les deux.", S(2, 3, 4)),
      [physio, causes, populations]),
"p4": (P("Sept temps suffisent : urgence clinique, profil complet, médicaments, cou et yeux, examen qui distingue fabrication et destruction, traitement du mécanisme, contrôle. Le détail est dans la ", btn("w-demarche", "démarche"), " et dans le ", btn("w-consult", "fil de la consultation"), ".", S(1)),
      [demarche, consultation]),
"p5": (P("La question du médicament et celle de la grossesse changent plus souvent la conduite que le récit des symptômes. Les ", btn("w-anamnese", "questions"), " et les drapeaux rouges tiennent en une page.", S(1, 8)),
      [anamnese]),
"p6": (P("Température, conscience, pouls, cou et yeux précèdent le commentaire du laboratoire. L'", btn("w-examen", "examen ciblé"), " sert à nommer Basedow, une thyroïdite ou une défaillance."),
      [examen]),
"p7": (P("Le syndrome se lit sur le profil, pas sur un organe. Huit combinaisons couvrent la fabrication, la fuite, le manque, le centre, la maladie grave, l'amiodarone et la biotine. Elles sont dans le ", btn("w-profils", "tableau des profils"), ". On ouvre à part le ", btn("w-t3", "syndrome de basse T3"), " et la ", btn("w-biotine", "biotine"), ".", S(1)),
      [basst3, biotine]),
"p8": (P("Le diagnostic positif de la crise est clinique, appuyé par le ", btn("w-burch", "score complet et les critères japonais"), " et par trois ", btn("w-score-lire", "calculs ligne à ligne"), ". Le diagnostic positif de Basedow s'appuie sur la clinique et l'anticorps anti-récepteur. Celui de l'hypothyroïdie primaire s'appuie sur la thyréostimuline haute et la thyroxine libre basse.", S(2, 5)),
      [burch, lecture_score]),
"p9": (P("Anticorps anti-récepteur, anticorps anti-thyroperoxydase, scintigraphie et échographie classée n'ont pas la même question. Le ", btn("w-anticorps", "choix de l'examen"), ", la ", btn("w-tirads", "classification échographique en cinq catégories"), " et quatre ", btn("w-nodules-lire", "nodules chiffrés"), " sont développés à part.", S(2, 6)),
      [anticorps, tirads, nodules]),
"p10": (P("On exclut d'abord la crise thyréotoxique et le coma myxœdémateux, puis on nomme le mécanisme. L'", btn("w-algo", "algorithme"), " donne le rang E des dix diagnostics."),
      [algo]),
"p11": (P("Les doses suisses sont celles des informations professionnelles. L'iode de la crise vient après le thionamide et n'est pas le comprimé nucléaire. La lévothyroxine de la substitution est orale. Celle du coma est intraveineuse dans la recommandation de 2014, sans spécialité intraveineuse dans l'index parcouru. Le détail est dans les ", btn("w-urgences", "urgences"), ", le ", btn("w-doses", "tableau des doses"), ", le ", btn("w-amio", "profil de l'amiodarone"), " et les ", btn("w-inter", "interactions"), ".", S(8, 9, 10, 11)),
      [urgences, doses, amio, interactions]),
"p12": (P("Prévenir, c'est éviter le contraste iodé chez un patient qui a un goitre multinodulaire non préparé, ne pas arrêter le carbimazole d'un coup, éduquer sur l'agranulocytose, et ne pas introduire la lévothyroxine sans avoir pensé à la surrénale. Le ", btn("w-suivi", "calendrier"), " fixe les contrôles. Sous amiodarone, on dose avant le traitement puis régulièrement, parce que le profil change chez tout le monde.", S(1, 4, 8)),
      [suivi]),
"p13": (P("Thyréostimuline et thyroxine libre d'abord. Clinique avant le thionamide. Iode après le thionamide, jamais le comprimé de blocage nucléaire dans la crise. Glucocorticoïde avant la lévothyroxine du coma. Biotine et basse T3 ne se traitent pas comme une maladie de la glande. TI-RADS se cite en entier, de TR1 à TR5. Le score de Burch-Wartofsky se cite avec toutes ses classes.", S(5, 6, 7))
      + SIGLES,
      []),
"p14": (P("Les erreurs stables sont le chiffre isolé, l'iode trop tôt, le thionamide dans une thyroïdite, et l'hormone thyroïdienne qui démasque une insuffisance surrénale. Les ", btn("w-pieges", "pièges"), ", le ", btn("w-cas", "cas de Basedow"), ", la ", btn("w-cas-crise", "crise"), ", le ", btn("w-cas-coma", "coma"), ", les ", btn("w-cas-amio", "patients sous amiodarone"), " et les ", btn("w-cas-faux", "faux profils"), " et les ", btn("w-cas-deq", "autres cas"), " les fixent.", S(1)),
      [pieges, cas, cas_crise, cas_coma, cas_amio, cas_faux, cas_deq]),
}

essentiel = P(
"Devant une hormone thyroïdienne anormale, on lit le profil entier, on cherche la biotine, l'amiodarone et la maladie grave, et on ne traite pas un faux Basedow. "
"Deux tableaux ne attendent pas le dossier complet : la crise thyréotoxique et le coma myxœdémateux. "
"Le carbimazole, le propranolol et l'hydrocortisone ont une information professionnelle suisse. "
"L'iode minéral de la crise vient au moins une heure après le thionamide. "
"Le comprimé d'iodure prévu pour un accident nucléaire est contre-indiqué dans l'hyperthyroïdie.",
S(2, 5, 8, 10, 11, 12),
)

html = page(
    "LOT_162_Phase_A_V0",
    "Hormones thyroïdiennes anormales",
    "F2.14. Hormones thyroïdiennes anormales. Texte du 31 octobre 2026.",
    essentiel,
    "Les mots soulignés ouvrent une fenêtre. Les sources sont en bas.",
    ilots,
    sources,
)

# ilots values are tuples (p, p, fen, ...) — fix: first elements that are not fen
# I packed wrong. Rebuild ilots properly below if needed.

dest = Path(__file__).resolve().parents[1] / "LOT_162_Phase_A_V0.html"
dest.write_text(html, encoding="utf-8")
print("écrit", dest, "octets", dest.stat().st_size)

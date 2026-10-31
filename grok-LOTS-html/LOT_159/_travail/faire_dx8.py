#!/usr/bin/env python3
"""DX.8 Hémochromatose héréditaire."""
from base_dx import P, W, construire, A
from moteur import S

EASL = A("European Association for the Study of the Liver", "EASL")
TS = "saturation de la transferrine"
FE = "ferritine"

def F(point, ident, titre, textes, *refs):
    return point, W(ident, titre, "\n".join(P(t, *refs) for t in textes))

fen = []
fen.append(F(1, "d8", "Définition", [
    f"L'hémochromatose héréditaire, dans le texte {EASL} de juin 2022, se reconnaît d'abord par le fer du sang, pas par une biopsie systématique. Chez l'homozygote p.Cys282Tyr, des seuils de {TS} et de {FE} suffisent au diagnostic provisoire.",
    "Un autre génotype du gène ne suffit pas : il faut le fer du foie à l'imagerie ou à la biopsie. Une ferritine isolée, sans saturation, ne porte pas le nom.",
], 6))
fen.append(F(3, "ph8", "Physiopathologie", [
    "Le fer s'accumule parce que l'absorption n'est plus freinée comme elle devrait l'être. Il se dépose dans le foie. La ferritine monte avec les réserves. La saturation monte avec le fer qui circule, lié à la transferrine.",
    "La ferritine monte aussi avec l'inflammation, l'alcool, la stéatose, la cytolyse. C'est pourquoi elle ne se lit jamais seule. La saturation du matin distingue l'overload du bruit.",
    "Le jeûne n'améliore pas le rendement diagnostique de la saturation. Le matin, oui. Un prélèvement de fin d'après-midi ne se compare pas aux seuils comme s'il était du matin.",
], 6))
fen.append(F(3, "et8", "Qui a le diagnostic provisoire, qui ne l'a pas", [
    f"Saturation élevée : au-dessus de 50 % chez l'homme, au-dessus de 45 % chez la femme. En dessous, on ne part pas vers le gène sur une ferritine seule.",
    f"Homozygote p.Cys282Tyr, femme : saturation au-dessus de 45 % et {FE} au-dessus de 200 µg/l. Homme, ou femme ménopausée : saturation au-dessus de 50 % et {FE} au-dessus de 300 µg/l. Les deux chiffres sont exigés. L'un sans l'autre ne suffit pas.",
    "Autre génotype : fer hépatique en imagerie ou en histologie. On ne pose pas le nom sur le papier du laboratoire de génétique seul.",
    "Pas d'hépatite virale, pas d'obstacle, pas d'alcool comme explication unique d'une ferritine, tant que la saturation n'a pas été vue. On ne saigne pas une inflammation.",
], 6))
fen.append(F(8, "dg8", "Les seuils, sans en retirer", [
    f"Premier geste, toujours : {TS} et {FE}, le matin. Le jeûne n'est pas requis.",
    f"Femme non ménopausée, homozygote : saturation au-dessus de 45 % et ferritine au-dessus de 200 µg/l. Les deux.",
    f"Homme ou femme ménopausée, homozygote : saturation au-dessus de 50 % et ferritine au-dessus de 300 µg/l. Les deux. Une femme ménopausée ne garde pas le seuil de 45 % et 200 µg/l.",
    "Saturation au-dessus du seuil mais ferritine en dessous : pas le diagnostic provisoire. Ferritine au-dessus et saturation normale : pas le diagnostic. On cherche l'inflammation.",
    "Génotype autre que l'homozygotie p.Cys282Tyr : l'imagerie du fer ou la biopsie. Un hétérozygote avec une ferritine haute n'est pas « une petite hémochromatose ».",
], 6))
fen.append(F(11, "sa8", "Saignées, cibles lues", [
    f"Induction : ferritine en dessous de 50 µg/l. Entretien : ferritine en dessous de 100 µg/l. Deux cibles, deux temps. S'arrêter à 100 pendant l'induction laisse du fer. Viser 50 toute la vie épuise sans texte.",
    "Le rythme et le volume de la saignée ne sont pas dans l'extrait lu. On ne les invente pas. On écrit la cible, et le geste se fait selon le protocole du service.",
    "On ne dose pas une hormone du fer qui n'est pas le premier pas du texte. Le premier pas reste la saturation et la ferritine.",
], 6))
fen.append(F(4, "de8", "Démarche", [
    f"Enzyme anormale ou ferritine demandée pour une fatigue : saturation du matin et ferritine. Si la saturation est haute, génotype. Si l'homozygotie et les deux seuils sont là, diagnostic provisoire, pas de biopsie obligatoire pour le nom. Si le génotype est autre, fer du foie.",
    "En parallèle, on ne rate pas l'alcool, la stéatose, le virus, l'inflammation, qui expliquent beaucoup de ferritines. La saturation basse les laisse en place et écarte le diagnostic provisoire.",
], 5, 6))
fen.append(F(5, "an8", "Anamnèse", [
    "Fatigue, arthralgies, peau, diabète, famille déjà saignée, alcool en mots, règles encore présentes ou non. La ménopause change le seuil de la femme. On la demande, on ne la suppose pas à 48 ans.",
    "Un parent homozygote ne rend pas le consultant homozygote. On génotype la personne qui est dans la pièce.",
], 6))
fen.append(F(6, "ex8", "Examen", [
    "Peau bronzée, foie, diabète déjà connu, articulations. L'examen peut être normal au moment où la biologie est déjà décisive. On ne attend pas la mélanodermie pour doser la saturation.",
], 6))
fen.append(F(7, "sy8", "Syndromes", [
    "Découverte biologique chez un homme de 45 ans, enzymes un peu hautes. Fatigue et ferritine chez une femme non ménopausée. Ferritine très haute d'un syndrome inflammatoire avec saturation normale : ce n'est pas ce diagnostic. Trois portes, une seule se saigne selon les cibles.",
], 6))
fen.append(F(9, "la8", "Examens", [
    f"Matin : saturation et ferritine. Puis le gène si la saturation est haute. Imagerie du fer ou biopsie si le gène n'est pas l'homozygotie p.Cys282Tyr. Enzymes, pour le motif du chapitre. On ne commence pas par la biopsie chez l'homozygote qui a déjà les deux seuils.",
], 6))
fen.append(F(10, "ar8", "Arbre", [
    f"Saturation sous le seuil du sexe : stop pour ce diagnostic, chercher une autre cause de la ferritine ou de l'enzyme.",
    f"Saturation haute, homozygote, deux seuils remplis : diagnostic provisoire, saignées vers moins de 50 µg/l puis entretien sous 100 µg/l.",
    "Saturation haute, génotype autre : fer du foie avant le nom et avant de présenter la saignée comme le traitement de cette maladie.",
    "Inflammation évidente, saturation normale : pas de saignée pour « faire baisser la ferritine ».",
], 6))
fen.append(F(12, "pv8", "Famille et suite", [
    "Le texte lu ne donne pas un calendrier de dépistage familial chiffré. On ne l'invente pas. On dit au consultant que le premier pas, pour un apparenté, reste la saturation du matin et la ferritine, pas une saignée d'avance.",
    "On ne promet pas un intervalle de dépistage du carcinome qui n'est pas dans l'extrait. La question se pose au spécialiste si la fibrose est avancée. Elle ne se chiffre pas ici.",
], 6))
fen.append(F(13, "cl8", "Points de la copie", [
    "Matin, pas besoin de jeûne. Homme et femme ménopausée : saturation au-dessus de 50 % et ferritine au-dessus de 300 µg/l. Femme : saturation au-dessus de 45 % et ferritine au-dessus de 200 µg/l. Homozygote seulement pour le diagnostic provisoire sans imagerie. Saignée : sous 50 µg/l puis sous 100 µg/l.",
], 6))
fen.append(F(14, "pi8", "Pièges", [
    "Saigner une ferritine d'inflammation. Appliquer 200 µg/l à un homme. Appliquer 300 µg/l à une femme non ménopausée et le trouver « normal » alors que 250 serait déjà au-dessus de 200. Oublier le matin. Biopsier un homozygote qui a déjà les deux seuils. Appeler hémochromatose un hétérozygote sans fer hépatique.",
], 6))
fen.append(F(14, "cas8", "Cas corrigé", [
    f"Homme de 47 ans, alanine à 1,6 fois la limite, ferritine 900 µg/l, saturation du matin 62 %. Homozygote p.Cys282Tyr. Saturation au-dessus de 50 %, ferritine au-dessus de 300 µg/l. Diagnostic provisoire. Pas de biopsie pour poser le nom. Cible d'induction : ferritine sous 50 µg/l, puis entretien sous 100 µg/l.",
    f"Femme de 36 ans, règles présentes, ferritine 280 µg/l, saturation du matin 42 %. 42 n'est pas au-dessus de 45. 280 est au-dessus de 200, mais les deux seuils sont exigés. Pas de diagnostic provisoire. On ne génotype pas « pour voir » comme si la saturation était haute. On cherche l'inflammation et la stéatose.",
    f"Femme de 61 ans, ménopausée, saturation 55 %, ferritine 400 µg/l, homozygote. On utilise le seuil de l'homme et de la femme ménopausée : 50 % et 300 µg/l. Les deux sont dépassés. Diagnostic provisoire. Le seuil de 45 % et 200 µg/l serait trop bas pour elle et n'est pas le texte.",
    "Frère hétérozygote, ferritine 500 µg/l, saturation 48 %. Pas le diagnostic provisoire : il n'est pas homozygote, et sa saturation d'homme n'est pas au-dessus de 50 %. S'il fallait aller plus loin, ce serait le fer du foie, pas une saignée sur le nom de la sœur.",
], 6))

LONGS = [
    "Le matin n'est pas un détail. La page dit que le prélèvement de saturation se fait le matin. Un résultat de 16 heures ne se compare pas aux pourcentages comme un résultat du matin. On le refait.",
    "Le jeûne n'améliore pas le rendement. Imposer un jeûne et retarder le prélèvement n'est pas le texte. Le dire au patient évite un faux obstacle.",
    "Saturation d'homme à 50 % pile. Le texte dit au-dessus de 50 %. L'égalité n'est pas au-dessus. On ne coche pas. À 51 %, on coche.",
    "Saturation de femme à 45 % pile. Au-dessus de 45 % est exigé. 45 % ne suffit pas. 46 % oui. La borne est stricte.",
    "Ferritine de femme à 200 µg/l pile. Le texte dit au-dessus de 200 µg/l. L'égalité ne suffit pas. 210 µg/l oui, si la saturation est aussi au-dessus de 45 % et si elle est homozygote.",
    "Ferritine d'homme à 300 µg/l pile. Même logique : au-dessus de 300. 300 ne suffit pas. 310 oui, avec la saturation au-dessus de 50 % et l'homozygotie.",
    "Femme de 50 ans encore réglée. Elle n'est pas dans le groupe ménopausé. Seuils 45 % et 200 µg/l. Lui appliquer 50 % et 300 µg/l la sous-diagnostique. Lui appliquer ces seuils hauts « par sécurité » est une erreur de texte.",
    "Femme de 58 ans ménopausée. Seuils 50 % et 300 µg/l. Lui laisser 45 % et 200 µg/l la sur-diagnostique. La ménopause se note dans le dossier avant le calcul.",
    "Homme de 25 ans. Même seuil que l'homme plus âgé : au-dessus de 50 % et, s'il est homozygote, ferritine au-dessus de 300 µg/l. L'âge ne crée pas un troisième barème.",
    "Homozygote, saturation 70 %, ferritine 180 µg/l, femme. La saturation dépasse 45 %. La ferritine ne dépasse pas 200. Les deux sont exigés. Pas de diagnostic provisoire. On surveille, on ne saigne pas pour un nom qui n'est pas posé.",
    "Homozygote, saturation 40 %, ferritine 800 µg/l, homme. La ferritine est très au-dessus de 300. La saturation n'est pas au-dessus de 50 %. Pas de diagnostic provisoire. 800 µg/l d'inflammation ou d'alcool reste possible. On ne saigne pas.",
    "Hétérozygote, saturation 60 %, ferritine 700 µg/l. Les chiffres d'homme seraient « bons » pour un homozygote. Il ne l'est pas. Il faut le fer du foie. La saignée ne se présente pas comme le traitement déjà indiqué par le seul génotype partiel.",
    "Homozygote composé ou autre variant. Le texte est clair : les autres génotypes exigent le fer hépatique. On ne les fait pas entrer dans le diagnostic provisoire par analogie.",
    "Pas de mutation, saturation haute, ferritine haute. Ce n'est pas l'hémochromatose HFE provisoire. On cherche une autre surcharge, une hématopoïèse, une hépatite. On ne pose pas le nom.",
    "Induction et entretien. Sous 50 µg/l, puis sous 100 µg/l. Un patient à 80 µg/l en cours d'induction n'a pas fini. Un patient à 80 µg/l en entretien est dans la cible, puisqu'elle est sous 100. Le temps du traitement change le jugement du même chiffre.",
    "Ferritine à 50 µg/l pile en induction. Le texte dit en dessous de 50. L'égalité n'est pas en dessous. On continue l'induction. À 40 µg/l, la cible est atteinte.",
    "Ferritine à 100 µg/l pile en entretien. En dessous de 100 est la cible. 100 n'est pas en dessous. 90 l'est. On ne arrondit pas.",
    "Volume de poche et rythme hebdomadaire : absents de l'extrait. Les écrire serait une invention. La copie juste donne la cible en µg/l et dit que le rythme est celui du service.",
    "Hormone du fer. Le premier pas du texte n'est pas ce dosage. Le demander à la place de la saturation retarde. On ne le présente pas comme nécessaire au diagnostic provisoire.",
    "Biopsie chez l'homozygote qui remplit les deux seuils. Le texte dit que les paramètres sériques suffisent. Biopsier pour « confirmer le nom » n'est pas demandé. Biopsier pour une autre question, fibrose ou autre maladie, est une autre discussion, pas ce seuil.",
    "Imagerie du fer. Elle devient nécessaire quand le génotype n'est pas l'homozygotie. Elle ne remplace pas la saturation du matin chez quelqu'un qui n'a pas encore eu le premier pas.",
    "Alcool et ferritine. L'alcool monte la ferritine. Si la saturation du matin est basse, on traite l'alcool, pas le fer. Si la saturation est haute et l'homozygotie là, les deux peuvent coexister : on ne choisit pas le plus facile et on ne nie pas l'autre.",
    "Stéatose et ferritine. Très fréquent. Saturation d'abord. Une saturation à 30 % avec une ferritine à 400 µg/l n'est pas ce diagnostic. Le FIB-4, s'il se calcule, appartient au fichier de la stéatose, pas à la place de la saturation.",
    "Virus et ferritine. Une hépatite peut monter la ferritine. La saturation et le virus se demandent tous les deux. On ne saigne pas un virus.",
    "Inflammation, protéine réactive haute, ferritine haute, saturation normale. Mécanisme clair. Pas de saignée. Pas de génotype en urgence.",
    "Cytolyse très haute, ferritine qui suit les enzymes, saturation normale. Le fer sort des cellules. Ce n'est pas une surcharge. On traite la cause de la nécrose.",
    "Obstacle et ictère. La ferritine n'est pas l'outil. Tokyo l'est. On ne retarde pas un drainage pour un gène.",
    "Hépatite auto-immune. Le score de Hennes ne contient pas de ferritine. Une ferritine haute ne donne pas de point. La saturation évite de saigner une inflammation immune.",
    "Wilson. Un jeune avec hémolyse et enzymes. La ferritine n'est pas Leipzig. On ne choisit pas le fer parce que le dosage est plus facile.",
    "Insuffisance aiguë. La ferritine monte avec la nécrose. Elle ne pose pas l'hémochromatose aux urgences. King et Clichy d'abord si l'INR et la conscience bougent.",
    "Famille. On n'écrit pas un pourcentage de dépistage qui n'est pas dans l'extrait. On écrit le premier pas : saturation du matin et ferritine, chez l'adulte concerné, pas une saignée préventive.",
    "Carcinome. L'extrait lu ne donne pas l'intervalle. On ne l'invente pas. On ne prétend pas que la question n'existe pas : on la laisse au spécialiste si la fibrose est là, sans chiffre.",
    "La copie minimale. Sexe et ménopause, saturation du matin avec le bon seuil, ferritine avec le bon seuil, homozygote ou non, cible 50 puis 100 si l'on traite. Cinq éléments. Le volume de la poche n'en fait pas partie.",
    "La copie qui perd les points. « Ferritine haute, saignée ». Il manque la saturation. « Femme, 300 µg/l, donc non ». Faux si elle n'est pas ménopausée et que 250 dépasse 200. « Hétérozygote, c'est pareil ». Faux. « Jeûne obligatoire ». Faux. « Sous 100 µg/l dès le début ». Faux, l'induction va sous 50.",
    "Lettre. Âge, sexe, ménopause, heure du prélèvement, saturation, ferritine, génotype, décision (provisoire, ou fer du foie, ou autre cause), cible si saignée. Une lettre sans l'heure du matin et sans la ménopause est incomplète.",
    "Ordonnance de saignée. Cible écrite : induction sous 50 µg/l, entretien sous 100 µg/l. Pas de volume inventé. Prochain dosage de ferritine daté. Pas de conseil d'arrêter le matin sous prétexte que le jeûne ne sert à rien : le matin reste.",
]

CAS = [
    "Cas homme limite. Saturation 50 %, ferritine 450 µg/l, homozygote. Saturation non au-dessus de 50. Pas de diagnostic provisoire malgré la ferritine. On refait un matin. On ne saigne pas sur l'égalité.",
    "Cas homme juste au-dessus. Saturation 51 %, ferritine 301 µg/l, homozygote. Les deux sont au-dessus. Diagnostic provisoire. La marge est d'une unité. On recopie les chiffres, on ne les arrondit pas vers le bas pour éviter la saignée.",
    "Cas femme limite. Saturation 45 %, ferritine 260 µg/l, non ménopausée, homozygote. Saturation non au-dessus de 45. Stop. La ferritine seule ne décide pas.",
    "Cas femme juste au-dessus. Saturation 46 %, ferritine 201 µg/l, non ménopausée, homozygote. Diagnostic provisoire. On n'exige pas 300 µg/l.",
    "Cas ménopause mal notée. Femme de 62 ans, plus de règles, saturation 48 %, ferritine 350 µg/l, homozygote. 48 n'est pas au-dessus de 50. 350 est au-dessus de 300. Il manque la saturation. Si on avait gardé le seuil de 45 %, on l'aurait à tort déclarée. Le bon seuil la laisse en dehors.",
    "Cas induction. Ferritine de départ 1 200 µg/l, après plusieurs saignées 70 µg/l. 70 n'est pas sous 50. L'induction continue. Dire « presque » n'est pas la cible.",
    "Cas entretien. Ferritine 70 µg/l après une induction qui était passée sous 50. 70 est sous 100. L'entretien est dans la cible. On ne reprend pas l'induction parce que 70 est au-dessus de 50.",
    "Cas confusion des cibles. Quelqu'un écrit « toujours sous 50 ». Faux pour l'entretien. Quelqu'un écrit « toujours sous 100 ». Faux pour l'induction. Les deux phrases se disent avec leur temps.",
    "Cas inflammation. Protéine réactive haute, ferritine 1 000 µg/l, saturation du matin 22 %, homme. Très loin de 50 %. Pas de gène en urgence. Pas de saignée. On traite l'inflammation.",
    "Cas alcool. Homme, consommation au-dessus du seuil de maladie alcoolique dit en mots, ferritine 600 µg/l, saturation 28 %. On s'occupe de l'alcool. La saturation protège d'une saignée inutile.",
    "Cas coexistence. Homme, alcool et homozygotie, saturation 65 %, ferritine 1 000 µg/l. Les deux seuils sont là. Diagnostic provisoire en plus de l'alcool. On ne choisit pas. Abstinence et cible de ferritine.",
    "Cas stéatose. Diabète, ferritine 450 µg/l, saturation 33 %, femme. Pas ce diagnostic. Le fichier de la stéatose reprend la main. Pas de saignée « métabolique ».",
    "Cas virus B. Antigène présent, ferritine 500 µg/l, saturation 30 %. On classe la phase du virus. On ne saigne pas.",
    "Cas hétérozygote insistant. Il a lu que la famille est malade. Saturation 40 %, ferritine 320 µg/l. Ni l'homozygotie ni les seuils d'homme. On explique. On ne saigne pas pour calmer l'inquiétude.",
    "Cas autre génotype avec fer hépatique montré. Alors le texte autorise le diagnostic, parce que le fer du foie est là. La saignée se discute comme traitement de la surcharge montrée. On ne l'a pas appelée provisoire sur le seul sang.",
    "Cas autre génotype sans imagerie. On ne pose pas le nom. On demande l'imagerie ou la biopsie. La copie qui saute cette étape a retiré une phrase du texte.",
    "Cas biopsie inutile. Homme homozygote, saturation 80 %, ferritine 2 000 µg/l. Le texte dit que c'est suffisant. Proposer la biopsie pour le nom est en trop. La cible de saignée suffit pour la décision de traiter.",
    "Cas prélèvement de 18 heures, saturation 48 %, homme. On ne conclut pas. On refait le matin. 48 pourrait monter ou non. Le texte a choisi le matin pour une raison.",
    "Cas jeûne refusé. Le patient a mangé. On prélève quand même le matin. Le jeûne n'améliore pas le rendement. Retarder de 24 heures pour un jeûne n'est pas le texte.",
    "Cas enzyme du chapitre. Alanine à deux fois la limite, le reste du bilan de stéatose banal, mais saturation du matin 58 % chez un homme. On ne s'arrête pas au FIB-4. On demande la ferritine et le gène. L'enzyme était le motif, le fer est le diagnostic.",
    "Cas ferritine demandée sans enzyme. Fatigue, ferritine 700 µg/l, saturation non faite. Le premier pas manque. On ne génotype pas encore. On complète le matin.",
    "Cas famille déjà saignée. La mère est homozygote. Le fils a une saturation du matin à 35 %. Il n'entre pas. On ne le saigne pas « comme maman ».",
    "Cas cible dépassée vers le bas. Entretien, ferritine 20 µg/l, fatigue nouvelle. La cible d'entretien est sous 100, pas « le plus bas possible ». Descendre très sous 50 en entretien n'est pas demandé. On espace. On ne invente pas un plancher chiffré autre que les deux cibles lues.",
    "Lettre type positive. Homme, 52 ans, matin, saturation 64 %, ferritine 880 µg/l, homozygote p.Cys282Tyr, diagnostic provisoire, induction vers moins de 50 µg/l, entretien ensuite sous 100 µg/l, pas de volume inventé.",
    "Lettre type négative. Femme non ménopausée, matin, saturation 38 %, ferritine 320 µg/l, pas de diagnostic, pas de saignée, recherche d'une inflammation ou d'une stéatose, génotype non indiqué par la saturation.",
    "Ce que l'on ne retire pas. Les deux seuils de saturation, 45 et 50. Les deux ferritines, 200 et 300. La distinction homozygote et autres génotypes. Le matin. L'inutilité du jeûne. Les deux cibles de saignée, 50 puis 100. En retirer un change la maladie.",
    "Mémo. Premier pas : saturation et ferritine, le matin, jeûne inutile. Élevée : plus de 50 % chez l'homme, plus de 45 % chez la femme. Provisoire seulement si homozygote, avec ferritine au-dessus de 200 µg/l chez la femme et au-dessus de 300 µg/l chez l'homme ou la femme ménopausée. Sinon fer du foie. Saignée : sous 50 µg/l puis sous 100 µg/l. Pas de volume inventé. Pas de calendrier de carcinome inventé.",
    "Pourquoi deux chiffres et pas un. La saturation sans ferritine dit que le fer circule, pas que les réserves sont déjà au seuil du diagnostic provisoire. La ferritine sans saturation dit que quelque chose élève les réserves ou l'inflammation, pas que c'est cette maladie. Le texte de 2022 les a mis ensemble. Les séparer est la faute.",
    "Pourquoi l'homozygotie seulement. Le diagnostic provisoire sur le sang est une exception écrite pour p.Cys282Tyr à l'état homozygote. L'étendre à toute anomalie du gène retire la phrase sur l'imagerie et la biopsie. Cette phrase protège des saignées inutiles.",
    "Pourquoi le matin. La saturation bouge dans la journée. Le texte a choisi un moment. Un résultat hors de ce moment n'est pas faux, il n'est pas comparable. On le répète. On ne moyenne pas un soir et un matin.",
    "Pourquoi le jeûne ne se exige pas. La page le dit : il n'améliore pas le rendement. Un protocole local qui l'impose quand même ne doit pas être enseigné comme la recommandation. On prévient le patient qu'il peut manger, et qu'il doit venir le matin.",
    "Parcours d'un homme positif, étape par étape. Enzyme anormale. Saturation du matin au-dessus de 50 %. Ferritine au-dessus de 300 µg/l. Génotype homozygote. Nom provisoire. Pas de biopsie pour ce nom. Induction jusqu'en dessous de 50 µg/l. Puis entretien en dessous de 100 µg/l. Huit étapes. En sauter une change la décision.",
    "Parcours d'une femme non ménopausée positive. Même logique avec 45 % et 200 µg/l. On écrit « non ménopausée » sur la feuille pour que le correcteur voie quel seuil a été choisi. Sans ce mot, 200 µg/l peut être lu comme une erreur.",
    "Parcours d'une femme ménopausée. On barre le seuil de 45 % et 200 µg/l. On prend 50 % et 300 µg/l. Si l'un des deux manque, on s'arrête. La ménopause n'est pas un détail gynécologique dans ce fichier : c'est un aiguillage.",
    "Parcours d'un hétérozygote. Saturation peut être haute. Cela ne suffit pas. On demande le fer du foie. S'il est absent, on ne saigne pas au nom de la famille. S'il est présent, le texte permet alors de parler de surcharge, pas du raccourci provisoire.",
    "Parcours d'une ferritine d'hôpital. Patient alité, infection, ferritine 1 500 µg/l, saturation 25 %. On traite l'infection. On ne fait pas venir le généticien le jour même. On refera la saturation le matin quand l'infection sera calme, si l'enzyme reste anormale.",
    "Parcours d'une enzyme très haute. Alanine à plusieurs milliers, ferritine qui suit, saturation normale. Nécrose, pas surcharge. Ischémie, virus, intoxication : les autres fichiers. La saignée n'a pas sa place aux urgences.",
    "Articulations et peau. Elles orientent l'anamnèse. Elles ne remplacent aucun seuil. Un patient bronzé avec une saturation à 30 % n'a pas le diagnostic provisoire. Un patient pâle avec les deux seuils et l'homozygotie l'a.",
    "Diabète. Il peut accompagner la surcharge avancée. Il ne se traite pas par la saignée seule, et la saignée ne se justifie pas par le diabète si la saturation est basse. Deux maladies, deux décisions.",
    "Contrôle après induction. La ferritine est à 40 µg/l. On passe à l'entretien, cible sous 100 µg/l. On ne continue pas le rythme d'induction jusqu'à une ferritine indosable. Le texte a deux cibles pour cette raison.",
    "Contrôle d'entretien trop haut. Ferritine remontée à 180 µg/l. 180 n'est pas sous 100. On resserre. On ne dit pas que 180 est acceptable parce que c'est moins que le 300 du diagnostic. Le 300 n'est plus le seuil une fois que l'on traite.",
    "Contrôle d'entretien correct. Ferritine 60 µg/l. Sous 100, au-dessus de la cible d'induction, et c'est normal : on n'est plus en induction. On espace selon le service. On ne réécrit pas 50 comme plafond permanent.",
    "Erreur de laboratoire. Ferritine rendue en ng/ml. C'est la même grandeur que µg/l. On ne multiplie pas par mille. On ne divise pas. Le seuil 300 µg/l se lit 300 ng/ml. Une conversion inventée fabrique une maladie ou l'efface.",
    "Erreur d'unité de saturation. 0,62 n'est pas 62 % si l'on oublie le facteur cent. On écrit le pourcent. Le texte parle en pourcent, au-dessus de 50 et de 45. Un 0,62 comparé à 50 est absurde et rassure à tort.",
    "Enfant et adolescent. L'extrait lu donne les seuils adultes, femme et homme. On ne les divise pas par deux pour un adolescent. On adresse. On ne saigne pas un adolescent sur un seuil bricolé.",
    "Grossesse. La ferritine baisse souvent. Une saturation se lit avec le spécialiste. Le cours ne donne pas un seuil de grossesse qui n'est pas dans l'extrait. On ne déclare pas la maladie sur la ferritine du premier trimestre.",
    "Après les saignées, l'enzyme. Si l'alanine était haute à cause du fer, elle peut baisser. Si elle reste haute, on cherche la stéatose, l'alcool, le virus, qui coexistent. Une enzyme normalisée ne prouve pas que la cible de ferritine est atteinte : on dose la ferritine, pas seulement l'alanine.",
    "Coexistence avec la cholangite biliaire primitive. Rare, possible. La phosphatase et les anticorps antimitochondries ne se traitent pas par la saignée. La saturation ne se traite pas par l'acide de l'information 60812. Deux fichiers, deux décisions.",
    "Ce que le correcteur compte. Bon seuil selon sexe et ménopause. Les deux paramètres, pas un. Homozygote nommé ou imagerie demandée. Cible d'induction distincte de l'entretien. Absence de volume inventé. Cinq coches. Une copie lyrique sans ces coches ne passe pas.",
    "Phrase d'ouverture de copie, modèle. « Saturation du matin 62 % chez un homme, ferritine 900 µg/l, homozygote p.Cys282Tyr : au-dessus de 50 % et de 300 µg/l, diagnostic provisoire, induction sous 50 µg/l puis entretien sous 100 µg/l. » Une phrase. Elle contient la décision.",
    "Phrase d'ouverture négative, modèle. « Femme non ménopausée, saturation du matin 42 %, ferritine 280 µg/l : la saturation n'est pas au-dessus de 45 %, pas de diagnostic provisoire, pas de saignée, on cherche une autre cause de la ferritine. » La ferritine au-dessus de 200 ne renverse pas la saturation.",
]

SCEN = [
    ("Homme, 44 ans, matin", "63 %", "740 µg/l", "homozygote", "diagnostic provisoire : 63 est au-dessus de 50 et 740 au-dessus de 300. Induction sous 50 µg/l."),
    ("Homme, 44 ans, matin", "49 %", "740 µg/l", "homozygote", "pas de provisoire : 49 n'est pas au-dessus de 50. La ferritine ne compense pas."),
    ("Femme non ménopausée, 33 ans", "47 %", "210 µg/l", "homozygote", "provisoire : au-dessus de 45 % et de 200 µg/l. On n'exige pas les seuils de l'homme."),
    ("Femme non ménopausée, 33 ans", "44 %", "900 µg/l", "homozygote", "pas de provisoire. 900 µg/l ne rachète pas une saturation à 44 %."),
    ("Femme ménopausée, 66 ans", "52 %", "310 µg/l", "homozygote", "provisoire avec les seuils 50 % et 300 µg/l. Le couple 45 % et 200 µg/l serait le mauvais aiguillage."),
    ("Femme ménopausée, 66 ans", "48 %", "800 µg/l", "homozygote", "pas de provisoire. 48 % est haut pour une femme non ménopausée, pas pour elle."),
    ("Homme, 70 ans", "80 %", "2 200 µg/l", "homozygote", "provisoire sans biopsie de nom. La hauteur de la ferritine ne change pas la cible : sous 50 µg/l puis sous 100 µg/l."),
    ("Homme, 38 ans", "55 %", "290 µg/l", "homozygote", "saturation suffisante, ferritine non au-dessus de 300 µg/l. Pas de provisoire. On surveille, on ne commence pas l'induction."),
    ("Femme non ménopausée", "60 %", "190 µg/l", "homozygote", "saturation largement au-dessus de 45 %, ferritine non au-dessus de 200 µg/l. Les deux manquent d'en être un. Pas de saignée de nom."),
    ("Homme", "58 %", "600 µg/l", "hétérozygote", "pas le raccourci provisoire. Fer du foie avant de parler de saignée au nom de la maladie."),
    ("Femme non ménopausée", "50 %", "400 µg/l", "hétérozygote", "même refus du raccourci. 50 % serait au-dessus de 45, la ferritine au-dessus de 200, mais le génotype n'est pas homozygote."),
    ("Homme, prélèvement à 19 heures", "52 %", "400 µg/l", "non fait", "on ne génotype pas sur un soir. On refait le matin. 52 % le soir n'est pas le chiffre du texte."),
    ("Homme, matin, a mangé", "61 %", "500 µg/l", "homozygote", "le repas n'invalide pas. Le jeûne n'améliore pas le rendement. Provisoire si le reste est homozygote et au-dessus de 300 µg/l."),
    ("Homme, infection aiguë", "24 %", "1 800 µg/l", "non demandé", "saturation très loin de 50 %. On traite l'infection. Pas de saignée du jour."),
    ("Femme, alcool dit en mots au-dessus du seuil de maladie", "30 %", "550 µg/l", "non demandé", "saturation basse. L'alcool explique mieux la ferritine. Pas de saignée."),
    ("Homme, diabète et stéatose", "32 %", "480 µg/l", "non demandé", "fichier de la stéatose. La saturation à 32 % ferme celui-ci."),
    ("Homme homozygote en induction, ferritine 80 µg/l", "déjà traitée", "80 µg/l", "homozygote", "80 n'est pas sous 50. L'induction continue. L'entretien n'a pas commencé."),
    ("Homme homozygote en entretien, ferritine 80 µg/l", "déjà traitée", "80 µg/l", "homozygote", "80 est sous 100. L'entretien est dans la cible. On ne retourne pas à l'induction."),
    ("Femme en entretien, ferritine 100 µg/l", "traitée", "100 µg/l", "homozygote", "100 n'est pas en dessous de 100. On resserre. L'égalité n'est pas la cible."),
    ("Femme en induction, ferritine 50 µg/l", "traitée", "50 µg/l", "homozygote", "50 n'est pas en dessous de 50. On continue l'induction. Le palier n'est pas franchi."),
    ("Homme, ferritine 40 µg/l après induction", "traitée", "40 µg/l", "homozygote", "sous 50 : on bascule vers l'entretien, dont la cible est sous 100 µg/l, pas une poursuite jusqu'à zéro."),
    ("Apparenté, saturation du matin 33 %", "33 %", "100 µg/l", "inconnu", "premier pas rassurant. Pas de saignée d'avance. Pas de pourcentage familial inventé."),
    ("Adolescent, saturation 40 %", "40 %", "150 µg/l", "non fait", "on n'applique pas un demi-seuil adulte. On adresse. L'extrait lu est celui de l'adulte."),
    ("Homme, alanine encore haute alors que la ferritine est à 40 µg/l", "traité", "40 µg/l", "homozygote", "la cible de fer est atteinte en induction, l'enzyme ne l'est pas. On cherche une seconde maladie. On ne reprend pas une saignée pour l'alanine seule."),
    ("Homme, saturation 50 % pile", "50 %", "1 000 µg/l", "homozygote", "au-dessus de 50 % n'inclut pas 50. Pas de provisoire malgré 1 000 µg/l. On refait ou l'on attend un vrai dépassement."),
    ("Femme non ménopausée, saturation 45 % pile", "45 %", "500 µg/l", "homozygote", "45 % n'est pas au-dessus de 45. Pas de provisoire. La ferritine à 500 µg/l reste insuffisante sans la saturation."),
    ("Homme, ferritine 300 µg/l pile", "60 %", "300 µg/l", "homozygote", "saturation oui, ferritine non : 300 n'est pas au-dessus de 300. Pas de provisoire."),
    ("Femme non ménopausée, ferritine 200 µg/l pile", "55 %", "200 µg/l", "homozygote", "saturation oui, ferritine non. L'égalité ne compte pas. On ne commence pas l'induction."),
    ("Homme en induction, ferritine 49 µg/l", "traité", "49 µg/l", "homozygote", "49 est en dessous de 50. L'induction a atteint sa cible. On passe à l'entretien, sous 100 µg/l."),
    ("Femme en entretien, ferritine 99 µg/l", "traitée", "99 µg/l", "homozygote", "99 est en dessous de 100. Cible d'entretien tenue. On n'exige pas de redescendre sous 50."),
    ("Homme, deux maladies", "70 %", "1 100 µg/l", "homozygote et phosphatase haute avec anticorps antimitochondries", "le fer se traite par la saignée selon les cibles, la cholangite biliaire primitive par l'information 60812. On ne choisit pas un seul fichier."),
    ("Synthèse des égalités", "50 % ou 45 % ou 300 µg/l ou 200 µg/l ou 50 µg/l ou 100 µg/l", "égalité", "tous", "aucune égalité ne vaut « au-dessus » ni « en dessous ». 50 % de saturation ne déclenche pas l'homme. 45 % ne déclenche pas la femme. 300 µg/l et 200 µg/l ne déclenchent pas la ferritine. 50 µg/l ne termine pas l'induction. 100 µg/l ne tient pas l'entretien. On écrit la borne, puis le chiffre du patient, puis le sens de l'inégalité. Cette discipline évite de saigner un doute et d'arrêter une induction trop tôt."),
]
SUITE = [
    f"{qui}. Saturation {sat}, ferritine {fe}, statut {stat}. Lecture : {lec} Les seuils 45, 50, 200 et 300 ne se prêtent pas."
    for qui, sat, fe, stat, lec in SCEN
]

def main():
    fen.append((8, W("w-long8", "Bornes strictes", "\n".join(P(p, 6) for p in LONGS))))
    fen.append((14, W("w-scen8", "Vingt-quatre lectures de borne", "\n".join(P(p, 6) for p in SUITE))))
    fen.append((14, W("w-cas8b", "Cas de borne", "\n".join(P(p, 5, 6) for p in CAS))))
    essentiel = (
        P(f"Matin, jeûne inutile. Homme ou femme ménopausée, homozygote : saturation au-dessus de 50 % et {FE} au-dessus de 300 µg/l. Femme : au-dessus de 45 % et au-dessus de 200 µg/l.", 6)
        + P(f"Autre génotype : fer du foie. Saignées : {FE} sous 50 µg/l en induction, sous 100 µg/l en entretien.", 6)
    )
    phrases = {
        1: "Surcharge en fer génétique. Le nom provisoire est biologique chez l'homozygote.",
        2: "Pas de prévalence suisse lue. Le jeûne n'améliore pas le rendement.",
        3: "La saturation lit le fer qui circule. La ferritine lit les réserves et aussi l'inflammation.",
        4: "Matin, saturation, ferritine, puis le gène, puis le foie si le gène n'est pas homozygote.",
        5: "Ménopause, famille, alcool, arthralgies. La ménopause change le seuil.",
        6: "L'examen peut être normal. On ne l'attend pas.",
        7: "Surcharge, inflammation, ou les deux. La saturation sépare.",
        8: "Deux seuils ensemble, pas un seul. 45 et 200, ou 50 et 300.",
        9: "Pas de biopsie pour le nom si l'homozygote a déjà les deux seuils.",
        10: "Saturation basse : stop. Homozygote complet : saignée. Autre génotype : imagerie.",
        11: "Sous 50 µg/l, puis sous 100 µg/l. Pas de volume inventé.",
        12: "Pas de calendrier familial chiffré dans l'extrait. Premier pas identique.",
        13: "Matin, deux paires de seuils, homozygote, deux cibles.",
        14: "L'égalité n'est pas « au-dessus ». 200 µg/l pile ne suffit pas.",
    }
    fiches = {n: P(phrases[n], 6) for n in phrases}
    sources = [
        f"{EASL}, hémochromatose, Journal of Hepatology, juin 2022.{S(6)}",
        f"{EASL}, stéatose métabolique, 2024, si la ferritine vient du métabolisme et non du fer.{S(5)}",
    ]
    sous = (
        f"Diagnostic différentiel DX.8 de {A('situation de départ F2.11 de PROFILES','F2.11')} "
        f"« Enzymes hépatiques anormales ». Texte du 31.10.2026."
    )
    par = {}
    for point, html in fen:
        par.setdefault(point, []).append(html)
    path = construire(8, "Hémochromatose héréditaire", essentiel, sous, fiches, par, sources)
    print(path)

if __name__ == "__main__":
    main()

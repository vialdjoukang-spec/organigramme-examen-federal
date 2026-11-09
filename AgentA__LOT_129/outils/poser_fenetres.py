#!/usr/bin/env python3
"""Ajoute des fenêtres popover uniques et rebâtit Phase A + DX impairs."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assembler import page

ROOT = Path("/tmp/wt129/AgentA__LOT_129")
TEXTES = ROOT / "textes"

def W(i, mot, titre, a, b, c, d):
    return (i, mot, titre, [a, b, c, d])

FEN = {}

FEN["dx0"] = [
W("w30","144","Numéro 144","Le 144 déclenche la chaîne de sauvetage suisse, du lieu de l'événement jusqu'à l'hôpital, au sol, sur l'eau ou dans les airs.","Exemple : une respiration qui se raréfie fait composer le 144 avant tout questionnaire.","On se trompe en demandant au 144 un conseil de sevrage pour la semaine suivante.","Page de l'Interverband für Rettungswesen lue le 9 novembre 2026, phase générale."),
W("w31","145","Numéro 145","Le 145 est le numéro d'urgence affiché par Tox Info Suisse pour une intoxication.","Exemple : un flacon identifié chez une personne encore éveillée justifie le 145 pour décider du transport.","On se trompe en attendant d'avoir ouvert les schémas d'antidotes, qui n'ont pas été lus.","Accueil de Tox Info Suisse lu le 9 novembre 2026, phase générale."),
W("w32","147","Numéro 147","Le 147 est la ligne pour un enfant ou un adolescent en détresse, reprise sur les pages Infodrog.","Exemple : un élève de quinze ans qui mise en ligne et parle de honte oriente vers le 147, pas vers une ambulance d'emblée.","On se trompe en lui lisant l'amende de 500 000 francs, qui vise la publicité et non l'enfant.","Pages Infodrog lues le 9 novembre 2026, rappel du 147 dans la phase générale."),
W("w33","CIM-11","CIM-11","La CIM-11, depuis 2022, inscrit le trouble du jeu vidéo comme diagnostic, distinct d'une substance.","Exemple : des nuits d'écran sans mise d'argent relèvent de ce trouble, pas de la loi des casinos.","On se trompe en accusant l'objet écran alors qu'Infodrog dit que l'usage est en cause.","Page Infodrog sur internet et les écrans, lue le 9 novembre 2026."),
W("w34","benzodiazépines","Benzodiazépines","Les benzodiazépines calment, favorisent le sommeil et, avec l'alcool ou un opioïde, peuvent paralyser la respiration.","Exemple : la page Infodrog limite l'usage habituel à quatre semaines, avec un maximum de deux à huit.","On se trompe en coupant la boîte d'un coup : l'arrêt brutal peut provoquer une convulsion.","Page Infodrog sur les benzodiazépines, lue le 9 novembre 2026, phase générale."),
W("w35","méthadone","Méthadone","La méthadone est un agoniste opioïde de longue demi-vie, utilisé comme traitement de la dépendance.","Exemple : la SSAM estime qu'environ 70 pour cent des personnes en traitement hors diacétylmorphine la recevaient en 2018.","On se trompe en l'arrêtant parce qu'un stimulant s'y ajoute : le papier cocaïne demande de la poursuivre.","Recommandations SSAM du 16 juillet 2020, rappelées dans la phase générale."),
W("w36","cannabis","Cannabis","Le cannabis est, selon Infodrog, la substance illégale la plus consommée en Suisse, sans que chaque essai soit un trouble.","Exemple : le THC peut rester détectable plus de douze heures dans le sang et plusieurs jours dans l'urine.","On se trompe en lisant une urine positive comme la preuve d'une intoxication de cette minute.","Page Infodrog cannabis, lue le 9 novembre 2026, phase générale."),
W("w37","cocaïne","Cocaïne","La cocaïne est un stimulant sans médicament de substitution établi, selon le papier SSAM du 20 janvier 2024.","Exemple : avec l'alcool elle forme le cocaéthylène, plus toxique pour le cœur.","On se trompe en prescrivant un stimulant de mémoire pour la remplacer.","Papier SSAM sur la cocaïne adopté le 20 janvier 2024, cité dans la phase générale."),
W("w38","sos-jeu","sos-jeu.ch","sos-jeu.ch est la plateforme et le téléphone que les cantons doivent offrir contre le jeu excessif.","Exemple : une dette de loyer liée aux machines oriente vers cette adresse avant tout dosage.","On se trompe en inventant un groupe local quand cette adresse existe déjà.","Page Infodrog sur la politique des jeux, article 85, lue le 9 novembre 2026."),
W("w39","pupille","Pupille","La pupille serrée oriente vers un opioïde, la pupille large vers un stimulant, sans prouver la molécule si les deux se mêlent.","Exemple : respiration rare et pupille en tête d'épingle font passer le tri vers l'intoxication, pas vers un score.","On se trompe en choisissant l'antidote sur la seule pupille quand l'histoire dit un mélange.","Synthèse des pages Infodrog opioïdes et amphétamines, phase générale, 9 novembre 2026."),
W("w40","écran","Écran","L'écran n'est pas l'addiction : Infodrog dit que c'est l'usage qui l'est, jeux, achats ou réseaux.","Exemple : une nuit blanche sur un jeu sans mise se range avec le trouble du jeu vidéo de la CIM-11.","On se trompe en appliquant l'exclusion de casino à un jeu qui ne mise pas d'argent.","Page Infodrog internet et écrans, lue le 9 novembre 2026."),
W("w41","sevrage","Sevrage","Le sevrage est le manque après l'arrêt, distinct de l'intoxication qui est le trop-plein de l'heure.","Exemple : couper une benzodiazépine peut convulser, donc le sevrage menaçant appelle les secours et non des félicitations.","On se trompe en donnant encore un somnifère à quelqu'un dont la respiration ralentit déjà.","Page Infodrog benzodiazépines et tri de la phase générale, 9 novembre 2026."),
W("w42","amphétamine","Amphétamine","L'amphétamine accélère le cœur et peut porter la température jusqu'à 41 degrés en surdosage.","Exemple : un sniff agit en deux à dix minutes et l'effet dure souvent trois à six heures.","On se trompe en collant ce 41 degrés à toutes les autres molécules stimulantes.","Page Infodrog amphétamines, rappelée dans la phase générale le 9 novembre 2026."),
W("w43","somnifère","Somnifère","Un somnifère benzodiazépinique ou Z qui dure des mois sort du cadre court recommandé et majore chutes et confusion chez l'aîné.","Exemple : au-delà de quatre semaines, la dépendance devient le risque principal cité par Infodrog.","On se trompe en renouvelant trois mois d'un coup parce que l'insomnie du manque ressemble au motif initial.","Page Infodrog sur les somnifères et tranquillisants, phase générale, 9 novembre 2026."),
]

FEN["dx1"] = [
W("w30","monoxyde de carbone","CO expiré","Le CO expiré estime l'imprégnation récente et sert de miroir motivationnel, pas de diagnostic de cancer.","Exemple : il dépasse en général 10 ppm chez un fumeur, sauf abstinence de quatre à six heures.","On se trompe en félicitant un chiffre bas pris l'après-midi chez quelqu'un qui a fumé le matin.","Stratégie tabac HUG 2024, chapitre dépistages, lue le 9 novembre 2026."),
W("w31","spirométrie","Spirométrie","La spirométrie cherche un syndrome obstructif chez le fumeur ou l'ex-fumeur exposé.","Exemple : la stratégie la recommande dès 20 paquets-années, surtout avec toux, crachats, sibilances ou dyspnée.","On se trompe en annonçant une BPCO sur la seule toux, sans la courbe.","Stratégie tabac HUG 2024, même chapitre dépistages."),
W("w32","varénicline","Varénicline","La varénicline était un agoniste partiel des récepteurs nicotiniques, retiré du marché mondial en décembre 2022.","Exemple : l'ancien schéma montait de 0,5 mg une fois par jour à 1 mg deux fois par jour, avec des nausées chez 28,2 pour cent des personnes.","On se trompe en la prescrivant encore comme si la boîte existait.","Tableau des médicaments non nicotiniques, stratégie tabac HUG 2024."),
W("w33","cytisine","Cytisine","La cytisine est un agoniste nicotinique jugé efficace, non commercialisé en Suisse, importable sans posologie dans le texte lu.","Exemple : aucune dose suisse n'est écrite dans la stratégie, donc aucune ordonnance ne peut être recopiée d'ici.","On se trompe en inventant un comprimé de cytisine pour combler le retrait de la varénicline.","Stratégie tabac HUG 2024, paragraphe suivant le retrait de décembre 2022."),
W("w34","patch","Patch de nicotine","Le patch délivre une nicotine continue pour doubler, avec les autres substituts, les chances d'arrêt.","Exemple : la forte dose est 21 mg pendant quatre semaines, puis 14 mg deux à quatre semaines, puis 7 mg.","On se trompe en le refusant par peur du cancer : la stratégie attribue cancers et BPCO à la combustion.","Tableau des substituts, stratégie tabac HUG 2024."),
W("w35","vapoteuse","Vapoteuse","La vapoteuse chauffe un liquide sans combustion et contient beaucoup moins de toxiques que la fumée, sans être inoffensive.","Exemple : en Suisse le liquide va de 0 à 20 mg/ml, et l'on part souvent d'environ 1 mg/ml par cigarette quotidienne.","On se trompe en la proposant d'emblée à un adolescent : la stratégie la réserve à des échecs ou à un arrêt urgent de la combustion.","Chapitre vapotage, stratégie tabac HUG 2024."),
W("w36","snus","Snus","Le snus est un tabac oral humide, sans combustion, mais porteur des toxiques du tabac et d'un risque cardiovasculaire établi.","Exemple : la stratégie le juge plus nocif que des poches de nicotine orale sans tabac.","On se trompe en le présentant à un sportif comme une forme anodine.","Tableau des formes et paragraphe snus, stratégie tabac HUG 2024."),
W("w37","paquets-années","Paquets-années","Les paquets-années mesurent l'exposition cumulée et ouvrent des dépistages, ils ne diagnostiquent pas la dépendance.","Exemple : le seuil lu pour la spirométrie et pour discuter le scanner faible dose est de 20.","On se trompe en les confondant avec le score de Fagerström, qui cote le manque et non les années.","Stratégie tabac HUG 2024, dépistages respiratoires."),
W("w38","sevrage","Sevrage nicotinique","Le sevrage nicotinique est l'ensemble des signes de manque quand la fumée s'arrête, fréquent au-dessus de cinq cigarettes par jour.","Exemple : il peut durer de trois semaines à trois mois, avec craving, insomnie, irritabilité et faim.","On se trompe en y voyant un défaut de caractère ou en l'arrêtant au bout de quatre jours.","Stratégie tabac HUG 2024, critères CIM-10 et clinique du manque."),
]

FEN["dx3"] = [
W("w30","méthadone","Méthadone","La méthadone est un agoniste complet qui s'accumule : l'équilibre plasmatique arrive en général en cinq à six jours.","Exemple : le départ usuel ne dépasse pas 30 mg, puis la hausse quotidienne reste de 5 à 10 mg.","On se trompe en doublant la dose le deuxième soir parce que le manque de la veille a fait peur.","Chapitre d'induction des recommandations SSAM du 16 juillet 2020."),
W("w31","buprénorphine","Buprénorphine","La buprénorphine est un agoniste partiel, peu dangereux seule pour la respiration, sauf avec un sédatif ou de l'alcool.","Exemple : la première journée peut aller jusqu'à 34 mg en prises fractionnées, puis souvent autour de 16 mg le lendemain.","On se trompe en la donnant au milieu de l'effet d'un agoniste complet : elle précipite alors un manque.","Chapitre buprénorphine, SSAM 16 juillet 2020."),
W("w32","morphine","Morphine retard","La morphine orale à libération prolongée suit la même prudence de départ que la méthadone, avec d'autres nombres.","Exemple : 200 mg sont tenus pour supportables même avec peu de tolérance, et le pas suivant ne dépasse pas 120 mg.","On se trompe en additionnant méthadone et morphine le même jour pour aller plus vite.","Chapitre SROM, recommandations SSAM du 16 juillet 2020."),
W("w33","diacétylmorphine","Diacétylmorphine","La diacétylmorphine pharmaceutique est le second pilier, réservé à peu de centres, pas au cabinet.","Exemple : environ 1 700 personnes la recevaient en 2018, à côté des 16 700 autres traitements.","On se trompe en la comptant comme une méthadone pour l'aptitude à conduire : le papier de 2024 l'exclut.","SSAM 2020 pour l'effectif, SGRM-SSAM du 6 décembre 2024 pour la route."),
W("w34","clonidine","Clonidine","La clonidine, agoniste alpha-2, peut calmer un sevrage déclenché par l'induction de buprénorphine.","Exemple : le texte la cite sans milligrammes, donc aucune dose ne sort de ce fichier.","On se trompe en recopiant une posologie de mémoire qui n'est pas dans le chapitre lu.","Recommandations SSAM du 16 juillet 2020, induction de buprénorphine."),
W("w35","hépatite","Hépatite C","L'hépatite C et le VIH sont liés par Infodrog aux conditions d'injection et d'échange de matériel, pas à une propriété magique de l'héroïne.","Exemple : un test se propose quand l'histoire comporte des effractions, sans délai de fenêtre inventé ici.","On se trompe en arrêtant la méthadone au motif d'une hépatite, sans avis hépatologique.","Page Infodrog héroïne et opioïdes, lue le 9 novembre 2026."),
W("w36","creux","Creux plasmatique","Le creux est le taux de méthadone prélevé avant la prise, utile seulement si la dose dépasse 120 mg et que le manque persiste.","Exemple : les seuils cités sont 250 ng/ml de (R)-méthadone et 500 ng/ml du racémate.","On se trompe en dosant la buprénorphine pour la même question : la SSAM dit ce dosage inutile.","Chapitre d'équilibre, SSAM 16 juillet 2020."),
W("w37","lévométhadone","Lévométhadone","La lévométhadone est l'isomère actif, marginal dans les chiffres suisses de 2018.","Exemple : elle représentait environ 1,6 pour cent des traitements hors diacétylmorphine.","On se trompe en la confondant avec un double de la dose racémique sans lecture du chapitre dédié, non détaillé ici.","Épidémiologie des recommandations SSAM du 16 juillet 2020."),
W("w38","sédation","Sédation","La sédation est le premier signe sérieux de surdosage d'agoniste et impose de baisser la dose tout de suite.","Exemple : au deuxième ou troisième jour de méthadone, un calme excessif peut précéder l'œdème pulmonaire.","On se trompe en le prenant pour le soulagement attendu du manque.","Chapitre intoxication et induction, SSAM 16 juillet 2020."),
W("w39","automobiles","Loi sur les stupéfiants","La loi sur les stupéfiants encadre les antalgiques opioïdes comme substances psychotropes soumises à prescription.","Exemple : conduire sous antalgique en étant inapte peut valoir une amende, une peine ou un retrait de permis d'au moins trois mois.","On se trompe en interdisant le volant à tout patient douloureux : Infodrog laisse la décision au médecin.","Page Infodrog sur les analgésiques opioïdes, lue le 9 novembre 2026."),
W("w40","conduite","Aptitude à conduire","Sous agoniste, conduire est une exception, jamais un droit, après une expertise de niveau 4 si le service des automobiles le sait.","Exemple : il faut au moins six mois stables, sans diacétylmorphine, et deux semaines sans conduire pendant l'équilibration.","On se trompe en signant une aptitude le jour de la première ordonnance.","Recommandations SGRM et SSAM approuvées le 6 décembre 2024."),
]

FEN["dx5"] = [
W("w30","cocaïne","Cocaïne","La cocaïne libère de la dopamine, accélère le cœur et dilate les pupilles, puis laisse un vide qui pousse à reprendre.","Exemple : aucun médicament établi n'existe, papier du comité SSAM du 20 janvier 2024.","On se trompe en arrêtant une méthadone déjà en cours pour punir le crack.","Page Infodrog cocaïne et papier SSAM du 20 janvier 2024."),
W("w31","amphétamine","Amphétamine","L'amphétamine libère noradrénaline et dopamine, coupe faim et sommeil, et peut surchauffer.","Exemple : par voie nasale l'effet dure souvent trois à six heures, avec des restes jusqu'à vingt-quatre heures.","On se trompe en déclarant l'épisode clos au bout d'une heure parce que la personne parle mieux.","Page Infodrog amphétamines, lue le 9 novembre 2026."),
W("w32","méthamphétamine","Méthamphétamine","La méthamphétamine atteint le cerveau plus vite que l'amphétamine et tient beaucoup plus longtemps.","Exemple : l'effet principal peut durer de six à trente heures, et les effets secondaires jusqu'à soixante-dix heures.","On se trompe en calquant la surveillance sur une simple amphétamine d'une soirée.","Page Infodrog méthamphétamines, lue le 9 novembre 2026."),
W("w33","MDMA","MDMA","La MDMA vide en partie la sérotonine, d'où une empathie puis parfois un jour terne.","Exemple : l'effet commence vers trente minutes, parfois seulement à quatre-vingt-dix, et la sérotonine peut mettre jusqu'à une semaine à se refaire.","On se trompe en donnant une seconde pilule parce que la première semble muette à vingt minutes.","Page Infodrog ecstasy-MDMA, lue le 9 novembre 2026."),
W("w34","crack","Crack","Le crack est la forme que la SSAM place au centre de plusieurs scènes urbaines, sans que ce fichier n'en décrive la fabrication.","Exemple : les structures bas seuil sont saturées et les personnes les plus malades n'entrent pas d'elles-mêmes.","On se trompe en exigeant l'abstinence de crack comme ticket pour garder un agoniste opioïde.","Papier SSAM du 20 janvier 2024, paragraphe sur la poursuite du traitement agoniste."),
W("w35","sérotonine","Sérotonine","La sérotonine porte une part de l'humeur, et la MDMA en consomme les réserves.","Exemple : jusqu'à une semaine peut être nécessaire pour les remplir à nouveau après une prise.","On se trompe en posant une dépression chronique le lendemain, avant ce délai.","Page Infodrog MDMA, mécanisme sérotoninergique."),
W("w36","drug checking","Drug checking","Le drug checking analyse la composition réelle et s'accompagne d'un entretien bref.","Exemple : les comprimés d'ecstasy varient fortement et peuvent contenir du 2C-B.","On se trompe en identifiant une pilule sur son logo ou sa couleur.","Pages Infodrog cocaïne et MDMA, réduction des risques."),
W("w37","logement","Housing first","Le logement d'abord fait partie des mesures de survie que la SSAM met avant un médicament inexistant.","Exemple : manger, se laver et dormir à l'abri sont les besoins nommés avec les soins de base.","On se trompe en promettant un comprimé à quelqu'un qui dort dehors.","Papier SSAM du 20 janvier 2024, dommages et besoins de base."),
W("w38","contingency","Contingency management","Le contingency management renforce des actes concrets, rendez-vous tenu, repas, dépistage accepté.","Exemple : la SSAM juge bonne l'évidence de le combiner au psychosocial, et dit que le rendement suisse reste à mesurer.","On se trompe en annonçant un taux de réussite qui n'est pas dans le papier.","Papier SSAM du 20 janvier 2024, interventions thérapeutiques."),
W("w39","pupilles","Pupilles larges","Les pupilles larges accompagnent la cocaïne et les amphétamines, avec le cœur rapide.","Exemple : une pupille large plus une douleur thoracique oriente vers l'urgence, pas vers un conseil du lendemain.","On se trompe en rassurant parce que la personne a surtout bu : l'alcool ajoute le cocaéthylène.","Page Infodrog cocaïne, effets physiques."),
W("w40","41","Quarante et un degrés","Quarante et un degrés est le repère de surchauffe du surdosage d'amphétamine, souvent sous-estimé.","Exemple : Infodrog y associe déshydratation et risque mortel, avec défaillance d'organes.","On se trompe en couvrant une personne qui tremble de chaleur.","Page Infodrog amphétamines, paragraphe surdosage."),
W("w41","stupéfiants","LStup et stimulants","La cocaïne et l'amphétamine sont soumises à la loi sur les stupéfiants, tandis que le méthylphénidate a un usage médical distinct.","Exemple : le méthylphénidate vise la narcolepsie ou le trouble de l'attention, pas le craving de cocaïne.","On se trompe en ouvrant cette ordonnance pour remplacer une poudre de rue.","Pages Infodrog cocaïne et amphétamines, cadres légaux."),
W("w42","craving","Craving","Le craving est l'envie forte de reprendre quand l'effet tombe, décrit pour la cocaïne et encore plus net pour la méthamphétamine inhalée.","Exemple : après l'amphétamine, le sevrage psychique dépasse les une à deux semaines du sevrage physique.","On se trompe en le prenant pour un simple coup de fatigue du lendemain.","Pages Infodrog cocaïne, amphétamines et méthamphétamines."),
]

FEN["dx7"] = [
W("w30","Gespa","Gespa","La Gespa, autrefois Comlot, autorise et surveille les jeux de grande envergure hors casino et combat les offres illégales.","Exemple : une loterie en ligne ou intercantonale relève d'elle, pas de la commune.","On se trompe en lui écrivant pour une dette ordinaire de casino, qui va d'abord à l'exploitant.","Page Infodrog sur la politique des jeux, lue le 9 novembre 2026."),
W("w31","Commission","Commission fédérale des maisons de jeu","La Commission fédérale des maisons de jeu surveille les casinos terrestres et, depuis 2019, les casinos en ligne.","Exemple : une roulette ou une machine se signale de ce côté, pas à la Gespa.","On se trompe en lui demandant de soigner une dette : elle surveille l'exploitant.","Même page Infodrog, répartition des autorités."),
W("w32","exclusion","Exclusion de jeu","L'exclusion interdit l'accès quand il y a surendettement, mises trop hautes pour le revenu, ou dépendance.","Exemple : l'article 80 permet au joueur, à un tiers, au casino, à Swisslos ou à la Loterie Romande de la demander.","On se trompe en croyant qu'elle ferme tous les sites : le contournement en ligne est écrit.","Article 80 LJAr, page politique des jeux Infodrog."),
W("w33","sos-jeu","sos-jeu.ch","sos-jeu.ch est le dispositif cantonal de conseil, financé notamment par une taxe de prévention.","Exemple : on le donne dès le premier appel, avant même le rendez-vous.","On se trompe en le remplaçant par un pourcentage de joueurs que la page ne donne pas.","Article 85 et taxe de 0,5 pour cent, page Infodrog."),
W("w34","mineurs","Mineurs","Les mineurs sont protégés à part : pas de casino avant 18 ans, et pas de grand jeu sous 16 ans.","Exemple : un compte ouvert à quinze ans se ferme, et le 147 s'ajoute si la détresse est là.","On se trompe en brandissant contre l'enfant l'amende qui punit la publicité.","Article 72 LJAr, page Infodrog lue le 9 novembre 2026."),
W("w35","machines","Machines à sous","Les machines sont jugées particulièrement dangereuses et ne peuvent être exploitées en Suisse que dans les casinos.","Exemple : un café qui en proposerait sortirait du cadre lu.","On se trompe en les traitant comme une loterie de village.","Page Infodrog jeux d'argent, formes et dangers."),
W("w36","Swisslos","Swisslos","Swisslos est tenu, avec la Loterie Romande, à un programme social de repérage et de limites.","Exemple : une demande d'exclusion peut partir de la personne vers Swisslos, pas seulement d'un croupier.","On se trompe en écrivant un réquisitoire au lieu d'une lettre courte avec les faits.","Article 76 LJAr, page politique Infodrog."),
W("w37","Loterie","Loterie Romande","La Loterie Romande partage ce devoir social pour les jeux qu'elle exploite en Suisse romande.","Exemple : un compte de loterie en ligne qui dépasse le revenu peut motiver une exclusion.","On se trompe en la confondant avec la Commission des maisons de jeu.","Même article 76, page Infodrog du 9 novembre 2026."),
W("w38","publicité","Publicité","La publicité des jeux ne doit ni être outrancière, ni tromper, ni viser un mineur ou une personne exclue.","Exemple : l'amende peut atteindre 500 000 francs quand elle cible des mineurs.","On se trompe en gronder le joueur exclu qui a seulement ouvert le message.","Articles 74 et 131 LJAr, page Infodrog."),
W("w39","quasi-gains","Quasi-gain","Le quasi-gain, quand il ne manque qu'un symbole, entretient le retour au jeu.","Exemple : Infodrog le met avec la vitesse des parties, les jetons et l'atmosphère du casino.","On se trompe en le racontant comme une simple malchance neutre.","Page Infodrog jeux d'argent, facteurs du jeu lui-même."),
W("w40","article 80","Article 80","L'article 80 ouvre l'exclusion pour dettes, mises excessives ou dépendance.","Exemple : un loyer passé après la mise place déjà cet article dans la pièce, même sans lettre.","On se trompe en l'imposant dans le dos d'une personne capable, hors danger grave.","Page politique des jeux, Infodrog, 9 novembre 2026."),
W("w41","article 72","Article 72","L'article 72 fixe la protection des mineurs et les âges d'accès.","Exemple : 18 ans pour les casinos et les grands jeux en ligne, jamais moins de 16 ans pour les autres grands jeux.","On se trompe en laissant un adolescent juste regarder un casino en ligne.","Article 72 LJAr tel que résumé par Infodrog."),
W("w42","article 85","Article 85","L'article 85 oblige les cantons à prévenir le jeu excessif et à offrir conseil et traitement.","Exemple : la taxe de 0,5 pour cent du revenu brut des grands jeux alimente cette prévention.","On se trompe en y voyant un droit individuel à des soins illimités.","Article 85 LJAr, page Infodrog."),
W("w43","taxe","Taxe de 0,5 pour cent","Cette taxe de 0,5 pour cent explique pourquoi un dispositif cantonal existe, elle ne rembourse pas la mise perdue.","Exemple : elle se distingue de l'impôt sur le produit brut des casinos, qui va vers l'AVS et l'AI entre 20 et 80 pour cent selon le cadre.","On se trompe en disant au patient que le casino lui doit les soins parce qu'il a perdu.","Page politique des jeux, financement, lue le 9 novembre 2026."),
]

FEN["dx9"] = [
W("w30","144","Numéro 144","Le 144 lance la chaîne de secours, du lieu vers l'hôpital.","Exemple : une poitrine qui ne se soulève plus fait composer le 144 avant le nom du produit.","On se trompe en finissant l'interrogatoire pendant que l'air manque.","Site de l'Interverband, lu le 9 novembre 2026, monographie de l'intoxication."),
W("w31","145","Numéro 145","Le 145 conseille sur le poison quand Tox Info Suisse est joint, sans remplacer l'ambulance.","Exemple : un cachet inconnu chez un lycéen encore stable se décrit au 145, avec l'heure.","On se trompe en citant un schéma d'antidote que l'accueil annonce mais que ce fichier n'a pas ouvert.","Accueil Tox Info Suisse, 9 novembre 2026, monographie intoxication."),
W("w32","naloxone","Naloxone","La naloxone renverse un agoniste opioïde puis dure moins longtemps que lui, d'où un rendormissement possible.","Exemple : après une dose nasale donnée par un proche, l'hôpital devient urgent à cause de l'œdème qui peut suivre.","On se trompe en inventant les milligrammes : le chapitre SSAM ne les chiffre pas.","Chapitre intoxication, SSAM 16 juillet 2020."),
W("w33","méthadone","Méthadone","La méthadone a une demi-vie longue : l'intoxication ne se juge pas sur la première heure seule.","Exemple : en induction, les décès lus tombent plutôt le deuxième ou le troisième jour.","On se trompe en reprenant l'ancienne dose après une pause, quand la tolérance a fondu.","Même chapitre SSAM, demi-vie et tolérance."),
W("w34","buprénorphine","Buprénorphine","La buprénorphine tient le récepteur plus fort que la naloxone, si bien que les doses usuelles d'antagoniste échouent largement.","Exemple : on assure quand même l'oxygène et l'hôpital, sans promettre un réveil.","On se trompe en annonçant une dose haute de naloxone qui n'est pas écrite.","SSAM 2020, paragraphe sur l'affinité de la buprénorphine."),
W("w35","pupille","Pupille serrée","La pupille en tête d'épingle, avec une respiration rare, oriente vers l'opioïde sans le certifier.","Exemple : on ventile et on appelle même si un stimulant a pu être mêlé.","On se trompe en choisissant l'antidote sur ce seul signe.","Page Infodrog opioïdes, signes aigus, monographie intoxication."),
W("w36","cocaéthylène","Cocaéthylène","Le cocaéthylène se forme quand cocaïne et alcool sont pris ensemble et pèse davantage sur le cœur.","Exemple : une douleur thoracique dans ce récit part aux urgences comme un syndrome coronarien possible.","On se trompe en rassurant parce que la personne a surtout bu.","Page Infodrog cocaïne, rappelée pour l'intoxication aiguë."),
W("w37","benzodiazépine","Benzodiazépine","La benzodiazépine ralentit la respiration et, avec un opioïde ou de l'alcool, peut la paralyser.","Exemple : un somnifère d'un ami ajouté à une méthadone et une bière n'est pas un sommeil, c'est souvent une voie qui se ferme.","On se trompe en ajoutant un deuxième calmant pour la nuit.","Page Infodrog benzodiazépines, mélanges sédatifs."),
W("w38","amphétamine","Amphétamine","L'amphétamine en surdosage peut porter la température jusqu'à 41 degrés.","Exemple : on découvre, on sort de la pièce, on n'attend pas le dernier degré pour appeler si la chaleur est déjà clinique.","On se trompe en remettant une couverture parce que la personne tremble.","Page Infodrog amphétamines, utilisée ici pour l'urgence thermique."),
W("w39","MDMA","MDMA","La MDMA peut mettre jusqu'à quatre-vingt-dix minutes à agir et surchauffe dans une pièce close.","Exemple : une seconde pilule prise parce que la première semble inactive est le piège de ce délai.","On se trompe en collant le seuil de 41 degrés, qui n'est écrit que pour l'amphétamine.","Page Infodrog MDMA, délais et chaleur, monographie intoxication."),
W("w40","oxygène","Oxygène","L'oxygène est la mesure de grade le plus haut du chapitre SSAM, avant le nom du produit.","Exemple : on le demande ou on ventile dès que la poitrine ne se soulève plus.","On se trompe en partant chercher un dossier en laissant la personne seule.","SSAM 16 juillet 2020, recommandation de grade A sur l'oxygène."),
W("w41","œdème","Œdème pulmonaire","L'œdème pulmonaire non cardiogénique accompagne l'opioïde grave, et l'hyperventilation de besoin peut manquer.","Exemple : il motive l'hôpital après naloxone, même si les yeux se sont rouverts.","On se trompe en laissant repartir quelqu'un réveillé.","Chapitre intoxication SSAM, œdème et demi-vie de la naloxone."),
W("w42","flacon","Liquide de vapotage","Avaler un liquide de vapoteuse peut intoxiquer un enfant, à l'inverse du patch porté en fumant encore.","Exemple : on garde le flacon pour le nommer au 145 et l'on ne fait pas vomir.","On se trompe en donnant du lait ou un vomitif, qui ne sont pas dans la stratégie lue.","Stratégie tabac HUG 2024, passage sur l'ingestion de liquide."),
W("w43","médicaments Z","Médicaments Z","Le zolpidem et la zopiclone ne sont pas chimiquement des benzodiazépines mais partagent une grande part de leurs risques.","Exemple : chez l'aîné, l'élimination plus lente allonge l'effet et la chute peut être une intoxication.","On se trompe en mettant la confusion sur le seul compte de l'âge.","Page Infodrog benzodiazépines, analogues Z."),
W("w44","convulsion","Convulsion","Une convulsion se protège, se chronomètre, et part avec le 144 si elle ne cède pas.","Exemple : Infodrog la cite pour la MDMA, l'amphétamine, et l'arrêt brutal d'une benzodiazépine.","On se trompe en mettant un objet dans la bouche, geste écrit nulle part ici.","Pages Infodrog MDMA, amphétamines et benzodiazépines, geste commun de l'urgence."),
]

def masquer_zones(lignes):
    """Retourne les index de lignes éditables (hors @@, %%, titres)."""
    ok = []
    bloc = None
    for i, ln in enumerate(lignes):
        s = ln.strip()
        if bloc == "at":
            if s.startswith("@@"):
                bloc = None
            continue
        if bloc == "raw":
            if s == "%%":
                bloc = None
            continue
        if s.startswith("@@"):
            bloc = "at"
            continue
        if s in ("%%TABLE", "%%HTML"):
            bloc = "raw"
            continue
        if s.startswith("##"):
            continue
        ok.append(i)
    return ok

def remplacer(ligne, mot):
    masques = []
    def cacher(m):
        masques.append(m.group(0))
        return "\u0000%d\u0000" % (len(masques) - 1)
    cachee = re.sub(r"\[\[[^\]]+\]\]", cacher, ligne)
    pat = re.compile(r"(?<!\w)" + re.escape(mot) + r"(?!\w)", re.I)
    m = pat.search(cachee)
    if not m:
        return ligne, False
    ins = "[[" + "ID" + "|" + m.group(0) + "]]"
    # l'id est posé par l'appelant
    return (cachee, m, masques)

def poser(md, items):
    lignes = md.splitlines()
    editables = set(masquer_zones(lignes))
    manques = []
    for ident, mot, titre, paras in items:
        fait = False
        for i in range(len(lignes)):
            if i not in editables:
                continue
            masques = []
            def cacher(m, masques=masques):
                masques.append(m.group(0))
                return "\u0000%d\u0000" % (len(masques) - 1)
            cachee = re.sub(r"\[\[[^\]]+\]\]", cacher, lignes[i])
            pat = re.compile(r"(?<!\w)" + re.escape(mot) + r"(?!\w)", re.I)
            m = pat.search(cachee)
            if not m:
                continue
            insere = "[[" + ident + "|" + m.group(0) + "]]"
            cachee = cachee[:m.start()] + insere + cachee[m.end():]
            def rendre(mm, masques=masques):
                return masques[int(mm.group(1))]
            lignes[i] = re.sub(r"\u0000(\d+)\u0000", rendre, cachee)
            fait = True
            break
        if not fait:
            manques.append((ident, mot))
    extra = []
    if manques:
        bouts = ", ".join("[[" + i + "|" + m + "]]" for i, m in manques)
        extra.append("")
        extra.append("D'autres repères de ce fichier s'ouvrent ici : " + bouts + ".")
    extra.append("")
    for ident, mot, titre, paras in items:
        extra.append("@@" + ident + " " + titre)
        for p in paras:
            extra.append(p)
            extra.append("")
        extra.append("@@")
        extra.append("")
    return "\n".join(lignes + extra) + "\n", manques

FICHIERS = {
    "dx0": ("phaseA.md", "Phase A — Usage non médical de substances et addictions",
            "Phase A du lot 129, syndrome S9.13, texte non validé cliniquement.",
            "LOT_129_Phase_A_V0.html", [
                "[S1] Probst, Favrod-Coune, De Lucia et Humair : stratégie HUG sur le tabac, 2024, PDF ouvert le 9 novembre 2026 à l'adresse https://www.hug.ch/sites/interhug/files/2024-10/strategie_tabac_doi.pdf",
                "[S2] Société suisse de médecine de l'addiction : recommandations d'agoniste opioïde datées du 16 juillet 2020, et position sur la cocaïne adoptée le 20 janvier 2024, toutes deux parcourues pour cette phase générale",
                "[S3] Infodrog, centrale nationale : pages cannabis, benzodiazépines, écrans, jeux d'argent, opioïdes et stimulants, consultées pour le tri du 9 novembre 2026",
                "[S4] Accueil de Tox Info Suisse et site de l'Interverband für Rettungswesen (chaîne du 144), ouverts le 9 novembre 2026 pour les numéros d'urgence",
            ]),
    "dx1": ("dx1.md", "DX.1 — Tabagisme",
            "DX.1 tabagisme du lot 129, texte non validé cliniquement.",
            "LOT_129_Phase_B_V0_DX.1.html", [
                "[S1] Probst C, Favrod-Coune T, De Lucia S et Humair JP : stratégie tabac des HUG, service de médecine de premier recours, version 2024, PDF consulté le 9 novembre 2026 via https://www.hug.ch/sites/interhug/files/2024-10/strategie_tabac_doi.pdf",
            ]),
    "dx3": ("dx3.md", "DX.3 — Trouble de l'usage d'opioïdes",
            "DX.3 opioïdes du lot 129, texte non validé cliniquement.",
            "LOT_129_Phase_B_V0_DX.3.html", [
                "[S1] Infodrog, page héroïne et opioïdes, consultée le 9 novembre 2026 : https://www.infodrog.ch/fr/ressources/formes-de-dependances/heroine-opioides.html",
                "[S2] Infodrog, page des analgésiques opioïdes, ouverte le même jour : https://www.infodrog.ch/fr/ressources/formes-de-dependances/analgesiques-opioides.html",
                "[S3] SSAM, recommandations du traitement agoniste opioïde en date du 16 juillet 2020, chapitres d'épidémiologie, d'induction, d'équilibre et d'intoxication, PDF parcouru le 9 novembre 2026",
                "[S4] SGRM et SSAM, aptitude à conduire sous agoniste opioïde, texte approuvé le 6 décembre 2024, lu intégralement le 9 novembre 2026",
                "[S5] Rochat et collaborateurs, Revue Médicale Suisse 2026, pages 1786 à 1790 : seul le résumé en accès libre a été lu le 9 novembre 2026, pas le corps de l'article",
            ]),
    "dx5": ("dx5.md", "DX.5 — Trouble de l'usage de stimulants",
            "DX.5 stimulants du lot 129, texte non validé cliniquement.",
            "LOT_129_Phase_B_V0_DX.5.html", [
                "[S1] Infodrog, page cocaïne, lue pour ce diagnostic le 9 novembre 2026 : https://www.infodrog.ch/fr/ressources/formes-de-dependances/cocaine.html",
                "[S2] Infodrog, page amphétamines et speed, parcourue le 9 novembre 2026 : https://www.infodrog.ch/fr/ressources/formes-de-dependances/amphetamines-speed.html",
                "[S3] Infodrog, page méthamphétamines, ouverte le 9 novembre 2026 : https://www.infodrog.ch/fr/ressources/formes-de-dependances/methamphetamines.html",
                "[S4] Infodrog, page MDMA et ecstasy, consultée le 9 novembre 2026 : https://www.infodrog.ch/fr/ressources/formes-de-dependances/ecstasy-mdma.html",
                "[S5] Berthel T pour la SSAM, position sur la cocaïne et le crack adoptée en comité le 20 janvier 2024, PDF relu le 9 novembre 2026",
            ]),
    "dx7": ("dx7.md", "DX.7 — Jeu d'argent excessif",
            "DX.7 jeu d'argent du lot 129, texte non validé cliniquement.",
            "LOT_129_Phase_B_V0_DX.7.html", [
                "[S1] Infodrog, page jeux d'argent, lue le 9 novembre 2026 : https://www.infodrog.ch/fr/ressources/formes-de-dependances/jeux-d-argent.html",
                "[S2] Infodrog, page de politique des jeux d'argent, parcourue le 9 novembre 2026 : https://www.infodrog.ch/fr/ressources/politique-addictions/politique-des-jeux-d-argent.html",
                "[S3] Gespa, page d'accueil, ouverte le 9 novembre 2026 : le rôle de surveillance y est confirmé, sans chiffre de prévalence clinique",
            ]),
    "dx9": ("dx9.md", "DX.9 — Intoxication aiguë",
            "DX.9 intoxication aiguë du lot 129, texte non validé cliniquement.",
            "LOT_129_Phase_B_V0_DX.9.html", [
                "[S1] SSAM, chapitre intoxication des recommandations d'agoniste opioïde du 16 juillet 2020, extrait lu le 9 novembre 2026",
                "[S2] Infodrog, pages héroïne, amphétamines, MDMA et benzodiazépines, mobilisées pour les signes aigus le 9 novembre 2026",
                "[S3] Tox Info Suisse : page d'accueil (145) et liste des antidotes 2026/2027, lignes naloxone et charbon actif, lues le 9 novembre 2026 ; les autres fiches de la liste n'ont pas été ouvertes",
                "[S4] Interverband für Rettungswesen, présentation de la chaîne du 144, lue le 9 novembre 2026",
                "[S5] Stratégie tabac des HUG, 2024, seul le passage sur l'ingestion d'un liquide à vapoter a été repris ici, lecture du 9 novembre 2026",
            ]),
}

def main():
    for cle, (nom, h2, chapeau, sortie, sources) in FICHIERS.items():
        md = (TEXTES / nom).read_text(encoding="utf-8")
        nouveau, manques = poser(md, FEN[cle])
        (TEXTES / nom).write_text(nouveau, encoding="utf-8")
        html = page(cle, h2, nouveau, sources, chapeau)
        (ROOT / sortie).write_text(html, encoding="utf-8")
        print(cle, "manques", manques, "octets", len(html.encode()))

if __name__ == "__main__":
    main()

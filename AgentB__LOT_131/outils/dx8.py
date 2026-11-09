# -*- coding: utf-8 -*-
"""DX.8 Carcinome épidermoïde du pénis."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from dx_lib import b, w, ilot, tableau
DX = 8

def body() -> str:
    P = []
    P.append(ilot(DX, 1, "Définition et sémantique", """
<p>Le carcinome épidermoïde du pénis est, pour l’Association européenne d’urologie dans le chapitre d’épidémiologie relu le 9 novembre 2026, la forme qui représente plus de 95 % des cancers du pénis. Il naît en règle de l’épithélium du prépuce interne ou du gland. [S1]</p>
""" + w("dx8-p1-pein",
"La néoplasie intra-épithéliale du pénis, ou PeIN, est le précurseur, pas encore invasif.",
"L’OMS 2022, reprise par le chapitre, sépare la PeIN indépendante du papillomavirus, dite différenciée, et la PeIN associée au papillomavirus.",
"Les anciens noms cliniques, érythroplasie de Queyrat, maladie de Bowen et papulose bowénoïde, sont découragés.",
"Exemple : une lésion rouge du gland n’est pas « une Bowen » dans un compte rendu moderne. On dit PeIN, puis on précise le lien avec le virus. [S1]",
"Le piège est de traiter un nom historique comme un stade.",
"Source [S1].") + """
<p>Le chapitre distingue les sous-types liés au papillomavirus humain et ceux qui ne le sont pas. Le sous-type usuel, indépendant du virus, représente 45 à 75 % des cas. Le verruqueux, le papillaire, le basaloïde et le warty ont d’autres fréquences et d’autres mortalités, données plus bas. On ne dit pas « cancer de la peau du pénis » sans le mot épidermoïde quand c’est lui. [S1]</p>
<p>La Revue Médicale Suisse de 2024, dans le résumé accessible, rappelle que ce cancer est rare mais grave dans le monde occidental, où il fait moins de 1 % des cancers de l’homme, et que le stade ganglionnaire décide du pronostic. Le corps de l’article n’était pas dans l’extrait reçu : on n’y puise pas de dose ni de seuil. [S5]</p>
"""))
    P.append(ilot(DX, 2, "Épidémiologie (Suisse, puis Europe)", """
<p>La Suisse est citée par le chapitre dans le groupe européen à incidence basse, avec les Pays-Bas, la Slovénie, la Pologne et la Finlande. Aucun taux OFS précis, du type pour 100 000, n’est écrit pour la Suisse dans la page lue. On ne l’invente pas. [S1]</p>
<p>L’Europe, globalement, est à environ 0,94 pour 100 000 hommes. La France, sur 16 registres entre 2009 et 2011, était à 0,59 pour 100 000, intervalle de confiance à 95 % de 0,50 à 0,68, stable depuis 1989. D’autres pays européens montent : la Saxe est passée de 0,86 en 2000 à 2,67 pour 100 000 en 2018. Les Pays-Bas sont passés de 0,92 à 1,83 pour 100 000 et par an entre 1990 et 2020. [S1]</p>
""" + w("dx8-p2-age",
"L’incidence augmente avec l’âge et culmine à la sixième décennie, tout en existant chez l’homme plus jeune.",
"Environ un tiers à la moitié des cas sont attribués à la carcinogenèse liée au papillomavirus. Une revue de 52 études trouve une prévalence virale de 50,8 %, intervalle 44,8 à 56,7.",
"Le génotype 16 représente 68,3 % des cas associés au virus, intervalle 58,9 à 77,1.",
"Le piège est de citer le chiffre américain de 0,5 pour 100 000 comme s’il était suisse. [S1]",
"Source [S1].") + """
<p>Les facteurs de risque lus sont le phimosis, l’inflammation chronique, le lichen scléreux, le tabac, la photothérapie UVA et un niveau socio-économique ou d’éducation bas. Le smegma n’est pas un cancérogène. La circoncision néonatale réduit le cancer invasif, odds ratio 0,41, mais cet effet faiblit à 0,79, intervalle 0,29 à 2, quand on ne garde que les hommes sans antécédent de phimosis. Elle ne semble pas réduire la PeIN. [S1]</p>
<p>La survie relative à cinq ans dans les données SEER citées par le chapitre est de 67 % au total, jusqu’à 81 % si la maladie est localisée, et 16 % s’il y a des métastases à distance. Ce n’est pas un registre suisse. On le présente comme tel. La p16 positive s’associe à une survie spécifique à cinq ans proche de 88 % contre 58 % si elle est négative. [S1]</p>
"""))
    P.append(ilot(DX, 3, "Physiopathologie", """
<p>Deux amorces existent. L’une est virale : le papillomavirus, surtout le 16, agit sur p16, p53 et Rb. L’autre est inflammatoire et indépendante du virus : phimosis, lichen, inflammation chronique. Le développement va de la PeIN au carcinome invasif, mais une série nord-américaine citée trouve que la PeIN isolée récidive souvent, 30 à 48 % après excision, et ne progresse vers l’invasion que dans environ 2 % des cas. [S1]</p>
<p>L’installation locale se fait dans le gland ou le prépuce, puis vers le corps spongieux, classé T2, ou les corps caverneux, classés T3, parce que l’invasion du spongieux métastase moins et survit mieux que celle des caverneux. L’urètre distal peut être envahi à travers le spongieux sans le mauvais pronostic qu’on lui prêtait autrefois : ce n’est plus un T3 pour cette seule raison. [S2]</p>
""" + w("dx8-p3-hpv",
"Le virus n’explique pas tous les épidermoïdes.",
"Dans les sous-types histologiquement indépendants du virus, la prévalence virale n’était que de 19,4 %. Dans le basaloïde elle atteint 84 %, dans le warty-basaloïde 75,7 %, dans le warty 58,7 %.",
"La p16 en immunohistochimie est le substitut d’activité virale, et elle prédit mieux la survie spécifique que la seule présence d’ADN viral, hazard ratio 0,45 dans les méta-analyses citées.",
"Le piège est de vacciner « après le cancer » en croyant effacer une lésion déjà là : le plan suisse dit que le vaccin n’élimine pas une infection ou une lésion précancéreuse déjà acquise. [S1] [S4]",
"Source [S1] [S4].") + """
<p>Le maintien métastatique passe par l’aine. Un ou deux ganglions inguinaux unilatéraux ne portent pas le même pronostic que trois ganglions, une atteinte bilatérale, une extension extra-capsulaire ou un ganglion pelvien. C’est la logique du pN. Aucun médicament ne « ferme » cette cascade à la place de la chirurgie ganglionnaire quand elle est indiquée. [S2] [S3]</p>
""" + tableau([
("Lésion", "Examen qui la montre", "Ce qui la corrige ou la classe"),
("PeIN confirmée par biopsie.", "Biopsie avant un traitement non chirurgical.", "Le résumé européen cite le 5-fluorouracile ou l’imiquimod. Les notices suisses lues ne nomment pas la PeIN du pénis : Efudix interdit le contact muqueux, Aldara vise les condylomes. [S3]"),
("Invasion du spongieux.", "L’examen et l’histologie, IRM si l’on doute de l’invasion des caverneux.", "Chirurgie d’épargne d’organe si la lésion reste au gland ou au prépuce et que le suivi sera strict. [S2] [S3]"),
("Ganglion inguinal suspect.", "Palpation des deux aines, puis biopsie guidée.", "Pas de traitement avant la preuve, puis bilan pelvien et à distance. [S3]"),
("Maladie liée au papillomavirus encore absente.", "Pas un test chez l’homme déjà cancéré pour « classer le vaccin ».", "Vaccination 9-valente des garçons selon le plan suisse 2026, avant l’exposition idéalement. [S4]"),
]) + """
"""))
    P.append(ilot(DX, 4, "Démarche diagnostique", """
<p>L’ordre commence par ne pas manquer une lésion invasive ou un ganglion fixé, puis par distinguer les dermatoses fréquentes. Une ulcération du gland qui ne guérit pas n’est pas un « champignon » jusqu’à preuve du contraire. [S5] [S1]</p>
<p>Le concurrent grave est le carcinome déjà ganglionnaire. Le signe qui tranche est un ganglion inguinal dur, fixé, ou multiple. Le piège est une antibiothérapie d’épreuve qui retarde la biopsie. La conduite, dans le résumé EAU-ASCO, est la biopsie du ganglion suspect avant de traiter, puis un TEP au fluorodésoxyglucose ou un scanner thorax-abdomen. [S3]</p>
<p>Viennent le lichen scléreux, les infections et les balanites, que le chapitre cite comme terrain plus que comme diagnostic final. Le piège est une crème prolongée sans biopsie quand la lésion persiste ou qu’un traitement non chirurgical est envisagé. La biopsie est alors forte. [S1] [S3]</p>
<p>La PeIN n’est pas l’invasion. Le piège est d’amputer pour une lésion intra-épithéliale, ou l’inverse, de topicaliser une lésion qui infiltre déjà. La biopsie sépare les deux. [S1] [S3]</p>
"""))
    P.append(ilot(DX, 5, "Anamnèse ciblée et drapeaux rouges", """
<p>On demande l’âge et depuis quand la lésion du gland ou du prépuce ne cicatrise pas, parce que le pic est à la sixième décennie et que la durée distingue une balanite aiguë d’une tumeur. [S1]</p>
<p>On demande un phimosis ancien, un lichen, un tabagisme, une photothérapie, parce que ce sont les facteurs lus, et le smegma n’en fait pas partie comme cancérogène. [S1]</p>
<p>On demande si le prépuce s’ouvre et si le malade a vu un ganglion à l’aine, parce que l’examen du prépuce caché et des deux aines change le stade. [S3]</p>
<p>On demande le statut vaccinal contre le papillomavirus et l’âge de la première dose, parce que le plan suisse 2026 change le nombre de doses selon que la première a eu lieu avant ou après le quinzième anniversaire. [S4]</p>
<p>Les drapeaux qui imposent une biopsie rapide, et non une crème de plus, sont une lésion qui s’étend, un saignement, un gland caché par un phimosis serré, et tout ganglion inguinal palpable. Un ganglion fixé ou une rétention d’urine par envahissement urétral orientent vers une filière spécialisée sans délai décoratif. Le 144 s’impose s’il existe un sepsis ou une hémorragie, pas pour une lésion stable vue au cabinet. [S3] [S5]</p>
"""))
    P.append(ilot(DX, 6, "Examen physique ciblé, région par région", """
<p>Le normal est un gland lisse, un méat au sommet, un prépuce qui se rétracte, et deux aines sans ganglion palpable. On décrit cela avant la lésion. [S3]</p>
<p>Région du gland et du prépuce. On note le siège, la taille, l’aspect et ce qui est envahi : prépuce, gland, sillon, corps. On rétracte le prépuce. Si un phimosis l’interdit, on ne conclut pas que « le gland va bien ». Le pathologique est une lésion persistante, dont la morphologie est écrite, pas le mot « plaie ». [S3]</p>
<p>Région des corps. On palpe une induration profonde qui ferait craindre un T3. L’IRM précise cette invasion quand on doute de la possibilité d’épargner l’organe. L’érection artificielle n’est pas obligatoire pour cette IRM. Si l’IRM manque, l’échographie est l’alternative faible. [S3]</p>
<p>Région des deux aines. On compte les ganglions, le côté, la mobilité ou la fixation. cN0 : rien de palpable ni de visiblement augmenté. cN1 : un ganglion mobile unilatéral. cN2 : plusieurs ganglions mobiles ou une atteinte bilatérale. cN3 : masse fixée ou adénopathie pelvienne. [S2]</p>
"""))
    P.append(ilot(DX, 7, "Approche syndromique", """
<p><em>7.1 Lésion de gland ou de prépuce</em></p>
<p>Le signe fonctionnel peut être une démangeaison, un saignement ou une impossibilité de décalotter. Le signe physique est la lésion que l’on mesure. Le geste est l’inspection après rétraction. Le mécanisme est l’épidermoïde naissant de l’épithélium interne. [S1] [S3]</p>
<p><em>7.2 Aine suspecte</em></p>
<p>Le signe fonctionnel peut manquer : le malade ne sent pas toujours le ganglion. Le signe physique est le nodule inguinal, mobile ou fixé. Le geste est la palpation comparative des deux plis. Le mécanisme est le drainage lymphatique du pénis vers l’aine, avant le pelvis. [S2] [S3]</p>
<p><em>7.3 Terrain de lichen et de phimosis</em></p>
<p>Le signe physique est un prépuce blanc, serré, ou un gland caché. Le mécanisme lu est l’inflammation chronique, pas le smegma. Le lichen est fréquent chez ces malades mais n’est pas, dans le chapitre, lié à de plus mauvais critères histologiques ni à la PeIN de façon adverse. [S1]</p>
"""))
    P.append(ilot(DX, 8, "Diagnostic positif et critères", """
<p>Le diagnostic d’invasion repose sur l’histologie. Il suffit d’une biopsie quand la malignité n’est pas évidente ou qu’on prévoit un traitement non chirurgical. Il ne suffit pas d’un aspect clinique pour commencer une crème, un laser ou une radiothérapie. L’EAU et l’ASCO le disent avec une force forte. [S3]</p>
<p>Le stade suit l’UICC, 8e édition, inchangée sur ce point dans la 9e édition de 2025 selon le chapitre. Tis : PeIN. Ta : carcinome verruqueux non invasif. T1 : tissu conjonctif sous-épithélial, T1a sans embol vasculaire, sans engainement nerveux et sans faible différenciation, T1b si l’un de ces trois est présent. T2 : corps spongieux, avec ou sans urètre. T3 : corps caverneux, avec ou sans urètre. T4 : structures adjacentes, graisse prépubienne, scrotum, cordon, os pubien, prostate. [S2]</p>
""" + w("dx8-p8-n",
"Le pN ne compte pas comme le cN.",
"pN1 : métastase dans un ou deux ganglions inguinaux. pN2 : plus de deux ganglions unilatéraux, ou une atteinte bilatérale. pN3 : ganglion pelvien ou extension extra-ganglionnaire.",
"Le texte explicatif précise que la modification visait jusqu’à deux ganglions inguinaux unilatéraux pour le pN1, parce que trois ganglions ou une bilatéralité vont plus mal.",
"Le piège est d’appeler N1 deux ganglions de chaque côté.",
"Source [S2].") + """
<p>Le stade de groupe : 0 si Tis ou Ta, N0, M0. I si T1a N0 M0. IIA si T1b ou T2, N0 M0. IIB si T3 N0 M0. IIIA si N1. IIIB si N2. IV si T4, N3 ou M1. [S2]</p>
"""))
    P.append(ilot(DX, 9, "Examens complémentaires", """
<p><em>9.a Gold standard</em></p>
<p>Le gold standard diagnostique local est l’histologie, avec le type, le grade, l’invasion, les emboles, l’engainement nerveux, les marges et la p16. Le chapitre demande ce compte rendu, idéalement selon le jeu de données ICCR, et une relecture spécialisée est souhaitable pour cette tumeur rare. [S1] [S3]</p>
<p><em>9.b 1<sup>re</sup> intention</em></p>
<p>En première intention clinique : examen du pénis et des deux aines, biopsie si besoin, échographie inguinale avec cytoponction des ganglions anormaux avant un ganglion sentinelle. L’IRM du pénis si l’on doute de l’invasion des corps ou de la faisabilité d’une chirurgie conservatrice. L’érection artificielle n’est pas obligatoire. L’échographie remplace l’IRM si elle n’est pas disponible, recommandation faible. [S3]</p>
<p>Le terme IRM juste est l’{b("dx8-p9-signal","hyposignal ou l’hypersignal")} selon la séquence, pas une « tache ». Le chapitre lu ne décrit pas une séquence unique obligatoire. On n’invente pas un hypersignal T2 chiffré. On dit que l’IRM cherche l’invasion des corps caverneux quand l’examen hésite. [S3]</p>
""" + w("dx8-p9-signal",
"En IRM, le signal se compare à un tissu de référence et se nomme avec la séquence.",
"Un hypersignal T2 n’a pas le même sens qu’un hyposignal T1. Le chapitre de stadification ne fige pas une séquence pour le pénis. Il dit quand demander l’examen.",
"Exemple : doute sur l’invasion du corps caverneux avant de promettre une épargne du gland. L’IRM aide. Elle ne remplace pas la biopsie. [S3]",
"Le piège est d’écrire « IRM anormale » sans dire ce qui est envahi.",
"Source [S3].") + """
""" + tableau([
("Résultat", "Interprétation", "Hypothèse"),
("Biopsie : PeIN, p16 positive, pas d’invasion.", "Précurseur associé au virus.", "Un traitement topique peut se discuter, pas une amputation. [S1] [S3]"),
("Biopsie : invasion du chorion, grade élevé ou embole.", "Au moins T1b si le reste du compte rendu le confirme.", "Stadification ganglionnaire chirurgicale à discuter, car le risque de micrométastase est haut. [S2] [S3]"),
("Aines vides, tumeur T1a.", "cN0 à faible risque relatif.", "La surveillance peut se discuter selon le grade. Pour T1a G2, la surveillance est une alternative faible si le suivi sera strict. [S3]"),
("Ganglion palpable.", "cN+ jusqu’à preuve histologique.", "Biopsie d’abord, pas de curage sur la seule palpation. [S3]"),
("p16 absente sur une tumeur invasive.", "Ce n’est pas un échec de coloration anodin.", "Le pronostic spécifique est moins bon dans les séries citées, environ 58 % de survie à cinq ans contre 88 %. [S1]"),
]) + """
<figure>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 160" role="img" aria-label="Schéma des niveaux T2 et T3">
<rect width="360" height="160" fill="#fbfaf7"/>
<rect x="40" y="40" width="280" height="70" rx="30" fill="#f3e6d4" stroke="#6b4f32"/>
<rect x="70" y="55" width="220" height="18" fill="none" stroke="#b45309" stroke-dasharray="4 3"/>
<text x="78" y="68" font-size="12" fill="#9a3412">1 spongieux T2</text>
<rect x="90" y="78" width="180" height="22" fill="none" stroke="#9f1239" stroke-dasharray="4 3"/>
<text x="98" y="94" font-size="12" fill="#9f1239">2 caverneux T3</text>
</svg>
<figcaption>Schéma didactique. Aucune photographie clinique libre n’a été embarquée le 9 novembre 2026.</figcaption>
<ol>
<li>Le contour ocre rappelle le corps spongieux, dont l’invasion définit le T2, urètre compris ou non.</li>
<li>Le contour rouge rappelle les corps caverneux, dont l’invasion définit le T3.</li>
</ol>
</figure>
<p><em>9.c Alternatives</em></p>
<p>Si l’IRM est impossible, échographie. Si le malade ne peut pas recevoir un produit iodé, le chapitre ne fait pas du scanner le test du pénis lui-même. L’allergie et le débit de filtration ne sont pas détaillés dans les pages lues pour cette tumeur : on ne fixe pas un seuil de DFG. [S3]</p>
<p><em>9.d 2<sup>e</sup> intention</em></p>
<p>Pour un cN0 à risque, T1b ou plus, le ganglion sentinelle est proposé. S’il n’est pas disponible ou si le malade informé le refuse, le curage inguinal, ouvert ou vidéo-endoscopique, est l’alternative. Pour un cN+, le TEP ou le scanner thorax-abdomen cherche le pelvis et les métastases avant le traitement. [S3]</p>
"""))
    P.append(ilot(DX, 10, "Arbre décisionnel", """
<p>Si la lésion n’est pas évidemment maligne ou qu’on veut un traitement non chirurgical, alors biopsie d’abord.</p>
<p>Si la biopsie montre une PeIN, alors traitement topique par 5-fluorouracile ou imiquimod, contrôle clinique après un intervalle sans traitement, nouvelle biopsie si doute, et pas de second essai topique en cas d’échec. [S3]</p>
<p>Si la lésion est limitée au gland ou au prépuce, Ta, T1 ou T2, et que le malade acceptera un suivi strict, alors chirurgie d’épargne, en le prévenant que la récidive locale est plus fréquente qu’après amputation. Marge congelée si l’on doute. [S3]</p>
<p>Si les aines sont vides et la tumeur T1b ou plus, alors stadification ganglionnaire chirurgicale, sentinelle de préférence. Si c’est un T1a G2 et que le suivi sera strict, la surveillance est une alternative faible. [S3]</p>
<p>Si un ganglion est palpable, alors biopsie, puis TEP ou scanner, puis traitement adapté. On ne commence pas par une chimiothérapie d’induction hors lésion primitive non résécable ou maladie locale avancée, situations où le résumé propose induction puis chirurgie chez les répondeurs, ou chimioradiothérapie. [S3]</p>
"""))
    P.append(ilot(DX, 11, "Prise en charge selon les recommandations suisses", """
<p><em>11.A But</em></p>
<p>Le but local est d’enlever la tumeur avec une marge saine tout en gardant le plus de verge possible quand la lésion s’y prête. Le but ganglionnaire est de ne pas laisser une micrométastase chez un malade à risque, sans curage inutile chez tous les T1a. Le but chiffré de survie n’est pas une promesse individuelle : les chiffres SEER cités sont 81 % à cinq ans si localisé et 16 % si métastatique. [S1] [S3]</p>
<p><em>11.B Moyens</em></p>
<p>Il n’y a pas de minute vitale hors saignement ou sepsis, qui relèvent du 144. Une lésion vue au cabinet est une filière rapide, pas une urgence de la nuit, sauf ces complications. [S5]</p>
""" + w("dx8-p11-topique",
"Le topique concerne la PeIN biopsée, pas une ulcération non prouvée.",
"Le résumé EAU-ASCO offre le 5-fluorouracile ou l’imiquimod. On contrôle après une fenêtre sans traitement. En cas d’échec, on ne recommence pas le même topique.",
"Aucune spécialité suisse, aucun pourcentage de crème et aucun rythme hebdomadaire ne figurent dans cette monographie : le texte Swissmedic de ces topiques n’a pas été ouvert le 9 novembre 2026, et le corpus AIPS local manquait.",
"Le piège est de donner la crème à la place de la biopsie.",
"Source [S3].") + """
<p>L’ordre local est : biopsie si nécessaire, discussion partagée qui dit le surcroît de récidive locale de l’épargne d’organe, puis conservation si le gland et le prépuce contiennent la maladie et que le suivi sera tenu, sinon chirurgie plus large. La radiothérapie est une option pour des T1 ou T2 sélectionnés et biopsiés. Le laser CO2 ou Nd:YAG est cité pour PeIN, Ta ou T1 biopsiés. [S3]</p>
<p>L’ordre ganglionnaire chez le cN0 à risque est l’échographie de l’aine avec cytoponction de ce qui est anormal, puis le ganglion sentinelle, puis le curage si la sentinelle n’est pas accessible. Chez le cN+, biopsie puis imagerie du tronc avant le traitement. [S3]</p>
<p>Aucune chimiothérapie n’a de dose dans cette monographie. Le résumé parle d’induction pour les lésions primitives non résécables ou localement avancées, chez les répondeurs, avant la chirurgie. Il ne donne pas le cisplatine en milligrammes par mètre carré dans l’extrait lu. On ne le reconstitue pas. [S3]</p>
<p>La prévention par Gardasil® 9 suit la notice n° 65387, qui renvoie aux recommandations officielles. Le plan suisse 2026 vise les filles et les garçons, avec un rattrapage jusqu’au vingtième anniversaire. Le vaccin couvre les types 6, 11, 16, 18, 31, 33, 45, 52 et 58. Il n’efface pas une lésion déjà présente. [S4]</p>
<p>Situations particulières. L’immunodépression chez l’adolescent vaccinable impose trois doses. L’homme déjà porteur d’un cancer n’est pas « rattrapé » par le vaccin pour guérir la tumeur. Le chapitre ne détaille pas la grossesse d’une partenaire comme une contre-indication opératoire. L’insuffisance rénale n’a pas de palier lu pour la chirurgie. [S4] [S3]</p>
<p><em>11.C Surveillance</em></p>
<p>Le suivi est strict après épargne d’organe, parce que la récidive locale est plus fréquente qu’après amputation. Après topique, on revoit à distance de l’arrêt et l’on rebiopsie au doute. Le résumé ne donne pas, dans l’extrait, un calendrier en mois. On n’en fabrique pas. On dit que le suivi manqué retire l’indication de la conservation. [S3] [S5]</p>
<p><em>11.D Pronostic</em></p>
<p>La PeIN isolée progresse peu, environ 2 %, mais récidive souvent après excision. Le verruqueux a une mortalité citée à 0 % dans le tableau des sous-types. Le sarcomatoïde va de 45 à 90 %. La p16 positive améliore la survie spécifique. Une extension extra-ganglionnaire ou un ganglion pelvien classent pN3 et assombrissent le stade. [S1] [S2]</p>
<p>Sortie après chirurgie : plaie expliquée, consigne de reconsulter si le gland saigne ou si un ganglion apparaît, et date de suivi écrite. Pas de promesse que l’épargne vaut une amputation pour le risque local. [S3]</p>
"""))
    P.append(ilot(DX, 12, "Prévention", """
<p>Primaire : le plan suisse 2026 fait de la vaccination contre le papillomavirus une vaccination de base des garçons comme des filles, avec un objectif de couverture relevé de 80 à 90 % jusqu’à 14 ans. Le schéma à deux ou trois doses est celui du point 11. Idéalement avant les premiers rapports, mais le plan vaccine encore après, parce qu’une infection déjà là ne protège pas contre les autres types du vaccin. [S4]</p>
<p>Secondaire : ne pas laisser un phimosis cacher un gland, et biopsier ce qui ne guérit pas. Le chapitre rappelle que la circoncision néonatale réduit l’invasif surtout via le phimosis, sans être présentée comme un programme suisse obligatoire. [S1]</p>
<p>Tertiaire : suivi après traitement conservateur, et arrêt du tabac, facteur lu, sans seuil de paquets-années dans la page. [S1] [S3]</p>
"""))
    P.append(ilot(DX, 13, "Points clés", """
<p>Plus de 95 % des cancers du pénis sont des épidermoïdes, et la Suisse est dans le groupe européen à incidence basse, sans taux OFS lu.</p>
<p>Tis est la PeIN. T2 est le spongieux. T3 est le caverneux. L’urètre seul ne fait plus un T3.</p>
<p>pN1 est un ou deux ganglions inguinaux. Trois ganglions, la bilatéralité ou l’extension extra-capsulaire changent de catégorie.</p>
<p>On ne met pas de crème, de laser ou de radiothérapie sans biopsie, et un topique qui échoue ne se répète pas.</p>
<p>L’épargne d’organe se paie d’un suivi strict, parce que la récidive locale y est plus fréquente.</p>
<p>Le vaccin 9-valent des garçons est une base suisse depuis le plan 2026. Il ne traite pas une tumeur déjà là.</p>
"""))
    P.append(ilot(DX, 14, "Pièges et questions fréquentes à l'examen fédéral suisse", """
<p>Question : T2 ou T3 si le corps spongieux et l’urètre sont envahis, sans caverneux ? Réponse : T2. Le caverneux fait le T3. [S2]</p>
<p>Question : deux ganglions inguinaux d’un seul côté, c’est quoi ? Réponse : pN1. Le troisième, ou l’autre aine, font pN2. Un ganglion pelvien ou une extension extra-capsulaire font pN3. [S2]</p>
<p>Question : 0,94 pour 100 000 est-il suisse ? Réponse : non. C’est l’ordre de grandeur européen. La Suisse est citée dans le groupe à incidence basse, sans ce taux propre dans la page. [S1]</p>
<p>Question : le smegma est-il cancérogène ? Réponse : non, selon le chapitre. Le phimosis, lui, est fortement associé à l’invasif. [S1]</p>
<p>Question : odds ratio 0,41 de la circoncision néonatale, que devient-il sans phimosis ? Réponse : 0,79, intervalle 0,29 à 2, donc l’effet n’est plus net. [S1]</p>
<p>Question : 50,8 % de virus signifie-t-il que tous les basaloïdes sont viraux ? Réponse : non. 50,8 % est la prévalence globale. Le basaloïde est à 84 %, le sous-type indépendant à 19,4 %. [S1]</p>
<p>Question : peut-on surveiller un T1b cN0 ? Réponse : non comme option faible standard. La stadification chirurgicale est forte à partir de T1b. La surveillance alternative faible citée vise le T1a G2 si le suivi est strict. [S3]</p>
<p>Question : combien de doses de Gardasil® 9 si la première injection a lieu à 14 ans ? Réponse : la notice 65387 prévoit trois doses de 0,5 ml à 0, 2 et 6 mois, ou deux doses si la seconde est donnée entre 5 et 13 mois après la première. [S4]</p>
<p>Question : le vaccin guérit-il une PeIN ? Réponse : non. Le plan dit qu’il n’élimine pas une infection ou une lésion précancéreuse déjà là. [S4]</p>
<p>Question : la posologie d’Aldara pour les condylomes s’applique-t-elle à la PeIN du pénis ? Réponse : non. La notice 55070 réserve cette crème, trois fois par semaine, aux condylomes acuminés externes de l’adulte. La PeIN n’y est pas indiquée. [S3]</p>
<p>On ajoute, pour ne pas laisser le stade en adjectifs, la lecture d’un compte rendu fictif mais conforme. « Épidermoïde usuel du gland, 18 mm, invasion du spongieux, caverneux indemnes, urètre superficiel atteint, p16 positive, marges saines, aines sans ganglion palpable. » Cela se code T2 cN0, stade IIA si M0, et non T3. L’urètre n’a pas fait monter le T. Le spongieux l’a fixé à T2. La p16 positive ne change pas le T. Elle change le commentaire pronostique. Ensuite seulement on discute l’épargne, parce que la lésion est au gland, et la sentinelle, parce qu’un T2 n’est pas un T1a G2 surveillable. [S2] [S3]</p>
<p>Deuxième compte rendu. « PeIN différenciée du prépuce, pas d’invasion, p16 négative. » Pas d’amputation. Topique ou exérèse locale. Pas de curage. Le vaccin ne traite pas cette lésion. Le nom de Bowen n’est pas repris. [S1] [S3] [S4]</p>
<p>Troisième compte rendu, pour le piège bilatéral. « Deux ganglions inguinaux métastatiques, un de chaque côté, pas de pelvis, pas de rupture capsulaire. » Ce n’est pas pN1, malgré le mot « deux ». La bilatéralité, dans le texte qui explique la réforme du N, sort du pN1. On dit pN2, stade IIIB si le T reste entre T1 et T3. Une rupture capsulaire sur un seul de ces ganglions ferait pN3 et stade IV, même sans métastase viscérale. Cette bascule est le cœur du point 8. [S2]</p>
<p>On peut enfin répondre à la question du candidat qui mélange vaccination et stade. Le vaccin 9-valent du plan 2026 réduit le risque d’infection par les types qu’il contient. Il ne reclasse pas un T2 déjà biopsié, il n’efface pas une PeIN, et il ne remplace pas la sentinelle d’un T1b. Inversement, un stade lourd n’interdit pas de dire à un frère de 14 ans qu’il est encore dans la fenêtre à deux doses. Les deux sujets partagent le virus. Ils ne partagent pas le geste. [S3] [S4]</p>
<p>Dernière vérification de cohérence avant de quitter le fichier. T2 veut dire spongieux, pas caverneux. T3 veut dire caverneux. pN1 veut dire un ou deux ganglions inguinaux, et le texte explicatif les veut unilatéraux. pN2 commence au troisième ganglion ou à l’autre aine. pN3 est le pelvis ou la capsule rompue. La crème vient après la biopsie et ne se répète pas si elle échoue. L’épargne suppose un malade qui reviendra. La Suisse est dans le groupe bas, sans taux propre lu. Le plan 2026 vaccine les garçons. Les doses de crème et de vaccin qui comptent sont celles des notices 36464, 55070 et 65387, pas une extrapolation. [S1] [S2] [S3] [S4]</p>
<p>Si une seule erreur devait être évitée le jour de l’épreuve, ce serait d’appeler T3 un envahissement de l’urètre distal qui ne touche que le spongieux : le chapitre a corrigé cette ancienne équivalence, parce que ce trajet n’aggrave pas le pronostic comme l’atteinte des caverneux, et la bonne lettre est donc T2. Les caverneux, eux, restent le T3, et c’est cette distinction que l’IRM doit éclairer quand le toucher hésite, sans que l’érection artificielle soit exigée. [S2] [S3]</p>
"""))
    P.append("""
<section class="ilot sources">
<h3>Sources</h3>
<p>[S1] Association européenne d’urologie, Guidelines on Penile Cancer, chapitre épidémiologie, étiologie et pathologie, consulté le 9 novembre 2026. https://uroweb.org/guidelines/penile-cancer/chapter/epidemiology-aetiology-and-pathology</p>
<p>[S2] Même guideline, chapitre classification et stade TNM, 8e et 9e éditions UICC, consulté le 9 novembre 2026. https://uroweb.org/guidelines/penile-cancer/chapter/staging-and-classification-systems</p>
<p>[S3] Résumé des recommandations EAU-ASCO sur le cancer du pénis, diapositives collaboratives, consultées le 9 novembre 2026. https://ascopubs.org/pb-assets/guideline-assets/2023-EAU-ASCO-Penile-Cancer/2023-EAU-ASCO-Penile-Cancer-Slides.pdf</p>
<p>[S4] Office fédéral de la santé publique, Plan de vaccination suisse 2026, chapitre HPV, PDF consulté le 9 novembre 2026. https://www.bag.admin.ch/dam/fr/sd-web/Oj0BSN-w-Ggs/Plan%20de%20vaccination%20suisse_2026_FR_Web_final.pdf</p>
<p>[S5] Revue Médicale Suisse 2024;897, Narimani et al., cancer du pénis, résumé consulté le 9 novembre 2026. Le corps de l’article n’était pas dans l’extrait reçu. https://www.revmed.ch/revue-medicale-suisse/2024/revue-medicale-suisse-897/cancer-du-penis-tour-d-horizon-des-approches-diagnostiques-et-therapeutiques</p>
<p>Cette monographie du carcinome épidermoïde du pénis cite ces pages et demeure non validé cliniquement.</p>
</section>
""")
    html = "\n".join(P)
    from dx8_extra import extra
    from dx8_extra2 import extra2
    from dx8_extra3 import extra3
    from dx8_extra4 import extra4
    from dx8_extra5 import extra5
    from dx8_extra6 import extra6
    from dx8_extra7 import extra7
    plus = extra()
    for src in (extra2(), extra3(), extra4(), extra5(), extra6(), extra7()):
        for k, v in src.items():
            plus[k] = plus.get(k, "") + v
    for n, block in plus.items():
        start = html.find(f'id="dx{DX}-i{n}"')
        if start < 0:
            raise SystemExit(n)
        end = html.find("</section>", start)
        html = html[:end] + block + html[end:]
    from dx8_aips import BLOC
    ancre = 'id="dx8-i11"'
    h3fin = html.find("</h3>", html.find(ancre))
    if h3fin < 0:
        raise SystemExit("dx8 point 11")
    return html[: h3fin + 5] + BLOC + html[h3fin + 5 :]

if __name__ == "__main__":
    from assembler import ecrire
    ecrire(8, "Carcinome épidermoïde du pénis", body())

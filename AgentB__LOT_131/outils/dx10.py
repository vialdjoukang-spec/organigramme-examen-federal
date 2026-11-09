# -*- coding: utf-8 -*-
"""DX.10 Gangrène de Fournier. Doses = EAU 2024 ou RMS, pas AIPS."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from dx_lib import b, w, ilot, tableau
DX = 10

def body() -> str:
    P = []
    P.append(ilot(DX, 1, "Définition et sémantique", """
<p>La gangrène de Fournier est, dans le résumé 2024 des recommandations européennes d’infections urologiques, une infection polymicrobienne agressive et souvent mortelle des tissus mous du périnée, de la région péri-anale et des organes génitaux externes. [S1]</p>
""" + w("dx10-p1-fn",
"La Revue Médicale Suisse classe cette atteinte comme la localisation génitale d’une fasciite nécrosante.",
"Le fascia superficiel du tissu sous-cutané se nécrose, les microthrombi coupent la perfusion, la peau peut encore paraître presque banale.",
"Le type I est polymicrobien, surtout chez l’immunodéprimé. Le type II est à streptocoque du groupe A, y compris chez un sujet sain. La revue de 2014 ne trouve pas de différence de morbi-mortalité ni de prise en charge entre ces types.",
"Le piège est de réserver le mot Fournier au diabétique : le type II touche aussi l’homme sain. [S2]",
"Source [S1] [S2].") + """
<p>Ce n’est pas un érysipèle, qui reste superficiel et peut se traiter sans bistouri. Ce n’est pas une gangrène gazeuse à clostridie, rare, liée à une plaie très contaminée. Ce n’est pas une cellulite qui répond aux antibiotiques seuls. Le chapitre urologique et les deux revues romandes convergent : sans excision, l’antibiotique ne suffit pas. [S1] [S2] [S3]</p>
"""))
    P.append(ilot(DX, 2, "Épidémiologie (Suisse, puis Europe)", """
<p>Aucune incidence OFS, Obsan ou cantonale de la gangrène de Fournier n’a été ouverte le 9 novembre 2026. Le résumé EAU ne donne pas non plus un taux pour 100 000. On n’en fabrique pas. La liste du lot place cette entité en fin de fréquence, justement parce que l’incidence populationnelle manquait dans les chapitres lus. [S1]</p>
<p>Ce qui est chiffré, c’est le mode de début et le terrain. Jusqu’à 40 % des cas commencent de façon insidieuse, et la douleur non reconnue retarde le traitement. Les facteurs de survenue et de mortalité cités sont l’immunodépression, le plus souvent le diabète ou la dénutrition, une chirurgie urétrale ou périnéale récente, et un indice de masse corporelle élevé. [S1]</p>
""" + w("dx10-p2-40",
"Quarante pour cent n’est pas une mortalité.",
"C’est la part de débuts trompeurs dans le résumé EAU. La mortalité est dite fréquente, et la revue romande de 2014 la dit encore très élevée, conditionnée par le délai entre l’admission et le bloc, sans pourcentage unique dans les passages lus.",
"Exemple : un homme obèse diabétique avec une douleur périnéale depuis quatre jours est dans le scénario insidieux, pas dans une cellulite du jour.",
"Le piège est de rassurer parce que la fièvre manque : la revue de 2014 dit la fièvre et les crépitations rares à l’admission. [S1] [S2]",
"Source [S1] [S2].") + """
<p>Chez l’individu, l’histoire va de la porte d’entrée, parfois inaperçue, à la nécrose qui dépasse largement la peau, puis au sepsis. La revue de 2020 dit que la chirurgie dans les 24 heures après l’admission améliore la survie. La revue de 2014 parle d’heures après l’hospitalisation. Les deux insistent sur le délai. Aucun ne donne une létalité suisse. [S2] [S3]</p>
"""))
    P.append(ilot(DX, 3, "Physiopathologie", """
<p>L’amorce est une effraction cutanée, urétrale ou péri-anale, parfois invisible. Le développement est celui d’une fasciite : enzymes et toxines liquéfient le tissu, le long du fascia superficiel, pas d’abord du fascia musculaire. L’installation est une douleur majeure pour une peau encore modeste, puis des bulles, une crépitation inconstante, un sepsis. Le maintien est la nécrose qui court plus loin que la rougeur, avec des microthrombi. [S2]</p>
<p>Le streptocoque du groupe A peut faire un érysipèle ou une fasciite. Le staphylocoque peut faire un abcès ou une bactériémie. La revue refuse donc de classer seulement par le germe. Elle classe par la profondeur. Quand les organes génitaux sont pris, le nom devient Fournier, sans changer la logique. [S2]</p>
""" + w("dx10-p3-toxine",
"La clindamycine est citée pour bloquer la synthèse des toxines, pas seulement pour tuer.",
"La revue de 2014 la dose à 600 mg toutes les six heures ou 900 mg toutes les huit heures, par voie intraveineuse, pendant trois à cinq jours, même si le germe est résistant in vitro.",
"Une seule étude observationnelle montrait un bénéfice, odds ratio 4,7, intervalle de confiance à 95 % de 1,0 à 25,0 : l’incertitude reste large.",
"Le piège est de présenter cet odds ratio comme une preuve définitive. [S2]",
"Source [S2]. Ce schéma n’est pas une information professionnelle Swissmedic relue.") + """
<p>La stratégie qui corrige la nécrose est le bistouri, répété. L’antibiotique couvre les germes et, pour la clindamycine, les toxines. Aucun des deux ne remplace l’autre. L’EAU 2024 réserve les traitements adjuvants, en dehors de cette paire, aux essais. [S1] [S2]</p>
""" + tableau([
("Lésion", "Ce qui la montre", "Ce qui la corrige"),
("Nécrose du fascia bien plus large que la peau.", "L’examen, puis le bloc : tissu gris, peu saignant, qui se décolle au doigt.", "Excision de tout ce qui se décolle, reprise jusqu’à stabilisation. [S2]"),
("Toxines streptococciques ou staphylococciques.", "Le tableau de sepsis, pas un dosage de toxine au cabinet.", "Clindamycine intraveineuse en plus du bêtalactame large, doses des revues citées, pas un schéma Swissmedic. [S2] [S3]"),
("Atteinte pararectale.", "Scanner ou IRM, si cela ne retarde pas la première excision quand le diagnostic est clinique.", "Dérivation digestive si l’imagerie le suggère, sonde sus-pubienne pour l’urine. [S1]"),
("Participation musculaire.", "Créatine phosphokinase sanguine élevée, sans seuil chiffré dans la revue.", "Le même débridement, étendu au muscle mort. [S2]"),
]) + """
"""))
    P.append(ilot(DX, 4, "Démarche diagnostique", """
<p>L’ordre est la vie d’abord. On traite comme une fasciite tant que la douleur, l’état général et la progression ne l’ont pas écartée. L’érysipèle et la cellulite, plus fréquents, viennent après, pas avant. [S2] [S3]</p>
<p>Le concurrent mortel est la fasciite elle-même. Le signe qui tranche est la douleur disproportionnée, la limite floue, l’aggravation en heures, un sepsis. Le piège est une peau encore « pas si mauvaise ». La conduite est le bloc, pas un scanner qui retarde si le tableau est déjà clair. La revue de 2020 le dit : la chirurgie précoce ne se diffère pas. [S2] [S3]</p>
<p>L’abcès simple se collecte, se flucue, et ne court pas sous une peau à distance. La gangrène gazeuse clostridienne est rare et historique dans la revue. La torsion du testicule fait mal, mais elle ne nécrose pas le périnée. On n’envoie pas un périnée noir vers l’arbre de la bourse aiguë seule. [S2]</p>
<p>Jusqu’à 40 % des Fournier commencent sans le tableau fulminant. Le piège est l’homme obèse chez qui on n’a pas écarté les plis. L’EAU demande un examen soigneux, surtout dans ce cas. [S1]</p>
"""))
    P.append(ilot(DX, 5, "Anamnèse ciblée et drapeaux rouges", """
<p>On demande le diabète, la dénutrition, une opération urétrale ou périnéale récente et le poids, parce que ce sont les facteurs du résumé EAU. [S1]</p>
<p>On demande depuis quand la douleur dépasse ce que la peau montre, parce que cette disproportion est le drapeau de la revue de 2014 et de 2020. [S2] [S3]</p>
<p>On demande une fièvre, sans être rassuré par son absence : elle est rare à l’admission dans la fasciite de la revue de 2014, de même que les crépitations. [S2]</p>
<p>On demande les antibiotiques déjà pris, parce qu’ils peuvent négativer les cultures, fait noté par la revue. [S2]</p>
<p>Les drapeaux qui imposent le 144 et le bloc sont le sepsis, la progression en quelques heures, la douleur majeure, une crépitation, une bulle, un périnée dont on ne voit pas la limite. On n’attend pas la biologie pour appeler. [S1] [S2] [S3]</p>
"""))
    P.append(ilot(DX, 6, "Examen physique ciblé, région par région", """
<p>Le normal du périnée est une peau souple, douloureuse seulement si on pince fort, sans bulle, sans crépitation, avec des plis que l’on peut écarter. On regarde cela, chez l’obèse, en écartant vraiment. [S1]</p>
<p>Région cutanée. Le pathologique précoce peut être une rougeur mal limitée, peu impressionnante. Le pathologique tardif est la bulle, la plaque livide, la nécrose noire. La revue insiste : la douleur et l’état général précèdent souvent ces signes. [S2]</p>
<p>Région des organes génitaux et du périnée. On cherche jusqu’où la douleur et la crépitation, si elle existe, dépassent la rougeur. Le doigt, au bloc, confirme : le tissu gris se décolle sans résistance et saigne peu. Ce geste n’est pas un examen de cabinet. [S2]</p>
<p>Région générale. Le sepsis se voit au regard, à la tension, à la conscience. La revue de 2014 rappelle que la fasciite est une maladie de système, pas une peau. [S2]</p>
"""))
    P.append(ilot(DX, 7, "Approche syndromique", """
<p><em>7.1 Syndrome de douleur disproportionnée</em></p>
<p>Le signe fonctionnel est une douleur qui ne colle pas à la rougeur. Le signe physique peut être pauvre au début. Le geste est de croire le malade et de marquer au feutre les limites pour voir la progression. Le mécanisme est la nécrose du fascia sous une peau encore vivante. [S2] [S3]</p>
<p><em>7.2 Syndrome de sepsis périnéal</em></p>
<p>Le signe fonctionnel est le malaise, le frisson peut manquer. Le signe physique est l’atteinte hémodynamique. Le geste est le 144 ou la salle d’urgence, les voies, le remplissage selon l’équipe de réanimation, sans dose inventée ici. Le mécanisme est toxémique et nécrotique. [S1] [S2]</p>
<p><em>7.3 Syndrome de crépitation et de bulle</em></p>
<p>Le signe physique tardif est la neige sous le doigt ou la bulle hémorragique. Il est inconstant à l’arrivée. Son mécanisme est le gaz bactérien ou le décollement. L’attendre pour décider, c’est arriver trop tard. [S2]</p>
"""))
    P.append(ilot(DX, 8, "Diagnostic positif et critères", """
<p>Le diagnostic qui décide est clinique. La revue de 2014 le dit essentiel. L’EAU décrit le gonflement douloureux avec sepsis. Il n’y a pas de score obligatoire dans ces pages. Aucun total de points de LRINEC n’est recopié, parce que ce score n’était pas dans les textes ouverts. [S1] [S2]</p>
<p>Ce qui suffit à aller au bloc : la suspicion forte. Ce qui ne suffit pas à rester au lit : un scanner « pour confirmer », une culture en attente, une amélioration partielle sous antibiotique déjà commencé en ville. La preuve visuelle est opératoire : tissu gris, peu saignant, qui file au doigt. L’histologie aide, elle ne précède pas l’excision. [S2] [S3]</p>
"""))
    P.append(ilot(DX, 9, "Examens complémentaires", """
<p><em>9.a Gold standard</em></p>
<p>Le gold standard décisionnel est l’exploration chirurgicale. Elle confirme, prélève, et traite. L’imagerie n’est pas l’étalon. [S2] [S3]</p>
<p><em>9.b 1<sup>re</sup> intention</em></p>
<p>En première intention, si le diagnostic est déjà clinique, on n’attend rien. Si l’on hésite sur l’extension pararectale, le scanner ou l’IRM peuvent montrer une collection ou une fasciite et suggérer une dérivation digestive. Ils ne doivent pas reculer l’heure du premier bloc quand la suspicion est forte. [S1] [S3]</p>
<p>Le terme scanographique juste, quand il y a du gaz, est une {b("dx10-p9-gaz","clarté gazeuse")} des parties molles, pas une « tache ». La revue dit que les crépitations sont rares à l’admission : l’absence de gaz n’élimine donc pas la fasciite. [S2]</p>
""" + w("dx10-p9-gaz",
"Une clarté gazeuse au scanner est du gaz dans un tissu qui ne devrait pas en contenir.",
"Elle peut manquer au début. La fasciite de type II, streptococcique, n’est pas la gangrène gazeuse clostridienne.",
"Exemple : douleur majeure, peau peu marquée, scanner sans gaz. On opère quand même si la clinique est celle d’une fasciite. [S2] [S3]",
"Le piège est d’exiger le gaz pour appeler le chirurgien.",
"Source [S2].") + """
""" + tableau([
("Résultat", "Interprétation", "Hypothèse"),
("Douleur majeure, peau modeste, pas de gaz au scanner.", "L’image n’innocente pas.", "Fasciite encore possible, le bloc ne se négocie pas sur l’absence de gaz. [S2] [S3]"),
("Scanner : extension pararectale.", "Le rectum ou l’anus peuvent être dans le trajet.", "Discuter une dérivation digestive, sans remplacer l’excision. [S1]"),
("Créatine phosphokinase élevée.", "Le muscle participe.", "Élargir le débridement au muscle mort. Le seuil exact n’est pas dans la revue. [S2]"),
("Hémocultures et prélèvements de tissu positifs ensuite.", "On adapte l’antibiotique.", "On ne les attend pas pour inciser ni pour commencer le traitement large. [S1]"),
("Culture négative après antibiotique préalable.", "Faux négatif possible.", "La clinique et le bloc restent vrais. [S2]"),
]) + """
<figure>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 150" role="img" aria-label="Schéma de nécrose plus large que la peau">
<rect width="360" height="150" fill="#fbfaf7"/>
<ellipse cx="180" cy="80" rx="70" ry="40" fill="#fecaca" stroke="#991b1b"/>
<ellipse cx="180" cy="80" rx="120" ry="60" fill="none" stroke="#9f1239" stroke-width="3" stroke-dasharray="5 4"/>
<text x="150" y="84">1</text>
<text x="250" y="40" fill="#9f1239">2</text>
</svg>
<figcaption>Schéma didactique. Aucune photographie de périnée n’a été embarquée le 9 novembre 2026.</figcaption>
<ol>
<li>La zone rouge rappelle la peau visible, souvent trop petite.</li>
<li>Le contour pointillé rappelle la nécrose sous-cutanée, plus large, que le bloc doit suivre.</li>
</ol>
</figure>
<p><em>9.c Alternatives</em></p>
<p>Si le scanner iodé est impossible, l’IRM est l’autre examen cité par l’EAU pour l’extension pararectale. Ni l’un ni l’autre ne remplace le doigt du chirurgien. L’allergie et le débit de filtration ne changent pas l’indication d’inciser. [S1]</p>
<p><em>9.d 2<sup>e</sup> intention</em></p>
<p>L’histologie et la culture de tissu viennent du bloc, pas d’une biopsie programmée la veille. La sérologie antistreptolysine O peut confirmer un streptocoque après coup. Elle ne décide pas l’heure de l’incision. [S2]</p>
"""))
    P.append(ilot(DX, 10, "Arbre décisionnel", """
<p>Si la douleur périnéale est disproportionnée ou le sepsis est là, alors 144 ou bloc, antibiotique large dès la présentation, excision sans attendre une image parfaite.</p>
<p>Si l’on est obèse ou diabétique et que la douleur est là depuis des jours, alors on examine les plis comme si le tableau insidieux des 40 % était le sien. [S1]</p>
<p>Si le scanner montre une extension pararectale, alors on discute une stomie, et l’on met une sonde sus-pubienne pour détourner l’urine, comme le dit l’EAU. [S1]</p>
<p>Si le premier débridement est fait, alors on prévoit une reprise, à 24-48 heures dans la revue de 2020, ou environ toutes les 48 heures jusqu’à stabilisation dans la revue de 2014, puis tous les un à deux jours tant qu’il reste de la nécrose. [S2] [S3]</p>
<p>Si l’on pense à une oxygénation hyperbare ou à des immunoglobulines, alors on n’en retarde pas le bloc. L’EAU 2024 réserve les adjuvants aux essais. La revue de 2014 les discute avec un niveau de preuve faible et la même interdiction de retarder. [S1] [S2]</p>
"""))
    P.append(ilot(DX, 11, "Prise en charge selon les recommandations suisses", """
<p><em>11.A But</em></p>
<p>Le but est de stopper la nécrose et le sepsis. Le délai est l’instrument : heures après l’arrivée selon la revue de 2014, et dans les 24 heures après l’admission selon la revue de 2020 pour améliorer la survie. L’EAU dit que des excisions répétées et une dérivation urinaire sus-pubienne sont nécessaires pour réduire la mortalité, sans donner un pourcentage cible. [S1] [S2] [S3]</p>
<p><em>11.B Moyens</em></p>
<p>L’ordre est : reconnaître, appeler, remplir et soutenir selon la réanimation, commencer l’antibiotique à la présentation, couper tout de suite, revoir la plaie, adapter le germe, couvrir plus tard. [S1] [S3]</p>
""" + w("dx10-p11-chrono",
"Urgence, conduite chronologique.",
"Minute 0 : douleur disproportionnée reconnue, 144 si l’on n’est pas à l’hôpital. À l’arrivée : voies, prélèvements, antibiotique du tableau sans attendre le scanner si la clinique est claire. Dans les heures : bloc, excision au doigt de tout ce qui se décolle, sonde sus-pubienne.",
"À 24-48 heures : second regard. Ensuite reprises tant que la nécrose continue.",
"Exemple : admis à 22 h, bloc à 8 h le lendemain, c’est déjà une nuit. La revue de 2020 lie ce délai à la survie. [S3]",
"Le piège est un antibiotique en chambre avec un scanner « demain matin ».",
"Source [S1] [S3].") + """
<p>Les schémas suggérés par le tableau 16 du résumé EAU 2024, pour une flore mixte, sont les suivants. Pipéracilline-tazobactam 4,5 g toutes les 6 à 8 heures en intraveineux, plus vancomycine 15 mg/kg toutes les 12 heures. Ou imipénem-cilastatine 1 g toutes les 6 à 8 heures. Ou méropénem 1 g toutes les 8 heures. Ou ertapénem 1 g une fois par jour. Ou gentamicine 5 mg/kg par jour. Ou céfotaxime 2 g toutes les 6 heures plus métronidazole 500 mg toutes les 6 heures, ou bien clindamycine 600 à 900 mg toutes les 8 heures. Ou céfotaxime 2 g toutes les 6 heures plus fosfomycine 5 g toutes les 8 heures plus métronidazole 500 mg toutes les 6 heures. Ce sont des suggestions du résumé, adaptées ensuite à la culture. [S1]</p>
<p>La revue romande de 2020, pour la fasciite en général, propose pipéracilline-tazobactam ou un carbapénème ou ceftriaxone plus métronidazole, avec clindamycine 900 mg trois fois par jour en intraveineux. Elle dit que l’amoxicilline-acide clavulanique plus clindamycine peut se discuter pour une infection communautaire. Elle rappelle qu’en Suisse le staphylocoque résistant à la méticilline n’entre pas d’office dans le choix, hors facteurs de risque. L’EAU, elle, met la vancomycine dans une ligne du tableau de Fournier. On montre les deux textes. On n’efface pas la vancomycine de l’EAU ni la réserve suisse sur le SARM de la revue. [S1] [S3]</p>
<p>Aucune de ces lignes n’est une information professionnelle Swissmedic relue le 9 novembre 2026. Le corpus AIPS local était absent. Il n’y a donc ni nom commercial, ni numéro d’autorisation, ni adaptation au débit de filtration. Avant de prescrire, il faut ouvrir la monographie suisse du jour. Cette monographie d’examen ne la remplace pas. [S1]</p>
<p>Au bloc, on excise jusqu’au tissu qui saigne et qui résiste. On reprend. La fermeture viendra plus tard, greffe ou lambeau. La revue de 2014 dit l’usage courant d’un système d’aspiration pour la granulation. Ce n’est pas le premier geste. [S2]</p>
<p>Forme compliquée : choc, machine, amines. La revue cite des mortalités très hautes dans des sous-groupes ventilés ou sous amines, dans une littérature d’infection nécrosante, sans que je ne transpose un pourcentage non relu dans le passage Fournier. On réanime en parallèle du bloc, on ne choisit pas l’un contre l’autre. [S2]</p>
<p>Adjuvants. Immunoglobulines : la revue de 2014 cite 2 g/kg en une fois, ou 1 g/kg puis 0,5 g/kg deux jours, et un petit essai non concluant. Elle ne recommande pas cela comme standard. L’EAU 2024 dit de ne pas utiliser les adjuvants hors essai. L’hyperbare ne doit pas retarder l’incision. On suit l’EAU pour le Fournier urologique : pas d’adjuvant hors essai. [S1] [S2]</p>
<p>Situations particulières. Le diabétique et le dénutri sont le terrain le plus cité, pas une contre-indication au bloc. L’obèse se fait examiner dans les plis. La femme peut être atteinte : le résumé parle des organes génitaux externes, pas seulement de l’homme. La grossesse n’est pas détaillée. L’enfant n’a pas de dose pédiatrique dans les pages lues : on n’en invente pas. L’insuffisance rénale impose de relire l’AIPS avant gentamicine, vancomycine ou carbapénème. Ce texte ne donne pas le palier. [S1]</p>
<p><em>11.C Surveillance</em></p>
<p>On surveille la plaie à chaque reprise, la tension, la diurèse, et la créatine phosphokinase si le muscle était pris. On arrête la clindamycine « antitoxine » après trois à cinq jours dans la logique de la revue de 2014, puis on adapte le reste à la culture et à l’évolution. Il n’y a pas de seuil d’arrêt chiffré pour la vancomycine dans les pages lues. [S1] [S2]</p>
<p><em>11.D Pronostic</em></p>
<p>La mortalité reste élevée. Le facteur modifiable lu est le délai avant l’excision. La guérison locale est l’absence de nouvelle nécrose, puis la couverture. Il n’y a pas, dans les textes ouverts, un score de sortie unique. [S1] [S2] [S3]</p>
<p>Sortie, plus tard, un par un : plus de débridement nécessaire, alimentation possible, plaie couverte ou plan de couverture daté, diabète repris en main, consignes si la fièvre ou la douleur reviennent, rendez-vous de plastie s’il le faut. [S2]</p>
"""))
    P.append(ilot(DX, 12, "Prévention", """
<p>Primaire : équilibre du diabète et nutrition, terrains cités, sans seuil d’HbA1c dans ces pages. Pas de vaccin spécifique. [S1]</p>
<p>Secondaire : toute douleur périnéale disproportionnée est une fasciite jusqu’à preuve du contraire, surtout après un geste urétral et chez l’obèse. Le délai est la prévention de la mort. [S1] [S3]</p>
<p>Tertiaire : reprises jusqu’à tissu sain, puis couverture, pour éviter la nécrose résiduelle. Les adjuvants ne sont pas la prévention. [S1] [S2]</p>
"""))
    P.append(ilot(DX, 13, "Points clés", """
<p>Fournier est une fasciite nécrosante des organes génitaux : la nécrose dépasse la peau, et l’antibiotique seul ne suffit pas.</p>
<p>La fièvre et les crépitations manquent souvent au début. La douleur, elle, est trop forte.</p>
<p>On incise dans les heures, on reprend à 24-48 heures, on dérive l’urine par une sonde sus-pubienne.</p>
<p>Les doses du tableau EAU 2024 et de la revue romande sont des suggestions lues, pas des monographies Swissmedic.</p>
<p>Jusqu’à 40 % des débuts sont insidieux : on examine les plis de l’obèse.</p>
<p>L’hyperbare et les immunoglobulines ne retardent pas le bloc. L’EAU 2024 les réserve aux essais.</p>
"""))
    P.append(ilot(DX, 14, "Pièges et questions fréquentes à l'examen fédéral suisse", """
<p>Question : 40 % est-il la mortalité ? Réponse : non. C’est la part de débuts insidieux dans le résumé EAU. [S1]</p>
<p>Question : faut-il du gaz au scanner pour opérer ? Réponse : non. Les crépitations sont rares à l’admission, et la clinique suffit. [S2]</p>
<p>Question : 600 mg toutes les six heures ou 900 mg toutes les huit heures, quelle molécule, quelle source ? Réponse : clindamycine intraveineuse, revue romande 2014, trois à cinq jours, y compris si le germe est résistant in vitro, pour la toxine. Ce n’est pas une ligne Swissmedic. [S2]</p>
<p>Question : 4,5 g toutes les 6 à 8 heures, c’est quoi ? Réponse : pipéracilline-tazobactam intraveineuse dans le tableau EAU 2024, souvent avec vancomycine 15 mg/kg toutes les 12 heures. [S1]</p>
<p>Question : la revue suisse met-elle la vancomycine d’emblée ? Réponse : la revue 2020 dit que le SARM n’est pas le choix de routine en Suisse hors risque. L’EAU met pourtant la vancomycine dans une ligne de Fournier. On cite les deux. [S1] [S3]</p>
<p>Question : amoxicilline-acide clavulanique seule pour un Fournier septique ? Réponse : non. La revue 2020 la discute avec la clindamycine, et pour des infections communautaires, pas comme le schéma du sepsis du tableau EAU. [S3] [S1]</p>
<p>Question : quand revoir la plaie ? Réponse : second regard à 24-48 heures, puis tant qu’il y a de la nécrose. La revue 2014 parle aussi de reprises espacées d’environ 48 heures jusqu’à stabilité. [S2] [S3]</p>
<p>Question : les immunoglobulines à 2 g/kg sont-elles le standard ? Réponse : non. La revue 2014 les cite comme discutées, avec un essai petit et non concluant. Le résumé européen de 2024 ne les retient pas en dehors d’un essai. [S1] [S2]</p>
<p>Question : type I ou type II changent-ils la mortalité ? Réponse : non selon la revue 2014. La prise en charge non plus. [S2]</p>
<p>Question : où est le numéro Swissmedic de la pipéracilline-tazobactam ? Réponse : non lu. Les pages ouvertes ce jour-là sur swissmedicinfo concernaient d’autres molécules. On ne déduit pas un numéro. [S1]</p>
"""))
    P.append("""
<section class="ilot sources">
<h3>Sources</h3>
<p>[S1] European Urology, résumé des recommandations EAU sur les infections urologiques, 2024, section gangrène de Fournier et tableau 16, consulté le 9 novembre 2026. https://www.europeanurology.com/article/S0302-2838(24)02263-2/fulltext</p>
<p>[S2] Revue Médicale Suisse 2014;427, infections profondes des tissus mous, consultée le 9 novembre 2026. https://www.revmed.ch/revue-medicale-suisse/2014/revue-medicale-suisse-427/infections-profondes-des-tissus-mous</p>
<p>[S3] Revue Médicale Suisse 2020;690, infections de la peau et des tissus mous, consultée le 9 novembre 2026. https://www.revmed.ch/revue-medicale-suisse/2020/revue-medicale-suisse-690/rubor-calor-dolor-tumor-infections-de-la-peau-et-des-tissus-mous</p>
<p>La monographie de la gangrène de Fournier s’appuie sur ces trois textes et reste non validé cliniquement.</p>
<p>Les posologies chiffrées du point 11 sont celles des informations professionnelles AIPS du 8 octobre 2026, recopiées avec leur numéro Swissmedic. Le céfotaxime est absent de ce corpus. La fosfomycine intraveineuse du tableau européen n’a pas de spécialité correspondante. KIOVIG n’a pas la gangrène de Fournier dans ses indications.</p>
</section>
""")
    html = "\n".join(P)
    from dx10_aips import BLOC, neutraliser
    ancre = f'id="dx{DX}-i11"'
    h3fin = html.find("</h3>", html.find(ancre))
    if h3fin < 0:
        raise SystemExit("point 11 introuvable")
    html = html[: h3fin + 5] + BLOC + html[h3fin + 5 :]
    from dx10_extra import extra
    from dx10_extra2 import extra2
    from dx10_extra3 import extra3
    from dx10_extra4 import extra4
    from dx10_extra5 import extra5
    from dx10_extra6 import extra6
    from dx10_extra7 import extra7
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
    return neutraliser(html)

if __name__ == "__main__":
    from assembler import ecrire
    ecrire(10, "Gangrène de Fournier", body())

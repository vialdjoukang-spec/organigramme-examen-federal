from pathlib import Path
import json,html
B=Path(__file__).resolve().parent
PQ=json.loads((B/'paquet.json').read_text())
A=PQ['aliases']; IDS={x['id'] for x in PQ['passages']}
def C(*keys):
    z=[]
    for k in keys:
        i=A.get(k,k); assert i in IDS,i
        z.append(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>')
    return ''.join(z)
def P(t,*ks):return '<div class="p">'+html.escape(t)+C(*ks)+'</div>\n'
def H(t):return '<h4><em>'+html.escape(t)+'</em></h4>\n'
def W(i,t,body):
    i='dx10-'+i
    return f'<h4><button class="w" popovertarget="{i}">{html.escape(t)}</button></h4>\n<div id="{i}" popover class="fenetre"><h4>{html.escape(t)}</h4>\n'+body+'</div>\n'
def T(headers,rows):
    s='<div class="t" style="overflow-x:auto"><table><thead><tr>'+''.join('<th>'+html.escape(x)+'</th>' for x in headers)+'</tr></thead><tbody>\n'
    for row in rows:
        s+='<tr>'+''.join('<td>'+html.escape(x[0])+C(*x[1:])+'</td>' for x in row)+'</tr>\n'
    return s+'</tbody></table></div>\n'
def save(n,s):
    p=B/'fragments'/f'p{n:02d}.html';p.write_text(s);print(p.name,len(p.read_bytes()))

s=H('Une dilatation artérielle définie, puis une présentation clinique à qualifier')
s+=P('La Société européenne de chirurgie vasculaire définit l’anévrisme comme une dilatation focale permanente d’au moins 50 % du diamètre normalement attendu.','definition','bib')
s+=P('Dans ses recommandations de 2024, le seuil clinique utilisé pour définir un AAA est un diamètre aortique d’au moins 30 mm.','seuil','bib')
s+=P('Le support hospitalier bâlois retient également un diamètre d’au moins 3 cm, tout en distinguant la dilatation sous-anévrismale de 2.5–2.9 cm.','basel-def','basel-surveillance')
s+=P('Ainsi, le diamètre décrit la dilatation, tandis que la douleur, la sensibilité et les complications déterminent sa présentation symptomatique.','e203','e250')
s+=P('L’aorte descend du cœur à travers le thorax, puis irrigue les organes abdominaux avant de se diviser en artères iliaques vers les jambes.','chuv-anatomie')
s+=P('La recommandation européenne distingue les AAA fusiformes sous-rénaux des formes complexes et des problèmes infectieux, inflammatoires ou sacciformes.','e38')
s+=H('Symptomatique intact, rupture et rupture contenue')
s+=P('Un AAA symptomatique non rompu peut provoquer une douleur abdominale ou dorsale, être sensible à la palpation ou produire des embolies périphériques.','e203')
s+=P('Cependant, cette présentation ne comporte pas de brèche de la paroi aortique dans la définition européenne du groupe non rompu.','e203')
s+=P('La rupture correspond à une hémorragie qui franchit la paroi aortique et produit du sang rétropéritonéal ou intrapéritonéal.','e203')
s+=P('Une rupture contenue est temporairement colmatée par le rétropéritoine ; elle reste donc une rupture.','e203')
s+=P('Dès lors, une apparente stabilité clinique ne transforme pas une rupture contenue en simple anévrisme à surveiller.','e203','e205')
s+=P('Dans un petit anévrisme douloureux, l’équipe recherche rapidement les éléments qui permettent d’attribuer les symptômes à l’aorte.','e250')
s+=P('Cette attribution est importante, car une découverte aortique fortuite et une douleur liée à une autre cause peuvent coexister.','e37','e250')
s+=T(['Terme clinique','Ce que le terme établit','Décision qu’il ne faut pas confondre'],[
 [('AAA anatomique','seuil'),('Le diamètre atteint le seuil diagnostique de dilatation.','seuil'),('Le diamètre seul ne dit pas que la douleur est aortique.','e250')],
 [('AAA symptomatique non rompu','e203'),('Les symptômes sont compatibles et la paroi n’est pas rompue.','e203'),('Une évaluation rapide peut précéder la réparation urgente sous surveillance.','e251')],
 [('AAA rompu','e203'),('Le sang a franchi la paroi aortique.','e203'),('Une voie d’hémostase urgente remplace le parcours électif.','e205','e207')],
 [('Rupture contenue','e203'),('Le rétropéritoine colmate temporairement l’hématome.','e203'),('Le colmatage ne constitue pas une réparation définitive.','e203','e207')]
])
s+=W('p1-f1','Fusiforme, dilaté et disséqué ne désignent pas le même phénomène',P('Le terme anévrisme décrit un élargissement du vaisseau, souvent fusiforme dans la description européenne.','e0')+P('En revanche, une dissection commence par une déchirure qui permet au sang de séparer les couches de la paroi et de créer un faux chenal.','ph-dissection')+P('Ces processus peuvent être associés, mais la dilatation et la séparation des couches restent deux descriptions différentes.','ph-dissection')+P('La lecture de l’imagerie précise donc la lésion et son extension avant de choisir le traitement.','e18','e20'))
s+=W('p1-f2','Pourquoi une douleur dorsale peut signaler un problème abdominal',P('La douleur d’un AAA peut être située au niveau abdominal ou irradier vers le dos et les organes génitaux.','e7')+P('Par ailleurs, un anévrisme peut comprimer les structures voisines ou emboliser vers les territoires distaux.','e7')+P('La plainte dorsale doit ainsi rester reliée à l’examen abdominal, à la perfusion et au contexte vasculaire.','e7','e8','n1.1.7'))
save(1,s)

s=H('Données suisses : une population hospitalière définie')
s+=P('L’étude nationale de Meuli et collaborateurs analyse les données de sortie hospitalière de l’Office fédéral de la statistique pour 2009–2018.','smw-methodes')
s+=P('Elle inclut les AAA non rompus opérés et les AAA rompus hospitalisés et traités ; son recrutement est donc hospitalier.','smw-methodes')
s+=P('Les hommes représentent 87.1 % des cas inclus dans cette analyse.','smw-resultats')
s+=P('Par ailleurs, 22.7 % des cas présentent une rupture dans la population étudiée.','smw-resultats')
s+=P('Parmi les cas rompus, les auteurs rapportent 46 % de traitement chirurgical et 54 % de traitement conservateur.','smw-resultats')
s+=P('Ces proportions décrivent les cas inclus ; elles ne mesurent donc pas la fréquence d’un AAA chez une personne consultant pour lombalgie.','smw-methodes','smw-resultats')
s+=P('Les auteurs rapportent une stabilité des incidences hospitalières annuelles pendant la décennie observée.','smw-resultats','smw-conclusion')
s+=H('Distribution et mortalité : conserver les conditions de mesure')
s+=P('La mortalité hospitalière est ajustée sur l’âge, le sexe et un score de comorbidité dans cette analyse des données suisses.','smw-methodes')
s+=P('Pour le traitement des AAA non rompus, la mortalité ajustée passe de 5.5 % à 1.4 % chez les femmes entre 2009 et 2018.','smw-resultats')
s+=P('Chez les hommes, cette mortalité ajustée passe de 2.4 % à 0.6 % sur la même période.','smw-resultats')
s+=P('Pour les AAA rompus, les auteurs rapportent une mortalité ajustée de 32.4 % chez les femmes et de 19.7 % chez les hommes.','smw-resultats')
s+=P('Cependant, une mesure hospitalière sur des cas traités ne représente pas la totalité des décès survenant avant l’arrivée à l’hôpital.','smw-methodes')
s+=T(['Mesure rapportée','Population et période','Valeur et portée'],[
 [('Répartition masculine','smw-resultats'),('Cas hospitaliers suisses inclus, 2009–2018.','smw-methodes'),('87.1 % ; ce sont des cas de la série.','smw-resultats')],
 [('Présentation avec rupture','smw-resultats'),('Population hospitalière de cette étude.','smw-methodes'),('22.7 % ; il ne s’agit pas d’un risque individuel de rupture.','smw-resultats')],
 [('Traitement des cas rompus','smw-resultats'),('Sous-groupe présentant une rupture.','smw-resultats'),('46 % chirurgical, 54 % conservateur.','smw-resultats')],
 [('Mortalité ajustée des cas rompus','smw-resultats'),('Traitements rapportés dans la série nationale.','smw-methodes'),('32.4 % chez les femmes, 19.7 % chez les hommes.','smw-resultats')]
])
s+=H('Histoire naturelle, âge et facteurs de risque')
s+=P('La prévalence est très faible avant 55–60 ans dans la synthèse européenne, puis elle augmente régulièrement avec l’âge.','age')
s+=P('Toutefois, la prédominance masculine de la maladie ne signifie pas une moindre gravité chez la femme, pour laquelle NICE signale un risque de rupture plus élevé.','smw-resultats','n1.1.8')
s+=P('Le tabac constitue le facteur de risque le plus fortement associé à l’AAA dans la synthèse européenne.','e4')
s+=P('L’athérosclérose, l’hypertension et l’histoire familiale participent aussi au profil de risque.','e5')
s+=P('Ainsi, l’interrogatoire vasculaire accompagne l’évaluation d’une douleur nouvelle plutôt que de se limiter à son caractère rachidien.','e5','n1.1.7')
s+=P('Les petits AAA augmentent de diamètre chez la majorité des patients, et leur agrandissement s’accompagne d’un risque de rupture croissant.','e6')
s+=P('La prévalence et l’incidence ont diminué au cours des dernières décennies dans les séries européennes, notamment avec la baisse du tabagisme.','e1','e27')
s+=P('Cependant, les taux issus du dépistage dépendent du sexe, de l’âge et de la population examinée.','basel-epi','e3')
s+=P('La présentation symptomatique constitue donc une situation différente du dépistage d’une dilatation silencieuse.','e203','n1.1.7')
s+=W('p2-f1','Incidence pédagogique et incidence nationale ne se remplacent pas',P('Le support de Bâle rapporte une incidence de 3 à 117 pour 100‘000 personnes-années pour les AAA asymptomatiques.','basel-epi')+P('Pour les ruptures, il rapporte une plage de 1 à 21 pour 100‘000 personnes-années.','basel-epi')+P('Ces plages pédagogiques sont rapprochées de la variabilité des populations ; elles ne deviennent pas une estimation nationale unique.','basel-epi')+P('L’étude suisse, quant à elle, décrit des incidences hospitalières selon ses critères de recrutement.','smw-methodes'))
s+=W('p2-f2','Pourquoi l’enjeu dépasse la seule taille de l’anévrisme',P('Les patients avec AAA présentent aussi un risque élevé d’événements cardiovasculaires futurs.','e45')+P('La réduction du risque cardiovasculaire accompagne donc la surveillance et la réparation de l’anévrisme.','e47')+P('Après réparation, le suivi cherche également les complications tardives et la progression d’autres lésions anévrismales.','e310','e311')+P('Ainsi, une hémostase réussie ne termine pas à elle seule le parcours de prévention vasculaire.','e47','e336'))
save(2,s)

s=H('Amorce : inflammation et remodelage de la paroi')
s+=P('La paroi aortique normale doit ses propriétés mécaniques à l’élastine, au collagène et aux cellules musculaires lisses.','ph-collagene','ph-cml')
s+=P('Les fibres d’élastine de la média interagissent avec ces cellules et les fibres de collagène pour maintenir la structure du vaisseau.','ph-collagene')
s+=P('Dans l’AAA humain, les observations associent infiltration inflammatoire, destruction de matrice et diminution des cellules musculaires lisses.','ph-patho')
s+=P('Des macrophages et des cellules musculaires produisent des protéases, dont les métalloprotéinases matricielles, qui participent à ce remodelage destructeur.','ph-patho')
s+=P('Ainsi, la maladie de la paroi ne se réduit pas à une simple augmentation géométrique du diamètre.','ph-patho','ph-collagene')
s+=H('Développement : perte de matrice et de capacité de réparation')
s+=P('Les métalloprotéinases favorisent la dégradation du collagène et de l’élastine dans les tissus anévrismaux.','ph-collagene')
s+=P('La perte d’élastine est associée à la dilatation, tandis que la perte de collagène est reliée à la rupture dans la revue mécanistique.','ph-collagene')
s+=P('Les cellules musculaires lisses participent normalement à la production de matrice et à la régulation du tonus vasculaire.','ph-cml')
s+=P('Lors du changement de phénotype cellulaire, la diminution des protéines contractiles accompagne une production accrue de protéases.','ph-cml')
s+=P('Par ailleurs, l’apoptose diminue le nombre de cellules musculaires dans la média des AAA humains.','ph-cml')
s+=P('Cette perte cellulaire s’ajoute donc à la destruction des composants qui assurent la résistance de la paroi.','ph-cml','ph-collagene')
s+=H('Installation et maintien : un tissu inflammatoire remanié')
s+=P('Les neutrophiles, lymphocytes, macrophages et autres cellules inflammatoires peuvent infiltrer la paroi anévrismale.','ph-inflammation')
s+=P('Les cytokines et chimiokines modulent ensuite les cellules vasculaires et la production de protéines qui dégradent la matrice.','ph-inflammation')
s+=P('Une néovascularisation est également observée dans les tissus humains, au voisinage de zones riches en macrophages et en élastine dégradée.','ph-neo')
s+=P('Ainsi, inflammation, perte de matrice et modifications cellulaires se retrouvent dans une même paroi en remodelage.','ph-patho','ph-neo')
s+=P('Les lésions athéroscléreuses sont fréquemment associées, mais leur coexistence ne décrit pas à elle seule toute la pathogenèse de l’AAA.','ph-arteriosclerose')
s+=P('Les facteurs de risque communs, notamment le tabac et l’hypertension, doivent donc être intégrés au raisonnement vasculaire.','ph-arteriosclerose','e5')
s+=T(['Perturbation','Exploration qui l’évalue','Conséquence thérapeutique et mécanisme'],[
 [('La paroi perd des éléments de matrice et se dilate.','ph-patho','ph-collagene'),('L’échographie mesure le diamètre et suit son évolution.','e10','n1.2.3'),('La réparation écarte la paroi fragilisée du circuit sous pression ou remplace le segment.','e149','e218')],
 [('Le sang franchit la paroi lors d’une rupture.','e203'),('L’angioscanner recherche l’hémorragie et précise l’anatomie si le patient peut le supporter.','e205','e206'),('L’équipe obtient une hémostase urgente ; l’instabilité extrême peut conduire directement au bloc.','e207')],
 [('Des débris thrombotiques peuvent emboliser vers les jambes.','chuv-symptomes'),('L’examen compare température, sensibilité et pouls périphériques.','oxford-membres'),('Une ischémie aiguë impose une évaluation vasculaire rapide et parfois une revascularisation.','e249','chuv-occlusion')],
 [('Une endofuite réexpose le sac à un flux après EVAR.','endofuite-def'),('L’imagerie classe la fuite et mesure le sac.','n1.7.3','n1.7.4'),('La correction dépend du type et de l’évolution du sac.','n1.8.1','n1.8.2')]
])
s+=W('p3-f1','Le remplacement ouvert et l’exclusion endovasculaire agissent différemment',P('Lors d’une réparation ouverte, le segment malade est remplacé par une prothèse vasculaire.','e218','chuv-ouverte')+P('En revanche, l’EVAR laisse la paroi anévrismale en place et exclut le sac de la circulation systémique par l’intérieur.','e149')+P('Les zones d’ancrage doivent donc assurer à la fois la fixation et l’étanchéité de l’endoprothèse.','e149')+P('Une étanchéité initialement satisfaisante doit ensuite rester durable, ce qui explique la surveillance après EVAR.','e149','e323','e336'))
s+=W('p3-f2','Rupture contenue et choc : deux aspects d’une même menace',P('Le rétropéritoine peut temporairement contenir le sang qui s’échappe d’une rupture.','e203')+P('Cependant, l’hémorragie peut s’accompagner d’un collapsus et d’une altération de la conscience.','e8','e206')+P('La réanimation restrictive vise alors à éviter une aggravation du saignement avant le contrôle proximal de l’aorte.','e210')+P('L’analgésie et la surveillance hémodynamique accompagnent cette stratégie, sans remplacer le contrôle de la fuite.','e212','e207'))
s+=W('p3-f3','Une cible biologique ne devient pas automatiquement un médicament clinique',P('La revue mécanistique décrit des cellules, des enzymes et des voies de remodelage dans les AAA humains.','ph-patho','ph-cml')+P('Toutefois, la prise en charge médicale courante vise surtout le risque cardiovasculaire plutôt qu’un ralentissement démontré de la croissance par un traitement spécifique.','e49','e50')+P('L’indication de réparation reste donc fondée sur les symptômes, l’anatomie et le rapport bénéfice-risque.','e251','n1.5.2'))
save(3,s)

s=H('🚩 Une douleur nouvelle avec menace circulatoire ouvre la démarche')
s+=P('Une douleur abdominale ou dorsale nouvelle, un collapsus ou une perte de connaissance font rechercher une rupture d’AAA.','n1.1.7')
s+=P('La suspicion augmente notamment en présence d’un AAA connu, d’un tabagisme ou d’une hypertension.','n1.1.7')
s+=P('Cependant, la triade associant douleur, hypotension et masse pulsatile n’est présente que chez environ 50 % des patients avec rupture.','e204')
s+=P('Son absence ne permet donc pas de fermer la branche aortique devant un tableau compatible.','e204','n1.1.9')
s+=P('L’équipe recherche rapidement l’aorte par échographie au lit et contacte immédiatement le service vasculaire selon le résultat et la suspicion persistante.','n1.1.9')
s+=P('Si le patient peut supporter l’examen, alors l’angioscanner précise la rupture et les possibilités de réparation.','e205','e206')
s+=P('En revanche, une instabilité majeure peut conduire directement au bloc pour contrôle hémorragique et imagerie peropératoire adaptée.','e207')
s+=H('Un AAA présent doit ensuite être relié à la douleur')
s+=P('La douleur ou la sensibilité d’un AAA intact peut justifier une réparation urgente après une évaluation rapide surveillée.','e250','e251')
s+=P('Toutefois, un petit diamètre n’établit pas à lui seul que l’anévrisme explique les symptômes.','e250')
s+=P('Des investigations urgentes sont donc nécessaires pour préciser une présentation symptomatique lorsque l’attribution est incertaine.','e250')
s+=P('La colique urétérale fait partie des erreurs diagnostiques décrites lors d’une rupture d’AAA.','e204')
s+=P('La conclusion de lombalgie commune, quant à elle, repose sur une anamnèse et un examen ayant écarté une cause spécifique.','commune')
s+=T(['Hypothèse','Élément qui tranche','Piège d’interprétation','Conduite'],[
 [('🚩 La rupture ou la rupture contenue doit être exclue en tête.','e203'),('L’angioscanner recherche le sang extravasculaire si l’état clinique le permet.','e205','e206'),('Une triade incomplète ou une échographie ne montrant pas de fuite ne suffit pas à exclure la rupture.','e204','e205'),('L’avis vasculaire et la voie d’hémostase sont immédiats ; le bloc peut précéder le scanner si nécessaire.','n1.1.9','e207')],
 [('🚩 Une compression de la queue de cheval peut aussi provoquer une douleur lombaire grave.','cessignes','cesurgence'),('La rétention, la continence anale et la sensibilité en selle orientent l’examen neurologique et l’imagerie.','cessignes','cesexamen'),('Une douleur décrite comme lombaire ne dispense pas de rechercher les symptômes sacrés.','cessignes','cesurgence'),('L’imagerie du rachis et l’avis neurochirurgical sont obtenus sans attendre si les signaux d’alarme sont présents.','cesurgence')],
 [('Un calcul urétéral peut expliquer une douleur du flanc.','calcul'),('L’échographie puis le CT sans contraste confirment la lithiase selon le parcours EAU.','calculimage'),('Le tableau colique ne protège pas d’une confusion avec une rupture d’AAA.','e204'),('La branche urologique recherche en particulier obstacle infecté, sepsis ou anurie.','decompression')],
 [('Une lombalgie commune reste un diagnostic clinique après triage.','commune'),('L’anamnèse et l’examen écartent les signes d’une origine spécifique.','commune'),('La présence d’une alarme impose de rouvrir l’évaluation spécifique.','cesurgence','n1.1.7'),('Le maintien d’une mobilité adaptée appartient au traitement de la forme commune confirmée.','communemob')]
])
s+=W('p4-f1','L’échographie positive répond à une question ; le scanner répond à d’autres',P('L’échographie au lit identifie rapidement la présence d’un AAA.','n1.1.9')+P('Cependant, elle détecte mal l’hémorragie rétropéritonéale et ne permet pas d’exclure une fuite.','e205')+P('L’angioscanner précise l’hémorragie, l’aorte et les artères iliaques pour préparer la réparation.','e205')+P('Ainsi, un anévrisme visible chez un patient instable fait fortement suspecter une rupture, même si l’échographie ne montre pas le saignement.','e205'))
s+=W('p4-f2','La branche neurologique reste indépendante de la branche vasculaire',P('L’examen recherche une anomalie de sensibilité péri-anale ou glutéale et du tonus anal si une queue de cheval est suspectée.','cesexamen')+P('Ces signes renvoient à une atteinte des racines sacrées, alors que le collapsus d’une rupture traduit la menace circulatoire.','cesexamen','e8','e210')+P('La décision dépend donc des signes présents et non du seul mot lombalgie.','cesurgence','n1.1.7'))
s+=W('p4-f3','Deux lésions aortiques peuvent demander des stratégies différentes',P('La dissection crée une séparation des couches pariétales et un faux chenal.','ph-dissection')+P('Un AAA décrit d’abord une dilatation focale de l’artère.','definition')+P('Une association est possible ; l’imagerie doit donc décrire la lésion au lieu de traiter tous les tableaux comme une dilatation fusiforme standard.','ph-dissection','e38','e20'))
save(4,s)

s=H('Questions initiales : le temps, le siège et la gravité')
s+=P('Le clinicien recherche une douleur abdominale ou dorsale nouvelle, car elle fait partie des présentations qui doivent évoquer une rupture.','n1.1.7')
s+=P('Il recherche aussi un malaise, une perte de connaissance ou un collapsus, qui changent immédiatement la priorité.','n1.1.7','e8')
s+=P('La douleur peut irradier vers le dos ou les organes génitaux ; son siège apparent ne suffit donc pas à identifier son origine.','e7')
s+=P('Une sensibilité abdominale et des symptômes emboliques sont également compatibles avec un anévrisme symptomatique intact.','e203','e250')
s+=P('Lorsqu’un AAA est déjà connu, l’équipe recueille les examens antérieurs afin de préciser son évolution et son anatomie.','n1.1.7','e20','chuv-suivi-actuel')
s+=P('Elle recherche une réparation ouverte ou endovasculaire antérieure, car des complications tardives peuvent nécessiter une nouvelle évaluation.','e310','e323')
s+=H('Terrain : reconnaître le risque sans exclure les autres patients')
s+=P('L’histoire tabagique est importante, car le tabac est le principal facteur de risque identifié dans la synthèse européenne.','e4')
s+=P('Les antécédents familiaux, l’hypertension et les maladies athéroscléreuses complètent cette évaluation.','e5')
s+=P('Un âge supérieur à 60 ans augmente la probabilité d’une rupture devant des symptômes compatibles dans le cadre de NICE.','n1.1.7')
s+=P('Cependant, la décision de réparer une rupture ne repose pas sur un seul facteur lié au patient.','n1.4.4')
s+=P('La fonction antérieure, les comorbidités et l’espérance de vie participent au choix partagé de traitement.','n1.5.2')
s+=P('Le clinicien recherche notamment une maladie cardiaque, pulmonaire ou rénale, car l’évaluation opératoire dépend du contexte individuel.','e90','e109','n1.5.2')
s+=H('Médicaments et traitements antérieurs : transmettre les informations utiles')
s+=P('La liste des traitements accompagne le patient, car les antiagrégants et les situations de double antiagrégation modifient l’évaluation périopératoire.','e118','e119')
s+=P('Le risque de saignement et le risque cardiovasculaire sont ensuite appréciés ensemble par l’équipe de réparation.','e118','e119','n1.5.2')
s+=P('Le clinicien recherche aussi un antécédent de réaction au contraste et identifie le produit en cause lorsque cette information existe.','esur-allergie')
s+=P('Une insuffisance rénale impose une adaptation du bilan d’imagerie et de la préparation, sans faire perdre de vue l’urgence présente.','e110','e111','e207')
s+=T(['Question ou signal','Raison clinique','Action qui en découle'],[
 [('La douleur est-elle nouvelle et associée à un malaise ou une perte de connaissance ?','n1.1.7'),('Une rupture peut provoquer douleur et défaillance circulatoire.','e8','e203'),('L’évaluation aortique et l’appel vasculaire deviennent immédiats.','n1.1.9')],
 [('Un AAA est-il connu et des examens précédents sont-ils disponibles ?','n1.1.7','chuv-suivi-actuel'),('La connaissance de l’anatomie et des traitements aide à préparer la réparation.','e20','e81'),('Les images et informations sont transmises à l’équipe vasculaire.','chuv-suivi-actuel')],
 [('Une jambe est-elle soudainement douloureuse ou froide ?','chuv-occlusion'),('Des débris peuvent obstruer les artères distales.','chuv-symptomes'),('Une évaluation vasculaire urgente recherche une ischémie.','chuv-occlusion','e249')],
 [('Une réparation antérieure a-t-elle été effectuée ?','e310','e323'),('L’endoprothèse et les anastomoses peuvent présenter des complications tardives.','e310','endofuite-def'),('Le bilan recherche une complication adaptée au type de réparation.','e313','n1.7.4')],
 [('Une rétention ou une modification de la continence ou de la sensibilité en selle est-elle présente ?','cessignes'),('La compression des racines sacrées est une autre urgence possible.','cesexamen'),('Le parcours neurologique obtient imagerie et avis sans attendre.','cesurgence')],
 [('Une réaction préalable au contraste est-elle connue ?','esur-allergie'),('Une réexposition exige une évaluation du risque et du rendement diagnostique.','esur-allergie'),('La radiologie prépare une stratégie sûre et une alternative lorsque celle-ci suffit.','esur-allergie')]
])
s+=W('p5-f1','Une information sur la fragilité sert à décider, pas à appliquer une exclusion automatique',P('La décision partagée prend en compte l’autonomie, la santé actuelle et future, ainsi que les contraintes de récupération et de suivi.','n1.5.2')+P('Cependant, un score pronostique ne doit pas décider à lui seul de l’acceptation d’une réparation de rupture.','n1.4.5')+P('L’appréciation reste donc clinique et multidisciplinaire, avec discussion des bénéfices et des limites du traitement.','n1.5.2','n1.4.4'))
s+=W('p5-f2','La douleur après EVAR n’est pas simplement une récidive de lombalgie',P('Une endofuite correspond à un flux qui persiste dans le sac anévrismal après exclusion endovasculaire.','endofuite-def')+P('Les endofuites directes exposent à nouveau la paroi à une pression et un flux pulsatiles.','endofuite-def','endofuite-1','endofuite-3')+P('Ainsi, une plainte nouvelle chez un patient réparé justifie de préciser le dispositif, le dernier contrôle et le type de complication possible.','e323','e327','n1.7.4'))
save(5,s)

s=H('Référence normale : pulsation, expansion et perfusion sont distinguées')
s+=P('Une aorte non anévrismale peut être palpable chez une personne mince.','oxford-aorte')
s+=P('La pulsation normale n’est pas une expansion latérale de la masse ; sa seule présence ne définit donc pas un AAA.','oxford-normal','oxford-aorte')
s+=P('C’est la largeur et le caractère expansif qui motivent la suspicion clinique, plutôt que l’intensité de la pulsation isolée.','oxford-aorte')
s+=P('Cependant, l’absence de masse palpable ne permet pas d’exclure un AAA chez un patient dont la morphologie gêne la palpation.','oxford-aorte','e9')
s+=P('La recherche clinique complète doit ainsi rester proportionnée à l’état circulatoire et ne pas retarder la voie d’hémostase.','e206','e207')
s+=H('Préparation et inspection de l’abdomen')
s+=P('Le patient est installé à plat pour la palpation, avec la tête et les bras relâchés afin de diminuer la tension de la paroi abdominale.','oxford-preparation')
s+=P('Le clinicien demande où la douleur est maximale et observe le visage pendant les gestes pour repérer l’inconfort.','oxford-preparation')
s+=P('Lorsque la palpation est appropriée, il commence loin de la zone la plus douloureuse et progresse doucement.','oxford-preparation')
s+=P('L’inspection recherche ensuite une distension, une pâleur et les éléments de défaillance circulatoire décrits lors d’une rupture.','e8')
s+=P('Les cicatrices de laparotomie et les abords inguinaux apportent aussi des indices sur une réparation vasculaire antérieure.','oxford-normal','oxford-membres')
s+=H('Palpation aortique : préciser le geste et sa limite')
s+=P('Les deux mains sont placées au-dessus de l’ombilic sur un abdomen relâché pour rechercher les limites de la pulsation aortique.','oxford-aorte')
s+=P('Les doigts se dirigent vers l’épigastre et les bords des mains suivent les rebords costaux selon la technique enseignée.','oxford-aorte')
s+=P('Le clinicien peut rechercher un bord à la fois, puis apprécier la largeur entre les index.','oxford-aorte')
s+=P('Une expansion latérale, associée à la pulsation, rend la masse suspecte et conduit à l’imagerie.','oxford-aorte','n1.1.6')
s+=P('L’expérience de l’examinateur, le diamètre aortique et la morphologie du patient influencent la détection par palpation.','e9')
s+=P('Ainsi, la palpation oriente l’exploration ; elle ne remplace pas la mesure échographique ni la recherche de rupture.','e9','e10','e205')
s+=H('Examen circulatoire et territoires distaux')
s+=P('Le bilan décrit la conscience et la pression systolique, car leur altération participe à l’évaluation de l’instabilité.','e206')
s+=P('Le pouls radial, la température, la sensibilité et la recoloration capillaire complètent l’évaluation artérielle clinique.','oxford-arteriel')
s+=P('Le clinicien compare ensuite la couleur, la température et la sensibilité des membres inférieurs.','oxford-membres')
s+=P('Le pouls fémoral se recherche au point situé à mi-distance entre l’épine iliaque antérosupérieure et la symphyse pubienne.','oxford-membres')
s+=P('Le pouls pédieux se recherche latéralement au tendon du long extenseur du gros orteil.','oxford-membres')
s+=P('Le pouls tibial postérieur se recherche en arrière et sous la malléole médiale.','oxford-membres')
s+=P('Une douleur distale soudaine et un membre froid font rechercher rapidement une complication artérielle occlusive.','chuv-occlusion','e249')
s+=P('Toutefois, un pouls pédieux isolément non perçu doit être interprété avec les autres données, car ce pouls peut manquer chez un sujet normal.','oxford-membres')
s+=H('Auscultation et examen orienté par les autres alarmes')
s+=P('Le clinicien peut écouter un souffle aortique au-dessus de l’ombilic et décrire les souffles rénaux ou fémoraux associés.','oxford-aorte','oxford-normal','oxford-membres')
s+=P('Ces observations sont rapprochées de l’imagerie et du tableau clinique, qui restent déterminants pour la conduite.','e10','e205')
s+=P('Si des symptômes sacrés font suspecter une queue de cheval, alors l’examen porte aussi sur la sensibilité péri-anale et glutéale et le tonus anal.','cesexamen')
s+=P('L’imagerie neurologique urgente et l’avis spécialisé accompagnent cette branche si les signaux d’alarme sont confirmés.','cesurgence')
s+=W('p6-f1','Le normal évite une fausse attribution à l’aorte',P('Chez une personne mince, une pulsation aortique perceptible peut être physiologique.','oxford-aorte')+P('En revanche, une expansion latérale et une largeur anormale motivent la suspicion d’anévrisme.','oxford-aorte')+P('La mesure d’imagerie est donc nécessaire pour confirmer la dilatation et décrire son diamètre.','e10','seuil')+P('Une échographie non concluante en contexte symptomatique appelle toujours une discussion immédiate si l’AAA reste suspecté.','n1.1.9'))
s+=W('p6-f2','La technique de mesure influence l’interprétation clinique',P('La mesure échographique doit être perpendiculaire à l’axe du vaisseau, et non simplement à l’axe du corps.','basel-planmesure')+P('Une coupe oblique peut surestimer le diamètre ; le plan et la méthode doivent donc être identifiés dans le compte rendu.','basel-planmesure','e17')+P('NICE demande le diamètre antéropostérieur maximal interne à interne, tandis que l’ESVS insiste sur une méthode constante et explicitée.','n1.1.10','e17')+P('La comparaison d’examens successifs doit ainsi conserver la même convention de mesure.','e17','e320'))
save(6,s)

s=H('7.1 Syndrome de dilatation aortique douloureuse sans rupture démontrée')
s+=P('Les signes fonctionnels associent une douleur abdominale ou dorsale, parfois une irradiation vers les organes génitaux.','e7','e203')
s+=P('La palpation peut retrouver une masse expansive sensible, mais la visibilité clinique dépend du diamètre et de la morphologie.','e9','e250','oxford-aorte')
s+=P('Le raisonnement associe donc symptômes, examen et imagerie pour qualifier un AAA symptomatique intact.','e203','e250')
s+=P('Une embolie périphérique sans autre source évidente peut également appartenir à cette présentation.','e250')
s+=H('7.2 Syndrome de rupture et de défaillance circulatoire')
s+=P('La douleur abdominale ou dorsale s’accompagne alors parfois d’un collapsus, d’une pâleur ou d’une distension abdominale.','e8')
s+=P('La conscience et la pression systolique sont évaluées, car elles participent à la description de l’instabilité.','e206')
s+=P('La présence de sang rétropéritonéal ou intrapéritonéal après franchissement de la paroi définit la rupture.','e203')
s+=P('Cependant, un colmatage rétropéritonéal transitoire peut modifier la présentation sans supprimer la menace.','e203','e205')
s+=H('7.3 Syndrome embolique ou compressif associé')
s+=P('Une occlusion artérielle des jambes peut résulter de débris de caillots libérés par l’anévrisme.','chuv-symptomes')
s+=P('La douleur soudaine et le refroidissement d’un membre imposent donc un examen vasculaire rapide.','chuv-occlusion','oxford-membres')
s+=P('Par ailleurs, un AAA peut comprimer des structures voisines comme les voies urinaires, l’intestin ou les veines.','e7','chuv-symptomes')
s+=P('L’exploration précise alors les rapports anatomiques et les conséquences qui influencent le traitement.','e20','e7')
s+=H('7.4 Syndrome de complication après réparation')
s+=P('Après EVAR, une endofuite expose le sac à un flux situé à l’extérieur de l’endoprothèse.','endofuite-def')
s+=P('Une aggravation après réparation de rupture fait aussi rechercher un syndrome compartimental abdominal.','n1.6.5','n1.6.6')
s+=P('L’ischémie colique ou l’ischémie d’un membre sont d’autres complications qui justifient une surveillance rapprochée.','e247','e249')
s+=T(['Syndrome','Signes fonctionnels','Signes physiques et exploration'],[
 [('Le tableau intact est douloureux sans brèche pariétale démontrée.','e203'),('La douleur siège à l’abdomen ou au dos et peut irradier.','e7'),('Une masse sensible peut orienter ; l’imagerie qualifie l’anévrisme.','e250','e205')],
 [('Le tableau rompu correspond à une hémorragie extravasculaire.','e203'),('La douleur nouvelle peut s’associer à un malaise ou une perte de connaissance.','n1.1.7'),('La pâleur, le collapsus et la distension renforcent la suspicion.','e8')],
 [('Le tableau embolique atteint un territoire artériel distal.','chuv-symptomes'),('Une jambe devient soudainement douloureuse.','chuv-occlusion'),('Le refroidissement et la comparaison des pouls orientent l’examen.','chuv-occlusion','oxford-membres')],
 [('La complication post-réparation dépend du mécanisme en cause.','endofuite-def','e239'),('Une dégradation clinique ou une douleur sévère appelle une réévaluation urgente.','n1.6.6','nhs-alerte'),('L’imagerie du sac et l’évaluation d’une dysfonction d’organe guident la suite.','n1.7.4','e239')]
])
s+=W('p7-f1','Masse pulsatile expansive : définition et recherche',P('Une pulsation correspond au mouvement perçu avec le cycle artériel ; elle peut être perceptible sur une aorte normale chez une personne mince.','oxford-aorte')+P('Le caractère expansif correspond au déplacement latéral des limites de la masse pendant la pulsation.','oxford-aorte','oxford-normal')+P('Les mains placées au-dessus de l’ombilic recherchent donc la largeur et l’expansion plutôt que la seule intensité du battement.','oxford-aorte')+P('Toutefois, l’absence de masse palpable ne permet pas d’exclure la dilatation lorsque l’examen est limité par la morphologie.','oxford-aorte','e9'))
s+=W('p7-f2','Instabilité : un signe de gravité à reconnaître directement',P('Une perte ou réduction de conscience, ou une pression systolique inférieure à 80 mmHg, caractérise une instabilité dans la définition européenne.','e206')+P('L’équipe observe la conscience et mesure la pression au cours de l’évaluation et de la réanimation.','e206','e211')+P('La stratégie d’hypotension permissive est une mesure transitoire de réanimation ; elle ne signifie donc pas que la circulation est redevenue normale.','e210','e211')+P('Si le patient est trop instable pour le scanner, alors une confirmation peropératoire et un contrôle urgent sont possibles.','e207'))
s+=W('p7-f3','Douleur et sensibilité : localiser puis confronter à l’aorte',P('La douleur est rapportée par le patient, tandis que la sensibilité est recherchée lors d’une palpation adaptée.','e7','oxford-preparation')+P('Le clinicien commence loin de la zone la plus douloureuse et demande au patient de signaler l’inconfort.','oxford-preparation')+P('Une douleur dorsale ou abdominale inexpliquée et une sensibilité aortique peuvent caractériser un AAA symptomatique.','e250')+P('L’imagerie et la recherche d’autres causes sont donc nécessaires pour établir cette attribution.','e250','e205'))
s+=W('p7-f4','Membre froid et douloureux : le mécanisme peut être embolique',P('Le patient décrit une douleur soudaine et le clinicien compare température, couleur, sensibilité et pouls des deux membres.','chuv-occlusion','oxford-membres')+P('L’anévrisme peut produire des embolies qui obstruent des artères distales.','chuv-symptomes')+P('Cette association impose alors une évaluation vasculaire urgente pour préserver le territoire menacé.','chuv-occlusion','e249'))
s+=W('p7-f5','Syndrome compartimental : pression et atteinte d’organe doivent être associées',P('La recommandation européenne définit l’hypertension intra-abdominale par une pression pathologique soutenue ou répétée supérieure à 12 mmHg.','e239')+P('Le syndrome compartimental associe une pression intra-abdominale supérieure à 20 mmHg à une dysfonction ou défaillance d’organe nouvelle.','e239')+P('Il peut survenir après réparation ouverte ou endovasculaire d’une rupture.','e240')+P('La détérioration postopératoire doit donc conduire à sa recherche et à une prise en charge spécialisée rapide.','n1.6.6','e242'))
save(7,s)

s=H('Deux questions positives : existe-t-il une dilatation et quelle est sa présentation ?')
s+=P('La définition anatomique repose sur une dilatation focale permanente, appréciée par rapport au diamètre attendu.','definition')
s+=P('En pratique, un diamètre d’au moins 30 mm définit l’AAA dans les recommandations ESVS de 2024.','seuil','bib')
s+=P('La mesure est documentée avec son plan et la position des curseurs, car ces conventions influencent le résultat.','e17','n1.1.10')
s+=P('Le diagnostic de présentation symptomatique exige ensuite une concordance avec douleur, sensibilité ou complication embolique.','e203','e250')
s+=P('Une dilatation fortuite ne suffit donc pas à expliquer toute douleur observée chez le même patient.','e37','e250')
s+=P('La rupture, quant à elle, correspond au franchissement de la paroi avec hémorragie extravasculaire.','e203')
s+=T(['Critère ou catégorie','Élément requis','Usage et limite'],[
 [('La définition relative de l’anévrisme est une dilatation d’au moins 50 %.','definition'),('Le diamètre est comparé à celui normalement attendu pour le segment.','definition'),('Cette définition ne mesure pas à elle seule la gravité de la présentation aiguë.','e203','e206')],
 [('Le seuil clinique de l’AAA est d’au moins 30 mm.','seuil'),('Une mesure d’imagerie précise le diamètre aortique.','e10','e17'),('Le plan et la convention de curseurs doivent être conservés.','e17')],
 [('Un AAA symptomatique intact comporte des symptômes compatibles.','e203'),('La douleur, la sensibilité ou une embolie sont reliées à l’anévrisme.','e203','e250'),('La paroi n’est pas rompue dans cette catégorie.','e203')],
 [('Une rupture implique une hémorragie hors de la paroi.','e203'),('Le sang peut être rétropéritonéal ou intrapéritonéal.','e203'),('Une rupture contenue reste une rupture.','e203')],
 [('Après EVAR, le succès technique doit rester durable.','e325','e336'),('Le sac est exclu et le flux dans les branches de l’endoprothèse est préservé.','e325'),('Une surveillance est requise pour reconnaître les complications tardives.','e323','e336')]
])
s+=H('Ne pas transformer un diamètre d’intervention en critère de symptômes')
s+=P('Le diamètre qui définit une dilatation et les critères de réparation d’un anévrisme asymptomatique répondent à des questions différentes.','seuil','n1.5.1')
s+=P('Un AAA non rompu symptomatique fait partie des situations pour lesquelles NICE propose d’envisager une réparation.','n1.5.1')
s+=P('L’ESVS demande des investigations urgentes pour confirmer l’attribution symptomatique lorsqu’un anévrisme douloureux est inférieur à 55 mm.','e250')
s+=P('Ainsi, un diamètre inférieur au seuil habituel de réparation élective ne suffit pas à autoriser une attente routinière devant une douleur suspecte.','e250','e251')
s+=H('L’anatomie complète détermine la faisabilité du traitement')
s+=P('L’équipe caractérise les zones d’étanchéité, les accès artériels et l’anatomie aorto-iliaque avant de sélectionner une endoprothèse.','e81','e83')
s+=P('Chaque dispositif possède ses propres instructions d’utilisation, qui encadrent les conditions anatomiques de son emploi.','e152')
s+=P('Par conséquent, la seule valeur du diamètre maximal ne suffit pas à décider de la possibilité d’un EVAR standard.','e81','e152')
s+=W('p8-f1','Les scores pronostiques ne remplacent pas l’indication clinique',P('NICE recommande de ne pas décider de la possibilité d’une réparation de rupture sur un score pronostique.','n1.4.5')+P('De même, un signe ou un facteur de risque isolé ne doit pas constituer à lui seul la décision.','n1.4.4')+P('L’équipe discute donc l’état actuel, le bénéfice attendu et les préférences du patient dans une évaluation individualisée.','n1.5.2'))
s+=W('p8-f2','Après EVAR : classer le mécanisme d’une endofuite',P('Une endofuite désigne un flux dans le sac à l’extérieur de l’endoprothèse.','endofuite-def')+P('Le type 1 correspond à une perte d’étanchéité proximale ou distale, avec flux direct dans le sac.','endofuite-1','endofuite-def')+P('Le type 2 provient de vaisseaux collatéraux.','type2')+P('Le type 3 correspond à une séparation de composants ou à une déchirure du matériau.','endofuite-3')+P('Les types 1 et 3 exposent directement la paroi à la pression artérielle et justifient une prise en charge correctrice.','endofuite-def','n1.8.1')+P('En revanche, la conduite devant un type 2 dépend notamment de l’expansion du sac.','n1.8.2'))
save(8,s)

s=H('9.a Référence : l’angioscanner pour la rupture et la planification')
s+=P('L’angioscanner est la modalité clé pour confirmer une rupture suspectée et planifier la réparation lorsque l’état du patient le permet.','e205','e206')
s+=P('Il fournit une analyse de l’aorte thoraco-abdominale et des axes iliaques utile à la décision ouverte ou endovasculaire.','e205','e20')
s+=P('La prescription préopératoire précise des coupes fines avec phase artérielle après contraste.','n1.1.11','n1.1.12')
s+=P('La reconstruction de planification nécessite des coupes d’au plus 1 mm selon le consensus européen.','e20','e87')
s+=P('Les reconstructions multiplanaires et centrées sur l’axe vasculaire précisent alors les diamètres, longueurs et zones d’ancrage.','e20','e81')
s+=P('Cependant, un patient trop instable peut être conduit directement au bloc pour contrôle urgent et confirmation peropératoire.','e207')
s+=H('9.b Première exploration rapide : une échographie qui répond à la bonne question')
s+=P('L’échographie aortique au lit est proposée immédiatement lorsqu’un AAA symptomatique ou rompu est envisagé.','n1.1.9')
s+=P('Pour la détection des petits AAA, l’échographie et le duplex présentent une sensibilité et une spécificité supérieures à 97 % dans la synthèse européenne.','e10')
s+=P('Toutefois, ces performances de détection de dilatation ne signifient pas que l’échographie exclut une hémorragie rétropéritonéale.','e10','e205')
s+=P('Si l’examen est indisponible ou non diagnostique et que l’AAA reste suspecté, alors la discussion vasculaire est immédiate.','n1.1.9')
s+=P('Le compte rendu précise le diamètre maximal, le plan de mesure et la convention de placement des curseurs.','e17','n1.1.10')
s+=P('Une mesure perpendiculaire à l’axe du vaisseau réduit le risque de surestimation sur une coupe oblique.','basel-planmesure')
s+=H('9.c Alternatives : adapter sans retarder une exploration indispensable')
s+=P('La fonction rénale est appréciée par la créatinine et le DFGe avant une préparation aortique lorsqu’une évaluation programmée est possible.','e110','e111')
s+=P('Le risque lié à une injection iodée intraveineuse mérite une attention particulière lorsque le DFGe est inférieur à 30 ml/min/1.73 m².','esur-rein')
s+=P('Dans ce contexte, l’équipe considère une méthode sans produit iodé et adapte la stratégie au besoin diagnostique.','esur-alternative','e320')
s+=P('Une hypersensibilité antérieure au contraste fait également discuter une autre modalité ou un examen non injecté si son rendement suffit.','esur-allergie')
s+=P('Cependant, une exploration injectée bien indiquée ne doit pas être refusée lorsqu’aucune alternative adéquate n’est disponible.','esur-allergie')
s+=T(['Situation particulière','Adaptation fondée sur les sources','Interprétation et garde-fou'],[
 [('Une insuffisance rénale sévère complique un bilan électif.','e111'),('Un avis néphrologique prépare l’optimisation avant réparation programmée.','e111'),('La menace circulatoire reste évaluée selon la branche aiguë.','e206','e207')],
 [('Le DFGe est inférieur à 30 ml/min/1.73 m² avant injection iodée intraveineuse.','esur-rein'),('Une alternative sans produit iodé est envisagée selon son rendement.','esur-alternative'),('L’échographie et le duplex ne comportent pas de contraste néphrotoxique.','e320')],
 [('Une réaction préalable au contraste est connue.','esur-allergie'),('La modalité et le produit sont discutés avec la radiologie.','esur-allergie'),('Le choix conserve un rendement suffisant pour la prise en charge urgente.','esur-allergie')],
 [('Une grossesse accompagne une indication d’exploration essentielle.','esur-grossesse'),('ESUR autorise exceptionnellement un produit iodé si l’examen radiologique est indispensable.','esur-grossesse'),('Après exposition maternelle, la fonction thyroïdienne néonatale est contrôlée durant la première semaine.','esur-grossesse')],
 [('Une IRM injectée est envisagée pendant la grossesse.','esur-grossesse'),('Une indication très forte est requise pour un agent macrocyclique au gadolinium.','esur-grossesse'),('La question du contraste est distinguée de celle de l’imagerie nécessaire à l’urgence.','esur-grossesse','e205')],
 [('Une mère allaite et une IRM avec agent macrocyclique est indiquée.','esur-allaitement'),('L’allaitement peut être poursuivi normalement selon ESUR, en dehors de la restriction rénale indiquée ici.','esur-allaitement'),('Chez une mère enceinte ou allaitante présentant une insuffisance rénale, ESUR interdit l’administration de produits gadolinés.','esur-allaitement')],
 [('L’IRM ne peut pas être réalisée.','e18','e205'),('L’angioscanner reste la modalité principale de planification et de rupture.','e18','e205'),('L’échographie renseigne la dilatation, sans exclure à elle seule une fuite.','e205')],
 [('Le patient est jeune et exposé à des contrôles répétés.','e318'),('Le choix tient compte de l’irradiation cumulative et des méthodes échographiques.','e318','e320'),('La modalité doit toujours conserver les informations nécessaires.','e317','e320')]
])
s+=H('9.d Informations préopératoires et interprétation du résultat')
s+=P('Le bilan minimal préopératoire comprend anamnèse, examen, évaluation fonctionnelle, numération sanguine, électrolytes, fonction rénale et ECG.','e90')
s+=P('Les investigations supplémentaires sont ensuite choisies selon les circonstances individuelles.','e90')
s+=P('L’imagerie décrit le collet proximal, les artères iliaques, les vaisseaux viscéraux et les éventuelles anomalies anatomiques.','e82','e83','e84','e86')
s+=P('Ces éléments déterminent la zone de clampage ou d’étanchéité, les accès et la stratégie de réparation.','e81','e82','e83')
s+=T(['Résultat','Signification','Conduite'],[
 [('Une dilatation aortique est visualisée.','e10'),('Le diamètre et l’anatomie doivent être précisés.','e17','e20'),('L’équipe les confronte aux symptômes et au risque de rupture.','e250','n1.5.2')],
 [('Du sang franchit la paroi vers le rétropéritoine ou le péritoine.','e203'),('Cette image correspond à une rupture.','e203'),('La voie de réparation urgente et d’hémostase est activée.','e205','e207')],
 [('L’échographie est non concluante en contexte suspect.','n1.1.9'),('Le diagnostic reste ouvert malgré cet examen.','n1.1.9','e205'),('L’avis vasculaire immédiat organise l’étape suivante.','n1.1.9')],
 [('Le collet ou les accès ne répondent pas aux conditions du dispositif.','e81','e152'),('Un EVAR standard peut ne pas être adapté.','e152'),('Une autre stratégie est choisie avec l’équipe spécialisée.','e81','n1.5.2')],
 [('Le sac augmente après EVAR.','suivi-echec'),('Une complication de l’exclusion doit être recherchée.','endofuite-def','suivi-echec'),('L’imagerie classe l’endofuite ou recherche une autre défaillance.','n1.7.4','suivi-echec')]
])
s+=W('p9-f1','Une convention de mesure peut déplacer un seuil apparent',P('Les mesures internes à internes sont généralement plus petites que les mesures externes à externes dans les comparaisons européennes.','e15')+P('La différence rapportée est d’environ 3–6 mm ; elle doit donc être connue lors d’une comparaison d’examens.','e15')+P('L’ESVS insiste sur une convention constante et explicitée au sein d’un programme de suivi.','e17')+P('Le diamètre CT et le diamètre échographique ne sont pas directement interchangeables pour suivre la dynamique du sac.','e320'))
s+=W('p9-f2','Après EVAR : recherche d’endofuite et mesure du sac sont deux objectifs complémentaires',P('L’angioscanner et le duplex constituent la base de l’imagerie de suivi.','e314')+P('Le duplex mesure le sac sans irradiation et sans contraste néphrotoxique.','e320')+P('Si une endofuite est suspectée, alors NICE recommande l’angioscanner injecté ou une échographie de contraste si celui-ci est contre-indiqué.','n1.7.4')+P('Une échographie couleur négative isolée ne suffit donc pas à exclure une endofuite.','n1.7.5')+P('L’angio-IRM peut aussi être utile lorsque le sac augmente et que le scanner ne résout pas la question.','e319'))
save(9,s)

s=H('Arbre initial : signes, examen et décision')
s+=P('Si une douleur abdominale ou dorsale nouvelle s’accompagne d’un malaise, d’un collapsus ou d’une perte de connaissance, alors une rupture d’AAA est recherchée immédiatement.','n1.1.7')
s+=P('Si la douleur évoque une rupture en dehors de l’hôpital, alors l’information suisse aux patients prévoit un appel immédiat au 144.','chuv144')
s+=P('Si l’AAA est visible en échographie, alors le service vasculaire est contacté immédiatement pour organiser la suite.','n1.1.9')
s+=P('Si l’échographie est non diagnostique ou indisponible et que la suspicion persiste, alors le même contact immédiat est nécessaire.','n1.1.9')
s+=P('Si le patient peut supporter l’acquisition, alors un angioscanner confirme la rupture et fournit l’anatomie de réparation.','e205','e206')
s+=P('Si le patient est trop instable pour cette étape, alors la voie opératoire avec confirmation peropératoire est une possibilité d’urgence.','e207')
s+=H('Arbre de qualification : rompu, intact symptomatique ou découverte fortuite')
s+=P('Si l’imagerie montre une hémorragie au-delà de la paroi, alors l’AAA est classé comme rompu.','e203')
s+=P('Si cette hémorragie est temporairement contenue par le rétropéritoine, alors elle reste dans le parcours de rupture.','e203')
s+=P('Si l’AAA est intact mais que douleur, sensibilité ou embolie lui sont attribuées, alors une réparation urgente est discutée après une évaluation rapide surveillée.','e250','e251')
s+=P('Si l’attribution est incertaine, alors l’équipe recherche rapidement les autres causes possibles au lieu de conclure sur le seul diamètre.','e250')
s+=P('Si une autre cause spécifique est retenue, alors son traitement est organisé selon ses propres signes de gravité.','cesurgence','decompression')
s+=P('Si une forme commune est finalement retenue après exclusion d’une cause spécifique, alors la prise en charge suit le cadre de lombalgie commune.','commune','communemob')
s+=H('Arbre de réparation : anatomie et état du patient')
s+=P('Si une réparation endovasculaire est envisagée, alors les zones d’étanchéité et les accès sont confrontés aux instructions du dispositif.','e81','e152')
s+=P('Si l’anatomie ne permet pas un EVAR standard, alors l’équipe spécialisée choisit une autre stratégie adaptée au patient.','e81','e152','n1.5.2')
s+=P('Si une rupture impose une réanimation avant le contrôle proximal, alors une stratégie restrictive peut limiter l’aggravation du saignement.','e210')
s+=P('Si l’AAA est symptomatique intact et surveillé avant réparation, alors pression et douleur font l’objet d’une prise en charge attentive.','e251')
s+=H('Arbre de suivi : reconnaître une défaillance après EVAR')
s+=P('Si une endofuite est suspectée, alors l’angioscanner injecté ou l’échographie de contraste selon les contre-indications complète le bilan.','n1.7.4')
s+=P('Si une endofuite directe ou une augmentation importante du sac est identifiée, alors une intervention secondaire est envisagée.','suivi-echec')
s+=P('Si l’imagerie précoce établit un faible risque, alors le programme de contrôle peut être allégé selon les critères anatomiques européens.','suivi-bas')
s+=P('Si les critères de haut risque sont présents, alors une surveillance plus rapprochée est organisée et réévaluée.','suivi-haut')
s+=P('Dans tous les cas, le patient conserve un suivi à long terme et sait quels symptômes doivent faire consulter sans attendre.','e336','nhs-alerte','chuv144')
s+=W('p10-f1','Un objectif transitoire ne devient pas un critère de retour à domicile',P('La stratégie restrictive de réanimation vise la période qui précède le contrôle du saignement.','e210')+P('Elle repose sur la tolérance clinique et une surveillance de la conscience et de la pression.','e211')+P('La sortie de l’hôpital relève ensuite d’une récupération fonctionnelle, alimentaire et clinique distincte.','nhs-sortie','nhs-surveillance')+P('Ainsi, un chiffre de pression utilisé pendant la réanimation ne suffit pas à déclarer le patient stabilisé ou apte à sortir.','e211','nhs-surveillance','nhs-sortie'))
save(10,s)

s=H('11.A But : contrôler la fuite, protéger la perfusion et organiser le traitement urgent')
s+=P('Le but de la réparation est d’exclure le sac de la circulation ou de remplacer le segment malade pour prévenir ou contrôler la rupture.','e149','e218')
s+=P('Dans une rupture, la priorité est donc le contrôle du saignement associé à une réanimation adaptée.','e207','e210')
s+=P('L’ESVS propose une pression systolique transitoire de 70–90 mmHg pendant l’hypotension permissive, à condition que le patient reste conscient.','e211')
s+=P('Cette recommandation repose sur un niveau de preuve faible et exige une appréciation clinique continue, notamment chez la personne âgée.','e211')
s+=P('NICE prévoit un départ de l’unité adresseuse dans les 30 minutes suivant la décision de transfert lorsque le service vasculaire a accepté le patient.','n1.3.4')
s+=P('Ce délai concerne donc l’organisation du transfert urgent, et non une permission d’attendre avant l’évaluation initiale.','n1.3.4','n1.1.9')
s+=W('p11-urgence','Urgence — conduite chronologique',H('Reconnaître et mobiliser l’équipe')+P('D’abord, une douleur compatible, un collapsus ou une perte de connaissance déclenche la recherche d’une rupture.','n1.1.7')+P('En situation extrahospitalière, le patient ou son entourage appelle le 144 selon l’information suisse sur les signes de rupture.','chuv144')+P('L’équipe hospitalière organise ensuite l’échographie rapide et le contact vasculaire immédiat, y compris lorsque l’échographie reste non diagnostique.','n1.1.9')+H('Confirmer et maintenir la perfusion sans aggraver le saignement')+P('Lorsque l’état le permet, l’angioscanner confirme la rupture et prépare le choix de réparation.','e205','e206')+P('Si le patient est trop instable, alors l’équipe peut le conduire directement au bloc avec imagerie peropératoire adaptée.','e207')+P('Avant le contrôle proximal, une réanimation trop vigoureuse peut augmenter le saignement ; une approche restrictive est donc privilégiée.','e210')+P('La réanimation utilise préférentiellement sang et produits sanguins selon les principes de transfusion massive et les protocoles locaux.','e210','e212')+P('La conscience, la pression et la douleur sont suivies pendant cette période afin d’adapter la conduite.','e211','e212')+H('Obtenir le contrôle aortique et réparer')+P('La réparation ouverte obtient le contrôle proximal par clampage et remplace le segment malade par une prothèse.','e215','e218')+P('La réparation endovasculaire exclut le sac de l’intérieur lorsque les conditions anatomiques et techniques sont réunies.','e149','e81','e152')+P('Enfin, une surveillance spécialisée recherche les conséquences de l’hémorragie, de l’ischémie et de la réparation.','e239','e247','e249'))
s+=H('11.B Moyens : distinguer rupture et AAA symptomatique non rompu')
s+=P('Pour une rupture, la recommandation européenne retient l’EVAR comme première option, avec une sélection anatomique adaptée.','e238','e81','e152')
s+=P('Cependant, une réparation ouverte reste une possibilité lorsque l’endovasculaire standard est inadapté.','n1.6.2','e218')
s+=P('Pour l’AAA intact symptomatique, l’ESVS autorise une brève phase d’évaluation rapide et d’optimisation suivie d’une réparation urgente dans les meilleures conditions.','e251')
s+=P('La pression et la douleur sont surveillées attentivement pendant cette phase, qui ne constitue pas une attente élective habituelle.','e251')
s+=P('L’anatomie, les comorbidités, la capacité de récupération et les préférences du patient participent ensuite à la décision.','n1.5.2')
s+=P('Un score seul ne peut donc pas remplacer la décision clinique sur la possibilité d’une réparation.','n1.4.5')
s+=H('Réparation et anesthésie : ce que chaque modalité implique')
s+=P('La chirurgie ouverte utilise une prothèse de configuration tubulaire ou bifurquée pour remplacer la portion pathologique.','e218')
s+=P('Elle nécessite une anesthésie générale dans la prise en charge décrite des ruptures.','e213')
s+=P('L’induction peut provoquer une chute circulatoire ; les équipes chirurgicale et anesthésique se coordonnent donc avant de la débuter.','e213')
s+=P('En revanche, un EVAR peut être réalisé sous anesthésie locale, avec une adaptation à la tolérance du patient.','e214','n1.6.4')
s+=P('Une conversion anesthésique peut être nécessaire selon la conscience, le confort et les besoins d’accès vasculaire.','e214')
s+=P('Le choix ne repose donc pas sur une préférence abstraite, mais sur l’anatomie, l’état actuel et les ressources de réparation.','e81','e152','e214')
s+=T(['Moyen','Mécanisme et objectif','Condition ou surveillance'],[
 [('L’équipe met en œuvre une réanimation restrictive.','e210'),('Elle limite l’aggravation hémorragique avant contrôle proximal.','e210'),('La conscience et la pression guident l’adaptation.','e211')],
 [('La réparation ouverte remplace le segment malade.','e218'),('Le clampage permet le contrôle aortique pendant la reconstruction.','e215'),('La coordination anesthésique anticipe la chute de pression à l’induction.','e213')],
 [('L’EVAR exclut le sac en laissant sa paroi en place.','e149'),('L’endoprothèse doit assurer une fixation et une étanchéité durables.','e149'),('Les instructions du dispositif et l’imagerie conditionnent la faisabilité.','e81','e152')],
 [('L’analgésie accompagne la prise en charge spécialisée.','e212','e251'),('Le contrôle de la douleur participe à la stratégie hémodynamique et à l’attente surveillée.','e212','e251'),('La modalité est adaptée à l’intervention et à l’état du patient.','e213','e214','n1.5.8')],
 [('La réduction du risque cardiovasculaire accompagne le parcours.','e47'),('Elle vise le risque vasculaire associé, au-delà de la seule paroi dilatée.','e47','e49'),('Le sevrage tabagique, la pression et les traitements de prévention sont réévalués.','e47','n1.2.1','n1.2.2')]
])
s+=H('Traitements associés et situations particulières')
s+=P('La prévention cardiovasculaire comprend sevrage tabagique, contrôle tensionnel et évaluation des traitements antiagrégants et hypolipémiants.','e47')
s+=P('Ces moyens traitent le risque cardiovasculaire ; ils ne remplacent donc pas une réparation urgente indiquée pour les symptômes ou la rupture.','e49','e251','e207')
s+=P('Une double antiagrégation ou d’autres circonstances à haut risque nécessitent une discussion périopératoire individualisée.','e119')
s+=P('L’insuffisance rénale sévère appelle une optimisation spécialisée avant réparation programmée, tandis que l’urgence vitale reste évaluée séparément.','e111','e206','e207')
s+=P('Chez une femme enceinte, le caractère indispensable de l’exploration et le produit de contraste sont discutés avec les équipes concernées.','esur-grossesse')
s+=P('Chez une mère enceinte ou allaitante présentant une insuffisance rénale, ESUR interdit l’administration de produits gadolinés.','esur-allaitement')
s+=P('Cette interdiction concerne le produit gadoliné, tandis que les précautions du contraste iodé suivent leur propre cadre rénal.','esur-allaitement')
s+=P('Elle porte donc sur l’injection de gadolinium, et non sur une IRM réalisée sans ce produit.','esur-allaitement')
s+=P('Chez une personne fragile, la décision expose les risques de l’intervention, la récupération attendue et les contraintes du suivi.','n1.5.2')
s+=H('11.C Surveillance : distinguer hémorragie, ischémie et complications de réparation')
s+=P('Après une rupture réparée, l’équipe surveille la récupération circulatoire et recherche les complications d’organes.','e239','e247','e249','nhs-surveillance')
s+=P('Une dégradation ou une absence d’amélioration doit faire rechercher un syndrome compartimental abdominal.','n1.6.6')
s+=P('Cette complication peut survenir après réparation ouverte comme après EVAR.','n1.6.5')
s+=P('La surveillance recherche aussi une ischémie colique et une ischémie aiguë des membres, qui nécessitent une évaluation rapide.','e247','e249')
s+=T(['Élément surveillé','Interprétation clinique','Action'],[
 [('La conscience et la pression changent pendant la phase aiguë.','e206','e211'),('La perfusion et la réanimation doivent être réévaluées.','e211'),('L’équipe adapte la stratégie en lien avec le contrôle hémorragique.','e210','e207')],
 [('Une pression intra-abdominale élevée s’associe à une défaillance d’organe.','e239'),('Un syndrome compartimental peut expliquer la dégradation.','e239'),('Le traitement spécialisé peut aller jusqu’à une laparotomie de décompression si les mesures initiales échouent.','e242')],
 [('Une ischémie colique est suspectée.','e247'),('Cette complication grave existe après les deux modes de réparation de rupture.','e247'),('L’équipe réalise une évaluation répétée et utilise une exploration adaptée à la suspicion.','e247')],
 [('Un membre devient soudainement ischémique.','e249'),('Une complication artérielle peut menacer le membre et la survie.','e249'),('Une revascularisation immédiate peut être nécessaire selon la cause.','e249')],
 [('Une endofuite directe ou une expansion du sac est détectée.','suivi-echec'),('Une défaillance de l’exclusion est possible.','suivi-echec'),('Une correction secondaire est discutée selon le mécanisme.','suivi-echec','n1.8.1','n1.8.2')]
])
s+=W('p11-suivi','Après EVAR : calendrier initial et stratification du suivi',P('Une imagerie précoce dans les 30 jours après EVAR évalue l’exclusion du sac et les complications d’accès.','e325')+P('L’angioscanner est préféré pour cette évaluation ; un duplex peut devoir être complété par un CT non injecté pour certains détails du dispositif.','e325')+P('Le faible risque exige absence d’endofuite, anatomie dans les instructions, chevauchement adéquat et zones d’étanchéité proximale et distale d’au moins 10 mm.','suivi-bas')+P('Le diamètre du collet proximal est inférieur à 30 mm et son angulation reste inférieure à 60°.','suivi-bas')+P('Le diamètre iliaque est inférieur à 20 mm, car le groupe ne comporte pas les caractéristiques anatomiques de haut risque décrites.','suivi-bas')+P('Dans ce groupe standard sélectionné, une imagerie différée jusqu’à cinq ans peut être envisagée selon le schéma européen.','suivi-bas')+P('Les situations de haut risque peuvent justifier une évaluation annuelle par CT ou duplex, avec réévaluation à chaque contrôle.','suivi-haut')+P('Une endofuite directe ou une croissance du sac supérieure à 10 mm conduit à envisager une intervention secondaire.','suivi-echec')+P('Toutefois, le suivi à long terme reste nécessaire après toute réparation et le schéma des dispositifs standards ne s’applique pas automatiquement aux réparations complexes.','e334','e336'))
s+=W('p11-ouvert','Après réparation ouverte : une surveillance existe aussi',P('Une surveillance après réparation ouverte recherche notamment pseudoanévrisme anastomotique et progression anévrismale sur d’autres segments.','e310','e311')+P('L’ESVS considère une imagerie périodique chez les patients susceptibles de bénéficier d’un traitement si une nouvelle lésion est découverte.','e311')+P('L’intervalle de cinq ans est proposé dans cette stratégie, avec un niveau de preuve limité.','e312')+P('L’angioscanner ou l’angio-IRM explore les lésions aortiques, tandis que le duplex est adapté aux territoires périphériques.','e313')+P('Ainsi, la solidité d’une reconstruction ouverte ne signifie pas la disparition de toute surveillance vasculaire.','e311','e336'))
s+=H('11.D Pronostic, sortie et continuité : énumérer les conditions')
s+=P('Le pronostic dépend de la rupture, du terrain et des complications, plutôt que d’un seul diamètre.','smw-resultats','n1.5.2','e239')
s+=P('La sortie est organisée après évaluation de la récupération, et non par application d’un jour fixe à toutes les situations.','nhs-sortie','nhs-surveillance','nhs-social')
s+='<ol>\n'
for text,ks in [
 ('La stabilité clinique permet le passage des soins critiques au secteur chirurgical selon l’évaluation de l’équipe.',['nhs-surveillance']),
 ('La mobilité permet au patient de se déplacer de manière autonome dans le secteur de soins.',['nhs-sortie']),
 ('La reprise des boissons et de l’alimentation est suffisamment tolérée pour permettre le retour à domicile.',['nhs-sortie','nhs-nutrition']),
 ('La stratégie antalgique est adaptée à la récupération et peut être relayée par voie orale lorsque l’alimentation est reprise.',['nhs-douleur','nhs-nutrition']),
 ('Les soins de plaie, les traitements et les aides nécessaires sont expliqués avant le départ.',['nhs-plaie','nhs-remise','nhs-social']),
 ('Le patient et ses proches savent reconnaître les symptômes imposant un recours urgent, notamment une douleur sévère ou un membre froid.',['nhs-alerte','chuv144','chuv-occlusion']),
 ('Le suivi vasculaire et son imagerie sont programmés, avec transmission des informations au médecin traitant.',['chuv-angiologie','chuv-suivi-actuel','e336'])]:
    s+='<li>'+html.escape(text)+C(*ks)+'</li>\n'
s+='</ol>\n'
s+=P('L’organisation du domicile tient compte de l’aide disponible, des activités habituelles et du rôle éventuel d’aidant du patient.','nhs-social')
s+=P('Les informations sont partagées avec l’entourage et les préférences du patient sont intégrées à la décision.','n1.1.15','n1.5.2')
s+=P('La résolution de l’urgence ne dispense donc pas de surveiller l’endoprothèse, les anastomoses et le risque cardiovasculaire.','e336','e311','e47')
s+=P('L’arrêt d’une surveillance d’imagerie peut être individualisé lorsqu’aucune intervention élective secondaire n’est retenue, tout en prévoyant la réévaluation de symptômes aigus.','e335')
save(11,s)

s=H('Prévention primaire : agir sur les facteurs modifiables chez les personnes à risque')
s+=P('Le tabac est le principal facteur de risque décrit dans la synthèse européenne, ce qui en fait une cible majeure de prévention.','e4')
s+=P('L’information du CHUV demande aux personnes à risque ou déjà atteintes d’arrêter de fumer et de surveiller leur pression.','chuv-quotidien')
s+=P('Lorsque le patient fume, une aide au sevrage est proposée afin de soutenir cette modification concrète.','n1.2.1')
s+=P('La prise en charge de l’hypertension suit également son parcours de soins propre.','n1.2.2')
s+=P('Ainsi, la prévention vasculaire vise les facteurs de risque plutôt qu’une promesse de disparition de toute maladie anévrismale.','e47','e49')
s+=H('Prévention secondaire : dépister les groupes à risque et surveiller les dilatations silencieuses')
s+=P('L’ESVS recommande un dépistage des groupes à haut risque, dont la définition dépend du contexte de population et du système de santé.','e30')
s+=P('L’information suisse demande aussi d’avertir les proches du besoin d’un dépistage selon les recommandations.','chuv-quotidien')
s+=P('L’échographie constitue l’examen de première ligne pour le dépistage et le suivi des petites dilatations.','e10','basel-surveillance')
s+=P('Cependant, les intervalles de surveillance d’un AAA silencieux ne doivent pas être appliqués à une douleur attribuable à l’anévrisme.','n1.2.3','e250','e251')
s+=T(['Cadre asymptomatique décrit dans l’enseignement bâlois','Intervalle proposé','Condition de lecture'],[
 [('La dilatation sous-anévrismale mesure 2.5–2.9 cm.','basel-surveillance'),('Un contrôle tous les 5 ans est proposé.','basel-surveillance'),('Ce schéma concerne une surveillance et ne remplace pas l’évaluation d’un symptôme nouveau.','basel-surveillance','e250')],
 [('Le diamètre est de 3.0–3.9 cm.','basel-surveillance'),('L’intervalle est de 3 ans.','basel-surveillance'),('La taille, la situation individuelle et les possibilités de traitement restent prises en compte.','e43')],
 [('Le diamètre est de 4.0–4.9 cm chez l’homme et de 4.0–4.4 cm chez la femme.','basel-surveillance'),('Une surveillance annuelle est proposée.','basel-surveillance'),('Une présentation symptomatique change le parcours.','e251')],
 [('Le diamètre atteint au moins 50 mm chez l’homme ou 45 mm chez la femme.','surv-hommes','surv-femmes'),('Le support propose des contrôles tous les 6 mois.','basel-surveillance'),('L’indication de réparation doit être confrontée au terrain et aux critères cliniques.','n1.5.2','basel-indication')]
])
s+=H('Prévention tertiaire : maintenir le résultat et prévenir les complications')
s+=P('Après réparation, le suivi cherche les endofuites, les complications de prothèse et la progression d’autres lésions vasculaires.','e310','e323','e336')
s+=P('La consultation du CHUV recherche systématiquement les endofuites par ultrasons après EVAR et utilise au besoin l’échographie de contraste.','chuv-suivi-actuel')
s+=P('Le médecin traitant reçoit les informations utiles à la continuité des soins et à l’organisation des contrôles.','chuv-angiologie','chuv-suivi-actuel')
s+=P('Par ailleurs, la reprise progressive d’activité et les aides à domicile accompagnent la récupération après chirurgie.','nhs-sortie','nhs-social')
s+=P('Le risque cardiovasculaire reste traité par les mesures de mode de vie et les classes thérapeutiques indiquées.','e47')
s+=P('Enfin, le patient et son entourage connaissent les signes de rupture et la conduite d’urgence suisse.','chuv-quotidien','chuv144')
s+=W('p12-f1','Le suivi est une mesure de prévention, pas une simple photographie répétée',P('L’imagerie précoce après EVAR évalue le succès de l’exclusion et aide à déterminer le risque de complication.','e325','e327')+P('La fréquence ultérieure est donc adaptée au risque anatomique et aux constatations du premier contrôle.','suivi-bas','suivi-haut')+P('Une nouvelle douleur ou une alarme de perfusion réouvre toutefois la branche clinique urgente, même entre deux examens programmés.','nhs-alerte','chuv144')+P('La continuité à long terme permet aussi de reconnaître des lésions aortiques ou périphériques apparues après la réparation initiale.','e310','e311'))
save(12,s)

s=H('Six décisions à conserver')
s+=P('Une douleur abdominale ou dorsale nouvelle avec malaise ou collapsus fait rechercher immédiatement une rupture d’AAA.','n1.1.7')
s+=P('Une échographie qui identifie l’anévrisme ne permet pas à elle seule d’exclure une fuite rétropéritonéale.','e205')
s+=P('L’angioscanner prépare la réparation si l’état le permet ; un patient trop instable peut être conduit directement au bloc.','e205','e207')
s+=P('Un AAA symptomatique intact relève d’une évaluation rapide surveillée puis d’une réparation urgente, même avant le diamètre habituel d’intervention élective.','e250','e251')
s+=P('Le choix de réparation dépend de l’anatomie, de l’état du patient et du bénéfice attendu, sans décision fondée sur un score isolé.','e81','e152','n1.5.2','n1.4.5')
s+=P('La sortie de l’épisode aigu et la réussite technique ne suppriment pas la nécessité d’un suivi vasculaire à long terme.','e336','e311')
save(13,s)

s=H('Questions d’examen : préciser le signe, sa portée et l’action')
s+=T(['Question','Réponse','Raison clinique'],[
 [('Une pulsation abdominale palpable suffit-elle à diagnostiquer un AAA ?','oxford-aorte'),('Non, car une aorte normale peut être palpable chez une personne mince.','oxford-aorte'),('La largeur et l’expansion orientent ; l’imagerie confirme la dilatation.','oxford-aorte','e10')],
 [('L’absence de masse palpable exclut-elle une rupture ?','e9','e204'),('Non, car la détection dépend de la morphologie et la présentation peut être incomplète.','e9','e204'),('La suspicion clinique conduit à une exploration et un avis immédiats.','n1.1.9')],
 [('Faut-il exiger la triade complète avant d’évoquer une rupture ?','e204'),('Non, elle n’est présente que chez environ 50 % des patients avec rupture.','e204'),('Une douleur nouvelle et des signes circulatoires peuvent suffire à déclencher la recherche urgente.','n1.1.7')],
 [('Une rupture contenue peut-elle être surveillée comme un petit AAA silencieux ?','e203'),('Non, le rétropéritoine ne colmate que temporairement l’hémorragie.','e203'),('La lésion reste une rupture et nécessite son parcours urgent.','e203','e207')],
 [('Une douleur avec un AAA inférieur à 55 mm permet-elle d’attendre le contrôle périodique ?','e250'),('Non, l’attribution symptomatique doit être explorée rapidement.','e250'),('Un AAA symptomatique intact peut justifier une réparation urgente après évaluation surveillée.','e251')],
 [('Le scanner doit-il toujours précéder l’entrée au bloc ?','e207'),('Non, un patient trop instable peut être conduit directement au bloc.','e207'),('La confirmation peut être peropératoire pour éviter de différer le contrôle hémorragique.','e207')],
 [('L’échographie sans signe de fuite exclut-elle une hémorragie rétropéritonéale ?','e205'),('Non, sa sensibilité pour ce saignement est limitée.','e205'),('Elle identifie surtout l’anévrisme, tandis que l’angioscanner renseigne la rupture et l’anatomie.','e205')],
 [('Faut-il rapidement normaliser toute pression basse par une réanimation abondante avant contrôle aortique ?','e210'),('Non, une stratégie restrictive peut limiter l’aggravation du saignement.','e210'),('La conscience et la tolérance circulatoire guident la réanimation transitoire.','e211')],
 [('Le but transitoire de 70–90 mmHg signifie-t-il que le patient est apte à rentrer chez lui ?','e211'),('Non, ce cadre concerne l’hypotension permissive chez un patient restant conscient.','e211'),('La sortie nécessite une récupération clinique et fonctionnelle distincte.','nhs-sortie','nhs-surveillance')],
 [('Un score pronostique ou l’âge seul permet-il de refuser une réparation de rupture ?','n1.4.4','n1.4.5'),('Non, NICE exclut une décision fondée sur un score ou un facteur isolé.','n1.4.4','n1.4.5'),('L’évaluation est clinique et individualisée selon le bénéfice, les risques et les préférences.','n1.5.2')],
 [('Une endofuite de type 2 impose-t-elle la même correction immédiate qu’un type 1 ou 3 ?','type2','endofuite-def'),('Non, la conduite du type 2 dépend notamment de l’expansion du sac.','n1.8.2'),('Les types 1 et 3 exposent directement la paroi à la pression artérielle.','endofuite-def','n1.8.1')],
 [('Un duplex couleur négatif suffit-il à exclure une endofuite suspectée ?','n1.7.5'),('Non, une exploration complémentaire adaptée reste nécessaire.','n1.7.4','n1.7.5'),('L’angioscanner injecté ou l’échographie de contraste répond à cette suspicion selon le contexte.','n1.7.4')],
 [('Une modification du diamètre prouve-t-elle toujours une croissance réelle ?','e15','e17'),('Non, le plan et la position des curseurs peuvent modifier la mesure.','e15','e17'),('Les comparaisons doivent conserver une méthode explicitée et cohérente.','e17','e320')],
 [('La réparation ouverte signifie-t-elle la fin de toute surveillance vasculaire ?','e311'),('Non, des lésions anastomotiques ou d’autres anévrismes peuvent apparaître tardivement.','e310','e311'),('Une surveillance adaptée demeure pertinente chez les patients pouvant bénéficier d’une intervention.','e311')],
 [('L’EVAR retire-t-il la paroi anévrismale ?','e149'),('Non, il exclut le sac de l’intérieur en laissant sa paroi en place.','e149'),('L’étanchéité et la fixation doivent rester durables, ce qui justifie le suivi.','e149','e336')],
 [('La fréquence d’une dilatation dans une série de dépistage donne-t-elle la fréquence d’AAA parmi les lombalgies ?','basel-epi','smw-methodes'),('Non, ces mesures ne portent pas sur la même population ni sur le même recrutement.','basel-epi','smw-methodes'),('Les chiffres restent donc attachés au sexe, à l’âge et au lieu de soins décrits.','basel-epi','smw-methodes')]
])
s+=W('p14-f1','Pourquoi une douleur évoquant une colique ne ferme-t-elle pas la branche vasculaire ?',P('La colique urétérale fait partie des diagnostics erronés rapportés lors d’une rupture d’AAA.','e204')+P('Une douleur du flanc peut donc demander une évaluation aortique lorsque le contexte et les signes de gravité sont compatibles.','e7','n1.1.7')+P('L’obstacle urétéral infecté possède aussi sa propre urgence ; les deux branches sont discriminées par la clinique et l’imagerie.','decompression','calculimage','e205'))
s+=W('p14-f2','Pourquoi faut-il encore un contrôle alors que l’opération a réussi ?',P('L’imagerie précoce établit l’exclusion du sac et recherche les complications initiales.','e325')+P('Cependant, des complications de dispositif, d’anastomose ou d’autres segments peuvent apparaître ensuite.','e310','e323')+P('Le patient garde donc un programme de suivi et des consignes pour les symptômes nouveaux.','e336','nhs-alerte'))
s+='<div class="p" id="dx10-question-finale">Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ?'+C('prompt-question-finale')+'</div>\n'
save(14,s)

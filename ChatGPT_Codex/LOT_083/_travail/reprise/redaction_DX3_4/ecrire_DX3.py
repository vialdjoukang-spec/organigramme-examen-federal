from pathlib import Path
import json
B=Path(__file__).parent;D=B/'DX.3';A={'entite':'Courbatures retardées après effort','references':{},'points':{str(n):{'blocs':[],'fenetres':[],'tableaux':[]}for n in range(1,15)}}
def lines(s):return [x.split('|',1)for x in s.strip().split('\n')if x.strip()]
def b(n,title,s):A['points'][str(n)]['blocs'].append([title,lines(s)])
def w(n,title,s):A['points'][str(n)]['fenetres'].append([title,lines(s)])
def table(n,title,heads,rows):A['points'][str(n)]['tableaux'].append([title,heads,[[x.split('|',1)for x in row]for row in rows]])
b(1,'Une douleur retardée liée à une charge musculaire', '''doms-definition|Les courbatures retardées correspondent à des manifestations douloureuses après une sollicitation musculaire, associées à des modifications ultrastructurales plutôt qu’à une rupture macroscopique.
ismult-indirect+doms-mecanisme|La société italienne ISMuLT les classe parmi les lésions indirectes non structurelles de type 1B dans son édition de 2013.
doms-definition|La revue européenne de Schroeter et collaborateurs, publiée en août 2024 avec participation GOTS et suisse, actualise leur description.
doms-mecanisme|Le terme anglais Delayed Onset Muscle Soreness explique l’abréviation DOMS et souligne le décalage entre la charge et les symptômes.
doms-mecanisme|Une contraction excentrique ou une charge inhabituelle favorise ce tableau ; son mécanisme précis ne se réduit toutefois pas à une explication unique.
ismult-direct+ismult-clinique|Une contusion résulte au contraire d’un choc direct, tandis qu’une déchirure peut provoquer une douleur aiguë localisée pendant un mouvement.
rhabdo-clinique+rhabdo-laboratoire|Une douleur après exercice ne suffit pas à conclure aux courbatures, car une rhabdomyolyse peut survenir dans le même contexte.
rms-doms|La synthèse du CHUV publiée en 2018 préconise une adaptation transitoire de l’entraînement pour les courbatures sans lésion nécessitant des soins aigus.''')
w(1,'Ce que signifie « non structurel » dans cette classification', '''ismult-indirect|La classification ISMuLT emploie ce terme lorsque les fibres ne présentent pas de lésion anatomique évidente à l’échelle considérée.
doms-definition+doms-mecanisme|Cette terminologie ne nie pas les changements ultrastructuraux décrits après effort, notamment ceux des sarcomères et des membranes cellulaires.
doms-biologie-imagerie|Un œdème peut apparaître sur les séquences sensibles aux liquides en IRM, même sans rupture musculaire macroscopique.
ismult-clinique|Une rupture partielle garde des arguments différents, comme une douleur brusque précisément localisée et reproduite par la contraction résistée.''')
w(1,'Trois mots à distinguer pendant l’entretien', '''doms-mecanisme|L’effort excentrique met en charge un muscle pendant son allongement et constitue un contexte classique de symptômes retardés.
ismult-clinique|La raideur désigne ici la limitation ressentie ou constatée avec augmentation du tonus, sans démontrer à elle seule une déchirure.
ismult-direct|Une contusion décrit le mécanisme direct du traumatisme et peut s’accompagner d’un hématome dont le volume influence les symptômes.
rhabdo-physiopath|La rhabdomyolyse implique une destruction cellulaire et une libération du contenu musculaire, avec des complications rénales ou électrolytiques possibles.''')
b(2,'Population exposée et histoire naturelle', '''doms-mecanisme|Une modification inhabituelle de charge ou un travail excentrique exposent aux courbatures, indépendamment du seul nom du sport pratiqué.
doms-prevention|Le niveau d’entraînement préalable compte dans le choix de la charge ; une progression adaptée vise à limiter l’agression initiale.
doms-definition|La limitation de performance peut être importante pendant l’épisode, même lorsque l’évolution habituelle reste bénigne et sans séquelle.
doms-mecanisme|La revue de 2024 décrit un début clinique entre 6 et 12 heures après l’exercice et un maximum entre 48 et 72 heures.
doms-mecanisme|Elle rapporte une guérison habituelle en une semaine, ce qui décrit une tendance clinique et non une autorisation individuelle de compétition.
ismult-clinique+rms-persistance|Des symptômes persistants ou récidivants conduisent à réexaminer l’hypothèse initiale, notamment devant une faiblesse ou des anomalies biologiques durables.
doms-definition|Les conséquences immédiates portent surtout sur la douleur, la mobilité et les performances, avec un risque de blessure secondaire pendant cette période.
rms-reprise|La reprise se décide donc avec les symptômes et la fonction récupérée, puis progresse vers les contraintes réelles de l’activité.''')
w(2,'Lire correctement les repères temporels', '''doms-mecanisme|Les délais de début et de maximum décrits dans la revue correspondent au développement des manifestations après la sollicitation initiale.
ismult-clinique|Une douleur apparaissant immédiatement sur un geste précis n’entre pas dans ce scénario retardé et justifie une autre analyse lésionnelle.
rhabdo-clinique|L’horaire ne distingue pas à lui seul une rhabdomyolyse, dont la présentation peut être incomplète et peu spécifique.
rms-persistance|Une trajectoire défavorable malgré les adaptations appelle une nouvelle évaluation, plutôt qu’une prolongation automatique de l’étiquette de courbatures.''')
b(3,'De la contrainte mécanique aux manifestations retardées', '''doms-mecanisme|Une charge dépassant la capacité ultrastructurale peut altérer les éléments de la fibre, puis déclencher dégradation protéique, autophagie et réaction inflammatoire locale.
doms-mecanisme|L’hypothèse mécanique occupe une place centrale dans la revue actuelle, tandis que les mécanismes exacts conservent des incertitudes.
doms-mecanisme|Les changements décrits concernent notamment les stries Z, les sarcomères et les membranes ; ils précèdent les symptômes pleinement constitués.
doms-mecanisme|L’intervalle initial peu symptomatique explique pourquoi une séance apparemment tolérée peut être suivie de douleurs et de difficultés fonctionnelles.
doms-mecanisme|L’inflammation et l’accumulation liquidienne accompagnent ensuite gonflement, tonus augmenté, diminution de force et limitation douloureuse des mouvements.
doms-biologie-imagerie|Les marqueurs musculaires ou inflammatoires peuvent augmenter, mais leur interprétation clinique doit distinguer cette réponse d’une destruction musculaire compliquée.
rhabdo-physiopath|Dans la rhabdomyolyse, l’épuisement énergétique et l’accumulation de calcium intracellulaire activent des mécanismes cytolytiques qui libèrent le contenu cellulaire.
rhabdo-physiopath|La myoglobine, l’hypovolémie et les perturbations électrolytiques expliquent alors des risques qui dépassent une simple gêne musculaire après entraînement.''')
table(3,'Relier le mécanisme à l’évaluation et à la décision',['Perturbation','Exploration','Conséquence thérapeutique'],[
['doms-mecanisme|La contrainte inhabituelle dépasse les capacités du muscle sollicité.','rms-clinique|L’entretien reconstitue charge, intensité, mécanisme et antécédents.','doms-prevention|Le programme réduit la charge initiale puis l’adapte progressivement au niveau acquis.'],
['doms-mecanisme|La réaction retardée s’accompagne de raideur et de douleur au mouvement.','rms-clinique|L’examen compare mobilité, palpation et réponse aux contractions.','rms-doms|L’activité est transitoirement adaptée aux symptômes et aux possibilités fonctionnelles.'],
['doms-biologie-imagerie|L’œdème intramusculaire modifie le signal sur les séquences sensibles aux liquides.','doms-biologie-imagerie|L’IRM est réservée aux présentations où la clinique laisse une incertitude.','doms-biologie-imagerie+ismult-clinique|Le résultat est confronté au mécanisme avant d’attribuer une rupture à toute anomalie de signal.'],
['rhabdo-physiopath|Une destruction musculaire peut libérer myoglobine et électrolytes dans la circulation.','rhabdo-laboratoire+rhabdo-orientation|Les CK et l’évaluation des complications précisent le diagnostic et l’orientation.','rhabdo-orientation|La filière de soins prévient les complications rénales et électrolytiques sans attendre une évolution spontanée.']])
w(3,'L’œdème n’est pas un diagnostic étiologique', '''doms-biologie-imagerie|L’IRM peut montrer un œdème intramusculaire et parfois une accumulation périfasciale dans les manifestations plus avancées des courbatures.
ismult-clinique|Une lésion structurale se recherche aussi par le mécanisme, la localisation, la contraction résistée et les autres constatations cliniques.
rhabdo-physiopath|La destruction musculaire peut également produire un œdème, dont l’importance dans un compartiment fermé menace la perfusion des tissus.
r82-boast2025-loges-0|Une douleur disproportionnée ou déclenchée par la mobilisation passive réoriente donc immédiatement vers la recherche d’un syndrome compartimental.''')
b(4,'Les complications précèdent le diagnostic rassurant', '''r82-boast2025-loges-0|Une douleur disproportionnée avec douleur à la mobilisation passive fait rechercher en priorité un syndrome aigu des loges.
r82-boast2025-loges-3|Lorsque ce diagnostic est posé, une décompression chirurgicale immédiate est nécessaire ; une investigation d’imagerie ne remplace pas cette décision.
rhabdo-clinique|Des douleurs associées à faiblesse, gonflement ou urines foncées imposent d’envisager une rhabdomyolyse, même si la triade n’est pas complète.
rhabdo-laboratoire|Le dosage des CK et l’analyse des urines aident à identifier cette situation, tandis que la prise en charge évalue ses complications.
ismult-clinique|Une douleur aiguë localisée sur un mouvement, avec claquement ou perte fonctionnelle, évoque davantage une lésion structurale qu’une courbature retardée.
ismult-direct|Un coup reçu sur la région douloureuse conduit à rechercher une contusion et un hématome, même si l’activité a pu continuer initialement.
rms-clinique|Une présentation discordante appelle aussi la recherche d’une cause veineuse, tendineuse, osseuse ou neurologique selon le contexte.''')
table(4,'Comparer les hypothèses qui changent la conduite',['Hypothèse','Élément discriminant','Piège','Action'],[
['r82-boast2025-loges-0|Le syndrome aigu des loges compromet la perfusion d’un compartiment.','r82-boast2025-loges-0|La douleur disproportionnée et celle provoquée passivement constituent des signes majeurs.','r82-boast2025-loges-1|Une simple estimation initiale de douleur ne remplace pas les examens neurovasculaires répétés.','r82-boast2025-loges-3|Le diagnostic établi entraîne une décompression immédiate par l’équipe chirurgicale.'],
['rhabdo-clinique|Une rhabdomyolyse peut suivre l’effort sans traumatisme direct.','rhabdo-laboratoire|Les CK et le contexte biologique étayent le diagnostic.','rhabdo-clinique|L’absence de pigmenturie ne suffit pas à exclure cette destruction musculaire.','rhabdo-orientation|L’évaluation organise rapidement prévention des complications et lieu de soins adapté.'],
['ismult-clinique|Une rupture partielle produit une lésion musculaire localisée.','ismult-clinique|La douleur brusque et focale, reproduite contre résistance, soutient cette hypothèse.','ismult-clinique|Une petite rupture peut ne laisser aucun défaut palpable.','rms-imagerie|L’imagerie précise une lésion ou complication lorsque l’examen et l’évolution l’indiquent.'],
['ismult-direct|Une contusion provient d’un impact direct sur le muscle.','ismult-clinique|La douleur immédiate et l’hématome concordent avec le mécanisme rapporté.','ismult-direct|Une capacité initiale à poursuivre l’effort ne suffit pas à juger la gravité.','ismult-direct|La région est réévaluée après le traumatisme pour préciser le retentissement et la lésion.']])
w(4,'Ne pas attendre des urines brunes pour agir', '''rhabdo-clinique|La triade musculaire et urinaire classique est présente chez moins de 10 % des patients dans les causes non traumatiques.
rhabdo-clinique|La moitié de ces patients n’ont pas de plainte musculaire, ce qui illustre les limites d’un dépistage fondé sur la douleur seule.
rhabdo-laboratoire|Une bandelette positive pour le sang sans érythrocytes au sédiment peut orienter vers une myoglobinurie dans un contexte compatible.
rhabdo-laboratoire|Les seuils historiques de CK varient et ne constituent pas une frontière universelle entre courbatures simples et complication systémique.''')
b(5,'Relier chaque question à une décision', '''rms-clinique|L’entretien commence par la séance, le geste, l’intensité et la chronologie, car ces informations séparent charge inhabituelle et traumatisme précis.
doms-mecanisme|La date de début est comparée à la fin de l’activité et à l’évolution suivante, plutôt qu’au seul jour de consultation.
rms-clinique|Les limitations quotidiennes et la possibilité de marcher ou d’utiliser le membre précisent le retentissement fonctionnel réel.
ismult-clinique|La répétition d’épisodes disproportionnés ou d’anomalies persistantes peut conduire à rechercher une pathologie musculaire sous-jacente.
rhabdo-physiopath+rhabdo-orientation|Les médicaments, substances et facteurs traumatiques sont examinés, car plusieurs mécanismes peuvent contribuer à une destruction musculaire.''')
table(5,'Questions, raisons et réponses opérationnelles',['Question','Raison','Conduite'],[
['doms-mecanisme|La charge était-elle nouvelle, plus intense ou particulièrement excentrique ?','doms-mecanisme|Une contrainte inhabituelle favorise l’agression ultrastructurale initiale.','doms-prevention|La reprise corrige la progression de charge au lieu de reproduire immédiatement la même séance.'],
['ismult-clinique|La douleur a-t-elle commencé pendant un geste précis ou plusieurs heures après ?','ismult-clinique|Une douleur aiguë focale et une douleur retardée ne soutiennent pas la même hypothèse.','ismult-clinique+rms-imagerie|Un mécanisme lésionnel aigu conduit à un examen ciblé et à l’imagerie si elle est indiquée.'],
['ismult-direct|Un choc direct, une chute ou un contact ont-ils touché le muscle ?','ismult-direct|Une contusion peut produire un hématome avec limitation du mouvement.','ismult-clinique|L’inspection et la palpation recherchent une lésion traumatique concordante.'],
['rhabdo-clinique|Des urines foncées, une faiblesse importante ou des symptômes généraux sont-ils apparus ?','rhabdo-physiopath|Une destruction musculaire peut avoir des conséquences rénales et électrolytiques.','rhabdo-laboratoire+rhabdo-orientation|Ces éléments conduisent au bilan biologique et à l’évaluation rapide des complications.'],
['r82-boast2025-loges-0|La douleur augmente-t-elle de façon disproportionnée ou lors d’un mouvement passif ?','r82-boast2025-loges-0|Une augmentation de pression peut compromettre les tissus d’une loge musculaire.','r82-boast2025-loges-2+r82-boast2025-loges-3|La suspicion engage la surveillance urgente et l’avis chirurgical approprié.'],
['aips-oa82-dafalgan-prudence+aips-oa82-dafalgan-posologie|Un antalgique est-il déjà utilisé et d’autres produits contiennent-ils du paracétamol ?','aips-oa82-dafalgan-prudence|Le cumul expose à une toxicité hépatique qui peut être retardée.','aips-oa82-dafalgan-posologie|L’ordonnance tient compte de toutes les prises, de la formulation et des plafonds adaptés au terrain.']])
w(5,'Ce qui conduit à sortir du parcours des courbatures', '''r82-boast2025-loges-0+r82-boast2025-loges-3|Une suspicion compartimentale impose une évaluation urgente ; le diagnostic confirmé conduit au traitement chirurgical immédiat.
rhabdo-clinique+rhabdo-orientation|Une présentation compatible avec rhabdomyolyse déclenche un bilan et une orientation fondée sur le risque de complications.
rms-persistance|Des symptômes persistants ou récidivants malgré une prise en charge adaptée nécessitent de reconsidérer le diagnostic et les complications possibles.
aips-oa82-dafalgan-prudence|Un surdosage suspecté ou une réaction cutanée sous antalgique relève d’une conduite médicamenteuse spécifique et non d’une simple surveillance sportive.''')
b(6,'Commencer par la fonction habituelle et le côté comparatif', '''rms-clinique+n81-hug22-force-normale|L’examen compare les deux côtés et prend comme référence une mobilité préservée et une force normale cotée à 5.
rms-clinique|L’inspection vérifie les contours, la peau et l’absence habituelle d’encoche, de voussure ou d’ecchymose avant de décrire les anomalies.
rms-clinique|La palpation explore ensuite la région douloureuse et les tissus voisins, en recherchant douleur provoquée, contracture ou modification du ballant musculaire.
ismult-clinique|Dans les courbatures, la raideur peut concerner le muscle sollicité, tandis qu’une douleur ponctuelle sur un défaut oriente autrement.
rms-clinique|La mobilité active puis passive est évaluée avec les articulations concernées, sans confondre limitation douloureuse et déficit moteur neurologique.
n81-cen-force|La force s’examine de manière segmentaire et comparative, en tenant compte de l’action du muscle et de la résistance opposée.
r82-boast2025-loges-0|Une douleur disproportionnée lors d’un mouvement passif interrompt le raisonnement de courbature banale et impose la recherche d’une complication.
n81-cen-sensibilite|L’examen sensitif compare les régions droites et gauches ainsi que les segments distaux et proximaux lorsque des symptômes neurologiques sont rapportés.''')
w(6,'Mesurer la force sans confondre les mécanismes', '''n81-cen-force|Une contraction contre résistance correspond à la cotation 4, tandis que la cotation 5 décrit une force normale.
n81-hug22-force-normale|Une force cotée 3 permet le mouvement contre la gravité ; la cotation 2 correspond à un mouvement dans le plan du lit.
n81-hug22-force-normale|Une contraction visible sans mouvement correspond à 1, tandis que l’absence de contraction visible correspond à 0.
rms-clinique+ismult-clinique|La douleur pendant la contraction est consignée avec la force obtenue, car une inhibition douloureuse ne décrit pas la même anomalie qu’une interruption musculaire.
doms-mecanisme|Les courbatures peuvent réduire la force et modifier la mécanique du mouvement ; leur caractère habituellement bénin n’annule pas cette limitation fonctionnelle.''')
w(6,'Mobiliser, étirer et comparer', '''rms-clinique|Le patient réalise d’abord le mouvement actif ; l’examinateur apprécie ensuite le mouvement passif et la réponse à l’étirement du muscle concerné.
ismult-clinique|Une douleur bien localisée reproduite par la contraction contre résistance renforce la recherche d’une lésion partielle dans le contexte approprié.
ismult-clinique|L’absence de défaut palpable ne suffit pas à exclure une petite lésion structurale, dont la taille peut limiter la détection manuelle.
rms-reprise|Les amplitudes et la force servent aussi de repères au suivi, avec comparaison fonctionnelle avant d’augmenter les contraintes sportives.''')
w(6,'Compléter l’examen neurologique quand il est indiqué', '''n81-cen-sensibilite|Le tact peut être exploré au doigt ou avec un coton passé sur la peau, en comparant les territoires correspondants.
n81-cen-sensibilite|Le compte rendu localise les anomalies et l’examen peut être répété lorsque la compréhension ou la coopération limite sa valeur.
n81-cen-force|Une évaluation globale aux membres supérieurs utilise les bras tendus à l’horizontale, puis une exploration segmentaire précise les anomalies.
n81-cen-force|Aux membres inférieurs, la manœuvre de Mingazzini utilise le décubitus dorsal, avec cuisses verticales et jambes horizontales.
n81-cen-force|L’observation dure 10 à 20 secondes avant de conclure à l’absence de déficit lors de ces manœuvres.''')
b(7,'7.1 — Syndrome douloureux musculaire retardé', '''doms-mecanisme|Les signes fonctionnels associent douleur retardée, gêne au mouvement et baisse des possibilités physiques après une charge inhabituelle.
ismult-clinique|La palpation peut retrouver une raideur musculaire diffuse, sans que cette constatation seule détermine la cause de la douleur.
doms-mecanisme|Les manifestations résultent de la succession contrainte ultrastructurale puis réaction locale, plutôt que d’une douleur obligatoirement immédiate pendant l’exercice.''')
b(7,'7.2 — Retentissement moteur et limitation douloureuse', '''doms-mecanisme|La réduction de force, le tonus accru et la limitation fonctionnelle accompagnent les symptômes, avec modification possible de la biomécanique.
rms-clinique+n81-cen-force|Le bilan sépare plainte de faiblesse, force mesurée, douleur provoquée et amplitude, afin de préciser le mécanisme du déficit constaté.
rms-reprise|Le suivi vérifie la récupération de ces dimensions avant une reprise progressive des gestes contraignants.''')
b(7,'7.3 — Signes qui évoquent une autre atteinte', '''rhabdo-clinique|Une association de faiblesse, gonflement et pigmenturie évoque une destruction musculaire, mais chaque signe doit être interprété sans exiger la triade complète.
r82-boast2025-loges-0|Une douleur disproportionnée et provoquée passivement évoque une complication compartimentale plutôt qu’un simple retentissement sportif.
ismult-clinique|Un défaut palpable, une douleur aiguë localisée ou une perte fonctionnelle immédiate évoquent une lésion structurale à caractériser.''')
w(7,'Raideur et douleur au mouvement', '''ismult-clinique|La raideur correspond à la sensation de muscle tendu et à la résistance appréciée lors de la palpation ou des mouvements.
doms-mecanisme|Une augmentation du tonus et l’œdème peuvent accompagner cette gêne après effort, dans le processus inflammatoire retardé décrit.
rms-clinique|Le geste de recherche compare palpation, mobilité et contraction, avec consignation de la localisation et des circonstances de la douleur.''')
w(7,'Pigmenturie et faiblesse : donner un sens aux mots', '''rhabdo-laboratoire|Une urine couleur thé peut correspondre à une myoglobinurie lorsque la bandelette détecte du sang sans érythrocytes au sédiment.
rhabdo-physiopath|La myoglobine libérée par la fibre détruite peut participer aux lésions rénales, ce qui explique la portée systémique du signe.
n81-cen-force|La faiblesse objective se démontre par l’évaluation motrice comparative, plutôt que par la seule déclaration de fatigue après une séance.
doms-mecanisme+rhabdo-clinique|Une baisse de performance peut accompagner les courbatures, mais sa sévérité et les signes associés déterminent la nécessité d’une exploration plus large.''')
(D/'contenu.json').write_text(json.dumps(A,ensure_ascii=False,indent=2)+'\n')

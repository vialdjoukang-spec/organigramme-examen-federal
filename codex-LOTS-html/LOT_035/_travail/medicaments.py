from format_lecon import D,paras
from html import escape
def raw(n):return (D/f'evidence/AIPS_{n}.txt').read_text()
def q(n,s):
 assert s in raw(n),(n,s[:80])
 return '<blockquote><p>'+escape(s).replace('\n','<br>\n')+'</p></blockquote>'
def sec(n,a,b):
 s=raw(n);i=s.index(a);return s[i:s.index(b,i)].strip()
def antalgie(l):
 n='46206'
 body=paras('DAFALGAN comprimés de paracétamol, autorisation Swissmedic 46206. La notice de février 2025 couvre les comprimés de 500 mg et de 1 g ; elle indique que la présentation de 1 g est alors indisponible dans le commerce. Cette disponibilité n’est pas vérifiée en pharmacie en temps réel. Utiliser une forme adaptée à la déglutition et au poids ; une personne aphagique sort du traitement oral ambulatoire.')
 for a,b in [('Posologie\n','Mode d\'administration'),('Instructions spéciales de dosage','Mises en garde et précautions'),('Grossesse, allaitement','Effet sur l’aptitude')]:body+=q(n,sec(n,a,b))
 body+=q(n,next(t for t in raw(n).splitlines() if t.startswith('Le paracétamol peut entraîner des réactions cutanées graves')))
 body+=paras('Le plafond quotidien inclut toutes les associations contenant du paracétamol. Une hépatite aiguë, notamment au cours d’une mononucléose, est une contre-indication de cette notice : ne pas se contenter de diminuer la dose. En cas de surdosage suspecté, demander immédiatement une prise en charge, même sans symptômes ; Tox Info Suisse peut guider la conduite.', 'La notice rapporte un renforcement possible de l’effet anticoagulant des coumarines lors de prises prolongées. En cas de déshydratation, de consommation excessive d’alcool, de maladie hépatique ou d’insuffisance rénale, revoir l’indication, le plafond et l’intervalle avant toute prescription.')
 return l.subwindow('paracetamol','Paracétamol : dose, terrain et sécurité AIPS',body,(13,))
def amoxicilline(l):
 n='49923'
 body=paras('Amoxicilline Sandoz : comprimés pelliculés 500/750/1000 mg, autorisation 49924 ; granulés pour suspension buvable 100 mg/4 ml et 200 mg/4 ml, autorisation 49923. Les deux formes figurent dans l’information professionnelle commune ci-dessous. Ne pas confondre ces concentrations lors du calcul en millilitres.')
 body+=q(n,sec(n,'Posologie usuelle','Pour le traitement de la gonorrhée'))
 body+=q(n,'Lors d’infections dues aux streptocoques β-hémolytiques du groupe A, le traitement devrait durer au moins dix jours.'.replace('d’infections',"d'infections"))
 body+=q(n,sec(n,'Enfants jusqu’à 40 kg'.replace('jusqu’à',"jusqu'à"),'Recommandation posologique'))
 body+=q(n,sec(n,'Patients présentant des troubles de la fonction rénale','Dialyse péritonéale'))
 body+=q(n,sec(n,'Contre-indications','Mises en garde et précautions'))
 body+=q(n,sec(n,'Grossesse, allaitement','Effet sur l’aptitude'))
 body+=q(n,"· L'apparition de réactions allergiques, de quelque nature qu'elles soient, impose un arrêt immédiat de la prise du médicament.")
 body+=q(n,next(t for t in raw(n).splitlines() if t.startswith('· La survenue d’une diarrhée'.replace('d’une',"d'une"))))
 body+=paras('Différence explicite avec les recommandations suisses : si l’antibiothérapie est indiquée, la SSI propose chez l’adulte 1 g toutes les douze heures pendant six jours. Chez l’enfant, elle propose 25 mg/kg toutes les douze heures pendant six jours. Ce schéma de recommandation ne correspond pas aux trois à quatre prises et à la durée d’au moins dix jours de cette spécialité : son emploi selon la SSI est hors information professionnelle pour ces modalités. Il doit être assumé et documenté par le prescripteur ; il n’est pas présenté comme une citation AIPS.', 'Portée pédiatrique du schéma SSI : ni la page SSI ni le tableau de Pédiatrie suisse 2023 consultés ne précisent un plafond par prise ou une règle de passage au schéma adulte. Ne pas extrapoler sans limite les 25 mg/kg par prise chez un enfant de poids élevé. Le prescripteur doit vérifier le plafond applicable et le choix éventuel du schéma adulte avant de prescrire. Le seuil de 40 kg et le maximum pédiatrique de 2000 mg par jour figurant dans la notice ci-dessus concernent son schéma en trois à quatre prises ; ils ne démontrent pas un plafond validé pour le schéma SSI en deux prises.',
 'La notice ne recommande pas cette amoxicilline pendant l’allaitement et prévoit le sevrage si son emploi est nécessaire. Une mononucléose est une contre-indication, et non une simple remarque sur un rash. Préciser la nature de toute allergie aux bêta-lactamines ; ne pas choisir une alternative de mémoire.', 'Une diarrhée importante ou persistante, des lésions cutanées sévères ou des signes d’allergie imposent une réévaluation rapide. Vérifier les interactions, notamment méthotrexate et anticoagulants, dans la notice complète avant prescription.')
 return l.subwindow('amoxicilline','Amoxicilline : notice suisse et divergence de la recommandation SSI',body,(1,2,12))
def ceftriaxone(l):
 n='44625'
 body=paras('Rocephin, ceftriaxone, autorisation Swissmedic 44625 pour les présentations injectables et perfusables décrites dans la notice de juin 2025. La reconstitution dépend de la forme choisie : une préparation contenant de la lidocaïne ne passe jamais par voie intraveineuse.')
 body+=q(n,sec(n,'Adultes et enfants de plus de douze ans','Nouveau-nés, nourrissons'))
 body+=q(n,sec(n,'Nouveau-nés, nourrissons et enfants jusqu’à douze ans'.replace('jusqu’à',"jusqu'à"),'Patients âgés'))
 body+=q(n,'Dans le traitement de la blennorragie (souches produisant ou non des pénicillinases), il est recommandé de procéder à l’administration unique de 0,25 g de Rocephin par voie i.m.'.replace('l’administration',"l'administration"))
 body+=q(n,sec(n,'\nContre-indications\n','\nMises en garde'))
 body+=q(n,sec(n,'Grossesse, allaitement','Effet sur l’aptitude'))
 body+=q(n,'En présence de réactions d’hypersensibilité graves, le traitement par la ceftriaxone doit être immédiatement interrompu et des mesures d’urgence adéquates doivent être prises.'.replace('d’hypersensibilité',"d'hypersensibilité").replace('d’urgence',"d'urgence"))
 body+=paras('Pour la gonorrhée oropharyngée, la SSI validée le 23 octobre 2026 recommande ceftriaxone 1 g par injection intramusculaire ; la voie intraveineuse est également possible. La dose de 1 g de la recommandation est hors information professionnelle par rapport aux 0,25 g indiqués pour la blennorragie dans cette notice. La dose historique AIPS n’est donc pas transposée comme traitement contemporain du pharynx. Le spécialiste choisit et documente le schéma actualisé, vérifie les résistances et les contraintes de préparation.', 'En cas de grossesse, la notice impose une préparation sans lidocaïne si le traitement est indispensable ; pendant l’allaitement, elle demande l’interruption de celui-ci si le traitement est absolument nécessaire. Chez le nouveau-né, appliquer les contre-indications spécifiques, notamment bilirubine, prématurité et calcium, avant tout raisonnement de dose.', 'Les mélanges calciques sont incompatibles. En cas d’anémie sous traitement, rechercher une hémolyse médicamenteuse ; contrôler la coagulation selon terrain et interactions. Une allergie grave ou une réaction cutanée sévère impose l’arrêt et une prise en charge immédiate. Le choix d’une alternative relève de l’antibiogramme et de l’avis infectiologique.')
 return l.subwindow('ceftriaxone','Ceftriaxone : limites AIPS et recommandation suisse actualisée',body,(8,14))

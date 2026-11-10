from rendu import outils

p,c,h,w,table,liste,save=outils(12)
a=w('Progression de l’entraînement et facteurs associés',[
('La prévention européenne ENMC2025 associe hydratation et nutrition appropriées, familiarisation progressive et réduction des activités à risque inhabituel.',['e15']),
('L’augmentation brutale des contraintes, notamment des contractions excentriques, est discutée avec la personne et l’encadrement sportif.',['e15','e02']),
('Une contraction excentrique survient pendant l’allongement du muscle qui travaille ; ce type d’entraînement figure parmi les situations de risque décrites.',['e15']),
('La chaleur, l’humidité, une infection récente et les produits qui influencent la thermorégulation sont intégrés à la préparation de l’activité.',['e15']),
('Les symptômes musculaires préoccupants doivent pouvoir être signalés et conduire à une évaluation plutôt qu’à la poursuite sous pression collective.',['e02','e15'])])
b=w('Prévenir une nouvelle crise sur terrain susceptible',[
('Une caractéristique RHABDO motive la recherche d’une cause génétique ou métabolique pouvant modifier les conseils préventifs.',['e06','e14']),
('Une anomalie d’oxydation lipidique conduit à limiter les déclencheurs identifiés, notamment le jeûne, les efforts prolongés et les maladies intercurrentes.',['e04']),
('Une glycogénose et une anomalie liée à RYR1 ne reçoivent pas un conseil identique ; la nutrition, l’intensité et les températures sont adaptées au diagnostic.',['e03','e15']),
('Le conseil génétique et l’explication des manifestations familiales font partie de la prise en charge d’une susceptibilité confirmée.',['e04','e14']),
('La reprise se construit avec les spécialistes lorsque les symptômes ou le terrain rendent le parcours habituel insuffisant.',['e15','e16'])])
s=h('La prévention primaire agit sur l’exposition')
s+=p('Le CHUV rappelle en2020 que l’effort, les toxiques et les traumatismes comptent parmi les causes fréquentes, souvent associées entre elles.','r06')
s+=p('Le programme de prévention situe donc les charges d’exercice dans leur contexte réel, puis écarte les cofacteurs évitables identifiés à l’anamnèse.','r06','s03','e15')
s+=p('La fenêtre '+a+' traduit les recommandations européennes ENMC2025 en décisions concernant l’entraînement et son environnement.','e15')
s+=p('Une reprise après interruption augmente progressivement les contraintes ; l’athlète et l’encadrement tiennent compte du caractère réellement inhabituel de la séance.','e02','e15')
s+=p('L’hydratation et la nutrition sont adaptées à l’activité, à la chaleur et au terrain ; un apport imposé sans considération clinique ne remplace pas la prévention.','e15','s04')
s+=p('L’activité est réorganisée en cas d’infection récente ou d’exposition à des produits pouvant contribuer à la crise.','e15','e06')
s+=h('La prévention secondaire reconnaît tôt la complication')
s+=p('La référence suisse décrit une triade inconstante ; l’absence de pigmenturie ne doit donc pas retarder le bilan d’une présentation préoccupante.','r07')
s+=p('Une douleur sévère, un gonflement inhabituel, une baisse des urines ou une coloration foncée conduit à une évaluation médicale adaptée au risque.','e13','r08')
s+=p('Les personnes ayant un terrain rénal ou des comorbidités reçoivent une surveillance plus prudente, car les conséquences du même épisode peuvent différer.','e13','s04')
s+=p('La protection rénale inclut l’identification des facteurs réversibles et la surveillance des électrolytes ; elle ne repose pas sur un protocole automatique d’alcalinisation.','s03','e10')
s+=h('La prévention tertiaire organise une récupération durable')
s+=p('La '+b+' relie les résultats du bilan spécialisé à un conseil réellement adapté aux déclencheurs de la personne.','e06','e14','e15')
s+=p('Le rapport ENMC recommande une réintroduction progressive de l’activité au moins4semaines après la résolution des symptômes.','e15')
s+=p('Le niveau de reprise et l’accompagnement tiennent compte de la force, des douleurs, de la fatigue et du retentissement psychologique.','e11','e15','e16')
s+=p('Après une insuffisance rénale sévère, un suivi rénal à distance recherche une récupération incomplète ou une évolution vers une maladie rénale chronique.','s10')
s+=p('Une CK durablement élevée, des récidives ou des manifestations familiales motivent le bilan étiologique, afin de réduire le risque d’un nouvel épisode.','r09','e06','e14')
s+=p('La préparation de la reprise professionnelle et sportive comprend les adaptations de charge, les contacts de soins et les conditions d’une nouvelle consultation.','e15','e16')
save(s)

p,c,h,w,table,liste,save=outils(13)
s=p('Une élévation isolée de CK après le sport ne démontre pas une rhabdomyolyse compliquée ; la clinique, le rein et les électrolytes déterminent la conduite.','e02','e09','e13')
s+=p('L’absence de la triade douleur, faiblesse et pigmenturie n’exclut pas la maladie ; une présentation inquiétante reçoit son bilan immédiatement.','r07','e13')
s+=p('Une douleur disproportionnée ou déclenchée passivement fait rechercher une loge aiguë, dont la confirmation impose une décompression chirurgicale immédiate.','b01')
s+=p('Le remplissage est individualisé selon volémie, diurèse et tolérance ; la persistance de CK élevées ne justifie pas seule une perfusion prolongée.','s04','aips-n4')
s+=p('La récidive, une crise après exercice habituel ou une hyperCKémie persistante à8semaines motive la discussion d’un bilan neuromusculaire.','e06','e14')
s+=p('La reprise physique est progressive et respecte la période d’au moins4semaines après résolution des symptômes décrite par le consensus ENMC2025.','e15')
save(s)

p,c,h,w,table,liste,save=outils(14)
s=h('Les questions distinguent preuve, risque et conduite')
s+=table(['Question d’examen','Réponse','Raison'],[
['Une CK élevée après un entraînement suffit-elle pour imposer une perfusion intensive ?','La décision repose sur la clinique, la fonction rénale, les électrolytes et le terrain, après interprétation du résultat.'+c('e09','e13'),'Des personnes saines peuvent libérer beaucoup de CK après l’exercice sans développer de complication rénale.'+c('e02','e09')],
['Faut-il attendre des urines brunes pour rechercher une rhabdomyolyse ?','La recherche se poursuit avec les autres signes et le dosage des CK, même si les urines sont claires.'+c('r07','r08'),'La triade classique est inconstante et sa présence n’est pas une condition de sécurité pour décider du bilan.'+c('r07','e13')],
['Quel seuil le consensus ENMC2025 propose-t-il pour l’épisode d’effort symptomatique ?','Il retient une hausse rapide des CK supérieure à10000UI/L avec un tableau de douleur, faiblesse ou gonflement.'+c('e12'),'Le critère est contextualisé à l’effort ; il est associé à une cinétique et ne constitue pas un seuil universel de danger.'+c('e12','e13')],
['Une CK sous ce seuil exclut-elle une urgence dès la première consultation ?','Les signes rouges ou un prélèvement précoce maintiennent le besoin d’évaluation et de surveillance.'+c('e12','e13'),'Le pic peut survenir1–4jours après l’événement, tandis qu’une complication clinique détermine sa propre priorité.'+c('e12','e13')],
['Une bandelette positive pour le sang prouve-t-elle la myoglobinurie ?','Le résultat est confronté aux érythrocytes du sédiment et à l’histoire musculaire.'+c('r08'),'La réaction ne distingue pas myoglobine et hémoglobine ; l’interprétation dépend donc du contexte et de la microscopie.'+c('r08')],
['Quel changement local fait craindre une loge aiguë ?','Une douleur disproportionnée ou augmentée à l’étirement passif déclenche l’avis chirurgical et la démarche dédiée.'+c('b01'),'La pression peut compromettre la perfusion ; une décompression immédiate suit le diagnostic retenu.'+c('b01')],
['La CK doit-elle descendre sous5000UI/L avant toute réduction des apports ?','Le volume est ajusté selon volémie, diurèse, fonction rénale et cinétique globale, sans poursuite mécanique sur cette seule valeur.'+c('s04'),'La revue SRLF2026 souligne le risque de surcharge sans bénéfice démontré d’un maintien de perfusion fondé uniquement sur ce chiffre.'+c('s04')],
['La dose adulte500mLà3litres/24h de Chlorure de sodium0,9%Baxter représente-t-elle un protocole de rhabdomyolyse ?','Cette dose de notice concerne la déshydratation extracellulaire isotonique et la déplétion sodique ; la prescription reste individualisée.'+c('aips-n4'),'L’indication, le terrain et la réponse déterminent la posologie, le débit et la durée ; le cadre général ne remplace pas leur évaluation.'+c('aips-n4','s04')],
['Une hypocalcémie initiale asymptomatique reçoit-elle toujours une supplémentation ?','Elle est respectée en l’absence de symptômes ou d’une indication propre à une hyperkaliémie menaçante.'+c('s08'),'La correction excessive peut favoriser les dépôts phosphocalciques et une hypercalcémie pendant la récupération.'+c('s08')],
['Le bicarbonate ou le mannitol est-il un traitement systématique de chaque épisode ?','L’alcalinisation urinaire systématique ne repose pas sur une preuve retenue par ENMC ; le mannitol n’est pas recommandé par la revue SRLF2026.'+c('e10','s07'),'Le rationnel physiopathologique ne suffit pas à démontrer un bénéfice et ces interventions comportent leurs propres risques.'+c('s06','s07')],
['La dialyse sert-elle préventivement à retirer la myoglobine dès qu’elle augmente ?','L’indication répond à la complication rénale ou métabolique, appréciée avec le néphrologue ou le réanimateur.'+c('s09','k04'),'L’épuration prophylactique du pigment ne dispose pas d’un bénéfice clinique justifiant son emploi systématique.'+c('s09')],
['Une crise après exercice habituel dispense-t-elle de rechercher une cause musculaire ?','Cette discordance, la récidive ou les antécédents familiaux orientent au contraire vers le bilan spécialisé RHABDO.'+c('e06','e14'),'Un effort peut révéler une susceptibilité génétique ou métabolique au lieu d’expliquer seul l’épisode.'+c('e03','e04','e06')],
['Le second souffle donne-t-il un diagnostic génétique certain ?','Il guide le phénotypage d’une glycogénose, puis la biologie et la génétique sont interprétées ensemble.'+c('e03','d01'),'Une histoire évocatrice ne remplace pas la confirmation spécialisée et la confrontation des variants au phénotype.'+c('e03')],
['La normalisation des analyses suffit-elle pour reprendre immédiatement une séance maximale ?','La reprise est progressive ; ENMC2025 propose une réintroduction au moins4semaines après disparition des symptômes.'+c('e15'),'La récupération peut inclure des séquelles fonctionnelles ou psychologiques qui nécessitent un accompagnement.'+c('e11','e16')],
['Une IRM injectée suit-elle la règle générale d’allaitement si la mère a aussi une atteinte rénale ?','La règle spécifique ESUR interdit le gadolinium chez la mère enceinte ou allaitante présentant une atteinte rénale.'+c('im7'),'Cette situation maternelle est distinguée de la règle générale de poursuite de l’allaitement après un macrocyclique.'+c('im2','im7')]])
s+=p('Chaque décision conserve le contexte du résultat : l’urgence porte sur la personne et les complications, puis le bilan étiologique explique la crise et prépare la prévention.','e13','e14','e16')
s+=h('Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ?'+c('ed'))
save(s)

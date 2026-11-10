def rediger(c):
 c.block(12,'Prévention primaire : ne pas promettre de supprimer une maladie multifactorielle',[
 ('Le modèle physiopathologique associe susceptibilité et facteurs environnementaux ; il ne démontre pas une mesure unique empêchant toute dermatomyosite.','cedef-meca'),
 ('La photoprotection recommandée dans la maladie vise surtout à diminuer le risque de poussée cutanée ou musculaire.','bsr-ii'),
 ('Elle associe une limitation de l’exposition solaire et une protection solaire large spectre de facteur élevé, selon la recommandation britannique.','bsr-ii'),
 ('La prévention des risques provoqués par les traitements se prépare avant l’introduction, avec le terrain infectieux et les médicaments associés.','rms-bilan+im-inter+oc-warn'),
 ('La notice suisse d’Imurek, actualisée en avril 2026, rappelle les risques liés aux vaccinations sous immunosuppression.','im-date+im-warn'),
 ('Les vaccins vivants sont déconseillés pendant ce traitement et la notice demande d’attendre au moins trois mois après l’arrêt pour les administrer.','im-warn+im-inter')])
 c.block(12,'Prévention secondaire : reconnaître les organes et organiser le dépistage',[
 ('Une faiblesse proximale associée à des signes cutanés conduit à une caractérisation spécialisée plutôt qu’à une simple prescription antalgique.','pnds-examen+pnds-severite'),
 ('Le dépistage des difficultés de déglutition concerne tous les patients selon la proposition de la BSR.','bsr-xi'),
 ('La recherche d’une atteinte interstitielle utilise les facteurs de risque et le scanner selon ERS/EULAR.','ers-depistage'),
 ('Le bilan cardiaque adulte considère la troponine I, l’ECG et les explorations complémentaires adaptées.','bsr-x'),
 ('La surveillance tumorale adulte repose sur un niveau de risque, en plus des dépistages habituels du pays.','imacs-risk+imacs-screen'),
 ('Un dépistage tumoral systématique n’est pas recommandé dans la forme juvénile sans suspicion clinique particulière.','bsr-vii')])
 c.fen(12,'IMACS : qui reçoit quel dépistage tumoral ?',[
 ('La stratégie IMACS décrite s’applique aux adultes diagnostiqués dans les 3 ans suivant le début des symptômes de myopathie inflammatoire.','imacs-screen'),
 ('La dermatomyosite constitue un facteur de haut risque ; les anticorps anti-TIF1γ et anti-NXP2 font également partie de cette catégorie.','imacs-risk'),
 ('Un début après 40 ans, une activité persistante, une dysphagie importante et des lésions nécrotiques ou ulcérées contribuent aussi à l’appréciation.','imacs-risk'),
 ('Au moins 2 facteurs de haut risque définissent un risque global élevé dans cette classification.','imacs-risk'),
 ('Un seul facteur de haut risque ou au moins 2 facteurs intermédiaires définissent un risque global modéré.','imacs-risk'),
 ('Ces catégories comparent des patients atteints de myopathie inflammatoire et ne signifient pas que le risque standard égale celui de la population générale.','imacs-risk'),
 ('Le dépistage de base est réalisé au diagnostic dans la catégorie standard ; le dépistage renforcé s’y ajoute dans la catégorie modérée.','imacs-screen'),
 ('En cas de risque élevé, les deux bilans sont réalisés au diagnostic et le bilan de base est répété chaque année pendant 3 ans.','imacs-screen')])
 c.tab(12,'Les deux niveaux de dépistage sont des ensembles attribués à IMACS',['Niveau','Examens décrits','Précaution d’application'],[
  [('Le bilan de base associe histoire clinique et examen complet.','imacs-screen'),('Il comprend numération, bilan hépatique, inflammation, électrophorèse avec chaînes légères, urines et radiographie thoracique.','imacs-screen'),('Il s’ajoute aux programmes de dépistage usuels adaptés à l’âge et au sexe.','imacs-screen')],
  [('Le bilan renforcé comprend un scanner du cou, du thorax, de l’abdomen et du pelvis.','imacs-screen'),('Il considère les examens mammaires, cervicaux, prostatiques, ovariens et digestifs décrits par la recommandation.','imacs-screen'),('Les examens déjà réalisés dans un programme national sont pris en compte pour éviter une répétition automatique.','imacs-screen')],
  [('La stratification est réévaluée dans le contexte clinique.','imacs-risk'),('Les anticorps, la présentation et l’activité persistante participent au risque.','imacs-risk'),('La décision d’imagerie tient aussi compte du bénéfice attendu et des risques de l’exposition.','imacs-screen')]
 ])
 c.block(12,'Prévention tertiaire : préserver la fonction et limiter les complications',[
 ('Le risque de fracture est évalué chez les patients atteints de myosite, y compris indépendamment de l’exposition aux glucocorticoïdes.','bsr-iv'),
 ('L’exercice adapté et la réadaptation limitent le retentissement fonctionnel et soutiennent la participation quotidienne.','bsr-i+bsr-xii'),
 ('Une infection, une jaunisse ou des saignements sous azathioprine déclenchent les conduites prévues par la notice, plutôt qu’une attente jusqu’au contrôle suivant.','im-warn'),
 ('L’hydratation, la fonction rénale et la tolérance de perfusion sont suivies sous immunoglobulines afin de limiter les complications.','oc-warn'),
 ('La préparation de la grossesse et le suivi après l’accouchement sont organisés avec les spécialistes, en recherchant une maladie bien contrôlée.','bsr-viii'),
 ('Les adaptations professionnelles et l’intervention précoce de l’AI peuvent soutenir le maintien dans l’activité lorsque la maladie menace l’emploi.','ai-reintegration'),

 ])
 c.block(13,'Six décisions à retenir',[
 ('Une peau évocatrice et une faiblesse des ceintures conduisent à caractériser la myopathie et à rechercher ses atteintes d’organes.','pnds-examen+rms-conclusion'),
 ('Une CK normale ne protège pas d’une forme amyopathique avec pneumopathie interstitielle menaçante.','fr-mda5'),
 ('La dysphagie et les manifestations respiratoires ou cardiaques changent la filière selon leur gravité clinique.','pnds-severite'),
 ('Les critères EULAR/ACR classent les myopathies inflammatoires et ne remplacent pas le diagnostic individuel.','rms-class'),
 ('Une immunothérapie est prescrite avec la notice propre au produit, puis surveillée selon son risque et la réponse clinique.','sp-dose+im-warn+oc-dose'),
 ('Le contrôle inflammatoire, la récupération des activités et les dépistages associés restent des objectifs complémentaires.','pnds-objectif+rms-fonction+imacs-screen')])

 c.tab(14,'Questions d’examen : réponse explicite et raison',['Question','Réponse attendue','Raison clinique'],[
  [('Une faiblesse proximale douloureuse suffit-elle à définir une dermatomyosite ?','rms-clin'),('Non ; le diagnostic confronte la peau, la distribution du déficit et les investigations nécessaires.','rms-conclusion'),('Les causes endocriniennes, toxiques, neurologiques et les autres myopathies doivent être considérées.','rms-clin+rms-hist')],
  [('Une CK normale permet-elle de renoncer au bilan pulmonaire d’un phénotype cutané anti-MDA5 ?','fr-mda5'),('Non ; la présentation peut être amyopathique et exposer à une atteinte interstitielle sévère.','fr-mda5'),('La gravité pulmonaire ne suit pas nécessairement l’importance de la lésion musculaire clinique.','fr-mda5')],
  [('Une probabilité EULAR/ACR d’au moins 55 % constitue-t-elle un diagnostic individuel automatique ?','crit-cutoffs'),('Non ; elle permet une classification probable dans le cadre défini par la méthode.','crit-cutoffs+rms-class'),('L’absence de meilleure explication est une condition et la démarche clinique reste nécessaire.','crit-table')],
  [('Les papules de Gottron et le signe de Gottron ont-ils la même morphologie ?','crit-table'),('Non ; les papules sont en relief, tandis que le signe correspond à des macules non palpables.','crit-table'),('La description morphologique permet d’utiliser correctement les variables cliniques.','crit-table')],
  [('Une force périphérique encore correcte exclut-elle une dysphagie importante ?','bsr-xi'),('Non ; la déglutition doit être interrogée et évaluée pour elle-même.','bsr-xi'),('La faiblesse générale ne prédit pas toujours l’atteinte de déglutition et son risque d’inhalation.','bsr-xi')],
  [('Quelle troponine la BSR préfère-t-elle pour le dépistage cardiaque adulte dans la myosite ?','bsr-x'),('La troponine I est préférée dans cette recommandation.','bsr-x'),('La troponine T peut aussi être exprimée par du muscle squelettique en régénération.','bsr-x')],
  [('Peut-on utiliser les explorations fonctionnelles respiratoires à la place du scanner de dépistage interstitiel ?','ers-hrct'),('Non ; ERS/EULAR recommande de ne pas remplacer le scanner par ces explorations.','ers-hrct'),('Les deux modalités explorent des dimensions différentes et le guide maintient le scanner dans le dépistage à risque.','ers-hrct+ers-depistage')],
  [('La fourchette générale de Spiricort est-elle un protocole pondéral autonome de dermatomyosite ?','sp-dose'),('Non ; elle appartient au cadre général AIPS et la dose dépend de la maladie, de sa gravité et de la réponse.','sp-dose'),('L’induction et la réduction sont organisées avec l’équipe spécialisée, sans extrapoler une préparation intraveineuse depuis les comprimés.','sp-dose+bsr-i')],
  [('Sous Imurek, un panel génétique rassurant dispense-t-il des contrôles de numération ?','im-warn'),('Non ; une surveillance sanguine rapprochée reste indispensable.','im-warn'),('Les tests ne repèrent pas tous les patients exposés à une toxicité sévère et les cellules peuvent encore diminuer après l’arrêt.','im-warn')],
  [('La dermatomyosite traitée par Octagam permet-elle un débit supérieur à 0,04 mL/kg/min si la perfusion paraît tolérée ?','oc-dose'),('Non ; ce plafond spécifique doit être respecté dans la dermatomyosite.','oc-dose'),('Cette population présente un risque thromboembolique accru dans la notice.','oc-warn')],
  [('Une absence d’effet après 6 mois d’Octagam justifie-t-elle une poursuite inchangée automatique ?','oc-dose'),('Non ; l’AIPS demande l’arrêt en l’absence d’effet à cette échéance.','oc-dose'),('La réponse est évaluée après chaque cycle et la poursuite suppose une efficacité individuelle.','oc-dose')],
  [('Les dépistages tumoraux adultes sont-ils reproduits systématiquement dans la forme juvénile ?','bsr-vii'),('Non ; un dépistage systématique n’est pas recommandé sans suspicion particulière.','bsr-vii'),('L’association tumorale et les recommandations de dépistage diffèrent entre les formes adultes et juvéniles.','bsr-v+bsr-vii')],
  [('Une CK diminuée suffit-elle à déclarer une guérison fonctionnelle ?','rms-bilan+rms-fonction'),('Non ; la force utile, les organes et les activités quotidiennes doivent aussi être évalués.','bsr-i+bsr-xii'),('L’activité de maladie et le handicap peuvent être dissociés.','rms-fonction')]
 ])

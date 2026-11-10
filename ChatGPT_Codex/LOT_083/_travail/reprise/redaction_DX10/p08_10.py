def rediger(c):
 c.block(8,'Le diagnostic positif est une intégration clinique, immunologique et parfois histologique',[
 ('Le diagnostic repose sur la concordance entre les manifestations cutanées, la distribution musculaire, le bilan biologique et les explorations adaptées.','rms-conclusion+fr-definition'),
 ('Une éruption héliotrope ou des lésions de Gottron ont une valeur d’orientation importante dans une constellation compatible.','crit-table+pnds-examen'),
 ('La présence de ces signes n’empêche pas de rechercher un diagnostic différentiel ou une complication d’organe.','rms-clin+rms-conclusion'),
 ('Une biopsie musculaire peut être moins déterminante dans une dermatomyosite cutanéomusculaire typique que devant une myopathie non caractérisée.','rms-hist'),
 ('L’imagerie et l’électroneuromyographie complètent la caractérisation ; aucun de ces examens n’est interprété isolément comme une preuve universelle.','rms-bilan+rms-hist'),
 ('Les autoanticorps facilitent le phénotypage et l’appréciation pronostique, mais leur positivité doit rester cohérente avec la clinique.','bsr-vi+fr-anticorps')])
 c.fen(8,'EULAR/ACR : des critères de classification de 2017, distincts du diagnostic',[
 ('Les critères EULAR/ACR sont utilisés lorsqu’aucune meilleure explication ne rend compte des symptômes et des signes.','crit-table'),
 ('Ils combinent l’âge, la faiblesse objectivée, la peau, la déglutition, les enzymes, un anticorps et certaines données de biopsie.','crit-table'),
 ('Chaque variable possède un poids ; le calcul dépend notamment de la disponibilité d’une biopsie musculaire.','crit-table+crit-cutoffs'),
 ('La probabilité calculée concerne une myopathie inflammatoire idiopathique avant la classification des sous-groupes.','crit-subtypes'),
 ('Le seuil de 55 % est proposé pour classer une myopathie inflammatoire probable.','crit-cutoffs'),
 ('Le terme de classification certaine correspond à une probabilité d’au moins 90 % dans cette méthode.','crit-cutoffs'),
 ('Ces catégories ne dispensent pas de l’exclusion d’autres causes et ne représentent pas un ordre de traitement automatique.','crit-table+rms-class')])
 c.tab(8,'Variables de la classification : leur définition clinique reste nécessaire',['Domaine','Variables recherchées','Interprétation et limite'],[
  [('L’âge intervient dans le calcul.','crit-table'),('Les catégories distinguent un début entre 18 et moins de 40 ans ou à partir de 40 ans.','crit-table'),('L’âge apporte un poids et ne suffit pas à établir une dermatomyosite.','crit-table')],
  [('La force est documentée objectivement.','crit-table'),('Les membres supérieurs et inférieurs, la prédominance proximale et les fléchisseurs du cou sont évalués.','crit-table'),('Une plainte de fatigue seule ne remplace pas ces variables.','crit-table+rms-clin')],
  [('Les manifestations cutanées sont décrites selon leur morphologie.','crit-table'),('Le calcul distingue l’héliotrope, les papules de Gottron et le signe de Gottron.','crit-table'),('Une lésion en relief ne reçoit pas le même nom qu’une macule non palpable.','crit-table')],
  [('La déglutition apporte une variable clinique.','crit-table'),('Une dysphagie ou une anomalie objective de motilité œsophagienne est recherchée.','crit-table'),('Son évaluation de gravité demeure prioritaire sur son poids statistique.','bsr-xi+crit-table')],
  [('Le laboratoire comprend les enzymes et les anticorps anti-Jo-1.','crit-table'),('Les enzymes sont interprétées par rapport à la limite supérieure du laboratoire.','crit-table'),('Les autres anticorps de dermatomyosite restent utiles au phénotypage sans être assimilés à cette variable.','bsr-vi+fr-definition+crit-table')],
  [('La biopsie peut contribuer par plusieurs caractères histologiques.','crit-table'),('Le calcul considère notamment les infiltrats, l’atrophie périfasciculaire et les vacuoles bordées.','crit-table'),('Le pathologiste interprète ces aspects dans le diagnostic différentiel des myopathies.','rms-hist')]
 ])
 c.tab(8,'Seuils publiés et usage exact',['Catégorie de classification','Sans biopsie musculaire','Avec biopsie musculaire'],[
  [('Une probabilité d’au moins 55 % permet la classification probable.','crit-cutoffs'),('Le seuil de score est de 5,5 dans le modèle sans biopsie.','crit-cutoffs'),('Le seuil de score est de 6,7 dans le modèle avec biopsie.','crit-cutoffs')],
  [('Une probabilité d’au moins 90 % définit la catégorie certaine.','crit-cutoffs'),('Le score correspondant est d’au moins 7,5.','crit-cutoffs'),('Le score correspondant est d’au moins 8,7.','crit-cutoffs')],
  [('Une probabilité entre 50 % et moins de 55 % est qualifiée de possible.','crit-cutoffs'),('Cette catégorie ne remplace pas une réévaluation clinique.','rms-class+crit-cutoffs'),('L’échantillon et les caractéristiques de la biopsie doivent rester cohérents avec la clinique.','rms-hist+crit-table')]
 ])
 c.block(8,'Ce qui ne suffit pas',[
 ('Une élévation des CK peut avoir plusieurs causes et ne constitue pas à elle seule un diagnostic de dermatomyosite.','rms-bilan+rms-clin'),
 ('Un taux de CK peu élevé ou normal ne suffit pas non plus à exclure une forme amyopathique à risque systémique.','fr-mda5'),
 ('Un anticorps de panel isolé n’est pas une confirmation autonome ; les faux positifs exigent une interprétation clinico-biologique.','fr-anticorps'),
 ('La classification reconnaît imparfaitement certains sous-groupes récents ; la caractérisation spécialisée conserve donc son importance.','crit-subtypes'),

 ])
 c.block(9,'9.a La référence diagnostique est intégrée, avec histologie selon la constellation',[
 ('La démarche des HUG associe anamnèse, examen, biologie, autoanticorps, imagerie, électroneuromyographie et biopsie selon le cas.','rms-conclusion'),
 ('La biopsie permet de reconnaître une distribution inflammatoire et de distinguer plusieurs formes de myopathie.','rms-hist'),
 ('Elle n’est cependant pas une obligation uniforme devant chaque présentation cutanéomusculaire typique de dermatomyosite.','rms-hist'),
 ('Le choix d’un prélèvement est discuté avec l’équipe spécialisée et peut être orienté par l’imagerie musculaire.','rms-bilan+rms-hist'),
 ('Une biopsie cutanée est recommandée dans le cadre décrit par les critères lorsqu’il existe des lésions évocatrices sans symptômes musculaires.','crit-peau+fr-definition'),
 ('L’interprétation finale reste une confrontation entre clinique et examens, plutôt qu’un résultat histologique détaché du patient.','rms-hist+rms-conclusion')])
 c.tab(9,'9.b Première intention : question, prescription et lecture',['Examen demandé','Question clinique','Lecture et conséquence'],[
  [('La CK et les autres enzymes musculaires utiles sont dosées.','rms-bilan'),('Le bilan recherche une atteinte musculaire biologique.','rms-bilan'),('Une élévation s’interprète avec la force et le contexte ; sa hauteur ne mesure pas seule la gravité.','rms-bilan')],
  [('Une numération complète, la créatinine et les électrolytes complètent la biologie.','rms-bilan'),('Le bilan explore des causes de faiblesse et prépare les décisions thérapeutiques.','rms-bilan'),('Une anomalie rénale ou électrolytique modifie les investigations et les précautions de traitement.','rms-bilan+oc-warn')],
  [('La TSH et le bilan hépatique sont demandés dans le bilan de base.','rms-bilan'),('Une cause endocrinienne et le contexte viscéral sont recherchés.','rms-clin+rms-bilan'),('La faiblesse n’est pas attribuée d’emblée à une myosite sur les seuls symptômes proximaux.','rms-clin')],
  [('Les marqueurs inflammatoires et les autoanticorps sont intégrés au bilan.','rms-bilan'),('La présentation systémique et le phénotype immunologique sont caractérisés.','bsr-vi+rms-bilan'),('Un immunoblot est interprété dans son contexte ; ses titres ne servent pas à suivre l’activité.','bsr-vi')],
  [('Les examens microbiologiques sont orientés par la suspicion et le traitement envisagé.','rms-bilan'),('Le bilan recherche notamment des infections pertinentes avant immunosuppression.','rms-bilan'),('Les sérologies et le dépistage de tuberculose latente sont adaptés à cette indication.','rms-bilan')],
  [('L’ECG, la troponine I et l’échocardiographie sont considérés pour le bilan cardiaque adulte.','bsr-x'),('Une participation cardiaque peut accompagner la maladie.','bsr-x'),('Une anomalie est confrontée à la clinique et peut conduire à une IRM cardiaque.','bsr-x')]
 ])
 c.fen(9,'Valeur normale et unités : ne pas généraliser la valeur d’une vignette',[
 ('Le compte rendu enzymatique doit fournir sa limite supérieure de référence, puisque les critères comparent le résultat à cette limite.','crit-table'),
 ('La CK peut être exprimée en U/L dans les données cliniques citées ; le résultat est lu avec la référence du laboratoire.','esp-labo+crit-table'),
 ('La valeur d’un patient ou d’une série n’est pas utilisée comme norme universelle pour tous les patients.','crit-table+esp-adulte'),
 ('La persistance d’une faiblesse avec une CK peu élevée demande donc une analyse clinique plutôt qu’un classement automatique en rémission.','rms-bilan+rms-fonction'),
 ('La troponine I est préférée à la troponine T pour le dépistage cardiaque dans la recommandation britannique.','bsr-x'),
 ('La troponine T peut être exprimée par du muscle squelettique en régénération, ce qui crée une ambiguïté d’origine.','bsr-x')])
 c.block(9,'9.b Imagerie musculaire : préciser la question avant la demande',[
 ('L’IRM musculaire recherche un œdème, des modifications tissulaires et un site pertinent pour une biopsie éventuelle.','rms-bilan+cedef-irm'),
 ('La demande précise les groupes symptomatiques et la question de myopathie inflammatoire, afin que l’exploration soit reliée à la topographie clinique.','pnds-examen+rms-bilan'),
 ('Les séquences T2 sensibles à l’eau et STIR peuvent montrer un hypersignal intramusculaire diffus ou multifocal.','cedef-irm'),
 ('Une séquence T1 et l’analyse morphologique apportent des informations complémentaires sur les tissus examinés.','cedef-irm'),
 ('Un hypersignal n’est pas spécifique d’une dermatomyosite ; l’imagerie accompagne la démarche diagnostique et la sélection du prélèvement.','cedef-irm+rms-bilan'),
 ])
 c.fen(9,'Bilan pulmonaire : scanner et fonctions respiratoires sont complémentaires',[
 ('Les recommandations ERS/EULAR préconisent le dépistage par scanner thoracique de haute résolution chez les patients à risque de pneumopathie interstitielle.','ers-depistage'),
 ('Les facteurs décrits comprennent une forme cliniquement amyopathique, certains anticorps, les mains de mécanicien et une arthrite.','ers-depistage'),
 ('L’anti-MDA5 et les anticorps antisynthétases font notamment partie des marqueurs pris en compte.','ers-depistage'),
 ('Les explorations fonctionnelles respiratoires ne remplacent pas le scanner pour le dépistage de l’atteinte interstitielle.','ers-hrct'),
 ('L’exploration de la capacité vitale et de la diffusion complète l’appréciation fonctionnelle et le suivi.','bsr-iii+ers-cadence'),
 ('Une suspicion d’aggravation conduit à renouveler l’évaluation plutôt qu’à attendre l’échéance planifiée.','ers-cadence+ers-suivi'),
 ('La prise en charge est coordonnée avec des pneumologues expérimentés dans les pneumopathies interstitielles.','bsr-iii')])
 c.tab(9,'9.c Alternatives et précautions adaptées à la situation',['Situation','Décision d’exploration','Précaution qui reste nécessaire'],[
  [('Une grossesse modifie la discussion d’une exploration irradiant le patient.','radio-grossesse'),('L’OFSP recommande de différer si la situation médicale le permet et de justifier un examen nécessaire.','radio-grossesse'),('La grossesse est signalée avant l’examen ; une urgence justifiée ne reçoit pas un refus automatique.','radio-grossesse')],
  [('Un enfant nécessite une justification spécifique et une technique adaptée.','radio-enfant'),('Le bénéfice attendu et les alternatives pertinentes sont discutés avant l’examen irradiant.','radio-enfant'),('Le parcours reste pédiatrique et le bilan est relié au phénotype de dermatomyosite juvénile.','bsr-v+radio-enfant')],
  [('Un DFGe inférieur à 30 mL/min/1,73 m² impose des précautions si un contraste iodé intraveineux est envisagé.','esur-rein'),('L’ESUR propose de considérer une méthode sans contraste iodé chez le patient à risque.','esur-rein'),('La nécessité d’une injection et la prévention rénale sont décidées avec l’équipe d’imagerie.','esur-rein')],
  [('Un antécédent de réaction au produit de contraste doit être précisé.','esur-reaction'),('La stratégie peut retenir un autre examen ou un autre produit après appréciation spécialisée.','esur-reaction'),('Le compte rendu antérieur et le produit impliqué sont confrontés à la nouvelle indication.','esur-reaction')],
  [('Une IRM impossible ne termine pas l’exploration de la myopathie.','rms-bilan+rms-hist'),('L’examen, la biologie, l’électroneuromyographie et la biopsie restent discutés selon la constellation.','rms-conclusion'),('Ces examens répondent à des questions différentes et ne sont pas présentés comme des remplaçants strictement équivalents.','rms-bilan+rms-hist')]
 ])
 c.fen(9,'Le contraste n’est prescrit que pour une question qui le nécessite',[
 ('Les séquences musculaires sensibles à l’eau font partie de l’exploration décrite ; leur présence ne constitue pas une prescription automatique de gadolinium.','cedef-irm'),
 ('Une exploration cardiaque ou tumorale injectée éventuelle demande une décision d’imagerie adaptée à sa propre question.','bsr-x+imacs-screen+esur-rein'),
 ('Pendant la grossesse, l’ESUR réserve le gadolinium à une indication très forte et à la plus faible dose possible d’un agent macrocyclique.','esur-grossesse'),
 ('Chez une patiente enceinte ou allaitante avec insuffisance rénale, ce guide demande de ne pas administrer de gadolinium.','esur-grossesse'),
 ('Ces précautions concernent le produit et le terrain ; elles ne sont pas transformées en interdiction de tout bilan musculaire ou clinique.','esur-grossesse+rms-conclusion'),
 ('La discussion d’une injection est donc séparée de la décision de rechercher une dermatomyosite et ses complications.','rms-conclusion+esur-rein')])
 c.block(9,'9.d Seconde intention : étiologie, tissus et organes',[
 ('L’électroneuromyographie complète le bilan lorsqu’une localisation neurologique ou jonctionnelle doit être distinguée d’une atteinte musculaire.','rms-bilan'),
 ('La biopsie peut reconnaître une atrophie périfasciculaire, une nécrose ou des éléments de myosite à inclusions selon la maladie en cause.','rms-hist'),
 ('Les lésions cutanées et la présentation amyopathique peuvent conduire à une discussion dermatologique et histologique spécifique.','crit-peau+fr-definition'),
 ('L’évaluation spécialisée de déglutition précise le mécanisme et les moyens de réduire le risque d’inhalation.','bsr-xi'),
 ('Le dépistage tumoral adulte est organisé selon le risque IMACS, en complément des programmes habituels appropriés.','imacs-risk+imacs-screen'),

 ])
 c.block(10,'Un parcours décisionnel relie chaque constat à une action',[
 ('Si la respiration, la déglutition ou le cœur sont menacés, alors la prise en charge urgente des fonctions concernées précède le bilan différé.','pnds-severite'),
 ('Si la présentation est stable, alors l’examen précise la distribution de faiblesse et recherche les signes cutanés caractéristiques.','rms-clin+pnds-examen'),
 ('Si un héliotrope ou des lésions de Gottron accompagnent un tableau compatible, alors la dermatomyosite devient une hypothèse structurée.','crit-table+fr-definition'),
 ('Si la faiblesse reste atypique ou sans peau caractéristique, alors les autres myopathies, les causes endocrines et les localisations neurologiques sont explorées.','rms-clin+rms-hist'),
 ('Si un panel d’anticorps revient positif, alors son résultat est confronté à la clinique et au bilan d’organes.','bsr-vi+fr-anticorps'),
 ('Si la CK est normale mais le phénotype est évocateur, alors le bilan se poursuit au lieu d’exclure une forme amyopathique.','fr-mda5'),
 ('Si l’incertitude persiste, alors l’imagerie, l’électroneuromyographie et la biopsie sont discutées avec l’équipe spécialisée.','rms-conclusion')])
 c.fen(10,'Trois embranchements après la reconnaissance du phénotype',[
 ('Si le profil comporte un risque pulmonaire, alors le scanner thoracique et les explorations fonctionnelles sont organisés selon les recommandations ERS/EULAR.','ers-depistage+ers-hrct'),
 ('Si le patient adulte présente des facteurs de risque tumoral, alors le niveau de dépistage est défini selon IMACS.','imacs-risk+imacs-screen'),
 ('Si une dysphagie est présente, alors la sécurité nutritionnelle et la déglutition sont évaluées avec les professionnels concernés.','bsr-xi'),
 ('Si une atteinte cardiaque est suspectée, alors la troponine I et les explorations cardiaques appropriées complètent l’évaluation.','bsr-x'),
 ('Si une immunosuppression est envisagée, alors le terrain, les infections pertinentes et les notices des spécialités sont vérifiés avant prescription.','rms-bilan+sp-ci+im-ci+oc-ci'),
 ('Si l’évolution n’est pas favorable, alors activité, séquelles, adhésion et complications thérapeutiques sont réexaminées avant de modifier la stratégie.','pnds-suivi+rms-fonction+bsr-i')])
 c.tab(10,'La décision de traitement reste reliée à son objectif',['Situation évaluée','Décision spécialisée','Contrôle associé'],[
  [('Une inflammation musculaire active nécessite un contrôle de maladie.','bsr-i'),('Une induction par glucocorticoïde et une stratégie d’épargne sont discutées.','bsr-i'),('La force et les autres domaines cliniques sont suivis.','bsr-i')],
  [('Une atteinte interstitielle pulmonaire est confirmée.','ers-traitement'),('L’immunosuppression est organisée avec l’équipe pulmonaire et peut être combinée.','ers-traitement+ers-association'),('La fonction respiratoire et l’imagerie surveillent le risque de progression.','ers-cadence+ers-suivi')],
  [('Une myosite ou une atteinte cutanée demeure réfractaire.','bsr-i+bsr-ii'),('Des immunoglobulines ou d’autres options spécialisées sont considérées selon le domaine atteint.','bsr-i+bsr-ii'),('L’efficacité et la tolérance sont évaluées avec les limites de la notice retenue.','oc-dose+oc-warn')],
  [('La récupération fonctionnelle reste incomplète malgré une moindre activité.','rms-fonction'),('La réadaptation et l’analyse des séquelles complètent le traitement de maladie.','bsr-xii'),('Les activités concrètes et les besoins sociaux sont réévalués.','bsr-xii+ai-reintegration')]
 ])

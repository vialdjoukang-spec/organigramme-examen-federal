from rendu import outils

p,c,h,w,table,liste,save=outils(8)
a=w('Consensus ENMC2025 : critères de l’épisode d’effort',[
('Le consensus publié en2025 retient une augmentation rapide des CK supérieure à10000UI/L dans la forme d’effort.',['e12']),
('La présentation comporte une douleur musculaire, une faiblesse ou un gonflement ; les trois manifestations ne sont pas exigées simultanément.',['e12']),
('La CK atteint un maximum environ1–4jours après l’événement et revient au niveau de base après1–2semaines de repos.',['e12']),
('La normalisation constitue un élément d’évolution attendu ; elle ne peut pas être exigée pour orienter et traiter une urgence au premier contact.',['e12','e13']),
('Une CK préexistante élevée dans une maladie neuromusculaire impose la comparaison au niveau de base, avec le repère5–10fois celui-ci.',['e12'])])
b=w('Seuil diagnostique et seuil de danger ne se confondent pas',[
('Les études et les synthèses ont utilisé différentes définitions ; le rapport ENMC distingue explicitement effort et causes non liées à l’effort.',['e01','e12']),
('La revue SRLF2026, consacrée à la réanimation et aux causes multiples, emploie une CK supérieure à5fois la limite normale pour le diagnostic biologique.',['s02']),
('Ces cadres de définition sont conservés avec leur population ; une limite générale n’est pas substituée silencieusement au consensus sur l’effort.',['s02','e12']),
('Une valeur élevée peut aussi suivre un exercice chez une personne saine, tandis qu’une complication clinique peut nécessiter des soins avant le pic enzymatique.',['e02','e12','e13']),
('Le risque rénal est donc apprécié séparément avec la créatinine, les électrolytes, la diurèse et le terrain.',['e09','e13'])])
d=w('McMahon : outil pronostique, pas preuve étiologique',[
('Le score McMahon estime le risque de recours à l’épuration rénale ou de décès chez des personnes hospitalisées pour rhabdomyolyse.',['e09','s10']),
('Il combine l’âge, le sexe, la cause et des paramètres initiaux : créatinine, calcium, phosphate, bicarbonate et CK.',['e09','s10']),
('La cause d’effort appartient à une catégorie de risque plus faible dans le modèle ; les autres données restent cependant nécessaires.',['e09']),
('Le résultat aide la décision d’hospitalisation et de surveillance, sans remplacer les signes rouges ou la recherche d’un syndrome des loges.',['e13','b01']),
('Il ne désigne pas le mécanisme génétique et ne remplace pas les caractéristiques RHABDO pour sélectionner le bilan spécialisé.',['e06','e14'])])
s=h('La confirmation associe l’épisode clinique et la biologie')
s+=p('Le '+a+' fournit une définition contextualisée de la rhabdomyolyse d’effort et la distingue des seules conséquences enzymatiques d’un exercice.','e12','e02')
s+=p('Le diagnostic initial repose sur l’histoire, les symptômes et les CK, puis l’évolution permet de confirmer la cohérence de la cinétique.','e12')
s+=p('Une myoglobinurie documentée constitue un argument diagnostique majeur dans le consensus ; une bandelette positive isolée n’identifie toutefois pas précisément le pigment.','e12','r08')
s+=table(['Élément du consensus','Interprétation','Décision associée'],[
['Une douleur, une faiblesse ou une tuméfaction musculaire accompagne l’épisode.'+c('e12'),'Le syndrome clinique est compatible, sans exiger une triade complète.'+c('e12','r07'),'Les CK et le bilan de complications sont confrontés à la chronologie.'+c('e12','s02')],
['La CK augmente rapidement et dépasse10000UI/L dans la forme d’effort.'+c('e12'),'Le seuil appartient à la définition ENMC2025 de ce contexte.'+c('e12'),'La créatinine, les électrolytes et la diurèse déterminent séparément le risque immédiat.'+c('e09','e13')],
['Le maximum survient environ1–4jours après le déclenchement.'+c('e12'),'Un premier prélèvement peut précéder le pic.'+c('e12'),'La surveillance biologique est répétée selon l’évolution clinique et la gravité.'+c('s02','s04')],
['Le niveau de base est retrouvé après1–2semaines de repos dans l’évolution décrite.'+c('e12'),'Une persistance inhabituelle fait réexaminer l’étiologie et le suivi.'+c('e06','e14'),'La crise est réévaluée à distance ; le délai ne diffère pas le traitement d’une complication aiguë.'+c('e13','e14')],
['Une maladie neuromusculaire préexistante peut élever la CK habituelle.'+c('e12'),'Le repère est une élévation supérieure à5–10fois le niveau de base.'+c('e12'),'Le résultat est rapproché des valeurs antérieures et du phénotype connu.'+c('e12','e14')]])
s+=p('La fenêtre '+b+' permet d’interpréter les divergences des anciennes définitions sans créer un seuil universel de sécurité.','e01','e13','s02')
s+=h('Les outils répondent à des questions distinctes')
s+=p('Le '+d+' appartient à la stratification pronostique ; la présence d’une urgence clinique conserve la priorité sur tout calcul.','e09','e13')
s+=p('Les caractéristiques RHABDO orientent la recherche d’une prédisposition ; une seule caractéristique peut motiver la discussion génétique spécialisée.','e06','e14')
s+=p('Une myopathie n’est pas confirmée par un simple panel génétique anormal : les résultats sont confrontés aux manifestations et aux autres examens.','e03')
s+=p('La biopsie ne constitue pas le test de confirmation courant d’un épisode simple ; elle intervient selon une suspicion inflammatoire ou un bilan spécialisé ultérieur.','e08','s02')
s+=p('La gravité est décrite par les complications réellement présentes, le terrain et la tendance biologique, plutôt que par une catégorie construite à partir des seules CK.','e09','e13','s04')
save(s)

p,c,h,w,table,liste,save=outils(9)
a=w('CK : prescrire le dosage et lire sa cinétique',[
('Le dosage sanguin des CK totales est demandé dans un contexte d’atteinte musculaire suspectée ; l’heure du prélèvement et du déclenchement sont consignées.',['r08','e12']),
('Le résultat enUI/L est comparé à la référence du laboratoire et aux valeurs antérieures lorsqu’une maladie musculaire est connue.',['e12','d02']),
('Un effort récent peut modifier fortement les valeurs ; il doit donc figurer dans l’interprétation d’une hyperCKémie.',['d02','e02']),
('Le contrôle à distance d’une hyperCKémie isolée peut nécessiter une période de repos, tandis que l’urgence symptomatique reçoit d’emblée son bilan.',['d02','e13']),
('Une baisse de CK ne dispense pas de suivre la fonction rénale, les urines et les paramètres métaboliques.',['s02','s04'])])
b=w('Créatinine, électrolytes et équilibre acido-basique',[
('La créatinine sanguine est rapprochée de la valeur de base et de la diurèse ; la tendance contribue à identifier une atteinte rénale aiguë.',['s02','s04']),
('Le bilan dose notamment potassium, sodium, calcium et phosphate ; les bicarbonates ou les gaz du sang évaluent le retentissement acido-basique.',['s02','d02','e09']),
('La kaliémie est interprétée avec sa vitesse de variation et l’électrocardiogramme ; une urgence peut être documentée au gaz du sang en attendant le laboratoire.',['k01','s11']),
('Le calcium et le phosphate sont lus ensemble, car la phase initiale et la récupération n’entraînent pas les mêmes risques.',['s08']),
('Les résultats rénaux et métaboliques guident la surveillance et les apports hydriques, au-delà de la valeur enzymatique musculaire.',['s04'])])
d=w('Urines : bandelette, sédiment et quantité',[
('La bandelette urinaire recherche une réaction pour le sang ; le sédiment précise la présence ou l’absence d’érythrocytes.',['r08']),
('Une réaction positive sans érythrocytes oriente vers un pigment libre, mais ne distingue pas la myoglobine de l’hémoglobine.',['r08']),
('L’histoire musculaire et la CK aident à interpréter ce résultat ; la couleur seule ne quantifie pas la gravité rénale.',['r08','e09']),
('La quantité d’urines est suivie parallèlement aux apports, au poids et à la fonction rénale.',['s04']),
('Une anurie persistante ou des signes de surcharge font réévaluer immédiatement la stratégie de remplissage et l’indication d’épuration.',['s04','s09'])])
e=w('Électrocardiogramme et monitorage cardiaque',[
('L’électrocardiogramme, abrégé ECG, recherche une conséquence électrique de l’hyperkaliémie et complète son dosage.',['k01']),
('Le guide UKKA recommande un ECG à12dérivations chez les personnes hospitalisées avec une kaliémie≥6,5mmol/L.',['k01']),
('Le monitorage continu concerne cette hyperkaliémie sévère, les signes électriques et certaines valeurs entre6,0et6,4mmol/L avec risque accru.',['k01']),
('La progression attendue et l’état clinique modifient la surveillance ; l’avis rénal ou de réanimation est sollicité en cas de menace vitale.',['k01','k04']),
('Un contrôle biologique rapproché évalue la réponse et un éventuel rebond après les premières mesures.',['k03'])])
f=w('Imagerie musculaire et biopsie : indications ciblées',[
('Une imagerie de routine n’est pas indiquée dans le bilan initial d’un épisode musculaire de rhabdomyolyse.',['r08']),
('L’imagerie par résonance magnétique peut localiser une atteinte musculaire et aider le bilan d’une myopathie ou la sélection d’un site de biopsie.',['r08','d04']),
('Le signal d’œdème est sensible à une anomalie musculaire mais ne désigne pas régulièrement une cause unique.',['d04']),
('Une biopsie précoce se discute si une myopathie inflammatoire est suspectée ; la nécrose aiguë peut compliquer l’analyse d’autres causes.',['e08','s02']),
('Le consensus envisage une biopsie après plus de8semaines dans les situations non résolues qui nécessitent un complément diagnostique.',['e14']),
('La mesure de pression compartimentale relève d’une autre question urgente ; l’IRM ne doit pas différer une décompression déjà indiquée.',['b01'])])
g=w('Alternatives et sécurité d’un examen avec contraste',[
('La biologie et l’évaluation clinique constituent le bilan initial de la rhabdomyolyse ; une injection de contraste n’est pas un préalable à sa confirmation.',['r08','s02']),
('Lorsqu’une autre indication conduit à une IRM injectée pendant la grossesse, ESUR2026 exige une indication très forte et une quantité minimale de macrocyclique.',['im1']),
('La règle générale de poursuite de l’allaitement après un macrocyclique est distincte du cas maternel avec atteinte rénale.',['im2','im7']),
('Chez la mère enceinte ou allaitante avec atteinte rénale, ESUR interdit l’administration d’un produit de contraste à base de gadolinium.',['im7']),
('Une atteinte rénale sévère, une réaction antérieure ou l’âge pédiatrique impose une discussion spécifique de l’indication et du protocole radiologique.',['im3','im5','im6'])])
s=h('9.a La confirmation biologique est confrontée au tableau clinique')
s+=p('L’examen décisif initial est le dosage des CK, interprété avec les manifestations et la chronologie ; une imagerie systématique n’est pas nécessaire.','r08','e12')
s+=p('La fenêtre '+a+' précise la prescription et la différence entre l’évaluation aiguë symptomatique et l’étude à distance d’une hyperCKémie isolée.','e12','d02','e13')
s+=p('Le bilan doit reconnaître la complication en parallèle de la lésion, car une insuffisance rénale ou une hyperkaliémie peut déterminer la priorité thérapeutique.','s02','s11')
s+=h('9.b Les premières demandes couvrent muscle, rein, électrolytes et urines')
s+=p('Les '+b+' sont demandés avec les CK ; les prélèvements et les contrôles sont adaptés à la gravité et à leur vitesse d’évolution.','s02','s04')
s+=p('Le recueil des '+d+' apporte une information complémentaire, sans faire de la pigmenturie une condition obligatoire du diagnostic.','r07','r08')
s+=p('L’'+e+' est organisé selon la kaliémie, les anomalies électriques et la possibilité d’une augmentation rapide.','k01')
s+=table(['Résultat et unité','Signification','Conduite'],[
['La CK est rapportée enUI/L et comparée à sa référence de laboratoire.'+c('r08','d02'),'La hausse peut correspondre à une lésion, une réponse postexercice ou une valeur de base déjà élevée.'+c('e02','e12'),'La clinique, les antériorités et la cinétique sont rapprochées du résultat.'+c('e12')],
['La créatinine est interprétée avec son antériorité ; la diurèse est mesurée.'+c('s02','s04'),'Une hausse ou une baisse des urines peut signaler une agression rénale.'+c('s02'),'La volémie, le bilan métabolique et l’indication d’avis néphrologique sont réévalués.'+c('s04','s09')],
['La kaliémie atteint≥6,5mmol/L.'+c('k01'),'Elle appartient au groupe nécessitant une surveillance électrique continue.'+c('k01'),'L’ECG, le monitorage et le circuit urgent de traitement sont mis en place.'+c('k01','k04')],
['Le potassium est entre6,0et6,4mmol/L et la personne est malade ou une hausse rapide est prévue.'+c('k01'),'Le contexte augmente le risque malgré une valeur sous le seuil du groupe sévère.'+c('k01'),'Le monitorage continu est également organisé selon la recommandation britannique.'+c('k01')],
['Le calcium diminue tandis que le phosphate augmente.'+c('s08'),'La lyse et les dépôts phosphocalciques peuvent expliquer ces anomalies.'+c('s08'),'La correction calcique dépend des symptômes ou d’une indication électrique, sans supplémentation automatique.'+c('s08')],
['Les urines réagissent pour le sang sans érythrocytes au sédiment.'+c('r08'),'Un pigment libre est probable dans le contexte compatible.'+c('r08'),'Le résultat est confronté aux CK et à l’histoire ; la fonction rénale est évaluée séparément.'+c('r08','s02')],
['Le sodium et le chlorure sont dosés enmmol/L pendant la perfusion.'+c('aips-n6','aips-n12'),'La notice cite des concentrations plasmatiques physiologiques de137–147pour le sodium et94–111pour le chlorure.'+c('aips-n12'),'Ces repères de notice sont confrontés aux références locales ; l’équilibre hydro-électrolytique et acido-basique guide les apports.'+c('aips-n6')]])
s+=p('Dans une forme sévère, le bilan d’hémostase recherche une coagulation intravasculaire disséminée ; les examens étiologiques suivent les autres manifestations observées.','s02')
s+=p('Les transaminases peuvent augmenter avec une atteinte musculaire ; leur présence est interprétée avec l’ensemble du tableau et le bilan clinique.','s02')
s+=h('9.c Les situations particulières modifient un examen, pas la priorité clinique')
s+=p('La fenêtre '+g+' sépare la nécessité du bilan musculaire de la sécurité d’une éventuelle exploration radiologique complémentaire.','r08','im7')
s+=table(['Situation','Adaptation de l’exploration','Décision'],[
['Une grossesse est connue.','Le bilan clinique et biologique reste prioritaire ; l’IRM injectée répond à une autre indication qui doit être très forte.'+c('r08','s02','im1'),'La discussion radiologique suit ESUR et tient compte de la fonction rénale maternelle.'+c('im1','im7')],
['La mère enceinte ou allaitante présente une atteinte rénale.','Le gadolinium ne doit pas être administré dans ce contexte maternel.'+c('im7'),'Une stratégie radiologique adaptée est choisie ; l’interdiction porte sur ce contraste et non sur le dosage biologique.'+c('im7','r08')],
['Le débit de filtration glomérulaire estimé est inférieur à30mL/min.','Le rapport bénéfice-risque de certains contrastes dépend de l’agent et de l’indication ; la règle maternelle spécifique reste applicable.'+c('im3','im7'),'Le radiologue sélectionne le protocole approprié ; l’urgence rénale et les apports sont évalués séparément.'+c('im3','s04')],
['Une réaction antérieure est rapportée comme une « allergie à l’iode ».','L’histoire consigne le produit exact, le type de contraste, la voie et la réaction observée.'+c('im6'),'Le protocole dépend de cette histoire précise et de l’utilité réelle d’un contraste.'+c('im6','im4')],
['Un enfant nécessite une exploration injectée.','La sécurité et les quantités dépendent de l’âge et du poids, selon les recommandations pédiatriques.'+c('im5'),'L’équipe pédiatrique et radiologique adapte l’examen ; les posologies adultes ne sont pas appliquées directement.'+c('im5')],
['Une IRM est impossible.','Le bilan d’un épisode aigu reste clinico-biologique ; la mesure de pression répond à la suspicion de loge.'+c('r08','b01'),'Le spécialiste sélectionne les autres examens nécessaires à l’étiologie sans différer une urgence chirurgicale.'+c('e14','b01')]])
s+=h('9.d La seconde intention recherche une cause sous-jacente')
s+=p('L’'+f+' intervient en fonction de la persistance, des récidives et de la suspicion inflammatoire ou neuromusculaire.','e08','e14','d04')
s+=p('Une suspicion de défaut d’oxydation lipidique conduit au profil des acylcarnitines et aux autres explorations métaboliques choisies par le spécialiste.','e04')
s+=p('Une glycogénose peut être explorée par un exercice non ischémique avec lactate et ammoniac, interprété dans le contexte clinique spécialisé.','e03','d03')
s+=p('L’épreuve ischémique peut provoquer une rhabdomyolyse dans certaines glycogénoses ; cette possibilité justifie le choix spécialisé du protocole.','d03')
s+=p('Les anticorps de myosite, la génétique, l’électrophysiologie et la biopsie sont sélectionnés selon le phénotype plutôt que demandés indistinctement après chaque effort.','d03','e08','e14')
save(s)

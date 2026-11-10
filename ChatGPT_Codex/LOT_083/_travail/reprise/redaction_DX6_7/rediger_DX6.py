from pathlib import Path
import json, html, re

B=Path(__file__).resolve().parent;D=B/'DX.6';F=D/'fragments';F.mkdir(exist_ok=True)
P=json.loads((D/'paquet.json').read_text());S={x['id']:x for x in P['passages']};C=json.loads((D/'contrat.json').read_text())
N=0;K=0
def start(n):
 global N,K
 N=n;K=0
def cite(ids):
 for i in ids:assert i in S,i
 return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'for i in ids)
def p(t,*ids):
 global K
 assert ids
 K+=1
 return f'<div class="p" id="dx6-p{N}-f{K}">'+html.escape(t)+cite(ids)+'</div>\n'
def h(t):return '<h4><em>'+html.escape(t)+'</em></h4>\n'
def rows(headers,data):
 return '<div class="t" style="overflow-x:auto"><table><thead><tr>'+''.join('<th>'+html.escape(x)+'</th>'for x in headers)+'</tr></thead><tbody>\n'+''.join('<tr>'+''.join('<td>'+p(t,*ids)+'</td>'for t,ids in row)+'</tr>\n'for row in data)+'</tbody></table></div>\n'
def w(key,title,paras):
 i=f'dx6-p{N}-{key}'
 return f'<button class="w" popovertarget="{i}">{html.escape(title)}</button><div class="fenetre" id="{i}" popover><h4>{html.escape(title)}</h4>\n'+''.join(p(t,*ids)for t,ids in paras)+'</div>\n'
def save(s):
 ids=list(dict.fromkeys(re.findall(r'href="#sb-([\w.\-:]+)"',s)))
 C['points'][str(N)]['citations_autorisees']=ids;P['points'][str(N)]=ids
 (F/f'p{N:02d}.html').write_text(s)
 print(N,len(s.encode()))

start(1)
s=h('Nommer les symptômes sans conclure trop tôt à leur cause')
s+=p('Le consensus de l’European Atherosclerosis Society de 2015 regroupe sous SAMS les plaintes musculaires survenant sous statine : douleur, faiblesse ou crampes.','eas-definition','eas-date')
s+=p('Ces symptômes sont classés avec ou sans élévation de la créatine kinase, abrégée CK ; leur association au médicament ne démontre pas sa responsabilité.','eas-definition')
s+=p('Le terme français retenu est « symptômes musculaires associés aux statines » ; une myalgie désigne plus précisément une douleur ressentie dans le muscle.','eas-definition','dgn-definition')
s+=p('Cette monographie part d’une plainte sans myopathie grave établie ; une faiblesse progressive ou une lyse musculaire ouvre une autre filière.','dgn-statine','dgn-imnm','rhabdo-e13')
s+=p('Une CK normale reste compatible avec des symptômes, tandis qu’une valeur augmentée demande une interprétation clinique et une recherche d’autres causes.','eas-definition','dgn-ck')
s+=p('La chronologie, l’examen et l’évolution après modification encadrée du traitement construisent donc une probabilité clinique, sans test unique de causalité.','eas-definition','eas-imputabilite')
s+=w('vocabulaire','Myalgie, déficit moteur et myopathie : trois informations distinctes',[
('La myalgie renseigne une perception douloureuse ; elle peut être diffuse ou localisée et ne constitue pas une mesure de force.',['dgn-definition','dgn-examen']),
('Une faiblesse rapportée est explorée par les activités quotidiennes, puis par un examen comparatif et une cotation segmentaire.',['cen-myogene-clinique','cen-force']),
('Un déficit moteur objectivé est une constatation différente d’une douleur qui gêne l’effort ; il fait rechercher une atteinte musculaire ou neurologique.',['cen-force','cen-myogene-clinique']),
('La myopathie désigne une maladie du muscle lui-même ; tous les symptômes sous statine ne répondent pas à cette définition.',['cen-myogene-definition','eas-definition']),
('Une petite élévation des CK peut suivre un effort, tandis que des symptômes peuvent apparaître avec des CK dans la référence du laboratoire.',['dgn-ck','eas-definition']),
('Le nom de SAMS conserve ainsi l’incertitude étiologique tant que la confrontation clinique et médicamenteuse reste incomplète.',['eas-definition','eas-imputabilite'])])
s+=rows(['Présentation','Ce qui la caractérise','Ce qui change la démarche'],[
 [('Les symptômes simples peuvent associer douleurs ou crampes.',['eas-definition']),('Ils surviennent souvent sans forte élévation des CK ni parésie.',['dgn-statine']),('L’entretien et la recherche de facteurs associés précèdent une décision individualisée.',['eas-interactions'])],
 [('Une myopathie toxique peut produire une faiblesse douloureuse symétrique.',['dgn-toxique']),('Elle concerne particulièrement les muscles proximaux et peut régresser après l’arrêt.',['dgn-toxique']),('La statine est suspendue et la gravité musculaire, rénale et métabolique est évaluée.',['aips83-sortis-prudence','rhabdo-s02'])],
 [('La myopathie nécrosante auto-immune est une sortie spécialisée.',['dgn-imnm']),('La faiblesse proximale persiste ou progresse malgré le retrait de la statine.',['dgn-imnm']),('Les anticorps anti-HMGCR et le bilan neuromusculaire participent au diagnostic.',['dgn-imnm'])],
 [('Une hypothyroïdie peut expliquer ou favoriser des symptômes.',['dgn-thyroide','dgn-statine']),('Les mécanismes endocrinien et médicamenteux peuvent coexister.',['dgn-thyroide','dgn-statine']),('La fonction thyroïdienne est recherchée avant de fixer l’imputabilité.',['eas-interactions','mdx-diagnostic'])]])
s+=w('cadre','Une chronologie compatible augmente une probabilité',[
('L’EAS décrit typiquement des douleurs symétriques et proximales, intéressant notamment cuisses, fesses, mollets et dos.',['eas-definition']),
('Une apparition dans les 4–6 semaines après introduction est compatible, mais une survenue tardive reste possible.',['eas-definition']),
('Une augmentation de dose ou l’ajout d’un médicament interagissant peut aussi précéder le début des plaintes.',['eas-definition','eas-interactions']),
('L’amélioration après retrait et la réapparition lors d’une réexposition encadrée renforcent le lien, sans autoriser une réexposition après toute complication.',['eas-imputabilite','aips83-sortis-prudence']),
('La rhabdomyolyse et la suspicion de myopathie auto-immune demandent une stratégie spécialisée, distincte de l’essai de tolérance d’un symptôme léger.',['dgn-imnm','rhabdo-s03'])])
save(s)

start(2)
s=h('Mesurer les plaintes et leur imputabilité avec des dénominateurs distincts')
s+=p('Le cadre suisse mediX aborde l’intolérance musculaire dans la prise en charge de l’hyperlipidémie et recherche les facteurs qui modifient le choix du traitement.','mdx-sams','mdx-diagnostic')
s+=p('Le consensus EAS de 2015 rapporte des symptômes chez 7–29 % des patients dans des registres et études observationnelles.','eas-frequence','eas-date')
s+=p('Cette proportion concerne des plaintes associées à une exposition ; elle ne correspond pas à la fraction démontrée comme causée par la statine.','eas-frequence','eas-definition')
s+=p('La méta-analyse CTT publiée en 2022 compare les symptômes rapportés sous statine et sous placebo dans des essais en double aveugle.','ctt-methodes','ctt-date')
s+=p('Dans ces essais, les proportions de douleur ou de faiblesse rapportées sous statine et sous placebo restent proches, avec un petit excès attribuable au traitement.','ctt-resultats')
s+=p('L’excès absolu durant la première année est de 11 événements pour 1000 personnes-années ; cette mesure ne se confond pas avec les proportions cumulées.','ctt-resultats')
s+=p('La DGN de 2025 cite une incidence de myopathie de onze pour cent mille personnes-années avec la définition combinant symptômes et CK au moins dix fois la norme.','dgn-statine','dgn-date')
s+=p('Les définitions, la méthode d’observation et la sévérité diffèrent donc entre ces résultats ; ils ne doivent pas être additionnés.','dgn-statine','ctt-resultats','eas-definition')
s+=rows(['Chiffre publié','Population et définition','Année et portée'],[
 [('Le consensus rapporte une plage de 7–29 % de symptômes.',['eas-frequence']),('Les données viennent de registres et d’études observationnelles chez des personnes exposées.',['eas-frequence']),('La synthèse EAS date de 2015 ; elle ne fournit pas une fréquence nationale suisse.',['eas-date','eas-frequence'])],
 [('Durant la première année, la hausse relative des symptômes est de 7 % sous statine.',['ctt-resultats']),('Le critère est une douleur ou une faiblesse rapportée dans les essais contre placebo.',['ctt-resultats']),('CTT publie cette méta-analyse en 2022 ; la différence évalue un effet de groupe.',['ctt-date','ctt-resultats'])],
 [('L’excès initial est de 11 événements pour 1000 personnes-années.',['ctt-resultats']),('Il concerne la première année, sans convertir ce taux en risque individuel certain.',['ctt-resultats']),('Cette estimation CTT de 2022 se distingue des symptômes de toute origine.',['ctt-date','ctt-resultats'])],
 [('La DGN rapporte onze cas de myopathie pour cent mille personnes-années.',['dgn-statine']),('La définition exige des symptômes et des CK au moins dix fois la norme.',['dgn-statine']),('Le guide de 2025 reprend cette estimation ; elle ne décrit pas tous les SAMS.',['dgn-date','dgn-statine'])]])
s+=w('causalite','Les essais aident à interpréter la fréquence, pas à nier une plainte',[
('La comparaison randomisée montre un petit excès de douleurs principalement légères attribuable au traitement dans la population étudiée.',['ctt-interpretation']),
('La plupart des symptômes rapportés sous statine dans ces essais n’étaient pas imputables à la statine.',['ctt-interpretation']),
('Une douleur reste donc évaluée pour sa topographie, sa gravité et les causes concurrentes, même lorsque le lien pharmacologique paraît peu probable.',['eas-definition','eas-interactions']),
('L’observation individuelle ne peut pas reproduire automatiquement une fraction attribuable calculée sur l’ensemble des participants.',['ctt-resultats','eas-definition']),
('Une suspicion de rhabdomyolyse ne se déduit pas de cette fréquence moyenne : elle impose le bilan de ses complications.',['rhabdo-s02','rhabdo-e13'])])
s+=w('terrain','Facteurs qui augmentent la vigilance',[
('La DGN cite notamment les fortes doses, les associations médicamenteuses, l’âge avancé et les comorbidités parmi les facteurs de risque.',['dgn-statine']),
('Une hypothyroïdie non traitée ou une insuffisance rénale modifie la vulnérabilité musculaire et doit être recherchée.',['dgn-statine','aips83-sortis-prudence']),
('L’effort récent augmente les CK et peut également fournir une cause indépendante de douleur.',['dgn-ck','eas-interactions']),
('L’enjeu est de réduire la souffrance et l’iatrogénie tout en préservant une prévention cardiovasculaire adaptée au risque.',['eas-therapie','esc-nonstatines']),
('Une interruption répétée sans stratégie de remplacement ne constitue donc pas un plan complet lorsque le traitement hypolipémiant reste indiqué.',['eas-therapie','esc-nonstatines'])])
save(s)

start(3)
s=h('De l’exposition pharmacologique à la manifestation musculaire')
s+=p('L’atorvastatine et la rosuvastatine inhibent la HMG-CoA réductase, enzyme de la synthèse du mévalonate puis du cholestérol.','aips83-sortis-pd','aips83-crestor-pd')
s+=p('Dans le foie, la réponse augmente la captation des LDL ; ce mécanisme explique l’objectif lipidique du traitement.','aips83-sortis-pd','aips83-crestor-pd')
s+=p('Le mécanisme de tous les symptômes musculaires associés reste cependant imparfaitement établi et ne se réduit pas à cette action hépatique.','eas-mecanisme')
s+=p('L’EAS discute une modification de la fonction mitochondriale, de la production énergétique et du renouvellement protéique musculaire.','eas-mecanisme')
s+=p('Ces hypothèses biologiques n’établissent pas qu’une douleur donnée sous statine résulte nécessairement d’une lésion mitochondriale.','eas-mecanisme','ctt-interpretation')
s+=p('Une concentration accrue par interaction ou forte exposition peut augmenter le risque toxique, tandis qu’une hypothyroïdie fournit un autre mécanisme musculaire.','eas-interactions','dgn-thyroide')
s+=rows(['Perturbation','Exploration qui la recherche','Action correspondant au mécanisme'],[
 [('Une interaction augmente l’exposition à l’atorvastatine.',['aips83-sortis-prudence']),('La liste des médicaments, leur chronologie et les symptômes sont rapprochés.',['eas-interactions']),('L’association est corrigée et la décision de poursuivre ou suspendre suit la notice du produit.',['aips83-sortis-prudence'])],
 [('Une lésion musculaire peut libérer des CK dans le sang.',['dgn-ck','rhabdo-s02']),('La CK est mesurée avec sa référence locale et confrontée à l’effort récent.',['dgn-ck']),('Le traitement myotoxique est arrêté lorsque les critères de sécurité sont atteints.',['aips83-sortis-prudence','aips83-crestor-prudence'])],
 [('Une lyse importante expose à des complications rénales et métaboliques.',['rhabdo-s02']),('La créatinine, la diurèse et les électrolytes complètent le bilan musculaire.',['rhabdo-s02']),('Les complications menaçantes imposent la filière urgente et le retrait du facteur déclenchant.',['rhabdo-s03','rhabdo-s11'])],
 [('L’hypothyroïdie perturbe le métabolisme énergétique musculaire.',['dgn-thyroide']),('Les paramètres thyroïdiens sont recherchés dans ce contexte.',['dgn-thyroide','mdx-diagnostic']),('La cause endocrinienne est prise en charge avant une attribution exclusive au médicament.',['eas-interactions','aips83-crestor-prudence'])],
 [('Une myopathie nécrosante auto-immune entretient une faiblesse malgré l’arrêt.',['dgn-imnm']),('La recherche anti-HMGCR et le bilan neuromusculaire précisent ce mécanisme.',['dgn-imnm']),('Une prise en charge immunologique spécialisée remplace le simple essai de changement de statine.',['dgn-imnm'])]])
s+=w('pharmacocinetique','Deux statines : des interactions différentes, un risque musculaire toujours présent',[
('L’atorvastatine est métabolisée par le cytochrome P450 3A4 ; ses métabolites actifs contribuent à l’effet pharmacologique.',['aips83-sortis-pk']),
('Ses transporteurs hépatiques interviennent également dans l’exposition ; la seule liste des inhibiteurs enzymatiques ne résume pas les interactions.',['aips83-sortis-pk','aips83-sortis-prudence']),
('La rosuvastatine subit un métabolisme limité et dépend notamment de transporteurs pour sa disposition.',['aips83-crestor-pk','aips83-crestor-posologie']),
('Une moindre dépendance au métabolisme ne rend donc pas la rosuvastatine exempte d’interactions ou de toxicité musculaire.',['aips83-crestor-prudence','aips83-crestor-posologie']),
('La ciclosporine est contre-indiquée avec Crestor, alors que Sortis dispose d’une restriction posologique propre à cette association.',['aips83-crestor-ci','aips83-sortis-prudence']),
('Le choix d’une alternative porte par conséquent sur le patient, le risque rénal et les associations réellement présentes.',['eas-interactions','aips83-crestor-ci'])])
s+=w('maintien','Ce qui explique une persistance après l’arrêt',[
('Une cause musculaire indépendante peut persister après retrait de la statine : endocrinopathie, maladie métabolique ou autre atteinte musculaire.',['eas-interactions','dgn-thyroide','dgn-biopsie']),
('Dans la myopathie toxique décrite par la DGN, la régression peut demander plusieurs semaines après l’arrêt.',['dgn-toxique']),
('Dans l’IMNM, la faiblesse et les CK peuvent rester anormales malgré le retrait, parce qu’une réaction auto-immune prolonge l’atteinte.',['dgn-imnm']),
('Une évolution progressive ou une dysphagie conduit donc à reclasser le tableau et à organiser une évaluation neuromusculaire.',['dgn-imnm']),
('L’absence d’amélioration ne justifie pas de multiplier seul les réintroductions ou les suppléments.',['dgn-imnm','eas-complements'])])
save(s)

start(4)
s=h('Écarter d’abord les tableaux qui ne suivent pas le parcours de symptômes légers')
s+=p('🚩 E1 s’applique à une rhabdomyolyse compliquée de menace rénale sévère ou de trouble électrolytique vital ; une myalgie isolée n’en reçoit pas ce rang.','rhabdo-s02','rhabdo-s11','rhabdo-e13')
s+=p('Des douleurs intenses, un gonflement important, une faiblesse ou des urines foncées font rechercher une lyse musculaire et ses complications.','rhabdo-s02')
s+=p('Une oligurie, une anurie, des constantes anormales ou des manifestations métaboliques changent la priorité de prise en charge.','rhabdo-e13','rhabdo-s02')
s+=p('Une faiblesse proximale progressive, une dysphagie et des CK très élevées font aussi sortir du cadre de SAMS simples vers une suspicion d’IMNM.','dgn-imnm')
s+=p('L’arrêt d’une statine est nécessaire dans ces situations, mais ne suffit pas à traiter leurs complications ni une maladie auto-immune.','aips83-sortis-prudence','dgn-imnm','rhabdo-s03')
s+=rows(['Diagnostic ou mécanisme concurrent','Élément discriminant','Piège','Conduite si positif'],[
 [('La rhabdomyolyse peut menacer le rein ou l’équilibre métabolique.',['rhabdo-s02']),('CK, créatinine, électrolytes et diurèse documentent l’atteinte.',['rhabdo-s02']),('La triade complète n’est pas constante et son absence ne protège pas des complications.',['rhabdo-s02']),('La statine est arrêtée ; les complications menaçantes relèvent de l’évaluation urgente surveillée.',['aips83-sortis-prudence','rhabdo-s03','rhabdo-s11'])],
 [('L’IMNM anti-HMGCR correspond à une myopathie distincte.',['dgn-imnm']),('La faiblesse proximale persiste ou progresse malgré l’arrêt et la recherche d’anticorps soutient le diagnostic.',['dgn-imnm']),('Un simple retrait médicamenteux peut ne pas faire régresser l’atteinte.',['dgn-imnm']),('Le patient est orienté en neuromusculaire pour les investigations et le traitement spécialisé.',['dgn-imnm'])],
 [('Une myopathie hypothyroïdienne peut coexister avec l’exposition.',['dgn-thyroide','dgn-statine']),('TSH et hormones thyroïdiennes libres confrontées à la clinique précisent la fonction endocrine.',['dgn-thyroide']),('Les CK peuvent être normales ou élevées ; ce seul résultat ne tranche pas entre mécanismes.',['dgn-thyroide']),('La cause thyroïdienne est corrigée dans un suivi médical, avec réévaluation de la stratégie lipidique.',['eas-interactions','aips83-crestor-prudence'])],
 [('L’effort musculaire fournit une cause concurrente de douleur et d’hyperCKémie.',['dgn-ck','eas-interactions']),('L’entretien précise l’activité récente et le laboratoire est replacé dans cette chronologie.',['dgn-anamnese','dgn-ck']),('Une CK augmentée après effort ne prouve pas une toxicité pharmacologique.',['dgn-ck']),('La gravité est évaluée ; une répétition interprétable du dosage est organisée si la situation est stable.',['dgn-ck','aips83-sortis-prudence'])]])
s+=w('rhabdo','Rhabdomyolyse suspectée : bilan simultané de la gravité',[
('La douleur, la faiblesse et les urines foncées sont évocatrices, mais seuls certains patients présentent cette triade complète.',['rhabdo-s02']),
('Le bilan ne s’arrête pas à la CK : la fonction rénale, les électrolytes et la diurèse recherchent les complications.',['rhabdo-s02']),
('L’hyperkaliémie peut apparaître précocement et s’aggraver rapidement ; la surveillance clinique et électrique suit cette menace.',['rhabdo-s11']),
('L’équipe retire le médicament myotoxique et corrige les troubles volémiques et métaboliques dans une filière adaptée.',['rhabdo-s03']),
('Un syndrome des loges constitue une autre urgence locale et peut exiger une décompression chirurgicale.',['rhabdo-s03','rhabdo-e13']),
('La mesure de CK seule ne décide donc pas de la sécurité d’un retour à domicile.',['rhabdo-e13','rhabdo-s02'])])
s+=w('imnm','Faiblesse persistante : rechercher une maladie qui dépasse la toxicité simple',[
('La DGN décrit une faiblesse proximale ou axiale progressive, parfois accompagnée de dysphagie et de myalgies.',['dgn-imnm']),
('Les anti-HMGCR soutiennent la suspicion d’une myopathie nécrosante auto-immune ; ils ne sont pas un dépistage de chaque douleur légère.',['dgn-imnm','dgn-statine']),
('La biopsie peut montrer nécrose et régénération avec peu d’infiltration lymphocytaire.',['dgn-imnm']),
('L’évolution persistante après arrêt distingue cette hypothèse d’une atteinte toxique réversible, sans suffire isolément à un diagnostic définitif.',['dgn-imnm','dgn-toxique']),
('Le service neuromusculaire choisit les examens et l’immunothérapie selon la maladie établie, sans réexposition banalisée à la statine.',['dgn-imnm'])])
save(s)

start(5)
s=h('Reconstituer une chronologie médicamenteuse et fonctionnelle utilisable')
s+=p('L’entretien situe les douleurs, leur caractère, leur fréquence et leur déclenchement au repos ou à l’effort.','dgn-anamnese','dgn-examen')
s+=p('La date d’introduction de la statine et les modifications de dose sont rapprochées du début des plaintes.','eas-definition','eas-imputabilite')
s+=p('La liste comprend les médicaments prescrits, l’automédication et les produits à base de plantes, qui peuvent participer aux interactions.','eas-interactions')
s+=p('Les activités gênées sont décrites concrètement : marche, escaliers, relèvement et port de charge renseignent le retentissement musculaire.','cen-myogene-clinique')
s+=p('L’interrogatoire recherche aussi une hypothyroïdie, une atteinte rénale, un antécédent musculaire et la consommation d’alcool.','dgn-statine','aips83-sortis-prudence')
s+=rows(['Question ciblée','Pourquoi elle compte','Décision préparée'],[
 [('Quand les douleurs ont-elles commencé par rapport au traitement ou à son augmentation ?',['eas-definition']),('La concordance temporelle participe à l’estimation de causalité.',['eas-imputabilite']),('Le clinicien compare les épisodes et prépare éventuellement une modification encadrée.',['eas-imputabilite','eas-therapie'])],
 [('Un antibiotique, un antifongique ou un autre traitement a-t-il été ajouté ?',['aips83-sortis-prudence']),('Certains produits augmentent l’exposition ou le risque myotoxique.',['aips83-sortis-prudence']),('L’association exacte est vérifiée avant de décider la suite de la statine.',['aips83-sortis-prudence'])],
 [('L’effort récent a-t-il été inhabituel, intense ou prolongé ?',['dgn-anamnese','dgn-ck']),('Il peut provoquer des symptômes et perturber l’interprétation des CK.',['dgn-ck']),('Le dosage est interprété avec l’activité et répété dans des conditions adaptées si la gravité le permet.',['dgn-ck'])],
 [('Le patient peut-il se lever, monter un escalier et porter les objets usuels ?',['cen-myogene-clinique']),('Ces actes distinguent le ressenti douloureux d’un déficit fonctionnel à objectiver.',['cen-myogene-clinique','cen-force']),('La force est testée comparativement et les tâches professionnelles sont rapprochées des capacités.',['cen-force','fmh-evaluation'])],
 [('Existe-t-il une dysphagie ou une faiblesse qui progresse malgré l’arrêt ?',['dgn-imnm']),('Ce profil peut correspondre à une myopathie auto-immune.',['dgn-imnm']),('La filière neuromusculaire devient prioritaire au lieu d’un changement empirique répété de médicament.',['dgn-imnm'])],
 [('Les urines sont-elles foncées ou devenues rares ?',['rhabdo-s02']),('Une pigmenturie, une oligurie ou une anurie peut accompagner une rhabdomyolyse.',['rhabdo-s02']),('Le bilan rénal et métabolique est organisé sans attendre une triade complète.',['rhabdo-s02','rhabdo-e13'])],
 [('Une maladie thyroïdienne ou rénale est-elle connue ou insuffisamment traitée ?',['dgn-statine','dgn-thyroide']),('Elle peut contribuer au symptôme ou augmenter le risque sous statine.',['dgn-statine']),('Le bilan et la prescription intègrent ce facteur modifiable.',['mdx-diagnostic','aips83-crestor-prudence'])]])
s+=w('alarme','Drapeaux rouges : question, constat et action',[
('Une faiblesse nouvelle importante est vérifiée par l’examen moteur, sans l’attribuer automatiquement à une douleur de traitement.',['dgn-examen','cen-force']),
('Une dysphagie associée à une faiblesse progressive fait rechercher une myopathie grave, notamment l’IMNM.',['dgn-imnm']),
('Des urines foncées ou une diurèse qui chute imposent la recherche d’une lyse musculaire et de ses complications.',['rhabdo-s02']),
('Des constantes anormales ou des perturbations métaboliques font privilégier une prise en charge surveillée plutôt qu’un essai ambulatoire de tolérance.',['rhabdo-e13','rhabdo-s11']),
('Le patient sait ainsi quels changements justifient un contact rapide, au-delà du seul chiffre de CK.',['rhabdo-e13','aips83-sortis-prudence'])])
save(s)

start(6)
s=h('Décrire la réponse normale avant de chercher un déficit')
s+=p('La force segmentaire normale reçoit la cotation 5 ; elle s’apprécie comparativement à droite et à gauche, muscle par muscle si nécessaire.','cen-force')
s+=p('La percussion musculaire normale provoque une contraction en masse suivie d’une décontraction rapide ; elle ne doit pas être confondue avec un réflexe tendineux.','cen-myogene-clinique')
s+=p('Les réflexes ostéotendineux peuvent être présents et normaux ; leur interprétation tient compte de la symétrie et du reste de l’examen.','cen-rot')
s+=p('Le clinicien recherche ensuite la douleur provoquée, la faiblesse objective, la topographie et les anomalies de volume musculaire.','dgn-examen','cen-myogene-clinique')
s+=p('Une plainte douloureuse ne suffit donc pas à retenir une parésie, et un examen préservé ne démontre pas l’origine médicamenteuse d’une douleur.','cen-force','eas-definition')
s+=w('force','Force : comment obtenir une constatation reproductible',[
('Le patient réalise un mouvement demandé et l’examinateur recherche ensuite la capacité à l’effectuer contre la pesanteur puis contre résistance.',['cen-force']),
('La comparaison entre les côtés distingue une faiblesse localisée d’une atteinte symétrique, sans imposer que toute atteinte musculaire soit parfaitement bilatérale.',['cen-force','cen-myogene-clinique']),
('La cotation 0 correspond à l’absence de contraction, tandis que 1 décrit une contraction sans effet moteur.',['cen-force']),
('La cotation 2 décrit un déplacement sans lutte contre la pesanteur, et 3 un mouvement contre la pesanteur.',['cen-force']),
('La cotation 4 correspond à une contraction contre résistance, alors que 5 est la référence normale.',['cen-force']),
('Le résultat doit être rapproché de la douleur et du retentissement fonctionnel plutôt que transformé directement en preuve d’une toxicité.',['dgn-examen','eas-definition'])])
s+=w('ceintures','Ceintures et activités : observer un déficit proximal',[
('Le relevé d’un siège et de la position accroupie renseigne la fonction proximale ; le clinicien note une aide par les mains ou une difficulté manifeste.',['cen-myogene-clinique']),
('Un patient qui s’aide des mains sur les genoux puis le long des cuisses utilise une compensation décrite dans le syndrome myogène.',['cen-myogene-clinique']),
('La marche dandinante et une hyperlordose peuvent accompagner l’atteinte pelvienne ou axiale, mais leur cause reste à établir.',['cen-myogene-clinique']),
('Aux membres supérieurs, les deltoïdes, les muscles du bras et les fléchisseurs de la nuque sont examinés selon la plainte.',['cen-myogene-clinique']),
('Ces observations complètent une cotation segmentaire ; elles ne remplacent pas la recherche d’une limitation articulaire ou douloureuse.',['cen-force','dgn-examen']),
('Une faiblesse majeure ou rapidement progressive fait interrompre le parcours de simple tolérance médicamenteuse et rechercher une myopathie grave.',['dgn-imnm','rhabdo-e13'])])
s+=w('palpation','Palpation, volume et sensibilité : compléter la force',[
('La palpation du muscle recherche une douleur à la pression et localise son siège, notamment au ventre musculaire.',['dgn-examen']),
('L’inspection décrit une amyotrophie, une hypertrophie ou une asymétrie ; ces éléments orientent une maladie musculaire concurrente.',['cen-myogene-clinique']),
('Un déficit sensitif ou des fasciculations ne correspondent pas au profil négatif habituel du syndrome myogène et orientent l’examen neurologique.',['cen-myogene-clinique']),
('L’absence d’abolition des réflexes est compatible avec une atteinte musculaire ; elle ne suffit pas à affirmer l’étiologie statinique.',['cen-myogene-clinique','eas-definition']),
('L’examen de la peau cherche aussi les signes particuliers d’une myosite, lorsque le contexte évoque cette possibilité.',['dgn-examen']),
('Le résultat est ainsi une description anatomique et fonctionnelle avant de devenir une hypothèse étiologique.',['dgn-examen','eas-definition'])])
s+=rows(['Geste','Réponse recherchée','Valeur et limite'],[
 [('La force est comparée dans les mêmes groupes musculaires des deux côtés.',['cen-force']),('Une cotation normale de 5 se distingue des niveaux de déficit.',['cen-force']),('La mesure objective la motricité ; elle ne prouve pas la cause d’une myalgie.',['cen-force','eas-definition'])],
 [('Le passage assis-debout est observé avec les compensations éventuelles.',['cen-myogene-clinique']),('La difficulté et l’usage des mains renseignent le retentissement proximal.',['cen-myogene-clinique']),('Le constat est confronté au testing et à la douleur, sans diagnostic causal immédiat.',['cen-force','dgn-examen'])],
 [('La palpation explore la région musculaire douloureuse.',['dgn-examen']),('L’examinateur note le siège de la douleur provoquée.',['dgn-examen']),('Une sensibilité locale ne distingue pas à elle seule effort, toxicité ou maladie inflammatoire.',['dgn-examen','eas-interactions'])],
 [('La percussion d’un tendon étudie un arc réflexe.',['cen-rot']),('Les réponses et leur répartition sont comparées à l’examen moteur et sensitif.',['cen-rot']),('Des réflexes présents n’excluent pas un syndrome myogène.',['cen-myogene-clinique'])]])
save(s)

start(7)
s=h('7.1 — Plaintes musculaires sans déficit majeur établi')
s+=p('La personne décrit douleur, courbature ou crampe au cours d’un traitement par statine ; la CK peut rester dans la référence.','eas-definition')
s+=p('L’examen vérifie la force et le retentissement afin de ne pas confondre gêne douloureuse et myopathie sévère.','dgn-examen','cen-force')
s+=p('La topographie et la chronologie soutiennent une évaluation de probabilité, sans démonstration automatique de causalité.','eas-definition','eas-imputabilite')
s+=h('7.2 — Syndrome myogène avec atteinte proximale')
s+=p('Une difficulté au relevé, à l’escalier ou au port de charge fait rechercher une faiblesse musculaire proximale et axiale.','cen-myogene-clinique')
s+=p('La cotation segmentaire et la comparaison des groupes musculaires décrivent le déficit réellement présent.','cen-force')
s+=p('Une progression persistante, notamment avec dysphagie, demande la recherche d’une myopathie spécialisée plutôt qu’une simple adaptation de confort.','dgn-imnm')
s+=h('7.3 — Lyse musculaire et risque de complication')
s+=p('Des douleurs, un gonflement et une faiblesse peuvent accompagner la rhabdomyolyse, parfois avec urines foncées ou diminution de diurèse.','rhabdo-s02')
s+=p('Le bilan recherche simultanément l’atteinte musculaire, rénale et métabolique parce que les symptômes seuls ne quantifient pas le risque.','rhabdo-s02','rhabdo-e13')
s+=p('Une menace rénale sévère ou une perturbation électrolytique vitale ouvre la branche 🚩 E1.','rhabdo-s02','rhabdo-s11')
s+=h('7.4 — Tableau concurrent ou facteur de vulnérabilité')
s+=p('Une hypothyroïdie peut associer fatigue musculaire, douleurs et faiblesse proximale avec des CK normales ou élevées.','dgn-thyroide')
s+=p('Un effort récent, une interaction ou une autre maladie musculaire peut produire un tableau partiellement semblable.','eas-interactions','dgn-ck','dgn-biopsie')
s+=p('Les associations de mécanismes restent possibles ; la lecture syndromique prépare donc le bilan au lieu d’attribuer tout le tableau à une exposition.','dgn-statine','dgn-thyroide','eas-definition')
s+=rows(['Ensemble clinique','Signes fonctionnels','Signes physiques et mécanisme'],[
 [('Les plaintes simples dominent parfois le tableau.',['dgn-statine']),('Le patient décrit douleur ou crampe avec gêne variable.',['eas-definition']),('La force est recherchée ; son maintien et des CK normales sont compatibles avec cette présentation.',['cen-force','eas-definition'])],
 [('Le syndrome myogène concerne le muscle lui-même.',['cen-myogene-definition']),('Les activités proximales deviennent difficiles.',['cen-myogene-clinique']),('Un déficit bilatéral proximal est objectivé, avec recherche d’éléments d’une cause concurrente.',['cen-myogene-clinique','eas-interactions'])],
 [('La rhabdomyolyse libère des constituants musculaires.',['rhabdo-s02']),('Douleur, faiblesse ou urines foncées peuvent être rapportées.',['rhabdo-s02']),('Le bilan biologique et la diurèse recherchent les complications rénales et électrolytiques.',['rhabdo-s02'])],
 [('Le mécanisme thyroïdien peut contribuer au tableau.',['dgn-thyroide']),('Fatigue et myalgies peuvent accompagner une hypothyroïdie symptomatique.',['dgn-thyroide']),('La force et les paramètres thyroïdiens sont confrontés aux CK et à l’histoire médicamenteuse.',['dgn-thyroide','eas-interactions'])]])
s+=w('signes','Définir les mots employés par le patient',[
('La myalgie désigne une douleur ressentie dans le muscle, localisée ou diffuse.',['dgn-definition']),
('La crampe décrite dans la sémiologie myogène comporte une contraction musculaire en boule, déclenchée ou non par un effort.',['cen-myogene-clinique']),
('La faiblesse fonctionnelle est appréciée par les activités, puis séparée du déficit moteur mesuré à l’examen.',['cen-myogene-clinique','cen-force']),
('Une difficulté au relevé d’un siège correspond à un signe fonctionnel proximal ; l’aide des bras est observée plutôt que supposée.',['cen-myogene-clinique']),
('Ces définitions guident les questions et les gestes, sans définir à elles seules une responsabilité de la statine.',['eas-definition','dgn-examen'])])
s+=w('deficit','Proximal, axial et persistant : préciser chaque terme',[
('Une atteinte proximale prédomine à la racine des membres ; une atteinte axiale concerne notamment la musculature du tronc ou de la nuque.',['cen-myogene-clinique']),
('La répartition est testée dans plusieurs muscles, car un mouvement global ne remplace pas la comparaison segmentaire.',['cen-force']),
('La persistance après arrêt devient préoccupante lorsqu’elle s’accompagne d’une progression, d’une dysphagie ou de CK très élevées.',['dgn-imnm']),
('Ce regroupement oriente vers une IMNM, dont le bilan et le traitement dépassent la simple correction d’une interaction.',['dgn-imnm']),
('L’évolution clinique est donc consignée avec la dose, les changements de traitement et les résultats biologiques.',['eas-imputabilite','aips83-sortis-prudence'])])
save(s)

start(8)
s=h('Diagnostic clinique de probabilité, puis critères de sécurité du produit')
s+=p('Le consensus EAS de 2015 propose une évaluation clinique associant nature des symptômes, CK et relation temporelle avec introduction, arrêt et réexposition.','eas-definition','eas-date')
s+=p('Il n’existe pas de test unique qui démontre, pour chaque plainte, que la statine est la cause du symptôme.','eas-definition')
s+=p('Un profil symétrique proximal et une chronologie compatible augmentent la plausibilité, mais les causes secondaires restent recherchées.','eas-definition','eas-interactions')
s+=p('La suspicion devient plus forte lorsque les symptômes et les CK s’améliorent après retrait puis réapparaissent lors d’une réexposition médicalement appropriée.','eas-imputabilite')
s+=p('Une réexposition n’est toutefois pas un test à réaliser dans la filière simple lorsqu’une rhabdomyolyse ou une IMNM est suspectée.','rhabdo-s03','dgn-imnm')
s+=rows(['Constat ou critère','Interprétation','Conséquence'],[
 [('Les symptômes surviennent sous statine avec une CK normale.',['eas-definition']),('Ils peuvent appartenir aux SAMS, mais la causalité reste incertaine.',['eas-definition']),('L’entretien, le testing et les causes concurrentes orientent la décision.',['eas-definition','eas-interactions'])],
 [('Le contexte d’effort peut expliquer une petite élévation des CK.',['dgn-ck']),('La valeur ne constitue pas une preuve pharmacologique spécifique.',['dgn-ck']),('Le résultat est confronté à la chronologie et répété de manière interprétable si besoin.',['dgn-ck'])],
 [('Les CK dépassent 5 fois la limite supérieure sous Sortis ou Crestor.',['aips83-sortis-prudence','aips83-crestor-prudence']),('La condition suisse d’arrêt du médicament est atteinte.',['aips83-sortis-prudence','aips83-crestor-prudence']),('La statine est arrêtée et la clinique ainsi que les complications possibles sont évaluées.',['aips83-sortis-prudence','rhabdo-s02'])],
 [('Les symptômes sont importants et constituent une gêne permanente malgré des CK inférieures à 5 fois la limite.',['aips83-sortis-prudence','aips83-crestor-prudence']),('Le chiffre ne suffit pas à autoriser une poursuite automatique.',['aips83-sortis-prudence','aips83-crestor-prudence']),('L’arrêt est envisagé et la stratégie de remplacement ou de reprise est préparée.',['aips83-sortis-prudence','eas-therapie'])],
 [('La faiblesse persiste et progresse avec des CK très élevées après arrêt.',['dgn-imnm']),('Une myopathie nécrosante auto-immune entre dans les hypothèses.',['dgn-imnm']),('Le bilan anti-HMGCR et neuromusculaire prend le relais.',['dgn-imnm'])]])
s+=w('seuil','Pourquoi le seuil d’arrêt ne doit pas être confondu avec un diagnostic causal',[
('La DGN discute une poursuite possible dans certaines présentations tolérables avec des CK inférieures à dix fois la norme.',['dgn-statine']),
('Les informations suisses de Sortis et Crestor imposent cependant l’arrêt au-delà de 5 fois la limite supérieure.',['aips83-sortis-prudence','aips83-crestor-prudence']),
('La prescription de ces spécialités suit leurs conditions propres, sans attendre un seuil plus élevé tiré d’une recommandation générale.',['aips83-sortis-prudence','aips83-crestor-prudence']),
('Ce seuil de sécurité ne confirme pas une origine médicamenteuse et ne mesure pas seul le risque rénal ou métabolique.',['eas-definition','rhabdo-e13']),
('Un tableau grave peut donc demander une prise en charge urgente avant toute discussion de réintroduction.',['rhabdo-e13','rhabdo-s11'])])
s+=w('insuffisant','Ce qui ne suffit pas pour conclure',[
('La seule coïncidence entre douleur et prise de statine ne démontre pas la causalité.',['eas-definition','ctt-interpretation']),
('Des CK normales n’excluent pas les symptômes et ne dispensent pas de rechercher une faiblesse progressive.',['eas-definition','dgn-imnm']),
('Une élévation isolée après exercice ne permet pas de diagnostiquer une myopathie toxique.',['dgn-ck']),
('Une TSH ou un contexte thyroïdien anormal fait rechercher une contribution endocrine plutôt que confirmer une responsabilité exclusive de la statine.',['dgn-thyroide','eas-interactions']),
('Un anticorps anti-HMGCR soutient une hypothèse spécialisée et s’interprète avec le phénotype, l’évolution et les autres examens.',['dgn-imnm'])])
save(s)

start(9)
s=h('9.a — Référence : confrontation clinique, chronologique et biologique')
s+=p('Le diagnostic des SAMS est clinique et probabiliste ; aucune prise de sang n’est un gold standard isolé de causalité.','eas-definition')
s+=p('La CK mesure un signal de lésion musculaire et fournit une information de sécurité, différente de l’imputabilité pharmacologique.','dgn-ck','aips83-sortis-prudence')
s+=p('L’examen de la force, la recherche des causes secondaires et l’évolution sous stratégie encadrée complètent cette interprétation.','eas-definition','eas-interactions','eas-imputabilite')
s+=h('9.b — Première intention : demander ce qui change la décision')
s+=p('Chez un patient sous statine qui rapporte douleur, faiblesse ou crampes, les notices suisses demandent un dosage des CK/CPK.','aips83-sortis-prudence','aips83-crestor-prudence')
s+=p('Le résultat est rendu avec son unité, sa limite supérieure de référence et son rapport à cette limite, sans imposer une valeur normale universelle.','dgn-ck','aips83-sortis-prudence')
s+=p('Le prélèvement et l’activité récente sont documentés, car un effort important peut augmenter les CK et compliquer leur lecture.','dgn-ck','aips83-sortis-prudence')
s+=p('La recherche d’une hypothyroïdie et le bilan hépatique sont rapprochés du contexte clinique et de la prescription hypolipémiante.','mdx-diagnostic','eas-interactions')
s+=p('Si une rhabdomyolyse est suspectée, créatinine, électrolytes et surveillance de la diurèse sont recherchés sans se limiter au bilan de tolérance habituel.','rhabdo-s02')
s+=rows(['Examen et prescription contextualisée','Résultat et signification','Action'],[
 [('Le dosage sanguin des CK est prescrit pour symptômes musculaires sous statine.',['aips83-sortis-prudence']),('Une CK normale reste compatible avec des SAMS ; une valeur augmentée n’en prouve pas la cause.',['eas-definition','dgn-ck']),('L’interprétation est couplée aux symptômes, à l’effort et aux conditions de sécurité du produit.',['dgn-ck','aips83-sortis-prudence'])],
 [('Les CK sont comparées à la limite supérieure du laboratoire.',['aips83-sortis-prudence']),('Un résultat supérieur à 5 fois cette limite impose l’arrêt sous Sortis ou Crestor.',['aips83-sortis-prudence','aips83-crestor-prudence']),('Le médicament est arrêté et les causes ainsi que les complications sont recherchées.',['aips83-sortis-prudence','rhabdo-s02'])],
 [('Le bilan thyroïdien est demandé si le contexte évoque une contribution endocrine.',['dgn-thyroide','mdx-diagnostic']),('Une hypothyroïdie peut expliquer douleur ou faiblesse et augmenter la vulnérabilité sous statine.',['dgn-thyroide','dgn-statine']),('La prise en charge endocrine est intégrée avant de figer la causalité ou de réintroduire.',['eas-interactions','aips83-crestor-prudence'])],
 [('La créatinine et les électrolytes accompagnent une suspicion de lyse musculaire.',['rhabdo-s02']),('Une atteinte rénale ou une hyperkaliémie indique une complication potentiellement grave.',['rhabdo-s02','rhabdo-s11']),('Le lieu de soins et le monitorage sont adaptés sans attendre la seule cinétique des CK.',['rhabdo-e13','rhabdo-s11'])],
 [('Le bilan hépatique suit les indications de la spécialité.',['aips83-sortis-prudence','aips83-crestor-prudence']),('Une anomalie persistante des transaminases peut modifier la prescription.',['aips83-sortis-prudence','aips83-crestor-ci']),('La dose ou le traitement est réévalué selon la notice et le contexte hépatique.',['aips83-sortis-prudence','aips83-crestor-ci'])]])
s+=w('conditions','Conditions du dosage : un délai n’autorise pas à attendre en présence de gravité',[
('Pour une interprétation élective fiable, la DGN recommande de tenir compte du repos musculaire et des gestes susceptibles d’augmenter les CK.',['dgn-ck']),
('Les notices évitent un dosage de référence juste après un effort intense lorsque son résultat serait difficile à interpréter.',['aips83-sortis-prudence','aips83-crestor-prudence']),
('Avant l’initiation, des CK supérieures à 5 fois la limite sont revérifiées dans les 5–7 jours ; cette instruction concerne le bilan préalable.',['aips83-sortis-prudence','aips83-crestor-prudence']),
('Une suspicion actuelle de rhabdomyolyse, une anurie ou une menace métabolique exige au contraire le bilan urgent de complications.',['rhabdo-s02','rhabdo-e13']),
('Le patient symptomatique grave ne doit donc pas attendre une période de repos pour obtenir une première évaluation.',['rhabdo-e13','rhabdo-s11'])])
s+=h('9.c — Terrains particuliers et alternatives')
s+=p('Le bilan initial décrit repose sur l’examen et les dosages ; il ne prévoit pas d’imagerie injectée de routine.','eas-definition','dgn-labo')
s+=p('Une insuffisance rénale renforce la vigilance et modifie les possibilités de prescription, notamment pour la rosuvastatine.','aips83-crestor-ci','aips83-sortis-prudence')
s+=p('Pendant une grossesse, les spécialités statiniques décrites sont contre-indiquées ; les symptômes et la stratégie lipidique demandent une réévaluation médicale.','aips83-sortis-grossesse','aips83-crestor-grossesse')
s+=p('Chez l’enfant, le schéma adulte de cette monographie n’est pas transposé ; Sortis n’est pas autorisé dans cette population et Crestor a des indications pédiatriques précises.','aips83-sortis-posologie','aips83-crestor-indications')
s+=h('9.d — Deuxième intention : faiblesse persistante ou tableau atypique')
s+=p('La recherche anti-HMGCR est envisagée dans un phénotype de faiblesse proximale persistante avec CK très élevées évoquant une IMNM.','dgn-imnm')
s+=p('L’EMG aide à caractériser une atteinte myogène ou neurogène ; ses anomalies ne déterminent pas à elles seules la cause d’une myopathie.','cen-myogene-emg','dgn-emg')
s+=p('Une IRM des territoires musculaires concernés peut étudier la distribution des lésions aiguës ou chroniques et aider au choix d’une biopsie.','dgn-imagerie')
s+=p('La DGN précise que les séquences musculaires modernes peuvent généralement rechercher l’atteinte sans produit de contraste.','dgn-imagerie')
s+=p('Si l’IRM est impossible, le service choisit les autres explorations utiles, notamment électrophysiologie ou échographie, sans prétendre qu’elles donnent la même information.','cen-myogene-emg','dgn-imagerie')
s+=p('La biopsie musculaire reste réservée à des indications sélectionnées après le bilan non invasif, particulièrement si une maladie inflammatoire est suspectée.','dgn-biopsie','dgn-imnm')
s+=w('imagerie','Une anomalie d’imagerie n’est pas une signature de toxicité',[
('L’IRM est sensible à des anomalies musculaires, mais leurs aspects peuvent se recouvrir entre plusieurs maladies.',['dgn-imagerie']),
('La DGN demande donc une corrélation avec la clinique, la biologie et, selon le cas, les autres explorations.',['dgn-imagerie']),
('Une image anormale n’établit pas à elle seule que la statine est responsable de la plainte.',['dgn-imagerie','eas-definition']),
('Inversement, les SAMS courants ne nécessitent pas une IRM pour être évalués cliniquement et pharmacologiquement.',['eas-definition','eas-interactions']),
('Le recours spécialisé est guidé par la faiblesse, la persistance et les signes atypiques, plutôt que par la seule présence d’une exposition.',['dgn-imnm','dgn-biopsie'])])
save(s)

start(10)
s=h('Des décisions explicites à partir de la gravité et des conditions suisses')
branches=[
('Si des douleurs et un gonflement important s’accompagnent d’urines foncées ou d’une baisse de diurèse, rechercher la rhabdomyolyse et ses complications.',['rhabdo-s02']),
('Si une complication rénale sévère ou électrolytique menace le pronostic vital, prendre la branche 🚩 E1 et organiser la prise en charge urgente surveillée.',['rhabdo-s02','rhabdo-s11']),
('Si une faiblesse proximale progresse malgré le retrait de la statine, surtout avec dysphagie et CK très élevées, adresser en neuromusculaire pour suspicion d’IMNM.',['dgn-imnm']),
('Si les CK dépassent 5 fois la limite supérieure sous Sortis ou Crestor, arrêter la spécialité et évaluer la clinique ainsi que les complications possibles.',['aips83-sortis-prudence','aips83-crestor-prudence','rhabdo-s02']),
('Si les symptômes sont importants ou continuellement gênants malgré des CK inférieures à 5 fois la limite, envisager aussi l’arrêt et un plan médical de remplacement.',['aips83-sortis-prudence','aips83-crestor-prudence','eas-therapie']),
('Si une interaction est retrouvée, vérifier la recommandation propre à la spécialité et corriger l’association avant toute reprise.',['aips83-sortis-prudence','aips83-crestor-posologie']),
('Si une hypothyroïdie est présente, intégrer sa correction et réévaluer les symptômes ainsi que la stratégie lipidique.',['dgn-thyroide','eas-interactions','aips83-crestor-prudence']),
('Si l’effort récent fournit une explication plausible et que le patient est stable, interpréter les CK dans cette chronologie et organiser le contrôle utile.',['dgn-ck','rhabdo-e13']),
('Si les plaintes restent légères et sans signe de myopathie grave, discuter la dose tolérée et les causes concurrentes au lieu d’un arrêt définitif automatique.',['dgn-statine','eas-interactions']),
('Si une suspension a été retenue, attendre la disparition des symptômes et la normalisation requise des CK avant une reprise médicalement appropriée à faible dose.',['aips83-sortis-prudence','aips83-crestor-prudence']),
('Si la tolérance de la statine reste insuffisante alors que la prévention est indiquée, choisir une autre stratégie hypolipémiante selon risque, bénéfice et préférences.',['esc-nonstatines','eas-therapie'])]
for t,ids in branches:s+=p(t,*ids)
s+=w('urgence','Urgence — conduite chronologique',[
('L’examen commence par les constantes, la faiblesse, le gonflement, les urines et la diurèse afin de repérer les complications.',['rhabdo-e13','rhabdo-s02']),
('Le médicament myotoxique est retiré lorsque la myopathie grave ou la rhabdomyolyse est suspectée.',['aips83-sortis-prudence','rhabdo-s03']),
('Le bilan musculaire, rénal et électrolytique est réalisé sans attendre une épreuve de réexposition.',['rhabdo-s02','rhabdo-s11']),
('Une hyperkaliémie peut s’aggraver rapidement et impose une surveillance ainsi qu’un traitement spécialisé adapté à la menace.',['rhabdo-s11']),
('La correction des troubles volémiques et métaboliques ainsi que l’orientation sont décidées selon la gravité et les comorbidités.',['rhabdo-s03','rhabdo-e13']),
('Après stabilisation, une faiblesse persistante ou progressive déclenche le bilan d’une cause musculaire sous-jacente, notamment auto-immune.',['dgn-imnm','dgn-biopsie'])])
save(s)

start(11)
s=h('11.A — Traiter la plainte et préserver une prévention appropriée')
s+=p('Le but est une tolérance musculaire acceptable sans méconnaître une myopathie, avec une baisse lipidique adaptée au risque cardiovasculaire.','eas-therapie','esc-nonstatines')
s+=p('Le suivi inscrit la force sur la cotation de 0 à 5, les activités gênées, les CK et leur rapport à la référence du laboratoire.','cen-force','cen-myogene-clinique','aips83-sortis-prudence')
s+=p('La disparition des symptômes et la normalisation des CK sont des conditions de reprise lorsque la notice les demande après un arrêt.','aips83-sortis-prudence','aips83-crestor-prudence')
s+=p('Les objectifs lipidiques restent individualisés ; une faible tolérance ne se résout pas par un abandon sans projet si la prévention demeure indiquée.','esc-nonstatines','eas-therapie')
s+=h('11.B — Choisir dans l’ordre : sécurité, facteurs favorisants, puis stratégie lipidique')
s+=p('La première décision est de repérer une rhabdomyolyse, une faiblesse grave ou une complication rénale ou métabolique.','rhabdo-s02','rhabdo-e13')
s+=p('Les interactions, l’hypothyroïdie et l’effort récent sont ensuite recherchés parce qu’ils peuvent expliquer ou amplifier les symptômes.','eas-interactions','dgn-statine','dgn-ck')
s+=p('Lorsque le tableau est léger et tolérable, la décision peut conserver une exposition adaptée sous surveillance plutôt que retirer définitivement toute statine.','dgn-statine','eas-therapie')
s+=p('Lorsqu’un arrêt est nécessaire, le médecin définit les conditions du contrôle et de la reprise éventuelle, sans réexposition improvisée.','aips83-sortis-prudence','aips83-crestor-prudence')
s+=w('urgence','Urgence — conduite chronologique',[
('Le patient présentant urines foncées, diurèse basse, faiblesse importante ou constantes anormales reçoit d’abord une évaluation de gravité.',['rhabdo-s02','rhabdo-e13']),
('La statine est arrêtée si une myopathie grave est suspectée ; la recherche des complications ne dépend pas de la preuve finale de causalité.',['aips83-sortis-prudence','rhabdo-s03']),
('Les CK, la fonction rénale et les électrolytes sont évalués avec la diurèse, puis le monitorage suit les anomalies constatées.',['rhabdo-s02','rhabdo-s11']),
('Une complication rénale sévère ou électrolytique vitale relève de la branche 🚩 E1 et d’une prise en charge urgente surveillée.',['rhabdo-s02','rhabdo-s11']),
('Le facteur déclenchant est retiré et les anomalies volémiques, rénales et métaboliques sont traitées par l’équipe responsable.',['rhabdo-s03']),
('Une faiblesse persistante ou progressive, notamment avec dysphagie, déclenche le bilan spécialisé d’IMNM ou d’une autre maladie musculaire.',['dgn-imnm','dgn-biopsie'])])
s+=h('Spécialités suisses : posologies adultes lorsque la reprise est médicalement appropriée')
s+=p('Une myopathie active est contre-indiquée pour les statines présentées ; les doses ci-dessous ne sont pas une prescription pendant une rhabdomyolyse ou une IMNM.','aips83-sortis-ci','aips83-crestor-ci','dgn-imnm')
s+=rows(['Spécialité et indication','Dose, voie et adaptation','Condition de sécurité et durée'],[
 [('Sortis® contient de l’atorvastatine pour les indications lipidiques ou préventives de sa notice.',['aips83-sortis-indications']),('Chez l’adulte, la dose initiale usuelle orale est de 10 mg une fois par jour ; les adaptations se font à intervalles de 4 semaines ou plus.',['aips83-sortis-posologie']),('Le maximum est de 80 mg par jour, sans constituer un objectif de reprise après symptômes ; la durée suit l’indication et la tolérance.',['aips83-sortis-posologie','aips83-sortis-prudence'])],
 [('Crestor® contient de la rosuvastatine ; l’indication lipidique est vérifiée avant le choix d’une alternative.',['aips83-crestor-indications']),('Chez l’adulte prédisposé à la myopathie, la dose initiale est de 5 mg par voie orale une fois par jour ; la posologie générale de départ est de 5–10 mg.',['aips83-crestor-posologie']),('La réintroduction attend la disparition des symptômes et la normalisation des CK, avec faible dose et surveillance étroite.',['aips83-crestor-prudence'])],
 [('Ezetrol® contient de l’ézétimibe, autorisé notamment en monothérapie ou avec statine pour l’hypercholestérolémie primaire.',['aips83-ezetrol-indications']),('La posologie orale est de 10 mg une fois par jour, indépendamment des repas.',['aips83-ezetrol-posologie']),('Le choix dépend du risque et du besoin lipidique ; la molécule n’est pas un antalgique et demande aussi une surveillance musculaire.',['aips83-ezetrol-pd','aips83-ezetrol-prudence','esc-nonstatines'])]])
s+=p('Les autorisations sont 54085 pour Sortis, 56139 pour Crestor et 56195 pour Ezetrol ; leurs notices lues datent respectivement d’avril 2025, juin 2026 et mars 2024.','aips83-sortis-autorisation','aips83-crestor-autorisation','aips83-ezetrol-autorisation','aips83-sortis-date','aips83-crestor-date','aips83-ezetrol-date')
s+=w('sortis','Atorvastatine : reprise, rein, foie et interactions pertinentes',[
('La prise de Sortis peut avoir lieu à tout moment, avec ou sans repas ; le régime hypolipémiant est poursuivi.',['aips83-sortis-posologie']),
('La dose est individualisée selon la réponse lipidique ; une reprise après symptômes n’impose pas la dose maximale.',['aips83-sortis-posologie','aips83-sortis-prudence']),
('Une insuffisance rénale ne demande pas d’adaptation posologique propre à l’atorvastatine, mais reste un facteur de vigilance pour le risque musculaire.',['aips83-sortis-posologie','aips83-sortis-prudence']),
('Une maladie hépatique active, une cholestase, une myopathie ou une élévation durable inexpliquée des transaminases au-delà du triple de la normale contre-indique Sortis.',['aips83-sortis-ci']),
('Les tests hépatiques sont effectués avant traitement puis à intervalles réguliers ; une élévation persistante significative fait réévaluer la dose ou l’arrêt.',['aips83-sortis-prudence']),
('Le comprimé de 20, 40 ou 80 mg possède une rainure permettant sa division ; cette propriété ne remplace pas le choix d’une dose prescrite.',['aips83-sortis-posologie']),
('L’association à glécaprévir/pibrentasvir est contre-indiquée et le risque musculaire impose une vérification de l’ensemble de l’ordonnance.',['aips83-sortis-ci','aips83-sortis-prudence'])])
s+=rows(['Association rencontrée','Règle de la notice','Action pratique'],[
 [('L’acide fusidique systémique ne doit pas être associé à Sortis ou Crestor.',['aips83-sortis-prudence','aips83-crestor-prudence']),('La statine est suspendue pendant le traitement indispensable et peut reprendre 7 jours après la dernière prise selon la notice.',['aips83-sortis-prudence','aips83-crestor-prudence']),('Le nom exact du médicament et la date de fin sont transmis au prescripteur avant la reprise.',['aips83-sortis-prudence','aips83-crestor-prudence'])],
 [('La ciclosporine modifie fortement les possibilités d’association.',['aips83-sortis-prudence','aips83-crestor-ci']),('Sortis est limité à 10 mg par jour dans cette association, tandis que Crestor est contre-indiqué.',['aips83-sortis-prudence','aips83-crestor-ci']),('Le simple changement de statine ne dispense donc pas de vérifier l’interaction propre à la spécialité.',['aips83-sortis-prudence','aips83-crestor-ci'])],
 [('Le gemfibrozil augmente le risque musculaire des associations statiniques.',['aips83-sortis-prudence','aips83-crestor-prudence']),('L’atorvastatine est à éviter et l’association de Crestor au gemfibrozil n’est pas recommandée.',['aips83-sortis-prudence','aips83-crestor-prudence']),('La stratégie hypolipémiante est revue plutôt que considérer l’association comme une réponse aux symptômes.',['aips83-sortis-prudence','aips83-crestor-prudence'])],
 [('La daptomycine associée à Sortis peut accroître le risque de myopathie ou de rhabdomyolyse.',['aips83-sortis-prudence']),('La notice envisage une interruption temporaire ; si l’association est incontournable, les CK sont mesurées deux à trois fois par semaine.',['aips83-sortis-prudence']),('Une surveillance rigoureuse des manifestations musculaires accompagne cette décision médicale.',['aips83-sortis-prudence'])]])
s+=w('crestor','Rosuvastatine : une alternative possible, avec ses propres exclusions',[
('Une dose initiale de 5 mg est recommandée chez les patients prédisposés à la myopathie, âgés de plus de 70 ans ou d’origine asiatique.',['aips83-crestor-posologie']),
('La forme est prise une fois par jour, indépendamment des repas ; une adaptation peut intervenir après 4 semaines si nécessaire.',['aips83-crestor-posologie']),
('Crestor est contre-indiqué lorsque la clairance de créatinine est inférieure à 30 ml/min.',['aips83-crestor-ci']),
('La dose de 40 mg possède des contre-indications supplémentaires, notamment insuffisance rénale modérée, hypothyroïdie et antécédent d’atteinte toxico-musculaire.',['aips83-crestor-ci']),
('Chez les patients asiatiques, cette dose de 40 mg est également contre-indiquée.',['aips83-crestor-ci']),
('La dose élevée relève de situations lipidiques sélectionnées et d’un contrôle spécialisé ; elle n’est pas une réponse standard à une intolérance antérieure.',['aips83-crestor-posologie','aips83-crestor-ci']),
('Les médicaments agissant sur les transporteurs peuvent augmenter l’exposition et imposent une vérification spécifique avant l’association.',['aips83-crestor-posologie']),
('Une hypercholestérolémie secondaire à une hypothyroïdie demande le traitement de la cause sous-jacente avant l’instauration de Crestor.',['aips83-crestor-prudence'])])
s+=w('ezetrol','Ézétimibe : traiter le risque lipidique sans promettre l’absence d’effet musculaire',[
('L’ézétimibe inhibe l’absorption intestinale du cholestérol en ciblant le transporteur NPC1L1 ; son mécanisme diffère de celui des statines.',['aips83-ezetrol-pd']),
('Ezetrol est pris oralement à 10 mg une fois par jour, seul ou dans une association conforme à sa notice.',['aips83-ezetrol-posologie']),
('La dose ne demande habituellement pas d’adaptation rénale ou liée au seul âge avancé.',['aips83-ezetrol-posologie']),
('En cas d’insuffisance hépatique modérée ou sévère, le traitement n’est pas recommandé.',['aips83-ezetrol-posologie']),
('Une hypersensibilité au principe actif ou aux excipients est contre-indiquée.',['aips83-ezetrol-ci']),
('De rares cas de myopathie et de rhabdomyolyse sont rapportés ; une suspicion de myopathie fait arrêter Ezetrol et la statine éventuellement associée.',['aips83-ezetrol-prudence']),
('Le risque musculaire ne disparaît donc pas du suivi lorsque la stratégie comporte un médicament non statinique.',['aips83-ezetrol-prudence']),
('La prise d’Ezetrol se place au moins 2 heures avant ou 4 heures après la cholestyramine.',['aips83-ezetrol-interactions']),
('Une association avec la warfarine demande des contrôles rapprochés de l’INR selon l’information professionnelle.',['aips83-ezetrol-interactions'])])
s+=w('situations','Grossesse, allaitement, âge et prescription pédiatrique',[
('Sortis et Crestor sont contre-indiqués pendant la grossesse et l’allaitement ; une grossesse débutante fait arrêter la statine et réévaluer le traitement.',['aips83-sortis-grossesse','aips83-crestor-grossesse']),
('Les patientes susceptibles de concevoir reçoivent les informations de contraception et de retour médical propres à la spécialité.',['aips83-sortis-grossesse','aips83-crestor-grossesse']),
('Ezetrol en association avec une statine est aussi contre-indiqué pendant grossesse et allaitement ; sa monothérapie ne devient pas une alternative automatique.',['aips83-ezetrol-ci','aips83-ezetrol-grossesse']),
('Pour l’ézétimibe seul, les données de grossesse sont insuffisantes et la notice demande de la prudence.',['aips83-ezetrol-grossesse']),
('L’ézétimibe pendant l’allaitement n’est pas recommandé sauf si l’avantage attendu justifie le risque potentiel pour l’enfant.',['aips83-ezetrol-grossesse']),
('Chez la personne âgée, les maladies associées et les interactions sont recherchées ; la rosuvastatine dispose d’une dose initiale adaptée.',['aips83-crestor-posologie','aips83-sortis-prudence']),
('Sortis n’est pas autorisé chez l’enfant ou l’adolescent ; les schémas adultes décrits ne sont pas transposés.',['aips83-sortis-posologie']),
('Crestor dispose d’une indication précise pour certaines hypercholestérolémies familiales pédiatriques ; un symptôme musculaire y demande un avis adapté à cette population.',['aips83-crestor-indications','aips83-crestor-prudence']),
('Ezetrol n’est pas recommandé avant 10 ans ; la décision pédiatrique respecte ses indications et son suivi propres.',['aips83-ezetrol-posologie'])])
s+=h('Mesures non médicamenteuses et information partagée')
s+=p('Le régime et les autres mesures de prévention cardiovasculaire sont maintenus selon l’indication, sans promettre qu’ils remplacent toute pharmacothérapie nécessaire.','aips83-sortis-posologie','aips83-crestor-posologie','esc-nonstatines')
s+=p('L’effort récent est pris en compte pour interpréter les douleurs et les CK, puis l’activité est adaptée à la situation musculaire réelle.','dgn-ck','rhabdo-e13')
s+=p('Le coenzyme Q10 n’est pas recommandé par mediX pour améliorer la tolérance statinique ; une hypothèse mitochondriale n’établit pas l’efficacité d’un supplément.','mdx-sams','eas-mecanisme','eas-complements')
s+=p('Les schémas intermittents évoqués dans certaines recommandations relèvent d’un plan prescrit et surveillé, et non d’une modification improvisée du régime quotidien de la notice.','mdx-sams','eas-therapie','aips83-sortis-posologie')
s+=p('La mise à jour ESC/EAS de 2025 permet de choisir des traitements non statiniques selon le besoin résiduel, les préférences, la disponibilité et le coût.','esc-nonstatines','esc-reprise-ch')
s+=h('11.C — Surveillance : clinique, CK, interactions et objectifs lipidiques')
s+=rows(['Ce qui est surveillé','Quand et dans quel contexte','Constat qui modifie la conduite'],[
 [('La douleur, les crampes et la force sont reconsidérées.',['aips83-sortis-prudence','cen-force']),('Une modification de dose, une nouvelle association ou une aggravation conduit au contrôle clinique et biologique utile.',['aips83-sortis-prudence','eas-definition']),('Une faiblesse progressive ou une dysphagie fait rechercher une maladie musculaire grave.',['dgn-imnm'])],
 [('Les CK sont dosées en présence de symptômes musculaires sous statine.',['aips83-sortis-prudence','aips83-crestor-prudence']),('Avant initiation, une valeur supérieure à 5 fois la limite est vérifiée dans les 5–7 jours.',['aips83-sortis-prudence','aips83-crestor-prudence']),('Sous traitement, le dépassement de 5 fois la limite impose l’arrêt ; des symptômes importants peuvent le justifier en dessous.',['aips83-sortis-prudence','aips83-crestor-prudence'])],
 [('La fonction hépatique accompagne le suivi prescrit.',['aips83-sortis-prudence','aips83-crestor-prudence']),('Crestor demande un bilan avant traitement puis à 3 mois ; Sortis prévoit un bilan initial puis régulier.',['aips83-sortis-prudence','aips83-crestor-prudence']),('Une hausse persistante significative des transaminases entraîne une réduction ou un arrêt selon la spécialité.',['aips83-sortis-prudence','aips83-crestor-prudence'])],
 [('Le besoin lipidique et la tolérance sont évalués ensemble.',['eas-therapie','esc-nonstatines']),('Les adaptations usuelles de Sortis sont espacées d’au moins 4 semaines et Crestor réévalue son adaptation après 4 semaines.',['aips83-sortis-posologie','aips83-crestor-posologie']),('Une tolérance insuffisante conduit à choisir une autre stratégie plutôt qu’à augmenter mécaniquement.',['eas-therapie','esc-nonstatines'])],
 [('La créatinine, les électrolytes et la diurèse sont suivis en cas de lyse suspectée.',['rhabdo-s02']),('La surveillance se rapproche selon les anomalies, leur évolution et les comorbidités.',['rhabdo-e13','rhabdo-s11']),('Une menace rénale sévère ou une hyperkaliémie évolutive impose l’orientation surveillée adaptée.',['rhabdo-s02','rhabdo-s11'])]])
s+=h('11.D — Conditions de suivi ambulatoire ou de relais, une par une')
conditions=[
('Le bilan n’a pas retenu une complication musculaire, rénale ou métabolique nécessitant une filière urgente.',['rhabdo-e13','rhabdo-s02']),
('La force et les symptômes ont été documentés et ne présentent pas une progression imposant un bilan neuromusculaire immédiat.',['dgn-imnm','cen-force']),
('Le patient sait si sa statine est maintenue, réduite ou arrêtée, avec une décision médicale cohérente avec la notice.',['aips83-sortis-prudence','aips83-crestor-prudence']),
('Les médicaments interagissants et les causes associées ont été identifiés ou font l’objet d’un bilan organisé.',['eas-interactions','mdx-diagnostic']),
('Le contrôle clinique et biologique est prévu selon l’évolution, les seuils de sécurité et la modification thérapeutique retenue.',['aips83-sortis-prudence','aips83-crestor-prudence']),
('Le patient connaît les motifs de retour rapide : faiblesse importante, dysphagie, gonflement marqué, urines foncées ou baisse de diurèse.',['dgn-imnm','rhabdo-s02','aips83-sortis-prudence']),
('Une éventuelle réintroduction est expliquée comme une décision différée et surveillée, après les conditions de résolution prévues.',['aips83-sortis-prudence','aips83-crestor-prudence']),
('Le projet hypolipémiant reste défini si la prévention cardiovasculaire est indiquée.',['esc-nonstatines','eas-therapie'])]
for t,ids in conditions:s+=p(t,*ids)
s+=w('social','Travail, conduite et assurance : partir des capacités observées',[
('La gêne au relevé, à la marche ou au port de charge est rapprochée des exigences réelles de l’activité professionnelle.',['cen-myogene-clinique','fmh-evaluation']),
('La capacité de travail est évaluée médicalement à partir des observations et du poste, sans durée d’arrêt automatique liée au seul mot SAMS.',['fmh-evaluation']),
('Le certificat précise début, fin ou prochaine consultation, ainsi que le degré d’incapacité complète ou partielle.',['fmh-certificat']),
('Le document destiné à l’employeur n’expose pas le diagnostic ni le traitement, conformément au cadre ASSM/FMH.',['fmh-secret','fmh-certificat']),
('L’information nécessaire au suivi avec les assureurs respecte le cadre du destinataire et le secret médical.',['fmh-secret','fmh-evaluation']),
('Sortis peut altérer la capacité de réaction ; pour Crestor, la notice demande notamment de tenir compte des vertiges lors de la conduite.',['aips83-sortis-conduite','aips83-crestor-conduite']),
('Les fonctions nécessaires au travail et à la conduite sont donc réévaluées avec les symptômes et les effets du traitement.',['fmh-evaluation','aips83-sortis-conduite','aips83-crestor-conduite'])])
save(s)

start(12)
s=h('Prévention primaire : réduire les situations favorisant une atteinte musculaire')
s+=p('Avant la prescription, l’indication lipidique et les facteurs de risque sont discutés pour choisir une exposition adaptée.','eas-interactions','aips83-sortis-posologie')
s+=p('La recherche d’interactions comprend aussi l’automédication et les produits à base de plantes, car ils peuvent modifier l’exposition.','eas-interactions')
s+=p('Une hypothyroïdie et les autres situations de vulnérabilité sont recherchées avant d’attribuer une nouvelle plainte au seul médicament.','dgn-statine','eas-interactions')
s+=p('Les notices demandent un dosage préalable des CK dans certains terrains prédisposés, notamment atteinte rénale, hypothyroïdie ou antécédent musculaire.','aips83-sortis-prudence','aips83-crestor-prudence')
s+=p('La stratégie respecte les contre-indications de grossesse, allaitement et myopathie au lieu de considérer toutes les statines comme interchangeables.','aips83-sortis-ci','aips83-crestor-ci')
s+=h('Prévention secondaire : reconnaître une atteinte avant ses complications')
s+=p('Le patient est informé de signaler rapidement douleur, faiblesse ou crampes nouvelles, surtout lorsqu’elles s’accompagnent d’un état général altéré.','aips83-sortis-prudence')
s+=p('La mesure des CK est interprétée avec l’activité récente et l’examen, afin de ne pas confondre un signal d’effort avec une toxicité prouvée.','dgn-ck','eas-definition')
s+=p('Le franchissement des conditions d’arrêt du produit et les symptômes importants déclenchent une réévaluation avant une aggravation.','aips83-sortis-prudence','aips83-crestor-prudence')
s+=p('Des urines foncées, une baisse de diurèse ou une faiblesse progressive orientent vers les filières rénale, métabolique ou neuromusculaire appropriées.','rhabdo-s02','dgn-imnm')
s+=h('Prévention tertiaire : éviter une récidive et préserver la fonction')
s+=p('Après un épisode, la cause, les médicaments associés et les conditions de reprise sont consignés pour éviter une réexposition inadaptée.','eas-imputabilite','aips83-sortis-prudence')
s+=p('Une autre statine à faible dose ou une stratégie non statinique peut être choisie lorsque le bénéfice lipidique reste nécessaire.','eas-therapie','esc-nonstatines')
s+=p('La persistance d’une faiblesse ou d’une hyperCKémie conduit à rechercher une cause musculaire sous-jacente plutôt qu’à multiplier les changements sans bilan.','dgn-imnm','dgn-biopsie')
s+=p('Le maintien des activités est ajusté aux capacités, tandis que les limitations professionnelles sont documentées dans le cadre suisse.','cen-myogene-clinique','fmh-evaluation')
s+=w('information','Une information juste participe à la prévention des interruptions inadaptées',[
('Les symptômes musculaires sont fréquents dans les populations traitées et peuvent avoir plusieurs causes.',['eas-frequence','ctt-interpretation']),
('Les résultats contrôlés montrent un petit excès imputable aux statines, sans nier la plainte individuelle ni exclure une atteinte rare grave.',['ctt-interpretation','dgn-statine']),
('La personne sait donc quand consulter, quel traitement elle doit réellement prendre et pourquoi un plan de prévention reste discuté.',['aips83-sortis-prudence','esc-nonstatines']),
('Un symptôme tolérable ne justifie pas une augmentation empirique des suppléments ; mediX déconseille le coenzyme Q10 dans cette indication.',['mdx-sams']),
('Le dialogue porte sur bénéfice, symptômes et préférences, avec un suivi qui permet de modifier la décision sur des constatations nouvelles.',['eas-definition','esc-nonstatines'])])
save(s)

start(13)
s=h('Six décisions à retenir')
for t,ids in [
('Les SAMS décrivent une association entre exposition et symptômes, tandis que la causalité se construit par la clinique, les causes concurrentes et l’évolution.',['eas-definition','eas-imputabilite']),
('Une rhabdomyolyse compliquée ou une faiblesse progressive avec dysphagie fait sortir du parcours de simples symptômes sous traitement.',['rhabdo-s02','dgn-imnm']),
('Sous Sortis ou Crestor, des CK supérieures à 5 fois la limite supérieure imposent l’arrêt ; des symptômes importants peuvent le justifier en dessous.',['aips83-sortis-prudence','aips83-crestor-prudence']),
('Une hypothyroïdie, l’effort et les interactions sont recherchés parce qu’ils peuvent expliquer ou amplifier la plainte musculaire.',['eas-interactions','dgn-statine','dgn-ck']),
('Une réintroduction appropriée attend les conditions de résolution prévues et utilise une faible dose avec surveillance, sans essai improvisé après myopathie grave.',['aips83-sortis-prudence','aips83-crestor-prudence','dgn-imnm']),
('Le suivi préserve un projet de prévention cardiovasculaire tolérable, avec relais spécialisé lorsque la statine seule ne convient pas.',['eas-therapie','esc-nonstatines'])]:s+=p(t,*ids)
save(s)

start(14)
s=h('Questions d’examen : répondre avec une raison clinique')
qs=[
('Une douleur apparaissant sous statine prouve-t-elle sa toxicité ?','Non ; l’association temporelle ne démontre pas, à elle seule, la causalité.','Le profil clinique et les causes concurrentes sont confrontés à l’évolution sous stratégie encadrée.',['eas-definition','eas-imputabilite']),
('Une CK normale exclut-elle les SAMS ?','Non ; de nombreuses plaintes musculaires s’accompagnent de CK normales ou peu augmentées.','La force, le retentissement et les signes de gravité restent examinés.',['eas-definition','dgn-examen']),
('Une hyperCKémie après un effort intense confirme-t-elle une atteinte pharmacologique ?','Non ; l’activité physique peut augmenter les CK indépendamment de la statine.','La chronologie et le contexte du prélèvement sont nécessaires à l’interprétation.',['dgn-ck']),
('Le seuil général de dix fois la norme autorise-t-il à poursuivre Sortis ou Crestor jusqu’à cette valeur ?','Non ; les notices suisses imposent l’arrêt au-delà de 5 fois la limite supérieure.','Les conditions propres au produit ne sont pas remplacées par un autre seuil de recommandation générale.',['dgn-statine','aips83-sortis-prudence','aips83-crestor-prudence']),
('Des symptômes musculaires importants peuvent-ils justifier un arrêt avec des CK inférieures à 5 fois la limite ?','Oui ; les notices envisagent l’arrêt lorsque les symptômes sont importants et constamment gênants.','Le chiffre biologique ne suffit pas à imposer une poursuite automatique.',['aips83-sortis-prudence','aips83-crestor-prudence']),
('Une faiblesse persistante après retrait signifie-t-elle qu’il suffit d’essayer une autre statine ?','Non ; une progression proximale avec dysphagie ou CK très élevées fait rechercher une IMNM.','Les anti-HMGCR et le bilan neuromusculaire participent alors à une filière spécialisée.',['dgn-imnm']),
('La rhabdomyolyse exige-t-elle toujours douleur, faiblesse et urines foncées réunies ?','Non ; la triade complète n’est pas constante.','La suspicion clinique et la recherche des complications rénales ou métaboliques priment sur cette exigence.',['rhabdo-s02']),
('La CK suffit-elle à décider d’une sortie ambulatoire ?','Non ; les constantes, la diurèse, le rein, les électrolytes et les comorbidités comptent aussi.','La gravité ne se réduit pas à une valeur musculaire isolée.',['rhabdo-e13','rhabdo-s02']),
('Un changement vers Crestor supprime-t-il les problèmes d’interaction ?','Non ; cette spécialité possède ses propres transporteurs, restrictions et contre-indications.','La ciclosporine y est contre-indiquée et la fonction rénale modifie les possibilités de prescription.',['aips83-crestor-posologie','aips83-crestor-ci']),
('Le médicament hypolipémiant Ezetrol traite-t-il directement la douleur musculaire ?','Non ; son indication est lipidique et son mécanisme cible l’absorption intestinale du cholestérol.','Il doit être choisi pour le projet de prévention et reste lui-même soumis à une vigilance musculaire.',['aips83-ezetrol-pd','aips83-ezetrol-prudence','esc-nonstatines']),
('La disparition de l’effet musculaire est-elle la seule condition d’une reprise ?','Non ; les contre-indications, les interactions et la normalisation des CK requise sont aussi vérifiées.','La réintroduction utilise un dosage minimal et une surveillance accrue lorsque la situation le permet.',['aips83-sortis-prudence','aips83-crestor-prudence']),
('Une hypothyroïdie est-elle incompatible avec l’hypothèse de symptômes associés aux statines ?','Non ; elle peut fournir une cause musculaire et accroître la vulnérabilité à la toxicité.','Les mécanismes peuvent coexister et leur bilan précède une attribution exclusive.',['dgn-statine','dgn-thyroide']),
('Le coenzyme Q10 est-il indiqué parce que des mécanismes mitochondriaux sont discutés ?','Non ; une hypothèse biologique ne démontre pas l’efficacité clinique d’une supplémentation.','mediX ne recommande pas cette stratégie pour la tolérance statinique.',['eas-mecanisme','eas-complements','mdx-sams']),
('Le schéma adulte de Sortis peut-il être appliqué à un adolescent présentant une myalgie ?','Non ; Sortis n’est pas autorisé chez l’enfant ou l’adolescent.','Une indication pédiatrique précise et ses conditions doivent être vérifiées pour la spécialité réellement choisie.',['aips83-sortis-posologie','aips83-crestor-indications']),
('La grossesse permet-elle une simple poursuite de Sortis ou Crestor sous surveillance ?','Non ; ces spécialités sont contre-indiquées pendant la grossesse et l’allaitement.','Le traitement est réévalué médicalement plutôt que continué sur la seule absence de forte douleur.',['aips83-sortis-ci','aips83-crestor-ci']),
('Le certificat destiné à l’employeur doit-il raconter le diagnostic et les changements de statine ?','Non ; il précise la capacité ou l’incapacité et ses dates dans le respect du secret.','Le cadre ASSM/FMH distingue les informations nécessaires au destinataire.',['fmh-secret','fmh-certificat'])]
s+=rows(['Question','Réponse','Raison ou conduite'],[[ (a,ids),(b,ids),(c,ids)]for a,b,c,ids in qs])
question='Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ?'
s+='<p class="question-finale" id="dx6-question-finale">'+question+cite(['prompt-question-finale'])+'</p>\n'
save(s)

(D/'paquet.json').write_text(json.dumps(P,ensure_ascii=False,indent=2)+'\n')
(D/'contrat.json').write_text(json.dumps(C,ensure_ascii=False,indent=2)+'\n')

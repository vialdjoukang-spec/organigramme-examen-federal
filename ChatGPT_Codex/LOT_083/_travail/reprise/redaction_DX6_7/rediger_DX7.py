from pathlib import Path
import json, html, re
B=Path(__file__).resolve().parent;D=B/'DX.7';F=D/'fragments';F.mkdir(exist_ok=True)
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
 return f'<div class="p" id="dx7-p{N}-f{K}">'+html.escape(t)+cite(ids)+'</div>\n'
def h(t):return '<h4><em>'+html.escape(t)+'</em></h4>\n'
def rows(headers,data):
 return '<div class="t" style="overflow-x:auto"><table><thead><tr>'+''.join('<th>'+html.escape(x)+'</th>'for x in headers)+'</tr></thead><tbody>\n'+''.join('<tr>'+''.join('<td>'+p(t,*ids)+'</td>'for t,ids in row)+'</tr>\n'for row in data)+'</tbody></table></div>\n'
def w(key,title,paras):
 i=f'dx7-p{N}-{key}'
 return f'<button class="w" popovertarget="{i}">{html.escape(title)}</button><div class="fenetre" id="{i}" popover><h4>{html.escape(title)}</h4>\n'+''.join(p(t,*ids)for t,ids in paras)+'</div>\n'
def save(s):
 ids=list(dict.fromkeys(re.findall(r'href="#sb-([\w.\-:]+)"',s)))
 C['points'][str(N)]['citations_autorisees']=ids;P['points'][str(N)]=ids
 (F/f'p{N:02d}.html').write_text(s)
 print(N,len(s.encode()))

start(1)
s=h('La maladie du muscle est replacée dans son contexte hormonal')
s+=p('La Deutsche Gesellschaft für Neurologie décrit en 2025 une atteinte musculaire de l’hypothyroïdie associant surtout parésie proximale, fatigue musculaire et myalgies.','dgn-thyroide','dgn-date')
s+=p('La myopathie hypothyroïdienne désigne cette atteinte du muscle dans un déficit en hormones thyroïdiennes ; une douleur isolée ne suffit pas à l’établir.','dgn-thyroide','cen-myogene-definition','has-clinique')
s+=p('Le référentiel SFE/CEEDMM de 2021 définit l’hypothyroïdie par une insuffisance de sécrétion hormonale, d’origine thyroïdienne ou hypothalamo-hypophysaire.','sfe-definition','sfe-clinique')
s+=p('La forme primaire atteint la glande ; la forme centrale, appelée de préférence insuffisance thyréotrope, concerne sa commande hypothalamo-hypophysaire.','sfe-definition')
s+=p('Une hypothyroïdie primaire patente associe une T4 libre basse à une TSH élevée ; une forme fruste conserve une T4 libre dans la référence.','sfe-definition','has-diagnostic')
s+=p('La démonstration d’une anomalie hormonale et la caractérisation d’un déficit musculaire répondent à deux questions complémentaires.','has-diagnostic','cen-force','dgn-thyroide')
s+=w('termes','Myalgie, fatigue et déficit : préciser ce que le patient éprouve',[
('Une myalgie est une douleur localisée dans le muscle ; elle peut exister avec une force conservée.',['dgn-definition','dgn-examen']),
('Une crampe associe une douleur à une contraction du muscle en boule ; elle se distingue d’une faiblesse mesurée.',['cen-myogene-clinique']),
('La fatigue musculaire rapportée est confrontée aux tâches devenues difficiles, notamment les escaliers, le lever d’un siège et le port de charges.',['dgn-thyroide','cen-myogene-clinique']),
('Le déficit moteur est objectivé par l’examen comparatif et segmentaire ; sa topographie proximale oriente vers le muscle sans déterminer à elle seule sa cause.',['cen-force','cen-myogene-clinique']),
('Une neuropathie peut également accompagner l’hypothyroïdie ; toutes les plaintes neuromusculaires ne relèvent donc pas d’une myopathie pure.',['dgn-thyroide'])])
s+=rows(['Terme','Donnée nécessaire','Conséquence clinique'],[
 [('La myopathie est une affection du muscle.',['cen-myogene-definition']),('Un tableau moteur ou musculaire est recherché et décrit.',['cen-myogene-clinique']),('La fonction thyroïdienne est confrontée au tableau et aux autres causes.',['dgn-thyroide','dgn-labo'])],
 [('L’hypothyroïdie avérée est un diagnostic hormonal.',['has-diagnostic']),('La HAS retient une TSH supérieure à 10 mUI/L et une T4 libre sous l’intervalle de référence.',['has-diagnostic']),('L’indication substitutive est posée après vérification biologique.',['has-therapie'])],
 [('L’hypothyroïdie fruste ne signifie pas une myopathie certaine.',['has-clinique','dgn-thyroide']),('La T4 libre reste normale malgré une TSH durablement au-dessus de la référence.',['has-diagnostic']),('Les symptômes modestes ou absents et les diagnostics concurrents sont pris en compte.',['has-clinique','has-suivi'])],
 [('L’insuffisance thyréotrope peut échapper à une TSH isolée.',['sfe-definition']),('La T4 libre est basse alors que la TSH est inadaptée, parfois normale.',['sfe-definition']),('Le bilan de la commande hypophysaire et des autres fonctions précède une substitution encadrée.',['sfe-central','aips83-euthyrox-prudence'])]])
s+=w('coexistence','Une étiologie endocrinienne peut coexister avec une toxicité médicamenteuse',[
('La DGN classe l’hypothyroïdie parmi les facteurs qui favorisent des complications musculaires sous statine.',['dgn-statine']),
('Une hypothyroïdie retrouvée chez un patient sous statine ne prouve donc pas que le médicament soit sans rôle.',['dgn-statine','dgn-thyroide']),
('Inversement, l’exposition à une statine ne dispense pas du bilan hormonal devant des douleurs ou une faiblesse.',['dgn-statine','dgn-labo']),
('Une faiblesse proximale progressive avec dysphagie et CK très élevées, persistant après retrait de la statine, ouvre la recherche d’une myopathie nécrosante immunomédiée.',['dgn-imnm']),
('La correction thyroïdienne ne remplace pas le traitement spécialisé de cette autre atteinte lorsqu’elle est établie.',['dgn-imnm','has-therapie'])])
s+=p('La CK peut rester normale dans l’atteinte hypothyroïdienne ; son absence d’élévation n’annule ni les symptômes ni la nécessité d’un examen.','dgn-thyroide','dgn-examen')
s+=p('Le syndrome de Hoffmann est une présentation rare, avec pseudohypertrophie musculaire au cours d’une hypothyroïdie prolongée et possibles troubles douloureux de décontraction.','dgn-thyroide')
s+=p('Le coma myxœdémateux et la rhabdomyolyse compliquée sont des sorties de gravité, distinctes de la présentation musculaire stable décrite ici.','sfe-gravite','rhabdo-e13','rhabdo-s02')
save(s)

start(2)
s=h('Distinguer la fréquence du déficit thyroïdien de celle de ses manifestations musculaires')
s+=p('En Suisse, le document clinique Hirslanden décrit une hypothyroïdie acquise plus fréquente avec l’âge et chez les femmes, avec une possible faiblesse musculaire.','ch-hypothyroide')
s+=p('L’algorithme suisse mediX de 2026 intègre les causes auto-immunes, les suites de chirurgie ou d’irradiation et plusieurs traitements susceptibles de provoquer un déficit.','mdx-thyroide','mdx-thyroide-date')
s+=p('Ces populations à risque orientent le dépistage devant une plainte musculaire ; elles ne définissent pas, à elles seules, la cause de chaque myalgie.','mdx-thyroide','has-clinique','dgn-thyroide')
s+=p('La DGN rapporte en 2025 des symptômes neuromusculaires chez 30–80 % des patients ayant une hypothyroïdie symptomatique.','dgn-thyroide','dgn-date')
s+=p('Ce dénominateur concerne des patients déjà symptomatiques ; le numérateur regroupe faiblesse, fatigue, myalgies et parfois neuropathies.','dgn-thyroide')
s+=p('La plage ne mesure donc ni la prévalence d’une myopathie isolée dans toute la population, ni un risque national suisse.','dgn-thyroide')
s+=rows(['Chiffre publié','Population concernée','Lecture et date'],[
 [('La DGN cite 30–80 % de manifestations neuromusculaires.',['dgn-thyroide']),('Il s’agit de patients présentant une hypothyroïdie symptomatique.',['dgn-thyroide']),('La recommandation de 2025 regroupe plusieurs manifestations, dont la polyneuropathie.',['dgn-date','dgn-thyroide'])],
 [('Le référentiel SFE indique moins de 2 % de formes primaires patentes.',['sfe-epidemio']),('Le chiffre porte sur l’hypothyroïdie primaire, pas sur sa complication musculaire.',['sfe-epidemio']),('Le support CEEDMM de 2021 fournit un contexte endocrinologique européen.',['sfe-clinique','sfe-epidemio'])],
 [('La forme fruste est rapportée chez 7,5 % des femmes et 3 % des hommes.',['sfe-epidemio']),('Les proportions décrivent un état hormonal fréquemment peu symptomatique.',['sfe-epidemio','has-clinique']),('Ces chiffres SFE ne deviennent pas une fréquence de faiblesse musculaire.',['sfe-epidemio','dgn-thyroide'])],
 [('La SFE rapporte 10 % de formes frustes chez les sujets âgés.',['sfe-epidemio']),('La TSH augmente aussi avec l’âge et peut surestimer cette prévalence.',['sfe-epidemio','has-age']),('L’interprétation exige une référence adaptée et une décision distincte du simple dépassement.',['has-age'])],
 [('L’insuffisance thyréotrope représente moins de 5 % des hypothyroïdies.',['sfe-epidemio']),('Cette proportion concerne la répartition des causes du déficit hormonal.',['sfe-epidemio']),('Sa rareté ne permet pas de l’exclure devant une TSH normale et une T4 libre basse.',['sfe-definition'])]])
s+=w('risques','Les groupes à risque changent les questions posées',[
('Une thyroïdite auto-immune, une thyroïdectomie ou une irradiation expliquent des situations dans lesquelles la production hormonale peut diminuer.',['mdx-thyroide','ch-hypothyroide']),
('Le lithium, l’amiodarone, les antithyroïdiens et certaines immunothérapies figurent dans les causes iatrogènes de l’algorithme mediX.',['mdx-thyroide']),
('Le diabète de type 1, la trisomie 21 et le syndrome de Turner sont associés à une fréquence accrue de formes frustes dans le référentiel SFE.',['sfe-epidemio']),
('Un antécédent hypophysaire, une chirurgie de cette région ou un traumatisme crânien justifie de penser à une insuffisance thyréotrope.',['sfe-central']),
('Chez la personne âgée, une hausse modérée et isolée de TSH ne suffit pas à décider d’une substitution.',['has-age','aips83-euthyrox-posologie'])])
s+=h('L’histoire naturelle dépend de la profondeur, de la durée et de la cause')
s+=p('La sémiologie devient plus marquée selon la profondeur et l’ancienneté du déficit ; les formes frustes restent souvent pauci- ou asymptomatiques.','sfe-clinique','has-clinique')
s+=p('Le dosage hormonal permet actuellement un diagnostic plus précoce, ce qui rend les formes compliquées moins souvent observées.','sfe-epidemio','sfe-gravite')
s+=p('Une hypothyroïdie prolongée peut produire un tableau proximal ou une pseudohypertrophie rare ; une rhabdomyolyse a également été décrite.','dgn-thyroide')
s+=p('Le coma myxœdémateux est rare mais de pronostic sévère ; sa reconnaissance ne repose pas sur le calcul d’une mortalité individuelle.','sfe-gravite')
s+=p('Le traitement vise une correction hormonale accompagnée d’une amélioration clinique ; une persistance des symptômes conduit à reprendre le diagnostic différentiel.','has-therapie','has-suivi')
s+=w('enjeux','L’enjeu de santé publique associe diagnostic et prévention du surtraitement',[
('Une plainte banale de fatigue ou de crampes peut révéler un déficit hormonal, mais ces symptômes restent non spécifiques.',['has-clinique']),
('L’association de signes augmente la probabilité clinique sans remplacer les dosages.',['has-clinique']),
('La répétition d’une TSH modérément élevée évite de traiter une variation transitoire comme une maladie permanente.',['has-diagnostic']),
('À l’inverse, une exploration limitée à la TSH manque certaines atteintes centrales ; le contexte hypophysaire impose la T4 libre d’emblée.',['has-diagnostic','sfe-definition']),
('Un traitement excessif expose notamment à des complications cardiaques et osseuses, ce qui justifie une titration et une surveillance individualisées.',['aips83-euthyrox-prudence','has-age'])])
save(s)

start(3)
s=h('Le déficit hormonal modifie le fonctionnement énergétique du muscle')
s+=p('Les hormones thyroïdiennes interviennent dans le métabolisme des protéines, des lipides et des glucides, ainsi que dans la fonction mitochondriale musculaire.','dgn-thyroide')
s+=p('Le déficit perturbe donc plusieurs fonctions du myocyte ; la fatigue, les myalgies et la parésie proximale en constituent des manifestations cliniques possibles.','dgn-thyroide')
s+=p('La lévothyroxine synthétique est identique à la T4 endogène et exerce ses effets par des interactions ligand-récepteur dans les noyaux, mitochondries et microsomes.','aips83-euthyrox-pd')
s+=p('Son action augmente la production énergétique et thermique et influence les métabolismes protéique, glucidique et lipidique.','aips83-euthyrox-pd')
s+=p('La substitution traite le déficit causal ; elle ne sert pas à augmenter la performance musculaire d’une personne euthyroïdienne.','aips83-euthyrox-indications','aips83-euthyrox-prudence')
s+=w('axe','Comprendre le couple TSH–T4 libre',[
('La TSH reflète la stimulation hypophysaire de la thyroïde ; sa hausse dans l’atteinte primaire traduit la levée du rétrocontrôle hormonal.',['sfe-definition']),
('La T4 libre mesure la fraction hormonale disponible sans reprendre les variations de la T4 totale liées aux protéines de transport.',['sfe-definition']),
('Une TSH augmentée avec T4 libre basse concorde avec un déficit primaire patent.',['sfe-definition','has-diagnostic']),
('Une T4 libre basse avec TSH basse, normale ou insuffisamment augmentée fait rechercher une atteinte centrale.',['sfe-definition']),
('Dans certaines atteintes hypothalamiques, une TSH mesurée légèrement élevée peut être biologiquement peu active ; la lecture isolée de son chiffre devient trompeuse.',['sfe-definition'])])
s+=rows(['Perturbation','Exploration qui la documente','Traitement ou décision reliée au mécanisme'],[
 [('La production thyroïdienne devient insuffisante.',['sfe-definition']),('La TSH puis la T4 libre caractérisent le déficit primaire.',['has-diagnostic']),('La lévothyroxine remplace l’hormone manquante après confirmation.',['has-therapie','aips83-euthyrox-indications'])],
 [('La commande hypothalamo-hypophysaire ne répond pas correctement au déficit.',['sfe-definition']),('La T4 libre est interprétée avec la TSH et le contexte hypophysaire.',['sfe-definition','has-diagnostic']),('La cause centrale et les autres axes hormonaux sont évalués avant une substitution spécialisée.',['sfe-central','aips83-euthyrox-prudence'])],
 [('Le métabolisme du muscle et sa fonction mitochondriale sont perturbés.',['dgn-thyroide']),('La force proximale, les gestes fonctionnels et le retentissement sont décrits.',['dgn-thyroide','cen-myogene-clinique']),('La correction hormonale est confrontée à l’évolution fonctionnelle, sans promettre un délai fixe de récupération.',['has-therapie','has-suivi'])],
 [('Une atteinte de la fibre peut augmenter les enzymes musculaires.',['sfe-biologie','dgn-thyroide']),('La CK renseigne une souffrance musculaire mais peut rester normale.',['dgn-thyroide']),('Une élévation importante impose une recherche de lyse et de complications ; elle ne dicte pas seule la dose de T4.',['rhabdo-s02','aips83-euthyrox-posologie'])],
 [('L’absorption de la T4 est diminuée par certains aliments ou médicaments.',['aips83-euthyrox-pk','aips83-euthyrox-interactions']),('L’entretien vérifie les horaires, les sels de fer ou de calcium, les résines et les traitements gastriques.',['aips83-euthyrox-interactions']),('La prise est organisée selon l’AIPS avant d’augmenter une dose sur un résultat instable.',['aips83-euthyrox-posologie','has-suivi'])],
 [('Une quantité excessive de T4 stimule trop fortement les tissus.',['aips83-euthyrox-prudence']),('Les palpitations, le tremblement, les sueurs et les signes biologiques orientent le contrôle.',['aips83-euthyrox-ei','has-suivi']),('La dose est revue ou temporairement interrompue médicalement selon la notice et la gravité.',['aips83-euthyrox-prudence'])]])
s+=h('La CK et la force donnent des informations différentes')
s+=p('La CK est un marqueur musculaire, tandis que la cotation de force mesure une fonction ; leurs anomalies ne sont pas obligatoirement parallèles.','dgn-ck','dgn-thyroide','cen-force')
s+=p('La DGN admet explicitement une CK normale dans l’hypothyroïdie avec symptômes musculaires ; cette valeur ne constitue donc pas un test d’exclusion.','dgn-thyroide')
s+=p('Une augmentation des ASAT peut accompagner celle des enzymes musculaires ; elle est relue avec le contexte et le reste du bilan.','sfe-biologie','dgn-labo')
s+=p('Un effort récent, des médicaments et d’autres maladies musculaires modifient aussi la CK ; une élévation n’est pas une signature endocrinienne spécifique.','dgn-ck','dgn-toxique','dgn-labo')
s+=w('maintien','Ce qui peut maintenir les symptômes malgré une ordonnance',[
('Une prise irrégulière ou une prise au moment d’un repas peut empêcher l’exposition hormonale prévue.',['aips83-euthyrox-pk','has-suivi']),
('Les sels de fer, de calcium et les produits contenant de l’aluminium diminuent l’absorption ; les horaires doivent être vérifiés concrètement.',['aips83-euthyrox-interactions']),
('Les inhibiteurs de la pompe à protons peuvent réduire l’absorption par modification du pH gastrique et justifient une surveillance adaptée.',['aips83-euthyrox-interactions']),
('Une maladie cœliaque, une chirurgie bariatrique ou d’autres affections digestives peuvent contribuer à une mauvaise équilibration.',['has-suivi']),
('Une biotine prise comme complément peut fausser le dosage sans refléter une vraie variation hormonale ; le laboratoire doit en être informé.',['aips83-euthyrox-prudence','has-suivi']),
('Une autre cause de faiblesse, notamment une atteinte toxique ou immunomédiée, peut persister indépendamment de la correction thyroïdienne.',['dgn-toxique','dgn-imnm','has-suivi'])])
s+=h('Le mécanisme hormonal ne justifie pas toutes les interventions possibles')
s+=p('La HAS retient la lévothyroxine seule comme traitement de référence de l’hypothyroïdie primaire avérée.','has-therapie')
s+=p('Une association avec la T3 relève d’une évaluation endocrinologique lorsqu’elle est envisagée ; elle n’est pas déduite d’une simple fatigue persistante.','has-specialiste','has-suivi')
s+=p('L’auto-immunité thyroïdienne documentée par les anti-TPO décrit une cause endocrinienne ; elle ne démontre pas une myosite nécessitant une immunosuppression.','has-anticorps','dgn-imnm')
s+=p('Le raisonnement relie donc chaque anomalie à son domaine : hormones pour le déficit, force pour la fonction et bilan neuromusculaire pour une atteinte discordante.','has-diagnostic','cen-force','dgn-emg')
save(s)

start(4)
s=h('La première bifurcation recherche une menace vitale ou fonctionnelle')
s+=p('Une myopathie hypothyroïdienne stable peut être explorée en consultation ; un coma, une défaillance respiratoire ou une complication de lyse musculaire change immédiatement le circuit.','sfe-gravite','rhabdo-e13','rhabdo-s02')
s+=p('La gravité est appréciée sur la conscience, la respiration, la circulation, la diurèse et les complications métaboliques, avant de discuter une titration orale.','sfe-gravite','rhabdo-e13','aips83-euthyrox-posologie')
s+=rows(['Diagnostic ou sortie','Élément qui départage','Piège','Conduite si positif'],[
 [('🚩 La décompensation myxœdémateuse est une urgence vitale.',['sfe-gravite','ch-hypothyroide']),('Une somnolence majeure ou un coma avec hypothermie, bradycardie, bradypnée ou hypotension est évocateur.',['sfe-gravite']),('Il ne faut pas attendre un chiffre de TSH pour prendre en charge les défaillances.',['sfe-gravite','ch-hypothyroide']),('Une prise en charge hospitalière immédiate remplace le protocole oral ambulatoire.',['ch-hypothyroide','aips83-euthyrox-posologie'])],
 [('🚩 La rhabdomyolyse compliquée ouvre une sortie E1.',['rhabdo-e13','rhabdo-s02']),('Des douleurs ou une faiblesse importantes avec oligo-anurie, anomalies ioniques ou atteinte rénale imposent le bilan de gravité.',['rhabdo-e13','rhabdo-s02']),('La triade complète douleur, faiblesse et urines foncées peut manquer.',['rhabdo-s02']),('Les constantes, le rein, les électrolytes et les complications cardiaques sont évalués en urgence.',['rhabdo-e13','rhabdo-s11'])],
 [('Une myopathie nécrosante immunomédiée doit être distinguée d’une atteinte endocrine seule.',['dgn-imnm']),('Sous statine, une faiblesse proximale ou axiale progressive, une dysphagie et des CK très élevées orientent vers cette cause.',['dgn-imnm']),('L’arrêt de la statine peut ne pas faire régresser les symptômes ; une hypothyroïdie associée ne suffit pas à clore le bilan.',['dgn-imnm','dgn-statine']),('Le bilan spécialisé recherche notamment les anti-HMGCR et discute la biopsie et le traitement spécifique.',['dgn-imnm'])],
 [('Une atteinte toxique médicamenteuse peut coexister avec le déficit thyroïdien.',['dgn-statine','dgn-thyroide']),('La chronologie des traitements, les interactions, la force et les CK sont confrontées.',['dgn-anamnese','dgn-toxique']),('Une hormone anormale ne disculpe pas automatiquement la statine.',['dgn-statine','dgn-thyroide']),('La notice du produit est appliquée et les autres causes sont corrigées ; sous Sortis, la CK et les symptômes guident l’arrêt.',['aips83-sortis-prudence','dgn-statine'])]])
s+=w('urgence','Urgence — les premières décisions suivent la défaillance observée',[
('La conscience, la température, le pouls, la pression et la respiration sont appréciés immédiatement lorsque le tableau évoque une décompensation sévère.',['sfe-gravite','rhabdo-e13']),
('Une altération de conscience avec hypothermie et ralentissement cardiorespiratoire impose une orientation hospitalière urgente pour suspicion de coma myxœdémateux.',['sfe-gravite','ch-hypothyroide']),
('Devant une suspicion de rhabdomyolyse, la CK, la créatinine, les électrolytes et la diurèse sont évalués avec les constantes.',['rhabdo-s02','rhabdo-e13']),
('Une hyperkaliémie peut évoluer rapidement ; les manifestations électriques et le contexte clinique commandent la surveillance et le traitement spécialisés.',['rhabdo-s11']),
('Un syndrome de loge ou une menace rénale et métabolique ne doit pas être traité comme une simple douleur endocrine à revoir tardivement.',['rhabdo-e13','rhabdo-s03']),
('Le schéma d’augmentation orale d’Euthyrox décrit pour l’hypothyroïdie usuelle ne constitue pas un protocole de réanimation du coma.',['aips83-euthyrox-posologie','sfe-gravite'])])
s+=h('La sécurité endocrinienne précède la première dose')
s+=p('Une atteinte hypophysaire ou surrénalienne non traitée est une contre-indication d’Euthyrox ; son origine doit être évaluée avant substitution.','aips83-euthyrox-ci','aips83-euthyrox-prudence')
s+=p('Lorsque la fonction surrénalienne nécessite une substitution, les glucocorticoïdes sont institués avant l’hormone thyroïdienne selon la notice.','aips83-euthyrox-prudence')
s+=p('Une cardiopathie ischémique, une insuffisance cardiaque ou une tachyarythmie modifie aussi la préparation et la surveillance du traitement.','aips83-euthyrox-prudence','has-specialiste')
s+=w('discrimination','La concordance utile ne repose pas sur une seule donnée',[
('Une douleur diffuse avec frilosité, constipation récente et ralentissement motive le bilan thyroïdien, sans valider d’emblée son résultat causal.',['has-clinique']),
('Une parésie proximale objectivée rend l’exploration musculaire plus importante qu’une fatigue seulement décrite.',['cen-force','cen-myogene-clinique','dgn-examen']),
('Une perte sensitive ou une aréflexie peut orienter vers une composante neuropathique ; la DGN rappelle que celle-ci peut aussi accompagner l’hypothyroïdie.',['cen-myogene-clinique','cen-rot','dgn-thyroide']),
('Une progression malgré une bonne équilibration hormonale impose de reprendre les hypothèses plutôt que d’augmenter sans fin la T4.',['has-suivi','dgn-imnm']),
('L’urgence et le diagnostic étiologique sont donc deux décisions distinctes : un bilan thyroïdien positif ne neutralise aucun drapeau rouge.',['sfe-gravite','rhabdo-e13','dgn-thyroide'])])
save(s)

start(5)
s=h('L’entretien reconstruit le retentissement et les causes possibles du déficit')
s+=p('Le patient décrit les régions douloureuses, la date de début, l’évolution et le lien avec les efforts ; ces données distinguent une plainte diffuse d’un déficit progressif.','dgn-anamnese','dgn-examen')
s+=p('Les difficultés pour monter un escalier, se relever ou porter une charge recherchent le retentissement proximal, ensuite vérifié à l’examen.','cen-myogene-clinique')
s+=p('La frilosité acquise, la constipation récente, la somnolence, le ralentissement et la peau sèche sont recherchés ensemble car chaque signe est peu spécifique.','has-clinique','sfe-clinique')
s+=rows(['Question ciblée','Raison de la question','Conséquence pratique'],[
 [('Le patient distingue-t-il douleur, crampe, manque d’endurance et incapacité à accomplir un geste ?',['dgn-anamnese','cen-myogene-clinique']),('Ces plaintes ne mesurent pas toutes la même fonction musculaire.',['cen-force','cen-myogene-clinique']),('Le geste déficitaire est observé et coté, au lieu d’être seulement nommé fatigue.',['cen-force'])],
 [('Existe-t-il une chirurgie thyroïdienne, une irradiation ou une maladie auto-immune connue ?',['mdx-thyroide']),('Ces événements peuvent expliquer une diminution durable de production hormonale.',['mdx-thyroide','ch-hypothyroide']),('La chronologie du déficit et les anciens dosages sont recherchés.',['dgn-anamnese','has-diagnostic'])],
 [('Le traitement comprend-il lithium, amiodarone, antithyroïdien ou immunothérapie ?',['mdx-thyroide']),('Certaines hypothyroïdies sont iatrogènes.',['mdx-thyroide']),('La surveillance hormonale et la décision thérapeutique sont adaptées au médicament concerné.',['has-age','mdx-thyroide'])],
 [('Une statine a-t-elle été débutée, augmentée ou associée à un nouveau médicament ?',['dgn-statine','dgn-anamnese']),('Le déficit thyroïdien peut augmenter la vulnérabilité musculaire sous statine.',['dgn-statine']),('Le bilan recherche à la fois une composante endocrine et une toxicité médicamenteuse.',['dgn-statine','dgn-thyroide'])],
 [('Le patient prend-il déjà de la T4, et comment la prend-il exactement ?',['has-suivi']),('Les repas, les omissions et les interactions modifient l’exposition.',['aips83-euthyrox-posologie','aips83-euthyrox-interactions']),('Les horaires et les produits associés sont corrigés avant une majoration injustifiée.',['has-suivi'])],
 [('Une maladie hypophysaire, un traumatisme crânien ou d’autres troubles hormonaux sont-ils présents ?',['sfe-central','has-specialiste']),('Une commande centrale déficiente peut laisser la TSH normale malgré une T4 libre basse.',['sfe-definition']),('La TSH et la T4 libre sont dosées ensemble et le bilan endocrinologique est organisé.',['has-diagnostic','sfe-central'])]])
s+=w('medicaments','Faire préciser une journée réelle de traitement',[
('L’entretien demande à quel moment la T4 est avalée, avec quel repas ou quelle boisson, et quels autres comprimés sont pris ensemble.',['aips83-euthyrox-posologie','aips83-euthyrox-pk','has-suivi']),
('Le fer, le calcium, les produits contenant de l’aluminium et les résines sont nommés explicitement ; le patient peut ne pas les considérer comme des médicaments.',['aips83-euthyrox-interactions']),
('L’introduction ou l’arrêt d’un inhibiteur de pompe à protons peut modifier l’équilibre et justifie une réévaluation clinique et biologique.',['aips83-euthyrox-interactions']),
('Les compléments à base de biotine sont recherchés parce qu’ils peuvent fausser les immunodosages.',['aips83-euthyrox-prudence']),
('Les difficultés d’adhésion sont abordées sans les confondre avec une résistance pharmacologique ; les modalités de prise font partie du diagnostic d’un déséquilibre.',['has-suivi'])])
s+=rows(['Drapeau rouge','Ce qu’il fait craindre','Action déclenchée'],[
 [('Une somnolence croissante, une hypothermie ou une respiration anormalement lente est rapportée.',['sfe-gravite','ch-hypothyroide']),('Une décompensation myxœdémateuse peut engager le pronostic vital.',['sfe-gravite']),('Une évaluation urgente et une orientation hospitalière sont organisées.',['ch-hypothyroide'])],
 [('Les urines deviennent foncées ou très rares dans un tableau musculaire important.',['rhabdo-e13','rhabdo-s02']),('Une rhabdomyolyse avec complication rénale ou métabolique est possible.',['rhabdo-s02']),('La diurèse, la fonction rénale et les électrolytes sont évalués sans attendre le contrôle thyroïdien programmé.',['rhabdo-e13','rhabdo-s02'])],
 [('La faiblesse progresse et la déglutition devient difficile, notamment sous statine.',['dgn-imnm']),('Une myopathie immunomédiée ou une autre atteinte neuromusculaire sévère est possible.',['dgn-imnm']),('Le patient est adressé rapidement à une filière spécialisée selon la gravité fonctionnelle.',['dgn-imnm','rhabdo-e13'])],
 [('Une douleur thoracique ou des palpitations surviennent à l’introduction de T4.',['aips83-euthyrox-ei','sfe-gravite']),('Une complication cardiaque ou une stimulation excessive doit être évaluée.',['aips83-euthyrox-prudence','aips83-euthyrox-ei']),('La situation clinique est réévaluée immédiatement et la prescription est revue médicalement.',['aips83-euthyrox-prudence'])],
 [('Un antécédent hypophysaire est associé à des résultats hormonaux discordants.',['sfe-definition','sfe-central']),('Une insuffisance thyréotrope avec autre déficit hormonal peut être méconnue.',['sfe-central']),('L’exploration endocrine précède une substitution non encadrée.',['aips83-euthyrox-ci','aips83-euthyrox-prudence'])]])
s+=p('L’anamnèse précise aussi grossesse, projet de grossesse ou allaitement, car la substitution se poursuit mais requiert un suivi adapté.','aips83-euthyrox-grossesse','has-specialiste')
s+=p('Le métier, les déplacements, les escaliers et les tâches dangereuses sont décrits afin d’évaluer les capacités résiduelles et le besoin d’adaptation.','fmh-evaluation','cen-myogene-clinique')
save(s)

start(6)
s=h('L’examen commence par une description de la normalité')
s+=p('Une force normale correspond au grade 5 de l’échelle segmentaire du CEN ; chaque groupe musculaire testé est comparé au côté opposé.','cen-force')
s+=p('Une contraction idiomusculaire normale est déclenchée par percussion directe du muscle, puis se relâche rapidement.','cen-myogene-clinique')
s+=p('Au genou, la réponse rotulienne attendue associe contraction du quadriceps et extension ; au tendon d’Achille, la réponse associe contraction surale et flexion plantaire.','cen-rot')
s+=p('Les réflexes s’interprètent avec leur symétrie, le reste de l’examen et les variations constitutionnelles, plutôt qu’avec une exigence uniforme de vivacité.','cen-rot')
s+=p('Dans un syndrome myogène pur, la sensibilité est conservée, les réflexes ostéotendineux ne sont habituellement pas abolis et les fasciculations manquent.','cen-myogene-clinique')
s+=w('force','Comment décrire et coter la force',[
('L’examen global des membres supérieurs utilise les bras tendus à l’horizontale.',['cen-force']),
('Aux membres inférieurs, Mingazzini s’effectue en décubitus dorsal, cuisses verticales et jambes horizontales.',['cen-force']),
('La manœuvre de Barré s’effectue en décubitus ventral, jambes à la verticale.',['cen-force']),
('Le maintien est observé pendant 10–20 secondes avant de conclure à l’absence de déficit.',['cen-force']),
('L’examen segmentaire complète cette appréciation en testant l’action de chaque muscle et en comparant droite et gauche.',['cen-force']),
('Le grade 0 signifie absence de contraction ; le grade 1, contraction sans effet moteur.',['cen-force']),
('Le grade 2 correspond à un déplacement sans vaincre la pesanteur ; le grade 3, à un mouvement contre la pesanteur.',['cen-force']),
('Le grade 4 correspond à un mouvement contre résistance et le grade 5 à la force normale.',['cen-force'])])
s+=h('Ceinture pelvienne et musculature axiale')
s+=p('Le lever d’un siège, la marche et le relever de la position accroupie recherchent un retentissement proximal dans des gestes courants.','cen-myogene-clinique')
s+=p('Un patient myopathe peut s’aider des mains sur les genoux puis remonter le long des cuisses ; l’observation est décrite sans en déduire une étiologie unique.','cen-myogene-clinique')
s+=p('La marche dandinante et une hyperlordose peuvent accompagner une atteinte de ceinture ou paravertébrale, mais ne sont pas obligatoires.','cen-myogene-clinique')
s+=p('Le résultat fonctionnel est confronté à la douleur et à l’examen segmentaire : une tâche interrompue parce qu’elle fait mal n’équivaut pas à une cotation complète.','dgn-examen','cen-force')
s+=w('palpation','Palper et percuter le muscle avec une question précise',[
('La palpation manuelle recherche une douleur à la pression du corps musculaire ; la région et le côté sont précisés.',['dgn-examen']),
('Une douleur du corps musculaire peut accompagner certaines myopathies, tandis que des points déclencheurs orientent vers un syndrome myofascial.',['dgn-examen']),
('La percussion directe renseigne la contraction idiomusculaire et sa décontraction ; elle ne remplace pas le test de force volontaire.',['cen-myogene-clinique','cen-force']),
('Une décontraction lente après serrage de la main ou après percussion thénarienne correspond à un phénomène myotonique clinique.',['cen-myogene-clinique']),
('Dans la présentation générale du CEN, la myotonie est habituellement indolore ; la DGN décrit cependant de possibles myotonies douloureuses dans le rare syndrome de Hoffmann.',['cen-myogene-clinique','dgn-thyroide']),
('Le volume musculaire est inspecté car une pseudohypertrophie ne signifie pas une force augmentée.',['dgn-thyroide','cen-myogene-clinique'])])
s+=h('Ceinture scapulaire, nuque et territoires distaux')
s+=p('Les deltoïdes, biceps, triceps et fléchisseurs de la nuque sont inclus dans l’examen d’une faiblesse proximale ou axiale.','cen-myogene-clinique')
s+=p('Un décollement de l’omoplate et d’autres anomalies de répartition sont notés lorsqu’ils sont présents ; ils élargissent la description musculaire.','cen-myogene-clinique')
s+=p('Les territoires distaux, la sensibilité et les réflexes aident à repérer une composante neurologique associée plutôt qu’à imposer un tableau myogène pur.','cen-myogene-clinique','cen-rot','dgn-thyroide')
s+=rows(['Geste','Réponse ou observation attendue','Anomalie utile et limite'],[
 [('Le tendon rotulien est percuté chez le patient assis, jambes pendantes, ou couché avec la jambe soutenue en semi-flexion.',['cen-rot']),('La contraction du quadriceps entraîne une extension du genou.',['cen-rot']),('Une réponse lente est décrite dans les formes hypothyroïdiennes sévères, mais aucun réflexe isolé ne confirme le diagnostic hormonal.',['sfe-gravite','has-clinique'])],
 [('Le tendon d’Achille est percuté pour examiner la réponse surale.',['cen-rot']),('La flexion plantaire accompagne la contraction du triceps sural.',['cen-rot']),('Une réponse faible ou absente est relue avec le contexte, car elle peut être constitutionnelle ou liée à une atteinte de l’arc réflexe.',['cen-rot'])],
 [('Le tendon bicipital est examiné avec l’avant-bras en semi-flexion et supination ; le marteau percute le pouce placé sur le tendon.',['cen-rot']),('La réponse est une contraction du biceps avec flexion du coude.',['cen-rot']),('La comparaison avec l’autre côté participe à la recherche d’une distribution neurologique.',['cen-force','cen-rot'])],
 [('Le patient serre puis relâche la main, ou l’examinateur percute l’éminence thénar.',['cen-myogene-clinique']),('La décontraction normale est rapide après la contraction.',['cen-myogene-clinique']),('Un relâchement retardé est un signe à caractériser ; il ne suffit pas à diagnostiquer une maladie génétique ni un syndrome de Hoffmann.',['cen-myogene-clinique','dgn-thyroide'])]])
s+=h('Peau, cou et état général complètent la lecture musculaire')
s+=p('La peau sèche, les cheveux cassants, le gonflement des paupières et la voix rauque renforcent une hypothèse endocrine lorsqu’ils sont associés.','has-clinique','sfe-clinique')
s+=p('La palpation thyroïdienne recherche notamment une augmentation de volume, une consistance ferme ou une hétérogénéité ; le résultat dépend de la cause.','sfe-morphologie')
s+=p('Une thyroïde de taille normale, diminuée ou à peine palpable n’exclut pas une hypothyroïdie, notamment atrophique ou centrale.','sfe-morphologie')
s+=p('La conscience, la température, le pouls, la respiration et la pression sont confrontés aux signes musculaires pour repérer une décompensation sévère.','sfe-gravite','rhabdo-e13')
s+=p('Une atteinte cutanée de type héliotrope ou des lésions de Gottron font rechercher une autre myopathie inflammatoire plutôt que tout attribuer à la thyroïde.','dgn-examen')
s+=p('Le compte rendu conserve la topographie, la cotation, la douleur provoquée, les réflexes et le retentissement fonctionnel comme état de référence pour le suivi.','cen-force','cen-myogene-clinique','has-suivi')
save(s)

start(7)
s=h('7.1 — Le syndrome douloureux et de fatigabilité musculaire')
s+=p('Les signes fonctionnels peuvent associer myalgies, crampes, enraidissement et fatigue musculaire ; leur intensité ne se déduit pas d’un seul dosage.','dgn-thyroide','sfe-clinique')
s+=p('Les signes physiques recherchés sont une sensibilité musculaire à la palpation et un éventuel déficit objectivable, qui ne sont pas systématiquement réunis.','dgn-examen','dgn-thyroide','cen-force')
s+=w('douleur','Définir la douleur et la crampe puis les rechercher',[
('La myalgie est une douleur ressentie dans le muscle ; l’entretien précise siège, durée, déclenchement et évolution.',['dgn-definition','dgn-anamnese']),
('La crampe associe une contraction en boule à la plainte douloureuse ; elle est recherchée dans le récit et, si elle survient, observée.',['cen-myogene-clinique']),
('La palpation du corps musculaire recherche une douleur provoquée, en distinguant une sensibilité diffuse de points myofasciaux.',['dgn-examen']),
('Le mécanisme endocrinien est recherché car les hormones thyroïdiennes régulent le métabolisme et la fonction mitochondriale du muscle.',['dgn-thyroide']),
('Aucune de ces observations ne devient à elle seule un critère biologique de déficit thyroïdien.',['has-clinique','has-diagnostic'])])
s+=h('7.2 — Le syndrome moteur proximal')
s+=p('Le patient décrit une difficulté dans les escaliers, au lever d’un siège ou pour porter ; le signe physique est une faiblesse proximale, souvent bilatérale.','cen-myogene-clinique','dgn-thyroide')
s+=p('La force segmentaire et les gestes fonctionnels documentent ce syndrome, tandis que la biologie identifie ou non une cause endocrine compatible.','cen-force','has-diagnostic')
s+=w('proximal','Ce que signifie une parésie proximale',[
('La parésie est une diminution de force objectivée ; elle se distingue d’un simple sentiment de fatigue.',['cen-force','cen-myogene-clinique']),
('La topographie proximale concerne principalement les racines des membres et parfois les muscles axiaux.',['cen-myogene-clinique']),
('Le lever du siège et le relever accroupi explorent la ceinture pelvienne ; l’aide des mains sur les cuisses est un signe de compensation.',['cen-myogene-clinique']),
('Les deltoïdes, biceps, triceps et fléchisseurs du cou complètent l’examen des ceintures et de l’axe.',['cen-myogene-clinique']),
('La cotation de chaque groupe permet de comparer l’évolution sous correction hormonale, sans transformer la topographie en preuve étiologique.',['cen-force','has-suivi','dgn-thyroide'])])
s+=h('7.3 — Le syndrome de pseudohypertrophie et de décontraction anormale')
s+=p('Le rare syndrome de Hoffmann apparaît au cours d’une hypothyroïdie prolongée avec pseudohypertrophie musculaire et possibles myotonies douloureuses.','dgn-thyroide')
s+=p('Le signe fonctionnel peut être une difficulté de relâchement ; l’inspection et les manœuvres de décontraction recherchent les anomalies physiques correspondantes.','dgn-thyroide','cen-myogene-clinique')
s+=w('hoffmann','Volume et relâchement : deux observations différentes',[
('La pseudohypertrophie désigne ici l’augmentation apparente du volume musculaire décrite par la DGN ; elle ne signifie pas un gain de puissance.',['dgn-thyroide','cen-myogene-clinique']),
('L’examen inspecte le volume puis mesure séparément la force.',['cen-myogene-clinique','cen-force']),
('La myotonie clinique est un retard de décontraction après une contraction volontaire ou une percussion.',['cen-myogene-clinique']),
('Le serrage-relâchement de la main et la percussion thénarienne permettent de décrire ce retard sans conclure d’emblée à une maladie héréditaire.',['cen-myogene-clinique']),
('Le contexte prolongé d’hypothyroïdie est nécessaire à l’hypothèse de Hoffmann ; une autre myopathie reste recherchée devant un profil atypique.',['dgn-thyroide','dgn-labo'])])
s+=h('7.4 — Le syndrome d’hypométabolisme associé')
s+=p('La frilosité acquise, la constipation récente, la somnolence et le ralentissement sont des signes fonctionnels qui rendent le contexte endocrinien plus cohérent.','sfe-clinique','has-clinique')
s+=p('La peau sèche, la bradycardie, le gonflement palpébral ou la voix rauque sont recherchés comme signes physiques associés.','sfe-clinique','has-clinique')
s+=p('Leur association augmente la probabilité d’une hypothyroïdie ; leur non-spécificité impose toujours la confirmation hormonale.','has-clinique')
s+=w('hypometabolisme','Définir le ralentissement sans banaliser une défaillance',[
('La frilosité acquise correspond à une sensibilité au froid nouvellement présente ; son caractère récent est confronté aux autres signes.',['sfe-clinique','has-clinique']),
('La constipation acquise est distinguée d’un transit lent ancien ; elle participe à un faisceau clinique.',['sfe-clinique']),
('La baisse de production énergétique et thermique donne un cadre physiopathologique à cet ensemble de manifestations.',['aips83-euthyrox-pd','sfe-clinique']),
('Une hypothermie avec altération de conscience, bradypnée ou hypotension dépasse ce syndrome stable et impose une recherche urgente de décompensation.',['sfe-gravite']),
('La gravité clinique ne doit pas être retardée par l’attente d’un dosage de confirmation.',['ch-hypothyroide','sfe-gravite'])])
s+=h('7.5 — Une composante neuropathique ou une lyse modifie la suite')
s+=p('Une perte sensitive, une aréflexie ou une distribution atypique invite à rechercher une composante neurologique, parfois associée à l’hypothyroïdie.','cen-myogene-clinique','cen-rot','dgn-thyroide')
s+=p('Une atteinte rénale, des troubles ioniques ou une oligo-anurie dans un tableau musculaire sévère ouvrent le bilan de rhabdomyolyse et de ses complications.','rhabdo-s02','rhabdo-e13')
s+=rows(['Syndrome','Signes fonctionnels','Signes physiques ou biologiques utiles'],[
 [('Le syndrome douloureux renseigne la plainte musculaire.',['dgn-thyroide']),('Le patient rapporte myalgies, crampes ou enraidissement.',['sfe-clinique']),('La douleur provoquée et la force sont examinées séparément.',['dgn-examen','cen-force'])],
 [('Le syndrome proximal renseigne une atteinte motrice.',['cen-myogene-clinique']),('Les escaliers, le lever du siège et les charges deviennent difficiles.',['cen-myogene-clinique']),('Un déficit comparatif coté est objectivé aux ceintures.',['cen-force','cen-myogene-clinique'])],
 [('Le syndrome rare de Hoffmann associe volume et décontraction.',['dgn-thyroide']),('Des phénomènes douloureux de relâchement peuvent être décrits.',['dgn-thyroide']),('Une pseudohypertrophie et des anomalies de décontraction sont recherchées.',['dgn-thyroide','cen-myogene-clinique'])],
 [('Le syndrome endocrinien apporte le contexte systémique.',['sfe-clinique']),('La frilosité, la constipation et le ralentissement sont précisés.',['sfe-clinique']),('Les signes cutanés et cardiaques sont confrontés à la TSH et à la T4 libre.',['sfe-clinique','has-diagnostic'])]])
save(s)

start(8)
s=h('Les critères hormonaux sont explicites ; l’attribution musculaire reste une confrontation clinique')
s+=p('Les recommandations HAS validées en décembre 2022 définissent l’hypothyroïdie primaire avérée par une TSH supérieure à 10 mUI/L et une T4 libre basse.','has-date','has-diagnostic')
s+=p('La limite basse de T4 libre est celle du laboratoire utilisé ; une valeur isolée sans intervalle de référence perd une partie de son sens.','has-diagnostic')
s+=p('L’hypothyroïdie fruste associe une TSH supérieure à la référence sur au moins deux prélèvements espacés d’au moins 6 semaines et une T4 libre normale.','has-diagnostic')
s+=p('Le tableau musculaire est retenu sur les symptômes, le déficit objectivé et leur cohérence avec le déficit hormonal, tout en recherchant les causes concurrentes.','dgn-thyroide','cen-force','dgn-labo')
s+=p('Une CK élevée peut soutenir l’atteinte musculaire, mais sa normalité ne l’exclut pas et sa hausse n’en définit pas la cause.','dgn-thyroide','dgn-ck')
s+=rows(['Situation','Critère ou constatation','Ce qui est conclu','Ce qui reste à faire'],[
 [('L’hypothèse est une hypothyroïdie primaire avérée.',['has-diagnostic']),('La TSH dépasse 10 mUI/L et la T4 libre est sous la référence.',['has-diagnostic']),('Le déficit hormonal primaire est documenté selon la HAS 2022.',['has-date','has-diagnostic']),('La force, le retentissement et les causes concurrentes précisent l’atteinte musculaire.',['cen-force','dgn-labo'])],
 [('L’hypothèse est une forme primaire fruste.',['has-diagnostic']),('La TSH est durablement au-dessus de la référence, avec T4 libre normale, sur les contrôles requis.',['has-diagnostic']),('Le résultat ne se confond pas avec une hypothyroïdie patente ni avec une myopathie démontrée.',['has-diagnostic','has-clinique']),('L’âge, les symptômes et le contexte guident la décision, sans prescription automatique.',['has-age','has-therapie'])],
 [('L’hypothèse est une insuffisance thyréotrope.',['sfe-definition']),('La T4 libre est basse et la TSH est inadaptée, parfois normale ou légèrement élevée.',['sfe-definition']),('Une TSH normale n’exclut pas ce déficit central.',['sfe-definition']),('Le contexte hypophysaire et les autres fonctions hormonales sont évalués.',['sfe-central','aips83-euthyrox-prudence'])],
 [('La faiblesse est objectivée malgré une CK dans la référence.',['cen-force','dgn-thyroide']),('Le déficit segmentaire existe indépendamment du marqueur enzymatique.',['cen-force','dgn-thyroide']),('La CK normale ne rejette pas une atteinte hypothyroïdienne.',['dgn-thyroide']),('Le bilan reste guidé par la clinique, la fonction thyroïdienne et les autres hypothèses.',['dgn-labo','has-diagnostic'])]])
s+=w('seuils','Interpréter les seuils avec leur contexte',[
('Devant une TSH initialement au-dessus de la référence mais inférieure à 10 mUI/L, la HAS demande un contrôle à au moins 6 semaines.',['has-diagnostic']),
('Si cette hausse persiste, la T4 libre est ajoutée ; une TSH initialement supérieure à 10 mUI/L justifie d’emblée la T4 libre.',['has-diagnostic']),
('Le dosage en cascade réalise cet ajout sur le même tube lorsque les conditions prescrites sont réunies.',['has-diagnostic']),
('L’intervalle de référence varie selon les méthodes ; chez la personne âgée, son interprétation doit aussi tenir compte de l’âge.',['has-diagnostic','has-age']),
('Un épisode aigu peut perturber transitoirement la fonction thyroïdienne, ce qui renforce la nécessité d’interpréter le contexte.',['has-diagnostic']),
('La T3 libre n’est pas recommandée pour le diagnostic usuel d’une hypothyroïdie primaire ; une T3 basse isolée peut accompagner maladie, stress ou dénutrition.',['has-diagnostic'])])
s+=h('Les exclusions se recherchent avant une attribution exclusive')
s+=p('La chronologie médicamenteuse, l’effort récent et les autres maladies musculaires sont relus lorsqu’une CK est élevée.','dgn-anamnese','dgn-ck','dgn-toxique')
s+=p('Des anti-TPO positifs renseignent une étiologie auto-immune thyroïdienne ; ils ne constituent ni un score de faiblesse ni un marqueur de myosite.','has-anticorps','dgn-imnm')
s+=p('Des signes de déficit sensitif ou un profil moteur atypique font rechercher une composante neurologique plutôt que forcer un syndrome musculaire pur.','cen-myogene-clinique','dgn-thyroide')
s+=p('La dysphagie, la progression de la faiblesse et des CK très élevées sous statine orientent vers une IMNM, même si une hypothyroïdie est également présente.','dgn-imnm','dgn-statine')
s+=w('confirmation','Ce qui renforce l’attribution et ce qui impose de la réviser',[
('Un déficit proximal documenté et un déficit hormonal confirmé forment une concordance clinique et biologique utile.',['cen-myogene-clinique','has-diagnostic','dgn-thyroide']),
('L’amélioration clinique est recherchée pendant la normalisation hormonale et participe à l’appréciation de l’équilibre.',['has-therapie','has-suivi']),
('La persistance de signes malgré une TSH équilibrée impose un diagnostic différentiel ; elle n’autorise pas une majoration indéfinie de T4.',['has-suivi']),
('L’instabilité biologique impose d’abord de vérifier prise, interactions, malabsorption et interférences analytiques.',['has-suivi']),
('La cotation de force décrit une sévérité fonctionnelle ; elle ne remplace pas les critères hormonaux ni une recherche de complications de lyse.',['cen-force','has-diagnostic','rhabdo-s02'])])
s+=p('La démarche n’utilise pas une classification histologique obligatoire pour confirmer chaque présentation endocrine ; la biopsie est réservée aux indications sélectionnées.','dgn-biopsie','dgn-thyroide')
save(s)

start(9)
s=h('9.a — La référence associe biologie hormonale et examen musculaire')
s+=p('La confirmation du déficit hormonal repose sur les dosages adaptés à son origine ; l’examen documente séparément l’atteinte musculaire et son retentissement.','has-diagnostic','cen-force','dgn-thyroide')
s+=p('Il n’est pas nécessaire de prescrire systématiquement une biopsie ou une IRM musculaire devant toute hypothyroïdie avec myalgies.','dgn-biopsie','has-diagnostic','dgn-imagerie')
s+=p('Les examens invasifs ou spécialisés répondent à une discordance, une persistance ou une hypothèse neuromusculaire particulière.','dgn-biopsie','dgn-labo','has-suivi')
s+=h('9.b — La prescription de première intention indique sa question')
s+=rows(['Examen et indication','Prescription utile','Interprétation et conduite'],[
 [('Une suspicion de déficit primaire justifie la TSH.',['has-diagnostic']),('Le bon précise diagnostic initial, contrôle ou suivi sous traitement, avec T4 libre en cascade selon le résultat.',['has-diagnostic']),('La TSH s’interprète en mUI/L avec l’intervalle du laboratoire, puis avec la T4 libre si les conditions sont réunies.',['has-diagnostic'])],
 [('Un contexte central justifie la TSH et la T4 libre d’emblée.',['has-diagnostic']),('Le contexte hypophysaire et les autres symptômes hormonaux sont communiqués.',['has-specialiste','sfe-central']),('Une T4 libre basse avec TSH inadaptée conduit au bilan endocrinologique, sans exclusion par TSH normale.',['sfe-definition','sfe-central'])],
 [('Une plainte musculaire avec suspicion de myopathie justifie la CK.',['dgn-ck']),('L’effort récent, les injections, l’examen électromyographique et les médicaments sont renseignés.',['dgn-ck','dgn-anamnese']),('Le résultat est comparé à la référence du laboratoire ; normal, il ne rejette pas l’atteinte hypothyroïdienne.',['dgn-thyroide','dgn-ck'])],
 [('Une lyse ou ses complications sont suspectées devant un tableau sévère.',['rhabdo-s02']),('Le bilan comprend notamment CK, fonction rénale et électrolytes avec évaluation de la diurèse.',['rhabdo-s02','rhabdo-e13']),('Une atteinte rénale, une anomalie ionique ou une oligo-anurie modifie l’orientation immédiatement.',['rhabdo-e13','rhabdo-s11'])],
 [('La recherche étiologique thyroïdienne peut nécessiter les anti-TPO.',['has-anticorps']),('Ils sont demandés après le diagnostic initial pour rechercher une auto-immunité, selon l’indication.',['has-anticorps']),('Leur positivité n’impose pas des dosages répétés de suivi et ne quantifie pas la myopathie.',['has-anticorps','dgn-thyroide'])]])
s+=w('reference','Normales et seuils : lire les données effectivement mesurées',[
('La HAS rapporte les seuils de TSH en mUI/L et demande de conserver l’intervalle de référence fourni par le laboratoire.',['has-diagnostic']),
('Une T4 libre normale est une T4 libre dans l’intervalle de la méthode utilisée ; une limite numérique universelle ne doit pas être substituée au compte rendu.',['has-diagnostic']),
('La CK est relue avec son unité et sa limite supérieure ; la comparaison à cette limite et le contexte clinique sont plus utiles qu’un ancien seuil unique.',['dgn-ck','dgn-thyroide']),
('L’examen de force complète la biologie par une cotation de 0 à 5, où 5 correspond à la normalité.',['cen-force']),
('Une TSH légèrement augmentée chez une personne âgée ne se lit pas exactement comme chez un adulte jeune ; la référence et l’intervention sont deux notions différentes.',['has-age'])])
s+=h('9.c — Les terrains particuliers changent la stratégie plutôt que le besoin de confirmation')
s+=p('La grossesse et le désir de grossesse conduisent à une prise en charge endocrinologique adaptée ; la confirmation et le suivi reposent sur la biologie hormonale.','aips83-euthyrox-grossesse','has-specialiste')
s+=p('Une hypothyroïdie de l’enfant nécessite un traitement et des doses propres à l’âge ; le protocole adulte présenté au point 11 ne lui est pas appliqué.','aips83-euthyrox-posologie','aips83-euthyrox-prudence')
s+=p('Une insuffisance rénale ou hépatique impose une attention à la liaison protéique et à la surveillance, car l’AIPS ne fournit pas de recommandation posologique quantitative spécifique.','aips83-euthyrox-posologie','aips83-euthyrox-pk')
s+=p('Le parcours diagnostique initial décrit ici repose sur des prélèvements et l’examen, sans besoin de contraste iodé ni d’IRM systématique.','has-diagnostic','has-anticorps','dgn-biopsie')
s+=p('Si une imagerie musculaire devient nécessaire, la DGN indique que les séquences modernes permettent généralement l’évaluation sans produit de contraste.','dgn-imagerie')
s+=p('Si une IRM musculaire est impossible, l’échographie peut fournir un dépistage complémentaire à l’électrophysiologie, sans garantir l’exclusion de toute pathologie.','dgn-imagerie')
s+=h('9.d — Les examens de seconde intention répondent à une discordance')
s+=rows(['Examen','Question précise','Interprétation et suite'],[
 [('L’électromyogramme est discuté devant une faiblesse inexpliquée, persistante ou atypique.',['dgn-labo','cen-myogene-emg']),('Il recherche un profil myogène et peut distinguer une composante neurogène selon le bilan.',['cen-myogene-emg','dgn-emg']),('Un tracé myogène ne précise pas seul l’étiologie ; des anomalies spontanées ne sont pas spécifiques d’une myosite.',['dgn-emg','cen-myogene-emg'])],
 [('L’IRM musculaire est discutée devant une suspicion de myosite ou une autre atteinte structurale.',['dgn-imagerie']),('Elle apprécie la distribution et peut aider à choisir un site représentatif de biopsie.',['dgn-imagerie']),('Des anomalies se recouvrent entre maladies ; la corrélation avec clinique et biologie reste nécessaire.',['dgn-imagerie'])],
 [('La biopsie musculaire est réservée à certaines maladies non clarifiées ou inflammatoires suspectées.',['dgn-biopsie']),('Elle est considérée après exploitation des méthodes non invasives appropriées.',['dgn-biopsie']),('Elle n’est pas une condition systématique à la substitution d’un déficit hormonal confirmé.',['dgn-biopsie','has-therapie'])],
 [('L’IRM hypothalamo-hypophysaire répond à une insuffisance thyréotrope.',['sfe-central']),('Elle recherche une cause de la commande centrale déficiente.',['sfe-central']),('Cette indication ne se confond pas avec une IRM musculaire de routine.',['sfe-central','dgn-imagerie'])]])
s+=w('pieges','Éviter un résultat trompeur ou un examen sans conséquence',[
('La biotine peut produire des résultats faussement élevés ou abaissés dans certains immunodosages ; le laboratoire en est averti.',['aips83-euthyrox-prudence']),
('Une méthode non sensible à cette interférence est préférée lorsqu’elle est disponible et que le contexte le justifie.',['aips83-euthyrox-prudence']),
('Une CK mesurée après effort important peut être augmentée chez une personne sans maladie musculaire.',['dgn-ck']),
('Pour une réévaluation non urgente fiable, la DGN recommande une période de repos physique et l’évitement récent d’injections intramusculaires ou d’EMG ; ce délai ne s’applique pas au triage d’une lyse compliquée.',['dgn-ck','rhabdo-e13']),
('L’échographie thyroïdienne n’est pas systématique dans l’hypothyroïdie et la scintigraphie n’a pas d’intérêt dans ce bilan usuel.',['has-anticorps']),
('Un nodule palpable ou un goitre peut cependant justifier un avis spécialisé dans son propre contexte.',['has-specialiste'])])
save(s)

start(10)
s=h('Chaque embranchement associe une constatation à une action')
s+=rows(['Si la situation suivante est constatée…','…la décision est la suivante'],[
 [('Si conscience, respiration ou circulation sont altérées dans un contexte d’hypothyroïdie sévère…',['sfe-gravite']),('…le patient quitte la filière ambulatoire pour une prise en charge hospitalière immédiate.',['ch-hypothyroide','sfe-gravite'])],
 [('Si le tableau musculaire s’accompagne d’oligo-anurie ou d’anomalies rénales ou ioniques…',['rhabdo-e13','rhabdo-s02']),('…le bilan et le traitement des complications de rhabdomyolyse sont engagés en urgence.',['rhabdo-s03','rhabdo-s11'])],
 [('Si une faiblesse progressive avec dysphagie et CK très élevées survient sous statine…',['dgn-imnm']),('…une IMNM est recherchée en filière spécialisée, sans attendre que la correction endocrine résolve tout.',['dgn-imnm','dgn-thyroide'])],
 [('Si le patient est stable et présente des signes compatibles avec un déficit primaire…',['has-clinique']),('…la TSH est prescrite avec le contexte, et la T4 libre est ajoutée selon l’algorithme hormonal.',['has-diagnostic'])],
 [('Si la TSH est modérément augmentée et inférieure à 10 mUI/L…',['has-diagnostic']),('…elle est contrôlée à au moins 6 semaines ; une persistance conduit au dosage de T4 libre.',['has-diagnostic'])],
 [('Si la TSH initiale dépasse 10 mUI/L…',['has-diagnostic']),('…la T4 libre est dosée, en cascade sur le même tube lorsque cela est prescrit.',['has-diagnostic'])],
 [('Si une atteinte centrale est plausible…',['sfe-central']),('…TSH et T4 libre sont dosées ensemble ; une TSH normale ne clôt pas l’exploration.',['has-diagnostic','sfe-definition'])],
 [('Si une hypothyroïdie avérée est confirmée…',['has-diagnostic']),('…les risques cardiaques et les fonctions hypophysaire ou surrénalienne sont vérifiés avant substitution.',['aips83-euthyrox-ci','aips83-euthyrox-prudence'])],
 [('Si un déficit surrénalien nécessite un traitement…',['aips83-euthyrox-prudence']),('…la substitution glucocorticoïde précède la T4 selon la notice, dans un cadre endocrinologique.',['aips83-euthyrox-prudence'])],
 [('Si une substitution adulte ambulatoire est appropriée…',['aips83-euthyrox-indications','aips83-euthyrox-posologie']),('…la dose orale est individualisée selon l’AIPS et les modalités de prise sont expliquées.',['aips83-euthyrox-posologie'])],
 [('Si le traitement vient de débuter ou sa dose vient de changer…',['has-suivi']),('…la TSH primaire et l’évolution clinique sont réévaluées à 6–8 semaines, avec vigilance sur les signes de surdosage.',['has-suivi'])],
 [('Si les symptômes persistent malgré un équilibre biologique…',['has-suivi']),('…la prise, les interactions, les interférences et les autres causes musculaires sont réexaminées avant toute escalade.',['has-suivi','dgn-labo'])]])
s+=w('centrale','La branche centrale possède son propre suivi',[
('Une T4 libre basse avec TSH inadaptée oriente vers l’insuffisance thyréotrope.',['sfe-definition']),
('Le bilan étiologique recherche une pathologie hypothalamo-hypophysaire et les déficits associés.',['sfe-central']),
('L’évaluation surrénalienne et sa substitution si nécessaire précèdent la T4.',['aips83-euthyrox-prudence']),
('La TSH n’est pas un indicateur fiable d’ajustement dans cette branche ; le suivi repose sur la T4 libre et le contexte spécialisé.',['sfe-central-suivi']),
('Le calendrier usuel de TSH d’une hypothyroïdie primaire ne doit donc pas être appliqué mécaniquement à une atteinte centrale.',['has-suivi','sfe-central-suivi'])])
s+=w('reprise','L’évolution musculaire est confrontée à l’évolution hormonale',[
('Le suivi reprend les gestes fonctionnels et les groupes musculaires initialement déficitaires.',['cen-force','cen-myogene-clinique','has-suivi']),
('Une amélioration du ressenti et des signes cliniques participe à la notion d’équilibre, avec les résultats biologiques.',['has-suivi']),
('Une aggravation rapide, une dysphagie ou des signes rénaux imposent une nouvelle orientation avant le rendez-vous programmé.',['dgn-imnm','rhabdo-e13']),
('Une CK élevée isolée est interprétée avec l’effort, les traitements et la fonction musculaire ; elle n’est pas une instruction automatique de majoration hormonale.',['dgn-ck','aips83-euthyrox-posologie']),
('Un retour à des tâches exigeantes dépend des capacités réellement retrouvées et des exigences du poste, plutôt que d’une date universelle.',['fmh-evaluation','cen-myogene-clinique'])])
save(s)

start(11)
s=h('11.A — Le but associe équilibre hormonal, fonction et absence d’iatrogénie')
s+=p('Dans l’hypothyroïdie primaire, la cible est une TSH dans l’intervalle du laboratoire accompagnée d’une amélioration clinique et du ressenti.','has-therapie')
s+=p('La HAS considère l’équilibre atteint lorsque deux TSH sont dans la référence à 3 mois d’intervalle sous la même dose, avec prise en compte de la clinique.','has-suivi')
s+=p('La force est suivie sur l’échelle de 0 à 5 et sur les gestes déficitaires initiaux ; le grade 5 désigne la force normale.','cen-force','cen-myogene-clinique')
s+=p('Ce résultat est intégré à la clinique et à l’équilibre hormonal, sans imposer la seule cotation comme critère universel de sortie.','cen-force','has-suivi')
s+=p('L’absence de signes de surdosage fait partie de l’objectif ; une amélioration de la douleur ne justifie pas une stimulation hormonale excessive.','has-suivi','aips83-euthyrox-prudence')
s+=p('En insuffisance thyréotrope, l’objectif biologique est défini avec l’endocrinologue sur la T4 libre ; la TSH ne sert pas à ajuster le traitement.','sfe-central-suivi')
s+=h('11.B — La sécurité et la cause précèdent la prescription usuelle')
s+=w('urgence','Urgence — conduite chronologique',[
('La première étape identifie une altération de conscience, une hypothermie, un ralentissement respiratoire ou une défaillance circulatoire.',['sfe-gravite','rhabdo-e13']),
('Une suspicion de coma myxœdémateux impose une prise en charge hospitalière immédiate ; le schéma oral progressif ci-dessous n’est pas son traitement de réanimation.',['ch-hypothyroide','sfe-gravite','aips83-euthyrox-posologie']),
('Une rhabdomyolyse possible est évaluée avec constantes, diurèse, fonction rénale et électrolytes, sans attendre la triade complète.',['rhabdo-e13','rhabdo-s02']),
('Une hyperkaliémie ou une autre complication métabolique nécessite la surveillance et le traitement spécialisés appropriés ; une CK seule ne résume pas la gravité.',['rhabdo-s11','rhabdo-e13']),
('Le facteur causal de lyse est éliminé et les complications sont traitées en parallèle dans la filière adaptée.',['rhabdo-s03']),
('Chez un patient stable, l’origine du déficit et les contre-indications sont vérifiées avant d’introduire la T4.',['has-diagnostic','aips83-euthyrox-ci']),
('Une fonction surrénalienne nécessitant substitution est traitée par glucocorticoïdes avant la T4 ; les troubles hypophysaires non traités sont également évalués.',['aips83-euthyrox-prudence','aips83-euthyrox-ci'])])
s+=p('La lévothyroxine seule est le traitement de référence de l’hypothyroïdie primaire avérée ; la vérification biologique précède son initiation.','has-therapie')
s+=p('Euthyrox® dispose en Suisse de l’indication de substitution des hormones thyroïdiennes dans l’hypothyroïdie de toute origine.','aips83-euthyrox-indications')
s+=p('La spécialité porte le numéro Swissmedic 54949 ; l’information professionnelle consultée est datée de février 2023.','aips83-euthyrox-autorisation','aips83-euthyrox-date')
s+=rows(['Prescription adulte concernée','Dose et mode AIPS','Durée et conditions','Risque ou surveillance'],[
 [('La prescription concerne l’adulte atteint d’hypothyroïdie, après vérification de l’indication et des contre-indications.',['aips83-euthyrox-indications','aips83-euthyrox-ci']),('La dose initiale usuelle est de 25–50 µg par jour par voie orale.',['aips83-euthyrox-posologie']),('La dose est individualisée selon l’état clinique, la durée et la sévérité du déficit.',['aips83-euthyrox-posologie']),('La surveillance recherche l’amélioration et les signes de stimulation excessive.',['has-suivi','aips83-euthyrox-prudence'])],
 [('L’ajustement suit la réponse et la tolérance de cet adulte.',['aips83-euthyrox-posologie']),('L’AIPS décrit des augmentations de 25–50 µg à intervalles de 2–4 semaines.',['aips83-euthyrox-posologie']),('Ces paliers sont adaptés au patient ; ils ne constituent pas une augmentation automatique sans réévaluation.',['aips83-euthyrox-posologie']),('La TSH primaire est contrôlée selon le calendrier hormonal et le terrain.',['has-suivi','aips83-euthyrox-posologie'])],
 [('La dose d’entretien usuelle adulte figure dans la notice.',['aips83-euthyrox-posologie']),('La plage indiquée est de 100–200 µg par jour.',['aips83-euthyrox-posologie']),('Il s’agit d’une plage usuelle, pas d’une cible obligatoire ni d’un plafond universel pour toutes les indications.',['aips83-euthyrox-posologie']),('Les personnes âgées ou fragiles peuvent nécessiter une dose d’entretien inférieure.',['aips83-euthyrox-posologie'])],
 [('L’adulte âgé ou ayant une hypothyroïdie sévère ou prolongée exige une prudence accrue.',['aips83-euthyrox-posologie']),('La dose initiale recommandée est plus faible, à 25 µg par jour.',['aips83-euthyrox-posologie']),('L’augmentation est prudente, avec des intervalles plus longs et des contrôles fréquents.',['aips83-euthyrox-posologie']),('Une comorbidité cardiovasculaire ou endocrine impose aussi cette individualisation.',['aips83-euthyrox-posologie'])],
 [('La dose quotidienne entière est prise le matin.',['aips83-euthyrox-posologie']),('La prise se fait à jeun, au moins une demi-heure avant le petit-déjeuner, avec un peu de liquide et sans croquer.',['aips83-euthyrox-posologie']),('Les comprimés sécables peuvent être divisés si nécessaire au dosage prescrit.',['aips83-euthyrox-posologie']),('La prise alimentaire simultanée diminue l’absorption.',['aips83-euthyrox-pk'])],
 [('Le traitement substitutif d’une hypothyroïdie est le plus souvent prolongé.',['aips83-euthyrox-posologie']),('La dose quotidienne reste déterminée par l’évaluation clinique et biologique.',['aips83-euthyrox-posologie']),('L’AIPS indique une durée le plus souvent à vie dans l’hypothyroïdie.',['aips83-euthyrox-posologie']),('Une disparition des myalgies ne suffit pas à décider seul d’un arrêt.',['aips83-euthyrox-posologie','has-suivi'])]])
s+=w('contreindications','Les contre-indications et précautions sont relues avant la première prise',[
('La notice contre-indique notamment l’insuffisance cardiaque avec accélération de fréquence, la pancardite ou myocardite aiguë, l’infarctus aigu et l’angine de poitrine.',['aips83-euthyrox-ci']),
('Les troubles hypophysaires ou surrénaliens non traités et l’hypersensibilité au principe actif ou aux excipients sont également contre-indiqués.',['aips83-euthyrox-ci']),
('L’hyperthyroïdie est une contre-indication hors indication particulière de traitement associé ; cette exception ne concerne pas la myopathie hypothyroïdienne.',['aips83-euthyrox-ci','aips83-euthyrox-indications']),
('Une maladie vasculaire grave, une hypertension ou une pathologie cardiaque doit être évaluée et traitée avant l’hormonothérapie selon l’AIPS.',['aips83-euthyrox-prudence']),
('Une cardiopathie ischémique ou une difficulté d’équilibre motive l’avis spécialisé ; la faible dose ne dispense pas de vérifier les contre-indications.',['has-specialiste','aips83-euthyrox-ci','aips83-euthyrox-posologie']),
('Les hormones thyroïdiennes ne sont pas prescrites pour faire maigrir ou améliorer la performance chez un patient euthyroïdien.',['aips83-euthyrox-prudence'])])
s+=w('interactions','Organiser les interactions au lieu d’augmenter aveuglément',[
('La T4 est prise au moins 2 heures avant les sels d’aluminium, de fer ou de calcium selon l’AIPS Euthyrox.',['aips83-euthyrox-interactions']),
('Avec colestyramine ou colestipol, la lévothyroxine est prise 4–5 heures avant la résine.',['aips83-euthyrox-interactions']),
('Les inhibiteurs de pompe à protons peuvent diminuer l’absorption ; leur introduction ou leur arrêt justifie une surveillance clinique et hormonale.',['aips83-euthyrox-interactions']),
('Le sévélamer, l’orlistat et les produits à base de soja peuvent également modifier l’exposition et requièrent une réévaluation adaptée.',['aips83-euthyrox-interactions']),
('Les inducteurs enzymatiques, certains traitements hormonaux et d’autres médicaments peuvent modifier les besoins ; la liste complète est relue lors d’une instabilité.',['aips83-euthyrox-interactions','has-suivi']),
('Sous antivitamine K, la lévothyroxine peut renforcer l’effet anticoagulant ; les paramètres de coagulation sont contrôlés et le traitement adapté si nécessaire.',['aips83-euthyrox-interactions']),
('Chez le patient diabétique, la glycémie est contrôlée plus fréquemment au début, car les besoins en traitement hypoglycémiant peuvent changer.',['aips83-euthyrox-prudence','aips83-euthyrox-interactions']),
('La biotine est signalée au laboratoire et une méthode non soumise à son interférence est recherchée si possible ; un résultat discordant n’impose pas une escalade immédiate.',['aips83-euthyrox-prudence','has-suivi'])])
s+=h('Les situations spéciales modifient la prescription et son suivi')
s+=rows(['Situation','Conduite sourcée','Limite à conserver'],[
 [('La personne âgée a une TSH légèrement élevée.',['has-age','aips83-euthyrox-posologie']),('L’âge et la référence adaptée sont considérés avant de traiter ; si la substitution est indiquée, l’AIPS prévoit une initiation prudente à 25 µg.',['has-age','aips83-euthyrox-posologie']),('Une faible dose n’est pas une indication à traiter toute hausse isolée.',['has-age'])],
 [('L’adulte présente une insuffisance rénale ou hépatique.',['aips83-euthyrox-posologie']),('La pharmacocinétique spécifique n’a pas été étudiée ; la clinique, les hormones et les modifications de liaison protéique sont prises en compte.',['aips83-euthyrox-posologie','aips83-euthyrox-pk']),('La notice ne fournit pas de règle quantitative d’ajustement ; cela ne signifie pas absence de vigilance.',['aips83-euthyrox-posologie'])],
 [('Une grossesse est présente ou souhaitée.',['aips83-euthyrox-grossesse','has-specialiste']),('La T4 substitutive est poursuivie sans interruption avec surveillance spécialisée étroite ; une dose plus élevée peut être nécessaire.',['aips83-euthyrox-grossesse']),('La contre-indication pendant la grossesse vise l’association aux thyréostatiques d’une hyperthyroïdie, pas la substitution indiquée.',['aips83-euthyrox-grossesse'])],
 [('La patiente vient d’accoucher après adaptation de dose pendant la grossesse.',['aips83-euthyrox-grossesse']),('L’AIPS prévoit le retour immédiat à la dose d’avant grossesse et le contrôle de TSH à 6–8 semaines après l’accouchement.',['aips83-euthyrox-grossesse']),('Le plan est expliqué et coordonné, avec réévaluation clinique individuelle.',['aips83-euthyrox-grossesse','has-suivi'])],
 [('La patiente allaite.',['aips83-euthyrox-grossesse']),('La substitution est poursuivie ; Euthyrox peut être utilisé pendant l’allaitement.',['aips83-euthyrox-grossesse']),('Le faible passage dans le lait est pris en compte si la fonction thyroïdienne du nourrisson est examinée.',['aips83-euthyrox-grossesse'])],
 [('Un enfant présente un déficit hormonal ou une faiblesse.',['aips83-euthyrox-posologie','aips83-euthyrox-prudence']),('Les besoins pédiatriques et l’importance de la substitution pour la croissance sont considérés dans une prise en charge adaptée.',['aips83-euthyrox-posologie','aips83-euthyrox-prudence']),('Le tableau de prescription adulte de cette leçon ne sert pas d’ordonnance pédiatrique.',['aips83-euthyrox-posologie'])],
 [('Une insuffisance thyréotrope est retenue.',['sfe-definition']),('La cause centrale et les autres axes sont explorés ; l’adaptation repose sur la T4 libre en filière spécialisée.',['sfe-central','sfe-central-suivi']),('La TSH ne sert pas de cible autonome de titration.',['sfe-central-suivi'])]])
s+=p('La HAS propose chez la femme enceinte substituée un dosage de TSH toutes les 4–6 semaines jusqu’à 22 semaines d’aménorrhée, puis au moins une fois entre 30 et 34 semaines.','has-grossesse-suivi')
s+=p('Ce calendrier européen complète la surveillance spécialisée demandée par l’AIPS ; les adaptations posologiques sont individualisées dans le cadre suisse.','has-grossesse-suivi','aips83-euthyrox-grossesse','aips83-euthyrox-posologie')
s+=h('Les moyens non médicamenteux et sociaux accompagnent la récupération')
s+=p('L’information explique la cause hormonale, la marge thérapeutique étroite et la nécessité de ne pas modifier seul la dose devant une fatigue persistante.','has-therapie','has-suivi','aips83-euthyrox-prudence')
s+=p('Les activités réellement limitées sont identifiées pour adapter temporairement les tâches et suivre la récupération fonctionnelle.','cen-myogene-clinique','fmh-evaluation')
s+=p('La capacité de travail dépend des fonctions résiduelles et des exigences du poste ; temps de présence et rendement peuvent être distincts.','fmh-evaluation')
s+=p('Selon le cadre suisse ASSM/FMH, le certificat à l’employeur indique le degré et les dates de l’incapacité ou la prochaine consultation, sans diagnostic ni détail du traitement.','fmh-certificat','fmh-secret')
s+=p('La notice ne prévoit pas d’effet sur la conduite lorsque le produit est utilisé selon l’indication ; l’état fonctionnel ou la somnolence du patient reste évalué séparément.','aips83-euthyrox-conduite','sfe-clinique','fmh-evaluation')
s+=p('Une disparition de la douleur ne remplace pas l’évaluation d’une faiblesse résiduelle pour les tâches de sécurité ou physiquement exigeantes.','cen-force','cen-myogene-clinique','fmh-evaluation')
s+=h('11.C — La surveillance relie calendrier, résultats et seuils d’alerte')
s+=rows(['Quand ou pourquoi contrôler','Ce qui est contrôlé','Décision selon le résultat'],[
 [('Le traitement primaire commence ou sa dose change.',['has-suivi']),('La TSH est contrôlée à 6–8 semaines avec les signes cliniques et le ressenti.',['has-suivi']),('Le résultat est confronté à la prise, aux interactions et à la tolérance avant ajustement.',['has-suivi'])],
 [('La spécialité à base de T4 change.',['has-suivi']),('Une surveillance clinique et une TSH à 6–8 semaines sont prévues.',['has-suivi']),('Une TSH instable ne suffit pas à imputer le problème à une seule cause sans enquête.',['has-suivi'])],
 [('La TSH reste fluctuante ou les symptômes persistent.',['has-suivi']),('La prise, la malabsorption, les interactions et les interférences sont recherchées ; T4 libre si discordance.',['has-suivi']),('Les causes sont traitées avant une augmentation et un diagnostic différentiel est repris si nécessaire.',['has-suivi'])],
 [('Le traitement est bien équilibré et toléré.',['has-suivi']),('Le suivi primaire devient annuel par TSH avec appréciation clinique.',['has-suivi','mdx-thyroide']),('Une nouvelle symptomatologie ou une variation importante de poids justifie une réévaluation plus tôt.',['has-suivi'])],
 [('Une faiblesse ou une douleur musculaire est suivie.',['dgn-thyroide','cen-myogene-clinique']),('Les groupes musculaires et les gestes initialement limités sont réexaminés ; la CK est relue selon le contexte.',['cen-force','dgn-ck']),('Une progression, une dysphagie ou une atteinte rénale impose une réorientation, pas l’attente du suivi annuel.',['dgn-imnm','rhabdo-e13'])],
 [('Des signes de stimulation excessive apparaissent.',['aips83-euthyrox-prudence']),('Palpitations, tremblement, sueurs, insomnie, diarrhée ou autres effets rapportés sont évalués.',['aips83-euthyrox-ei']),('La dose est diminuée ou la prise interrompue plusieurs jours selon l’évaluation et l’AIPS, puis reprise prudemment après disparition des effets.',['aips83-euthyrox-prudence'])]])
s+=w('alertes','Les effets indésirables définissent aussi les consignes de rappel',[
('Une tachycardie, une arythmie, un état pectangineux ou une insuffisance cardiaque révélée sous traitement nécessite une évaluation clinique adaptée à sa gravité.',['aips83-euthyrox-ei','aips83-euthyrox-prudence']),
('Une réaction d’hypersensibilité, en particulier respiratoire ou avec angiœdème, impose une prise en charge immédiate et une révision du traitement.',['aips83-euthyrox-ei','aips83-euthyrox-ci']),
('Les fréquences des effets rapportés ne peuvent pas être déterminées à partir des données de la notice ; aucun risque numérique individuel n’en est déduit.',['aips83-euthyrox-ei']),
('Une augmentation trop rapide ou une dose trop élevée peut produire des symptômes de type hyperthyroïdien.',['aips83-euthyrox-prudence']),
('Une prise visant la perte de poids expose à des effets graves et ne constitue pas une indication.',['aips83-euthyrox-prudence']),
('Une aggravation musculaire accompagnée d’urines rares, d’urines foncées ou de signes systémiques est réévaluée en urgence pour rechercher une autre complication.',['rhabdo-e13','rhabdo-s02'])])
s+=h('11.D — Le pronostic et les critères de sortie sont explicités séparément')
s+=p('L’amélioration clinique est attendue dans un projet de substitution, mais la persistance de symptômes conduit à chercher une autre cause ou une mauvaise équilibration.','has-therapie','has-suivi')
s+=p('Le plein effet pharmacologique de la T4 est décrit en 1–3 semaines dans la notice ; ce délai n’est pas une garantie de récupération musculaire complète.','aips83-euthyrox-pd','has-suivi')
s+=p('L’AIPS décrit une demi-vie prolongée en hypothyroïdie ; cela soutient l’individualisation du suivi et ne justifie pas des modifications quotidiennes non encadrées.','aips83-euthyrox-pk','aips83-euthyrox-posologie')
s+=w('sortie','Critères de poursuite ambulatoire ou d’espacement du suivi',[
('Le premier critère est l’absence d’une défaillance de conscience, respiratoire ou circulatoire évoquant un coma myxœdémateux.',['sfe-gravite','ch-hypothyroide']),
('Le deuxième critère est l’absence de complication rénale ou métabolique de lyse imposant une filière urgente.',['rhabdo-e13','rhabdo-s02']),
('Le troisième critère est une évolution motrice compatible avec le plan, sans progression inquiétante ni dysphagie nouvelle.',['dgn-imnm','cen-force','has-suivi']),
('Le quatrième critère est un traitement compréhensible et réalisable, avec horaires, interactions et contre-indications pris en compte.',['aips83-euthyrox-posologie','aips83-euthyrox-interactions','has-specialiste']),
('Le cinquième critère est un contrôle hormonal programmé selon la phase du traitement ; l’espacement annuel attend l’équilibre et la bonne tolérance.',['has-suivi']),
('Le sixième critère est l’amélioration clinique intégrée à l’équilibre biologique ; une TSH normale avec faiblesse persistante impose une réévaluation.',['has-suivi']),
('Le septième critère est une décision fonctionnelle explicite pour les activités et le travail, avec les capacités résiduelles et les restrictions utiles.',['fmh-evaluation','cen-myogene-clinique']),
('Le huitième critère est la connaissance des signes qui imposent un rappel rapide ou une urgence, sans attendre le prochain dosage.',['sfe-gravite','rhabdo-e13','aips83-euthyrox-ei'])])
save(s)

start(12)
s=h('Prévenir le retard diagnostique, l’iatrogénie et la rechute fonctionnelle')
s+=p('En Suisse, l’algorithme mediX de 2026 rappelle les causes auto-immunes et iatrogènes du déficit et le suivi de la substitution.','mdx-thyroide','mdx-thyroide-date')
s+=p('La prévention s’adresse à ces situations à risque et aux traitements réellement présents ; une simple fatigue ne justifie pas une hormone sans confirmation.','mdx-thyroide','has-clinique','has-therapie')
s+=h('Prévention primaire : éviter une exposition inadaptée ou un déséquilibre prévisible')
s+=p('La liste des médicaments est revue chez les patients exposés au lithium, à l’amiodarone, aux antithyroïdiens ou à certaines immunothérapies.','mdx-thyroide')
s+=p('Chez la personne âgée sous amiodarone, la HAS recommande une surveillance régulière de TSH et rappelle qu’une élévation isolée modérée ne commande pas automatiquement un traitement.','has-age')
s+=p('Les modifications de prise de fer, calcium, résines ou IPP sont anticipées, car elles peuvent déstabiliser une substitution auparavant adéquate.','aips83-euthyrox-interactions')
s+=p('La T4 n’est utilisée ni pour faire maigrir ni pour améliorer une performance ; le patient est informé des risques d’une augmentation autonome.','aips83-euthyrox-prudence')
s+=p('Une hypothyroïdie connue est recherchée parmi les facteurs musculaires de risque sous statine ; une plainte nouvelle mérite une réévaluation du contexte.','dgn-statine','dgn-thyroide')
s+=h('Prévention secondaire : confirmer tôt et distinguer les formes')
s+=p('Une association nouvelle de crampes, faiblesse proximale, frilosité et constipation motive une recherche hormonale adaptée, plutôt qu’une attribution immédiate à l’âge.','has-clinique','dgn-thyroide','has-age')
s+=p('Une TSH modérément élevée est contrôlée dans les conditions recommandées avant de conclure à un déficit permanent.','has-diagnostic')
s+=p('Un contexte hypophysaire impose le couple TSH–T4 libre d’emblée afin d’éviter le faux réconfort d’une TSH normale.','has-diagnostic','sfe-definition')
s+=p('Les signes de coma myxœdémateux ou de complication de lyse sont expliqués comme motifs d’évaluation urgente.','sfe-gravite','rhabdo-e13')
s+=h('Prévention tertiaire : stabiliser l’équilibre et préserver les capacités')
s+=p('Le contrôle de TSH à 6–8 semaines jusqu’à stabilité, puis annuel, figure dans l’algorithme suisse mediX ; la clinique et la tolérance restent associées.','mdx-thyroide','has-suivi')
s+=p('Le patient conserve des modalités de prise régulières et connaît les produits à espacer ainsi que l’intérêt de signaler la biotine.','aips83-euthyrox-posologie','aips83-euthyrox-interactions','aips83-euthyrox-prudence')
s+=p('Une persistance de faiblesse malgré l’équilibre conduit à rechercher une autre cause au lieu de poursuivre une escalade hormonale.','has-suivi','dgn-labo')
s+=p('L’examen fonctionnel et l’évaluation du poste permettent d’adapter les tâches, puis de réévaluer les capacités réellement retrouvées.','cen-myogene-clinique','fmh-evaluation')
s+=p('La prévention du surtraitement est particulièrement importante chez les personnes âgées, cardiaques et postménopausées en raison des risques cardiaques et osseux.','has-age','aips83-euthyrox-prudence')
s+=w('education','Ce que le patient doit pouvoir expliquer avec ses mots',[
('Le traitement apporte une hormone manquante ; il ne constitue pas un antidouleur à prendre seulement lors des crises.',['aips83-euthyrox-indications','aips83-euthyrox-posologie']),
('La prise quotidienne suit un horaire et des espacements précis, parce que l’absorption varie avec les aliments et plusieurs produits associés.',['aips83-euthyrox-posologie','aips83-euthyrox-interactions']),
('La grossesse ou l’allaitement ne justifie pas l’arrêt de la substitution, mais une surveillance spécialisée.',['aips83-euthyrox-grossesse']),
('Une amélioration ressentie ne dispense pas du suivi biologique et une fatigue persistante ne justifie pas d’augmenter seul la dose.',['has-suivi','aips83-euthyrox-prudence']),
('Une somnolence majeure avec hypothermie, une baisse de diurèse ou une faiblesse progressive avec dysphagie impose une nouvelle évaluation rapide.',['sfe-gravite','rhabdo-e13','dgn-imnm'])])
save(s)

start(13)
s=h('Six phrases à conserver dans le raisonnement')
for t,ids in [
('La myopathie hypothyroïdienne se caractérise par un tableau musculaire compatible confronté à un déficit hormonal confirmé, sans exclure des causes associées.',['dgn-thyroide','has-diagnostic','dgn-statine']),
('Une CK normale n’exclut pas cette atteinte, tandis qu’une CK élevée ne démontre pas à elle seule son origine endocrine.',['dgn-thyroide','dgn-ck']),
('Une T4 libre basse avec TSH inadaptée fait rechercher une insuffisance thyréotrope même lorsque la TSH est normale.',['sfe-definition']),
('Une décompensation myxœdémateuse ou une rhabdomyolyse compliquée impose une filière urgente et sort du protocole substitutif ambulatoire.',['sfe-gravite','ch-hypothyroide','rhabdo-e13']),
('La lévothyroxine est individualisée après vérification des risques cardiaques et des fonctions surrénalienne et hypophysaire, avec des modalités de prise expliquées.',['aips83-euthyrox-posologie','aips83-euthyrox-prudence','aips83-euthyrox-ci']),
('Une faiblesse persistante malgré un équilibre hormonal conduit à réexaminer la prise, les interactions et les autres diagnostics plutôt qu’à augmenter sans limite la T4.',['has-suivi','dgn-labo'])]:s+=p(t,*ids)
save(s)

start(14)
s=h('Questions fréquentes : donner la réponse et son motif')
qs=[
('Une fatigue avec crampes suffit-elle à poser une myopathie hypothyroïdienne ?','Non ; ces symptômes sont non spécifiques et doivent être confrontés à l’examen et au bilan hormonal.','La force décrit l’atteinte fonctionnelle tandis que TSH et T4 libre caractérisent le déficit.',['has-clinique','has-diagnostic','cen-force']),
('Les 30–80 % cités par la DGN représentent-ils la prévalence d’une myopathie dans toute la population ?','Non ; le dénominateur est une hypothyroïdie symptomatique et le numérateur regroupe plusieurs symptômes neuromusculaires.','La faiblesse, la fatigue, les myalgies et parfois les neuropathies sont réunies dans cette plage.',['dgn-thyroide']),
('Une CK normale écarte-t-elle le diagnostic ?','Non ; la DGN décrit des CK normales comme des CK nettement augmentées.','Le résultat ne remplace ni la cotation de force ni la confirmation hormonale.',['dgn-thyroide','cen-force','has-diagnostic']),
('Une TSH normale élimine-t-elle toutes les hypothyroïdies ?','Non ; une insuffisance thyréotrope peut comporter une TSH normale inadaptée à une T4 libre basse.','Le contexte central impose le dosage conjoint et un bilan hypophysaire.',['sfe-definition','has-diagnostic','sfe-central']),
('Une TSH légèrement augmentée avec T4 libre normale prouve-t-elle une myopathie endocrine ?','Non ; la forme fruste exige les contrôles hormonaux et reste souvent peu ou pas symptomatique.','L’âge, la clinique et les autres causes de plainte sont considérés séparément.',['has-diagnostic','has-clinique','has-age']),
('La T3 libre doit-elle être dosée systématiquement pour confirmer une hypothyroïdie primaire ?','Non ; la HAS ne la recommande pas dans ce diagnostic usuel.','Une T3 basse isolée peut accompagner des états pathologiques sans dysfonction thyroïdienne.',['has-diagnostic']),
('Des anti-TPO positifs démontrent-ils une myosite auto-immune ?','Non ; ils renseignent une étiologie auto-immune thyroïdienne.','Ils ne remplacent pas l’évaluation neuromusculaire ou les marqueurs propres à une IMNM.',['has-anticorps','dgn-imnm']),
('La découverte d’une hypothyroïdie suffit-elle à disculper une statine ?','Non ; l’hypothyroïdie peut elle-même accroître le risque musculaire sous statine.','Les mécanismes peuvent coexister et leur chronologie doit être examinée.',['dgn-statine','dgn-thyroide']),
('Le coma myxœdémateux est-il traité par la montée orale habituelle en consultation ?','Non ; une altération de conscience avec défaillance cardiorespiratoire ou hypothermie impose une prise en charge hospitalière immédiate.','La titration orale usuelle ne constitue pas un protocole de réanimation.',['sfe-gravite','ch-hypothyroide','aips83-euthyrox-posologie']),
('La T4 peut-elle être commencée sans évaluer un déficit surrénalien associé ?','Non ; les troubles surrénaliens non traités sont contre-indiqués et la substitution glucocorticoïde doit précéder la T4 lorsqu’elle est nécessaire.','La sécurité endocrine précède la correction isolée du chiffre thyroïdien.',['aips83-euthyrox-ci','aips83-euthyrox-prudence']),
('La plage adulte de 100–200 µg par jour est-elle un objectif à atteindre chez tous ?','Non ; elle correspond à une dose d’entretien usuelle de la notice.','La dose dépend du patient, et les personnes âgées ou fragiles peuvent nécessiter moins.',['aips83-euthyrox-posologie']),
('Une personne âgée doit-elle recevoir d’emblée la même dose qu’un adulte sans comorbidité ?','Non ; l’AIPS recommande une initiation plus faible à 25 µg et une augmentation prudente à intervalles plus longs.','L’âge et le terrain modifient la tolérance, sans créer une indication à traiter toute TSH légèrement élevée.',['aips83-euthyrox-posologie','has-age']),
('Le schéma adulte présenté peut-il être repris automatiquement chez un enfant ?','Non ; les besoins pédiatriques et les conditions propres à l’âge doivent être considérés.','Le rôle hormonal dans la croissance rend cette adaptation particulièrement importante.',['aips83-euthyrox-posologie','aips83-euthyrox-prudence']),
('Peut-on prendre la T4 avec le fer puis augmenter la dose si la TSH monte ?','La T4 doit être prise au moins 2 heures avant les sels de fer selon l’AIPS Euthyrox.','Les modalités de prise et interactions sont corrigées avant une augmentation non justifiée.',['aips83-euthyrox-interactions','has-suivi']),
('Une biotine peut-elle expliquer un résultat hormonal discordant ?','Oui ; certains immunodosages deviennent faussement hauts ou bas.','Le laboratoire est informé et une méthode non soumise à cette interférence est recherchée si possible.',['aips83-euthyrox-prudence']),
('La grossesse impose-t-elle l’arrêt de la lévothyroxine substitutive ?','Non ; la prise est poursuivie sans interruption sous surveillance spécialisée, avec adaptation possible des besoins.','L’arrêt confondrait la substitution indiquée avec une autre situation contre-indiquée d’association aux thyréostatiques.',['aips83-euthyrox-grossesse']),
('Une faiblesse persistante avec TSH équilibrée impose-t-elle toujours davantage de T4 ?','Non ; la HAS demande de rechercher les causes d’instabilité ou un diagnostic différentiel.','Une escalade sans justification expose au surtraitement et peut manquer une autre maladie musculaire.',['has-suivi','aips83-euthyrox-prudence','dgn-imnm']),
('Le plein effet pharmacologique à 1–3 semaines garantit-il une guérison musculaire complète dans ce délai ?','Non ; cette donnée décrit l’effet de la T4 et ne constitue pas un délai universel de récupération fonctionnelle.','L’amélioration clinique et la force sont suivies avec l’équilibre biologique.',['aips83-euthyrox-pd','has-suivi','cen-force']),
('Un certificat destiné à l’employeur doit-il mentionner l’hypothyroïdie et la dose ?','Non ; le cadre ASSM/FMH prévoit le degré et les dates de l’incapacité sans diagnostic ni traitement.','Les capacités résiduelles sont évaluées selon le poste, en respectant le secret médical.',['fmh-certificat','fmh-evaluation','fmh-secret'])]
s+=rows(['Question','Réponse correcte','Raison clinique'],[[ (a,ids),(b,ids),(c,ids)]for a,b,c,ids in qs])
question='Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ?'
s+='<p class="question-finale" id="dx7-question-finale">'+question+cite(['prompt-question-finale'])+'</p>\n'
save(s)
(D/'paquet.json').write_text(json.dumps(P,ensure_ascii=False,indent=2)+'\n')
(D/'contrat.json').write_text(json.dumps(C,ensure_ascii=False,indent=2)+'\n')

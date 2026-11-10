from pathlib import Path
import json
B=Path(__file__).parent;D=B/'DX.4';A={'entite':'Contusion musculaire traumatique','references':{},'points':{str(n):{'blocs':[],'fenetres':[],'tableaux':[]}for n in range(1,15)}}
def lines(s):return[x.split('|',1)for x in s.strip().split('\n')if x.strip()]
def b(n,t,s):A['points'][str(n)]['blocs'].append([t,lines(s)])
def w(n,t,s):A['points'][str(n)]['fenetres'].append([t,lines(s)])
def table(n,t,h,rows):A['points'][str(n)]['tableaux'].append([t,h,[[x.split('|',1)for x in r]for r in rows]])
b(1,'Une lésion liée à un impact externe', '''ismult-direct+ismult-date|La société ISMuLT définit la contusion comme une atteinte provoquée par un traumatisme direct, dans ses recommandations de 2013.
ismult-direct|L’impact peut survenir contre un adversaire ou un objet sportif et produire une incapacité fonctionnelle de sévérité variable.
ismult-contusion-grade|La douleur et la diminution des amplitudes accompagnent un hématome localisé ou diffus après ce traumatisme.
ismult-clinique|La chronologie typique commence au moment du choc ; les symptômes peuvent ensuite augmenter avec la taille de l’hématome.
rms-mecanisme|Ce mécanisme extrinsèque se distingue de la lésion indirecte par allongement excessif, contraction violente ou déséquilibre des contraintes musculaires.
ismult-direct|Une lacération implique un contact avec une surface tranchante et ne doit pas être assimilée à une simple contusion fermée.
doms-mecanisme|Les courbatures retardées suivent une charge inhabituelle avec un intervalle peu symptomatique, au lieu d’être définies par un impact direct.
rhabdo-physiopath|Une destruction musculaire étendue peut provoquer une rhabdomyolyse ; cette conséquence systémique exige alors une analyse dépassant la seule lésion locale.''')
w(1,'Nommer le mécanisme et décrire la gravité séparément', '''ismult-direct|Le mot contusion renseigne sur la cause directe, tandis que la gravité dépend notamment de la limitation fonctionnelle qui suit.
ismult-contusion-grade|Un hématome peut être local ou diffus et la douleur varie avec l’impact, le gonflement et les mouvements.
ismult-direct|L’évaluation immédiate peut surestimer la lésion lorsque la douleur domine ; une réévaluation à 24 heures affine l’appréciation.
r82-boast2025-loges-0|Cette réévaluation programmée ne s’applique pas à une suspicion de syndrome compartimental, dont les signes réclament une conduite urgente.''')
w(1,'Lésion fermée, hématome et complication', '''ismult-direct+ismult-contusion-grade|L’absence de plaie ne signifie pas absence de dommage musculaire, puisque l’impact peut entraîner une accumulation sanguine intramusculaire.
gots-ponction|L’hématome correspond à une collection sanguine liée aux lésions vasculaires et tissulaires, dont l’aspect évolue au cours du temps.
r82-boast2025-loges-0|Le syndrome compartimental résulte d’une pression accrue dans un espace myofascial, avec ischémie des tissus qu’il contient.
gots-ains|La myosite ossifiante désigne une formation osseuse ou cartilagineuse hétérotopique non tumorale, parfois observée après une lésion avec hématome.''')
b(2,'Des données sportives à replacer dans leur population', '''sems-3|La revue suisse SEMS décrit les lésions musculaires directes dans moins de 15 % des cas du contexte sportif qu’elle analyse.
sems-3|Cette proportion ne constitue pas une fréquence nationale des contusions parmi tous les motifs de consultation pour douleur musculaire.
ismult-direct|Tout muscle exposé à un impact peut être concerné ; la circonstance traumatique aide donc à identifier la région à examiner.
rms-clinique|L’âge, les comorbidités, les antécédents et la pratique sportive influencent l’évaluation et les décisions thérapeutiques individuelles.
ismult-contusion-grade|La limitation du mouvement et la douleur dépendent de l’étendue de l’hématome et de la sévérité de l’impact.
gots-ponction|Une collection peut devenir plus apparente secondairement, ce qui explique l’intérêt des contrôles lorsque la symptomatologie évolue.
sems-13|Une contusion sévère de certains muscles, notamment le vaste intermédiaire, peut évoluer vers une myosite ossifiante.
rms-persistance|Une douleur persistante ou une fonction qui ne progresse pas invite à rechercher une complication et à reconsidérer le diagnostic initial.''')
w(2,'Le pronostic ne se résume pas à une date de retour', '''rms-reprise|Le retour au sport tient compte de la douleur, des amplitudes et de la force, puis augmente progressivement les contraintes.
ismult-rehab|La réhabilitation introduit des contraintes contrôlées en fonction du muscle touché et des exigences de l’activité.
sems-13|Un retour trop précoce et les massages profonds par friction sont déconseillés dans les situations à risque de myosite ossifiante.
rms-persistance|Une récupération discordante avec la lésion attendue appelle un nouvel examen plutôt qu’une simple prolongation du calendrier sportif.''')
b(3,'Du choc aux perturbations locales', '''ismult-contusion-grade|L’impact direct peut produire un hématome et une douleur immédiate, puis limiter le mouvement de la région atteinte.
gots-ponction|Les lésions des vaisseaux associés au muscle permettent l’accumulation sanguine ; celle-ci peut accentuer la réaction inflammatoire locale.
sems-10|Le tissu conjonctif musculaire contient les structures neurovasculaires et contribue à limiter le saignement ainsi que la rétraction des faisceaux.
sems-10|Une atteinte du périmysium ou de l’aponévrose modifie le processus de guérison et peut prolonger les limitations.
gots-price|Le traitement initial cherche à réduire saignement, douleur et œdème, en tenant compte du niveau de preuve limité de plusieurs mesures.
gots-mobilisation|La réparation comporte une matrice provisoire et l’intervention de cellules satellites, tandis que la mobilisation doit respecter le stade et la gravité.
r82-boast2025-loges-0|Une augmentation excessive de pression dans la loge menace la perfusion, ce qui transforme une lésion locale en urgence fonctionnelle.
rhabdo-physiopath|Si une destruction musculaire étendue survient, la libération de myoglobine et d’électrolytes expose aussi à des complications systémiques.''')
table(3,'Relier dommage, exploration et traitement',['Mécanisme','Constat utile','Réponse clinique'],[
['ismult-contusion-grade|Le choc s’accompagne d’une douleur et d’un saignement musculaire.','rms-clinique|L’inspection et la palpation recherchent ecchymose, gonflement, douleur et anomalies des contours.','gots-price|La protection et les mesures initiales visent à limiter l’aggravation du saignement et de l’œdème.'],
['gots-ponction|Une accumulation sanguine peut se constituer ou se délimiter après l’examen initial.','ismult-us+gots-ponction|L’échographie caractérise la collection et peut guider un geste lorsqu’il est retenu.','gots-ponction|Une aspiration se discute selon la localisation et l’état du sang, sans promesse de bénéfice démontré sur le retour sportif.'],
['r82-boast2025-loges-0|Une pression intracompartimentale excessive réduit la perfusion des tissus.','r82-boast2025-loges-0+r82-boast2025-loges-1|La douleur disproportionnée, la douleur passive et les signes neurovasculaires sont recherchés et répétés.','r82-boast2025-loges-3|Le diagnostic établi déclenche une décompression chirurgicale immédiate.'],
['gots-ains|Une ossification hétérotopique peut compliquer certaines lésions avec hématome.','gots-ains|L’imagerie peut montrer des calcifications périphériques selon le stade de la complication.','rms-persistance+sems-13|L’évolution est réévaluée et les contraintes ou massages aggravants sont évités.'],
['rhabdo-physiopath|La nécrose musculaire libère des composants susceptibles d’atteindre le rein.','rhabdo-laboratoire+rhabdo-orientation|Le bilan biologique et urinaire recherche une atteinte musculaire systémique et ses complications.','rhabdo-orientation|Le lieu de soins et la surveillance sont adaptés à la gravité plutôt qu’au seul aspect de l’ecchymose.']])
w(3,'Un hématome change avec le temps', '''gots-ponction|Dans la phase précoce, le sang extravasé peut être difficile à distinguer des tissus voisins et la collection peut apparaître secondairement.
ismult-us|La concordance entre examen clinique et échographie doit donc être réévaluée lorsque les symptômes ou les constatations se modifient.
gots-ponction|La coagulation et l’organisation du sang peuvent ensuite limiter la possibilité d’aspiration, même lorsque l’hématome reste visible.
gots-ponction|Une hémorragie diffuse ne se traite pas comme une collection bien délimitée, car l’évacuation complète peut être techniquement impossible.''')
w(3,'Protection et charge : deux objectifs successifs', '''gots-protection|Une protection initiale réduit les contraintes supplémentaires sur les tissus lésés, en plaçant le membre dans une position de soulagement.
ismult-rehab|Le programme ultérieur apporte progressivement des contraintes mécaniques contrôlées plutôt qu’une immobilité prolongée indépendante de la fonction.
gots-mobilisation|La recommandation GOTS souligne que la durée optimale d’immobilisation n’a pas été établie par des comparaisons cliniques suffisamment solides.
rms-reprise|La décision de progression utilise donc les observations cliniques et la tolérance fonctionnelle, avec un suivi adapté à la lésion.''')
b(4,'Avant de conclure à une contusion simple', '''r82-boast2025-loges-0|Une douleur disproportionnée ou accentuée par l’étirement passif exige de rechercher un syndrome aigu des loges.
r82-boast2025-loges-3|Une fois confirmé, ce syndrome relève d’une décompression immédiate ; l’attente d’un contrôle sportif est inappropriée.
rhabdo-physiopath+rhabdo-clinique|Un traumatisme avec atteinte musculaire importante peut aussi provoquer une rhabdomyolyse, parfois sans présentation clinique complète.
rms-clinique|Une fracture, un arrachement osseux, une atteinte tendineuse ou une cause veineuse font partie des diagnostics à considérer selon l’examen.
ismult-clinique|Une perte immédiate de fonction avec défaut palpable évoque une interruption musculotendineuse et demande une caractérisation spécifique.
doms-mecanisme|Une douleur retardée diffuse après charge inhabituelle relève d’un autre mécanisme que la douleur attribuable à un impact identifié.''')
table(4,'Distinguer les lésions qui imposent une autre filière',['Diagnostic','Élément discriminant','Piège','Action'],[
['r82-boast2025-loges-0|Le syndrome aigu des loges menace les tissus du compartiment.','r82-boast2025-loges-0|La douleur disproportionnée et la douleur passive constituent des signes d’alerte.','r82-boast2025-loges-1|Une seule évaluation ne remplace pas le suivi neurovasculaire et douloureux documenté.','r82-boast2025-loges-2+r82-boast2025-loges-3|La suspicion entraîne une réévaluation urgente et le diagnostic confirmé une décompression.'],
['rhabdo-physiopath|Une rhabdomyolyse complique une destruction musculaire.','rhabdo-laboratoire|Les CK et le contexte urinaire ou biologique caractérisent cette atteinte.','rhabdo-clinique|L’absence de triade complète ne rassure pas suffisamment.','rhabdo-orientation|La prévention des complications rénales et électrolytiques détermine la prise en charge.'],
['ismult-clinique|Une rupture importante interrompt la continuité musculotendineuse.','ismult-clinique|Le déficit fonctionnel immédiat, un claquement et un défaut palpable soutiennent cette hypothèse.','ismult-clinique|Une lésion moins étendue peut rester non palpable malgré la douleur.','ismult-irm+ismult-rehab|L’imagerie et l’avis spécialisé précisent la lésion et les possibilités thérapeutiques.'],
['rms-clinique|Une lésion osseuse ou tendineuse peut expliquer la douleur après traumatisme.','rms-clinique|La localisation, le mécanisme et l’examen des structures voisines guident la recherche.','ismult-direct|La seule existence d’un choc ne prouve pas que le muscle constitue l’unique structure lésée.','rms-imagerie|Les examens sont orientés vers la structure suspectée et le degré de gravité.']])
w(4,'Ne pas confondre réaction locale et atteinte systémique', '''rhabdo-clinique|Une rhabdomyolyse peut associer douleur, faiblesse et pigmenturie, mais la forme non traumatique présente rarement toute cette triade.
rhabdo-physiopath|L’atteinte systémique résulte de la destruction cellulaire et de ses conséquences circulatoires, rénales et électrolytiques.
rhabdo-laboratoire|La bandelette urinaire positive pour le sang sans érythrocytes au sédiment peut soutenir une myoglobinurie dans le bon contexte.
rhabdo-orientation|Le bilan de cette complication ne doit pas être repoussé au seul motif qu’une contusion semble expliquer la douleur locale.''')
b(5,'Reconstituer l’impact et le retentissement', '''rms-clinique|Le récit précise l’activité, l’intensité, le geste et les circonstances de l’impact, puis décrit la fonction immédiatement après l’événement.
ismult-direct|Le mécanisme contre une personne ou un objet renseigne sur la zone exposée et la possibilité d’une atteinte directe.
ismult-clinique|L’augmentation secondaire des symptômes est confrontée à la progression du gonflement et à la taille potentielle de l’hématome.
rms-clinique|Les antécédents, les comorbidités et les exigences sportives permettent d’individualiser les examens et les mesures de protection.
aips-oa82-dafalgan-interactions|Les traitements habituels, notamment anticoagulants, sont recensés avant de discuter une antalgie répétée et ses interactions.
rms-persistance|Une histoire de symptômes antérieurs ou d’évolution atypique fait envisager une autre lésion révélée par le traumatisme ou par l’activité.''')
table(5,'Anamnèse reliée aux risques',['Question','Pourquoi la poser','Conséquence'],[
['ismult-direct|Quelle région a reçu le choc et contre quelle surface ?','ismult-direct|La contusion implique un impact direct, différent du contact tranchant d’une lacération.','rms-clinique|L’examen inspecte la peau et explore les structures de cette région.'],
['ismult-clinique|La fonction a-t-elle disparu immédiatement ou diminué progressivement ?','ismult-clinique|Une rupture importante et un hématome évolutif peuvent avoir des expressions différentes.','ismult-clinique+rms-imagerie|La réponse guide l’examen ciblé et le besoin d’imagerie.'],
['r82-boast2025-loges-0|La douleur paraît-elle excessive et augmente-t-elle lors d’un mouvement passif ?','r82-boast2025-loges-0|Une pression excessive dans une loge peut menacer la perfusion tissulaire.','r82-boast2025-loges-2|Les signes déclenchent la conduite urgente et la réévaluation rapprochée.'],
['rhabdo-clinique|Des urines foncées, une faiblesse inhabituelle ou des symptômes généraux sont-ils associés ?','rhabdo-physiopath|Une destruction musculaire peut dépasser le dommage local apparent.','rhabdo-laboratoire+rhabdo-orientation|Le bilan biologique recherche les complications et détermine la filière de soins.'],
['rms-clinique|Quelles activités quotidiennes et sportives deviennent impossibles ?','rms-reprise|Le retentissement fonctionnel constitue un repère de gravité et de progression.','ismult-rehab|La protection et la réhabilitation sont adaptées aux contraintes réelles du patient.'],
['aips-oa82-dafalgan-posologie|Quels antalgiques ont déjà été pris et sous quelles formulations ?','aips-oa82-dafalgan-prudence|Le cumul peut exposer à une toxicité malgré une intention de soulagement.','aips-oa82-dafalgan-posologie|Les doses totales et les conditions de terrain sont vérifiées avant une nouvelle prise.']])
w(5,'Drapeaux rouges à convertir en action', '''r82-boast2025-loges-0+r82-boast2025-loges-3|Une suspicion compartimentale réclame un avis urgent ; sa confirmation impose le traitement chirurgical sans délai de surveillance ambulatoire.
rhabdo-physiopath+rhabdo-orientation|Une atteinte musculaire étendue avec signes systémiques entraîne l’évaluation rénale et électrolytique et une orientation adaptée.
ismult-clinique+ismult-rehab|Une perte complète de fonction ou une interruption palpable motive une recherche de rupture importante et l’avis spécialisé correspondant.
rms-persistance|Une douleur durable, une masse ou une limitation qui ne suit pas l’évolution attendue impose de revoir le diagnostic et ses complications.''')
b(6,'Le normal avant la lésion : établir un examen de référence', '''rms-clinique|Un muscle habituellement fonctionnel présente des contours sans encoche ni voussure traumatique, et les mouvements sont comparés au côté opposé.
n81-hug22-force-normale|Une force normale correspond à la cotation 5 ; l’examen la distingue d’un mouvement possible uniquement contre la gravité ou sans résistance.
rms-clinique|L’inspection décrit peau, ecchymose, gonflement et contours avant que la palpation localise la douleur ou un éventuel défaut.
ismult-contusion-grade|Dans la contusion, douleur, tuméfaction et amplitudes diminuées sont rapprochées de la zone d’impact et du retentissement.
rms-clinique|Les amplitudes actives et passives, la douleur à l’étirement et la contraction musculaire ciblée complètent l’analyse.
r82-boast2025-loges-1|Le bilan neurologique et vasculaire, l’horaire des observations et la réponse antalgique sont consignés lorsque la situation expose à une complication.
n81-cen-sensibilite|Le tact est comparé entre les côtés et entre segments, afin de repérer une anomalie sensitive qui ne relève pas de la douleur seule.''')
w(6,'Palper et tester sans réduire l’examen au bleu visible', '''rms-clinique|La palpation recherche contracture, diminution du ballant et douleur provoquée, en précisant la localisation dans le muscle et les tissus voisins.
ismult-clinique|Un défaut palpable ou une perte de fonction évoque une interruption plus importante que ne le suggère parfois l’aspect cutané.
ismult-clinique|Une contraction contre résistance peut reproduire une douleur focale dans une petite lésion structurale, même sans creux palpable.
gots-ponction|Un hématome précoce peut rester difficile à identifier, ce qui rend l’évolution clinique et les examens répétés importants.
r82-boast2025-loges-0|La mobilisation passive douloureuse est particulièrement préoccupante lorsqu’elle paraît disproportionnée au traumatisme et à l’examen initial.''')
w(6,'Cotation motrice et interprétation de la douleur', '''n81-cen-force|Le mouvement est évalué muscle par muscle en comparant les côtés, avec résistance appropriée à l’action recherchée.
n81-cen-force|La cotation 4 décrit un mouvement contre résistance, tandis que 3 correspond au mouvement contre la pesanteur.
n81-cen-force|La cotation 2 correspond à un déplacement sans lutte contre la pesanteur ; 1 décrit une contraction sans effet moteur.
n81-cen-force|La cotation 0 signale l’absence de contraction et 5 une force normale, à interpréter avec la qualité de l’examen.
rms-clinique+ismult-clinique|Le compte rendu distingue douleur limitante, force observée et perte de fonction, afin de ne pas attribuer toute faiblesse au même mécanisme.''')
w(6,'Répéter l’examen lorsque le tableau change', '''ismult-direct|L’ISMuLT conseille un nouvel examen à 24 heures après une contusion pour mieux apprécier la lésion malgré la douleur initiale.
gots-ponction|Le GOTS recommande aussi des contrôles lorsque l’hématome peut apparaître secondairement et avant les décisions de mobilisation.
r82-boast2025-loges-2|Ces contrôles programmés ne remplacent pas les examens horaires lorsque l’évaluation compartimentale demeure incomplète ou équivoque.
r82-boast2025-loges-1|Chaque observation conserve son horaire et les constatations neurovasculaires, afin de comparer réellement l’évolution.''')
b(7,'7.1 — Syndrome contusif local', '''ismult-contusion-grade|Le patient décrit une douleur après impact, tandis que l’examen retrouve une tuméfaction, un hématome possible et une mobilité réduite.
ismult-clinique|Le caractère immédiat et la concordance avec le point d’impact soutiennent la nature contusive, sans exclure les lésions associées.
rms-clinique|La palpation et les mouvements ciblés déterminent les zones douloureuses et le retentissement, plutôt que la seule couleur de la peau.''')
b(7,'7.2 — Syndrome déficitaire musculotendineux', '''ismult-clinique|Une impotence importante, une interruption palpable ou une contraction inefficace fait envisager une atteinte structurale étendue.
rms-clinique+n81-cen-force|La force, les amplitudes et la réponse douloureuse sont documentées séparément pour différencier l’inhibition douloureuse d’une perte mécanique de continuité.
ismult-irm|L’imagerie peut préciser l’étendue, les structures profondes et une éventuelle participation tendineuse ou une avulsion.''')
b(7,'7.3 — Syndrome compartimental et atteinte systémique', '''r82-boast2025-loges-0|Une douleur disproportionnée avec douleur passive évoque l’augmentation dangereuse de pression dans la loge musculaire.
r82-boast2025-loges-1|Les constatations neurologiques et vasculaires sont relevées avec la douleur et son évolution après analgésie.
rhabdo-clinique+rhabdo-physiopath|Une faiblesse accompagnée de pigmenturie ou de manifestations générales peut indiquer une destruction musculaire avec conséquences systémiques.
rhabdo-laboratoire|La biologie et l’examen urinaire contribuent alors à identifier une rhabdomyolyse, au lieu de limiter le diagnostic au traumatisme local.''')
w(7,'Hématome, ecchymose et gonflement', '''gots-ponction|L’hématome est une accumulation de sang dans les tissus lésés, dont la morphologie et la possibilité d’évacuation varient avec le temps.
rms-clinique|L’ecchymose constitue une constatation cutanée à l’inspection, tandis que le gonflement et la douleur se précisent aussi par palpation.
ismult-contusion-grade|La présence d’un hématome peut accompagner une diminution de mobilité et une douleur croissante après la contusion.
gots-ponction|Une échographie peut aider à distinguer une collection accessible d’une hémorragie diffuse, sans justifier automatiquement une ponction.''')
w(7,'Myosite ossifiante : une complication différente de la douleur initiale', '''gots-ains|La myosite ossifiante correspond à une formation hétérotopique de tissu osseux ou cartilagineux, non néoplasique, dans ce contexte traumatique.
gots-ains|Elle est souvent associée à un antécédent d’hématome intramusculaire et peut se révéler par des signes de calcification à l’échographie.
sems-13|La revue suisse signale particulièrement le risque après contusion du vaste intermédiaire et conseille d’éviter retour trop précoce et friction profonde.
rms-persistance|Une limitation durable ou une évolution inhabituelle appelle donc une réévaluation, plutôt qu’une intensification aveugle des massages.''')
(D/'contenu.json').write_text(json.dumps(A,ensure_ascii=False,indent=2)+'\n')

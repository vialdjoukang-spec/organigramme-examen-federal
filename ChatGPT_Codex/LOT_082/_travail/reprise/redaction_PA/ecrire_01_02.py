from rendu import Point

p = Point(1)
p.h('Le siège et le tissu atteint précisent le sens de la déformation')
p.p('Une modification de forme peut traduire un trouble articulaire, osseux ou aponévrotique ; son aspect ne suffit donc pas à nommer sa cause.', ['p82-arthrose', 'p82-radius', 'p82-dupuytren'])
p.p('Chez un enfant, une modification de l’axe peut aussi appartenir au développement normal, lorsque sa présentation et son évolution restent physiologiques.', 'p82-genou')
p.p('La priorité 🚩 E1 concerne une fracture du radius ouverte ou menaçant la peau, les nerfs ou la vascularisation.', 'p82-radius')
p.p('La priorité 🚩 E2 concerne un Charcot actif suspecté devant un pied rouge, chaud et gonflé sur terrain diabétique neuropathique.', 'p82-charcot')
p.p('Ces situations demandent une conduite immédiate, alors que les variantes souples indolores de l’enfant relèvent souvent d’une observation clinique.', ['p82-radius', 'p82-charcot', 'p82-plat-examen'])
p.fenetre('Déviation articulaire, déviation osseuse et rétraction des tissus', [
    ('Dans l’arthrose de la main, la destruction cartilagineuse s’accompagne d’inflammation et peut produire des articulations gonflées et des doigts déformés.', 'p82-arthrose'),
    ('Dans l’hallux valgus, le gros orteil dévie latéralement tandis que le premier métatarsien se dirige médialement, ce qui modifie l’avant-pied.', 'p82-hallux'),
    ('Dans la maladie de Dupuytren, l’aponévrose située sous la peau palmaire épaissit puis se rétracte, ce qui empêche l’extension complète.', 'p82-dupuytren'),
    ('Dans le doigt en maillet, l’appareil extenseur terminal est lésé ; l’extrémité digitale ne peut donc plus être tendue activement.', 'p82-maillet'),
    ('Ainsi, une perte d’extension ne désigne pas automatiquement une arthrose : son siège et le tissu concerné permettent de distinguer ces présentations.', ['p82-arthrose', 'p82-dupuytren', 'p82-maillet']),
])
p.h('La souplesse et la croissance séparent variante et maladie')
p.p('Le pied plat valgus souple présente une voûte visible hors charge et aplatie debout ; la réductibilité guide donc son interprétation.', 'p82-plat-examen')
p.p('Cependant, un pied rigide ou douloureux ne rejoint pas automatiquement cette variante physiologique et impose une évaluation différente.', 'p82-plat-examen')
p.p('Le genu varum du nouveau-né puis le genu valgum du jeune enfant constituent des formes décrites de variation physiologique frontale.', 'p82-genou')
p.p('En revanche, une déformation progressive associée à une croissance disproportionnée peut orienter vers un rachitisme hypophosphatémique plutôt que vers cette évolution habituelle.', 'p82-xlh-clinique')
p.fenetre('Hypophosphatémie liée à l’X : un diagnostic étiologique précis', [
    ('L’hypophosphatémie liée à l’X, abrégée XLH, est une maladie rare du métabolisme osseux avec pertes rénales excessives de phosphate.', 'p82-xlh-definition'),
    ('Elle est aussi appelée rachitisme hypophosphatémique ou rachitisme résistant à la vitamine D, mais sa cause est une mutation du gène PHEX.', 'p82-xlh-definition'),
    ('Le déficit chronique en phosphate perturbe alors la minéralisation et peut entraîner des déformations en varus ou en valgus des jambes.', ['p82-xlh-clinique', 'p82-xlh-mecanisme-bilan']),
    ('La perte de phosphate doit être interprétée selon l’âge, car les valeurs de référence adultes peuvent masquer une hypophosphatémie chez l’enfant.', 'p82-xlh-mecanisme-bilan'),
])
p.h('Le rachis et le pied neuropathique possèdent leurs définitions propres')
p.p('La scoliose est une déformation tridimensionnelle de la colonne, du thorax et du tronc ; elle ne se réduit donc pas à une inclinaison frontale.', 'p82-scoliose-definition')
p.p('La scoliose idiopathique de l’adolescent se distingue des formes secondaires neuromusculaires, syndromiques ou congénitales, dont la cause doit être recherchée.', 'p82-scoliose-definition')
p.p('Une différence de longueur des jambes peut modifier la position du bassin ; sa compensation participe donc à l’évaluation d’une asymétrie rachidienne.', 'p82-scoliose-clinique')
p.p('Le Charcot est un processus inflammatoire stérile sur neuropathie qui peut léser les os, les articulations et les tissus mous.', 'p82-charcot')
p.p('Les fractures et luxations progressives expliquent la déformation du pied, mais l’inflammation peut déjà imposer une protection avant cette déformation fixée.', 'p82-charcot')
p.fenetre('Déformation, douleur et activité de la maladie ne sont pas synonymes', [
    ('Un hallux valgus peut être asymptomatique, alors que le frottement de sa saillie dans la chaussure peut devenir douloureux.', 'p82-hallux'),
    ('La rétraction palmaire de Dupuytren est habituellement indolore ; le motif de consultation est souvent la difficulté croissante à étendre les doigts.', 'p82-dupuytren'),
    ('La douleur liée à l’arthrose augmente généralement avec l’usage de la main et diminue au repos, ce qui précise le retentissement fonctionnel.', 'p82-arthrose'),
    ('Dans le Charcot, la disparition d’un signe isolé ne définit pas la rémission : température, œdème et imagerie doivent être confrontés.', 'p82-charcot'),
])
p.sauver()

p = Point(2)
p.h('Les fréquences s’interprètent dans leur population et leur territoire')
p.p('Les Hôpitaux universitaires de Genève, abrégés HUG, décrivent l’arthrose de la main comme très fréquente avec l’âge, notamment après la ménopause.', 'p82-arthrose')
p.p('Ainsi, une déformation articulaire de la main chez une personne âgée s’inscrit dans un contexte différent d’une déviation développementale des jambes.', ['p82-arthrose', 'p82-genou'])
p.p('L’hallux valgus est décrit par les HUG comme une déformation fréquente de l’avant-pied, avec une prédominance féminine.', 'p82-hallux')
p.p('Le Centre hospitalier universitaire vaudois, abrégé CHUV, qualifie le doigt en maillet d’extrêmement fréquent dans son lexique clinique.', 'p82-maillet')
p.p('Ces qualifications concernent des tableaux localisés ; elles ne constituent pas une distribution commune de toutes les déformations du squelette.', ['p82-arthrose', 'p82-hallux', 'p82-maillet'])
p.tableau(['Observation rapportée', 'Population et territoire', 'Source datée et portée'], [
    [('Les HUG rapportent une proportion de 23 %.', 'p82-hallux'), ('Ce chiffre concerne l’hallux valgus entre 18 et 65 ans.', 'p82-hallux'), ('L’information institutionnelle des HUG sur l’hallux décrit cette population par âge, sans la limiter à une cohorte suisse.', 'p82-hallux')],
    [('La proportion rapportée dépasse 35 % après 65 ans.', 'p82-hallux'), ('Le territoire reste l’avant-pied atteint d’un hallux valgus.', 'p82-hallux'), ('La même information HUG souligne une prédominance féminine ; le chiffre ne mesure pas toutes les déformations articulaires.', 'p82-hallux')],
    [('Paediatrica rapporte 54 % de pieds plats valgus à trois ans dans une étude observationnelle citée.', 'p82-plat-physio'), ('Les enfants observés appartiennent au groupe d’âge de trois ans.', 'p82-plat-physio'), ('La synthèse pédiatrique distingue ce constat du diagnostic individuel de pied symptomatique.', ['p82-plat-physio', 'p82-plat-examen'])],
    [('La même étude citée rapporte 26 % à six ans.', 'p82-plat-physio'), ('Cette observation concerne le développement de la voûte plantaire pendant l’enfance.', 'p82-plat-physio'), ('La fréquence diminue avec la croissance ; une forme flexible indolore conserve donc une signification développementale.', ['p82-plat-physio', 'p82-plat-examen'])],
])
p.fenetre('Ce que les données de population disent de la croissance du pied', [
    ('La synthèse pédiatrique rapporte aussi une prévalence de 97 % du pied plat valgus pendant les premières années de vie.', 'p82-plat-physio'),
    ('Elle relie la diminution de fréquence à la formation progressive de la voûte, notamment entre trois et six ans.', 'p82-plat-physio'),
    ('D’autres auteurs cités décrivent un redressement lié à la croissance jusqu’à dix ans, ce qui explique la variabilité des repères temporels.', 'p82-plat-physio'),
    ('Cependant, le caractère douloureux, rigide ou neurologique du pied impose une autre appréciation que la seule comparaison à l’âge.', 'p82-plat-examen'),
])
p.h('L’histoire naturelle précise la place de chaque hypothèse')
p.p('Les déviations physiologiques frontales du genou sont un motif fréquent d’inquiétude parentale et de consultation, avec une évolution habituellement spontanément résolutive.', 'p82-genou')
p.p('La majorité relève d’une surveillance clinique, tandis que les rares troubles pathologiques non reconnus peuvent entraîner un retentissement fonctionnel ultérieur.', 'p82-genou')
p.p('Selon la description de l’Hôpital universitaire de Zurich, Dupuytren apparaît généralement entre 40 et 60 ans et touche davantage les hommes.', 'p82-dupuytren')
p.p('La maladie est souvent bilatérale ; sa progression habituellement lente peut néanmoins être plus agressive chez certains sujets jeunes.', 'p82-dupuytren')
p.p('Les formes débutant avant 40 ans, bilatérales ou familiales figurent parmi les présentations associées à une évolution plus agressive.', 'p82-dupuytren')
p.p('Les HUG relient la fracture distale du radius à l’ostéoporose chez les sujets âgés et aux traumatismes à haute énergie chez les jeunes.', 'p82-radius')
p.p('Ainsi, le mécanisme traumatique et la fragilité osseuse modifient l’hypothèse clinique devant un poignet récemment déformé.', 'p82-radius')
p.h('La scoliose et les maladies rares gardent leur contexte propre')
p.p('La synthèse suisse sur la scoliose distingue environ 80 % de formes idiopathiques et environ 20 % de formes secondaires.', 'p82-scoliose-definition')
p.p('Ces proportions concernent les scolioses ; elles ne classent donc ni les déformations de la main ni les anomalies des axes des membres.', 'p82-scoliose-definition')
p.p('La forme idiopathique de l’adolescent est la plus fréquente des scolioses et concerne des adolescents dès dix ans.', 'p82-scoliose-definition')
p.p('Les formes plus marquées touchent davantage les filles, et la croissance résiduelle intervient dans les choix de prise en charge.', 'p82-scoliose-definition')
p.p('L’XLH appartient aux maladies rares, mais ses déformations progressives peuvent apparaître dès la petite enfance avec une croissance disproportionnée.', ['p82-xlh-definition', 'p82-xlh-clinique'])
p.p('Des mutations spontanées représentent jusqu’à 30 % des cas rapportés ; une histoire familiale négative n’élimine donc pas cette maladie.', 'p82-xlh-definition')
p.fenetre('Transmission et conséquences à long terme de l’XLH', [
    ('La transmission est dominante liée à l’X ; toutes les filles d’un père atteint héritent de cette atteinte décrite par la source.', 'p82-xlh-definition'),
    ('Chez une mère porteuse de la mutation, le risque de transmission rapporté est de 50 %, indépendamment du sexe de l’enfant.', 'p82-xlh-definition'),
    ('Les adultes non diagnostiqués peuvent présenter une ostéomalacie, des douleurs osseuses, des pseudo-fractures, une raideur ou des enthésopathies.', 'p82-xlh-clinique'),
    ('Les abcès dentaires et les complications crâniennes rappellent que cette maladie concerne plusieurs organes, au-delà de l’aspect des jambes.', 'p82-xlh-clinique'),
])
p.h('Le retentissement ne se mesure pas seulement à l’aspect visible')
p.p('L’arthrose peut limiter fortement les activités manuelles ordinaires, car les mouvements usuels deviennent douloureux ou parfois impossibles.', 'p82-arthrose')
p.p('Dupuytren gêne progressivement l’usage de la main lorsque la rétraction empêche l’extension, même en l’absence de douleur importante.', 'p82-dupuytren')
p.p('Dans le Charcot actif, la protection peut durer plusieurs mois et demande un suivi rapproché pour prévenir les complications du traitement.', 'p82-charcot')
p.p('L’immobilisation prolongée peut notamment s’accompagner d’ulcération, d’atrophie musculaire ou de surcharge du membre opposé, ce qui impose une surveillance adaptée.', 'p82-charcot')
p.sauver()

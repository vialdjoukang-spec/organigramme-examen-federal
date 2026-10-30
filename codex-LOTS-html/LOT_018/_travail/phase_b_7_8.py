from format_phase_b import Lesson, paras, table, steps
from medicaments_phase_b import methylprednisolone

def rediger():
    l=Lesson(7,[2,19,20,21,27])
    l.add('Le décollement rhegmatogène sépare la rétine neurosensorielle de son support par passage de liquide à travers une déchirure. Les {mécanismes de décollement} le distinguent des formes tractionnelles et exsudatives. La suspicion impose un examen rétinien urgent.',
        paras('Une déchirure permet au vitré liquéfié de passer sous la rétine. Une traction peut au contraire soulever la rétine sans déchirure initiale, notamment dans une rétinopathie proliférante. Une exsudation peut aussi décoller la rétine sans rupture.',
              'Le décollement postérieur du vitré est fréquent avec l’âge et ne constitue pas à lui seul un décollement de rétine. Il peut toutefois provoquer une déchirure lors de ses tractions : les symptômes récents doivent donc être examinés.'))
    l.add('Le risque augmente avec la myopie, l’âge, les traumatismes et certains antécédents chirurgicaux. Les {terrains à risque et le pronostic} orientent la vigilance. L’état de la macula influence fortement la récupération.',
        paras('La page HUG décrit une affection rare, surtout après 50 ans, et cite un ordre de grandeur d’une personne sur 10 000. Elle ne précise pas dans l’extrait retenu un dénominateur temporel suffisant pour en faire ici une incidence annuelle suisse.',
              'Un antécédent dans l’autre œil ou dans la famille augmente la vigilance. Le décollement peut progresser d’un déficit périphérique vers la macula. La restauration anatomique n’assure pas une récupération parfaite, notamment si la vision centrale était déjà atteinte.'))
    l.add('La traction vitréenne peut déchirer la rétine, puis le liquide la sépare de l’épithélium pigmentaire. La {chaîne anatomique et thérapeutique} explique l’urgence. Les techniques visent à fermer la rupture et à réappliquer la rétine.',
        paras('Les photorécepteurs ont besoin de leurs échanges avec l’épithélium pigmentaire et la circulation choroïdienne. Leur séparation perturbe rapidement la fonction. Une réaction fibreuse secondaire peut entretenir des tractions et compliquer la réparation.')+
        table(['Perturbation','Exploration','Correction mécanique'],[
            ['Traction et déchirure.','Examen périphérique spécialisé.','Laser ou cryothérapie pour créer une adhérence dans les indications adaptées.'],
            ['Rétine soulevée avec liquide.','Fond d’œil ; échographie si milieux opaques.','Indentation ou vitrectomie, avec traitement des ruptures.'],
            ['Traction persistante.','Examen rétinien et imagerie.','Vitrectomie et retrait de membranes selon cas.'],
            ['Besoin de maintenir l’apposition.','Évaluation peropératoire.','Gaz ou silicone selon technique ; consignes spécifiques après opération.']]))
    l.add('Éclairs, corps flottants et rideau imposent de rechercher une déchirure ou un décollement. Les {diagnostics différentiels prioritaires} incluent aussi l’ischémie et l’hémorragie vitréenne. Une bonne acuité centrale ne rassure pas sur la périphérie.',
        table(['Alternative','Discriminant','Action'],[
            ['🚩 E1 — Ischémie rétinienne.','Perte brutale ou transitoire sans progression typique de rideau.','Filière vasculaire urgente.'],
            ['Décollement postérieur du vitré sans déchirure.','Examen périphérique sans rupture.','Consignes et contrôle adapté ; l’examen initial doit être complet.'],
            ['Hémorragie vitréenne.','Fond d’œil masqué, voile et corps flottants.','Rechercher une déchirure/décollement par échographie et examen spécialisé.'],
            ['Migraine avec aura.','Phénomènes visuels à caractériser dans les deux yeux et leur évolution.','Ne pas attribuer un rideau monoculaire récent à la migraine sans évaluation.']]),[2,19])
    l.add('L’interrogatoire précise les symptômes et le risque rétinien. Les {questions qui déterminent l’urgence} cherchent surtout l’extension du déficit. Un traumatisme récent modifie aussi les précautions d’examen.',
        table(['Question','Mécanisme et action'],[
            ['Éclairs ou nouveaux corps flottants ?','Traction et possible rupture ; examen périphérique urgent.'],
            ['Ombre, rideau ou perte de lecture centrale ?','Décollement en extension ou macula atteinte ; documenter la chronologie.'],
            ['Myopie forte, chirurgie, traumatisme ou autre œil déjà atteint ?','Terrain à risque ; éviter une fausse rassurance.'],
            ['Douleur ou plaie possible ?','Rechercher une autre urgence ou un globe ouvert ; éviter les manœuvres compressives.'],
            ['Gaz déjà injecté et projet de voyage ou d’anesthésie ?','Prévenir une expansion dangereuse de la bulle.']]))
    l.add('L’examen compare l’acuité, le champ et les pupilles, puis explore la rétine périphérique. Les {gestes et limites de l’examen} doivent être documentés. Une échographie complète un fond d’œil inaccessible.',
        table(['Geste','Normal','Pathologique et limite'],[
            ['Acuité monoculaire et champ par confrontation.','Fonction sans déficit nouveau.','Déficit périphérique ou central ; l’acuité peut rester bonne si macula appliquée.'],
            ['Pupilles.','Réponses symétriques.','Un défaut afférent peut accompagner une atteinte étendue.'],
            ['Fond d’œil dilaté et exploration périphérique spécialisée.','Rétine appliquée, pas de rupture.','Rétine soulevée, plis et rupture ; l’ophtalmoscopie directe seule peut manquer une lésion périphérique.'],
            ['Échographie si milieux opaques.','Pas de décollement visible.','Confirmer ou préciser la rétine soulevée ; tenir compte des limites de l’examen.']]))
    l.add('Les {syndromes vitréorétiniens} décrivent une progression possible des signes. Les symptômes seuls ne permettent pas de dire si la rétine est intacte. La localisation du décollement explique le territoire du déficit.',
        table(['Syndrome','Signes fonctionnels','Signes physiques'],[
            ['7.1 — Traction/rupture.','Éclairs et corps flottants récents.','Déchirure ou signes vitréens à l’examen périphérique.'],
            ['7.2 — Décollement périphérique.','Rideau ou ombre.','Rétine soulevée avec macula encore appliquée possible.'],
            ['7.3 — Décollement maculaire.','Baisse de lecture et d’acuité centrale.','Macula décollée ; pronostic fonctionnel différent.'],
            ['7.4 — Complication proliférative.','Déficit persistant ou récidivant.','Membranes et tractions compliquant la réapplication.']]))
    l.add('Le diagnostic positif repose sur la visualisation d’une rétine décollée et la recherche de rupture. Les {critères anatomiques utiles} guident le geste opératoire. Le délai se décide avec l’équipe rétinienne, sans attente ambulatoire indéfinie.',
        paras('Décrire l’étendue, les ruptures, l’état maculaire et les facteurs compliquant la chirurgie. Le qualificatif rhegmatogène suppose une rupture expliquant le passage liquidien ; une traction ou une exsudation sans déchirure correspond à un autre mécanisme.',
              'Une macula encore appliquée doit être protégée rapidement. Une macula décollée reste une indication urgente d’évaluation et de réparation ; elle n’autorise pas à banaliser le délai. Les HUG évoquent des délais de quelques heures à quelques jours selon le cas, à déterminer par le spécialiste.'))
    l.add('Les {explorations nécessaires} recherchent les ruptures et précisent l’état maculaire. La clinique rétinienne reste centrale. Une imagerie disponible ne doit pas retarder l’appel spécialisé.',
        paras('9.a — Référence : examen rétinien dilaté spécialisé, avec exploration périphérique.',
              '9.b — Documenter acuité, champ, macula et ruptures ; OCT si utile pour préciser une atteinte maculaire sans retarder la conduite.',
              '9.c — Échographie si cataracte ou hémorragie empêche de voir le fond d’œil. Adapter les gestes si globe ouvert suspecté.',
              '9.d — Explorations supplémentaires guidées par le diagnostic différentiel ; pas d’angiographie systématique pour un décollement rhegmatogène évident.')+
        table(['Résultat','Signification','Conduite'],[
            ['Déchirure sans décollement significatif.','Lésion susceptible de progresser.','Traitement rétinien préventif selon indication.'],
            ['Décollement avec macula appliquée.','Vision centrale encore préservable.','Organisation urgente de la chirurgie.'],
            ['Rétine masquée.','Diagnostic non exclu.','Échographie et suivi spécialisé.']]))
    l.add('L’{arbre de décision} part des symptômes récents et aboutit à un examen périphérique. La distinction entre rupture seule et décollement change le traitement. Les restrictions après gaz doivent être anticipées.',
        steps('Si éclairs, nouveaux corps flottants ou rideau → contacter rapidement l’ophtalmologie pour examen périphérique.',
              'Si rétine non visible → organiser l’échographie sans conclure à l’absence de décollement.',
              'Si déchirure accessible sans décollement important → traitement rétinien selon spécialiste.',
              'Si décollement → déterminer macula, ruptures et technique chirurgicale ; organiser le délai urgent.',
              'Après intervention avec gaz → consignes écrites de position, altitude, avion et anesthésie.'))
    l.add('Le traitement est principalement chirurgical. Les {étapes et consignes postopératoires} visent la réapplication puis la sécurité du retour. La présence d’un gaz intraoculaire doit être signalée à tout soignant.',
        paras('11.A — Fermer les ruptures, réappliquer la rétine et préserver la fonction restante. Le résultat anatomique et le résultat visuel sont deux critères différents.',
              '11.B — Selon le cas, indentation externe, vitrectomie et traitement de la rupture sont associés. Un gaz ou du silicone peut maintenir l’apposition. La position de la tête dépend de la rupture et du geste ; elle n’est pas prescrite uniformément à tous.',
              'Tant qu’un gaz reste dans l’œil, pas de voyage aérien ; la brochure HUG indique aussi d’éviter les altitudes supérieures à 800 m jusqu’à disparition. Faire préciser le trajet et les restrictions par le chirurgien. Le protoxyde d’azote est à éviter impérativement en anesthésie ou analgésie tant que le gaz persiste, selon l’alerte du RCOphth.',
              '11.C — Contrôler rétine, pression et inflammation selon le calendrier remis. Baisse nouvelle, douleur croissante, rougeur importante ou sécrétions demandent un avis immédiat. Les gouttes postopératoires dépendent de la prescription chirurgicale vérifiée.',
              '11.D — Les HUG demandent un accompagnement au retour et une présence la première nuit. Avant sortie : rendez-vous, ordonnance, position et restrictions compris, signalement du gaz disponible. La récupération dépend notamment de la macula ; un déficit persistant peut nécessiter une réadaptation.'))
    l.add('Les {mesures de prévention} associent protection contre les traumatismes et reconnaissance des symptômes. Le suivi est adapté aux lésions et au terrain. Une chirurgie réfractive ne supprime pas tous les risques d’un œil myope.',
        paras('Primaire : protection oculaire lors d’activités à risque et information des personnes fortement myopes ou déjà opérées.',
              'Secondaire : examen rapide devant symptômes nouveaux ; traitement de certaines ruptures selon l’évaluation rétinienne, sans laser systématique de toute lésion périphérique.',
              'Tertiaire : respecter suivi et restrictions du tamponnement, reconnaître une récidive et adapter les activités à la vision restante.'))
    l.add('Éclairs et rideau demandent un examen rétinien urgent. Une acuité centrale conservée n’exclut pas un décollement. Le traitement dépend des ruptures et de la macula. Avec un gaz intraoculaire, respecter les restrictions d’avion, d’altitude et de protoxyde d’azote.')
    l.quiz([
        ('Que signifie rhegmatogène ?','Un décollement lié à une rupture rétinienne laissant passer du liquide.'),
        ('Un décollement du vitré est-il toujours un décollement de rétine ?','Non : il peut être isolé, mais peut aussi provoquer une déchirure.'),
        ('Une bonne lecture centrale exclut-elle un décollement ?','Non : la macula peut rester appliquée.'),
        ('Les éclairs seuls permettent-ils d’affirmer une déchirure ?','Non : un examen périphérique est nécessaire.'),
        ('Que faire si une hémorragie empêche de voir la rétine ?','Organiser une exploration adaptée, notamment une échographie.'),
        ('Le décollement est-il habituellement douloureux ?','Non ; la douleur impose aussi la recherche d’une autre cause.'),
        ('Le laser suffit-il pour tout décollement étendu ?','Non : une réparation chirurgicale est généralement nécessaire.'),
        ('Une macula décollée signifie-t-elle qu’il n’y a plus d’urgence ?','Non : le spécialiste doit organiser rapidement la réparation.'),
        ('La position postopératoire est-elle identique pour tous ?','Non : elle dépend du geste et de la localisation des ruptures.'),
        ('Peut-on prendre l’avion avec une bulle de gaz persistante ?','Non : son expansion peut augmenter dangereusement la pression.'),
        ('Quel gaz anesthésique doit être signalé comme dangereux dans ce contexte ?','Le protoxyde d’azote en présence de gaz intraoculaire.'),
        ('Le silicone et le gaz ont-ils exactement les mêmes consignes ?','Non : identifier le tamponnement et suivre les instructions propres du chirurgien.'),
        ('Une rétine recollée garantit-elle une vision normale ?','Non : des séquelles fonctionnelles peuvent persister.'),
        ('Quel symptôme après opération exige un retour rapide ?','Une baisse nouvelle, une douleur croissante, une rougeur importante ou des sécrétions.')])
    l.write()

    l=Lesson(8,[16,18,28,8])
    l.add('La névrite optique est une atteinte inflammatoire du nerf optique. Les {formes étiologiques} incluent la SEP, les maladies associées à AQP4 ou MOG et d’autres causes. Une névrite n’équivaut pas automatiquement à une SEP.',
        paras('Le terme rétrobulbaire désigne une atteinte située derrière la papille, qui peut laisser un fond d’œil normal. Une papillite correspond à une atteinte antérieure avec œdème papillaire.',
              'Les maladies associées aux anticorps AQP4 et MOG constituent des cadres distincts. Leur pronostic, les récidives et le traitement de fond peuvent différer de ceux de la SEP. Une infection ou une maladie inflammatoire systémique peut aussi produire une neuropathie inflammatoire.'))
    l.add('La présentation typique concerne souvent un adulte jeune, mais l’âge et le phénotype varient selon la cause. Les {repères d’évolution} doivent être rattachés à leur maladie. Le pronostic d’une névrite typique ne se généralise pas aux formes atypiques.',
        paras('Le COUF 2025 décrit une douleur aux mouvements dans environ 80 % des présentations typiques qu’il expose. Il rapporte une récupération souvent favorable sur plusieurs mois, avec possibles séquelles de contraste ou de couleurs. Ce chiffre n’est pas une sensibilité universelle pour toutes les névrites.',
              'Les formes AQP4 peuvent être sévères et laisser des séquelles importantes ; les formes MOG peuvent être bilatérales, œdémateuses et récidivantes. Une incidence suisse actuelle distinguant ces causes n’a pas été établie dans les sources retenues.'))
    l.add('L’inflammation altère la conduction du signal visuel, puis peut léser les axones. Les {mécanismes du déficit optique} relient pupilles, couleurs et imagerie. La récupération dépend de la cause et de la lésion axonale résiduelle.',
        paras('Les axones des cellules ganglionnaires forment le nerf optique. La myéline facilite la conduction ; sa perturbation ralentit ou bloque le signal. Une inflammation rétrobulbaire peut réduire la vision sans rendre la papille immédiatement anormale.',
              'Une démyélinisation peut rendre la conduction sensible à la chaleur : un symptôme transitoire lors d’un effort ou d’un bain chaud ne prouve pas à lui seul une nouvelle poussée. Une perte axonale laisse une atrophie mesurable.')+
        table(['Perturbation','Exploration','Stratégie'],[
            ['Conduction afférente altérée.','Pupilles, couleurs, champ et potentiels évoqués selon indication.','Traiter la cause inflammatoire selon le phénotype.'],
            ['Inflammation du nerf.','IRM orbitaire dédiée avec séquences adaptées.','Glucocorticoïdes selon indication et sécurité.'],
            ['Atteinte immunologique sévère AQP4.','Contexte, IRM et anticorps.','Traitement urgent ; aphérèse précoce si indiquée selon recommandations spécialisées.'],
            ['Perte axonale.','OCT à distance et fonction visuelle.','Prévenir les récidives et réadapter ; ne pas promettre de régénération.']]))
    l.add('La démarche écarte les {neuropathies urgentes et les imitateurs}. Une baisse instantanée, indolore ou un tableau atypique modifie les hypothèses. Le caractère inflammatoire ne doit pas être supposé sur la seule douleur.',
        table(['Alternative','Discriminant','Conduite'],[
            ['🚩 E2 — Neuropathie ischémique artéritique.','Plus de 50 ans, symptômes crâniens ou systémiques, baisse brutale.','Recherche et traitement urgent de l’ACG si suspicion forte.'],
            ['🚩 Compression ou atteinte infiltrative.','Progression inhabituelle, signes orbitaires, récupération absente.','Imagerie et avis spécialisés rapides.'],
            ['Maculopathie.','Métamorphopsies, lésion à l’OCT maculaire.','Explorer la rétine ; une dyschromatopsie ne suffit pas à localiser.'],
            ['Infection ou inflammation systémique.','Contexte et signes associés.','Bilan orienté avant immunosuppression aveugle.']]),[2,15,16,18])
    l.add('L’anamnèse précise la vitesse, les mouvements douloureux et les épisodes antérieurs. Les {questions d’étiologie et de gravité} recherchent aussi une atteinte neurologique associée. Une forme bilatérale ou très sévère demande une attention particulière.',
        table(['Question','Pourquoi'],[
            ['Baisse sur des heures/jours ou instantanée ?','Différencier inflammation et ischémie, sans règle absolue.'],
            ['Douleur aux mouvements, couleurs moins vives ?','Arguments pour une atteinte du nerf.'],
            ['Autre œil, récidives, récupération antérieure ?','Orienter AQP4/MOG ou autre maladie récidivante.'],
            ['Troubles sensitifs, faiblesse, sphincters, vomissements inexpliqués ?','Rechercher une atteinte centrale associée.'],
            ['Infection, exposition, maladie systémique, médicament ou toxique ?','Diriger le bilan différentiel.']]))
    l.add('L’examen compare acuité, couleurs, pupilles et champ. La {recherche du déficit afférent} est utile lorsque l’atteinte est asymétrique. Un fond d’œil normal n’exclut pas une névrite.',
        table(['Geste','Normal','Anomalie et limite'],[
            ['Acuité corrigée et comparaison des couleurs.','Perception comparable entre les yeux.','Baisse et désaturation orientent mais ne sont pas spécifiques.'],
            ['Éclairage alterné des yeux.','Constriction comparable.','Dilatation relative quand l’œil le plus atteint est éclairé : défaut afférent ; peut manquer si atteinte bilatérale symétrique.'],
            ['Champ visuel.','Pas de déficit nouveau.','Scotome central, cæcocentral ou autre déficit à documenter.'],
            ['Fond d’œil.','Papille et macula sans lésion.','Papille normale possible ; œdème ou hémorragies modifient la discussion.'],
            ['Examen neurologique ciblé.','Pas de signe associé.','Déficit moteur, sensitif ou oculomoteur : compléter l’évaluation centrale.']]))
    l.add('Les {syndromes neuro-ophtalmologiques} orientent les investigations sans imposer seuls un diagnostic étiologique. Les critères se recouvrent partiellement. Le contexte, l’IRM et la biologie doivent être concordants.',
        table(['Syndrome','Fonctionnel','Physique/imagerie'],[
            ['7.1 — Présentation typique.','Baisse subaiguë unilatérale avec douleur aux mouvements.','Défaut afférent, couleurs altérées, papille souvent normale.'],
            ['7.2 — Forme sévère ou bilatérale.','Baisse profonde, récidives possibles.','Atteinte étendue ; rechercher AQP4/MOG selon phénotype.'],
            ['7.3 — Atteinte avec œdème papillaire marqué.','Baisse et douleur variables.','Inflammation antérieure, parfois MOG ; exclure les autres causes.'],
            ['7.4 — Séquelles de conduction.','Gêne de contraste, couleurs ou chaleur.','Atrophie et amincissement à distance possibles.']]))
    l.add('Le diagnostic associe une neuropathie optique inflammatoire probable et l’exclusion de ses imitateurs. Les {critères étiologiques} nécessitent une évaluation spécialisée. Un anticorps isolé ou une image non spécifique ne suffit pas.',
        paras('Le COUF 2025 décrit le diagnostic clinique puis l’IRM cérébrale et orbitaire pour documenter l’atteinte et rechercher une maladie associée. Les critères de SEP doivent être appliqués dans leur version reconnue et le contexte approprié ; une névrite seule ne les satisfait pas automatiquement.',
              'La revue MOG de 2024 souligne l’importance d’un phénotype compatible et d’une recherche sérique par méthode cellulaire adaptée. Les résultats AQP4/MOG se discutent avec le laboratoire et le spécialiste, particulièrement si faible positivité ou tableau atypique.'))
    l.add('Les {explorations orientées} documentent le nerf, recherchent les causes et préparent le traitement. L’IRM doit comporter des séquences adaptées aux orbites. Un examen standard sans question précise peut être insuffisant.',
        paras('9.a — Il n’existe pas de gold standard unique pour toutes les névrites : clinique, IRM et tests ciblés se complètent.',
              '9.b — IRM cérébrale et orbitaire, avec contraste si approprié ; acuité, pupilles, couleurs, périmétrie et OCT de référence.',
              '9.c — Adapter l’imagerie à grossesse, fonction rénale et dispositifs implantés avec le radiologue. L’absence de contraste ou une limite technique doit être explicitée.',
              '9.d — Anticorps AQP4/MOG, ponction lombaire et bilan infectieux ou systémique selon présentation ; potentiels évoqués si question résiduelle.')+
        table(['Résultat','Interprétation','Conduite'],[
            ['Nerf inflammatoire et contexte concordant.','Névrite soutenue.','Définir cause et traitement.'],
            ['Phénotype sévère avec AQP4/MOG.','Cadre différent de SEP possible.','Traitement et prévention des rechutes spécifiques.'],
            ['Discordance ou absence d’amélioration.','Diagnostic incomplet ou autre cause.','Réévaluer rapidement, notamment compression ou infection.']]))
    l.add('L’{algorithme de névrite} commence par les alternatives qui menacent la vision. Une forme sévère demande une prise en charge rapide. La prévention des récidives dépend du diagnostic étiologique.',
        steps('Si baisse brutale ou suspicion d’ACG → évaluer la filière ischémique urgente.',
              'Si neuropathie inflammatoire probable → avis neuro-ophtalmologique et IRM adaptée.',
              'Si forme bilatérale, sévère, récidivante ou atypique → élargir rapidement aux causes AQP4/MOG, systémiques et infectieuses.',
              'Si traitement indiqué → protocole spécialisé et surveillance ; dans une attaque AQP4 sévère ou insuffisamment répondeuse, discuter précocement une aphérèse.',
              'Si évolution discordante → reconsidérer le diagnostic plutôt que répéter aveuglément le même traitement.'))
    med=methylprednisolone(l,sep=True)
    l.add('La prise en charge vise à limiter l’atteinte et à traiter la maladie responsable. Les {traitements et leur suivi} varient selon le phénotype. Le pronostic favorable d’une névrite typique ne justifie pas d’attendre devant une forme sévère.',
        paras('11.A — Préserver la fonction et accélérer la récupération quand le traitement est indiqué, puis prévenir les récidives selon l’étiologie.',
              '11.B — Les glucocorticoïdes à forte dose sont discutés rapidement. Le cadre suisse est détaillé ici : '+med+'. Une faible dose orale empirique ne remplace pas un protocole adapté de poussée.',
              'Dans les attaques du spectre AQP4, les recommandations NEMOS 2023 préconisent un traitement précoce et une aphérèse précoce en cas de récupération insuffisante après fortes doses. Les formes sévères peuvent justifier une association dès le début. Cela ne constitue pas une indication universelle d’aphérèse pour toute névrite.',
              '11.C — Suivre acuité, couleurs, champ et signes neurologiques, ainsi que pression, glycémie et tolérance des corticoïdes. Une aggravation ou l’atteinte de l’autre œil exige une réévaluation immédiate.',
              '11.D — La sortie dépend de l’étiologie, de la stabilité et de l’organisation du traitement et du suivi. Le retour de l’acuité n’exclut pas des séquelles de contraste ou de couleurs. Informer sur conduite, activités et nouvelles manifestations neurologiques.'))
    l.add('La prévention est surtout secondaire et tertiaire. Les {mesures selon la cause} visent à reconnaître une rechute et à choisir le traitement de fond approprié. Un traitement de SEP ne se transpose pas automatiquement à AQP4 ou MOG.',
        paras('Primaire : aucune mesure générale n’est présentée comme capable de prévenir toutes les névrites. Prévenir les risques infectieux et médicamenteux dépend de la cause et des traitements.',
              'Secondaire : identifier rapidement le phénotype et une maladie associée ; donner les signes d’alerte et le point de contact.',
              'Tertiaire : prévention des rechutes par une stratégie spécialisée, surveillance des toxicités et réadaptation des séquelles. La chaleur peut majorer transitoirement un déficit ancien sans prouver une nouvelle inflammation.'))
    l.add('Un fond d’œil normal n’exclut pas une névrite. Une névrite ne prouve pas une SEP. Une forme sévère, bilatérale ou récidivante impose un bilan élargi. Adapter traitement et pronostic à l’étiologie.')
    l.quiz([
        ('La douleur aux mouvements suffit-elle au diagnostic ?','Non : elle oriente mais doit être confrontée à la fonction et au bilan.'),
        ('Un fond d’œil normal exclut-il l’atteinte ?','Non : une névrite rétrobulbaire peut laisser la papille normale.'),
        ('Le défaut afférent manque-t-il toujours dans la névrite ?','Non ; il est fréquent en atteinte asymétrique, mais peut manquer si l’atteinte est symétrique.'),
        ('La névrite signifie-t-elle automatiquement SEP ?','Non : de nombreuses causes existent.'),
        ('Pourquoi rechercher des séquences IRM orbitaires ?','Pour examiner le nerf avec une technique adaptée.'),
        ('AQP4 et MOG sont-ils le même marqueur ?','Non : ils renvoient à des cadres distincts.'),
        ('Une faible positivité isolée suffit-elle sans clinique compatible ?','Non : discuter méthode, contexte et valeur du résultat.'),
        ('Une baisse bilatérale sévère peut-elle être banalisée comme forme typique ?','Non : elle exige une évaluation élargie et rapide.'),
        ('Les faibles doses orales remplacent-elles un protocole de poussée ?','Non : le traitement doit correspondre à l’étiologie et à la gravité.'),
        ('Le schéma AIPS de poussée de SEP s’applique-t-il automatiquement à toute névrite ?','Non : l’indication et le cadre maladie-spécifique doivent être vérifiés.'),
        ('Quand discuter une aphérèse dans une attaque AQP4 ?','Précocement si sévère ou insuffisamment répondeuse, selon les recommandations spécialisées.'),
        ('Les corticoïdes garantissent-ils le résultat visuel définitif d’une forme typique ?','Non : ils peuvent accélérer la récupération sans garantir un meilleur résultat final.'),
        ('Une gêne à la chaleur prouve-t-elle une nouvelle poussée ?','Non : elle peut refléter une conduction démyélinisée thermosensible.'),
        ('L’absence d’amélioration doit-elle faire répéter aveuglément les corticoïdes ?','Non : revoir diagnostic, complications et stratégie.')])
    l.write()

if __name__=='__main__': rediger()

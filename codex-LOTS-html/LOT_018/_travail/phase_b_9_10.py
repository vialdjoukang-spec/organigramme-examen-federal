from format_phase_b import Lesson, paras, table, steps
from medicaments_phase_b import prednisone, methylprednisolone

def rediger():
    l=Lesson(9,[15,2,6])
    l.add('Une occlusion artérielle rétinienne interrompt l’apport sanguin d’un territoire rétinien. Les {formes centrales, de branche et transitoires} menacent la vision et peuvent révéler une maladie systémique. Une présentation aiguë impose une évaluation neurovasculaire et ophtalmologique urgente.',
        paras('L’occlusion centrale atteint la circulation de l’artère centrale ; une branche intéresse un secteur. L’épargne d’un territoire alimenté par une artère ciliorétinienne peut préserver une partie de la vision centrale.',
              'Une cécité monoculaire transitoire peut refléter une ischémie sans laisser de signe entre les épisodes. Une occlusion de l’artère ophtalmique peut affecter aussi la circulation choroïdienne. Ces nuances anatomiques ne suppriment pas la recherche urgente de la cause.'))
    l.add('Le terrain est souvent vasculaire, mais une embolie, une dissection ou une artérite sont possibles. Les {enjeux de fréquence et de pronostic} dépassent le seul œil. Aucun taux suisse actuel directement exploitable n’a été trouvé dans les sources retenues.',
        paras('L’âge et les facteurs de risque cardiovasculaire orientent la probabilité, sans exclure l’affection chez un sujet jeune. Une douleur cervicale ou un traumatisme cervical doit faire envisager une dissection dans le contexte approprié.',
              'La perte visuelle peut être profonde et définitive. L’événement peut annoncer une autre embolie cérébrale ; le bilan ne doit donc pas être abandonné si la vision ne récupère pas ou si les symptômes ont disparu. Une occlusion de branche peut préserver l’acuité tout en amputant le champ.'))
    l.add('La rétine interne dépend d’une circulation artérielle terminale. Les {mécanismes d’ischémie} expliquent la rapidité de la perte fonctionnelle. Une atteinte artéritique demande un traitement de la vascularite en parallèle de la protection vasculaire.',
        paras('L’interruption du flux provoque un déficit énergétique et un œdème intracellulaire de la rétine interne. La pâleur rétinienne contraste parfois avec la fovéa, donnant une tache rouge cerise. Ce signe peut manquer au début ou selon le territoire atteint.')+
        table(['Mécanisme','Exploration','Action'],[
            ['Embole carotidien ou cardiaque.','Bilan vasculaire cervical et cardiaque orienté.','Prise en charge de la source et prévention secondaire.'],
            ['Ischémie rétinienne.','Fond d’œil et OCT.','Évaluation immédiate des options de phase aiguë par l’équipe.'],
            ['Artérite à cellules géantes.','Clinique, inflammation, imagerie/biopsie adaptée.','Glucocorticoïdes sans retard si suspicion forte.'],
            ['Dissection chez un sujet compatible.','Imagerie artérielle appropriée.','Filière neurovasculaire urgente.']]))
    l.add('La démarche commence par l’urgence vasculaire et la recherche d’ACG. Les {diagnostics à distinguer immédiatement} se confrontent au champ, aux pupilles et au fond d’œil. Un examen précoce peu contributif ne suffit pas à rassurer.',
        table(['Alternative','Discriminant','Conduite'],[
            ['🚩 E2 — Neuropathie ischémique artéritique.','Papille œdémateuse, contexte crânien/systémique compatible.','Traitement urgent si forte suspicion et confirmation parallèle.'],
            ['🚩 AVC rétrochiasmatique.','Déficit homonyme dans les deux yeux, signes neurologiques possibles.','Filière AVC immédiate.'],
            ['🚩 E4 — Décollement.','Rideau, éclairs et rétine soulevée.','Avis rétinien urgent.'],
            ['Occlusion veineuse.','Hémorragies étendues et veines dilatées.','Stratégie rétinienne distincte, sans confusion des traitements.']]))
    l.add('Le dernier moment de vision normale doit être documenté. Les {questions prioritaires} recherchent embolie, dissection et artérite. La disparition des symptômes ne met pas fin à la démarche.',
        table(['Question','Pourquoi elle change la conduite'],[
            ['Heure exacte de début ou dernier état normal ?','Les options aiguës dépendent du délai et du protocole.'],
            ['Un seul œil vérifié séparément ?','Distinguer rétine et déficit homonyme cérébral.'],
            ['Nouvelle céphalée, douleur du cuir chevelu, mâchoire douloureuse à la mastication ?','Rechercher l’ACG, surtout après 50 ans.'],
            ['Palpitations, maladie carotidienne, événements antérieurs ?','Orienter la source emboligène.'],
            ['Douleur ou traumatisme cervical, signes neurologiques ?','Envisager dissection ou atteinte cérébrale associée.']]))
    l.add('L’examen mesure chaque œil et recherche un défaut afférent, sans retarder l’appel urgent. Les {signes rétiniens et neurologiques} orientent le siège. La tache rouge cerise n’est pas une condition obligatoire de l’orientation.',
        table(['Geste','Normal','Anomalie et limite'],[
            ['Acuité et champ séparés.','Fonction sans déficit nouveau.','Baisse centrale ou amputation sectorielle ; un secteur maculaire épargné peut préserver l’acuité.'],
            ['Éclairage pupillaire alterné.','Réponse afférente comparable.','Défaut afférent possible en atteinte rétinienne étendue.'],
            ['Fond d’œil.','Rétine sans pâleur ischémique ni embole visible.','Blanchiment diffus ou sectoriel, embole parfois visible ; aspect initial parfois discret.'],
            ['Examen neurologique et artères temporales selon contexte.','Pas de signe focal ou inflammatoire évident.','Tout signe associé réoriente le bilan ; une artère temporale normale n’exclut pas l’ACG.']]))
    l.add('Les {syndromes artériels} relient territoire et fonction. L’ischémie transitoire garde une valeur d’alarme. Une forme artéritique peut aussi toucher le nerf optique.',
        table(['Syndrome','Fonctionnel','Physique'],[
            ['7.1 — Occlusion centrale.','Perte monoculaire brutale souvent profonde et indolore.','Ischémie diffuse, défaut afférent, tache rouge cerise possible.'],
            ['7.2 — Occlusion de branche.','Déficit sectoriel, acuité variable.','Blanchiment dans le territoire de la branche.'],
            ['7.3 — Ischémie transitoire.','Rideau ou perte récupérée.','Examen parfois normal entre les épisodes.'],
            ['7.4 — Atteinte artéritique.','Perte visuelle avec signes crâniens possibles.','Ischémie rétinienne ou papillaire ; confirmation vasculaire/inflammatoire.']]))
    l.add('Le diagnostic associe le tableau aigu et les signes d’ischémie rétinienne. Les {critères cliniques et d’imagerie} peuvent se compléter si l’aspect initial est discret. Le bilan étiologique doit avancer en même temps.',
        paras('Le COUF 2025 retient le fond d’œil comme examen clinique central. L’OCT peut montrer un épaississement et une hyperréflectivité des couches internes au stade aigu, puis une atrophie à distance.',
              'L’absence d’embole visible n’exclut pas une origine embolique. Une angiographie peut préciser la perfusion mais n’est pas indispensable dans un tableau évident et ne doit pas retarder la filière urgente. Une ischémie transitoire s’évalue même sans lésion persistante.'))
    l.add('Les {explorations oculaires et vasculaires} recherchent le territoire et la cause. Le bilan cardiaque et carotidien protège aussi le cerveau. Les tests inflammatoires sont urgents si l’ACG est plausible.',
        paras('9.a — Diagnostic clinique et imagerie rétinienne concordante ; pas de test unique qui identifie toutes les étiologies.',
              '9.b — Fond d’œil/OCT, examen neurologique, électrocardiogramme et imagerie vasculaire selon la filière ; bilan inflammatoire et numération si suspicion d’ACG.',
              '9.c — Choisir les modalités vasculaires selon grossesse, fonction rénale, allergies et disponibilité, avec l’équipe neurovasculaire. Une contre-indication à une technique ne supprime pas le besoin de bilan.',
              '9.d — Échocardiographie, recherche rythmique prolongée ou explorations supplémentaires selon les résultats ; bilan ciblé des formes jeunes ou atypiques.')+
        table(['Résultat','Signification','Conduite'],[
            ['Source emboligène identifiée.','Risque de récidive systémique.','Prévention secondaire adaptée à la cause.'],
            ['Forte suspicion d’ACG.','Risque pour l’autre œil et autres territoires.','Traiter sans attendre la confirmation.'],
            ['Bilan initial négatif.','Cause non établie, pas absence de risque.','Compléter et assurer le suivi.']]))
    l.add('L’{arbre d’urgence vasculaire} doit être parcouru sans délai. L’évaluation de la cause accompagne celle de la rétine. La récupération ou l’absence de traitement visuel certain ne supprime pas l’urgence.',
        steps('Si perte monoculaire soudaine, même récupérée → noter le début et activer la filière neurovasculaire/ophtalmologique.',
              'Si symptômes ou contexte compatibles avec ACG → bilan rapide et glucocorticoïdes immédiats si suspicion forte.',
              'Si signes neurologiques ou déficit homonyme → prise en charge AVC sans retard.',
              'Confirmer le siège rétinien et rechercher source carotidienne, cardiaque ou dissection selon contexte.',
              'Choisir les options aiguës et la prévention secondaire avec l’équipe, puis organiser suivi visuel et vasculaire.'))
    l.add('La priorité est une prise en charge urgente conjointe. Les {actions thérapeutiques et le suivi} dépendent du mécanisme et du délai. Aucune manœuvre locale n’est présentée ici comme un traitement universellement efficace.',
        paras('11.A — Préserver la fonction encore récupérable, prévenir un événement cérébral et protéger l’autre œil si une vascularite est suspectée.',
              '11.B — Appeler immédiatement la filière compétente, noter la chronologie et les traitements. Les options de reperfusion sont décidées selon les preuves, le délai et le protocole du centre ; une thrombolyse n’est pas prescrite systématiquement dans cette leçon. Aucun massage oculaire ou traitement hypotonisant empirique ne doit retarder cette évaluation.',
              'Si ACG probable, débuter les glucocorticoïdes selon la stratégie spécialisée décrite dans <a href="LOT_018_Phase_B_V0_DX.10.html#dx10-p11">DX.10</a>. La prévention antithrombotique et le traitement de la source emboligène relèvent du bilan : ne pas confondre indication vasculaire identifiée et prescription automatique.',
              '11.C — Surveiller évolution visuelle et neurologique, complications et facteurs vasculaires. Revoir la rétine selon le spécialiste ; la perte visuelle initiale ne permet pas d’abandonner les soins.',
              '11.D — Le retour ne se décide qu’après organisation de l’évaluation urgente et du plan de prévention. Donner symptômes de récidive, contacts, rendez-vous et aides visuelles nécessaires. Le pronostic central est souvent réservé, mais le bénéfice systémique du bilan demeure.'))
    l.add('La prévention vise les facteurs cardiovasculaires et les récidives. Les {mesures de suivi} doivent correspondre à l’étiologie trouvée. Une cécité monoculaire transitoire est un signal d’alarme à connaître.',
        paras('Primaire : traiter les facteurs vasculaires selon leurs indications et encourager l’arrêt du tabac.',
              'Secondaire : prise en charge rapide d’une ischémie transitoire et traitement de la source emboligène ou inflammatoire ; ne pas attendre un déficit permanent.',
              'Tertiaire : réadaptation visuelle, adaptation de la conduite et suivi cardiovasculaire. Informer l’entourage des signes imposant un nouvel appel urgent.'))
    l.add('Une perte monoculaire brutale est une urgence vasculaire. Noter le dernier moment normal. Rechercher l’ACG et une source emboligène en parallèle. La récupération visuelle ne dispense pas du bilan.')
    l.quiz([
        ('Une récupération complète exclut-elle une ischémie ?','Non : une ischémie transitoire peut laisser un examen normal.'),
        ('Quel horaire faut-il documenter ?','Le début précis ou le dernier moment connu de vision normale.'),
        ('La tache rouge cerise est-elle toujours visible ?','Non : son absence ne suffit pas à rassurer.'),
        ('Une occlusion de branche peut-elle préserver l’acuité centrale ?','Oui si la macula est épargnée.'),
        ('Un embole doit-il être visible pour retenir une origine embolique ?','Non.'),
        ('Pourquoi rechercher une cause carotidienne ou cardiaque ?','Pour traiter la source et prévenir d’autres événements, notamment cérébraux.'),
        ('Un sujet jeune peut-il avoir une cause artérielle ?','Oui ; rechercher notamment une dissection selon le contexte.'),
        ('Quels signes font penser à l’ACG ?','Notamment nouvelle céphalée, sensibilité du cuir chevelu et claudication mandibulaire dans un contexte compatible.'),
        ('Faut-il attendre l’angiographie rétinienne avant l’appel urgent ?','Non : elle ne doit pas retarder la filière.'),
        ('La thrombolyse est-elle systématique ?','Non : la décision relève d’une équipe spécialisée et du protocole applicable.'),
        ('Le massage oculaire doit-il retarder le bilan vasculaire ?','Non.'),
        ('Un déficit homonyme signifie-t-il forcément un œil malade ?','Non : il oriente vers les voies rétrochiasmatiques.'),
        ('Une mauvaise récupération rend-elle le bilan inutile ?','Non : la prévention des récidives systémiques reste essentielle.'),
        ('L’occlusion veineuse se traite-t-elle avec le même raisonnement antithrombotique ?','Non : les mécanismes et les indications diffèrent.')])
    l.write()

    l=Lesson(10,[6,15,23,26,8])
    l.add('L’ACG est une vascularite des grosses et moyennes artères pouvant provoquer une ischémie visuelle. Les {manifestations oculaires} comprennent neuropathie ischémique et occlusion rétinienne. Une forte suspicion avec signe visuel impose un traitement immédiat.',
        paras('Les recommandations EULAR 2025, publiées en 2026, fondent le diagnostic sur la clinique et sa confirmation par imagerie ou biopsie. Elles rappellent que les critères de classification ne doivent pas être utilisés comme un test diagnostique individuel.',
              'Le terme artérite temporale décrit une localisation possible, mais l’atteinte peut inclure d’autres artères et l’aorte. Une perte visuelle, une diplopie ou un épisode transitoire peuvent précéder une atteinte définitive.'))
    l.add('La maladie concerne surtout les personnes de plus de 50 ans. Les {repères européens et le risque visuel} dépendent de l’âge et de la population. L’absence de signes généraux marqués ne suffit pas à exclure une atteinte oculaire.',
        paras('Les recommandations EULAR récentes rapportent des incidences plus élevées en Scandinavie, de 14,6 à 43,6 pour 100 000 dans les populations citées. Ce repère n’est pas une incidence suisse et ne se transpose pas à une population non sélectionnée par l’âge.',
              'La menace majeure est une lésion ischémique irréversible et une atteinte de l’autre œil. Les rechutes et les toxicités du traitement imposent un suivi prolongé. Une maladie des gros vaisseaux peut persister ou se manifester à distance des symptômes crâniens.'))
    l.add('L’inflammation de la paroi artérielle peut réduire la lumière et interrompre la perfusion. Les {mécanismes d’ischémie et de traitement} relient l’artère au nerf et à la rétine. Le traitement protège surtout le tissu encore viable.',
        paras('L’infiltration inflammatoire et le remodelage de la paroi favorisent sténose et occlusion. L’atteinte des artères ciliaires postérieures peut provoquer une neuropathie optique ischémique antérieure ; d’autres territoires oculaires ou cérébraux peuvent être concernés.',
              'Les glucocorticoïdes freinent l’inflammation, mais ne restaurent pas un tissu déjà infarci. Une amélioration des céphalées ne prouve donc pas une récupération visuelle et ne suffit pas à confirmer le diagnostic.')+
        table(['Lésion','Exploration','Action'],[
            ['Paroi inflammatoire.','Échographie temporale et axillaire experte.','Glucocorticoïdes et confirmation rapide.'],
            ['Ischémie du nerf ou de la rétine.','Acuité, pupilles, fond d’œil, OCT selon besoin.','Traitement urgent pour prévenir l’extension.'],
            ['Atteinte extracrânienne.','Imagerie vasculaire orientée.','Suivi et prise en charge multidisciplinaire.'],
            ['Toxicité du traitement.','Clinique, pression, glycémie, risque osseux et infectieux.','Prévention et adaptation de la stratégie, sans arrêt brutal.']]))
    l.add('La démarche recherche l’ACG avant de banaliser une neuropathie ischémique. Les {diagnostics concurrents} sont examinés en parallèle. Le besoin de confirmation ne doit pas retarder le traitement d’une forte suspicion.',
        table(['Alternative','Discriminant','Action'],[
            ['🚩 Occlusion embolique rétinienne.','Début brutal et contexte vasculaire ; fond d’œil.','Bilan neurovasculaire urgent également.'],
            ['Neuropathie ischémique non artéritique.','Contexte et papille compatibles, sans preuve d’artérite.','Exclure l’ACG de façon adaptée ; ne pas conclure sur l’absence de céphalée seule.'],
            ['Névrite optique.','Douleur aux mouvements, phénotype et IRM.','Évaluer cause inflammatoire distincte.'],
            ['Compression ou autre maladie systémique.','Évolution atypique ou discordances.','Élargir le bilan et revoir la probabilité.']]))
    l.add('Les {questions crâniennes, visuelles et systémiques} recherchent les arguments d’ACG. La claudication mandibulaire désigne une douleur à l’effort de mastication. Une atteinte visuelle récente impose l’urgence même si d’autres symptômes manquent.',
        table(['Question','Raison et conduite'],[
            ['Nouvelle céphalée ou douleur du cuir chevelu ?','Atteinte crânienne possible ; préciser caractère nouveau.'],
            ['Douleur de mâchoire ou de langue pendant la mastication ?','Ischémie à l’effort ; argument important dans le contexte.'],
            ['Perte transitoire, diplopie ou baisse de l’autre œil ?','Menace visuelle ; prise en charge immédiate.'],
            ['Raideur des ceintures, fièvre, amaigrissement ?','Manifestations associées possibles.'],
            ['Claudication d’un membre, douleur thoracique ou dorsale nouvelle ?','Atteinte des gros vaisseaux ou complication à évaluer selon gravité.']]))
    l.add('L’examen documente la vision et les signes de vascularite. Les {gestes ciblés} recherchent notamment une neuropathie ischémique et une atteinte artérielle. Des artères temporales apparemment normales n’excluent pas la maladie.',
        table(['Geste','Normal','Pathologique et limite'],[
            ['Acuité, champ et pupilles de chaque œil.','Fonction stable et réponses afférentes comparables.','Déficit nouveau ou défaut afférent : documenter sans retarder le traitement.'],
            ['Fond d’œil.','Papille sans œdème ni ischémie rétinienne.','Œdème papillaire pâle ou ischémie ; l’aspect ne remplace pas la recherche étiologique.'],
            ['Inspection et palpation douce des artères temporales.','Artère sans douleur ou épaississement notable.','Douleur, épaississement ou pouls diminué ; leur absence ne suffit pas à exclure.'],
            ['Pouls périphériques, pression et examen général.','Pas d’asymétrie nouvelle ou signe systémique.','Souffle, asymétrie ou autre signe orientent l’imagerie vasculaire.']]))
    l.add('Les {syndromes de l’ACG} peuvent se combiner. La plainte visuelle peut dominer le tableau. Une amélioration sous corticoïdes ne remplace pas la confirmation.',
        table(['Syndrome','Fonctionnel','Physique ou exploration'],[
            ['7.1 — Crânien.','Céphalée nouvelle, claudication mandibulaire.','Artère anormale ou inflammation pariétale à l’échographie.'],
            ['7.2 — Ischémique visuel.','Perte transitoire ou permanente, diplopie.','Neuropathie ischémique ou occlusion rétinienne.'],
            ['7.3 — Systémique/polymyalgique.','Fièvre, altération générale, raideur des ceintures.','Inflammation et examen compatible, sans spécificité absolue.'],
            ['7.4 — Gros vaisseaux.','Claudication ou symptômes selon territoire.','Anomalie pariétale ou structurelle à l’imagerie.']]))
    l.add('Le diagnostic se fonde sur la probabilité clinique et une confirmation adaptée. Les {critères de confirmation} privilégient l’imagerie experte disponible rapidement. Une CRP normale ou un examen négatif isolé ne suffit pas toujours à exclure l’ACG.',
        paras('EULAR imagerie 2023 recommande en première intention l’échographie des artères temporales et axillaires si elle est disponible rapidement et réalisée avec expertise. En forte probabilité clinique avec imagerie positive, une confirmation supplémentaire peut être inutile ; en situation discordante, poursuivre le bilan.',
              'La biopsie temporale reste une option, notamment si l’imagerie est indisponible, non concluante ou sans expertise suffisante. Une maladie segmentaire peut être manquée. Les critères de classification sont destinés à homogénéiser des groupes, pas à décider seuls du traitement individuel.'))
    l.add('Les {examens urgents et de confirmation} sont organisés en parallèle du traitement. L’échographie doit être rapide parce que les signes inflammatoires peuvent s’atténuer. La sécurité visuelle prime sur l’attente d’un créneau d’imagerie.',
        paras('9.a — Aucune technique n’exclut seule toutes les formes ; clinique, imagerie et parfois histologie se complètent.',
              '9.b — Prélever si cela ne retarde rien : CRP, vitesse de sédimentation, numération et bilans utiles au traitement ; organiser échographie temporale et axillaire experte.',
              '9.c — EULAR propose IRM haute résolution ou tomographie par émission de positons selon territoire et disponibilité. Évaluer leurs contraintes et contre-indications avec l’équipe.',
              '9.d — Biopsie et imagerie des gros vaisseaux selon probabilité résiduelle, discordance ou suspicion extracrânienne. EULAR conseille l’imagerie avant ou idéalement dans les 72 heures après début des corticoïdes, sans retarder ceux-ci.')+
        table(['Résultat','Signification','Conduite'],[
            ['Forte probabilité et imagerie positive.','Diagnostic soutenu.','Poursuivre stratégie et suivi spécialisés.'],
            ['Probabilité forte mais test négatif.','Faux négatif ou technique insuffisante possible.','Compléter ; ne pas arrêter automatiquement le traitement.'],
            ['Faible probabilité et examen négatif de qualité.','ACG moins probable.','Rechercher une autre cause selon la clinique.'],
            ['Inflammation biologique normale.','Exclusion non certaine.','Interpréter avec traitement préalable et phénotype.']]))
    l.add('L’{arbre d’urgence de l’ACG} commence par la menace visuelle. Le traitement ne dépend pas du retour de la biopsie. Les résultats servent ensuite à confirmer et à ajuster la stratégie.',
        steps('Si forte suspicion d’ACG avec symptôme visuel → contact spécialisé immédiat et glucocorticoïdes sans délai.',
              'Documenter les deux yeux et prélever les bilans utiles seulement sans retarder la prise en charge.',
              'Organiser échographie temporale/axillaire rapide ou autre confirmation disponible.',
              'Si discordance → compléter par biopsie ou imagerie adaptée ; réévaluer aussi les diagnostics concurrents.',
              'Après confirmation → plan de décroissance, surveillance, prévention des toxicités et prise en charge des rechutes.'))
    pred=prednisone(l);meth=methylprednisolone(l,sep=False)
    l.add('Une forte suspicion avec atteinte visuelle impose des glucocorticoïdes immédiats et un avis spécialisé. Les {modalités d’induction, de relais et de surveillance} distinguent recommandations et information professionnelle. La confirmation diagnostique se poursuit pendant le traitement.',
        paras('11.A — Prévenir de nouvelles lésions ischémiques, surtout de l’autre œil, et obtenir une rémission avec la moindre toxicité possible. La récupération de la vision déjà perdue n’est pas garantie.',
              '11.B — EULAR 2025 propose une induction orale à 40–60 mg/jour en équivalent prednisone, avec décroissance individualisée après réponse. Le lien avec l’autorisation et la plage suisse est explicité dans '+pred+'. Ne pas interpréter la dose minimale d’une plage générale comme suffisante pour une menace visuelle.',
              'Dans certaines pertes visuelles aiguës attribuables à une ACG active, EULAR discute des bolus intraveineux de méthylprednisolone de 0,25–1 g/jour jusqu’à trois jours, avec bénéfice incertain. Ce schéma est une recommandation de maladie, hors posologie spécifique de l’ACG décrite dans l’extrait AIPS : '+meth+'. Le choix se fait immédiatement avec le spécialiste.',
              'Un traitement d’épargne cortisonique est discuté selon rechutes, réfractarité et risque de toxicité. Les recommandations récentes incluent des stratégies ciblées ; indication suisse, contre-indications, infections, risque cardiovasculaire et remboursement doivent être vérifiés pour la spécialité avant prescription. Aucun schéma de traitement de fond n’est extrapolé ici.',
              '11.C — Réévaluer symptômes visuels et crâniens, examen, marqueurs inflammatoires et complications. Contrôler pression et glycémie, organiser prévention osseuse et infectieuse. Une nouvelle perte visuelle impose une urgence, même si les marqueurs sont bas ou sous un traitement qui les modifie.',
              '11.D — Le retour nécessite stabilité évaluée, traitement disponible, plan écrit, accès à une réévaluation urgente et rendez-vous organisés. La décroissance et les rechutes se gèrent avec le spécialiste ; ne pas arrêter brutalement un traitement prolongé. Prévoir suivi vasculaire et réadaptation si déficit résiduel.'))
    l.add('La prévention vise les séquelles ischémiques et la toxicité thérapeutique. Les {mesures aux trois niveaux} s’intègrent au suivi. Un résultat biologique rassurant ne remplace pas l’écoute d’un nouveau symptôme visuel.',
        paras('Primaire : aucune prévention spécifique de l’ACG n’est établie dans les sources retenues ; prendre en charge les risques cardiovasculaires habituels.',
              'Secondaire : reconnaître les signes crâniens et visuels, faciliter l’accès rapide au diagnostic et au traitement.',
              'Tertiaire : plan de décroissance compris, surveillance osseuse, infectieuse, métabolique et cardiovasculaire ; éducation sur rechute et insuffisance surrénale. Les antiagrégants ou anticoagulants ne sont pas systématiques pour la seule ACG en l’absence d’autre indication.'))
    l.add('Une forte suspicion avec signe visuel se traite sans attendre la confirmation. Documenter les deux yeux et rechercher la vascularite. Distinguer dose AIPS générale et protocole de recommandation. Prévenir rechutes et toxicités pendant la décroissance.')
    l.quiz([
        ('L’ACG se limite-t-elle à l’artère temporale ?','Non : elle peut atteindre d’autres artères et les gros vaisseaux.'),
        ('L’absence de céphalée exclut-elle une atteinte oculaire ?','Non.'),
        ('Que signifie claudication mandibulaire ?','Une douleur liée à l’effort de mastication dans un contexte compatible d’ischémie.'),
        ('Faut-il attendre la biopsie avant de traiter une forte suspicion visuelle ?','Non : traitement immédiat et confirmation parallèle.'),
        ('Quelle imagerie EULAR privilégie-t-elle d’abord ?','L’échographie temporale et axillaire, disponible rapidement et réalisée avec expertise.'),
        ('Une biopsie négative exclut-elle toute ACG ?','Non : la maladie peut être segmentaire et le contexte reste décisif.'),
        ('Une CRP normale exclut-elle toujours l’ACG ?','Non : interpréter dans le contexte et avec les traitements.'),
        ('Les critères de classification sont-ils un test diagnostique individuel ?','Non.'),
        ('Pourquoi examiner l’autre œil ?','Pour documenter sa fonction et prévenir une nouvelle atteinte.'),
        ('La plage AIPS générale autorise-t-elle à choisir arbitrairement sa dose minimale ?','Non : la menace visuelle exige un protocole maladie-spécifique approprié.'),
        ('Les bolus discutés par EULAR garantissent-ils une récupération visuelle ?','Non : leur bénéfice dans les cas sélectionnés reste incertain.'),
        ('L’amélioration des céphalées suffit-elle à confirmer le diagnostic ?','Non : la réponse aux corticoïdes n’est pas un test spécifique.'),
        ('Une nouvelle perte visuelle pendant la décroissance peut-elle attendre ?','Non : elle impose une réévaluation urgente.'),
        ('Faut-il donner systématiquement un antiagrégant pour la seule ACG ?','Non : rechercher une indication vasculaire propre et évaluer les risques.')])
    l.write()

if __name__=='__main__': rediger()

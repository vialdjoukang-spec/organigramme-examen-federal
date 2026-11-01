# -*- coding: utf-8 -*-
"""Développements propres à chaque situation du LOT_232."""
from rediger import CC, ASSM, FMH, LRH, OFSP, ATF, PAFA, MMSE, P, cliche, s

# Chaque situation : faits assez précis pour que le raisonnement change.
SITUATIONS = [
dict(
    n=1, cle="sans",
    nom="Acte médical sans consentement valable",
    qui="Une femme de 54 ans, enseignante, sans trouble cognitif",
    geste="une cure de hernie inguinale programmée, sous anesthésie générale",
    recit="Elle arrive à 7 h. L'accueil lui tend un formulaire de « consentement opératoire ». Elle croit signer l'autorisation administrative. Personne ne nomme le risque d'atteinte nerveuse, la douleur chronique, ni l'option d'une surveillance. À 10 h elle est au bloc.",
    manque="Il n'y a eu ni information sur les risques graves, ni vérification de ce qu'elle avait compris, ni moment pour refuser.",
    capacite="Elle est capable : elle travaille, elle raconte sa journée, elle pose des questions dès qu'on lui en laisse le temps.",
    liberte="Rien n'indique une contrainte. Le défaut n'est pas la liberté. C'est l'absence d'information et donc l'absence d'un vrai oui.",
    info="Le formulaire cite le nom du geste. Il ne décrit ni bénéfice attendu, ni alternative, ni risque grave.",
    juste="On n'opère pas. On reprend l'entretien le jour même si elle le souhaite et si le délai du guide est tenu, sinon on reporte.",
    dossier="Pas d'entretien médical avant la signature. Patiente capable. Information non donnée. Intervention reportée.",
    piege="Dire que le geste, bien fait, reste licite parce que la hernie était indiquée.",
    dit="Je ne peux pas vous opérer sur cette signature. Voici le but, les risques graves, les autres options, et le droit de refuser.",
    proche="Son conjoint est dans la salle d'attente. Il n'a pas à signer à sa place.",
    urgence="Il n'y a pas d'étranglement ni de douleur incoercible. Rien ne justifie l'article 379.",
    cliche_mot="formulaire signé", cid="LOT_232-DX.1-1",
),
dict(
    n=2, cle="info",
    nom="Défaut d'information avant une intervention",
    qui="Un homme de 61 ans, comptable, opéré d'un goitre",
    geste="une thyroïdectomie totale programmée",
    recit="L'entretien a duré huit minutes, trois semaines avant. On a parlé de la cicatrice et de l'hormone à prendre ensuite. On n'a pas parlé de la voix, de l'hypocalcémie, ni de la possibilité d'une lobo-isthmectomie. Au réveil, une corde vocale est paralysée.",
    manque="Un risque grave, rare mais connu, et une alternative raisonnable n'ont pas été dits.",
    capacite="Il était capable le jour de l'entretien et le jour du geste. Le défaut n'est pas la capacité.",
    liberte="Il dit qu'il aurait demandé un deuxième avis s'il avait su pour la voix, parce qu'il chante dans un chœur.",
    info="L'information a porté sur des suites banales. Elle a tu le risque qui pouvait changer sa décision.",
    juste="Avant le geste, nommer la paralysie récurrentielle, l'hypocalcémie, l'hématome, et l'alternative d'un geste plus limité si elle est défendable.",
    dossier="Risques graves nommés : voix, calcium, hématome. Alternative discutée : geste limité. Délai : trois semaines. Décision du patient après reformulation.",
    piege="Croire qu'un pourcentage très bas dispense de dire un risque qui abîme une fonction précieuse pour cette personne.",
    dit="Le risque de voix bitonale ou de paralysie est rare. Pour vous qui chantez, il compte. Voici l'autre option, et ce qui se passe si l'on n'opère pas.",
    proche="Son épouse était présente et posait les questions. Il n'a pas eu de temps seul.",
    urgence="Le goitre n'est pas compressif. Le délai de réflexion était possible.",
    cliche_mot="voix bitonale", cid="LOT_232-DX.2-1",
),
dict(
    n=3, cle="incap",
    nom="Consentement recueilli d'une personne incapable de discernement",
    qui="Un homme de 82 ans, habituellement autonome, hospitalisé pour une fracture du col",
    geste="une prothèse de hanche proposée le soir de l'admission",
    recit="Il est désorienté par moments, s'endort en parlant, et dit oui à tout sans pouvoir redire le but du geste. Sa fille, pressée, guide sa main pour signer. Le matin il était plus clair, l'après-midi non.",
    manque="On a pris un acquiescement fluctuant pour un consentement, sans évaluer les quatre capacités et sans chercher les directives.",
    capacite="Le doute est fondé : fluctuation, impossibilité de reformuler, heure tardive, douleur. On ne présume plus. On évalue.",
    liberte="La main guidée par un proche est une contrainte, en plus du doute sur la capacité.",
    info="Même une information parfaite ne rend pas capable une personne qui ne peut pas l'utiliser.",
    juste="Ne pas faire signer. Corriger douleur, heure et médicaments s'ils troublent, réévaluer au moment le plus clair. Sinon, directives puis représentant de l'article 378, et plan de l'article 377.",
    dossier="Capacité non retenue à 20 h : ne reformule pas le but, vigilance fluctuante. Signature annulée. Réévaluation prévue à 8 h. Fille entendue comme proche, pas encore comme représentante : on vérifie l'ordre légal.",
    piege="Conclure à l'incapacité parce qu'il hésite, ou à la capacité parce qu'il a dit oui.",
    dit="Je ne vous demande pas de signer ce soir. Je revérifierai demain matin, quand vous serez plus clair.",
    proche="La fille aide régulièrement et fait ménage commun depuis le veuvage. Elle peut représenter s'il n'y a ni directive ni curateur, et seulement selon la volonté présumée.",
    urgence="La fracture fait mal mais la prothèse peut attendre le matin. Ce n'est pas l'article 379.",
    cliche_mot="fluctuation", cid="LOT_232-DX.3-1",
),
dict(
    n=4, cle="refus",
    nom="Passage outre un refus éclairé",
    qui="Une femme de 47 ans, Témoin de Jéhovah, ingénieure",
    geste="une prothèse de hanche élective, avec un plan sans transfusion",
    recit="Elle refuse toute transfusion et tout dérivé, par écrit, après un entretien où elle reformule le risque hémorragique et la possibilité de mourir. L'équipe prévoit quand même de transfuser « si vraiment il le faut ».",
    manque="Le refus est éclairé, stable, capable. Le projet de passer outre est une atteinte illicite.",
    capacite="Elle comprend, elle relie le risque à sa foi et à sa vie, elle défend son choix hors de la présence de l'ancien de la congrégation. Les quatre capacités sont là.",
    liberte="On a vérifié l'absence de pression en lui parlant seule. Le choix reste le même.",
    info="Elle a entendu le bénéfice de la prothèse, le risque de saignement, les techniques d'épargne, et l'option de ne pas opérer.",
    juste="Respecter le refus. Organiser l'épargne sanguine, le fer, le chirurgien habitué, et un plan si l'hémorragie met la vie en danger sans transfusion : on ne transfuse pas.",
    dossier="Refus de transfusion éclairé, capable, répété seule. Alternatives d'épargne acceptées. Transfusion exclue même en cas de danger vital peropératoire.",
    piege="Transfuser au nom du bien de la patiente, ou déclarer le refus incapable parce qu'il paraît déraisonnable.",
    dit="Votre refus tient, y compris si le saignement devient grave. Je ne vous transfuserai pas. Voici comment on réduit ce risque, et vous pouvez encore renoncer à l'opération.",
    proche="Son mari souhaite qu'on transfuse. Il ne décide pas. Elle est capable.",
    urgence="Il n'y a pas d'urgence. Le refus anticipé écrit vaudrait aussi si elle devenait incapable pendant l'opération.",
    cliche_mot="refus de transfusion", cid="LOT_232-DX.4-1",
),
dict(
    n=5, cle="urg",
    nom="Urgence chez une personne incapable de discernement",
    qui="Un motard de 29 ans, inconscient après un choc",
    geste="une laparotomie pour choc hémorragique abdominal",
    recit="Il ne parle pas, la pression tombe, l'échographie montre du liquide. Aucun proche n'est là. Le portefeuille contient une carte : pas de directives déposées. L'équipe hésite à inciser sans signature.",
    manque="L'hésitation retarde les soins indispensables. L'article 379 est le fait justificatif.",
    capacite="L'incapacité est manifeste. On ne cherche pas les quatre capacités au milieu du choc.",
    liberte="Il ne peut pas s'exprimer. On ne fabrique pas un accord.",
    info="On n'informe pas une personne inconsciente. On informe le représentant dès qu'il est joignable, sans retarder le geste qui sauve.",
    juste="Contrôler l'hémorragie. Ne pas ajouter un geste de confort ou une recherche. Chercher ensuite directives et proches. Réévaluer dès qu'il reprend conscience.",
    dossier="Choc hémorragique, patient inconscient, aucun représentant joignable, pas de refus anticipé connu. Laparotomie selon l'article 379. Heure, constat, et limite du geste écrite.",
    piege="Étendre la cicatrice à une cure de hernie « tant qu'on y est », ou attendre une signature qui ne viendra pas.",
    dit="Au réveil : vous ne pouviez pas décider. J'ai arrêté le saignement. Voici ce qui a été fait, et ce qui reste à décider avec vous.",
    proche="Les parents arrivent deux heures après. On les informe. On ne leur demande pas de valider rétroactivement comme si le droit l'exigeait pour le geste déjà indispensable.",
    urgence="Le danger est immédiat. C'est le cœur de l'article 379.",
    cliche_mot="choc hémorragique", cid="LOT_232-DX.5-1",
),
dict(
    n=6, cle="valide",
    nom="Consentement valable d'une personne capable de discernement",
    qui="Une femme de 43 ans, boulangère, sans traitement psychotrope",
    geste="une cholécystectomie sous cœlioscopie pour coliques répétés",
    recit="Deux consultations. Elle reformule : retirer la vésicule, diminuer les coliques, risques de plaie biliaire, d'ouverture, de phlébite, option d'attendre en évitant les graisses. Elle choisit l'opération, puis confirme la veille.",
    manque="Rien d'essentiel ne manque si la trace est complète. Ce dossier est le modèle, pas un manquement.",
    capacite="Elle comprend, applique l'information à son travail de nuit, choisit, et défend son choix.",
    liberte="Délai de dix jours. Personne ne la presse. Elle sait qu'elle peut revenir en arrière.",
    info="Bénéfice, risques fréquents, risque grave rare, alternative d'attente, suites et arrêt de travail ont été dits.",
    juste="Opérer. Garder la trace. Vérifier la veille qu'elle n'a pas changé d'avis et qu'aucun sédatif n'a été donné avant la confirmation.",
    dossier="Entretien du 12, confirmation la veille. Risques nommés dont plaie biliaire. Alternative d'expectative expliquée. Décision d'opérer. Capable. Libre.",
    piege="Ajouter la veille un geste non discuté, ou faire confirmer après la prémédication.",
    dit="Vous pouvez encore dire non demain matin. Si vous dites oui, je noterai que vous avez reformulé le risque de plaie des voies biliaires.",
    proche="Elle vient seule et le souhaite. On ne retient pas un proche pour « être en règle ».",
    urgence="Les coliques sont douloureuses mais pas une angiocholite ce jour-là. Le délai a été respecté.",
    cliche_mot="reformulation", cid="LOT_232-DX.6-1",
),
dict(
    n=7, cle="mineur",
    nom="Consentement personnel du mineur capable de discernement",
    qui="Une adolescente de 16 ans, au lycée, fracture du ménisque instable",
    geste="une arthroscopie du genou",
    recit="Elle comprend le but, le risque de raideur, l'alternative d'un plâtre plus long, et elle veut être opérée pour reprendre le handball. Ses parents refusent « pour ne pas manquer les examens » et exigent que rien ne se fasse sans leur signature.",
    manque="Le manque serait d'obéir aux parents alors qu'elle est capable pour ce soin, ou l'inverse : opérer un enfant de 7 ans sur son seul oui.",
    capacite="Pour cette arthroscopie, elle remplit les quatre capacités. Les directives de 2019 disent que le mineur capable consent lui-même et que la représentation parentale n'est plus admissible pour ce consentement.",
    liberte="On lui parle sans ses parents. Le choix ne change pas. On vérifie qu'elle ne cède pas seulement à l'entraîneur.",
    info="Même contenu que pour un adulte, avec des mots qu'elle reformule.",
    juste="Recueillir son consentement. Informer les parents du cadre, sans leur donner un veto sur le soin. Le contrat d'hospitalisation et les frais peuvent encore relever du représentant : les directives de 2019 laissent cette question ouverte.",
    dossier="Mineure de 16 ans, capable pour l'arthroscopie. Consentement personnel. Parents opposés pour un motif scolaire, informés, sans veto sur le soin. Frais : à clarifier avec le représentant.",
    piege="Exiger la signature parentale comme condition du soin, ou traiter tout mineur comme incapable.",
    dit="C'est à vous de dire oui ou non pour votre genou. Vos parents peuvent être informés. Ils ne signent pas à votre place si vous décidez vous-même.",
    proche="Les deux parents sont titulaires de l'autorité. Leur désaccord entre eux ne retire pas la capacité de l'adolescente.",
    urgence="Le genou est stable sous attelle pour quelques jours. On a le temps de l'entretien seul.",
    cliche_mot="mineur capable", cid="LOT_232-DX.7-1",
),
dict(
    n=8, cle="curat",
    nom="Personne sous curatelle encore capable de discernement",
    qui="Un homme de 58 ans, sous curatelle de portée générale pour une maladie psychique stabilisée",
    geste="une coloscopie après un test de sang occulte positif",
    recit="Le curateur écrit qu'il « décide des soins ». Le patient, ce matin-là, explique le but de la coloscopie, le risque de perforation, l'alternative de ne pas la faire, et il veut la faire. Il est calme, sans délire, et il répète son choix le lendemain.",
    manque="Confondre la curatelle avec l'incapacité. L'article 17 lui retire l'exercice des droits civils. L'article 19c lui laisse les droits strictement personnels s'il est capable.",
    capacite="Pour cette coloscopie, les quatre capacités sont présentes. La curatelle ne les efface pas.",
    liberte="On le voit sans le curateur. Pas de menace. Il sait qu'il peut refuser.",
    info="Perforation, saignement, examen incomplet, et la possibilité de ne rien faire ont été dits.",
    juste="C'est lui qui consent. Le curateur n'a pas à autoriser le soin. Il reste utile pour l'organisation et les frais. S'il devenait incapable, le curateur chargé du domaine médical viendrait au deuxième rang de l'article 378.",
    dossier="Curatelle de portée générale. Capacité retenue pour la coloscopie : reformule but, risque de perforation, alternative. Consentement personnel. Curateur informé de l'organisation, pas substitut.",
    piege="Appeler le curateur pour qu'il signe, ou croire qu'une curatelle de portée générale est une incapacité permanente.",
    dit="La curatelle organise une partie de votre vie. Pour cet examen, c'est vous qui décidez, parce que vous comprenez l'enjeu.",
    proche="Le curateur est de bonne foi. On lui explique l'article 19c sans l'humilier, et on l'associe à ce qui n'est pas le soin lui-même.",
    urgence="Le test positif n'est pas une hémorragie active. On a le temps.",
    cliche_mot="curatelle", cid="LOT_232-DX.8-1",
),
dict(
    n=9, cle="langue",
    nom="Information non comprise pour cause de barrière linguistique",
    qui="Un homme de 67 ans, albanophone, peu lecteur du français",
    geste="une colectomie droite pour un cancer",
    recit="Son fils de 19 ans traduit. Le patient hoche la tête. En le faisant reformuler avec un interprète professionnel, on découvre qu'il croit à une « petite ablation de polype » et qu'il ignore la poche possible et la chimiothérapie.",
    manque="L'information n'est pas adéquate tant qu'elle n'est pas comprise. L'acquiescement poli n'est pas un consentement.",
    capacite="Avec un interprète, il est capable. Sans interprète, on ne peut même pas évaluer les quatre capacités.",
    liberte="Le fils veut « ne pas l'effrayer » et adoucit les risques. Ce filtre retire la liberté de choisir.",
    info="Le contenu médical existait dans la tête du chirurgien. Il n'est pas arrivé au patient.",
    juste="Reporter le geste électif. Reprendre avec un interprète professionnel, dans la langue du patient, avec reformulation. Écrire le nom de l'interprète et la langue.",
    dossier="Entretien initial non valable : traduction par le fils, reformulation impossible. Nouvel entretien avec interprète professionnel, langue albanaise. Risques graves reformulés par le patient.",
    piege="Se contenter des hochements de tête, ou faire signer un formulaire français illisible pour lui.",
    dit="Je vais chercher un interprète. Votre fils peut rester si vous le voulez, mais ce n'est pas lui qui traduit l'opération.",
    proche="Le fils aime son père. Il n'est pas neutre. On le remercie et on le sort du rôle de traducteur.",
    urgence="Le cancer est à opérer sans des mois d'attente, mais pas dans l'heure. L'interprète fait partie du soin.",
    cliche_mot="interprète", cid="LOT_232-DX.9-1",
),
dict(
    n=10, cle="rech",
    nom="Consentement à une recherche sur l'être humain",
    qui="Une femme de 70 ans, déjà consentante pour une prothèse de genou",
    geste="la même prothèse, plus un tirage au sort dans un essai sur un ciment",
    recit="On lui a bien expliqué l'opération. À la fin, une phrase dit qu'elle « participe à l'amélioration des soins » et qu'elle signe le même papier. Elle ne sait pas qu'elle peut refuser l'essai et être quand même opérée.",
    manque="Le consentement de soin ne couvre pas la recherche. La loi de 2011 sépare les deux.",
    capacite="Elle est capable pour l'opération. Pour l'essai, elle ne peut pas encore décider : elle n'a pas reçu l'information de l'article 16.",
    liberte="Mélanger les deux signatures crée une pression : refuser l'essai semblerait refuser le soin.",
    info="Il manque, pour l'essai, la nature, le but, la durée, le déroulement, les risques, le bénéfice attendu, la protection des données et les droits, par oral et par écrit.",
    juste="Séparer les entretiens. Laisser un délai raisonnable. Consentement écrit pour la recherche, révocable sans justification et sans effet sur l'opération. Vérifier l'autorisation de la commission d'éthique.",
    dossier="Consentement opératoire distinct. Essai : information orale et écrite remise, délai jusqu'à demain, signature séparée, droit de retrait expliqué. Numéro d'autorisation de la commission noté.",
    piege="Glisser la recherche dans le formulaire opératoire, ou utiliser une information partielle sans les conditions de l'article 18.",
    dit="L'opération est décidée. L'étude est autre chose. Vous pouvez la refuser et je vous opère de la même façon.",
    proche="Sa fille lit l'étude plus vite qu'elle. La fille ne signe pas la recherche à sa place.",
    urgence="Une prothèse élective n'est pas une urgence qui dispenserait du délai de réflexion de la recherche.",
    cliche_mot="formulaire de recherche", cid="LOT_232-DX.10-1",
),
]


def _p(n, *xs):
    return P(*xs)


def extras(d):
    """HTML long, propre à la situation, rangé par point."""
    q = d
    c = cliche(q["cid"], q["cliche_mot"])
    out = {}
    out[1] = _p(1,
        f"Cette situation s'appelle : {q['nom']}. {q['qui']}. Le geste est {q['geste']}. {q['recit']}{s(9)}",
        f"Ce qui qualifie le dossier, ce n'est pas le nom commercial du geste. C'est le défaut ou la qualité du consentement. Ici : {q['manque']}{s(7,9)}",
        f"On ne confond pas cette situation avec les neuf autres du motif. Le voisin le plus trompeur change selon le fait principal : capacité, information, liberté, urgence, minorité, curatelle, langue ou recherche.{s(8)}",
        f"Le mot que l'étudiant doit pouvoir montrer du doigt est {c}. Il ne remplace pas l'analyse. Il empêche de passer à côté du fait qui reclasse le dossier.",
    )
    out[2] = _p(2,
        f"Pour {q['qui'].split(',')[0].lower()}, aucune source lue en 2026 ne donne une incidence suisse de ce manquement précis. On n'invente pas un pourcentage.{s(8)}",
        f"On peut seulement situer le décor. Les directives anticipées concernent la voie de l'incapacité, pas le patient capable. En 2022, 24 pour cent des adultes interrogés en avaient rédigé, et la synthèse de 2018 sur les soins palliatifs en trouvait 16 pour cent déposées.{s(10,11)}",
        f"La gravité de {q['nom'].lower()} ne dépend pas de la rareté. Un seul dossier comme celui de {q['geste']} suffit à rendre l'acte illicite si la condition manque.{s(9)}",
        f"Le médecin retient donc deux nombres, et seulement eux : 24 pour cent en 2022 pour des directives rédigées, 16 pour cent dans l'enquête dont la synthèse est de 2018 pour des directives déposées. Il ne les plaque pas sur cette situation si elle ne concerne pas les directives.{s(10,11)}",
    )
    out[3] = _p(3,
        f"Physiopathologie normative de ce dossier. L'atteinte, c'est {q['geste']}. Le fait justificatif cherché, c'est un consentement valable ou, à défaut, l'article 379 du {CC} si la personne est incapable et le danger immédiat.{s(6,9)}",
        f"État de l'information : {q['info']} État de la capacité : {q['capacite']} État de la liberté : {q['liberte']}{s(7,8)}",
        f"Le mécanisme du dommage juridique n'est pas la complication technique. C'est la décision prise sans le titre qui l'autorise. {q['piege']}{s(9)}",
        f"L'urgence dans ce dossier : {q['urgence']} Le proche : {q['proche']}{s(5,6)}",
    )
    out[4] = _p(4,
        f"Démarche pas à pas. D'abord, écarter le danger immédiat. {q['urgence']} Ensuite, lire ce qui a déjà été dit et signé. {q['info']}{s(6,8)}",
        f"Puis tester la capacité seulement si le doute est fondé ou l'incapacité manifeste. {q['capacite']} Puis tester la liberté, y compris hors de la présence du proche. {q['liberte']}{s(7)}",
        f"La conduite qui sort de cette démarche : {q['juste']}{s(8,9)}",
        f"On compare alors aux situations voisines du même motif, sans recycler un réflexe. Un formulaire, un oui, un parent ou un curateur ne ferment pas la démarche.{s(2,7)}",
    )
    out[5] = _p(5,
        f"Questions pour {q['qui'].split(',')[0].lower()}. Que croyez-vous qu'on va vous faire, et dans quel but ? Quel risque grave vous a été nommé ? Que se passe-t-il si vous dites non ? Qui vous a conseillé, et voulez-vous un moment seul ?{s(8,9)}",
        f"Ce qu'il faut entendre dans ce dossier : {q['recit']} La réponse utile n'est pas « oui, j'ai signé ». C'est une reformulation.{s(7)}",
        f"Drapeaux rouges ici : {q['manque']} On les écrit avec l'heure et les personnes présentes.{s(8)}",
        f"Phrase que le médecin peut dire : {q['dit']}{s(9)}",
    )
    out[6] = _p(6,
        f"Examen de la capacité, s'il est indiqué. {q['capacite']} Les quatre capacités de 2019 se cherchent dans ses mots, pas dans un {MMSE}.{s(7)}",
        f"On regarde le {c} comme un fait clinique ou documentaire, puis on le relie à une capacité ou à une condition du consentement. Le signe seul ne pose pas le diagnostic de situation.",
        f"Examen de la liberté : entretien sans le tiers, recherche d'une menace, d'un délai trop court, d'une sédation déjà donnée. {q['liberte']}{s(8)}",
        f"Ce que l'on ne fait pas : un examen neurologique complet à la place de l'entretien, ni une demande de signature pour « objectiver ».{s(7,9)}",
    )
    out[7] = _p(7,
        f"Tableau de ce dossier. Personne : {q['qui']}. Geste : {q['geste']}. Fait dominant : {q['manque']}{s(9)}",
        f"Ce n'est pas un refus éclairé, ou ça l'est, selon les faits suivants, et non selon l'étiquette. Capacité : {q['capacite']}{s(7)}",
        f"Ce n'est pas non plus, automatiquement, une urgence. {q['urgence']} Ce n'est pas non plus, automatiquement, une affaire de représentant. {q['proche']}{s(5,6)}",
        f"Le classement juste ouvre une seule conduite principale : {q['juste']}{s(8)}",
    )
    out[8] = _p(8,
        f"Critères positifs pour retenir « {q['nom']} ». Premier critère : {q['manque']} Deuxième : {q['info']} Troisième : {q['capacite']}{s(7,9)}",
        f"Le critère négatif compte autant. On ne retient pas cette situation si le dossier montre déjà l'inverse, par exemple une reformulation complète, un délai tenu et une capacité claire, lorsque la situation est un manquement.{s(8)}",
        f"Phrase de dossier qui suffit à un correcteur : {q['dossier']}{s(8,9)}",
        f"Le piège de classement : {q['piege']}{s(7)}",
    )
    out[9] = _p(9,
        f"Pièces à réunir pour ce geste, {q['geste']}. Trace de l'entretien, identité de la personne qui a informé, heure, risques graves nommés, alternatives, décision, et témoins utiles.{s(8)}",
        f"Pièces de représentation, seulement si la capacité manque : directives datées et signées, carte d'assuré, mandat, curatelle, lien du proche et aide régulière.{s(3,5)} {q['proche']}",
        f"Pièce linguistique : nom de l'interprète professionnel et langue, dès que le français ne permet pas la reformulation. {q['info']}{s(8)}",
        f"Si la situation est une recherche, pièces de la loi de 2011 : information écrite, écrit distinct, délai, autorisation de la commission. {q['juste']}{s(13)}",
    )
    out[10] = _p(10,
        f"Place dans l'arbre. {q['urgence']} Si l'arbre part vers l'urgence, on s'arrête aux soins indispensables. Sinon on descend vers la capacité.{s(6,7)}",
        f"Place dans la chaîne d'information. {q['info']} Le maillon manquant se corrige avant le geste, sauf l'urgence de l'article 379.{s(8,9)}",
        f"Place dans le parcours refus. {q['liberte']} Un refus capable se respecte. Un silence ou un oui incompris n'est pas un refus, ni un accord.{s(7)}",
        f"Décision lue sur les trois dessins : {q['juste']}{s(9)}",
    )
    out[11] = _p(11,
        f"Conduite à tenir, en Suisse, pour ce dossier. {q['juste']}{s(8,9)}",
        f"Ce que le médecin dit, avec des mots simples : {q['dit']}{s(9)}",
        f"Ce qu'il écrit tout de suite : {q['dossier']} La preuve lui incombe. La mémoire de l'après-midi ne suffit pas.{s(8)}",
        f"Ce qu'il ne prescrit pas : aucune dose n'est indiquée par ce motif. Un sédatif donné pour « faciliter la signature » détruirait le consentement, selon le guide de juin 2026.{s(8)}",
        f"Représentant et directives, rappel utile même si ce n'est pas le fait principal. Ordre de l'article 378, plan de l'article 377, urgence de l'article 379, saisine de l'autorité selon l'article 381, traitement psychiatrique d'une personne placée selon les règles du {PAFA}, article 380.{s(4,5,6)} Ici : {q['proche']}",
    )
    out[12] = _p(12,
        f"Prévention pour le prochain patient du même type. Annoncer l'entretien comme un soin, pas comme une formalité d'accueil. Prévoir la langue, le délai, et le moment sans tiers.{s(8)}",
        f"Pour {q['geste']}, la prévention concrète est de ne pas répéter le défaut : {q['manque']}{s(9)}",
        f"Au bloc, une check-list tient en quatre lignes : qui a informé, quels risques graves, quelle alternative, quelle décision, à quelle heure, et la personne était-elle encore capable et non sédatée.{s(8)}",
        f"Après coup, si le défaut est déjà réalisé, on le dit à la personne, on le trace, et on ne le couvre pas par une signature tardive.{s(9)}",
    )
    out[13] = _p(13,
        f"À retenir pour « {q['nom']} ». {q['manque']}{s(9)}",
        f"La conduite en une phrase : {q['juste']}{s(8)}",
        f"La phrase vraie que l'étudiant écrit : {q['dossier']}{s(8)}",
        f"La phrase fausse qu'il faut rayer : {q['piege']}{s(7,9)}",
    )
    out[14] = _p(14,
        f"Cas corrigé. {q['qui']}. {q['recit']} Le premier réflexe, faire comme si la signature suffisait, est le piège : {q['piege']}{s(9)}",
        f"Correction. {q['juste']} Le médecin dit : {q['dit']} Il écrit : {q['dossier']}{s(8)}",
        f"Ce que le cas enseigne sur la capacité et la liberté. {q['capacite']} {q['liberte']}{s(7)}",
        f"Ce que le cas enseigne sur l'entourage et l'urgence. {q['proche']} {q['urgence']}{s(5,6)}",
        f"Question d'examen. Quel fait reclasse le dossier, et quelle conduite en découle ? Réponse : le fait est {q['manque']} La conduite est {q['juste']}{s(9)}",
    )
    # Cartes courtes : première phrase seulement, sans couper un mot au milieu.
    cartes = {}
    resumes = {
        1: f"Situation : {q['nom']}. {q['qui']}.",
        2: f"Aucun pourcentage suisse de ce manquement n'a été lu en 2026. Les chiffres de directives, 24 pour cent et 16 pour cent, ne se recyclent pas ici sans raison.",
        3: f"L'atteinte est {q['geste']}. Le titre juridique se juge sur l'information, la capacité et la liberté.",
        4: f"On écarte d'abord l'urgence vitale, puis on décrit information, capacité et liberté.",
        5: f"L'anamnèse cherche ce que la personne a compris, pas ce qu'elle a signé.",
        6: f"L'examen clé est l'entretien des quatre capacités, quand le doute est fondé.",
        7: f"Le tableau se classe par le fait dominant, pas par le nom du geste.",
        8: f"Le diagnostic de situation exige des critères positifs écrits dans le dossier.",
        9: f"Les pièces utiles sont la trace, et, si besoin, directives, représentant ou interprète.",
        10: f"L'arbre, la chaîne d'information et le parcours du refus donnent la même conduite.",
        11: f"Conduite : {q['juste'][:180]}",
        12: f"On prévient le défaut en séparant l'entretien de la signature d'accueil.",
        13: f"Le piège à rayer : {q['piege'][:160]}",
        14: f"Le cas corrigé part du dossier réel et aboutit à une phrase de dossier.",
    }
    for n, txt in resumes.items():
        cartes[n] = txt
    return out, cartes


TABLEAU_DX = """
<div class="tw"><table>
<caption>Dix situations du motif, et le fait qui les sépare</caption>
<thead><tr><th>Situation</th><th>Fait qui reclasse</th><th>Conduite immédiate</th></tr></thead>
<tbody>
<tr><td>Acte sans consentement valable</td><td>Une condition manque, souvent l'information, et le geste est parti ou va partir.</td><td>Arrêter ou reporter. Reprendre l'entretien.</td></tr>
<tr><td>Défaut d'information</td><td>Risque grave ou alternative tus, alors que la personne était capable.</td><td>Compléter avant le geste. Prouver ensuite.</td></tr>
<tr><td>Consentement d'une personne incapable</td><td>Acquiescement sans les quatre capacités.</td><td>Ne pas faire signer. Directives, puis représentant.</td></tr>
<tr><td>Passage outre un refus</td><td>Refus capable, stable, éclairé.</td><td>Respecter. Organiser l'alternative.</td></tr>
<tr><td>Urgence, personne incapable</td><td>Danger immédiat, personne qui ne décide pas, soins indispensables.</td><td>Article 379. Pas d'élargissement.</td></tr>
<tr><td>Consentement valable</td><td>Information, capacité, liberté, trace.</td><td>Faire le geste. Confirmer avant toute sédation.</td></tr>
<tr><td>Mineur capable</td><td>Il décide pour ce soin. Les parents n'ont pas de veto.</td><td>Consentement personnel. Frais à part.</td></tr>
<tr><td>Curatelle avec capacité</td><td>La curatelle ne retire pas le discernement.</td><td>La personne consent elle-même.</td></tr>
<tr><td>Barrière linguistique</td><td>Pas de reformulation dans sa langue.</td><td>Interprète professionnel. Reporter si électif.</td></tr>
<tr><td>Recherche</td><td>Projet distinct du soin.</td><td>Écrit, délai, commission, retrait libre.</td></tr>
</tbody></table></div>
"""

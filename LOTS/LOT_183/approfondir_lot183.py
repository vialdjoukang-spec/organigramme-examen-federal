# -*- coding: utf-8 -*-
"""Approfondissement du 25.10.2026. Faits lus ce jour, doses AIPS non prescrites."""
from html import escape


def p(text):
    return f"<p style='margin:4px 0 6px;'>{text}</p>"


def table(headers, rows):
    th = "".join(
        f"<th style='background:#d4e6f1;text-align:left;vertical-align:top;'>{escape(h)}</th>"
        for h in headers
    )
    body = []
    for row in rows:
        tds = "".join(
            f"<td style='vertical-align:top;'>{escape(c)}</td>" for c in row
        )
        body.append(f"<tr>{tds}</tr>")
    return (
        "<div style='overflow-x:auto;'><table border='1' cellpadding='7' cellspacing='0' "
        "style='width:100%;border-collapse:collapse;font-size:0.92em;'>"
        f"<thead><tr>{th}</tr></thead><tbody>{''.join(body)}</tbody></table></div>"
    )


def fen(title, chunks, source):
    inner = []
    for c in chunks:
        inner.append(c if c.startswith("<") else p(c))
    return (
        "<details style='margin:8px 0;border-left:4px solid #1a5276;background:#f8f9f9;"
        "padding:6px 10px;'><summary style='cursor:pointer;font-weight:bold;color:#1a5276;'>"
        f"{escape(title)}</summary><div style='margin-top:6px;'>{''.join(inner)}"
        f"<em>Source : {escape(source)}.</em></div></details>"
    )


def sec(title, lines, source):
    return fen(title, lines, source)


def dx5():
    e, z, j, s, w = "[S201]", "[S202]", "[S203]", "[S204]", "[S205]"
    o = []
    o.append(sec("Ce que le dépliant ESPE est, et ce qu'il n'est pas", [
        "Le document rouvert le 25.10.2026 est un guide patient de la série Hormone Disorders, niveau de lisibilité moyenne, révisé en novembre 2019. Il explique le retard constitutionnel de croissance et de puberté. Il n'est pas une recommandation de la Société suisse de pédiatrie, ni une information professionnelle Swissmedic.",
        "Le dépliant dit que son développement a été financé, comme service à la médecine, par Merck, à partir des livrets de la Child Growth Foundation britannique et de la BSPED, puis adaptés par l'ESPE. Vous le citez comme source pédagogique européenne. Vous ne le transformez pas en autorisation de mise sur le marché.",
        "Il annonce qu'il aide à discuter avec le médecin de famille ou l'équipe spécialisée. Cette phrase fixe votre rôle : expliquer, puis adresser quand le seuil ou la souffrance l'exige, sans signer une dose absente du texte suisse.",
        "Vous dites à l'étudiant que la définition y est clinique : petite taille temporaire due à un retard du développement pubertaire, chez une personne par ailleurs en bonne santé, sans anomalie physique qui expliquerait le retard.",
        "Le même texte précise que la situation est plus fréquente chez les garçons que chez les filles, et qu'elle trouble autant les deux sexes. Vous n'en déduisez pas une prévalence suisse.",
        "Piège : présenter ce dépliant comme une AIPS ou comme un consensus chiffré de pédiatrie suisse. Il ne contient ni numéro Swissmedic ni schéma en milligrammes.",
    ], e))
    o.append(sec("Calendrier que vous récitez sans le déplacer", [
        "La puberté est le passage de l'enfant à l'adulte. Chez la fille, le dépliant nomme le développement mammaire. Chez le garçon, il nomme l'augmentation du pénis et la croissance des testicules. L'ordre d'apparition de ces changements reste le même même si le début est retardé.",
        "Le début moyen est 10 à 11 ans chez la fille et 12 ans chez le garçon. L'absence de tout signe physique à 13 ans chez la fille ou à 14 ans chez le garçon fait envisager un avis.",
        "Le pic statural, hausse rapide de la taille et du poids, se place d'habitude à 10–12 ans chez la fille et à 12–14 ans chez le garçon. Dans ce retard, le pic de vitesse est réduit, et les garçons traversent la puberté plus lentement.",
        "La durée normale de la puberté est de trois à quatre ans. Si un traitement est décidé, la progression ne doit pas être plus rapide qu'en un à deux ans.",
        "Vous séparez donc trois horloges : l'âge civil, l'âge du premier signe, et la durée du parcours. Confondre les trois fait prescrire trop tôt ou trop vite.",
        "Une fille de 12 ans et 8 mois sans sein n'a pas franchi 13 ans. Vous mesurez et vous revoyez. Vous ne lancez pas le bilan d'exclusion comme si le seuil était déjà tombé, et vous ne promettez pas non plus d'attendre encore une année entière sans date.",
    ], e))
    o.append(sec("Âge osseux : ce que le dépliant vous autorise à dire", [
        "À la naissance, de larges espaces séparent les extrémités des os longs. Ces espaces laissent la croissance se faire. Ils diminuent avec l'âge. À la fin de la puberté, les os fusionnent et la croissance s'arrête.",
        "Mesurer cet espace, c'est lire l'âge osseux. Le dépliant demande une radiographie de la main et du poignet gauches, comparée à l'âge de l'enfant. Cette lecture estime le temps de croissance restant.",
        "La plupart des enfants petits pour leur âge ont un âge osseux retardé, et certains enfants grands ont un âge osseux avancé. Le spécialiste de la croissance s'en sert pour dire combien de croissance reste possible. Le dépliant ne donne pas une équation qui transformerait ce cliché en centimètres adultes garantis.",
        "Vous refusez donc la phrase « l'âge osseux promet 178 cm ». Vous dites « le cartilage n'est pas fermé, le temps restant existe, la cible parentale n'est pas sauvée d'office si le retard est extrême ».",
        "Le côté gauche est nommé. Vous ne remplacez pas le cliché par une main droite sans l'écrire. Le nom de l'atlas utilisé en Suisse n'est pas dans le dépliant : donnée non trouvée dans cette source.",
        "Piège d'examen : traiter l'âge osseux comme une preuve que la taille finale sera normale. Le paragraphe suivant du dépliant dit le contraire pour les retards extrêmes.",
    ], e))
    o.append(sec("Taille finale : l'idée ancienne et la correction", [
        "La tradition disait que le seul décalage de l'âge osseux n'empêchait pas d'atteindre la taille adulte, parce qu'il ne s'agissait que d'un retard. Le dépliant écrit qu'on a montré plus récemment que les enfants dont la puberté est extrêmement retardée peuvent ne pas atteindre une taille finale appropriée à la taille parentale.",
        "Le mécanisme qu'il donne est double : le pic de vitesse est réduit, et les garçons avancent plus lentement. La taille finale et le développement sexuel arrivent donc encore plus tard que le simple décalage ne le laissait croire.",
        "Vous expliquez cette nuance aux parents avant qu'ils n'entendent « il rattrapera tout ». Vous ne convertissez pas la nuance en un nombre de centimètres perdus : le dépliant ne donne pas ce nombre.",
        "Vous reliez cette limite au but du traitement éventuel. La testostérone à faible dose, dit le dépliant, ne réduit pas la taille adulte que le garçon peut espérer. Elle change le moment du pic et l'âge auquel ce pic est atteint.",
        "Cette phrase n'est pas une autorisation de dose. Elle dit l'effet attendu sur le calendrier, pas le milligramme suisse.",
        "Piège : promettre la cible parentale à un garçon de 16 ans encore prépubère, ou au contraire annoncer une perte chiffrée que la source ne contient pas.",
    ], e))
    o.append(sec("Quatre diagnostics que le dépliant vous fait écarter", [
        "Le dépliant dit qu'il est souvent difficile de distinguer ce retard d'autres conditions, et qu'il faut écarter les problèmes médicaux courants puis certaines entités plus rares.",
        "L'insuffisance gonadique : les testicules ou les ovaires ne produisent pas leurs hormones. Un prélèvement sanguin cherche cette défaillance. Vous attendez des gonadotrophines hautes si le stéroïde est bas. Une hormone basse isolée chez le prépubère ne suffit pas, fait déjà tiré de la revue et non contredit par le dépliant.",
        "Le syndrome de Turner : condition génétique limitée aux filles, qui ralentit la croissance et la puberté et peut toucher le cœur et les reins. Toute fille avec puberté retardée doit avoir une étude chromosomique. Vous ne cherchez pas d'abord un pterygium pour décider le prélèvement.",
        "La dysplasie osseuse : le trait principal est un développement osseux anormal. Si vous le voyez, vous envisagez ce diagnostic et vous quittez la variante.",
        "Le déficit en hormone de croissance : dans cette tranche d'âge, ces enfants sont habituellement beaucoup plus petits que ceux qui ont un retard constitutionnel.",
        "Vous nommez les quatre avant de rassurer. L'ordre du dépliant est un ordre d'exclusion, pas une liste décorative.",
    ], e))
    o.append(sec("Traitement selon le dépliant, sans le transformer en ordonnance", [
        "Habituellement, aucun traitement n'est nécessaire. Si une aide est utile, une hormone sexuelle peut accélérer le processus pour rapprocher l'adolescent de ses pairs, sans parcourir la puberté plus vite qu'en un à deux ans.",
        "Le traitement vise deux choses : accélérer la croissance et développer les caractères sexuels secondaires.",
        "Chez la fille, une faible dose d'œstrogène est donnée en comprimé quotidien pendant six mois à un an, ou en partie d'un patch cutané. Le sein apparaît tôt, avec l'accélération de croissance attendue. On continue jusqu'à ce que la puberté propre de l'enfant dépasse celle que l'œstrogène a produite.",
        "Chez le garçon, une faible dose de testostérone peut lancer le pic : injection chaque mois, ou comprimé chaque jour, pendant trois à six mois. Un gel à faible dose est parfois utilisé à la place. Pour les garçons plus âgés très inquiets de l'absence de caractères sexuels et de la croissance lente, l'injection est le traitement le plus habituel du dépliant : elle démarre les caractères et le pic.",
        "Aucun de ces modes n'est accompagné d'une spécialité suisse, d'un numéro d'autorisation ni d'une dose en milligrammes dans le dépliant. Les chiffres de milligrammes lus ailleurs viennent de la revue européenne déjà citée. Vous ne les recopiez pas sur une ordonnance.",
        "Vous écrivez dans le dossier : explication faite, seuil ESPE rappelé, dose AIPS non lue, adressage si la souffrance ou le retard extrême justifie qu'un endocrinologue ouvre l'information professionnelle.",
    ], e))
    o.append(sec("Souffrance : le dépliant en fait une indication de conseil", [
        "L'adolescence est faite de changements sociaux, d'adaptation à la vie adulte et du début des relations. Beaucoup d'enfants qui ont ce retard, surtout les garçons, peinent à suivre ces changements.",
        "La difficulté porte d'abord sur la taille, puis, en grandissant, sur l'absence de développement sexuel. Certains répondent par un comportement agressif ou immature.",
        "Si ce comportement désorganise l'école ou la maison, le dépliant demande d'envisager un conseil. Le conseil n'est pas un médicament, et il ne remplace pas l'exclusion d'une maladie.",
        "Vous posez trois questions concrètes : l'école se plaint-elle, la maison se désorganise-t-elle, l'adolescent évite-t-il les vestiaires ou le sport. Une réponse oui ouvre le conseil et la discussion d'un adressage. Une réponse non laisse la surveillance au premier plan.",
        "Vous ne minimisez pas la plainte parce que la condition est transitoire. Le dépliant dit qu'elle trouble autant les filles, même si les garçons consultent et souffrent plus souvent dans ce texte.",
        "Piège : attendre que la taille finale soit connue pour prendre au sérieux une souffrance actuelle.",
    ], e))
    o.append(sec("Mesure : les 15 mm de la journée et l'erreur de 2 à 3 cm", [
        "La page familles du PEZZ, relue le 25.10.2026, écrit que le corps peut diminuer de jusqu'à 15 mm dans la journée, parce que les disques intervertébraux perdent de l'eau. La nuit, allongé, le disque se réhydrate. Vous mesurez donc toujours à la même heure.",
        "Pour la vie de famille, le soir est présenté comme le meilleur moment. Au cabinet, vous gardez l'heure de la visite et vous la notez, pour ne pas comparer un matin à un soir sans le dire.",
        "L'enfant se tient droit. Les jeunes enfants montent sur la pointe des pieds : une deuxième personne maintient les deux pieds à plat. L'équerre au-dessus de la tête est à angle droit. Sans toise, un livre tenu verticalement contre le mur, abaissé jusqu'au sommet du crâne, laisse un trait que l'on mesure depuis le sol.",
        "La même page dit que des erreurs de 2 à 3 cm surviennent même dans les cabinets. Un enfant de 10 ans grandit d'environ 5 cm par an. Mesuré deux fois dans l'année, la différence attendue est d'environ 2,5 cm. Une erreur de 2,5 cm rend impossible de savoir si la croissance de l'année était normale.",
        "Calcul dérivé : 5 cm par an sur 6 mois font 2,5 cm. Ce 2,5 cm est l'exemple du PEZZ, pas un seuil de pathologie. Vous l'utilisez pour exiger une technique stable avant d'interpréter une vitesse.",
        "Piège : conclure à une cassure sur deux mesures prises l'une le matin sans chaussures, l'autre le soir avec une toise différente, sans avoir écarté les 15 mm et l'erreur de manipulation.",
    ], w))
    o.append(sec("Canal, percentile et ce que la courbe compare", [
        "La taille et le poids du nouveau-né reflètent surtout la vie intra-utérine. Les deux premières années servent à ajuster la croissance au modèle hérité. Après le deuxième anniversaire, la croissance suit le canal de percentile hérité jusqu'au début de la puberté.",
        "Pendant ces deux premières années, un changement de canal est l'ajustement, pas la preuve d'une maladie. Après deux ans, quitter le canal est suspect.",
        "Exemple du PEZZ : un garçon au 50e percentile à 2 ans devrait y rester jusqu'à environ 12 ans si tel est son canal. Le mot « courbe de croissance » désigne en réalité une courbe de comparaison avec les pairs.",
        "Au 10e percentile, sur 100 enfants sains du même âge et du même sexe, 9 sont plus petits et 90 sont plus grands. Sous le 3e percentile, les spécialistes cités par la page considèrent l'enfant trop petit. Au-dessus du 97e, trop grand. Ces phrases décrivent une position, pas la cause.",
        "La page demande une mesure au moins annuelle, précise, reportée. L'évolution dit si le mécanisme fonctionne, par exemple si l'intestin, le rein et les hormones thyroïdiennes, somatotropes, surrénaliennes et sexuelles permettent la croissance. Ce n'est pas une liste d'examens obligatoires à chaque visite annuelle d'un enfant dont le canal est stable.",
        "Vous appliquez cela au retard constitutionnel : une cassure franche après 2 ans vous fait quitter le tempo et chercher une maladie, dont celles des DX suivants.",
    ], w))
    o.append(sec("Trois cibles, et l'arithmétique que la page imprime mal pour le garçon", [
        "La page familles part d'une différence de 13 cm entre hommes et femmes adultes, différence constatée dans une des premières études de Tanner, et dit que l'on sait encore peu de chose sur la transmission de la taille finale et de la vitesse.",
        "Méthode simple, fille : elle reçoit la taille de sa mère, et la taille de son père diminuée de 13 cm. Garçon : la taille de son père, et la taille de sa mère augmentée de 13 cm. Si chaque parent contribue pour moitié, la cible de la fille est (taille du père − 13 cm) / 2 + taille de la mère / 2, et celle du garçon (taille de la mère + 13 cm) / 2 + taille du père / 2.",
        "La page écrit aussi (mère + père) / 2 + 6,5 cm chez le garçon et − 6,5 cm chez la fille. Calcul dérivé : ajouter 6,5 cm après la moyenne égale ajouter 13 cm avant de diviser par deux. Les deux écritures sont la même formule.",
        "Exemple de la page, parents tous deux à 170 cm, fille. Mère corrigée 170 cm. Père corrigé 170 − 13 = 157 cm. Moyenne (157 + 170) / 2 = 163,5 cm. Ce résultat imprimé est juste. Calcul dérivé vérifié : 157 + 170 = 327, et 327 / 2 = 163,5.",
        "Même exemple, garçon. Mère corrigée 170 + 13 = 183 cm. Père 170 cm. Moyenne (183 + 170) / 2 = 176,5 cm. Calcul dérivé : 183 + 170 = 353, et 353 / 2 = 176,5. La page imprime 178,5 cm pour ce total. 178,5 ne correspond pas à l'addition. Vous corrigez l'erreur arithmétique et vous ne la recopiez pas.",
        "La page juge cette formule la moins fiable quand les parents ont des tailles très différentes, et elle propose de tracer trois repères : la cible maternelle corrigée, la cible paternelle corrigée, et leur moyenne. Vous les tracez. Vous ne promettez pas lequel des trois l'enfant réalisera.",
    ], w))
    o.append(sec("Régression vers la moyenne : formule de Cole–Hermanussen, sans SDS inventé", [
        "La page dit que les modèles simples exagèrent les cas extrêmes, parce que les enfants de parents très grands sont en moyenne un peu moins grands que le modèle, et les enfants de parents très petits un peu moins petits. C'est la régression vers la moyenne.",
        "Elle donne la formule de Cole–Hermanussen : cible en déviation standard = (SDS du père + SDS de la mère) / 2, multiplié par 0,72. Le calcul exige une calculatrice et, surtout, les déviations standards parentales lues sur une référence. Vous ne fabriquez pas un SDS à partir d'une taille en centimètres sans la courbe.",
        "Vous pouvez donc énoncer la formule et son sens. Vous ne pouvez pas, dans ce dossier, produire un chiffre de Cole pour une famille dont vous n'avez pas les SDS. Donnée non calculable tant que la référence n'est pas appliquée aux parents.",
        "La page ajoute que le mécanisme exact de l'hérédité de la taille reste largement inconnu, et que des calculs situent l'information de la taille finale à au moins quatre endroits du génome. Vous ne transformez pas cette phrase en un panel de quatre gènes à prescrire.",
        "Vous dites aussi que la page familles n'est pas un article de méthode. Elle explique un principe aux familles. Le 0,72 est le coefficient qu'elle imprime. Vous ne l'arrondissez pas et vous ne l'appliquez pas à des centimètres bruts.",
        "Piège d'examen : multiplier la cible en centimètres par 0,72 et appeler cela Cole. Le coefficient s'applique à la moyenne des SDS, pas aux centimètres.",
    ], w))
    o.append(sec("Lecture de l'âge osseux selon le PEZZ, et ses limites", [
        "Le PEZZ rappelle que deux enfants du même jour de naissance peuvent avoir des maturations différentes. Si la puberté commence tôt, la croissance finit tôt. Si elle commence tard, la croissance finit tard. Le programme précoce ou tardif se transmet souvent dans la famille.",
        "Dès le deuxième anniversaire, l'âge biologique peut être estimé sur une radiographie de la main. On ne mesure pas la longueur des os de la main. On juge leur forme tridimensionnelle sur une image plane. Selon la méthode, on cote 13 ou 20 os, puis on moyenne.",
        "Quand c'est possible, la page dit que l'âge osseux est déterminé selon Greulich–Pyle et selon Tanner (TW2 et TW3), et que les prévisions utilisent Bayley–Pinneau, Roche et Tanner (TW2 et TW3), plus une lecture clinique. Vous nommez ces méthodes. Vous n'en inventez pas le mode d'emploi chiffré : il n'est pas détaillé sur la page.",
        "La page affirme qu'une méthode fondée permet d'estimer le début probable de la puberté, puis elle explique pourquoi beaucoup de jeunes adultes sont déçus : une prévision de 180 cm aboutit parfois à 165 cm. L'erreur la plus fréquente est la lecture elle-même. L'expérience qu'elle décrit est celle de qui cote plus de cent âges osseux par an, souvent avec plusieurs méthodes, en général chez l'endocrinologue pédiatre.",
        "Plus l'enfant grandit de façon moyenne, plus la prévision est précise. Or ce sont les croissances atypiques qui motivent la prévision. La prévision est un sous-produit : le but premier est de savoir s'il existe une maladie.",
        "Vous ne dites donc pas « totalement fiable » comme conclusion personnelle. Vous rapportez que la page emploie des mots forts, puis qu'elle documente elle-même l'erreur de lecture, l'exemple 180 contre 165, et la moindre précision hors du schéma moyen.",
    ], w))
    o.append(sec("Enfant né petit pour l'âge gestationnel : ne pas lui appliquer la prévision moyenne", [
        "La page dit que la croissance future n'est pas moyenne lorsque les proportions sont très inhabituelles, ou lorsque l'enfant est né small for gestational age.",
        "Une part importante de ces enfants ne grandit pas comme la majorité. Ils ont souvent une petite poussée vers 8–10 ans, puis une poussée pubertaire qui apporte moins de centimètres que chez les autres. La taille adulte tombe alors sous la prévision initiale. La page dit que cela n'est su que depuis quelques années, après analyse des enfants qui n'avaient pas atteint la taille prévue.",
        "Vous ne chiffrez pas cette « part importante » : la page ne donne pas de pourcentage. Vous ne chiffrez pas non plus les centimètres manquants de la poussée pubertaire.",
        "Devant un adolescent né petit pour l'âge gestationnel, un âge osseux retardé et une histoire familiale de puberté tardive peuvent coexister. Vous ne concluez pas au seul retard constitutionnel. Vous dites que la prévision moyenne est moins fiable, et vous cherchez les exclusions du dépliant ESPE.",
        "Le protocole suisse de l'hormone de croissance chez l'enfant né petit pour l'âge gestationnel n'a pas été lu. Vous n'inventez ni indication ni dose.",
        "Piège : rassurer avec une cible parentale calculée comme si la naissance avait été eutrophe et le canal moyen.",
    ], w + ", " + e))
    o.append(sec("Ce que la page familles dit de la génétique, et ce que vous n'en faites pas", [
        "La page écrit qu'environ 80 % des variations de croissance peuvent s'expliquer génétiquement, en général par plusieurs gènes. Elle écrit que les variants courants, qu'elle situe présents chez moins de 5 % de la population, expliquent environ 50 % des différences de taille adulte. Tous les gènes ne sont pas connus.",
        "Vous citez ces deux ordres de grandeur comme les phrases de la page familles, pas comme un article de génétique que vous auriez ouvert. Vous ne les mélangez pas avec le chiffre de 7 % de variants d'hypogonadisme déjà tiré de la revue de Galazzi le 24.10.2026.",
        "Les retards sévères sont plus souvent liés à un variant rare d'un seul gène. Plus l'enfant est petit, plus cette probabilité augmente, dit la page, sans donner le seuil de taille à partir duquel le test devient indiqué.",
        "Le conseil génétique du PEZZ se dit non directif. L'ADN ne voit en général que les modifications les plus courantes. Même un variant identifié ne prédit pas avec certitude si et quand une maladie apparaîtra.",
        "La page nomme Genetica et des techniques (NGS, array-CGH, et d'autres) comme l'offre du laboratoire qu'elle utilise. Vous ne prescrivez pas ces sigles. Aucun remboursement suisse n'a été lu pour un panel de routine du retard constitutionnel.",
        "Piège : annoncer « 80 % donc c'est génétique, pas besoin d'examen ». Le pourcentage explique la variance populationnelle. Il ne ferme pas un Turner, une cassure ou une anosmie.",
    ], w))
    o.append(sec("Courbes nationales 2026 : ce que le communiqué ajoute à la lecture du 24 octobre", [
        "Le communiqué du 16 juin 2026, relu le 25.10.2026, rappelle que les courbes utilisées en Suisse depuis 2011 s'appuyaient en partie sur l'OMS et sur des données américaines, et qu'elles ne correspondent plus à l'état des connaissances. Les nouvelles courbes sont les premières courbes nationales sur une base élargie.",
        "Elles ont été construites au PEZZ sous la direction d'Urs Eiholzer, à partir de plus de 43 000 enfants et adolescents de toutes les régions linguistiques, mesurés par plus de 100 pédiatres, dans les écoles, avec un complément sur les nouveau-nés et les recrues. Le communiqué dit qu'environ un enfant sur 40 vivant en Suisse, soit un habitant sur 210, a été mesuré et pesé, et que la modélisation utilise la méthode LMS.",
        "Taille, poids et IMC dès 2 ans viennent de ces données nationales. L'IMC des deux premières années reste celui de l'OMS. Le périmètre crânien combine les études longitudinales de Zurich de 0 à 2 ans et KiGGS de 2 à 18 ans. Les courbes de vitesse restent celles de Zurich.",
        "Les seuils cliniques, dont la petite taille, restent ceux des sociétés compétentes. Le communiqué fixe en revanche, dès 2 ans, les seuils inférieurs du surpoids et de l'obésité par des courbes d'équivalence qui atteignent à 18 ans un IMC de 25 kg/m² et de 30 kg/m². Ces ancres concernent le poids, pas le diagnostic de retard constitutionnel.",
        "Le communiqué cite Eiholzer et coll., Journal of Clinical Medicine 2025, article 5912, dont le titre annonce l'absence de différence de taille et des variations d'IMC associées à la migration. Le texte intégral de cet article n'a pas été ouvert. Vous ne tirez aucun pourcentage de migration ni aucun delta de centimètres de ce titre seul. La page familles du PEZZ écrit de son côté que l'augmentation de l'obésité infantile en Suisse est principalement due à la migration : vous attribuez cette phrase à la page familles, sans la fusionner avec un chiffre absent de l'article non lu.",
        "Pour ce DX, la conséquence est pratique : vous reportez la taille sur la courbe recommandée depuis le 15 juin 2026, vous gardez la courbe de vitesse zurichoise, et vous ne laissez pas un changement de référence réécrire le seuil ESPE de 13 et 14 ans.",
    ], s + ", " + w))
    o.append(sec("Poids pour la taille : ne pas conclure le retard sur un IMC isolé", [
        "Le PEZZ préfère, pour suivre un enfant qui grandit, une courbe du poids en fonction de la taille, calculée à Zurich il y a 25 ans selon la page, plutôt que le seul IMC. Il rappelle que le poids pour l'âge perd de son sens dès que l'enfant s'éloigne de la taille moyenne.",
        "La page décrit l'IMC comme une mesure reprise de l'adulte. Elle écrit l'unité de façon lâche. Vous ne recopiez pas une unité fausse. Le communiqué de pédiatrie suisse ancre le surpoids et l'obésité sur 25 et 30 kg/m² à 18 ans. Vous utilisez kg/m².",
        "Dans le retard constitutionnel, la revue déjà lue le 24.10.2026 signalait des enfants qui mangent parfois peu et un indice de masse corporelle plutôt bas. Vous le notez, parce que la leptine relie l'énergie à l'axe. Vous ne posez pas le diagnostic sur cet indice.",
        "Un poids qui monte pendant que la taille casse oriente vers une autre cause, dont l'hypothyroïdie de la fiche lausannoise, et non vers un simple tempo.",
        "Vous reportez donc trois choses : taille pour l'âge sur la courbe 2026, vitesse, et rapport du poids à la taille. Un seul de ces trois graphes ne suffit pas.",
        "Piège : appeler malnutrition ou retard constitutionnel un enfant seulement parce que son IMC est sous la moyenne, sans vitesse et sans stade pubertaire.",
    ], w + ", " + s))
    o.append(sec("Station — garçon de 14 ans et 3 mois, père au tempo lent", [
        "Il entre parce qu'il est le plus petit de la classe. La mère dit que le père s'est rasé tard. Vous notez la phrase et vous ne concluez pas.",
        "Vous mesurez l'adolescent, le père et la mère, à une heure notée, pieds nus, talons au sol. Vous calculez la cible avec +13 cm et l'intervalle de ± 8,5 cm déjà lu dans Paediatrica. Vous refusez les tailles de mémoire.",
        "Vous palpez les testicules. S'ils sont encore infantiles, le seuil de 14 ans du dépliant est franchi. Vous demandez l'âge osseux de la main et du poignet gauches. Un retard d'au moins un an entre dans le type 1 déjà décrit.",
        "Vous demandez s'il sent les odeurs et si les testicules sont descendus. Vous cherchez une céphalée matinale, un vomissement, un trouble visuel. Un de ces signes vous fait quitter la variante le jour même.",
        "Vous demandez TSH, thyroxine libre, LH, FSH et testostérone. Vous ne démarrez pas d'hormone de croissance. Vous n'écrivez pas de testostérone tant que l'AIPS n'est pas lue.",
        "Au retour, âge osseux retardé, bilan d'exclusion négatif, vitesse qui n'est pas effondrée : vous expliquez le retard probable, le pic possiblement atténué, et la visite de contrôle. Vous proposez un conseil si l'école se désorganise.",
    ], e + ", " + w + ", " + j))
    o.append(sec("Station — fille de 13 ans et 1 mois sans bourgeon", [
        "Aucun bourgeon mammaire n'est palpable. Le seuil féminin du dépliant est franchi. Le caryotype part, parce que le Turner ralentit croissance et puberté et peut toucher le cœur et les reins.",
        "Vous ne conditionnez pas le caryotype à une dysmorphie. Vous mesurez la cible et la vitesse. Un déficit somatotrope rend habituellement l'enfant beaucoup plus petit que ce retard.",
        "Vous expliquez que l'attente seule est interdite tant que le caryotype est inconnu. Si le caryotype est 46,XX, que l'âge osseux retarde, que les gonadotrophines ne montrent pas une insuffisance ovarienne et que l'examen est normal, le cadre constitutionnel redevient discutable.",
        "Si la FSH est élevée et que l'œstradiol est bas, vous quittez ce DX. C'est une insuffisance gonadique, et le dépliant demande le prélèvement précisément pour cela.",
        "La guideline cœliaque, dans un autre DX, met le syndrome de Turner parmi les situations où l'on envisage la sérologie. Vous ne faites pas de ce rappel une obligation chiffrée de ce dépliant. Vous y pensez si la croissance ou les symptômes digestifs sortent du tempo.",
        "Vous ne prescrivez pas d'œstrogène sur la foi du dépliant. Le comprimé et le fragment de patch y sont décrits sans dose suisse.",
    ], e))
    o.append(sec("Station — la vitesse tombe sous le profil habituel des garçons", [
        "La revue lue le 24.10.2026 écrit que la vitesse des garçons dans ce cadre dépasse souvent 3,6 cm par an. Ce seuil ne discrimine pas chez les filles, selon la même revue.",
        "Exemple de méthode, calcul dérivé, déjà vérifié : 118,0 cm à 6,0 ans et 122,4 cm à 6,8 an donnent 4,4 / 0,8 = 5,5 cm par an. Ce chiffre reste compatible avec un canal lent. Il ne prouve pas le diagnostic à lui seul.",
        "Autre exemple, calcul dérivé : 140,0 cm à 12,0 ans et 142,2 cm à 12,8 an donnent 2,2 cm en 0,8 an, soit 2,75 cm par an. Vous êtes sous 3,6. Le profil habituel du garçon avec retard constitutionnel ne tient plus. Vous cherchez un déficit somatotrope, une maladie chronique, une cœliaquie, une hypothyroïdie.",
        "Vous ne comparez pas ce prépubère à un camarade déjà en pic sans le dire. Le pic manque parce que les stéroïdes ne sont pas là. Une vitesse basse n'est donc pas, à elle seule, un déficit en hormone de croissance. Une vitesse très basse et une taille très sévère le deviennent.",
        "Le PEZZ ajoute que l'erreur de mesure peut fabriquer une fausse chute. Vous vérifiez la technique avant de lancer un test de stimulation.",
        "Piège : répéter « c'est comme le père » devant 2,75 cm par an.",
    ], "[S202], " + w))
    o.append(sec("Station — céphalée du matin, vous ne classez pas", [
        "Une céphalée matinale, un vomissement ou un trouble visuel ne sont pas des symptômes du dépliant ESPE pour cette variante. La revue vous faisait déjà quitter l'étiquette.",
        "Vous mesurez quand même, parce que la courbe sert, mais vous n'attendez pas l'âge osseux pour reconnaître l'urgence relative. L'imagerie dépend de la clinique neurologique. Le protocole suisse d'imagerie n'a pas été ouvert : vous n'inventez ni séquence ni délai en minutes.",
        "Vous ne rassurez pas avec l'histoire du père. Un tempo familial n'exclut pas une lésion.",
        "Vous différerez le conseil scolaire et toute discussion de stéroïde. Le problème du jour n'est pas le calendrier pubertaire.",
        "Si le signe neurologique est absent et que seuls l'école et la taille inquiètent, vous revenez au chemin du retard, sans avoir banalisé la question.",
        "Piège d'examen : cocher « variante bénigne » sur une copie qui mentionne des vomissements du matin.",
    ], e))
    o.append(sec("Tableau — cinq cadres, un signe qui tranche", [
        table(
            ["Cadre", "Signe qui l'approche", "Signe qui le fait quitter", "Erreur"],
            [
                ["Retard constitutionnel", "Prépubère à 13 ans (fille) ou 14 ans (garçon), âge osseux retardé, enfant sain.", "Caryotype anormal, gonadotrophines hautes, vitesse effondrée, signe neurologique.", "Croire le père sans cliché ni exclusion."],
                ["Petite taille familiale", "Canal stable après 2 ans, cible basse, puberté à l'heure, âge osseux concordant.", "Puberté absente aux seuils, âge osseux retardé.", "Appeler familial un impubère de 14 ans."],
                ["Turner", "Fille sans sein à 13 ans.", "Caryotype 46,XX, qui ferme cette entité et aucune autre.", "Attendre une dysmorphie."],
                ["Insuffisance gonadique", "FSH élevée, stéroïde bas.", "Gonadotrophines basses, qui sont attendues chez le prépubère et ne prouvent rien seules.", "Rassurer un garçon dont les testicules ne grandissent jamais."],
                ["Déficit somatotrope", "Taille habituellement beaucoup plus basse, vitesse très faible.", "Vitesse souvent supérieure à 3,6 cm par an chez le garçon de ce retard, taille non sévère.", "Hormone de croissance le premier jour."],
            ],
        ),
        "Ce tableau assemble le dépliant, la revue déjà citée et la définition auxologique suisse. Il n'est pas une classification officielle unique d'une société suisse. Vous le dites.",
    ], e + ", " + j))
    o.append(sec("Calculs à refaire à voix haute, tous dérivés", [
        "Cible, mère 164 cm, père 178 cm. Somme 342. Garçon (342 + 13) / 2 = 177,5 cm, intervalle 169 à 186 cm. Fille (342 − 13) / 2 = 164,5 cm, intervalle 156 à 173 cm. Vous écrivez le signe avant de diviser.",
        "Parents 170 et 170, garçon : 176,5 cm, pas 178,5 cm. Fille : 163,5 cm. L'erreur imprimée sur la page familles est corrigée ici et signalée comme telle.",
        "Vitesse : 131,0 cm à 10,0 ans et 136,0 cm à 11,0 ans font 5,0 cm par an. Ce 5,0 cm rejoint l'ordre de grandeur « environ 5 cm par an à 10 ans » du PEZZ. Ce n'est pas une norme personnalisée.",
        "Vitesse piège : 131,0 cm puis 133,5 cm six mois plus tard. Différence 2,5 cm en 0,5 an, soit 5,0 cm par an. Annoncer 2,5 cm par an, c'est oublier de convertir les mois. Le PEZZ utilise précisément 2,5 cm comme différence attendue sur six mois quand l'année vaut 5 cm.",
        "Vous dites « calcul dérivé » à chaque fois. Aucun de ces résultats n'est une recommandation de traitement.",
        "Vous refusez de calculer un SDS de Cole sans la déviation standard parentale lue sur la courbe.",
    ], w + ", " + j))
    o.append(sec("Ce que vous écrivez dans le dossier, ligne par ligne", [
        "Heure de la mesure, taille de l'enfant, taille du père, taille de la mère, formule avec le signe, intervalle ± 8,5 cm, courbe utilisée et sa date de recommandation (depuis le 15 juin 2026 pour la taille).",
        "Stade : bourgeon palpable ou non, volume testiculaire comparé à l'orchidomètre, anosmie demandée, cryptorchidie demandée, signe neurologique absent ou présent.",
        "Examens demandés : âge osseux main et poignet gauches, TSH, thyroxine libre, gonadotrophines et stéroïde selon l'âge, caryotype si fille au seuil. Vous écrivez « en attente » plutôt que « normal » tant que le résultat n'est pas là.",
        "Phrase thérapeutique : aucun médicament signé, AIPS non ouverte, conseil proposé ou non, date de revue clinique choisie par vous et assumée, parce que le dépliant ne fixe pas un nombre de semaines.",
        "Vous n'écrivez pas « retard constitutionnel certain » le premier jour. Vous écrivez « compatible si les exclusions reviennent négatives ».",
        "Piège : un dossier qui dit « familial » sans un seul centimètre parental mesuré.",
    ], e + ", " + s))
    o.append(sec("Questions orales — réponses brèves que la relecture autorise", [
        "Pourquoi 13 et 14 ans, et pas l'inverse ? Le dépliant place le seuil féminin à 13 ans et le seuil masculin à 14 ans, après des débuts moyens à 10–11 et 12 ans.",
        "Pourquoi la main gauche ? C'est le cliché que le dépliant nomme pour comparer les espaces des os longs à l'âge civil.",
        "Le traitement habituel est-il une hormone ? Non. Habituellement aucun traitement n'est nécessaire. L'hormone n'accélère le calendrier que si une aide est requise, sans aller plus vite qu'en un à deux ans.",
        "La testostérone diminue-t-elle la taille adulte ? Le dépliant dit que non : elle change le moment du pic. Cela ne vous donne pas le milligramme.",
        "Peut-on citer 2 à 2,5 % ? Oui, comme phrase de la revue européenne déjà lue, pas comme registre suisse. La relecture du 25 octobre n'a pas rouvert cette revue.",
        "Peut-on citer 0,72 ? Oui, comme coefficient de la formule de Cole imprimée par le PEZZ, appliqué aux SDS, jamais aux centimètres, et jamais avec un SDS inventé.",
    ], e + ", " + w))
    o.append(sec("Ce qui resterait une faute même si le dossier est long", [
        "Signer 50 mg d'énanthate, ou un quart de patch de 25 µg, parce qu'une revue européenne les cite. Ces chiffres ne sont pas une AIPS lue.",
        "Oublier le caryotype d'une fille de 13 ans sans sein.",
        "Classer une céphalée avec vomissements en variante constitutionnelle.",
        "Recopier 178,5 cm pour deux parents de 170 cm. L'addition fait 176,5 cm.",
        "Jeter la courbe de vitesse zurichoise sous prétexte que « tout a changé le 15 juin 2026 ». Le communiqué la conserve.",
        "Annoncer une prévision de taille adulte au centimètre près. Le PEZZ raconte lui-même des écarts du type 180 cm prévus et 165 cm atteints, et l'ESPE refuse la garantie en cas de retard extrême.",
    ], e + ", " + w + ", " + s))
    return "".join(o)


def dx6():
    j, w, s, e = "[S304]", "[S303]", "[S302]", "[S306]"
    o = []
    o.append(sec("Petite taille familiale : appliquer la cible sans voler le tempo", [
        "Ce DX est le canal bas hérité, pas le réveil tardif de l'axe. La puberté arrive à l'heure et l'âge osseux ne retarde pas comme dans le retard constitutionnel du dépliant ESPE.",
        "Vous mesurez les parents avant de prononcer le mot familial. Paediatrica fait de cette mesure un acte médical. Une taille déclarée de mémoire ne crée pas de cible.",
        "Formule relue par le PEZZ et déjà lue dans Paediatrica : moyenne parentale ajustée de 13 cm selon le sexe, intervalle ± 8,5 cm. Vous gardez les deux.",
        "Le canal, après l'ajustement des deux premières années, doit rester stable. Un garçon au 50e percentile à 2 ans y reste jusque vers 12 ans si c'est son canal. Un canal bas stable, avec une cible basse, est le cœur de ce DX.",
        "Vous quittez ce DX si la puberté manque à 13 ans chez la fille ou à 14 ans chez le garçon, ou si l'âge osseux retarde d'au moins un an dans le sens du type 1.",
        "Piège : le père « a toujours été petit » remplace la toise et le stade de Tanner.",
    ], j + ", " + w + ", " + e))
    o.append(sec("Même arithmétique, autre décision", [
        "Parents 170 cm et 170 cm. Fille : 163,5 cm, calcul juste sur la page du PEZZ. Garçon : 176,5 cm. La page imprime 178,5 cm, qui ne vaut pas (183 + 170) / 2. Vous corrigez.",
        "Si cette fille mesure, en fin de croissance, 160 cm, elle est dans l'intervalle 163,5 ± 8,5, soit 155 à 172 cm. Le mot familial peut tenir si le canal a été stable et la puberté à l'heure.",
        "Si elle mesure 148 cm, elle est sous l'intervalle. Le patrimoine parental ne suffit plus. Vous reprenez la démarche, y compris cœliaquie et thyroïde, sans rester sur « la mère est moyenne ».",
        "Trois repères à tracer : cible de la mère corrigée selon le sexe, cible du père corrigée, moyenne. La page les propose parce qu'un enfant peut ressembler à l'un, à l'autre, ou au mélange, surtout quand les tailles parentales diffèrent.",
        "Vous ne multipliez pas ces centimètres par 0,72. Ce coefficient est celui des SDS dans la formule de Cole–Hermanussen. Sans SDS lus sur la courbe, vous n'écrivez pas de résultat.",
        "La formule simple est la moins fiable quand les parents sont très discordants ou très extrêmes, parce que les enfants régressent vers la moyenne. Vous le dites, sans inventer le nombre de centimètres de cette régression hors de la formule.",
    ], w + ", " + j))
    o.append(sec("Technique de mesure avant d'interpréter un canal", [
        "Jusqu'à 15 mm de moins en fin de journée, disques déshydratés. Vous comparez des mesures de la même heure.",
        "Talons au sol, deuxième personne chez le petit enfant, équerre ou livre vertical. Vous notez la méthode. Un changement de méthode, debout vers couché, fausse la vitesse.",
        "Erreur de 2 à 3 cm possible même au cabinet. À 10 ans, environ 5 cm par an, donc environ 2,5 cm en six mois. Une erreur égale à ce gain rend l'année illisible. Vous ne déclarez pas une cassure sur un seul intervalle bruité.",
        "Vous exigez au moins une mesure annuelle reportée, comme le PEZZ le demande, et plus rapprochée si les parents décrivent un changement de canal.",
        "La courbe de taille est celle que pédiatrie suisse recommande depuis le 15 juin 2026. La courbe de vitesse reste zurichoise. Vous ne les opposez pas.",
        "Sous le 3e percentile, soit −1,88 déviation standard dans le texte suisse de 2016, il y a petite taille statistique. Ce n'est pas, à soi seul, la petite taille familiale.",
    ], w + ", " + s + ", " + j))
    o.append(sec("Ce que vous ne traitez pas", [
        "Le cartilage répond. Rien n'est à corriger par un médicament dans la variante pure. L'hormone de croissance n'est pas le traitement d'une cible basse cohérente.",
        "Vous l'expliquez avec la physiologie du PEZZ : après deux ans, le canal hérité traduit un mécanisme intact, pas une hormone manquante.",
        "Vous ne promettez pas un gain en centimètres. Les sources lues n'en promettent pas pour cette variante.",
        "Surveillance : mesure au moins annuelle sur la courbe en vigueur. Retour plus tôt si une cassure est décrite. Pas d'hospitalisation.",
        "Sortie de la filière endocrinienne : canal stable, cible respectée, puberté à l'heure. Les examens de santé ordinaires continuent.",
        "Spécialité, dose, numéro Swissmedic : sans objet. Si quelqu'un demande malgré tout une hormone, la donnée AIPS est non trouvée et vous ne l'inventez pas.",
    ], w + ", " + j))
    o.append(sec("Station — fille toujours au 3e percentile depuis l'âge de 3 ans", [
        "Elle a 8 ans. Mère mesurée 152 cm, père mesuré 165 cm. Pas de sein, ce qui est attendu à 8 ans. Examen harmonieux.",
        "Cible fille : (152 + 165 − 13) / 2. Calcul dérivé : 152 + 165 = 317, 317 − 13 = 304, 304 / 2 = 152 cm. Intervalle environ 143,5 à 160,5 cm.",
        "Le canal est stable depuis 3 ans, donc après le deuxième anniversaire. Vous expliquez la cohérence. Vous ne demandez pas un test de stimulation.",
        "Vous revoyez chaque année. Vous reverrez le stade quand l'âge se rapprochera de 10–11 ans, début moyen féminin du dépliant, et vous n'attendrez pas 13 ans sans regarder si une cassure apparaît avant.",
        "Si à 13 ans le sein manque encore, vous quittez ce DX et vous ouvrez le retard, avec caryotype.",
        "Piège : traiter dès 8 ans parce que le percentile est bas, alors que la cible explique la position.",
    ], j + ", " + e))
    o.append(sec("Station — le canal casse après 4 ans", [
        "Garçon suivi au 10e percentile depuis l'âge de 2 ans, parents petits et mesurés, cible basse cohérente. À 9 ans il est passé sous le 3e percentile et la vitesse annuelle est nettement inférieure à l'ordre de 5 cm cité par le PEZZ pour un enfant de 10 ans.",
        "Le changement de canal après 2 ans est le signe que le PEZZ appelle suspect. Le mot familial ne tient plus, même si les parents sont petits.",
        "Vous cherchez une maladie acquise : digestive, thyroïdienne, chronique. Vous ne démarrez pas une hormone de croissance pour « rattraper la cible ».",
        "Vous vérifiez d'abord que les deux mesures sont comparables : même heure, même technique, écart supérieur à l'erreur de 2 à 3 cm.",
        "S'il s'agit d'une vraie cassure, la sérologie cœliaque et la TSH entrent dans le raisonnement des DX suivants, pas dans une variante familiale pure.",
        "Piège : « il reste dans la famille » alors qu'il a quitté son propre canal.",
    ], w))
    o.append(sec("Génétique et test : la page familles ne vous donne pas d'indication de routine", [
        "Environ 80 % de la variance de croissance, plusieurs gènes, variants courants expliquant environ 50 % des différences de taille adulte, information située à au moins quatre loci : phrases de la page familles, à citer comme telles.",
        "Un canal bas cohérent avec deux parents mesurés n'est pas, sur cette page, l'indication d'un test. Le test se discute surtout quand la petite taille est sévère et qu'un variant rare devient plus probable, sans seuil chiffré lu.",
        "Vous ne confondez pas ce conseil avec le panel d'hypogonadisme du retard constitutionnel. Ici l'axe pubertaire est à l'heure.",
        "Un résultat négatif ne prouverait pas la variante familiale, et un variant ne prédirait pas à lui seul la maladie. La page le dit pour le conseil en général.",
        "Vous expliquez aux parents que la taille se transmet de façon complexe, que les modèles se trompent aux extrêmes, et que la courbe répétée reste l'outil.",
        "Donnée non trouvée : rendement diagnostique suisse d'un exome dans la petite taille familiale pure.",
    ], w))
    o.append(sec("Questions qui séparent ce DX du retard constitutionnel", [
        table(
            ["Question", "Réponse qui garde ce DX", "Réponse qui l'abandonne"],
            [
                ["Les parents ont-ils été mesurés ?", "Oui, et la cible ± 8,5 cm contient l'enfant.", "Non, ou l'enfant est sous l'intervalle."],
                ["Le canal depuis l'âge de 2 ans ?", "Stable, même s'il est bas.", "Changement de canal."],
                ["La puberté ?", "À l'heure par rapport aux seuils de 13 et 14 ans.", "Seuil franchi sans signe."],
                ["L'âge osseux ?", "Concordant avec l'âge civil.", "Retard d'au moins un an, type 1."],
                ["La vitesse ?", "Elle prolonge le canal, au-delà du bruit de mesure.", "Chute franche, surtout sous le profil de 3,6 cm par an chez un garçon que l'on croyait seulement familial."],
            ],
        ),
        "Vous posez les cinq questions dans cet ordre. Le médicament n'arrive pas avant.",
    ], j + ", " + e + ", " + w))
    return "".join(o)


def dx7():
    g = "[S307]"
    o = []
    o.append(sec("Pourquoi la croissance amène à la guideline 2020", [
        "La guideline ESPGHAN 2020, JPGN, DOI 10.1097/MPG.0000000000002497, relue le 25.10.2026, dit que les symptômes classiques de malabsorption — cassure staturo-pondérale, perte de poids, diarrhée chronique — sont les plus spécifiques. La petite taille et le retard pubertaire figurent dans son tableau 2 des signes qui font envisager le diagnostic.",
        "Le tableau 2 liste aussi, côté digestif, la diarrhée chronique ou intermittente, la constipation chronique qui ne répond pas au traitement usuel, la douleur abdominale chronique, l'abdomen distendu, les nausées et vomissements répétés.",
        "Côté extradigestif, il ajoute l'irritabilité et la fatigue chronique, la neuropathie, l'arthrite ou les arthralgies, l'anémie ferriprive chronique, la baisse de minéralisation osseuse et les fractures répétées, les aphtes récidivants, le rash de type dermatite herpétiforme, les défauts de l'émail, et une biologie hépatique anormale.",
        "Les situations particulières du même tableau comprennent les apparentés au premier degré, le diabète de type 1, la maladie thyroïdienne autoimmune, la maladie hépatique autoimmune, la trisomie 21, le syndrome de Turner, le syndrome de Williams–Beuren et le déficit en IgA.",
        "Vous testez donc une cassure de croissance dans ce cadre, et vous pensez au Turner déjà exclu par le caryotype dans le DX du retard pubertaire : la guideline le remet dans les situations à tester, sans que le dépliant ESPE ne l'ait chiffré.",
        "Les symptômes contribuent peu à la précision diagnostique, dit le résumé. Vous ne exigez pas la diarrhée pour demander la sérologie, et vous ne posez pas le diagnostic sur la seule petite taille.",
    ], g))
    o.append(sec("Ce que les études citées par la guideline vous permettent de dire", [
        "Dans la cohorte ProCeDE d'enfants diagnostiqués sur des symptômes, l'anémie ferriprive est rapportée chez 17 %. Vous pouvez citer 17 % avec cette source. Vous ne dites pas que 17 % des petites tailles suisses sont cœliaques.",
        "Une revue de dossiers de 165 enfants malades trouve la douleur abdominale dans 52,7 % des présentations et la constipation dans 38,9 %. Une étude cas-témoins trouve une sérologie positive chez 1,1 % des douleurs abdominales et 1,2 % des témoins, sans biopsie. La douleur abdominale isolée n'est donc pas, dans ce fragment, un argument fort.",
        "La guideline dit qu'il y a des arguments pour un risque accru en cas de symptômes de type intestin irritable à prédominance diarrhéique, d'anémie ferriprive, de constipation chronique et de défauts de l'émail. Pour la douleur, la dyspepsie et le ballonnement, elle juge les arguments insuffisants.",
        "Vous hiérarchisez ainsi l'anamnèse d'un enfant qui ne grandit plus : diarrhée, constipation rebelle, anémie, aphtes et émail passent avant une douleur abdominale vague.",
        "La prévalence suisse de la maladie cœliaque chez l'enfant avec cassure staturale n'est pas dans les pages lues : donnée non trouvée.",
        "Piège : rassurer parce qu'il n'y a pas de diarrhée, alors que le tableau 2 inclut la petite taille et l'anémie sans exiger le syndrome classique complet.",
    ], g))
    o.append(sec("Premier prélèvement : IgA totale et TGA-IgA, enfant qui mange du gluten", [
        "Si la maladie est suspectée, la combinaison IgA totale et anticorps IgA anti-transglutaminase 2 est supérieure aux autres combinaisons, plus exacte et plus efficiente. Vous ne commencez pas par les anticorps anti-peptides de gliadine déamidés : la guideline le déconseille pour le test initial.",
        "L'enfant doit consommer des quantités habituelles de gluten. Une sérologie faite après un régime déjà lancé peut être faussement négative. Vous le demandez aux parents avant le tube.",
        "Si l'IgA est normale pour l'âge, la TGA-IgA sert quel que soit l'âge. Si l'IgA est basse pour l'âge, ou inférieure à 0,2 g/L après 3 ans, vous passez à un test IgG (DGP, EMA ou TGA). Vous ne concluez pas « sérologie négative » sur une TGA-IgA seule chez un enfant déficitaire en IgA.",
        "Tout résultat positif va chez un gastroentérologue pédiatre ou un spécialiste de la maladie. Le médecin de premier recours ne clôt pas seul le diagnostic.",
        "Les anticorps antigliadine IgG et IgA ne sont pas recommandés pour le dépistage initial en pratique clinique.",
        "Piège : régime sans gluten « d'essai » pendant trois semaines avant la prise de sang, puis sérologie négative interprétée comme une exclusion.",
    ], g))
    o.append(sec("Sans biopsie : les conditions exactes, pas un titre isolé", [
        "La voie sans biopsie peut s'appliquer si la TGA-IgA atteint au moins 10 fois la limite supérieure de la normale, si la famille est d'accord, et si les anticorps anti-endomysium IgA sont positifs sur un second prélèvement.",
        "Le typage HLA DQ2/DQ8 et la présence de symptômes ne sont pas des critères obligatoires de cette voie. C'est le changement par rapport à 2012, où le HLA faisait partie de ce que des publications appelaient un triple test. La guideline dit que ce mot laissait croire, à tort, que les trois tests sortaient d'un seul tube.",
        "Le test doit calculer le titre sur une courbe de calibration, et la valeur 10 fois la normale doit être à l'intérieur de sa plage de mesure. Un titre « haut » sur un kit qui ne mesure pas jusque-là ne suffit pas.",
        "La valeur prédictive positive attendue pour omettre la biopsie est discutée dans la guideline au-delà de 95 % pour ce seuil. Vous ne descendez pas le seuil à 7 fois ou à 5 fois : la question est posée dans le texte, et la recommandation garde 10 fois.",
        "L'enfant asymptomatique peut, recommandation conditionnelle, être diagnostiqué sans biopsie avec les mêmes critères, après décision partagée avec les parents et, s'il y a lieu, avec l'enfant. La petite taille isolée n'est pas un passe-droit pour sauter une condition.",
        "Tous les patients déficitaires en IgA et positifs en test IgG doivent être biopsiés. On n'omet pas la biopsie dans ce cas. Le seuil de 10 fois n'est pas validé pour la TGA-IgG.",
    ], g))
    o.append(sec("Avec biopsie : où, combien, et comment lire", [
        "Si la TGA-IgA est positive mais inférieure à 10 fois la normale, vous faites des biopsies pour limiter le faux positif : au moins quatre au duodénum distal et au moins une au bulbe, sous régime contenant du gluten.",
        "L'orientation du fragment est critique. Une étude d'accord inter-observateur en pédiatrie, citée par la guideline, ne juge optimale l'orientation que d'environ la moitié des biopsies. Le kappa pour le diagnostic de maladie cœliaque atteint 0,84 quand on s'en tient à ce diagnostic, mais l'accord sur le grade de Marsh–Oberhuber est mauvais.",
        "Dans l'étude de Werkstetter citée, le désaccord sur le fait qu'il y ait ou non une maladie est de 7 %, et le désaccord tous grades confondus (Marsh 0, 1, 2, 3a, 3b, 3c) atteint 58 %. Certains pathologistes concluent malgré une biopsie de mauvaise qualité au lieu d'en redemander une.",
        "Un rapport villosités sur cryptes inférieur à 2 sur une partie d'au moins une biopsie duodénale est considéré en accord avec la maladie, si l'orientation permet la morphométrie. Le grade de Marsh ne se donne pas sans cette orientation.",
        "La légende de figure de la guideline place le seuil des lymphocytes intra-épithéliaux à plus de 25 pour 100 entérocytes. Vous ne transformez pas un compte isolé en diagnostic si l'architecture est normale : Marsh 1 ne suffit pas à poser la maladie.",
        "Résultats discordants entre TGA-IgA et histologie : recoupe des biopsies et second avis d'un pathologiste expérimenté. Vous ne tranchez pas au téléphone sur un compte-rendu ambigu.",
    ], g))
    o.append(sec("HLA : utile pour exclure, inutile pour confirmer la voie sans biopsie", [
        "Si les autres critères sont remplis, le HLA n'ajoute pas à la certitude. Werkstetter et coll. décrivent 645 enfants avec TGA-IgA positive et maladie prouvée par biopsie ; 399 avaient un titre supérieur à 10 fois, des EMA positifs et des lésions Marsh 2 ou 3, et tous les 399 étaient DQ2 et/ou DQ8. Wolf et coll. décrivent 409 malades au-dessus de 10 fois avec EMA et biopsie ; le HLA, disponible chez 227, était positif chez tous.",
        "Une population australasienne de 356 malades était DQ2/DQ8 positive à 99,6 %. Des publications plus anciennes allaient jusqu'à 5 % de malades dits HLA négatifs : méthode de typage, groupes trop hétérogènes, et histologie faussement positive entrent dans l'explication. La variabilité inter-observateur histologique est citée entre 5 et 7 % selon le passage.",
        "Les tests SNP reconnaissent les variants fréquents DQ2.5, DQ8, DQ2.2 et DQ7.5. Les allèles rares demandent un typage plus profond. Un HLA négatif mal fait n'exclut donc pas aussi bien qu'un typage complet.",
        "Règle à dire : HLA négatif, risque très faible, maladie peu probable. HLA positif, vous n'avez rien confirmé. Vous ne demandez pas le HLA pour « verrouiller » un dossier qui a déjà 10 fois la normale et un second EMA positif.",
        "Vous pouvez le demander dans d'autres circonstances, par exemple pour rassurer un apparenté ou pour éviter des sérologies répétées si le risque génétique est absent. La guideline le permet sans le rendre obligatoire.",
        "Piège : exiger le triple test 2012 alors que la version 2020 a retiré cette obligation.",
    ], g))
    o.append(sec("Maladie potentielle : Marsh 0 ou I, vous ne banalisez pas et vous ne diagnostiquez pas trop vite", [
        "Des lésions absentes ou légères (Marsh 0 ou I) avec une auto-immunité confirmée, TGA-IgA ou EMA-IgA positive, demandent un suivi rapproché. La guideline le dit dans le résumé.",
        "Marsh 1 n'est pas suffisant pour diagnostiquer. Certaines observations suggèrent que ces formes évoluent plus souvent vers l'atrophie que Marsh 0. Il n'y a pas d'étude spécifique comparant le devenir à long terme de Marsh 0 contre Marsh 1, et la guideline le reconnaît.",
        "Une muqueuse faussement « potentielle » peut venir d'un gluten déjà réduit, d'un échantillonnage insuffisant ou d'une mauvaise orientation. Vous vérifiez le régime des semaines précédentes avant d'accepter l'étiquette.",
        "Le régime sans gluten à vie est la conséquence d'un diagnostic posé avec ou sans biopsie selon les règles. La guideline demande de dire que réévaluer après coup imposerait une réexposition prolongée au gluten et de nouveaux examens. Vous ne lancez donc pas le régime avant d'avoir fermé la démarche.",
        "La dose de gluten de réexposition, le protocole suisse de provocation et les produits sans gluten remboursés : donnée non trouvée dans les pages lues. Vous n'inventez pas de grammes.",
        "Piège : dire à la famille « ce n'est pas la maladie » devant Marsh 1 et des anticorps positifs, ou au contraire démarrer le régime le jour du premier titre faiblement positif.",
    ], g))
    o.append(sec("Station — cassure staturale sans diarrhée", [
        "Garçon de 7 ans, canal stable au 25e percentile jusqu'à 5 ans, puis perte de canal, fatigue, une anémie ferriprive. Pas de diarrhée. Les parents sont de taille moyenne mesurée : la cible ne explique pas la cassure.",
        "Le tableau 2 vous autorise à chercher la maladie devant la cassure, le retard de croissance et l'anémie, sans attendre la diarrhée. La ProCeDE rappelle que l'anémie ferriprive accompagne 17 % des diagnostics symptomatiques.",
        "Vous vérifiez qu'il mange du pain et des pâtes. Vous demandez IgA totale et TGA-IgA. Vous ne commencez pas un régime.",
        "Si le titre dépasse 10 fois la normale sur un test qui mesure cette zone, vous adressez, vous expliquez la voie possible sans biopsie, et vous attendez l'EMA sur un second tube et l'accord des parents. Vous ne posez pas le diagnostic sur le premier tube seul.",
        "Si le titre est positif mais plus bas, vous adressez pour au moins quatre biopsies distales et une biopsie du bulbe. Vous ne multipliez pas les kits dans l'intervalle.",
        "La croissance est le motif. Le traitement de la croissance est celui de la maladie, discuté par le spécialiste, pas une hormone de croissance décidée ce jour.",
    ], g))
    o.append(sec("Station — fille déjà suivie pour un retard pubertaire", [
        "Le caryotype est demandé à 13 ans sans sein, par le dépliant ESPE. S'il revient 45,X ou une forme de Turner, la guideline 2020 place ce syndrome parmi les situations où la sérologie cœliaque se discute, au même titre que la thyroïdite autoimmune.",
        "Vous ne mélangez pas les deux démarches. Le caryotype cherche le Turner. La sérologie cherche une maladie qui peut, en plus, freiner la croissance. L'une ne remplace pas l'autre.",
        "Un canal qui casse chez une fille au caryotype normal reste une indication de penser au tableau 2, surtout s'il existe une anémie, des aphtes ou une constipation rebelle.",
        "Vous n'attribuez pas toute petite taille de fille au Turner, ni toute cassure à la cœliaquie. Vous faites le test qui tranche et vous lisez le résultat.",
        "Donnée non trouvée : prévalence suisse de la maladie cœliaque dans le Turner. Vous n'inventez pas un pourcentage local.",
        "Piège : un seul diagnostic pour deux mécanismes. Les deux peuvent coexister, et la guideline a prévu la situation.",
    ], g + ", [S306]"))
    o.append(sec("Ce que vous dites aux parents le jour du prélèvement", [
        "Vous expliquez que le sang ne sert que si l'enfant mange encore du gluten. Vous expliquez qu'un titre très haut peut, avec un second test et leur accord, éviter la biopsie, et qu'un titre moins haut la rend nécessaire.",
        "Vous expliquez que le typage génétique n'est pas obligatoire pour confirmer, et qu'un typage positif ne prouve rien.",
        "Vous expliquez qu'un diagnostic retenu, avec ou sans biopsie, implique un régime sans gluten à vie, et qu'il ne faut pas commencer ce régime pour « voir » avant la confirmation.",
        "Vous ne promettez pas un nombre de centimètres rattrapés après le régime. Les pages lues ne donnent pas ce rattrapage chiffré.",
        "Vous ne donnez pas de marque de produit sans gluten ni de montant d'assurance. Donnée non trouvée.",
        "Vous fixez qui rappellera le résultat et qui adressera au gastroentérologue pédiatre. Le premier recours garde la courbe.",
    ], g))
    o.append(sec("Erreurs d'examen que la guideline 2020 rend visibles", [
        "Exiger des symptômes pour la voie sans biopsie. La version 2020 dit que les symptômes ne sont pas obligatoires.",
        "Omettre la biopsie à 6 fois la normale parce que « c'est déjà haut ». Le seuil écrit est 10 fois, sur un test capable de le mesurer.",
        "Omettre la biopsie chez un enfant déficitaire en IgA. C'est explicitement déconseillé.",
        "Compter un seul prélèvement EMA fait le même jour que la TGA. Il faut un second échantillon.",
        "Accepter un Marsh 1 comme preuve, ou jeter un Marsh 1 avec anticorps positifs sans suivi.",
        "Citer un pourcentage suisse de prévalence. Il n'est pas dans les pages ouvertes.",
    ], g))
    return "".join(o)


def dx8():
    t = "[S401]"
    o = []
    o.append(sec("Fiche lausannoise relue : ce qu'elle ajoute au signe statural", [
        "Pedlaus, fiche d'enseignement de la Faculté de biologie et de médecine de Lausanne, relue le 25.10.2026, dit qu'un enfant d'âge scolaire sur 500 peut présenter une hypothyroïdie acquise. Vous citez 1/500 avec cette source. Vous ne le convertissez pas en incidence OFS.",
        "La qualité de vie pendant la phase d'hypothyroïdie est clairement diminuée, surtout par la limitation des activités habituelles et la labilité émotionnelle, avec une perception globale de mauvaise santé. La plainte n'est donc pas seulement une taille.",
        "Signes écrits : intolérance au froid, constipation, retard de croissance avec prise de poids, goitre, baisse de l'attention en classe, moindre croissance des os longs avec baisse du rapport segment supérieur sur segment inférieur, cheveux secs et cassants qui tombent.",
        "La puberté retardée est fréquente. Une puberté avancée peut aussi se voir. Vous ne classez donc pas toute puberté tardive en retard constitutionnel, ni toute puberté précoce en variante, sans avoir dosé la thyroïde.",
        "La cause la plus fréquente est la thyroïdite auto-immune de Hashimoto. Vous la cherchez. Vous ne la posez pas sur le seul goitre.",
        "Cette fiche n'est pas l'information professionnelle Swissmedic. Tout chiffre de dose qu'elle contient reste un chiffre d'enseignement, non prescrit ici.",
    ], t))
    o.append(sec("Causes rares : vous les nommez pour ne pas les inventer ensuite", [
        "Kyste du tractus thyréoglosse, avec des cas familiaux décrits. Hypothyroïdie malformative, par exemple une hémithyroïde. Excès d'iode. Lithium, amiodarone, radioiode.",
        "Un hémangiome hépatique peut augmenter l'activité de la désiodase de type 3, qui convertit la T4 en T3 reverse et la T3 en T2. Vous y pensez chez le nourrisson avec un gros foie vasculaire et une thyroïde périphérique basse, pas chez l'adolescent ordinaire.",
        "Une augmentation de la TBG sous œstrogène ou pendant la grossesse diminue la biodisponibilité apparente. Le dosage de TBG est rarement nécessaire, dit la fiche, de même que la T3 libre.",
        "L'absence de TSH par atteinte hypophysaire ou hypothalamique est rare. Elle se reconnaît à une TSH basse ou inappropriée avec une thyroxine libre basse, et elle ouvre l'IRM et la recherche d'autres déficits, pas l'échographie seule.",
        "Vous interrogez donc sur le lithium, l'amiodarone, l'iode et un traitement par radioiode avant d'appeler Hashimoto toute hypothyroïdie.",
        "Donnée non trouvée sur cette fiche : incidence suisse de chacune de ces causes rares.",
    ], t))
    o.append(sec("Biologie et imagerie : deux chemins, pas un bilan unique", [
        "Vous examinez la loge thyroïdienne, puis vous dosez TSH et thyroxine libre. Les anticorps anti-TPO et anti-thyroglobuline se demandent si une thyroïdite est suspectée.",
        "Hypothyroïdie primaire : thyroxine libre basse, TSH haute. L'échographie cervicale, de la loge, cherche une malformation, un nodule, un kyste ou une infiltration immune.",
        "Hypothyroïdie centrale : TSH et thyroxine libre basses. L'IRM hypothalamo-hypophysaire et les autres axes sont indiqués. L'échographie ne répond pas à cette question.",
        "T3 libre et TBG : très rarement. Vous ne les ajoutez pas pour faire complet.",
        "Vous ne traitez pas un goitre sans avoir vu TSH et thyroxine libre. La fiche sépare l'observation possible de certains Hashimoto et le traitement de l'hypothyroïdie ou du goitre.",
        "Piège : une TSH seule, sans thyroxine libre, puis une dose décidée sur un chiffre isolé.",
    ], t))
    o.append(sec("Lévothyroxine : ce que la fiche affirme, et ce que vous ne signez pas", [
        "Toute hypothyroïdie est traitée par substitution en lévothyroxine, écrit la fiche. Dans le Hashimoto, le traitement est indiqué si hypothyroïdie et/ou goitre. Dans certains cas, l'observation seule suffit. Le traitement combat les symptômes et ne guérit pas la maladie.",
        "La fiche écrit des doses de 1,5 à 2 µg par kilogramme et par jour. Vous lisez cette plage comme un contenu d'enseignement lausannois. Vous ne la recopiez pas sur une ordonnance : l'AIPS suisse n'a pas été ouverte, la spécialité ® n'a pas été choisie, le numéro Swissmedic n'a pas été lu.",
        "Le but écrit est de normaliser la TSH et la thyroxine libre et de corriger les signes cliniques. Le calendrier en semaines n'est pas sur la fiche. Vous ne l'inventez pas. Vous suivez la courbe pour voir le cartilage répondre, sans promettre un nombre de centimètres.",
        "Un surdosage peut induire une hyperthyroïdie. Vous le dites au patient et aux parents. Les signes de ce surdosage à enseigner selon l'AIPS : donnée non trouvée ici.",
        "Grossesse : une hypothyroïdie non traitée chez la femme enceinte peut nuire au développement neuronal du fœtus. Pour une adolescente, vous ne démarrez pas une substitution sans avoir écarté une grossesse si le contexte l'exige, et le libellé suisse de cette précaution n'a pas été lu dans une AIPS.",
        "Insuffisance rénale, hépatique, sujet âgé : sans adaptation chiffrée sur cette fiche. Vous n'inventez pas de palier.",
    ], t))
    o.append(sec("Complications que vous citez sans les amplifier", [
        "Non traitée, l'hypothyroïdie est associée à une baisse de qualité de vie à long terme, à un retard de croissance et de développement, à une baisse des réflexes, de la mémoire et de la force, et à des problèmes sociaux.",
        "Atrophie et fibrose progressives. Association à d'autres maladies auto-immunes spécifiques. Vous reliez cela à la guideline cœliaque, qui place la maladie thyroïdienne autoimmune parmi les situations où la sérologie cœliaque se discute.",
        "L'encéphalopathie de Hashimoto est qualifiée de très rare. La fiche renvoie à une publication où seulement 32 % des patients avaient des signes de maladie thyroïdienne au moment du diagnostic de cette encéphalopathie. Vous ne cherchez pas cette encéphalopathie devant une simple cassure staturale. Vous ne l'excluez pas non plus par une TSH normale si le tableau neurologique est celui d'une encéphalopathie, cas hors de ce DX courant.",
        "La référence unique affichée sur la fiche pédagogique ne remplace pas une recommandation de société suisse sur le rythme de contrôle. Donnée non trouvée pour un intervalle officiel en semaines.",
        "Vous surveillez jusqu'à la correction des signes et la normalisation de la TSH et de la thyroxine libre, but de la fiche, puis vous gardez un suivi parce que la maladie autoimmune ne guérit pas sous hormone.",
        "Piège : arrêter la lévothyroxine quand la taille reprend, comme si le cartilage guéri fermait la thyroïdite.",
    ], t))
    o.append(sec("Lien avec la puberté : retard fréquent, avance possible, os en retard si les deux coexistent", [
        "Pedlaus : puberté retardée fréquente, puberté avancée possible. Le chapitre espagnol de puberté précoce, lu pour le DX.10, place l'hypothyroïdie (syndrome de Van Wyk–Grumbach) parmi les causes de puberté précoce centrale, et il fait de l'âge osseux retardé l'exception quand une puberté précoce s'associe à une hypothyroïdie.",
        "Vous dosez donc TSH et thyroxine libre devant une puberté trop tôt ou trop tard si la croissance ne colle pas au tempo simple, et devant toute cassure avec prise de poids.",
        "Un âge osseux retardé n'écarte pas une puberté précoce si la thyroïde est basse. C'est l'exception écrite par le chapitre espagnol à la règle d'un âge osseux avancé de plus de 2 déviations standards.",
        "Vous ne traitez pas cette puberté par un analogue tant que l'hypothyroïdie n'est pas reconnue. La substitution est le traitement de la cause thyroïdienne. L'analogue n'est pas le sujet de la fiche, et sa dose AIPS n'est pas lue.",
        "Le rapport des segments, diminué parce que les os longs grandissent moins, se cherche à l'examen. Vous le décrivez. Vous n'inventez pas un chiffre seuil du rapport : la fiche n'en donne pas.",
        "Piège : âge osseux retardé égal automatiquement retard constitutionnel, chez un enfant frileux qui prend du poids.",
    ], t + ", [S404]"))
    o.append(sec("Station — garçon de 11 ans qui ralentit et prend du poids", [
        "Il était sur son canal. Depuis un an, la vitesse tombe et le poids monte. Il a froid, il est constipé, l'école parle d'attention. La thyroïde est palpable.",
        "Vous dosez TSH et thyroxine libre avant toute hormone de croissance et avant d'appeler le père en cause. Si la thyroxine libre est basse et la TSH haute, vous êtes dans l'hypothyroïdie primaire de la fiche.",
        "Vous demandez alors les anticorps si la thyroïdite est suspectée, et l'échographie de la loge. Vous n'envoyez pas d'IRM d'emblée : l'IRM est le chemin de la forme centrale.",
        "Vous expliquez que le traitement substitutif, une fois l'AIPS lue par celui qui prescrit, vise la biologie et les signes, et qu'il ne guérit pas un Hashimoto. Vous n'écrivez pas 1,5 à 2 µg/kg sur l'ordonnance de cette session.",
        "Vous reportez la taille sur la courbe recommandée depuis le 15 juin 2026 pour voir la réponse. Vous ne promettez pas les centimètres.",
        "Vous pensez à la sérologie cœliaque si d'autres signes du tableau 2 existent, sans la rendre automatique par la seule fiche thyroïdienne.",
    ], t))
    o.append(sec("Ce que vous répondez si l'on vous tend la fiche comme une AIPS", [
        "Vous reconnaissez la fiche, son 1/500, ses signes, son Hashimoto, sa séparation primaire contre centrale, et son but biologique.",
        "Vous refusez d'y lire une spécialité, un numéro à cinq chiffres, une adaptation rénale ou un schéma de comprimés.",
        "Vous dites que 1,5 à 2 µg/kg/jour est la plage écrite par l'enseignement lausannois, et que la prescrire sans AIPS contredit la règle de ce dossier.",
        "Vous dites que l'observation seule existe dans certains Hashimoto, sans seuil chiffré supplémentaire sur la fiche. Vous recontrôlez plutôt que d'inventer le seuil.",
        "Vous dites que le surdosage rend hyperthyroïdien, donc qu'un suivi biologique fait partie du traitement, même si l'intervalle exact n'est pas écrit.",
        "Piège de copie : « la dose suisse est 2 µg/kg ». La phrase juste est « la fiche d'enseignement écrit 1,5 à 2 µg/kg/jour ; l'AIPS n'a pas été ouverte ».",
    ], t))
    return "".join(o)


def dx9():
    a, b = "[S402]", "[S403]"
    o = []
    o.append(sec("Ce que la synthèse Cochrane CD009471 chiffre vraiment", [
        "La revue de Zhang, Prietsch et Ducharme, recherche jusqu'en janvier 2014, publiée le 17 juillet 2014, a été relue le 25.10.2026 sur la page Cochrane. Elle inclut 25 essais, 8471 enfants asthmatiques persistants légers à modérés, dont 5128 sous corticoïde inhalé et 3343 sous placebo ou médicament non stéroïdien.",
        "La vitesse linéaire baisse en moyenne de 0,48 cm par an la première année (14 essais, 5717 participants, intervalle de confiance à 95 % de −0,65 à −0,30, certitude modérée). Le changement de taille depuis la ligne de base baisse de 0,61 cm par an (15 essais, 3275 participants, intervalle −0,83 à −0,38, certitude modérée).",
        "Six molécules sont dans les essais : dipropionate de béclométasone, budésonide, ciclésonide, flunisolide, propionate de fluticasone, furoate de mométasone, à doses faibles ou moyennes, sur trois mois à quatre–six ans. Vous nommez la classe. Vous ne choisissez pas une marque suisse : aucune AIPS n'a été ouverte.",
        "L'effet dépend de la molécule : la différence entre les six molécules sur la vitesse à un an est significative (chi-deux 26,1, 5 degrés de liberté). Elle persiste même quand on se limite aux doses équivalentes à 200 µg par jour de béclométasone HFA. Ce 200 µg est une équivalence d'essai, pas une posologie suisse à recopier.",
        "Les sous-groupes ne montrent pas d'effet significatif de la dose faible contre moyenne, du dispositif ou de l'âge sur l'ampleur de la baisse de vitesse à un an. La revue demande malgré cela des comparaisons directes avant de conclure que la dose et le dispositif ne comptent pas.",
        "Vous dites à la famille : en moyenne un demi-centimètre par an en moins la première année, pas la perte garantie de cet enfant. L'intervalle individuel n'est pas une fourchette à appliquer tel quel à un patient.",
    ], a))
    o.append(sec("Années suivantes et taille adulte : le ralentissement n'est pas une soustraction infinie", [
        "La deuxième année, cinq essais et 3174 participants, la différence de vitesse est de −0,19 cm par an, intervalle −0,48 à 0,11, p = 0,22. La revue ne retient pas de différence significative cette année-là.",
        "La troisième année, un essai de 667 participants montre 5,34 cm par an sous budésonide et 5,34 cm par an sous placebo. Un autre essai, 1974 participants, montre encore −0,33 cm par an sous budésonide, intervalle −0,52 à −0,14.",
        "Après l'arrêt, quatre essais parlent de la croissance. Trois ne décrivent pas de rattrapage significatif deux à quatre mois après l'arrêt. Un essai montre une vitesse accélérée sous fluticasone douze mois après l'arrêt, mais il reste 0,7 cm d'écart avec le placebo à la fin d'un essai de trois ans.",
        "Un essai suivi jusqu'à l'âge adulte : enfants prépubères, budésonide 400 µg par jour pendant en moyenne 4,3 ans, réduction moyenne de la taille adulte de 1,20 cm, intervalle −1,90 à −0,50, par rapport au placebo. Ce 400 µg est l'exposition de l'essai. Vous ne le prescrivez pas comme dose suisse.",
        "La revue conclut que l'effet est maximal la première année, moindre ensuite, et petit au regard du bénéfice connu sur le contrôle de l'asthme. L'asthme non contrôlé, rappelle la revue sœur, freine aussi la croissance.",
        "Vous ne promettez pas un retour au millimètre près après la baisse de dose. Vous ne dramatisez pas non plus 0,48 cm par an en une perte cumulée de plusieurs centimètres par année de traitement : les années suivantes ne reproduisent pas le chiffre de la première.",
    ], a))
    o.append(sec("Molécules et dispositifs : CD010126, certitude limitée", [
        "La revue d'Axelsson, Naumburg, Prietsch et Zhang, recherche mise à jour jusqu'en avril 2019, page Cochrane relue le 25.10.2026, compare des molécules entre elles ou des dispositifs entre eux, au moins trois mois, enfants de 4 à 12 ans, asthme persistant léger à modéré.",
        "Six essais, 1199 enfants, 1008 dans l'analyse selon le protocole. Quatre essais comparent la fluticasone à la béclométasone ou au budésonide. Deux comparent des dispositifs. Quatre sont multicentriques et financés par l'industrie du produit ou du dispositif. La revue ne couvre pas les autres molécules ni les associations avec un bêta-2 de longue durée : vous ne généralisez pas.",
        "Un essai de 23 participants : fluticasone contre béclométasone à dose équivalente, différence de vitesse +0,81 cm par an pour la fluticasone, intervalle 0,46 à 1,16, certitude basse.",
        "Fluticasone contre budésonide : sur le changement de taille, deux essais et 359 participants, différence 0,97 cm en faveur de la fluticasone, intervalle 0,62 à 1,32, certitude modérée, horizons de 20 semaines à 12 mois. Sur la vitesse, deux essais et 236 participants, différence 0,39 cm par an, intervalle −0,94 à 1,73, certitude très basse, non significative.",
        "Dispositifs : béclométasone HFA en aérosol à demi-dose contre CFC à dose équivalente, 212 participants, différence de vitesse −0,44 cm par an, intervalle −1,00 à 0,12, certitude basse. Budésonide Easyhaler contre la même dose en Turbuhaler, 229 participants, sur six mois, +0,37 cm pour Easyhaler, intervalle 0,12 à 0,62, certitude basse.",
        "La revue dit que ces données ne suffisent pas à choisir la molécule ou le dispositif pour un enfant. La peur de l'effet statural fait abandonner l'inhalateur, l'asthme se décontrôle, et l'asthme non contrôlé freine lui aussi la croissance, avec une morbidité et une mortalité que la revue rappelle. Vous parlez de cela avant de parler du demi-centimètre.",
    ], b))
    o.append(sec("Mécanisme déjà lu, appliqué à la décision", [
        "Le produit absorbé diminue la sécrétion pulsatile d'hormone de croissance, réduit le récepteur au cartilage et au foie, réduit l'IGF-1 et son activité. Les chondrocytes prolifèrent moins et entrent davantage en apoptose. L'os long grandit plus lentement.",
        "Vous corrigez l'exposition : dose la plus faible qui contrôle, technique d'inhalation, molécule discutée sans transformer la revue en ordonnance. Vous ne corrigez pas l'IGF-1 par un médicament absent de ces revues, et vous ne compensez pas d'emblée par une hormone de croissance.",
        "Vous mesurez surtout la première année, là où l'effet moyen est le plus grand. Vous continuez ensuite, parce qu'un essai de troisième année montre encore un écart et qu'un suivi adulte montre 1,20 cm en moyenne dans les conditions citées.",
        "Un ralentissement massif, des vergetures, une prise de poids rapide ou une hypertension dépassent l'effet moyen des essais. Vous cherchez une autre cause du SSP, dont l'hypothyroïdie et la cœliaquie, et vous discutez un hypercorticisme. Le protocole suisse du freinage à la dexaméthasone n'a pas été lu.",
        "Vous additionnez les voies : inhalée, nasale, orale, cutanée. Le piège est l'inhalateur « local » oublié, ou la crème forte oubliée.",
        "La fréquence suisse de cet effet n'est pas dans les revues. Vous ne l'inventez pas.",
    ], a + ", " + b))
    o.append(sec("Station — premier hiver sous corticoïde inhalé", [
        "Fille de 8 ans, asthme persistant, corticoïde inhalé quotidien depuis dix mois, canal auparavant stable. Les parents ont lu « les corticoïdes empêchent de grandir » et veulent tout arrêter avant l'hiver.",
        "Vous mesurez avec la même technique, vous calculez la vitesse, vous la situez par rapport à environ 5 cm par an à 10 ans selon l'ordre de grandeur du PEZZ, en sachant qu'elle a 8 ans et que ce chiffre n'est pas sa norme. Vous cherchez une cassure franche, pas un écart d'un demi-centimètre confondu avec l'erreur de toise.",
        "Vous expliquez 0,48 cm par an en moyenne la première année, l'intervalle de confiance, et le fait que ce n'est pas la perte de leur enfant. Vous expliquez que l'arrêt expose à un asthme non contrôlé, qui freine aussi la croissance.",
        "Vous vérifiez la technique et la dose réellement prise. Vous n'écrivez ni marque ni microgramme suisse. Vous adressez au prescripteur de l'asthme pour la plus petite dose efficace.",
        "Vous ne demandez pas un test de stimulation de l'hormone de croissance pour un écart compatible avec l'effet moyen. Vous le discutez si la vitesse s'effondre bien au-delà.",
        "Vous revoyez la taille, surtout pendant cette première année, puis vous gardez une mesure annuelle.",
    ], a + ", [S303]"))
    o.append(sec("Station — l'écart dépasse le demi-centimètre", [
        "Garçon de 11 ans, plusieurs corticoïdes inhalés et un dermocorticoïde fort, vitesse annuelle tombée de plusieurs centimètres sous son canal, prise de poids, vergetures.",
        "L'effet moyen de 0,48 cm par an ne décrit plus le tableau. Vous listez toutes les voies de corticoïdes. Vous cherchez une hypothyroïdie et une cœliaquie, parce que la cassure appartient aussi à ces DX.",
        "Vous n'annoncez pas un Cushing prouvé. Vous dites que le tableau dépasse les essais d'asthme léger à modéré, et que le test de freinage suisse n'a pas été lu ici.",
        "Vous ne compensez pas par une hormone de croissance « pour les centimètres perdus ». Cette conduite n'est pas dans les deux revues.",
        "Vous documentez la vitesse en centimètres par an, seule grandeur qui rend l'effet visible, et l'heure des mesures, à cause des 15 mm diurnes.",
        "Piège : attribuer 4 cm de moins dans l'année au seul spray, sans avoir regardé le poids, la peau et la thyroïde.",
    ], a + ", " + b))
    o.append(sec("Ce que vous avez le droit de citer, et l'unité de chaque chiffre", [
        table(
            ["Chiffre", "Ce qu'il désigne", "Ce qu'il n'est pas"],
            [
                ["−0,48 cm/an", "Différence moyenne de vitesse, première année, 14 essais, 5717 enfants, IC −0,65 à −0,30.", "La perte de cet enfant, ou une dose."],
                ["−0,61 cm/an", "Changement de taille depuis la base, 15 essais, 3275 enfants.", "Un second effet à additionner sans lire qu'il s'agit d'une autre métrique."],
                ["−0,19 cm/an", "Deuxième année, non significatif, IC croisant zéro.", "La preuve que l'effet a disparu chez tous."],
                ["−1,20 cm", "Taille adulte, un essai, budésonide 400 µg/j pendant 4,3 ans en moyenne, IC −1,90 à −0,50.", "Une posologie suisse et une perte universelle."],
                ["+0,97 cm", "Changement de taille, fluticasone moins freinatrice que budésonide, certitude modérée, 359 enfants.", "Une raison suffisante pour imposer une molécule sans AIPS."],
                ["+0,37 cm en six mois", "Easyhaler contre Turbuhaler, certitude basse, 229 enfants.", "Un choix de dispositif opposable en Suisse."],
            ],
        ),
        "Vous récitez le chiffre avec son dénominateur. Un chiffre sans essai, sans métrique et sans certitude est une faute de lecture, même s'il est exact.",
    ], a + ", " + b))
    o.append(sec("Prévention : ni abstinence systématique, ni indifférence", [
        "Les corticoïdes inhalés sont le traitement de fond de l'asthme persistant dans les deux revues. La prévention primaire n'est pas l'arrêt systématique.",
        "La prévention secondaire est la mesure de la taille dès la première année de traitement, avec une technique stable.",
        "La prévention tertiaire est la baisse vers la plus faible dose qui contrôle, pour éviter une exposition inutile, sans sacrifier le contrôle.",
        "Vous dites la crainte parentale avant qu'elle ne devienne un arrêt secret. La revue sur les dispositifs fait de cette crainte une cause de mauvaise observance, donc de mauvais contrôle, donc de mauvaise croissance.",
        "Vous n'écrivez aucune marque. Vous n'inventez pas un seuil de centimètres qui imposerait l'arrêt.",
        "Recherche après avril 2019 pour les dispositifs, et après janvier 2014 pour la revue de vitesse : donnée non rouverte au-delà de ces synthèses. Vous datez vos chiffres.",
    ], a + ", " + b))
    return "".join(o)


def dx10():
    p = "[S404]"
    o = []
    o.append(sec("Ce que le chapitre 8 sépare avant tout traitement", [
        "Le chapitre de la société espagnole d'endocrinologie pédiatrique, relu le 25.10.2026, définit la puberté précoce par des caractères sexuels secondaires avant 8 ans chez la fille et avant 9 ans chez le garçon, pour une population caucasienne de pays développés. Il note un avancement séculaire, en partie lié à des contaminants à action œstrogénique, autolimité dans certains pays d'Europe de l'Est.",
        "Il appelle puberté avancée une situation limite autour de 8 ans chez la fille et de 9 ans chez le garçon. Ce n'est pas strictement pathologique, mais la taille finale ou le vécu social peuvent en pâtir, et le chapitre dit que la conduite se rapproche alors de la puberté précoce vraie.",
        "Les variantes incomplètes — thélarche isolée, pubarche isolée, ménarche isolée — peuvent rester stables, régresser, puis laisser venir une puberté normale, ou progresser vers une puberté précoce vraie. Vous ne les traitez pas comme une puberté précoce le jour où elles sont isolées et stables.",
        "L'incidence citée de la puberté précoce va de 1/5 000 à 1/10 000, sex-ratio filles sur garçons de 20 pour 1. Ce n'est pas l'incidence de la thélarche isolée. La fréquence suisse de la variante n'est pas dans le chapitre.",
        "Chez la fille, 98 % des pubertés précoces seraient centrales, et une série multicentrique italienne est citée avec 74 % de formes idiopathiques. La part neurogène est plus haute avant 4 ans, et la part idiopathique plus haute entre 7 et 8 ans. Le chapitre recommande néanmoins de ne pas exclure l'étude du système nerveux central chez des filles de plus de 7 ans lorsqu'une lésion est possible, parce que des lésions tumorales ou congénitales ont été vues à ces âges.",
        "Chez le garçon, la part neurogène varie de 94 % à 40 % selon les auteurs du chapitre. Vous n'appliquez pas l'expectative de la fille. L'hamartome hypothalamique est le plus souvent cité, malformation congénitale à pulses de GnRH, mieux vue à l'IRM, souvent de croissance lente.",
    ], p))
    o.append(sec("Tableau 4 : trois colonnes à ne pas fusionner", [
        "Le tableau 4, malgré une mise en page dense, oppose la thélarche prématurée, l'adrénarche prématurée et la puberté précoce.",
        "Thélarche : sein isolé, âge osseux avancé de moins d'un an, vitesse non accélérée, échographie pelvienne normale chez la fille.",
        "Adrénarche : pilosité isolée, âge osseux avancé de moins de deux ans, vitesse variable, échographie pelvienne normale, testicules inférieurs à 4 ml.",
        "Puberté précoce : sein, pilosité et règles possibles, vitesse accélérée, âge osseux supérieur à l'âge civil de deux ans, échographie pubertaire, testicules supérieurs à 4 ml.",
        "Dès que la vitesse accélère, qu'un second caractère apparaît, ou que l'os avance au-delà de ces marges, vous quittez la variante stable.",
        "Vous palpez une glande. Le chapitre dit qu'une thélarche chez une fille en surpoids se confond avec une adipomastie, et que l'échographie mammaire sépare la graisse du tissu glandulaire. Vous ne comptez pas un coussin graisseux.",
    ], p))
    o.append(sec("Ménarche isolée : rare, et seulement après exclusions", [
        "Filles de 1 à 9 ans, saignements cycliques, aucun autre signe pubertaire. Les règles peuvent revenir pendant un à six ans, puis la puberté vraie commence à un âge normal.",
        "Vous écartez une infection, un corps étranger, une tumeur, un McCune–Albright, un œstrogène exogène et une hypothyroïdie. Le chapitre demande alors une échographie pelvienne, un âge osseux, un test à la GnRH et un estradiol.",
        "Vous informez et vous rassurez seulement après ces exclusions, et vous surveillez une progression vers un McCune–Albright ou une puberté précoce vraie.",
        "Vous ne posez pas un analogue sur ce seul saignement. Le traitement freinateur appartient à la puberté précoce évolutive, pas à cette variante rare une fois les autres causes écartées.",
        "La dose suisse de l'analogue n'a pas été lue. Le chapitre espagnol écrit, pour la puberté précoce idiopathique, une dose moyenne efficace de triptoréline de 100 µg/kg chez 95 % des patientes, le reste étant avancé à 21 jours, et il ne parle que de formes dépôt intramusculaires. Vous citez ce chiffre comme une phrase du chapitre, pas comme une AIPS. Vous ne le prescrivez pas, et vous ne le prescrivez surtout pas pour une thélarche stable.",
        "Piège : un saignement isolé appelé « règles précoces bénignes » sans échographie ni thyroïde.",
    ], p))
    o.append(sec("Central ou périphérique : ce que le chapitre vous fait mesurer", [
        "La puberté précoce centrale dépend de la GnRH : LH et FSH pubertaires, de base ou après stimulation. La forme périphérique ne réveille pas l'axe : gonadotrophines prépubertaires, stéroïdes néanmoins pubertaires.",
        "Après GnRH, le chapitre retient une activation si le rapport LH/FSH dépasse 0,6 chez la fille et 3,6 chez le garçon. Un test négatif n'exclut pas l'activation : les premiers mois, elle est progressive et oscillante, et le résultat dépend du jour. Des stéroïdes bas à un instant donné n'excluent pas non plus.",
        "Chez le garçon, des testicules symétriques orientent vers une forme centrale. Une asymétrie oriente vers une tumeur testiculaire, une sécrétion d'hCG, ou un reste surrénalien. L'hCG peut faire croître les testicules en général à moins de 8 ml tout en activant fortement les cellules de Leydig. Vous ne vous contentez pas du volume.",
        "Chez la fille, l'exploration gonadique est l'échographie. Le corps utérin dépasse 3 cm en phase pubertaire. Le rapport corps sur col passe d'environ 1:1 à 2:1. Un volume ovarien supérieur à 4–4,5 cm³ indique une puberté cliniquement reconnaissable. Des microkystes de moins de 9 mm se voient chez 53 % des filles prépubères normales et 63 % des pubertés précoces : ils ne prouvent pas le diagnostic. Un gros kyste asymétrique évoque une forme périphérique, un kyste autonome ou un McCune–Albright.",
        "Âge osseux : dans les vraies pubertés précoces, il est en général avancé de plus de 2 déviations standards. Deux exceptions écrites : associé à un déficit en hormone de croissance, l'âge osseux est très variable ; associé à une hypothyroïdie, il est retardé. C'est le pont avec la fiche Pedlaus, qui admet une puberté avancée dans l'hypothyroïdie acquise.",
        "Une ménarche maternelle précoce n'est retrouvée que dans 4 % d'une série citée pour les formes centrales idiopathiques. L'histoire familiale ne ferme pas le dossier. Chez le garçon, l'histoire familiale fait chercher la testotoxicose : testostérone pubertaire, gonadotrophines prépubertaires.",
    ], p + ", [S401]"))
    o.append(sec("Causes que vous listez sans les traiter dans la variante stable", [
        "Centrales, filles : idiopathique, hydrocéphalie, myéloméningocèle, hamartome, microadénome, pinéalome, épendymome, neurofibromatose et gliome du nerf optique, agénésie du corps calleux, astrocytome du chiasma, hypothyroïdie de Van Wyk–Grumbach, encéphalite, encéphalocèle, hémorragie, malformation vasculaire, tumeur du quatrième ventricule, selle turcique vide.",
        "Centrales, garçons : le chapitre insiste sur l'atteinte du système nerveux, l'hamartome, la neurofibromatose, la méningite, la radiothérapie, le craniopharyngiome postopératoire, les tumeurs, l'infection congénitale à cytomégalovirus, l'hypothyroïdie, et la même liste résiduelle. La forme idiopathique existe mais n'est pas le pari par défaut.",
        "Périphériques : tumeurs surrénaliennes, hyperplasie surrénalienne congénitale, tumeur de Leydig, testotoxicose, kyste ou tumeur ovarienne (granulosa et thèque au premier rang, 2 % des pubertés précoces de fille sont d'origine ovarienne), hCG, McCune–Albright, stéroïdes exogènes. L'hCG ectopique, rare et de haute malignité, n'est associé à une puberté précoce que chez le garçon.",
        "Virilisation de fille : le chapitre discute le 17-hydroxyprogestérone, l'androstènedione et la DHEA-S, et une DHEA-S très haute, au-dessus de 600 µg/dl dans le texte, fait chercher une tumeur surrénalienne. Vous ne convertissez pas cette unité en un seuil suisse. Vous ne posez pas une hyperplasie congénitale sans le dosage.",
        "McCune–Albright : taches café au lait et dysplasie fibreuse. Le chapitre dit qu'une scintigraphie au technétium 99 est plus sensible et moins lourde qu'une série osseuse pour la dysplasie. Vous ne la demandez pas devant une thélarche isolée sans tache ni signe osseux.",
        "Aucun de ces cadres n'est la thélarche stable. Les confondre est le piège du DX.",
    ], p))
    o.append(sec("Analogue de la GnRH : mécanisme du chapitre, hors ordonnance suisse", [
        "Le chapitre date de 1981 l'usage des analogues dans la puberté précoce idiopathique. En aigu, ils stimulent les gonadotrophines. En chronique, ils désensibilisent l'hypophyse, effet que le texte nomme Knobill, et la maturation gonadique régresse.",
        "Les effets indésirables qu'il regroupe viennent surtout d'un usage indiscriminé : réaction locale, baisse de vitesse, prise de poids, os, céphalées, troubles de l'humeur, bouffées de chaleur. Il attribue les troubles gonadiques après traitement davantage à la cause inconnue de la puberté précoce qu'au médicament.",
        "Efficacité décrite : les caractères régressent, les règles cessent à la deuxième dose si elles existaient, le volume mammaire régresse presque, la pilosité change peu, la vitesse revient au niveau prépubère, l'os ralentit, le pronostic de taille s'améliore. Beaucoup d'auteurs retirent le traitement vers 12 ans d'âge osseux. Les règles reviennent 9 à 18 mois après l'arrêt.",
        "Les meilleurs résultats staturaux concernent les filles commencées avant 6 ans, avec une grande cible parentale, une plus grande taille au diagnostic et moins d'avance osseuse. Entre 7,5 et 8,5 ans, formes lentement progressives, le chapitre dit que l'analogue n'a pas amélioré la taille finale, et qu'un tiers seulement des filles de cet âge pourrait en bénéficier sans réduire le pronostic. La taille finale réelle se situe à mi-chemin entre le pronostic du début et celui de la fin du traitement.",
        "L'association analogue et hormone de croissance est réservée, dans le texte, à des essais ponctuels, avec un gain de pronostic cité entre 7 et 10 cm par rapport au groupe sous analogue seul. Vous ne proposez pas cette association. Aucune AIPS n'a été ouverte.",
        "Pour la variante isolée stable, la conduite du chapitre est d'informer, de rassurer après exclusion, et de surveiller. L'analogue n'est pas son traitement.",
    ], p))
    o.append(sec("Station — sein isolé à 6 ans, vitesse calme", [
        "Fille de 6 ans, bourgeon palpable, pas de pilosité, pas de tache café au lait, pas de produit œstrogénique retrouvé, vitesse non accélérée, parents inquiets parce qu'une camarade est traitée.",
        "Vous palpez une glande et vous écartez l'adipomastie. Vous datez le premier signe. Vous reportez la vitesse sur la courbe suisse en vigueur. Vous demandez l'âge osseux : s'il est avancé de moins d'un an, le tableau 4 reste compatible avec la thélarche.",
        "Vous ne demandez pas d'emblée une IRM ni un analogue. Vous expliquez les trois issues : stabilité, régression, ou progression vers une puberté précoce. Vous ne donnez pas un pourcentage suisse de chacune.",
        "Vous revoyez la palpation et la courbe. Le chapitre ne fixe pas le nombre de semaines. Vous choisissez un délai clinique et vous le dites. Toute accélération, tout second caractère, tout garçon dans un tableau analogue, tout signe neurologique, vous fait quitter ce DX.",
        "Vous dosez la TSH si la croissance ou un signe de la fiche lausannoise l'évoque, parce que l'hypothyroïdie peut avancer la puberté et retarder l'os.",
        "Vous n'écrivez pas 100 µg/kg. Ce chiffre n'est pas une AIPS, et l'indication du chapitre n'est pas cette présentation stable.",
    ], p + ", [S401], [S405]"))
    o.append(sec("Station — garçon de 8 ans, pilosité et testicule qui grandit", [
        "Il a 8 ans, donc avant le seuil de 9 ans. Une pilosité est apparue et un testicule dépasse le volume infantile, de façon symétrique. La vitesse accélère.",
        "Ce n'est plus une pubarche isolée : le testicule au-dessus de 4 ml et la vitesse accélérée entrent dans la colonne puberté précoce du tableau 4. Chez le garçon, vous ne pariez pas sur une forme idiopathique.",
        "Vous adressez pour gonadotrophines, testostérone, âge osseux et imagerie selon le spécialiste. Le chapitre attend des gonadotrophines pubertaires si la forme est centrale, et une IRM pathologique si elle est neurogène.",
        "Une asymétrie testiculaire vous fait chercher une tumeur ou une hCG, pas un simple adrénarche. Le seuil de DHEA-S à 600 µg/dl est celui du chapitre pour une suspicion de tumeur surrénalienne : vous ne le convertissez pas seul en conduite suisse, vous le transmettez comme alerte au spécialiste.",
        "Vous ne rassurez pas avec le sex-ratio de 20 filles pour 1 garçon. Ce ratio dit que le garçon est rare, donc plus souvent organique, pas qu'il est bénin.",
        "Aucun analogue n'est signé ici. La forme dépôt et la dose espagnole restent des phrases du chapitre.",
    ], p))
    o.append(sec("Surveillance et prévention sans médicaliser la variante", [
        "Primaire : écarter les œstrogènes exogènes, crèmes et produits, que le chapitre met dans les causes périphériques.",
        "Secondaire : revoir toute thélarche ou pubarche précoce pour ne pas manquer la progression, et ne pas appliquer à un garçon l'expectative des filles.",
        "Tertiaire : quand la progression est réelle, la prise en charge de la puberté précoce vise à protéger la taille et à traiter la cause. Elle sort de ce DX stable. Les meilleurs gains staturaux décrits concernent les filles de moins de 6 ans, pas la variante non évolutive.",
        "Vous informez avec trois issues, sans pourcentage suisse. Vous redonnez les drapeaux : vitesse, second caractère, signe neurologique, virilisation, tache cutanée, âge osseux qui avance, saignement.",
        "Pas d'hospitalisation pour une thélarche isolée stable. Pas de régime. Pas de spécialité.",
        "Piège final : traiter une forme stable « pour la taille » avec un analogue dont la dose suisse est inconnue et dont le chapitre dit qu'il n'est pas l'outil de la variante incomplète non progressive.",
    ], p))
    return "".join(o)


def plus(key):
    fn = {
        "dx5": dx5,
        "dx6": dx6,
        "dx7": dx7,
        "dx8": dx8,
        "dx9": dx9,
        "dx10": dx10,
    }[key]
    import importlib.util
    import os
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "approfondir_suite.py")
    spec = importlib.util.spec_from_file_location("suite183", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return fn() + mod.more(key)

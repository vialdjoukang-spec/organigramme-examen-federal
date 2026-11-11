# -*- coding: utf-8 -*-
"""Second palier d'approfondissement, mêmes sources, 25.10.2026."""
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
        tds = "".join(f"<td style='vertical-align:top;'>{escape(c)}</td>" for c in row)
        body.append(f"<tr>{tds}</tr>")
    return (
        "<div style='overflow-x:auto;'><table border='1' cellpadding='7' cellspacing='0' "
        "style='width:100%;border-collapse:collapse;font-size:0.92em;'>"
        f"<thead><tr>{th}</tr></thead><tbody>{''.join(body)}</tbody></table></div>"
    )


def fen(title, chunks, source):
    inner = []
    for c in chunks:
        inner.append(c if isinstance(c, str) and c.startswith("<") else p(c))
    return (
        "<details style='margin:8px 0;border-left:4px solid #6c3483;background:#f5eef8;"
        "padding:6px 10px;'><summary style='cursor:pointer;font-weight:bold;color:#4a235a;'>"
        f"{escape(title)}</summary><div style='margin-top:6px;'>{''.join(inner)}"
        f"<em>Source : {escape(source)}.</em></div></details>"
    )


def more(key):
    return {
        "dx5": dx5,
        "dx6": dx6,
        "dx7": dx7,
        "dx8": dx8,
        "dx9": dx9,
        "dx10": dx10,
    }[key]()


def dx5():
    e, w, s, j = "[S201]", "[S205]", "[S204]", "[S203]"
    o = []
    o.append(fen("Scénario chiffré — le matin puis le soir fabriquent une fausse cassure", [
        "Un garçon est mesuré à 141,0 cm un matin de janvier, à jeun, à la toise du cabinet. En juin, la famille le mesure le soir à la maison, après une journée d'école, et trouve 140,2 cm. Elle conclut qu'il a rétréci.",
        "Le PEZZ rappelle jusqu'à 15 mm de moins en fin de journée. Calcul dérivé : 15 mm égalent 1,5 cm. Une part de l'écart de 0,8 cm peut n'être que l'heure. Le reste peut être l'erreur de 2 à 3 cm que la même page décrit dans les cabinets et, a fortiori, à la maison.",
        "Vous ne calculez pas une vitesse négative. Vous refaites les deux mesures le même jour, à la même heure, avec la même méthode, talons au sol. Ensuite seulement vous divisez des centimètres par des années.",
        "Si la seconde mesure de cabinet, six mois plus tard et à heure égale, est 143,6 cm, la différence est 2,6 cm en 0,5 an, soit 5,2 cm par an. Calcul dérivé. Cet ordre de grandeur rejoint les 5 cm par an cités vers 10 ans. Il ne prouve pas le retard constitutionnel. Il retire l'alarme fabriquée par la méthode.",
        "Vous l'écrivez ainsi dans le dossier : mesure du soir écartée, contrôle apparié en attente ou déjà fait, pas de cassure retenue sur des conditions non comparables.",
        "Piège d'oral : accepter le chiffre parental du soir comme point de courbe au même titre que la toise du matin.",
    ], w))
    o.append(fen("Scénario — deux frères, un seul a un retard de tempo", [
        "L'aîné a 15 ans, des testicules pubères, une taille dans la cible, un âge osseux concordant. Le cadet a 14 ans et 2 mois, des testicules encore infantiles, un père qui a grandi tard. La famille veut un seul mot pour les deux.",
        "L'aîné peut illustrer une cible familiale. Il ne prouve pas le diagnostic du cadet. Le dépliant ESPE juge chaque enfant sur ses signes physiques, pas sur la ressemblance.",
        "Pour le cadet, le seuil de 14 ans est franchi. Vous demandez l'âge osseux gauche, les gonadotrophines, la testostérone, la TSH et la thyroxine libre. Vous cherchez l'anosmie et un signe neurologique. Vous ne lui appliquez pas le canal de son frère.",
        "Si l'aîné est petit et que ses parents sont petits, vous pouvez discuter une petite taille familiale pour lui, dans le DX.6, à condition que son canal ait été stable. Le cadet, impubère à 14 ans, n'est pas dans ce DX.",
        "Vous expliquez aux parents que deux mécanismes peuvent coexister dans une fratrie : un canal bas hérité et un réveil tardif. Les traiter par le même silence serait faux. Les traiter par la même hormone le serait aussi.",
        "Vous ne promettez pas que le cadet « fera comme le père » au centimètre près. Le dépliant a retiré cette garantie pour les retards extrêmes, et le PEZZ montre des prévisions déçues quand la lecture osseuse est fragile.",
    ], e + ", " + w))
    o.append(fen("Ce que vous répondez à « est-ce que 2,5 % veut dire bénin »", [
        "La revue européenne, lue le 24.10.2026 et non rouverte le 25, estime 2 à 2,5 % de la population, jusqu'à 80 % des garçons qui consultent pour une puberté retardée, environ un tiers des filles, et environ 10 % dans une cohorte géorgienne de filles. Vous répétez ces chiffres avec leur source et leur biais de recours.",
        "Bénin, au sens du dépliant, veut dire : pas une maladie d'organe une fois les exclusions faites, et habituellement pas de traitement. Cela ne veut pas dire : aucune souffrance, aucune erreur de classement, taille finale toujours égale à la cible.",
        "Vous dites que les garçons consultent plus, donc qu'une fille au seuil n'est pas rassurante parce qu'elle est une fille. Le dépliant dit que la situation trouble autant les deux sexes.",
        "Vous refusez un pourcentage vaudois, genevois ou zurichois. Aucun registre cantonal n'a été lu. Le communiqué de 2026 parle de courbes, pas de ce diagnostic.",
        "Vous refusez aussi d'appeler mortelle une condition dont les sources lues ne donnent pas de mortalité. L'enjeu est la taille, le développement et la vie scolaire.",
        "Piège : « 2,5 %, donc une fille sur quarante dans ma classe ». Le chiffre n'est pas un registre scolaire suisse, et la part féminine parmi les consultantes est plus basse dans les cohortes citées.",
    ], e + ", [S202]"))
    o.append(fen("Ordre du jour de consultation, minute par minute clinique", [
        "Vous commencez par l'âge exact en années et mois, pas par l'année scolaire. Un garçon de 13 ans et 11 mois n'a pas franchi 14 ans. Une fille de 13 ans et 0 mois a franchi le seuil si aucun sein n'est palpable.",
        "Vous demandez le motif en une phrase : taille, absence de règles, moqueries, comparaison avec un frère. Vous ne posez pas le diagnostic dans cette phrase.",
        "Vous mesurez l'enfant puis les deux parents, vous notez l'heure, vous calculez la cible avant d'ouvrir le dossier ancien. Une courbe déjà tracée sur une référence d'avant le 15 juin 2026 est relue, pas jetée, et le nouveau point va sur la courbe désormais recommandée.",
        "Vous palpez. Vous posez les questions d'odeur, de cryptorchidie, de céphalée, de vomissement, de vue, d'appétit et de poids. Vous demandez l'âge des règles de la mère et l'époque de la poussée du père, parce que la revue en fait un critère des types 1 et 3, sans que ce récit suffise.",
        "Puis seulement les examens : âge osseux, TSH, thyroxine libre, gonadotrophines, stéroïde, caryotype chez la fille au seuil. Le médicament, s'il existe un jour, vient après le retour et après l'AIPS.",
        "Vous terminez par la phrase que les parents peuvent répéter : ce qui ferait revenir plus tôt, c'est un signe neurologique, une cassure, ou l'absence de toute progression au contrôle.",
    ], e + ", " + s))
    o.append(fen("Prévision de taille : comment vous parlez des 180 cm devenus 165", [
        "Le PEZZ raconte le jeune adulte à qui l'on avait annoncé 180 cm et qui mesure 165 cm. Vous utilisez cet écart de 15 cm, calcul dérivé 180 − 165, comme l'illustration d'une prévision fausse, pas comme une marge officielle à soustraire à chaque enfant.",
        "Vous expliquez les sources d'erreur que la page elle-même aligne : lecture de la forme de 13 ou 20 os, et non de leur longueur ; schéma de croissance non moyen ; enfant né petit pour l'âge gestationnel, avec une poussée vers 8–10 ans puis une poussée pubertaire pauvre ; proportions inhabituelles.",
        "Vous nommez Greulich–Pyle, Tanner TW2 et TW3, Bayley–Pinneau et Roche comme les méthodes que la page dit utiliser. Vous n'en récitez pas les planches. Vous dites que l'expérience décrite est celle de plus de cent lectures par an, et que le but premier reste de chercher une maladie.",
        "Devant le retard constitutionnel, vous ajoutez la limite de l'ESPE : un retard extrême peut manquer la cible parce que le pic est atténué. La prévision osseuse et la cible parentale sont deux estimations. Elles peuvent diverger. Vous ne choisissez pas la plus rassurante.",
        "Vous ne dites pas qu'une lecture par un non-spécialiste « suffit pour l'examen ». Vous dites qu'un cliché mal lu est une cause fréquente de promesse tenue pour vraie.",
        "Piège : annoncer un chiffre unique de taille adulte sans dire la méthode, l'heure de la mesure et le caractère non garanti.",
    ], w + ", " + e))
    o.append(fen("Famille où les parents sont très éloignés l'un de l'autre", [
        "Mère 152 cm, père 190 cm. La page du PEZZ dit que la formule simple est la moins fiable dans ce cas. Vous la calculez quand même, puis vous tracez les trois repères, et vous dites la régression vers la moyenne sans inventer son ampleur en centimètres.",
        "Garçon, calcul dérivé : somme 342, (342 + 13) / 2 = 177,5 cm. Mère corrigée 152 + 13 = 165 cm. Père corrigé 190 cm. Les trois repères sont donc 165, 190 et 177,5. L'écart entre 165 et 190 est large. L'enfant peut se rapprocher de l'un ou de l'autre. La moyenne n'est pas une promesse.",
        "Fille, calcul dérivé : (342 − 13) / 2 = 164,5 cm. Père corrigé 190 − 13 = 177 cm. Mère 152 cm. Repères 152, 177 et 164,5.",
        "Vous ne multipliez pas 177,5 par 0,72. Sans les SDS des deux parents sur la courbe suisse en vigueur, la formule de Cole–Hermanussen reste une formule, pas un résultat.",
        "Si ce garçon est en plus impubère à 14 ans, la discordance parentale ne le classe pas. Le tempo se juge sur le stade et l'âge osseux. La cible ne fait que situer la taille.",
        "Piège : choisir le parent le plus grand comme « vraie cible » pour rassurer, ou le plus petit pour justifier un médicament.",
    ], w + ", " + j))
    o.append(fen("Ce que le communiqué 2026 change dans la phrase que vous direz à l'oral", [
        "Vous pouvez dire : depuis le 15 juin 2026, pédiatrie suisse recommande des courbes nationales construites au PEZZ, méthode LMS, plus de 43 000 enfants, environ un enfant sur 40 et un habitant sur 210, toutes les régions linguistiques, plus de 100 pédiatres, écoles, nouveau-nés et recrues.",
        "Vous pouvez dire : les courbes de 2011 mêlaient en partie l'OMS et des données américaines, et le communiqué les juge dépassées pour la taille, le poids et l'IMC dès 2 ans. Vous pouvez dire que l'IMC avant 2 ans reste OMS, que le périmètre crânien mélange Zurich et KiGGS, et que la vitesse reste zurichoise.",
        "Vous pouvez dire : le surpoids et l'obésité, dès 2 ans, suivent des courbes qui valent 25 et 30 kg/m² à 18 ans. Vous ne pouvez pas dire que ces ancres définissent la petite taille. Le communiqué renvoie ce seuil aux sociétés.",
        "Vous pouvez dire que le communiqué cite Eiholzer 2025 dans le Journal of Clinical Medicine, et que vous n'avez pas ouvert l'article. Vous ne traduisez pas son titre en un pourcentage de différence de taille, puisque le titre annonce justement l'absence de différence de taille.",
        "Vous ne dites pas que la nouvelle courbe déplace les seuils de 13 et 14 ans. Ces seuils sont ceux du dépliant ESPE, pas ceux d'une courbe.",
        "Vous ne dites pas que l'obésité suisse a un chiffre unique tiré du communiqué. La phrase sur la migration et l'obésité est celle de la page familles du PEZZ, séparée, sans pourcentage.",
    ], s + ", " + w))
    o.append(fen("Copie d'examen — réponse rédigée que vous pouvez tenir", [
        "Énoncé interne : garçon de 14 ans et 4 mois, testicules infantiles, père au développement tardif, taille −2 déviations standards, âge osseux retardé de 18 mois, examen par ailleurs normal, pas de céphalée. Que faites-vous ?",
        "Vous dites que le seuil masculin est franchi et que le tableau ressemble au type 1 déjà décrit par la revue à partir de l'ESPE 2007 : prépubère, âge osseux retardé d'au moins un an, histoire familiale possible. Vous ne dites pas que le diagnostic est certain le premier jour.",
        "Vous vérifiez que les parents ont été mesurés et que la cible est écrite avec +13 cm. Vous vérifiez l'anosmie, la descente des testicules et l'absence de signe neurologique. Vous lisez TSH, thyroxine libre, LH, FSH et testostérone s'ils sont demandés. Vous ne donnez pas d'hormone de croissance.",
        "Vous expliquez que la vitesse des garçons dans ce cadre dépasse souvent 3,6 cm par an, et vous demandez le calcul avant de rassurer. Vous expliquez que la taille finale n'est pas garantie si le retard est extrême.",
        "Vous proposez l'attente et un conseil si l'école souffre. Vous n'écrivez pas de milligrammes. Vous adressez si un stéroïde est envisagé, pour que l'AIPS soit lue.",
        "Vous citez le dépliant pour les seuils, la durée de trois à quatre ans et l'absence habituelle de traitement, et la revue pour les types et le 3,6 cm par an. Vous ne mélangez pas ces deux documents en une seule phrase chiffrée qui n'existe dans aucun des deux.",
    ], e + ", [S202]"))
    o.append(fen("Hérédité du tempo : ce que vous pouvez dessiner sans arbre faux", [
        "La revue lue le 24.10.2026 décrit surtout une transmission autosomique dominante à pénétrance incomplète, et aussi d'autres modes. Vous pouvez le redire. La relecture du 25 octobre ne l'a pas contredit, parce qu'elle n'a pas rouvert l'article.",
        "Le dépliant, lui, ne donne pas de mode de transmission. Il dit que l'âge seul est un mauvais indicateur du potentiel. Le PEZZ, de son côté, voit souvent le programme précoce ou tardif se répéter dans les familles. Vous attribuez chaque phrase à son texte.",
        "Une mère réglée à 16 ans, exemple que le PEZZ met dans la bouche d'une mère, rend le tempo familial plausible chez sa fille petite. Elle ne remplace pas le caryotype si la fille atteint 13 ans sans sein. L'exemple pédagogique n'est pas un critère diagnostique chiffré.",
        "Jusqu'à 7 % de variants hétérozygotes de gènes d'hypogonadisme dans des cohortes de retard constitutionnel : chiffre de la revue, pas de la page familles. Les 80 % et les 50 % de la page familles parlent de la variance de la taille, pas de ces gènes. Vous ne les additionnez pas.",
        "Vous ne proposez pas de test génétique le premier jour. Vous proposez le temps, l'âge osseux et les exclusions. Le test se discute si le tableau devient celui d'un hypogonadisme permanent ou d'une petite taille sévère, sans seuil suisse lu.",
        "Piège : un arbre « dominant donc un enfant sur deux » dessiné comme une loi, alors que la pénétrance est incomplète et que d'autres modes existent.",
    ], e + ", " + w + ", [S202]"))
    return "".join(o)


def dx6():
    j, w, s = "[S304]", "[S303]", "[S302]"
    o = []
    o.append(fen("Quatre familles, quatre calculs dérivés, une seule règle", [
        "Famille 1. Mère 160 cm, père 174 cm. Somme 334. Garçon (334 + 13) / 2 = 173,5 cm, intervalle 165 à 182 cm. Fille (334 − 13) / 2 = 160,5 cm, intervalle 152 à 169 cm.",
        "Famille 2. Mère 155 cm, père 168 cm. Somme 323. Garçon (323 + 13) / 2 = 168 cm, intervalle 159,5 à 176,5 cm. Fille (323 − 13) / 2 = 155 cm, intervalle 146,5 à 163,5 cm.",
        "Famille 3. Mère 170 cm, père 170 cm. Fille 163,5 cm, juste sur la page du PEZZ. Garçon 176,5 cm. Vous ne répétez pas le 178,5 imprimé, qui ne sort pas de l'addition.",
        "Famille 4. Mère 148 cm, père 160 cm. Somme 308. Garçon (308 + 13) / 2 = 160,5 cm. Fille (308 − 13) / 2 = 147,5 cm. Une fille qui termine à 146 cm est dans l'intervalle 139 à 156 cm. Une fille qui termine à 132 cm ne l'est pas.",
        "Dans les quatre cas, la règle est la même : parents mesurés, signe selon le sexe, intervalle ± 8,5 cm, canal stable après 2 ans, puberté à l'heure. Le calcul sans ces conditions n'est pas ce DX.",
        "Vous inscrivez la cible sur la courbe, comme Paediatrica le demande. Vous datez la courbe utilisée.",
    ], j + ", " + w))
    o.append(fen("Poids et taille : l'enfant petit n'est pas jugé sur le poids pour l'âge", [
        "Le PEZZ explique qu'un poids au 25e percentile pour l'âge veut dire, sur 100 enfants, 24 plus légers et 75 plus lourds, mais que ce rang perd son sens si l'enfant est beaucoup plus petit ou plus grand que la moyenne. Ce que l'on veut savoir, c'est le poids pour la taille.",
        "Dans la petite taille familiale, un poids bas pour l'âge peut n'être que le reflet d'une taille basse. Vous regardez le couloir du poids pour la taille, ou l'IMC en kg/m², avant de parler de dénutrition.",
        "La page préfère le poids pour la taille, surtout sous 2 ans et quand la taille s'éloigne de la moyenne. Le communiqué de 2026, lui, publie des courbes d'IMC et ancre le surpoids à 25 et 30 kg/m² à 18 ans. Vous utilisez les deux informations sans les opposer : l'une suit la trajectoire individuelle, l'autre situe le surpoids selon la société.",
        "Un enfant familialement petit qui croise vers le haut en poids pendant que la taille casse n'est plus dans la variante. Vous ouvrez l'hypothyroïdie et la cœliaquie.",
        "Vous ne dites pas qu'un IMC normal prouve le diagnostic familial. Il retire seulement un argument de maladie nutritionnelle grossière.",
        "Piège : régime amaigrissant chez un enfant petit dont le poids pour la taille est ordinaire, parce que le poids pour l'âge « a l'air bas ».",
    ], w + ", " + s))
    o.append(fen("Ce que vous dites aux parents qui demandent l'hormone de croissance", [
        "Vous revenez au mécanisme. Après deux ans, un canal stable veut dire que le modèle hérité est en place. Le PEZZ décrit ce canal comme le signe d'un mécanisme qui fonctionne, intestin, rein et hormones compris, tant qu'il ne change pas.",
        "La petite taille statistique, sous le 3e percentile, soit −1,88 déviation standard dans Paediatrica, est une position. Elle ne crée pas une indication. Il y a autant d'enfants sous le 3e percentile qu'au-dessus du 97e.",
        "Vous montrez le calcul de cible. Si l'enfant est dedans et que la puberté est à l'heure, l'hormone de croissance ne corrige pas un déficit. Elle médicaliserait une trajectoire parallèle. Aucune source lue ne l'indique dans cette variante pure.",
        "Vous dites ce qui changerait la décision : une cassure, une vitesse effondrée, une taille très en dessous de la cible, une puberté absente aux seuils ESPE, un âge osseux retardé. Alors le dossier quitte ce DX.",
        "Vous ne citez pas de gain en centimètres, de marque, ni de condition de remboursement. Donnée non trouvée dans les sources ouvertes pour une indication suisse de l'hormone de croissance dans la petite taille familiale pure.",
        "Vous proposez la mesure annuelle et la phrase de retour. C'est le traitement qui respecte le mécanisme.",
    ], w + ", " + j + ", [S306]"))
    o.append(fen("Enfant né petit pour l'âge gestationnel dans une famille déjà petite", [
        "Les deux faits peuvent être vrais ensemble : parents petits, et naissance en dessous du poids ou de la taille attendus. Le PEZZ dit que la prévision moyenne est moins fiable chez l'enfant né petit pour l'âge gestationnel, avec souvent une poussée vers 8–10 ans puis une poussée pubertaire qui apporte moins.",
        "Vous ne chiffrez pas cette perte. Vous ne dites pas non plus que la naissance efface la cible parentale. Vous dites que la cible situe le patrimoine, et que le schéma de croissance peut s'en écarter.",
        "Vous suivez le canal réel, pas la prévision. Un canal stable après 2 ans, dans la zone parentale, peut rester compatible avec une variante familiale malgré la naissance. Une cassure ne le peut pas.",
        "L'indication suisse d'hormone de croissance pour l'enfant né petit pour l'âge gestationnel n'a pas été lue. Vous ne la reconstruisez pas à partir de la page familles.",
        "Vous le séparez du retard constitutionnel : ici la question est le potentiel et le canal, pas d'abord le seuil de 13 ou 14 ans, sauf si la puberté manque aussi.",
        "Piège : un seul mot, « constitutionnel », pour un nouveau-né petit, un enfant familialement petit et un adolescent impubère. Ce sont trois dossiers.",
    ], w))
    o.append(fen("Contrôle à un an : comment vous décidez de rester ou de partir", [
        "Vous avez deux tailles à la même heure, séparées d'environ un an. Vous soustrayez, vous divisez par l'intervalle en années, vous obtenez des centimètres par an. Vous comparez au canal, pas à un camarade déjà pubère.",
        "Si le percentile est le même, à l'erreur de mesure près, et que la cible contient l'enfant, vous restez dans ce DX. L'erreur de 2 à 3 cm vous interdit de crier à la cassure pour un écart plus petit que ce bruit.",
        "Si le percentile a clairement changé, au-delà du bruit, vous partez de ce DX même si les parents sont petits. Le PEZZ appelle ce changement suspect après 2 ans.",
        "Vous revoyez le stade. Une fille qui approche 13 ans sans sein, ou un garçon qui approche 14 ans sans croissance testiculaire, sort de la variante familiale le jour du seuil, même si la cible était juste jusque-là.",
        "Vous n'ajoutez pas de bilan sanguin si rien n'a bougé et qu'aucun symptôme du tableau cœliaque ou thyroïdien n'est apparu. Les sources lues ne rendent pas ce bilan obligatoire dans la variante pure sans doute.",
        "Vous notez la courbe 2026 pour la taille et la courbe zurichoise pour la vitesse, et vous le dites si les deux graphes sont sur la table.",
    ], w + ", " + s))
    o.append(fen("Réponses courtes que l'examinateur attend sur ce DX", [
        table(
            ["Question", "Réponse tenue par les sources", "Réponse refusée"],
            [
                ["Quel est le gold standard ?", "La clinique et l'auxologie. Aucun dosage ne prouve la variante.", "Une IGF-1 normale comme preuve."],
                ["Quelle formule ?", "[mère + père ± 13 cm] / 2, + chez le garçon, − chez la fille, ± 8,5 cm.", "La moyenne des frères et sœurs."],
                ["Que vaut 0,72 ?", "Le coefficient de Cole–Hermanussen sur la moyenne des SDS parentaux.", "Un facteur à appliquer aux centimètres."],
                ["Quand le canal est-il parlant ?", "Après 2 ans. Avant, le changement peut être l'ajustement au modèle hérité.", "Dès la naissance, tout écart est une maladie."],
                ["Quel médicament ?", "Aucun dans la variante pure, d'après les textes lus.", "Une hormone de croissance « pour aider »."],
                ["Quelle courbe en 2026 ?", "Taille nationale PEZZ depuis le 15 juin 2026. Vitesse encore zurichoise.", "Tout jeter, y compris la vitesse."],
            ],
        ),
        "Vous répondez en une phrase, puis vous citez la source. Vous ne comblez pas un silence par un pourcentage.",
    ], j + ", " + w + ", " + s))
    o.append(fen("Consultation de contrôle — ce que vous dites debout devant la courbe", [
        "Vous montrez le point d'aujourd'hui et le point d'il y a un an, mesurés à des heures comparables. Vous dites le percentile, puis la cible, puis seulement le mot familial si les deux concordent.",
        "Vous refaites la soustraction devant les parents. Exemple dérivé : 128,4 cm puis 133,6 cm un an plus tard font 5,2 cm par an. Vous rapprochez ce rythme de l'ordre de 5 cm par an cité par le PEZZ vers 10 ans, en rappelant l'âge réel de l'enfant et le fait que 5 cm n'est pas un seuil diagnostique.",
        "Si l'écart annuel est de 1,2 cm, vous ne le mettez pas sur le compte de l'erreur de 2 à 3 cm sans le dire : 1,2 cm est plus petit que cette erreur, donc une seule paire de mesures ne tranche pas. Vous rapprochez le contrôle et vous vérifiez la toise. Deux écarts successifs du même sens, au-delà du bruit, deviennent une cassure.",
        "Vous montrez l'intervalle de ± 8,5 cm autour de la cible comme une zone, pas comme une ligne. Un enfant au bord haut de la zone et un enfant au bord bas ont le même droit au mot familial si le canal est stable et la puberté à l'heure.",
        "Vous rappelez que la courbe de taille est nationale depuis le 15 juin 2026 et que la vitesse, elle, reste lue sur les références longitudinales de Zurich. Changer de référence en cours de route sans le noter peut fabriquer un faux changement de canal.",
        "Vous terminez sans ordonnance. Le prochain point est une date, pas un médicament. Les parents repartent avec la phrase qui ferait revenir : cassure, puberté absente au seuil, disproportion.",
    ], w + ", " + s + ", " + j))
    o.append(fen("Dire la régression vers la moyenne sans chiffre inventé", [
        "Les parents très grands craignent un enfant « trop petit pour eux ». Les parents très petits craignent un enfant « encore plus petit ». Le PEZZ répond que les modèles simples exagèrent les deux bords : les enfants de parents très grands sont en moyenne un peu moins grands que le calcul, et les enfants de parents très petits un peu moins petits. C'est la régression vers la moyenne, pas une maladie.",
        "Vous le dites avec la formule de Cole–Hermanussen seulement si vous avez les déviations standards parentales. Le coefficient 0,72 multiplie la moyenne des deux SDS. Il ne multiplie pas une taille en centimètres. Sans SDS, vous vous arrêtez à la formule de Tanner et aux trois repères.",
        "Exemple que vous pouvez calculer, parents 152 et 190 cm, déjà fait : garçon 177,5 cm, repères maternel corrigé 165 cm et paternel 190 cm. L'écart de 25 cm entre les deux repères, calcul dérivé 190 − 165, montre pourquoi la moyenne seule est pauvre. Vous tracez les trois. Vous ne choisissez pas 190 pour faire plaisir ni 165 pour justifier un bilan.",
        "Vous ajoutez que l'hérédité de la taille reste mal connue. La page parle d'au moins quatre emplacements du génome et d'environ 80 % de la variance expliquée génétiquement, en général par plusieurs gènes. Ces phrases n'ouvrent pas un test chez un enfant dont le canal bas est stable et contenu dans la cible.",
        "Si l'enfant sort de l'intervalle de ± 8,5 cm, la régression vers la moyenne ne sert pas d'excuse. Sortir de l'intervalle veut dire que le patrimoine, tel que la formule le résume, ne suffit plus. Vous reprenez la démarche diagnostique.",
        "Vous ne dites pas « il sera plus grand que le calcul parce que la moyenne attire ». Vous dites « le calcul simple peut être trop extrême, et je ne corrige ce biais que si j'ai les SDS ».",
        "Piège : appliquer 0,72 à 177,5 cm et annoncer 127,8 cm. Ce produit n'a aucun sens clinique. Calcul dérivé montré seulement pour l'interdire : 177,5 × 0,72 = 127,8, qui n'est pas une taille cible.",
    ], w + ", " + j))
    return "".join(o)


def dx7():
    g = "[S307]"
    o = []
    o.append(fen("Algorithme que vous déroulez sans sauter une case", [
        "Case 1. Y a-t-il une raison du tableau 2 : cassure ou petite taille, retard pubertaire, diarrhée, constipation rebelle, anémie ferriprive, aphtes, émail, fatigue, maladie autoimmune, Turner, apparenté au premier degré, déficit en IgA, ou un autre item de ce tableau ? Si non, vous ne lancez pas une sérologie « pour voir » sans le dire.",
        "Case 2. L'enfant mange-t-il des quantités habituelles de gluten ? Si un régime a déjà commencé, vous l'arrêtez comme test et vous expliquez qu'il faudra réexposer, sans inventer la durée : la guideline dit qu'une réévaluation demanderait une réexposition prolongée et de nouveaux examens.",
        "Case 3. IgA totale et TGA-IgA. IgA basse pour l'âge ou inférieure à 0,2 g/L après 3 ans : test IgG, puis biopsie si ce test est positif. Vous n'empruntez pas la voie sans biopsie.",
        "Case 4. TGA-IgA au moins 10 fois la normale, sur un test qui mesure cette zone par courbe de calibration, famille d'accord, EMA-IgA positif sur un second tube : le diagnostic sans biopsie peut être posé par le spécialiste. HLA et symptômes : non obligatoires.",
        "Case 5. TGA-IgA positive mais sous 10 fois : au moins quatre biopsies du duodénum distal et une du bulbe, gluten maintenu. Orientation correcte, sinon le grade de Marsh ne se donne pas.",
        "Case 6. Marsh 0 ou I avec auto-immunité confirmée : suivi rapproché, pas de diagnostic arrêté sur Marsh 1, pas de régime lancé pour tester.",
    ], g))
    o.append(fen("Pourquoi le second tube n'est pas une formalité", [
        "La guideline veut un EMA-IgA positif dans un second prélèvement, pas un second regard sur le même sérum. Le mot « triple test » de 2012 laissait croire qu'un seul tube suffisait. Le texte de 2020 corrige cette lecture.",
        "Vous expliquez à la famille qu'il y aura deux prises de sang si le premier titre est très haut, et que l'accord porte sur le diagnostic et sur le régime à vie, pas seulement sur le geste.",
        "Vous vérifiez que le laboratoire peut rendre un titre quantitatif jusqu'à 10 fois sa propre limite. Un résultat rendu « supérieur à » sans que la zone de 10 fois soit dans la plage ne remplit pas la condition.",
        "Vous ne téléphonez pas « c'est sûr » entre les deux tubes. Vous dites « le premier résultat ouvre une voie, le second la confirme ou la ferme ».",
        "Si le second EMA est négatif, vous ne forcez pas la voie sans biopsie. Vous revenez vers le spécialiste et, selon le titre, vers les biopsies. Vous n'inventez pas une troisième règle.",
        "Piège de copie : « HLA plus EMA plus TGA le même matin ». Ce paquet n'est pas la recommandation 2020.",
    ], g))
    o.append(fen("Lire un compte-rendu de biopsie sans surinterpréter le grade", [
        "Vous cherchez d'abord la qualité : orientation, nombre de fragments, bulbe présent ou absent. Environ la moitié des biopsies, dans l'étude citée, ne sont pas jugées optimalement orientées. Un grade précis sur un fragment mal orienté est fragile.",
        "Vous distinguez deux accords. L'accord sur « maladie ou non » peut être bon, kappa 0,84 dans l'étude pédiatrique citée quand on s'en tient à ce jugement. L'accord sur le grade exact de Marsh–Oberhuber est mauvais. Werkstetter est cité avec 7 % de désaccord sur la présence de la maladie et 58 % tous grades confondus.",
        "Un rapport villosités sur cryptes inférieur à 2, sur une partie d'au moins une biopsie bien orientée, est en accord avec la maladie. Vous ne transformez pas un lymphocyte isolé en atrophie. Le seuil de la légende, plus de 25 lymphocytes intra-épithéliaux pour 100 entérocytes, marque l'augmentation. Il ne pose pas le diagnostic à lui seul.",
        "Si le titre et l'histologie se contredisent, la guideline demande une recoupe et un second avis. Vous suivez cette demande. Vous ne choisissez pas le résultat qui arrange le calendrier familial.",
        "Marsh 1 peut évoluer plus souvent que Marsh 0 vers l'atrophie, suggestion de la guideline, sans étude dédiée au devenir comparé. Vous surveillez. Vous ne dites ni « ce n'est rien », ni « c'est prouvé ».",
        "Piège : traiter un 3b et un 3c comme deux maladies différentes pour la conduite de premier recours. Le désaccord entre grades est précisément ce que la guideline souligne.",
    ], g))
    o.append(fen("Cassure staturale : ce que vous attendez du régime, et ce que vous ne promettez pas", [
        "La croissance ralentie est un motif de test, pas un résultat thérapeutique chiffré. Les pages lues ne donnent pas le nombre de centimètres rattrapés après le régime sans gluten.",
        "Vous continuez la courbe suisse en vigueur, à heure comparable, pour voir si le canal se reprend une fois le diagnostic retenu et le régime réellement suivi. Une reprise est un argument clinique. Une absence de reprise fait vérifier le régime, les biopsies ou une autre cause, dont la thyroïde.",
        "Vous ne donnez pas d'hormone de croissance pour « aider le rattrapage » le jour du diagnostic. Cette conduite n'est pas dans la guideline lue.",
        "Vous ne donnez pas non plus un délai en semaines après lequel la taille « aurait dû » reprendre. Donnée non trouvée.",
        "Vous expliquez le régime à vie seulement quand le diagnostic est retenu selon les règles. Avant cela, le gluten continue, y compris le jour de la biopsie.",
        "Apparenté au premier degré : le tableau 2 le liste. Vous pouvez proposer la discussion du test aux frères et sœurs et aux parents. Vous ne posez pas leur diagnostic par procuration.",
    ], g))
    o.append(fen("Liens avec les autres DX de ce lot, sans les fusionner", [
        "Turner : le dépliant ESPE demande le caryotype si la puberté de la fille tarde. La guideline 2020 met le Turner dans les situations où l'on envisage la sérologie. Vous faites les deux gestes quand les deux seuils sont là. Vous n'en faites pas un seul.",
        "Thyroïde autoimmune : le tableau 2 la cite, et la fiche Pedlaus rappelle que les maladies thyroïdiennes auto-immunes s'associent à d'autres maladies auto-immunes. Une cassure avec TSH anormale et une sérologie cœliaque peuvent donc se discuter ensemble, chacune avec son test.",
        "Déficit en IgA : il figure dans le tableau 2 et il change la biologie. Vous ne lisez pas une TGA-IgA négative comme une exclusion.",
        "Retard pubertaire et aménorrhée figurent dans le tableau 2. Un retard constitutionnel ne se conclut pas sans avoir au moins pensé à cette ligne si la croissance casse ou si des signes digestifs existent. Penser n'est pas doser tout le tableau chez un enfant dont le canal est stable et l'examen pauvre.",
        "Petite taille familiale : si la cible explique la taille et que le canal est stable, le tableau 2 ne vous oblige pas à une sérologie systématique. La guideline lie le test à des symptômes, des signes et des situations. Une position basse isolée, cohérente avec les parents, n'est pas à elle seule une cassure.",
        "Piège : un bilan « SSP O2.1 complet » identique pour les six DX. Chaque DX a son geste qui tranche.",
    ], g + ", [S201], [S401]"))
    o.append(fen("Phrases d'oral sur la cœliaquie de l'enfant qui grandit mal", [
        "Vous dites 10 fois, second prélèvement, accord de la famille, test capable de mesurer ce titre. Vous ne dites pas 10 fois tout court.",
        "Vous dites quatre plus une pour les biopsies. Vous ne dites pas « quelques biopsies duodénales ».",
        "Vous dites que le HLA négatif rend la maladie peu probable et que le HLA positif ne la prouve pas. Vous citez, si on vous le demande, les 399 patients de Werkstetter et les 227 de Wolf, tous porteurs des allèles à risque dans ces séries très sélectionnées, comme argument pour ne pas ajouter le HLA à la voie sans biopsie, pas comme une prévalence populationnelle.",
        "Vous dites 17 % d'anémie ferriprive dans la ProCeDE symptomatique, 52,7 % de douleurs et 38,9 % de constipation dans une série de 165 dossiers, et 1,1 % contre 1,2 % dans l'étude cas-témoins sans biopsie. Vous ne mélangez pas ces dénominateurs.",
        "Vous dites que la diarrhée, la constipation rebelle, l'anémie et l'émail ont des arguments d'association, et que la douleur isolée, la dyspepsie et le ballonnement n'en ont pas assez selon la guideline.",
        "Vous ne dites aucun gramme de gluten, aucun produit commercial, aucune dose d'immunosuppresseur. Rien de cela n'a été lu comme recommandation suisse.",
    ], g))
    o.append(fen("Duodénum et bulbe : pourquoi les deux comptent dans la phrase d'examen", [
        "La guideline demande au moins quatre biopsies du duodénum distal et au moins une du bulbe lorsque le titre est positif mais inférieur à 10 fois la normale. Oublier le bulbe, c'est ne pas avoir suivi la recommandation, même si quatre fragments distaux sont dans le pot.",
        "Vous le dites au gastroentérologue dans le courrier, et vous le vérifiez au compte-rendu. « Biopsies duodénales » sans site ni nombre ne suffit pas à coter la qualité.",
        "L'orientation se demande aussi. Un fragment tangentiel peut faire croire à une atrophie ou la masquer. Le kappa à 0,84 concerne le jugement maladie ou non quand on peut le porter. Il ne sauve pas un prélèvement mal orienté sur lequel on voudrait un grade fin.",
        "Vous maintenez le gluten jusqu'au jour du geste. Un arrêt du gluten dans les semaines qui précèdent l'endoscopie peut affaisser les lésions et faire appeler potentielle une maladie vraie. La guideline cite un apport en gluten déjà bas avant les biopsies parmi les raisons d'un Marsh trop léger. Elle ne donne pas, dans les pages lues, un nombre de semaines de réexposition : vous n'en inventez pas.",
        "Après le geste, vous ne lancez le régime que lorsque le spécialiste a retenu le diagnostic selon les règles, avec ou sans biopsie. Le premier recours continue la courbe et ne double pas les avis anatomopathologiques de son côté.",
        "Piège : compter cinq fragments distaux et zéro bulbe comme un examen complet, ou compter un bulbe unique sans les quatre distaux.",
    ], g))
    o.append(fen("Courrier au gastroentérologue : les seules phrases utiles", [
        "Vous écrivez l'âge, les deux tailles datées, la vitesse en centimètres par an, la cible parentale si vous l'avez calculée, et le fait que le canal a changé après l'âge de 2 ans. Le spécialiste a besoin de la trajectoire, pas du seul percentile du jour.",
        "Vous écrivez ce qui, dans le tableau 2, a motivé le test : anémie, constipation rebelle, aphtes, fatigue, maladie autoimmune, Turner, apparenté, ou la cassure elle-même. Vous n'écrivez pas une liste copiée en entier si seul un item est présent.",
        "Vous écrivez le résultat chiffré de la TGA-IgA, la limite supérieure du laboratoire, et si 10 fois cette limite tombe dans la plage du test. « Positive » sans multiple ne permet pas de choisir la voie.",
        "Vous écrivez l'IgA totale, pour que personne n'interprète une TGA-IgA chez un enfant déficitaire. Sous 0,2 g/L après 3 ans, ou basse pour l'âge, vous signalez le passage au test IgG et l'obligation de biopsier si ce test est positif.",
        "Vous écrivez que l'enfant mange encore du gluten, ou depuis quand il a arrêté. Cette ligne change la lecture de tout le dossier.",
        "Vous n'écrivez pas de demande d'analogue, d'hormone de croissance ni de régime déjà commencé. Vous demandez la confirmation selon la guideline 2020 et vous gardez la courbe.",
        "Piège : un courrier qui dit « petite taille, merci de prendre en charge » sans vitesse, sans titre et sans gluten.",
    ], g))
    return "".join(o)


def dx8():
    t = "[S401]"
    o = []
    o.append(fen("Examen que la fiche vous fait décrire, région par région", [
        "Vous regardez d'abord l'enfant habillé comme il se plaint : frilosité, ralentissement, prise de poids. Puis vous mesurez la taille et le poids à heure notée, parce qu'un ralentissement se calcule et ne se devine pas.",
        "Cou : vous palpez la loge à la déglutition. Un goitre se voit et se touche. Vous ne l'affirmez pas sur un cou large. La fiche en fait un signe, pas un diagnostic.",
        "Cheveux : secs, cassants, qui tombent. Peau et constipation se demandent. Attention en classe : vous le demandez à l'enfant et à l'école, parce que la fiche en fait un signe et que la qualité de vie baisse par la labilité et la limitation des activités.",
        "Segments : la fiche décrit une moindre croissance des os longs et une baisse du rapport du segment supérieur sur le segment inférieur. Vous savez chercher une disproportion. Le seuil chiffré de ce rapport n'est pas sur la fiche. Vous décrivez, vous ne inventez pas le nombre.",
        "Puberté : vous cotez le stade. Un retard est fréquent. Une avance est possible. Les deux vous gardent dans la réflexion thyroïdienne si la croissance ne colle pas.",
        "Vous ne commencez pas par le système nerveux. L'encéphalopathie de Hashimoto est très rare. Un enfant qui grandit mal n'est pas une encéphalopathie.",
    ], t))
    o.append(fen("TSH haute et thyroxine libre encore normale : vous ne comblez pas le silence", [
        "La fiche dit que, dans certains Hashimoto, l'observation seule suffit et que le traitement n'est pas toujours nécessaire. Elle ne donne pas le seuil de TSH à partir duquel cette observation s'arrête.",
        "Vous recontrôlez. Vous lisez une recommandation spécialisée avant de traiter une forme sans thyroxine libre basse. Cette recommandation n'a pas été ouverte ici : donnée non trouvée au-delà de la phrase de la fiche.",
        "Vous ne dites pas « subclinique donc bénin » comme une catégorie suisse. Le mot n'est pas celui de la fiche. Vous dites : thyroxine libre encore dans les normes du laboratoire, TSH au-dessus, conduite non chiffrée par la fiche, pas de microgramme signé.",
        "Vous surveillez la courbe. Une cassure franche pendant cette observation vous fait revoir la décision plus tôt, et chercher aussi une autre cause de cassure.",
        "Si la thyroxine libre est basse et la TSH haute, la fiche est plus directe : hypothyroïdie primaire, échographie, et substitution dont la dose AIPS reste à lire. La plage 1,5 à 2 µg/kg/jour reste un enseignement, pas une ordonnance.",
        "Piège : traiter ou ne pas traiter sur une seule TSH, sans thyroxine libre et sans seconde lecture.",
    ], t))
    o.append(fen("Forme centrale : le piège de la TSH « normale » ou basse", [
        "Une TSH basse avec une thyroxine libre basse n'est pas une thyroïde rassurante. C'est le chemin central de la fiche : rare, IRM hypothalamo-hypophysaire, autres déficits à chercher.",
        "Vous ne demandez pas d'abord les anticorps anti-TPO pour cette constellation. Les anticorps servent si la thyroïdite est suspectée. Ici le problème peut être au-dessus de la glande.",
        "Vous ne vous arrêtez pas à l'hypothyroïdie. La fiche demande de chercher d'autres déficits hormonaux. Le détail de ces déficits et l'ordre suisse des tests n'est pas sur la fiche : vous adressez sans inventer le panel.",
        "Un enfant avec céphalées et une thyroxine libre basse quitte aussi le retard constitutionnel, pour la même raison neurologique que dans le DX.5. Les deux DX se parlent. Ils ne se remplacent pas.",
        "L'échographie normale n'écarte pas la forme centrale. Elle répond à la question de la loge : malformation, nodule, kyste, infiltration.",
        "Piège d'oral : « TSH basse, tout va bien, la thyroïde est au repos ». Cette phrase confond le freinage périphérique et le déficit central. La thyroxine libre tranche.",
    ], t))
    o.append(fen("Qualité de vie et école, sans score inventé", [
        "La fiche dit la qualité de vie clairement diminuée pendant la phase d'hypothyroïdie, surtout par la limitation des activités et la labilité émotionnelle, plus une impression globale de mauvaise santé. Elle ne donne pas de score chiffré. Vous n'en fabriquez pas.",
        "Vous demandez ce que l'enfant a arrêté : sport, attention, humeur. Vous le notez comme un signe, au même titre que le froid et la constipation.",
        "Vous dites que le but du traitement, une fois prescrit selon l'AIPS, est aussi de corriger ces signes, pas seulement de ramener un chiffre de TSH.",
        "Vous ne promettez pas le délai de cette correction. Il n'est pas écrit.",
        "Vous prévenez qu'un surdosage peut rendre hyperthyroïdien : agitation, amaigrissement, tachycardie sont des alertes cliniques générales. La liste officielle des effets indésirables suisses n'a pas été lue. Vous le dites, et vous ne présentez pas votre liste comme celle de l'AIPS.",
        "Piège : ignorer l'école parce que « c'est une histoire de taille ».",
    ], t))
    return "".join(o)


def dx9():
    a, b = "[S402]", "[S403]"
    o = []
    o.append(fen("Comment vous lisez la certitude sans la transformer en doute total", [
        "Onze essais sur vingt-cinq ne disent pas comment le hasard a été garanti. Tous sauf six ne disent pas comment la liste d'attribution a été cachée. La revue juge que cette limite ne change guère le résultat, parce que l'exclure laisse des chiffres presque identiques. Vous le dites. Vous ne jetez pas 0,48 cm par an pour ce motif, et vous ne le présentez pas non plus comme une certitude haute.",
        "La certitude est modérée pour le −0,48 et le −0,61 de la première année. Modérée veut dire, dans le langage de ces pages, qu'une recherche ultérieure peut encore peser. Elle ne veut pas dire que l'effet est imaginaire.",
        "Soixante-huit pour cent des essais de la revue de vitesse étaient financés par l'industrie. Cinq étaient internationaux. Quatre-vingts pour cent étaient multicentriques. Vous nommez le financement. Vous ne concluez pas que le chiffre est fabriqué.",
        "Dans la revue des dispositifs, la certitude va de très basse à modérée, surtout parce qu'il y a peu d'essais, peu de sujets, une qualité inégale et un financement industriel possible. Le +0,81 cm par an repose sur 23 enfants. Vous ne choisissez pas une molécule nationale sur 23 enfants.",
        "Vous séparez donc deux messages. Le ralentissement moyen de la première année est assez étayé pour être dit aux parents. Le choix de la molécule et du dispositif ne l'est pas assez pour être imposé à partir de ces seules revues.",
        "Piège : « les études sont biaisées, donc l'effet est nul », ou « c'est prouvé, donc on arrête le traitement ».",
    ], a + ", " + b))
    o.append(fen("Ne pas additionner −0,48 et −0,61", [
        "Les deux chiffres décrivent deux métriques. L'une est la vitesse linéaire. L'autre est le changement de taille depuis la ligne de base. Les essais et les effectifs ne sont pas les mêmes : 14 essais et 5717 enfants d'un côté, 15 essais et 3275 de l'autre.",
        "Les additionner en « plus d'un centimètre par an » est une faute de lecture. Vous dites l'un ou l'autre, avec son nom.",
        "De la même façon, le −1,20 cm de taille adulte n'est pas 0,48 multiplié par le nombre d'années. C'est le résultat d'un essai précis, budésonide 400 µg par jour, durée moyenne 4,3 ans, enfants prépubères, contre placebo. Vous le citez tel quel, comme exposition d'essai.",
        "La deuxième année à −0,19 cm par an, intervalle qui contient zéro, empêche de prolonger automatiquement le chiffre de la première année. La troisième année est discordante selon l'essai : 5,34 contre 5,34 cm par an dans l'un, −0,33 cm par an dans l'autre.",
        "Vous résumez ainsi : effet moyen clair la première année, moindre et inconstant ensuite, trace possible à l'âge adulte dans un essai, bénéfice de l'asthme contrôlé maintenu par les deux revues.",
        "Piège de calcul à l'oral : 0,48 fois 10 ans égalent 4,8 cm, annoncés comme la perte d'un enfant traité dix ans. Ce produit n'est pas dans la revue.",
    ], a))
    o.append(fen("Parler aux parents sans minimiser et sans faire peur", [
        "Vous commencez par le contrôle de l'asthme. Les deux revues rappellent que ces médicaments sont le traitement de fond de l'asthme persistant, et que la peur fait sauter des prises. L'asthme non contrôlé freine la croissance et peut tuer. Cette phrase se dit avant le demi-centimètre.",
        "Vous donnez ensuite le chiffre moyen, l'intervalle de confiance et la limite : ce n'est pas la prédiction individuelle. Vous dites que la première année est celle qu'il faut mesurer.",
        "Vous montrez la toise, l'heure, les talons. Une erreur de 2 à 3 cm, rappel du PEZZ, est plus grande que 0,48 cm. Vous ne déclarez donc pas un effet indésirable sur deux mesures bruyantes. Vous exigez une série.",
        "Vous vérifiez ce que l'enfant prend vraiment : device, technique, doses oubliées, corticoïde nasal ou cutané ajouté. Le freinage vient de ce qui est absorbé, pas de l'étiquette « local ».",
        "Vous n'opposez pas fluticasone et budésonide comme un choix déjà suisse. Vous dites que la revue voit souvent moins de freinage avec la fluticasone, avec une certitude inégale selon la métrique, et que cela ne remplace pas l'autorisation suisse ni le contrôle obtenu chez cet enfant.",
        "Vous fixez la prochaine mesure. Le nombre de semaines n'est pas dans la revue. Vous le choisissez et vous le notez.",
    ], a + ", " + b + ", [S205]"))
    o.append(fen("Ce que vous ne faites pas le jour où la vitesse est compatible avec l'effet moyen", [
        "Vous ne stoppez pas un asthme contrôlé pour un écart de l'ordre du demi-centimètre, une fois la technique de mesure vérifiée.",
        "Vous ne demandez pas une IGF-1 pour « prouver » l'effet indésirable. Le mécanisme passe par l'IGF-1, mais la revue n'en fait pas le gold standard clinique de cet effet.",
        "Vous ne faites pas un test de stimulation. La taille et la vitesse collent alors à l'effet décrit, pas à un déficit somatotrope.",
        "Vous ne commencez pas une hormone de croissance de compensation. Conduite absente des deux revues.",
        "Vous ne changez pas de molécule sur la foi du seul essai de 23 enfants. Vous en parlez au prescripteur de l'asthme comme d'une donnée incertaine.",
        "Vous documentez, vous rassurez avec les bons chiffres, et vous revoyez. C'est la conduite qui respecte à la fois le cartilage et les bronches.",
    ], a + ", " + b))
    return "".join(o)


def dx10():
    psrc = "[S404]"
    o = []
    o.append(fen("Seuils d'âge : 8 et 9 ans ne sont pas 13 et 14 ans", [
        "Le chapitre espagnol place la puberté précoce avant 8 ans chez la fille et avant 9 ans chez le garçon. Le dépliant ESPE place l'absence de puberté à signaler à 13 ans chez la fille et à 14 ans chez le garçon. Vous ne les inversez pas et vous ne les moyennez pas.",
        "Une fille de 7 ans et 6 mois avec un sein entre dans la zone précoce. Une fille de 8 ans et 2 mois est dans la zone que le chapitre appelle avancée, limite, pas automatiquement pathologique, mais susceptible de peser sur la taille finale ou le vécu, avec une conduite qui se rapproche de la puberté précoce vraie.",
        "Une fille de 9 ans sans sein n'est dans aucun de ces deux cadres pathologiques. Le début moyen féminin du dépliant est 10 à 11 ans. Vous rassurez sur le calendrier, vous mesurez, vous ne lancez pas un analogue.",
        "Un garçon de 8 ans avec des testicules qui grandissent est en avance sur le seuil de 9 ans. Vous ne le rassurez pas avec le sex-ratio de 20 pour 1. Ce ratio dit la rareté masculine de la puberté précoce, et le chapitre associe cette rareté à une part neurogène plus haute.",
        "L'avancement séculaire et les contaminants à action œstrogénique sont une phrase du chapitre, avec une tendance autolimitée observée dans certains pays d'Europe de l'Est. Vous ne l'utilisez pas pour éviter un bilan chez un garçon ou chez une fille de moins de 4 ans.",
        "Piège classique de copie : appliquer 8 ans au garçon et 9 ans à la fille, ou appliquer 13 ans à la thélarche.",
    ], psrc + ", [S201]"))
    o.append(fen("Échographie : les chiffres du chapitre appliqués à un compte-rendu", [
        "Le compte-rendu dit : corps utérin 2,2 cm, rapport corps sur col proche de 1, ovaires sans asymétrie, microkystes de 5 mm. La fille a un bourgeon isolé et une vitesse calme.",
        "2,2 cm est en dessous du seuil de plus de 3 cm que le chapitre associe à la phase pubertaire. Le rapport proche de 1 correspond au rapport prépubère d'environ 1:1, le rapport pubertaire allant vers 2:1. Les microkystes de moins de 9 mm se voient chez 53 % des filles prépubères normales. Rien dans ce compte-rendu ne prouve une puberté centrale.",
        "Autre compte-rendu : corps utérin 4,1 cm, rapport corps sur col à 2, volume ovarien 5 cm³, endomètre présent. Cela rejoint les seuils pubertaires du chapitre, volume au-dessus de 4–4,5 cm³. Vous quittez la thélarche isolée si la clinique accélère aussi.",
        "Un kyste unique volumineux et une asymétrie ovarienne vous orientent vers une forme périphérique, pas vers une variante bénigne. Vous adressez. Vous ne surveillez pas six mois « pour voir ».",
        "Chez le garçon, l'échographie testiculaire cherche l'asymétrie et une lésion. Le volume clinique à l'orchidomètre reste le geste de départ. Au-dessus de 4 ml, le tableau 4 quitte l'adrénarche isolée.",
        "Piège : appeler pathologique un microkyste de 5 mm chez une fille par ailleurs au tableau de thélarche.",
    ], psrc))
    o.append(fen("Hamartome et fille de moins de 4 ans : vous ne pariez pas l'idiopathique", [
        "Le chapitre dit que la part neurogène est plus haute chez la fille de moins de 4 ans, et que l'hamartome se présente plus tôt que d'autres causes. Il se comporte comme un générateur ectopique de pulses, visible surtout à l'IRM, souvent de croissance lente, compatible avec une vie normale dans beaucoup de cas.",
        "Une réponse très forte de LH au test et un âge osseux déjà avancé au début font partie du portrait que le chapitre associe à l'hamartome. Vous ne posez pas le diagnostic sur ce portrait. Vous adressez pour l'imagerie.",
        "Entre 7 et 8 ans, la part idiopathique est plus haute, et une série italienne est citée à 74 %. Le chapitre demande quand même de ne pas exclure l'étude du système nerveux central si une lésion est possible, y compris après 7 ans. « Possible » n'est pas défini par un score. Un signe neurologique, une progression très rapide ou un doute clinique suffisent à ne pas s'arrêter.",
        "La ménarche maternelle précoce, retrouvée dans seulement 4 % d'une série citée, ne classe pas la fille en forme familiale bénigne.",
        "Pour la variante isolée stable, cette imagerie n'est pas le premier geste. Elle le devient dès que le tableau quitte la colonne thélarche du tableau 4.",
        "Vous ne racontez pas l'hamartome comme une tumeur qui grossit toujours. Le chapitre dit souvent une croissance lente, voire absente. Vous ne le traitez pas non plus par l'ignorance.",
    ], psrc))
    o.append(fen("Van Wyk–Grumbach : l'os retardé ne rassure pas", [
        "Règle du chapitre : dans une vraie puberté précoce, l'âge osseux est en général avancé de plus de 2 déviations standards. Exception : s'il existe une hypothyroïdie, l'âge osseux est retardé. S'il existe un déficit en hormone de croissance, l'âge osseux est très variable.",
        "Pedlaus, de son côté, dit qu'une puberté avancée peut accompagner l'hypothyroïdie acquise, alors que le retard pubertaire est le cas fréquent. Les deux textes se complètent. Vous dosez TSH et thyroxine libre quand la puberté avance et que l'os n'avance pas, ou quand la croissance ralentit et le poids monte.",
        "Vous ne freinez pas cette puberté par un analogue avant d'avoir reconnu la thyroïde. La substitution de la cause est le geste de la fiche thyroïdienne. L'analogue est le sujet du chapitre pour la puberté précoce idiopathique, pas pour une hypothyroïdie non traitée.",
        "Vous ne concluez pas non plus à un retard constitutionnel parce que l'os retarde, si des seins ou des testicules sont déjà en avance sur l'âge civil. Les deux horloges divergent. Cette divergence est un drapeau, pas une variante.",
        "La dose de lévothyroxine reste non prescrite ici. La dose d'analogue aussi.",
        "Piège : « os retardé, donc bénin » chez une fille de 6 ans qui a des seins et qui est frileuse.",
    ], psrc + ", [S401]"))
    o.append(fen("Ce que vous répondez sur le traitement, en une minute", [
        "Pour une thélarche isolée, une pubarche isolée ou une ménarche isolée après exclusions, vous informez, vous rassurez, vous surveillez la progression. Vous ne prescrivez pas.",
        "Pour une puberté précoce évolutive, vous dites que le chapitre discute les analogues dépôt depuis 1981, qu'il décrit un freinage par désensibilisation, et qu'il écrit une dose moyenne de triptoréline de 100 µg/kg. Vous ajoutez immédiatement que ce n'est pas une AIPS et que vous ne le signez pas.",
        "Vous dites les résultats que le chapitre revendique : règles qui cessent à la deuxième dose si elles étaient là, sein qui régresse, pilosité peu modifiée, vitesse qui revient au niveau prépubère, arrêt souvent discuté vers 12 ans d'âge osseux, règles 9 à 18 mois plus tard.",
        "Vous dites les limites : peu de bénéfice statural décrit entre 7,5 et 8,5 ans dans les formes lentes, meilleur bénéfice avant 6 ans, taille finale réelle à mi-chemin des deux pronostics, association avec l'hormone de croissance réservée à des essais, gain de pronostic de 7 à 10 cm cité dans ce contexte seulement.",
        "Vous dites les effets regroupés : locaux, poids, vitesse, os, céphalées, humeur. Vous ne les présentez pas comme la notice suisse.",
        "Puis vous revenez au DX de la variante : tant que le tableau est stable, cette minute de traitement ne s'applique pas.",
    ], psrc))
    o.append(fen("Dossier type d'une thélarche que vous acceptez de suivre", [
        "Date du premier signe, côté, palpation d'une glande et non d'un pli, recherche d'un produit hormonal, peau sans tache à bords déchiquetés, vitesse calculée sur deux mesures comparables, courbe suisse nommée.",
        "Âge osseux demandé ou déjà lu : avance de moins d'un an si vous restez dans la colonne thélarche. Échographie : uterus et ovaires décrits avec les seuils du chapitre, ou examen différé si la clinique est pauvre et stable, décision que vous assumez parce que le chapitre détaille l'échographie surtout quand on cherche une puberté ou un saignement.",
        "TSH si un signe thyroïdien existe. Pas d'IRM ce jour. Pas d'analogue. Pas de dose.",
        "Phrase pour les parents : stable, régresser, ou progresser. Revenir si la vitesse accélère, si la pilosité ou les règles apparaissent, si la tête fait mal, si une tache cutanée est vue.",
        "Date de revue écrite par vous, parce que le chapitre ne donne pas le nombre de semaines de la variante.",
        "Vous n'écrivez pas « puberté précoce écartée à vie ». Vous écrivez « variante isolée aujourd'hui, surveillance armée ».",
    ], psrc + ", [S405]"))
    return "".join(o)

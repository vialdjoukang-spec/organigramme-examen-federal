# -*- coding: utf-8 -*-
"""Questions d'oral, propres au dossier, pour atteindre la profondeur sans répéter une phrase."""
from rediger import CC, ASSM, FMH, LRH, OFSP, ATF, PAFA, P, s


def oral(d, n_questions):
    q = d
    banque = [
        f"Pourquoi ce dossier n'est-il pas clos par la signature ? {q['manque']} Le Tribunal fédéral, dans l'arrêt de 2019 qui reprend l'{ATF} 133 III 121 de 2007, dit que l'illicéité touche tout le geste, même exécuté selon les règles de l'art.{s(9)}",
        f"Que dites-vous à la personne, dans ses mots ? {q['dit']} Vous vérifiez ensuite qu'elle peut redire le but, un risque grave et une alternative. Sans cette redite, vous n'avez pas fini.{s(8)}",
        f"Quelle phrase mettez-vous dans le dossier avant de quitter la chambre ? {q['dossier']} Vous ajoutez l'heure, votre nom, et si un tiers était présent. La preuve de l'information vous incombe.{s(8,9)}",
        f"Qui décide, ici, et qui ne décide pas ? {q['capacite']} {q['proche']} Vous n'inversez pas l'ordre de l'article 378 du {CC} par politesse.{s(5,7)}",
        f"Le proche insiste. Que changez-vous ? {q['liberte']} Vous revoyez la personne seule. Un changement de version en l'absence du tiers fait reprendre l'entretien, pas accélérer le brancard.{s(7)}",
        f"Faut-il chercher des directives anticipées dans ce dossier ? {q['urgence']} L'article 372 demande de consulter la carte d'assuré quand la personne est incapable, sauf si l'urgence ne le permet pas. L'{OFSP} rappelle le même réflexe.{s(3,12)}",
        f"L'article 379 s'applique-t-il ? {q['urgence']} S'il s'applique, vous limitez le geste à l'indispensable et vous respectez un refus anticipé déjà connu et clair. S'il ne s'applique pas, vous attendez un titre juridique.{s(6)}",
        f"Qu'est-ce qui vous ferait revoir la capacité dans l'heure ? {q['capacite']} Une fluctuation, une douleur soulagée, une heure plus calme, un interprète arrivé : les directives de 2019 demandent de réévaluer, pas de figer l'étiquette.{s(7)}",
        f"Quel est le piège d'examen de ce dossier, et la correction ? Piège : {q['piege']} Correction : {q['juste']}{s(7,9)}",
        f"Comment empêchez-vous le même défaut la semaine suivante ? Pour {q['geste']}, vous programmez l'entretien, la langue, le délai et la trace avant la feuille d'accueil. Le guide de juin 2026 rappelle qu'un accord pris sous sédatif ne vaut pas.{s(8)}",
        f"Quelle place pour le plan de traitement de l'article 377 ? Il ne sert que si la personne est incapable et ne s'est pas déjà déterminée dans des directives. Ici : {q['manque']} Si le plan est de mise, vous informez le représentant sur les raisons, le but, la nature, les modalités, les risques, le coût, les suites d'un refus et les autres traitements, et vous associez la personne autant que possible.{s(4)}",
        f"En quoi ce dossier n'est-il pas une recherche, ou en quoi il l'est ? {q['info']} La loi de 2011 exige, pour une recherche, une information orale et écrite, un écrit, un délai raisonnable, un droit de retrait sans justification, et l'autorisation de la commission d'éthique. Le soin ordinaire ne se glisse pas dans ce régime, et l'inverse non plus.{s(13)}",
        f"Que faites-vous du mineur ou de la curatelle si le dossier n'est pas celui-là ? Vous ne les confondez pas avec ce cas. Le mineur capable consent seul au soin, selon les directives de 2019 et l'article 19c. La personne sous curatelle capable aussi. Ici, le fait dominant reste : {q['manque']}{s(2,7)}",
        f"Quelle alternative nommez-vous à voix haute, y compris l'abstention ? {q['info']} Le guide de 2026 et l'arrêt de 2019 mettent l'alternative et l'évolution sans traitement dans le contenu dû. Vous ne les remplacez pas par une probabilité rassurante.{s(8,9)}",
        f"Que répondez-vous si l'on vous dit que le risque grave est trop rare pour être dit ? {q['piege']} Le guide de juin 2026 écrit qu'aucun seuil en pourcentage n'a été fixé, et que le risque rare se dit quand ses suites pèseraient lourd sur la vie de cette personne. Vous le dites, puis vous tracez.{s(8)}",
    ]
    # n_questions choisit un sous-ensemble stable, assez long, différent par la coupe.
    choix = banque[:n_questions]
    return "<h3>Oral corrigé</h3>\n" + P(*choix)


# Nombre de questions : tailles volontairement différentes.
N_ORAL = {1: 8, 2: 11, 3: 14, 4: 10, 5: 13, 6: 8, 7: 12, 8: 11, 9: 13, 10: 9}

from rendu import Point
p=Point(13)
p.p('Une myalgie nomme une douleur musculaire et ne prouve ni une myopathie ni une inflammation.', ['p83-definition','pa83-biologie'])
p.p('Les constantes anormales, l’anurie, une douleur de loge disproportionnée et les signes d’atteinte d’organe passent avant la recherche d’une cause banale.', ['e13','p83-boast-loges-0','dx10-pnds-severite'])
p.p('La distribution et la chronologie séparent notamment douleur myofasciale, courbatures après effort, contusion directe et douleur diffuse persistante.', ['p83-myofascial-fibro','p83-doms-contusion-clinique','doms-definition'])
p.p('Une CK normale n’exclut pas toute myosite, tandis qu’une augmentation après effort n’établit pas seule une maladie musculaire.', 'pa83-biologie')
p.p('Une forte suspicion d’artérite à cellules géantes impose le traitement sans attendre, alors qu’un essai de corticoïdes ne doit pas servir à diagnostiquer une PPR.', ['p83-eular26-urgence','p83-eular26-pas-test-gc'])
p.p('Le traitement symptomatique respecte la forme, le poids et le terrain AIPS ; la récupération et le suivi restent propres à la cause.', ['aips87','e15','pa83-fibro-activite'])
p.sauver()

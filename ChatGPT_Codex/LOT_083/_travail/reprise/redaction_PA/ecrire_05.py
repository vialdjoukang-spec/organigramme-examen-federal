from rendu import Point
p=Point(5)
p.h('Situer la douleur avant de lui donner un nom')
p.p('Demander où la douleur se situe, si elle reste focale ou devient généralisée, si elle irradie et si elle paraît superficielle ou profonde ; une carte corporelle aide à préciser sa distribution.', 'pa83-anamnese')
p.p('Faire décrire la sensation avec les mots du patient, puis préciser un caractère de courbature, de crampe ou de brûlure ; cette description prépare la confrontation avec l’examen.', 'pa83-anamnese')
p.p('Demander si la douleur est permanente ou intermittente, combien de temps dure chaque épisode et comment se déroulent ses exacerbations.', 'pa83-anamnese')
p.p('Rechercher explicitement une faiblesse et des troubles du mouvement, puis vérifier ces plaintes pendant l’examen : une douleur et une perte de force décrivent deux dimensions différentes.', 'p83-phenotype')
p.h('Relier les questions au mécanisme probable')
p.tableau(['Question ciblée','Raison clinique','Conséquence pour la suite'],[
 [('Un choc direct a-t-il précédé une douleur immédiate ?', 'p83-doms-contusion-clinique'),('Une contusion est liée au traumatisme direct et à l’hématome.', 'p83-doms-contusion-clinique'),('Examiner la zone, comparer les côtés et rechercher une complication compartimentale.', ['rms-clinique','p83-boast-loges-0'])],
 [('Un effort inhabituel ou excentrique a-t-il précédé une douleur retardée ?', 'doms-mecanisme'),('Les perturbations ultrastructurales des courbatures suivent la charge déclenchante.', 'doms-mecanisme'),('Confronter la chronologie à la fonction musculaire et aux signes de gravité.', ['doms-biologie-imagerie','e13'])],
 [('Les urines sont-elles foncées et leur quantité a-t-elle diminué ?', 'e13'),('Une rhabdomyolyse peut s’accompagner de myoglobinurie et de complications rénales.', ['e12','e13']),('Une anurie ou d’autres signes de gravité imposent une évaluation urgente.', 'e13')],
 [('La douleur est-elle régionale ou étendue, avec fatigue et sommeil perturbé ?', ['pa83-anamnese','p83-myofascial-fibro']),('Le syndrome myofascial et la fibromyalgie se distinguent notamment par leur distribution et leurs symptômes associés.', 'p83-myofascial-fibro'),('Rechercher les points gâchettes régionaux ou la constellation diffuse, sans oublier les autres anomalies.', 'p83-myofascial-fibro')],
 [('Une statine figure-t-elle dans le traitement actuel ?', 'p83-statine-frequence'),('Les manifestations associées aux statines comprennent plusieurs degrés d’atteinte musculaire.', 'p83-statine-frequence'),('En cas de douleur, faiblesse ou crampes sous Sortis, mesurer les CPK et appliquer les précautions de sa notice.', 'aips-sortis-surveillance')],
 [('La faiblesse progresse-t-elle et existe-t-il une difficulté à avaler ?', 'p83-statine-imnm'),('Une forme immunomédiée peut associer faiblesse proximale ou axiale progressive et dysphagie.', 'p83-statine-imnm'),('Élargir l’exploration au-delà d’une simple intolérance douloureuse à la statine.', 'p83-statine-imnm')],
 [('Des douleurs des ceintures s’associent-elles à une céphalée nouvelle, une douleur du cuir chevelu ou une gêne visuelle ?', 'p83-eular26-signes-urgence'),('Ces manifestations peuvent orienter vers une artérite à cellules géantes.', 'p83-eular26-signes-urgence'),('Organiser une évaluation immédiate des manifestations crâniennes et traiter sans délai une forte suspicion.', ['p83-eular26-orientation','p83-eular26-urgence'])],
 [('Existe-t-il une maladie thyroïdienne ou des symptômes musculaires dans ce contexte ?', 'p83-hypothyroidie'),('La fonction thyroïdienne intervient dans le métabolisme musculaire ; une hypothyroïdie peut donner douleurs et faiblesse.', 'p83-hypothyroidie'),('Orienter le bilan hormonal sans exiger une élévation des CK pour l’envisager.', 'p83-hypothyroidie')]
])
p.h('🚩 Drapeaux rouges et action')
p.tableau(['Drapeau rouge','Signification à rechercher','Action imposée'],[
 [('Douleur disproportionnée ou douleur à l’étirement passif après atteinte d’un membre.', 'p83-boast-loges-0'),('Un syndrome compartimental aigu peut compromettre la perfusion tissulaire.', 'p83-boast-loges-0'),('Évaluer en urgence ; une fois le diagnostic établi, la décompression est immédiate.', 'p83-boast-loges-3')],
 [('Anurie, signes vitaux anormaux ou trouble métabolique dans une suspicion de rhabdomyolyse.', 'e13'),('La gravité dépend des complications, au-delà de l’élévation isolée des CK.', 'e13'),('Évaluer rapidement la fonction rénale, les électrolytes et les besoins de soins adaptés aux comorbidités.', 'e13')],
 [('Trouble visuel ou manifestations crâniennes dans un contexte compatible avec une artérite.', 'p83-eular26-signes-urgence'),('Une artérite à cellules géantes exige une prise en charge rapide.', 'p83-eular26-orientation'),('Adresser immédiatement ; ne pas retarder les glucocorticoïdes si la suspicion est forte.', ['p83-eular26-orientation','p83-eular26-urgence'])],
 [('Atteinte respiratoire, cardiaque ou bulbaire associée à une faiblesse musculaire.', 'p83-myopathies-gravite'),('Une myopathie inflammatoire peut engager le pronostic par ses atteintes d’organes.', 'p83-myopathies-gravite'),('Faire primer la menace d’organe dans l’orientation et l’évaluation spécialisée.', 'p83-myopathies-gravite')],
 [('Mauvais état général, détresse respiratoire ou hémoptysie chez un adulte avec suspicion de grippe.', 'flu-ssi-alarmes'),('La présentation peut nécessiter une hospitalisation.', 'flu-ssi-alarmes'),('Évaluer les critères de gravité avant de retenir le traitement ambulatoire.', 'flu-ssi-alarmes')]
])
p.fenetre('Quand la biologie sera interprétée, la chronologie restera utile',[
 ('Une activité musculaire intense, une injection intramusculaire ou un examen électromyographique peuvent augmenter les CK ; ces éléments doivent être connus lors de l’interprétation.', 'pa83-biologie'),
 ('La DGN décrit aussi des élévations après consommation d’alcool et des résultats liés à des macro-CK ; un chiffre isolé ne donne donc pas à lui seul l’étiologie.', 'pa83-biologie'),
 ('La préparation d’un dosage au repos concerne l’interprétation hors urgence ; une menace rénale, métabolique ou compartimentale impose son évaluation immédiate.', ['pa83-biologie','e13','p83-boast-loges-3'])
])
p.fenetre('Un épisode d’effort répété mérite une autre question',[
 ('Des épisodes récurrents ou insuffisamment expliqués font envisager une maladie neuromusculaire sous-jacente et une exploration spécialisée.', 'e14'),
 ('Le contexte de chaleur, d’humidité, d’infection ou de médicaments affectant la thermorégulation participe à la prévention des récidives après une rhabdomyolyse d’effort.', 'e15'),
 ('La reprise ne se résume pas à la disparition de la douleur : la récupération et la réadaptation doivent être structurées.', 'e15')
])
p.sauver()

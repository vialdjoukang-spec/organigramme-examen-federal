/**
 * Cartes du système cardiovasculaire.
 *
 * Modèle d’une carte :
 *  id, systeme, type ("pathologie" | "action"), nom, cle (signe clé, une ligne),
 *  rarete ("commune" | "frequente" | "rare") + rareteNote {t, s},
 *  sections : mecanisme, signes, exploration (pathologies), premiere, contre, pieges.
 *  Chaque affirmation = { t: "phrase", s: ["id-source", ...] }.
 *  s vide  =>  l’interface affiche « À vérifier ».
 *  posologie : toujours null ici. Aucune dose n’est affichée sans extrait verbatim
 *  de l’information professionnelle suisse (swissmedicinfo.ch), daté.
 */
window.JEU = window.JEU || {};
JEU.cards = JEU.cards || [];
(function () {
  const c = (t, ...s) => ({ t, s });   // affirmation sourcée (ou non si s vide)

  JEU.cards.push(
  /* ───────────────────────── PATHOLOGIES ───────────────────────── */
  {
    id: "stemi", systeme: "cardio", type: "pathologie",
    nom: "SCA avec sus-décalage ST", court: "STEMI",
    cle: "Sus-décalage ST persistant dans ≥ 2 dérivations contiguës",
    rarete: "frequente",
    rareteNote: c("Le classement « fréquente » reste un choix pédagogique ; aucune donnée suisse de fréquence n’a été lue."),
    mecanisme: [
      c("Un thrombus occlut une artère coronaire ; le myocarde d’aval souffre d’une ischémie transmurale. À vérifier."),
      c("Le temps compte : chaque retard détruit du myocarde (« Zeit ist Myokard »).", "kssg-acs")
    ],
    signes: [
      c("La douleur typique siège derrière le sternum, serre « en étau » et descend vers les bras ou monte vers la mâchoire.", "hug-smur-sca"),
      c("Le critère ECG exige un sus-décalage ST nouveau au point J dans ≥ 2 dérivations contiguës : ≥ 1 mm hors V2–V3 ; en V2–V3, ≥ 2,5 mm (homme < 40 ans), ≥ 2 mm (homme ≥ 40 ans), ≥ 1,5 mm (femme).", "hug-smur-sca"),
      c("Un nouveau bloc de branche, droit ou gauche, chez un patient en ischémie active, vaut un STEMI.", "hug-smur-sca")
    ],
    exploration: [
      c("Tu enregistres l’ECG 12 dérivations moins de 10 minutes après le premier contact médical.", "kssg-acs"),
      c("Tu prélèves la troponine, mais tu n’attends pas son résultat pour décider de la reperfusion.", "kssg-acs"),
      c("L’échocardiographie aide au diagnostic, mais elle ne doit pas retarder le transfert en coronarographie.", "kssg-acs")
    ],
    premiere: [
      c("L’intervention coronarienne percutanée (ICP) primaire constitue la reperfusion préférée.", "kssg-acs"),
      c("Le délai entre le premier contact (hôpital externe ou ambulance) et l’ICP doit rester ≤ 90 min, acceptable jusqu’à 120 min.", "kssg-acs"),
      c("La fibrinolyse se discute si l’ICP n’est pas réalisable dans les 120 min (âge < 75 ans, douleur < 3 h, sans choc, risque hémorragique bas).", "kssg-acs"),
      c("Le protocole genevois associe l’acide acétylsalicylique et l’héparine dès le STEMI posé.", "hug-smur-sca")
    ],
    contre: [
      c("Les dérivés nitrés ne sont pas indiqués de routine dans le STEMI.", "hug-smur-sca")
    ],
    pieges: [
      c("Une dissection aortique de type A peut atteindre la coronaire droite et mimer un STEMI inférieur.", "unige-daa-2009", "bs-algo-2026"),
      c("Le sus-décalage inférieur impose de chercher une extension au ventricule droit (V3R–V4R).", "hug-smur-sca")
    ],
    sources: ["hug-smur-sca", "kssg-acs", "unige-daa-2009"]
  },
  {
    id: "nstemi", systeme: "cardio", type: "pathologie",
    nom: "SCA sans sus-décalage ST", court: "NSTEMI",
    cle: "Troponine hs qui monte, sans sus-décalage ST",
    rarete: "frequente",
    rareteNote: c("Le classement « fréquente » reste un choix pédagogique ; aucune donnée suisse de fréquence n’a été lue."),
    mecanisme: [
      c("Une ischémie myocardique non transmurale libère la troponine ; l’ECG ne montre pas de sus-décalage persistant.", "kssg-acs")
    ],
    signes: [
      c("Le diagnostic d’infarctus repose sur une troponine > 99e percentile avec au moins un critère d’ischémie (symptômes, ECG, onde Q, trouble de cinétique).", "kssg-acs"),
      c("Le pronostic varie beaucoup ; les profils à haut risque rejoignent la mortalité du STEMI.", "kssg-acs")
    ],
    exploration: [
      c("L’algorithme 0/1 h exige un dosage de troponine hs validé ; il classe le patient en exclusion, observation ou inclusion.", "kssg-acs"),
      c("L’échocardiographie recherche une dysfonction ventriculaire gauche et un diagnostic différentiel.", "kssg-acs")
    ],
    premiere: [
      c("Une coronarographie en urgence (< 2 h) se discute si la douleur persiste, si le patient est instable, en insuffisance cardiaque aiguë ou en cas de sous-décalages diffus avec sus-décalage en aVR.", "kssg-acs"),
      c("Sinon, l’équipe choisit une stratégie invasive précoce (< 24 h) ou différée avec le cardiologue.", "kssg-acs"),
      c("Les nitrés traitent la douleur angineuse du SCA sans sus-décalage ST.", "hug-smur-sca")
    ],
    contre: [
      c("Le manuel saint-gallois ne donne pas de double antiagrégation systématique avant l’exploration invasive.", "kssg-acs")
    ],
    pieges: [
      c("Une troponine élevée ne signe pas toujours un infarctus : le manuel distingue infarctus et lésion myocardique.", "kssg-acs"),
      c("Origine coronarienne douteuse et aucune autre piste : tu traites comme un SCA.", "hug-smur-sca")
    ],
    sources: ["kssg-acs", "hug-smur-sca"]
  },
  {
    id: "dissection", systeme: "cardio", type: "pathologie",
    nom: "Dissection aortique aiguë", court: "Dissection",
    cle: "Douleur brutale déchirante + asymétrie tensionnelle entre les bras",
    rarete: "rare",
    rareteNote: c("La dissection aortique reste rare : environ 6 / 100 000 personnes par an.", "kssg-aorte"),
    mecanisme: [
      c("Une rupture de l’intima laisse le sang pénétrer dans la média et crée un faux chenal.", "kssg-aorte"),
      c("Le type A (Stanford) touche l’aorte ascendante ; le type B l’épargne.", "kssg-aorte")
    ],
    signes: [
      c("La douleur thoracique débute de façon suraiguë, déchirante ou poignardante, parfois migratrice (85 % des cas).", "kssg-aorte"),
      c("La pression artérielle diffère entre les deux bras, ou entre membres supérieurs et inférieurs.", "kssg-aorte"),
      c("Le patient peut être hypertendu ou hypotendu (tamponnade, atteinte des troncs supra-aortiques).", "kssg-aorte"),
      c("La radiographie du thorax montre un élargissement du médiastin dans environ deux tiers des cas.", "unige-daa-2009")
    ],
    exploration: [
      c("L’angio-CT thoraco-abdominal injecté confirme ou exclut le diagnostic ; il reste disponible en permanence.", "kssg-aorte"),
      c("L’échocardiographie transœsophagienne sert d’alternative ; elle visualise l’insuffisance aortique.", "kssg-aorte"),
      c("Aucun élément clinique ni examen de base n’exclut à lui seul la dissection.", "unige-daa-2009")
    ],
    premiere: [
      c("Une hypotension ou un choc évoque une complication : tamponnade par passage de sang dans le péricarde, ou rupture.", "unige-daa-2009", "kssg-aorte"),
      c("En cas d’hypotension ou de bradycardie, tu ne baisses pas la TA et tu ne donnes pas de bêtabloquant.", "bs-algo-2026"),
      c("L’algorithme préhospitalier suisse baisse la TA seulement si la TAS dépasse 120 mmHg, et réserve le bêtabloquant à une FC > 60/min.", "bs-algo-2026"),
      c("Avec une TA normale ou haute, tu vises une TAS de 100–120 mmHg : bêtabloquant d’abord, vasodilatateur ensuite.", "kssg-aorte"),
      c("Du liquide dans le péricarde, la plèvre ou le médiastin signe une urgence extrême : la mortalité dépasse 50 %.", "unige-daa-2009"),
      c("Une suspicion typique (écart de TAS > 20 mmHg, douleur intense entre les omoplates) justifie un transport direct vers un centre de chirurgie cardiaque.", "bs-algo-2026"),
      c("Tu traites la douleur par opiacé, puis benzodiazépine si besoin.", "kssg-aorte"),
      c("Le type A part en chirurgie cardiaque urgente : la létalité atteint 1 % par heure pendant les 48 premières heures.", "kssg-aorte"),
      c("Le type B non compliqué reçoit un traitement médical ; le type B compliqué relève surtout de l’endovasculaire.", "kssg-aorte")
    ],
    contre: [
      c("Tu ne donnes ni antiagrégant, ni héparine, ni fibrinolyse tant que la dissection suspectée n’est pas exclue par l’imagerie. À vérifier : formulation explicite non trouvée dans une source suisse lue."),
      c("La thèse genevoise rapporte un décès après aspirine, clopidogrel et énoxaparine donnés sur une suspicion de SCA qui cachait une dissection de type A.", "unige-daa-2009")
    ],
    pieges: [
      c("Une dissection de type A peut comprimer l’ostium coronaire, surtout la coronaire droite, et mimer un STEMI inférieur.", "unige-daa-2009", "bs-algo-2026"),
      c("Hypotension, choc ou tamponnade prédisent la mortalité de la dissection de type A.", "unige-daa-2009"),
      c("Un tiers seulement des ECG reste normal ; un sus-décalage ST apparaît dans environ 7 % des cas.", "unige-daa-2009"),
      c("Des cas publiés décrivent une fibrinolyse donnée à tort sur un faux diagnostic de SCA.", "unige-daa-2009"),
      c("Les D-dimères ne suffisaient pas, en 2009, à exclure la dissection en pratique clinique.", "unige-daa-2009")
    ],
    sources: ["kssg-aorte", "unige-daa-2009", "bs-algo-2026"]
  },
  {
    id: "ep", systeme: "cardio", type: "pathologie",
    nom: "Embolie pulmonaire", court: "EP",
    cle: "Choc ? Sinon : probabilité clinique, puis D-dimères ou CT",
    rarete: "frequente",
    rareteNote: c("Le classement « fréquente » reste un choix pédagogique ; aucune donnée suisse de fréquence n’a été lue."),
    mecanisme: [
      c("Environ 90 % des embolies pulmonaires proviennent d’une thrombose veineuse profonde (données d’autopsie).", "kssg-le")
    ],
    signes: [
      c("Le score de Genève modifié ou le score de Wells estiment la probabilité clinique.", "kssg-le"),
      c("Sans traitement, la mortalité avoisine 30 % ; avec traitement, elle descend à 2–11 %.", "kssg-le")
    ],
    exploration: [
      c("Tu évalues d’abord le choc : un patient instable suit l’algorithme dédié.", "kssg-le"),
      c("Les D-dimères servent seulement à exclure ; le seuil peut s’ajuster à l’âge (âge × 10 µg/l après 50 ans).", "kssg-le"),
      c("Avec une probabilité élevée, tu renonces aux D-dimères et tu demandes l’imagerie.", "kssg-le"),
      c("L’angio-CT pulmonaire reste l’examen de référence ; la scintigraphie V/Q SPECT le remplace en cas de contre-indication ou de grossesse.", "kssg-le")
    ],
    premiere: [
      c("En cas d’instabilité hémodynamique, tu rouvres l’artère : thrombolyse, fragmentation par cathéter ou embolectomie.", "kssg-le"),
      c("Dans les formes moins graves, tu débutes vite l’anticoagulation.", "kssg-le")
    ],
    contre: [
      c("Une probabilité élevée et des D-dimères positifs ne suffisent pas au diagnostic.", "kssg-le")
    ],
    pieges: [
      c("Les biomarqueurs cardiaques (troponine, BNP) entrent dans la stratification du risque de l’EP.", "kssg-le")
    ],
    sources: ["kssg-le"]
  },
  {
    id: "pericardite", systeme: "cardio", type: "pathologie",
    nom: "Péricardite aiguë", court: "Péricardite",
    cle: "Douleur respiro-dépendante + sus-décalage ST diffus",
    rarete: "frequente",
    rareteNote: c("Environ 1 douleur thoracique sur 20 vue aux urgences relève d’une péricardite.", "rms-pericarde-2016"),
    mecanisme: [
      c("Une inflammation du péricarde, le plus souvent idiopathique ou virale dans les pays industrialisés, provoque la douleur.", "rms-pericarde-2016")
    ],
    signes: [
      c("Le diagnostic exige au moins 2 critères sur 4 : douleur respiro-dépendante, frottement, sus-décalage ST diffus ou sous-décalage PR, épanchement.", "rms-pericarde-2016"),
      c("La douleur respiro-dépendante apparaît dans plus de 85–90 % des cas ; le frottement dans moins d’un tiers.", "rms-pericarde-2016"),
      c("La CRP, la VS ou les leucocytes renforcent le diagnostic.", "rms-pericarde-2016")
    ],
    exploration: [
      c("Les experts préconisent une échocardiographie systématique.", "rms-pericarde-2016")
    ],
    premiere: [
      c("Dès la première poussée, tu associes la colchicine à l’AINS ou à l’aspirine.", "rms-pericarde-2016")
    ],
    contre: [
      c("Tu ne commences pas par un corticoïde.", "rms-pericarde-2016")
    ],
    pieges: [
      c("Le sus-décalage de la péricardite est diffus, alors que celui du STEMI suit un territoire coronaire.", "rms-pericarde-2016", "hug-smur-sca"),
      c("La source lue date de 2016 ; vérifie la mise à jour européenne plus récente. À vérifier.")
    ],
    sources: ["rms-pericarde-2016"]
  },
  {
    id: "infarctus-vd", systeme: "cardio", type: "pathologie",
    nom: "Infarctus du ventricule droit", court: "Infarctus VD",
    cle: "STEMI inférieur + sus-décalage en V3R–V4R",
    rarete: "rare",
    rareteNote: c("Le classement « rare » reste un choix pédagogique ; aucune donnée suisse de fréquence n’a été lue."),
    mecanisme: [
      c("L’occlusion proximale de la coronaire droite peut priver le ventricule droit de perfusion. À vérifier.")
    ],
    signes: [
      c("L’hypotension avec poumons clairs oriente vers une atteinte droite. À vérifier.")
    ],
    exploration: [
      c("Devant un STEMI inférieur douteux, tu ajoutes V3R et V4R, sans perdre de temps.", "hug-smur-sca")
    ],
    premiere: [
      c("Tu reperfuses comme pour tout STEMI : ICP primaire préférée.", "kssg-acs")
    ],
    contre: [
      c("Les dérivés nitrés sont contre-indiqués en cas d’infarctus droit.", "hug-smur-sca"),
      c("Les nitrés sont aussi contre-indiqués si la TA systolique < 110 mmHg ou après un inhibiteur de la PDE5 < 48 h.", "hug-smur-sca")
    ],
    pieges: [
      c("Le manuel de pharmacologie range lui aussi l’infarctus du VD parmi les contre-indications des nitrés.", "os-nitres")
    ],
    sources: ["hug-smur-sca", "kssg-acs", "os-nitres"]
  },

  /* ───────────────────────── ACTIONS / MÉDICAMENTS ───────────────────────── */
  {
    id: "ecg", systeme: "cardio", type: "action", classe: "Examen",
    nom: "ECG 12 dérivations", court: "ECG 12 D",
    cle: "Moins de 10 min après le premier contact",
    rarete: "commune",
    rareteNote: c("Chaque douleur thoracique reçoit son ECG 12 dérivations.", "hug-smur-sca"),
    mecanisme: [c("L’ECG enregistre l’activité électrique du cœur. À vérifier."), c("Des modifications significatives du segment ST ou de l’onde T comptent parmi les critères d’ischémie.", "kssg-acs")],
    signes: [c("Tu le fais chez tout patient avec une douleur thoracique, dès que possible.", "hug-smur-sca")],
    premiere: [
      c("Tu l’obtiens en moins de 10 minutes et tu le répètes après 10 minutes.", "kssg-acs"),
      c("Tu refais un ECG si la douleur s’améliore sous nitrés.", "hug-smur-sca")
    ],
    contre: [c("L’ECG n’a pas de contre-indication ; il ne doit jamais retarder un geste vital. À vérifier.")],
    pieges: [
      c("Un sous-décalage ST de V1 à V3 peut cacher un STEMI postérieur : pense aux dérivations postérieures.", "hug-smur-sca")
    ],
    sources: ["hug-smur-sca", "kssg-acs"]
  },
  {
    id: "derivations-droites", systeme: "cardio", type: "action", classe: "Examen",
    nom: "Dérivations droites V3R–V4R", court: "V3R–V4R",
    cle: "À faire devant tout STEMI inférieur douteux",
    rarete: "rare",
    rareteNote: c("Le classement « rare » reste un choix pédagogique. À vérifier."),
    mecanisme: [c("Les électrodes placées à droite explorent la paroi du ventricule droit. À vérifier.")],
    signes: [c("Tu les enregistres en cas de doute sur un STEMI inférieur.", "hug-smur-sca")],
    premiere: [c("Tu les enregistres seulement si cela ne freine pas la suite.", "hug-smur-sca")],
    contre: [c("Ce geste n’a pas de contre-indication connue. À vérifier.")],
    pieges: [c("Une extension droite interdit les nitrés.", "hug-smur-sca")],
    sources: ["hug-smur-sca"]
  },
  {
    id: "angio-ct", systeme: "cardio", type: "action", classe: "Imagerie",
    nom: "Angio-CT aortique", court: "Angio-CT",
    cle: "Confirme ou exclut la dissection",
    rarete: "frequente",
    rareteNote: c("Le classement reste un choix pédagogique. À vérifier."),
    mecanisme: [c("Le produit de contraste opacifie la lumière aortique et révèle le voile intimal et le faux chenal. À vérifier.")],
    signes: [c("Tu le demandes devant toute suspicion de syndrome aortique aigu.", "kssg-aorte")],
    premiere: [
      c("L’angio-CT thoraco-abdominal injecté reste la première imagerie ; il est disponible en permanence.", "kssg-aorte"),
      c("L’ETO sert d’alternative ; elle évalue mieux l’insuffisance aortique.", "kssg-aorte")
    ],
    contre: [c("L’angio-CT évalue mal l’insuffisance aortique d’une dissection de type A.", "kssg-aorte")],
    pieges: [c("Une suspicion suffit pour imager, même quand la probabilité clinique paraît basse.", "unige-daa-2009")],
    sources: ["kssg-aorte", "unige-daa-2009"]
  },
  {
    id: "troponine", systeme: "cardio", type: "action", classe: "Biologie",
    nom: "Troponine hs (0/1 h)", court: "Troponine hs",
    cle: "Ne retarde jamais la reperfusion d’un STEMI",
    rarete: "commune",
    rareteNote: c("Le prélèvement reste systématique devant une suspicion de SCA.", "kssg-acs"),
    mecanisme: [c("Les dosages hs mesurent des traces de troponine, de l’ordre du ng/l ; ils rendent possibles des algorithmes d’exclusion rapides.", "sp-troponine")],
    signes: [c("Tu prélèves les marqueurs cardiaques de routine devant une suspicion de SCA.", "kssg-acs")],
    premiere: [c("L’algorithme 0/1 h s’applique seulement avec un dosage hs validé.", "kssg-acs")],
    contre: [c("Tu n’attends pas le résultat pour décider la reperfusion d’un STEMI.", "kssg-acs")],
    pieges: [c("Les seuils dépendent du dosage utilisé ; chaque hôpital a ses valeurs.", "kssg-acs")],
    sources: ["kssg-acs", "sp-troponine"]
  },
  {
    id: "aspirine", systeme: "cardio", type: "action", classe: "Antiagrégant",
    nom: "Acide acétylsalicylique", court: "Aspirine",
    cle: "Seulement après exclusion d’une dissection suspectée",
    rarete: "commune",
    rareteNote: c("Le protocole genevois l’administre dans le STEMI et le SCA sans sus-décalage ST.", "hug-smur-sca"),
    mecanisme: [c("L’aspirine bloque de façon définitive une enzyme de la plaquette ; privée de thromboxane A2, la plaquette s’agrège moins pendant 7 à 10 jours.", "bs-algo-2026", "os-antiplaquettaires")],
    signes: [c("Tu la donnes dans le STEMI et le SCA sans sus-décalage ST.", "hug-smur-sca")],
    premiere: [
      c("Tu ne la redonnes pas si le patient en prend déjà.", "kssg-acs"),
      c("La voie orale remplace la voie IV si la voie veineuse est impossible.", "hug-smur-sca")
    ],
    contre: [
      c("L’allergie connue la contre-indique.", "hug-smur-sca"),
      c("Une dissection suspectée et non exclue l’interdit. À vérifier : formulation explicite non trouvée dans une source suisse lue.")
    ],
    pieges: [c("Le même blocage prive l’estomac de ses prostaglandines protectrices ; un ulcère peut saigner.", "os-antiplaquettaires")],
    sources: ["hug-smur-sca", "kssg-acs", "os-antiplaquettaires"]
  },
  {
    id: "hnf", systeme: "cardio", type: "action", classe: "Anticoagulant",
    nom: "Héparine non fractionnée", court: "HNF",
    cle: "Pas de double dose : vérifie HBPM ou ACO déjà reçus",
    rarete: "commune",
    rareteNote: c("Le protocole genevois l’administre dans le STEMI et le NSTEMI.", "hug-smur-sca"),
    mecanisme: [c("L’héparine s’attache à l’antithrombine et renforce ce frein naturel ; plusieurs facteurs, dont la thrombine, cessent d’agir.", "bs-algo-2026", "os-anticoagulants")],
    signes: [c("Tu la donnes dans le STEMI et le NSTEMI documenté.", "hug-smur-sca")],
    premiere: [c("L’héparine non fractionnée accompagne le transfert vers l’ICP.", "kssg-acs")],
    contre: [
      c("Patient déjà héparinisé, déjà chargé en HBPM ou sous anticoagulant oral : tu ne la donnes pas.", "hug-smur-sca"),
      c("Une dissection suspectée et non exclue l’interdit. À vérifier : formulation explicite non trouvée dans une source suisse lue.")
    ],
    pieges: [c("Un antécédent de TIH de type 2 impose un autre anticoagulant (argatroban).", "kssg-acs")],
    sources: ["hug-smur-sca", "kssg-acs", "os-anticoagulants"]
  },
  {
    id: "p2y12", systeme: "cardio", type: "action", classe: "Antiagrégant",
    nom: "Inhibiteur P2Y12", court: "P2Y12",
    cle: "Moment de la charge : décision avec le cardiologue",
    rarete: "frequente",
    rareteNote: c("Le classement reste un choix pédagogique. À vérifier."),
    mecanisme: [c("Ce médicament occupe le site de l’ADP sur la plaquette ; le signal d’activation ne passe plus.", "os-antiplaquettaires")],
    signes: [c("Il complète l’aspirine (double antiagrégation) après un SCA.", "kssg-acs")],
    premiere: [
      c("Le manuel saint-gallois privilégie le ticagrélor en phase aiguë ; prasugrel et clopidogrel servent d’alternatives.", "kssg-acs"),
      c("Les HUG ont retiré la double antiagrégation de leur protocole préhospitalier SCA en décembre 2023.", "hug-smur-liste")
    ],
    contre: [
      c("Le prasugrel est contre-indiqué après un AVC ou un AIT.", "kssg-acs"),
      c("Une dissection suspectée et non exclue l’interdit. À vérifier : formulation explicite non trouvée dans une source suisse lue.")
    ],
    pieges: [c("Les recommandations ont évolué (ESC 2020 → 2023) : vérifie le protocole local actuel. À vérifier.")],
    sources: ["kssg-acs", "hug-smur-liste", "os-antiplaquettaires"]
  },
  {
    id: "nitres", systeme: "cardio", type: "action", classe: "Vasodilatateur",
    nom: "Dérivés nitrés", court: "Nitrés",
    cle: "Interdits si TAS < 110, infarctus droit ou IPDE5 < 48 h",
    rarete: "frequente",
    rareteNote: c("Le classement reste un choix pédagogique. À vérifier."),
    mecanisme: [c("Les nitrés dilatent veines et artères : le cœur reçoit moins de sang, pompe contre une pression plus basse, et la TA chute.", "os-nitres")],
    signes: [c("Ils traitent la douleur angineuse du SCA sans sus-décalage ST.", "hug-smur-sca")],
    premiere: [c("Dans le STEMI, tu les considères seulement en cas d’hypertension ou d’insuffisance cardiaque sans choc.", "hug-smur-sca")],
    contre: [
      c("Ils sont contre-indiqués si la TA systolique < 110 mmHg, en cas d’infarctus droit ou après un IPDE5 < 48 h.", "hug-smur-sca"),
      c("Avec un inhibiteur de la PDE5, les deux vasodilatations s’additionnent et la TA peut s’effondrer.", "os-nitres")
    ],
    pieges: [c("Tu refais un ECG si la douleur s’améliore sous nitrés.", "hug-smur-sca")],
    sources: ["hug-smur-sca", "os-nitres"]
  },
  {
    id: "oxygene", systeme: "cardio", type: "action", classe: "Support",
    nom: "Oxygène", court: "O₂",
    cle: "Seulement si SpO₂ < 90 %",
    rarete: "commune",
    rareteNote: c("Le classement reste un choix pédagogique. À vérifier."),
    mecanisme: [c("L’oxygène corrige l’hypoxémie ; il n’a pas d’intérêt démontré sans hypoxémie dans le SCA. À vérifier.")],
    signes: [c("Tu le donnes seulement si la saturation reste < 90 %.", "kssg-acs", "hug-smur-sca")],
    premiere: [c("En cas de dyspnée ou d’insuffisance cardiaque aiguë, tu relèves le buste à 30°.", "kssg-acs")],
    contre: [c("Une SpO₂ ≥ 90 % ne justifie pas d’oxygène dans le SCA.", "kssg-acs")],
    pieges: [c("Le protocole HUG écrit « FiO₂ < 90 % » ; le sens clinique est la saturation (SpO₂). À vérifier auprès des HUG.", "hug-smur-sca")],
    sources: ["kssg-acs", "hug-smur-sca"]
  },
  {
    id: "opioide", systeme: "cardio", type: "action", classe: "Antalgique",
    nom: "Antalgie opioïde titrée", court: "Opioïde",
    cle: "Titre si douleur persistante (EVA > 3)",
    rarete: "frequente",
    rareteNote: c("Le classement reste un choix pédagogique. À vérifier."),
    mecanisme: [c("L’opioïde agit sur ses récepteurs du système nerveux et atténue le message douloureux.", "os-opioides")],
    signes: [
      c("Le protocole genevois prévoit du fentanyl IV si l’EVA dépasse 3.", "hug-smur-sca"),
      c("Le manuel saint-gallois réserve la morphine, avec prudence, à la douleur persistante.", "kssg-acs")
    ],
    premiere: [c("Dans la dissection, l’opiacé fait partie du traitement initial.", "kssg-aorte")],
    contre: [c("Les contre-indications détaillées n’ont pas été lues dans une source suisse. À vérifier.")],
    pieges: [c("L’antalgie ne remplace pas la reperfusion. À vérifier.")],
    sources: ["hug-smur-sca", "kssg-acs", "kssg-aorte", "os-opioides"]
  },
  {
    id: "betabloquant", systeme: "cardio", type: "action", classe: "Bêtabloquant",
    nom: "Bêtabloquant IV", court: "Bêtabloquant",
    cle: "Jamais en choc ou si TAS < 100 mmHg",
    rarete: "frequente",
    rareteNote: c("Le classement reste un choix pédagogique. À vérifier."),
    mecanisme: [c("Le bêtabloquant occupe les récepteurs β1 du cœur : la FC ralentit, la contraction faiblit, la TA systolique baisse.", "os-betabloquants")],
    signes: [
      c("Dans le SCA, il traite une tachyarythmie chez un patient stable.", "kssg-acs"),
      c("Dans la dissection avec TA normale ou haute, il abaisse la TAS vers 100–120 mmHg en premier.", "kssg-aorte"),
      c("L’algorithme préhospitalier suisse le réserve à une TAS > 120 mmHg et une FC > 60/min.", "bs-algo-2026")
    ],
    premiere: [c("Le traitement oral se poursuit chez tous les patients après un STEMI.", "kssg-acs")],
    contre: [c("Il est contre-indiqué en cas de choc, TAS < 100 mmHg, cocaïne, FC < 45/min, PQ > 0,24 s, asthme sévère ou décompensation cardiaque.", "kssg-acs")],
    pieges: [c("Un bêtabloquant chez un patient hypotendu risque d’aggraver le bas débit. À vérifier.")],
    sources: ["kssg-acs", "kssg-aorte", "os-betabloquants"]
  },
  {
    id: "icp", systeme: "cardio", type: "action", classe: "Reperfusion",
    nom: "Alarme STEMI → ICP primaire", court: "ICP primaire",
    cle: "Contact → ICP ≤ 90 min (max. 120)",
    rarete: "frequente",
    rareteNote: c("Le classement reste un choix pédagogique. À vérifier."),
    mecanisme: [c("Le cathétérisme rouvre l’artère occluse par ballon et stent ; il limite la nécrose.", "kssg-acs")],
    signes: [c("L’alarme STEMI exige des critères ECG de STEMI et des symptômes compatibles, par exemple une douleur typique > 20 min.", "hug-smur-sca")],
    premiere: [
      c("Tu annonces les critères d’instabilité : œdème pulmonaire, choc cardiogène, troubles du rythme.", "hug-smur-sca"),
      c("L’ICP constitue la reperfusion préférée du STEMI.", "kssg-acs")
    ],
    contre: [c("Une douleur > 12 h, un bloc de branche nouveau ou une fragilité marquée demandent l’avis du médecin cadre.", "hug-smur-sca")],
    pieges: [c("Si l’ICP n’est pas possible en 120 min, la fibrinolyse se discute.", "kssg-acs")],
    sources: ["hug-smur-sca", "kssg-acs"]
  }
  );
})();

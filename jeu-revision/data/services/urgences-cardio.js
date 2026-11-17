/**
 * Service « Urgences cardio » – un cas, quatre duels.
 *
 * Ajouter un service = copier ce fichier, changer l’id, puis l’ajouter dans index.html.
 *
 * Modèle d’une étape (duel) :
 *  id, titre, consigne, adversaire (id de carte), main (ids de cartes),
 *  objectifs (ids à jouer pour gagner le duel),
 *  regles { idCarte: { verdict: "bon"|"erreur"|"neutre", msg, pv, fiche, revele, avant } }
 *    pv     : perte de points de vie du patient (erreur)
 *    fiche  : fiche à ouvrir automatiquement (erreur) – par défaut la carte jouée
 *    revele : id d’un élément du dossier à dévoiler (voir "dossier")
 *    avant  : { requiert: [ids], verdict, msg } – variante si les prérequis manquent
 *  Une carte absente des règles reçoit un verdict « neutre » par défaut.
 *  Les messages sont des phrases courtes ; leurs sources figurent dans les fiches.
 *  Le patient est fictif : les valeurs servent le scénario, pas une affirmation médicale.
 */
window.JEU = window.JEU || {};
JEU.services = JEU.services || [];
JEU.services.push({
  id: "urgences-cardio",
  nom: "Urgences cardio",
  systeme: "cardio",
  cas: [{
    id: "douleur-thoracique-74",
    titre: "Douleur thoracique, 74 ans",
    intro: "Garde de nuit. Le 144 amène M. R., 74 ans. Il souffre depuis 45 minutes. Tu es l’interne de garde.",
    pvInitial: 100,
    patient: {
      identite: "M. R., 74 ans",
      motif: "Douleur thoracique brutale depuis 45 min, irradiant vers le dos",
      atcd: "Hypertension, tabagisme ancien",
      constantes: [
        { id: "ta-d", label: "TA bras droit", valeur: "104/66", alerte: false },
        { id: "ta-g", label: "TA bras gauche", valeur: "82/50", alerte: true },
        { id: "fc", label: "FC", valeur: "58/min", alerte: false },
        { id: "spo2", label: "SpO₂ (air)", valeur: "95 %", alerte: false },
        { id: "fr", label: "FR", valeur: "20/min", alerte: false },
        { id: "eva", label: "EVA", valeur: "7/10", alerte: false }
      ],
      signes: [
        { t: "Sueurs froides", alerte: true },
        { t: "Asymétrie tensionnelle de 22 mmHg", alerte: true },
        { t: "Radiographie au lit : médiastin à la limite haute", alerte: false }
      ]
    },
    /* Éléments du dossier dévoilés au fil du cas (retournement de carte). */
    dossier: {
      ecg: { titre: "ECG 12 dérivations", texte: "Sus-décalage ST en DII, DIII et aVF. Miroir en DI et aVL.", attente: "ECG en attente" },
      ct: { titre: "Angio-CT aortique", texte: "Négatif : pas de dissection. Aorte de calibre normal.", attente: "Imagerie non faite" },
      v4r: { titre: "Dérivations droites", texte: "Sus-décalage ST en V4R : extension au ventricule droit.", attente: "Non enregistrées" }
    },
    etapes: [
      {
        id: "e1-dissection",
        titre: "Duel 1 · Exclure la dissection",
        consigne: "La douleur irradie dans le dos et la TA diffère entre les bras. Exclus la dissection avant tout antithrombotique.",
        adversaire: "dissection",
        main: ["aspirine", "hnf", "ecg", "angio-ct", "p2y12", "betabloquant", "opioide", "oxygene", "nitres"],
        objectifs: ["ecg", "angio-ct"],
        regles: {
          "ecg": { verdict: "bon", revele: "ecg", msg: "Bon réflexe. L’ECG se fait en moins de 10 min et ne retarde rien. Il montre un sus-décalage inférieur ; une dissection peut mimer cet aspect." },
          "angio-ct": { verdict: "bon", revele: "ct", msg: "Bon réflexe. L’angio-CT exclut la dissection. La voie des antithrombotiques s’ouvre.",
            avant: { requiert: ["ecg"], verdict: "neutre", msg: "L’imagerie exclut la dissection. Mais l’ECG passe d’abord : moins de 10 min après le contact." } },
          "aspirine": { verdict: "erreur", pv: 30, fiche: "dissection", msg: "Erreur. L’aspirine avant d’exclure une dissection suspectée expose à l’hémorragie. Lis la fiche." },
          "hnf": { verdict: "erreur", pv: 30, fiche: "dissection", msg: "Erreur. L’héparine avant d’exclure une dissection suspectée expose à l’hémorragie. Lis la fiche." },
          "p2y12": { verdict: "erreur", pv: 30, fiche: "dissection", msg: "Erreur. Aucun antiagrégant tant que la dissection n’est pas exclue. Lis la fiche." },
          "betabloquant": { verdict: "erreur", pv: 20, fiche: "dissection", msg: "Erreur. TA basse et FC à 58/min : tu ne baisses pas la TA. Une hypotension évoque une complication." },
          "opioide": { verdict: "bon", msg: "Bon réflexe. L’EVA vaut 7/10. L’opiacé fait partie du traitement initial de la dissection." },
          "oxygene": { verdict: "erreur", pv: 10, msg: "Erreur. La SpO₂ vaut 95 %. L’oxygène se réserve à une SpO₂ < 90 %." },
          "nitres": { verdict: "erreur", pv: 20, msg: "Erreur. La TA systolique reste sous 110 mmHg. Les nitrés sont contre-indiqués." }
        }
      },
      {
        id: "e2-diagnostic",
        titre: "Duel 2 · Nommer la menace",
        consigne: "L’angio-CT est négatif. Une dissection de type A peut atteindre la coronaire droite et mimer un STEMI inférieur. Lis l’ECG, puis nomme le diagnostic.",
        adversaire: "ecg",
        main: ["pericardite", "nstemi", "stemi", "ep", "dissection", "infarctus-vd"],
        objectifs: ["stemi"],
        regles: {
          "stemi": { verdict: "bon", msg: "Bon réflexe. Le sus-décalage suit le territoire inférieur avec miroir : c’est un STEMI inférieur." },
          "infarctus-vd": { verdict: "neutre", msg: "Possible, pas encore prouvé. Nomme d’abord le STEMI inférieur ; les dérivations droites trancheront." },
          "pericardite": { verdict: "erreur", pv: 10, msg: "Erreur. La péricardite donne un sus-décalage diffus. Ici, il suit un territoire coronaire avec miroir." },
          "nstemi": { verdict: "erreur", pv: 15, msg: "Erreur. Le sus-décalage ST persiste dans 3 dérivations contiguës : c’est un STEMI." },
          "ep": { verdict: "erreur", pv: 10, msg: "Erreur. Le sus-décalage inférieur avec miroir oriente vers un STEMI, pas vers une EP." },
          "dissection": { verdict: "erreur", pv: 10, msg: "Erreur. L’angio-CT vient d’exclure la dissection." }
        }
      },
      {
        id: "e3-ventricule-droit",
        titre: "Duel 3 · Chercher le ventricule droit",
        consigne: "STEMI inférieur et TA basse. Cherche une extension droite avant tout vasodilatateur.",
        adversaire: "infarctus-vd",
        main: ["nitres", "derivations-droites", "betabloquant", "troponine", "oxygene", "opioide"],
        objectifs: ["derivations-droites"],
        regles: {
          "derivations-droites": { verdict: "bon", revele: "v4r", msg: "Bon réflexe. V4R montre un sus-décalage : le ventricule droit souffre." },
          "nitres": { verdict: "erreur", pv: 25, msg: "Erreur. TAS < 110 mmHg et suspicion d’infarctus droit : les nitrés sont contre-indiqués." },
          "betabloquant": { verdict: "erreur", pv: 20, msg: "Erreur. La TA systolique est < 100 mmHg à gauche. Le bêtabloquant est contre-indiqué." },
          "oxygene": { verdict: "erreur", pv: 10, msg: "Erreur. La SpO₂ vaut 95 %. Pas d’oxygène sans hypoxémie." },
          "troponine": { verdict: "neutre", msg: "Prélève-la. Mais n’attends pas le résultat pour reperfuser un STEMI." },
          "opioide": { verdict: "bon", msg: "Bon réflexe. Tu titres l’antalgie : la douleur persiste." }
        }
      },
      {
        id: "e4-reperfusion",
        titre: "Duel 4 · Reperfuser",
        consigne: "STEMI inférieur étendu au VD, dissection exclue. Lance le traitement et la reperfusion.",
        adversaire: "stemi",
        main: ["oxygene", "aspirine", "nitres", "hnf", "p2y12", "icp", "betabloquant", "troponine"],
        objectifs: ["aspirine", "hnf", "icp"],
        regles: {
          "aspirine": { verdict: "bon", msg: "Bon réflexe. La dissection est exclue : l’aspirine s’impose." },
          "hnf": { verdict: "bon", msg: "Bon réflexe. Le patient n’a reçu ni HBPM ni anticoagulant oral : l’héparine part." },
          "icp": { verdict: "bon", msg: "Bon réflexe. Tu déclenches l’alarme STEMI et annonces l’hypotension. Cible : ICP en ≤ 90 min." },
          "p2y12": { verdict: "neutre", msg: "Décide le moment de la charge avec le cardiologue. Les protocoles suisses lus divergent." },
          "troponine": { verdict: "neutre", msg: "Le prélèvement part. La reperfusion n’attend pas son résultat." },
          "nitres": { verdict: "erreur", pv: 25, msg: "Erreur. Infarctus droit et TAS < 110 mmHg : les nitrés restent interdits." },
          "oxygene": { verdict: "erreur", pv: 10, msg: "Erreur. La SpO₂ vaut 95 %. L’oxygène ne protège pas le myocarde ici." },
          "betabloquant": { verdict: "erreur", pv: 20, msg: "Erreur. Patient hypotendu : le bêtabloquant est contre-indiqué." }
        }
      }
    ],
    debrief: [
      "Tu as exclu la dissection avant les antithrombotiques.",
      "Tu as reconnu un STEMI inférieur étendu au ventricule droit.",
      "Tu as évité les nitrés, l’oxygène réflexe et le bêtabloquant chez un patient hypotendu.",
      "Le patient part en salle de cathétérisme."
    ]
  }]
});

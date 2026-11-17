/**
 * Schéma v2 et validateur des données d’auteur (navigateur ET Node).
 * Une spécialité = catalogue de pathologies + cartes (8 rubriques) + cas (3 à 5 duels).
 * valider() renvoie { erreurs, avertissements, stats } ; zéro erreur exigé avant tout push.
 */
(function (root) {
  const JEU = root.JEU = root.JEU || {};

  const RUBRIQUES = [
    ["fondamentaux", "Fondamentaux", "Anatomie, physiologie et physiopathologie qui expliquent les signes."],
    ["demarche", "Démarche diagnostique", "Anamnèse ciblée, examen ciblé, drapeaux rouges, probabilité avant test."],
    ["differentiels", "Diagnostics différentiels", "À évoquer absolument, ceux qui tuent d’abord, avec le signe qui discrimine."],
    ["exploration", "Exploration ciblée", "Chaque examen répond à une question ; les examens inutiles sont signalés."],
    ["diagnostic", "Diagnostic", "Critères retenus et leur source."],
    ["priseEnCharge", "Prise en charge", "Des mesures générales aux mesures spécifiques, sans excès."],
    ["suivi", "Suivi et orientation", "Quand hospitaliser, adresser ou revoir."],
    ["explication", "Explication des coups", "Chaque bon coup et chaque erreur en 1 à 3 phrases."]
  ];
  const CLES = RUBRIQUES.map(r => r[0]);
  /** Rubriques cliniques : une source suisse ou « À vérifier » est exigée. */
  const CLINIQUES = ["demarche", "differentiels", "exploration", "diagnostic", "priseEnCharge", "suivi"];
  /** Rubriques qui peuvent valoir « Sans objet » pour une carte d’action. */
  const NA_OK = ["differentiels", "exploration", "diagnostic", "suivi"];
  const PHASES = ["trier", "explorer", "differencier", "diagnostiquer", "traiter"];
  const TYPES = ["pathologie", "examen", "traitement", "geste", "fondamental"];
  const VERDICTS = ["bon", "erreur", "neutre", "inutile"];
  const TRIBOOL = [true, false, "à vérifier"];
  const AV = /À vérifier/;
  // Dose apparente : nombre + unité de dose, sauf concentration (µg/l, mg/dl…).
  const DOSE = /\b\d+(?:[.,]\d+)?\s?(?:mg|µg|mcg|g|ml|mL|UI|U|E|mmol|gtt)\b(?!\s?\/\s?(?:l|dl|ml)\b)/;

  const sentences = t => (String(t).match(/[.!?](\s|$)/g) || []).length;

  function valider(specs, sources, opts = {}) {
    const E = [], W = [];
    const err = m => E.push(m), warn = m => W.push(m);
    const profiles = new Set(((opts.profiles || {}).ssp || []).map(x => x.code));
    const parcoursIds = new Set((opts.parcours || []).flatMap(l => l.specialites.map(s => s.id)));
    const stats = { specialites: 0, cartes: 0, cas: 0, affirmations: 0, aVerifier: 0, pathologies: 0 };
    const cartesGlobales = new Map();

    // Sources
    Object.entries(sources || {}).forEach(([id, s]) => {
      if (!s.titre || !s.url || !s.lu_le) err(`Source ${id} : titre, url et lu_le obligatoires`);
      if (s.lu_le && !/^\d{4}-\d{2}-\d{2}$/.test(s.lu_le)) err(`Source ${id} : lu_le doit être une date ISO`);
      if (!["suisse", "pharmaco", "international"].includes(s.type)) err(`Source ${id} : type inconnu « ${s.type} »`);
      if (s.type === "suisse" && !s.categorie) err(`Source ${id} : catégorie suisse manquante`);
    });
    const src = id => (sources || {})[id];
    const suisse = cl => (cl.s || []).some(id => src(id) && src(id).type === "suisse");

    function claim(cl, where, { clinique = false, naOk = false } = {}) {
      if (!cl || typeof cl.t !== "string" || !cl.t.trim()) { err(`${where} : texte manquant`); return; }
      if (!Array.isArray(cl.s)) { err(`${where} : liste de sources « s » manquante`); return; }
      stats.affirmations++;
      if (cl.quiz !== undefined && typeof cl.quiz !== "boolean") err(`${where} : « quiz » doit être un booléen`);
      if (cl.na) { if (!naOk) err(`${where} : « Sans objet » interdit ici`); return; }
      cl.s.forEach(id => { if (!src(id)) err(`${where} : source inconnue « ${id} »`); });
      const av = AV.test(cl.t);
      if (av) stats.aVerifier++;
      if (!cl.s.length && !av) err(`${where} : affirmation sans source ni « À vérifier »`);
      if (clinique && cl.s.length && !suisse(cl) && !av) err(`${where} : clinique sans source suisse (ajoute « À vérifier » ou une source suisse)`);
      if (DOSE.test(cl.t)) {
        const d = cl.dose;
        if (!d || !d.verbatim || !/swissmedicinfo/.test(d.url || "") || !d.lu_le) err(`${where} : dose sans extrait swissmedicinfo daté`);
      }
    }

    (specs || []).forEach(sp => {
      stats.specialites++;
      const W0 = `Spécialité ${sp.id}`;
      if (sp.schema !== 2) err(`${W0} : schema 2 attendu`);
      if (!sp.id || !sp.nom || !sp.lot) err(`${W0} : id, nom et lot obligatoires`);
      if (parcoursIds.size && !parcoursIds.has(sp.id)) err(`${W0} : absente du parcours`);
      ["pathologies", "cartes", "cas"].forEach(k => { if (!Array.isArray(sp[k])) err(`${W0} : « ${k} » doit être une liste`); });
      if (!Array.isArray(sp.pathologies) || !Array.isArray(sp.cartes) || !Array.isArray(sp.cas)) return;
      const ids = new Set();
      sp.cartes.forEach(c => {
        const w = `${W0} · carte ${c.id}`;
        stats.cartes++;
        if (!c.id || ids.has(c.id) || cartesGlobales.has(c.id)) err(`${w} : id absent ou en double`);
        ids.add(c.id); cartesGlobales.set(c.id, c);
        if (!TYPES.includes(c.type)) err(`${w} : type inconnu`);
        ["nom", "court", "cle"].forEach(k => { if (!c[k]) err(`${w} : « ${k} » manquant`); });
        if (c.posologie) err(`${w} : champ posologie interdit (dose = affirmation avec extrait swissmedicinfo)`);
        if (!c.rubriques) { err(`${w} : rubriques manquantes`); return; }
        Object.keys(c.rubriques).forEach(k => { if (!CLES.includes(k)) err(`${w} : rubrique inconnue « ${k} »`); });
        CLES.forEach(k => {
          const L = c.rubriques[k];
          if (!Array.isArray(L)) { err(`${w} : rubrique « ${k} » manquante`); return; }
          if (!L.length && k !== "explication") err(`${w} : rubrique « ${k} » vide (écris « À vérifier »)`);
          L.forEach((cl, i) => {
            claim(cl, `${w}.${k}[${i}]`, { clinique: CLINIQUES.includes(k), naOk: c.type !== "pathologie" && NA_OK.includes(k) });
            if (cl.echelon !== undefined && !(k === "fondamentaux" && (cl.echelon === 1 || cl.echelon === 2))) err(`${w}.${k}[${i}] : « echelon » 1 ou 2, seulement en fondamentaux`);
            if (k === "differentiels" && !cl.na) {
              if (!cl.dx) err(`${w}.differentiels[${i}] : nom du différentiel « dx » manquant`);
              if (typeof cl.tue !== "boolean") err(`${w}.differentiels[${i}] : booléen « tue » manquant`);
            }
          });
          if (k === "differentiels") {
            const t = L.filter(x => !x.na).map(x => x.tue);
            if (t.some((v, i) => !v && t.slice(i + 1).some(Boolean))) err(`${w} : les différentiels qui tuent passent en premier`);
          }
        });
        ["contre", "pieges"].forEach(k => (c[k] || []).forEach((cl, i) => claim(cl, `${w}.${k}[${i}]`)));
        if (c.noteFrequence) claim(c.noteFrequence, `${w}.noteFrequence`);
        (c.sources || []).forEach(id => { if (!src(id)) err(`${w}.sources : source inconnue « ${id} »`); });
        if (c.type === "pathologie" && !c.sources.some(id => src(id) && src(id).type === "suisse")) err(`${w} : aucune source suisse`);
      });

      const pids = new Set();
      sp.pathologies.forEach(p => {
        const w = `${W0} · pathologie ${p.id}`;
        stats.pathologies++;
        if (!p.id || pids.has(p.id)) err(`${w} : id absent ou en double`);
        pids.add(p.id);
        if (!p.nom) err(`${w} : nom manquant`);
        if (!Array.isArray(p.ssp) || !p.ssp.length) err(`${w} : au moins une SSP PROFILES exigée`);
        (p.ssp || []).forEach(code => { if (profiles.size && !profiles.has(code)) err(`${w} : SSP inconnue « ${code} »`); });
        if (!TRIBOOL.includes(p.frequente) || !TRIBOOL.includes(p.grave)) err(`${w} : frequente et grave valent true, false ou « à vérifier »`);
        if (p.carte && !ids.has(p.carte)) err(`${w} : carte inconnue « ${p.carte} »`);
        (p.justif || []).forEach((cl, i) => claim(cl, `${w}.justif[${i}]`, { clinique: true }));
        if ((p.frequente === true || p.grave === true) && !(p.justif || []).length) warn(`${w} : drapeau sans justification sourcée`);
      });

      const casIds = new Set();
      sp.cas.forEach(cs => {
        const w = `${W0} · cas ${cs.id}`;
        stats.cas++;
        if (!cs.id || casIds.has(cs.id)) err(`${w} : id absent ou en double`);
        casIds.add(cs.id);
        if (!["urgence", "consultation", "final"].includes(cs.mode)) err(`${w} : mode urgence, consultation ou final`);
        if ((cs.mode === "urgence" || cs.mode === "final") && !(cs.chrono > 0)) err(`${w} : chrono (s) exigé en mode ${cs.mode}`);
        if (cs.mode === "final" && ((cs.pathologies || []).length < 2 || !cs.piege)) err(`${w} : un cas final combine ≥ 2 pathologies et décrit son piège`);
        if (!(cs.pvInitial > 0)) err(`${w} : pvInitial manquant`);
        if (!Array.isArray(cs.pathologies) || !cs.pathologies.length) err(`${w} : pathologies couvertes manquantes`);
        (cs.pathologies || []).forEach(p => { if (!pids.has(p)) err(`${w} : pathologie hors catalogue « ${p} »`); });
        if (!cs.patient || !cs.dossier) err(`${w} : patient et dossier obligatoires`);
        const et = cs.etapes || [];
        if (et.length < 3 || et.length > 5) err(`${w} : 3 à 5 duels exigés (${et.length})`);
        let last = -1;
        et.forEach((e, n) => {
          const we = `${w} · duel ${e.id}`;
          const pi = PHASES.indexOf(e.phase);
          if (pi < 0) err(`${we} : phase inconnue « ${e.phase} »`);
          else { if (pi < last) err(`${we} : phase hors ordre clinique (${PHASES.join(" → ")})`); last = pi; }
          if (!ids.has(e.adversaire)) err(`${we} : adversaire inconnu`);
          if (!(cs.pathologies || []).includes(e.pathologie)) err(`${we} : « pathologie » doit appartenir aux pathologies du cas`);
          if (e.echelon !== undefined && !(e.echelon >= 1 && e.echelon <= 7)) err(`${we} : échelon hors 1–7`);
          (e.main || []).forEach(id => { if (!cartesGlobales.has(id) && !ids.has(id)) err(`${we} : carte de main inconnue « ${id} »`); });
          if ((e.main || []).length > 9) err(`${we} : 9 cartes au plus (raccourcis 1–9)`);
          (e.objectifs || []).forEach(id => { if (!(e.main || []).includes(id)) err(`${we} : objectif hors main « ${id} »`); });
          if (!(e.objectifs || []).length) err(`${we} : au moins un objectif`);
          Object.entries(e.regles || {}).forEach(([id, r]) => {
            const wr = `${we} · règle ${id}`;
            if (!(e.main || []).includes(id)) err(`${wr} : carte hors main`);
            if (!VERDICTS.includes(r.verdict)) err(`${wr} : verdict inconnu`);
            if (r.verdict === "erreur" && !["dangereuse", "mineure"].includes(r.gravite)) err(`${wr} : gravité dangereuse ou mineure exigée`);
            if (r.verdict === "inutile") { const c = cartesGlobales.get(id); if (c && c.type !== "examen") warn(`${wr} : « inutile » vise d’habitude un examen`); }
            if (!r.msg) err(`${wr} : explication manquante`);
            else if (sentences(r.msg) > 4) err(`${wr} : explication > 3 phrases`);
            if (r.revele && !(cs.dossier || {})[r.revele]) err(`${wr} : élément de dossier inconnu`);
            if (r.fiche && !ids.has(r.fiche) && !cartesGlobales.has(r.fiche)) err(`${wr} : fiche inconnue`);
            if (r.pv !== undefined) err(`${wr} : « pv » obsolète (la gravité fixe la perte)`);
          });
          (e.main || []).forEach(id => { if (!(e.regles || {})[id]) warn(`${we} : ${id} sans règle (verdict neutre par défaut)`); });
        });
        if (et.length && et[0].phase !== "trier") warn(`${w} : le premier duel devrait trier`);
        if (et.length && et[et.length - 1].phase !== "traiter") warn(`${w} : le dernier duel devrait traiter`);
      });
      // Questions rédigées (échelle à 7 échelons)
      (sp.questions || []).forEach((q, i) => {
        const w = `${W0} · question ${q.id || i}`;
        if (!q.id) err(`${w} : id manquant`);
        if (!pids.has(q.pathologie)) err(`${w} : pathologie hors catalogue`);
        if (!(q.echelon >= 1 && q.echelon <= 7)) err(`${w} : échelon hors 1–7`);
        if (!q.enonce) err(`${w} : énoncé manquant`);
        if (!Array.isArray(q.choix) || q.choix.length < 2 || q.choix.filter(c => c.juste).length !== 1) err(`${w} : 2 choix au moins, un seul juste`);
        if (!q.explication) err(`${w} : explication manquante`);
        else claim(q.explication, `${w}.explication`, { clinique: q.echelon >= 3 });
      });
      // Carte jamais jouée ni expliquée
      sp.cartes.forEach(c => {
        const jouee = sp.cas.some(cs => (cs.etapes || []).some(e => e.adversaire === c.id || (e.main || []).includes(c.id)));
        if (!jouee && !c.rubriques.explication.length) warn(`${W0} · carte ${c.id} : ni cas ni explication`);
      });
    });
    stats.tauxAVerifier = stats.affirmations ? Math.round(stats.aVerifier / stats.affirmations * 1000) / 10 : 0;
    return { erreurs: E, avertissements: W, stats };
  }

  JEU.schema = { RUBRIQUES, CLES, CLINIQUES, PHASES, TYPES, VERDICTS, DOSE, valider };
  if (typeof module !== "undefined") module.exports = JEU.schema;
})(typeof window !== "undefined" ? window : globalThis);

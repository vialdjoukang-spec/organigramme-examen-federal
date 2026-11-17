/**
 * Registre v2 : spécialités chargées (data/specialites/*.js), index des cartes,
 * cas et pathologies, poids PROFILES des cartes, validation au démarrage.
 */
window.JEU = window.JEU || {};
JEU.specialites = JEU.specialites || [];
/** Chaque fichier de spécialité appelle JEU.specialite({...}). */
JEU.specialite = JEU.specialite || function (sp) { JEU.specialites.push(sp); };

JEU.registry = (function () {
  const cartes = new Map(), cas = new Map(), patho = new Map();
  let rapport = { erreurs: [], avertissements: [], stats: {} };

  /**
   * Poids d’une carte (affiché comme rareté) : approximation objective et documentée,
   * en attendant une pondération officielle. Pathologie : nombre de SSP PROFILES rattachées
   * (≥ 4 : élevé, 3 : moyen, ≤ 2 : ciblé). Carte d’action : poids le plus élevé des
   * pathologies des cas où elle est un objectif.
   */
  function poids(nSsp) { return nSsp >= 4 ? "commune" : nSsp === 3 ? "frequente" : "rare"; }

  function init() {
    cartes.clear(); cas.clear(); patho.clear();
    JEU.specialites.forEach(sp => {
      sp.cartes.forEach(c => cartes.set(c.id, Object.assign(c, { specialite: sp.id })));
      sp.pathologies.forEach(p => patho.set(p.id, Object.assign(p, { specialite: sp.id })));
      sp.cas.forEach(k => cas.set(k.id, Object.assign(k, { specialite: sp.id })));
    });
    const ordre = ["commune", "frequente", "rare"];
    cartes.forEach(c => {
      if (c.type === "pathologie") {
        const p = [...patho.values()].find(x => x.carte === c.id);
        c.rarete = poids(p ? p.ssp.length : 0);
      } else {
        let best = "rare";
        cas.forEach(k => k.etapes.forEach(e => {
          if (!e.objectifs.includes(c.id)) return;
          const p = patho.get(e.pathologie); const w = poids(p ? p.ssp.length : 0);
          if (ordre.indexOf(w) < ordre.indexOf(best)) best = w;
        }));
        c.rarete = best;
      }
    });
    rapport = JEU.schema.valider(JEU.specialites, JEU.sources, { profiles: JEU.profiles, parcours: JEU.parcours });
    rapport.erreurs.forEach(e => console.warn("[données]", e));
    return rapport.erreurs;
  }

  const card = id => cartes.get(id);
  const cards = sp => [...cartes.values()].filter(c => !sp || c.specialite === sp);
  const unCas = id => cas.get(id);
  const casDe = (sp, mode) => [...cas.values()].filter(k => k.specialite === sp && (!mode || k.mode === mode));
  const tousLesCas = () => [...cas.values()];
  const pathologies = sp => [...patho.values()].filter(p => !sp || p.specialite === sp);
  const pathologie = id => patho.get(id);
  const specialite = id => JEU.specialites.find(s => s.id === id);
  const source = id => (JEU.sources || {})[id];
  const isSourced = cl => Array.isArray(cl.s) && cl.s.length > 0;
  const hasSwissSource = c => (c.sources || []).some(s => source(s) && source(s).type === "suisse");
  /** Ordre des spécialités du parcours (plan de production). */
  const ordreParcours = () => (JEU.parcours || []).flatMap(l => l.specialites.map(s => Object.assign({ lot: l.id, lotNom: l.nom }, s)));
  const validate = () => rapport.erreurs;
  const rapportValidation = () => rapport;

  return { init, card, cards, cas: unCas, casDe, tousLesCas, pathologies, pathologie, specialite, source, isSourced, hasSwissSource, ordreParcours, validate, rapportValidation };
})();

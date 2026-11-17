/**
 * Registre : accès aux données chargées (cartes, services, systèmes, sources)
 * et validation de cohérence au démarrage (ids inconnus, sources absentes).
 */
window.JEU = window.JEU || {};
JEU.registry = (function () {
  const cardIndex = new Map();

  function init() {
    cardIndex.clear();
    (JEU.cards || []).forEach(c => {
      if (cardIndex.has(c.id)) console.warn("Carte en double :", c.id);
      cardIndex.set(c.id, c);
    });
    return validate();
  }

  const card = id => cardIndex.get(id);
  const cards = () => Array.from(cardIndex.values());
  const source = id => (JEU.sources || {})[id];
  const system = id => (JEU.systems || []).find(s => s.id === id);
  const service = id => (JEU.services || []).find(s => s.id === id);

  /** Retourne la liste des problèmes de données (vide = tout va bien). */
  function validate() {
    const pb = [];
    const checkSrc = (ids, where) => (ids || []).forEach(s => { if (!source(s)) pb.push(`${where} : source inconnue « ${s} »`); });
    cards().forEach(c => {
      if (!system(c.systeme)) pb.push(`Carte ${c.id} : système inconnu`);
      ["mecanisme", "signes", "exploration", "premiere", "contre", "pieges"].forEach(k =>
        (c[k] || []).forEach((a, i) => checkSrc(a.s, `Carte ${c.id}.${k}[${i}]`)));
      checkSrc(c.sources, `Carte ${c.id}.sources`);
      if (c.posologie) pb.push(`Carte ${c.id} : posologie présente – exige un extrait suisse daté`);
    });
    (JEU.services || []).forEach(sv => sv.cas.forEach(cs => cs.etapes.forEach(e => {
      [e.adversaire, ...e.main, ...e.objectifs, ...Object.keys(e.regles)].forEach(id => {
        if (!card(id)) pb.push(`Étape ${e.id} : carte inconnue « ${id} »`);
      });
      Object.values(e.regles).forEach(r => { if (r.revele && !cs.dossier[r.revele]) pb.push(`Étape ${e.id} : élément de dossier inconnu « ${r.revele} »`); });
    })));
    pb.forEach(p => console.warn("[données]", p));
    return pb;
  }

  /** Une affirmation est « sourcée » si elle cite au moins une source lue. */
  const isSourced = claim => Array.isArray(claim.s) && claim.s.length > 0;
  /** Une fiche est validée si au moins une source clinique suisse y figure. */
  const hasSwissSource = c => (c.sources || []).some(s => source(s) && source(s).type === "suisse");

  return { init, card, cards, source, system, service, validate, isSourced, hasSwissSource };
})();

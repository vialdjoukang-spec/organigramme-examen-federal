/**
 * Journal de progression, persisté dans localStorage.
 * Agrège les verdicts par système et garde la liste des erreurs.
 */
window.JEU = window.JEU || {};
JEU.journal = (function () {
  const KEY = "revmed.journal.v1";
  const SEUIL_FAIBLE = 0.7;      // précision sous laquelle un système est signalé faible
  const MIN_ESSAIS = 3;          // nombre minimal de coups avant de juger

  const vide = () => ({ version: 1, systemes: {}, erreurs: [], parties: [] });
  let data = load();

  function load() {
    try {
      const raw = localStorage.getItem(KEY);
      const d = raw ? JSON.parse(raw) : vide();
      return d && d.version === 1 ? d : vide();
    } catch (e) { return vide(); }
  }
  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(data)); } catch (e) { /* stockage indisponible */ }
  }

  function enregistrerCoup({ systeme, service, cas, etape, carte, verdict, fiche, msg }) {
    const s = data.systemes[systeme] || (data.systemes[systeme] = { bons: 0, erreurs: 0, neutres: 0 });
    if (verdict === "bon") s.bons++;
    else if (verdict === "erreur") s.erreurs++;
    else s.neutres++;
    if (verdict === "erreur") data.erreurs.unshift({ ts: new Date().toISOString(), systeme, service, cas, etape, carte, fiche, msg });
    save();
  }

  function enregistrerPartie({ cas, pv, resultat, erreurs }) {
    data.parties.unshift({ ts: new Date().toISOString(), cas, pv, resultat, erreurs });
    data.parties = data.parties.slice(0, 20);
    save();
  }

  /** Statistiques d’un système : précision et drapeau « faible ». */
  function stats(systeme) {
    const s = data.systemes[systeme] || { bons: 0, erreurs: 0, neutres: 0 };
    const juges = s.bons + s.erreurs;
    const precision = juges ? s.bons / juges : null;
    return { ...s, juges, precision, faible: juges >= MIN_ESSAIS && precision < SEUIL_FAIBLE };
  }

  /** Fiches les plus souvent ratées. */
  function fichesARevoir() {
    const n = {};
    data.erreurs.forEach(e => { n[e.fiche] = (n[e.fiche] || 0) + 1; });
    return Object.entries(n).sort((a, b) => b[1] - a[1]);
  }

  function reset() { data = vide(); save(); }
  const get = () => data;

  return { enregistrerCoup, enregistrerPartie, stats, fichesARevoir, reset, get, SEUIL_FAIBLE, MIN_ESSAIS };
})();

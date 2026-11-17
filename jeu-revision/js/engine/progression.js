/**
 * Traqueur de progression (docs/PROGRESSION.md, § 1 à 3).
 * Source unique de vérité : un journal d’événements « coups ». Tout le reste
 * (carte de chaleur, calibration, angles morts, vitesse, Leitner, maîtrise, grades,
 * préparation PROFILES) se recalcule depuis ce journal. L’import fusionne donc
 * deux journaux par identifiant de coup, sans perte.
 * Fonctionne dans le navigateur et dans Node (tests).
 */
(function (root) {
  const JEU = root.JEU = root.JEU || {};
  const KEY = "revmed.progression.v2";
  const KEY_V1 = "revmed.journal.v1";
  const SCHEMA = "revmed.progression";
  const VERSION = 2;
  const JOUR = 86400000;

  const ECHELONS = [
    [1, "Fondamental", "Relier structure et fonction."],
    [2, "Mécanisme", "Expliquer la physiopathologie des signes."],
    [3, "Clinique", "Reconnaître le signe clé et les drapeaux rouges."],
    [4, "Démarche et différentiels", "Classer les hypothèses, celles qui tuent d’abord."],
    [5, "Exploration", "Choisir l’examen qui tranche, rejeter l’inutile."],
    [6, "Diagnostic", "Appliquer les critères suisses."],
    [7, "Prise en charge", "Du général au spécifique, puis au suivi."]
  ];
  const CONFIANCES = { sur: "Sûr", hesitant: "Hésitant", hasard: "Au hasard" };
  /** Leitner, 5 boîtes : intervalle avant la prochaine révision (jours). */
  const LEITNER = [0, 1, 7, 14, 30];
  const GRADES = [[0, "Externe"], [0.25, "Interne"], [0.5, "Chef de clinique"], [0.75, "Médecin cadre"], [0.9, "Médecin cadre · prêt pour l’examen blanc"]];
  const SEUIL_FAIBLE = 0.7, MIN_ESSAIS = 3, OBJECTIF_URGENCE_MS = 20000, RONDE_MS = 20 * 60000;

  const horloge = JEU.horloge = JEU.horloge || { now: () => Date.now() };
  const jourDe = ts => { const d = new Date(ts); return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`; };
  const joursEntre = (a, b) => Math.round((Date.parse(b + "T12:00:00") - Date.parse(a + "T12:00:00")) / JOUR);
  const juge = c => c.v === "bon" || c.v === "erreur" || c.v === "inutile";
  const median = a => { if (!a.length) return null; const s = [...a].sort((x, y) => x - y); const m = s.length >> 1; return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2; };
  const uid = () => horloge.now().toString(36) + "-" + Math.random().toString(36).slice(2, 9);

  const vide = () => ({ schema: SCHEMA, version: VERSION, coups: [], parties: [], rondes: [] });
  let store = null;
  const storage = () => { try { return root.localStorage || null; } catch (e) { return null; } };

  function charger() {
    const ls = storage();
    let d = null;
    try { d = ls && JSON.parse(ls.getItem(KEY) || "null"); } catch (e) { d = null; }
    if (!d || d.schema !== SCHEMA) d = vide();
    // Migration v1 (journal du prototype) : les erreurs deviennent des coups sans confiance.
    try {
      const v1 = ls && JSON.parse(ls.getItem(KEY_V1) || "null");
      if (v1 && v1.version === 1 && !d.migreV1) {
        (v1.erreurs || []).forEach(e => d.coups.push({ id: "v1-" + e.ts, ts: Date.parse(e.ts) || 0, sp: "cardiologie", pa: null, ech: null, src: "duel", cas: e.cas, et: e.etape, carte: e.carte, v: "erreur", g: null, conf: null, ms: null, mode: "urgence", fiche: e.fiche }));
        d.migreV1 = true;
      }
    } catch (e) { /* rien à migrer */ }
    store = d; sauver();
    return store;
  }
  function sauver() { const ls = storage(); if (ls) try { ls.setItem(KEY, JSON.stringify(store)); } catch (e) { /* quota */ } }
  const get = () => store || charger();

  /** Enregistre un coup. Champs : sp, pa, ech, src, cas, et, carte, rep, v, g, conf, ms, mode, fiche, msg. */
  function enregistrer(c) {
    const coup = Object.assign({ id: uid(), ts: horloge.now() }, c);
    if (coup.conf && !CONFIANCES[coup.conf]) throw new Error("Confiance inconnue : " + coup.conf);
    get().coups.push(coup); sauver();
    return coup;
  }
  function enregistrerPartie(p) { const x = Object.assign({ id: uid(), ts: horloge.now() }, p); get().parties.push(x); sauver(); return x; }
  function enregistrerRonde(r) { const x = Object.assign({ id: uid(), ts: horloge.now(), j: jourDe(horloge.now()) }, r); get().rondes.push(x); sauver(); return x; }

  /* ---------- Agrégats ---------- */
  function chaleur() {
    const m = {};
    get().coups.filter(c => juge(c) && c.ech).forEach(c => {
      const k = `${c.sp}|${c.ech}`; const x = m[k] || (m[k] = { n: 0, bons: 0 });
      x.n++; if (c.v === "bon") x.bons++;
    });
    Object.values(m).forEach(x => { x.precision = x.bons / x.n; });
    return m;
  }
  function parSpecialite(sp) {
    const L = get().coups.filter(c => c.sp === sp && juge(c));
    const bons = L.filter(c => c.v === "bon").length;
    const precision = L.length ? bons / L.length : null;
    return { n: L.length, bons, precision, faible: L.length >= MIN_ESSAIS && precision < SEUIL_FAIBLE };
  }
  function calibration() {
    const r = {};
    Object.keys(CONFIANCES).forEach(k => {
      const L = get().coups.filter(c => c.conf === k && juge(c));
      const b = L.filter(c => c.v === "bon").length;
      r[k] = { n: L.length, bons: b, precision: L.length ? b / L.length : null };
    });
    const s = r.sur, h = r.hesitant;
    r.exces = s.n >= 5 && (s.precision < 0.8 || (h.n >= 5 && s.precision < h.precision));
    return r;
  }
  /** Angles morts : erreurs « sûr », drapeaux rouges manqués (échelon 3), différentiels mortels oubliés (échelon 4). */
  function anglesMorts() {
    const g = {};
    get().coups.filter(c => c.v === "erreur").forEach(c => {
      const types = [];
      if (c.conf === "sur") types.push("sur");
      if (c.ech === 3 && c.g === "dangereuse") types.push("drapeau-rouge");
      if (c.ech === 4 && (c.g === "dangereuse" || c.mortel)) types.push("differentiel-mortel");
      if (!types.length) return;
      const k = `${c.carte}|${c.cas || c.src}`;
      const x = g[k] || (g[k] = { carte: c.carte, cas: c.cas || null, src: c.src, sp: c.sp, pa: c.pa, ech: c.ech, fiche: c.fiche || c.carte, n: 0, dernier: 0, types: new Set() });
      x.n++; x.dernier = Math.max(x.dernier, c.ts); types.forEach(t => x.types.add(t));
    });
    return Object.values(g).map(x => Object.assign(x, { types: [...x.types] }))
      .sort((a, b) => b.dernier - a.dernier || b.n - a.n);
  }
  function vitesse() {
    const r = {};
    ECHELONS.forEach(([e]) => { const L = get().coups.filter(c => c.ech === e && c.ms > 0).map(c => c.ms); r[e] = { n: L.length, median: median(L) }; });
    const U = get().coups.filter(c => c.mode === "urgence" && c.ms > 0).map(c => c.ms);
    r.urgence = { n: U.length, median: median(U), objectif: OBJECTIF_URGENCE_MS, atteint: U.length ? median(U) < OBJECTIF_URGENCE_MS : null };
    return r;
  }

  /* ---------- Leitner (5 boîtes) et maîtrise, rejoués depuis le journal ---------- */
  function items() {
    const it = {};
    get().coups.filter(c => juge(c) && c.pa && c.ech).sort((a, b) => a.ts - b.ts).forEach(c => {
      const k = `${c.pa}|${c.ech}`;
      const x = it[k] || (it[k] = { cle: k, sp: c.sp, pa: c.pa, ech: c.ech, boite: 1, dernier: 0, n: 0, bons: 0, joursSurs: [], dernierJuste: false, angleMort: false });
      const ok = c.v === "bon";
      x.n++; if (ok) x.bons++;
      if (!ok) { x.boite = 1; if (c.conf === "sur") x.angleMort = true; }
      else if (c.conf === "hasard" || !c.conf) x.boite = 1;          // juste au hasard : non maîtrisé
      else { x.boite = Math.min(5, x.boite + 1); if (c.conf === "sur") x.angleMort = false; }
      if (ok && c.conf === "sur") { const j = jourDe(c.ts); if (!x.joursSurs.includes(j)) x.joursSurs.push(j); }
      x.dernierJuste = ok; x.dernier = c.ts;
    });
    Object.values(it).forEach(x => {
      x.due = x.dernier + LEITNER[x.boite - 1] * JOUR;
      x.maitrise = x.dernierJuste && maitriseJours(x.joursSurs);
      x.rappel = x.maitrise && horloge.now() - x.dernier >= 30 * JOUR;
    });
    return it;
  }
  /** Réussi « sûr » à J0, puis au moins à J+1 et à J+7. */
  function maitriseJours(js) {
    for (const j0 of js) {
      const d = js.map(j => joursEntre(j0, j));
      if (d.some(x => x >= 1) && d.some(x => x >= 7)) return true;
    }
    return false;
  }
  function dues(now = horloge.now()) {
    return Object.values(items()).filter(x => x.due <= now || x.angleMort || x.rappel)
      .sort((a, b) => (b.angleMort - a.angleMort) || (a.boite - b.boite) || (a.due - b.due));
  }
  /** Pathologies maîtrisées : les 7 échelons maîtrisés. */
  function maitrise(pathologies) {
    const it = items();
    const res = {};
    pathologies.forEach(p => {
      const e = ECHELONS.map(([n]) => it[`${p.id}|${n}`]);
      res[p.id] = { echelons: e.map(x => !!(x && x.maitrise)), maitrisee: e.every(x => x && x.maitrise), rappel: e.some(x => x && x.rappel) };
    });
    return res;
  }
  function grade(pathologies) {
    const m = maitrise(pathologies);
    const total = pathologies.length, n = Object.values(m).filter(x => x.maitrisee).length;
    const part = total ? n / total : 0;
    let g = GRADES[0];
    GRADES.forEach(x => { if (part >= x[0]) g = x; });
    const suivant = GRADES.find(x => x[0] > part) || null;
    return { grade: g[1], part, n, total, suivant: suivant && { grade: suivant[1], seuil: suivant[0] } };
  }
  /** Préparation par domaine PROFILES (groupe de SSP) : part des pathologies maîtrisées. */
  function preparation(pathologies, profiles) {
    const m = maitrise(pathologies);
    const dom = {};
    Object.keys(profiles.groupes).forEach(g => { dom[g] = { label: profiles.groupes[g], total: 0, maitrisees: 0, ssp: new Set() }; });
    const grp = code => code.startsWith("G") ? "G" : code.split(".")[0];
    pathologies.forEach(p => {
      const gs = new Set((p.ssp || []).map(grp));
      gs.forEach(g => { if (!dom[g]) return; dom[g].total++; if (m[p.id] && m[p.id].maitrisee) dom[g].maitrisees++; });
      (p.ssp || []).forEach(code => dom[grp(code)] && dom[grp(code)].ssp.add(code));
    });
    Object.entries(dom).forEach(([g, x]) => {
      x.sspTotal = profiles.ssp.filter(s => grp(s.code) === g).length; x.sspTouchees = x.ssp.size; delete x.ssp;
      x.part = x.total ? x.maitrisees / x.total : null;
    });
    return dom;
  }
  const rondeDuJour = () => get().rondes.filter(r => r.j === jourDe(horloge.now()));

  /* ---------- Export / import ---------- */
  function exporter() {
    return JSON.stringify(Object.assign({}, get(), { exporte_le: new Date(horloge.now()).toISOString() }), null, 1);
  }
  /** Valide puis fusionne (union par identifiant). Renvoie { ok, ajoutes, erreurs }. */
  function importer(texte) {
    let d;
    try { d = typeof texte === "string" ? JSON.parse(texte) : texte; } catch (e) { return { ok: false, erreurs: ["Fichier illisible : JSON invalide."] }; }
    const er = [];
    if (!d || d.schema !== SCHEMA) er.push("Schéma inconnu : ce fichier ne vient pas du jeu.");
    if (d && d.version !== VERSION) er.push(`Version ${d && d.version} non prise en charge (attendue : ${VERSION}).`);
    ["coups", "parties", "rondes"].forEach(k => { if (d && !Array.isArray(d[k])) er.push(`Champ « ${k} » absent ou invalide.`); });
    if (!er.length) d.coups.forEach((c, i) => {
      if (!c.id || typeof c.ts !== "number") er.push(`Coup ${i} : id ou ts manquant.`);
      if (c.conf && !CONFIANCES[c.conf]) er.push(`Coup ${i} : confiance inconnue.`);
      if (c.ech && !(c.ech >= 1 && c.ech <= 7)) er.push(`Coup ${i} : échelon hors 1–7.`);
    });
    if (er.length) return { ok: false, erreurs: er.slice(0, 10) };
    const s = get(); let ajoutes = 0;
    ["coups", "parties", "rondes"].forEach(k => {
      const vus = new Set(s[k].map(x => x.id));
      d[k].forEach(x => { if (!vus.has(x.id)) { s[k].push(x); vus.add(x.id); ajoutes++; } });
      s[k].sort((a, b) => a.ts - b.ts);
    });
    sauver();
    return { ok: true, ajoutes, erreurs: [] };
  }
  function reset() { store = vide(); store.migreV1 = true; sauver(); }

  JEU.progression = { KEY, SCHEMA, VERSION, ECHELONS, CONFIANCES, LEITNER, GRADES, SEUIL_FAIBLE, OBJECTIF_URGENCE_MS, RONDE_MS,
    charger, get, enregistrer, enregistrerPartie, enregistrerRonde, chaleur, parSpecialite, calibration, anglesMorts, vitesse,
    items, dues, maitrise, maitriseJours, grade, preparation, rondeDuJour, exporter, importer, reset, jourDe };
  if (typeof module !== "undefined") module.exports = JEU.progression;
})(typeof window !== "undefined" ? window : globalThis);

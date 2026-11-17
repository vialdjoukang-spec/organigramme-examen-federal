/**
 * Rapport de couverture par spécialité, contre le catalogue de pathologies et les SSP PROFILES.
 * Usage : node tools/couverture.js [dossier-sortie]   (défaut : docs/couverture)
 * Sorties : couverture.json (machine), INDEX.md (toutes les spécialités du plan), <specialite>.md.
 *
 * Règles (PLAN_PRODUCTION.md, Phase 1) :
 *  – chaque pathologie du catalogue exige au moins un cas ;
 *  – une pathologie fréquente OU grave (ou « à vérifier », par prudence) exige un cas Urgence ET un cas Consultation ;
 *  – couverte = exigences de cas remplies ET contenu sourcé sur les 7 échelons ;
 *  – partielle = au moins un cas, exigences incomplètes ; manquante = aucun cas.
 */
const fs = require("fs"), path = require("path");
const { charger, RACINE } = require("./charger");
const J = charger();
const sortie = process.argv[2] || path.join(RACINE, "docs/couverture");
fs.mkdirSync(sortie, { recursive: true });

const ECH = { fondamentaux: 2, demarche: 3, differentiels: 4, exploration: 5, diagnostic: 6, priseEnCharge: 7, suivi: 7 };
const AV = /À vérifier/;
const src = id => J.sources[id];
function echelonsSources(carte) {
  const e = new Set();
  if (!carte) return e;
  Object.entries(ECH).forEach(([rub, n]) => (carte.rubriques[rub] || []).forEach(cl => {
    if (cl.na || AV.test(cl.t) || !cl.s.length) return;
    if (rub !== "fondamentaux" && !cl.s.some(id => src(id) && src(id).type === "suisse")) return;
    e.add(rub === "fondamentaux" ? (cl.echelon || 2) : n);
  }));
  return e;
}
const exige = p => p.frequente === true || p.grave === true || p.frequente === "à vérifier" || p.grave === "à vérifier";
const grp = code => code.startsWith("G") ? "G" : code.split(".")[0];

const rapport = { genere_le: new Date().toISOString().slice(0, 10), profiles: J.profiles.source, regles: "Voir l’en-tête de tools/couverture.js.", specialites: [], sspNonTouchees: [] };
const sspTouchees = new Set();
J.parcours.forEach(lot => lot.specialites.forEach(s => {
  const sp = J.specialites.find(x => x.id === s.id);
  if (!sp) { rapport.specialites.push({ id: s.id, nom: s.nom, lot: lot.id, statut: "catalogue à produire", pathologies: [] }); return; }
  const cartes = new Map(sp.cartes.map(c => [c.id, c]));
  const L = sp.pathologies.map(p => {
    const casP = sp.cas.filter(k => (k.pathologies || []).includes(p.id));
    const n = m => casP.filter(k => k.mode === m).length;
    const u = n("urgence"), c = n("consultation"), f = n("final");
    const ech = [...echelonsSources(cartes.get(p.carte))].sort();
    const manquentEch = [1, 2, 3, 4, 5, 6, 7].filter(x => !ech.includes(x));
    const besoins = [];
    if (!casP.length) besoins.push("au moins un cas");
    if (exige(p) && !u) besoins.push("un cas Urgence");
    if (exige(p) && !c) besoins.push("un cas Consultation");
    if (manquentEch.length) besoins.push(`contenu sourcé aux échelons ${manquentEch.join(", ")}`);
    (p.ssp || []).forEach(x => sspTouchees.add(x));
    const statut = !casP.length ? "manquante" : besoins.length ? "partielle" : "couverte";
    return { id: p.id, nom: p.nom, ssp: p.ssp, frequente: p.frequente, grave: p.grave, exigeUrgenceEtConsultation: exige(p), cas: { urgence: u, consultation: c, final: f }, echelonsSources: ech, statut, besoins };
  });
  let aff = 0, av = 0;
  const compter = cl => { if (!cl || cl.na) return; aff++; if (AV.test(cl.t)) av++; };
  sp.cartes.forEach(k => { Object.values(k.rubriques).flat().forEach(compter); (k.contre || []).forEach(compter); (k.pieges || []).forEach(compter); compter(k.noteFrequence); });
  rapport.specialites.push({ id: sp.id, nom: sp.nom, lot: lot.id, statut: sp.catalogue && sp.catalogue.complet ? "catalogue complet" : "catalogue incomplet", note: sp.catalogue && sp.catalogue.note,
    totaux: { pathologies: L.length, couvertes: L.filter(x => x.statut === "couverte").length, partielles: L.filter(x => x.statut === "partielle").length, manquantes: L.filter(x => x.statut === "manquante").length, cas: sp.cas.length, cartes: sp.cartes.length, affirmations: aff, aVerifier: av, tauxAVerifier: aff ? Math.round(av / aff * 1000) / 10 : 0 },
    sspTouchees: [...new Set(L.flatMap(x => x.ssp))].sort(), pathologies: L });
}));
rapport.sspNonTouchees = J.profiles.ssp.filter(s => !sspTouchees.has(s.code)).map(s => s.code);
fs.writeFileSync(path.join(sortie, "couverture.json"), JSON.stringify(rapport, null, 1));

const md = [];
md.push(`# Couverture par spécialité`, ``, `Généré le ${rapport.genere_le} par \`node tools/couverture.js\`. Référence : PROFILES 2023, ${J.profiles.ssp.length} SSP (${J.profiles.source.url}, lu le ${J.profiles.source.lu_le}).`, ``,
  `| Lot | Spécialité | Statut | Pathologies | Couvertes | Partielles | Manquantes | Cas | « À vérifier » |`, `|---|---|---|---|---|---|---|---|---|`);
rapport.specialites.forEach(s => { const t = s.totaux; md.push(t ? `| ${s.lot} | [${s.nom}](${s.id}.md) | ${s.statut} | ${t.pathologies} | ${t.couvertes} | ${t.partielles} | ${t.manquantes} | ${t.cas} | ${t.tauxAVerifier} % |` : `| ${s.lot} | ${s.nom} | ${s.statut} | — | — | — | — | — | — |`); });
md.push(``, `SSP PROFILES touchées par au moins une pathologie : ${J.profiles.ssp.length - rapport.sspNonTouchees.length}/${J.profiles.ssp.length}.`, ``, `SSP non touchées : ${rapport.sspNonTouchees.join(", ")}.`, ``);
fs.writeFileSync(path.join(sortie, "INDEX.md"), md.join("\n"));

rapport.specialites.filter(s => s.totaux).forEach(s => {
  const t = s.totaux, o = [];
  o.push(`# Couverture · ${s.nom} (lot ${s.lot})`, ``, `${s.statut}. ${s.note || ""}`, ``,
    `- Pathologies : ${t.pathologies} · couvertes ${t.couvertes} · partielles ${t.partielles} · manquantes ${t.manquantes}`,
    `- Cas : ${t.cas} · cartes : ${t.cartes} · affirmations : ${t.affirmations} · « À vérifier » : ${t.aVerifier} (${t.tauxAVerifier} %)`,
    `- SSP PROFILES touchées : ${s.sspTouchees.join(", ")}`, ``,
    `| Pathologie | Fréquente | Grave | SSP | Urgence | Consultation | Final | Échelons sourcés | Statut | Manque |`, `|---|---|---|---|---|---|---|---|---|---|`);
  s.pathologies.forEach(p => o.push(`| ${p.nom} | ${p.frequente} | ${p.grave} | ${p.ssp.join(", ")} | ${p.cas.urgence} | ${p.cas.consultation} | ${p.cas.final} | ${p.echelonsSources.join(", ") || "—"} | **${p.statut}** | ${p.besoins.join(" ; ") || "—"} |`));
  o.push(``, `## Pathologies couvertes`, ...(s.pathologies.filter(p => p.statut === "couverte").map(p => `- ${p.nom}`)), s.pathologies.some(p => p.statut === "couverte") ? "" : "- aucune", ``,
    `## Pathologies manquantes ou partielles`, ...s.pathologies.filter(p => p.statut !== "couverte").map(p => `- ${p.nom} : ${p.besoins.join(" ; ")}`), ``);
  fs.writeFileSync(path.join(sortie, `${s.id}.md`), o.join("\n"));
});
const c = rapport.specialites.filter(s => s.totaux);
console.log(`Couverture écrite dans ${path.relative(RACINE, sortie) || sortie} : ${c.length} spécialité(s) avec données, ${rapport.specialites.length - c.length} à produire, ${rapport.sspNonTouchees.length} SSP non touchées.`);

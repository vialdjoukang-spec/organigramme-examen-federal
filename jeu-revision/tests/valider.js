/**
 * Validateur des données : schéma v2, sources, « À vérifier », doses, cas.
 * Usage : node tests/valider.js [dossier-specialites]   → code 1 si une erreur.
 */
const { charger } = require("../tools/charger");
const J = charger(process.argv[2]);
const r = J.schema.valider(J.specialites, J.sources, { profiles: J.profiles, parcours: J.parcours });
r.erreurs.forEach(e => console.log("ERREUR  " + e));
r.avertissements.forEach(w => console.log("AVERTIT " + w));
const s = r.stats;
console.log(`\n${s.specialites} spécialité(s), ${s.pathologies} pathologies, ${s.cartes} cartes, ${s.cas} cas, ${s.affirmations} affirmations, « À vérifier » ${s.aVerifier} (${s.tauxAVerifier} %).`);
console.log(r.erreurs.length ? `ÉCHEC : ${r.erreurs.length} erreur(s).` : "Validation réussie : 0 erreur.");
process.exit(r.erreurs.length ? 1 : 0);

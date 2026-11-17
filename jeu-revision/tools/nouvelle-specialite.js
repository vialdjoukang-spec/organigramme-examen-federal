/**
 * Gabarit : crée data/specialites/<id>.js vide et valide, prêt à remplir depuis des sources suisses.
 * Aucun contenu clinique n’est généré ; on n’ouvre aucun cours ni aucun LOT du dépôt.
 * Usage : node tools/nouvelle-specialite.js <id> [dossier]   ·   --tous [dossier] : toutes les spécialités du plan sans fichier.
 */
const fs = require("fs"), path = require("path");
const { charger, RACINE } = require("./charger");
const J = charger();
const args = process.argv.slice(2);
const tous = args[0] === "--tous";
const dir = (tous ? args[1] : args[1]) || path.join(RACINE, "data/specialites");
const plan = J.parcours.flatMap(l => l.specialites.map(s => Object.assign({ lot: l.id }, s)));
const cibles = tous ? plan.filter(s => !fs.existsSync(path.join(dir, `${s.id}.js`))) : plan.filter(s => s.id === args[0]);
if (!cibles.length) { console.error("Spécialité inconnue du parcours, ou déjà présente."); process.exit(1); }

function gabarit(s) {
  const corps = {
    schema: 2, id: s.id, nom: s.nom, lot: s.lot, statut: "brouillon",
    catalogue: { complet: false, note: "Catalogue à établir depuis les sociétés savantes, facultés et hôpitaux universitaires suisses. Chaque pathologie cite ses SSP PROFILES." },
    pathologies: [], cartes: [], cas: [], questions: []
  };
  return `/**
 * Spécialité : ${s.nom} (lot ${s.lot}). Gabarit généré par tools/nouvelle-specialite.js.
 * Remplis pathologies → cartes (8 rubriques) → cas (3 à 5 duels) → questions, puis lance node tests/valider.js.
 * Format : docs/FORMAT_AUTEUR.md. Exemple complet : data/specialites/cardiologie.js.
 */
window.JEU = window.JEU || {};
JEU.specialite(
${JSON.stringify(corps, null, 1)}
);
`;
}
fs.mkdirSync(dir, { recursive: true });
cibles.forEach(s => fs.writeFileSync(path.join(dir, `${s.id}.js`), gabarit(s)));
console.log(`${cibles.length} gabarit(s) écrit(s) dans ${dir}. Ajoute chaque fichier à index.html quand il contient au moins un cas.`);

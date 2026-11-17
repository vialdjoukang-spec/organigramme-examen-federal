/**
 * Charge les données du jeu dans Node, comme le navigateur (scripts classiques).
 * Utilisé par tests/valider.js, tools/couverture.js et tests/audit.js.
 */
const fs = require("fs"), path = require("path"), vm = require("vm");
const RACINE = path.join(__dirname, "..");

function charger(dossierSpecialites) {
  const ctx = { console };
  ctx.window = ctx; ctx.globalThis = ctx;
  vm.createContext(ctx);
  const run = f => vm.runInContext(fs.readFileSync(f, "utf8"), ctx, { filename: f });
  run(path.join(RACINE, "data/sources.js"));
  run(path.join(RACINE, "data/parcours.js"));
  run(path.join(RACINE, "data/profiles-ssp.js"));
  run(path.join(RACINE, "js/engine/schema.js"));
  ctx.JEU.specialites = [];
  ctx.JEU.specialite = sp => { ctx.JEU.specialites.push(sp); };
  const dir = dossierSpecialites || path.join(RACINE, "data/specialites");
  fs.readdirSync(dir).filter(f => f.endsWith(".js") && !f.startsWith("_")).sort().forEach(f => run(path.join(dir, f)));
  ctx.JEU.__ctx = ctx; ctx.JEU.__global = ctx;
  return ctx.JEU;
}
module.exports = { charger, RACINE };

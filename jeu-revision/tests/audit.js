/**
 * Auto-audit des données (Node, sans dépendance) :
 *  – affirmations sans source (« À vérifier ») ;
 *  – affirmations cliniques sans source suisse (seulement pharmacologie) ;
 *  – posologies présentes ; nombres de cartes par rareté.
 * Usage : node tests/audit.js > docs/AUDIT-donnees.md
 */
const fs = require("fs"), path = require("path"), vm = require("vm");
const root = path.resolve(__dirname, "..");
const ctx = { window: {} }; ctx.window.window = ctx.window; vm.createContext(ctx);
["data/sources.js", "data/systems.js", "data/cards/cardio.js", "data/services/urgences-cardio.js"]
  .forEach(f => vm.runInContext(fs.readFileSync(path.join(root, f), "utf8").replace(/window\.JEU = window\.JEU \|\| \{\};/, "var JEU = window.JEU = window.JEU || {};"), ctx));
const JEU = ctx.window.JEU;
const S = JEU.sources;
const sections = { mecanisme: "Mécanisme", signes: "Signes", exploration: "Exploration", premiere: "1re intention", contre: "Contre-indications", pieges: "Pièges" };
const out = [];
out.push("# Auto-audit des données", "", `Généré le ${new Date().toISOString().slice(0, 10)} par \`node tests/audit.js\`.`, "");
let nVerif = 0, nPharmaOnly = 0, nTot = 0;
const rar = {};
const lignesVerif = [], lignesPharma = [];
JEU.cards.forEach(c => {
  rar[c.rarete] = (rar[c.rarete] || 0) + 1;
  const all = Object.keys(sections).flatMap(k => (c[k] || []).map(a => ({ k, a })));
  all.push({ k: "rarete", a: c.rareteNote });
  all.forEach(({ k, a }) => {
    nTot++;
    const sansSrc = !a.s.length, verif = /À vérifier/.test(a.t);
    if (sansSrc || verif) { nVerif++; lignesVerif.push(`| ${c.nom} | ${sections[k] || "Rareté"} | ${a.t.replace(/\|/g, "/")} |`); }
    else if (a.s.every(id => S[id].type !== "suisse")) { nPharmaOnly++; lignesPharma.push(`| ${c.nom} | ${sections[k]} | ${a.t} | ${a.s.join(", ")} |`); }
  });
});
out.push(`- Cartes : ${JEU.cards.length} (${Object.entries(rar).map(([k, v]) => `${k} ${v}`).join(", ")}).`);
out.push(`- Affirmations : ${nTot}. Marquées « À vérifier » : ${nVerif}. Sourcées uniquement en pharmacologie internationale : ${nPharmaOnly}.`);
out.push(`- Posologies affichées : ${JEU.cards.filter(c => c.posologie).length}.`, "");
out.push("## Affirmations « À vérifier » (sans source suisse lue)", "", "| Carte | Rubrique | Affirmation |", "|---|---|---|", ...lignesVerif, "");
out.push("## Affirmations appuyées seulement sur une source de pharmacologie (autorisé pour la science fondamentale)", "", "| Carte | Rubrique | Affirmation | Source |", "|---|---|---|---|", ...lignesPharma, "");
out.push("## Sources", "", ...Object.entries(S).map(([id, s]) => `- **${id}** (${s.type}) — ${s.titre}. ${s.editeur}. <${s.url}> — lu le ${s.lu_le}. ${s.portee}`));
console.log(out.join("\n"));

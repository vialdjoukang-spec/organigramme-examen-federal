/**
 * Auto-audit des données v2 (Node, sans dépendance), par spécialité :
 *  – affirmations « À vérifier » ; affirmations appuyées seulement sur la pharmacologie internationale ;
 *  – doses détectées ; validation du schéma ; sources.
 * Usage : node tests/audit.js > docs/AUDIT-donnees.md
 */
const { charger } = require("../tools/charger");
const J = charger(), S = J.sources;
const v = J.schema.valider(J.specialites, S, { profiles: J.profiles, parcours: J.parcours });
const R = Object.fromEntries(J.schema.RUBRIQUES.map(r => [r[0], r[1]]));
const out = ["# Auto-audit des données", "", `Généré le ${new Date().toISOString().slice(0, 10)} par \`node tests/audit.js\`. Validation : ${v.erreurs.length} erreur(s), ${v.avertissements.length} avertissement(s).`, ""];
J.specialites.forEach(sp => {
  let tot = 0, av = 0, ph = 0, doses = 0; const lv = [], lp = [];
  const voir = (c, k, a) => {
    if (!a || a.na) return; tot++;
    if (J.schema.DOSE.test(a.t)) doses++;
    if (!a.s.length || /À vérifier/.test(a.t)) { av++; lv.push(`| ${c.nom} | ${R[k] || k} | ${a.t.replace(/\|/g, "/")} |`); }
    else if (a.s.every(id => S[id].type !== "suisse")) { ph++; lp.push(`| ${c.nom} | ${R[k] || k} | ${a.t} | ${a.s.join(", ")} |`); }
  };
  sp.cartes.forEach(c => { Object.entries(c.rubriques).forEach(([k, L]) => L.forEach(a => voir(c, k, a))); (c.contre || []).forEach(a => voir(c, "contre", a)); (c.pieges || []).forEach(a => voir(c, "pièges", a)); voir(c, "fréquence", c.noteFrequence); });
  out.push(`## ${sp.nom}`, "", `- Pathologies : ${sp.pathologies.length} · cartes : ${sp.cartes.length} · cas : ${sp.cas.length} · questions rédigées : ${(sp.questions || []).length}.`,
    `- Affirmations : ${tot}. « À vérifier » : ${av} (${tot ? Math.round(av / tot * 1000) / 10 : 0} %). Pharmacologie internationale seule : ${ph}. Doses détectées : ${doses}.`, "",
    "### Affirmations « À vérifier »", "", "| Carte | Rubrique | Affirmation |", "|---|---|---|", ...lv, "",
    "### Affirmations appuyées seulement sur la pharmacologie internationale (autorisé)", "", "| Carte | Rubrique | Affirmation | Source |", "|---|---|---|---|", ...lp, "");
});
out.push("## Sources", "", ...Object.entries(S).map(([id, s]) => `- **${id}** (${s.type}${s.categorie ? " · " + s.categorie : ""}) — ${s.titre}. ${s.editeur}. <${s.url}> — lu le ${s.lu_le}. ${s.portee}`));
console.log(out.join("\n"));

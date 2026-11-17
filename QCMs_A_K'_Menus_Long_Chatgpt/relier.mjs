// node relier.mjs G2_OBJECTIFS.json index.html sortie.html
import fs from 'node:fs';
const [registre, entree, sortie] = process.argv.slice(2);
if (!sortie || sortie === entree) throw Error('Indiquer le registre, la banque source et un fichier de sortie distinct.');
const doc = JSON.parse(fs.readFileSync(registre, 'utf8'));
const html = fs.readFileSync(entree, 'utf8');
const pattern = /(<script type="application\/json" id="donnees">)([^<]+)(<\/script>)/;
const data = JSON.parse(html.match(pattern)[2]);
const ids = new Set();
const questions = new Map(data.items.map(q => [q.id, q]));
const objectifs = data.production.objectifsFacultaires ??= {};
for (const row of doc.items) {
  const q = questions.get(row.id), source = doc.objectives[row.objective_id];
  if (!q || q.code !== doc.ssp || ids.has(q.id) || q.aim !== row.aim) throw Error('Rattachement incohérent : '+row.id);
  if (!source?.institution || !source.section || !source.document || !source.learning_objective || !/^https:\/\//.test(source.url)) throw Error('Source incomplète : '+row.id);
  if (!row.rationale || !row.relationship) throw Error('Justification absente : '+row.id);
  if (objectifs[row.objective_id] && JSON.stringify(objectifs[row.objective_id]) !== JSON.stringify(source)) throw Error('Objectif partagé modifié : '+row.objective_id);
  ids.add(q.id);
  objectifs[row.objective_id] = source;
  q.objectifFacultaire = row.objective_id;
  q.rattachement = row.relationship;
  q.motifRattachement = row.rationale;
  q.objective = source.url;
}
const output = html.replace(pattern, (_, a, body, b) => a + JSON.stringify(data).replace(/</g, '\\u003c') + b);
fs.writeFileSync(sortie, output);
console.log(`${doc.ssp} : ${ids.size} objectifs rattachés aux corrigés.`);

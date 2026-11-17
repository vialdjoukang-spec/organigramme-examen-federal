// node rapprocher.mjs LOT.json [index.html] [--en-cours]
// Avec --en-cours, confronter aussi les réservations déjà rédigées des autres tranches.
import {readFileSync,readdirSync,existsSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
import {basename, dirname, join} from 'node:path';

const args = process.argv.slice(2);
const [lot, index = fileURLToPath(new URL('./index.html', import.meta.url))] = args.filter(x => x !== '--en-cours');
if (!lot) throw Error('Fournir le fichier JSON du lot ou du sous-lot.');
const data = JSON.parse(readFileSync(index, 'utf8').match(/id="donnees">([^<]+)<\/script>/)[1]);
const input = JSON.parse(readFileSync(lot, 'utf8'));
const proposed = Array.isArray(input) ? input : input.items;
const stop = new Set('apres avec avoir chez cette contre devant elle elles etre femme font homme leurs leur meme plus pour prise rapide rechercher retrouve sans sont sous selon suite vers vous ainsi dans dont entre faire faut jeune jours lors mois ou quel quelle quels quelles signe signes patients patiente patient prise choisir clinique clinical examen examens' .split(' '));
function terms(str) {
  return new Set(str.normalize('NFD').replace(/\p{M}/gu, '').toLowerCase().replaceAll('œ','oe').split(/[^a-z0-9]+/).filter(t => t.length > 3 && !stop.has(t)).map(t => t.length > 5 ? t.replace(/s$/, '') : t));
}
function decision(q) {
  return terms([q.aim, q.answer, ...(q.options || []).filter(o => o[1]).map(o => o[0])].join(' '));
}
// Les brouillons peuvent précéder le lot contrôlé ou être réservés plus loin dans la file.
const bodyName = /^(\d+)-([GSFO]\d+(?:\.\d+)*)-(\d+)\.json$/;
const localId = (code, n) => code + '-' + String(n).padStart(3,'0');
const head = basename(lot).match(bodyName);
const start = input.start || (head && Number(head[3]));
const ids = proposed.map((q,i) => q.id || (start ? localId(q.code, start+i) : null));
const reserved = [];
if (args.includes('--en-cours')) {
  const dir = join(dirname(index),'en_cours');
  if (!existsSync(dir)) throw Error('Dossier en_cours/ introuvable auprès de la banque.');
  const ignored = new Set([...data.items.map(q=>q.id), ...ids.filter(Boolean)]);
  for (const entry of readdirSync(dir).sort()) {
    const parts = entry.match(bodyName);
    if (!parts || basename(lot)===entry) continue;
    const rows = JSON.parse(readFileSync(join(dir,entry),'utf8'));
    if (!Array.isArray(rows) || rows.some(q=>q.code!==parts[2])) throw Error('Tranche incompatible : '+entry);
    rows.forEach((q,i)=>{
      const id=localId(parts[2],Number(parts[3])+i);
      if (!ignored.has(id)) {reserved.push({...q,id});ignored.add(id)}
    });
  }
}
const indexed = [...data.items, ...reserved];
const questions = [...indexed, ...proposed];
const vectors = questions.map(q => ({action:decision(q), cas:terms(q.case)}));
const frequency = new Map();
for (const row of vectors) for (const word of new Set([...row.action, ...row.cas])) frequency.set(word, (frequency.get(word) || 0) + 1);
const weights = new Map(Array.from(frequency, ([word, n]) => [word, 1 + Math.log((1 + vectors.length) / (1 + n))]));
function similarity(a, b) {
  let common = 0, totalA = 0, totalB = 0;
  for (const t of a) { const w = weights.get(t); totalA += w; if (b.has(t)) common += w; }
  for (const t of b) totalB += weights.get(t);
  return common / (Math.sqrt(totalA * totalB) || 1);
}
function id(i) {
  const q = questions[i];
  return q.id || ids[i-indexed.length] || `proposition ${i-indexed.length+1}`;
}
for (let i = indexed.length; i < questions.length; i++) {
  const hits = [];
  for (let j = 0; j < i; j++) {
    if (id(i) === id(j)) continue;
    const score = 0.72 * similarity(vectors[i].action, vectors[j].action) + 0.28 * similarity(vectors[i].cas, vectors[j].cas);
    hits.push({id:id(j), decision:questions[j].aim, score:Number(score.toFixed(3))});
  }
  hits.sort((a,b) => b.score - a.score);
  console.log(JSON.stringify({item:id(i), decision:questions[i].aim, comparer:hits.slice(0,3)}));
}

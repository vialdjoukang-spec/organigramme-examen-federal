// node rapprocher.mjs LOT.json [index.html] ; rapprochements à examiner avant audit.
import {readFileSync} from 'node:fs';
import {fileURLToPath} from 'node:url';

const [lot, index = fileURLToPath(new URL('./index.html', import.meta.url))] = process.argv.slice(2);
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
const questions = [...data.items, ...proposed];
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
  return q.id || (input.start ? `${q.code}-${String(input.start + i - data.items.length).padStart(3, '0')}` : `proposition ${i - data.items.length + 1}`);
}
for (let i = data.items.length; i < questions.length; i++) {
  const hits = [];
  for (let j = 0; j < i; j++) {
    if (questions[i].id && questions[i].id === questions[j].id) continue;
    const score = 0.72 * similarity(vectors[i].action, vectors[j].action) + 0.28 * similarity(vectors[i].cas, vectors[j].cas);
    hits.push({id:id(j), decision:questions[j].aim, score:Number(score.toFixed(3))});
  }
  hits.sort((a,b) => b.score - a.score);
  console.log(JSON.stringify({item:id(i), decision:questions[i].aim, comparer:hits.slice(0,3)}));
}

// node integrer.mjs lot.json [index.html]
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {execFileSync} from 'node:child_process';
const home = path.dirname(fileURLToPath(import.meta.url));
const target = path.resolve(process.argv[3] || path.join(home, 'index.html'));
const batch = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const original = fs.readFileSync(target, 'utf8');
const pattern = /(<script type="application\/json" id="donnees">)([^<]+)(<\/script>)/;
const match = original.match(pattern);
if (!match) throw Error('Données embarquées absentes');
const data = JSON.parse(match[2]);
const code = data.catalogue.find(([c]) => !data.production.statuts[c].clos)?.[0];
const previous = data.items.filter(q => q.code === code).length;
if (!code || batch.code !== code || batch.start !== previous + 1) throw Error('SSP actif ou numéro de reprise incorrect');
if (batch.items.length !== 20 || !batch.audit?.result || batch.audit.lot !== data.audits.length+1) throw Error('Lot ou audit incomplet');
const signatures = new Set(data.items.map(q => q.aim.trim().toLocaleLowerCase('fr')));
for (const [i,q] of batch.items.entries()) {
  const key = q.aim.trim().toLocaleLowerCase('fr');
  if (q.code !== code || signatures.has(key)) throw Error('Objectif dupliqué ou SSP incorrect : '+q.aim);
  signatures.add(key);
  q.id = code+'-'+String(batch.start+i).padStart(3,'0');
  data.items.push(q);
  if (q.type === 'M' && !data.lexique.includes(q.options[0][0])) data.lexique.push(q.options[0][0]);
}
data.production.statuts[code].integrees = previous+batch.items.length;
data.lexique.sort((a,b)=>a.localeCompare(b,'fr'));
data.audits.push({...batch.audit,items:batch.items.length});
const output = original.replace(pattern,(_,open,body,close)=>open+JSON.stringify(data).replace(/</g,'\\u003c')+close);
const stage = fs.mkdtempSync(path.join(path.dirname(target),'.qcm-'));
try {
  fs.writeFileSync(path.join(stage,'index.html'),output);
  fs.copyFileSync(path.join(home,'verifier.mjs'),path.join(stage,'verifier.mjs'));
  execFileSync(process.execPath,[path.join(stage,'verifier.mjs')],{stdio:'pipe'});
  if (fs.readFileSync(target,'utf8') !== original) throw Error('Modification concurrente, reprendre sur la dernière version');
  fs.renameSync(path.join(stage,'index.html'),target);
  console.log(JSON.stringify({code,lot:batch.audit.lot,total:data.items.length,ssp:data.production.statuts[code].integrees}));
} finally {
  fs.rmSync(stage,{recursive:true,force:true});
}

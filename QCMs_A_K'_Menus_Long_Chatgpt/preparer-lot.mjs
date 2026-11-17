// Depuis la banque : node preparer-lot.mjs 033 G4 1 > lot.json
// Puis : node integrer.mjs lot.json && node verifier.mjs
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {dirname,join} from 'node:path';
const home=dirname(fileURLToPath(import.meta.url));
const [numero,code,debut]=process.argv.slice(2);
const lot=Number(numero),start=Number(debut);
if (!Number.isSafeInteger(lot)||lot<1||!Number.isSafeInteger(start)||start<1||!(/^[GSFO]\d+(\.\d+)*$/.test(code))) throw Error('Indiquer numéro de lot, code local et première question.');
const tag=String(lot).padStart(3,'0');
const auditName=`AUDIT-${tag}-${code}.json`;
const audit=JSON.parse(readFileSync(join(home,'en_cours',auditName),'utf8'));
if (audit.statut!=='validé' || !Array.isArray(audit.fourFinalBlobs) || audit.fourFinalBlobs.length!==4) throw Error('Manifeste ou contre-audit incomplet : '+auditName);
const items=[];
for (const offset of [0,5,10,15]) {
  const n=start+offset;
  const file=`${tag}-${code}-${String(n).padStart(3,'0')}.json`;
  const body=readFileSync(join(home,'en_cours',file));
  const hash=createHash('sha1').update(`blob ${body.byteLength}\0`).update(body).digest('hex');
  if (audit.fourFinalBlobs.find(r=>r.start===n)?.sha!==hash) throw Error('Le manuscrit a changé après le contre-audit : '+file);
  const group=JSON.parse(body.toString('utf8'));
  if (!Array.isArray(group)||group.length!==5||group.some(q=>q.code!==code)) throw Error('Cinq questions du même SSP requises : '+file);
  for(const q of group){if(q.menuLong&&!q.menu){q.menu=q.menuLong;delete q.menuLong}items.push(q)}
}
if(!/^\d{4}-\d{2}-\d{2}$/.test(audit.date)) throw Error('Date du contre-audit absente.');
const result=`Contre-audit indépendant validé en_cours/${auditName}. Les quatre empreintes des cinq questions correspondent aux manuscrits relus.`;
console.log(JSON.stringify({code,start,items,audit:{lot,date:audit.date,result}},null,2));

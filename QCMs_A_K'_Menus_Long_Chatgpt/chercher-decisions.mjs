// node chercher-decisions.mjs DRESS
// node chercher-decisions.mjs "retour à l’école" commotion
// Ajouter --en-cours pour vérifier également les manuscrits non publiés.
import {readFileSync,readdirSync} from 'node:fs';
import {dirname,join} from 'node:path';
import {fileURLToPath} from 'node:url';
const dir=dirname(fileURLToPath(import.meta.url));
const args=process.argv.slice(2);
const normal=s=>String(s||'').toLowerCase().normalize('NFD').replace(/\p{M}/gu,'').replaceAll('œ','oe').replaceAll('’',"'");
const mots=args.filter(x=>x!=='--en-cours');
const termes=mots.map(normal);
const acronymes=new Set(mots.filter(x=>/^[A-Z0-9]{2,12}$/.test(x)).map(normal));
function position(texte,terme){
  if(!acronymes.has(terme))return texte.indexOf(terme);
  return texte.search(new RegExp('(?<![a-z0-9])'+terme+'(?![a-z0-9])'));
}
if(!termes.length)throw Error('Indiquer au moins une notion, une clé ou un acronyme.');
const bank=JSON.parse(readFileSync(join(dir,'index.html'),'utf8').match(/id="donnees">([^<]+)<\/script>/)[1]);
const rows=bank.items.map(q=>({q,origin:'publié'}));
const occupied=new Set(rows.map(row=>row.q.id));
if(args.includes('--en-cours')){
  for(const file of readdirSync(join(dir,'en_cours')).sort()){
    const parts=file.match(/^\d+-([GSFO]\d+(?:\.\d+)*)-(\d+)\.json$/);
    if(!parts)continue;
    const group=JSON.parse(readFileSync(join(dir,'en_cours',file),'utf8'));
    group.forEach((q,i)=>{
      const id=parts[1]+'-'+String(Number(parts[2])+i).padStart(3,'0');
      if(!occupied.has(id)){rows.push({q:{...q,id},origin:file});occupied.add(id)}
    });
  }
}
const findings=[];
for(const {q,origin} of rows){
  const relevant=[['décision',q.aim],['réponse',q.answer],['énoncé',q.case],['question',q.ask],['argumentation',q.why]];
  q.options.forEach(([option,correct,reason])=>relevant.push([correct?'option exacte':'distracteur',option],['commentaire de proposition',reason]));
  q.recap.forEach(phrase=>relevant.push(['rappel',phrase]));
  const texts=relevant.map(([field,s])=>[field,String(s||''),normal(s)]);
  if(!termes.every(t=>texts.some(([, ,v])=>position(v,t)>=0)))continue;
  const rank=([field])=>['décision','réponse','option exacte','énoncé','question','argumentation','rappel','commentaire de proposition','distracteur'].indexOf(field);
  const matched=texts.filter(([, ,v])=>termes.some(t=>position(v,t)>=0)).sort((a,b)=>rank(a)-rank(b));
  const [field,original,value]=matched[0];
  const offset=Math.max(0,Math.min(...termes.filter(t=>position(value,t)>=0).map(t=>position(value,t)))-40);
  findings.push({rang:rank(matched[0]),id:q.id,origine:origin,decision:q.aim,trouveDans:[...new Set(matched.map(row=>row[0]))],extrait:(offset?'…':'')+original.slice(offset,offset+190)});
}
findings.sort((a,b)=>a.rang-b.rang||a.id.localeCompare(b.id,'fr',{numeric:true}));
for(const {rang,...row} of findings)console.log(JSON.stringify(row));

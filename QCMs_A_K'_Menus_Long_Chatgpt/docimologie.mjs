// node docimologie.mjs [index.html] [code SSP]
import {readFileSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
const [path=fileURLToPath(new URL('./index.html',import.meta.url)),ssp]=process.argv.slice(2);
const data=JSON.parse(readFileSync(path,'utf8').match(/id="donnees">([^<]+)<\/script>/)[1]);
for (const [code] of data.catalogue.filter(([code])=>!ssp||code===ssp)) {
  const items=data.items.filter(q=>q.code===code);
  if(!items.length)continue;
  const a=items.filter(q=>q.type==='A'),k=items.filter(q=>q.type==='K');
  const fortes=[],profil=[0,0,0,0,0];
  let maxUnique=0, exAequo=0;
  for(const q of a){
    const n=x=>Array.from(x[0].trim()).length;
    const cle=n(q.options.find(x=>x[1]));
    const autre=Math.max(...q.options.filter(x=>!x[1]).map(n));
    if(cle>autre)maxUnique++;
    if(cle===autre)exAequo++;
    if(cle>1.6*autre)fortes.push({id:q.id,rapport:Number((cle/autre).toFixed(2))});
  }
  for(const q of k)profil[q.options.filter(o=>o[1]).length]++;
  console.log(JSON.stringify({code,typesA:a.length,cleLaPlusLongue:maxUnique,exAequo,clesLonguesAExaminer:fortes,typesK:k.length,nombreDeVraies:profil}));
}

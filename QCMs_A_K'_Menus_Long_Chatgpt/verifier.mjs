import {readFileSync} from 'node:fs';
const html = readFileSync(new URL('./index.html', import.meta.url), 'utf8');
const data = JSON.parse(html.match(/id="donnees">([^<]+)<\/script>/)[1]);
function verify(d){
const fail=m=>{throw Error(m)}, ids=new Set(), sig=new Set(), counts={G:0,S:0,F:0,O:0}, types={A:0,K:0,M:0};
for(const [c,t] of d.catalogue){if(!t||ids.has(c)||!Array.isArray(d.agenda[c]))fail(c);ids.add(c);counts[c[0]]++}
if(JSON.stringify(counts)!==JSON.stringify({G:16,S:113,F:44,O:75}))fail("Catalogue incomplet");
for(const q of d.items){if(!ids.has(q.code)||!q.ask||!q.why||!q.aim||!q.answer||q.recap.length!==7||q.recap.some(s=>!s.trim())||!q.sources.length)fail(q.aim);
for(const u of [q.objective,...q.sources])if(!/^https?:\/\//.test(u))fail(u);
const n=q.options.length,truth=q.options.filter(o=>o[1]).length;
if(!(q.type in types)||q.options.some(o=>o.length!==3||typeof o[1]!=="boolean"||!o[2]))fail(q.aim);
if(q.type==="A"&&(n<3||n>5||truth!==1)||q.type==="K"&&n!==4||q.type==="M"&&(n!==1||truth!==1||!d.lexique.includes(q.options[0][0])))fail(q.aim);
const key=q.case.trim().toLowerCase()+"|"+q.ask.trim().toLowerCase();if(sig.has(key))fail("Doublon "+q.aim);sig.add(key);types[q.type]++}

const sequences=new Map();
for(const q of d.items){
  const n=(sequences.get(q.code)||0)+1;
  const expected=q.code+'-'+String(n).padStart(3,'0');
  if(q.id!==expected)fail('Identifiant hors séquence : '+q.id+' ; attendu '+expected);
  sequences.set(q.code,n);
  if(q.type==='M'){
    const pool=q.familleMenu ? d.production.menusLongs?.[q.code]?.pools?.[q.familleMenu] : q.menu;
    if(q.familleMenu&&!Array.isArray(pool))fail('Famille de menu absente : '+q.id);
    if(pool&&(!Array.isArray(pool)||pool.filter(t=>t===q.options[0][0]).length!==1||pool.some(t=>typeof t!=='string'||!t.trim())))fail('Clé absente, répétée ou menu illisible : '+q.id);
  }
  if(q.objectifFacultaire||d.production.statuts[q.code]?.clos&&d.production.statuts[q.code]?.registre){
    const obj=d.production.objectifsFacultaires?.[q.objectifFacultaire];
    if(!obj?.institution||!obj.section||!obj.learning_objective||!q.rattachement||!q.motifRattachement)fail('Rattachement incomplet : '+q.id);
  }
}

const plan=d.production;
if(!plan || plan.minimumParSSP < 200 || plan.minimumTotal !== d.catalogue.length * plan.minimumParSSP)fail("Seuil de production incorrect");
const progress={};
for(const [code] of d.catalogue){
  const total=d.items.filter(q=>q.code===code).length;
  const state=plan.statuts[code];
  if(!state || state.integrees!==total || state.minimum < 200)fail("Progression incohérente "+code);
  if(state.clos && (total<state.minimum || !state.couvertureComplete || !state.auditComplet))fail("Clôture prématurée "+code);
  progress[code]={integrees:total,minimum:state.minimum,reste:Math.max(0,state.minimum-total)};
}
return {progression:progress,catalogue:ids.size,branches:counts,items:d.items.length,formats:types,plan:Object.values(d.agenda).flat().length}}
console.log(JSON.stringify(verify(data), null, 2));

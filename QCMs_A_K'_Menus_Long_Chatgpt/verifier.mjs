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
return {catalogue:ids.size,branches:counts,items:d.items.length,formats:types,plan:Object.values(d.agenda).flat().length}}
console.log(JSON.stringify(verify(data), null, 2));

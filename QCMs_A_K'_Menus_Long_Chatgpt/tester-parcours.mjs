import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import {webcrypto} from 'node:crypto';
const html=fs.readFileSync(process.argv[2]||'index.html','utf8');
const raw=html.match(/id="donnees">([^<]+)<\/script>/)[1], data=JSON.parse(raw);
class Element {
  constructor(){this.value='';this.children=[];this.innerHTML='';this.textContent='';}
  append(...els){this.children.push(...els)}
  replaceChildren(...els){this.children=els;this.textContent=''}
  setAttribute(k,v){this[k]=v}
  showModal(){this.open=true}
  close(){this.open=false}
}
const dom=new Map();function el(id){if(!dom.has(id))dom.set(id,new Element);return dom.get(id)}
el('#donnees').textContent=raw;
const script=[...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].at(-1)[1];
vm.runInNewContext(script,{document:{querySelector:el,createElement:()=>new Element},crypto:webcrypto,URL});
function click(container,dataset){el(container).onclick({target:{closest:()=>({dataset})}})}
const actifs=[...new Set(data.items.map(q=>q.code))];
for(const code of actifs){click('#tabs',{family:code[0]});click('#ssps',{code});const group=data.items.filter(q=>q.code===code);assert.equal((el('#body').innerHTML.match(/<article>/g)||[]).length,group.length);click('#body',{correct:'0'});assert(el('#modal').open);assert(el('#corr').innerHTML.includes('RAISONNEMENT CLINIQUE'));el('#close').onclick();assert(!el('#modal').open)}
for (const type of ['A','K','M']) {
  const question=data.items.find(q=>q.type===type);
  if(!question)continue;
  click('#tabs',{family:question.code[0]});
  click('#ssps',{code:question.code});
  const index=data.items.filter(q=>q.code===question.code).indexOf(question);
  const div=el('#opts'+index);
  if(type==='M'){
    const [input,results]=div.children.slice(-2);
    input.value=question.options[0][0];
    input.oninput();
    const choix=results.children.find(item=>item.textContent===input.value);
    assert(choix,question.id);
    choix.onclick();
  } else {
    question.options.forEach((option,i)=>{
      if(type==='K'||option[1])div.onchange({target:{dataset:{i},value:String(option[1])}});
    });
  }
  click('#body',{correct:String(index)});
  assert(el('#corr').innerHTML.includes('Score · 1 / 1'),question.id);
  el('#close').onclick();
}
for(const code of actifs){
 const groupe=data.production.menusLongs?.[code];
 click('#tabs',{family:code[0]});click('#ssps',{code});let n=0;
 for(const q of data.items.filter(x=>x.code===code)){
   if(q.type==='K'){
     const rendered=el('#opts'+n).innerHTML;
     const indices=Array.from(rendered.matchAll(/data-i="(\d+)" value="true"/g), match=>Number(match[1]));
     assert.equal(indices.length,4,q.id);
     const key=indices.map((i,j)=>(j+1)+'. '+(q.options[i][1]?'Vrai':'Faux')).join(' · ');
     click('#body',{correct:String(n)});
     assert(el('#corr').innerHTML.includes('Dans l’ordre affiché : '+key),q.id);
     el('#close').onclick();
   }
   if(q.type==='M'){
     const cle=q.options[0][0],aliases=groupe?.aliases?.[cle]||q.aliases||[];
     const [champ,res]=el('#opts'+n).children.slice(-2);
     for(const terme of new Set([cle,...aliases])){
       if(terme.trim().length<2)continue;
       champ.value=terme;champ.oninput();const choix=res.children.find(e=>e.textContent===cle);assert(choix,`${q.id} : ${terme}`);choix.onclick();
     }
     click('#body',{correct:String(n)});assert(el('#corr').innerHTML.includes('Score · 1 / 1'),q.id);el('#close').onclick();
   }
   n++;
 }
}
click('#tabs',{page:'plan'});assert(el('#body').innerHTML.includes('Plan question par question'));click('#tabs',{page:'watch'});assert.equal(el('#watch').hidden,false);console.log('Parcours logiques validés pour '+actifs.length+' SSP, clés et synonymes des menus, trois formats, corrigés, plan et veille.');

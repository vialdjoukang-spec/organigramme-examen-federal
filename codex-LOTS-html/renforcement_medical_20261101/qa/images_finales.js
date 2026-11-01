const{chromium}=require('playwright');
const fs=require('fs'),path=require('path'),crypto=require('crypto'),assert=require('assert');
const BASE=path.resolve(__dirname,'../..'),D=path.join(__dirname,'images_finales');fs.mkdirSync(D,{recursive:true});
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const report={date:new Date().toISOString(),portee:'Rendu des paires, accès, repères et contraste ; ne valide pas le diagnostic médical ni la licence.',rendus:[],erreurs:[]};
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/chromium',args:['--no-sandbox']});
 try{
  for(const n of [18,29])for(const mobile of [false,true])for(const sombre of [false,true]){
   const lot=String(n).padStart(3,'0'),file=`LOT_${lot}/LOT_${lot}_Phase_A_V0.html`,raw=fs.readFileSync(path.join(BASE,file));
   const page=await browser.newPage({viewport:mobile?{width:390,height:844}:{width:1365,height:1000},isMobile:mobile,hasTouch:mobile,colorScheme:sombre?'dark':'light'});page.setDefaultTimeout(6000);
   await page.setContent(raw.toString('utf8'));await page.evaluate(()=>document.fonts.ready);
   await page.locator('h2[id$="-p9"]').locator('..').locator('button[popovertarget]').first().click();
   await page.locator(`[popovertarget="image-reelle-${lot}"]:not([popovertargetaction="hide"])`).click();
   const w=page.locator(`#image-reelle-${lot}`);assert(await w.evaluate(e=>e.matches(':popover-open')));
   const fig=w.locator('.illustration');assert.equal(await fig.count(),1);assert.equal(await fig.locator('.paire > div').count(),2);
   assert(await fig.locator('.paire img').evaluate(e=>e.complete&&e.naturalWidth>0));
   const row={fichier:file,sha256:sha(raw),mobile,sombre,captures:[],repères:[]};
   const label=`lot${lot}-${mobile?'mobile':'bureau'}-${sombre?'sombre':'clair'}`;
   for(const [name,node] of [['original',fig.locator('.paire > div').nth(0)],['annote',fig.locator('.paire > div').nth(1)],['legende',fig.locator('figcaption')]]){
    await node.scrollIntoViewIfNeeded();await page.evaluate(()=>getSelection()?.removeAllRanges());const capture=label+'-'+name+'.png';await page.screenshot({path:path.join(D,capture)});row.captures.push(capture);
   }
   row.couleurs=await fig.locator('h3,h4,a').evaluateAll(es=>es.map(e=>({texte:e.textContent.trim(),couleur:getComputedStyle(e).color,fond:getComputedStyle(e.closest('.illustration')).backgroundColor})));
   for(const c of row.couleurs){const ns=c.couleur.match(/[\d.]+/g)||[];if(ns.slice(0,3).every(v=>+v>190))report.erreurs.push({file,mobile,sombre,erreur:'Texte trop pâle sur fond blanc',element:c})}
   const reps=fig.locator('.repere');
   for(let i=0;i<await reps.count();i++){
    const rep=reps.nth(i);await rep.scrollIntoViewIfNeeded();
    if(!mobile){await rep.hover();assert(await rep.locator('.nom').isVisible())}
    if(mobile)await rep.tap();else await rep.click();const target=await rep.getAttribute('popovertarget');const popup=page.locator(`[id="${target}"]`);assert(await popup.evaluate(e=>e.matches(':popover-open')));
    const metric=await popup.evaluate(e=>({texte:e.textContent.trim(),couleur:getComputedStyle(e).color,fond:getComputedStyle(e).backgroundColor,debordement:e.scrollWidth>e.clientWidth+1}));
    row.repères.push({id:target,...metric});if(metric.debordement)report.erreurs.push({file,mobile,sombre,target,erreur:'Débordement de définition'});
    if(i===0){const capture=label+'-definition.png';await page.screenshot({path:path.join(D,capture)});row.captures.push(capture)}
    await popup.locator(`[popovertarget="${target}"][popovertargetaction="hide"]`).click();
   }
   row.debordement=await w.evaluate(e=>e.scrollWidth>e.clientWidth+1);assert(!row.debordement);await w.locator(`:scope > .barre button`).click();assert(!(await w.evaluate(e=>e.matches(':popover-open'))));
   row.sha_stable=sha(fs.readFileSync(path.join(BASE,file)))===row.sha256;if(!row.sha_stable)report.erreurs.push({file,erreur:'Fichier modifié pendant test'});
   report.rendus.push(row);await page.close();
  }
 }finally{await browser.close();fs.writeFileSync(path.join(D,'IMAGES.json'),JSON.stringify(report,null,2)+'\n')}
 console.log(JSON.stringify({rendus:report.rendus.length,erreurs:report.erreurs.length}));process.exitCode=report.erreurs.length?1:0;
})().catch(e=>{console.error(e);process.exit(1)});

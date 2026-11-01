const fs=require('fs'),path=require('path'),crypto=require('crypto');
const {chromium}=require('playwright');
const D=__dirname, B=path.dirname(D), Q=path.join(D,'qa');fs.mkdirSync(Q,{recursive:true});
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/chromium',args:['--no-sandbox']});
 const rows=[];
 for(const lot of ['018','029']) for(const mobile of [false,true]) for(const colorScheme of ['light','dark']){
  const file=`LOT_${lot}/LOT_${lot}_Phase_B_V0_DX.4.html`,raw=fs.readFileSync(path.join(B,file));
  const page=await browser.newPage({viewport:mobile?{width:390,height:844}:{width:1440,height:1200},colorScheme});
  const errors=[];page.on('pageerror',e=>errors.push(e.message));await page.setContent(raw.toString());await page.evaluate(()=>document.fonts.ready);
  const prefix=`${lot}-${mobile?'mobile':'bureau'}-${colorScheme}`;
  const direct=await page.locator('section:has(h2[id*="-p"]) button[popovertarget]').evaluateAll(ns=>ns.map(n=>n.getAttribute('popovertarget')));
  if(direct.length!==14)throw Error('14 fenêtres attendues');let answers=0;
  for(const id of direct){
   await page.evaluate(()=>document.querySelectorAll('[popover]').forEach(x=>{if(x.matches(':popover-open'))x.hidePopover()}));
   await page.locator(`section button[popovertarget="${id}"]`).click();
   if(!await page.locator('#'+id).evaluate(e=>e.matches(':popover-open')))throw Error('Fenêtre fermée '+id);
   const over=await page.locator('#'+id).evaluate(e=>e.scrollWidth>e.clientWidth+2);if(over)throw Error('Débordement '+id);
   const quiz=page.locator(`#${id} details.quiz`);
   for(let i=0;i<await quiz.count();i++){await quiz.nth(i).locator('summary').click();if(!await quiz.nth(i).getAttribute('open').then(x=>x!==null))throw Error('Réponse fermée');answers++;}
  }
  await page.evaluate(()=>document.querySelectorAll('[popover]').forEach(x=>{if(x.matches(':popover-open'))x.hidePopover()}));
  await page.locator('section button[popovertarget="dx4-detail9"]').click();
  const imageId='dx4-detail9';

  const figure=page.locator(`#${imageId} figure.illustration`);
  if(await figure.count())await figure.scrollIntoViewIfNeeded();
  await page.screenshot({path:path.join(Q,`${prefix}-image.png`)});
  const defs=await figure.locator('button.repere[popovertarget]').evaluateAll(ns=>ns.map(n=>n.getAttribute('popovertarget')));
  for(const id of defs){
   const button=figure.locator(`button.repere[popovertarget="${id}"]`);
   const parent=button.locator('xpath=ancestor::details[1]');
   if(await parent.count() && !await parent.getAttribute('open').then(x=>x!==null))await parent.locator('summary').first().click();
   await button.click();
   if(!await page.locator('#'+id).evaluate(e=>e.matches(':popover-open')))throw Error('Définition fermée');
   await page.locator(`#${id} button[popovertargetaction="hide"]`).click();
  }
  await page.locator('#'+imageId).evaluate(e=>e.scrollTop=e.scrollHeight);
  await page.screenshot({path:path.join(Q,`${prefix}-legende.png`)});
  if(errors.length)throw Error(errors.join(';'));
  rows.push({fichier:file,sha256:crypto.createHash('sha256').update(raw).digest('hex'),mobile,colorScheme,fenetres_directes:direct.length,reponses_ouvertes:answers,definitions_ouvertes:defs.length,debordement:false,erreurs:errors,captures:[`${prefix}-image.png`,`${prefix}-legende.png`]});await page.close();
 }
 await browser.close();fs.writeFileSync(path.join(Q,'CONTROLE_NAVIGATEUR.json'),JSON.stringify({date:new Date().toISOString(),methode:'Chromium réel, contenu local setContent, clics Playwright ; captures à inspecter séparément',rendus:rows},null,2)+'\n');console.log(JSON.stringify({rendus:rows.length,fenetres:rows.reduce((s,x)=>s+x.fenetres_directes,0),reponses:rows.reduce((s,x)=>s+x.reponses_ouvertes,0)}));
})().catch(e=>{console.error(e);process.exit(1)});

const fs=require('fs'),path=require('path'),crypto=require('crypto'),{chromium}=require('playwright');
(async()=>{
 const d=__dirname,raw=fs.readFileSync(path.join(d,'../../BILAN_IMAGERIE_ECG.html'));
 const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});const essais=[];
 try{
  for(const [vue,width] of [['ordinateur',1200],['mobile',390]]){
   const c=await browser.newContext({viewport:{width,height:950},hasTouch:vue==='mobile'}),p=await c.newPage();await p.setContent(raw.toString());
   const cli=async x=>vue==='mobile'?x.tap():x.click();
   if(await p.locator('details.lecon:visible').count()!==215||await p.locator('[data-triage="effectue"]').count()!==44)throw Error('Comptes du bilan');
   if(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Débordement');
   essais.push({vue,action:'comptes',mentions:215,triages:44});await p.screenshot({path:path.join(d,`accueil-${vue}.png`)});
   for(const lot of ['LOT_020','LOT_021']){
    await p.fill('#recherche',lot);if(await p.locator('details.lecon:visible').count()!==9)throw Error('Recherche '+lot);essais.push({vue,action:'recherche',lot,affiches:9});
   }
   await p.fill('#recherche','');if(await p.locator('details.lecon:visible').count()!==215)throw Error('Réinitialisation');essais.push({vue,action:'reinitialiser',affiches:215});
   const cs=await p.locator('details.candidat-suite').all();if(cs.length!==3)throw Error('Candidats');
   for(let i=0;i<cs.length;i++){
    await cli(cs[i].locator('summary'));if(await cs[i].getAttribute('open')===null)throw Error('Ouverture candidat');
    if(!(await cs[i].innerText()).includes('CC BY 4.0'))throw Error('Licence');
    essais.push({vue,action:'candidat',numero:i});if(i===0)await cs[i].screenshot({path:path.join(d,`candidat-${vue}.png`)});await cli(cs[i].locator('summary'));
   }
   const ns=await p.locator('details.sans-imagerie').all();if(ns.length!==4)throw Error('Fenêtres sans mention');
   for(let i=0;i<ns.length;i++){
    await cli(ns[i].locator('summary'));if(await ns[i].getAttribute('open')===null)throw Error('Ouverture complément');
    essais.push({vue,action:'sans mention',numero:i});if(i===2)await ns[i].screenshot({path:path.join(d,`biologie-${vue}.png`)});await cli(ns[i].locator('summary'));
   }
   if(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Débordement final');await c.close();
  }
  const result={date:new Date().toISOString(),sha256_rapport:crypto.createHash('sha256').update(raw).digest('hex'),essais,captures:6,portee:'Bilan documentaire et fiches de candidats, aucun cliché clinique.'};fs.writeFileSync(path.join(d,'NAVIGATEUR.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({essais:essais.length,captures:6}));
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});

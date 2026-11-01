const fs=require('fs'),path=require('path'),crypto=require('crypto'),{chromium}=require('playwright');
(async()=>{
 const d=__dirname,raw=fs.readFileSync(path.join(d,'../../BILAN_IMAGERIE_ECG.html'));
 const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});const essais=[];
 try{
  for(const [vue,width] of [['ordinateur',1200],['mobile',390]]){
   const c=await browser.newContext({viewport:{width,height:950},hasTouch:vue==='mobile'}),p=await c.newPage();await p.setContent(raw.toString());
   const cli=async x=>vue==='mobile'?x.tap():x.click();
   if(await p.locator('details.lecon:visible').count()!==215||await p.locator('[data-triage="effectue"]').count()!==77)throw Error('Comptes');
   if(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Débordement');
   essais.push({vue,action:'comptes',mentions:215,triages:77});await p.screenshot({path:path.join(d,`accueil-${vue}.png`)});
   for(const [lot,n] of [['LOT_022',8],['LOT_023',11],['LOT_024',10]]){
    await p.fill('#recherche',lot);if(await p.locator('details.lecon:visible').count()!==n)throw Error('Recherche '+lot);essais.push({vue,action:'recherche',lot,affiches:n});
   }
   await p.fill('#recherche','LOT_023');await p.selectOption('#modalite',{label:'Vidéofluoroscopie / transit'});
   const n=await p.locator('details.lecon:visible').count();if(n!==7)throw Error('Déglutition '+n);essais.push({vue,action:'filtre transit',affiches:n});
   const first=p.locator('details.lecon:visible').first();await cli(first.locator('summary'));if(await first.getAttribute('open')===null)throw Error('Ouverture');
   await first.screenshot({path:path.join(d,`deglutition-${vue}.png`)});essais.push({vue,action:'ouvrir deglutition'});
   await p.fill('#recherche','');await p.selectOption('#modalite','');if(await p.locator('details.lecon:visible').count()!==215)throw Error('Réinitialisation');essais.push({vue,action:'reinitialiser'});
   const cs=await p.locator('details.candidat-nouveau').all();if(cs.length!==4)throw Error('Candidats');
   for(let i=0;i<cs.length;i++){
    await cli(cs[i].locator('summary'));if(await cs[i].getAttribute('open')===null)throw Error('Ouverture candidat');
    if(!(await cs[i].innerText()).includes('CC BY'))throw Error('Licence');essais.push({vue,action:'candidat',numero:i});
    if(i===3)await cs[i].screenshot({path:path.join(d,`pieges-${vue}.png`)});await cli(cs[i].locator('summary'));
   }
   if(await p.locator('details.sans-imagerie').count()!==8)throw Error('Sans mention');
   const ns=p.locator('details.sans-imagerie').filter({hasText:'Kératite'});await cli(ns.locator('summary'));if(await ns.getAttribute('open')===null)throw Error('Kératite');essais.push({vue,action:'photographie clinique sans mot-cle radiologique'});
   if(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Débordement final');await c.close();
  }
  fs.writeFileSync(path.join(d,'NAVIGATEUR.json'),JSON.stringify({date:new Date().toISOString(),sha256_rapport:crypto.createHash('sha256').update(raw).digest('hex'),essais,captures:6,portee:'Rapport documentaire uniquement ; aucun cliché clinique inspecté.'},null,2)+'\n');console.log(JSON.stringify({essais:essais.length,captures:6}));
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});

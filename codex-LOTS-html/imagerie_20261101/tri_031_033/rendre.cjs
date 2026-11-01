const fs=require('fs'),path=require('path'),crypto=require('crypto'),{chromium}=require('playwright');
(async()=>{
 const d=__dirname,raw=fs.readFileSync(path.join(d,'RAPPORT_INTERMEDIAIRE.html'));
 const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});const essais=[];
 try{
  for(const [vue,width] of [['ordinateur',1200],['mobile',390]]){
   const c=await browser.newContext({viewport:{width,height:950},hasTouch:vue==='mobile'}),p=await c.newPage();await p.setContent(raw.toString());
   const cli=async x=>vue==='mobile'?x.tap():x.click();
   if(await p.locator('details.lecon:visible').count()!==215||await p.locator('[data-triage="effectue"]').count()!==176)throw Error('Comptes');
   if(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Débordement');
   essais.push({vue,action:'comptes',mentions:215,triages:176});await p.screenshot({path:path.join(d,`accueil-${vue}.png`)});
   for(const [lot,n] of [['LOT_031',11],['LOT_032',10],['LOT_033',5]]){
    await p.fill('#recherche',lot);if(await p.locator('details.lecon:visible').count()!==n)throw Error('Recherche '+lot);essais.push({vue,action:'recherche',lot,affiches:n});
   }
   await p.fill('#recherche','');if(await p.locator('details.lecon:visible').count()!==215)throw Error('Réinitialisation');essais.push({vue,action:'reinitialiser'});
   const cs=await p.locator('details.candidat-auto[data-campagne="tri_031_033"]').all();if(cs.length!==7)throw Error('Candidats');
   for(let i=0;i<cs.length;i++){
    await cli(cs[i].locator('summary'));if(await cs[i].getAttribute('open')===null)throw Error('Ouverture candidat');
    const t=await cs[i].innerText();if(!t.includes('CC BY 4.0')||!t.includes('Original non acquis')||!t.includes('inspection visuelle : non'))throw Error('Crédits ou état');
    essais.push({vue,action:'candidat',numero:i});if(i===5){if(!t.includes('LOT_033/DX10')||!t.includes('Ne pas inventer un signe en T'))throw Error('Réserve signe en T');await cs[i].screenshot({path:path.join(d,`sclerite-${vue}.png`)});}await cli(cs[i].locator('summary'));
   }
   const ns=await p.locator('details.sans-imagerie').all();if(ns.length!==21)throw Error('Sans mention');
   const cible=p.locator('details.sans-imagerie').filter({hasText:'Spondylodiscite cervicale'});await cli(cible.locator('summary'));if(await cible.getAttribute('open')===null)throw Error('Spondylodiscite');
   essais.push({vue,action:'fiche sans mention lexicale'});await cible.screenshot({path:path.join(d,`spondylodiscite-${vue}.png`)});
   if(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Débordement final');await c.close();
  }
  fs.writeFileSync(path.join(d,'NAVIGATEUR.json'),JSON.stringify({date:new Date().toISOString(),sha256_rapport:crypto.createHash('sha256').update(raw).digest('hex'),essais,captures:6,portee:'Rapport documentaire uniquement ; pas de cliché clinique inspecté.'},null,2)+'\n');console.log(JSON.stringify({essais:essais.length,captures:6}));
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});

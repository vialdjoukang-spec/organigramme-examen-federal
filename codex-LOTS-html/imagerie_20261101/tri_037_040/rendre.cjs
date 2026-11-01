const fs=require('fs'),path=require('path'),crypto=require('crypto'),{chromium}=require('playwright');
(async()=>{
 const d=__dirname,raw=fs.readFileSync(path.join(d,'../../BILAN_IMAGERIE_ECG.html'));
 const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});const essais=[];
 try{
  for(const [vue,width] of [['ordinateur',1200],['mobile',390]]){
   const c=await browser.newContext({viewport:{width,height:950},hasTouch:vue==='mobile'}),p=await c.newPage();await p.setContent(raw.toString());
   const cli=async x=>vue==='mobile'?x.tap():x.click();
   if(await p.locator('details.lecon:visible').count()!==215||await p.locator('[data-triage="effectue"]').count()!==244||await p.locator('details.sans-imagerie').count()!==29)throw Error('Comptes');
   if(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Débordement');
   essais.push({vue,action:'comptes',mentions:215,triages:244,sans_mention:29});await p.screenshot({path:path.join(d,`accueil-${vue}.png`)});
   const inv=JSON.parse(fs.readFileSync(path.join(d,'../INVENTAIRE.json')));
   for(let lot=31;lot<=40;lot++){
    const name='LOT_'+String(lot).padStart(3,'0'),n=inv.lecons.filter(x=>x.lot===lot&&x.passages.length).length;
    await p.fill('#recherche',name);if(await p.locator('details.lecon:visible').count()!==n)throw Error('Recherche '+name);essais.push({vue,action:'recherche',lot:name,affiches:n});
   }
   await p.fill('#recherche','');if(await p.locator('details.lecon:visible').count()!==215)throw Error('Réinitialisation');essais.push({vue,action:'reinitialiser'});
   const cs=await p.locator('details.candidat-auto[data-campagne="tri_031_033"]').all();if(cs.length!==7)throw Error('Candidats');
   for(let i=0;i<cs.length;i++){
    await cli(cs[i].locator('summary'));if(await cs[i].getAttribute('open')===null)throw Error('Ouverture candidat');const t=await cs[i].innerText();
    if(!t.includes('CC BY 4.0')||!t.includes('Original non acquis')||!t.includes('inspection visuelle : non'))throw Error('Crédits ou état');
    essais.push({vue,action:'candidat',numero:i});if(i===5){if(!t.includes('Ne pas inventer un signe en T'))throw Error('Réserve');await cs[i].screenshot({path:path.join(d,`sclerite-${vue}.png`)});}await cli(cs[i].locator('summary'));
   }
   const cible=p.locator('details.lecon').filter({hasText:'LOT_040 — Apnée, apnée avec éveil'});await cli(cible.locator('summary'));if(await cible.getAttribute('open')===null)throw Error('PhaseA040');
   if(!(await cible.innerText()).includes('Apnées : signaux respiratoires'))throw Error('Tri absent');essais.push({vue,action:'derniere phase A triee'});await cible.screenshot({path:path.join(d,`apnee-${vue}.png`)});
   if(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Débordement final');await c.close();
  }
  fs.writeFileSync(path.join(d,'NAVIGATEUR.json'),JSON.stringify({date:new Date().toISOString(),sha256_rapport:crypto.createHash('sha256').update(raw).digest('hex'),essais,captures:6,portee:'Rapport documentaire final ; pas de cliché clinique inspecté, pas de test des fenêtres médicales.'},null,2)+'\n');console.log(JSON.stringify({essais:essais.length,captures:6}));
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});

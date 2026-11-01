const fs=require('fs'),path=require('path'),crypto=require('crypto');
const {chromium}=require('playwright');
(async()=>{
 const d=__dirname,raw=fs.readFileSync(path.join(d,'../BILAN_IMAGERIE_ECG.html'));
 const data=JSON.parse(fs.readFileSync(path.join(d,'INVENTAIRE.json')));
 const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
 const essais=[];
 try{
  for(const [nom,width] of [['ordinateur',1200],['mobile',390]]){
   const c=await browser.newContext({viewport:{width,height:900},hasTouch:nom==='mobile'}),p=await c.newPage();
   await p.setContent(raw.toString());
   if(await p.locator('details.lecon:visible').count()!==212)throw Error('Compte initial');
   if(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Débordement');
   await p.screenshot({path:path.join(d,`accueil-${nom}.png`)});
   const options=await p.locator('#modalite option').allTextContents();
   for(const option of options.slice(1)){
    await p.selectOption('#modalite',{label:option});
    const expected=data.lecons.filter(x=>x.categories.includes(option)).length;
    const count=await p.locator('details.lecon:visible').count();
    if(count!==expected)throw Error('Filtre '+option);
    essais.push({vue:nom,filtre:option,affiches:count});
   }
   await p.selectOption('#modalite','');await p.fill('#recherche','LOT_019');
   if(await p.locator('details.lecon:visible').count()!==11)throw Error('Recherche LOT019');
   essais.push({vue:nom,recherche:'LOT_019',affiches:11});
   await p.fill('#recherche','zzzz-sans-resultat');
   if(await p.locator('details.lecon:visible').count()!==0)throw Error('Recherche vide');
   essais.push({vue:nom,recherche:'zzzz-sans-resultat',affiches:0});
   await p.fill('#recherche','');await p.selectOption('#modalite','ECG');
   const row=p.locator('details.lecon:visible').first();
   if(nom==='mobile')await row.locator('summary').tap();else await row.locator('summary').click();
   if(await row.getAttribute('open')===null)throw Error('Ouverture');
   await row.screenshot({path:path.join(d,`extraits-${nom}.png`)});
   essais.push({vue:nom,ouverture:true,filtre:'ECG'});
   await c.close();
  }
  const result={date:new Date().toISOString(),rapport_sha256:crypto.createHash('sha256').update(raw).digest('hex'),essais,portee:'Rapport seulement, ordinateur et tactile émulé ; aucune image clinique rendue.',captures:4};
  fs.writeFileSync(path.join(d,'NAVIGATEUR.json'),JSON.stringify(result,null,2)+'\n');
  console.log(JSON.stringify({essais:essais.length,captures:4}));
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});

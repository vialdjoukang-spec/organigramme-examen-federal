const { chromium }=require('playwright');
const fs=require('fs'),path=require('path'),assert=require('assert');
(async()=>{
 const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
 const tests=[];
 for(const mobile of [false,true]){
  const page=await browser.newPage({viewport:{width:mobile?390:1200,height:mobile?844:1000},hasTouch:mobile,isMobile:mobile});
  for(const [label,file,target] of [
   ['PhaseA','LOT_018_Phase_A_V0.html','a-explorations'],
   ['DX8','LOT_018_Phase_B_V0_DX.8.html','dx8-detail9']]){
   await page.setContent(fs.readFileSync(path.join(__dirname,'../..',file),'utf8'));
   await page.locator(`button[popovertarget="${target}"]`).first().click();
   assert(await page.locator('#'+target).evaluate(e=>e.matches(':popover-open')));
   await page.locator(`#${target} .illustration details`).evaluateAll(es=>es.forEach(e=>e.open=true));
   for(const b of await page.locator(`#${target} .repere`).all()){
    if(mobile)await b.tap();else {await b.hover();assert(await b.locator('.nom').isVisible());await b.click();}
    assert(await b.locator('.nom').isVisible());
    const id=await b.getAttribute('popovertarget');assert(await page.locator('#'+id).evaluate(e=>e.matches(':popover-open')));
    await page.locator('#'+id+' button').click();
    tests.push({lecon:label,mobile,repere:id,nom_visible:true,definition_ouverte_et_fermee:true});
   }
   const figure=page.locator('figure[data-illustration="i018-niveaux-visuels"]');
   let index=0;
   for(const scene of await figure.locator('.scene').all()){
    await scene.scrollIntoViewIfNeeded();
    await scene.screenshot({path:path.join(__dirname,`${label}-${mobile?'mobile':'desktop'}-niveau${++index}.png`)});
    const box=await scene.boundingBox();assert(box.width<=(mobile?390:1200));
   }
   assert(index===3);
   tests.push({lecon:label,mobile,trois_niveaux:true,fenetre_examen_ouverte:true});
  }
  await page.close();
 }
 await browser.close();
 fs.writeFileSync(path.join(__dirname,'TEST_INTEGRATION.json'),JSON.stringify({date:new Date().toISOString(),moteur:'Chromium /usr/bin/chromium ; souris et émulation tactile, pas téléphone physique',portee:'PhaseA et DX8 ; tous leurs repères illustrés, pas seulement le nouveau composant',tests},null,2)+'\n');
 console.log(tests.length+' contrôles d’intégration réussis.');
})().catch(e=>{console.error(e);process.exit(1)});

const {chromium}=require('playwright');
const fs=require('fs');
const path=require('path');
const assert=require('assert');
(async()=>{
 const dir=__dirname, root=path.dirname(dir), results=[];
 const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/chromium',args:['--no-sandbox']});
 for(const mobile of [false,true]){
  const context=await browser.newContext({viewport:mobile?{width:390,height:844}:{width:1365,height:1000},isMobile:mobile,hasTouch:mobile});
  const page=await context.newPage();
  for(const lot of [34,40]){
   const erreurs=[]; page.on('pageerror',e=>erreurs.push(e.message));
   await page.setContent(fs.readFileSync(path.join(root,`LOT_0${lot}/LOT_0${lot}_Phase_B_V0_DX.1.html`),'utf8'));
   await page.locator('#dx1-p9').scrollIntoViewIfNeeded();
   await page.locator('[popovertarget="dx1-detail9"]').first().click();
   await page.locator('[popovertarget="sommeil-signaux-fenetre"]').first().click();
   assert(await page.locator('#sommeil-signaux-fenetre').evaluate(e=>e.matches(':popover-open')));
   const figure=page.locator('[data-illustration="sommeil-signaux"]');
   const vues=figure.locator(':scope > details');
   assert.equal(await vues.count(),3);
   for(let k=0;k<3;k++){
    for(let j=0;j<3;j++) await vues.nth(j).evaluate((e,open)=>e.open=open,j===k);
    const vue=vues.nth(k);await vue.scrollIntoViewIfNeeded();
    const reperes=vue.locator('.repere');
    for(let j=0;j<await reperes.count();j++){
     const rep=reperes.nth(j);await rep.click();
     const target=await rep.getAttribute('popovertarget');
     assert(await page.locator('#'+target).evaluate(e=>e.matches(':popover-open')));
     const box=await page.locator('#'+target).boundingBox(); assert(box.x>=0 && box.x+box.width<=(mobile?391:1366));
     await page.locator('#'+target+' button').click();
    }
    await vue.locator('.scene').scrollIntoViewIfNeeded();
    const file=`lot${lot}-${mobile?'mobile':'bureau'}-vue${k}.png`;
    await page.screenshot({path:path.join(dir,file)});
    const over=await page.locator('#sommeil-signaux-fenetre').evaluate(e=>e.scrollWidth>e.clientWidth+1);assert(!over);
    results.push({lot,mobile,vue:k,repères:await reperes.count(),capture:file,debordement:false});
   }
   await page.locator('#sommeil-signaux-fenetre > .barre button').click();
   assert(!(await page.locator('#sommeil-signaux-fenetre').evaluate(e=>e.matches(':popover-open'))));
   assert.equal(erreurs.length,0);
  }
  await context.close();
 }
 await browser.close();
 fs.writeFileSync(path.join(dir,'NAVIGATEUR.json'),JSON.stringify({date:new Date().toISOString(),moteur:'Chromium via Playwright',vues:results,limite:'Contrôles fonctionnels ; revue des captures consignée séparément.'},null,2)+'\n');
 console.log('12 vues testées ; 32 ouvertures et fermetures de définitions vérifiées.');
})().catch(e=>{console.error(e);process.exit(1)});

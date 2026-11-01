const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const assert = require('assert');
(async () => {
  const browser = await chromium.launch({executablePath:'/usr/bin/chromium', headless:true, args:['--no-sandbox']});
  const checks = [];
  for (const mobile of [false, true]) {
    const page = await browser.newPage({viewport:{width:mobile?390:1040,height:900},hasTouch:mobile,isMobile:mobile});
    await page.setContent('<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{font:17px/1.5 system-ui;margin:16px}</style>' + fs.readFileSync(path.join(__dirname,'coupes.html'),'utf8'));
    await page.locator('details').evaluateAll(es => es.forEach(e => e.open = true));
    await page.screenshot({path:path.join(__dirname,mobile?'coupes-mobile.png':'coupes-desktop.png'),fullPage:true});
    for (const scene of await page.locator('.scene').all()) {
      const buttons = await scene.locator('.repere').all();
      for (let i=0;i<buttons.length;i++) for (let j=i+1;j<buttons.length;j++) {
        const a = await buttons[i].boundingBox(), b = await buttons[j].boundingBox();
        assert(a.x+a.width<=b.x || b.x+b.width<=a.x || a.y+a.height<=b.y || b.y+b.height<=a.y, 'Repères superposés');
      }
    }
    for (const b of await page.locator('.repere').all()) {
      if(mobile) await b.tap(); else {await b.hover(); assert(await b.locator('.nom').isVisible()); await b.click();}
      assert(await b.locator('.nom').isVisible());
      const id=await b.getAttribute('popovertarget');
      assert(await page.locator('#'+id).evaluate(e=>e.matches(':popover-open')));
      await page.locator('#'+id+' button').click();
      checks.push({mobile,repere:id,nom_visible:true,definition_ouverte_et_fermee:true});
    }
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    await page.close();
  }
  await browser.close();
  fs.writeFileSync(path.join(__dirname,'TEST_COMPOSANT.json'),JSON.stringify({date:new Date().toISOString(),moteur:'Chromium ; émulation tactile, pas appareil physique',checks},null,2)+'\n');
  console.log(checks.length+' interactions ; aucune superposition des repères ni débordement horizontal.');
})().catch(e=>{console.error(e);process.exit(1)});

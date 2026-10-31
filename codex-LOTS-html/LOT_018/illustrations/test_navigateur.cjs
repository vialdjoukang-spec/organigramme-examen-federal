const {chromium}=require('playwright');const fs=require('fs');const path=require('path');const assert=require('assert');
(async()=>{const b=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});const cases=[['Phase_A','LOT_018_Phase_A_V0.html','a-explorations'],['DX7','LOT_018_Phase_B_V0_DX.7.html','dx7-detail9'],['DX8','LOT_018_Phase_B_V0_DX.8.html','dx8-detail9']];let tests=[];
for(const mobile of [false,true]){const context=await b.newContext({viewport:{width:mobile?390:1200,height:mobile?844:1000},isMobile:mobile,hasTouch:mobile});const p=await context.newPage();
for(const [name,file,target] of cases){await p.setContent(fs.readFileSync(path.join(__dirname,'..',file),'utf8'));await p.evaluate(()=>document.fonts.ready);await p.locator(`button[popovertarget="${target}"]`).first().click();assert(await p.locator('#'+target).evaluate(e=>e.matches(':popover-open')));
await p.locator(`#${target} .illustration details`).evaluateAll(es=>es.forEach(e=>e.open=true));
for(const button of await p.locator(`#${target} .repere`).all()){
 if(mobile)await button.tap();else{await button.hover();assert(await button.locator('.nom').isVisible());await button.click();}
 const id=await button.getAttribute('popovertarget');assert(await p.locator('#'+id).evaluate(e=>e.matches(':popover-open')));assert(await p.locator('#'+id).innerText());
 await p.locator(`#${id} button`).click();tests.push({lecon:name,mobile,repere:id,ouverture_et_fermeture:true});
}
const figs=await p.locator(`#${target} .illustration`).all();for(let i=0;i<figs.length;i++){await figs[i].scrollIntoViewIfNeeded();await figs[i].screenshot({path:path.join(__dirname,`${name}-${mobile?'mobile':'desktop'}-${i}.png`)});const box=await figs[i].boundingBox();assert(box.width<=(mobile?390:1200));}
 tests.push({lecon:name,mobile,fenetre_examen:true,illustrations:figs.length});
}
await context.close();}
await b.close();fs.writeFileSync(path.join(__dirname,'TEST_NAVIGATEUR.json'),JSON.stringify({date:new Date().toISOString(),moteur:'Chromium /usr/bin/chromium',mode:'HTML local chargé par setContent ; émulation tactile, pas appareil physique',tests},null,2));console.log(tests.length+' contrôles navigateur réussis');})().catch(e=>{console.error(e);process.exit(1)});

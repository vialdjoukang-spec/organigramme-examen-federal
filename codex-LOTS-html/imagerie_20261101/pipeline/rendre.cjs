const fs=require('fs'),path=require('path'),crypto=require('crypto'),{chromium}=require('playwright');
(async()=>{
 const d=__dirname,raw=fs.readFileSync(path.join(d,'DEMONSTRATION.html'));
 const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
 const essais=[];
 try{
  for(const [vue,width] of [['ordinateur',1200],['mobile',390]]){
   const context=await browser.newContext({viewport:{width,height:1000},hasTouch:vue==='mobile'}),page=await context.newPage();
   await page.setContent(raw.toString());
   const click=async el=>{if(vue==='mobile')await el.tap();else await el.click()};
   const window=page.locator('#image-i018-optique');
   if(await window.isVisible())throw Error('Fenêtre visible avant clic');
   await click(page.locator('#examens button'));
   if(!await window.isVisible())throw Error('Fenêtre absente');
   essais.push({vue,action:'clic du terme ouvre directement les deux vues'});
   const left=window.locator('.paire img'),right=window.locator('.paire svg');
   if(await left.getAttribute('src')!==await right.locator('image').getAttribute('href'))throw Error('Clichés différents');
   const a=await left.boundingBox(),b=await right.boundingBox();
   if(vue==='ordinateur'&&b.x<=a.x+a.width-1)throw Error('Non juxtaposés');
   if(vue==='mobile'&&b.y<=a.y+a.height-1)throw Error('Non empilés');
   if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Débordement page');
   if(await window.evaluate(el=>el.scrollWidth>el.clientWidth))throw Error('Débordement fenêtre');
   await window.screenshot({path:path.join(d,`paire-${vue}.png`)});
   for(let i=1;i<=2;i++){
    const button=window.locator(`.repere[popovertarget="i018-optique-def${i}"]`);
    await click(button);
    const def=window.locator(`#i018-optique-def${i}`);
    if(!await def.isVisible())throw Error('Définition invisible');
    essais.push({vue,action:'définition visible',numero:i});
    await click(def.locator('button'));
    if(await def.isVisible())throw Error('Définition non fermée');
    essais.push({vue,action:'fermeture définition',numero:i});
   }
   await window.locator('figcaption').scrollIntoViewIfNeeded();
   await page.screenshot({path:path.join(d,`legende-${vue}.png`)});
   await click(window.locator('.barre button'));
   if(await window.isVisible())throw Error('Fenêtre non fermée');
   essais.push({vue,action:'fermeture fenêtre'});
   await context.close();
  }
  fs.writeFileSync(path.join(d,'NAVIGATEUR.json'),JSON.stringify({date:new Date().toISOString(),sha256_demo:crypto.createHash('sha256').update(raw).digest('hex'),essais,captures:4,portee:'Démonstration technique avec anatomie normale, pas un nouveau cliché clinique.'},null,2)+'\n');
  console.log(JSON.stringify({essais:essais.length,captures:4}));
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});

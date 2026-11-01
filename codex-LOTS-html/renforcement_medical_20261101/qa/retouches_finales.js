const {chromium}=require('playwright');
const fs=require('fs'),path=require('path'),crypto=require('crypto'),assert=require('assert');
const BASE=path.resolve(__dirname,'../..'),D=path.join(__dirname,'retouches_finales');fs.mkdirSync(D,{recursive:true});
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const report={date:new Date().toISOString(),portee:'Contrôle ciblé des retouches CSS, de la question6 et du bilan. Pas de validation médicale.',rendus:[]};
(async()=>{const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/chromium',args:['--no-sandbox']});try{
for(const f of ['LOT_018/LOT_018_Phase_A_V0.html','LOT_018/LOT_018_Phase_B_V0_DX.1.html','LOT_029/LOT_029_Phase_A_V0.html'])for(const mobile of [false,true]){
const raw=fs.readFileSync(path.join(BASE,f)),lot=f.slice(4,7),dx=f.includes('DX.1');
const p=await browser.newPage({viewport:mobile?{width:390,height:844}:{width:1365,height:1000},isMobile:mobile,hasTouch:mobile,colorScheme:'dark'});await p.setContent(raw.toString());
await p.locator('h2[id$="-p9"]').locator('..').locator('button[popovertarget]').first().click();
if(!dx)await p.locator(`[popovertarget="image-reelle-${lot}"]:not([popovertargetaction="hide"])`).click();
const figure=dx?p.locator('.fenetre:popover-open .illustration').first():p.locator(`#image-reelle-${lot} .illustration`);
await figure.locator('figcaption').scrollIntoViewIfNeeded();
const colors=await figure.locator('h3,h4,figcaption,a').evaluateAll(es=>es.map(e=>({text:e.textContent.slice(0,100),color:getComputedStyle(e).color})));
assert(colors.every(x=>x.color!=='rgb(158, 184, 203)'));assert(colors.every(x=>Math.max(...x.color.match(/\d+/g).slice(0,3).map(Number))<190));
const capture=path.basename(f)+'.'+(mobile?'mobile':'bureau')+'.png';await p.screenshot({path:path.join(D,capture)});
report.rendus.push({fichier:f,sha256:sha(raw),sha_stable:sha(fs.readFileSync(path.join(BASE,f)))===sha(raw),mobile,sombre:true,capture,colors});await p.close();}
for(const mobile of [false,true]){
const f='LOT_029/LOT_029_Phase_B_V0_DX.1.html',raw=fs.readFileSync(path.join(BASE,f));const p=await browser.newPage({viewport:mobile?{width:390,height:844}:{width:1365,height:1000},isMobile:mobile,hasTouch:mobile});await p.setContent(raw.toString());await p.locator('h2[id$="-p14"]').locator('..').locator('button[popovertarget]').first().click();const q=p.locator('details.quiz').nth(5);await q.locator('summary').click();assert(await q.evaluate(e=>e.open));await q.scrollIntoViewIfNeeded();const capture='029-dx1-question6-'+(mobile?'mobile':'bureau')+'.png';await p.screenshot({path:path.join(D,capture)});report.rendus.push({fichier:f,sha256:sha(raw),sha_stable:sha(fs.readFileSync(path.join(BASE,f)))===sha(raw),mobile,question:6,texte:await q.innerText(),capture});await p.close();}
for(const mobile of [false,true]){
const f='BILAN_RENFORCEMENT_MEDICAL.html',raw=fs.readFileSync(path.join(BASE,f));const p=await browser.newPage({viewport:mobile?{width:390,height:844}:{width:1365,height:1000},isMobile:mobile,hasTouch:mobile});await p.setContent(raw.toString());assert.equal(await p.locator('tbody tr').count(),6);const links=await p.locator('a[href]').evaluateAll(es=>es.map(e=>e.getAttribute('href')));for(const link of links)assert(fs.existsSync(path.resolve(BASE,link)));const overflow=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1);assert(!overflow);const table=await p.locator('.table').evaluate(e=>({scrollWidth:e.scrollWidth,clientWidth:e.clientWidth}));const capture='bilan-'+(mobile?'mobile':'bureau')+'.png';await p.screenshot({path:path.join(D,capture),fullPage:true});report.rendus.push({fichier:f,sha256:sha(raw),sha_stable:sha(fs.readFileSync(path.join(BASE,f)))===sha(raw),mobile,lignes:6,liens:links,debordement_page:overflow,table,capture});await p.close();}
}finally{await browser.close();fs.writeFileSync(path.join(D,'RETOUCHES.json'),JSON.stringify(report,null,2)+'\n')}console.log(JSON.stringify({rendus:report.rendus.length}));})().catch(e=>{console.error(e);process.exit(1)});

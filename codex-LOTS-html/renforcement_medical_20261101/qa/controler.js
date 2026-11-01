/* Contrôles de présentation réels ; aucune conclusion médicale. */
const {chromium}=require('playwright');
const fs=require('fs'),path=require('path'),crypto=require('crypto'),cp=require('child_process');
const ROOT=path.resolve(__dirname,'../../..');
const BASE=path.join(ROOT,'codex-LOTS-html');
const FINAL=process.argv.includes('--final');
const MODE=FINAL?'final':'historique';
const out=process.argv.find(a=>a.startsWith('--out='))?.slice(6)||MODE;
if(!/^[a-z0-9_-]+$/.test(out))throw Error('Nom de sortie invalide');
const DIR=path.join(__dirname,out);
const checkpoint=JSON.parse(fs.readFileSync(path.join(__dirname,'../BASELINE.json'),'utf8')).commit;
fs.mkdirSync(DIR,{recursive:true});
const sha=s=>crypto.createHash('sha256').update(s).digest('hex');
const files=process.argv.find(a=>a.startsWith('--files='))?.slice(8).split(',')||[18,29].flatMap(n=>['Phase_A_V0','Phase_B_V0_DX.1'].map(s=>`LOT_${String(n).padStart(3,'0')}/LOT_${String(n).padStart(3,'0')}_${s}.html`));
if(files.some(f=>!/^LOT_(018|029)\/LOT_(018|029)_(Phase_A_V0|Phase_B_V0_DX\.[12])\.html$/.test(f)))throw Error('Fichier hors périmètre QA');
const report={date:new Date().toISOString(),mode:MODE,commit_historique:FINAL?null:checkpoint,limite:'Contrôles du rendu et des interactions, pas une validation du contenu médical.',fichiers:[],erreurs:[]};
async function main(){
 const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/chromium',args:['--no-sandbox']});
 try{
  for(const file of files){
   const raw=FINAL?fs.readFileSync(path.join(BASE,file)):cp.execFileSync('git',['show',checkpoint+':codex-LOTS-html/'+file],{cwd:ROOT});
   const info={fichier:file,sha256:sha(raw),rendus:[]};
   for(const mobile of [false,true]){
    const ctx=await browser.newContext({viewport:mobile?{width:390,height:844}:{width:1365,height:1000},isMobile:mobile,hasTouch:mobile});
    const page=await ctx.newPage();page.setDefaultTimeout(6000);
    const errors=[];page.on('pageerror',e=>errors.push(e.message));
    await page.setContent(raw.toString('utf8'));await page.evaluate(()=>document.fonts.ready);
    const result={mobile,parties:[],popovers_secondaires:[],captures:[],erreurs_javascript:errors};
    const sections=await page.locator('section').evaluateAll(es=>es.filter(e=>e.querySelector(':scope > h2[id*="-p"]')).map(e=>({id:e.querySelector(':scope > h2').id,targets:[...e.querySelectorAll('button[popovertarget]:not([popovertargetaction="hide"])')].map(b=>b.getAttribute('popovertarget'))})));
    if(sections.length!==14)throw Error('Nombre de parties : '+sections.length);
    result.questions=await page.locator('details.quiz').count();
    if(result.questions!==14)throw Error('Nombre de questions : '+result.questions);
    const direct=new Set(sections.flatMap(s=>s.targets));
    for(const [idx,section] of sections.entries()){
     const part={partie:idx+1,cibles:section.targets,resultats:[]};
     if(FINAL && !section.targets.length)report.erreurs.push({file,mobile,partie:idx+1,erreur:'Aucune fenêtre directe'});
     for(const target of section.targets){
      await page.evaluate(()=>document.querySelectorAll('[popover]:popover-open').forEach(e=>e.hidePopover()));
      const button=page.locator(`section:has(> #${section.id}) button[popovertarget="${target}"]`).first();
      await button.scrollIntoViewIfNeeded();
      if(idx===0&&!mobile){await button.focus();await page.keyboard.press('Enter')}else if(mobile)await button.tap();else await button.click();
      const window=page.locator(`[id="${target}"]`);
      const metric=await window.evaluate(e=>({ouvert:e.matches(':popover-open'),largeur:e.getBoundingClientRect().width,haut:e.getBoundingClientRect().top,gauche:e.getBoundingClientRect().left,debordement:e.scrollWidth>e.clientWidth+1,defilable:e.scrollHeight>e.clientHeight,titres:e.querySelectorAll('h3,h4').length,gras:e.querySelectorAll('strong,b').length,italique:e.querySelectorAll('em,i').length}));
      if(!metric.ouvert||metric.gauche<0||metric.largeur>(mobile?391:1366)||metric.debordement)report.erreurs.push({file,mobile,target,metric});
      part.resultats.push({target,...metric});
      if((!mobile&&[3,9,13,14].includes(idx+1))||(mobile&&[11,13,14].includes(idx+1))){
       const name=path.basename(file,'.html')+'-'+(mobile?'mobile':'bureau')+'-p'+(idx+1)+(section.targets.length>1?'-'+target:'')+'.png';
       await page.evaluate(()=>getSelection()?.removeAllRanges());
       await page.screenshot({path:path.join(DIR,name)});result.captures.push(name);
      }
      const close=window.locator(`button[popovertarget="${target}"][popovertargetaction="hide"]`).first();
      await close.click();
      if(await window.evaluate(e=>e.matches(':popover-open')))report.erreurs.push({file,mobile,target,erreur:'Fermeture échouée'});
     }
     result.parties.push(part);
    }
    // Ouvrir les fenêtres imbriquées par les vrais boutons de leur chemin.
    const graph=await page.locator('button[popovertarget]:not([popovertargetaction="hide"])').evaluateAll(bs=>bs.map((b,i)=>({target:b.getAttribute('popovertarget'),parent:b.closest('[popover]')?.id||null,index:i})));
    const opened=new Set();
    async function ouvrir(target,trail=[]){
     if(trail.includes(target))throw Error('Cycle de fenêtres '+trail.join('>'));
     if(await page.locator(`[id="${target}"]`).evaluate(e=>e.matches(':popover-open')))return;
     const edge=graph.find(x=>x.target===target&&!x.parent)||graph.find(x=>x.target===target);
     if(!edge)throw Error('Fenêtre sans déclencheur '+target);
     if(edge.parent)await ouvrir(edge.parent,[...trail,target]);
     const button=page.locator('button[popovertarget]:not([popovertargetaction="hide"])').nth(edge.index);
     for(const detail of await button.locator('xpath=ancestor::details').all()){
      if(!(await detail.evaluate(e=>e.open)))await detail.locator(':scope > summary').click();
     }
     await button.scrollIntoViewIfNeeded();if(mobile)await button.tap();else await button.click();opened.add(target);
    }
    const ids=await page.locator('[popover]').evaluateAll(es=>es.map(e=>e.id));
    for(const target of ids.filter(id=>!direct.has(id))){
     await page.evaluate(()=>document.querySelectorAll('[popover]:popover-open').forEach(e=>e.hidePopover()));
     try{
      await ouvrir(target);
      const win=page.locator(`[id="${target}"]`);const metric=await win.evaluate(e=>({ouvert:e.matches(':popover-open'),debordement:e.scrollWidth>e.clientWidth+1}));
      result.popovers_secondaires.push({id:target,...metric});
      if(!metric.ouvert||metric.debordement)report.erreurs.push({file,mobile,target,...metric});
      await win.locator(`button[popovertarget="${target}"][popovertargetaction="hide"]`).first().click();
     }catch(e){report.erreurs.push({file,mobile,target,erreur:e.message})}
    }
    result.debordement_page=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1);
    info.rendus.push(result);await ctx.close();
   }
   if(FINAL&&sha(fs.readFileSync(path.join(BASE,file)))!==info.sha256)report.erreurs.push({file,erreur:'Fichier modifié pendant la passe : recommencer après gel'});
   report.fichiers.push(info);
  }
 }finally{
  await browser.close();report.fin=new Date().toISOString();fs.writeFileSync(path.join(DIR,'NAVIGATEUR.json'),JSON.stringify(report,null,2)+'\n');
 }
 console.log(JSON.stringify({mode:MODE,fichiers:report.fichiers.length,rendus:report.fichiers.reduce((n,f)=>n+f.rendus.length,0),erreurs:report.erreurs.length}));
 process.exitCode=report.erreurs.length?1:0;
}
main().catch(e=>{report.erreurs.push({erreur:e.stack});fs.writeFileSync(path.join(DIR,'NAVIGATEUR.json'),JSON.stringify(report,null,2)+'\n');console.error(e);process.exit(1)});

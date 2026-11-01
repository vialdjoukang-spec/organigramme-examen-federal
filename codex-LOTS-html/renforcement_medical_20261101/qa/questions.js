const {chromium}=require('playwright');
const fs=require('fs'),path=require('path'),crypto=require('crypto'),assert=require('assert');
const BASE=path.resolve(__dirname,'../..');
const out=process.argv.find(a=>a.startsWith('--out='))?.slice(6)||'questions';
if(!/^[a-z0-9_-]+$/.test(out))throw Error('Sortie invalide');
const DIR=path.join(__dirname,out);fs.mkdirSync(DIR,{recursive:true});
const files=process.argv.find(a=>a.startsWith('--files='))?.slice(8).split(',')||[18,29].flatMap(n=>['Phase_A_V0','Phase_B_V0_DX.1'].map(s=>`LOT_${String(n).padStart(3,'0')}/LOT_${String(n).padStart(3,'0')}_${s}.html`));
const sha=s=>crypto.createHash('sha256').update(s).digest('hex');
const result={date:new Date().toISOString(),portee:'Ouverture des14questions et affichage de leurs réponses, sans audit médical.',fichiers:[]};
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'/usr/bin/chromium',args:['--no-sandbox']});
 try{
  for(const f of files){
   const raw=fs.readFileSync(path.join(BASE,f));const row={fichier:f,sha256:sha(raw),rendus:[]};
   for(const mobile of [false,true]){
    const page=await browser.newPage({viewport:mobile?{width:390,height:844}:{width:1365,height:1000},isMobile:mobile,hasTouch:mobile});await page.setContent(raw.toString('utf8'));
    const h=page.locator('h2[id$="-p14"]');await h.scrollIntoViewIfNeeded();await h.locator('..').locator('button[popovertarget]').first().click();
    const quiz=page.locator('details.quiz');assert.equal(await quiz.count(),14);const infos=[];
    for(let i=0;i<14;i++){
     const q=quiz.nth(i),s=q.locator(':scope > summary');await s.scrollIntoViewIfNeeded();
     if(i===0&&!mobile){await s.focus();await page.keyboard.press('Enter')}else if(mobile)await s.tap();else await s.click();
     assert(await q.evaluate(e=>e.open));
     const info=await q.evaluate(e=>({numero:[...document.querySelectorAll('details.quiz')].indexOf(e)+1,reponse:[...e.children].filter(x=>x.tagName!=='SUMMARY').map(x=>x.textContent).join(' ').trim(),largeur:e.getBoundingClientRect().width}));assert(info.reponse.length>0);infos.push(info);
     if((!mobile&&i===0)||(mobile&&i===13)){
      await q.scrollIntoViewIfNeeded();await page.evaluate(()=>getSelection()?.removeAllRanges());
      const capture=path.basename(f,'.html')+'-'+(mobile?'mobile':'bureau')+'-question'+(i+1)+'.png';await page.screenshot({path:path.join(DIR,capture)});
     }
     await s.click();assert(!(await q.evaluate(e=>e.open)));
    }
    row.rendus.push({mobile,reponses_ouvertes:infos.length,questions:infos});await page.close();
   }
   row.sha_stable=sha(fs.readFileSync(path.join(BASE,f)))===row.sha256;result.fichiers.push(row);
  }
 }finally{await browser.close();fs.writeFileSync(path.join(DIR,'QUESTIONS.json'),JSON.stringify(result,null,2)+'\n')}
 console.log(JSON.stringify({fichiers:result.fichiers.length,reponses_ouvertes:result.fichiers.reduce((n,f)=>n+f.rendus.reduce((n,r)=>n+r.reponses_ouvertes,0),0)}));
})().catch(e=>{console.error(e);process.exit(1)});

const {chromium}=require('playwright');
const fs=require('fs'); const path=require('path');
(async()=>{const b=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});const p=await b.newPage({viewport:{width:1050,height:1050}});const dir=__dirname;
for(const name of ['optique','retine']){
 await p.setContent(fs.readFileSync(path.join(dir,name+'.html'),'utf8'));await p.addStyleTag({content:'body{font:17px system-ui;max-width:900px;margin:auto;padding:20px}'});
 if(name==='retine')await p.locator('details').nth(1).evaluate(e=>e.open=true);
 await p.screenshot({path:path.join(dir,name+'-rendu.png'),fullPage:true});
}
await b.close();})();

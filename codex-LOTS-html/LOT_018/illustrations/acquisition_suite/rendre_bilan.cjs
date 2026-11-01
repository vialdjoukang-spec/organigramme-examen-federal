const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const crypto = require('crypto');
const d = __dirname;
const base = path.resolve(d, '../../..');
const fichier = path.join(base, 'BILAN_CLICHES_LOT_018.html');

(async () => {
  const raw = fs.readFileSync(fichier);
  const navigateur = await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
  const essais = [];
  try {
    for (const [nom, viewport] of [['ordinateur',{width:1200,height:1000}],['mobile',{width:390,height:844}]]) {
      const context = await navigateur.newContext({viewport,hasTouch:nom==='mobile'});
      const page = await context.newPage();
      await page.setContent(raw.toString('utf8'));
      if (await page.locator('tbody tr').count() !== 11) throw new Error('Onze leçons attendues');
      const largeur = await page.evaluate(() => ({body:document.documentElement.scrollWidth,viewport:innerWidth}));
      if (largeur.body > largeur.viewport) throw new Error('Débordement horizontal du document');
      for (const el of await page.locator('details').all()) {
        const summary = el.locator('summary');
        if(nom==='mobile') await summary.tap(); else await summary.click();
        if (!(await el.getAttribute('open') !== null)) throw new Error('Détail non ouvert');
        essais.push({vue:nom,id:await el.getAttribute('id'),ouverture:true});
        if(nom==='mobile') await summary.tap(); else await summary.click();
      }
      await page.evaluate(() => scrollTo(0,0));
      await page.screenshot({path:path.join(d,`bilan-${nom}.png`),fullPage:nom==='ordinateur'});
      const suspendu = page.locator('#rd-fond-oeil');
      if(nom==='mobile') await suspendu.locator('summary').tap(); else await suspendu.locator('summary').click();
      if(await suspendu.getAttribute('open') === null || !(await suspendu.innerText()).includes('Import suspendu')) throw new Error('Alerte de provenance absente');
      essais.push({vue:nom,id:'rd-fond-oeil',ouverture:true,alerte_provenance:true});
      await suspendu.screenshot({path:path.join(d,`provenance-${nom}.png`)});
      await context.close();
    }
    fs.writeFileSync(path.join(d,'TEST_RAPPORT_NAVIGATEUR.json'),JSON.stringify({date:new Date().toISOString(),fichier:'BILAN_CLICHES_LOT_018.html',sha256:crypto.createHash('sha256').update(raw).digest('hex'),portee:'Rapport seulement ; aucun cliché clinique ni HTML de leçon rendu dans cette campagne.',essais,appareil_physique:false},null,2)+'\n');
    console.log(JSON.stringify({interactions:essais.length,captures:4}));
  } finally { await navigateur.close(); }
})().catch(e=>{console.error(e);process.exit(1)});

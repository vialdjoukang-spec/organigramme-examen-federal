#!/usr/bin/env node
// Captures d'écran : 2 par LOT, fichier et chapitre (h2) tirés au hasard.
// Usage : node captures.js [--lots 001 002] [--sortie DOSSIER] [--source DOSSIER_LOT_Claude_Finaux] [--graine N]
// Source par défaut : origin/main (git archive).
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path'), os = require('os'), cp = require('child_process');
const arg = (k, d) => { const i = process.argv.indexOf('--' + k); return i < 0 ? d : process.argv[i + 1]; };
const list = (k) => { const i = process.argv.indexOf('--' + k); if (i < 0) return null; const o = []; for (let j = i + 1; j < process.argv.length && !process.argv[j].startsWith('--'); j++) o.push(process.argv[j]); return o; };
let s = parseInt(arg('graine', Date.now() % 2147483647)) || 1;
const rnd = () => (s = (s * 48271) % 2147483647) / 2147483647;
const pick = (a) => a[Math.floor(rnd() * a.length)];
const sortie = arg('sortie', 'harnais/bilan/sortie/captures'); fs.mkdirSync(sortie, { recursive: true });
let src = arg('source');
if (!src) { const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'lotsrc_')); cp.execSync(`git fetch -q origin main && git archive origin/main LOT_Claude_Finaux | tar -x -C ${tmp}`); src = path.join(tmp, 'LOT_Claude_Finaux'); }
const lots = list('lots') || fs.readdirSync(src).filter(n => /^LOT_\d{3}$/.test(n)).map(n => n.slice(4)).sort();
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1280, height: 900 } }); const rap = [];
  for (const lot of lots) {
    const dir = path.join(src, 'LOT_' + lot); if (!fs.existsSync(dir)) continue;
    const fich = fs.readdirSync(dir).filter(f => /_Phase_B_V0_DX\.\d+\.html$/.test(f));
    const choisis = []; while (choisis.length < Math.min(2, fich.length)) { const f = pick(fich); if (!choisis.includes(f)) choisis.push(f); }
    let k = 0;
    for (const f of choisis) {
      k++; await pg.goto('file://' + path.resolve(dir, f)); await pg.waitForTimeout(300);
      const hs = []; for (const h of await pg.$$('h2')) if (await h.isVisible() && !/^(sources|références)/i.test((await h.innerText()).trim())) hs.push(h); let titre = 'début';
      if (hs.length) { const h = pick(hs); titre = (await h.innerText()).trim().slice(0, 70); await h.scrollIntoViewIfNeeded(); await pg.evaluate(() => window.scrollBy(0, -20)); }
      const nom = `LOT_${lot}_${k}_${f.match(/DX\.\d+/)[0]}.png`; await pg.screenshot({ path: path.join(sortie, nom) });
      rap.push({ lot, fichier: f, chapitre: titre, image: nom }); console.log(nom, '|', titre);
    }
  }
  fs.writeFileSync(path.join(sortie, 'captures.json'), JSON.stringify(rap, null, 1)); await b.close();
})();

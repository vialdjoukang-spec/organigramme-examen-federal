#!/usr/bin/env node
// 10 captures par LOT : 10 leçons au hasard, une partie (1 à 14) par leçon, parties distinctes et tournantes d'un LOT à l'autre.
// Usage : node captures10.js <dossier_LOT> <sortie> [rang_LOT]
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const [dir, out, rang = '1'] = process.argv.slice(2); fs.mkdirSync(out, { recursive: true });
const fich = fs.readdirSync(dir).filter(f => /_Phase_(A|B_V0_DX\.\d+)(_V0)?\.html$/.test(f)).sort();
let s = parseInt(rang) * 7919 + Date.now() % 1000; const rnd = () => (s = (s * 48271) % 2147483647) / 2147483647;
const shuf = a => a.map(x => [rnd(), x]).sort((p, q) => p[0] - q[0]).map(p => p[1]);
const choisis = shuf(fich).slice(0, 10), off = (parseInt(rang) * 4) % 14;
const parties = Array.from({ length: 14 }, (_, i) => ((i + off) % 14) + 1).slice(0, 10);
const NOM = ['Définition','Épidémiologie','Physiopathologie','Démarche','Anamnèse','Examen','Syndromes','Diagnostic positif','Examens','Arbre','Prise en charge','Prévention','Points clés','Pièges'];
(async () => { const b = await chromium.launch(), pg = await b.newPage({ viewport: { width: 1280, height: 900 } }), rap = [];
  for (let i = 0; i < choisis.length; i++) { const f = choisis[i], k = parties[i]; await pg.goto('file://' + path.resolve(dir, f)); await pg.waitForTimeout(250);
    const ok = await pg.evaluate(k => { const e = document.querySelector(`[id$="-p${k - 1}"]`); if (!e) return false; e.scrollIntoView(); window.scrollBy(0, -70); return true; }, k);
    const nom = `c${String(i + 1).padStart(2, '0')}_${f.replace(/^LOT_\d+_/, '').replace('.html', '')}_pt${k}.png`; await pg.screenshot({ path: path.join(out, nom) }); rap.push({ image: nom, partie: `${k}. ${NOM[k - 1]}`, ancre: ok }); }
  fs.writeFileSync(path.join(out, 'captures.json'), JSON.stringify(rap, null, 1)); await b.close(); console.log(rap.map(r => r.image + ' | ' + r.partie).join('\n')); })();

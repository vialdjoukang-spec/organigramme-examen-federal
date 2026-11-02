// node harnais/captures_forme.js <dir_conv> <dir_out> : 3 captures par fichier (cadrage point 1 · gros tableau · médicament cliquable ouvert)
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
(async () => {
  const [src, out] = process.argv.slice(2); fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1100, height: 760 } });
  for (const f of fs.readdirSync(src).filter(f => f.endsWith('.html')).sort()) {
    const n = f.replace('LOT_001_', '').replace('_V0', '').replace('.html', '');
    await pg.goto('file://' + path.resolve(src, f)); await pg.waitForTimeout(300);
    const ar = await pg.$('details.arbre'); if (ar) { await ar.evaluate(e => e.open = true); await ar.evaluate(e => e.scrollIntoView({block:'start'})); await pg.evaluate(() => window.scrollBy(0, -80)); }
    await pg.screenshot({ path: path.join(out, n + '_1_cadrage.png') });
    const tabs = await pg.$$('table'); let big = null, mx = 0; for (const t of tabs) { const h = await t.evaluate(e => e.getBoundingClientRect().height); if (h > mx && h < 2000) { mx = h; big = t } }
    if (big) { await big.evaluate(e => e.scrollIntoView({block:'start'})); await pg.evaluate(() => window.scrollBy(0, -60)); }
    await pg.screenshot({ path: path.join(out, n + '_2_tableau.png') });
    pg.setDefaultTimeout(5000); const m = await pg.$('.tm.med'); if (m) { await m.evaluate(e => { let d = e.closest('details'); while (d) { d.open = true; d = d.parentElement && d.parentElement.closest('details') } }); await m.evaluate(e => e.scrollIntoView({block:'center'})); try { await m.hover({ timeout: 3000, force: true }) } catch (e) {} await pg.waitForTimeout(150); }
    await pg.screenshot({ path: path.join(out, n + '_3_medicament.png') });
  }
  await b.close();
})();

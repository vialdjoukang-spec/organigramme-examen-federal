// 3 captures par HTML (début, milieu, fin) — node harnais/captures.js <fichier.html> <dossier_sortie>
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [f, out] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 900 } });
  await p.goto('file://' + path.resolve(f)); await p.waitForTimeout(500);
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const base = path.basename(f, '.html');
  for (const [i, y] of [[1, 0], [2, Math.max(0, h / 2 - 450)], [3, Math.max(0, h - 900)]]) {
    await p.evaluate(v => window.scrollTo(0, v), y); await p.waitForTimeout(150);
    await p.screenshot({ path: path.join(out, `${base}_${i}.png`) });
  }
  await b.close(); console.log(base, h);
})();

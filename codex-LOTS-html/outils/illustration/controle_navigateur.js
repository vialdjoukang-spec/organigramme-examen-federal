// Contrôle technique local ; les captures doivent ensuite être inspectées.
// node controle_navigateur.js INTEGRATION.json apercu.html dossier-captures
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const { chromium } = require('playwright');
const sha = raw => crypto.createHash('sha256').update(raw).digest('hex');

async function main() {
  if (process.argv.length !== 5) throw Error('Arguments : INTEGRATION.json apercu.html dossier-captures');
  const [jobPath, previewPath, capturePath] = process.argv.slice(2).map(p => path.resolve(p));
  const base = fs.realpathSync(path.resolve(__dirname, '../..'));
  for (const file of [jobPath, previewPath]) {
    if (!fs.realpathSync(file).startsWith(base + path.sep)) throw Error('Lecture hors périmètre');
  }
  if (!capturePath.startsWith(base + path.sep)) throw Error('Captures hors périmètre');
  // Vérifie également les ancêtres existants pour refuser les liens sortants.
  let ancestor = capturePath;
  while (!fs.existsSync(ancestor)) ancestor = path.dirname(ancestor);
  const realAncestor = fs.realpathSync(ancestor);
  if (realAncestor !== base && !realAncestor.startsWith(base + path.sep)) throw Error('Lien hors périmètre');
  const job = JSON.parse(fs.readFileSync(jobPath));
  const partie = job.partie_insertion === undefined ? 9 : job.partie_insertion;
  if (![8, 9].includes(partie) || !/^[a-z][a-z0-9-]*$/.test(job.id)) throw Error('Travail invalide');
  const raw = fs.readFileSync(previewPath), rows = [];
  fs.mkdirSync(capturePath, { recursive: true });
  const browser = await chromium.launch({ headless: true, executablePath: process.env.CHROMIUM_PATH || '/usr/bin/chromium', args: ['--no-sandbox'] });
  try {
    for (const mobile of [false, true]) {
      const page = await browser.newPage({ viewport: mobile ? { width: 390, height: 844 } : { width: 1440, height: 1100 }, hasTouch: mobile });
      const errors = [];
      page.on('pageerror', e => errors.push(e.message));
      await page.route('**/*', route => route.abort());
      await page.setContent(raw.toString());
      const chain = await page.evaluate(({ partie, anchor }) => {
        const sections = [...document.querySelectorAll('section > h2[id]')].filter(h => h.id.endsWith('-p' + partie));
        if (sections.length !== 1) throw Error('Section ambiguë');
        const queue = [[sections[0].parentElement, []]], seen = new Set();
        for (const [node, chain] of queue) {
          if (node.id === anchor || node.contains(document.getElementById(anchor))) return chain;
          for (const button of node.querySelectorAll('button[popovertarget]')) {
            if (button.getAttribute('popovertargetaction') === 'hide') continue;
            const target = button.getAttribute('popovertarget'), win = document.getElementById(target);
            if (win && win.hasAttribute('popover') && !seen.has(target)) {
              seen.add(target); queue.push([win, [...chain, target]]);
            }
          }
        }
        throw Error('Ancre inaccessible');
      }, { partie, anchor: job.ancre });
      for (const target of chain) {
        await page.locator(`button[popovertarget=${JSON.stringify(target)}]:not([popovertargetaction="hide"])`).filter({ visible: true }).first().click();
      }
      const trigger = page.locator(`[id=${JSON.stringify(job.ancre)}] button[popovertarget="image-${job.id}"]`);
      if ((await trigger.textContent()).trim() !== job.expression.trim()) throw Error('Expression incorrecte');
      await trigger.click();
      const win = page.locator(`[id="image-${job.id}"]`);
      if (!await win.evaluate(e => e.matches(':popover-open'))) throw Error('Fenêtre fermée');
      if (await win.locator('.paire img').count() !== 1 || await win.locator('.paire svg image').count() !== 1) throw Error('Paire originale/annotée absente');
      await win.locator('.paire img').evaluate(e => e.decode());
      const same = await win.evaluate(e => e.querySelector('.paire img').src === e.querySelector('.paire svg image').getAttribute('href'));
      if (!same) throw Error('Originaux différents');
      if (await win.evaluate(e => e.scrollWidth > e.clientWidth + 2)) throw Error('Débordement horizontal');
      const captures = [];
      const metrics = await win.evaluate(e => ({ max: e.scrollHeight - e.clientHeight, step: Math.max(1, Math.floor(e.clientHeight * 0.75)) }));
      const positions = [...new Set([...Array.from({ length: Math.ceil(metrics.max / metrics.step) }, (_, i) => i * metrics.step), metrics.max])];
      for (let i = 0; i < positions.length; i++) {
        await win.evaluate((e, y) => { e.scrollTop = y; }, positions[i]);
        const file = path.join(capturePath, `comparaison-${mobile ? 'mobile' : 'bureau'}-${String(i).padStart(2, '0')}.png`);
        await page.screenshot({ path: file });
        captures.push({ fichier: path.relative(base, file), sha256: sha(fs.readFileSync(file)), scrollTop: await win.evaluate(e => e.scrollTop) });
      }
      let definitions = 0;
      for (const button of await win.locator('button.repere').all()) {
        await button.click();
        const id = await button.getAttribute('popovertarget');
        const def = page.locator(`[id=${JSON.stringify(id)}]`);
        if (!await def.evaluate(e => e.matches(':popover-open'))) throw Error('Définition fermée');
        await def.locator('button[popovertargetaction="hide"]').click();
        definitions++;
      }
      if (!definitions || errors.length) throw Error('Définitions absentes ou erreur JavaScript : ' + errors.join('; '));
      rows.push({ mobile, tactile_emule: mobile, partie, definitions, errors, debordement: false, captures });
      await page.close();
    }
  } finally { await browser.close(); }
  const report = { date: new Date().toISOString(), sha256_apercu: sha(raw), sha256_integration: sha(fs.readFileSync(jobPath)), configurations: rows, inspection_visuelle: false, validation_clinique: false };
  fs.writeFileSync(path.join(capturePath, 'CONTROLE_NAVIGATEUR.json'), JSON.stringify(report, null, 2) + '\n');
  console.log(JSON.stringify(report));
}
main().catch(e => { console.error(e); process.exitCode = 1; });

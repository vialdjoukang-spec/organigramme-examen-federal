#!/usr/bin/env python3
"""CAPTURE5 — 5 captures d'écran par chapitre (ordre de Vial du 10.11.2026), zéro modèle.
Pour chaque leçon : 1 première partie · 2 fenêtre explicative ouverte · 3 examens complémentaires (point 9)
· 4 prise en charge (point 11) · 5 dernière partie. Sortie : captures/LOT_XXX/<leçon>_1..5.png
Repérage robuste des points 9 et 11 : identifiant *-pN ou pN, sinon titre h2–h4 « N. … », sinon mot-clé, hors menu ;
défilement instantané (scroll-behavior neutralisé). La capture 2 n'est écrite que si une fenêtre est vérifiée ouverte.
Usage : python3 Claude/_outils/capture5.py Claude/LOT_001/*.html [--sortie captures] [--largeur 1440]"""
import os, subprocess, tempfile, argparse

JS = r"""
const { chromium } = require('playwright');
const [fichier, base, largeur] = process.argv.slice(2);
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: +largeur, height: 900 }, deviceScaleFactor: 1 });
  await p.goto('file://' + fichier, { waitUntil: 'load' });
  await p.addStyleTag({ content: 'html,body{scroll-behavior:auto!important}' });
  await p.evaluate(() => document.fonts && document.fonts.ready);
  await p.waitForTimeout(500);
  const res = {};
  const nettoyer = async () => {
    await p.keyboard.press('Escape').catch(() => {});
    await p.evaluate(() => {
      document.querySelectorAll('[popover]').forEach(e => { try { if (e.matches(':popover-open')) e.hidePopover(); } catch (_) {} });
      if (document.activeElement) document.activeElement.blur(); });
    await p.mouse.move(2, 2);
  };
  const allerPartie = async (n, mots) => p.evaluate(([n, mots]) => {
    const visible = e => { const r = e.getBoundingClientRect(); return r.height > 0 && r.width > 0 && !e.closest('#brain-barre14, nav'); };
    const re = new RegExp('(^|-)p' + n + '$');
    let e = [...document.querySelectorAll('[id]')].find(x => re.test(x.id) && visible(x));
    const hs = [...document.querySelectorAll('h2,h3,h4')].filter(visible);
    if (!e) e = hs.find(h => new RegExp('^\\s*' + n + '\\s*[.)\\-–:]?\\s+\\D').test(h.textContent));
    if (!e) e = hs.find(h => mots.some(w => h.textContent.toLowerCase().includes(w)));
    if (!e) return null;
    window.scrollTo({ top: e.getBoundingClientRect().top + window.scrollY - 12, behavior: 'instant' });
    return (e.id ? '#' + e.id : e.tagName) + ' y=' + Math.round(window.scrollY);
  }, [n, mots]);

  await p.evaluate(() => window.scrollTo({ top: 0, behavior: 'instant' })); await p.waitForTimeout(200);
  await p.screenshot({ path: base + '_1.png' }); res[1] = 'début';

  // 2. fenêtre explicative réellement ouverte : popover, terme .tm (.df visible) ou details, dans le corps du cours
  const cands = await p.$$('[popovertarget], .tm, details:not([open]) > summary');
  let ouvert = null;
  for (const c of cands.slice(0, 60)) {
    const ok = await c.evaluate(e => { const r = e.getBoundingClientRect();
      return r.height > 0 && !e.closest('#brain-barre14, nav, .df, [popover]') && window.scrollY + r.top > 250; });
    if (!ok) continue;
    await c.evaluate(e => window.scrollTo({ top: e.getBoundingClientRect().top + window.scrollY - 260, behavior: 'instant' }));
    await p.waitForTimeout(120);
    const genre = await c.evaluate(e => e.hasAttribute('popovertarget') ? 'pop' : (e.tagName === 'SUMMARY' ? 'det' : 'tm'));
    if (genre === 'tm') { await c.hover({ timeout: 1500 }).catch(() => {}); await c.evaluate(e => e.focus()); }
    else await c.click({ timeout: 1500 }).catch(() => {});
    await p.waitForTimeout(350);
    ouvert = await c.evaluate((e, g) => {
      if (g === 'pop') { const f = document.getElementById(e.getAttribute('popovertarget')); return f && f.matches(':popover-open') ? 'popover' : null; }
      if (g === 'det') return e.parentElement.open ? 'details' : null;
      const d = e.querySelector('.df'); if (!d) return null; const r = d.getBoundingClientRect();
      return getComputedStyle(d).display !== 'none' && r.height > 0 && r.bottom > 0 && r.top < innerHeight ? 'terme' : null;
    }, genre);
    if (ouvert) break;
    await nettoyer();
  }
  if (!ouvert) {  // gabarit L1 : fenêtre centrale :target, ouverte par un lien a.ouvre (de préférence au point 9 ou 11)
    const id = await p.evaluate(() => { const L = [...document.querySelectorAll('a.ouvre[href^="#f-"]')].filter(a => !a.closest('section.fenetre, nav'));
      const c = L.find(a => /-p(9|11)-/.test(a.getAttribute('href'))) || L[0]; return c ? c.getAttribute('href').slice(1) : null; });
    if (id) { await p.evaluate(i => { location.hash = '#' + i; }, id); await p.waitForTimeout(400);
      const vu = await p.evaluate(i => { const s = document.getElementById(i); if (!s) return false; const r = s.getBoundingClientRect();
        return getComputedStyle(s).display !== 'none' && r.height > 0 && r.width > 0; }, id);
      if (vu) ouvert = ':target #' + id; }
  }
  if (ouvert) { await p.screenshot({ path: base + '_2.png' }); res[2] = 'fenêtre ' + ouvert; } else res[2] = 'AUCUNE FENÊTRE';
  await nettoyer();
  await p.evaluate(() => { if (location.hash) { history.replaceState(null, '', location.pathname); location.hash = '#'; } }); await p.waitForTimeout(150);

  const s9 = await allerPartie(9, ['examens complémentaires']);
  await p.waitForTimeout(250); await p.screenshot({ path: base + '_3.png' });
  res[3] = s9 ? 'examens ' + s9 : 'examens (NON TROUVÉ)';
  const s11 = await allerPartie(11, ['prise en charge']);
  await p.waitForTimeout(250); await p.screenshot({ path: base + '_4.png' });
  res[4] = s11 ? 'prise en charge ' + s11 : 'prise en charge (NON TROUVÉE)';
  await p.evaluate(() => window.scrollTo({ top: document.documentElement.scrollHeight, behavior: 'instant' }));
  await p.waitForTimeout(250);
  await p.screenshot({ path: base + '_5.png' }); res[5] = 'fin';
  console.log(JSON.stringify(res));
  await b.close();
})();
"""

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('fichiers', nargs='+')
    ap.add_argument('--sortie', default='captures')
    ap.add_argument('--largeur', default='1440')
    a = ap.parse_args()
    d = tempfile.mkdtemp()
    js = os.path.join(d, 'cap5.js'); open(js, 'w').write(JS)
    env = dict(os.environ)
    for f in a.fichiers:
        f = os.path.abspath(f)
        lot = os.path.basename(os.path.dirname(f))
        out = os.path.join(a.sortie, lot); os.makedirs(out, exist_ok=True)
        base = os.path.abspath(os.path.join(out, os.path.basename(f)[:-5]))
        r = subprocess.run(['node', js, f, base, a.largeur], capture_output=True, text=True, cwd=d, env=env)
        print(os.path.basename(f), (r.stdout.strip() or r.stderr.strip()[-300:]))

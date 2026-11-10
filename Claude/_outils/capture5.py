#!/usr/bin/env python3
"""CAPTURE5 — 5 captures d'écran par chapitre (ordre de Vial du 10.11.2026), zéro modèle.
Pour chaque leçon : 1 première partie · 2 fenêtre explicative ouverte · 3 examens complémentaires (point 9)
· 4 prise en charge (point 11) · 5 dernière partie. Sortie : captures/LOT_XXX/<leçon>_1..5.png
Usage : python3 Claude/_outils/capture5.py Claude/LOT_001/*.html [--sortie captures] [--largeur 1440]"""
import os, sys, json, subprocess, tempfile, argparse

JS = r"""
const { chromium } = require('playwright');
const [fichier, base, largeur] = process.argv.slice(2);
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: +largeur, height: 900 }, deviceScaleFactor: 1 });
  await p.goto('file://' + fichier, { waitUntil: 'load' });
  await p.waitForTimeout(700);
  const aller = async (sel) => p.evaluate((s) => {
    for (const q of s) { const e = document.querySelector(q); if (e) { e.scrollIntoView({ block: 'start' }); window.scrollBy(0, -10); return q; } }
    return null; }, sel);
  const parTitre = async (mots) => p.evaluate((m) => {
    const hs = [...document.querySelectorAll('h2,h3')];
    const h = hs.find(x => m.some(w => x.textContent.toLowerCase().includes(w)));
    if (h) { h.scrollIntoView({ block: 'start' }); window.scrollBy(0, -10); return true; } return false; }, mots);
  const res = {};
  await p.evaluate(() => window.scrollTo(0, 0)); await p.waitForTimeout(250);
  await p.screenshot({ path: base + '_1.png' }); res[1] = 'début';
  // 2. fenêtre : premier terme interactif visible dans le corps du cours, ouvert au focus
  const ok = await p.evaluate(() => {
    const t = [...document.querySelectorAll('main .tm, article .tm, body .tm, details:not([open]) > summary')]
      .find(e => e.closest('#brain-barre14') === null && e.getBoundingClientRect().height > 0);
    if (!t) return false;
    t.scrollIntoView({ block: 'center' });
    if (t.tagName === 'SUMMARY') t.parentElement.open = true; else t.focus();
    return true; });
  await p.waitForTimeout(400);
  if (ok) { await p.screenshot({ path: base + '_2.png' }); res[2] = 'fenêtre'; }
  const s9 = await aller(['[id$="-p9"]', '[id$="p9"]', '#p9']) || (await parTitre(['examens complémentaires', '9.'])) ;
  await p.waitForTimeout(300); await p.screenshot({ path: base + '_3.png' }); res[3] = s9 ? 'examens' : 'examens (non trouvé)';
  const s11 = await aller(['[id$="-p11"]', '[id$="p11"]', '#p11']) || (await parTitre(['prise en charge', '11.']));
  await p.waitForTimeout(300); await p.screenshot({ path: base + '_4.png' }); res[4] = s11 ? 'prise en charge' : 'prise en charge (non trouvée)';
  await p.evaluate(() => window.scrollTo(0, document.body.scrollHeight)); await p.waitForTimeout(300);
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
    for f in a.fichiers:
        f = os.path.abspath(f)
        lot = os.path.basename(os.path.dirname(f))
        out = os.path.join(a.sortie, lot); os.makedirs(out, exist_ok=True)
        base = os.path.abspath(os.path.join(out, os.path.basename(f)[:-5]))
        r = subprocess.run(['node', js, f, base, a.largeur], capture_output=True, text=True, cwd=d)
        print(os.path.basename(f), (r.stdout.strip() or r.stderr.strip()[-200:]))

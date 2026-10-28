#!/usr/bin/env node
// Scriptone S7 · captures sur TOUTE la longueur de la page, découpées par chapitre, avec rotation des chapitres (doléance 7 de Vial). Région VIS.
// Chaque fichier choisi est capturé chapitre par chapitre (h3 « N. … », sinon h2) du haut jusqu'à la fin du cours ; un chapitre plus haut
// que --tuile px est découpé en tuiles. --chapitres K limite à K chapitres par fichier : l'ordre tourne d'un passage à l'autre
// (état dans rotation.json) et la première page n'est jamais capturée seule. Mesures au pixel, émises en doléances typées :
//   V1 texte hors Atkinson (police calculée)   V2 fin de paragraphe orpheline (dernière ligne < 12 % de la colonne)
//   V3 blanc vertical inutile (> 3 interlignes) V4 débordement horizontal      V5 texte coupé (overflow caché)
//   mesure : lignes réelles du point 2 et caractères par ligne (calibrage de s4_budget, CPL)
// Usage : node harnais/bilan/captures.js [--lots 008 009] [--fichier F.html …] [--fichiers 2] [--chapitres K|tout] [--sortie D]
//         [--source DOSSIER_LOT_Claude_Finaux] [--graine N] [--tuile 1800] [--mesures-seules]
// Source par défaut : origin/main (git archive). Sortie : <sortie>/captures.json (+ PNG).
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path'), os = require('os'), cp = require('child_process');
const argv = process.argv;
const arg = (k, d) => { const i = argv.indexOf('--' + k); return i < 0 ? d : argv[i + 1]; };
const list = (k) => { const i = argv.indexOf('--' + k); if (i < 0) return null; const o = []; for (let j = i + 1; j < argv.length && !argv[j].startsWith('--'); j++) o.push(argv[j]); return o; };
let s = parseInt(arg('graine', '0')) || 0;
const rnd = () => (s = (s * 48271) % 2147483647) / 2147483647;
const sortie = arg('sortie', 'harnais/bilan/sortie/captures'); fs.mkdirSync(sortie, { recursive: true });
const TUILE = parseInt(arg('tuile', '1800')); const NFICH = parseInt(arg('fichiers', '2')); const KCH = arg('chapitres', 'tout');
const SEULES = argv.includes('--mesures-seules');
const fRot = path.join(sortie, 'rotation.json');
let rot = {}; try { rot = JSON.parse(fs.readFileSync(fRot, 'utf8')); } catch (e) { rot = {}; }

function cibles() {
  const unitaires = list('fichier');
  if (unitaires) return unitaires.map(f => ({ lot: (path.basename(f).match(/LOT_(\d{3})/) || [, '000'])[1], chemin: path.resolve(f) }));
  let src = arg('source');
  if (!src) { const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'lotsrc_')); cp.execSync(`git fetch -q origin main && git archive origin/main LOT_Claude_Finaux | tar -x -C ${tmp}`); src = path.join(tmp, 'LOT_Claude_Finaux'); }
  const lots = list('lots') || fs.readdirSync(src).filter(n => /^LOT_\d{3}$/.test(n)).map(n => n.slice(4)).sort();
  const out = [];
  for (const lot of lots) {
    const dir = path.join(src, 'LOT_' + lot); if (!fs.existsSync(dir)) continue;
    const fich = fs.readdirSync(dir).filter(f => /_Phase_(A_V0|B_V0_DX\.\d+)\.html$/.test(f)).sort((a, b) => (parseInt((a.match(/DX\.(\d+)/) || [, 0])[1]) - parseInt((b.match(/DX\.(\d+)/) || [, 0])[1])));
    const r = rot[lot] = rot[lot] || { fichier: s ? Math.floor(rnd() * fich.length) : 0, chapitres: {} };
    for (let k = 0; k < Math.min(NFICH, fich.length); k++) out.push({ lot, chemin: path.join(dir, fich[(r.fichier + k) % fich.length]) });
    r.fichier = (r.fichier + NFICH) % Math.max(1, fich.length);   // rotation des fichiers d'un passage à l'autre
  }
  return out;
}

// mesures exécutées dans la page
function mesurer() {
  const main = document.querySelector('main') || document.querySelector('section.monograph') || document.body;
  const vis = (el) => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return r.height > 0 && r.width > 0 && cs.visibility !== 'hidden' && cs.display !== 'none'; };
  const sel = (el) => { let x = el, k = ''; while (x && x !== document.body) { if (x.id) { k = '#' + x.id + (k ? ' ' + k : ''); break; } x = x.parentElement; } return (k || 'main') + ' ' + el.tagName.toLowerCase(); };
  const out = { police: [], orphelines: [], blancs: [], debordement: null, coupes: [], lignes_point2: 0, cpl: [] };
  const poids = new Set([...document.fonts].filter(f => /Atkinson/i.test(f.family) && f.status === 'loaded').map(f => String(f.weight)));
  out.atkinson_poids = [...poids].sort(); out.atkinson_chargee = poids.has('400') && poids.has('700');
  for (const el of main.querySelectorAll('p,li,td,th,h2,h3,h4,summary,caption,label,dt,dd,b,span.dfn')) {
    if (!vis(el) || !el.textContent.trim()) continue;
    const fam = getComputedStyle(el).fontFamily.split(',')[0].replace(/["']/g, '').trim();
    if (!/Atkinson/i.test(fam)) out.police.push({ ancre: sel(el), famille: fam, extrait: el.textContent.trim().slice(0, 60) });
  }
  const p2 = [...main.querySelectorAll('h3')].find(h => /^\s*2\.\s/.test(h.textContent));
  for (const p of main.querySelectorAll('p')) {
    if (!vis(p) || p.closest('.df,.dxc,table')) continue;
    const rg = document.createRange(); rg.selectNodeContents(p);
    const rects = [...rg.getClientRects()].filter(r => r.width > 0);
    const lignes = {}; for (const r of rects) { const k = Math.round(r.top / 4); lignes[k] = Math.max(lignes[k] || 0, r.right) - 0; }
    const tops = Object.keys(lignes).map(Number).sort((a, b) => a - b);
    // regrouper les rectangles d'une même ligne (tolérance 4 px) : largeur = droite max - gauche du paragraphe
    const g = []; for (const t of tops) { if (g.length && t - g[g.length - 1].t <= 2) g[g.length - 1].d = Math.max(g[g.length - 1].d, lignes[t]); else g.push({ t, d: lignes[t] }); }
    const pr = p.getBoundingClientRect(); const n = g.length;
    if (n >= 2) {
      const der = g[n - 1].d - pr.left; if (der < 0.12 * pr.width) out.orphelines.push({ ancre: sel(p), largeur: Math.round(der), colonne: Math.round(pr.width), extrait: p.textContent.trim().slice(-50) });
      out.cpl.push(p.textContent.trim().length / n);
    }
    if (p2) { const h3s = [...main.querySelectorAll('h3')]; const i = h3s.indexOf(p2); const suiv = h3s[i + 1];
      if ((p2.compareDocumentPosition(p) & 4) && (!suiv || (suiv.compareDocumentPosition(p) & 2))) out.lignes_point2 += n; }
  }
  const blocs = [...main.children].filter(vis);
  for (let i = 1; i < blocs.length; i++) {
    const a = blocs[i - 1].getBoundingClientRect(), b = blocs[i].getBoundingClientRect(); const lh = parseFloat(getComputedStyle(blocs[i]).lineHeight) || 24;
    const gap = b.top - a.bottom; if (gap > 3 * lh) out.blancs.push({ ancre: sel(blocs[i]), ecart: Math.round(gap), interligne: Math.round(lh) });
  }
  const de = document.documentElement; out.debordement = de.scrollWidth > de.clientWidth + 1 ? de.scrollWidth - de.clientWidth : 0;
  for (const el of main.querySelectorAll('p,td,th,li,h2,h3')) {
    const cs = getComputedStyle(el); if (!vis(el) || el.closest('.df,.dxc')) continue;
    if (/(hidden|clip)/.test(cs.overflow + cs.overflowY) && el.scrollHeight > el.clientHeight + 2) out.coupes.push({ ancre: sel(el), extrait: el.textContent.trim().slice(0, 50) });
  }
  out.cpl = out.cpl.length ? Math.round(out.cpl.reduce((a, b) => a + b, 0) / out.cpl.length) : null;
  const ch = [...main.querySelectorAll('h3')].filter(h => /^\s*\d{1,2}\.\s/.test(h.textContent) && vis(h));
  const hs = ch.length ? ch : [...document.querySelectorAll('h2')].filter(h => vis(h) && !/^(sources|références)/i.test(h.textContent.trim()));
  const fin = (() => { const r = document.querySelector('details.refs, #refs'); return r ? r.getBoundingClientRect().top + scrollY : de.scrollHeight; })();
  out.chapitres = hs.map((h, i) => ({ titre: h.textContent.trim().slice(0, 70), y: Math.max(0, Math.floor(h.getBoundingClientRect().top + scrollY - 8)),
    fin: Math.ceil(i + 1 < hs.length ? hs[i + 1].getBoundingClientRect().top + scrollY - 8 : fin) }));
  if (!out.chapitres.length || out.chapitres[0].y > 40) out.chapitres.unshift({ titre: 'début', y: 0, fin: out.chapitres.length ? out.chapitres[0].y : fin });
  out.hauteur = de.scrollHeight;
  return out;
}

function doleance(code, fichier, ancre, severite, constat, correction, executant, preuve) {
  const id = require('crypto').createHash('sha1').update(`s7_captures|${code}|${ancre}|${constat}`).digest('hex').slice(0, 12);
  return { id, region: 'VIS', scriptone: 's7_captures', code, fichier, ancre, severite, constat, correction_prescrite: correction, executant, preuve: String(preuve || '').slice(0, 400) };
}

(async () => {
  const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: parseInt(arg('largeur', '1280')), height: parseInt(arg('hauteur', '900')) } });
  const rap = { captures: [], doleances: [], mesures: {} };
  for (const c of cibles()) {
    const nomf = path.basename(c.chemin); const court = (nomf.match(/DX\.\d+|Phase_A/) || ['page'])[0];
    await pg.goto('file://' + c.chemin); await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(150);
    const m = await pg.evaluate(mesurer); const n = m.chapitres.length;
    const r = rot[c.lot] = rot[c.lot] || { fichier: 0, chapitres: {} }; const off = r.chapitres[nomf] || 0;
    let ordre = [...Array(n).keys()].map(i => (i + off) % n);
    const K = KCH === 'tout' ? n : Math.min(n, parseInt(KCH));
    if (K === 1 && ordre[0] === 0 && n > 1) ordre = ordre.slice(1).concat(0);   // jamais la première page seule
    const choix = ordre.slice(0, K).sort((x, y) => x - y); r.chapitres[nomf] = (off + K) % Math.max(1, n);
    for (const i of choix) {
      const ch = m.chapitres[i]; let y = ch.y; let t = 1;
      while (y < ch.fin) {
        const h = Math.min(TUILE, ch.fin - y); const img = `LOT_${c.lot}_${court}_ch${String(i).padStart(2, '0')}_t${t}.png`;
        if (!SEULES && h > 4) await pg.screenshot({ path: path.join(sortie, img), fullPage: true, clip: { x: 0, y, width: pg.viewportSize().width, height: h } });
        rap.captures.push({ lot: c.lot, fichier: nomf, chapitre: ch.titre, index: i, tuile: t, y, hauteur: h, image: SEULES ? null : img });
        y += h; t++;
      }
    }
    const couvert = choix.reduce((a, i) => a + (m.chapitres[i].fin - m.chapitres[i].y), 0);
    rap.mesures[nomf] = { chapitres: n, captures: choix.length, couverture_pct: Math.round(100 * couvert / Math.max(1, m.hauteur)), hauteur: m.hauteur,
      atkinson_chargee: m.atkinson_chargee, hors_atkinson: m.police.length, orphelines: m.orphelines.length, blancs: m.blancs.length, debordement: m.debordement,
      coupes: m.coupes.length, lignes_point2: m.lignes_point2, cpl_reel: m.cpl };
    if (!m.atkinson_chargee) rap.doleances.push(doleance('V1', nomf, 'document', 'CRITIQUE', `Atkinson Hyperlegible non chargée dans le navigateur (graisses chargées : ${m.atkinson_poids.join(', ') || 'aucune'} ; 400 et 700 attendues)`, 'embarquer la police : python3 harnais/brain/scriptones/s1_police.py <fichier> --appliquer', 'script', 'document.fonts'));
    const fams = {}; for (const x of m.police) (fams[x.famille] = fams[x.famille] || []).push(x);
    for (const [f, L] of Object.entries(fams)) rap.doleances.push(doleance('V1', nomf, L[0].ancre, 'GRAVE', `${L.length} élément(s) affichés en ${f}`, 'neutraliser : python3 harnais/brain/scriptones/s1_police.py <fichier> --appliquer', 'script', L.slice(0, 3).map(x => x.ancre + ' « ' + x.extrait + ' »').join(' | ')));
    for (const x of m.orphelines.slice(0, 15)) rap.doleances.push(doleance('V2', nomf, x.ancre, 'DETAIL', `dernière ligne orpheline (${x.largeur} px sur ${x.colonne})`, 'text-wrap:pretty : python3 harnais/brain/scriptones/s2_rythme.py <fichier> --appliquer ; sinon reformuler la fin de phrase', 'script', x.extrait));
    for (const x of m.blancs) rap.doleances.push(doleance('V3', nomf, x.ancre, 'MOYEN', `blanc vertical de ${x.ecart} px (> 3 interlignes de ${x.interligne} px)`, 'retirer l\'espaceur : python3 harnais/brain/scriptones/s2_rythme.py <fichier> --appliquer', 'script', ''));
    if (m.debordement) rap.doleances.push(doleance('V4', nomf, 'document', 'GRAVE', `débordement horizontal de ${m.debordement} px`, 'envelopper le tableau large dans <div style="overflow-x:auto">', 'agent', ''));
    for (const x of m.coupes) rap.doleances.push(doleance('V5', nomf, x.ancre, 'GRAVE', 'texte coupé (overflow caché)', 'retirer la hauteur fixe ou l\'overflow caché de cet élément', 'agent', x.extrait));
    console.log(`${nomf} | ${choix.length}/${n} chapitres | couverture ${rap.mesures[nomf].couverture_pct} % | hors Atkinson ${m.police.length} | orphelines ${m.orphelines.length} | blancs ${m.blancs.length} | lignes point 2 ${m.lignes_point2} | ${m.cpl} car./ligne`);
  }
  fs.writeFileSync(path.join(sortie, 'captures.json'), JSON.stringify(rap, null, 1)); fs.writeFileSync(fRot, JSON.stringify(rot, null, 1));
  await b.close();
})().catch(e => { console.error('ERREUR captures :', e.message); process.exit(2); });

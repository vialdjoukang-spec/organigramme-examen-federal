#!/usr/bin/env node
/**
 * Capture 50 real Chromium headless screenshots across the live QCM Arène 2027 app
 * and compile them into a numbered PDF Catalogue:
 *   qcm-arene-2027/CATALOGUE_CAPTURES_50_ARENE_2027.pdf
 */
import http from 'http';
import fs from 'fs';
import path from 'path';
import { spawn } from 'child_process';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const APP_DIR = path.resolve(__dirname, '..');
const OUT_SHOTS = path.join('/tmp', 'arene_shots_50');
const GALLERY_HTML = path.join('/tmp', 'arene_catalogue_50.html');
const PDF_OUT = path.join(APP_DIR, 'CATALOGUE_CAPTURES_50_ARENE_2027.pdf');

fs.mkdirSync(OUT_SHOTS, { recursive: true });

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.webp': 'image/webp',
  '.svg': 'image/svg+xml',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png'
};

function startServer() {
  return new Promise((resolve) => {
    const srv = http.createServer((req, res) => {
      const urlPath = decodeURIComponent((req.url || '/').split('?')[0]);
      const rel = urlPath === '/' ? 'index.html' : urlPath.replace(/^\/+/, '');
      const full = path.join(APP_DIR, rel);
      if (!full.startsWith(APP_DIR) || !fs.existsSync(full) || fs.statSync(full).isDirectory()) {
        res.writeHead(404);
        res.end('Not found');
        return;
      }
      const ext = path.extname(full);
      res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
      fs.createReadStream(full).pipe(res);
    });
    srv.listen(0, '127.0.0.1', () => {
      resolve({ srv, port: srv.address().port });
    });
  });
}

class CDP {
  constructor(wsUrl) {
    this.ws = new WebSocket(wsUrl);
    this.id = 1;
    this.pending = new Map();
    this.ready = new Promise((res, rej) => {
      this.ws.onopen = res;
      this.ws.onerror = rej;
    });
    this.ws.onmessage = (ev) => {
      const msg = JSON.parse(ev.data);
      if (msg.id && this.pending.has(msg.id)) {
        const { resolve, reject } = this.pending.get(msg.id);
        this.pending.delete(msg.id);
        if (msg.error) reject(new Error(JSON.stringify(msg.error)));
        else resolve(msg.result);
      }
    };
  }
  async send(method, params = {}) {
    await this.ready;
    const id = this.id++;
    return new Promise((resolve, reject) => {
      this.pending.set(id, { resolve, reject });
      this.ws.send(JSON.stringify({ id, method, params }));
    });
  }
  async evalExpr(expression) {
    const r = await this.send('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true });
    if (r.exceptionDetails) throw new Error('JS Error: ' + JSON.stringify(r.exceptionDetails));
    return r.result?.value;
  }
  async shot(filename) {
    const r = await this.send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(path.join(OUT_SHOTS, filename), Buffer.from(r.data, 'base64'));
  }
  close() {
    this.ws.close();
  }
}

const wait = (ms) => new Promise((r) => setTimeout(r, ms));

async function run() {
  const { srv, port } = await startServer();
  const baseUrl = `http://127.0.0.1:${port}/index.html`;
  const dbgPort = 9245;

  const chrome = spawn('/usr/bin/chromium', [
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    `--remote-debugging-port=${dbgPort}`,
    '--window-size=1440,900',
    'about:blank'
  ], { stdio: 'ignore' });

  let wsUrl = null;
  for (let i = 0; i < 30; i++) {
    try {
      const list = await (await fetch(`http://127.0.0.1:${dbgPort}/json/list`)).json();
      const page = list.find((t) => t.type === 'page');
      if (page) { wsUrl = page.webSocketDebuggerUrl; break; }
    } catch {}
    await wait(250);
  }
  if (!wsUrl) throw new Error('Chromium CDP failed to start');

  const cdp = new CDP(wsUrl);
  await cdp.send('Page.enable');
  await cdp.send('Runtime.enable');
  await cdp.send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1.5, mobile: false });
  await cdp.send('Page.navigate', { url: baseUrl });
  await wait(1400);

  const captures = [];
  async function snap(num, label, fn) {
    if (fn) await fn();
    await wait(350);
    const file = `cap_${String(num).padStart(2, '0')}.png`;
    await cdp.shot(file);
    captures.push({ num, label, file });
    console.log(`Captured ${String(num).padStart(2, '0')}/50: ${label}`);
  }

  async function openSSPAndWait(cat, code) {
    await cdp.evalExpr(`(async () => { closeAnswer(); await openSSP('${cat}', '${code}'); })()`);
    await wait(450);
  }

  async function openAnsOfType(qType, preferredIdx = 0) {
    await cdp.evalExpr(`(() => {
      closeAnswer();
      setQFilter('${qType || 'ALL'}');
      const idx = Math.min(${preferredIdx}, Math.max(0, STATE.filteredQuestions.length - 1));
      openAnswer(idx);
    })()`);
  }

  // 01-04: Home & Veille
  await snap(1, 'Accueil · Arène Examen Fédéral 2027 (Vue générale, formule a·A + k\'·K\' + m·M, portails G/S/F/O)');
  await snap(2, 'Accueil · Arène (Aperçu Veille officielle 2027)', () => cdp.evalExpr(`window.scrollTo(0, 520)`));
  await snap(3, 'Bandeau Santé Suisse (Actualité suivante OFSP/IML/Swissmedic)', () => cdp.evalExpr(`window.scrollTo(0, 0); nextTicker(); nextTicker();`));
  await snap(4, 'Onglet Veille 2027 & Réseau officiel suisse (SSMIG, Smarter Medicine, SSI, Compendium, Hôpitaux & Facultés)', () => cdp.evalExpr(`switchTab('VEILLE')`));

  // 05-08: Categories G, S, F, O
  await snap(5, 'Catégorie G · Situations générales (16 cellules uniformes arrondies bleu, fond blanc papier)', () => cdp.evalExpr(`switchTab('G')`));
  await snap(6, 'Catégorie S · Symptômes spécifiques (113 SSP, cellules vert émeraude)', () => cdp.evalExpr(`switchTab('S')`));
  await snap(7, 'Catégorie F · Findings & Résultats anormaux (44 SSP, cellules ambre)', () => cdp.evalExpr(`switchTab('F')`));
  await snap(8, 'Catégorie O · Autres situations cliniques (75 SSP, cellules violet)', () => cdp.evalExpr(`switchTab('O')`));

  // 09-14: G1 deep dive
  await snap(9, 'G1 Sudation anormale · Combat QCM Page 1 + Panoramique des causes par fréquence déployé', async () => {
    await openSSPAndWait('G', 'G1');
    await cdp.evalExpr(`document.querySelector('#combatPanoramique details')?.setAttribute('open', '')`);
  });
  await snap(10, 'G1 · Interaction Type A avec score validé (1/1 pt) et Chronomètre actif', () => cdp.evalExpr(`(() => {
    document.querySelector('#combatPanoramique details')?.removeAttribute('open');
    setQFilter('A');
    answerA(0, STATE.filteredQuestions[0].an);
    if (!STATE.chronoRunning) toggleChrono();
  })()`));
  await snap(11, 'G1 · Pleine page Réponses (Type A) · Planche peau + Schéma Système Nerveux Autonome', () => cdp.evalExpr(`openAnswer(0)`));
  await snap(12, 'G1 · Type K\' (4 propositions Vrai/Faux) · Réponse soumise & Pleine page Réponses', () => cdp.evalExpr(`(() => {
    closeAnswer();
    setQFilter('K');
    const q = STATE.filteredQuestions[0];
    for (let i = 0; i < 4; i++) answerK(0, i, q.an[i]);
    openAnswer(0);
  })()`));
  await snap(13, 'G1 · Menu Long (Liste étendue) · Sélection & Pleine page Réponses', () => cdp.evalExpr(`(() => {
    closeAnswer();
    setQFilter('M');
    answerM(0, STATE.filteredQuestions[0].an);
    openAnswer(0);
  })()`));
  await snap(14, 'G1 · Page 21 (Preuve des 405+ QCMs / 21 pages pour un seul SSP)', () => cdp.evalExpr(`(() => {
    closeAnswer();
    setQFilter('ALL');
    const lastP = Math.ceil(STATE.filteredQuestions.length / 20);
    goPage(lastP);
  })()`));

  // 15-46: Broad clinical & visual tour across G, S, F, O
  const tour = [
    [15, 'G', 'G2', 'K', 0, false, 'G2 Tuméfaction, masse, adénopathies · Combat Type K\' (Entraînement interactif)'],
    [16, 'G', 'G6', 'A', 1, true,  'G6 Fièvre, frissons, hyperthermie · Pleine page Réponses (Causes stratifiées & Pratiques suisses)'],
    [17, 'G', 'G10', 'A', 0, true, 'G10 Douleur, tous types · Pleine page Réponses (Planche douleur & Parcours clinique suisse)'],
    [18, 'S', 'S2.1', 'ALL', 0, false, 'S2.1 Apnée, apnée avec micro-éveil · Combat QCM + Panoramique des causes déployé'],
    [19, 'S', 'S2.6', 'A', 2, true,  'S2.6 Toux, expectoration, hémoptysie · Pleine page Réponses (Courbe Débit-Volume Spirométrie & Thorax)'],
    [20, 'S', 'S2.5', 'ALL', 0, false, 'S2.5 Douleur thoracique · Panoramique avec prévalences suisses (Verda/SMW : SCA 1.5%, EP 0.3%)'],
    [21, 'S', 'S2.5', 'A', 0, true,  'S2.5 Douleur thoracique · Pleine page Réponses (Tracé ECG STEMI vs Normal & Foyers cardiaques)'],
    [22, 'S', 'S2.1', 'K', 1, true,  'S2.1 Apnée, apnée avec micro-éveil · Pleine page Réponses Type K\' (Courbe Hb-O₂ & Voies aériennes)'],
    [23, 'S', 'S3.1', 'M', 0, false, 'S3.1 Douleur abdominale · Combat Menu Long'],
    [24, 'S', 'S3.1', 'A', 0, true,  'S3.1 Douleur abdominale · Pleine page Réponses (Topographie 9 quadrants & Parcours)'],
    [25, 'S', 'S3.6', 'ALL', 0, false, 'S3.6 Hématémèse · Combat QCM (Questions entrelacées A/K\'/M)'],
    [26, 'S', 'S4.1', 'A', 1, true,  'S4.1 Variations du développement sexuel · Pleine page Réponses (Planche & Parcours clinique)'],
    [27, 'S', 'S4.5', 'K', 2, true,  'S4.5 Symptômes menstruels · Pleine page Réponses Type K\' (Courbe Hb-O₂ & Stratification)'],
    [28, 'S', 'S5.1', 'A', 0, true,  'S5.1 Posture anormale, déformations rachidiennes · Pleine page Réponses (Planche Rachis & Drapeaux rouges)'],
    [29, 'S', 'S6.1', 'A', 1, true,  'S6.1 Lésions des muqueuses buccale, génitale ou périanale · Pleine page Réponses (Davenport & Repères)'],
    [30, 'S', 'S7.1', 'A', 0, true,  'S7.1 Troubles de l\'équilibre, chutes · Pleine page Réponses (Planche & Système nerveux)'],
    [31, 'S', 'S8.1', 'ALL', 0, false, 'S8.1 Traumatismes abdominaux · Combat QCM (Propreté rédactionnelle vérifiée)'],
    [32, 'S', 'S8.1', 'A', 0, true,  'S8.1 Traumatismes abdominaux · Pleine page Réponses (Topographie abdominale & Urgences)'],
    [33, 'S', 'S9.1', 'A', 0, true,  'S9.1 Anxiété et panique · Pleine page Réponses (Système nerveux autonome & Statut)'],
    [34, 'F', 'F1.1', 'ALL', 0, false, 'F1.1 Pression artérielle anormale · Combat QCM + Panoramique des causes déployé'],
    [35, 'F', 'F1.1', 'A', 0, true,  'F1.1 Pression artérielle anormale · Pleine page Réponses (ECG & Système nerveux autonome)'],
    [36, 'F', 'F1.12', 'A', 0, true, 'F1.12 Exophtalmie, myosis ou mydriase · Pleine page Réponses (Nerfs crâniens & Autonome)'],
    [37, 'F', 'F1.19', 'A', 0, true, 'F1.19 Perte de connaissance transitoire, syncope · Pleine page Réponses (ECG & Foyers cardiaques)'],
    [38, 'F', 'F2.4', 'A', 0, true,  'F2.4 Radiographies anormales : abdomen, thorax, squelette · Pleine page Réponses'],
    [39, 'O', 'O1.1', 'A', 0, true,  'O1.1 Poids de naissance anormal, prématurité · Pleine page Réponses (Planche néonatale & SpO₂)'],
    [40, 'O', 'O2.2', 'A', 0, true,  'O2.2 Troubles du comportement de l\'enfant et de l\'adolescent · Pleine page Réponses'],
    [41, 'O', 'O3.1', 'A', 0, true,  'O3.1 Maltraitance et négligence de la personne âgée · Pleine page Réponses'],
    [42, 'O', 'O4.1', 'A', 0, true,  'O4.1 Consultation avant activité sportive ou après lésion sportive · Pleine page Réponses'],
    [43, 'O', 'O5.2', 'A', 0, true,  'O5.2 Réorientation des objectifs de soins, décisions de fin de vie · Pleine page Réponses'],
    [44, 'O', 'O5.5', 'A', 0, true,  'O5.5 Besoin de soutien psychosocial ou spirituel · Pleine page Réponses'],
    [45, 'O', 'O6.3', 'A', 0, true,  'O6.3 Violence domestique, abus sexuel, viol · Pleine page Réponses'],
    [46, 'O', 'O7.1', 'A', 0, true,  'O7.1 Consultation avant ou après un voyage en pays tropical · Pleine page Réponses']
  ];

  for (const [num, cat, code, qf, idx, openAns, lbl] of tour) {
    await snap(num, lbl, async () => {
      await openSSPAndWait(cat, code);
      if (openAns) {
        await openAnsOfType(qf, idx);
      } else {
        await cdp.evalExpr(`setQFilter('${qf}'); document.querySelector('#combatPanoramique details')?.setAttribute('open', '');`);
      }
    });
  }

  // 47-50: Multi-SSP Arena modes, Swiss filter, Final updated stats
  await snap(47, 'Défi rapide multi-SSP (15 QCMs tirés à travers les 248 SSPs)', async () => {
    await cdp.evalExpr(`closeAnswer(); startArenaChallenge(15, false);`);
    await wait(700);
  });
  await snap(48, 'Examen Blanc Chronométré (30 QCMs · Compte à rebours 45:00 actif)', async () => {
    await cdp.evalExpr(`closeAnswer(); startArenaChallenge(30, true);`);
    await wait(800);
  });
  await snap(49, 'G1 · Filtrage ciblé « Smarter Medicine / Sortie d\'hospitalisation » · Pleine page Réponses', async () => {
    await openSSPAndWait('G', 'G1');
    await cdp.evalExpr(`(() => {
      document.getElementById('qSearchBox').value = 'Smarter Medicine';
      onThemeChange();
      if (STATE.filteredQuestions.length > 0) openAnswer(0);
    })()`);
  });
  await snap(50, 'Accueil · Arène après combat (Statistiques de progression et taux de réussite mis à jour)', async () => {
    await cdp.evalExpr(`closeAnswer(); exitCombat(); switchTab('HOME'); window.scrollTo(0, 0);`);
  });

  cdp.close();
  chrome.kill();
  srv.close();

  // Build HTML Gallery and print to PDF via Chromium
  const cards = captures.map((c) => {
    const b64 = fs.readFileSync(path.join(OUT_SHOTS, c.file)).toString('base64');
    return `
      <div class="page-item">
        <div class="cap-head">
          <span class="badge">${String(c.num).padStart(2, '0')} / 50</span>
          <span class="title">${c.label}</span>
        </div>
        <img src="data:image/png;base64,${b64}" />
      </div>`;
  }).join('\n');

  const catRaw = fs.readFileSync(path.join(APP_DIR, 'data', 'catalog.js'), 'utf8');
  const catMeta = JSON.parse(catRaw.replace(/^window\.QCM_CATALOG\s*=\s*/, '').trim().replace(/;$/, ''));
  const props = catMeta.proportions;

  const html = `<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><title>Catalogue 50 Captures · Arène QCM 2027</title>
  <style>
    @page { size: A4 landscape; margin: 10mm; }
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; margin: 0; background: #fff; color: #0f172a; }
    .cover { height: 168mm; display: flex; flex-direction: column; justify-content: center; padding: 20px 36px; border: 3px solid #1d4ed8; border-radius: 16px; background: linear-gradient(135deg,#fcfbf7,#eff6ff); page-break-after: always; box-sizing: border-box; }
    .cover h1 { font-size: 26px; margin: 0 0 12px; color: #1e3a8a; }
    .cover p { font-size: 14.5px; color: #334155; line-height: 1.55; max-width: 860px; }
    .page-item { page-break-after: always; padding-top: 2px; }
    .page-item:last-child { page-break-after: auto; }
    .cap-head { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; padding: 6px 10px; background: #f1f5f9; border-radius: 8px; border-left: 5px solid #16a34a; }
    .badge { background: #14532d; color: #fff; font-weight: 800; font-size: 12px; padding: 3px 9px; border-radius: 999px; }
    .title { font-weight: 700; font-size: 13px; }
    img { width: 100%; max-height: 172mm; object-fit: contain; border: 1px solid #cbd5e1; border-radius: 8px; }
  </style></head><body>
    <div class="cover">
      <h1>Catalogue Officiel des 50 Captures · Arène QCM Examen Fédéral 2027</h1>
      <p><strong>Base auditée :</strong> ${catMeta.total_questions.toLocaleString('fr-CH')} QCMs Type Examen (Type A · Type K' · Menu Long, a=${props.a}, k'=${props.k_prime}, m=${props.m}) couvrant les ${catMeta.total_ssp} SSPs PROFILES et ${catMeta.total_dds.toLocaleString('fr-CH')} diagnostics différentiels stratifiés par fréquence.</p>
      <p><strong>Double Audit Indépendant validé :</strong> Contrôleur d'Aléa Absolu (CSPRNG, max streak 2, 16/16 vecteurs K', 0 répétition Menu Long) + Conformité Clinique Suisse (Compendium / AIPS, Smarter Medicine, OFSP, SSI, HUG/CHUV, sorties d'hospitalisation) + Planches anatomiques et courbes physiologiques annotées intégrées.</p>
      <p><strong>Contenu :</strong> 50 captures réelles haute résolution couvrant l'Accueil Arène, la Veille 2027, les 4 onglets G/S/F/O, les 3 types de QCM interactifs, le chronomètre, le panoramique des causes et les pages complètes « Réponses » avec illustrations médicales.</p>
    </div>
    ${cards}
  </body></html>`;

  fs.writeFileSync(GALLERY_HTML, html);
  console.log('Compiling PDF via Chromium --print-to-pdf...');
  const pdfProc = spawn('/usr/bin/chromium', [
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    `--print-to-pdf=${PDF_OUT}`,
    '--no-pdf-header-footer',
    `file://${GALLERY_HTML}`
  ], { stdio: 'inherit' });

  await new Promise((res, rej) => pdfProc.on('exit', (code) => code === 0 ? res() : rej(new Error('PDF failed: ' + code))));
  console.log('PDF created:', PDF_OUT, 'size:', fs.statSync(PDF_OUT).size);
  fs.rmSync(OUT_SHOTS, { recursive: true, force: true });
  fs.rmSync(GALLERY_HTML, { force: true });
}

run().catch((err) => { console.error(err); process.exit(1); });

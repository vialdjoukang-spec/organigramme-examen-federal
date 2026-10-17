# Contrôles de la sauvegarde (Atlas avec Janus, 17.10.2026) : export, effacement, import, refus, annulation, stockage plein, mobile.
# Variables : APP_FILE, CHROME_PATH, SHOTS_DIR. Sortie : JSON {contrôle: booléen, …, "errors": [...]}.
import asyncio, json, os, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.abspath(os.environ.get('APP_FILE', os.path.join(ROOT, 'app_v2.html')))
SHOTS = os.environ.get('SHOTS_DIR', os.path.join(ROOT, 'qa', 'shots'))
os.makedirs(SHOTS, exist_ok=True)
CHROME = os.environ.get('CHROME_PATH') or None
LAUNCH = dict(args=['--no-sandbox'], **({'executable_path': CHROME} if CHROME else {}))
from playwright.async_api import async_playwright

SNAP = "(()=>{const o={};for(let i=0;i<localStorage.length;i++){const k=localStorage.key(i);if(k.startsWith('orga-')&&k!=='orga-bak')o[k]=localStorage.getItem(k)}return o})()"
SEED = """(()=>{const id='t'+Date.now();S.seances[id]={date:iso(new Date()),start:480,dur:60,ssp:SSP[0][0],act:'lecture',done:true,score:4,qcm:80,note:'essai « aller-retour »',maj:new Date().toISOString()};
 S.exi={...S.exi,essai:true};local(true);const n=nGet(SSP[1][0]);n.m={d0:3};lsSet('orga-not',JSON.stringify(NS));
 CSLOG.x1={date:iso(new Date()),ssp:[SSP[2][0]],task:'a',asm:70,kk:[3,4,3,4],note:''};lsSet('orga-cs',JSON.stringify(CSLOG));return true})()"""


async def boot(pg):
    await pg.goto('file://' + APP); await pg.wait_for_timeout(2000)


async def main():
    out, errs = {}, []
    tmp = tempfile.mkdtemp()
    async with async_playwright() as p:
        b = await p.chromium.launch(**LAUNCH)
        c = await b.new_context(viewport={'width': 1366, 'height': 860}, accept_downloads=True)
        pg = await c.new_page(); pg.on('pageerror', lambda e: errs.append(str(e)))
        await boot(pg)
        out['rappel_sans_export'] = await pg.evaluate("bak.className.includes('warn')&&/jamais export/.test($('#bak-t').textContent)")
        # Progression réelle : séance, exigence, notion, simulation CS, puis deux gestes cochés dans l’interface.
        await pg.evaluate(SEED)
        await pg.locator('.tab[data-v=ges]').click(); await pg.wait_for_timeout(300)
        boxes = pg.locator('#g-list input[data-g]')
        for i in range(2):
            await boxes.nth(i).check()
        await pg.locator('.tab[data-v=exi]').click()
        await boot(pg)
        before = await pg.evaluate(SNAP)
        async with pg.expect_download() as d:
            await pg.locator('#bak-x').click()
        dl = await d.value; path = os.path.join(tmp, dl.suggested_filename); await dl.save_as(path)
        f = json.load(open(path, encoding='utf-8'))
        out['export_format_versionne'] = (f.get('format') == 'organigramme-examen-federal' and f.get('version') == 1
                                          and dl.suggested_filename.startswith('organigramme-progression-'))
        out['export_contient_tout'] = f.get('cles') == before and len(before) >= 5
        out['rappel_apres_export'] = await pg.evaluate("!bak.className.includes('warn')&&!!localStorage.getItem('orga-bak')")
        # Effacement complet, comme Safari après sept jours : WebKit efface aussi IndexedDB (copie de secours d’Hermès).
        await pg.evaluate("localStorage.clear();indexedDB.deleteDatabase('orga-sauvegarde')"); await boot(pg)
        out['effacement_vide'] = await pg.evaluate("Object.keys(GS).length===0&&!localStorage.getItem('orga-bak')")
        # Refus d’un fichier étranger : rien ne change.
        bad = os.path.join(tmp, 'autre.json'); json.dump({'format': 'autre', 'version': 1, 'cles': {'x': '1'}}, open(bad, 'w'))
        snap0 = await pg.evaluate(SNAP)
        await pg.set_input_files('#bak-f', bad); await pg.wait_for_timeout(300)
        out['import_refuse_fichier_etranger'] = await pg.evaluate("!$('#bak-m').hidden&&$('#bak-m').classList.contains('bad')&&$('#bak-pv').hidden") and await pg.evaluate(SNAP) == snap0
        # Aperçu puis annulation : rien ne change.
        await pg.set_input_files('#bak-f', path); await pg.wait_for_timeout(300)
        out['apercu_avant_ecrasement'] = await pg.evaluate("!$('#bak-pv').hidden&&/2 gestes cochés/.test($('#bak-pv').textContent)") and await pg.evaluate(SNAP) == snap0
        await pg.locator('#bak-no').click()
        out['annulation_sans_effet'] = await pg.evaluate("$('#bak-pv').hidden") and await pg.evaluate(SNAP) == snap0
        # Import confirmé : la page se recharge et l’état est identique.
        await pg.set_input_files('#bak-f', path); await pg.wait_for_timeout(300)
        async with pg.expect_navigation():
            await pg.locator('#bak-ok').click()
        await pg.wait_for_timeout(2000)
        after = await pg.evaluate(SNAP)
        out['aller_retour_identique'] = after == before
        out['etat_restitue_dans_l_interface'] = await pg.evaluate("Object.keys(GS).length===2&&Object.keys(S.seances).length>=1&&S.exi.essai===true&&!!$('#bak-m').textContent")
        # Stockage plein : l’écriture échoue et le message devient visible.
        await pg.evaluate("""(()=>{let n=0,sz=1<<20;while(sz>=1){try{localStorage.setItem('zz-'+(n++),'x'.repeat(sz))}catch(e){sz=sz>>1}}})()""")
        await pg.evaluate("S.params.essai='y'.repeat(4000);local(true)")
        out['stockage_plein_message_visible'] = await pg.evaluate("bak.className.includes('bad')&&/échoué/.test($('#bak-t').textContent)&&/Non enregistré/.test($('#sync').textContent)")
        await pg.screenshot(path=SHOTS + '/export_stockage_plein.png')
        await pg.evaluate("Object.keys(localStorage).filter(k=>k.startsWith('zz-')).forEach(k=>localStorage.removeItem(k));delete S.params.essai;local(true)")
        out['stockage_libere_message_retire'] = await pg.evaluate("!bak.className.includes('bad')")
        await c.close()
        # Mobile : le bandeau tient dans l’écran et ses boutons sont assez grands (WCAG 2.5.8).
        c = await b.new_context(**p.devices['Pixel 7']); pg = await c.new_page(); pg.on('pageerror', lambda e: errs.append(str(e)))
        await boot(pg)
        out['mobile_bandeau_lisible'] = await pg.evaluate("(()=>{const r=bak.getBoundingClientRect(),x=$('#bak-x').getBoundingClientRect();return r.width>0&&r.right<=innerWidth+1&&document.documentElement.scrollWidth<=innerWidth+1&&x.height>=24&&x.width>=24&&$('#bak-i').getBoundingClientRect().right<=r.right+1})()")
        await pg.screenshot(path=SHOTS + '/export_mobile.png')
        await b.close()
    out['errors'] = errs
    print(json.dumps(out, indent=1, ensure_ascii=False))

asyncio.run(main())

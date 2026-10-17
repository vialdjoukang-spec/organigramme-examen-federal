# Contrôles d’Hermès (NC-0, 17.10.2026) : lieur du glossaire gloLink, pile de fenêtres imbriquées (5 niveaux, « ← Retour »,
# fil d’Ariane, sans cycle), types CK (glo, syn, hyp, loc, nc), couches, vues et tour des schémas, repli <img>, clavier,
# souris et toucher (Pixel 7), aucun texte coupé dans la fenêtre, aucune erreur de console.
# Données : fixture tests/fixtures/ck/glo_fixture.json (jamais publiée dans l’application). Janus tient tests/test_ck.py
# (données, schémas, gardes) ; ce fichier couvre seulement l’interface.
# Variables : APP_FILE, APP_URL, CHROME_PATH. Sortie : JSON {contrôle: booléen, …, "errors": [...]}.
import asyncio, json, os, re
from playwright.async_api import async_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.abspath(os.environ.get('APP_FILE', os.path.join(ROOT, 'app_v2.html')))
URL = os.environ.get('APP_URL') or 'file://' + APP
CHROME = os.environ.get('CHROME_PATH') or None
LAUNCH = dict(args=['--no-sandbox'], **({'executable_path': CHROME} if CHROME else {}))
FIX = json.load(open(os.path.join(ROOT, 'tests', 'fixtures', 'ck', 'glo_fixture.json'), encoding='utf-8'))
INIT = ''.join(f'window.CK_{k}={json.dumps(v, ensure_ascii=False)};' for k, v in FIX.items() if not k.startswith('_'))
CLIP_JS = re.search(r'CLIP_JS = r"""(.*?)"""', open(os.path.join(ROOT, 'tests', 'visuel', 'capture.py'), encoding='utf-8').read(), re.S).group(1)
CLIP_TIP = '()=>(' + CLIP_JS + ')().filter(x=>x.el&&document.querySelector("#tip"))'
PAGE = ('<section id="fx-ck" class="card"><p id="fx1">Le faciès cushingoïde se recherche à l’inspection ; un faciès cushingoïde cité deux fois reste relié une fois.</p>'
        '<p id="fx3">facies cushingoide sans accents</p><p id="fx4">Un AVC brutal ; le mot avc en minuscules.</p>'
        '<h3 id="fx5">Faciès cushingoïde</h3><p><button type="button" id="fx6">Faciès cushingoïde</button></p>'
        '<p id="fx2"><span class="tw" id="t-loc" data-t="loc|neuro-nc|A" tabindex="0" role="button">Synthèse locale</span> · '
        '<span class="tw" id="t-nc" data-t="nc|ncT|face" tabindex="0" role="button">Schéma de test</span> · '
        '<span class="tw" id="t-nc99" data-t="nc|nc99|face" tabindex="0" role="button">Schéma sans fichier JS</span></p><label class="gr" id="fx7" data-t="g|thorax|0"><input type="checkbox" id="fx7c"><p>Recherche d’un purpura.</p></label></section>')
K = "(window.tipK||tipK)"


async def profile(b, mobile, out, errs):
    pre = 'mobile_' if mobile else ''
    c = await b.new_context(**(dict(b._pw.devices['Pixel 7']) if mobile else dict(viewport={'width': 1366, 'height': 900})))
    await c.add_init_script(INIT)
    pg = await c.new_page()
    pg.on('pageerror', lambda e: errs.append(pre + str(e)))
    pg.on('console', lambda m: errs.append(pre + m.text) if m.type == 'error' and 'absent.js' not in m.text and 'ERR_FILE_NOT_FOUND' not in m.text else None)
    await pg.goto(URL); await pg.wait_for_timeout(1500)
    await pg.evaluate("h=>{document.querySelector('.w').insertAdjacentHTML('afterbegin',h);scrollTo(0,0)}", PAGE)
    await pg.wait_for_timeout(900)
    tap = (lambda s: pg.locator(s).first.tap()) if mobile else (lambda s: pg.locator(s).first.click())
    ev = pg.evaluate
    # Lieur sur la page.
    out[pre + 'lieur_page_premiere_occurrence'] = await ev("$$('#fx1 .glo[data-t=\"glo|facies-cushingoide\"]').length===1")
    out[pre + 'lieur_sans_accent'] = await ev("!!$('#fx3 .glo[data-t=\"glo|facies-cushingoide\"]')")
    out[pre + 'lieur_abreviation_casse'] = await ev("(()=>{const L=$$('#fx4 .glo');return L.length===1&&L[0].textContent==='AVC'})()")
    out[pre + 'lieur_exclusions'] = await ev("!$('#fx5 .glo')&&!$('#fx6 .glo')&&!$('#grid .glo')&&!$('.tabs .glo')")
    out[pre + 'index_atlas'] = await ev("(()=>{const o=window.CK_GLO_IDX;window.CK_GLO_IDX={f:[['Faciès cushingoïde','facies-cushingoide']],a:[['AVC','avc']]};const I=gloIndex();"
                                         "const ok=!!I&&I.mF.get('facies cushingoide')==='facies-cushingoide'&&I.mA.get('AVC')==='avc'&&I.mF.size===1;window.CK_GLO_IDX=o;gloI=null;gloIndex();return ok})()")
    # Survol (ordinateur) puis clic qui épingle.
    if not mobile:
        await pg.hover('#fx1 .glo'); await pg.wait_for_timeout(450)
        out['survol_ouvre'] = await ev(f"!$('#tip').hidden&&{K}==='glo|facies-cushingoide'&&!tipPin")
    await tap('#fx1 .glo'); await pg.wait_for_timeout(250)
    out[pre + 'clic_epingle'] = await ev(f"!$('#tip').hidden&&tipPin&&{K}==='glo|facies-cushingoide'&&$('#tip').getAttribute('role')==='dialog'")
    if mobile:
        out['mobile_panneau_bas'] = await ev("(()=>{const r=$('#tip').getBoundingClientRect();return r.bottom>=innerHeight-24&&r.width>=innerWidth-24})()")
    # Pile : niveaux 2 à 5, sans cycle, puis plus aucun lien au niveau 5.
    await tap('#tip .ck-b [data-t="glo|plethore-faciale"]'); await pg.wait_for_timeout(200)
    out[pre + 'niveau2_fil_retour'] = await ev(f"{K}==='glo|plethore-faciale'&&tipStk.length===1&&!!$('#tip .bk')&&$('#tip .ck-fil').textContent.includes('Faciès cushingoïde ›')&&$('#tip .h').textContent.includes('niveau 2')")
    out[pre + 'sans_cycle'] = await ev("!$('#tip .ck-b [data-t=\"glo|facies-cushingoide\"]')&&$('#tip .ck-b').textContent.includes('faciès cushingoïde')")
    for t in ['erythrose', 'vitropression', 'purpura']:
        await tap(f'#tip .ck-b [data-t="glo|{t}"]'); await pg.wait_for_timeout(200)
    out[pre + 'niveau5_sans_lien'] = await ev(f"{K}==='glo|purpura'&&tipStk.length===4&&!$('#tip .ck-b [data-t]')&&$('#tip .ck-b').textContent.includes('extravasation')")
    out[pre + 'texte_coupe_fenetre'] = len(await ev(CLIP_TIP)) == 0
    await tap('#tip .bk'); await pg.wait_for_timeout(200)
    out[pre + 'retour'] = await ev(f"{K}==='glo|vitropression'&&tipStk.length===3")
    await tap('#tip [data-lv="0"]'); await pg.wait_for_timeout(200)
    out[pre + 'fil_ariane'] = await ev(f"{K}==='glo|facies-cushingoide'&&tipStk.length===0&&!$('#tip .bk')")
    await ev("hideTip(true)")
    # Corps d’une fenêtre historique (Fiche éclair) : rattrapage sans toucher aux données.
    await ev("showTip(document.querySelector('.it[data-c=\"G1\"]'),true)"); await pg.wait_for_timeout(150)
    out[pre + 'rattrapage_fenetre_existante'] = await ev("!!$('#tip .ck-b .glo[data-t=\"glo|hyperhidrose\"]')&&!TIP.G1.c[0].includes('data-t')&&!!$('#tip .glo').title")
    await ev("hideTip(true)")
    # Terme dans un geste cochable (label[data-t]) : ouvre le terme, ne coche pas.
    await tap('#fx7 .glo'); await pg.wait_for_timeout(200)
    out[pre + 'lien_dans_geste'] = await ev(f"{K}==='glo|purpura'&&!$('#fx7c').checked")
    await ev("hideTip(true)")
    # Synthèse locale (onglets A et B), chaîne hypothèse → exploration → prise en charge.
    await tap('#t-loc'); await pg.wait_for_timeout(200)
    ok = await ev("$('#ck-tab-A').getAttribute('aria-selected')==='true'&&!!$('#tip .ck-b [data-t=\"syn|pf-peripherique\"]')")
    await tap('#ck-tab-B'); await pg.wait_for_timeout(200)
    out[pre + 'synthese_onglets'] = ok and await ev(f"{K}==='loc|neuro-nc|B'&&tipStk.length===0&&$('#ck-tab-B').getAttribute('aria-selected')==='true'&&document.activeElement===$('#ck-tab-B')")
    await tap('#tip .ck-b [data-t="hyp|bell"]'); await pg.wait_for_timeout(200)
    ok = await ev(f"{K}==='hyp|bell'&&$('#tip .ck-b').textContent.includes('1re intention')&&$('#tip .ck-b').textContent.includes('2e intention')")
    await tap('#tip .ck-b [data-t="hyp|bell|pec"]'); await pg.wait_for_timeout(200)
    out[pre + 'chaine_hypothese'] = ok and await ev(f"{K}==='hyp|bell|pec'&&tipStk.length===2&&$('#tip .ck-b').textContent.includes('Dose suisse (AIPS) : À vérifier')"
                                                   "&&tipFor('hyp|avc-ischemique').h.includes('ck-urg')&&tipFor('syn|pf-peripherique').h.includes('glo|lagophtalmie')")
    await ev("hideTip(true)")
    # Schéma : SVG chargé à la demande (ncT.js), couches, vues, tour ; repli <img> sans fichier JS.
    await tap('#t-nc'); await pg.wait_for_timeout(600)
    ok = await ev("!!$('#tip .ck-fig svg')&&[...$$('#tip input[data-ck=cou]')].every(i=>!i.disabled&&i.checked)&&$$('#tip input[data-ck=cou]').length===7")
    await tap('#tip input[value=nerf]'); await pg.wait_for_timeout(100)
    out[pre + 'schema_couches'] = ok and await ev("$('#tip .ck-fig #nerf').style.display==='none'&&$('#tip .ck-fig #trait').style.display===''")
    await tap('#tip [data-k="nc|ncT|profil"]'); await pg.wait_for_timeout(200)
    out[pre + 'schema_vues'] = await ev(f"{K}==='nc|ncT|profil'&&$('#tip [data-k=\"nc|ncT|profil\"]').getAttribute('aria-pressed')==='true'&&$('#tip .ck-fig svg title').textContent.includes('profil')&&$('#tip .ck-fig #nerf').style.display==='none'")
    await tap('#tip [data-k="nc|ncT|tour"]'); await pg.wait_for_timeout(200)
    await pg.focus('#tip .ck-tour'); await pg.keyboard.press('ArrowRight'); await pg.keyboard.press('ArrowRight')
    ok = await ev("$('#tip .ck-tour').getAttribute('aria-valuenow')==='2'&&$('#tip .ck-couches').disabled")
    if not mobile:
        bx = await pg.locator('#tip .ck-tour').bounding_box()
        await pg.mouse.move(bx['x'] + 20, bx['y'] + 20); await pg.mouse.down(); await pg.mouse.move(bx['x'] + 110, bx['y'] + 20, steps=6); await pg.mouse.up()
        ok = ok and await ev("$('#tip .ck-tour').getAttribute('aria-valuenow')==='4'")
    out[pre + 'schema_tour'] = ok
    await ev("hideTip(true)")
    await tap('#t-nc99'); await pg.wait_for_timeout(700)
    out[pre + 'schema_repli_img'] = await ev("!!$('#tip .ck-fig img')&&!$('#tip .ck-fig svg')&&$('#tip .ck-couches').disabled")
    out[pre + 'texte_coupe_schema'] = len(await ev(CLIP_TIP)) == 0
    await ev("hideTip(true)")
    # Clavier : Entrée ouvre et épingle, Entrée dans la fenêtre empile, Échap ferme et rend le focus.
    await pg.focus('#fx1 .glo'); await pg.keyboard.press('Enter'); await pg.wait_for_timeout(200)
    ok = await ev(f"tipPin&&{K}==='glo|facies-cushingoide'&&$('#tip').contains(document.activeElement)")
    await pg.focus('#tip .ck-b [data-t="glo|plethore-faciale"]'); await pg.keyboard.press('Enter'); await pg.wait_for_timeout(200)
    ok = ok and await ev(f"{K}==='glo|plethore-faciale'&&document.activeElement===$('#tip .bk')")
    await pg.keyboard.press('Enter'); await pg.wait_for_timeout(200)
    ok = ok and await ev(f"{K}==='glo|facies-cushingoide'&&tipStk.length===0")
    await pg.keyboard.press('Escape'); await pg.wait_for_timeout(150)
    out[pre + 'clavier'] = ok and await ev("$('#tip').hidden&&document.activeElement===$('#fx1 .glo')")
    await c.close()


async def main():
    out, errs = {}, []
    async with async_playwright() as p:
        b = await p.chromium.launch(**LAUNCH); b._pw = p
        await profile(b, False, out, errs)
        await profile(b, True, out, errs)
        await b.close()
    out['sans_erreur_console'] = not errs
    out['errors'] = errs
    print(json.dumps(out, ensure_ascii=False))


if __name__ == '__main__':
    asyncio.run(main())

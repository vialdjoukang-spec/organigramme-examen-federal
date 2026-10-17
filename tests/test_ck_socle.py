# Atlas · chargement différé des données CK (patch 0011) : file:// sans réseau, index du glossaire à l'inactivité,
# autres fichiers au premier besoin, une seule balise <script> par fichier, échec propre si un fichier manque.
# Sortie : JSON de contrôles booléens + 'errors'. Variables : APP_FILE, CHROME_PATH.
import asyncio, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.abspath(os.environ.get('APP_FILE', os.path.join(ROOT, 'app_v2.html')))
CHROME = os.environ.get('CHROME_PATH') or None
from playwright.async_api import async_playwright


async def main():
    out, errs, cons = {}, [], []
    src = open(APP, encoding='utf-8').read()
    out['aucune_donnee_ck_dans_app'] = 'window.CK_' not in src and 'CK_GLO_INDEX=' not in src
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--no-sandbox'], **({'executable_path': CHROME} if CHROME else {}))
        ctx = await b.new_context(viewport={'width': 1280, 'height': 900})
        await ctx.set_offline(True)
        await ctx.add_init_script("window.__ck=null;document.addEventListener('DOMContentLoaded',()=>{window.__dcl=performance.now()});"
                                  "new MutationObserver((L,o)=>{for(const m of L)for(const n of m.addedNodes)if(n.tagName==='SCRIPT'&&/assets\\/ck\\/glo-index/.test(n.src)){window.__ck=performance.now();o.disconnect()}})"
                                  ".observe(document,{childList:true,subtree:true})")
        fails = []
        pg = await ctx.new_page()
        pg.on('requestfailed', lambda r: fails.append(r.url))
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.on('console', lambda m: m.type == 'error' and cons.append(m.text))
        await pg.goto('file://' + APP)
        try:
            await pg.wait_for_function('window.CK_GLO_INDEX&&Array.isArray(window.CK_GLO_INDEX.e)', timeout=8000)
            out['index_glossaire_charge_hors_ligne'] = True
        except Exception:
            out['index_glossaire_charge_hors_ligne'] = False
        out['index_apres_DOMContentLoaded'] = await pg.evaluate("window.__ck!==null&&window.__dcl!==undefined&&window.__ck>=window.__dcl")
        out['autres_fichiers_pas_encore_charges'] = await pg.evaluate(
            "!document.querySelector('script[src=\"assets/ck/syn.js\"]')&&!window.CK_SYN")
        out['meme_promesse_pendant_chargement'] = await pg.evaluate("(()=>{const a=ckLoad('hyp'),b=ckLoad('hyp');return a===b})()")
        out['charge_au_premier_besoin'] = await pg.evaluate(
            "Promise.all(['syn','hyp','nc','loc','src','doses_ch'].map(ckLoad)).then(L=>L.every(x=>x&&typeof x==='object'))")
        out['une_balise_par_fichier'] = await pg.evaluate(
            "ckLoad('glo-index').then(()=>ckLoad('syn')).then(()=>['glo-index','syn','hyp'].every(n=>document.querySelectorAll('script[src=\"assets/ck/'+n+'.js\"]').length===1))")
        out['tranche_glossaire_par_lettre'] = await pg.evaluate(
            "(window.CK_GLO_Z={'zz-test':{id:'zz-test'}},ckGlo('zz-test').then(e=>e&&e.id==='zz-test'))")
        out['aucun_echec_assets_ck'] = not [u for u in fails if '/assets/ck/' in u]
        out['console_sans_erreur'] = not [c for c in cons if not c.startswith('Failed to load resource')]
        out['fichier_absent_rejete_proprement'] = await pg.evaluate(
            "ckLoad('inexistant').then(()=>false,()=>!document.querySelector('script[src=\"assets/ck/inexistant.js\"]')&&(()=>{const q=ckLoad('inexistant');q.catch(()=>{});return q instanceof Promise})())")
        await pg.wait_for_timeout(200)
        out['tip_historique_intact'] = await pg.evaluate("typeof tipFor==='function'&&typeof showTip==='function'&&typeof hideTip==='function'")
        await b.close()
    out['errors'] = errs
    print(json.dumps(out, ensure_ascii=False))


asyncio.run(main())

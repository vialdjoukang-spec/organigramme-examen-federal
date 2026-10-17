#!/usr/bin/env python3
"""Automate Iris · capture : captures, débordement, polices, décalage de mise en page, axe-core.

Usage : python tests/visuel/capture.py [--sortie qa/visuel/out] [--variantes clair,dore] [--profils mobile]
Variables : APP_FILE, CHROME_PATH, AXE_JS (défaut .cache/axe.min.js).
Sortie : <sortie>/actuel/<variante>_<profil>_<onglet>.png et <sortie>/mesures.json.
L'horloge est figée (config.json) pour que les dates affichées ne changent pas d'un jour à l'autre.
"""
import argparse, datetime, json, os, sys, time
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CFG = json.load(open(os.path.join(ROOT, 'qa', 'visuel', 'config.json'), encoding='utf-8'))
APP = os.path.abspath(os.environ.get('APP_FILE', os.path.join(ROOT, 'app_v2.html')))
AXE = os.environ.get('AXE_JS', os.path.join(ROOT, '.cache', 'axe.min.js'))
CHROME = os.environ.get('CHROME_PATH') or None
LAUNCH = dict(args=['--no-sandbox', '--font-render-hinting=none', '--disable-lcd-text'],
              **({'executable_path': CHROME} if CHROME else {}))

# Le décalage de mise en page se mesure dès le premier octet, avant tout script de l'application.
CLS_INIT = """window.__cls=0;window.__clsN=0;try{new PerformanceObserver(l=>{for(const e of l.getEntries())
{if(!e.hadRecentInput){window.__cls+=e.value;window.__clsN++}}}).observe({type:'layout-shift',buffered:true})}catch(e){}"""

# Débordement horizontal : la page ne doit jamais défiler en largeur ; on nomme les éléments fautifs
# qui ne sont pas contenus dans un conteneur à défilement horizontal volontaire.
OVERFLOW_JS = """()=>{const W=document.documentElement.clientWidth,sw=document.documentElement.scrollWidth;const out=[];
if(sw>W+1){for(const el of document.querySelectorAll('body *')){const r=el.getBoundingClientRect();if(r.width===0||r.right<=W+1)continue;
let p=el.parentElement,clip=false;while(p&&p!==document.body){const o=getComputedStyle(p).overflowX;if(o!=='visible'){clip=true;break}p=p.parentElement}
if(clip||getComputedStyle(el).position==='fixed')continue;out.push((el.tagName.toLowerCase()+(el.id?'#'+el.id:'')+(el.className&&typeof el.className==='string'?'.'+el.className.trim().split(/\\s+/).join('.'):'')).slice(0,80)+' → '+Math.round(r.right)+'px');if(out.length>=8)break}}
return {largeur:W,largeur_defilement:sw,deborde:sw>W+1,fautifs:out}}"""

FONTS_JS = """async()=>{await document.fonts.ready;const f=[...document.fonts].map(x=>({famille:x.family,statut:x.status}));
const css=getComputedStyle(document.body).fontFamily;return {faces:f.length,echecs:f.filter(x=>x.statut==='error').map(x=>x.famille),famille_corps:css}}"""


# Séances de démonstration : deux par jour sur la semaine figée (16–22.11.2026), pour juger les bandes de séance
# sur chaque teinte de jour. Elles vivent seulement dans le stockage local de ce contexte de test.
SEED_JS = """()=>{const D=['2026-11-16','2026-11-17','2026-11-18','2026-11-19','2026-11-20','2026-11-21','2026-11-22'];
const A=['Cours CK','Fondamentaux F′','QCM','Révision'];const S0=JSON.parse(localStorage.getItem('orga-ef')||'{}');S0.seances={};
D.forEach((d,i)=>{for(let j=0;j<2;j++){const c=SSP[(i*31+j*17)%SSP.length][0];S0.seances['iris'+i+j]={date:d,start:7*60+j*120+i*15,dur:j?90:60,ssp:c,act:A[(i+j)%4],done:j===1&&i%2===0,score:0,qcm:null,note:'',maj:''}}});
localStorage.setItem('orga-ef',JSON.stringify(S0));localStorage.setItem('orga-tab','cal')}"""

# Contraste de chaque texte de séance contre le fond réellement peint (couleurs résolues par un canevas).
BLK_CONTRAST_JS = """()=>{const cv=document.createElement('canvas').getContext('2d',{willReadFrequently:true});
const rgb=c=>{cv.clearRect(0,0,1,1);cv.fillStyle='#000';cv.fillStyle=c;cv.fillRect(0,0,1,1);const d=cv.getImageData(0,0,1,1).data;return [d[0],d[1],d[2],d[3]/255]};
const lum=([r,g,b])=>{const f=v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)};return .2126*f(r)+.7152*f(g)+.0722*f(b)};
const over=(t,b)=>[0,1,2].map(i=>t[i]*t[3]+b[i]*(1-t[3]));
const out=[];for(const k of document.querySelectorAll('#grid .blk')){const col=k.closest('.col');let bg=rgb(getComputedStyle(k).backgroundColor);
if(bg[3]<1){const cb=rgb(getComputedStyle(col).backgroundColor);bg=over(bg,cb[3]?cb:[255,255,255,1]).concat(1)}
for(const el of [k.querySelector('b'),k.querySelector('.t'),k.querySelector('.du')]){if(!el)continue;const fg=over(rgb(getComputedStyle(el).color),bg);
const L1=lum(fg),L2=lum(bg),r=(Math.max(L1,L2)+.05)/(Math.min(L1,L2)+.05);out.push({jour:col.dataset.d,el:el.tagName.toLowerCase()+(el.className?'.'+el.className:''),ratio:Math.round(r*100)/100})}}
const days=[...document.querySelectorAll('#grid>.col')].map(c=>getComputedStyle(c).backgroundColor);
return {mesures:out,min:out.length?Math.min(...out.map(x=>x.ratio)):null,teintes_jours:days}}"""


def axe_run(pg):
    return pg.evaluate("""async(tags)=>{const r=await axe.run(document,{runOnly:{type:'tag',values:tags},resultTypes:['violations']});
return r.violations.map(v=>({id:v.id,impact:v.impact,aide:v.help,noeuds:v.nodes.length,exemples:v.nodes.slice(0,3).map(n=>n.target.join(' '))}))}""",
                       CFG['axe']['tags'])


def settle(pg, ms=450):
    pg.wait_for_timeout(ms)
    pg.evaluate("()=>document.fonts.ready")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sortie', default=os.path.join(ROOT, 'qa', 'visuel', 'out'))
    ap.add_argument('--variantes', default=','.join(CFG['variantes']))
    ap.add_argument('--profils', default=','.join(CFG['profils']))
    ap.add_argument('--sans-axe', action='store_true')
    a = ap.parse_args()
    shots = os.path.join(a.sortie, 'actuel')
    os.makedirs(shots, exist_ok=True)
    have_axe = os.path.exists(AXE) and not a.sans_axe
    if not have_axe:
        print('AVERTISSEMENT : axe.min.js absent ; aucun contrôle d’accessibilité.', file=sys.stderr)
    fixed = datetime.datetime.fromisoformat(CFG['horloge_figee'])
    H = CFG['hauteur_max_px']
    M = {'app': os.path.relpath(APP, ROOT), 'horloge': CFG['horloge_figee'], 'captures': {}, 'debordement': {},
         'polices': {}, 'cls': {}, 'axe': {}, 'erreurs_page': {}, 'hors_ligne': {}}
    t0 = time.time()
    with sync_playwright() as p:
        b = p.chromium.launch(**LAUNCH)
        for vn in a.variantes.split(','):
            v = CFG['variantes'][vn]
            for pn in a.profils.split(','):
                pr = CFG['profils'][pn]
                if 'device' in pr:
                    ctxa = dict(p.devices[pr['device']]); ctxa['device_scale_factor'] = pr.get('device_scale_factor', ctxa['device_scale_factor'])
                else:
                    ctxa = {'viewport': {'width': pr['viewport'][0], 'height': pr['viewport'][1]}}
                ctxa.update(color_scheme=v['schema'], reduced_motion='reduce', locale='fr-CH', timezone_id='Europe/Zurich')
                key = f'{vn}_{pn}'
                c = b.new_context(**ctxa)
                c.add_init_script(CLS_INIT)
                pg = c.new_page()
                pg.clock.set_fixed_time(fixed)
                errs, ext = [], []
                pg.on('pageerror', lambda e: errs.append(str(e)[:200]))
                # Toute requête réseau d'une page ouverte en file:// est une dépendance externe.
                pg.on('request', lambda r: ext.append(f'{r.resource_type} {r.url[:100]}') if r.url.startswith('http') else None)
                pg.goto('file://' + APP, wait_until='load')
                settle(pg, 2000)
                M['cls'][key] = round(pg.evaluate('window.__cls'), 4)
                M['polices'][key] = pg.evaluate(FONTS_JS)
                M['polices'][key]['externes'] = sorted({x for x in ext if x.split()[0] in ('font', 'stylesheet')})
                M.setdefault('requetes_externes', {})[key] = sorted(set(ext))
                if v.get('gilt') is not None:
                    pg.evaluate("g=>{const r=document.getElementById('d-gilt');r.value=g;r.dispatchEvent(new Event('input',{bubbles:true}))}", v['gilt'])
                if have_axe:
                    pg.add_script_tag(path=AXE)
                tabs = list(CFG['onglets']) + [e for e in CFG['etats'] if e != 'cal-seances']  # cal-seances : après rechargement
                for t in tabs:
                    tab = 'not' if t == 'not-fenetre' else t
                    loc = pg.locator(f'.tab[data-v={tab}]')
                    (loc.tap() if ctxa.get('has_touch') else loc.click())
                    if tab == 'not':
                        first = pg.locator('#n-list [data-n]').first
                        if first.count():
                            (first.tap() if ctxa.get('has_touch') else first.click())
                    pg.evaluate('()=>{window.scrollTo(0,0);document.activeElement&&document.activeElement.blur&&document.activeElement.blur()}')
                    settle(pg)
                    if t == 'not-fenetre':  # la fenêtre est fixe : on la capture dans la fenêtre visible
                        w = pg.locator('#v-not .nr .tw').first
                        if w.count():
                            (w.tap() if ctxa.get('has_touch') else w.click())
                            settle(pg, 400)
                    pg.mouse.move(0, 0)
                    k = f'{key}_{t}'
                    M['debordement'][k] = pg.evaluate(OVERFLOW_JS)
                    if have_axe and t != 'not-fenetre':
                        M['axe'][k] = axe_run(pg)
                    full = pg.evaluate('()=>document.documentElement.scrollHeight')
                    vw = pg.viewport_size['width']
                    path = os.path.join(shots, k + '.png')
                    if t == 'not-fenetre':
                        pg.screenshot(path=path, animations='disabled', caret='hide')
                    else:
                        pg.screenshot(path=path, full_page=True, animations='disabled', caret='hide',
                                      clip={'x': 0, 'y': 0, 'width': vw, 'height': min(full, H)})
                    M['captures'][k] = os.path.relpath(path, a.sortie)
                    if t == 'not-fenetre':
                        pg.keyboard.press('Escape')
                # État « cal-seances » : séances semées, rechargement, calendrier, contraste des bandes.
                pg.evaluate(SEED_JS); pg.reload(wait_until='load'); settle(pg, 1500)
                if v.get('gilt') is not None:
                    pg.evaluate("g=>{const r=document.getElementById('d-gilt');r.value=g;r.dispatchEvent(new Event('input',{bubbles:true}))}", v['gilt'])
                loc = pg.locator('.tab[data-v=cal]'); (loc.tap() if ctxa.get('has_touch') else loc.click())
                pg.evaluate('()=>{window.scrollTo(0,0);document.activeElement&&document.activeElement.blur&&document.activeElement.blur()}')
                settle(pg)
                k = f'{key}_cal-seances'
                M.setdefault('contraste_seances', {})[k] = pg.evaluate(BLK_CONTRAST_JS)
                if have_axe:
                    pg.add_script_tag(path=AXE); M['axe'][k] = axe_run(pg)
                M['debordement'][k] = pg.evaluate(OVERFLOW_JS)
                path = os.path.join(shots, k + '.png')
                pg.screenshot(path=path, full_page=True, animations='disabled', caret='hide',
                              clip={'x': 0, 'y': 0, 'width': pg.viewport_size['width'], 'height': min(pg.evaluate('()=>document.documentElement.scrollHeight'), H)})
                M['captures'][k] = os.path.relpath(path, a.sortie)
                M['erreurs_page'][key] = errs
                c.close()
        # Rendu sans réseau : toute dépendance externe (CDN de polices, scripts) modifie la capture.
        c = b.new_context(viewport={'width': 1440, 'height': 900}, color_scheme='light', reduced_motion='reduce',
                          locale='fr-CH', timezone_id='Europe/Zurich')
        c.route(lambda u: u.startswith('http'), lambda r: r.abort())
        pg = c.new_page(); pg.clock.set_fixed_time(fixed)
        errs = []; pg.on('pageerror', lambda e: errs.append(str(e)[:200]))
        pg.goto('file://' + APP, wait_until='load'); settle(pg, 2000)
        path = os.path.join(shots, 'hors-ligne_ordinateur_cal.png')
        pg.screenshot(path=path, full_page=True, animations='disabled', caret='hide',
                      clip={'x': 0, 'y': 0, 'width': 1440, 'height': min(pg.evaluate('()=>document.documentElement.scrollHeight'), H)})
        M['hors_ligne'] = {'capture': os.path.relpath(path, a.sortie), 'compare_a': 'actuel/clair_ordinateur_cal.png', 'erreurs_page': errs}
        c.close(); b.close()
    M['duree_s'] = round(time.time() - t0, 1)
    json.dump(M, open(os.path.join(a.sortie, 'mesures.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f"Captures : {len(M['captures'])} en {M['duree_s']} s → {shots}")


if __name__ == '__main__':
    main()

# Contrôles d’Hermès (17.10.2026) : recherche floue, clic et plage pour créer, déplacement et durée (souris, toucher émulé,
# clavier), sauvegarde automatique (statut, miroir IndexedDB, versions, restauration, refus d’une version altérée,
# récupération d’un stockage vide ou endommagé), sans erreur de console.
# Variables : APP_FILE, CHROME_PATH, SHOTS_DIR. Sortie : JSON {contrôle: booléen, …, "errors": [...]}.
import asyncio, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.abspath(os.environ.get('APP_FILE', os.path.join(ROOT, 'app_v2.html')))
URL = os.environ.get('APP_URL') or 'file://' + APP
CHROME = os.environ.get('CHROME_PATH') or None
LAUNCH = dict(args=['--no-sandbox'], **({'executable_path': CHROME} if CHROME else {}))
from playwright.async_api import async_playwright

COL = "(i=>{const c=$$('#grid .col')[i];c.scrollIntoView({block:'start',behavior:'instant'});scrollBy({top:-160,behavior:'instant'});const r=c.getBoundingClientRect();return [r.left+r.width/2,r.top]})"
NSE = "Object.keys(S.seances).length"
ONE = "(()=>{const v=Object.values(S.seances);return v[v.length-1]})()"
WAIT = "new Promise(r=>setTimeout(r,900))"
VERS = "svList().then(L=>L.length)"


def y_of(top, m):
    return top + (m - 360) / 60 * 48 + 6


async def boot(pg):
    await pg.goto(URL); await pg.wait_for_timeout(1800)


async def touch(pg, sel, steps):
    """Envoie des PointerEvent tactiles synthétiques : [(type, x, y, pause_ms), …]."""
    for t, x, y, ms in steps:
        await pg.evaluate("([s,t,x,y])=>{const el=t==='pointerdown'?document.querySelector(s):(document.elementFromPoint(x,y)||document.body);"
                          "el.dispatchEvent(new PointerEvent(t,{pointerType:'touch',pointerId:7,isPrimary:true,clientX:x,clientY:y,bubbles:true,cancelable:true}))}",
                          [sel, t, x, y])
        await pg.wait_for_timeout(ms)


async def profile(b, mobile, out, errs):
    pre = 'mobile_' if mobile else ''
    opts = dict(viewport={'width': 412, 'height': 915}, has_touch=True, is_mobile=True, device_scale_factor=2) if mobile \
        else dict(viewport={'width': 1366, 'height': 900})
    c = await b.new_context(**opts)
    pg = await c.new_page()
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
    await boot(pg)
    ci = 0 if mobile else 1
    # Recherche : accents, code, faute de frappe.
    await pg.fill('#cq', 'dyspnee'); await pg.wait_for_timeout(150)
    out[pre + 'recherche_sans_accent'] = await pg.evaluate("(()=>{const c=$('#cq-r .cq-i')?.dataset.c;return !!c&&norm(BY[c][1]+' '+GROUPES[BY[c][2]]).includes('dyspn')})()")
    code = await pg.evaluate("SSP.find(s=>/\\d/.test(s[0]))[0]")
    await pg.fill('#cq', code.lower()); await pg.wait_for_timeout(150)
    out[pre + 'recherche_par_code'] = await pg.evaluate("c=>$('#cq-r .cq-i')?.dataset.c===c", code)
    word, target = await pg.evaluate("(()=>{for(const s of SSP){const w=norm(s[1]).split(/[^a-z]+/).find(w=>w.length>=8);if(w)return [w,s[0]]}})()")
    typo = word[:3] + ('x' if word[3] != 'x' else 'y') + word[4:]
    await pg.fill('#cq', typo); await pg.wait_for_timeout(150)
    out[pre + 'recherche_floue'] = await pg.evaluate("c=>[...$$('#cq-r .cq-i')].some(l=>l.dataset.c===c)", target)
    # Diagnostic différentiel ou notion : l’exemple de la barre doit trouver des SSP, avec le titre trouvé (patch 0009).
    await pg.fill('#cq', 'Insuffisance cardiaque'); await pg.wait_for_timeout(150)
    out[pre + 'recherche_notion'] = await pg.evaluate("(()=>{const L=[...$$('#cq-r .cq-i')];return L.length>=3&&L.every(l=>{const c=l.dataset.c,t=l.querySelector('small');"
        "return !!t&&norm(t.textContent).includes('insuffisance cardiaque')&&JSON.stringify(NOT[c]).toLowerCase().includes('insuffisance cardiaque')})})()")
    # Placer depuis la recherche, puis cliquer une plage.
    await pg.fill('#cq', code); await pg.wait_for_timeout(150)
    await pg.locator('#cq-r .cq-p').first.click()
    x, top = await pg.evaluate(COL, ci)
    await pg.mouse.click(x, y_of(top, 7 * 60)) if not mobile else await pg.touchscreen.tap(x, y_of(top, 7 * 60))
    await pg.wait_for_timeout(300)
    out[pre + 'recherche_placer'] = await pg.evaluate(f"(()=>{{const x={ONE};return !!x&&x.ssp===%r&&{NSE}===1}})()" % code)
    await pg.evaluate("$('#e-close').click()"); await pg.wait_for_timeout(700)
    # Clic ou toucher sur une plage vide : fenêtre de création rapide.
    x, top = await pg.evaluate(COL, ci)
    if mobile:
        await pg.touchscreen.tap(x, y_of(top, 10 * 60))
    else:
        await pg.mouse.click(x, y_of(top, 10 * 60))
    await pg.wait_for_timeout(250)
    ok = await pg.evaluate("!$('#qp').hidden&&$('#qp-s').value==='10:00'")
    await pg.fill('#qp-q', code); await pg.wait_for_timeout(100)
    await pg.locator('#qp-r .cq-p').first.click(); await pg.wait_for_timeout(250)
    out[pre + 'clic_cree_seance'] = ok and await pg.evaluate(f"(()=>{{const x={ONE};return x.start===600&&{NSE}===2&&$('#qp').hidden}})()")
    if not mobile:
        # Sélection d’une plage à la souris : 12:00 → 13:30.
        x, top = await pg.evaluate(COL, 3)
        await pg.mouse.move(x, y_of(top, 12 * 60)); await pg.mouse.down()
        await pg.mouse.move(x, y_of(top, 12 * 60 + 40), steps=4); await pg.mouse.move(x, y_of(top, 13 * 60 + 20), steps=4)
        await pg.mouse.up(); await pg.wait_for_timeout(250)
        out['plage_glissee'] = await pg.evaluate("!$('#qp').hidden&&$('#qp-s').value==='12:00'&&$('#qp-d').value==='90'")
        await pg.evaluate("$('#qp-no').click()")
        # Déplacement à la souris : séance de 10:00 vers +1 h et le jour suivant.
        sel = "#grid .blk"
        bx = await pg.evaluate("(()=>{const id=Object.entries(S.seances).find(([,x])=>x.start===600)[0],b=$('#grid .blk[data-id=\"'+id+'\"]');b.scrollIntoView({block:'center',behavior:'instant'});const r=b.getBoundingClientRect();return [id,r.left+r.width/2,r.top+8,r.width]})()")
        sid, bx0, by0, bw = bx
        d0 = await pg.evaluate("id=>S.seances[id].date", sid)
        await pg.mouse.move(bx0, by0); await pg.mouse.down()
        await pg.mouse.move(bx0 + bw * 0.5, by0 + 20, steps=4); await pg.mouse.move(bx0 + bw + 6, by0 + 48, steps=6)
        await pg.mouse.up(); await pg.wait_for_timeout(300)
        out['deplacement_souris'] = await pg.evaluate("([id,d0])=>{const x=S.seances[id];return x.start===660&&x.date>d0&&$('#edit').classList.contains('on')===false}", [sid, d0])
        # Redimensionnement par le bord inférieur : +30 min.
        r = await pg.evaluate("id=>{const z=$('#grid .blk[data-id=\"'+id+'\"] .rz');z.scrollIntoView({block:'center',behavior:'instant'});const r=z.getBoundingClientRect();return [r.left+r.width/2,r.top+4]}", sid)
        dur0 = await pg.evaluate("id=>S.seances[id].dur", sid)
        await pg.mouse.move(*r); await pg.mouse.down(); await pg.mouse.move(r[0], r[1] + 12, steps=3); await pg.mouse.move(r[0], r[1] + 24, steps=3)
        await pg.mouse.up(); await pg.wait_for_timeout(300)
        out['redimension_souris'] = await pg.evaluate("([id,d])=>S.seances[id].dur===d+30", [sid, dur0])
        # Clavier : ↓ = +15 min, Maj+↓ = +15 min de durée, → = jour suivant.
        await pg.evaluate("id=>$('#grid .blk[data-id=\"'+id+'\"]').focus()", sid)
        st = await pg.evaluate("id=>({...S.seances[id]})", sid)
        await pg.keyboard.press('ArrowDown'); await pg.keyboard.press('Shift+ArrowDown'); await pg.keyboard.press('ArrowRight')
        await pg.wait_for_timeout(200)
        out['clavier_deplace_redimensionne'] = await pg.evaluate("([id,s])=>{const x=S.seances[id],d=parse(s.date);d.setDate(d.getDate()+1);return x.start===s.start+15&&x.dur===s.dur+15&&x.date===iso(d)&&document.activeElement?.dataset.id===id}", [sid, st])
    else:
        # Toucher émulé : maintien 400 ms puis glissement d’une heure ; puis bord inférieur +30 min.
        sid = await pg.evaluate("Object.entries(S.seances).find(([,x])=>x.start===600)[0]")
        r = await pg.evaluate("id=>{const b=$('#grid .blk[data-id=\"'+id+'\"]');b.scrollIntoView({block:'center',behavior:'instant'});const r=b.getBoundingClientRect();return [r.left+r.width/2,r.top+8]}", sid)
        s = f'#grid .blk[data-id="{sid}"]'
        await touch(pg, s, [('pointerdown', r[0], r[1], 420), ('pointermove', r[0], r[1] + 20, 30), ('pointermove', r[0], r[1] + 48, 30), ('pointerup', r[0], r[1] + 48, 300)])
        out['mobile_deplacement_toucher'] = await pg.evaluate("id=>S.seances[id].start===660", sid)
        r = await pg.evaluate("id=>{const z=$('#grid .blk[data-id=\"'+id+'\"] .rz');const r=z.getBoundingClientRect();return [r.left+r.width/2,r.top+4]}", sid)
        await touch(pg, s + ' .rz', [('pointerdown', r[0], r[1], 30), ('pointermove', r[0], r[1] + 12, 30), ('pointermove', r[0], r[1] + 24, 30), ('pointerup', r[0], r[1] + 24, 300)])
        out['mobile_redimension_toucher'] = await pg.evaluate("id=>S.seances[id].dur===90", sid)
        # Un glissement sans maintien fait défiler et ne déplace rien.
        r = await pg.evaluate("id=>{const b=$('#grid .blk[data-id=\"'+id+'\"]');const r=b.getBoundingClientRect();return [r.left+r.width/2,r.top+8]}", sid)
        await touch(pg, s, [('pointerdown', r[0], r[1], 20), ('pointermove', r[0], r[1] + 60, 30), ('pointerup', r[0], r[1] + 60, 200)])
        out['mobile_glisser_sans_maintien_defile'] = await pg.evaluate("id=>S.seances[id].start===660", sid)
    # Sauvegarde automatique : statut, miroir, version.
    await pg.evaluate(WAIT)
    out[pre + 'statut_enregistre'] = await pg.evaluate("/^Enregistré à \\d\\d:\\d\\d$/.test($('#sync').textContent)")
    out[pre + 'miroir_indexeddb'] = await pg.evaluate("svGet('cur').then(r=>svOk(r)&&JSON.parse(r.cles['orga-ef']).seances&&Object.keys(JSON.parse(r.cles['orga-ef']).seances).length===%s)" % await pg.evaluate(NSE))
    out[pre + 'persistance_affichee'] = await pg.evaluate("$('#sv-s').textContent.length>20")
    # Bandes de séance (patch 0010) : 15 à 120 min, aucun texte coupé sans « … » ; texte complet dans la fenêtre.
    await pg.evaluate("""(()=>{const k=iso(new Date()),L=SSP.slice().sort((a,b)=>b[1].length-a[1].length);[15,30,45,60,90,120].forEach((u,j)=>{
      S.seances['bd'+j]={date:k,start:13*60+j*120>H1*60-u?6*60+j*15:13*60+j*120,dur:u,ssp:L[j][0],act:'Cours CK',done:false,score:0,qcm:null,note:'',maj:''}});renderGrid()})()""")
    await pg.wait_for_timeout(200)
    out[pre + 'bandes_sans_coupure'] = await pg.evaluate("""(()=>{const B=[...$$('#grid .blk')].filter(k=>k.dataset.id.startsWith('bd'));if(B.length<1)return false;
      return B.every(k=>[k,...k.querySelectorAll('b,.t')].every(e=>{const c=getComputedStyle(e),v=e.scrollHeight>e.clientHeight+1,h=e.scrollWidth>e.clientWidth+1;
      if(!v&&!h)return true;return (parseInt(c.webkitLineClamp)>0||c.textOverflow==='ellipsis')&&!!e.closest('[data-t]')}))
      &&B.every(k=>{const x=tipFor(k.dataset.t);return x&&x.h.includes(esc(BY[S.seances[k.dataset.id].ssp][1]))&&x.h.includes(S.seances[k.dataset.id].dur+'′')})})()""")
    await pg.evaluate("(()=>{for(const j of [0,1,2,3,4,5])delete S.seances['bd'+j];renderGrid()})()")
    out[pre + 'fichier_auto_degrade'] = await pg.evaluate("$('#sv-fb').hidden===(typeof showSaveFilePicker!=='function')")
    if mobile:
        await c.close(); return
    # Versions : une version existe ; on supprime tout, puis on restaure.
    n_before = await pg.evaluate(NSE)
    out['version_creee'] = await pg.evaluate(VERS) >= 1
    await pg.click('#sv-v'); await pg.wait_for_timeout(200)
    await pg.click('#sv-new'); await pg.wait_for_timeout(300)
    out['version_manuelle'] = await pg.evaluate("svList().then(L=>L[0].kind==='manuel'&&/séances/.test($('#ver').textContent))")
    await pg.evaluate("S.seances={};local(true);renderAll()"); await pg.evaluate(WAIT)
    await pg.locator('#ver [data-r]').first.click(); await pg.locator('#ver [data-ok]').click()
    await pg.wait_for_timeout(2200)
    out['restauration_version'] = await pg.evaluate(f"{NSE}===%d&&/est restaurée/.test($('#bak-m').textContent)" % n_before)
    out['restauration_met_de_cote'] = await pg.evaluate("svList().then(L=>L.some(v=>v.kind==='avant-restauration'&&Object.keys(JSON.parse(v.cles['orga-ef']).seances).length===0))")
    # Une version altérée est refusée.
    await pg.evaluate("svTx('versions','readwrite',o=>{const q=o.openCursor();q.onsuccess=()=>{const c=q.result;if(c){const v=c.value;if(v.kind!=='avant-restauration'){v.cles['orga-ef']='{\"seances\":{}}';c.update(v)}c.continue()}}})")
    await pg.click('#sv-v'); await pg.wait_for_timeout(100)
    if await pg.evaluate("$('#ver').hidden"):
        await pg.click('#sv-v'); await pg.wait_for_timeout(200)
    vid = await pg.evaluate("svList().then(L=>L.find(v=>v.kind!=='avant-restauration').id)")
    await pg.evaluate("id=>svRestore(id)", vid); await pg.wait_for_timeout(300)
    out['version_alteree_refusee'] = await pg.evaluate(f"{NSE}===%d&&/endommagée/.test($('#bak-m').textContent)" % n_before)
    await pg.screenshot(path=os.path.join(os.environ.get('SHOTS_DIR', os.path.join(ROOT, 'qa', 'shots')), 'hermes-versions.png'))
    # Récupération : stockage vidé, puis endommagé.
    await pg.evaluate(WAIT)
    await pg.evaluate("localStorage.clear()"); await boot(pg); await pg.wait_for_timeout(800)
    out['recuperation_stockage_vide'] = await pg.evaluate(f"{NSE}===%d&&/récupérée/.test($('#bak-m').textContent)" % n_before)
    await pg.evaluate(WAIT)
    await pg.evaluate("localStorage.setItem('orga-ef','{endommagé')"); await boot(pg); await pg.wait_for_timeout(800)
    out['recuperation_stockage_endommage'] = await pg.evaluate(f"{NSE}===%d&&/récupérée/.test($('#bak-m').textContent)" % n_before)
    await c.close()


async def main():
    out, errs = {}, []
    os.makedirs(os.environ.get('SHOTS_DIR', os.path.join(ROOT, 'qa', 'shots')), exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(**LAUNCH)
        await profile(b, False, out, errs)
        await profile(b, True, out, errs)
        await b.close()
    out['errors'] = errs
    print(json.dumps(out, ensure_ascii=False))


if __name__ == '__main__':
    asyncio.run(main())

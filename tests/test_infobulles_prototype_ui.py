"""DD monographies and distinct SSP course sections open only on activation."""
import asyncio
import os
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]

async def check(page, touch=False):
    await page.goto((ROOT / 'app_v2.html').as_uri())
    await page.evaluate("""() => {
      const f=document.createElement('div');f.id='prototype-test';
      f.style.cssText='position:fixed;top:10px;left:10px;z-index:99999;background:white';
      f.innerHTML='<button class="tw" data-t="n|G1|d0">Hyperhidrose</button>';
      document.body.appendChild(f);
    }""")
    async def six():
        await page.wait_for_function("""() => !TIPEL.hidden &&
          [...TIPEL.querySelectorAll('.ck-b b')].filter(x=>/^[1-6]\\./.test(x.textContent)).length===6""")
        text = await page.locator('#tip .ck-b').inner_text()
        assert text.index('Examen de référence diagnostique') < text.index('À faire en premier')
        assert text.index('A- But') < text.index('B- Moyens') < text.index('Mesures générales')
        assert text.index('Bilan ordonné') < text.index('1 — À faire en premier') < text.index('2 —')
        assert text.index('B- Moyens') < text.index('Phase 1 —') < text.index('Phase 2 —')
        assert text.count('Examen de référence diagnostique') == 1
        assert text.count('Critères diagnostiques') == 1
        return text

    dd=page.locator('#prototype-test [data-t="n|G1|d0"]')
    if not touch:
        await dd.hover()
        await page.wait_for_timeout(650)
        assert await page.locator('#tip').is_hidden(), 'Hover must not open a monography'
        await page.mouse.move(1,1)
    await dd.tap() if touch else await dd.click()
    await six()
    await page.wait_for_function("document.querySelector('#tip .ck-b .glo')")
    term=page.locator('#tip .ck-b .glo').first
    if not touch:
        await term.hover()
        await page.wait_for_timeout(650)
        assert await page.evaluate('tipStk.length===0'), 'Hover must not open a nested definition'
        assert await term.get_attribute('title') is None, 'No native hover definition'
    await term.tap() if touch else await term.click()
    await page.wait_for_function('tipStk.length===1 && !TIPEL.hidden')
    await page.wait_for_function("!document.querySelector('#tip .ck-b').textContent.includes('Chargement…')")
    assert (await page.locator('#tip .ck-b').inner_text()).strip()
    back=page.locator('#tip .bk')
    await back.tap() if touch else await back.click()
    await six()
    if not touch:
        await page.locator('#tip .pvl .pv[role="button"]').focus()
        await page.keyboard.press('Enter')
        await page.wait_for_function("tipK==='pv|G1|0' && tipStk.length===1")
        await page.locator('#tip .bk').click()
        await six()
    await page.keyboard.press('Escape')

async def check_g2(page, touch=False):
    """Keep the nine revised G2 DD and their ordered six-rubric monographies."""
    await page.keyboard.press('Escape')
    await page.evaluate("""() => {
      document.getElementById('prototype-test').innerHTML =
        ['n|G2|d0','n|G2|d1','n|G2|d2','n|G2|d3','n|G2|d4','n|G2|d5','n|G2|d6','n|G2|d7','n|G2|d8'].map((key,i)=>
          `<button class="tw" id="g2-${i}" data-t="${key}">G2 ${i}</button>`).join('');
    }""")
    for index in range(9):
        target = page.locator(f'#g2-{index}')
        if not touch:
            await target.hover()
            await page.wait_for_timeout(650)
            assert await page.locator('#tip').is_hidden(), f'G2 {index}: hover opened a tip'
        await target.tap() if touch else await target.click()
        await page.wait_for_function("""() => !TIPEL.hidden &&
          [...TIPEL.querySelectorAll('.ck-b b')].filter(x=>/^[1-6]\\./.test(x.textContent)).length===6""")
        text = await page.locator('#tip .ck-b').inner_text()
        assert text.index('Examen de référence diagnostique') < text.index('1 — À faire en premier')
        assert text.index('B- Moyens') < text.index('Phase 1 —') < text.index('Phase 2 —')
        assert text.count('Critères diagnostiques') == 1
        if index == 2:
            assert 'ATRA' in text and 'sans attendre la confirmation génétique' in text
        if index == 3:
            assert 'surveillance' in text.lower() and 'Binet' in text
        if index == 4:
            assert 'primitif' in text and 'histologie' in text
        if index == 5:
            assert 'avant biopsie ou chirurgie' in text and 'ne remplace pas le tissu' in text
        if index == 6:
            assert 'IGRA' in text and 'prouve pas la maladie active' in text
        if index == 7:
            assert 'simultanément' in text and 'second prélèvement' in text
        if index == 8:
            assert 'sans délai' in text and 'LRINEC' in text and 'pas d’IRM préalable systématique' in text
        # A specialised term must open a definition and return to the same monography.
        await page.wait_for_function("document.querySelector('#tip .ck-b .glo')")
        term = page.locator('#tip .ck-b .glo').first
        await term.tap() if touch else await term.click()
        await page.wait_for_function('tipStk.length===1 && !TIPEL.hidden')
        await page.wait_for_function("!document.querySelector('#tip .ck-b').textContent.includes('Chargement…')")
        assert (await page.locator('#tip .ck-b').inner_text()).strip()
        back = page.locator('#tip .bk')
        await back.tap() if touch else await back.click()
        await page.wait_for_function("document.querySelector('#tip .ck-b').textContent.includes('Bilan ordonné')")
        await page.keyboard.press('Escape')
        if not touch:
            await target.focus()
            await page.keyboard.press('Enter')
            await page.wait_for_function("!TIPEL.hidden && document.querySelector('#tip .ck-b').textContent.includes('Bilan ordonné')")
            await page.keyboard.press('Escape')


async def check_courses(page, touch=False):
    """All 248 SSP keep 14 course sections; exercise every G1/G2/G3/G4/G5/G6 section in UI."""
    await page.keyboard.press('Escape')
    # An already loaded SSP monography must never hijack a course or flash summary.
    await page.evaluate(r"""async () => {
      await monoLoad('ssp');
      window.courseExpected = (code, i) => {
        const T=TIP[code], V=T.v && T.v.c && T.v.c[i];
        const x={hd:'L’essentiel pour 100 % des points · '+code,ti:CLIN[i],
          h:i===5?exFmt(T.c[i]):T.c[i]};
        if(V && V[0]==='silence')return {...x,
          h:'<i>Silence volontaire : aucune source vérifiée ne permet ici une information précise. Une information vague vaut moins qu’un silence.</i>',src:''};
        if(V && V[1].length)return {...x,ok:V[0],
          links:V[1].map(id=>T.v.S.find(source=>source.id===id)).filter(Boolean)};
        return {...x,src:(T.s?T.s+' · ':'')+'GLOBALITY, cours SSP '+code+' — '+BY[code][1],pend:true};
      };
      window.summaryExpected = code => ({hd:'Fiche éclair · '+code,ti:BY[code][1],
        h:'<b>Définition</b><br>'+TIP[code].c[0]+'<br><b>Points clés</b><br>'+TIP[code].c[12],
        src:(TIP[code].s?TIP[code].s+' · ':'')+'GLOBALITY'});
      window.tipText = html => {
        const div=document.createElement('div');div.innerHTML=html;
        return div.textContent.replace(/\s+/g,' ').trim();
      };
    }""")
    result = await page.evaluate("""() => {
      const codes=Object.keys(TIP),failures=[];let sections=0;
      if(CLIN.length!==14 || CLIN.some((title,i)=>!title.startsWith((i+1)+'- ') || !title.endsWith(' :')))
        failures.push('Titres ordinaux 1–14 attendus');
      for(const code of codes){
        if(TIP[code].c.length!==14)failures.push(code+': expected 14 course sections');
        for(let i=0;i<14;i++){
          const key='n|'+code+'|c'+i,actual=tipFor(key),expected=courseExpected(code,i);
          sections++;
          if(JSON.stringify(actual)!==JSON.stringify(expected))failures.push(key);
        }
        if(JSON.stringify(tipFor('s|'+code))!==JSON.stringify(summaryExpected(code)))
          failures.push('s|'+code);
      }
      return {codes:codes.length,sections,failures};
    }""")
    assert result == {'codes':248,'sections':3472,'failures':[]}, result

    # Les deux composantes du premier titre ne peuvent être fusionnées en un bloc.
    for code in ('G1','G2','G3','G4','G5','G6'):
        first = await page.evaluate("""code => {
          const el=document.createElement('div');el.innerHTML=TIP[code].c[0];
          return [...el.querySelectorAll(':scope > ul > li > b')].map(x=>x.textContent.trim());
        }""",code)
        assert first == ['Définition :','Sémantique de la plainte :'], (code,first)
        await page.evaluate("""code => {
          document.getElementById('prototype-test').innerHTML =
            ['s|'+code,...Array.from({length:14},(_,i)=>'n|'+code+'|c'+i)]
              .map((key,i)=>`<button class="tw" id="course-${i}" data-t="${key}">${key}</button>`).join('');
        }""",code)
        for index in range(15):
            key = f's|{code}' if index == 0 else f'n|{code}|c{index-1}'
            target=page.locator(f'#course-{index}')
            if not touch:
                await target.hover()
                await page.wait_for_timeout(650)
                assert await page.locator('#tip').is_hidden(), f'{key}: hover opened a tip'
                await page.mouse.move(1,1)
            await target.tap() if touch else await target.click()
            await page.wait_for_function('key => !TIPEL.hidden && tipK===key',arg=key)
            async def correct_section():
                result=await page.evaluate(r"""({code,index}) => {
                  const x=index===0?summaryExpected(code):courseExpected(code,index-1);
                  const body=TIPEL.querySelector('.ck-b'),source=TIPEL.querySelector('.s');
                  const expectedSource=x.links
                    ? '✓ Vérifié · '+(x.ok||'confirmé')+' Sources consultées : '+x.links.map(l=>
                        l.t+' ('+[l.o,l.n,l.a].filter(Boolean).join(', ')+')').join(' · ')
                    : (x.pend?'Contenu GLOBALITY · vérification externe en cours ':'')+'Sources : '+x.src;
                  return {title:TIPEL.querySelector('.t').textContent===x.ti,
                    body:tipText(body.innerHTML)===tipText(x.h),
                    source:source.textContent.replace(/\s+/g,' ').trim()===expectedSource.replace(/\s+/g,' ').trim(),
                    links:!x.links || JSON.stringify([...source.querySelectorAll('a')].map(a=>a.getAttribute('href')))
                      ===JSON.stringify(x.links.filter(l=>l.u).map(l=>l.u)),
                    examination:index!==6 || body.querySelectorAll('.ex-region .ex-region__h').length>=2};
                }""",{'code':code,'index':index})
                assert result == {'title':True,'body':True,'source':True,'links':True,
                                  'examination':True}, (key,result)
            await correct_section()
            if index==6:
                assert await page.locator('#tip .ex-chip').count() >= 1
            await page.keyboard.press('Escape')
            if not touch:
                for activation in ('Enter',' '):
                    await target.focus()
                    await page.keyboard.press(activation)
                    await page.wait_for_function('key => !TIPEL.hidden && tipK===key',arg=key)
                    await correct_section()
                    await page.keyboard.press('Escape')


async def main():
    async with async_playwright() as p:
        kwargs={'args':['--no-sandbox']}
        if os.environ.get('CHROME_PATH'):kwargs['executable_path']=os.environ['CHROME_PATH']
        browser=await p.chromium.launch(**kwargs)
        for touch in (False,True):
            context=await browser.new_context(**(p.devices['Pixel 7'] if touch else {'viewport':{'width':1366,'height':860}}))
            page=await context.new_page()
            errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
            await check(page,touch)
            await check_g2(page,touch)
            await check_courses(page,touch)
            assert not errors, errors
            await context.close()
        await browser.close()
    print('Infobulles : DD G1/G2 six rubriques et chronologies, 14 cours distincts G1/G2/G3/G4/G5/G6, 248 SSP, aucun survol, clic/toucher, clavier, définitions et retour : OK')

if __name__=='__main__':asyncio.run(main())

#!/usr/bin/env python3
"""Même fiche au clic/survol ; classement explicite sans probabilité inventée."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _app import read, write

s = before = read()

def replace(old, new):
    global s
    if new in s:
        return
    if s.count(old) != 1:
        raise SystemExit('Ancrage absent ou ambigu : ' + old[:70])
    s = s.replace(old, new)

old = next(line for line in s.splitlines() if line.startswith('const PV_LEG='))
new = "const PV_LEG='<p class=\"pvleg\">Le pourcentage décrit le cadre indiqué : consultation pour cette plainte ou population générale. Ces deux mesures ne sont pas interchangeables. Les chiffres comparables sont triés par fréquence décroissante ; un ordre qualitatif exige une source et un cadre. « % à vérifier » ne signifie pas zéro et ne prouve aucun rang. Ouvrez le pourcentage pour lire la source et le statut du classement.</p>';"
replace(old, new)

anchor = 'function pvOf(c,i)'
helper = "function pvRankText(c){const cl=((ckW('PREV')||{})[c]||{}).classement;return cl&&cl.etat==='valide'?'Ordre qualitatif documenté dans le cadre indiqué ; une fréquence inconnue reste inconnue.':'Classement qualitatif non établi : l’ordre des valeurs inconnues reste celui de la rédaction et ne démontre pas leur probabilité.'}\n"
if helper not in s:
    replace(anchor, helper + anchor)

replace('chaque pourcentage reste <b>à vérifier</b>, et l’ordre suit encore la rédaction d’origine.',
        'chaque pourcentage reste à vérifier, et l’ordre de rédaction ne démontre pas une fréquence décroissante.')
replace("'<p><span class=\"pv av\">% à vérifier</span> : aucune source suisse ou européenne n’a encore été lue pour ce chiffre ; le rang suit la probabilité clinique.</p>'",
        "'<p><span class=\"pv av\">% à vérifier</span> : la fréquence dans ce cadre n’est pas établie.</p>'")
replace("+(e.cadre?`<p><b>Cadre</b> : ${esc(e.cadre)}.</p>`:'')+(S?",
        "+`<p>${esc(pvRankText(a))}</p>`+(e.cadre?`<p><b>Cadre</b> : ${esc(e.cadre)}.</p>`:'')+(S?")

anchor = 'function tipFor(key)'
helper = "function sspMonoGet(c,key){const M=window.CK_MONO_SSP;if(M)return M[c]||null;if(!MONO_T.ssp){MONO_T.ssp=1;monoLoad('ssp').then(()=>{if(!TIPEL.hidden&&tipK===key)showTip({dataset:{t:key}},tipPin,tipOp||TIPEL,false,true)}).catch(()=>{delete MONO_T.ssp})}return null}\n"
if helper not in s:
    replace(anchor, helper + anchor)
replace("if(ty==='s'){const T=TIP[a],s=BY[a];if(!T)return null;const X=b&&S.seances[b];",
        "if(ty==='s'){const T=TIP[a],s=BY[a];if(!T)return null;const MO=sspMonoGet(a,key);if(MO)return {hd:'Fiche SSP · '+a,ti:s[1],h:MO.h,src:MO.s};const X=b&&S.seances[b];")

replace('#tip .t{font:600 .92rem/1.3 var(--fb);', '#tip .t{font:700 .92rem/1.3 var(--fb);')
if s != before:
    write(s)
    print('Infobulles : fiche SSP structurée et rang non sourcé explicite.')
else:
    print('Correctif déjà appliqué.')

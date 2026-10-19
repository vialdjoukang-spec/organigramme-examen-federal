#!/usr/bin/env python3
"""Restaurer les cours SSP par rubrique ; réserver les monographies aux DD."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _app import read, write

s = before = read()
course = "if(b[0]==='c'){const MO=sspMonoGet(a,key);if(MO){const exam=i===5?exFmt(T.c[i]).replace(/<\\/?(?:b|strong)\\b[^>]*>/gi,''):'';return {hd:'Monographie SSP · '+a,ti:s[1],h:exam?MO.h.replace('<b>5. Sémiologie aux explorations</b>','<br><b>Examen physique par région :</b>'+exam+'<br><b>5. Sémiologie aux explorations</b>'):MO.h,src:exam?MO.s+' · Examen physique : '+T.s:MO.s}}ti=CLIN[i];"
summary = "if(ty==='s'){const T=TIP[a],s=BY[a];if(!T)return null;const MO=sspMonoGet(a,key);if(MO)return {hd:'Fiche SSP · '+a,ti:s[1],h:MO.h,src:MO.s};const X=b&&S.seances[b];"
helper = "function sspMonoGet(c,key){const M=window['CK_MONO_SSP'];if(M)return M[c]||null;if(!MONO_T.ssp){MONO_T.ssp=1;monoLoad('ssp').then(()=>{if(!TIPEL.hidden&&tipK===key)showTip({dataset:{t:key}},tipPin,tipOp||TIPEL,false,true)}).catch(()=>{delete MONO_T.ssp})}return null}\n"

# Déjà restauré : ne rien réécrire. Une présence partielle est une erreur.
if 'sspMonoGet' not in s:
    assert "if(b[0]==='c'){ti=CLIN[i];" in s
    assert "if(ty==='s'){const T=TIP[a],s=BY[a];if(!T)return null;const X=" in s
    print('Cours SSP par rubrique déjà restauré.')
else:
    for anchor in (course, summary, helper):
        assert s.count(anchor) == 1, 'Ancrage absent ou ambigu : ' + anchor[:60]
    s = s.replace(course, "if(b[0]==='c'){ti=CLIN[i];", 1)
    s = s.replace(summary, "if(ty==='s'){const T=TIP[a],s=BY[a];if(!T)return null;const X=b&&S.seances[b];", 1)
    s = s.replace(helper, '', 1)
    assert 'sspMonoGet' not in s
    if s != before:
        write(s)
    print('Cours SSP spécifique par rubrique et fiche éclair restaurés ; DD conservés.')

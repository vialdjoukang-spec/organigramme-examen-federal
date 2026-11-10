import json
S=lambda i:f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
aud=json.load(open('../../audits/LOT_051_Phase_B_V0_DX.5.html.audit.json'))['corrections']
C=[]
for c in aud:
    if c['avant']==c['apres']:
        C.append((c['avant'],"")) if 'plan de soins partagé' in c['avant'] else None
    else: C.append((c['avant'],c['apres']))
C.append(("l'essai thérapeutique est la première intention pour le reflux. Le point de pratique propose un essai",
 "l'essai thérapeutique est la première intention pour le reflux"+S('w2a1b3e-25')+". Le point de pratique américain de l'AGA propose un essai"))
json.dump([{"avant":a,"apres":b} for a,b in C],open('corrections.json','w'),ensure_ascii=False,indent=1)
print(len(C))

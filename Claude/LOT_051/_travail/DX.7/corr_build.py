import json
S=lambda i:f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
aud=json.load(open('../../audits/LOT_051_Phase_B_V0_DX.7.html.audit.json'))['corrections']
def g(k):
    for c in aud:
        if k in c['avant']: return c
C=[]
c=g('denosumab ne doit pas'); C.append((c['avant'],c['apres']))
c=g('sillon supérieur T3 ou T4')
C.append((c['avant'],"<li>Si la tumeur est du sillon supérieur T3 ou T4, sans métastase et opérable, la trimodalité est le standard"+S('w923100-6')+S('w97dce3-8')+". Une métastase M1 ou une atteinte pN3 contre-indique la résection"+S('w97dce3-8')+".</li>"))
c=g('relève du spécialiste'); C.append((c['avant'],""))
c=g('créatinine sérique et la clairance'); C.append((c['avant'],c['apres']))
json.dump([{"avant":a,"apres":b} for a,b in C],open('corrections.json','w'),ensure_ascii=False,indent=1)

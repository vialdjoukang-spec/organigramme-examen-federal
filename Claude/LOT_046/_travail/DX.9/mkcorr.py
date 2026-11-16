import json
a=json.load(open('Claude/LOT_046/audits/LOT_046_Phase_B_V0_DX.9.html.audit.json'))['corrections']
C=[{'avant':x['avant'],'apres':x['apres']} for x in a]
def s(*ids): return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)
C[2]['apres']=("La prednisolone est efficace dans environ 80 % des anémies à anticorps chauds, avec une réponse en 7 à 25 jours"+s('wb601d8-31')+
 ". Prednisolone Streuli® est autorisée en Suisse dans l'anémie hémolytique auto-immune"+s('aips-29348-4')+
 ", avec une posologie initiale habituelle de 5 à 60 mg par jour"+s('aips-29348-7')+
 ". Des doses nettement plus élevées restent autorisées à court terme dans les cas aigus ou particulièrement sévères"+s('aips-29348-7')+".")
C[12]['apres']="Ensuite, le rituximab, hors indication autorisée en Suisse dans cette maladie, est conseillé dans la semaine en cas de résistance aux corticoïdes"+s('wb601d8-31','aips-54378-1','aips-54378-2','aips-54378-3','aips-54378-4')+"."
json.dump(C,open('Claude/LOT_046/_travail/DX.9/corrections.json','w'),ensure_ascii=False,indent=1)

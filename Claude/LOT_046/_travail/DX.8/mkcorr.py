import json
a=json.load(open('Claude/LOT_046/audits/LOT_046_Phase_B_V0_DX.8.html.audit.json'))['corrections']
C=[{'avant':x['avant'],'apres':x['apres']} for x in a]
def s(i): return f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
# 0 Liquémine
C[0]['apres']="Le premier jour d'une EP avec état de choc, la dose journalière doit être augmentée en fonction des résultats des tests de laboratoire, par exemple 40 000 à 60 000 UI en perfusion"+s('aips-15159-6')+"."
# 4 Pradaxa
C[4]['apres']=("Le rivaroxaban et l'apixaban se passent d'héparine de bas poids moléculaire (HBPM) au début du traitement, alors que l'edoxaban et le dabigatran exigent au moins 5 jours d'héparine"+s('wa70cb5-36')+". Pradaxa® se prescrit ensuite à 150 mg deux fois par jour"+s('aips-61385-3')+
 ". Arixtra® (fondaparinux) se donne par voie sous-cutanée une fois par jour, à 7,5 mg de 50 à 100 kg, à 5 mg au-dessous de 50 kg et à 10 mg au-dessus de 100 kg"+s('aips-55937-4')+", pendant au moins 5 jours"+s('aips-55937-5')+".")
# hyperventilation / EP : sans "Pays-Bas" (absent de l'extrait)
C[6]['apres']=C[6]['apres']
for x in C:
    x['apres']=x['apres'].replace(" aux Pays-Bas","")
# Marcoumar dose initiale
C.append({'avant':"<td>Dose selon l'INR, voie orale</td>",'apres':"<td>4,5 à 9 mg le 1er jour, 6 mg le 2e jour, puis selon l'INR, voie orale"+s('aips-19395-4')+"</td>"})
# noradrénaline / dobutamine
C.append({'avant':"La noradrénaline et la dobutamine sont à considérer chez le patient à haut risque (recommandation IIa C)"+s('wa6f758-176')+".",
 'apres':"La noradrénaline et la dobutamine sont à considérer chez le patient à haut risque (recommandation IIa C)"+s('wa6f758-176')+". Noradrenalin Sintetica® se perfuse par pompe, à une vitesse initiale de 8 à 12 µg/minute pour un poids de 70 kg"+s('aips-67023-2')+". Dobutrex® répond le plus souvent à des débits de 2,5 à 10 µg/kg/min, la dose se réduisant progressivement plutôt que d'un coup"+s('aips-45687-4')+"."})
json.dump(C,open('Claude/LOT_046/_travail/DX.8/corrections.json','w'),ensure_ascii=False,indent=1)
print(len(C))

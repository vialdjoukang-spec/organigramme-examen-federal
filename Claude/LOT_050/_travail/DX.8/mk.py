import json
d=json.load(open('../../audits/LOT_050_Phase_B_V0_DX.8.html.audit.json'))
S=lambda i:f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
C=[]
C.append({"avant":"Chez l'enfant en insuffisance cardiaque ou en choc cardiogénique, la cardioversion électrique synchronisée ou l'adénosine sont indiquées"+S('wefb035-29')+".",
"apres":"Chez l'enfant en insuffisance cardiaque ou en choc cardiogénique, la cardioversion électrique synchronisée (0,5 à 2 J/kg) est indiquée"+S('wefb035-29')+" ; l'adénosine n'est envisagée qu'après lecture d'un rythme régulier à QRS fins, jamais devant un rythme irrégulier"+S('we05299-90')+"."})
C.append({"avant":" La cause psychiatrique représente 31 % des palpitations dans une cohorte prospective"+S('wac5dd7-3')+".","apres":""})
C.append({"avant":"<td>Amiodarone i.v. (Labatec®, 59528)</td>","apres":"<td>Amiodarone i.v. (Labatec®, 59528), réservée à la tachycardie réciproque réfractaire et proscrite dans la fibrillation atriale pré-excitée (classe III)"+S('w4cc2cc-17')+"</td>"})
C.append({"avant":"<td>Cardioversion électrique ou antiarythmique choisi</td>","apres":"<td>Cardioversion électrique ; si stable, ibutilide, procaïnamide ou flécaïnide, jamais de bloqueur nodal ni d'amiodarone"+S('w4cc2cc-16')+S('we7a74c-21')+"</td>"})
C.append({"avant":"Si la tachycardie s'interrompt, alors la réentrée est confirmée, et si","apres":"Si la tachycardie s'interrompt, alors une réentrée impliquant le nœud est probable, et si"})
C.append({"avant":"indiquée en classe Ib pour la fibrillation atriale pré-excitée symptomatique","apres":"indiquée en classe I, niveau de preuve B, pour la fibrillation atriale pré-excitée symptomatique"})
C.append({"avant":"Les patients apprennent à réaliser les manœuvres vagales et peuvent reprendre le sport après arrêt de la crise. ","apres":""})
C.append({"avant":"Le pronostic est excellent après ablation réussie, qui réduit nettement le risque de fibrillation ventriculaire par la voie. ","apres":""})
json.dump(C,open('corrections.json','w'),ensure_ascii=False,indent=1)

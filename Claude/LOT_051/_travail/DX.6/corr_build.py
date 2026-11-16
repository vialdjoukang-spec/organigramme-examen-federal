import json
S=lambda i:f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
aud=json.load(open('../../audits/LOT_051_Phase_B_V0_DX.6.html.audit.json'))['corrections']
A={c['avant'][:50]:c for c in aud}
def g(k):
    for c in aud:
        if k in c['avant']: return c['avant']
    raise KeyError(k)
C=[]
C.append((g('Énoxaparine (Hepaxane'),
 "<tr><td>Énoxaparine (Hepaxane®)</td><td>Angor instable et NSTEMI : 1 mg/kg s.c. toutes les 12 h"+S('aips-67702-6')+" ; STEMI : bolus i.v. de 30 mg plus 1 mg/kg s.c., puis 1 mg/kg toutes les 12 h"+S('aips-67702-7')+" ; 75 ans ou plus : 0,75 mg/kg s.c. sans bolus"+S('aips-67702-14')+"</td>"))
C.append((g('5 mg si poids inférieur'),
 "<td>5 mg si poids inférieur à 60 kg ; en général non recommandé à 75 ans ou plus, dose initiale unique de 60 mg puis 5 mg par jour si le traitement est jugé nécessaire ; charge au moment de l'angioplastie si coronarographie dans les 48 h"))
C.append((g('La nitroglycérine soulage'),
 "La nitroglycérine soulage les symptômes angineux : Nitroglycérine Streuli® (Swissmedic 36830) se donne à 1 capsule de 0,8 mg croquée, exceptionnellement 2"+S('aips-36830-2')+S('aips-36830-0')+". Elle est contre-indiquée si la pression systolique est de 90 mmHg ou moins"+S('aips-36830-3')+". Le protocole du SMUR genevois retient un seuil de 110 mmHg"+S('w8db60a-6')+"."))
C.append((g('La fibrinolyse reste'),
 "La fibrinolyse reste la solution quand l'angioplastie n'est pas faisable dans le délai"+S('w480b78-185')+". Le bolus intraveineux unique de ténectéplase (Metalyse®, Swissmedic 55418) s'ajuste au poids, de 30 mg sous 60 kg à 50 mg dès 90 kg"+S('aips-55418-2')+S('aips-55418-0')+"."))
C.append((g('fentanyl, de 0,5'),
 "Le protocole genevois du SMUR utilise le fentanyl intraveineux en dose de charge titrée"+S('w8db60a-6')+". L'information professionnelle de Fentanyl-Mepha vise l'anesthésie et la douleur postopératoire, et conseille de réduire la dose chez les patients âgés et affaiblis"+S('aips-53484-1')+S('aips-53484-18')+"."))
C.append((g('très basse, ou basse'),
 "<li>Si la valeur initiale est très basse et la douleur a débuté plus de 3 h avant, ou si elle est basse sans variation à 1 h, l'infarctus est exclu"+S('w480b78-122')+S('w480b78-123')+"</li>"))
C.append((g('Troponine très basse à 0 heure'),
 "<tr><td>Troponine très basse à 0 heure, douleur depuis plus de 3 h</td><td>Exclusion possible de l'infarctus</td>"))
C.append((g('premier bolus par voie veineuse'),
 "<td>2,5 mg par jour ; première dose en bolus i.v. dans le STEMI seulement, au plus 8 jours"+S('aips-55937-6')+"</td>"))
C.append((g('Après la phase aiguë, un inhibiteur'),
 "Un inhibiteur de l'enzyme de conversion est recommandé en cas d'insuffisance cardiaque, de fraction d'éjection de 40 % ou moins, de diabète, d'hypertension ou d'insuffisance rénale chronique"+S('w480b78-453')+"."))
C.append((g('statine à haute intensité'),
 "Une statine à haute intensité, atorvastatine ou rosuvastatine, est démarrée dès que possible à l'hôpital"+S('w480b78-420')+". Pour Atorvastatine Sandoz® (Swissmedic 61285), la dose journalière maximale est de 80 mg 1x par jour"+S('aips-61285-4')+S('aips-61285-0')+", et elle est contre-indiquée pendant la grossesse et l'allaitement"+S('aips-61285-43')+"."))
json.dump([{"avant":a,"apres":b} for a,b in C],open('corrections.json','w'),ensure_ascii=False,indent=1)
print(len(C))

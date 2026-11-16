import json,re
S=lambda i:f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
aud=json.load(open('../../audits/LOT_051_Phase_B_V0_DX.4.html.audit.json'))['corrections']
A={}
for c in aud: A[c['avant'][:40]]=c['avant']
def av(k): 
    for a in A.values():
        if k in a: return a
    raise KeyError(k)
C=[]
C.append((av("la plupart des lignes directrices recommandent l'oseltamivir"),
 "Au quatrième temps, si l'on suspecte la grippe grave, on donne l'oseltamivir (Tamiflu®) à 75 mg 2x par jour pendant cinq jours"+S('wc41478-55')+S('aips-55196-3')+"."))
C.append((av("la clindamycine ou une céphalosporine avec le métronidazole"),
 av("la clindamycine ou une céphalosporine avec le métronidazole")+" Par voie parentérale, la Clindamycin Pfizer® se donne à 1200-1800 mg par jour en 2 à 4 doses dans l'infection sévère"+S('aips-61556-5')+"."))
C.append((av("est recommandée<sup class=\"r\"><a href=\"#sb-w97d9a5-25"),
 "En présence de comorbidités, le groupe européen réserve la lévofloxacine ou la moxifloxacine aux résistances cliniquement pertinentes envers les antibiotiques de premier choix"+S('w67059c-127')+". Pour une pneumonie communautaire, l'Azithromycine Sandoz® se donne à 500 mg par jour du jour 1 au jour 3"+S('aips-57482-5')+", la Lévofloxacine Sandoz® à 500 mg une à deux fois par 24 heures pendant 7 à 14 jours"+S('aips-59085-5')+", et la Moxifloxacine Sandoz® à 400 mg par jour pendant 10 jours"+S('aips-63183-6')+"."))
C.append(("Ainsi, À l'hôpital","Ainsi, à l'hôpital"))
C.append((av("Pour Ibuprofen-Mepha Teva, la dose simple"),
 "Pour Ibuprofen-Mepha Teva, l'AIPS ne cite pas la douleur pleurale ; dans les affections rhumatismales, la dose initiale est de 1200-1800 mg par jour en plusieurs doses, et dans certains cas jusqu'à 2400 mg"+S('aips-49156-4')+"."))
C.append((av("en cas d'ulcère gastro-duodénal actif ou ancien"),
 "Cette molécule est contre-indiquée au troisième trimestre de la grossesse et en cas d'ulcère ou d'hémorragie digestive actifs, ou d'au moins deux épisodes distincts dans l'anamnèse"+S('aips-49156-7')+"."))
C.append(("Ainsi, L'intervalle","Ainsi, l'intervalle"))
C.append(("<td>Intraveineuse</td><td>Selon l'évolution</td><td></td></tr><tr><td>Paracetamol-Mepha 1000</td>",
 "<td>Intraveineuse ou intramusculaire</td><td>Selon l'évolution</td><td></td></tr><tr><td>Paracetamol-Mepha 1000</td>"))
old_row='<tr><td>Ibuprofen-Mepha Teva</td><td>49156</td><td>400 à 800 mg par prise, au plus 2400 mg par jour'+S('aips-49156-4')+'</td><td>Orale</td><td>Court</td><td></td></tr>'
new_row=('<tr><td>Ibuprofen-Mepha Teva</td><td>49156</td><td>Affections rhumatismales : 1200-1800 mg par jour, jusqu\'à 2400 mg'+S('aips-49156-4')+'</td><td>Orale</td><td>Court</td><td></td></tr>'
 '<tr><td>Azithromycine Sandoz®</td><td>57482</td><td>500 mg par jour du jour 1 au jour 3'+S('aips-57482-5')+'</td><td>Orale</td><td>3 jours</td><td></td></tr>'
 '<tr><td>Lévofloxacine Sandoz®</td><td>59085</td><td>500 mg 1-2 fois par 24 h'+S('aips-59085-5')+'</td><td>Orale ou intraveineuse</td><td>7 à 14 jours</td><td></td></tr>'
 '<tr><td>Moxifloxacine Sandoz®</td><td>63183</td><td>400 mg par jour'+S('aips-63183-6')+'</td><td>Orale</td><td>10 jours</td><td></td></tr>'
 '<tr><td>Clindamycin Pfizer®</td><td>61556</td><td>1200-1800 mg par jour en 2 à 4 doses'+S('aips-61556-5')+'</td><td>Intramusculaire ou intraveineuse</td><td>Selon l\'évolution</td><td></td></tr>'
 '<tr><td>Tamiflu®</td><td>55196</td><td>75 mg 2 fois par jour'+S('aips-55196-3')+'</td><td>Orale</td><td>5 jours</td><td></td></tr>')
C.append((old_row,new_row))
# ajout phrase numéros + grossesse
C.append(("et Ibuprofen-Mepha Teva 49156"+S('aips-49156-0')+".",
 "et Ibuprofen-Mepha Teva 49156"+S('aips-49156-0')+". Les antibiotiques et l'antiviral ajoutés portent aussi un numéro : Azithromycine Sandoz® 57482"+S('aips-57482-0')+", Lévofloxacine Sandoz® 59085"+S('aips-59085-0')+", Moxifloxacine Sandoz® 63183"+S('aips-63183-0')+", Clindamycin Pfizer® 61556"+S('aips-61556-0')+" et Tamiflu® 55196"+S('aips-55196-0')+"."))
C.append(("et que l'ibuprofène est contre-indiqué au troisième trimestre"+S('aips-49156-7')+".",
 "et que l'ibuprofène est contre-indiqué au troisième trimestre"+S('aips-49156-7')+". La lévofloxacine et la moxifloxacine sont contre-indiquées pendant la grossesse et l'allaitement"+S('aips-59085-10')+S('aips-63183-9')+". La clindamycine ne s'administre pendant la grossesse qu'en cas de nécessité absolue, et l'allaitement doit être arrêté si elle est nécessaire"+S('aips-61556-32')+S('aips-61556-33')+". L'azithromycine ne s'utilise pendant la grossesse qu'en cas de nécessité clinique"+S('aips-57482-42')+". Pour l'oseltamivir, aucun ajustement posologique n'est recommandé chez la femme enceinte"+S('aips-55196-29')+"."))
# vaccination
C.append((av("vaccination séquentielle par le vaccin conjugué"),
 "En Suisse, l'Office fédéral de la santé publique recommande la vaccination antipneumococcique comme vaccination complémentaire pour toutes les personnes de 65 ans et plus"+S('wc90e13-7')+". Il publie aussi une prise de position sur les vaccins antipneumococciques conjugués selon le groupe d'âge"+S('wc90e13-6')+"."))
C.append(("Les recommandations suisses précises de l'Office fédéral de la santé publique n'ont pas pu être lues ici, et un enseignant doit donc les vérifier dans le plan de vaccination en vigueur.",
 "Le plan de vaccination suisse réunit les vaccins recommandés en Suisse"+S('wc90e13-9')+"."))
C.append(("Plan de vaccination suisse à vérifier","Plan de vaccination suisse de l'OFSP"))
json.dump([{"avant":a,"apres":b} for a,b in C],open('corrections.json','w'),ensure_ascii=False,indent=1)

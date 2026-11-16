import json
A=json.load(open('../../audits/LOT_044_Phase_B_V0_DX.7.html.audit.json'))['corrections']
def s(i): return f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
def S(*ids): return ''.join(s(i) for i in ids)
out=[]
for c in A:
    a,b=c['avant'],c['apres']
    if a.startswith('<tr><td>Altéplase'):
        b=("<tr><td>Altéplase (Actilyse®, 48313)</td><td>100 mg en 2 heures : bolus de 10 mg en 1 à 2 minutes, puis 90 mg en perfusion ; sous 65 kg, 1,5 mg/kg au maximum"+S('aips-48313-6')+"</td><td>Intraveineuse</td><td>2 heures</td><td>Antécédent d'AVC hémorragique ou d'étiologie inconnue</td><td>aips-48313-6</td></tr>"
           "<tr><td>Édoxaban (Lixiana®, 65149)</td><td>60 mg une fois par jour après au moins 5 jours d'héparine ; 30 mg si clairance de 15 à 50 ml/min, poids ≤ 60 kg ou inhibiteur de la P-gp"+S('aips-65149-3','aips-65149-4')+"</td><td>Orale</td><td>Selon le risque de récidive</td><td>Hémorragie aiguë significative, grossesse</td><td>aips-65149-15</td></tr>")
    elif a.startswith('Parmi les autres molécules de la classe figure l\'édoxaban'):
        b=("Parmi les autres molécules de la classe figure l'édoxaban (Lixiana®, n° Swissmedic 65149), dont la dose est de 60 mg une fois par jour après au moins 5 jours d'héparine"+S('aips-65149-3','aips-65149-83')+". La dose est de 30 mg une fois par jour en cas de clairance de 15 à 50 ml/min, de poids inférieur ou égal à 60 kg, ou d'association à la ciclosporine, à la dronédarone, à l'érythromycine, au kétoconazole, à la quinidine ou au vérapamil"+S('aips-65149-4')+". Les contre-indications comprennent l'hypersensibilité, les hémorragies aiguës cliniquement significatives, les maladies hépatiques avec coagulopathie, les lésions à risque hémorragique majeur, les autres anticoagulants et la grossesse"+S('aips-65149-15')+".")
        c['avant']=a[:a.index(' Les anticoagulants oraux directs ont fait')] if False else a
    elif a.startswith('Contre-indications du rivaroxaban'):
        b=("Les contre-indications du rivaroxaban comprennent l'hypersensibilité, l'endocardite aiguë d'origine bactérienne, le saignement évolutif cliniquement significatif, l'ulcère gastro-intestinal aigu et les maladies gastro-intestinales ulcéreuses"+S('aips-58728-24')+". Elles comprennent aussi l'hépatopathie et l'insuffisance hépatique sévères avec risque hémorragique majoré, l'insuffisance rénale nécessitant une dialyse, la grossesse et l'allaitement"+S('aips-58728-24')+".")
    elif a.startswith('Contre-indications : thrombopénie induite par l\'héparine actuelle'):
        b=("Les contre-indications de la Liquémine® comprennent l'hypersensibilité, la thrombopénie induite par l'héparine actuelle ou passée, la diathèse hémorragique, les maladies hépatiques, rénales ou pancréatiques sévères et la thrombopénie sévère"+S('aips-15159-11')+". Elles comprennent aussi l'hypertension artérielle de plus de 105 mmHg diastolique, l'hémorragie cérébrale, l'anesthésie spinale ou épidurale et la ponction lombaire"+S('aips-15159-11')+". Pour l'héparine B. Braun, la pression diastolique supérieure à 110 mmHg non maîtrisée et l'hémorragie active figurent parmi les contre-indications"+S('aips-46613-12')+".")
    out.append({'avant':a,'apres':b})
# apixaban CI
out.append({'avant':"Par ailleurs, contre-indications de l'apixaban : saignement évolutif cliniquement significatif et insuffisance hépatique sévère de classe Child Pugh C "+s('aips-61549-16')+".",
 'apres':"Par ailleurs, les contre-indications de l'apixaban comprennent l'hypersensibilité, le saignement évolutif cliniquement significatif, les maladies hépatiques avec coagulopathie et l'insuffisance hépatique sévère de classe Child Pugh C "+s('aips-61549-16')+"."})
# altéplase paragraphe
av="Elle augmente toutefois les hémorragies extracrâniennes majeures (6,3 % contre 1,2 %) "+s('wda45ff-60')+".</div>"
out.append({'avant':av,'apres':"Elle augmente toutefois les hémorragies extracrâniennes majeures (6,3 % contre 1,2 %) "+s('wda45ff-60')+".</div>"
 '<div class="p">L\'Actilyse® (altéplase, n° Swissmedic 48313) est indiquée dans l\'embolie pulmonaire massive aiguë avec instabilité hémodynamique'+S('aips-48313-1','aips-48313-84')+". Le schéma habituel donne 100 mg en 2 heures, soit un bolus de 10 mg en 1 à 2 minutes puis 90 mg en perfusion"+S('aips-48313-6')+". Au-dessous de 65 kg, la perfusion de 2 heures atteint au plus 1,5 mg/kg"+S('aips-48313-6')+'.</div>'
 '<div class="p">Les contre-indications valent pour toutes les indications : hypersensibilité, hémorragie grave ou dangereuse dans les 6 derniers mois, diathèse hémorragique connue et anticoagulation orale efficace'+S('aips-48313-13')+". Elles comprennent aussi un traumatisme crânien dans les 3 derniers mois, une chirurgie intracrânienne ou spinale, une hypertension sévère non contrôlée, une intervention majeure ou un traumatisme dans les 10 derniers jours"+S('aips-48313-13')+". S'y ajoutent l'accouchement récent, l'atteinte hépatique sévère, l'endocardite bactérienne, la péricardite, la pancréatite aiguë, l'ulcère actif, l'anévrisme artériel, les néoplasmes à risque hémorragique et, pour l'embolie pulmonaire, l'antécédent d'AVC hémorragique"+S('aips-48313-13','aips-48313-14')+'.</div>'
 '<div class="p">Pendant la grossesse, l\'expérience avec l\'altéplase est limitée, et le bénéfice attendu doit être évalué par rapport au risque dans une pathologie menaçant le pronostic vital'+S('aips-48313-36')+'.</div>'})
json.dump(out,open('corrections.json','w'),ensure_ascii=False,indent=1)

import json
A=json.load(open('Claude/LOT_044/audits/LOT_044_Phase_B_V0_DX.10.html.audit.json'))['corrections']
def s(i): return f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
def S(*ids): return ''.join(s(i) for i in ids)
by={}
for c in A: by[c['avant'][:60]]=c
out=[]
for c in A:
    a,b=c['avant'],c['apres']
    if a.startswith('Les contre-indications comprennent le bloc auriculo'):
        b=("Les contre-indications comprennent l'hypersensibilité au labétalol, le bloc AV de degré 2 et 3 sans stimulateur, le choc cardiogénique et les autres états avec hypotension marquée et persistante ou bradycardie sévère, l'asthme ou la bronchopneumopathie obstructive, l'insuffisance cardiaque non compensée, la dysfonction sinusale sans stimulateur, l'angor de Prinzmetal, le cœur pulmonaire, l'hypotension artérielle sévère, la bradycardie inférieure à 50 par minute, et le traitement concomitant par un inhibiteur de la monoamine-oxydase (IMAO) ou par un antagoniste calcique de type vérapamil ou diltiazem"+S('aips-41529-14')+'.')
    elif a.startswith('Les contre-indications de l\'esmolol'):
        b=("Les contre-indications de l'esmolol comprennent l'hypersensibilité, la bradycardie sinusale sévère inférieure à 50 par minute, la maladie du sinus, les troubles graves de la conduction AV sans stimulateur, les blocs AV du second et du troisième degré, le bloc sino-auriculaire, le choc cardiogénique, l'hypotension sévère, l'insuffisance cardiaque décompensée et l'administration intraveineuse concomitante ou récente de vérapamil ou de diltiazem"+S('aips-65741-16')+". S'y ajoutent le phéochromocytome non traité, l'hypertension pulmonaire, la crise d'asthme aiguë et l'acidose métabolique, et l'esmolol ne doit être donné que 48 heures après l'arrêt du vérapamil"+S('aips-65741-17')+'.')
    elif a.startswith('La dose se fixe selon le protocole'):
        b=("L'information professionnelle de Morphini HCl Streuli® (n° Swissmedic 56554) prévoit 2 à 10 mg par voie intraveineuse lente, à 10 mg par minute, uniquement lorsqu'un effet spécialement rapide est nécessaire"+S('aips-56554-5','aips-56554-64')+'.')
    elif a.startswith('<tr><td>Morphine i.v.'):
        b=b.replace('<sup class="r"><a href="#sb-aips-56554-5">aips-56554-5</a></sup>','<sup class="r"><a href="#sb-aips-56554-5">aips-56554-5</a></sup>')
    elif a.startswith('<tr><td>Nitroprussiate'):
        b=b.replace('Nipruss® (nitroprussiate, 67308)</td><td>0,2 µg/kg/min, doublé toutes les 3 à 5 minutes jusqu\'à la pression visée</td>','Nipruss® (nitroprussiate, 67308)</td><td>0,2 µg/kg/min, doublé toutes les 3 à 5 minutes jusqu\'à la pression visée'+S('aips-67308-3')+'</td>')
    elif a.startswith('Le Trandate® (labétalol), solution'):
        b=("La notice commune du Trandate® (labétalol), pour les comprimés et la solution injectable hospitalière, porte les numéros d'autorisation Swissmedic 41530 et 41529"+S('aips-41529-61')+'.')
    elif a.startswith('Cette notice ne mentionne pas la dissection'):
        pass
    out.append({'avant':a,'apres':b})
# paragraphe supplémentaire après urapidil
av="Comme les autres vasodilatateurs, il s'emploie après le bêtabloquant et non avant lui"+S('esc2024aorte-118')+'.</div>'
nv=("Comme les autres vasodilatateurs, il s'emploie après le bêtabloquant et non avant lui"+S('esc2024aorte-118')+'.</div>'
 '<div class="p">Le Nipruss® (nitroprussiate de sodium, n° Swissmedic 67308) est indiqué dans les crises hypertensives'+S('aips-67308-1')+". La perfusion débute à 0,2 µg/kg/min, puis la dose est doublée toutes les 3 à 5 minutes jusqu'à la pression désirée"+S('aips-67308-3')+". Les contre-indications comprennent l'hypersensibilité, l'hypertension compensatoire due à une coarctation de l'aorte ou à des shunts artérioveineux, l'atrophie optique de Leber, l'amblyopie tabagique, la carence en vitamine B12, l'acidose métabolique, l'hypothyroïdie et les shunts artérioveineux intrapulmonaires"+S('aips-67308-14')+". En outre, le nitroprussiate ne doit pas être administré pendant la grossesse"+S('aips-67308-21')+'.</div>'
 '<div class="p">La nicardipine (Nicardipin Aguettant, n° Swissmedic 67680) est indiquée dans l\'urgence hypertensive, y compris la dissection aortique lorsque le traitement par un bêtabloquant à courte durée d\'action ne convient pas ou lorsque le bêtabloquant seul est insuffisant'+S('aips-67680-1','aips-67680-0')+". On débute par 3-5 mg/h pendant 15 minutes, puis on augmente par paliers de 0,5 ou 1 mg toutes les 15 minutes sans dépasser 15 mg/h"+S('aips-67680-2')+". La dose d'entretien se situe généralement entre 2 et 4 mg/h, et la nicardipine s'administre uniquement en perfusion intraveineuse continue"+S('aips-67680-3','aips-67680-7')+". Elle est contre-indiquée en cas d'hypersensibilité, de sténose aortique sévère, d'hypertension compensatoire par shunt artérioveineux ou coarctation de l'aorte, d'angor instable et dans les 8 jours après un infarctus du myocarde"+S('aips-67680-9')+'.</div>'
 '<div class="p">Le Fentanyl-Mepha® i.v./i.m. (n° Swissmedic 53484) est un antalgique opioïde indiqué pour l\'anesthésie et la douleur postopératoire'+S('aips-53484-1','aips-53484-52')+". Sa notice ne cite pas la dissection aortique, de sorte que son emploi dans cette douleur reste hors indication, et elle contre-indique l'intolérance connue à l'un de ses composants ou à d'autres opioïdes"+S('aips-53484-8')+'.</div>')
out.append({'avant':av,'apres':nv})
json.dump(out,open('Claude/LOT_044/_travail/DX.10/corrections.json','w'),ensure_ascii=False,indent=1)
print(len(out))

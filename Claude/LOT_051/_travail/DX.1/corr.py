import sys,json
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad')
from rep import R,sup
r=R('DX.1')
A=json.load(open('/home/user/wt/lot-051/Claude/LOT_051/audits/LOT_051_Phase_B_V0_DX.1.html.audit.json'))['corrections']
OV={}
OV['Chez la femme enceinte, l\'ibuprofène']=("Pendant la grossesse, le diclofénac topique ne doit pas être utilisé et l'ibuprofène et le naproxène sont contre-indiqués au troisième trimestre"+sup('aips-61859-10','aips-49156-7','aips-51480-5')+". Aux premier et deuxième trimestres, l'ibuprofène est à éviter à moins d'une nécessité clairement établie, avec la dose et la durée les plus faibles possible"+sup('aips-49156-34')+". À partir de la 20e semaine, les AINS peuvent provoquer un oligohydramnios"+sup('aips-49156-35')+". L'emplâtre Perskindol Diclofenac Patch ne doit pas être utilisé au dernier trimestre"+sup('aips-69254-7')+". Le paracétamol peut être pris pendant la grossesse en cas de nécessité clinique, à la dose efficace la plus faible et pendant la durée la plus courte possible"+sup('aips-62116-20')+".</li><li>Pendant l'allaitement, l'ibuprofène ne doit pas être pris et le nourrisson doit être sevré si le traitement est indispensable"+sup('aips-49156-39')+". Le naproxène ne doit pas être pris par les femmes qui allaitent"+sup('aips-51480-36')+". Le diclofénac topique ne doit pas être utilisé chez la femme qui allaite, ni l'emplâtre chez les mères qui allaitent"+sup('aips-61859-11','aips-69254-8')+". Le paracétamol passe dans le lait maternel, mais il est considéré comme compatible avec l'allaitement, avec prudence"+sup('aips-62116-21')+".")
done=0
for c in A:
    av=c['avant']; ap=c['apres']
    for k,v in OV.items():
        if av.startswith(k): ap=v
    # find fragment
    import glob
    hit=None
    for f in sorted(glob.glob(r.d+'p*.html')):
        t=open(f,encoding='utf-8').read()
        if t.count(av)==1: hit=f.split('/')[-1]; break
        # for the grossesse bullet the avant sits inside <li>
    if not hit: print('INTROUVABLE',av[:60]); r.fail+=1; continue
    if ap=='':
        r(hit,' '+av,'') if ' '+av in open(r.d+hit,encoding='utf-8').read() else r(hit,av,'')
    else: r(hit,av,ap)
# ibuprofène CI : mission ulcère selon AIPS (apres audit omet l'anamnèse)
r('p11.html',"Il l'est aussi en cas d'ulcère ou d'hémorragie digestive, d'insuffisance rénale","Il l'est aussi en cas d'ulcère ou d'hémorragie digestive actifs ou dans l'anamnèse (au moins deux épisodes distincts), d'insuffisance rénale")
# connecteurs mécaniques restants
r('p07.html','Par ailleurs, Chaque syndrome ci-dessous','Chaque syndrome ci-dessous')
r('p14.html','En outre, Chaque piège ci-dessous','Chaque piège ci-dessous')
r('p04.html','Ainsi le score coronarien suisse de Gencer','Le score coronarien suisse de Gencer')
r('p05.html','Ainsi, dans le syndrome de Tietze, les poussées','Dans le syndrome de Tietze, les poussées')
r('p01.html','Ainsi, une côte fracturée','Par exemple, une côte fracturée')
r('p11.html','Par ailleurs, les études épidémiologiques n\'indiquent','Les études épidémiologiques n\'indiquent')
print('fail',r.fail)

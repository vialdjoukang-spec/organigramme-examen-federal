import json
S=lambda i:f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
C=[
("L'amoxicilline est indiquée dans la pneumonie bactérienne selon l'information professionnelle suisse"+S('aips-56203-1')+".",
 "L'information professionnelle suisse indique l'amoxicilline dans la pneumonie bactérienne, sans viser spécifiquement l'aspiration ; le choix de l'antibiotique suit donc le protocole hospitalier et la gravité"+S('aips-56203-1')+"."),
(" Amoxicilline Sandoz® (autorisation Swissmedic 56203) prévoit, chez l'adulte, 1500 à 3000 mg d'amoxicilline par jour en 3 à 4 doses dans les infections légères à moyennes"+S('aips-56203-0')+S('aips-56203-6')+".",""),
("Les contre-indications comprennent les inhibiteurs non sélectifs de la MAO, l'insuffisance rénale ou hépatique décompensée et les affections cardiaques"+S('aips-38096-15')+".",
 "Les contre-indications comprennent les inhibiteurs non sélectifs de la MAO, l'insuffisance endocrinienne, rénale ou hépatique décompensée, les affections cardiaques et l'âge inférieur à 25 ans"+S('aips-38096-15')+"."),
("Madopar est contre-indiqué pendant la grossesse et chez la femme apte à procréer sans contraception fiable, et un test de grossesse précède le traitement"+S('aips-38096-38')+".",
 "Madopar est contre-indiqué pendant la grossesse et chez la femme apte à procréer sans contraception fiable ; un test de grossesse précède le traitement"+S('aips-38096-38')+". Les mères traitées par Madopar doivent arrêter l'allaitement, car des malformations osseuses chez l'enfant ne peuvent être exclues"+S('aips-38096-39')+"."),
("Aspiration sous les cordes (PAS 4 à 8)","Pénétration ou aspiration sous les cordes (PAS 4 à 8)"),
("Si la PAS est de 3 à 5, alors la dysphagie est légère, et la rééducation avec les postures suffisent d'abord"+S('w2f6885-49')+".",
 "Si la PAS est de 3 à 5, alors la dysphagie est légère, et les stratégies compensatoires, textures et postures, visent surtout les phases aiguë et de récupération"+S('w2f6885-49')+S('w6c0e63-9')+"."),
(" L'incobotulinumtoxine A est la seule toxine A approuvée dans cette indication selon cette revue"+S('w7f4748-15')+".",""),
("Un premier épisode de pneumonie d'aspiration est suivi d'une mortalité de 65,2 % à 1 an"+S('wafe5c7-22')+".</div>",
 "Dans une cohorte coréenne, un premier épisode de pneumonie d'aspiration est suivi d'une mortalité de 65,2 % à 1 an, contre 67,4 % chez les témoins"+S('wafe5c7-22')+".</div>"),
]
json.dump([{"avant":a,"apres":b} for a,b in C],open('Claude/LOT_048/_travail/DX.4/corrections.json','w'),ensure_ascii=False)

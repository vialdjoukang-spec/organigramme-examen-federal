R=[
("Le risque dépend de la durée","Le risque est lié à la durée"),
("le type d'abord vasculaire influence le risque","le type d'abord vasculaire peut influencer le risque"),
("Une règle clinique aide à décider","Une règle clinique peut aider à décider"),
("La mortalité hospitalière de l'endocardite se situe entre 15 % et 30 %\", 'w37576c-4'),\n        S(\"L'équipe","La mortalité hospitalière reste élevée, entre 15 % et 30 %\", 'w37576c-4'),\n        S(\"Par ailleurs, l'équipe"),
("S(\"L'endocardite à S. aureus a donné","S(\"Par ailleurs, l'endocardite à S. aureus a donné"),
("S(\"Le risque est multiplié jusqu'à cinq fois","S(\"En outre, le risque est multiplié jusqu'à cinq fois"),
("S(\"Les cathéters veineux centraux multiplient","S(\"En outre, les cathéters veineux centraux multiplient"),
("S(\"Les complications hospitalières comprenaient","S(\"En effet, les complications hospitalières comprenaient"),
("S(\"La destruction valvulaire provoque","S(\"En effet, la destruction valvulaire provoque"),
("S(\"Le score VIRSTA comprend","S(\"Ainsi, le score VIRSTA comprend"),
("S(\"Sur une prothèse mitrale,","S(\"En revanche, sur une prothèse mitrale,"),
("S(\"Les articulations se recherchent","S(\"Ensuite, les articulations se recherchent"),
("S(\"Un sepsis complique","S(\"Par ailleurs, un sepsis complique"),
("S(\"Les événements emboliques sont présents","S(\"En effet, les événements emboliques sont présents"),
("S(\"Les critères de Duke, introduits en 1994,","S(\"Cependant, les critères de Duke, introduits en 1994,"),
("S(\"Ce critère peut faire passer","S(\"Ainsi, ce critère peut faire passer"),
("S(\"Dans la série lausannoise,","S(\"Ainsi, dans la série lausannoise,"),
("S(\"Les prélèvements précèdent l'antibiothérapie","S(\"Les prélèvements précèdent donc l'antibiothérapie"),
("S(\"Une méta-analyse de 2133","S(\"Par ailleurs, une méta-analyse de 2133"),
("S(\"Pour une prothèse précoce ou une infection","S(\"En revanche, pour une prothèse précoce ou une infection"),
("S(\"Dans l'endocardite à entérocoques, la vancomycine est","S(\"Par ailleurs, dans l'endocardite à entérocoques, la vancomycine est"),
("S(\"La flucloxacilline est réservée","S(\"En effet, la flucloxacilline est réservée"),
("S(\"Dans les infections sévères, l'adulte reçoit 2 g","S(\"Si l'infection est sévère, l'adulte reçoit 2 g"),
("S(\"Une étude multicentrique a associé","S(\"En effet, une étude multicentrique a associé"),
("S(\"Le suivi moyen de 5,4 ans","S(\"Par ailleurs, le suivi moyen de 5,4 ans"),
("S(\"Les patients décédés avaient","S(\"En effet, les patients décédés avaient"),
("S(\"Les recommandations européennes de 2023 ont fait passer","S(\"Ainsi, les recommandations européennes de 2023 ont fait passer"),
("S(\"Le schéma consiste en","S(\"Ensuite, le schéma consiste en"),
("S(\"Les recommandations pour ces actes figurent","S(\"Par ailleurs, les recommandations pour ces actes figurent"),
]
fs=['c1.py','c2.py','c3.py','c4.py']
T={f:open(f).read() for f in fs}
for old,new in R:
    n=sum(t.count(old) for t in T.values())
    if n!=1: print('!!',n,old[:70]); continue
    for f in fs:
        if old in T[f]: T[f]=T[f].replace(old,new)
for f in fs: open(f,'w').write(T[f])

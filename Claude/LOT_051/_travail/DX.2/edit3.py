import glob,re
def c(i): return f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
ADD=[ # (texte avant le point final, citation)
("59 médecins généralistes de Suisse romande ont enregistré chaque consultation pour douleur thoracique","wa104f4-2"),
("la douleur thoracique représente 11 % des motifs d'admission","wcdaf96-8"),
("l'âge moyen était de 43 ans, contre 51 ans pour les autres formes","wb521dd-14"),
("l'incidence de trouble panique atteint 11,1 % sur deux ans chez des patients sans trouble au départ","weba682-4"),
("de tout patient à douleur thoracique aiguë","wcdaf96-2"),
("soit 46,4 %","wa67d2b-29"),
("Le protocole recommandé est l'algorithme 0 h/1 h","wcdaf96-39"),
("mais au moins 1 heure après le début de la douleur","wcdaf96-39"),
("Un patient sur 300 suspect d'infarctus présente un arrêt cardiaque pendant son transport vers l'hôpital","wcdaf96-8"),
("Le traitement débute à 25 mg par jour, puis passe à 50 mg par jour après une semaine","aips-69307-6"),
("est débuté à 5 mg par jour la première semaine","aips-62641-5"),
("avec une valeur prédictive négative de 98,1 % dans une étude suisse portant sur 121 patients","w3b9dd1-4"),
]
for f in sorted(glob.glob('p*.html')):
    s=open(f).read();o=s
    for t,i in ADD:
        s=s.replace(t+".",t+c(i)+".")
    s=s.replace("La dose passe ensuite à 10 mg par jour, avec un maximum de 20 mg une fois par jour selon la réponse","La dose est ensuite portée à 10 mg par jour, avec un maximum de 20 mg une fois par jour selon la réponse")
    s=s.replace("Il recherche une dyspnée, une hyperthermie, une tachyarythmie, une asymétrie tensionnelle, un frottement péricardique, un souffle cardiaque, un foyer pulmonaire, une douleur à la palpation du thorax, des signes de phlébite et une atteinte neurologique","Il recherche une dyspnée, une hyperthermie, une tachyarythmie, une asymétrie tensionnelle, un frottement péricardique et un souffle cardiaque. Il recherche aussi un foyer pulmonaire, une douleur à la palpation du thorax, des signes de phlébite et une atteinte neurologique")
    s=s.replace("Le diagnostic initial de syndrome de la paroi thoracique a été abandonné chez 16 patients, pour une œsophagite (7), une anxiété ou somatisation (4), une maladie coronarienne (3), un cancer du poumon (1) ou des métastases pariétales (1)","Le diagnostic initial de syndrome de la paroi thoracique a été abandonné chez 16 patients. Les diagnostics finaux étaient une œsophagite (7), une anxiété ou somatisation (4), une maladie coronarienne (3), un cancer du poumon (1) ou des métastases pariétales (1)")
    s=s.replace("des palpitations, une douleur thoracique, des sueurs, des tremblements, des vertiges, des bouffées de chaleur, des nausées et un essoufflement","des palpitations, une douleur thoracique, des sueurs, des tremblements, des vertiges, des nausées et un essoufflement")
    if s!=o: open(f,'w').write(s)
# arbre
s=open('p10.html').read()
lab={"Nœud 1 :":"Nœud A :","Nœud 2 :":"Nœud B :","Nœud 2.1 :":"Nœud B.a :","Nœud 2.2 :":"Nœud B.b :","Nœud 2.2.1 :":"Nœud B.b.a :","Nœud 2.2.2 :":"Nœud B.b.b :","Nœud 3 :":"Nœud C :","Nœud 3.1 :":"Nœud C.a :","Nœud 3.2 :":"Nœud C.b :","Nœud 3.3 :":"Nœud C.c :","Nœud 4 :":"Nœud D :","Nœud 4.1 :":"Nœud D.a :","Nœud 4.1.1 :":"Nœud D.a.a :","Nœud 4.1.2 :":"Nœud D.a.b :","Nœud 4.2 :":"Nœud D.b :","Nœud 5 :":"Nœud E :","Nœud 6 :":"Nœud F :","Nœud 6.1 :":"Nœud F.a :","Nœud 6.2 :":"Nœud F.b :","Nœud 6.3 :":"Nœud F.c :","Nœud 7 :":"Nœud G :"}
for a,b in lab.items(): s=s.replace("<li>"+a,"<li>"+b)
s=s.replace("est enregistré dans les 10 minutes et la hs-cTn est dosée à l'admission<","est enregistré dans les 10 minutes et la hs-cTn est dosée à l'admission<")
open('p10.html','w').write(s)

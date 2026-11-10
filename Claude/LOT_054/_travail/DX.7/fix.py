import re
def rs(f,start,new,endtok=']].'):
    p='src/'+f; t=open(p).read()
    i=t.find(start)
    if i<0: print('MISS',f,start[:50]); return
    j=t.find(endtok,i)
    if endtok==']].': j+=3
    t=t[:i]+new+t[j:]
    open(p,'w').write(t)
def rp(f,a,b):
    p='src/'+f; t=open(p).read()
    if a not in t: print('MISS',f,a[:50]); return
    open(p,'w').write(t.replace(a,b,1))
# p01
rs('p01.src','La classification de l’Organisation mondiale de la santé (OMS) sert','La classification de l’Organisation mondiale de la santé (OMS) est la référence mondiale pour le diagnostic des tumeurs lymphoïdes depuis sa troisième édition[[w4b6ce9-2]].')
rp('p01.src','Il est défini par une morphologie à grandes cellules','Il est défini, en effet, par une morphologie à grandes cellules')
rp('p01.src','Ces trois entités illustrent trois comportements opposés.','Ces trois entités illustrent trois comportements opposés, car chacune évolue à son propre rythme.')
# p02
rs('p02.src','En Suisse, la Ligue contre le cancer rapporte','En Suisse, la Ligue contre le cancer rapporte environ 1’700 nouveaux cas de lymphome non hodgkinien par année pour la période 2018-2022[[w51201b-19|w51201b-7]]. Elle s’appuie sur l’Organe national d’enregistrement du cancer et sur l’Office fédéral de la statistique[[w51201b-1]].')
rs('p02.src','Le lymphome non hodgkinien est le septième cancer','Le lymphome non hodgkinien est le septième cancer par ordre de fréquence en Suisse[[w51201b-7|w51201b-19]]. Il vient après les cancers de la prostate, du sein, du poumon, du côlon, de la peau (mélanome) et du pancréas[[w51201b-7|w51201b-19]].')
rs('p02.src','Le Manuel MSD rappelle toutefois','Le Manuel MSD rappelle toutefois qu’environ 1% des adénopathies non différenciées vues en médecine générale impliquent un cancer[[w201626-8]]. Ce chiffre monte à 4% chez les patients de plus de 40 ans, car l’âge augmente le risque de cancer[[w201626-8]].')
rp('p02.src','Le point 12 reprend ces mesures.','Le point 12 reprend ces mesures, car elles relèvent de la prévention.')
rp('p02.src','Il précède le cancer de la vessie, les leucémies et le cancer du rein[[w51201b-7]]. Cela en fait','Il précède le cancer de la vessie, les leucémies et le cancer du rein[[w51201b-7]]. Ainsi, cela en fait')
rp('p02.src','Cela montre que le traitement de référence','Cela montre donc que le traitement de référence')
# p03
rs('p03.src','La cellule tumorale d’un lymphome B naît','La cellule tumorale d’un lymphome B naît d’un lymphocyte B normal dont la maturation est bloquée à un stade donné, ce qui explique les sous-types décrits ci-dessous[[w4b6ce9-51]].')
rs('p03.src','Le sous-type de type centre germinatif (GCB) présente','Le sous-type de type centre germinatif (GCB) présente un profil d’expression génique proche d’une cellule de centre germinatif[[w4b6ce9-51]]. Il est enrichi en translocation IGH::BCL2 ainsi qu’en mutations de gènes comme EZH2, KMT2D, TNFRSF14, B2M et CREBBP[[w4b6ce9-51]].')
rs('p03.src','Pour le Burkitt, le HUG cite','Pour le Burkitt, le HUG cite l’atteinte du tube digestif, des reins et des ovaires[[w959b4b-6]]. Il cite aussi l’atteinte du système nerveux central et de la moelle, ce qui montre que la tumeur se dissémine hors des ganglions[[w959b4b-6]].')
rs('p03.src','Le HUG décrit un patient de 35 ans','Le HUG décrit un patient de 35 ans en insuffisance rénale aiguë après un premier cycle R-CHOP[[w959b4b-2]]. Sa créatinine est à 750 µmol/l, son acide urique à 900, son potassium à 6.2 mmol/l, et il présente un œdème aigu du poumon[[w959b4b-2]].')
rs('p03.src','Le taux de cellules B périphériques chute','Le taux de cellules B périphériques chute en effet au-dessous de la valeur normale après la première dose[[aips-65813-67]].')
rp('p03.src','Cet exemple montre comment','Cet exemple montre, en effet, comment')
# p04
rs('p04.src','Le lymphome non hodgkinien occupe le rang E5','Le lymphome non hodgkinien occupe le rang E5 de cette situation (🚩), car il vient après l’anévrisme de l’aorte abdominale (E1) et le cancer colorectal (E2).')
rs('p04.src','Le cancer colorectal peut se présenter','Le cancer colorectal peut se présenter comme une masse du flanc ou de la fosse iliaque, avec un trouble du transit ou une anémie. Il se confirme par la coloscopie et la biopsie.',endtok='biopsie.')
rp('p04.src','Il se confirme par la coloscopie et la biopsie..','Il se confirme par la coloscopie et la biopsie.')
rp('p04.src','Un taux supérieur à deux fois','Ainsi, un taux supérieur à deux fois')
# p05
rs('p05.src','Le HUG qualifie les lymphomes agressifs','Le HUG qualifie les lymphomes agressifs d’urgence fréquente[[w959b4b-6]]. Cette urgence peut associer symptômes B, faillite médullaire, insuffisance rénale aiguë, compression médullaire, syndrome cave supérieur et tamponnade[[w959b4b-6|w959b4b-7]].')
# p06
rs('p06.src','Le Manuel MSD classe parmi les signes d’alarme','Le Manuel MSD classe parmi les signes d’alarme un ganglion cervical ou inguinal de plus de 2 cm[[w201626-25]]. Il y range aussi tout ganglion palpable sus-claviculaire ou axillaire quelle que soit sa taille, ainsi qu’un ganglion fistulisé, dur ou fixé[[w201626-25]].')
# p07
rs('p07.src','Le Burkitt abdominal, avec atteinte','Le Burkitt abdominal est la forme la plus explosive, car il atteint le tube digestif, les reins et les ovaires[[w959b4b-5|w959b4b-6]].')
rp('p07.src','Le syndrome tumoral abdominal associe','Le syndrome tumoral abdominal associe')
rp('p07.src','Le mécanisme est l’accumulation','Son mécanisme est donc l’accumulation')
rp('p07.src','Il traduit la réaction de l’hôte','Il traduit la réaction de l’hôte, car les cellules tumorales provoquent une réponse inflammatoire')
rp('p07.src','Le syndrome de lyse tumorale est biologique avant d’être clinique.','Le syndrome de lyse tumorale est biologique avant d’être clinique, car les anomalies du sang précèdent les symptômes.')
rp('p07.src','Les patients atteints de leucémie lymphoïde chronique ou de lymphome présentent un déficit immunitaire complexe.','Les patients atteints de leucémie lymphoïde chronique ou de lymphome présentent un déficit immunitaire complexe, si bien que les infections sont fréquentes.')
# p08
rs('p08.src','Le CHUV indique que le diagnostic repose','Le CHUV indique que le diagnostic repose sur les symptômes et sur des examens spécifiques[[w99af14-5]]. Ces examens comprennent généralement une prise de sang, la biopsie d’un ganglion lymphatique, une ponction de moelle osseuse et, si nécessaire, une ponction lombaire[[w99af14-5]].')
rs('p08.src','La classification OMS de cinquième édition conserve','La classification OMS de cinquième édition conserve deux sous-types de DLBCL sans autre précision, le type GCB et le type ABC[[w4b6ce9-51]]. Elle crée aussi de nouvelles catégories, comme le lymphome à grandes cellules B des sites immunoprivilégiés[[w4b6ce9-56]].')
rs('p08.src','Une biopsie de moelle osseuse n’est plus','Une biopsie de moelle osseuse n’est plus indiquée pour la stadification de routine du lymphome de Hodgkin et de la plupart des DLBCL[[wa42798-4]].')
rs('p08.src','Quel que soit le stade, la pratique','Quel que soit le stade, la pratique générale distingue la maladie limitée (stades I et II sans masse volumineuse) de la maladie avancée (stades III et IV)[[wa42798-5]]. Le stade II avec masse volumineuse est classé selon l’histologie et plusieurs facteurs pronostiques[[wa42798-5]].')
rs('p08.src','Le NCCN-IPI retient cinq','Le NCCN-IPI retient cinq prédicteurs : l’âge, la LDH, les sites atteints, le stade d’Ann Arbor et le statut de performance ECOG[[w3dee55-3]]. Il attribue au plus 8 points et forme quatre groupes de risque[[w3dee55-3]].')
rp('p08.src','Elle a été établie lors','Elle a été établie, en effet, lors')
rp('p08.src','Quel que soit le stade','Quel que soit le stade')
# p09
rs('p09.src','Le HUG exige un tissu frais','Le HUG exige un tissu frais et une coordination entre le chirurgien ou le radiologue, le pathologue spécialisé et l’onco-hématologue[[w959b4b-3]]. Il rappelle que plus de 70 anticorps sont utilisés en routine pour le phénotype[[w959b4b-3]].')
rs('p09.src','Le HUG insiste sur la prophylaxie','Le HUG insiste sur la prophylaxie du système nerveux central dans le Burkitt, car la tumeur envahit ce système[[w959b4b-6]].')
rp('p09.src','Le prélèvement porte de préférence','Le prélèvement porte de préférence')
# p12
rs('p12.src','Aucun facteur de risque modifiable','Aucun facteur de risque modifiable n’explique la majorité des lymphomes, si bien que la prévention primaire reste limitée[[w4b6ce9-62]].')
rs('p12.src','La prévention primaire consiste à traiter','La prévention primaire consiste à traiter les infections qui favorisent certains lymphomes[[w959b4b-5]]. L’infection par le VIH accroît le risque de Burkitt, et l’EBV joue un rôle essentiel au début de sa pathogenèse[[w959b4b-5|w4b6ce9-62]].')
rs('p12.src','Le HUG parle d’« exemple de prévention tertiaire','Le HUG parle d’« exemple de prévention tertiaire » à propos du lymphome de Hodgkin[[w959b4b-14]]. Il cite les cancers secondaires, l’excès d’infarctus lié aux anthracyclines et à la radiothérapie médiastinale, l’hypothyroïdie, la toxicité pulmonaire de la bléomycine et la stérilité[[w959b4b-14]].')
rp('p12.src','La prévention tertiaire vise les rechutes','La prévention tertiaire vise les rechutes')
# p14
rp('p14.src','Cette section transforme les pièges classiques en questions d’examen.','Cette section transforme les pièges classiques en questions d’examen, car la réponse doit être justifiée.')

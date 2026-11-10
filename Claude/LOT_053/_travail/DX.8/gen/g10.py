from common import *
p=Pt(10)
p.P("""L'arbre ci-dessous suit l'ordre de gravité décroissante et part du patient qui présente un côlon distendu. Chaque nœud est un signe, un examen ou une action, et chaque embranchement se lit « si X, alors Y ».""")
tree = """<ul>
<li>Si un péritonisme, un pneumopéritoine, une nécrose pariétale ou une pneumatose existe, alors le patient relève de la chirurgie{w1306ed-1 w1306ed-6}.</li>
<li>Si le patient est en choc ou instable, alors la réanimation précède l'imagerie, car l'ischémie et la perforation menacent{w1306ed-5}.</li>
<li>Si le patient est stable, alors un scanner injecté exclut une obstruction mécanique{wd21b7d-179}.
<ul>
<li>Si un obstacle mécanique existe, alors le patient relève de la leçon sur l'occlusion mécanique{wd21b7d-178}.</li>
<li>Si un volvulus existe, alors le sigmoïde se traite par colo-exsufflation, et le cæcum par chirurgie d'emblée{w1306ed-11}.</li>
<li>Si un mégacôlon toxique est évoqué, alors le patient sort de cette filière et relève de la leçon correspondante{w72d527-3}.</li>
<li>Si le scanner montre un côlon dilaté sans obstacle, alors on retient la pseudo-obstruction{wd21b7d-179}.
<ul>
<li>Dans tous les cas, on traite les causes réversibles : médicaments freinants, ionogramme, jeûne et mobilisation{wd21b7d-184 w1306ed-6}.</li>
<li>Si le cæcum mesure moins de 12 cm, si le patient est stable et si le ventre n'est pas péritonique, alors le traitement conservateur se poursuit 48 à 72 heures{wd21b7d-183}.</li>
<li>Si le cæcum dépasse 12 cm ou en cas d'échec, alors on envisage la néostigmine ou l'endoscopie{wd21b7d-186 wd21b7d-185}.
<ul>
<li>Si la néostigmine est contre-indiquée ou inefficace, alors la colonoscopie décompressive prend le relais{wd5dad6-6 wd24a99-9}.</li>
<li>Si le cæcum dépasse 10 à 12 cm d'emblée, alors le protocole vaudois propose l'exsufflation immédiate{w1306ed-10}.</li>
</ul></li>
<li>Si la dilatation se résout, alors un polyéthylèneglycol par voie orale prévient la récidive{wd21b7d-187}.</li>
<li>Si toutes les mesures échouent ou si une détérioration survient chez un patient apte, alors la chirurgie est envisagée{wd21b7d-189}.</li>
<li>Si le patient est à très haut risque opératoire, alors la caecostomie percutanée est une option à forte morbidité{wd21b7d-191}.</li>
</ul></li>
</ul></li>
</ul>"""
p.out.append(cite(tree))
p.P("""Cet arbre montre que la néostigmine et la colonoscopie se partagent la deuxième ligne, tandis que la chirurgie ferme la liste. Le choix entre les deux premières dépend des contre-indications du médicament, de la disponibilité de l'endoscopie d'urgence et de l'expertise locale{wd21b7d-188}.""")
p.save()

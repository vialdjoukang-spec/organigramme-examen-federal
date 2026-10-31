import gzip
from html import escape
from format_lecon import R,paras
def raw(n):return gzip.open(R/f'ressources_ia/aips/fi_fr/{n}.txt.gz','rt').read()
def q(n,s):
 assert s in raw(n),(n,s)
 return '<blockquote><p>« '+escape(s)+' »</p></blockquote>'
def line(n,prefix):return next(s for s in raw(n).splitlines() if s.startswith(prefix))
def segment(n,a,b):
 t=raw(n);i=t.index(a);return t[i:t.index(b,i)].strip()
def ketotifene(l):
 t=paras('Zaditen Ophtha/-SDU, information professionnelle suisse n°55341. Cette spécialité est indiquée pour la conjonctivite allergique saisonnière. Ne pas étendre automatiquement cette indication à une rougeur due aux lentilles, à une infection ou à toutes les allergies chroniques.')
 t+=q('55341',segment('55341','Adultes et enfants à partir de 3 ans','Mode d ’ administration'))
 t+=paras('La durée maximale suisse est de six semaines, même si un tableau de classe du protocole HUG indique deux mois. Aucun schéma chez l’enfant de moins de trois ans n’est proposé ici.')
 t+=q('55341',line('55341','Hypersensibilité au kétotifène'))
 t+=q('55341',line('55341','Zaditen Ophtha ne doit pas être utilisé'))
 t+=q('55341',segment('55341','On ne dispose d ’ aucune donnée concernant l ’ application','Fertilité'))
 t+=paras('Les unidoses ne contiennent pas le conservateur du flacon multidose. Le chlorure de benzalkonium de ce dernier peut irriter la surface oculaire et altérer les lentilles souples ; retirer celles-ci, avec délai de réinsertion d’au moins quinze minutes selon la notice. Ce délai ne donne pas la permission de reporter des lentilles sur un œil inflammatoire ou infecté.', 'Éviter le contact de l’embout avec l’œil. Espacer d’au moins cinq minutes les autres traitements ophtalmiques selon cette notice. Attendre la disparition du flou visuel avant de conduire ; interrompre et réévaluer en cas de réaction allergique ou aggravation.')
 return l.subwindow('ketotifene','Kétotifène : indication saisonnière et durée suisse',t,(1,5))
def carbomere(l):
 t=paras('Viscotears/-SDU, carbomère, information professionnelle n°48624. Exemple de substitution lacrymale pour sécheresse et film lacrymal altéré. Un lubrifiant ne traite pas une infection, une plaie ou une crise de fermeture de l’angle.')
 t+=q('48624',segment('48624','Adultes\nLa fréquence d\'utilisation est déterminée','Contre-indications'))
 t+=q('48624',line('48624',"Hypersensibilité connue à l'un"))
 t+=q('48624',segment('48624','Grossesse\nAucune étude contrôlée','Effet sur l’aptitude'))
 t+=paras('La notice ne dispose pas d’efficacité et de sécurité établies chez l’enfant et l’adolescent. Elle décrit un risque d’exposition faible pendant grossesse et allaitement, ce qui ne remplace pas l’évaluation clinique.', 'Le gel doit être utilisé hors port de lentilles ; celles-ci sont retirées, avec attente d’environ quinze minutes selon la notice avant remise. Un œil rouge chez un porteur de lentilles reste à examiner ; le soulagement ne suffit pas à exclure une kératite.', 'Ne pas toucher l’embout. La vision peut être temporairement floue ; attendre qu’elle soit normale pour conduire. Douleur, modification de vision, rougeur persistante ou absence d’amélioration demandent arrêt et réévaluation. Le gel est administré en dernier selon sa notice ; toute association avec un autre produit ayant des contraintes d’ordre doit être précisée par le prescripteur.')
 return l.subwindow('carbomere','Carbomère : exemple de lubrification et limites',t,(6,))
def azithromycine(l):
 t=paras('Azyter, azithromycine en récipient unidose, information professionnelle suisse n°68519. Exemple pour conjonctivite bactérienne purulente à germe sensible lorsque le traitement est indiqué. Cette autorisation ne transforme pas toute rougeur ou sécrétion en indication antibiotique.')
 t+=q('68519',segment('68519','Adultes:\nInstiller','Mode d\'administration'))
 t+=q('68519',line('68519','Hypersensibilité à la substance active'))
 t+=q('68519',segment('68519','\nUtilisation chez les nouveau-nés\n','Interactions'))
 t+=q('68519',segment('68519','Grossesse\nAucun effet','Fertilité'))
 t+=paras('La mention pédiatrique de la notice ne justifie pas une prise en charge autonome d’un nouveau-né. Gonocoque, infection néonatale à chlamydia ou suspicion d’infection systémique imposent un parcours spécifique et souvent un traitement systémique. Le traitement n’est pas une prophylaxie néonatale.', 'Ne pas prolonger au-delà des trois jours en raison de seuls signes résiduels ; en l’absence d’amélioration, reconsidérer le diagnostic. Douleur, baisse visuelle ou aggravation imposent une évaluation plus tôt. La kératite infectieuse ne se traite pas automatiquement par ce schéma de conjonctivite.', 'Mains propres, embout sans contact, unidose jetée après utilisation. Ne pas injecter ni avaler. Arrêter devant hypersensibilité ; brûlure et flou transitoire sont possibles. Ne pas porter de lentilles pendant la conjonctivite bactérienne.')
 t+=q('68519',line('68519','En cas de traitement concomitant par un autre collyre'))
 t+=paras('Les exemples de cette leçon sont des options pour des indications différentes, pas une association à administrer ensemble. L’ordre et l’espacement de plusieurs produits doivent être prescrits explicitement.')
 return l.subwindow('azithromycine','Azithromycine : schéma suisse pour conjonctivite',t,(1,2,3,7))
def exemples(l):return paras(ketotifene(l),carbomere(l),azithromycine(l))

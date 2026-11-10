from h import *

def p08x():
    p = Pt(8); p.k = 3
    o = [H4("8.b Seuils de classement et performances des critères")]
    o.append(p.P(
        S("Selon les critères Duke-ISCVID comme selon les critères ESC 2023, le diagnostic est certain lorsque deux critères majeurs, ou un critère majeur et trois critères mineurs, sont remplis", 'w2812c6-7'),
        S("Dans de rares cas, cinq critères mineurs sans critère majeur suffisent aussi à parler d'endocardite certaine", 'w2812c6-7'),
        S("Les critères Duke-ISCVID comptent trois critères majeurs, contre deux dans les nouveaux critères ESC", 'w2812c6-8')))
    o.append(p.P(
        S("Les " + p.w("germes typiques", fp(
            S("Un germe typique est un microorganisme dont, si deux hémocultures positives sont obtenues, elles forment un critère majeur de microbiologie", 'w2812c6-8'),
            S("Staphylococcus lugdunensis et Abiotrophia sont typiques quelle que soit la présence de matériel prothétique", 'w453fd0-31'),
            S("Staphylococcus epidermidis et Candida ne sont typiques que chez les porteurs de valve prothétique", 'w453fd0-31'))) +
          " ont été élargis : les critères Duke-ISCVID ont supprimé l'exigence de délai entre les hémocultures et ont ajouté plusieurs germes", 'w7f9670-8'),
        S("Tous les streptocoques sont désormais typiques, sauf Streptococcus pyogenes et Streptococcus pneumoniae, alors que seuls les streptocoques viridans et S. bovis l'étaient auparavant", 'w7f9670-34'),
        S("Les conditions prédisposantes comprennent aussi la bicuspidie aortique, l'endocardite antérieure, la cardiomyopathie hypertrophique et une régurgitation valvulaire plus que légère", 'w453fd0-195'),
        S("La preuve pathologique peut maintenant reposer sur la PCR, le séquençage et l'hybridation in situ", 'w7f9670-8')))
    o.append(p.P("Le tableau suivant permet de suivre l'évolution des critères jusqu'aux critères actuels."))
    o.append(T(["Version", "Principaux changements"], [
        ["Duke 1994" + c('w453fd0-191'), "Germes typiques, échographie, fièvre d'au moins 38 °C, phénomènes vasculaires et immunologiques"],
        ["Duke modifié 2000" + c('w453fd0-192'), "Bactériémie persistante définie, sérologie de Coxiella burnetii majeure"],
        ["ESC 2015" + c('w453fd0-193'), "TEP au FDG ou scanner comme critère majeur sur prothèse"],
        ["ESC 2023" + c('w453fd0-194'), "E. faecalis typique, phénomènes vasculaires élargis à la spondylodiscite et aux emboles silencieux"],
        ["Duke-ISCVID 2023" + c('w453fd0-195'), "Liste élargie de germes, preuve anatomopathologique, rôle accru du TEP"],
    ]))
    o.append(p.P(
        S("Chez les porteurs d'un dispositif électronique, la sensibilité atteint 97,1 % pour Duke-ISCVID 2023 et 93,8 % pour ESC 2023, mais la spécificité tombe à 31,1 % et à 41,0 %", 'w453fd0-27'),
        S("Ces critères captent donc plus de cas, au prix de classements faussement certains lorsque du matériel intracardiaque est présent", 'w453fd0-32'),
        S("Dans une cohorte de bactériémies à entérocoques de deux centres suisses, 146 épisodes sont certains selon Duke-ISCVID, contre 116 selon ESC 2015 et 133 selon ESC 2023", 'wb63926-30', 'wb63926-44'),
        S("Le gain de sensibilité vient surtout de E. faecalis devenu typique, au prix d'une spécificité réduite", 'wb63926-45')))
    return ''.join(o)

def p09x():
    p = Pt(9); p.k = 0
    o = [H4("9.e Précisions d'imagerie et de microbiologie")]
    o.append(p.P(
        S("Les recommandations européennes font de l'échographie transœsophagienne une indication de classe I, niveau C, chez tout patient suspect, même si l'échographie transthoracique est positive", 'w2812c6-6'),
        S("Seule l'endocardite native droite isolée peut échapper à cette règle, avec un examen transthoracique de bonne qualité et des images sans équivoque", 'w2812c6-6'),
        S("Dans l'endocardite native, l'échographie transœsophagienne bidimensionnelle atteint une sensibilité de 90 % à 100 % et sert de référence", 'w453fd0-63'),
        S("Sur prothèse, l'ombre acoustique peut abaisser la sensibilité de l'échographie transthoracique à 40 % à 70 %", 'w453fd0-63')))
    o.append(p.P(
        S("Le scanner cardiaque atteint une sensibilité de 100 % pour les pseudo-anévrismes", 'w453fd0-72'),
        S("Le " + p.w("TEP au FDG", fp(
            S("Le TEP au FDG montre une fixation métabolique intense, focale ou multifocale et hétérogène, au contact d'une valve ou d'un dispositif", 'wb6a5b9-21'),
            S("L'examen exige une glycémie inférieure à 180 mg/dL, car le glucose entre en compétition avec le FDG", 'w453fd0-210'))) +
          " a une sensibilité de 31 % sur valve native, de 86 % sur prothèse et de 72 % sur dispositif", 'w453fd0-75'),
        S("Il se réalise le plus tôt possible, idéalement avant les antibiotiques ou au plus tard durant la première semaine, car sa valeur prédictive négative baisse après plusieurs semaines de traitement", 'w453fd0-80'),
        S("Après une chirurgie valvulaire récente, on diffère le TEP d'au moins trois mois pour limiter les faux positifs", 'w453fd0-80'),
        S("Une fixation extracardiaque évoquant des emboles septiques de la rate, des poumons ou du système ostéo-articulaire peut renforcer la suspicion", 'w453fd0-79')))
    o.append(p.P(
        S("Par ailleurs, la scintigraphie aux leucocytes marqués a une spécificité proche de 100 %, mais une sensibilité d'environ 60 %", 'w453fd0-88'),
        S("Les hémocultures négatives viennent d'un antibiotique préalable ou de germes à croissance difficile comme Coxiella burnetii, Bartonella et le groupe HACEK", 'w453fd0-21'),
        S("Dans ce cas, la PCR 16S sur une valve excisée améliore la détection du germe", 'w453fd0-21')))
    return ''.join(o)

def p10x():
    p = Pt(10)
    o = [p.P(S("La branche chirurgicale de l'arbre s'organise selon l'indication et le délai", 'w2812c6-9'))]
    o.append(UL(
        S("Si le patient présente une insuffisance cardiaque, une infection non contrôlée ou un risque d'embolie, alors la chirurgie se discute", 'w2812c6-9'),
        S("Si la chirurgie est jugée urgente, alors elle se fait dans les 3 à 5 jours, sans attendre l'équipe d'endocardite", 'w2812c6-9'),
        S("Si une endocardite prothétique survient dans les six mois après une chirurgie valvulaire, alors une nouvelle chirurgie est recommandée", 'w2812c6-12'),
        S("Si l'endocardite sur dispositif est certaine, alors l'extraction complète se fait sans délai", 'w2812c6-14'),
        S("Si le centre n'a pas de chirurgie cardiaque, alors un transfert rapide s'organise, idéalement en 24 à 48 h dans les cas urgents", 'w453fd0-109')))
    return ''.join(o)

def p11x():
    p = Pt(11); p.k = 5
    o = [H4("Chirurgie, dispositifs et durées selon les recommandations européennes")]
    o.append(p.P(
        S("En effet, trois catégories motivent la chirurgie : l'insuffisance cardiaque, l'infection non contrôlée et la prévention des embolies", 'w2812c6-9'),
        S("La chirurgie urgente se définit désormais comme réalisée dans les 3 à 5 jours, sans attendre l'équipe d'endocardite", 'w2812c6-9'),
        S("Pour la taille des végétations, les recommandations 2023 ne distinguent plus que celles de plus de 10 mm", 'w2812c6-10'),
        S("Une chirurgie urgente peut être envisagée en classe IIb pour une végétation gauche d'au moins 10 mm, sans dysfonction valvulaire sévère ni embolie et avec un risque opératoire bas", 'w2812c6-10'),
        S("Une endocardite prothétique précoce, survenue dans les six mois après la chirurgie, relève d'une chirurgie de classe I, niveau C, avec nouveau remplacement et débridement complet", 'w2812c6-12'),
        S("Environ 25 % à 50 % des patients sont finalement opérés", 'w453fd0-113'),
        S("La mortalité à 30 jours après chirurgie atteint 10,2 %, et elle monte jusqu'à 30 % en urgence", 'w453fd0-53')))
    o.append(p.P(
        S("Pour une endocardite certaine sur dispositif, l'extraction complète du système est recommandée sans délai, en classe I, niveau B", 'w2812c6-14'),
        S("Cette formule n'implique pas forcément une urgence", 'w2812c6-14'),
        S("L'extraction percutanée transveineuse est la méthode de première intention, et l'on discute une chirurgie ouverte pour des végétations de plus de 20 mm", 'w453fd0-43'),
        S("Une réimplantation éventuelle se fait à distance du site précédent, après des hémocultures négatives pendant au moins 72 h sans végétation, et pendant au moins 2 semaines si des végétations étaient visibles", 'w2812c6-16')))
    o.append(p.P(
        S("Le traitement intraveineux hospitalier durait traditionnellement de 4 à 6 semaines", 'w453fd0-89'),
        S("Après extraction d'un dispositif, les antibiotiques ciblés se poursuivent par voie intraveineuse pendant 4 à 6 semaines", 'w453fd0-46'),
        S("Ce traitement peut être raccourci à 2 semaines si l'échographie transœsophagienne ne montre aucune atteinte valvulaire, si les hémocultures se stérilisent vite et si l'amélioration est rapide", 'w453fd0-46'),
        S("La durée totale ne doit jamais descendre sous 4 semaines en cas d'infection systémique", 'w453fd0-46'),
        S("Dans l'infection systémique d'un dispositif, une association intraveineuse est obligatoire, et la rifampicine s'ajoute en présence de matériel prothétique", 'w453fd0-45')))
    o.append(p.P(
        S("La phase aiguë est résolue après plus de 3 semaines pour une valve native ou prothétique et plus de 2 semaines pour un dispositif, ce qui autorise un traitement ambulatoire", 'w453fd0-91'),
        S("L'antibiothérapie empirique peut débuter après les hémocultures, puis s'adapte aux résultats de culture", 'w453fd0-44'),
        S("Les Néerlandais recommandent l'amoxicilline orale pour l'endocardite native à streptocoques viridans sensibles à la pénicilline", 'w2812c6-19'),
        S("Un hôpital sans chirurgie cardiaque doit pouvoir transférer un patient vers un centre chirurgical, idéalement en 24 à 48 h dans les cas urgents", 'w453fd0-109'),
        S("Les indications de transfert rapide comprennent la chirurgie urgente, l'œdème pulmonaire par dysfonction valvulaire et l'infection non contrôlée", 'w453fd0-110')))
    return ''.join(o)

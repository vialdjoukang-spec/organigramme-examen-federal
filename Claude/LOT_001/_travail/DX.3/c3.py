from h import *

def p08():
    p = Pt(8)
    o = []
    o.append(p.P(
        S("Le diagnostic positif s'appuie sur les critères Duke-ISCVID 2023, qui conservent le format des critères de Duke avec des critères majeurs d'imagerie et de microbiologie, complétés par des critères mineurs", 'w0e265d-5'),
        S("Cependant, les critères de Duke, introduits en 1994, ont une sensibilité globale d'environ 80 %", 'wc68439-13'),
        S("Chaque épisode est classé comme rejeté, possible ou certain, et le classement guide la suite de la prise en charge", 'w0c22e5-19')))
    o.append(H4("8.a Ce que les critères 2023 ont changé"))
    o.append(p.P(
        S("Enterococcus faecium n'est plus considéré comme un germe typique d'endocardite, de sorte que deux hémocultures positives à ce germe ne forment plus qu'un critère mineur", 'w0e265d-6'),
        S("À l'inverse, une bactériémie nosocomiale à Enterococcus faecalis avec foyer connu devient un critère majeur", 'w0e265d-8'),
        S("Le stimulateur cardiaque a été ajouté comme critère mineur, ce qui a fait passer un cas de possible à certain dans le registre suédois", 'w0e265d-7')))
    o.append(p.P(
        S("Dans ce registre, 14 épisodes sont passés de certains à possibles parce que l'espèce n'était plus jugée typique, alors que 13 de ces patients avaient des végétations à l'échographie", 'w0e265d-7'),
        S("Les auteurs en concluent que la sensibilité des critères diminue lorsque E. faecium est exclu des germes typiques", 'w0e265d-8')))
    o.append(p.P(
        S("L'imagerie nucléaire compte désormais : des foyers intenses, focaux ou multifocaux et hétérogènes de fixation du FDG, apparus au moins 3 mois après la chirurgie valvulaire, forment un critère majeur d'imagerie", 'wb6a5b9-21'),
        S("Ainsi, ce critère peut faire passer de nombreux cas d'endocardite prothétique suspectée de possible à certain", 'wb6a5b9-21'),
        S("Les phénomènes emboliques restent un critère mineur vasculaire : il était rempli dans 27 % des épisodes avant le TEP-scanner et dans 10 % de plus après lui", 'wa9c851-10')))
    o.append(p.P(
        S("Les recommandations européennes de 2023 ont aussi mis à jour les critères diagnostiques, intégré de nouvelles modalités d'imagerie et précisé l'indication d'une chirurgie précoce quand le risque embolique est élevé", 'wf45fc8-4')))
    o.append(p.P("Le tableau suivant permet de classer les critères selon leur usage."))
    o.append(T(["Famille de critères", "Contenu", "Usage"], [
        ["Majeurs de microbiologie" + c('w0e265d-5'), "Hémocultures positives à des germes typiques" + c('w0e265d-8'), "Confirment la bactériémie"],
        ["Majeurs d'imagerie" + c('w0e265d-5'), "Végétation, abcès, fixation du FDG" + c('wb6a5b9-21'), "Confirment la lésion"],
        ["Mineurs" + c('w0e265d-5'), "Dispositif, phénomènes vasculaires, E. faecium" + c('w0e265d-6'), "Complètent un cas possible"],
    ]))
    o.append(p.P(
        S("Aucun critère isolé ne suffit : le diagnostic combine la microbiologie, l'imagerie et la clinique, et un classement possible impose de poursuivre les examens", 'w0e265d-5', 'w0c22e5-19')))
    return ''.join(o)


def p09():
    p = Pt(9)
    o = []
    o.append(H4("9.a Gold standard"))
    o.append(p.P(
        S("Le diagnostic de certitude repose sur l'examen direct de la valve lors de la chirurgie ou de l'autopsie", 'w0c22e5-30'), S("Il comprend la culture de la végétation ou de l'abcès, test d'acide nucléique, histologie compatible et inspection macroscopique", 'w0c22e5-30'),
        S("Ainsi, dans la série lausannoise, 38 patients avaient une histologie compatible, 35 une culture positive et 16 un test d'acide nucléique positif", 'w0c22e5-30')))
    o.append(H4("9.b Première intention"))
    o.append(p.P(
        S("Les hémocultures constituent le premier examen : leur sensibilité dépend surtout du volume de sang prélevé, du remplissage correct des flacons et de leur nombre", 'wdb992c-1'),
        S("Les prélèvements précèdent donc l'antibiothérapie, avec un délai très court en cas de choc septique", 'wdb992c-6'),
        S("Les HUG recommandent deux paires, prélevées en un seul temps par une ponction veineuse périphérique, et jamais plus de 3 paires par jour", 'wdb992c-7', 'wdb992c-8')))
    o.append(p.P(
        S("Dans l'endocardite, deux paires initiales sont suivies d'une répétition au moins une heure plus tard avant les antibiotiques", 'wdb992c-11'), S("Un suivi quotidien documente ensuite la bactériémie continue et l'efficacité du traitement", 'wdb992c-11'),
        S("L'asepsie comprend trois applications d'antiseptique alcoolisé avec trois tampons stériles différents, et le flacon aérobie se remplit en premier", 'wdb992c-3', 'wdb992c-13')))
    o.append(p.P(
        S("L'échographie transthoracique est l'imagerie de première ligne, mais elle ne suffit pas, sauf pour une endocardite native droite isolée avec un examen de bonne qualité", 'wb6a5b9-8'),
        S("Sa sensibilité pour les végétations varie de 40 % à 63 %, alors que celle de l'échographie transœsophagienne atteint 85 % à 90 %", 'w0c22e5-11', 'wb6a5b9-9'),
        S("L'échographie transœsophagienne atteint une sensibilité d'environ 99 % pour la valve native, mais seulement 90 % pour les dispositifs", 'wb6a5b9-9')))
    o.append(H4("9.c Alternatives et situations particulières"))
    o.append(p.P(
        S("Lorsque l'échographie transœsophagienne est négative et que la suspicion persiste, l'imagerie complémentaire s'impose, car cet examen peut être faussement négatif lorsque les végétations sont petites", 'w0c22e5-13'),
        S("Le scanner cardiaque est plus précis que l'échographie transœsophagienne pour les abcès, les pseudo-anévrismes et les fistules", 'wb6a5b9-11'),
        S("Chez le patient avec dispositif ou prothèse, une échographie douteuse justifie un TEP-scanner au FDG", 'w0c22e5-14')))
    o.append(p.P(
        S("La scintigraphie aux leucocytes marqués ne demande aucune préparation, mais le protocole dure un à deux jours", 'wb6a5b9-18'),
        S("Par ailleurs, une méta-analyse de 2133 patients a trouvé des lésions ischémiques aiguës à l'IRM cérébrale dans 61,9 % des cas", 'wb6a5b9-15'), S("Elle a aussi trouvé des microsaignements dans 52,9 %, un abcès ou une méningite dans 9,5 % et un anévrisme mycotique dans 6,2 %", 'wb6a5b9-15')))
    o.append(H4("9.d Deuxième intention"))
    o.append(p.P(
        S("Lorsque la suspicion persiste malgré une imagerie négative ou douteuse, la répétition de l'échographie est recommandée après 5 à 7 jours par les Européens", 'w0c22e5-15'), S("Les Américains conseillent une échographie transœsophagienne après 7 à 10 jours", 'w0c22e5-15'),
        S("À Lausanne, une seconde échographie transthoracique a détecté de nouvelles végétations dans 7 % des épisodes et de nouvelles complications paravalvulaires dans 3 %", 'w0c22e5-6'), S("La sensibilité pour les végétations est passée de 47 % à 57 %", 'w0c22e5-6'),
        S("Elle n'a reclassé que 1 % des cas de possible à certain, donc l'imagerie plus sensible doit être préférée à la simple répétition", 'w0c22e5-6', 'w0c22e5-10')))
    o.append(p.P(
        S("Le TEP-scanner a détecté des embolies chez 12 % des patients, dont 8 % d'événements inconnus jusque-là, mais il n'a reclassé que 0,9 % des épisodes", 'wa9c851-9', 'wa9c851-10'),
        S("Il a aussi révélé de nouveaux foyers infectieux dans 6 % des épisodes, ce qui a prolongé l'antibiothérapie ou fait indiquer un contrôle de la source", 'wa9c851-11')))
    o.append(p.P("Le tableau suivant permet de relier le résultat à sa signification et à la conduite."))
    o.append(T(["Résultat", "Signification", "Conduite"], [
        ["Hémocultures positives persistantes" + c('wdb992c-11'), "Bactériémie continue", "Chercher un foyer endovasculaire"],
        ["Échographie transthoracique négative" + c('w0c22e5-11'), "N'exclut pas l'endocardite", "Échographie transœsophagienne" + c('wb6a5b9-8')],
        ["Abcès ou fistule suspectés" + c('wb6a5b9-11'), "Complication paravalvulaire", "Scanner cardiaque et avis chirurgical"],
        ["Fixation du FDG sur prothèse" + c('wb6a5b9-21'), "Critère majeur d'imagerie", "Classement certain"],
        ["Hémocultures négatives" + c('wc68439-16'), "Antibiotique préalable ou germe rare", "Sérologies et PCR"],
    ]))
    o.append(p.P(
        S("Une règle clinique peut aider à décider de l'échographie transœsophagienne dans la bactériémie à S. aureus", 'w318a1c-18'), S("L'échographie est faite chez tous, et l'on peut renoncer à la voie transœsophagienne si le score VIRSTA est inférieur à 3", 'w318a1c-18', 'w318a1c-20')))
    return ''.join(o)


def p10():
    p = Pt(10)
    o = []
    o.append(p.P(
        S("L'arbre décisionnel est organisé ainsi : exclusion des urgences d'abord, puis discrimination des diagnostics fréquents", 'wdb992c-6')))
    o.append(UL(
        S("Si le patient est en choc ou en sepsis, alors les hémocultures sont prélevées sans délai, puis l'antibiothérapie empirique démarre", 'wdb992c-6'),
        S("Si le patient est stable, alors deux paires d'hémocultures sont prélevées, puis répétées au moins une heure plus tard, avant tout antibiotique", 'wdb992c-11'),
        S("Si les hémocultures sont positives à S. aureus, alors une échographie est faite chez tous, et la voie transœsophagienne se discute selon le score VIRSTA", 'w318a1c-18', 'w318a1c-20'),
        S("Si l'échographie transthoracique est négative et que la suspicion persiste, alors l'échographie transœsophagienne s'impose", 'wb6a5b9-8'),
        S("Si l'échographie transœsophagienne reste douteuse et qu'il existe une prothèse ou un dispositif, alors le TEP-scanner au FDG est demandé", 'w0c22e5-14'),
        S("Si un abcès, une fistule ou un pseudo-anévrisme est suspecté, alors le scanner cardiaque précise la complication", 'wb6a5b9-11'),
        S("Si une insuffisance cardiaque, un abcès, une infection récidivante ou des embolies répétées apparaissent, alors une discussion chirurgicale s'impose", 'wa35a53-5'),
        S("Si les hémocultures restent négatives, alors on cherche un antibiotique préalable puis des germes à culture difficile par sérologie ou PCR", 'wc68439-16')))
    o.append(p.P(
        S("Cet arbre place l'équipe d'endocardite au centre : cardiologues, chirurgiens, infectiologues et microbiologistes discutent le cas ensemble", 'w37576c-33')))
    return ''.join(o)

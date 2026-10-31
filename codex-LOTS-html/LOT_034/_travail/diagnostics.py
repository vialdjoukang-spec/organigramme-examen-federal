from format_lecon import table
DIAGNOSTICS=[
('Syndrome d’apnées-hypopnées obstructives du sommeil de l’adulte','Fréquent ; gravité respiratoire et accidentelle.','Ronflement, pauses, étouffements, sommeil non réparateur ; somnolence inconstante.','Enregistrement du sommeil ; traitement et sécurité de conduite.'),
('Ronflement primaire','Usuel ; diagnostic après évaluation des troubles respiratoires.','Bruit nocturne isolé sans syndrome respiratoire démontré.','Mesures adaptées ; réévaluer si apparition de pauses ou de somnolence.'),
('Hypertrophie adénoamygdalienne de l’enfant','Cause pédiatrique usuelle ; obstruction parfois sévère.','Respiration buccale, pauses, agitation, énurésie ou troubles de croissance.','Évaluation pédiatrique et ORL ; traitement selon retentissement.'),
('Rhinite allergique','Usuelle ; peut coexister avec des apnées.','Obstruction fluctuante, prurit, éternuements, rhinorrhée claire.','Traitement ciblé de la rhinite ; ne pas lui attribuer toute somnolence.'),
('Déviation de la cloison nasale','Cause anatomique possible ; importance fonctionnelle variable.','Obstruction persistante, parfois après traumatisme.','Examen ORL ; septoplastie selon gêne et bilan, sans promesse de guérison des apnées.'),
('Polypose nasosinusienne','Inflammation chronique ; association possible à l’asthme.','Obstruction bilatérale et diminution de l’odorat.','Endoscopie et traitement local ; exclure une tumeur si unilatéralité.'),
('Rétrognathie mandibulaire','Facteur anatomique ; possible même sans obésité.','Mandibule en retrait et espace rétrolingual réduit.','Bilan sommeil et maxillo-facial ; orthèse ou chirurgie selon indication.'),
('Hypothyroïdie','Cause systémique à rechercher selon signes associés.','Frilosité, constipation, ralentissement, prise de poids.','Bilan hormonal ciblé ; substitution si indiquée et réévaluation du sommeil.'),
('Acromégalie','Rare ; complications générales importantes.','Modification des traits, des mains et des pieds ; sueurs, macroglossie.','Bilan endocrinien, imagerie hypophysaire et recherche d’apnées.'),
('Tumeur maligne nasosinusienne','🚩 Rare ; retard diagnostique à éviter.','Obstruction unilatérale progressive, épistaxis, douleur ou signes orbitaires.','Avis ORL rapide ; imagerie et prélèvement spécialisé.')]
def comparison():return table(['Diagnostic','Contexte et gravité','Orientation','Décision'],[[f'<a href="LOT_034_Phase_B_V0_DX.{i}.html">DX.{i} — {d[0]}</a>',*d[1:]] for i,d in enumerate(DIAGNOSTICS,1)])

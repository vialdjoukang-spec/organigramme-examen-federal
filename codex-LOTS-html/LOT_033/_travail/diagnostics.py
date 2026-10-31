from format_lecon import table
DIAGNOSTICS=[
('Conjonctivite virale non herpétique','Usuelle ; contagieuse.','Larmoiement, gêne, contage ; parfois un œil puis les deux.','Hygiène et soutien ; rechercher atteinte cornéenne si douleur ou photophobie.'),
('Conjonctivite bactérienne aiguë','Usuelle ; formes hyperpurulentes ou néonatales urgentes.','Sécrétions mucopurulentes et paupières collées, sans certitude étiologique isolée.','Évaluer gravité ; antibiotique ciblé si indiqué, pas pour tout œil rouge.'),
('Conjonctivite allergique','Usuelle sur terrain atopique.','Prurit bilatéral, larmoiement, exposition et rhinite.','Éviction et traitement local adapté ; exclure complication cornéenne.'),
('Sécheresse oculaire','Usuelle, multifactorielle.','Brûlure, sable, fluctuations et facteurs environnementaux.','Lubrification adaptée et recherche de cause ; alarme si baisse visuelle persistante.'),
('Blépharite','Usuelle, souvent chronique ou récidivante.','Bords palpébraux inflammatoires, croûtes, dysfonction des glandes.','Hygiène palpébrale et traitement selon cause.'),
('Hémorragie sous-conjonctivale','Souvent bénigne si spontanée et isolée.','Nappe rouge, sans baisse de vision ni douleur significative.','Contrôler contexte, pression artérielle et saignements ; traumatisme à évaluer.'),
('Kératite infectieuse','🚩 Menace visuelle.','Douleur, photophobie, infiltrat ou ulcère ; lentilles à risque.','Avis ophtalmologique urgent, prélèvements et traitement spécifique.'),
('Uvéite antérieure aiguë','🚩 Menace visuelle et complications.','Photophobie, douleur profonde, cercle périkératique ; pupille parfois petite.','Lampe à fente et avis urgent ; pas de corticoïde empirique.'),
('Crise aiguë de fermeture de l’angle','🚩 Urgence immédiate.','Douleur, baisse visuelle, halos, nausées ; pupille souvent en semi-mydriase.','Ophtalmologue immédiatement ; pression et mécanisme à confirmer.'),
('Sclérite','🚩 Inflammation profonde potentiellement menaçante.','Douleur intense profonde, rougeur et contexte systémique possible.','Avis spécialisé urgent ; distinguer épisclérite et infection.')]
def comparison():return table(['Diagnostic','Contexte et gravité','Orientation','Décision'],[[f'<a href="LOT_033_Phase_B_V0_DX.{i}.html">DX.{i} — {d[0]}</a>',*d[1:]] for i,d in enumerate(DIAGNOSTICS,1)])

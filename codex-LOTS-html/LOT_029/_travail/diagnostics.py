from format_lecon import table
DIAGNOSTICS=[
('Macrocéphalie familiale constitutionnelle','Périmètre élevé, trajectoire stable, développement et examen normaux.','Mesurer les parents ; le contexte familial ne neutralise pas un signe d’alarme.'),
('Élargissement bénin des espaces sous-arachnoïdiens du nourrisson','Macrocrânie et élargissement péricérébral caractéristique à l’imagerie.','Suivi développemental ; une collection sous-durale associée doit être explorée.'),
('Hydrocéphalie','Accumulation de liquide cérébrospinal avec dilatation ventriculaire.','🚩 Croissance rapide, fontanelle tendue ou troubles du regard : évaluation urgente.'),
('Hématome sous-dural','Collection sanguine intracrânienne, parfois macrocrânie progressive.','🚩 Évaluer gravité et cause, dont traumatisme accidentel ou infligé, sans conclusion automatique.'),
('Tumeur intracrânienne','Croissance céphalique anormale avec signes neurologiques, visuels ou endocriniens possibles.','🚩 Céphalées, vomissements et régression demandent un bilan orienté.'),
('Craniosténose','Fermeture prématurée d’une ou plusieurs sutures avec déformation caractéristique.','La forme compte même si le périmètre n’est pas petit ; avis spécialisé précoce.'),
('Microcéphalie primitive génétique','Petit périmètre congénital ou précocement révélé, développement variable.','Diagnostic moléculaire et accompagnement ; toute microcéphalie n’est pas de cette origine.'),
('Infection congénitale à cytomégalovirus','Microcéphalie possible avec atteintes neurologique, auditive ou systémique.','Diagnostic néonatal précoce et bilan d’extension ; ne pas attendre les séquelles.'),
('Troubles du spectre de l’alcoolisation fœtale','Atteinte neurodéveloppementale après exposition prénatale, microcéphalie possible.','Évaluation multidisciplinaire sans inférer une exposition à partir du seul périmètre.'),
('Syndrome des hamartomes tumoraux lié à PTEN','Macrocéphalie marquée, signes développementaux, cutanés ou vasculaires possibles.','Génétique et surveillance spécifique ; l’histoire familiale n’implique pas la bénignité.')]
def comparison():
 return table(['Diagnostic','Présentation utile','Vigilance'],[[f'<a href="LOT_029_Phase_B_V0_DX.{i}.html">DX.{i} — {a}</a>',b,c] for i,(a,b,c) in enumerate(DIAGNOSTICS,1)])

import json
S=lambda i:f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
C=[
("Pour l'œsophagite par reflux, la dose peut atteindre 40 mg par jour, voire 2 comprimés de 40 mg dans certains cas particuliers"+S('aips-59834-8')+".",
 "En règle générale, la dose est de 40 mg par jour ; elle pourra être doublée dans certains cas particuliers, comme l'œsophagite par reflux, soit 2 comprimés de 40 mg par jour"+S('aips-59834-8')+". En cas d'insuffisance hépatique sévère, la dose journalière est réduite à 20 mg"+S('aips-59834-11')+"."),
("Pendant l'allaitement, Nexium® ne doit pas être utilisé"+S('aips-55609-35')+".",
 "Pendant l'allaitement, Nexium® ne doit pas être utilisé"+S('aips-55609-35')+" ; pour le pantoprazole, la décision d'interrompre l'allaitement ou le traitement repose sur la mise en balance du bénéfice de l'allaitement pour l'enfant et du bénéfice du traitement pour la mère"+S('aips-59834-30')+"."),
("Une réponse au traitement de l'acidité confirme le lien causal sans le prouver. ",""),
("Sur 39 patients, 2 (5,7 %) devaient leur pression de relaxation élevée à une lésion manquée comme un anneau de Schatzki"+S('wd85c94-2')+".",
 "Dans cette série de 39 patients, 2 cas, soit 5,7 % selon les auteurs, devaient leur pression de relaxation élevée à une lésion manquée comme un anneau de Schatzki"+S('wd85c94-2')+"."),
]
json.dump([{"avant":a,"apres":b} for a,b in C],open('Claude/LOT_048/_travail/DX.5/corrections.json','w'),ensure_ascii=False)

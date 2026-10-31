from pathlib import Path
from html import escape
from format_lecon import paras
D=Path(__file__).resolve().parents[1]
def quote(n,starts):
 lines=(D/f'evidence/AIPS_{n}.txt').read_text().splitlines();out=[]
 for s in starts:
  hits=[x for x in lines if x.startswith(s)];assert len(hits)==1,(n,s,len(hits));out.append('<p>« '+escape(hits[0])+' »</p>')
 return '<blockquote>'+'\n'.join(out)+'</blockquote>'

def adrenaline(l):
 d=paras('L’adrénaline stimule les récepteurs alpha et bêta : elle soutient la circulation, réduit l’œdème et traite le bronchospasme de l’anaphylaxie. La spécialité décrite est Adrenalin Sintetica 1 mg/ml en ampoule, autorisation 56551, notice de novembre 2024. La concentration, la voie et le contexte doivent être vérifiés avant administration.')
 d+=quote('56551',["La dose habituelle est de 500 microgrammes", "L’utilisation d’adrénaline pour un traitement systémique d’urgence", "Le meilleur site pour l’injection intramusculaire", "Surveiller le patient dès que possible", "L'adrénaline doit être utilisée avec prudence chez les patients atteints d'insuffisance rénale sévère"])
 lines=(D/'evidence/AIPS_56551.txt').read_text().splitlines();a=lines.index("Les doses chez l'enfant et l’adolescent sont:");b=lines.index('En injection intraveineuse ( i.v .)',a)
 d+='<p>Tableau pédiatrique de la notice, dans la section intramusculaire du choc anaphylactique :</p><blockquote><p>« '+escape(' '.join(lines[a:b]))+' »</p></blockquote>'
 d+=paras('La dose adulte citée est de 0,5 mg, soit 0,5 ml de la solution à 1 mg/ml, par voie intramusculaire dans la cuisse. La répétition se décide sur la persistance des signes respiratoires ou circulatoires. Ne pas confondre ces doses avec celles de l’arrêt cardiaque ni administrer la solution à 1 mg/ml en bolus intraveineux pour une anaphylaxie ordinaire.', 'La notice mentionne des demi-doses potentiellement plus sûres sous certains traitements associés. Cette mention n’est pas transformée ici en règle automatique : la recommandation britannique insiste sur l’administration précoce et adaptée de l’adrénaline intramusculaire. Les interactions, l’âge et le terrain nécessitent surveillance et avis expert, sans retarder un traitement vital.', 'La voie intraveineuse et les perfusions d’adrénaline relèvent d’équipes expérimentées avec surveillance continue. Une réaction réfractaire malgré deux doses intramusculaires appropriées appelle une aide experte précoce. Les antihistaminiques et corticoïdes ne remplacent pas l’adrénaline pour l’atteinte respiratoire ou circulatoire.', 'Les précautions concernent notamment maladie cardiaque, troubles du rythme, hyperthyroïdie, hypertension, insuffisance rénale sévère et médicaments sensibilisant le myocarde. La notice reconnaît l’usage justifié par une indication vitale malgré des contre-indications générales. Elle ne fournit pas de palier rénal ou hépatique chiffré pour ce traitement d’urgence.', 'Pendant la grossesse, la notice réserve l’utilisation aux situations clairement indispensables et décrit des précautions obstétricales. Une anaphylaxie menaçante exige une prise en charge maternelle urgente avec expertise obstétricale. L’allaitement est à interrompre selon la notice citée, sans différer le traitement vital. Surveiller tachycardie, arythmie, hypertension, douleur thoracique et réponse clinique.')
 d+=quote('56551',["Des études chez l'animal ont montré des effets tératogènes.", "L'adrénaline passe dans le lait maternel."])
 return l.subwindow('adrenaline','Adrénaline : forme, voie et doses suisses',d,(13,14))


import json
a=json.load(open('Claude/LOT_046/audits/LOT_046_Phase_B_V0_DX.10.html.audit.json'))['corrections']
C=[{'avant':x['avant'],'apres':x['apres']} for x in a]
def s(*ids): return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)
C[1]['apres']=("Elle est contre-indiquée en cas d'hypersensibilité à la lidocaïne ou aux autres anesthésiques de type amide, d'hypovolémie, d'insuffisance cardiaque aiguë décompensée, de bloc cardiaque et d'autres troubles de la conduction, de choc sévère et de myasthénie grave. Elle ne doit pas être injectée dans une zone infectée ou enflammée"+s('aips-30015-5')+".")
C[2]['apres']=("Pour une douleur aiguë, Morphini HCl Streuli® s'injecte lentement par voie intraveineuse, à raison de 2 à 10 mg de chlorhydrate de morphine, à la vitesse de 10 mg par minute, uniquement si un effet spécialement rapide est nécessaire"+s('aips-56554-5')+
 ". Par voie intramusculaire ou sous-cutanée, la dose unique est de 5 à 10 mg, avec un maximum de 30 mg toutes les 4 à 6 heures"+s('aips-56554-6')+
 ". Le médecin garde à portée de main un appareil respiratoire et de la naloxone, car la morphine expose à la dépression respiratoire"+s('aips-56554-2')+
 ". La morphine ne s'administre pas pendant la grossesse sauf nécessité absolue, et l'allaitement est absolument contre-indiqué"+s('aips-56554-39')+
 ". Brufen® s'utilise à la dose efficace la plus faible possible, pendant le minimum de temps nécessaire"+s('aips-45031-3')+
 ", et la dose journalière maximale est de 2400 mg"+s('aips-45031-4')+
 ". L'ibuprofène peut aussi nuire au déroulement de la grossesse et au développement de l'embryon ou du fœtus, par inhibition de la synthèse des prostaglandines"+s('aips-45031-35')+
 ". L'oxygène relève d'une prescription individualisée, et ce cours n'en donne pas de dose.")
C[3]={'avant':"Chez la femme enceinte, les sources lues ne fixent pas d'imagerie particulière. Elles indiquent seulement que l'observation reste possible",'apres':"Chez la femme enceinte, l'observation reste possible"}
C[4]['apres']="Le syndrome coronarien aigu 🚩 est cité en premier parmi les diagnostics différentiels principaux du pneumothorax"+s('wfad2fa-13')+"."
C.append({'avant':"Pas en zone infectée, pas si hypovolémie ou bloc cardiaque",'apres':"Pas en zone infectée ou enflammée, ni si hypovolémie, insuffisance cardiaque aiguë décompensée ou bloc cardiaque"})
json.dump(C,open('Claude/LOT_046/_travail/DX.10/corrections.json','w'),ensure_ascii=False,indent=1)

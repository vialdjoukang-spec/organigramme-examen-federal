from pathlib import Path
import re,json,hashlib
B=Path(__file__).resolve().parent
def source(i):return f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
f=B/'fragments/p11.html';s=f.read_text()
ancre='<h4>Avant le dry needling : décision, sécurité et information</h4>\n'
assert s.count(ancre)==1
ajouts=[
('coag1','Selon le guide suisse, le dry needling n’est pas autorisé sous inhibiteur P2Y12, héparine ou pentasaccharide, coumarine ou anticoagulant oral direct. Le traitement antithrombotique n’est pas interrompu pour permettre ce geste.','dvs83-coagulation'),
('coag2','Les traitements permis par le groupeA du document restent confrontés aux comorbidités hémorragiques. La prudence individuelle et le choix d’un moyen non invasif préservent donc la sécurité sans interrompre une prévention cardiovasculaire.','dvs83-coagulation'),
('local1','Le guide suisse exclut localement les zones d’infection ou d’altération cutanée, de lymphœdème, d’hématome et de tumeur. Il exclut également le voisinage immédiat d’une ostéosynthèse ou d’une prothèse ainsi que le contact avec un implant.','dvs83-locaux'),
('consent1','Un consentement explicite et la capacité à donner un retour approprié sur les sensations sont nécessaires. Des paresthésies importantes ou une incapacité à comprendre le geste empêchent donc sa réalisation dans le cadre décrit.','dvs83-consentement'),
('spec1','Le guide suisse déconseille le geste près du thorax chez les personnes atteintes de maladie pulmonaire sévère. Un stimulateur cardiaque contre-indique la stimulation électrique intramusculaire décrite dans ce document.','dvs83-speciaux')]
bloc=''.join(f'<div class="p" id="dx1-p11-{i}">'+t+source(ref)+'</div>\n'for i,t,ref in ajouts)
# La contre-indication au stimulateur se trouve dans le passage locaux, avant grossesse.
bloc=bloc.replace('stimulateur cardiaque contre-indique la stimulation électrique intramusculaire décrite dans ce document.'+source('dvs83-speciaux'),'stimulateur cardiaque contre-indique la stimulation électrique intramusculaire décrite dans ce document.'+source('dvs83-locaux'))
s=s.replace(ancre,ancre+bloc);f.write_text(s)
def espacer(t):
    t=re.sub(r'\b(en|de|à|grade|cotée|sous|moins|plus|et|version)(?=\d)',r'\1 ',t)
    t=re.sub(r"(?<=\d)(mg|kg|ml|heures|jours|ans|h|g|m²)(?=[\s,.;:/]|$)",r' \1',t)
    t=re.sub(r'(\d{5}),(\d{5})',r'\1, \2',t)
    return t.replace('Dafalganà','Dafalgan® à').replace('rangE2','rang E2').replace('groupeA','groupe A').replace('🚩E','🚩 E')
for f in (B/'fragments').glob('p*.html'):
    t=f.read_text();t=re.sub(r'>([^<>]+)<',lambda m:'>'+espacer(m[1])+'<',t);f.write_text(t)
pq=json.loads((B/'paquet.json').read_text())
# Les offsets des caches JSON désignent le champ de texte extrait, pas les octets JSON.
for x in pq['passages']:
    z=x.get('preuve',{});f=str(z.get('fichier',''))
    if f.endswith('.json')and z.get('offset_debut')is not None:
        z['champ']='results[1].full_content'if ('DVS_NICE' in f and x['id'].startswith('nice83'))else'results[0].full_content'
(B/'paquet_AVANT_COMPACTION.json').write_text(json.dumps(pq,ensure_ascii=False,indent=2)+'\n')
mapping={};a=0;m=0
for x in pq['passages']:
    old=x['id']
    if old.startswith('aips-'):a+=1;new=f'aips-m{a}'
    else:m+=1;new=f'm{m}'
    mapping[old]=new;x['id_origine']=old;x['id']=new
for f in (B/'fragments').glob('p*.html'):
    t=f.read_text()
    for old,new in mapping.items():t=t.replace(f'href="#sb-{old}">{old}</a>',f'href="#sb-{new}">{new}</a>')
    f.write_text(t)
pq['statut']='RÉDACTION_COMPLÈTE, identifiants compactés sans changement des extraits'
pq['points']={str(n):sorted(set(re.findall(r'href="#sb-([^"]+)"',(B/'fragments'/f'p{n:02d}.html').read_text())))for n in range(1,15)}
(B/'paquet.json').write_text(json.dumps(pq,ensure_ascii=False,indent=2)+'\n')
(B/'CORRESPONDANCE_IDS.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n')
contract=json.loads((B/'contrat.json').read_text())
for n in range(1,15):contract['points'][str(n)]['sources']=pq['points'][str(n)]
(B/'contrat.json').write_text(json.dumps(contract,ensure_ascii=False,indent=2)+'\n')
(B/'HELP.md').write_text('LOT083 — DX1 — 10novembre2026\n\nÉpidémiologie : les sources consultées établissent la fréquence qualitative parmi myalgies localisées, sans incidence/prévalence nationale suisse propre au syndrome ni distribution âge/sexe ou mortalité comparable. Sources : DGN2025 ; résumé suisse Barbero2019 ; IASP ; Guérit2020. Aucun chiffre étranger non contextualisé transféré.\n\nBut thérapeutique : objectifs de fonction et d’autonomie définis et suivis ; aucun seuil numérique universel de guérison du syndrome n’a été déduit des études consultées. Ne pas fabriquer un seuil pour compléter Q11a.\n\nVersion : DGN2025 pour diagnostic et guide suisse DVS2.0/19.08.2022 pour sécurité du geste. NICE NG193, page officielle consultée10nov2026, appliquée seulement au champ de douleur chronique primaire. Les différences de champ et de date avec la fiche IASP et les revues mécanistiques sont explicites.\n\nImagerie : passe commune différée par ordre utilisateur. Aucune figure IA ni description d’image générée par IA utilisée comme preuve.\n')
(B/'PROVENANCE_REDACTION.json').write_text(json.dumps({'lot':'083','dx':1,'redacteur':'/root/sources_cutanees','date':'2026-11-10','statut':'Auteur seulement, aucun score ou autoaudit P3','ordre':'Paquet118passages préparé avant premier HTML ; critères et mécanismes issus des lectures ciblées.','normalisations':'Dernière préparation préassemblage : explicitation des contre-indications DVS, typographie des chiffres/unités et compaction bijective des identifiants. Aucun extrait médical modifié par compaction.','mapping':'CORRESPONDANCE_IDS.json','paquet_initial':'paquet_AVANT_COMPACTION.json'},ensure_ascii=False,indent=2)+'\n')
print('IDs compactés',len(mapping),'octets fragments',sum(f.stat().st_size for f in (B/'fragments').glob('p*.html')))

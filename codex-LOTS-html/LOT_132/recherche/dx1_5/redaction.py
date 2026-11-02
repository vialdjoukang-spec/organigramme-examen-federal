from pathlib import Path
import json,re,hashlib,datetime
B=Path('/workspace/organigramme-examen-federal/codex-LOTS-html/LOT_132')
P=json.load(open(B/'_travail/PHASEA_CONTENU.json'))
def source(old,new):
 x=next(x for x in P['sources'] if x['id']==old).copy();x['id']=new;return x
def aips(number,new):
 a=json.load(open(B/'recherche/pharmaco132/APPUIS_PHARMACO.json')); x=next(x for x in a['produits'] if x['numero_swissmedic_verifie']==number)
 return dict(id=new,titre='AIPS — '+x['produit'],url=x['source']['url'],passages_lus='Forme, indication, posologie adulte, contre-indications, précautions, interactions ; texte officiel acquis relu',preuve_locale='recherche/pharmaco132/'+number+'_officiel.txt',date_publication=x['date_information'])
def section(n,main,refs,paragraphs):
 return dict(numero=n,main=main,refs=refs,detail_html=''.join('<p>'+p+'</p>' for p in paragraphs.split('\n\n')))
def save(n,title,sources,blocks,quiz,notes):
 sections=[section(i+1,*b) for i,b in enumerate(blocks)]
 quizzes=[dict(question=q,reponse=a,refs=r) for q,a,r in quiz]
 d=dict(titre=title,sources=sources,sections=sections,quiz=quizzes)
 assert len(sections)==13 and len(quizzes)==14
 ids={x['id'] for x in sources};assert ids==set(range(1,len(ids)+1))
 for x in sections+quizzes:assert set(x['refs'])<=ids
 for x in sections:assert x['main'].count('{')==x['main'].count('}')==1
 for x in sources:assert (B/x['preuve_locale']).exists()
 f=B/f'_travail/DX{n}_CONTENU.json';f.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');sha=hashlib.sha256(f.read_bytes()).hexdigest()
 text=f'# Relecture auteur DX{n} — {datetime.datetime.now(datetime.timezone.utc).isoformat()}\n\nTitre canonique : {title}.\n\n'+notes+'\n\nContrôles : 13 sections/14 questions ; une expression cliquable par main ; ids numériques résolus ; preuves locales existantes ; JSON valide. Relecture rédactionnelle et clinique ciblée par auteur, pas audit indépendant ni validation des images. Aucun HTML final/global/Git modifié.\n\nSHA256 : '+sha+'\n'
 (B/f'recherche/dx1_5/RELECTURE_DX{n}.md').write_text(text)
 print(n,f.stat().st_size,sha)

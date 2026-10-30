"""Assemblage des textes originaux de Phase B ; aucune génération de score."""
from pathlib import Path
import ast, base64, json, re
from html import escape

D = Path(__file__).resolve().parent.parent
R = D.parents[1]
source_ast = ast.parse((D / '_travail/construire_phase_a.py').read_text())
SOURCES = ast.literal_eval(next(x.value for x in source_ast.body if isinstance(x, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'sources' for t in x.targets)))
SOURCES += [
('COUF, référentiel 2025, chapitre 2 : Réfraction et anomalies de la réfraction. Extraits consultés.', 'https://couf.fr/wp-content/uploads/2025/10/CH2_Ophtalmologie_-Sous-legide-du-College-des-ophtalmologistes-universitaires-de-France.pdf'),
('COUF, référentiel 2025, chapitre 13 : Cataracte. Extraits consultés.', 'https://couf.fr/xhtml/Ch013_233-248_B9782294786624500228.xhtml'),
('COUF, référentiel 2025, chapitre 14 : Glaucomes. Extraits consultés.', 'https://couf.fr/xhtml/Ch014_249-265_B978229478662450023X.xhtml'),
('COUF, référentiel 2025, chapitre 15 : Dégénérescence maculaire liée à l’âge. Extraits consultés.', 'https://couf.fr/xhtml/Ch015_267-281_B9782294786624500241.xhtml'),
('COUF, référentiel 2025, chapitre 20 : Rétinopathie diabétique. Extraits consultés.', 'https://couf.fr/xhtml/Ch020_347-369_B9782294786624500290.xhtml'),
('COUF, référentiel 2025, chapitre 17 : Occlusions veineuses rétiniennes. Extraits consultés.', 'https://couf.fr/xhtml/Ch017_303-320_B9782294786624500265.xhtml'),
('COUF, référentiel 2025, chapitre 16 : Occlusions artérielles rétiniennes et neuropathie optique ischémique. Extraits consultés.', 'https://couf.fr/xhtml/Ch016_283-302_B9782294786624500253.xhtml'),
('COUF, référentiel 2025, chapitre 19 : Œil et sclérose en plaques. Extraits consultés.', 'https://couf.fr/xhtml/Ch019_337-346_B9782294786624500289.xhtml'),
('Nicholson L et al. RCOphth. Retinal vein occlusion guideline: executive summary. Eye, 2022;36:909–912. DOI 10.1038/s41433-022-02007-4.', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9046155/'),
('Jeyakumar N et al. MOG antibody-associated optic neuritis. Eye, 2024. Résumé et légendes bibliographiques consultés.', 'https://pubmed.ncbi.nlm.nih.gov/38783085/'),
('HUG. Décollement de rétine : présentation et symptômes. Page sans date éditoriale vérifiée.', 'https://www.hug.ch/ophtalmologie/decollement-retine'),
('HUG. Décollement de rétine : le traitement. Page sans date éditoriale vérifiée.', 'https://www.hug.ch/ophtalmologie/decollement-retine-traitement'),
('HUG. Décollement de rétine : retour à la maison et brochure patient. Page sans date éditoriale vérifiée.', 'https://www.hug.ch/sites/interhug/files/documents/decollement_retine.pdf'),
('European Glaucoma Society. Terminology and guidelines for glaucoma, 6e édition, 2025. Extraits consultés.', 'https://bjo.bmj.com/content/109/Suppl_1/1'),
('Dejaco C et al. EULAR imaging recommendations, mise à jour 2023, publication 2024. DOI 10.1136/ard-2023-224543.', 'https://ard.bmj.com/content/83/6/741'),
('AIPS suisse. Xalatan®, latanoprost, collyre, Swissmedic 53675. Version locale du 08.10.2026 ; forme vérifiée dans la liste Swissmedic.', 'https://files.refdata.ch/simis-public-prod/MedicinalDocuments/023f62ad6a39471a992ce4377d0aa046-fr.html'),
('AIPS suisse. Eylea® 2 mg/50 µl. Seringue préremplie 62393 ; flacon 62397. Document local 62393002 de la version locale du 08.10.2026 ; formes vérifiées.', 'https://files.refdata.ch/simis-public-prod/MedicinalDocuments/3a50bb15b1b94fc9b3d3d187b066ad53-fr.html'),
('AIPS suisse. Prednisone Streuli®, comprimés, Swissmedic 29349. Version locale du 08.10.2026 ; formes vérifiées dans la liste Swissmedic.', 'https://files.refdata.ch/simis-public-prod/MedicinalDocuments/20fd4e0534634d9a939cba4c8509130b-fr.html'),
('RCOphth. Ophthalmic Safety Alert: Do not use nitrous oxide when there is gas in an operated eye. 18 décembre 2018.', 'https://curriculum.rcophth.ac.uk/2018/12/ophthalmic-safety-alert-use-of-nitrous-oxide-when-there-is-gas-in-an-operated-eye'),
('NEMOS. Revised recommendations, Part II: Attack therapy and long-term management. 2023. DOI 10.1007/s00415-023-11910-z. Recommandations d’attaque consultées.', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10770020/'),
('NICE. NG82, 2018, question de recherche sur les compléments antioxydants : bénéfices incertains selon le stade et risque du bêta-carotène chez les fumeurs. Extrait consulté.', 'https://www.nice.org.uk/about/what-we-do/research-and-development/research-recommendations/ng82/1'),
]
TITLES = ['Définition et sémantique','Épidémiologie','Physiopathologie et bases indispensables','Démarche diagnostique : les graves d’abord','Anamnèse et drapeaux rouges','Examen physique ciblé','Approche syndromique','Diagnostic positif et critères','Examens complémentaires','Arbre décisionnel','Prise en charge en Suisse','Prévention','Points clés','Pièges et questions de révision']

def ref(*ns):
    return '<sup class="s">'+','.join(f'<a href="#s{n}">{n}</a>' for n in ns)+'</sup>'

def p(s): return '<p>'+s+'</p>'
def paras(*ss): return '\n'.join(p(s) for s in ss)
def table(head, rows):
    return '<div class="tw"><table><thead><tr>'+''.join('<th scope="col">'+h+'</th>' for h in head)+'</tr></thead><tbody>\n'+'\n'.join('<tr>'+''.join('<td>'+v+'</td>' for v in row)+'</tr>' for row in rows)+'</tbody></table></div>'
def steps(*ss): return '<ol class="algo">'+'\n'.join('<li>'+s+'</li>' for s in ss)+'</ol>'
def cite(s):
    return '<blockquote>'+'\n'.join('<p>« '+escape(x)+' »</p>' for x in s.splitlines() if x.strip())+'</blockquote>'
def aips(n): return json.loads((D/f'evidence/AIPS_{n}.json').read_text())['sections']
def line(n,key,start): return next(s for s in aips(n)[key].splitlines() if s.startswith(start))
def segment(n,key,start,end): return aips(n)[key].split(start,1)[1].split(end,1)[0].strip()

ABBR = {'NICE':'National Institute for Health and Care Excellence, institut britannique de recommandations de santé','COUF':'Collège des ophtalmologistes universitaires de France','HUG':'Hôpitaux universitaires de Genève','OCT':'tomographie en cohérence optique','ACG':'artérite à cellules géantes','AIPS':'plateforme suisse de publication des informations sur les médicaments','EULAR':'Alliance européenne des associations de rhumatologie','EGS':'Société européenne du glaucome','RCOphth':'Royal College of Ophthalmologists','VEGF':'facteur de croissance de l’endothélium vasculaire','IRM':'imagerie par résonance magnétique','CRP':'protéine C réactive','SEP':'sclérose en plaques','MOG':'glycoprotéine de la myéline oligodendrocytaire','AQP4':'aquaporine 4','CYP3A4':'isoenzyme 3A4 du cytochrome P450','HbA1c':'hémoglobine glyquée','GPAO':'glaucome primitif à angle ouvert','DMLA':'dégénérescence maculaire liée à l’âge','i. v.':'intraveineuse','i. m.':'intramusculaire','p.ex.':'par exemple','p. ex.':'par exemple'}
ABBR.update({'DMLAe':'dégénérescence maculaire liée à l’âge exsudative','i.v.':'intraveineuse','i.m.':'intramusculaire','AVC':'accident vasculaire cérébral','MAVC':'meilleure acuité visuelle corrigée','OMD':'œdème maculaire diabétique','OVCR':'occlusion de la veine centrale de la rétine','OBVR':'occlusion de branche veineuse rétinienne','AREDS2':'Age-Related Eye Disease Study 2, étude de supplémentation dans la dégénérescence maculaire','NEMOS':'Neuromyelitis Optica Study Group, groupe de recommandations sur le spectre de la neuromyélite optique','BCG':'bacille de Calmette et Guérin','DOI':'identifiant numérique permanent d’un document'})

class Lesson:
    def __init__(self, n, refs):
        self.n=n; self.refs=refs; self.sections=[]; self.windows={}
        self.name=re.search(rf'^DX\.{n} — (.+)$',(D/'LISTE_DX_CANONIQUE.md').read_text(),re.M)[1]

    def window(self, key, title, body, sub=False):
        ident=f'dx{self.n}-{key}'
        self.windows[ident]=f'<div id="{ident}" popover class="fenetre'+(' sousf' if sub else '')+'"><div class="barre"><span>'+title+f'</span><button type="button" popovertarget="{ident}" popovertargetaction="hide" aria-label="Fermer">✕</button></div><div class="corps">'+body+'</div></div>'
        return f'<button type="button" class="terme" popovertarget="{ident}">{title}</button>'

    def add(self, main, detail='', refs=None):
        i=len(self.sections)+1; refs=refs or self.refs
        if detail:
            assert len(re.findall(r'\{([^{}]+)\}',main)) == 1, (self.n,i,main)
            main=re.sub(r'\{([^{}]+)\}',lambda m:self.window(f'detail{i}',m[1],detail+ref(*refs)),main)
        self.sections.append((main,refs))

    def quiz(self, items):
        assert len(items)==14
        detail='\n'.join('<details class="quiz"><summary>'+q+'</summary>'+p(a)+'</details>' for q,a in items)
        button=self.window('quiz','pièges d’examen',detail+ref(*self.refs))
        self.add('Les '+button+' entraînent à relier les signes, les examens et les décisions. Ces questions sont originales et pédagogiques ; elles ne sont pas présentées comme des sujets officiels de l’examen fédéral.')

    def write(self):
        assert len(self.sections)==14,(self.n,len(self.sections))
        css=(R/'harnais/modele_lecon/style_lecon.css').read_text()
        for weight in (400,700):
            data=base64.b64encode((R/f'codex-LOTS-html/outils/polices/atkinson-hyperlegible-latin-{weight}-normal.woff2').read_bytes()).decode()
            data='\\\n'.join(data[i:i+160] for i in range(0,len(data),160))
            css+='\n@font-face{font-family:"Atkinson Hyperlegible";font-style:normal;font-weight:'+str(weight)+';font-display:swap;src:url("data:font/woff2;base64,'+data+'") format("woff2")}'
        css+='\n@media(max-width:480px){.fenetre.sousf{translate:0 .6rem}.som{columns:1}}'
        out=['<!doctype html>','<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">','<title>'+self.name+' — S1.2</title>','<style>'+css.replace('}','}\n')+'</style></head><body><main>',
             '<h2>DX.'+str(self.n)+' — '+self.name+'</h2>',
             '<p class="sous">S1.2 · Sources consultées le 30 octobre 2026.</p>',
             '<p id="taille" class="taille">Taille en cours de mesure.</p>',
             p('Pour le tri initial d’une perte visuelle et les gestes communs, voir le <a href="LOT_018_Phase_A_V0.html">cours du symptôme</a>.'),
             '<nav class="ilot v" aria-label="Sommaire"><h2>Sommaire</h2><ol class="som">'+''.join(f'<li><a href="#dx{self.n}-p{i}">{t}</a></li>' for i,t in enumerate(TITLES,1))+'</ol></nav>']
        for i,(text,refs) in enumerate(self.sections,1):
            out.append(f'<section class="ilot {"c" if i%2 else "v"}"><h2 id="dx{self.n}-p{i}">{i}. {TITLES[i-1]}</h2>'+p(text+ref(*refs))+'</section>')
        out.extend(self.windows.values())
        used=sorted({int(n) for n in re.findall(r'href="#s(\d+)"',''.join(out))})
        out.append('<section class="ilot c sources"><h2>Sources</h2><ol>'+''.join(f'<li id="s{n}" value="{n}">{escape(SOURCES[n-1][0])} <a href="{escape(SOURCES[n-1][1],quote=True)}">Source</a>. Consulté le 30.10.2026.</li>\n' for n in used)+'</ol></section>')
        out += [p('Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.'),'</main></body></html>',f'<!-- FIN_FICHIER LOT_018_Phase_B_DX.{self.n} -->']
        source='\n'.join(out).replace('\u00a0',' ').replace('\u202f',' ')
        pattern=re.compile(r'(?<!\w)('+ '|'.join(re.escape(a) for a in ABBR) +r')(?!\w)')
        chunks=[];body=False
        for part in re.split(r'(<[^>]+>)',source):
            if part.startswith('<body'): body=True
            chunks.append(part if part.startswith('<') or not body else pattern.sub(lambda m:f'<abbr title="{ABBR[m[0]]}">{m[0]}</abbr>',part))
        source=''.join(chunks).replace('</li><li','</li>\n<li')
        dest=D/f'LOT_018_Phase_B_V0_DX.{self.n}.html';dest.write_text(source)
        print(dest.name,len(source.encode()),len(self.windows),'fenêtres')

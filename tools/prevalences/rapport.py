"""Centralisation des contrôles statistiques et synthèse PDF pour les jauges."""
from collections import Counter
from datetime import datetime, timezone
from html import escape
import hashlib
import json
from pathlib import Path
from zoneinfo import ZoneInfo
from tools.prevalences.relance_agent import review_completed



def _review_motif(review, default):
    motifs = review.get('motifs')
    if motifs is None: motifs = []
    elif not isinstance(motifs, (list, tuple)): motifs = [motifs]
    return ' ; '.join(str(value) for value in motifs if value is not None) or str(review.get('motif') or default)


def centraliser(states, code_errors=(), previous=None):
    events = {}
    def add(kind, category, key, candidate, code, message, source='', corrected=False, before=None, after=None, severity='information', fingerprint='', observation_date=None):
        identity = json.dumps([kind, category, key, candidate, code, source, fingerprint, before if corrected else None, after if corrected else None], ensure_ascii=False)
        eid = hashlib.sha256(identity.encode()).hexdigest()[:24]
        events[eid] = {'id': eid, 'nature': kind, 'categorie': category, 'tache': key,
                       'candidat_id': candidate, 'code': code, 'motif': str(message),
                       'source': source or '', 'empreinte_source': fingerprint, 'corrigee': corrected, 'avant': before, 'apres': after,
                       'gravite': severity, 'validation_clinique': False}
        if observation_date is not None:
            events[eid]['date'] = observation_date
    for category, state in states.items():
        if not isinstance(state,dict) or not isinstance(state.get('tasks'),dict):
            add('etat_invalide',category,'',None,'etat_non_lisible','État invalide : ne pas interpréter les zéros comme une absence de recherche');continue
        for key, row in state.get('tasks', {}).items():
            for q in row.get('queries', []):
                if q.get('ok') is not True:
                    add('acces_recherche', category, key, None, q.get('provider', '')+':'+q.get('id',''),
                        q.get('erreur','Recherche non aboutie'),q.get('url_recherche') or q.get('details_erreur',{}).get('url',''))
                for trace in q.get('trace_sources',[]):
                    if trace.get('ok') is False:
                        add('acces_recherche',category,key,None,'document:'+trace.get('source_id',''),trace.get('erreur','Accès non abouti'),trace.get('url',''))
            for c in row.get('candidates', []):
                audit = c.get('audit', {})
                for flag in audit.get('flags', []):
                    add('point_a_verifier',category,key,c.get('id'),flag,flag,c.get('url',''),fingerprint=c.get('sha256',''))
                for correction in audit.get('corrections', []):
                    add('correction_effectuee',category,key,c.get('id'),correction.get('champ','calcul'),
                        correction.get('motif') or correction.get('raison') or 'Correction arithmétique documentée',
                        c.get('url',''),True,correction.get('avant'),correction.get('apres'),'majeure',fingerprint=c.get('sha256',''))
                review = c.get('relecture_agent',{})
                if review_completed(c):
                    add('relecture_documentaire',category,key,c.get('id'),review.get('verdict','À vérifier'),
                        _review_motif(review, 'Relecture source consignée'),c.get('url',''),fingerprint=c.get('sha256',''))
                elif isinstance(review, dict) and review.get('statut') == 'source_inaccessible':
                    add('acces_relecture', category, key, c.get('id'), 'source_inaccessible',
                        _review_motif(review, 'Source inaccessible pendant la relecture de l’agent'),
                        review.get('source') or c.get('url', ''), fingerprint=c.get('sha256', ''),
                        observation_date=review.get('date'))
            for error in row.get('selection',{}).get('erreurs',[]):
                if not isinstance(error,dict):continue
                add('selection_a_verifier',category,key,error.get('candidat_id'),error.get('code','selection'),
                    error.get('motif','Sélection à vérifier'),error.get('source',''),error.get('corrigee') is True,
                    error.get('avant'),error.get('apres'),error.get('gravite','information'))
    for error in code_errors:
        add('correction_code', 'dispositif', '', None, error['id'], error['motif'],error.get('preuve',''),
            error.get('corrigee') is True,error.get('avant'),error.get('apres'),error.get('gravite','majeure'))
    # Migration des premières signatures : une archive sans empreinte qui
    # décrit le même événement actif ne crée pas une seconde erreur.
    def semantic(event):
        return json.dumps([event.get(k) for k in ('nature','categorie','tache','candidat_id','code','source','avant','apres')],ensure_ascii=False,sort_keys=True)
    active_semantics = {semantic(event) for event in events.values()}
    for error in (previous or {}).get('evenements', []):
        if error['id'] in events: continue
        if not error.get('empreinte_source') and semantic(error) in active_semantics: continue
        archived = dict(error);archived['non_reobserve_dans_instantane'] = True
        events[error['id']] = archived
    counts = Counter(e['nature'] for e in events.values() if not e.get('non_reobserve_dans_instantane'))
    archives = Counter(e['nature'] for e in events.values() if e.get('non_reobserve_dans_instantane'))
    return {'version':1,'validation_clinique':False,'synthese':dict(counts),'synthese_archives':dict(archives),
            'evenements':sorted(events.values(),key=lambda e:(e['nature'],e['categorie'],e['tache'],str(e['candidat_id']),e['code'])),
            'reserve':'Points à vérifier, échecs réseau et corrections confirmées sont comptés séparément ; aucune erreur médicale publiée ne se déduit d’une piste rejetée.'}


def ecrire_pdf(path, gauges, errors):
    import reportlab
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
    fonts=Path(reportlab.__file__).parent/'fonts'
    if 'StatSans' not in pdfmetrics.getRegisteredFontNames():
        pdfmetrics.registerFont(TTFont('StatSans',str(fonts/'Vera.ttf')))
        pdfmetrics.registerFont(TTFont('StatSans-Bold',str(fonts/'VeraBd.ttf')))
        pdfmetrics.registerFontFamily('StatSans',normal='StatSans',bold='StatSans-Bold')
    styles=getSampleStyleSheet()
    for style in styles.byName.values():style.fontName='StatSans';style.fontSize=9;style.leading=13
    styles['Title'].fontName='StatSans-Bold';styles['Title'].fontSize=19;styles['Title'].leading=24
    styles['Heading1'].fontName='StatSans-Bold';styles['Heading1'].fontSize=13;styles['Heading1'].leading=18
    styles['Heading2'].fontName='StatSans-Bold';styles['Heading2'].fontSize=10;styles['Heading2'].leading=15
    styles.add(ParagraphStyle('Petit',fontName='StatSans',fontSize=7,leading=10,wordWrap='CJK'))
    def P(s,style='BodyText'):return Paragraph(escape(str(s)).replace('\n','<br/>'),styles[style])
    local=datetime.fromisoformat(gauges['maj']).astimezone(ZoneInfo('Europe/Zurich'))
    story=[P('Prévalences · contrôle statistique et erreurs','Title'),
           P(local.strftime('%d.%m.%Y à %H:%M')+' · Europe/Zurich'),Spacer(1,10),
           P('Synthèse centralisée par le calculateur des jauges. Ce rapport décrit le dispositif et ses candidats ; il ne constitue pas une validation médicale.'),
           P('1. Progression par catégorie','Heading1')]
    table=[[P('Catégorie','Petit'),P('DD','Petit'),P('Recherches\nabouties','Petit'),P('Extraits\ncandidats','Petit'),P('Chiffres\npubliés sourcés','Petit')]]
    for category,m in gauges['categories'].items():
        table.append([P(category),P(m['total']),P(m['recherches_abouties']),P(m['candidats']),P(m['chiffres_sources'])])
    t=Table(table,colWidths=[65,65,105,105,135],hAlign='LEFT',repeatRows=1)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8eef4')),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#c4cbd3')),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]));story.append(t)
    total=gauges['total']
    story += [Spacer(1,8),P(f"{total['ssp_sans_dd']} SSP sur {total['ssp']} n’ont pas encore de différentiel. Les candidats ne font jamais monter la couverture clinique."),
              P('2. Règle de sélection des valeurs','Heading1'),
              P('Vérifier la source reconnue, la définition du diagnostic, le pays réel des participants, la période, les âges et le cadre. Comparer ensuite la qualité méthodologique et le risque de biais ; à qualité comparable, privilégier le plus grand effectif effectivement analysé. Un grand échantillon biaisé ne devient pas représentatif par sa taille.'),
              P('Aucune moyenne n’est calculée entre populations incompatibles. Incidence, risque, OR/HR, intervalle de confiance et prévalence sont distingués. Les plans pondérés ou en grappes exigent une précision tenant compte du plan. Une valeur retenue reste une proposition à relire, pas une écriture clinique automatique.'),
              P('3. Décompte des contrôles et corrections','Heading1')]
    labels={'acces_recherche':'Échecs d’accès ou de recherche','acces_relecture':'Réserves d’accès de l’agent par candidat','point_a_verifier':'Points candidats à vérifier','selection_a_verifier':'Réserves de sélection','correction_effectuee':'Corrections arithmétiques des candidats','correction_code':'Défauts du dispositif corrigés','relecture_documentaire':'Relectures documentaires consignées'}
    for key,label in labels.items():story.append(P(f"{label} : {errors['synthese'].get(key,0)}"))
    blocked_reviews = [e for e in errors['evenements'] if e['nature'] == 'acces_relecture'
                       and not e.get('non_reobserve_dans_instantane')]
    if blocked_reviews:
        story += [P('Sources inaccessibles pendant la relecture de l’agent', 'Heading2'),
                  P('Ces candidats restent à relire. Plusieurs extraits peuvent renvoyer au même article ; un refus d’accès ne compte jamais comme une relecture terminée.')]
        for event in blocked_reviews[:8]:
            attempted_at = 'Date non renseignée'
            if isinstance(event.get('date'), str):
                try:
                    instant = datetime.fromisoformat(event['date'].replace('Z', '+00:00'))
                    if instant.tzinfo is None: instant = instant.replace(tzinfo=timezone.utc)
                    attempted_at = instant.astimezone(ZoneInfo('Europe/Zurich')).strftime('%d.%m.%Y à %H:%M · Europe/Zurich')
                except (ValueError, OverflowError):
                    pass
            story += [P(f"{event['categorie']} · {event['tache']} · candidat {event['candidat_id']}", 'Petit'),
                      P(event['motif']), P(event['source'], 'Petit'), P(attempted_at, 'Petit')]
        if len(blocked_reviews) > 8:
            story.append(P('Autres réserves d’accès de l’agent dans le registre JSON complet.'))
    story += [P(errors['reserve']),P('4. Erreurs corrigées et contrôle de l’agent','Heading1')]
    confirmed=[e for e in errors['evenements'] if e['corrigee'] and not e.get('non_reobserve_dans_instantane')]
    if not confirmed:story.append(P('Aucune correction confirmée n’est enregistrée dans cet instantané.'))
    for e in confirmed[:60]:
        story += [P(e['code'],'Heading2'),P(e['motif']),P(f"Avant : {e['avant']}\nAprès : {e['apres']}"),P(e['source'],'Petit')]
    if len(confirmed)>60:story.append(P('Suite des corrections dans le registre JSON complet.'))
    story += [PageBreak(),P('5. Exemples de réserves encore ouvertes','Heading1'),
              P('Exemples limités pour garder une synthèse lisible. Le registre JSON conserve la liste complète ; une absence dans cette sélection ne signifie pas qu’un problème est résolu.')]
    pending=[e for e in errors['evenements'] if not e['corrigee'] and not e.get('non_reobserve_dans_instantane') and e['nature'] in ('relecture_documentaire','acces_recherche','selection_a_verifier')]
    # Les réserves documentaires concrètes précèdent les pannes répétées d'accès.
    pending.sort(key=lambda e: {'relecture_documentaire':0,'selection_a_verifier':1,'acces_recherche':2}[e['nature']])
    for e in pending[:35]:
        story += [P(f"{e['categorie']} · {e['tache']} · {e['code']}",'Heading2'),P(e['motif']),P(e['source'],'Petit')]
    story += [Spacer(1,12),P('Registre : prevalences-erreurs.json · Jauges : prevalences.html · Les identifiants et sources permettent de reproduire le contrôle.','Petit')]
    def footer(canvas,doc):
        canvas.setFont('StatSans',7);canvas.setFillColor(colors.HexColor('#435264'))
        canvas.drawString(48,24,'Prévalences · contrôle statistique · aucune validation clinique automatique')
        canvas.drawRightString(A4[0]-48,24,str(doc.page))
    target=Path(path);target.parent.mkdir(parents=True,exist_ok=True)
    tmp=target.with_name(target.name+'.tmp')
    SimpleDocTemplate(str(tmp),pagesize=A4,leftMargin=48,rightMargin=48,topMargin=40,bottomMargin=42,title='Prévalences : synthèse des erreurs et contrôles',author='Calculateur des jauges et auditeur statistique').build(story,onFirstPage=footer,onLaterPages=footer)
    tmp.replace(target)

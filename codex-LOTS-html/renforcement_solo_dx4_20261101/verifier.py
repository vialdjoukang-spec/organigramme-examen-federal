"""Contrôle de la transition solo DX4 depuis fdd11b10 ; conserve les preuves de la passe précédente."""
import hashlib, importlib.util, json, subprocess
from pathlib import Path
from datetime import datetime, timezone
from lxml import html
D=Path(__file__).resolve().parent;B=D.parent;R=B.parent
def sha(b):return hashlib.sha256(b).hexdigest()
def mod(name,p):
    s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def main():
    baseline=json.loads((D/'BASELINE.json').read_text()); before=baseline['lecons']
    current={str(p.relative_to(R)):sha(p.read_bytes()) for p in B.glob('LOT_*/*.html')}
    targets={f'codex-LOTS-html/LOT_{n:03}/LOT_{n:03}_Phase_B_V0_DX.4.html' for n in (18,29)}
    assert set(before)==set(current) and len(current)==244
    assert {p for p in current if current[p]!=before[p]}==targets
    # Les six leçons antérieurement contre-relues demeurent strictement identiques.
    previous=json.loads((B/'renforcement_medical_20261101/CONTROLE.json').read_text())
    for x in previous['lecons']:
        key='codex-LOTS-html/'+x['fichier'];assert current[key]==x['sha256_apres']
    previous_solo=json.loads((B/'renforcement_solo_dx3_20261101/CONTROLE.json').read_text())
    for x in previous_solo['lecons']:
        assert current['codex-LOTS-html/'+x['fichier']]==x['sha256_apres']
    v8=mod('v8_solo',B/'outils/verifier_lot_generique_v8.py')
    langue=mod('langue_solo',R/'harnais/audit_langue.py')
    reports={n:v8.verifier(B/f'LOT_{n:03}') for n in (18,29)}
    for n,r in reports.items():
        (D/f'V8_{n}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
        assert r['statique_ok'],[(f['fichier'],[c for c in f['controles'] if not c['ok']]) for f in r['fichiers'] if not f['statique_ok']]
    rows=[]
    for name in sorted(targets):
        old=subprocess.check_output(['git','show',baseline['commit']+':'+name],cwd=R);new=(R/name).read_bytes()
        a=html.fromstring(old);b=html.fromstring(new)
        assert set(a.xpath('//*[@id]/@id'))<=set(b.xpath('//*[@id]/@id'))
        for fig in a.xpath('//*[@data-illustration]'):
            after=b.xpath('//*[@data-illustration=$name]',name=fig.get('data-illustration'))[0]
            assert html.tostring(fig,with_tail=False)==html.tostring(after,with_tail=False)
        # Conservation exacte de la fenêtre thérapeutique AIPS et des sous-fenêtres liées.
        for node in a.xpath('//*[@popover and (contains(@id,"latanoprost") or contains(@id,"aips"))]'):
            assert html.tostring(node,with_tail=False)==html.tostring(b.get_element_by_id(node.get('id')),with_tail=False)
        sections=b.xpath('//section[h2[contains(@id,"-p")]]');assert len(sections)==14
        assert all(s.xpath('.//button[@popovertarget]') for s in sections)
        assert len(b.xpath('//details[@class="quiz"]'))==14
        n=int(Path(name).parent.name[4:]);r=next(f for f in reports[n]['fichiers'] if f['fichier']==Path(name).name)
        sizes=[]
        for doc in (a,b):
            sizes.append([len(' '.join(doc.get_element_by_id(s.xpath('.//button/@popovertarget')[0]).itertext()).encode()) if s.xpath('.//button/@popovertarget') else 0 for s in doc.xpath('//section[h2[contains(@id,"-p")]]')])
        audits={k:langue.audit(R/name,src=raw.decode(),nom=Path(name).name) for k,raw in [('avant',old),('apres',new)]}
        (D/f'LANGUE_{n}.json').write_text(json.dumps(audits,ensure_ascii=False,indent=2)+'\n')
        rows.append({'fichier':name.removeprefix('codex-LOTS-html/'),'sha256_avant':sha(old),'sha256_apres':sha(new),'octets_avant':len(old),'octets_apres':len(new),'texte_fiche_octets':r['texte_fiche_octets'],'texte_fenetres_octets':r['texte_fenetres_octets'],'octets_texte_fenetre_directe_par_partie_avant_apres':sizes,'figures_anterieures_preservees':len(a.xpath('//*[@data-illustration]')),'identifiants_anterieurs_preserves':True,'fenetres_therapeutiques_aips_preservees':True})
    shared=json.loads((R/'harnais/HARNAIS_MANIFESTE.json').read_text())['fichiers']
    assert all(sha((R/p).read_bytes())==s for p,s in shared.items())
    result={'date':datetime.now(timezone.utc).isoformat(timespec='seconds'),'base':baseline['commit'],'lecons':rows,'lecons_non_modifiees':242,'huit_lecons_precedentes_inchangees':True,'harnais_intacts':len(shared),'conditions_v8_reussies':sum(len(f['controles']) for r in reports.values() for f in r['fichiers']),'portee':'Conservation, structure, tailles et correspondance des citations AIPS aux fichiers originaux. Aucun score médical.','audit_medical_independant':False,'validation_clinique_humaine':False}
    (D/'CONTROLE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='lecons'},ensure_ascii=False))
if __name__=='__main__':main()

// À exécuter dans functions.exec, qui expose tools ; ce fichier n'est pas un programme Node.
(async function rechercherAvecConnecteur(tools, p="codex-LOTS-html/LOT_019/illustrations/recherche_web/PLAN.json") {
  const cwd="/workspace/organigramme-examen-federal";
  const quote=s=>"'"+s.replace(/'/g,"'\\''")+"'";
  const check="import sys,json;from pathlib import Path;sys.path.insert(0,'codex-LOTS-html/outils/illustration');import pipeline_images as m;plan=json.loads(m.path(Path(sys.argv[1]).resolve()).read_text());m.guard(plan['lot']);m.path(plan['resultats_web'],m.BASE/plan['lot']/'illustrations');print(json.dumps(plan))";
  const read=await tools.exec_command({cmd:"python3 -B -c "+quote(check)+" "+quote(p),workdir:cwd,max_output_tokens:2000});
  if(read.exit_code!==0)throw Error(read.output);
  const plan=JSON.parse(read.output), results=[];
  for(const q of plan.requetes){
    const r=await tools.mcp__codex_apps__search_service_web_run({system2_search_query:[{q}],response_length:"short"});
    if(r.isError)throw Error("Échec du connecteur web");
    for(const c of r.content||[]){
      if(c.type!=="text")continue;
      for(const m of c.text.matchAll(/^(.+) \((https:\/\/[^)\s]+)\)$/gm)) results.push({titre:m[1],url:m[2],requete:q});
    }
  }
  const doc={date:new Date().toISOString(),moteur:"search_service_web_run",requetes:plan.requetes,resultats:[...new Map(results.map(x=>[x.url,x])).values()],limite:"Titres et URL issus du connecteur ; aucune licence ni pertinence clinique validée par la recherche."};
  const dest="codex-LOTS-html/"+plan.resultats_web;
  const code="from pathlib import Path;import sys;p=Path(sys.argv[1]).resolve();b=Path('codex-LOTS-html').resolve();assert p.is_relative_to(b);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(sys.argv[2])";
  const saved=await tools.exec_command({cmd:"python3 -B -c "+quote(code)+" "+quote(dest)+" "+quote(JSON.stringify(doc,null,2)+"\n"),workdir:cwd,max_output_tokens:1000});
  if(saved.exit_code!==0)throw Error(saved.output);
  const run=await tools.exec_command({cmd:"python3 -B codex-LOTS-html/outils/illustration/pipeline_images.py rechercher "+quote(p),workdir:cwd,max_output_tokens:2000,yield_time_ms:10000});
  return {resultats_web:doc.resultats.length,execution:run};
})(tools);

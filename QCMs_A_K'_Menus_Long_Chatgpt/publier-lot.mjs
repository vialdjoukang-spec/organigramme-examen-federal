// Depuis le dossier de la banque dans un clone Git avec accès à origin/main.
// node publier-lot.mjs [numéro code début] [--verifier]
// Sans arguments, publie le prochain lot scellé. --verifier exécute tous les tests sans pousser.
import {execFileSync, spawnSync} from 'node:child_process';
import {mkdtempSync, readFileSync, writeFileSync, rmSync, mkdirSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
import {dirname, join, relative} from 'node:path';
import {tmpdir} from 'node:os';

const home=dirname(fileURLToPath(import.meta.url));
const git=(cwd,...args)=>execFileSync('git',args,{cwd,encoding:'utf8',maxBuffer:32*1024*1024}).trimEnd();
const repo=git(home,'rev-parse','--show-toplevel');
const sub=relative(repo,home);
const flags=process.argv.slice(2);
const verifyOnly=flags.includes('--verifier');
const requested=flags.filter(x=>x!=='--verifier');
if(![0,3].includes(requested.length))throw Error('Utilisation : node publier-lot.mjs [numéro code début] [--verifier]');
const scratch=mkdtempSync(join(tmpdir(),'qcm-publication-'));
const checkout=join(scratch,'copie');
let reference, cible;

function bank(dir) {
  const raw=readFileSync(join(dir,'index.html'),'utf8');
  return JSON.parse(raw.match(/id="donnees">([^<]+)<\/script>/)[1]);
}
function node(dir,script,...args) {
  return execFileSync(process.execPath,[join(dir,script),...args],{cwd:dir,encoding:'utf8',maxBuffer:32*1024*1024});
}
function fetchHead() {
  git(repo,'fetch','--quiet','origin','refs/heads/main');
  return git(repo,'rev-parse','FETCH_HEAD');
}
function pathAt(name) {return sub?sub+'/'+name:name}
function fingerprint(dir,sha,name) {return git(dir,'rev-parse',sha+':'+pathAt(name))}
function next(snapshot) {
  const open=snapshot.catalogue.find(([code])=>!snapshot.production.statuts[code]?.clos);
  if(!open)throw Error('Tous les SSP sont clos.');
  return [String(Math.max(0,...snapshot.audits.map(x=>x.lot))+1),open[0],String(snapshot.items.filter(q=>q.code===open[0]).length+1)];
}
function table(items) {
  const field=s=>String(s).replace(/[\t\r\n]+/g,' ').trim();
  return 'ID\tDécision évaluée\tRéponse retenue\n'+items.map(q=>[q.id,q.aim,q.answer].map(field).join('\t')).join('\n')+'\n';
}
function journal(batch,tag,manifest) {
  const cell=s=>String(s).replace(/\|/g,'\\|').replace(/[\r\n]+/g,' ');
  return '# Audit '+tag+' · '+batch.code+' Q'+batch.start+' à Q'+(batch.start+19)+'\n\n'+
    'Verdict indépendant et détail des corrections : [manifeste](../en_cours/AUDIT-'+tag+'-'+batch.code+'.json). '+
    'La vérification des quatre manuscrits a porté sur leurs empreintes Git. Validation humaine non documentée.\n\n'+
    manifest.fourFinalBlobs.map(row=>'- Q'+row.start+'–'+(row.start+4)+' : '+row.sha).join('\n')+
    '\n\n| Question | Décision évaluée | Réponse |\n|---|---|---|\n'+
    batch.items.map((q,i)=>'| '+batch.code+'-'+String(batch.start+i).padStart(3,'0')+' | '+cell(q.aim)+' | '+cell(q.answer)+' |').join('\n')+'\n';
}
try {
  for(let attempt=0;attempt<5;attempt++){
    const parent=fetchHead();
    if(attempt===0)git(repo,'worktree','add','--quiet','--detach',checkout,parent);
    else git(checkout,'reset','--hard',parent);
    const dir=join(checkout,sub),snapshot=bank(dir),expected=next(snapshot);
    if(!cible){
      cible=requested.length?[String(Number(requested[0])),requested[1],String(Number(requested[2]))]:expected;
      reference=fingerprint(checkout,parent,'index.html');
    }
    if(cible.join('/')!==expected.join('/')||reference!==fingerprint(checkout,parent,'index.html'))
      throw Error('La banque ou le prochain lot a changé ; relire la progression publiée. Attendu : '+expected.join(' '));
    const [n,code,start]=cible,tag=n.padStart(3,'0'),auditName='audits/'+tag+'.md';
    if(spawnSync('git',['cat-file','-e',parent+':'+pathAt(auditName)],{cwd:checkout}).status===0)
      throw Error('Un journal de ce numéro existe déjà : '+auditName);
    const prepared=node(dir,'preparer-lot.mjs',n,code,start);
    const batch=JSON.parse(prepared);
    const manifest=JSON.parse(readFileSync(join(dir,'en_cours','AUDIT-'+tag+'-'+code+'.json'),'utf8'));
    const stage=join(scratch,'lot.json');
    writeFileSync(stage,prepared);
    node(dir,'integrer.mjs',stage);
    node(dir,'verifier.mjs');
    node(dir,'tester-parcours.mjs');
    const after=bank(dir);
    if(after.items.length!==snapshot.items.length+20||after.audits.at(-1).lot!==Number(n))throw Error('Progression discordante.');
    writeFileSync(join(dir,'DECISIONS.tsv'),table(after.items));
    mkdirSync(join(dir,'audits'),{recursive:true});
    writeFileSync(join(dir,auditName),journal(batch,tag,manifest));
    const paths=['index.html','DECISIONS.tsv',auditName];
    const blobs=Object.fromEntries(paths.map(p=>[p,git(dir,'hash-object',p)]));
    if(verifyOnly){console.log(JSON.stringify({verification:true,lot:Number(n),code,total:after.items.length,blobs}));break}
    git(dir,'add','--',...paths);
    git(dir,'commit','--quiet','-m','Intégrer le lot '+tag+' · '+code+' Q'+start+'–'+(Number(start)+19));
    const commit=git(checkout,'rev-parse','HEAD');
    const push=spawnSync('git',['push','--quiet','origin',commit+':refs/heads/main'],{cwd:repo,encoding:'utf8'});
    const remote=fetchHead();
    if(spawnSync('git',['merge-base','--is-ancestor',commit,remote],{cwd:checkout}).status===0){
      for(const p of paths)if(fingerprint(checkout,commit,p)!==blobs[p])throw Error('Écart de SHA : '+p);
      console.log(JSON.stringify({lot:Number(n),code,total:after.items.length,commit,blobs}));break;
    }
    if(remote===parent||attempt===4)throw Error('Publication non confirmée. '+(push.stderr||'Reprendre sur main.'));
  }
} finally {
  spawnSync('git',['worktree','remove','--force',checkout],{cwd:repo});
  rmSync(scratch,{recursive:true,force:true});
}

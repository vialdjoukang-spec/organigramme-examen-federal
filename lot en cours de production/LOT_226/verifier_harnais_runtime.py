#!/usr/bin/env python3
"""Teste les outils réels sur des données synthétiques sans contenu médical."""
import argparse,json,hashlib,importlib.metadata as md,sys,time,uuid
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--agent',required=True);p.add_argument('--cache-dir',required=True);p.add_argument('--compression',action='store_true');args=p.parse_args()
root=Path(args.cache_dir);root.mkdir(parents=True,exist_ok=True)
r={'agent':args.agent,'runtime':sys.executable,'versions':{n:md.version(n) for n in ['chonkie','llmlingua','gptcache','torch','transformers']},'tests':{},'source_medicale_comprimee':False}
from chonkie import TokenChunker
sample='The editor keeps the section order and removes repeated editorial instructions. '*8
chunks=TokenChunker(tokenizer='character',chunk_size=100,chunk_overlap=0)(sample)
assert len(chunks)>1 and ''.join(x.text for x in chunks)==sample
r['tests']['chonkie']={'ok':True,'chunks':len(chunks),'reconstruction_exacte':True}
from gptcache import Cache
from gptcache.manager import get_data_manager
from gptcache.processor.pre import get_prompt
from gptcache.adapter.api import put,get
c=Cache();c.init(pre_embedding_func=get_prompt,data_manager=get_data_manager(data_path=str(root/'gptcache.map')))
key='synthetic-editorial-probe|2026-10-25|'+args.agent+'|'+str(uuid.uuid4());value='Keep the original section order.'
assert get(key,cache_obj=c) is None
put(key,value,cache_obj=c)
assert get(key,cache_obj=c)==value
assert get(key+'|different',cache_obj=c) is None
c.flush()
r['tests']['gptcache']={'ok':True,'ecriture_lecture_exactes':True,'cle_distincte_absente':True,'mode':'correspondance exacte; aucun cache sémantique clinique'}
if args.compression:
 from llmlingua import PromptCompressor
 start=time.time();compressor=PromptCompressor(model_name='microsoft/llmlingua-2-bert-base-multilingual-cased-meetingbank',device_map='cpu',use_llmlingua2=True,model_config={'cache_dir':'/workspace/scratch/7c350824dec4/harness-runtime/model-cache'})
 result=compressor.compress_prompt(sample,rate=0.6,force_tokens=['.'])
 assert result['compressed_tokens']<result['origin_tokens'] and result['compressed_prompt']
 r['tests']['llmlingua']={'ok':True,'origin_tokens':result['origin_tokens'],'compressed_tokens':result['compressed_tokens'],'seconds':round(time.time()-start,2),'donnees':'instructions éditoriales synthétiques; aucun seuil, dose ou extrait médical'}
else:r['tests']['llmlingua']={'ok':False,'raison':'modèle non exécuté par cette invocation'}
r['fonctionnel_complet']=all(x['ok'] for x in r['tests'].values())
print(json.dumps(r,ensure_ascii=False,indent=2))

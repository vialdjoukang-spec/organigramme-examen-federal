#!/usr/bin/env python3
"""Exerce réellement trois outils; n'appelle aucune API IA payante."""
import argparse
import atexit
import shutil
from datetime import datetime, timezone
import importlib.metadata as md
import json
from pathlib import Path
import tempfile
import time
import uuid

MODEL = 'microsoft/llmlingua-2-bert-base-multilingual-cased-meetingbank'
REVISION = '5f0c82792b7ea14c6484e015b6a072009496b7f2'

def probe(agent, model_cache):
    result = {'schema_version': 1, 'agent': agent, 'run_id': str(uuid.uuid4()),
              'tested_at': datetime.now(timezone.utc).isoformat(),
              'versions': {n: md.version(n) for n in ('chonkie','llmlingua','gptcache','torch','transformers')},
              'tests': {}, 'medical_source_compressed': False}
    from chonkie import TokenChunker
    sample = 'The editor keeps the section order and removes repeated editorial instructions. ' * 8
    chunks = TokenChunker(tokenizer='character', chunk_size=100, chunk_overlap=0)(sample)
    exact = ''.join(c.text for c in chunks) == sample
    if len(chunks) < 2 or not exact:
        raise RuntimeError('Chonkie: découpage ou reconstruction incorrects')
    result['tests']['chonkie'] = {'ok': True, 'chunks': len(chunks), 'exact_reconstruction': exact}
    from gptcache import Cache
    from gptcache.manager import get_data_manager
    from gptcache.processor.pre import get_prompt
    from gptcache.adapter.api import put, get
    tmp=tempfile.mkdtemp(prefix='gptcache-probe-')
    # Inscrit avant Cache.init: le cache ferme avant la suppression à la sortie.
    atexit.register(shutil.rmtree,tmp,ignore_errors=True)
    cache = Cache()
    cache.init(pre_embedding_func=get_prompt, data_manager=get_data_manager(data_path=str(Path(tmp)/'cache.map')))
    key = 'editorial-probe|' + str(uuid.uuid4())
    if get(key, cache_obj=cache) is not None:
        raise RuntimeError('GPTCache: clé neuve déjà présente')
    put(key, 'Preserve the original section order.', cache_obj=cache)
    if get(key, cache_obj=cache) != 'Preserve the original section order.':
        raise RuntimeError('GPTCache: lecture différente de l’écriture')
    if get(key+'|different', cache_obj=cache) is not None:
        raise RuntimeError('GPTCache: collision entre clés distinctes')
    cache.flush()
    result['tests']['gptcache'] = {'ok': True, 'mode': 'exact-match', 'write_read': True, 'distinct_key_miss': True}
    from llmlingua import PromptCompressor
    start = time.monotonic()
    compressor = PromptCompressor(model_name=MODEL, device_map='cpu', use_llmlingua2=True,
        model_config={'revision': REVISION, 'cache_dir': str(model_cache)})
    compressed = compressor.compress_prompt(sample, rate=0.6, force_tokens=['.'])
    before, after = compressed['origin_tokens'], compressed['compressed_tokens']
    if not isinstance(before, int) or not isinstance(after, int) or not 0 < after < before or not compressed['compressed_prompt']:
        raise RuntimeError('LLMLingua: compression réelle non démontrée')
    result['tests']['llmlingua'] = {'ok': True, 'origin_tokens': before, 'compressed_tokens': after,
        'model': MODEL, 'revision': REVISION, 'seconds': round(time.monotonic()-start, 3)}
    result['complete'] = True
    return result

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--agent', required=True)
    parser.add_argument('--model-cache', type=Path, default=Path.home()/'.cache/huggingface/hub')
    parser.add_argument('--output', required=True, type=Path)
    args=parser.parse_args()
    try:
        result=probe(args.agent, args.model_cache)
        exit_code=0
    except Exception as exc:
        result={'schema_version':1,'agent':args.agent,'tested_at':datetime.now(timezone.utc).isoformat(),
                'complete':False,'error':type(exc).__name__+': '+str(exc)[:700]}
        exit_code=1
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))
    return exit_code
if __name__=='__main__':
    raise SystemExit(main())

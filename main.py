import json
import time
import requests

def deepl_translator(sentence):
    data = {
        "jsonrpc":"2.0",
        "method":"LMT_handle_jobs",
        "params":{
            "jobs":[
                {
                    "kind":"default",
                    "raw_en_sentence": sentence,
                    "raw_en_context_before": [],
                    "raw_en_context_after": [],
                    "preferred_num_beams": 4,
                    "quality": "fast"
                }
            ],
            "lang":{
                "user_preferred_langs":["EN", "ZH"],
                "source_lang_user_selected":"auto",
                "target_lang":"EN"
            },
            "priority": -1,
            "timestamp": int(time.time() * 10000),
        }
    }
    r = requests.post('https://www2.deepl.com/jsonrpc', headers={'content-type': 'application/json'}, data=json.dumps(data))
    return r.json()['result']['translations'][0]['beams']
  
print(deepl_translator('你好'))
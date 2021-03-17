
import re
import time
import os
import json
import translators as ts

from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch(
    ['192.168.11.27'], 
    http_auth=('elastic', 'Pekalles12#$'),
    scheme='http', port=9200)

zh_regex = re.compile(r'[\u4e00-\u9fa5]') # 匹配中文字符
key_regex = re.compile(r'[^a-z0-9]')

def build_es_dict():
    es_dict = {}
    
    ''' 从es中读取中英文字典'''
    res = es.search(index='pekall-py-trans-zh-en', 
                body={ "size": 5000 })
    for doc in res['hits']['hits']:
        es_dict[doc['_source']['zh']] = doc['_source']['en']
    
    return es_dict
    # json.dumps(es_dict, indent=2, default=str)
    
def trans_zh_en(zh, es_dict):
    ''' 将中文翻译为英文。首先通过es字典，没找到则在线查询google'''

    trans_value = es_dict.get(zh)
    if not trans_value:
        print(f'google trans: {zh}')
        trans_value = ts.google(zh, 'zh', 'en')
        time.sleep(1)
        
        # 将翻译值添加缓存和es中
        es_dict[zh] = trans_value
        es.index(index='pekall-py-trans-zh-en', 
            body={
                'zh': zh,
                'en': trans_value
            })
        es.indices.refresh(index='pekall-py-trans-zh-en')
        
    trans_key = key_regex.sub('_', trans_value.lower()[:45])
    trans_value = trans_value.capitalize()

    return (trans_key, trans_value)


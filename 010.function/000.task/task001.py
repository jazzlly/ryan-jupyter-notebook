
#%%

'''
定时获取fyna数据，保存到es中
1. 获取全量数据，保存到es中
2. 获取增量数据，保存到es中
3. 定时任务，获取增量数据
'''

#%%
import numpy as np
import pandas as pd
import akshare as ak

import json
import time
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from elasticsearch import NotFoundError

es = Elasticsearch(
    ['192.168.10.252'], 
    http_auth=('elastic', 'Ryanes12#$'),
    scheme='http', port=9200)

#%%
def es_bulk(df, genDocFunc):
    """
        bulk insert dataframe to es
    """
    docs=[]
    for idx in df.index:
        docs.append(genDocFunc(df, idx))
        if (len(docs) >= 100):
            print(f'begin bulk: {time.time()}')
            helpers.bulk(es, docs)
            docs = []
            print(f'end bulk: {time.time()}')
            
    if docs:
        helpers.bulk(es, docs)
        docs = []

def getLastRecordDateInEs_macro_china_gksccz(es):
    """
        获取央行宏观操作的最新数据日期, yyyy-mm-dd
    """
    try:
        res = es.search(index='pyfy_macro_china_gksccz', 
        body= {
            "size": 1,
            "sort": [
                {
                    "operation_from_date": {
                        "order": "desc"
                    }
                }
            ]
        })
    except NotFoundError:
        print('index not exists!')
        return '1970-01-01'
    
    if not res['hits']['hits']:
        return '1970-01-01'

    for hit in res['hits']['hits']:
        # print(json.dumps(hit['_source'], indent=2))
        a, _=hit['_source']['operation_from_date'].split('T', 2)
    return a

def getLastRecordDateInEs_pyfy_rate_interbank(es):
    """
        获取Shibor最新数据日期, yyyy-mm-dd
    """
    try:
        res = es.search(index='pyfy_rate_interbank', 
        body= {
            "size": 1,
            "sort": [
                {
                    "date": {
                        "order": "desc"
                    }
                }
            ]
        })
    except NotFoundError:
        print('index not exists!')
        return '1970-01-01'

    if not res['hits']['hits']:
        return '1970-01-01'
    
    for hit in res['hits']['hits']:
        # print(json.dumps(hit['_source'], indent=2))
        a, _=hit['_source']['date'].split('T', 2)
    return a

def gen_macro_china_gksccz_doc(df, idx):
    """央行逆回购信息"""
    return {
        '_index': 'pyfy_macro_china_gksccz',
        '_source': {
            'operation_from_date': datetime.strptime(
                df['operation_from_date'][idx], "%Y-%m-%d"),
            'rate': float(df['rate'][idx]),
            'trading_method': df['trading_method'][idx],
            'deal_amount': float(df['deal_amount'][idx]),
            'period': float(df['period'][idx]),
        }
    }

def gen_rate_interbank_doc(df, idx):
    """ Shibor隔夜利率 """
    return {
        '_index': 'pyfy_rate_interbank',
        '_source': {
            'date': datetime.strptime(df['日期'][idx], "%Y-%m-%d"),
            'rate_pct': float(df['利率(%)'][idx]),
            'trend': df['涨跌(BP)'][idx]
        }
    }

# 获取央行宏观操作更新数据
last_date = getLastRecordDateInEs_macro_china_gksccz(es);
macro_china_gksccz_df = ak.macro_china_gksccz()
df = macro_china_gksccz_df[::-1][macro_china_gksccz_df['operation_from_date'] > last_date]
es_bulk(df, gen_macro_china_gksccz_doc)

# 获取Shibor隔夜利率数据
last_date = getLastRecordDateInEs_pyfy_rate_interbank(es);
page = '100' if last_date == '1970-01-01' else '5'
rate_interbank = ak.rate_interbank(market="上海银行同业拆借市场", 
    symbol="Shibor人民币", indicator="隔夜", need_page=page);
df = rate_interbank[rate_interbank['日期'] > last_date]
es_bulk(df, gen_rate_interbank_doc)


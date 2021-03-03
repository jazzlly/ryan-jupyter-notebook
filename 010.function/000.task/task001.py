
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

def getLastRecordDateInEs(es, es_index):
    """
        获取es最新数据日期, yyyy-mm-dd
    """
    print(f'get last record date for index: {es_index}')

    try:
        res = es.search(index=es_index, 
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
        print('not data in index!')
        return '1970-01-01'

    for hit in res['hits']['hits']:
        print(json.dumps(hit['_source'], indent=2))

        date = hit['_source']['date']
        print(date)
        if 'T' in date:
            a, _=hit['_source']['date'].split('T', 2)
        else:
            a=hit['_source']['date']
    return a

def getLastRecordDateInEs_macro_china_gksccz(es):
    """
        获取央行宏观操作的最新数据日期, yyyy-mm-dd
    """
    return getLastRecordDateInEs(es, 'pyfy_macro_china_gksccz')
    

def getLastRecordDateInEs_pyfy_rate_interbank(es):
    """
        获取Shibor最新数据日期, yyyy-mm-dd
    """
    return getLastRecordDateInEs(es, 'pyfy_rate_interbank')
    

def getLastRecordDateInEs_bond_investing_global(es):
    """
        获取中国10年期国债最新数据日期, yyyy-mm-dd
    """
    return getLastRecordDateInEs(es, 'pyfy_bond_investing_global')

def gen_macro_china_gksccz_doc(df, idx):
    """央行逆回购信息"""
    return {
        '_index': 'pyfy_macro_china_gksccz',
        '_source': {
            'operation_from_date': datetime.strptime(
                df['operation_from_date'][idx], "%Y-%m-%d"),
            'date': datetime.strptime(
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
    
def gen_bond_investing_global_doc(df, idx):
    """ 中国10年期国债 """
    return {
        '_index': 'pyfy_bond_investing_global',
        '_source': {
            'date': idx.strftime('%Y-%m-%d'),
            'close': float(df['收盘'][idx]),
            'open': float(df['开盘'][idx]),
            'trend': df['涨跌幅'][idx]
        }
    }

def gen_stock_zh_index_daily_doc(df, idx):
    """ 上证指数 """
    return {
        '_index': 'pyfy_stock_zh_index_daily',
        '_source': {
            'date': idx.strftime('%Y-%m-%d'),
            'close': float(df['close'][idx]),
            'open': float(df['open'][idx]),
            'volume': df['volume'][idx]
        }
    }

def gen_macro_china_shrzgm_doc(df, idx):
    """ 社融数据 """
    date=df['月份'][idx]
    
    return {
        '_index': 'pyfy_macro_china_shrzgm',
        '_source': {
            'date': date[:4] + '-' + date[4:] + '-01',
            'srzl': float(df['社会融资规模增量'][idx])
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

# 中国十年期国债
last_date = getLastRecordDateInEs(es, 'pyfy_bond_investing_global')
localtime = time.strftime('%Y-%m-%d', time.localtime())

if (last_date != localtime):
    bond_investing_global_df = ak.bond_investing_global(
        country="中国", index_name="中国10年期国债", period="每日", 
        start_date=last_date, end_date=time.strftime(
            '%Y-%m-%d', time.localtime()))
    es_bulk(bond_investing_global_df, gen_bond_investing_global_doc)
    
# 获取上证指数
df = ak.stock_zh_index_daily(symbol="sh000001")
last_date = getLastRecordDateInEs(es, "pyfy_stock_zh_index_daily")
es_bulk(df[df.index > last_date], gen_stock_zh_index_daily_doc)

# 社融数据
last_date = getLastRecordDateInEs(es, 
    "pyfy_macro_china_shrzgm").replace('-', '')[:6]
df = ak.macro_china_shrzgm()
print(last_date)
es_bulk(df[df['月份'] > last_date], 
    gen_macro_china_shrzgm_doc)

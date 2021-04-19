
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
import time

import json
import time
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from elasticsearch import NotFoundError
# from task001 import getLastRecordDateInEs
# from task001 import es_bulk

es = Elasticsearch(
    ['192.168.10.252'], 
    http_auth=('elastic', 'Ryanes12#$'),
    scheme='http', port=9200)

#%%

# 美国10年期国债
last_date = '2021-04-01'
df = ak.bond_investing_global(
    country="美国", index_name="美国10年期国债", period="每日", 
    start_date=last_date, end_date=time.strftime(
        '%Y-%m-%d', time.localtime()))
print('done!')
#%%
def gen_rate_interbank_doc(df, idx):
    """ Shibor隔夜利率 """
    return {
        '_index': 'pyfy_rate_interbank',
        '_source': {
            'date': datetime.strptime(df['日期'][idx], "%Y-%m-%d"),
            'rate_pct': float(df['利率'][idx]),
            'trend': df['涨跌'][idx]
        }
    }
    
# 获取Shibor隔夜利率数据
last_date = '2021-04-01'
page = '100' if last_date == '1970-01-01' else '5'
rate_interbank = ak.rate_interbank(market="上海银行同业拆借市场", 
    symbol="Shibor人民币", indicator="隔夜", need_page=page);
df = rate_interbank[rate_interbank['日期'] > last_date]
# es_bulk(df, gen_rate_interbank_doc)


#%%
index_us_dollar_df = ak.index_investing_global(
    country="美国", index_name="美元指数", period="每日", 
    start_date="2007-01-01", end_date="2021-04-06")
print(index_us_dollar_df)
print(index_us_dollar_df.info())
#%%
# 比特币
def gen_index_us_dollar_doc(df, idx):
    """ 美元指数 """
    return {
        '_index': 'pyfy_index_us_dollar',
        '_source': {
            'date': idx.strftime('%Y-%m-%d'),
            'open': float(df['开盘'][idx]),
            'close': float(df['收盘'][idx]),
            'amount': float(df['交易量'][idx])
        }
    }
    
last_date = getLastRecordDateInEs(es, "pyfy_index_us_dollar")
localtime = time.strftime('%Y-%m-%d', time.localtime())

if (last_date != localtime):
    index_us_dollar_df = ak.index_investing_global(
        country="美国", index_name="美元指数", period="每日", 
        start_date=last_date, end_date=localtime)
    index_us_dollar_df = index_us_dollar_df[::-1]
    
    es_bulk(index_us_dollar_df, gen_index_us_dollar_doc)
#%%
# 比特币
def gen_crypto_hist_bitcoin_doc(df, idx):
    """ 比特币 """
    return {
        '_index': 'pyfy_crypto_hist_bitcoin',
        '_source': {
            'date': idx.strftime('%Y-%m-%d'),
            'open': float(df['开盘'][idx]),
            'close': float(df['收盘'][idx]),
            'amount': float(df['交易量'][idx]),
            'trend': df['涨跌幅'][idx]
        }
    }
    
last_date = getLastRecordDateInEs(es, "pyfy_crypto_hist_bitcoin")
last_date = last_date.replace('-', '')
localtime = time.strftime('%Y%m%d', time.localtime())

if (last_date != localtime):
    crypto_hist_df = ak.crypto_hist(symbol="比特币", period="每日", 
                                start_date=last_date, 
                                end_date=localtime)
    crypto_hist_df = crypto_hist_df[::-1]
    
    es_bulk(crypto_hist_df, gen_crypto_hist_bitcoin_doc)
    

#%%
macro_china_gksccz_df = ak.macro_china_gksccz()
df = macro_china_gksccz_df[::-1]

#%%
def getLastRecordDateInEs_macro_china_gksccz(es):
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

    if not res['hits']['hits']:
        return '1970-01-01'
        
    for hit in res['hits']['hits']:
        # print(json.dumps(hit['_source'], indent=2))
        a, _=hit['_source']['operation_from_date'].split('T', 2)
    return a

last_date = getLastRecordDateInEs_macro_china_gksccz(es);
macro_china_gksccz_df = ak.macro_china_gksccz()
df = macro_china_gksccz_df[::-1][macro_china_gksccz_df['operation_from_date'] > last_date]

print(df)
#%%

def getLastRecordDateInEs_pyfy_rate_interbank(es):
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

    for hit in res['hits']['hits']:
        # print(json.dumps(hit['_source'], indent=2))
        a, _=hit['_source']['date'].split('T', 2)
    return a

last_date = getLastRecordDateInEs_pyfy_rate_interbank(es);
rate_interbank = ak.rate_interbank(market="上海银行同业拆借市场", 
    symbol="Shibor人民币", indicator="隔夜", need_page="5");

df = rate_interbank[rate_interbank['日期'] > last_date]
#%%


#%%
# 央行公开操作, 
# 逆回购：央行给商业银行贷款，商业银行抵押债券给央行。到期后商业银行还钱，收回债券
import akshare as ak

macro_china_gksccz_df = ak.macro_china_gksccz()
df = macro_china_gksccz_df[::-1]

# type(df['operation_from_date'])
type(macro_china_gksccz_df['operation_from_date'][0])
# rate trading_method deal_amount period operation_from_date
line = {
    'operation_from_date': datetime.strptime(
        df['operation_from_date'][0], "%Y-%m-%d"),
    'rate': float(df['rate'][0]),
    'trading_method': df['trading_method'][0],
    'deal_amount': float(df['deal_amount'][0]),
    'period': float(df['period'][0]),
}

line


#%%

#%%
from datetime import datetime
print('hello world')
dt = datetime.strptime('2021-02-12', "%Y-%m-%d")
print(dt)
print(type(dt))


#%%
'''
定时获取最新财经消息，发送到邮箱
'''

import akshare as ak
js_news_df = ak.js_news(indicator='最新资讯')
# js_news_df = ak.js_news(indicator='最新数据')
# print(js_news_df)
# js_news_df.to_excel('news.xlsx')

# print(type(js_news_df))
# js_news_df['content']
for i in range(len(js_news_df)):
    print(f"{js_news_df.iloc[i, 0]}")
    print(f"{js_news_df.iloc[i, 1]}")
    print()
    
#%%

try:
    res = es.search(index='index_not_exist', 
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


#%%
last_date = '1970-01-02'
page = '100' if last_date == '1970-01-01' else '5'
page

#%% 

def getLastRecordDateInEs_bond_investing_global(es):
    """
        获取中国10年期国债最新数据日期, yyyy-mm-dd
    """
    try:
        res = es.search(index='pyfy_bond_investing_global', 
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
        return '2000-01-01'
    
    if not res['hits']['hits']:
        return '1970-01-01'

    for hit in res['hits']['hits']:
        # print(json.dumps(hit['_source'], indent=2))
        a, _=hit['_source']['date'].split('T', 2)
    return a

def gen_bond_investing_global_doc(df, idx):
    """ 中国10年期国债 """
    return {
        '_index': 'pyfy_rate_interbank',
        '_source': {
            'date': idx.strftime('%Y-%m-%d'),
            'close': float(df['收盘'][idx]),
            'open': float(df['开盘'][idx]),
            'trend': df['涨跌幅'][idx]
        }
    }
    
bond_investing_global_df = ak.bond_investing_global(
    country="中国", index_name="中国10年期国债", period="每日", 
    start_date="2021-01-01", end_date=time.strftime(
        '%Y-%m-%d', time.localtime()))
# print(bond_investing_global_df
# getLastRecordDateInEs_bond_investing_global(es)

for idx in bond_investing_global_df.index:
    print(gen_bond_investing_global_doc(bond_investing_global_df, idx))


#%% 上证指数历史数据
import akshare as ak

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

df = ak.stock_zh_index_daily(symbol="sh000001")
# print(stock_zh_index_daily_df)
# df = stock_zh_index_daily_df[stock_zh_index_daily_df.index > ]

for idx in df.index:
    doc = gen_stock_zh_index_daily_doc(
        df, idx)
    print(doc)
    break

#%%
import akshare as ak

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

df = ak.macro_china_shrzgm()
print(df)
for idx in df.index:
    print(gen_macro_china_shrzgm_doc(df, idx))
    break

#%%

def gen_bond_investing_global_zh_10_doc(df, idx):
    """ 中国十年期国债 """
    return {
        '_index': 'pyfy_bond_investing_global_zh_10',
        '_source': {
            'date': idx.strftime('%Y-%m-%d'),
            'close': float(df['收盘'][idx]),
            'trend_pct': df['涨跌幅'][idx]
        }
    }

df = ak.bond_investing_global(
    country="中国", index_name="中国10年期国债", period="每日", 
    start_date="2005-01-01", end_date=time.strftime(
        '%Y-%m-%d', time.localtime()))

for idx in df.index:
    doc = gen_bond_investing_global_zh_10_doc(df, idx)
    print(doc)
    break

#%%

def gen_bond_investing_global_us_10_doc(df, idx):
    """ 中国十年期国债 """
    return {
        '_index': 'pyfy_bond_investing_global_us_10',
        '_source': {
            'date': idx.strftime('%Y-%m-%d'),
            'close': float(df['收盘'][idx]),
            'trend_pct': df['涨跌幅'][idx]
        }
    }

df = ak.bond_investing_global(
    country="美国", index_name="美国10年期国债", period="每日", 
    start_date="2005-01-01", end_date=time.strftime(
        '%Y-%m-%d', time.localtime()))

for idx in df.index:
    doc = gen_bond_investing_global_us_10_doc(df, idx)
    print(doc)
    break

#%%
date='202012'
print(date[:4])
print(date[4:])
print(date[:4] + '-' + date[4:] + '-01')


#%%
'2020-11-23'.replace('-', '')[:6]
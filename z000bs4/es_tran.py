#%%
"""
todo: 需要排除的文件
service_protocol.html
client_license.html
contains(function(), functionrandomString), window.location

script 标签不需要翻译

汉字的重复情况
 '请选择', '请选择', '请选择', '输入名称进行搜索', '获取中...', '请选择蓝牙白名单组', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', 
"""

#%%

    
#%% 将带翻译的句子提取到列表中
import re
import time
import os
import json
import translators as ts
from bs4 import Comment
from bs4 import BeautifulSoup
from bs4 import NavigableString

from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch(
    ['192.168.11.27'], 
    http_auth=('elastic', 'Pekalles12#$'),
    scheme='http', port=9200)

zh_regex = re.compile(r'[\u4e00-\u9fa5]')
exclude_files = ['client_license.html', 'service_protocol.html', 'templates']

def tagWithChinseAttrs(tag):
    for v in tag.attrs.values():    
        if isinstance(v, str) and zh_regex.search(v):
            return True
    return False

def get_zh_to_trans(file):
    to_trans = []
    
    for f in exclude_files:
        if f in file:
            return to_trans
    
    soup = BeautifulSoup(open(file, mode='r', encoding='utf-8'), 'html.parser')

    for tag in soup.find_all(tagWithChinseAttrs):
        for k, v in tag.attrs.items():
            if isinstance(v, str) and zh_regex.search(v):
                to_trans.append(v)
                break

    # for tag in soup(string=re.compile(r'[\u4e00-\u9fa5]')):
    for tag in soup(string=zh_regex):
        if (isinstance(tag, Comment)):
            continue
        
        # print(tag.parent.name);
        if (tag.parent.name == 'script' or tag.parent.name == 'style'):
            continue
        
        s = re.sub(r'\s+', '', tag)
        to_trans.append(s)
        
    return to_trans

to_trans = []

for root, dirs, files in os.walk("c:/Users/think/git/pekall/web/web-admin"):
    for file in files:
        if file.endswith(".html"):
            print(os.path.join(root, file))
            candidates = get_zh_to_trans(os.path.join(root, file))
            print(candidates)
            to_trans.extend(candidates)

for zh in to_trans:
    print(zh)
    res = es.search(index='pekall-py-trans-zh-en', 
        body={
            "query": {
                "term": {
                    "zh": {
                        "value": zh
                    }
                }
            }
        }
    )

    # print(json.dumps(res, indent=2))
    if res['hits']['hits']:
        print("found in es")
    else:
        print(f"no hits, google trans: {zh}")
        time.sleep(1)
        res = es.index(index='pekall-py-trans-zh-en', 
            body={
            'zh': zh,
            'en': ts.google(zh, 'zh', 'en')
        })


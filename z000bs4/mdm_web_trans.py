
#%%

import re
import time
import os
import json
from numpy.core.einsumfunc import einsum
import translators as ts
from bs4 import Comment
from bs4 import BeautifulSoup
from bs4 import NavigableString

from datetime import datetime
from elasticsearch import Elasticsearch
from translate import Translator

es = Elasticsearch(
    ['192.168.11.27'], 
    http_auth=('elastic', 'Pekalles12#$'),
    scheme='http', port=9200)

exclude_files = ['client_license.html', 'service_protocol.html', 'templates']
zh_regex = re.compile(r'[\u4e00-\u9fa5]')

def build_es_dict(es):
    es_dict = {}
    res = es.search(index='pekall-py-trans-zh-en', 
                body={ "size": 5000 })
    for doc in res['hits']['hits']:
        es_dict[doc['_source']['zh']] = doc['_source']['en']
    
    return es_dict

def tagWithChinseAttrs(tag):
    for v in tag.attrs.values():    
        if isinstance(v, str) and zh_regex.search(v):
            return True
    return False

def trans_zh_en(zh, lang_dict, ts):
    trans_value = lang_dict.get(zh)

    if not trans_value:
        print(f'google trans: {zh}')
        trans_value = ts.google(zh, 'zh', 'en')
        time.sleep(1)
    
    trans_key = trans_value.replace(' ', '_').lower()[:45]
    # print(f'zh: {zh}, en: {trans_value}, en_key: {trans_key}')
    return (trans_key, trans_value)

# todo: implement
def add_lang_props_to_resource(key, en, zh, filename):
    key = f'p_il8n_{key}'
    print()
    print(f"add lang props, key: {key}, en: {en}, zh: {zh}， filename: {filename}")
    print("todo: not implemented!")

es_dict = build_es_dict(es)

file_regex = re.compile(r'[/\\]')

def trans_html(fullname):
    tokens = file_regex.split(fullname)

    soup = BeautifulSoup(
        open(fullname, mode='r', encoding='utf-8'), 'html.parser')

    for tag in soup.find_all(tagWithChinseAttrs):
        for k, v in tag.attrs.items():
            if isinstance(v, str) and zh_regex.search(v):
                trans_key, trans_value = trans_zh_en(v, es_dict, ts)
                tag['data-i18n-attr']=f"{k}:p_il8n_{trans_key}"
                del tag[k]

                add_lang_props_to_resource(
                    trans_key, trans_value, v, tokens[-1])
                break

    # for tag in soup(string=re.compile(r'[\u4e00-\u9fa5]')):
    for tag in soup(string=zh_regex):
        if (isinstance(tag, Comment)):
            continue
        
        if (tag.parent.name == 'script' or
            tag.parent.name == 'style'):
            continue
        
        s = re.sub(r'\s+', '', tag)
        
        trans_key, trans_value = trans_zh_en(s, es_dict, ts)
        add_lang_props_to_resource(
            trans_key, trans_value, s, tokens[-1])
        
        if (tag.parent.name == 'div' or 
            tag.parent.name == 'a' or
            tag.parent.name == 'li' or
            tag.parent.name == 'button'):
            
            new_tag = soup.new_tag('span')
            new_tag['data-i18n-html'] = f"p_il8n_{trans_key}"
            
            tag.parent.append(new_tag)
            tag.extract()
            continue
            
        # print(s)
        # print(tag.parent.name)
        tag.parent["data-i18n-html"] = f"p_il8n_{trans_key}"
        tag.replace_with('')
        
    print('----------------------------------------------------------------')
    print(soup.prettify())

web_path = 'c:/Users/jiang/git/pekall/web/mdm/web-admin'
fullname = web_path + '/device/device_list.html'
trans_html(fullname)

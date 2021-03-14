
#%%

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
from translate import Translator

es = Elasticsearch(
    ['192.168.11.27'], 
    http_auth=('elastic', 'Pekalles12#$'),
    scheme='http', port=9200)

exclude_files = ['client_license.html', 'service_protocol.html', 'templates', 'third_party']
zh_regex = re.compile(r'[\u4e00-\u9fa5]') # 匹配中文字符

def build_es_dict(es):
    ''' 从es中读取中英文字典'''

    es_dict = {}
    res = es.search(index='pekall-py-trans-zh-en', 
                body={ "size": 5000 })
    for doc in res['hits']['hits']:
        es_dict[doc['_source']['zh']] = doc['_source']['en']
    
    return es_dict

key_regex = re.compile(r'[^a-z0-9]')
def trans_zh_en(zh, lang_dict, ts):
    ''' 将中文翻译为英文。首先通过es字典，没找到则在线查询google'''

    trans_value = lang_dict.get(zh)
    if not trans_value:
        print(f'google trans: {zh}')
        trans_value = ts.google(zh, 'zh', 'en')
        time.sleep(1)
    
    # trans_key = trans_value.replace(' ', '_').lower()[:45]

    trans_key = key_regex.sub('_', trans_value.lower()[:45])
    trans_value = trans_value.capitalize()

    # print(f'zh: {zh}, en: {trans_value}, en_key: {trans_key}')
    return (trans_key, trans_value)

lang_prop_dict = {}
def add_lang_props_to_resource(key, en, zh, filename):
    ''' 将翻译后的中英文写入属性文件。创建一个文件名资源的dict
        {
            "device_list_en-US.properties": {
                "key1": "en1",
                "key2": "en2"
            },
            "device_list_zh-CN.properties": {
                "key1": "zh1",
                "key2": "zh2"
            }
        }
        最后将这个map追加到资源文件中
    '''
    en_prop_file_name = filename.split('.')[0] + "_en-US.properties"
    zh_prop_file_name = filename.split('.')[0] + "_zh-CN.properties"

    en_dict = lang_prop_dict.setdefault(en_prop_file_name, {})
    zh_dict = lang_prop_dict.setdefault(zh_prop_file_name, {})
    
    key = f'p_il8n_{key}'
    en_dict[key] = en
    zh_dict[key] = zh
    print(f"add lang props, key: {key}, en: {en}, zh: {zh}， filename: {filename}")

def flush_lang_prop_to_files():
    filepath = 'c:/Users/jiang/git/pekall/web/mdm/web-admin/themes/default/resource/il8n'
    for k, v in lang_prop_dict.items():
        fullname = os.path.join(filepath, k)
        print(fullname)
        # print(v)
        with open(fullname, mode='a', encoding='utf-8') as f:
            f.write('\n\n###############################')
            f.write('\n# Added python translation')
            f.write('\n###############################\n')
            for k1, v1 in v.items():
                f.write(f'{k1}={v1}\n')

def tagWithChinseAttrs(tag):
    ''' 过滤包括了中文属性的tag'''
    for v in tag.attrs.values():    
        if isinstance(v, str) and zh_regex.search(v):
            return True
    return False

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
            # tag.parent.name == 'i' or
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
    
    # 保存文件到一个后缀为.pytr.html的备份文件
    with open(fullname + '.pytr.html', mode='a', encoding='utf-8') as f:
        f.write(soup.prettify())

def is_excluded_file(fullname):
    for f in exclude_files:
        if f in fullname:
            return True
    return False

for root, dirs, files in os.walk("c:/Users/jiang/git/pekall/web/mdm/web-admin"):
    for file in files:
        if file.endswith(".html"):
            print('##########################################')
            fullname = os.path.join(root, file)
            print(fullname)
            if is_excluded_file(fullname):
                continue
            # web_path = 'c:/Users/jiang/git/pekall/web/mdm/web-admin'
            # fullname = web_path + '/device/device_list.html'
            trans_html(fullname)

flush_lang_prop_to_files()


#%%
# def flush_lang_prop_to_files():
#     filepath = 'c:/Users/jiang/git/pekall/web/mdm/web-admin/themes/default/resource/il8n'
#     for k, v in lang_prop_dict.items():
#         fullname = os.path.join(filepath, k)
#         print(fullname)
#         # print(v)
#         with open(fullname, mode='a', encoding='utf-8') as f:
#             f.write('\n\n###############################')
#             f.write('\n# Added python translation')
#             f.write('\n###############################\n')
#             for k1, v1 in v.items():
#                 f.write(f'{k1}={v1}\n')


# flush_lang_prop_to_files()
#%%
"""
todo: 需要排除的文件
service_protocol.html
client_license.html
contains(function(), functionrandomString), window.location

script 标签不需要翻译

汉字的重复情况
 '请选择', '请选择', '请选择', '输入名称进行搜索', '获取中...', '请选择蓝牙白名单组', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', '请选择', 

"Hello world!".capitalize()
"""

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
# from translate import Translator

es = Elasticsearch(
    ['192.168.11.27'], 
    http_auth=('elastic', 'Pekalles12#$'),
    scheme='http', port=9200)


zh_regex = re.compile(r'[\u4e00-\u9fa5]')
js_html_line_regex = re.compile(r"^((\s*head_html\s*=)?)(\s*)('<.+>)([\u4e00-\u9fa5，。；：,.;:\s]+)(</[^']+')(.*)$")

def get_zh_to_trans(js_html):
    ''' 从js_html行中提取中文 '''
    m = js_html_line_regex.match(js_html)
    
    if not m:
        return ''
    
    return m.group(5)

def is_excluded_file(fullname):
    exclude_files = ['third_party', 'jquery', 'bootstrap', 'test']
    
    for f in exclude_files:
        if f in fullname:
            return True
    return False

def skip_line(line):
    # 注释
    if line.strip().startswith(r'//') or line.strip().startswith(r'*'):
        return True
    # 日志
    if 'console.log' in line or 'console.error' in line:
        return True
    
    return False

def skip_line_tmp(line):
    exclude_tokens = ['Tools.getTextCode', 
                      'Tools.showMessagePage', 
                      'Tools.setCommandDialogData', 
                      'Tools.showConfirmPage',
                      'Tools.getCodeIconHtml']
    for token in exclude_tokens:
        if token in line:
            return True
    
    return False

# 待翻译的中文列表
to_trans = []

# es中已经翻译过的中文
done_trans = set()
res = es.search(index='pekall-py-trans-zh-en', 
            body={
                "size": 5000, 
                "_source": ["zh"]
                })
for doc in res['hits']['hits']:
    done_trans.add(doc['_source']['zh'])


for root, dirs, files in os.walk("c:/Users/think/git/pekall/web/web-admin"):
    for file in files:
        if file.endswith(".js"):
            fullname = os.path.join(root, file)
            if is_excluded_file(fullname):
                continue
            
            # 忽略没有自动翻译框架的文件
            with open(fullname, 'r', encoding='utf-8') as f:
                content = f.read()
                if not 'Tools.i18n.autoFill' in content:
                    print(f'skip file {fullname} without translation framework ...')
                    continue
            
            print('##########################################')
            print(fullname)
            begin_trans = False
            
            with open(fullname, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    
                    # 设置开始翻译的标识
                    if 'function Translate(reader)' in line:
                        begin_trans = True
                    
                    if not begin_trans:
                        continue
                        
                    if skip_line(line):
                        continue
                    if skip_line_tmp(line): # todo: 调试使用，需要去掉
                        continue
                    if zh_regex.search(line):
                        zh = get_zh_to_trans(line)
                        if zh:
                            to_trans.append(zh)
                            print(line)
            
print(len(to_trans))

def do_trans(to_trans):
    for zh in to_trans:
        print(zh)

        if zh in done_trans:
            print('in done trans, continue')
            continue

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

        if res['hits']['hits']:
            print("found in es, continue")
        else:
            print(f"no hits, google trans: {zh}")
            # time.sleep(1)
            en = ts.google(zh, 'zh', 'en')
            print(f'en is {en}')
            res = es.index(index='pekall-py-trans-zh-en', 
                body={
                'zh': zh,
                # 'en': translator.translate(zh)
                'en': en
            })

        done_trans.add(zh)

retry = True
while retry:
    try:
        do_trans(to_trans)
        retry = False
    except BaseException:
        retry = True
        print("retry after 30 second ...")
        time.sleep(30)

print("Done trans!")

#%%
from translate import Translator
#在任何两种语言之间，中文翻译成英文
translator=Translator(from_lang="chinese",to_lang="english")
translation = translator.translate("早上好")
# translation = translator.translate("床前明月光，疑是地上霜;举头望明月,低头思故乡")
print(translation)

#%%


done_trans = set()
res = es.search(index='pekall-py-trans-zh-en', 
            body={ "size": 5000 })
for doc in res['hits']['hits']:
    done_trans.add(
        (doc['_source']['zh'], doc['_source']['en']))

#%%
for zh, en in done_trans:
    print(f"{zh}|{en.capitalize()}")

#%% 
"Hello world!".capitalize()

#%%
import os

for root, dirs, files in os.walk("c:/Users/jiang/git/pekall/web/mdm/web-admin"):
    for file in files:
        if file.endswith(".html"):
            print(file)
            print(os.path.join(root, file))

#%%
import re

file_regex = re.compile(r'[/\\]')
tokens = file_regex.split(fullname)

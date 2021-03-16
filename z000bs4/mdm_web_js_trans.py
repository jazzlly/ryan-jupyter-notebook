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
# from translate import Translator

es = Elasticsearch(
    ['192.168.11.27'], 
    http_auth=('elastic', 'Pekalles12#$'),
    scheme='http', port=9200)

zh_regex = re.compile(r'[\u4e00-\u9fa5]') # 匹配中文字符
regex = re.compile(r"^((\s*head_html\s*=)?)(\s*)('<.+>)([\u4e00-\u9fa5，。；：,.;:\s]+)(</[^']+')(.*)$")
file_regex = re.compile(r'[/\\]')

def tran_js_html(js_html, trans_key):
    m = regex.match(js_html)
    
    if not m:
        return 'python_translation_error!!!'
    
    if m.group(2):
        return m.group(1) + m.group(3) + m.group(4) + "' + " + 'reader("' + trans_key + '")' + " + '" + m.group(6) + m.group(7) + '\n'
    else:
        return m.group(3) + m.group(4) + "' + " + 'reader("' + trans_key + '")' + " + '"  + m.group(6) + m.group(7) + '\n'

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
    
    key = f'p_il8n_js_{key}'
    en_dict[key] = en
    zh_dict[key] = zh
    print(f"add lang props, key: {key}, en: {en}, zh: {zh}， filename: {filename}")

def flush_lang_prop_to_files():
    filepath = 'c:/Users/think/git/pekall/web/web-admin/themes/default/resource/il8n'
    for k, v in lang_prop_dict.items():
        fullname = os.path.join(filepath, k)
        print(fullname)
        # print(v)
        with open(fullname, mode='a', encoding='utf-8') as f:
            f.write('\n\n###############################')
            f.write('\n# Added python js translation')
            f.write('\n###############################\n')
            for k1, v1 in v.items():
                f.write(f'{k1}={v1}\n')
                
    print("flush_lang_prop_to_files done!")
                
def get_zh_to_trans(js_html):
    ''' 从js_html行中提取中文 '''
    m = regex.match(js_html)
    
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

# 调试使用, 正式翻译时需要去掉
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

es_dict = build_es_dict(es)

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
                    # print(f'skip file {fullname} without translation framework ...')
                    continue
            
            print('##########################################')
            print(fullname)
            begin_trans = False
            has_trans = False
            
            new_lines = [] # 新文件的行
            with open(fullname, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    new_lines.append(line)
                    
                    # 设置开始翻译的标识
                    if 'function Translate(reader)' in line:
                        begin_trans = True
                    
                    if not begin_trans:
                        continue
                    
                    if skip_line(line):
                        continue
                    
                    if skip_line_tmp(line):
                        continue
                    
                    if zh_regex.search(line):
                        zh = get_zh_to_trans(line)
                        if zh:
                            trans_key, trans_value = trans_zh_en(zh, es_dict, ts)
                            tokens = file_regex.split(fullname)
                            
                            add_lang_props_to_resource(
                                trans_key, trans_value, zh, tokens[-1])
                            
                            has_trans = True
                            nl = tran_js_html(line, f'p_il8n_js_{trans_key}')
                            del new_lines[-1]
                            new_lines.append(nl)
                            
            if has_trans:
                with open(fullname + ".pytr.js", mode='a', encoding='utf-8') as f:
                    f.writelines(new_lines)

print("################################")
print("js trans done!")
print("################################")
#%%
# flush_lang_prop_to_files()

#%%
#%%
'''
  '<a class="white check_perm_this"><i class="ace-icon fa fa-circle bigger-130 has-tooltip" title="提交审核"></i></a>' +
    
head_html = '<th class="table-sort">分发对象</th>' +

'<th class="table-sort th_time">状态更新时间</th>' +
'<th>备注</th>';

'<span  style="margin-left: 15px">设备合规，无违规项</span>' +

'<p class="check_perm_this"><i class="fa fa-folder"></i>锁定沙箱</p>' +

'<p class="check_perm_this" data-product-type="police">
    <i class="glyphicon glyphicon-new-window"></i>批量导出二维码</p>' +
    
'<button class="btn btn-sm btn-primary forbid_edit">
    <i class="ace-icon fa fa-pencil"></i>编辑</button>' +
'''
import re

regex = re.compile(r"^((\s*head_html\s*=)?)(\s*)('<.+>)([\u4e00-\u9fa5，。；：,.;:\s]+)(</[^']+')(.*)$")

def get_zh_to_trans(js_html):
    m = regex.match(js_html)
    
    if not m:
        return ''
    
    return m.group(5)
    
def tran_js_html(js_html):
    m = regex.match(js_html)
    
    if not m:
        return ''
    # print(f'g1: {m.group(1)}')
    # print(f'g2: {m.group(2)}')
    # print(f'g3: {m.group(3)}')
    # print(f'g4: {m.group(4)}')
    # print(f'g5: {m.group(5)}')
    # print(f'g6: {m.group(6)}')
    # print(f'g7: {m.group(7)}')
    
    # reader("help_danger")
    if m.group(2):
        return m.group(1) + m.group(3) + m.group(4) + "' + " + 'reader(' + m.group(5) + ')' + " + '" + m.group(6) + m.group(7)
    else:
        return m.group(3) + m.group(4) + "' + " + 'reader(' + m.group(5) + ')' + " + '"  + m.group(6) + m.group(7)

#%%
print(tran_js_html(''' '<span  style="margin-left: 15px">设备合规，无违规项</span>' + '''))

print(tran_js_html(''' head_html = '<th class="table-sort">分发对象</th>' + '''))

print(tran_js_html('''   '<a class="white check_perm_this"><i class="ace-icon fa fa-circle bigger-130 has-tooltip" title="提交审核"></i></a>' + '''))
# m = regex.match('''   '<a class="white check_perm_this"><i class="ace-icon fa fa-circle bigger-130 has-tooltip" title="提交审核"></i></a>' + ''')


print(tran_js_html(''' '<th class="table-sort th_time">状态更新时间</th>' + '''))

print(tran_js_html(''' '<th>备注</th>'; '''))
#%%
print(tran_js_html(''' '<p class="check_perm_this" data-product-type="police"><i class="glyphicon glyphicon-new-window"></i>批量导出二维码</p>' + '''))
#%%
print(tran_js_html(''' '<button class="btn btn-sm btn-primary forbid_edit"><i class="ace-icon fa fa-pencil"></i>编辑</button>' + '''))

#%%
'''
  '<a class="white check_perm_this"><i class="ace-icon fa fa-circle bigger-130 has-tooltip" title="提交审核"></i></a>' +
    
head_html = '<th class="table-sort">分发对象</th>' +

'<th class="table-sort th_time">状态更新时间</th>' +
'<th>备注</th>';

'<span  style="margin-left: 15px">设备合规，无违规项</span>' +

'<p class="check_perm_this"><i class="fa fa-folder"></i>锁定沙箱</p>' +

'<p class="check_perm_this" data-product-type="police"><i class="glyphicon glyphicon-new-window"></i>批量导出二维码</p>' +
    
'<button class="btn btn-sm btn-primary forbid_edit">
    <i class="ace-icon fa fa-pencil"></i>编辑</button>' +
'''
#%%
s = ''' '<span  style="margin-left: 15px">设备合规，无违规项</span>' '''
s = s.strip()

m = regex.search(s)

print(f'g1: {m.group(1)}')
print(f'g2: {m.group(2)}')
print(f'g3: {m.group(3)}')
print(f'g4: {m.group(4)}')
print(f'g5: {m.group(5)}')

#%%
import re
regex = re.compile(r'^[\u4e00-\u9fa5，。；：,.;:\s]+$')
match = regex.search('设备合规，无违规项')

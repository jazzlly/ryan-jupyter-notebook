#%%
import json, os, re
import translators as ts
import estrans as estr

'''
批量翻译web中的资源文件
'''

zh_regex = re.compile(r'[\u4e00-\u9fa5]') # 匹配中文字符
prop_regex = re.compile(r'^([^=]+)=(.*)$')
es_dict = estr.build_es_dict()

def parse_prop_line(line):
    ''' 解析属性为(key, value) '''
    m = prop_regex.match(line)
    if not m:
        return (None, None)
    
    return (m.group(1), m.group(2))

def trans_prop_line(line):
    ''' 翻译value包含中文的属性 '''
    key, value = parse_prop_line(line)
    if value and zh_regex.search(value):
        print(f'{key}, {value}')
        _, en = estr.trans_zh_en(value, es_dict)
        return f'{key}={en}\n'
    
    return None
    
def trans_prop_file(fullname):
    new_lines = []
    hasTrans = False
    with open(fullname, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            new_line = trans_prop_line(line)
            
            if new_line:
                new_lines.append(new_line)
                hasTrans = True
            else:
                new_lines.append(line)
                
    if hasTrans:
        return new_lines
    
    return None

dir='c:/Users/think/git/pekall/web/web-admin/https_page/themes/default/resource/il8n'
# dir='c:/Users/think/git/pekall/web/web-admin'
# dir='c:/Users/think/git/pekall/web/uni-auth-web'
for root, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith("_en-US.properties"):
            fullname = os.path.join(root, file)
            print(f'open file {fullname} ...')
            new_lines = trans_prop_file(fullname)
            
            if new_lines:
                print(f'write back to {fullname}')
                with open(fullname, 'w', encoding='utf-8') as f:
                    f.writelines(new_lines)

print("trans done!")
#%%
lines = trans_prop_file(
    r'c:/Users/think/git/pekall/web/web-admin/themes/default/resource/il8n/device_list_en-US.properties')
#%%

import json, os, re
import estrans as estr


print(trans_prop_line('config_sso=配置SSO'))
#%%
print(trans_prop_line('hahah哇哈哈'))
print('done!')

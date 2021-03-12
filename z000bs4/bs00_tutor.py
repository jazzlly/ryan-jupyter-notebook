#%%
from bs4 import BeautifulSoup

#检验是否含有中文字符
def contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

#%%
html_doc = """
<html>
    <head>
        <title>故事</title>
    </head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
<p class="story">你好</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())

#%% 
"""
soup基本结构就是DomTree<Tag>, tag有name和string的属性
name是标签的名称，string是标签的内容
如果 tag有多个child, string是none
"""
print(type(soup.html))          # bs4.element.Tag
print(type(soup.html.contents)) # list<Tag> 直系孩子
print(type(soup.html.contents[0])) # Tag
print(type(soup.html.children)) # list_iterator<Tag> 直系孩子
print(type(soup.html.descendants)) # generator<Tag> 所有子孙

#%% parent节点
print(soup.parent == None)
print(soup.html.parent == soup)
print(soup.html.head.parent == soup.html)

# string的上级节点是包含他的tag
print(soup.html.head.title.string.parent == soup.html.head.title)

#%% a节点的所有祖先
soup.a.parents

#%% 兄弟节点
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>", features="lxml")
print(sibling_soup.prettify())
print()

print(sibling_soup.b.next_sibling == sibling_soup.c)
print(sibling_soup.c.previous_sibling == sibling_soup.b)

print(sibling_soup.b.previous_sibling == None)
print(sibling_soup.c.next_sibling == None)

#%% 兄弟节点可能是换行
soup = BeautifulSoup(
    """
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
    """
    , features='lxml')
print(repr(soup.a.next_sibling)) # \n
print(soup.a.next_sibling == '\n')
print(soup.a.next_sibling.next_sibling == soup.find_all('a')[1])

#%% 所有的sibling
for sibling in soup.a.next_siblings:
    print(repr(sibling))

#%% 所有siblings
for sibling in soup.find(id='link3').previous_siblings:
    print(repr(sibling))
    
#%% 沿着dom tree遍历所有节点。节点包括Tag， NavigableString
soup = BeautifulSoup(html_doc, features='lxml')
# print(soup.prettify())

print(soup.html.next_element == '\n') # NavigableString
print(soup.html.next_element.next_element == soup.head) # Tag
print(soup.head.next_element == '\n')
print(soup.head.next_element.next_element == soup.title)
print(soup.body.next_element.next_element == soup.p)

#%%
print(soup.p.previous_element == '\n')
print(soup.p.previous_element.previous_element == soup.body)

#%%
print(soup.prettify())
print(soup.find(id='link3').next_sibling) # ;
print(soup.find(id='link3').next_element) # Tillie

#%% 向后遍历文档树
for e in soup.html.next_elements:
    print(repr(e))
    
#%% 搜索文档树

# 通过标签名过滤
print(soup.find_all('b')) # ResultSet
print(soup.find_all('b')[0]) #Tag
print(len(soup.find_all('b')))

#%% 通过标签名的正则表达式搜索文档树
import re
for tag in soup.find_all(re.compile(r'^b')):
    print(tag.name)

for tag in soup.find_all(re.compile(r't')):
    print(tag.name)

#%%
print(soup.find_all(['a', 'b']))

#%% 找到所有非NavigableString标签
for tag in soup.find_all(True):
    print(tag.name)
    
#%%
def my_filter(tag):
    return tag.has_attr('class') and not tag.has_attr('id');

for tag in soup.find_all(my_filter):
    print(tag.name)
    
print(soup.find_all(my_filter))

#%%
for tag in soup.find_all(
    lambda x : x.has_attr('class') and not x.has_attr('id')):
    print(tag.name)

#%% 过滤标签属性
for tag in soup.find_all(
    href=lambda x : x and not re.compile('lacie').search(x)):
    print(repr(tag))
    
#%% 复杂过滤
from bs4 import NavigableString

for tag in soup.find_all(lambda x: 
    isinstance(x.previous_element, NavigableString) and
    isinstance(x.next_element, NavigableString)):
    print(tag.name)
    
#%% find_all( name , attrs , recursive , string , **kwargs )

print(soup.find_all('a', {"class":"sister"}))

#%%
print(soup.find('a', id='link3'))


#%% keyword参数, 搜索navigable string
print(soup.find(string=re.compile('three little sisters')))


#%% keyword参数
for tag in soup.find_all(string=re.compile(r'[\u4e00-\u9fa5]')):
    print(tag)
    print(tag.parent)
    
#%%  keyword参数，搜索标签的属性
soup.find(href=re.compile('elsie'))
soup.find(id='link3')

#%% 搜索有id的
soup.find_all(id=True, href=re.compile('elsie'))

    
#%% css搜索
soup.find_all('a', class_='sister')
#%% find_all的简化写法
soup = BeautifulSoup(html_doc, 'html.parser')
for tag in soup(string=re.compile(r'[\u4e00-\u9fa5]')):
    print(tag)
    print(tag.parent.name)

#%% 修改标签
tag = soup.b
# tag.name = 'blockquote' 
tag['class'] = 'haha'
tag['id'] = '1234'

tag.string = 'wahaha'
tag

#%%
soup.title.append("bar") # 添加新的一行
soup.title.append(NavigableString('baz'))

#%%
new_tag = soup.new_tag('span')
new_tag['data-i18n-html'] = 'py_trans_1234'
soup.b.append(new_tag)


#%% find的简化写法
soup.head.title
# <title>The Dormouse's story</title>

soup.find("head").find("title")


#%%
soup.p['class']

#%%
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(contains_chinese(soup.title.string))
print(contains_chinese(soup.title.name))

#%%
soup.body.b

#%%
def recursiveChildren(x):
    if "childGenerator" in dir(x):
      for child in x.childGenerator():
          name = getattr(child, "name", None)
          if name is not None:
             print ("[Container Node]",child.name)
             print(type(child))
          recursiveChildren(child)
    else:
        if not x.isspace(): #Just to avoid printing "\n" parsed from document.
            # print(type(x))
            print ("[Terminal Node]",x)
            print(f'contain chinese: {contains_chinese(x)}')
            print(x.parent)

for child in soup.childGenerator():
    recursiveChildren(child)
    
#%%


#%% 替换标签的文字
soup.title.string.replace_with("haha") 
print(soup.prettify())

#%%
# from bs4.element import Comment
import re
import time
import translators as ts
from bs4 import Comment
from bs4 import BeautifulSoup
from bs4 import NavigableString

regex = re.compile(r'[\u4e00-\u9fa5]')

def tagWithChinseAttrs(tag):
    for v in tag.attrs.values():    
        if isinstance(v, str) and regex.search(v):
            return True
    return False

soup = BeautifulSoup(open('c:/Users/think/git/pekall/web/web-admin/device/device_list.html', 
          mode='r', encoding='utf-8'), 'html.parser')

for tag in soup.find_all(tagWithChinseAttrs):
    for k, v in tag.attrs.items():
        if isinstance(v, str) and regex.search(v):
            print(f'begin trans: {v}')
            trans_value = ts.google(v, 'zh', 'en')
            time.sleep(1)
            trans_key = trans_value.replace(' ', '_').lower()[:45]
            tag['data-i18n-attr']=f"{k}:p_il8n_{trans_key}"
            del tag[k]
            break

# for tag in soup(string=re.compile(r'[\u4e00-\u9fa5]')):
for tag in soup(string=regex):
    if (isinstance(tag, Comment)):
        continue
    
    if (tag.parent.name == 'script' or
        tag.parent.name == 'style'):
        continue
    
    s = re.sub(r'\s+', '', tag)
    
    print(f'begin trans: {s}')
    trans_value = ts.google(s, 'zh', 'en')
    time.sleep(1)
    trans_key = trans_value.replace(' ', '_').lower()[:45]
    
    if (tag.parent.name == 'div' or 
        tag.parent.name == 'a' or
        tag.parent.name == 'li' or
        tag.parent.name == 'button'):
        
        new_tag = soup.new_tag('span')
        new_tag['data-i18n-html'] = f"p_il8n_{trans_key}"
        
        tag.parent.append(new_tag)
        tag.extract()
        continue
        
    print(s)
    print(tag.parent.name)
    tag.parent["data-i18n-html"] = f"p_il8n_{trans_key}"
    tag.replace_with('')
    
print('----------------------------------------------------------------')
print(soup.prettify())

#%%



    

#%%
import translators as ts

trans_value = ts.google('请求的参数传递有误', 'zh', 'en')
trans_key = trans_value.replace(' ', '_').lower()[:45]
print(trans_key)
print(trans_value)

#%%
code_map = {
    "codeMap":
    [
        {
            "61901": "应用类型-安卓客户端",
            "61902": "应用类型-苹果客户端",
            "61903": "应用类型-iPad客户端",

            "62000": "轨迹跟踪-开启",
            "62001": "轨迹跟踪-关闭",

            "62100": "设备最后报告时间-3天内报告过",
            "62101": "设备最后报告时间-已超过3天没有报告",
            "62102": "设备最后报告时间-已超过7天没有报告",

            "64031": "设备列表-显示所有用户",
            "64032": "设备列表-隐藏无设备用户",

            "62700": "统计报表数据类型-设备操作系统",
            "62718": "统计报表数据类型-设备操作系统版本",

            "62701": "统计报表数据类型-设备所属",
            "62702": "统计报表数据类型-设备管理状态",
            "62703": "统计报表数据类型-设备在线状态",

            "62716": "统计报表数据类型-设备数量",
            "62717": "统计报表数据类型-新增设备数",

            "62719": "统计报表数据类型-设备型号",
            "62720": "统计报表数据类型-客户端版本",

            "62721": "统计报表数据类型-用户总数",
            "62722": "统计报表数据类型-新增用户数",
            "62723": "统计报表数据类型-在线用户数",

            "62704": "统计报表数据类型-设备合规状态",
            "62705": "统计报表数据类型-设备密码状态",
            "62706": "统计报表数据类型-Root",

            "62714": "统计报表数据类型-当前漫游状态",
            "62710": "统计报表数据类型-网络统计",
            "62712": "统计报表数据类型-SIM卡国家",

            "62713": "统计报表数据类型-当前网络运营商",
            "62715": "统计报表数据类型-当前网络国家",

            "62707": "统计报表数据类型-应用安装状态",

            "62708": "统计报表数据类型-设备注册统计",

            "61861": "统计报表表格类型-平台总览",
            "61863": "统计报表表格类型-用户数量",
            "61866": "统计报表表格类型-设备安全",
            "61867": "统计报表表格类型-网络",

            "70000": "证书类型-用户证书",
            "70001": "证书类型-设备证书",

            "70010": "证书状态-正常",
            "70011": "证书状态-已冻结",
            "70012": "证书状态-已废除",
            "70020": "证书状态-已使用",
            "70021": "证书状态-使用中",

            "70030": "证书操作-签发",
            "70031": "证书操作-冻结",
            "70032": "证书操作-恢复",
            "70033": "证书操作-更新",
            "70034": "证书操作-废除",

            "80000": "标签用户范围类型-用户",
            "80003": "标签用户范围类型-职位",
            "80004": "标签用户范围类型-从事业务",
            "80005": "标签用户范围类型-机构",
            "80006": "标签用户范围类型-标签",
            "80007": "标签用户范围类型-用户分组",

            "80100": "标签用户范围关系-无关系",
            "80101": "标签用户范围关系-与",
            "80102": "标签用户范围关系-或",
            "80103": "标签用户范围关系-非",

            "80200": "设备限制条件类型-设备厂商",
            "80201": "设备限制条件类型-设备型号",
            "80202": "设备限制条件类型-设备尺寸",

            "63000": "操作-添加应用",
            "63001": "操作-更新应用",
            "63002": "操作-删除应用",
            "63003": "操作-升级应用",

            "63004": "操作-添加文档",
            "63005": "操作-更新文档",
            "63006": "操作-删除文档",

            "90001": "操作-创建用户",
            "90002": "操作-启用用户",
            "90003": "操作-停用用户",
            "90004": "操作-编辑用户手机号",
            "90005": "操作-编辑用户姓名",
            "90006": "操作-改变用户所属机构",
            "90007": "操作-改变用户所属分组",
            "90008": "操作-用户注册设备",
            "90009": "操作-编辑用户身份证",
            "90010": "操作-编辑用户工号",
            "90011": "操作-编辑用户职位",
            "90012": "操作-编辑用户从事业务",

            "90020": "操作-创建机构",
            "90021": "操作-删除机构",
            "90022": "操作-编辑机构描述",
            "90023": "操作-编辑机构全称",
            "90024": "操作-编辑机构简称",
            "90025": "操作-移动机构",

            "90040": "操作-创建管理员",
            "90041": "操作-删除管理员",
            "90042": "操作-启用管理员",
            "90043": "操作-冻结管理员",
            "90044": "操作-修改管理员密码",
            "90045": "操作-重置管理员密码",
            "90046": "操作-编辑管理员所属机构",
            "90047": "操作-编辑管理员角色",

            "90060": "操作-创建用户分组",
            "90061": "操作-删除用户分组",
            "90062": "操作-编辑用户分组名称",
            "90063": "操作-编辑用户分组描述",
            "90064": "操作-用户分组注册设备",

            "90080": "操作-新建安卓策略",
            "90081": "操作-新建苹果策略",
            "90082": "操作-启用策略",
            "90083": "操作-停用策略",
            "90084": "操作-设置默认策略",
            "90085": "操作-编辑策略名称",
            "90086": "操作-编辑策略描述",
            "90087": "操作-编辑策略",

            "90100": "操作-创建规则",
            "90102": "操作-启用规则",
            "90103": "操作-停用规则",
            "90104": "操作-设置默认规则",
            "90105": "操作-编辑规则名称",
            "90106": "操作-编辑规则描述",
            "90107": "操作-编辑规则",

            "90120": "操作-创建设备分组",
            "90121": "操作-编辑设备分组名称",
            "90122": "操作-编辑设备分组描述",
            "90123": "操作-修改设备分组过滤条件",
            "90124": "操作-删除设备分组",

            "90140": "操作-下载应用",
            "90141": "操作-编辑应用",
            "90142": "操作-更新应用安装策略",
            "90143": "操作-更新应用安全策略",

            "90160": "操作-下载文档",
            "90161": "操作-编辑文档名称",
            "90162": "操作-编辑文档下载策略",

            "90180": "操作-添加通讯录",
            "90181": "操作-删除通讯录",
            "90182": "操作-编辑通讯录名称",
            "90183": "操作-更新通讯录",
            "90184": "操作-下载通讯录",

            "90200": "操作-创建角色",
            "90201": "操作-删除角色",
            "90202": "操作-编辑角色",

            "90240": "操作-添加服务器",
            "90241": "操作-编辑服务器名称",
            "90242": "操作-编辑服务器IP",
            "90243": "操作-编辑服务器掩码",
            "90244": "操作-删除服务器",

            "90260": "操作-修改CA服务器IP",
            "90261": "操作-修改CA服务器端口",
            "90262": "操作-修改VPN服务器IP",
            "90263": "操作-修改VPN服务器端口",

            "300074": "漫游状态-漫游中",
            "300075": "漫游状态-未漫游",

            "400001": "策略已存在",
            "400002": "策略不存在",
            "400003": "规则已存在",
            "400004": "规则不存在",

            "402000": "密码",
            "402001": "密码长度",
            "402002": "密码质量",
            "402100": "安全",
            "402101": "设备加密",
            "402102": "SD加密",
            "402103": "允许使用SD卡",
            "402104": "允许写SD卡",
            "402105": "禁止Keyguard功能",
            "402106": "安装非GooglePlay市场的应用",
            "402107": "安装应用前强制校验",
            "402108": "允许截屏",
            "402109": "允许剪切板",
            "402110": "备份数据",
            "402111": "自动恢复数据",
            "402112": "密码可视",
            "402113": "允许USB调试",
            "402114": "允许Google异常报告",
            "402115": "允许设备重置到出厂状态",
            "402116": "允许OTA升级",
            "402200": "功能限制",
            "402201": "后台数据同步",
            "402202": "自动同步",
            "402203": "相机",
            "402204": "允许使用蓝牙",
            "402205": "允许USB存储模式",
            "402206": "允许USB媒体播放器",
            "402207": "使用网络时间",
            "402208": "允许使用麦克风",
            "402209": "NFC",
            "402210": "通过无线信号定位",
            "402211": "通过GPS定位",
            "402212": "通过传感器辅助定位",
            "402213": "模拟定位",
            "402300": "应用",
            "402301": "应用黑名单",
            "402302": "限制应用权限",
            "402303": "应用白名单",
            "402304": "必装的应用",
            "402400": "网络限制",
            "402401": "只允许紧急通话",
            "402402": "允许WiFi",
            "402403": "允许数据网络",
            "402404": "移动接入点",
            "402405": "USB网络共享",
            "402406": "短信/彩信",
            "402407": "允许数据漫游",
            "402408": "允许漫游时同步数据",
            "402409": "允许漫游时语音通话",
            "402500": "浏览器限制",
            "402501": "浏览器允许弹窗",
            "402502": "浏览器允许JAVASCRIPT",
            "402503": "浏览器允许Cookie",
            "402504": "浏览器允许自动输入",
            "402505": "浏览器显示欺诈警告",
            "402600": "蓝牙限制",
            "402601": "允许设备通过蓝牙被发现",
            "402602": "允许蓝牙配对",
            "402603": "允许蓝牙耳机",
            "402604": "允许蓝牙免提",
            "402605": "允许A2DP蓝牙模式",
            "402606": "允许蓝牙电话呼出",
            "402607": "允许蓝牙数据传输",
            "402608": "允许蓝牙共享",
            "402609": "允许通过蓝牙连接到桌面电脑"
        }
    ],

    "carrierMap":
    [
        {
            "300054": "国家-中国",
            "300055": "国家-英国",
            "300056": "国家-美国",

            "46000": "网络运营商-中国移动",
            "46001": "网络运营商-中国联通",
            "46002": "网络运营商-中国移动",
            "46003": "网络运营商-中国电信"
        }
    ]
}

import json
import translators as ts

print(ts.google('再见，世界！', 'zh', 'en'))
# print(ts.youdao('页面未找到', 'zh', 'en'))

cmap = code_map['codeMap'][0]
# print(cmap)
# print(cmap['0'])
en_map = {}
for key in cmap.keys():
    if cmap[key]:
        print(cmap[key])
        en_map[key] = ts.google(cmap[key], 'zh', 'en')
    else:
        en_map[key] = ''
    
    print(json.dumps(en_map, indent=2, default=str))
    # break
    

# print(json.dumps(code_map, indent=2, default=str))
#%% 
import json
import translators as ts
print(ts.google('再见，世界！', 'zh', 'en'))
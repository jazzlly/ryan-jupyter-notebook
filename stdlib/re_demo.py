#%% 三个主题，模式匹配，替换，拆分

#%%
import re
s = 'foo  bar\t  barz\n haha'
words = re.split(r'\s+', s)  # 自动编译成正则表达式对象
print(words)

#%% 编译生成的正则表达式对象性能更好
regex = re.compile('\s+')
regex.split(s)

#%% 找到所有的匹配项
regex = re.compile(r'ba[^\s]+')
regex.findall(s)

#%%
text="""
Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""
pattern=r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
#re.IGNORECASE使正则表达式不区分大小写
regex=re.compile(pattern,flags=re.IGNORECASE)

print(regex.findall(text)) # 生成邮件列表

#%%
m = regex.search(text) # 文本中第一个匹配的字符串, 如果没有找到，则返回None
print(text[m.start(): m.end()])

#%%
print(regex.sub("email", text))

#%%
pattern=r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex=re.compile(pattern,flags=re.IGNORECASE)

m = regex.match('rui.jiang@pekall.com')
print(m.groups())  # 获取所有匹配组
print(f'{m.group(0)}, {m.group(1)}, {m.group(2)}, {m.group(3)}')
print(f'{m[0]}, {m[1]}, {m[2]}, {m[3]}')

# 获取匹配组的位置
print(m.start(0), m.end(0))
print(m.start(1), m.end(1))
print(m.start(2), m.end(2))

# 如果有分组的时候， 返回的是匹配到的分组的元组
# [('dave', 'google', 'com'), ('steve', 'gmail', 'com'), ('rob', 'gmail', 'com'), ('ryan', 'yahoo', 'com')]
print(regex.findall(text))

#%% 替换时可以使用\1, \2, \3表示匹配到的分组

print(regex.sub(r'username: \1, domain: \2, suffix: \3', 
        'rui.jiang@pekall.com'))
print(regex.sub(r'username: \1, domain: \2, suffix: \3', text))


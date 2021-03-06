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

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# search() vs. match()
# match从字符串开头检查
print(re.match("c", "abcdef"))      # No match
print(re.match("^.*c", "abcdef"))
# <re.Match object; span=(0, 3), match='abc'>

#%% search从任意位置开始匹配
print(re.search("c", "abcdef"))   # Match
# search可以通过定位符来匹配首字符

print(re.search("^ab", "abcdef"))   # Match
# <re.Match object; span=(0, 2), match='ab'>

#%% 多行模式下, match也仅仅匹配字符串的开始

print(re.match('X', 'A\nB\nX', re.MULTILINE))  # No match
print(re.match('A', 'A\nB\nX', re.MULTILINE))
# 仅仅匹配字符串的开始后 <re.Match object; span=(0, 1), match='A'>

#%% 多行模式下，search可以匹配到每个行的开始
print(re.search('^X', 'AX\nB\nX', re.MULTILINE)) 
# 匹配到每行的开始 <re.Match object; span=(5, 6), match='X'>

print(re.search('X', 'AX\nB\nX', re.MULTILINE))
# 匹配任意位置 <re.Match object; span=(1, 2), match='X'>

#%%
import re

key_regex = re.compile(r'[^a-z]')
s = 'WiFi traffic (M)'
s1 = regex.sub('_', s.lower()[:45])
print(s1)


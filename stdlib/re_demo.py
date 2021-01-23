#%%

import re

p = re.compile('a')
print(p.match('a'))
print(p.match('b'))


#%%

p = re.compile('ca+t')

print(p.match('cat'))
print(p.match('caat'))
m = p.match('caaat').string

print('haha')

#%% 使用r''表示不转义字符, group()方法

p = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.match('2019-03-30').group())
print(p.match('2019-03-30').group(0))
print(p.match('2019-03-30').group(1))
print(p.match('2019-03-30').groups())

year, month, day = p.match('2019-03-30').groups()

#%% search vs match

p = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.search('aaa2019-03-30').group())
print(p.search('2019-03-30bbb').group(0))
print(p.search('2019-03-30').group(1))
print(p.search('aaa2019-03-30').groups())

year, month, day = p.search('aaa2019-03-30').groups()

#%% 替换

phone = '123-123-2235 # 这是电话号码'
re.sub(r'#.*$', '', phone)
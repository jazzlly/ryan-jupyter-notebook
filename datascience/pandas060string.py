#%%

import numpy as np
import pandas as pd

s = "foo, bar,   wahaha "
words = [w.strip() for w in s.split(',')]

print(words)
#%%
'::'.join(words)

#%% 在数组和字符串中查找子串
print('foo' in words)

print('foo' in s)
print(s.find('haha'))
print(s.index('bar'))

#%%
print('far' in words)
print('far' in s)
print(s.find('kaka')) # -1
print(s.index('kaka')) # exception

#%% 字符串计数
print(s.count('a'))

#%% 字符串替换
print(s.replace(',', 'xx'))

#%% 
import re
s = 'foo  bar\t  barz\n haha'
words = re.split('\s+', s)  # 自动编译成正则表达式对象
print(words)

#%% 编译生成的正则表达式对象性能更好
regex = re.compile('\s+')
regex.split(s)

#%%
regex.findall(s)

#%%
regex.search(s)
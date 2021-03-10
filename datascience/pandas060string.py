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

#%% 对series的所有item应用正则表达式

import pandas as pd
import numpy as np
import re

data={
    'Dave':'dave@google.com',
    'Steve':'steve@gmail.com',
    'Rob':'rob@gmail.com',
    'Wes':np.nan
    }

data=pd.Series(data)
print(data)

#%% 正则匹配的广播
pattern=r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
print(data.str.findall(pattern, flags=re.IGNORECASE))
print(data.str.match(pattern,flags=re.IGNORECASE))

#%% 字符切片的广播
data.str[:5]

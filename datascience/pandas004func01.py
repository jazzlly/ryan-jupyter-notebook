#%%

import numpy as np
import pandas as pd

s = pd.Series(list('zyx'), index=list('cba'))
s

#%% 重建索引并返回新的series
s1 = s.reindex(list('abc'))
s1

#%%
s = pd.Series(list('abc'), index=range(0,5,2))
s

#%% index插值
s.reindex(index=range(6), method='ffill')

#%%
df = pd.DataFrame(np.arange(20).reshape(4,5),
    columns=list('abcde'), index=list('xyzo'))
df

#%% 行插值
df.reindex(list('x1y2z3abco'))

#%% 列插值
df.reindex(columns=list('a1b2c3d4e5'))

#%% 行列同时插值
df.reindex(list('x1y2z3abco'), columns=list('a1b2c3d4e5'))


#%% 删除行
df.drop('y')

#%% 删除行
df.drop('y', axis=0)

#%% 删除列
df.drop('c', axis=1)

#%% 删除列
df.drop('c', axis='columns')

#%% 原地删除数据
df.drop('z', axis=0, inplace=True)
df.drop('c', axis=1, inplace=True)
df

#%%
s = pd.Series(np.arange(5), index=list('abcde'))
s

#%%
s.drop('c')

#%%
s.drop(list('bc'))

#%% 通过key和下标都能索引到
s['a']

#%% 通过key和下标都能索引到
s[0]

#%% 数字切片不包括尾部
s[3:5]

#%% 索引切片包括尾部
s['d':'e']

#%% 
s[['c', 'b', 'a']]

#%%
s[[3, 2, 1]]

#%%
s[s >= 2]

#%%
s['b':'c'] = 100
s

#%%
df = pd.DataFrame(np.arange(20).reshape(4,5),
    columns=list('abcde'), index=list('xyzo'))
df

#%% 获得列
df['c']

#%%
df[['b', 'c']]

#%%
df['a':'e'] # TOD: 不支持？

#%% 获取行
df[:1]

#%%
df[:2]

#%% 过滤行

df[df['c']>3]
#%% 返回Boolean数组
df > 12

#%% 过滤并赋值
df[df < 12] = 100
df

#%%
#%%
df = pd.DataFrame(np.arange(20).reshape(4,5),
    columns=list('abcde'), index=list('xyzo'))
df

#%% 获取行
df.loc['x']

#%%
type(df.loc['x']) # series

#%% 选择行，列
df.loc['x', 'b':'e']

#%% 选择行，列
df.loc['y', ['a', 'c', 'e']]

#%% loc切片，选择到z行
df.loc[:'z']

#%%
df.loc['z':]

#%% 
df.loc[:'z', :'c']


#%% 选择行
df.iloc[0]

#%% 选择行，列
df.iloc[0, 1:4]

#%% 选择行，列
df.iloc[2, [2, 4]]

#%%
df.iloc[[1,3], [2,4]]

#%%
df

#%%
df.iloc[:, :3]

#%%
df.iloc[:, :3][df.c>10]


#%%

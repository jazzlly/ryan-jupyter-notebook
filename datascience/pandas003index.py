#%%
import pandas as pd
import numpy as np

obj= pd.Series(np.arange(4), index=list('abcd'))
obj

#%% 索引是只读的
index = obj.index
type(index)

#%% int64类型index
idx = pd.Index(np.arange(10))
idx

#%%
pd.Index(list('abcdefg'))

#%%
df = pd.DataFrame(np.arange(20).reshape(4,5), 
    columns=list('abcde'), index=range(4))
df
#%% 列是index
df.columns

#%%
df.index

#%%
df = pd.DataFrame(np.arange(20).reshape(4,5), 
    columns=list('abcde'), index=[1]*4)
df
# 行index是可以重复的
#%%
df[1:]

#%% 
idx = pd.Index([])
idx

#%% append方法
idx1 = idx.append(pd.Index(list('abcde')))
idx1

#%%
idx1 = pd.Index(list('abcde'))
idx2 = pd.Index(list('defgh'))

#%% 差集
idx1.difference(idx2)

#%% 交集
idx1.intersection(idx2)

#%%
idx1.union(idx2)

#%% index是否再集合中
idx1.isin(set('c'))

#%%
idx1.isin(set('cde'))

#%%
idx1.delete(2)

#%%
idx1.drop(list('abc'))

#%%
idx1.insert(1, 'x')

#%%

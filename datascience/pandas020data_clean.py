#%%
import pandas as pd
import numpy as np


data = pd.Series(['foo', 'bar', None, np.nan, 'wahahah'])
print(data)
    
data.isnull()
# NA: not available

#%% 丢弃NA值
data.dropna()

#%% 过滤出非空值
data[data.notnull()]

#%% 
data = pd.DataFrame([
    [1., 2., 3.,], 
    [1., 2., 3.,], 
    [1., np.nan, np.nan], 
    [np.nan, np.nan, np.nan]])

print(data)
#%% 删除所有包含了NA的行
data.dropna()

#%% 删除行中所有都是NA的行
data.dropna(how='all')

#%%
data[4] = np.nan
print(data)

data.dropna(axis=1, how='all')

#%%
data = pd.DataFrame(np.random.randn(5, 5))
print(data)

#%%
data.iloc[:4, 1] = np.nan
data.iloc[:2, 2] = np.nan
print(data)

#%% 补全缺失值
print(data)
data.fillna(0)

#%%
print(data)
data.fillna({1: 1., 2: 2.}) # 按列补全

#%% 补全原有数据
_ = data.fillna(0, inplace=True) 

#%%
df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                    [3, 4, np.nan, 1],
                    [np.nan, np.nan, np.nan, 5],
                    [np.nan, 3, np.nan, 4]],
                   columns=list('ABCD'))
df

#%% 从上向下fill
print(df)
df.fillna(method='ffill')

#%%
print(df)
df.fillna(axis=1, method='ffill')

#%% 按列fill
print(df)
df.fillna(value={'A': 0, 'B': 1, 'C': 2, 'D': 3})
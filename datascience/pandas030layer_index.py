#%%
import pandas as pd
import numpy as np

# 分层索引
data = pd.Series(np.random.randn( 9), 
    index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'], 
           [1, 2, 3, 1, 3, 1, 2, 2, 3]])

data

#%%
data.index

#%% 
data['a', 2]

#%% 选择一级索引
data['b']

#%%
data['b':'c'] # 全开区间

#%%
data[['b', 'c']]

#%%
data.loc[['b', 'c']]

#%%
print(data)
data[:, 2]
# data.loc[:, 2]

#%%
print(data)
data.unstack() # 转化为dataframe

#%%
data.unstack().stack() # dataframe转化为多层索引的series

#%% 类似一个excel, 行索引有两级， 列索引有两级

frame = pd. DataFrame(np.arange(12). reshape((4, 3)), 
    index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]], 
    columns=[['Ohio', 'Ohio', 'Colorado'], 
             ['Green', 'Red', 'Green']])

# 分层索引可以设置名称
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']

frame
#%%
frame['Ohio']

#%%
frame['Ohio']['Red']

#%%
frame['Ohio']['Red']['a', 2]

#%%
# MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']], names=[' state', 'color'])


#%% 对多级索引进行交换
print(frame)
frame.swaplevel('key1', 'key2')

#%%
print(frame)
frame.swaplevel('key1', 'key2').sort_index(level=0)

#%% 按照不同的轴和多级索引排序
print(frame)
frame.sum(level='key1') # 行剩下索引就是key1
 # level指定多级索引, axis指定轴
#%%
print(frame)
frame.sum(axis=1, level='color') # 列剩下索引就是color

#%%
print(frame)
frame.sum(axis=1, level='state').sum(level='key1')

#%% 将dataframe的列作为索引
df = pd.DataFrame({'month': [1, 4, 7, 10],
                   'year': [2012, 2014, 2013, 2014],
                   'sale': [55, 40, 84, 31]})
print(df)
df.set_index('month')

#%% 设置两列为索引
df.set_index(['year', 'month'])

#%%
df.set_index([pd.Index([1,2,3,4]), 'year'])

#%%
s = pd.Series(range(4))
df.set_index([s, s**s])


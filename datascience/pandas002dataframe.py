#%% 
import pandas as pd
import numpy as np

# dataframe本质上是一个添加了行和列索引的ndarray

data = pd.DataFrame(np.arange(20).reshape(4,5), 
    columns=list('xyzlm'), index=list('abcd'))

data.index.name = 'row'
data.columns.name = 'col'
print(data)

#%%

#%%
for i in range(len(data)):
    print(f'{i}: {data.iloc[i, 1]}, {data.iloc[i, 3]}')
    print()

#%% 列标识
data.columns

#%% 行标识
data.index

#%%
data.values

#%%
type(data.values) # ndarray

#%% 行数
len(data)

#%% 列数
data.columns.size

#%% 获取第一行
data[0:1]

#%% 
data[2:4]

#%%
type(data[0:1]) # dataframe

#%% 获取一列
data['x'] 

#%%
type(data['x']) # series

#%% 添加一列
data['m'] = [5]*4
data['n'] = np.arange(4)
data

#%%
data['o'] = data.z > 6
data

#%%
del data['o']
data

#%%
# data[4:] = [20] * 4
#%%

data = ((1,2,3), (4,5,6), (7,8,9))
df3 = pd.DataFrame(data, columns=['a', 'b', 'c'], 
    index=['x', 'y', 'z'])
df3

#%% 获取列
df3.b

#%%

data = {
    'c1': range(10),
    'c2': range(10,20),
    'c3': range(20,30)
}

df = pd.DataFrame(data)
df

#%% 输出前5行
df.head() 

#%% 输出指定列
pd.DataFrame(df, columns=['c3', 'c1'])

#%%
pd.DataFrame(df, columns=['c1', 'col_not_exist'])

#%%
df['c2']

#%%  dataframe的一列实际就是一个series
type(df['c2'])

#%%
df.c2

#%%
df.c2[0]

#%%
df2 = pd.DataFrame({
    'c1': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'c2': pd.Series([4, 5, 6], index=['l', 'm', 'n']),
})

df2

#%%
df3 = pd.DataFrame({
    'c1': {'r1': 'foo', 'r2': 'bar'},
    'c2': {'r1': 'haha', 'r2': 'wawa'},
    'c3': {'r1': 'mama', 'r2': 'papa'}
})

df3

#%% 转置
df3.T


#%%


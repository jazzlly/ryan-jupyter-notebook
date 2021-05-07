#%% memo crud

#%% 
import pandas as pd
import numpy as np

# dataframe本质上是一个添加了行和列索引的ndarray
data = pd.DataFrame(np.arange(20).reshape(4,5), 
    columns=list('xyzlm'), index=list('abcd'))

data.index.name = 'row'
data.columns.name = 'col'
data

#%% iloc可以通过数字下标访问数据 data.iloc[row, col]

for i in range(len(data)):
    print(f'row {i}: ', end='')
    for j in range(len(data.columns)):
        print(f'{data.iloc[i, j]}, ', end='')
    print()

#%% loc通过index和column访问数据 data.loc[row, col]

for r in data.index:
    for c in data.columns:
        print(f'{data.loc[r, c]}, ', end='')
    print()

#%% 数组下标访问: data[column][row]

for c in data.columns:
    for r in data.index:
        print(f'{data[c][r]}, ', end='')
    print()

#%% 列标识
data.columns

#%% 行标识
data.index

#%% ndarray
data.values

#%% 行数
len(data)

#%%
len(data.index)

#%% 列数
len(data.columns)

#%% 数组下标获取成员 data[col][row]
data['x']['c']

#%% 属性下标, data.column.row
data.x.c

#%% 获取列 data[col]
data['x'] # seria for col['x']

#%% 
data.x

#%% 通过获取列，并通过value过滤
print(data)
data['x'][data['x'] >= 10]

#%% 
data[data['x'] > 10]

#%% 
data.x[data.x>=10]

#%%
#%% 获取列
data[['x', 'z']]

type(data[['x', 'y']])  # pandas.core.frame.DataFrame

# two brackets to dataframe
type(data[['x']])  # pandas.core.frame.DataFrame

# one brackets to series
type(data['x'])  # pandas.core.series.Series

#%% 获取多列并过滤
data[['x', 'z']][data['x'] > 10][data['z'] > 10]

#%% 
data[:][data['x'] > 10]

#%%
data.loc['a']
# type(data.loc['a'])  # series, 行向量的转置

#%% 获取行，返回dataframe
data.loc[['c']]

#%% data.loc[row][col]
data.loc['a']['x']


#%% data.iloc[row][col]
data.iloc[0][0]

#%% 获取行, 转化为series
data.iloc[0]

#%% 获取行，返回dataframe
data.iloc[[0]]

#%% 获取行，返回dataframe
data.iloc[[0, -1]]

#%%  dataframe切片返回的是切片
# 通过切片获取行， 获取第一行。返回的是dataframe
data[0:1]

#%% 获取第一行
data[:1]

#%% 所有行
data[:]

#%% 所有行逆序
data[::-1] 

#%%
data[0:1]['x']['a']


#%% dataframe切片返回的是dataframe
data[2:4]

#%% dataframe切片返回的是切片
type(data[0:1]) # dataframe

#%% 获取一列, return serias
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

#%% 删除
df = pd.DataFrame(np.arange(12).reshape(3, 4),
     columns=['A', 'B', 'C', 'D'])
df
'''
   A  B   C   D
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
'''

# Drop a row by index
df.drop([0, 1])
'''
A  B   C   D
2  8  9  10  11
'''

# Drop columns
df.drop(['B', 'C'], axis=1)
'''
   A   D
0  0   3
1  4   7
2  8  11
'''


#%%
# data[4:] = [20] * 4

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

#%% reverse columns
pd.DataFrame(df, columns=df.columns[::-1])

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

#%% filter multiple conditions

data = {"grammer":["Python","C","Java","GO",np.nan,"SQL","PHP","python"],
       "score":[1,2,np.nan,4,5,6,7,10]}

df = pd.DataFrame(data)
df

#%% 提取包含字符串python的行

# df[df['grammer'] == 'Python'] # 错误!
df[df['grammer'].str.lower() == 'python']

#%% 
df.query('grammer.str.lower() == "python" | grammer.str.startswith("P")')
# df[df.eval("Salary_in_1000>=100 & (Age <60) & FT_Team.str.startswith('S').values")]
#%% 过滤组合条件, 使用 &, | 不能使用 and , or, 条件需要加上括号
df[(df['grammer'].str.lower() == 'python') |
   (df['grammer'].str.lower() == 'sql')]

#%%
df.loc[(df['grammer'].str.lower() == 'python') |
   (df['grammer'].str.lower() == 'sql')]

#%%
idx = np.where((df['grammer'].str.lower() == 'python') |
   (df['grammer'].str.lower() == 'sql'))
df.loc[idx[0]]

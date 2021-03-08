#%%

import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(12).reshape(3,4), 
    columns=list('xyzl'))
print(df)

# 从行轴方向求和
print(f'sum row: \n{df.sum(axis=0)}')
print()
print(f'sum column: \n{df.sum(axis=1)}')

#%%
print(df)
print(f'min index \n{df.idxmin()}') # 各个列最小索引
print(f'max index \n{df.idxmax()}') # 各个列最大索引

#%%
print(df)
# 默认axis=0, 按照行cumsum
print(f'cumsum row: \n{df.cumsum(axis=0)}')
print()
print(f'cumsum column: \n{df.cumsum(axis=1)}')


#%% describe 统计多维度信息
print(df)
df.describe()

#%%
s = pd.Series(list('abcdefg') * 4)
s.describe(include='all')

#%% 相关性, 计算series中index重叠的非na值的相关性

s1 = pd.Series(np.arange(5))
s2 = pd.Series(np.arange(20, 25))
s3 = pd.Series(np.arange(20, 30, 2))
s4 = pd.Series(np.arange(10, 5, -1))

s5 = pd.Series([1,2,-1, 4, 5])

print(f's1 corr s2: {s1.corr(s2)}')
print(f's1 corr s3: {s1.corr(s3)}')
print(f's1 corr s4: {s1.corr(s4)}')
print(f's1 corr s5: {s1.corr(s5)}')

#%% 协方差
print(f's1 cov s2: {s1.cov(s2)}')
print(f's1 cov s3: {s1.cov(s3)}')
print(f's1 cov s4: {s1.cov(s4)}')
print(f's1 cov s5: {s1.cov(s5)}')

#%% 股票涨跌pct
stock_pct_change = pd.DataFrame(
    {
        'google': np.arange(0, 0.5, 0.05),
        'facebook': np.arange(0, 1, 0.1),
        'maotai': np.arange(2, 1, -0.1)
    }
)

pd = stock_pct_change

#%%
print(pd.value_counts())


#%%
pd.google.corr(pd.facebook) # google和facebook的相关性

#%%
pd.maotai.corr(pd.google) # google和茅台的相关性

#%%
pd.corrwith(pd.google) # google

#%%
pd.corrwith(pd.maotai)

#%% 相关性矩阵
pd.corr()

#%% 协方差矩阵
pd.cov()

#%%
import pandas as pd

l = list('abcdefg')
l.extend('ace')
s = pd.Series(l)
s
#%%
s.unique()

#%%
s.value_counts()

#%%
pd.value_counts(s, sort=False)

#%%
print(s)
s.isin(['b', 'c'])

#%% 按列方式reshape
array = np.arange(12).reshape(3,4, order='F')
array
# array.reshape(2,6, order='F')
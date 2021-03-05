#%%
import numpy as np
import pandas as pd

data = pd. DataFrame( np.arange(12).reshape((3, 4)),
                     index=['Ohio', 'Colorado', 'New York'],
                     columns=['one', 'two', 'three', 'four'])

print(data)
data.index.map(lambda x: x[:4].upper()) # 每个index的前4个字符大写

#%%
print(data)
data.rename(index=str.title, columns=str.upper)

#%%
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
print(df)
df.rename(columns={"A": "a", "B": "b"})

#%%
print(df)
df.rename(index={0: "x", 1: "y", 2: "z"})

#%%
df.index
# RangeIndex(start=0, stop=3, step=1)
df.rename(index=str)
# Index(['0', '1', '2'], dtype='object')

#%%
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]

cats = pd.cut(ages, bins)
print(cats) # type pandas.core.arrays.categorical.Categorical

#%%
print(cats.codes) # 每个数字在箱子中的位置

#%%
cats.categories # bins

#%%
pd.value_counts(cats)

#%%
cats = pd.cut(ages, bins, right=False)
# right=False 产生[x, y)类型的半开区间
cats
#%% label=False, 返回categrical的codes
cats = pd.cut(ages, bins, labels=False)
cats
#%%
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
cats = pd.cut(ages, bins, labels=group_names)
cats

#%% 
pd.cut(np.random.rand(100), 4, precision=2)

#%%
cats = pd.qcut(np.random.randn(1000), 4) # 按照数量切成4分量
pd.value_counts(cats)
#%%
import pandas as pd
import numpy as np

#%% series的本质是一个带索引的ndarray

#%%
import pandas as pd

obj = pd.Series(['a', 'b', 'c'])
obj

#%%
for o in obj.index:
    print(f'{o}: {obj[o]}')

#%% Series = One-dimensional ndarray with axis labels (including time series).
# 类似加了一个数轴的一维array

obj = pd.Series(['a', 'b', 'c'], index=['x', 'y', 'z'])
obj

#%% 访问数轴
obj.index

#%% 
obj.values

#%%
type(obj.values) # numpy.ndarray

#%% get value
obj['x'], obj['y']

#%% 
obj = pd.Series(range(5))
obj

#%% 对所有成员进行操作
obj * 2

#%% 过滤
obj[obj>2]

#%% series是可变的
obj[0] = 100
obj

#%%
import numpy as np
np.exp(obj)

#%% Series as dict
obj = pd.Series(['a', 'b', 'c'], index=['x', 'y', 'z'])

# in是针对索引的操作
print('a' in obj)
print('y' in obj)

#%% series as dict
obj = pd.Series({'k1':'v1', 'k2':'v2'})
obj

#%% series as dict
d = {'a':'x', 'b':'y', 'c':'z'}

# 通过index来过滤
obj = pd.Series(d, index=['d', 'c', 'b'])
obj

#%% 
pd.isnull(obj)

#%% 
pd.notnull(obj)

#%% 
pd.isnull([0, 1, 2, pd.NaT, pd.NA, None, np.nan])

#%% 
obj1 = pd.Series([10, 100], index=['y', 'z'])
obj2 = pd.Series([1, 10], index=['x', 'y'])
print(obj1)
print(obj2)

obj1 + obj2
# any + NaN = NaN
#%% series的名称和series index的名称
 
obj = pd.Series([172, 168], index=['male', 'female'])
obj.name = 'avg height'
obj.index.name = 'gender'
obj

#%% 通过index顺序修改series的顺序
obj.index = ['female', 'male']
obj
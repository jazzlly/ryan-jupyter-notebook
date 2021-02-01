#%%

import numpy as np
import pandas as pd

#%%

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




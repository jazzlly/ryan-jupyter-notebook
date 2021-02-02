#%%
import pandas as pd
import numpy as np

s = pd.Series(np.arange(5))
s

#%% loc用于标签索引， iloc用于整数索引
# 中括号等效于loca

#%%
s[0]

#%%
s[:2]

#%%
s[0:]
#%%
s[-1:]

#%% 
s.iloc[0:-1]

#%%
s = pd.Series(np.arange(5), index=list('abcde'))

s['a']

#%%
s[:'d']

#%%
s.loc[:'d']
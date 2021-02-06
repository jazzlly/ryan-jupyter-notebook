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

#%% 对齐
import pandas as pd
import numpy as np

s1 = pd.Series(np.arange(4), index=list('abcd'))
s2 = pd.Series(np.arange(5), index=list('abcde'))

s1 + s2
#%%
s1.add(s2, fill_value=1000)

#%%
df1 = pd.DataFrame(np.arange(20).reshape(4,5),
    columns=list('abcde'), index=list('xyzm'))
df2 = pd.DataFrame(np.arange(20).reshape(4,5), 
    columns=list('abcdf'), index=list('xyzm'))

df1 + df2
#%%
df1.add(df2, fill_value=20)

#%%
1/ df1

#%%
df1.rdiv(1)

#%%
df2.reindex(columns=df1.columns, fill_value=100)
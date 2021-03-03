#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#%% 默认绘制折线图

s = pd.Series(np.random.randn(10).cumsum(), 
    index=np.arange(0, 100, 10))
s.plot()

#%%
df = pd.DataFrame(np.random.randn(10, 4).cumsum(axis=0), 
    columns = list('ABCD'), index = np.arange(0, 100, 10))
df.plot().bar()


#%%
list('abcde')

a = np.arange(12).reshape(3,4)
print(a)
a.cumsum()
a.cumsum(0)
# a.cumsum(1)

#%%
fig, ax = plt.subplots(2, 1)

s = pd.Series(np.random.rand(16), 
    index=list('abcdefghijklmnop'))

s.plot.bar(ax=ax[0], color='k', alpha=0.7)
s.plot.barh(ax=ax[1], color='k', alpha=0.5)

#%%
df = pd.DataFrame(np.random.rand(6,4), 
    index=list('abcdef'), columns=list('ABCD'))
# df.plot()
df.plot.bar()

#%% 柱状图重叠
df.plot.barh(stacked=True, alpha=0.5)



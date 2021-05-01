#%%
import pandas as pd
import numpy as np

# convert date range to list
date_rng = pd.date_range('2021-01-01', '2021-04-30', freq='D')
date_rng.format() # list

#%%
s = pd.Series(np.arange(len(date_rng)), index=date_rng.format())
print(s)

s1 = s[s%2 == 0]

s2 = s1.reindex(date_rng.format())
s2



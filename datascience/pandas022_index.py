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
print(cats)

#%%
print(cats.codes)

#%%
cats.categories

#%%
pd.value_counts(cats).plot()

#%%
import pandas as pd
import numpy as np

df1 = pd. DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 
                     'data1': range(7)}) 
df2 = pd. DataFrame({'key': ['a', 'a', 'b', 'd', 'b'], 
                     'data2': range(5)})

print(df1)
print(df2)

# df1.merge(df2)

# key相等的做一下笛卡尔集 inner join
df1.merge(df2, on='key')

#%%
df1 = pd. DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 
                     'data1': range(7)}) 
df2 = pd. DataFrame({'rkey': ['a', 'a', 'b', 'd', 'b'], 
                     'data2': range(5)})
# inner join
df1.merge(df2, left_on='lkey', right_on='rkey')

#%%

print(df1)
print(df2)
df1.merge(df2, left_on='lkey', right_on='rkey', how='outer')


# df1.merge(df2, left_on='lkey', right_on='rkey')
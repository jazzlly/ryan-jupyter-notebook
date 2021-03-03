#%%

import pandas as pd
import numpy as np
import json

#%% 删除重复的行

data = pd.DataFrame({
    'k1': [1, 2, 3, 3, 1], 
    'k2': [1, 2, 3, 3, 1]
})

print(data)
data.duplicated()

#%%
print(data)
data.drop_duplicates()

#%%
data['k3'] = range(5)
print(data)
data.drop_duplicates(['k1']) # 按照某一列drop


#%%
data = pd. DataFrame({
    'food': ['bacon', 'pulled pork', 'bacon', 
              'Pastrami', 'corned beef', 'Bacon', 
              'pastrami', 'honey ham', 'nova lox'],
    'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

meat_to_animal = {'bacon': 'pig', 'pulled pork': 'pig', 
                  'pastrami': 'cow', 'corned beef': 'cow', 
                  'honey ham': 'pig', 'nova lox': 'salmon'
}

print(data)
print(json.dumps(meat_to_animal, indent=2))

lowercased = data.food.str.lower()
# data['animal'] = lowercased.map(meat_to_animal)
data['animal'] = data.food.map(lambda x: meat_to_animal[x.lower()])

#%%
data

#%% 替换值

s = pd.Series([1, 2, 999, 3, 8, 999, 888, -1, 7, 888])
print(s)
s.replace(999, np.nan)

#%%
print(s)
s.replace([999, 888], np.nan)

#%%
print(s)
s.replace([888, 999], [-888, -999])

#%%
print(s)
s.replace({888:-888, 999:-999})

#%%
s = pd.Series([0, 1, 2, 3, 4])
print(s)
s.replace(0, 5)

#%%
print(s)
s.replace([1, 2], method='bfill')
#%%
df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c', 'd', 'e']})
print(df)
df.replace(0, 5)

#%%
print(df)
df.replace({0:5, 1:4, 2:3, 3:2, 4:1, 5:0})

#%%
print(df)
df.replace({'A': 0, 'B': 7, 'C': 'd'}, 100)

#%%
print(df)
df.replace({'A': {0:100, 3:300}})

#%%
df = pd.DataFrame({'A': ['bat', 'foo', 'bait'],
                   'B': ['abc', 'bar', 'xyz']})

print(df)
df.replace(regex=r'^ba.$', value='new')

#%%
print(df)
df.replace(regex={r'^ba.$': 'new', 'foo': 'xyz'})
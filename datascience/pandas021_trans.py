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

#%% 
import pandas as pd
import numpy as np
from datetime import datetime
import random

def randomDateTime():
   return datetime(
      random.choice(range(2008, 2022)), 
      random.choice(range(1, 13)), 
      random.choice(range(1, 28)))

def randomEducation():
   return random.choice(['大专', '本科', '硕士', '博士', '不限'])

def randomSalary():
   low = str(random.choice(range(9, 20))) + 'K'
   high = str(random.choice(range(20, 40))) + 'K'
   return low + '-' + high

#%% 
cnt = 100
df = pd.DataFrame({
   'createTime': [randomDateTime() for _ in range(cnt)],
   'education': [randomEducation() for _ in range(cnt)],
   'salary' : [randomSalary() for _ in range(cnt)]
})

df
#%%
def medianSalary(s):
   low, high = [int(v.replace('K', '000')) for v in s.split('-')]
   return (high + low)/2 

df['salary_mean'] = df['salary'].map(medianSalary)
df

#%%
df.groupby('education').mean()

#%%
df['createTime'].map(lambda d: d.strftime('%Y年-%m月-%d日'))

#%%
d = datetime.now().strftime('%Y年-%m月-%d日')

#%%
df.info()

#%%
df.describe()
# %%
delta = (df['salary_mean'].max() - df['salary_mean'].min()) / 3
min = df['salary_mean'].min()
bins = [min, min + delta, min + 2 * delta, min + 3*delta]

df['categories'] = pd.cut(df['salary_mean'], bins, labels = ['低','中', '高'])

# %%

df.sort_values(by='salary_mean', ascending=False)

#%%
df['salary_mean'].median()

#%%
import matplotlib.pyplot as plt

bins = np.arange(10000, 40000, 2500)


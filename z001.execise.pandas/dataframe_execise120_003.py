#%% 
import pandas as pd
import numpy as np
from datetime import datetime
import random
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码
plt.rcParams['axes.unicode_minus'] = False  # 解决符号问题

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

def medianSalary(s):
   low, high = [int(v.replace('K', '000')) for v in s.split('-')]
   return (high + low)/2 

df['salary_mean'] = df['salary'].map(medianSalary)
df

#%%
df['salary_mean'].rolling(5).mean()

#%%
# df['salary_mean'].plot()
df['salary_mean'].rolling(5).mean().plot()
# df['salary_mean'].rolling(10).mean().plot()
df['salary_mean'].rolling(20).mean().plot()

#%%
df_date_index = df.set_index('createTime')
df_date_index.sort_index().resample('W').mean()
# %%

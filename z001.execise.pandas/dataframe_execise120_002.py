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

box=pd.cut(df['salary_mean'], bins)
foo = [(v.left + v.right)/2 for v in box.value_counts().index]

# plt.bar(foo, box.value_counts().values, width=2000)
# df.salary_mean.plot(kind='hist')
df.salary_mean.plot(kind='kde')

#%%
df.salary_mean.plot(kind='kde')

#%%

# df.salary_mean.plot(kind='bar')

#%%
s = pd.Series([1, 2, 2, 3, 3, 3, 4, 4,  5, 4, 3, 2, 1])
s.plot(kind='kde')
s.plot(kind='hist')



#%%
df['test'] = df['createTime'].map(lambda x: x.strftime('%Y-%m-%d_')) + df['education']

#%%
del df['test']

#%%
# df['test'] = df['education'] + df['salary_mean'].map(lambda x: " " + str(x))
df['test'] = df['education'] + df['salary_mean'].map(str)

#%%
# df['salary_mean'].max() - df['salary_mean'].min()
df[['salary_mean']].apply(lambda x: x.max() - x.min())

# %%
ret = df[['salary_mean']].apply(lambda x: print(x), axis=0)
# %%
df1 = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
df1.apply(np.sqrt, result_type='broadcast').apply(np.sum)

df1.A = df1.A.apply(lambda x: x*3)
# %%
pd.concat([df[:1], df[-1:]])

# %%
df.iloc[[0, -1]]

#%%
df.iloc[[-1]]

#%%
df.append(df.iloc[7], ignore_index=True)

#%%
df.dtypes
df.describe()

#%%
df.set_index('createTime')

# %%
rdf=pd.DataFrame(np.random.randint(
   100, 9000, size=len(df)), columns=['random'])

df = pd.concat([df, rdf], axis=1)

#%%
df['new'] = df['salary_mean'] - df['random']

#%%
df.isnull().values.any()
# %%
arr = np.array([[False, False, False, False],
                [False, True, False, True]])
arr.any(axis=0)

#%%
df['salary_mean'].astype(np.str)

#%%
len(df[df['salary_mean'] > 20000])

#%%
df.groupby(by='education')['education'].count()
#%%
# from matplotlib import font_manager
from matplotlib.pyplot import gca
a = gca()

# fontP = font_manager.FontProperties()
# fontP.set_family('SimHei')
# fontP.set_size(14)

# for label in a.get_xticklabels():
#     label.set_fontproperties(fontP)

plt.hist(df.education, align='left')

# %%
df['education'].unique()


#%%
df[df['categories'].isnull()]

#%%

df.set_index('createTime', inplace=True)
# %%

df['salary_mean'].plot()
# %%

plt.plot(df.sort_index()['salary_mean'])

#%%
df.reset_index()
# %%
df['salary_mean'].diff()

#%%
df['salary_mean'].pct_change()

#%%
df['salary_mean'].rolling(3).mean()

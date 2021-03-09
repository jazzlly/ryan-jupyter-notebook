#%% 
from numpy.core.numeric import indices, zeros_like
import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.randn(10, 4))
print(data)
data.describe()

#%% 过滤

#%% 找出一列中绝对值大于三的值
col = data[2]
print(np.abs(col) > 2) # boolen数组
col[np.abs(col) > 2]

#%% 找出行中有绝对值大于3的行
print(np.abs(data) > 2)  # boolen dataframe
print((np.abs(data) > 2).any(1)) # boolen series

data[(np.abs(data) > 2).any(1)]

#%% 批量赋值
print(np.sign(data) * 2)
data[np.abs(data) > 2] = np.sign(data) * 2
data

#%% 随机抽样

#%% 对dataframe进行行抽样

df = pd.DataFrame(np.arange(20).reshape(5, 4))
samples = np.random.permutation(5)
print(samples)
print(df)

df.take(samples)

#%% 随机抽样
print(df)
df.sample(n=2) # 无重复的抽样

#%%
print(df)

df.sample(n=10, replace=True) # 允许重复的抽样

#%%
print(df)
df.sample(frac=0.2) # len(axis) * frac个sample返回

#%% 将数据使用矩阵进行标识，如果数据存在，对应位置为1
# 矩阵的行为数据数组的长度，矩阵的列是数据值的个数

s = pd.Series(list('abcbad'))
pd.get_dummies(s)

#%%
s1 = ['a', 'b', np.nan]
pd.get_dummies(s1)

#%%
pd.get_dummies(s1, dummy_na=True)

#%%
df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'],
                   'C': [1, 2, 3]})
print(df)

pd.get_dummies(df)

#%%
df = pd.DataFrame({
    'key': list('abcdef'),
    'data': np.arange(6)
})
print(df)

dummies = pd.get_dummies(df.key, prefix='key')
print(dummies)

df_with_dummies = df[df['data']].join(dummies)
df_with_dummies

#%%
titles = ('Toy Story (1995)',
'Jumanji (1995)',
'Grumpier Old Men (1995)',
'Waiting to Exhale (1995)',
'Father of the Bride Part II (1995)',
'Heat (1995)',
'Sabrina (1995)',
'Tom and Huck (1995)',
'Sudden Death (1995)',
'GoldenEye (1995)')

genres = (
"Animation|Children's|Comedy",
"Adventure|Children's|Fantasy",
'Comedy|Romance ',
'Comedy|Drama ',
'Comedy ',
'Action|Crime|Thriller ',
'Comedy|Romance ',
"Adventure|Children's",
'Action ',
'Action|Adventure|Thriller',
)

movies = pd.DataFrame({
    'movie_id': np.arange(1, 11),
    'title': titles,
    'genres': genres
})

all_genres = []
for g in movies.genres:
    all_genres.extend(g.split('|'))
genres = pd.unique(all_genres)
print(genres)

zero_matrix = np.zeros((len(movies), len(genres)))
# print(zero_matrix)
dummies = pd.DataFrame(zero_matrix, columns=genres)
dummies

gen = movies.genres[0]
print(dummies)
print(gen)
dummies.columns.get_indexer(gen.split('|'))

for i, gen in enumerate(movies.genres):
    indices = dummies.columns.get_indexer(gen.split('|'))
    dummies.iloc[i, indices] = 1
    
print(dummies)

# movies.join(dummies.add_prefix('Genres_'))
movies.join(dummies)

#%%
import numpy as np

values = np.random.rand(10)
bins = np.arange(0, 1.1, 0.2)

print(values)
print(bins)

pd.get_dummies(pd.cut(values, bins))

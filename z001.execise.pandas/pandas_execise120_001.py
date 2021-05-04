#%%

import pandas as pd
import numpy as np

data = {"grammer":["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
       "score":[1,2,np.nan,4,5,6,7,10]}

df = pd.DataFrame(data)
df

#%% 提取包含字符串python的行

# df[df['grammer'] == 'Python'] # 错误!
df[df['grammer'].str.lower() == 'python']

#%% 
df.query('grammer.str.lower() == "python" | grammer.str.startswith("P")')
# df[df.eval("Salary_in_1000>=100 & (Age <60) & FT_Team.str.startswith('S').values")]
#%% 过滤组合条件, 使用 &, | 不能使用 and , or, 条件需要加上括号
df[(df['grammer'].str.lower() == 'python') |
   (df['grammer'].str.lower() == 'sql')]

#%%
df.loc[(df['grammer'].str.lower() == 'python') |
   (df['grammer'].str.lower() == 'sql')]

#%%
idx = np.where((df['grammer'].str.lower() == 'python') |
   (df['grammer'].str.lower() == 'sql'))
df.loc[idx[0]]


# %%
df.columns

#%%
df.rename(columns={"score": "popularity"}, inplace=True)
df

#%%
df.rename({"popularity": "pop"}, axis='columns', inplace=True)
df

#%%
df.groupby(by='grammer').count()

#%%
df['grammer'].value_counts()

#%%
df['score'].interpolate()

#%%
df[df['score'] > 3]

#%%
df['grammer'].unique()

df.drop_duplicates('grammer')

#%%
df['score'].mean()

#%%
list(df['grammer']), df['grammer'].to_list(), tuple(df['grammer'])

#%%
df['grammer'].to_excel("foo.xlsx")

#%%
df.shape

#%%
df[(df['score'] > 3) & (df['score'] < 7)]
df.query("score > 3 & score < 7")

#%%
df['score'].max()

df[df['score'] == df['score'].max()]

#%%
df.head(), df.tail()

#%%
df.drop(index=len(df)-1, inplace=True)

#%%
df.iloc[-1] = ['Perl', 6.6]

#%%
df.append({'grammer': "perl", "score": 6.3}, ignore_index=True)

#%%
df.sort_values('score')

#%%

# df['grammer'].dropna().map(lambda x: len(x))
df['grammer'].map(lambda x: len(x), na_action='ignore')
#%%
# df.drop(index=-1, inplace=True)

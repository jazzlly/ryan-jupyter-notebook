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
# 默认使用同名的列作为join的key
# df1.merge(df2) 

#%%
df1 = pd. DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 
                     'data1': range(7)}) 
df2 = pd. DataFrame({'rkey': ['a', 'a', 'b', 'd', 'b'], 
                     'data2': range(5)})

print(df1)
print(df2)
# inner join: 对两张表都有的key进行联结
df1.merge(df2, left_on='lkey', right_on='rkey')
# df1.merge(df2, left_on='lkey', right_on='rkey', how='inner')

#%%
print(df1)
print(df2)
# left join: 对所有左表的键进行联结
df1.merge(df2, left_on='lkey', right_on='rkey', how='left')

#%%
print(df1)
print(df2)
# right join: 对所有右表的键进行联结
df1.merge(df2, left_on='lkey', right_on='rkey', how='right')

#%%
print(df1)
print(df2)
# outer join: 对所有左表和右表的键进行联结
df1.merge(df2, left_on='lkey', right_on='rkey', how='outer')

# df1.merge(df2, left_on='lkey', right_on='rkey')
#%% 使用多个key进行联结

left=pd.DataFrame({'key1':['foo','foo','bar'],
    'key2':['one','two','one'],
    'lval':[1,2,3]})

right=pd.DataFrame({'key1':['foo','foo','bar','bar'],
    'key2':['one','one','one','two'],
    'rval':[4,5,6,7]})

print(left)
print(right)

left.merge(right, on=['key1', 'key2'], how='outer')

#%%
print(left)
print(right)
print(pd.merge(left, right, on='key1'))

# 指定重名列的后缀
print(pd.merge(left, right, on='key1', suffixes=('_left', '_right')))

#%% cross join
df1 = pd.DataFrame({'left': ['foo', 'bar']})
df2 = pd.DataFrame({'right': [7, 8]})

print(df1)
print(df2)
df1.merge(df2, how='cross')

#%% 指定合并的key为索引
left1=pd.DataFrame({'key':['a','b','a','a','b','c'],
    'value':range(6)})
right1=pd.DataFrame({'group_val':[3.5,7]},index=['a','b'])

print(left1)
print(right1)
pd.merge(left1, right1, left_on='key', right_index=True)

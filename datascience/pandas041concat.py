#%% 沿着轴进行矩阵连接
 
 
#%% ndarray进行联结

import pandas as pd
import numpy as np

arr = np.arange(12).reshape((3,4))

print(arr)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
print(np.concatenate([arr, arr], axis=0)) # 沿着行轴连接
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''

# 沿着列轴进行联结
print(np.concatenate([arr, arr], axis=1)) 
'''
[[ 0  1  2  3  0  1  2  3]
 [ 4  5  6  7  4  5  6  7]
 [ 8  9 10 11  8  9 10 11]]
'''

#%% series进行联结, 一个series可以看成是一个列向量
s1 = pd.Series([0, 1, 2], index=list('abc'))
s2 = pd.Series([2, 3, 4], index=list('cde'))
s3 = pd.Series([4, 5, 6], index=list('efg'))

# 三个列向量合并成一列
s4 = pd.concat([s1, s2, s3])
'''
a    0
b    1
c    2
c    2
d    3
e    4
e    4
f    5
g    6
'''

#%% 三个列向量合并成三列
df = pd.concat([s1, s2, s3], axis=1)
'''

      0	  1	 2
a	0.0	NaN	NaN
b	1.0	NaN	NaN
c	2.0	2.0	NaN
d	NaN	3.0	NaN
e	NaN	4.0	4.0
f	NaN	NaN	5.0
g	NaN	NaN	6.0
'''

#%% with inner join, 找两个series中index相同的行
s3 = pd.concat([s1, s2], axis=1, join='inner')
'''
       0	1
c	2	2
'''

#%%
pd.concat([s2, s3], axis=1, join='inner')
'''
	0	1
e	4	4
'''

#%% 为列向量创建多级索引
ret = pd.concat([s1, s2, s3], keys=['one', 'two', 'three'])

'''
one    a    0
       b    1
       c    2
two    c    2
       d    3
       e    4
three  e    4
       f    5
       g    6
'''

ret.unstack()
''' 
unstack 将列向量旋转成行向量
	a	b	c	d	e	f	g
one	0.0	1.0	2.0	NaN	NaN	NaN	NaN
two	NaN	NaN	2.0	3.0	4.0	NaN	NaN
three	NaN	NaN	NaN	NaN	4.0	5.0	6.0
'''

#%% 列向量时， keys成为了dataframe的列头
ret = pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three'])

'''
       one	two	three
a	0.0	NaN	NaN
b	1.0	NaN	NaN
c	2.0	2.0	NaN
d	NaN	3.0	NaN
e	NaN	4.0	4.0
f	NaN	NaN	5.0
g	NaN	NaN	6.0
'''
#%%
df1=pd.DataFrame(np.arange(6).reshape(3,2),
       index=['a','b','c'],columns=['one','two'])

df2=pd.DataFrame(5+np.arange(4).reshape(2,2),
       index=['a','c'],columns=['three','four'])

print(df1)
print(df2)

df3 = pd.concat([df1,df2], axis=1)

#%% 使用keys创建多级索引
df4 = pd.concat([df1,df2], axis=1, keys=['level1', 'level2'])

'''
       level1	       level2
       one	two	three	four
a	0	1	5.0	6.0
b	2	3	NaN	NaN
c	4	5	7.0	8.0
'''

df4.level1.one.b # df4['level1']['one']['b']


#%% 类似keys命名参数
df5 = pd.concat({'level1': df1, 'level2': df2}, axis = 1)
'''
	level1	       level2
       one	two	three	four
a	0	1	5.0	6.0
b	2	3	NaN	NaN
c	4	5	7.0	8.0
'''

# %% 为多级索引命名
df5 = pd.concat({'level1': df1, 'level2': df2}, 
       names=['upper', 'lower'], axis = 1)

'''
upper	level1	       level2
lower	one	two	three	four
a	0	1	5.0	6.0
b	2	3	NaN	NaN
c	4	5	7.0	8.0
'''

# %%
df1 = pd.DataFrame(np.arange(12).reshape(3,4), 
       columns = list('abcd'))
'''
	a	b	c	d
0	0	1	2	3
1	4	5	6	7
2	8	9	10	11
'''
df2 = pd.DataFrame(np.arange(12, 18).reshape(2, 3),
       columns = list('bda'))
'''
	b	d	a
0	12	13	14
1	15	16	17
'''
df3 = pd.concat([df1, df2])
'''
保留了df2的索引
       a	b	c	d
0	0	1	2.0	3
1	4	5	6.0	7
2	8	9	10.0	11
0	14	12	NaN	13
1	17	15	NaN	16
'''

df3 = pd.concat([df1, df2], ignore_index=True)
'''
忽略了df2的索引
       a	b	c	d
0	0	1	2.0	3
1	4	5	6.0	7
2	8	9	10.0	11
3	14	12	NaN	13
4	17	15	NaN	16
'''

# %%

df1 = pd.DataFrame([['a', 1], ['b', 2], ['c', 3]],
                   columns=['letter', 'number'])
df2 = pd.DataFrame([['c', 3], ['d', 4]],
                   columns=['letter', 'number'])

df3 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']],
                    columns=['letter', 'number', 'animal'])

df4 = pd.concat([df1, df3], join='inner')

#%%
a=pd.Series([np.nan,2.5,0.0,3.5,4.5,np.nan],
       index=['f','e','d','c','b','a'])
'''
f    NaN
e    2.5
d    0.0
c    3.5
b    4.5
a    NaN
'''
b=pd.Series([0.,np.nan,2.,np.nan,np.nan,5.],
       index=['a','b','c','d','e', 'f'])
'''
a    0.0
b    NaN
c    2.0
d    NaN
e    NaN
f    5.0
'''
c = b.combine_first(a)

#%% 补全nan的数据
c = pd.concat([a, b, 
              a.combine_first(b), 
              b.combine_first(a)], 
       axis=1, keys=['a', 'b', 'a comb b', 'b comb a'])
'''
	a	b	a comb b	b comb a
f	NaN	5.0	5.0	       5.0
e	2.5	NaN	2.5	       2.5
d	0.0	NaN	0.0	       0.0
c	3.5	2.0	3.5	       2.0
b	4.5	NaN	4.5	       4.5
a	NaN	0.0	0.0	       0.0
'''

#%% 补全dataframe
df1 = pd.DataFrame({
       'a': [1., np.nan, 5., np.nan], 
       'b': [np.nan, 2., np.nan, 6.], 
       'c': range( 2, 18, 4)})

df2 = pd. DataFrame({
       'a': [5., 4., np.nan, 3., 7.],
       'b': [np.nan, 3., 4., 6., 8.]})

'''
	       df1	           df2
       a	b	c	a	b
0	1.0	NaN	2.0	5.0	NaN
1	NaN	2.0	6.0	4.0	3.0
2	5.0	NaN	10.0	NaN	4.0
3	NaN	6.0	14.0	3.0	6.0
4	NaN	NaN	NaN	7.0	8.0
'''

df3 = df1.combine_first(df2)
'''
       a	b	c
0	1.0	NaN	2.0
1	4.0	2.0	6.0
2	5.0	4.0	10.0
3	3.0	6.0	14.0
4	7.0	8.0	NaN
'''
# %%

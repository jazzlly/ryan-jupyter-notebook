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
pd.concat([s1, s2, s3])
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
pd.concat([s1, s2, s3], axis=1)
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
pd.concat([s1, s2], axis=1, join='inner')
'''
    0	1
c	2	2
'''

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

#%%
pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three'])

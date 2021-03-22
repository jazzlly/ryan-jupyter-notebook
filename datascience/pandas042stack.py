#%%
import pandas as pd
import numpy as np

# %%
df = pd.DataFrame([[0, 1], [2, 3]],
                    index=['cat', 'dog'],
                    columns=['weight', 'height'])
print(df)
'''
     weight  height
cat       0       1
dog       2       3
'''
stack = df.stack()
print(stack)
'''
将行向量顺时针旋转成列向量
同时将column顺时针旋转到index中，使index变成多级index

cat  weight    0
     height    1
dog  weight    2
     height    3
type(stack)
pandas.core.series.Series
'''
stack.dog.height

unstack = stack.unstack()
'''
将series中mutiple index逆时针旋转成column
    weight	height
cat	    0	    1
dog	    2	    3
'''

# %%
multicol1 = pd.MultiIndex.from_tuples([('weight', 'kg'),
                                       ('weight', 'pounds')])
df = pd.DataFrame([[1, 2], [2, 4]],
                                    index=['cat', 'dog'],
                                    columns=multicol1)
'''
	weight
    kg	pounds
cat	1	2
dog	2	4
'''

stack = df.stack()
'''
将行向量旋转成列向量
同时将columns中第二级index旋转到index中，使index变成多级index
		weight
cat	    kg	1
    pounds	2
dog	    kg	2
    pounds	4
'''

'''
stack.columns
Index(['weight'], dtype='object')

stack.index
MultiIndex([('cat',     'kg'),
            ('cat', 'pounds'),
            ('dog',     'kg'),
            ('dog', 'pounds')],
           )
'''
unstack = stack.unstack()
'''
	    weight
        kg	pounds
cat	    1	2
dog	    2	4
'''

# %%
multicol2 = pd.MultiIndex.from_tuples([('weight', 'kg'),
                                       ('height', 'm')])
df = pd.DataFrame([[1.0, 2.0], [3.0, 4.0]],
                                    index=['cat', 'dog'],
                                    columns=multicol2)
'''
	weight	height
    kg	    m
cat	1.0	    2.0
dog	3.0	    4.0
'''
stack = df.stack()

'''
将行向量旋转成列向量
同时将columns中第二级index旋转到index中，使index变成多级index
		height	weight
cat	kg	NaN	    1.0
    m	2.0 	NaN
dog	kg	NaN	    3.0
    m	4.0	    NaN
'''
unstack = stack.unstack()
'''
	height	weight
    kg	m	kg	m
cat	NaN	2.0	1.0	NaN
dog	NaN	4.0	3.0	NaN
'''
# %%

# %% 旋转column中的第一级索引
stack = df.stack(0)

'''
		    kg	m
cat	height	NaN	2.0
    weight	1.0	NaN
dog	height	NaN	4.0
    weight	3.0	NaN
'''


# %%
stack = df.stack([0, 1])

'''
将column中两级索引都旋转到index中
cat  height  m     2.0
     weight  kg    1.0
dog  height  m     4.0
     weight  kg    3.0
'''


# %%
df = pd.DataFrame([[None, 1.0], [2.0, 3.0]],
                    index=['cat', 'dog'],
                    columns=multicol2)

'''
	weight	height
    kg	m
cat	NaN	1.0
dog	2.0	3.0
'''

stack = df.stack(dropna=False)
'''
		height	weight
cat	kg	NaN	    NaN
    m	1.0	    NaN
dog	kg	NaN	    2.0
    m	3.0	    NaN
'''

stack = df.stack(dropna=True)
'''
去掉全na的行
		height	weight
cat	m	1.0	    NaN
dog	kg	NaN	    2.0
    m	3.0	    NaN
'''

# %%

index = pd.MultiIndex.from_tuples([('one', 'a'), ('one', 'b'),
                                   ('two', 'a'), ('two', 'b')])
s = pd.Series(np.arange(1.0, 5.0), index=index)

'''
one  a    1.0
     b    2.0
two  a    3.0
     b    4.0
'''

unstack = s.unstack()
'''
	a	b
one	1.0	2.0
two	3.0	4.0
'''

unstack = s.unstack(level=0)
'''
逆时针旋转多级索引中第0级
	one	    two
a	1.0	    3.0
b	2.0	    4.0
'''


# %%

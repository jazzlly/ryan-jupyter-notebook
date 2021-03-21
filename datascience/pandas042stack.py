#%%
import pandas as pd
import numpy as np

# %%
df_single_level_cols = pd.DataFrame([[0, 1], [2, 3]],
                                     index=['cat', 'dog'],
                                     columns=['weight', 'height'])
print(df_single_level_cols)
'''
     weight  height
cat       0       1
dog       2       3
'''
stack = df_single_level_cols.stack()
print(stack)
'''
将行向量旋转成列向量
同时将columns旋转到index中，使index变成多级index

cat  weight    0
     height    1
dog  weight    2
     height    3
type(stack)
pandas.core.series.Series
'''
stack.dog.height



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
df.stack()

'''
将行向量旋转成列向量
同时将columns中第二级index旋转到index中，使index变成多级index
		height	weight
cat	kg	NaN	    1.0
    m	2.0 	NaN
dog	kg	NaN	    3.0
    m	4.0	    NaN
'''

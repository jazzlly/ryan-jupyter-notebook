# -*- coding: utf-8 -*-
"""
Created on Fri May  8 05:59:32 2020

@author: jiang
"""

#%% 比较大小
(1) < (2)

#%% 
(3,1) > (2, 5)

#%%
emptyTup = ()
emptyTup

#%%
tup = (1, 2, 3)
a, b, c = tup
print('a: {}, b: {}, c: {}'.format(a, b, c))

#%%
tup = (1, 2, 'hahaha')
print(tup)

#%%
# tuple是不可变得
tup += ('foo',)
print(tup)

#%%
print(tup[-1])

#%%
print(tup[1:3])

#%%
mulTup = ((1,2,3),(2,3,4))
print(mulTup)

#%%
print(list(tup))

#%%
tup = (3, 2, 3, 7, 8, 1)
print(tup.count(3))
print(tup.index(7))

#%%
print(list(reversed(tup)))

print(sorted(tup))

#%%
a = (1, 2, 3, 4, 5, 6, 7)
afilter = filter(lambda x: x <= 4, a)

#%% 
tuple(afilter)

#%%
len(tuple(afilter))
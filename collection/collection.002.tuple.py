# -*- coding: utf-8 -*-
"""
Created on Fri May  8 05:59:32 2020

@author: jiang
"""
#%% tuple是不可变的list

#%%
tup = 1, 2, 3
tup

#%%
tup = (1,2,3), (3,4,5)
tup

#%%
tup = tuple('abcd')
tup

#%%
tup = tuple('1234')
tup[0]

#%%
tuple('123') + tuple('456')

#%% tuple multiply
tuple('123') * 2

#%% unpack tuple
a, b, c = tuple('123')
print(f'a:{a}, b:{b}, c:{c}')

#%% swap variable
a, b = 1, 2
a, b = b, a

print(f'a:{a}, b:{b}')

#%% tuple unpacking

seq = [tuple('123'), tuple('456'), tuple('789')]

for a,b,c in seq:
    print(f'a:{a}, b:{b}, c:{c}')
    
#%% tuple unpacking from a function
def unpack():
    return 1, 2, 3

a, b, c = unpack()
print(f'a:{a}, b:{b}, c:{c}')

#%%
a, b, *rest = 1, 2, 3, 4

print(f'a:{a}, b:{b}, rest:{rest}')
print(type(rest))

#%% 丢弃数据, 下划线表示不想要的变量
def unpacking():
    return tuple('123456789')

a, b, *_ = unpacking()

print(f'a:{a}, b:{b}')
_

#%%



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
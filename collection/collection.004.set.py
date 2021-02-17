# -*- coding: utf-8 -*-
"""
Created on Fri May  8 05:59:32 2020

@author: jiang
"""
#%%

s1 = {1, 2.0, 'hello'}
print(s1)

s2 = set([1, 2.0, 'hello'])
print(s2)

print(s1 == s2)

#%%
print(1 in s1)
print('hello' in s1)
print('foo' in s1)

#%% 集合是可变的
s1.add('foo')
s1.add('bar')
print(s1)

s1.remove('foo')
print(s1)
#%%
s2 = {7,6,8,9,1,3,2,5}
print(sorted(s2))
print(s2)

#%% 
a = {1,2,3,4,5}
b = {3,4,5,6,7,8,9}

print(f'a | b: {a | b}')
print(f'a & b: {a & b}')
print(f'a ^ b: {a ^ b}')
print(f'a - b: {a - b}')

#%% += / -= / |= / ^=

#%% hash化, 只有变量能够被hash化，才能作为set的成员

#%% 推导式

# [expr for val in collection if condition]
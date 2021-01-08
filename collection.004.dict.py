# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%

# 比较简便
d4 = dict(name='ryan', age=42)
print(d4)

d1 = {'name': 'ryan', 'age': 42}
print(d1)

d2 = dict({'name': 'ryan', 'age': 42})
print(d2)

d3 = dict([('name', 'ryan'), ('age', 42)])
print(d3)

print(d1 == d2 == d3 == d4)

d5 = {}
print(d5)

d6 = dict()
print(d6)

print(d5 == d6)
#%%

# 访问元素
print(d1['name'])
print(d1['age'])
print(d1.get('name'))
print(d1.get('age'))
print(d1.get('foo', 'null'))

print('bar' in d1)
print('name' in d1)

d1['foo'] = 'foo ha'
d1['bar'] = 3
print(d1)

#%%

d1.pop('bar')
print(d1)

print("len of d1: {}".format(len(d1)))

d = {'b': 1, 'a': 2, 'c': 10}
d_sorted_by_key = sorted(d.items(), key=lambda x: x[0])  # 根据字典键的升序排序
d_sorted_by_value = sorted(d.items(), key=lambda x: x[1])  # 根据字典值的升序排序

print(d_sorted_by_key)
print(d_sorted_by_value)

#%%

products = {
    143121312: 100,
    432314553: 30,
    32421912367: 150
}
print('The price of product 432314553 is {}'.format(products[432314553]))


#%% dict zip

foo = dict(zip(('a', 'b'), (1, 2)))
print(foo)
# {'a': 1, 'b': 2}

#%%

# dict comprehension
users = [User(1, 'foo', 'foopwd')]
username_mapping = {u.username: u for u in users}
user_id_mapping = {u.id: u for u in users}

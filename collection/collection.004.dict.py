# -*- coding: utf-8 -*-

#%%
emptyDict = {}
emptyDict

#%%
emptyDict = dict()
emptyDict

#%%
emptyDict.
emptyDict

#%%
type(emptyDict)

#%%
d1 = {'name': 'ryan', 'age': 42}
d1

#%%
d1['name']
#%%
d4 = dict(name='ryan', age=42)
d4
# print(d4)

#%%

d2 = dict({'name': 'ryan', 'age': 42})
d2
# print(d2)

#%%
d3 = dict([('name', 'ryan'), ('age', 42)])
# print(d3)
d3

#%%
print(d1 == d2 == d3 == d4)

#%%
d5 = {}
print(d5)

d6 = dict()
print(d6)

print(d5 == d6)
#%%

# 访问元素
print(d1['name'])
print(d1['age'])

#%%
print(d1.get('name'))
print(d1.get('age'))

#%% get可以避免没有key导致的KeyError异常

print(d1.get('foobar', 'null')) # 'null'
print(d1.get('foobar')) # None
print(d1['foobar']) # KeyError

#%%
print(d1)
print('bar' in d1)
print('name' in d1)

#%%

d1['foo'] = 'foo ha'
d1['bar'] = 3
print(d1)

#%% 删除信息

d1.pop('bar')
print(d1)

#%% 删除信息
del(d1['foo'])
d1

#%%
print("len of d1: {}".format(len(d1)))

#%%

d = {'b': 1, 'a': 2, 'c': 10}
d_sorted_by_key = sorted(d.items(), key=lambda x: x[0])  
# 根据字典键的升序排序
d_sorted_by_value = sorted(d.items(), key=lambda x: x[1])  
# 根据字典值的升序排序

print(d_sorted_by_key)
print(d_sorted_by_value)

#%%
products = {
    143121312: 100,
    432314553: 30,
    32421912367: 150
}
print('The price of product 432314553 is {}'
    .format(products[432314553]))

#%% dict zip
foo = dict(zip(('a', 'b'), (1, 2)))
print(foo)
# {'a': 1, 'b': 2}

#%%

# dict comprehension
users = [User(1, 'foo', 'foopwd')]
username_mapping = {u.username: u for u in users}
user_id_mapping = {u.id: u for u in users}

#%%
a = {
    'a':1,
    'b':2,
    'c':3
}

a
#%% 遍历数组
a = dict(zip('abcde', range(5)))

for k,v in a.items():
    print(f'key: {k}, value: {v}')

#%%
a.items()

#%%
a.keys()

#%%
for k in a.keys():
    print(f'key: {k}')

#%%
for v in a.values():
    print(f'value: {v}')


#%%
words = ['apple', 'banana', 'zombie', 'tangle', 'white',
    'alpha', 'orange', 'green', 'news', 'mango',
    'product', 'geek']

by_letter = {}
for word in words:
    by_letter.setdefault(word[0], []).append(word)

by_letter

#%%
from collections import defaultdict
by_letter = defaultdict(list)

for word in words:
    by_letter[word[0]].append(word)

by_letter

#%% dict的key必须是不可变变量
adict = {
    (1,2):'a',
    (2,3):'b',
    (3,4):'c'
}

print(f'{adict[(2,3)]}')

#%% hash化, 只有变量能够被hash化，才能作为dict的key
hash('123456789')
#%% 
hash((1,2,3))

#%%
hash((1,2,3, [4,5,6])) # !TypeError

#%% 推导式
# [expr for val in collection if condition]

#%%

words = ['foo', 'bar', 'baz', 'wahahah', 'apple', 'orange']
lens = [len(word) for word in words]
lens

#%%
lens = list(map(len, words))
lens

#%%
lens = list(map(lambda x: len(x), words))
lens


#%% 嵌套推导式
all_words = [['foo', 'bar', 'baz'], 
        ['wahahah', 'apple', 'orange']]

two_es = [word for words in all_words 
    for word in words if word.count('a') >= 2]
two_es

#%%
flattext = [word for words in all_words
    for word in words]
flattext

#%%
tup = [[x for x in words] for words in all_words]
tup
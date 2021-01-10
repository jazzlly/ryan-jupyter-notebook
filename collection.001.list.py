# -*- coding: utf-8 -*-

#%%
# create a list
import random
import re

# %%
colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
print(type(colors))

#%%
print(colors[0]) # 0 based index
print(colors[-1])  # last index
print(colors[-2])

# %%
emptyList = []
print(emptyList)

# %%

myList = [1, 2, 'foo', 'bar']

#%%
myList.append('kaka')
print(myList)

#%%
myList[1] = 100
print(myList)

#%%
print(myList[-1])  # 倒数第一个

#%%
print(myList[1:3]) # [1, 3)

# %% 随机访问
ilist = [1, 2, 3, 4]

ilist[0]  # 下标默认是0
ilist[1:4]  # slice [begin_idx:end_idx)
ilist[:3]  # == [0:3)
ilist[2:]  # == [2:-1]
ilist[:]  # == [0:-1]

# %%

mulList = [[1, 2, 3], [2, 3, 4]]
print(mulList)

# %%
print(tuple(myList))

# %%

l = [3, 2, 3, 7, 8, 1, 7]
print(l.count(3))
print(l.index(7))

#%%
l.reverse()
print(l)
l.sort()
print(l)

# %%

# append: Appends object at end.
x = [1, 2, 3]
x.append([4, 5])  # gives you: [1, 2, 3, [4, 5]]
x

#%%
# extend: Extends list by appending elements from the iterable.
x = [1, 2, 3]
x.extend([4, 5])  # gives you: [1, 2, 3, 4, 5]
x

# %%
ids = [x for x in range(0, 5)]
ids
#%%
prices = [x for x in range(10, 15)]
prices

#%%
products = list(zip(ids, prices))
products
# [(0, 10), (1, 11), (2, 12), (3, 13), (4, 14)]

#%%

def find_product_by_id(products, pid):
    for id, price in products:
        if id == pid:
            return price
    return None

print('The price of id 3 is {}'
      .format(find_product_by_id(products, 3)))

#%%

# products is  a list of tuples
for _, price in products:
    print(price)

#%%
print("len of list: {}".format(len(products)))

# %%

year, area, type = [''] * 3


#%%
tp = infoList[1].split(u'\xa0/\xa0')
tp.extend(['']*3)

#%%
year, area, type = tp[:3]

# %%
il = [1, 2, 3]
sl = ['hello', 'world']

cl = il + sl    # combine two list
cl

#%%
cl = cl + ['new element']
cl

#%%
1 in il         # True

#%%
2 not in il     # False

#%%
a, b, c = il    # a=1, b=2, c=3

#%%
ml = [1] * 3      # [1, 1, 1]
ml

#%%
ml.append(2)    # append
ml

#%%
ml.insert(1, 'abc')   # insert abc before index 1
ml
#%%
ml.remove('abc')      # delete by value
ml

#%%
ml = [1, 2, 3];
del ml[1]             # delete by index
ml

#%%
ml = [1, 2, 3, 4]
ml.sort()
ml.reverse()
ml

# %% 高级用法
infos = ['''miao
miao
miao
''', 'hahah papa', 'wahahah mama']

infos = [w.replace(' ', '').replace('\n', '') for w in infos]
infos
#%%

import re
infos = ['''miao
miao
miao
''', 'hahah papa', 'wahahah mama']

infos = [re.sub('[ \n]', '', w) for w in infos]
infos

#%%
words = ['wahahah', 'foo', 'bar', '<br/>']
words2 = map(lambda x: str.replace(x, "[br]", "<br/>"), words)

#%%

# filter
ret = [s for s in stores if s.get('name') == name]

regexp = re.compile(r'\s+', re.UNICODE)
prices_norm = [regexp.sub('', p) for p in prices]

#%%
# shuffle a list
quiz = [{'id': 3, 'q': 'fjkd', 'a': 'fkejk;'},
        {'id': 2, 'q': 'terjk', 'a': 'tekj'},
        {'id': 1, 'q': 'tejks', 'a': 'fjk'}]
random.shuffle(quiz)
quiz

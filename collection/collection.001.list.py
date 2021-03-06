'''
list是不可变的列表
C: 原始创建方法，(), tuple()
R: 下标: [], 下标可以为负数; 
   切片: [start:end:step], [start:end), 
        切片访问，半开区间
    查询 e1 in list
    
U: append(单个元素), extend(集合),  insert(pos, element)
    list1 + list1

D: remove(e) 删除第一个
    pop(pos) 右边出栈

特点：
unpacking, *实参, 下划线参数

常用方法：
    拼接 t1+t2, 反序， 排序, count

特殊方法
    one element tuple, 如何unpacking one element tuple/list
'''

#%%
# create a list
import random
import re

#%%

a = list('abcd')
a

#%%
# 字符串也是序列
# zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = -3
print(zodiac[year %12])

#%%
'狗' in zodiac

#%%
'卡' not in zodiac

#%%
'猫' * 3

#%% 切片
zodiac[0:4]

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
myList.insert(0, 'haha')
myList

#%%
del(myList[-1])
myList

#%% 弹出列表最后一个元素
p = myList.pop()
print(p)
print(myList)

#%% 弹出任意位置的元素
p = myList.pop(1)
print(p)
print(myList)

#%% 根据值删除
mylist = [1,1,2,2,3,3]
mylist.remove(2)
mylist

#%% 模拟 removeAll
mylist = [1,1,2,2,3,3]
while True:
    try:
        mylist.remove(2)
    except ValueError as ve:
        print('remove done!')
        break

mylist

#%%
myList[1] = 100
print(myList)

#%%
print(myList[-1])  # 倒数第一个

#%% 切片操作
print(myList[1:3]) # [1, 3)

# %% 随机访问
ilist = [1, 2, 3, 4]

ilist[0]  # 下标默认是0
ilist[1:4]  # slice [begin_idx:end_idx)
ilist[:3]  # == [0:3)
ilist[2:]  # == [2:-1]
ilist[:]  # == [0:-1]

#%% clone a list
l2 = ilist[:]
l2.pop()

print(f'ilist: {ilist}')
print(f'l2: {l2}')

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
x.append(3.5)
x.append([4, 5])  # gives you: [1, 2, 3, [4, 5]]
x
#%%
x = [1, 2, 3]
x.remove(3) # 删除第一个值
x

#%%
# extend: Extends list by appending elements from the iterable.
x = [1, 2, 3]
# x.extend(3.5) # error!
x.extend([4, 5])  # gives you: [1, 2, 3, 4, 5]
x

# %%
ids = [x*2 for x in range(0, 5)]
ids

#%%
prices = [x for x in range(10, 15)]
prices


#%%
import json
objs = [
    {
        'foo': 'bar',
        'age': age
    }   
    for age in range(20, 30)]

objs
print(json.dumps(objs, indent=2, default=str))
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
ml = [1, 2, 3, 4, -1, -9, -8, -7]
ml.sort()
ml

#%%
ml.sort(reverse=True)
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

#%% 
type(range(10))

#%%
min(range(1, 20))

#%%
sum(range(21))


#%% 生成式

[v*v for v in range(10)]

#%%
sum(range(1_000_001))


#%% list clone

list1 = list(range(5))
list2 = list1[:]

list1.append(100)
list2.append(200)

print(f'list1: {list1}')
print(f'list2: {list2}')

#%% 推导式

# [expr for val in collection if condition]

#%%

# for i in 可迭代对象

#%%
for i in range(5):  # [0,5)
  # for i in range(15, 20): # [15, 20)
  # for i in range(30, 40, 2): # [30, 40) step 2
  # for i in range(40, 30, -2): # [40, 30) step -2
  print('hi:' + str(i))

#%% 字符串也是序列
for c in 'hello':
  print(c)

#%% 格式化
for i in range(10):
  print("%s twice %s" %(2*i, i))

#%% 迭代器

alist = [0, 1, 2]
itr = alist.__iter__()  # 获取迭代器
print(itr)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr)) # StopIteration Exception

#%%
colors = ['red', 'green', 'blue', 'yellow']
for color in colors:
  print(color)

#%% 访问下标
for i, c in enumerate(colors):
  print(i, '--->', c);

#%%
for color in reversed(colors):
  print(color)

#%%
for color in colors[::-1]:
  print(color)

#%%
for i,c in enumerate(reversed(colors)):
  print(i, c, sep='->')

#%% zip
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

n = min(len(names), len(colors))
for i in range(n):
  print(names[i], "--->", colors[i])
  
#%%
for n, c in zip(names, colors):
  print(n, '--->', c)

#%% sorted(iterable, key=None, reverse=False)
colors = [('red', 5), ('green', 1), ('blue', 10), ('yellow', 3)]

for c in sorted(colors):
  print(c)
#%%
print('---------------')
for c in sorted(colors, reverse=True):
  print(c)
#%% 
print('---------------')
for c in sorted(colors, key=lambda x:x[1]):
  print(c)

#%% 遍历dict

d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
for k, v in d.items():
  print(k, v)

#%%
for k in d.keys():
  print(k)

#%%
for v in d.values():
  print(v)



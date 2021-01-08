#%%

for i in range(5):  # [0,5)
  # for i in range(15, 20): # [15, 20)
  # for i in range(30, 40, 2): # [30, 40) step 2
  # for i in range(40, 30, -2): # [30, 40) step 2
  print('hi:' + str(i))

#%% 模拟for循环

alist = [0, 1, 2]
itr = alist.__iter__() 
print(itr)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr)) # StopIteration Exception

#%%
colors = ['red', 'green', 'blue', 'yellow']
for color in colors:
  print(color)

# 访问下标
for i, c in enumerate(colors):
  print(i, '--->', c);

for color in reversed(colors):
  print(color)

#%% zip
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

n = min(len(names), len(colors))
for i in range(n):
  print(names[i], "--->", colors[i])

for n, c in zip(names, colors):
  print(n, '--->', c)



#%% sorted(iterable, key=None, reverse=False)
colors = [('red', 5), ('green', 1), ('blue', 10), ('yellow', 3)]

for c in sorted(colors):
  print(c)

print('---------------')
for c in sorted(colors, reverse=True):
  print(c)

print('---------------')
for c in sorted(colors, key=lambda x:x[1]):
  print(c)

#%% 遍历列表

d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
for k, v in d.items():
  print(k, v)

print('---------------')

for k in d.keys():
  print(k)

print('---------------')

for v in d.values():
  print(v)

#%%


# while count > 0:
while True:
  name = input('please input a string:')
  if name == 'stop':
    break
  elif name == 'continue':
    continue
  elif name == 'exit':
    sys.exit()

  print('hello: ' + name)

#%%


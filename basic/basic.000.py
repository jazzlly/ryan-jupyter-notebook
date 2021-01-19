# %% basic typye
type(123)

#%%
type(123.)

#%%
type(float(123))

#%%
type(True)

#%%
type(int('123'))

#%%
type(str(123))

#%%
type(bool('123'))

#%%
bool(123)

#%%
bool(0)

#%% 
bool(0.)

#%% 
bool('')

#%%
bool(None)

#%% 通过下划线分隔数字
14_000_000

#%%
14_00.00_03

#%%
a,b,c = 1, 2, 3
print(f'a:{a}, b:{b}, c:{c}')

x,y,z = (1,2,3)
print(f'x:{x}, y:{y}, z:{z}')

#%% 常量
MAX_CONNECTIONS=123

#%%
aComplex = 1.5 + 3.2j
print(type(aComplex))
print(aComplex.real)
print(aComplex.imag)

aBoolean = 3 > 4
print(type(aBoolean))

#%% 动态数据类型
v = 10
print(hex(id(v))) # 查看对象的地址

v += 1
print(hex(id(v))) # 地址没有变化

v = 3.5
print(hex(id(v))) # 地址发生变化

# %% basic type conversion
aFloat = 3 / 2
print(aFloat)
print(type(aFloat)) # python3自动将除法转化为float

aInt = 3 // 2  # 整除
print(aInt)
print(type(aInt))

# %%

# if
a if foo else b  # 三元运算符
# for i in range(0, 250, 25) if not isDebug else range(1):

if my_name == 'ryan':
  print('good for you: ' + my_name)
elif my_name == 'jerry':
  print('nice to meet you: ' + my_name)
else:
  print('hello my der: ' + my_name)

a == True and b == False or not C == True
0 == False

# +=, -=, *=, /=, %=

#%%
# None like void, null, nil, ...
# 函数如果没有返回语句，默认返回None
no = print('test')
if no == None:
  print('good')

#%% 
a=10
if a > 10:
  print("a > 10")
elif a == 10:
  print("a == 10")
else:
  print('a<10')

# %%
for i in range(0, 10, 2): # [0, 10), step 2
  print(i)

# %%

# 多行可以使用 \
import math
import os
import sys
import random
from requests import Session
import keyword


#%%
ml = []
help(ml.sort())
help(requests.sessions())

keyword.kwlist
# https: // docs.python.org/3/tutorial/index.html

# %%
help()


# %%

b = 'hello'
type(b) # str

#%%

c = b + b # hellohello
print(c)

#%%
d = 2*b # hellohello
print(d)

# %%

while True:
  name = input('please input a string:')
  if name == 'stop':
    break
  elif name == 'continue':
    continue
  elif name == 'exit':
    sys.exit()

  print('hello: ' + name)
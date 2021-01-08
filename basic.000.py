# %% basic typye
aInt = 1 + 1
print(type(aInt))

aFloat = 1.
print(type(aFloat))

aFloat = float(1)
print(type(aFloat))

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

# %% basic op
7 * 3.
2**5
print(8%3)


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

# None like void, null, nil, ...
# 函数如果没有返回语句，默认返回None
no = print('test')
if no == None:
  print('good')



for i in range(5):
  print(random.randint(1, 10))



# %%

# 多行可以使用 \
import math
import os
import sys
import random
from requests import Session
import keyword


# %%
help    # help
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

c = b + b # hellohello
print(c)

d = 2*b # hellohello
print(d)

#%%

'''
* 表达式
1. 列表展开
  f, t = [1, 2]
  f, *t = [1, 2, 3]
  f, *m, l = [1, 2, 3] 
  *h, t = [1, 2, 3]
2. 迭代展开
  for f, *args in [[1,2,3], [3,4]]:
3. 函数调用参数, 将列表拆分成参数
    foo(*[1,2])

4. 函数定义参数, 将调用的多个参数转化为tuple
    def foo(*args):

5. 不能单独写
*args = [1,2,3,4]

'''

#%%
f, *m, l = [1]       # 0-n个元素
# ValueError: not enough values to unpack
#    (expected at least 2, got 0)

#%% 
*h, tail = [1, 2, 3, 4, 5,6,7]
tail
h

#%%
for k, *vs in [[1,2,3], [3,4]]:
    print(f'k: {k}, vs: {vs}')

#%%
def foo(x, y):
    print(f'x: {x}, y: {y}')

# 下面两种调用等效
foo(1, 2)
foo(*[1,2])

# foo([1,2]) # Error!
#%%
def foo(*args):
    print(args)

# 下面两种调用等效
foo(1,2,3)
foo(*[1,2,3])

#%%
# *args = [1,2,3,4]
#%%

records = (
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
)

def foo(x, y):
    print(f'foo: {x}, {y}')

def bar(s):
    print(f'bar: {s}')

for f, *args in records:
    print(type(args)) # list
    print(*args)      # 将list拆分成独立的参数
    # print(type(*args)) # exception
    if f == 'foo':
        foo(*args)
    if f == 'bar':
        bar(*args)

#%%
l = [1, 2, 3]
print(*l)
print(1,2,3)

#%% positional arguments

def foo(*args):
    print(args)
    print(type(args)) # tuple

foo(1, 2, 3)

#%% 
def foo(size, *args):
    print(f'size:{size}, *args: {args})')

foo(25, 'a1', 'a2')
foo(32)
#%%
def foo(*args, size=None):
    print(f'args: {args}')
    print(f'size: {size}')

foo(1, 2, 3)
#%%
foo('s1', 's2', size=123)

#%% SyntaxError: positional argument follows keyword argument
# foo(size=234, 'a1', 'a2')
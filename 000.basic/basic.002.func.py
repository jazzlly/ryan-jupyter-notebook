
#%% hello function
def afunc():
    print('hello func!')
    # 不写return默认返回None
  
ret = afunc()
if ret == None:
    print('ret is None')

if ret == None:
    print('ret is not None');

def hah(args):
    print('hello')
    
#%% 函数参数
def hello(name):
    print('hello: ' + name)
    return 123

ret = hello('foo')
if ret == 123:
    print('ret is 123')

#%% 传值
def bar(name):
    name = 'haha'
    print(name)

s='foo'
bar(s)

print(f's:{s}')

#%% 传递引用
def foo(names):
    names.append('haha')

l=list('abcd')
foo(l)

l

#%% 关键字参数
print('123', '345', sep=',')
print('foo', 'bar', sep='...')

#%% 函数内部定义局部变量
eggs = 123

def func():
    global eggs
    eggs = 456

func()
print(eggs)

#%% 参数默认值
def foo(arg1='arg1', arg2='arg2'):
    print(f'arg1:{arg1}, arg2:{arg2}')

foo(1, 2)
foo(arg2='s2', arg1='s1')
foo()

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

#%% 任意关键字参数

def foo(**kwargs):
    print(f'type: {type(kwargs)}')
    kwargs['name'] = 'haha'
    return kwargs

a = foo(location='foo')
a

#%%

def foo(first, second, **user):
    user['first'] = first
    user['second'] = second
    return user

ryan = foo('ryan', 'jiang')
ryan

#%%
ryan = foo('ryan', 'jiang', location='beijing')
ryan

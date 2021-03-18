#%% 闭包, closure: 定义在函数内部的子函数
# 子函数能够读取外部函数的局部变量

#%% nonlocal 闭包中访问外部函数的局部变量

def foo():
    a = 2020
    def bar():
        nonlocal a
        a = a + 1
        print(a)
    return bar

f = foo()
f()
f()
f()
#%%
def mul(a, b):
    return a*b

#%%
def mulx(a):
    def mul(b):
        return a*b
    return mul

mul2 = mulx(2)
print(mul2(8))

mul5 = mulx(5)
print(mul5(8))
#%%

def outer(**kwargs):
    def inner():
        print(kwargs['foo'])
    return inner

inner = outer(foo='bar')
inner()

#%%
def afunc(a, b, c):
    print('a:%s, b%s, c%s' % (a,b,c))
    print(f'a:{a}, b:{b}, c:{c}')

afunc(1,2,3)
afunc(4, c=6, b=5)

#%%
def func1(a):
    a = 20
    print(a)
    
b='foo'
func1(b) # 函数传递的是值, 如何传递引用？
b

#%% 默认参数
def func2(a, b=20):
    print('a:%s, b:%s' % (a,b))

func2(10)
func2(30, 20)
func2(b=10, a=30)

#%% 可变长参数
def afunc(a, *others):
    print(type(others))
    print(others)

afunc(1,2,3)

#%% 迭代器

alist = [1, 2, 3]
it = iter(alist)
print(next(it))
print(next(it))
print(next(it))
print(next(it)) # StopIteration

#%% 生成器

def frange(start, end, step):
    while start < end:
        yield start
        start += step

alist = [1, 2, 3]
itr = iter(frange(10, 20, 0.5))
print(next(itr))
print(next(itr))
print(next(itr))

#%% 生成器
for i in frange(10,20,0.5):
    print(i)

#%% lambda

def true():
    return True

f = lambda : True
f()

#%%
f = lambda a, b : a+b
f(1, 3)

#%% filter
alist = [1,2,3,4,5,6,7]
for i in filter(lambda x: x%2 == 0, alist):
    print(i)

#%% filter
tuple(filter(lambda x: x%2 == 0, alist))

#%% map

alist = [1,2,3,4,5,6,7]
print(list(map(lambda x: x*2 , alist)))

#%% map
alist = [1,2,3]
blist = [1,2,3]

print(list(map(lambda x, y: x + y, alist, blist)))

#%% reduce
from functools import reduce

alist = [1,2,3,4,5,6,7]
print(reduce(lambda x, y: x + y, alist, 10))

#%% zip
dict(zip([1,2,3], [4,5,6]))

#%% zip
for x,y in zip((1,2,3),(4,5,6)):
    print("x:%s, y:%s" % (x, y))

#%% zip
d = {"a":"x", "b":"y", "c":"z"}
dict(zip(d.values(), d.keys()))


#%% clousure

def sum(a):
    def add(b):
        return a + b
    return add

f2 = sum(2)
f2(8)

#%%
def sum(a):
    return lambda x: a + x;

f2 = sum(2)
f2(3)

#%% clousure
def counter(FIRST=0):
    cnt = [FIRST]
    def inc():
        cnt[0] += 1
        return cnt[0]

    return inc

add4 = counter(4)
print(add4())
print(add4())
print(add4())
#%% 
add5 = counter(5)
print(add5())
print(add5())
print(add5())

#%% 装饰器
import time

def timer(func):
    def wrapper():
        start = time.time();
        func()
        print("函数运行了%s" %(time.time() - start))
    return wrapper

@timer
def mysleep():
    time.sleep(3);

mysleep()

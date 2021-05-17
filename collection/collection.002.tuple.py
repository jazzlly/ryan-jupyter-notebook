

#%% tuple是不可变的list
tup = (1, 2, 3)
tup
#%%
tup = 1, 2, 3
tup

#%%
tup = (1,2,3), (3,4,5)
tup

#%%
tup = tuple('abcd')
tup

#%%
tup = tuple('1234')
tup[0]

#%%
print(tup[-1])
#%% 下面几个切片等效
tup[:], tup[::], tup[0:len(tup):1]

#%%
tup[-1:], tup[len(tup)-1:]

#%%
'a' in tuple('abc')

#%%
'c' not in tuple('xyz')

#%%
tuple('123') + tuple('456')

#%% tuple multiply
tuple('123') * 2

#%% unpack tuple
a, b, c = tuple('123')
print(f'a:{a}, b:{b}, c:{c}')


#%% unpack
tp = (1, 2, 3, tuple('ab'))
a, b, c, (x, y) = tp
a, b, c, x, y

#%% swap variable
a, b = 1, 2
a, b = b, a

print(f'a:{a}, b:{b}')

#%% np unpacking
r1, r2, r3 = np.random.randn(3, 10)
r1, r2, r3

#%% tuple unpacking

seq = [tuple('123'), tuple('456'), tuple('789')]

for a,b,c in seq:
    print(f'a:{a}, b:{b}, c:{c}')
    
#%% tuple unpacking from a function
def unpack():
    return 1, 2, 3

a, b, c = unpack()
print(f'a:{a}, b:{b}, c:{c}')

#%%
a, b, *rest = 1, 2, 3, 4

print(f'a:{a}, b:{b}, rest:{rest}')
print(type(rest))

#%% 丢弃数据, 下划线表示不想要的变量
def unpacking():
    return tuple('123456789')

a, b, *_ = unpacking()

print(f'a:{a}, b:{b}')
_

#%%
tup = tuple('11223344')
tup.count('4')

#%% 比较大小
(1) < (2)

#%% 
(3,1) > (2, 5)

#%%
emptyTup = ()
emptyTup

#%%
tup = (1, 2, 'hahaha')
print(tup)

#%%
# tuple是不可变得
tup += ('foo',)
print(tup)


#%%
print(list(tup))

#%%
tup = (3, 2, 3, 7, 8, 1)
print(tup.count(3))
print(tup.index(7))

#%%
print(list(reversed(tup)))

print(sorted(tup))

#%%
a = (1, 2, 3, 4, 5, 6, 7)
afilter = filter(lambda x: x <= 4, a)

#%% 
tuple(afilter)

#%%
len(tuple(afilter))

#%% one element tuple
otp = 1,
print(otp)

opt1 = (1)  # 括号表达式不能够表示 单元素tuple
            # opt1还是一个int
print(otp == opt1)

olist = [1] # 方括号能够定一个list
print(olist)

#%% unpacking
fol, =  olist

# unpacking one element tuple
print(otp[0])

first, = otp
print(first)

(f,) = otp
print(f)

[f1] = otp
print(f1)



# %% tuple unpacking from a function
def unpack():
    return 1, 2, 3

a, b, c = unpack()
a, b, c
# %% unpacking
def ret_tuple():
    return (1, 2, 3, 4)

a, b, *tp = ret_tuple()
print(tp)

# %%
a, b, *rest = 1, 2, 3, 4

print(f'a:{a}, b:{b}, rest:{rest}')
print(type(rest))

# %% 丢弃数据, 下划线表示不想要的变量
def unpacking():
    return tuple('123456789')

a, b, *_ = unpacking()
print(f'a:{a}, b:{b}')
_


# %% np unpacking
r1, r2, r3 = np.random.randn(3, 10)
r1, r2, r3

# %% unpacking in for loop
seq = [tuple('123'), tuple('456'), tuple('789')]
for a, b, c in seq:
    print(f'a:{a}, b:{b}, c:{c}')

# %%
for a, b in zip(list('abcd'), list('1234')):
    print(a, b)

#%%
d = dict(zip(list('1234'), 'abcd'))
for k in d:
    print(k, d[k])

# %% 可变长形参


def afunc(a, *others):
    print(type(others))  # 可变长形参被封装成tuple
    print(others)


afunc(1, 2, 3)
afunc(23, 'foo', 'bar')

# %% 字典参数


def afunc(a, **kwargs):
    print(a)
    print(f'type(kwargs):{type(kwargs)}')
    print(f'kwargs: {kwargs}')
    return kwargs


afunc(123, k1='foo', k2='bar')

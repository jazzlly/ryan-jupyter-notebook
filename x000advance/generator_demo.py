#%% generator遵循迭代器协议， 实现__itter__, next接口

def gen_generator():
    for i in range(10):
        print(f'generating: {i}')
        yield i

g = gen_generator()
print(type(g))

iter = g.__iter__()
print(type(iter))
print(iter)
print(next(iter))
print(next(iter))
print(next(iter))

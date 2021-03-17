#%%
def identity(f):
    print("before...")
    return f

@identity
def foo():
    return 'foo'

foo()

#%%
# 类似如下过程
def foo1():
    return 'foo1'

foo11 = identity(foo1)
foo11()

#%% 将函数存储在全局字典中
_funcs = {}

def register(f):
    global _funcs
    _funcs[f.__name__] = f
    return f

@register
def foo():
    return 'foo'

foo()
#%%

#%%
class Store(object):
    def __init__(self):
        self.storage = {}

    def get_food(self, username, food_key):
        if username != 'admin':
            raise Exception("xxx")
        return self.storage.get(food_key)
    
    def put_food(self, username, food_key, food_value):
        if username != 'admin':
            raise Exception("xxx")
        self.storage[food_key] = food_value
        
#%% 装饰器模式，在函数内部定一个函数wrapper, 并返回wrapper

def check_is_admin(f):
    def wrapper(*args, **kwargs):
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')

        if kwargs['username'] != 'admin':
            raise Exception('xxx')
        return f(*args, **kwargs)

    return wrapper

class Store(object):
    def __init__(self):
        self.storage = {}

    @check_is_admin
    def get_food(self, food_key, **kwargs):
        return self.storage.get(food_key)
    
    @check_is_admin
    def put_food(self, food_key, food_value, **kwargs):
        self.storage[food_key] = food_value

store = Store()
store.put_food('haha', 'wawa', username='admin')
print(store.get_food('haha', username='admin'))
# %%

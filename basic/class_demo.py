
#%% 定义类
class Player():
    def __init__(self, name, hp):
        self.__name = name # __name变成私有变量了

        self.hp = hp
    
    def print_role(self):
        print("name :%s, hp: %s" % (self.__name, self.hp))

    def updateName(self, newname):
        self.__name = newname

p1 = Player('foo', 23)
p2 = Player('bar', 24)
p2.updateName('wahahah')

p1.print_role()
p2.print_role()

#%% 类的继承

class Monster():
    '定义怪物类'
    def __init__(self,hp=100):
        self.hp = hp
    
    def run(self):
        print('monster run: %s' % self.hp)

    def whoami(self):
        print('我是怪物基类')

class Animal(Monster):
    '普通怪物'
    def __init__(self,hp=10):
        super().__init__(hp)

    def whoami(self):
        print('我是普通怪物')

class Boss(Monster):
    '老怪'

    def whoami(self):
        print('我是老怪')

m1 = Monster(200)
m1.run()

a1 = Animal()
a1.run()

b1 = Boss()
b1.whoami()

#%% 检查类型

type(m1)
#%%
type(a1)

#%% 判断继承关系
isinstance(a1, Monster)

#%%
isinstance(b1, Boss)

#%%
isinstance(a1, Boss)
# %% 所有的类都是object

isinstance(123, object)
#%%
isinstance('123', object)

#%%
isinstance(None, object)

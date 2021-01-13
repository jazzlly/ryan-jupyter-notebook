
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

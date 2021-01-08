
#%% hello function
def afunc():
  print('hello func!')
  # 不写return默认返回None
  
afunc()

#%% 函数参数
def hello(name):
  print('hello: ' + name)
  return 123

hello('foo')
#%% 关键字参数
print('123', '345', sep=',')

#%% 函数内部定义局部变量

eggs = 123

def func():
  global eggs
  eggs = 456


func()
print(eggs)

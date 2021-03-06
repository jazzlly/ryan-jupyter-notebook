import pyperclip

#%%
'abc%s.txt' % 123

#%%
'abc%s-%s.txt' % (123, 234)

#%% 转移字符

print("What's your name?" 'What\' your name?')

#%% 
print('normal string\n')

#%% 原始字符串取消了转移

print(r'raw string\n')
print(r'What\' your name?')

#%% 多行字符串

print(
'''abc
ed
sdwer
  fjk;''')

#%%

""" 多行注释
特特
"""
#%%
s1 = 'hello'
s2 = "hello"
s3 = """hello"""
print(s1 == s2 == s3)  # True

#%%
print('a\nb\tc')

#%%
print('len of a\\nb\\tc: {}'.format(len('a\nb\tc')))

#%% 字符串实际上也是一个序列
name = 'ryan'
print('0 of ryan is: {}'.format(name[0]))
print('1:3 of ryan is: {}'.format(name[1:3]))

#%%
for c in name:
    print(c)

#%% 字符串是不可变的

# name[2] = 'x' # 
name = 'R' + name[1:]
print("name change to: {}".format(name))
name = name.replace('a', 'A')
print("name change to: {}".format(name))

#%%
s = ''
for i in range(0, 10):
    s += str(i)

print(s)
#%%

l = []
for i in range(0, 10):
    l.append(str(i))

print(','.join(l))
print(','.join(l).split(','))

#%%

path = 'hive://ads/training_table'
namespace = path.split('//')[1].split('/')[0] 
print(namespace) 
# 返回'ads'

#%%
table = path.split('//')[1].split('/')[1]  # 返回 'training_table'
print(table)

#%%
s = '  wahahah hh aa   '
print('origin s: {}'.format(s))
print('strip s: {}'.format(s.strip()))
print('strip s: {}'.format(s.strip().strip(' aa')))

print(s.find('hh'))

#%%
print("foo :{}, bar: {}".format(1, 2))
print('foo:%s, bar%s'%(1,2))
#%%
# lstrip, rstip

print('hello' in 'hello world!')
#%%
# >> > True

','.join(['1', '2', '3'])  # '1,2,3'
#%%
','.join(['1', '2', '3']).split(',') 
# ['1', '2', '3']

#%%
' hello world '.strip()

#%%
# 访问系统剪切板
# pip3 install pyperclip
pyperclip.copy(' Hello world!')
pyperclip.paste()

# %%
print('a' * 5)

#%%
print('a' + str(10))

# %% reverse a string

reversed = 'hello world'[::-1]
print(reversed)
#%%
l = [1, 2, 3]
print(l[::-1])

# %%
my_name = input('please input your name')
print('len: ' + str(len(my_name)))

print(int('9'))
print(int(9.9))

# string is like list
'abc'[0]
'abc'[:4]
for i in 'abc':
    print(i)

# list
infos = [w.replace(' ', '').replace('\n', '') for w in infos]
infos = [re.sub('[ \n]', '', w) for w in infos]
map(lambda x: str.replace(x, "[br]", "<br/>"), words)

#%% 常用方法系列

name='ryan jiang'
print(name.title()) # Ryan Jiang

#%%
print(name.upper())

#%%
print(name.lower())

#%% f表示format, 后面可以使用变量，方法
# f是3.6引入的语法, 以前可以使用format

first='ryan'
last='jiang'
full=f'{first} {last}'
print(full)

print(f'title: {full.title()}, len: {len(full)}')

#%%
foo='   bar   '
foo
#%%
foo.lstrip()
#%%
foo.rstrip()
#%%
foo.strip()

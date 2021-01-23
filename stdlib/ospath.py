#%%
from os import path

print(path.abspath('.'))

#%%

print(path.exists('/c/Users/jiang'))

#%%
print(path.exists(r'c:\Users\jiang\git\jiangrui\python\ryan-jupyter-notebook\stdlib'))

#%%
print(path.isdir('/c/Users/jiang'))

#%%
print(path.isfile('/c/Users/jiang'))

#%%
print(path.isdir(path.join('/c/Users/jiang', 'git')))

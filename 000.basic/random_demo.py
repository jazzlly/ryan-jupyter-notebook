#%%
import random

for i in range(0, 10):
    print(random.randint(1,100))

#%%
l = ['1', '2', '3', 'red', 'green', 'blue', 'yellow']
for i in range(0, 10):
    print(random.choice(l))
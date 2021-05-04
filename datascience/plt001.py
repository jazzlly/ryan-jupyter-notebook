#%% reference: https://matplotlib.org/stable/contents.html

import matplotlib.pyplot as plt
import numpy as np
import random

#%% 基本概念
'''
图形集合(figure)， 包括多个子图(axes)
axes有title, x axis label, y axis label, legend
axis label有tick
'''

#%%
fig = plt.figure() # 空图
fig.suptitle("empty figure")

#%%
fig, axes = plt.subplots(2, 1)
fig.suptitle("3 pictures")
axes[0].set_title('axes 0')
axes[0].set_xlabel('axes 0 xlabel')
axes[0].set_xlabel('axes 0 ylabel')

#%% 基本绘图

x = np.linspace(0, 2, 100)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.title('simple plot')
plt.xlabel('x label')
plt.ylabel('y label')

plt.legend()
plt.show()

#%%
x = np.arange(0, 10, 0.2)
y = np.sin(x)
plt.plot(x, y, label='sin')

plt.title('sin')
plt.xlabel('x label')
plt.ylabel('y label')

plt.legend()
plt.show()

#%% 
x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y, label='sin')

plt.xlabel('x label')
plt.ylabel('y label')
plt.legend()
plt.show()

#%%
r1, r2 = np.random.randn(2, 100)
fig, ax = plt.subplots()
ax.plot(r1, r2, marker='v')


#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x, y1)

plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y1, 'r--', label='linear')
plt.plot(x, y2, 'm', label='quadratic')

plt.xlim(-4, 4)
plt.ylim(-5, 10)

plt.xlabel('x label')
plt.ylabel('y label')

plt.xticks(np.linspace(-4, 4, 17))

plt.legend()
plt.show()

#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y1 = 2*x + 1
y2 = x**2

plt.figure(figsize=(8, 5))
plt.plot(x, y1, 'r--', label='linear')
plt.plot(x, y2, 'm', label='quadratic')

plt.xlim(-4, 4)
plt.ylim(-5, 10)

plt.xlabel('x label')
plt.ylabel('y label')

plt.xticks(np.linspace(-4, 4, 17))

# gca: get current axies
axis = plt.gca()
axis.spines['right'].set_color('none')
axis.spines['top'].set_color('none')


# plt.legend()
plt.legend(labels=['aaa', 'bbb'], loc='lower right')
# plt.legend()
plt.show()
#%%
x = np.linspace(-3, 3, 100)
y1 = 2*x + 1
y2 = x**2

plt.figure(figsize=(8, 5))
a = plt.plot(x, y1, 'r--', label='linear')
b, = plt.plot(x, y1, 'r--', label='linear')

# %%

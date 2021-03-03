#%% reference: https://matplotlib.org/stable/contents.html

import matplotlib.pyplot as plt
import numpy as np
import random

#%% 简单画图方法
data = np.arange(10)
plt.plot(data)

#%% 创建图片figure, 然后添加子图axes

fig = plt.figure() # 生成空白图片

# 创建四个子图
ax1 = fig.add_subplot(2,2,1) # row, column, index_1based
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

# 默认绘制在最后一张图上
plt.plot(np.random.randn(100).cumsum(), 'k--') # k--绘制黑色线段

_ = ax1.hist(np.random.randn(1000), bins=20, color='k', alpha=0.3)

ax2.plot(np.random.randn(50).cumsum(), '--')

ax3.scatter(np.arange(50), 
    np.arange(50) + 3 * np.random.randn(50))

#%% 

fig = plt.figure()
ax1 = fig.add_subplot(3, 1, (1, 2))
# ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)

#%% 一次创建多个图表

fig, axes = plt.subplots(2, 2) 
axes

#%% 调整图片间距为0
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
# fig, axes = plt.subplots(2, 2)
for i in range(2):
    for j in range(2):
        axes[i][j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
plt.subplots_adjust(wspace=0, hspace=0)

#%% 图片风格
plt.plot(np.random.randn(30), 'g--')
plt.plot(np.random.randn(30) + 10, linestyle='--', color='g')

plt.plot(np.random.randn(30) + 25, 'ro--')
plt.plot(np.random.randn(30) + 35, linestyle='--', color='r', marker='o')


#%%
data = np.random.randn(50).cumsum()
plt.plot(data, 'g--', label='Default')
plt.plot(data, 'g-', drawstyle='steps-post', label='steps-post')
plt.legend(loc='best')

#%%
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot(np.random.randn(50).cumsum(), 'ko--')
ax1.set_xlabel('x label')
ax1.set_ylabel('y label')
ticks = ax1.set_xticks([0, 25, 50])  # 设置x轴刻度
labels = ax1.set_xticklabels(['one', 'two', 'three'], 
                             rotation=30, fontsize='small')
ax1.set_title('My plot')
# %% 批量设置属性
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

props = {
    "title": "My plot 1",
    "xlabel": "x label 1",
    "ylabel": "y label 1"
}

ax1.set(**props)
ax1.plot(np.random.randn(50).cumsum(), 'ko--')

#%%
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

ax1.plot(np.random.randn(50).cumsum(), 'ko--', label='one')
ax1.plot(np.random.randn(50).cumsum() + 10, 'ro--', label='two')
ax1.plot(np.random.randn(50).cumsum() + 20, 'bo--', label='three')

ax1.legend(loc='upper right')

#%%
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

rect = plt.Rectangle((0.2, 0.2), 0.1, 0.2, color='r', alpha=0.5)
ax.add_patch(rect)



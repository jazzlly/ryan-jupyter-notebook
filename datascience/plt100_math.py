#%%

import matplotlib.pyplot as plt
import numpy as np
import random

#%% 标准正态分布
_, axes = plt.subplots(2,2)

axes[0][0].hist(np.random.randn(1000), bins=30)
axes[0][1].hist(5 + np.random.randn(1000), bins=30)
axes[1][0].hist(0.1 * np.random.randn(1000), bins=30)


#%% 简单数学曲线

x = np.linspace(0, 2, 100)
plt.plot(x, x, label="linear")
plt.plot(x, x**2, label="quadratic")
plt.plot(x, x**3, label="cubic")

plt.xlabel('x label')
plt.ylabel('y label')

plt.title('simple plot')
plt.legend()
plt.show()

#%% linspace plot
import matplotlib.pyplot as plt
N = 8
y = np.zeros(N)
x1 = np.linspace(0, 10, N, endpoint=True)
x2 = np.linspace(0, 10, N, endpoint=False)
plt.plot(x1, y, 'o')
plt.plot(x2, y + 0.5, 'o')
plt.ylim([-0.5, 1])
plt.show()

#%% 简单折线图

position = 0
walks = [position]
for i in range(100):
    position += random.randint(-1, 1);
    walks.append(position)

plt.plot(walks)

#%% 
steps = np.array([random.choice([-1, 0, 2]) for _ in range(100)])
walks = steps.cumsum()

plt.plot(walks)

#%% 绘制正态分布图表
import numpy as np
import matplotlib.pyplot as plt

'''
numpy.random.normal(loc=0.0, scale=1.0, size=None)的参数中，
loc、scale分别对应公式中的期望值μ，标准差σ，
默认呈标准正态分布(μ=0,σ=1)，size指输出的值的数量font
'''

plt.hist(np.random.normal(loc=0.0, scale=1.0, size=1000), bins=30)
plt.show()

#%%


#%%
p = np.arange(-5, 5, 0.1)
xs, ys = np.meshgrid(p, p)
xs, ys

z = np.sqrt(xs ** 2 + ys ** 2)

plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()

#%% meshgrid生成两个矩阵， xs 是 参数1向量的行扩展，共有参数2行
p = np.arange(0, 5, 0.1)
xs, ys = np.meshgrid(p, p)
print(xs, '\n\n', ys)

z = np.sqrt(xs + ys)

plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()



# %% https://numpy.org/devdocs/

# https://numpy.org/devdocs/user/absolute_beginners.html

#%% 统计学基本概念
import numpy as np

nparray = np.array([1, 2, 3])

#%% 
type(nparray) #numpy.ndarray

#%% 
nparray.dtype

#%% 
np.arange(5)

#%%
arange = np.arange(15)
print(f'arrange: {arange}')

#%%
sum = np.sum(arange)
print(f'sum of array: {sum}')

#%%
avg = np.average(arange)
print(f'avg: {avg}')

#%%
median = np.median(arange)
print("median: \n{}".format(median))

variance = np.var(arange)
print("variance: \n{}".format(variance))


brange = np.random.normal(loc=0.0, scale=1.0, size=1000)
brange = np.around(brange, 2)
# print("brange: \n{}".format(brange))

avg = np.average(brange)
print("avg: \n{}".format(avg))
median = np.median(brange)
print("median: \n{}".format(median))
variance = np.var(brange)
print("variance: \n{}".format(variance))

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
import numpy as np

# 生成均价为10元，标准差为1元的股票数据
stock_data = np.random.normal(loc=10.0, scale=1.0, size=50);
stock_data = np.around(stock_data, 2);

print("stock_data: \n{}".format(stock_data))

#%%
import numpy as np

alist = np.arange(15)
print("alist: \n{}".format(alist))
# 循环右移
alist = np.roll(alist, 1)
print("alist: \n{}".format(alist))

# 循环左移
alist = np.roll(alist,-2)
print("alist: \n{}".format(alist))


#%%
import numpy as np

foo = np.arange(15)

print(type(foo))

a = np.arange(15).reshape(3, 5)
print("size of a: {}".format(a.size))
print("dim of a: {}".format(a.ndim))
print("shape of a: {}".format(a.shape))
print("type of a: {}".format(a.dtype.name))
print("itemsize of a: {}".format(a.itemsize))
print("type of a: {}".format(type(a)))

vector = np.array([1, 2, 3])
matrix = np.array([(1, 2, 3), (2, 3, 4)])
matrix1 = np.array([[1, 2, 3], [2, 3, 4]])
print("matrix : {}".format(matrix1))

matrix2 = np.array([[1, 2, 3], [2, 3, 4]], dtype=complex)
print("matrix : {}".format(matrix2))

# %%

import numpy as np

print("zeros : {}".format(np.zeros([3, 3])))
print("zeros : {}".format(
    np.zeros([3, 3], dtype=np.int64)))

print("zeros : {}".format(
    np.zeros([2, 3, 4],  # 高 长 宽
             dtype=np.int64)))

print("foo")
print(np.empty((3, 3)))  # 没有初始化

# %%
import numpy as np


print(np.arange(10, 30, 5))

print(np.arange(0, 5, 0.5))

# 0 - 10 分成21个点
print(np.linspace(0, 10, 21))

x = np.linspace(0, 2 * pi, 100)
f = np.sin(x)
# print(f)


# %%
a = np.arange(24).reshape(2, 3, 4)
print(a)

print(np.arange(10000).reshape(100, 100))

# %% concatenate


a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(np.concatenate((a, b)))

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
print(np.concatenate((x, y), axis=0))

# %% 基本算术操作

a = np.arange(5)
b = np.arange(5)

c = a + b  # 向量相加
print(c)

# %% reshape

a = np.arange(6)
b = a.reshape((2, 3))

c = b.reshape((1, 6), order='F')  # 按列reshape
d = b.reshape((1, 6), order='C')  # 按行reshape

# %% new axios

a = np.arange(6)
print(a.shape)

row_vector1 = a.reshape((1, 6))
print("row vector: {}".format(row_vector1))

row_vector = a[np.newaxis, :]  # shape: (1, 6)
print("row vector: {}".format(row_vector))  # [[0 1 2 3 4 5]]  shape: (1, 6)

row_vector2 = np.expand_dims(a, 0)  # shape: (1, 6)
print(row_vector2)

col_vector = a[:, np.newaxis]
print(col_vector)  # shape: (6, 1)
col_vector2 = np.expand_dims(a, 1)  # shape: (1, 6)
print(col_vector2)

# %% Indexing and slicing

data = np.array([1, 2, 3])

data[1]
# 2

data[0:2]
# array([1, 2])

data[1:]
# array([2, 3])

data[-2:]
# array([2, 3])

# %% filter
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a < 5)
print(a[a < 5])

five_up = (a >= 5)
print(a[five_up])
print(five_up)

print(a[(a % 2 == 0) & (a < 10)])

# %% nonzero

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = np.nonzero(a < 5)  # 获取到index
print(b)
print(a[b])

c = np.nonzero(a < 10)
print(c)
print(a[c])

coords = list(zip(c[0], c[1]))
print(coords)

coords2 = ((1, 1, 1, 1), (0, 1, 2, 3))
print(a[coords2])

# %% stack

a1 = np.array([[1, 1],
               [2, 2]])
a2 = np.array([[3, 3],
               [4, 4]])
print(np.vstack((a1, a2)))  # same as concatenate()
print(np.concatenate((a1, a2), axis=0))

print(np.hstack((a1, a2)))
print(np.concatenate((a1, a2), axis=1))

# %% split

x = np.arange(1, 25).reshape(2, 12)
print(x)

print(np.hsplit(x, 3))  # 将矩阵按列分成了三个子矩阵
print(np.hsplit(x, (1, 3, 6)))

y = np.arange(1, 25).reshape(6, 4)
print(y)
print(np.split(y, 3))  # 将矩阵按行分成三个子矩阵

# %% view

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = a[0, :]  # 第一行, 返回的是a的一个view，内存共享
print(b)
b[0] = 99
print(b)
print(a)

c = a[0, :].copy()  # 分配了新的内存
print(c)
c[1] = 99
print(c)
print(a)

# %% basic array operations

a = np.array([1, 2, 3])
b = np.ones(3, dtype=int)
print(a + b)
print(a - b)

print(a * a)
print(a / a)

print(a.sum())

c = np.array([1, 2, 3, 4]).reshape(2, 2)
print(c.sum(axis=0))  # y轴
print(c.sum(axis=1))  # x轴

# %% broadcasting

a = np.array([1, 2, 3])
print(2 * a)

# %% more operation

a = np.array([1, 2, 3])
print(a.max())
print(a.min())
print(a.mean())

a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
              [0.54627315, 0.05093587, 0.40067661, 0.55645993],
              [0.12697628, 0.82485143, 0.26590556, 0.56917101]])

print(a.min(axis=0))
print(a.min(axis=1))

# %% matrix
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(data)
print(data[0, 1])
print(data[0:2, 0:2])
print(data[0:3, 0])

data = np.array([[1, 2], [3, 4]])
ones = np.array([[1, 1], [1, 1]])
print(data + ones)


data = np.array([[1, 2], [3, 4], [5, 6]])
ones_row = np.array([[1, 1]])
print(data + ones_row)
print(1 + data)
# %% random
rng = np.random.default_rng(0)
a = rng.random(3)

print(rng.random(3))
print(rng.random((3, 2)))

# generate a 2 x 4 array of random integers between 0 and 4 with:
print(rng.integers(5, size=(2, 4)))

# %% unique
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
print(np.unique(a))

unique_values, indices_list = np.unique(a, return_index=True)
print(indices_list)

unique_values, occurrence_count = np.unique(a, return_counts=True)
print(occurrence_count)

# %% transposing matrix

a = np.arange(6).reshape(2, 3)
print(a)
print(a.T)  # 转置
print(a.transpose())
print(a)

# %% reverse
a = np.arange(6)
print(a)
print(np.flip(a))

arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(np.flip(arr_2d))  # 行和列都翻转了
print(np.flip(arr_2d, axis=0))

arr_2d[1] = np.flip(arr_2d[1])  # 翻转第二行
print(arr_2d)

arr_2d[:, 2] = np.flip(arr_2d[:, 2])  # 翻转第三列
print(arr_2d)

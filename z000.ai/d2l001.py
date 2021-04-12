#%%
import torch

x = torch.arange(12)
print(x)
print(x.shape)
print(x.numel()) # 矩阵大小m*n

#%%
X = x.reshape(3, 4)
print(X)
print(X.shape)
print(X.numel())

#%%
X = x.reshape(3, -1) # -1 == 4
X

#%%
X = torch.zeros([2, 3, 4])
X

# 2个矩阵，每个矩阵3 * 4

#%%
X = torch.zeros([2,3,4,5])
X

#%%
X = torch.ones([2, 3, 4])
X

#%% 标准高斯(正态)分布 ,均值为0, 标准差为1
X = torch.randn(3,4)
X

#%%
torch.tensor([[1,2,3], [2, 3, 4], [3, 4, 5]])

#%%
torch.arange(12).reshape(3, -1)

#%%
x = torch.arange(4)
y = torch.arange(4, 8)

print(x + y)
print(x * y)
print(x ** y)

#%%
torch.exp(x)

#%%
X = torch.arange(12).reshape(3, 4)
Y = torch.arange(100, 112).reshape(3, 4)

print(torch.cat((X, Y), dim=0))
print(torch.cat([X, Y], dim=1))

#%%
print(X == Y)
print(X > Y)
print(X < Y)

#%%
print(X.sum())

#%%
X = torch.arange(3).reshape(3, -1)
print(X)
print(X.shape)

Y = torch.arange(2).reshape(1, -1)
print(Y)
print(Y.shape)

# 不同形状矩阵相加, X复制列， Y复制行
X + Y

#%%
X = torch.arange(3).reshape([3, 1, 1])
Y = torch.arange(2).reshape([1, 1, 2])
X, Y, X + Y

#%% 索引和切片
X = torch.arange(20).reshape(4, -1)
print(X)
print(X[-1])
print(X[1:3])
X[1,3] = 1000
X[2, :] = 2000
X[:, 4] = 3000
print(X)

#%% 节省内存
X = torch.arange(12).reshape(3, -1)
Y = torch.arange(100, 112).reshape(3, -1)

before = id(Y)
Y = X + Y
print(id(Y) == before)

#%%
X = torch.arange(12).reshape(3, -1)
Y = torch.arange(100, 112).reshape(3, -1)

before = id(Y)
Y[:] = X + Y # 原地操作
Y += X       # 原地操作
print(Y)
print(id(Y) == before)

# %% from tensor to numpy array
X = torch.arange(12).reshape(3, -1)
N = X.numpy()
X, type(X), N, type(N)

#%%
import numpy as np

# from numpy array to tensor
Y = torch.tensor(np.arange(12).reshape(3, 4))
Y

#%%
a = torch.tensor([3.5])     # from tensor to scalar
a, a.item(), float(a), int(a)
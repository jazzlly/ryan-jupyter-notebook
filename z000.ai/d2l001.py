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

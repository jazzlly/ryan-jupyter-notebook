#%% scalar

import torch

a = torch.tensor(1)
a, a.shape

#%%
x = torch.tensor([3.5])
y = torch.tensor([4.7])

x + y, x - y, x * y, x / y, x ** y, x.shape

#%% vector
x = torch.tensor([0, 1, 2])
x, x[1]

#%%
print(len(x))
print(x.shape)

#%% matrix
X = torch.arange(12).reshape(3, 4)
X, X.shape, X[2, 3]

#%% transpose
X, X.T

#%% symmetric matrix
B = torch.tensor([[1,2,3], [2,0,4], [3,4,5]])
B, B.T, B == B.T

#%% tensor, 1d tensor = vector, 2d tensor = matrix, 3d tensor = image, 
X = torch.arange(24).reshape(2, 3, 4)
X

#%% sum from axis
X, X.sum(axis=0), X.sum(axis=1), X.sum(axis=2)

#%% 保持轴数不变
X, X.sum(axis=0, keepdim=True), X.sum(axis=2, keepdim=True)

#%%
A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
A

#%%
A, A.cumsum(axis=0)

# %%

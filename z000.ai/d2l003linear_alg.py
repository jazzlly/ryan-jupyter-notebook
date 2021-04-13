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

# %% dot product
x = torch.arange(4, dtype=torch.float32)
y = torch.ones(4, dtype=torch.float32)
x, y, torch.dot(x, y)

#%% alias for torch
torch.sum(x * y)

#%% matrix-vector multiplication
A = torch.arange(20).reshape(4,5)
x = torch.ones(5, dtype=torch.float32)

A, x, torch.mv(A, x)

#%% matrix-matrix multiplication
A = torch.arange(20).reshape(4, 5)
B = torch.ones(5, 3)

A, B, torch.mm(A, B)

#%% norms

u = torch.tensor([3.0, -4.0])
torch.norm(u)  # L2 norm, like distance

#%% L1 norm
torch.abs(u).sum() # sum of abs values

#%% norm of matrix
torch.norm(torch.ones(3, 4))
# sqrt(for i in range(r): for j in range(c): A[i,j] ** 2)

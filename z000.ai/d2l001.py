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

t = torch.arange(24).reshape(2, 3, 4)
t, len(t),t.sum(axis=1) # 2

#%% 
t / t.sum(axis=1, keepdims=True)

#%% 按照不同的axis求值。将如果keepdim, 对应axis变成1。
# 否则去掉该axis
t.sum(axis=0), t.sum(axis=1), t.sum(axis=2)

#%% 
from torch import linalg as LA

a = torch.arange(9, dtype=torch.float) - 4
# tensor([-4., -3., -2., -1.,  0.,  1.,  2.,  3.,  4.])
A = a.reshape((3, 3))
'''
    tensor([[-4., -3., -2.],
        [-1.,  0.,  1.],
        [ 2.,  3.,  4.]])
'''

LA.norm(A, float('inf')) # 
#%%
LA.norm(a)
# tensor(7.7460)
LA.norm(A)
# tensor(7.7460)
LA.norm(a, float('inf')) # max(abs(x))
# tensor(4.)
LA.norm(A, float('inf')) # max(sum(abs(x), dim=1))
# tensor(9.)
LA.norm(a, -float('inf')) # min(abs(x))
# tensor(0.)
LA.norm(A, -float('inf')) # min(sum(abs(x), dim=1))
# tensor(2.)

#%%
LA.norm(a, 1)
# tensor(20.)
LA.norm(A, 1)
# tensor(7.)
LA.norm(a, -1)
# tensor(0.)
LA.norm(A, -1)
# tensor(6.)
LA.norm(a, 2)
# tensor(7.7460)
LA.norm(A, 2)
# tensor(7.3485)

#%%
# Using the :attr:`dim` argument to compute vector norms::
c = torch.tensor([[1., 2., 3.],
                  [-1, 1, 4]])
LA.norm(c, dim=0)
# tensor([1.4142, 2.2361, 5.0000])
LA.norm(c, dim=1)
# tensor([3.7417, 4.2426])
LA.norm(c, ord=1, dim=1)
# tensor([6., 6.])

#%%
# Using the :attr:`dim` argument to compute matrix norms::

m = torch.arange(8, dtype=torch.float).reshape(2, 2, 2)
m, LA.norm(m, dim=(1,2))
# tensor([ 3.7417, 11.2250])
# LA.norm(m[0, :, :]), LA.norm(m[1, :, :])
# (tensor(3.7417), tensor(11.2250))

#%% 
import math
print(math.sqrt(1+4+9))
print(math.sqrt(16+25+36+49))


#%%



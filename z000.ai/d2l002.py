#%%
from IPython.lib.display import YouTubeVideo
import numpy as np
from d2l import torch as d2l
from IPython import display

def f(x):
    return 3*x*x - 4*x

def numerical_lim(f, x, h):
    return (f(x+h) - f(x)) / h

h = 0.1
for i in range(8):
    print(numerical_lim(f, 1, h))
    h *= 0.1

# %% 求导
import torch

x = torch.arange(4.0, requires_grad=True)
x, x.grad

#%%
y = 2 * torch.dot(x, x)
print(y)

y.backward() # 求梯度
x.grad

#%% sum的导数
x.grad.zero_()
y = x.sum()
y.backward()
x.grad


#%%
# 对非标量调用`backward`需要传入一个`gradient`参数，
# 该参数指定微分函数关于`self`的梯度。
# 在我们的例子中，我们只想求偏导数的和，
# 所以传递一个1的梯度是合适的

x.grad.zero_()
y = x * x
print(y)
# y.backward()
# y.sum().backward()
y.backward(torch.ones(len(x)))
x.grad

#%%
x.grad.zero_()
y = x * x
u = y.detach()
z = u * x
z.sum().backward()
x.grad

#%% 
x.grad.zero_()
y.sum().backward()
x.grad

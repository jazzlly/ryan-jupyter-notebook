#%%
import torch
from torch.distributions import multinomial
from d2l import torch as d2l

#%%
fair_probs = torch.ones([6]) / 6

counts = multinomial.Multinomial(10000, fair_probs).sample()
fair_probs, counts / 10000

#%%
foo = multinomial.Multinomial(10, fair_probs)
counts = foo.sample((500, ))
cumsum_counts = counts.cumsum(dim=0)

estimate = cumsum_counts / cumsum_counts.sum(dim = 1, keepdims=True)

counts, cumsum_counts, estimate

# counts = multinomial.Multinomial(10, fair_probs).sample((500, ))
# counts

# %%
counts = multinomial.Multinomial(10, fair_probs).sample((500,))
cum_counts = counts.cumsum(dim=0)

estimates = cum_counts / cum_counts.sum(dim=1, keepdims=True)
# cum_counts.shape [500, 6]
# cum_counts.sum(dim=1, keepdims=True).shape [500, 1]

d2l.set_figsize((6, 4.5))
for i in range(6):
    d2l.plt.plot(estimates[:, i].numpy(), label=("P(die=" + str(i + 1) + ")"))
d2l.plt.axhline(y=0.167, color='black', linestyle='dashed')
d2l.plt.gca().set_xlabel('Groups of experiments')
d2l.plt.gca().set_ylabel('Estimated probability')
d2l.plt.legend()


#%% 正态分布
import math
import numpy as np
from d2l import torch as d2l

def normal(x, mu, sigma):
    p = 1 / math.sqrt(2 * math.pi * sigma**2)
    return p * np.exp(-0.5 / sigma**2 * (x - mu)**2)


# 再次使用numpy进行可视化
x = np.arange(-7, 7, 0.01)

# 均值和标准差对
params = [(0, 1), (0, 2), (3, 1)]
d2l.plot(x, [normal(x, mu, sigma) for mu, sigma in params], xlabel='x',
         ylabel='p(x)', figsize=(4.5, 2.5),
         legend=[f'mean {mu}, std {sigma}' for mu, sigma in params])

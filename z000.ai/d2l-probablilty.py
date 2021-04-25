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

#%%

import matplotlib.pyplot as plt
import numpy as np

p = np.arange(-5, 5, 0.1)
xs, ys = np.meshgrid(p, p)
xs, ys

z = np.sqrt(xs ** 2 + ys ** 2)

plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()

#%%
p = np.arange(0, 5, 0.1)
xs, ys = np.meshgrid(p, p)
print(xs, '\n\n', ys)

z = np.sqrt(xs + ys)

plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()


#%% reference: https://matplotlib.org/stable/contents.html

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 2)
y = 2*x + 1

plt.figure(figsize=(8, 5))
plt.plot(x, y, 'g', label='linear')

plt.xlabel('x label')
plt.ylabel('y label')

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

x0 = 1
y0 = 2*x0 + 1
plt.scatter(x0, y0, s=50, color='b')
plt.plot([x0, x0], [0, y0], 'k--', lw=2.5)

plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data',
                xytext=(+30, -30), textcoords='offset points',
                fontsize=16, arrowprops=dict(arrowstyle='->', 
                        connectionstyle='arc3, rad=.2'))
plt.text(-3.7, 3, r'$Foo\ bar\ \sigma_i\ \alpha_t$',
        fontdict={'size': 16, 'color':'r'})        
plt.legend()
plt.show()

#%%
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 10)
y = 2*x + 1

plt.scatter(x, y, s=9, c='g', marker='x')

plt.show()

#%%
n = 1024
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
t = np.arctan2(y, x)

plt.scatter(x, y, s=75, c=t, alpha=0.5)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.xticks(())
plt.yticks(())

plt.show()

#%%
n = 10
x1 = np.arange(n)
y1 = np.abs(np.random.normal(0, 1, n) * 50)
y2 = np.abs(np.random.normal(0, 1, n) * 50)

plt.bar(x1, +y1)
plt.bar(x1, -y2)

for x, y in zip(x1, y1):
    plt.text(x + 0.1, y + 1, "%.2f" % y, ha='center', va='bottom')

for x, y in zip(x1, y2):
    plt.text(x + 0.1, -y - 1, "%.2f" % y, ha='center', va='top')

# plt.xticks(())
# plt.yticks(())
plt.show()

#%%
def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)

plt.contourf(X, Y, f(X, Y), 10, alpha=0.5, cmap=plt.cm.hot)
C = plt.contour(X, Y, f(X, Y), 10, color='black', linewidth=.5)
plt.clabel(C, inline=True, fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()

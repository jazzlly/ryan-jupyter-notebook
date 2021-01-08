

#%% 统计实验

# 抛硬币实验
'''
一次实验：抛硬币10次，统计正面次数cnt
做1000次这样的实验
观察cnt的分布
'''
import numpy as np
import matplotlib.pyplot as plt


# alist = [0] * 10
alist = []
for i in range(10000):
    a = np.around(np.random.rand(10))
    # a = np.around(np.random.rand(20))
    # a = np.around(np.random.rand(100))
    # a = np.around(np.random.rand(1000))
    # a = np.around(np.random.rand(10000))
    cnt = 0
    for v in a:
        if (v == 1.):
            cnt += 1
    alist.append(cnt)

array = np.array(alist)

print(np.var(array))
# plt.hist(array, normed=True)
plt.hist(array) # normed表示统计计数的百分比
plt.show()  
    

#%%
alist = [0] * 10
print(alist)

array = np.array([1,2,3])
print(array)




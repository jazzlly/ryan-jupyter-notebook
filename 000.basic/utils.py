#%%
import time

print('begin sleep ...')
time.sleep(1.0)
print('end sleep ...')

print(time.time()) # 单位 秒

#%%
print(time.localtime())

#%%
print(time.strftime('%Y-%m-%d %H:%M:%S'))

#%%
import datetime

print(datetime.datetime.now())

#%% 获取时间差
delta = datetime.timedelta(minutes=50)
print(datetime.datetime.now() + delta)

#%%
oneday = datetime.datetime(2021,1,1)
delta = datetime.timedelta(days=10)
print(oneday - delta)

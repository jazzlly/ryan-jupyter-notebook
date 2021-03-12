#%%
import time
import calendar


time.sleep(1)

#%%
time.sleep(1)

#%% 基本概念
# struct_time alias time tuple
# 函数返回time tuple
utc_now = time.gmtime()
print(f'utc now: {utc_now}')

localtime_now = time.localtime()
print(f'localtime now: {localtime_now}')

atime = time.strptime('2021-02-05 13:00:00', '%Y-%m-%d %H:%M:%S')
print(f'atime: {atime}')

#%% 接收time tuple的函数
print(f'asctime: {time.asctime(localtime_now)}')
print(f'mktime: {time.mktime(localtime_now)}')
print(f'strftime: {time.strftime("%Y-%m-%d %H:%M:%S", localtime_now)}')

#%% 
epoch=time.gmtime(0)
print(time.strftime("%Y-%m-%d", epoch))

#%% UTC time
print(f'utc time struct: {time.gmtime()}')
print()


#%%
t = time.time()
t
#%%

#%%
from datetime import datetime

now = datetime.now()
now

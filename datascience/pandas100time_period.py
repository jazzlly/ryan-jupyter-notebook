
#%%

import numpy as np
import pandas as pd
np.random.seed(12345)
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(10, 6))
PREVIOUS_MAX_ROWS = pd.options.display.max_rows
pd.options.display.max_rows = 20
np.set_printoptions(precision=4, suppress=True)

from datetime import datetime
from datetime import timedelta
from datetime import timezone

#%% timedelta
now = datetime.now()
delta = timedelta(days=1)

print(delta)
print(now + delta)
print(now - delta)
#%% timedelta仅仅支持day, week 及以下单位
# delta = timedelta(year=1)

#%%
# Components of another_year add up to exactly 365 days
year = timedelta(days=365)
another_year = timedelta(weeks=40, days=84, hours=23,
                         minutes=50, seconds=600)
print(year == another_year)
print(year.total_seconds())
# 31536000.0

#%%
year = timedelta(days=365)
ten_years = 10 * year

print(ten_years)
print(ten_years // 365)

nine_years = ten_years - year
print(nine_years)

three_years = nine_years // 3
print(three_years, three_years.days)

#%%
now = datetime.now()    # 返回当前时间
print(f'now: {now}')
utcnow = datetime.utcnow()  # 返回utc时间
print(f'utcnow: {utcnow}')

utcnow2 = datetime.now(tz=timezone.utc) # 带时区的时间
print(f'utcnow2: {utcnow2}')

today = datetime.today() # 等价于不带tzinfo的now
print(now == today)
# print(now.tzinfo)

#%% replace方法
now = datetime.now()
furture = now.replace(year=2025)
furture

#%% 时区变换
now = datetime.now()
print(now)  # 简单时间类型，没有时区信息
# 2021-04-08 07:40:13.520855

# 添加当地时区信息，东八区
e8z = now.astimezone() 
# 2021-04-08 07:38:45.947857+08:00
print(e8z) 

# 添加指定的时区信息
utc = now.astimezone(timezone.utc) # utc比我们早8小时
# 2021-04-07 23:38:45.947857+00:00
print(utc)

#%%
now = datetime.now()
e8z = now.replace(tzinfo=timezone(timedelta(hours=8)))
print(e8z)
# print(now)

#%%
datetime.fromisoformat('2021-04-06T08:30:11')

#%%
datetime.fromisoformat('2021-04-06T08:30:11+08:00')


#%%
from datetime import datetime

now = datetime.now()
print(now.year, now.hour, now.minute, now.second)
print(now.tzinfo)
#%%
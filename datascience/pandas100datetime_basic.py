
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
from datetime import date
from datetime import time

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%% timedelta表示时间差， 支持week, day 及以下单位
# delta = timedelta(year=1) # exception
# timedelta可用于创建时区信息

delta = timedelta(weeks=1)
print(delta)
print(datetime.now() + delta)
print(datetime.now() - delta)

#%% time delta的比较

# Components of another_year add up to exactly 365 days
year = timedelta(days=365)
another_year = timedelta(weeks=40, days=84, hours=23,
                         minutes=50, seconds=600)
print(year == another_year)
print(year.total_seconds())
# 31536000.0

#%% timedelta的算术运算
year = timedelta(days=365)
ten_years = 10 * year

print(ten_years)
print(ten_years // 365)

nine_years = ten_years - year
print(nine_years)

three_years = nine_years // 3
print(three_years, three_years.days)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# time对象。有简单类型和时区类型
t = time(23, 30, 12)

print(datetime.now().time())

#%%
t = time.fromisoformat('23:02:09+08:00')
t
print(t.isoformat())

print(t.strftime('%H:%M:%S %Z'))

print(t.utcoffset())
print(t.tzname)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# date对象。只有简单类型，没有时区信息
d = date(2025, 4, 3)
print(d)

print(f'today : {date.today()}')

#%%
date.fromisoformat('2021-04-03')

#%% 支持和timedelta的算数运算
d = date.today() + timedelta(days=3)
print(d)

#%%
d = date(2025, 4, 24)
d1 = d.replace(year=2021)
print(d1)
print(d - d1)

#%%
print(d1.timetuple())

#%%
d = date.today()
d1 = d.replace(year=1978)
d - d1 # 类型timedelta
#%%
d = date.today()
print(d.isoformat())

#%% 
d = date.fromisoformat('2021-03-03')
d

#%%
d = date.today()
print(d.strftime('%d/%m/%Y'))

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# datetime

dt = datetime(2029, 3, 4)
dt
#%%

# 简单时间类型
now = datetime.now()    # 返回当前时间
print(f'now: {now}')
utcnow = datetime.utcnow()  # 返回utc时间
print(f'utcnow: {utcnow}')
# now: 2021-04-11 15:30:28.164636
# utcnow: 2021-04-11 07:30:28.165635

# 时区时间类型 = 简单时间类型 + timezone信息
utcnow2 = datetime.now(tz=timezone.utc) # 带时区的时间
print(f'utcnow2: {utcnow2}')
# utcnow2: 2021-04-11 07:30:28.165635+00:00

e8now = datetime.now(tz=timezone(timedelta(hours=8), 'e8'))
print(f'now with e8zone {e8now}')

today = datetime.today() # 等价于不带tzinfo的now
print(f'today: {today}')
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
utc = now.replace(tzinfo=timezone(timedelta(hours=0)))
print(e8z)
print(utc)
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
dt = datetime.strptime('4/2/2024', '%d/%m/%Y')
dt
#%
dt = datetime.today()
dt.strftime('%Y-%m-%d')
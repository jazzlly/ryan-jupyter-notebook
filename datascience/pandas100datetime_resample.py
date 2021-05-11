
#%% 总结

'''
底层结构
pd.DatetimeIndex -> [pd.Timestamp, pd.Timestamp, ...]
pd.PeriodIndex -> [pd.Period, pd.Period, ...]
pd.TimedeltaIndex -> [pd.Timedelta, pd.Timedelta, ...]
                    [pd.DateOffset]

常用方法
pd.date_range(start, periods=3, freq='D') -> pd.DatetimeIndex
(business day)
pd.bdate_range(start, periods=3, freq='D') -> pd.DatetimeIndex
pd.period_range(start, periods=3, freq='M') -> pd.PeriodIndex

将字符串，epoch long等等转化为Timestamp
pd.to_datetime([date_str, date_str]) -> pd.DatetimeIndex or pd.Timestamp


pd.DateOffset()
pd.offsets.BDay() 

pd.Timestamp('xxx')
pd.day_name()

# 出习题集， 给未来的自己，考试
'''

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

#%% 常用方法 
dti = pd.date_range('2021', periods=5, freq='D') # datetimeIndex

'''
DatetimeIndex(['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04',
               '2021-01-05'],
              dtype='datetime64[ns]', freq='D')
'''

s = pd.Series(np.arange(len(dti)), index=dti)
s1 = pd.Series(dti)

#%%
pd.date_range('2021', freq='M', periods=4)
# DatetimeIndex(['2021-01-31', '2021-02-28', '2021-03-31', '2021-04-30'], dtype='datetime64[ns]', freq='M')


#%% business day
pd.bdate_range('2021', '2022')

#%% 
pi = pd.period_range('2006-03-24', periods=5, freq='M')
'''
PeriodIndex(['2006-03', '2006-04', '2006-05', '2006-06', '2006-07'], dtype='period[M]', freq='M')
'''
spi = pd.Series(np.arange(len(pi)), index=pi)

#%% timestamp vs time span

# timestamp就是时间点
pd.Timestamp(datetime(2012, 5, 1))
# Out[28]: Timestamp('2012-05-01 00:00:00')

pd.Timestamp("2012-05-01")
# Out[29]: Timestamp('2012-05-01 00:00:00')

pd.Timestamp(2012, 5, 1)
# Out[30]: Timestamp('2012-05-01 00:00:00')

# span是一段时间
pd.Period("2011-01")
# Out[31]: Period('2011-01', 'M')

pd.Period("2012-05", freq="D")
# Out[32]: Period('2012-05-01', 'D')

#%% pd.DatetimeIndex的组成元素是pd.Timestamp
dates = [
    pd.Timestamp('2021-5-1'),
    pd.Timestamp('2021-5-2'),
    pd.Timestamp('2021-5-3'),
    pd.Timestamp('2021-5-4')
]
s = pd.Series(np.random.randint(len(dates)), index=dates)

# s.index
# DatetimeIndex(['2021-05-01', '2021-05-02', '2021-05-03', 
# '2021-05-04'], dtype='datetime64[ns]', freq=None)

#%% pd.PeriodIndex的元素是pd.Period
periods = [pd.Period('2019'), pd.Period('2020'), pd.Period('2021')]
s = pd.Series(np.random.randint(len(periods)), index=periods)
# PeriodIndex(['2019', '2020', '2021'], 
# dtype='period[A-DEC]', freq='A-DEC')

#%%
periods = [pd.Period('2019'), pd.Period('2020'), pd.Period('2021')]

#%% converting to timestamp
pd.to_datetime('2021')
# Timestamp('2021-01-01 00:00:00')

#%%
pd.to_datetime(['2021'])
#%%
pd.to_datetime(['2021', '2022'])
# DatetimeIndex(['2021-01-01', '2022-01-01'], dtype='datetime64[ns]', freq=None)

#%% 
pd.to_period(['2019', '2020', '2021'])

#%% epoch timestamps
pd.to_datetime(
    [1349720105, 1349806505, 1349892905, 1349979305, 1350065705], 
    unit="s")

#%% 
stamps = pd.date_range('2020-01-01', periods=3, freq='M')
(stamps - pd.Timestamp('1970-1-1')) // pd.Timedelta('1s')



#%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# 日期索引
rng = pd.date_range('2020', '2022', freq='BM')
series = pd.Series(np.random.randn(len(rng)), index=rng)

#%%
print(series)
print(series['1/31/2020'])

print(series['2020-3']) # 通过月份直接访问
print(series['2020-3':'2020-6']) # 通过月份直接访问, 双闭区间
print(series['2020'])   # 通过年份直接访问
# print(series['2020-03-03']) error

#%%
dft = pd.DataFrame(
    np.random.randn(100000, 1),
    columns=["A"],
    index=pd.date_range("20130101", periods=100000, freq="T"))

# 对于df, 推荐使用loc访问
# dft['2013-01']     depreciate! 不确定是选择index还是column
dft.loc['2013-01']

#%% 切片的时候，是双臂区间。包括结束日期内所有时间
dft["2013-1":"2013-2-28"]
#%%
dft["2013-1":"2013-2-28 00:00:00"]


#%% 多级索引
dft2 = pd.DataFrame(
    np.random.randn(20, 1),
    columns=["A"],
    index=pd.MultiIndex.from_product(
        [pd.date_range("20130101", periods=10, freq="12H"), ["a", "b"]]
    ))

dft2.loc['20130102']

#%% slice vs match
s = pd.Series(np.random.rand(1000), 
    index=pd.date_range("20130101 10:23:34", periods=1000, freq="S"))

print(s.index.resolution)

# print(s['2013-01-01 10:23:42:123'])  # 输入精度和分辨率一样, 返回scalar
print(s['2013-01-01 10:23:42'])  # 输入精度和分辨率一样, 返回scalar
print(s['2013-01-01 10:23'])     # 输入进度大于分辨率， 返回series


dft = pd.DataFrame(np.random.randn(len(s.index)), index=s.index)
dft.loc['2013-01-01 10:23:42'] # 返回series
dft.loc['2013-01-01 10:23'] # 返回dataframe

#%% truncate: 留下[before, after)半开区间的值

rng2 = pd.date_range("2011-01-01", "2012-01-01", freq="W")
ts2 = pd.Series(np.random.randn(len(rng2)), index=rng2)
ts2.truncate(before="2011-11", after="2011-12")
# equal ts2["2011-11":"2011-11-30"], 但是需要计算11的月底
'''
2011-11-06    0.437823
2011-11-13 - 0.293083
2011-11-20 - 0.059881
2011-11-27    1.252450
Freq: W-SUN, dtype: float64
'''

ts2["2011-11":"2011-12"]
'''
2011-11-06    0.437823
2011-11-13 - 0.293083
...
2011-12-18 - 0.286539
2011-12-25    0.841669
Freq: W-SUN, dtype: float64
'''

#%%
ts = pd.Timestamp('2020-01-01')
print(ts.day_name())
print(ts + pd.DateOffset(days=1))
print(ts + pd.offsets.BDay() * 4)

#%% date offset可以将一个时间点向前或向后推进
ts = pd.Timestamp("2018-01-06 00:00:00")
print(ts.day_name())

offset = pd.offsets.BusinessHour(start='9:00')
print(offset.rollforward(ts))

#%% normalize将时间设置为0点
ts = pd.Timestamp('2020-01-01 20:00')
day = pd.offsets.Day()

print(day.apply(ts))
print(day.apply(ts).normalize())

#%%
ts = pd.Timestamp('2014-01-01 22:00')
hour = pd.offsets.Hour()

print(hour.apply(ts))
print(hour.apply(ts).normalize())

#%%
pd.offsets.MonthBegin(n=1).rollforward(pd.Timestamp('2014-01-02'))

pd.offsets.MonthBegin(n=1).rollback(pd.Timestamp('2014-01-02'))

#%%
pd.offsets.MonthEnd(n=1).rollforward(pd.Timestamp('2014-01-02'))
pd.offsets.MonthEnd(n=1).rollback(pd.Timestamp('2014-01-02'))

#%%
#%% DateOffSet, freq字符串对应的对象, 类似timedelta



#%%
df = pd.DataFrame({
    "a": np.random.randn(1000),
    "b": np.random.randn(1000)
    }, index=pd.date_range('2020-01-01', periods=1000, freq='T'))
#%%
index = pd.date_range('1/1/2000', periods=9, freq='T')
series = pd.Series(range(9), index=index)
series

'''
2000-01-01 00:00:00    0
2000-01-01 00:01:00    1
2000-01-01 00:02:00    2
2000-01-01 00:03:00    3
2000-01-01 00:04:00    4
2000-01-01 00:05:00    5
2000-01-01 00:06:00    6
2000-01-01 00:07:00    7
2000-01-01 00:08:00    8
Freq: T, dtype: int64
'''

#%%
series.resample('3T').sum()
'''
2000-01-01 00:00:00     3
2000-01-01 00:03:00    12
2000-01-01 00:06:00    21
Freq: 3T, dtype: int64
'''

#%%
series.resample('3T', label='right').sum()
'''
2000-01-01 00:03:00     3
2000-01-01 00:06:00    12
2000-01-01 00:09:00    21
Freq: 3T, dtype: int64
'''

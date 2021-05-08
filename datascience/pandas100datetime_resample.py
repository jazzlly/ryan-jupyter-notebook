
#%% 总结

'''
底层结构
pd.DatetimeIndex -> [pd.Timestamp, pd.Timestamp, ...]
pd.PeriodIndex -> [pd.Period, pd.Period, ...]

常用方法
pd.date_range(start, periods=3, freq='D') -> pd.DatetimeIndex
(business day)
pd.bdate_range(start, periods=3, freq='D') -> pd.DatetimeIndex

pd.to_datetime([date_str, date_str]) -> pd.DatetimeIndex or pd.Timestamp

pd.period_range(start, periods=3, freq='M') -> pd.PeriodIndex


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

#%%

https://zhuanlan.zhihu.com/p/100185719


#%%
# 找一下国泰多策略的历史图

#%%

import matplotlib.pyplot as plt
import numpy as np
from numpy.core.numeric import normalize_axis_tuple
import pandas as pd

plt.plot(np.arange(10))

#%%

import akshare as ak

df = ak.rate_interbank(
    market="上海银行同业拆借市场", symbol="Shibor人民币",
    indicator="隔夜", need_page="10")
print(df)
del df['涨跌(BP)']
df.date = pd.to_datetime(df.日期)
df.plot()

# df.pivot(index='date', columns='利率(%)', values='利率(%)').plot(marker='o')
# plt.plot(rate_interbank_df)

#%%
import akshare as ak
macro_china_money_supply_df = ak.macro_china_money_supply()
print(macro_china_money_supply_df)

#%%

import akshare as ak
stock_zh_index_daily_df = ak.stock_zh_index_daily(symbol="sh000001")
print(stock_zh_index_daily_df)
stock_zh_index_daily_df['close'].plot()
# pstock_zh_index_daily_df['date' > '2020-01-01'].plot()
# df.pivot(values='close').plot()

#%%
import akshare as ak

macro_china_lpr_df = ak.macro_china_lpr()
print(macro_china_lpr_df)

macro_china_gdp_yearly_df = ak.macro_china_gdp_yearly()
print(macro_china_gdp_yearly_df)
print(macro_china_gdp_yearly_df.name)

macro_china_ppi_yearly_df = ak.macro_china_ppi_yearly()
print(macro_china_ppi_yearly_df)
print(macro_china_ppi_yearly_df.name)


macro_china_m2_yearly_df = ak.macro_china_m2_yearly()
print(macro_china_m2_yearly_df)
print(macro_china_m2_yearly_df.name)


#%%
import akshare as ak

macro_china_money_supply_df = ak.macro_china_money_supply()
print(macro_china_money_supply_df)

#%%
import akshare as ak
macro_china_new_house_price_df = ak.macro_china_new_house_price()
print(macro_china_new_house_price_df)


#%%
import akshare as ak
macro_china_enterprise_boom_index_df = ak.macro_china_enterprise_boom_index()
print(macro_china_enterprise_boom_index_df)
#%%

# https://zhuanlan.zhihu.com/p/100185719


#%%
# 找一下国泰多策略的历史图

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

#%%
import numpy as np
import matplotlib.pyplot as plt

#%%
import akshare as ak
js_news_df = ak.js_news(indicator='最新资讯')
print(js_news_df)
print(type(js_news_df))

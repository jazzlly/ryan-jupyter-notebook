#%%

# https://zhuanlan.zhihu.com/p/100185719


#%%
# 找一下国泰多策略的历史图

#%%
import akshare as ak

#%%
import akshare as ak
js_news_df = ak.js_news(indicator='最新资讯')
# js_news_df = ak.js_news(indicator='最新数据')
print(js_news_df)
# js_news_df.to_excel('news.xlsx')

# print(type(js_news_df))
# js_news_df['content']
for i in range(len(js_news_df)):
    print(f"{js_news_df.iloc[i, 0]}")
    print(f"{js_news_df.iloc[i, 1]}")
    print()


#%% 银行间拆借利率

import akshare as ak
rate_interbank_df = ak.rate_interbank(market="上海银行同业拆借市场", 
    symbol="Shibor人民币", indicator="隔夜", need_page="10")
# print(rate_interbank_df)
# rate_interbank_df.del
del rate_interbank_df['涨跌(BP)']
rate_interbank_df.plot()


#%%

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

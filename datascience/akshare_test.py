#%%
# https://zhuanlan.zhihu.com/p/100185719

#%%
import akshare as ak

#%%
import akshare as ak
js_news_df = ak.js_news(indicator='最新资讯')

# js_news_df['content']
for i in range(len(js_news_df)):
    print(f"{js_news_df.iloc[i, 0]}")
    print(f"{js_news_df.iloc[i, 1]}")
    print()
    

#%% 社融数据
import akshare as ak
df = ak.macro_china_shrzgm()
print(df)

#%% 央行公开操作
# 逆回购：央行给商业银行贷款，商业银行抵押债券给央行。到期后商业银行还钱，收回债券

import akshare as ak
macro_china_gksccz_df = ak.macro_china_gksccz()
# print(macro_china_gksccz_df)

macro_china_gksccz_df.columns
df = macro_china_gksccz_df
print(df['operation_from_date'][0])
print(type(df['operation_from_date'][0]))
# df[df['operation_from_date' > '2021-01-01']]

# filter_df=macro_china_gksccz_df[macro_china_gksccz_df['operation_from_date' > '2021-01-01']]
print(df[::-1][df['operation_from_date'] > '2021-01-01'])


#%% 银行间拆借利率
import akshare as ak
rate_interbank_df = ak.rate_interbank(market="上海银行同业拆借市场", 
    symbol="Shibor人民币", indicator="隔夜", need_page="10")
# print(rate_interbank_df)
# rate_interbank_df.del
del rate_interbank_df['涨跌(BP)']
rate_interbank_df.plot()

#%% 十年期国债
# "bond_investing_global" # 全球债券行情数据

import akshare as ak
bond_investing_global_df = ak.bond_investing_global(
    country="中国", index_name="中国10年期国债",
    period="每周", start_date="2010-01-01", end_date="2021-02-05")
print(bond_investing_global_df)

#%%
import akshare as ak
bond_investing_global_df = ak.bond_investing_global(
    country="美国", index_name="美国10年期国债", period="每周", 
    start_date="2019-01-01", end_date="2021-03-04")
print(bond_investing_global_df)

#%% 市盈率
import akshare as ak
stock_a_pe_df = ak.stock_a_pe(market="000016.XSHG")
print(stock_a_pe_df)

#%%  上海证券交易所-股票数据总貌
import akshare as ak
stock_sse_summary_df = ak.stock_sse_summary()
print(stock_sse_summary_df)
#%%

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
import time
import akshare as ak

bond_investing_global_df = ak.bond_investing_global(
    country="中国", index_name="中国10年期国债", period="每日", 
    start_date="2005-01-01", end_date=time.strftime(
        '%Y-%m-%d', time.localtime()))
print(bond_investing_global_df)
#%%
import time
import akshare as ak

bond_investing_global_us_10 = ak.bond_investing_global(
    country="美国", index_name="美国10年期国债", period="每日", 
    start_date="2005-01-01", end_date=time.strftime(
        '%Y-%m-%d', time.localtime()))
print(bond_investing_global_us_10)

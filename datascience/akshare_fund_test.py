#%%
import pandas as pd
import numpy as np
import akshare as ak

'''
假设我在10月19日下午3：00前用1万元买入农银新能源主题基金，
当天单位净值是2.1048，
申购费率是0.15%；
在11月2日下午三点前赎回农银新能源主题基金，当天单位净值为2.198，
赎回费率为0.75%。

申购手续费＝10000.00×0.15％＝15 (元)
申购份额＝(10000.00－15)÷2.1048＝4743.919(份)
赎回总额＝4743.919×2.198＝10427.13(元)
赎回手续费＝10427.13×0.75%＝78.2(元)
赎回净额＝10427.13－78.2＝10348.93(元) 
净收益＝10348.93－10000.00＝348.93(元)

所以，在我投资的11天里头，我一共赚到了348.93元。

作者：小马哥的理财日记
链接：https://www.zhihu.com/question/22971046/answer/1560030633
'''

#%%

''' 获取基金累计净值走势，并补全缺失日期数据 '''
def filled_fund_data_df(fund_code):
    '''
    <class 'pandas.core.frame.DataFrame'>
RangeIndex: 3770 entries, 0 to 3769
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   净值日期    3770 non-null   object
 1   累计净值    3770 non-null   object
'''
    src_df = ak.fund_em_open_fund_info(fund_code, indicator="累计净值走势")

    df_date_index = src_df.set_index('净值日期')
    date_rng = pd.date_range(df_date_index.index[0], 
        df_date_index.index[len(df_date_index) - 1], freq="D")

    return df_date_index.reindex(date_rng, method='ffill')

df = filled_fund_data_df("163402") # 兴全趋势混合



#%%

# dates.dt.strftime('%Y-%m-%d')
# datetime_list = pd.to_datetime(fund_em_info_df['净值日期'], format='%Y-%m-%d')
# date_rng_list = date_rng.format()
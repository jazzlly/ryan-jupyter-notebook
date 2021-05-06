#%%
import pandas as pd
import numpy as np
import akshare as ak
import matplotlib.pyplot as plt

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

df_fgthczhh_003494 = filled_fund_data_df("003494") # 富国天惠
df_xqqs_163402 = filled_fund_data_df("163402") # 兴全趋势混合
#df_gfwjzz_009326 = filled_fund_data_df("009326") # 广发稳健增长
df_yfdzxp_110011 = filled_fund_data_df("110011") # 易方达中小盘
df_zosdxf_004241 = filled_fund_data_df("004241") # 中欧时代先锋
df_gtra_003516 = filled_fund_data_df("003516") # 国泰融安多策略
df_jsccxin_260108 = filled_fund_data_df("260108") # 景顺长城新兴成长

print("done!")

#%%
#%%
deltas=[]
days = 365
fund = df_zosdxf_004241
for r in range(len(fund) - days):    
    deltas.append(float(fund.iloc[r + days][0]) - 
                  float(fund.iloc[r][0]))

s = pd.Series(deltas)
# s.plot(kind='hist')
s.plot(kind='kde')
'''
bins = list(range(-500, 500, 50))

cats = pd.cut(deltas, bins, include_lowest=True)
value_counts = pd.value_counts(cats, sort=False) / (len(fund) - days) * 100

ax = value_counts.plot.bar(rot=0, color="r", figsize=(6,4))
plt.xticks(rotation='vertical')
plt.show()
'''


#%%
fig, ax = plt.subplots(4, 1)
ax[0].plot(df_fgthczhh_003494.index, df_fgthczhh_003494['累计净值'])
ax[1].plot(df_xqqs_163402.index, df_xqqs_163402['累计净值'])
ax[2].plot(df_yfdzxp_110011.index, df_yfdzxp_110011['累计净值'])
ax[3].plot(df_zosdxf_004241.index, df_zosdxf_004241['累计净值'])

#%%

# dates.dt.strftime('%Y-%m-%d')
# datetime_list = pd.to_datetime(fund_em_info_df['净值日期'], format='%Y-%m-%d')
# date_rng_list = date_rng.format()

#%%
import akshare as ak
fund_em_fund_name_df = ak.fund_em_fund_name()
print(fund_em_fund_name_df)

#%%
fund_names=[
'富国天惠成长混合C', '003494',
'中欧价值', '004232',
'兴全趋势', '163402',
'中欧新蓝筹','004237',
'中欧时代先锋股票C', '004241',
'华安升级', '040020',
'汇添富成长', '011402',
'兴全合润', '163406',
'民生加银', '000136',
'景顺长城动力', '260103',
'易方达消费', '009265',
'银华内需', '161810',
'永赢惠添利', '005711',
'广发双擎升级', '009314',
'易方达中小盘', '110011',
'广发稳健增长', '009326',
'华夏回报 ',
'新锐公募基金经理',
'平安智慧中国',
'中欧医疗创新',
'银华富裕主题',
'交银新生活力',
'富国科创主题3年',
'汇添富医药保健',
'工银科技创新3年',
'汇添富消费升级',
'嘉实新兴产业']

fund_em_fund_name_df['基金简称']

print(fund_em_fund_name_df[fund_em_fund_name_df['基金简称'] == '华夏成长混合'])

for i in range(len(fund_em_fund_name_df)):
    fname = fund_em_fund_name_df['基金简称'][i]
    for name in fund_names:
        if (fname.find(name)):
            fund_em_fund_name_df.iloc[i]
    
#%%

for name in fund_names:
    print(name)
    print(fund_em_fund_name_df[name in fund_em_fund_name_df['基金简称']])

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

# 兴全趋势混合
fund_em_info_df = ak.fund_em_open_fund_info(fund="163402", 
                                            indicator="累计净值走势")
print(fund_em_info_df)


'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3770 entries, 0 to 3769
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   净值日期    3770 non-null   object
 1   累计净值    3770 non-null   object
'''


'''
将净值日期变成dateRange index?
            净值日期     累计净值
0     2005-11-03      1.0
1     2005-11-11   0.9999
2     2005-11-16   0.9999
3     2005-11-17   0.9999
4     2005-11-18   1.0007
...          ...      ...
3765  2021-04-23  11.2653
3766  2021-04-26  11.2729
3767  2021-04-27  11.2753
3768  2021-04-28  11.2821
3769  2021-04-29  11.3017

[3770 rows x 2 columns]
'''
#%%

import tushare as ts

ts.set_token('fd5d4daed542a00d15539135109a690e5da331f2fc7eaa653d0d6f20')

pro = ts.pro_api()
# print(ts.get_industry_classified())
cpi = ts.get_cpi()
print(cpi.head())
# ts.get_deposit_rate()

# ts.get_gdp_contrib()
# ts.get_gdp_year()
# df = pro.get_gdp_year();

#获取PCB月度营收
# df = pro.tmt_twincome(item='8')

#获取PCB月度营收（20120101-20181010）
# df = pro.tmt_twincome(item='8', start_date='20120101', end_date='20181010')

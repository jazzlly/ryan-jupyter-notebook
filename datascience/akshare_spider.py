


#%%
from selenium import webdriver
from bs4 import BeautifulSoup
from bs4 import NavigableString

from datetime import datetime
from datetime import date
from time import sleep

import pandas as pd

def us_10_bond():
    browser = webdriver.Chrome()
    browser.get('https://cn.investing.com/rates-bonds/u.s.-10-year-bond-yield-historical-data')
    browser.maximize_window()
    sleep(5)
    # browser.execute_script('window.scrollBy(0,200)')
    print("browser open!")

    soup = BeautifulSoup(browser.page_source, 'lxml')
    result_df = pd.DataFrame()

    for e in soup.find(id='results_box').table.tbody.children:
        if isinstance(e, NavigableString):
            continue
        
        for i, ec in enumerate(e.children):
            if isinstance(ec, NavigableString):
                continue
            print(i, ec)
            # 日期
            if i == 1:
                dates = ec.text.replace('年', '-').replace('月', '-').replace('日', "-").split('-')
                d = date(int(dates[0]), int(dates[1]), int(dates[2]))
                # print(d.strftime('%Y-%m-%d'))
                ds = d.strftime('%Y-%m-%d')
            # 收盘
            if i == 3:
                print(f'close: {ec.text}')
                close = ec.text
            # 趋势
            if i == 11:
                print(f"trend: {ec.text.replace('%', '')}")
                trend = ec.text.replace('%', '')
                
        df = pd.DataFrame({'date': [ds], '收盘': [close], '涨跌幅': [trend]})
        result_df = result_df.append(df, ignore_index=True)
    return result_df


df = us_10_bond()
df
    # print(result_df)
    # print(result_df.info())
    # result_df[result_df['date'] > '2021-04-01']
            
#%%
from datetime import datetime
d = datetime('2021-4-9')
print(d)

#%%
#%%
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
req = requests.get(
    'https://cn.investing.com/rates-bonds/u.s.-10-year-bond-yield-historical-data',
    headers=headers)

#  user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36
print(type(req))
print(req.status_code)
print(req.text)

html = req.text

#%%
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

data = {
    'curr_id': (None, '23705'),
    'smlID': (None, '200646'),
    'header': (None, '美国十年期国债收益率历史数据'),
    'st_date': (None, '2021/03/10'),
    'end_date': (None, '2021/04/09'),
    'interval_sec': (None, 'Daily'),
    'sort_col': (None, 'date'),
    'sort_ord': (None, 'DESC'),
    'action': (None, 'historical_data')
}

# data = {
#     'header': (None, '美国十年期国债收益率历史数据'),
#     'st_date': (None, '2021/03/10'),
#     'end_date': (None, '2021/04/09'),
#     'interval_sec': (None, 'Daily'),
#     'sort_col': (None, 'date'),
#     'sort_ord': (None, 'DESC'),
#     'action': (None, 'historical_data')
# }

req = requests.post(
    'https://cn.investing.com/instruments/HistoricalDataAjax',
    headers=headers, files=data)

html = req.text
print(req.text)
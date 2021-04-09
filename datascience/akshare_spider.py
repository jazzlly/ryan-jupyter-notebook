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


#%%

from selenium import webdriver

from time import sleep
import re

browser = webdriver.Chrome()
browser.get('https://cn.investing.com/rates-bonds/u.s.-10-year-bond-yield-historical-data')
browser.maximize_window()
sleep(5)

#%%
from selenium import webdriver
browser = webdriver.Chrome()

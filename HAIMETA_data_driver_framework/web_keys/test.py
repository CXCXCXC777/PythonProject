from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common import options
from web_keys import WebKeys,open_browser

wk=WebKeys('chrome')
wk.open('https://www.baidu.com')
print('test')
wk.quit()
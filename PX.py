import json
import unittest
import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setting():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_experimental_option('detach', True)
    options.add_argument('--user-data-dir=D:\\ChromeUserData')  # 使用双反斜杠

    options.add_argument(r"--profile-directory=Default")
    a1 = webdriver.Chrome(service=Service('chromedriver.exe'), options=options)
    return a1



a1 = setting()
a1.get('https://preview.haimeta.com/')




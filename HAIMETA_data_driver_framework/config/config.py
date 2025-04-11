from selenium import webdriver
from selenium.webdriver.common import options, service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def options():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        # 修改用户数据目录的路径格式
        chrome_options.add_argument('--user-data-dir=D:\\ChromeUserData')  # 使用双反斜杠
        # 添加一些常用的选项来提高稳定性
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--ignore-certificate-errors')
        # 禁用日志和自动化提示
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        return chrome_options

def service():
        service = Service(r'D:\PycharmProjects\PythonProject\HAIMETA_data_driver_framework\config\chromedriver.exe')
        return service

def driver():
        service = Service(r'D:\PycharmProjects\PythonProject\HAIMETA_data_driver_framework\config\chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=options())
        return driver

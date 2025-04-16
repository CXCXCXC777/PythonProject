from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common import options

from HAIMETA_data_driver_framework.config.element_config import ElementLocators
from web_keys import WebKeys,open_browser

wk=WebKeys('chrome')
wk.open('https://test.haimeta.com/login')
wk.input_visible('xpath',ElementLocators.EMAIL_INPUT_XPATH,ElementLocators.VALID_EMAIL_ACCOUNT)
wk.click_visible('xpath',ElementLocators.CONTINUE_BUTTON_XPATH)
wk.input_presence_10_times_while_clicking('xpath',ElementLocators.PASSWORD_INPUT_XPATH,ElementLocators.WRONG_PASSWORD,'xpath',ElementLocators.LOGIN_BUTTON_XPATH)
print(wk.get_text('xpath',ElementLocators.ERROR_MESSAGE_AFTER_INPUT_WRONG_PASSWORD))
wk.wait_sleep()

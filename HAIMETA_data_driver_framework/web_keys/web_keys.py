import time
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from HAIMETA_data_driver_framework.config.config import options as chrome_options
from selenium.webdriver.common.by import By

from HAIMETA_data_driver_framework.config.get_logger import get_logger

log=get_logger()

def open_browser(type_):
    # 基于反射实现浏览器生成
    log.info(f"正在打开浏览器: {type_}")
    try:
        if type_ == "chrome":
            chrom_service = Service(r'D:\PycharmProjects\PythonProject\HAIMETA_data_driver_framework\config\chromedriver.exe')
            driver = webdriver.Chrome(service=chrom_service, options=chrome_options())
            log.info("Chrome浏览器已成功启动")
        else:
            log.info(f"尝试启动{type_}浏览器")
            driver=getattr(webdriver, type_.lower())()
            log.info(f"{type_}浏览器已成功启动")
    except Exception as e:
        log.error(f"启动浏览器失败: {str(e)}")
        log.info("尝试使用Chrome浏览器作为备选")
        chrom_service = Service(r'D:\PycharmProjects\PythonProject\HAIMETA_data_driver_framework\config\chromedriver.exe')
        driver=webdriver.Chrome(service=chrom_service, options=chrome_options())
        log.info("备选Chrome浏览器已成功启动")
    return driver


class WebKeys:

    def __init__(self, type_):
        log.info("初始化WebKeys实例")
        self.driver = open_browser(type_)
        self.driver.implicitly_wait(5)
        log.info("设置隐式等待时间: 5秒")
        self.wait=WebDriverWait(self.driver, 10)
        log.info("设置显式等待时间: 10秒")
        self.action=ActionChains(self.driver)
        log.info("WebKeys实例初始化完成")

    def click(self, by, value):
        log.info(f"点击元素: {by}={value}")
        try:
            self.locator(by,value).click()
            log.info(f"元素点击成功: {by}={value}")
        except Exception as e:
            log.error(f"元素点击失败: {by}={value}, 错误: {str(e)}")
            raise

    def input(self,by, value, text):
        log.info(f"输入文本: {by}={value}, 文本内容: {text}")
        try:
            self.locator(by,value).send_keys(text)
            log.info(f"文本输入成功: {by}={value}")
        except Exception as e:
            log.error(f"文本输入失败: {by}={value}, 错误: {str(e)}")
            raise
    
    def open(self, url):
        log.info(f"打开URL: {url}")
        try:
            self.driver.get(url)
            log.info(f"URL打开成功: {url}")
        except Exception as e:
            log.error(f"URL打开失败: {url}, 错误: {str(e)}")
            raise

    def locator(self, by, value):
        log.info(f"定位元素: {by}={value}")
        try:
            element = self.driver.find_element(by, value)
            log.info(f"元素定位成功: {by}={value}")
            return element
        except Exception as e:
            log.error(f"元素定位失败: {by}={value}, 错误: {str(e)}")
            raise
    
    def quit(self):
        log.info("关闭浏览器")
        try:
            self.driver.quit()
            log.info("浏览器已成功关闭")
        except Exception as e:
            log.error(f"关闭浏览器失败: {str(e)}")
            raise

    def wait_sleep(self):
        log.info("等待2秒")
        time.sleep(2)
        log.info("等待完成")

    def wait_visible(self, by, value):
        log.info(f"等待元素可见: {by}={value}")
        try:
            element = self.wait.until(EC.visibility_of_element_located((by, value)))
            log.info(f"元素已可见: {by}={value}")
            return element
        except Exception as e:
            log.error(f"等待元素可见超时: {by}={value}, 错误: {str(e)}")
            raise
    
    def wait_presence(self, by, value):
        log.info(f"等待元素存在: {by}={value}")
        try:
            element = self.wait.until(EC.presence_of_element_located((by, value)))
            log.info(f"元素已存在: {by}={value}")
            return element
        except Exception as e:
            log.error(f"等待元素存在超时: {by}={value}, 错误: {str(e)}")
            raise

    def wait_clickable(self, by, value):
        log.info(f"等待元素可点击: {by}={value}")
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            log.info(f"元素已可点击: {by}={value}")
            return element
        except Exception as e:
            log.error(f"等待元素可点击超时: {by}={value}, 错误: {str(e)}")
            raise

    def wait_invisibility(self, by, value):
        log.info(f"等待元素不可见: {by}={value}")
        try:
            result = self.wait.until(EC.invisibility_of_element_located((by, value)))
            log.info(f"元素已不可见: {by}={value}")
            return result
        except Exception as e:
            log.error(f"等待元素不可见超时: {by}={value}, 错误: {str(e)}")
            raise

    def move_to_element(self, by, value):
        log.info(f"移动到元素: {by}={value}")
        try:
            element = self.locator(by, value)
            ActionChains(self.driver).move_to_element(element).perform()
            log.info(f"已成功移动到元素: {by}={value}")
        except Exception as e:
            log.error(f"移动到元素失败: {by}={value}, 错误: {str(e)}")
            raise
    
    def get_text(self, by, value):
        log.info(f"获取元素文本: {by}={value}")
        try:
            text = self.locator(by, value).text
            log.info(f"获取到元素文本: {by}={value}, 文本内容: {text}")
            return text
        except Exception as e:
            log.error(f"获取元素文本失败: {by}={value}, 错误: {str(e)}")
            raise

    def get_attribute(self, by, value, attribute):
        log.info(f"获取元素属性: {by}={value}, 属性名: {attribute}")
        try:
            attr_value = self.locator(by, value).get_attribute(attribute)
            log.info(f"获取到元素属性: {by}={value}, 属性名: {attribute}, 属性值: {attr_value}")
            return attr_value
        except Exception as e:
            log.error(f"获取元素属性失败: {by}={value}, 属性名: {attribute}, 错误: {str(e)}")
            raise
    
    def assert_text(self, by, value, expected):
        log.info(f"断言元素文本: {by}={value}, 预期文本: {expected}")
        try:
            reality=self.get_text(by, value)
            log.info(f"获取到实际文本: {reality}")
            assert reality == expected, f'''
            预期结果：{expected}
            实际结果：{reality}
            断言结果：{reality} != {expected}
            '''
            log.info(f"断言成功: 预期文本 '{expected}' 与实际文本 '{reality}' 匹配")
            return True
        except AssertionError as e:
            log.error(f"断言失败: 预期文本 '{expected}' 与实际文本 '{reality}' 不匹配")
            log.error(traceback.format_exc())
            return False
        except Exception as e:
            log.error(f"断言过程中发生异常: {str(e)}")
            log.error(traceback.format_exc())
            return False

    def click_visible(self, by, value):
        log.info(f"等待元素可见并点击: {by}={value}")
        try:
            self.wait_visible(by, value)
            self.click(by, value)
            log.info(f"元素可见并已成功点击: {by}={value}")
            return True, "操作成功"
        except Exception as e:
            log.error(f"等待元素可见并点击失败: {by}={value}, 错误: {str(e)}")
            log.error(traceback.format_exc())
            return False, f"发生未预期的错误: {str(e)}"

    def click_presence(self, by, value):
        log.info(f"等待元素存在并点击: {by}={value}")
        try:
            self.wait_presence(by, value)
            self.click(by, value)
            log.info(f"元素存在并已成功点击: {by}={value}")
            return True, "操作成功"
        except Exception as e:
            log.error(f"等待元素存在并点击失败: {by}={value}, 错误: {str(e)}")
            log.error(traceback.format_exc())
            return False, f"发生未预期的错误: {str(e)}"

    def click_clickable(self, by, value):
        try:
            self.wait_clickable(by, value)
            self.click(by, value)
        except Exception as e:
            traceback.print_exc()
            return False, f"发生未预期的错误: {str(e)}"

    def input_visible(self, by, value, text):
        try:
            self.wait_visible(by, value)
            self.input(by, value, text)
        except Exception as e:
            traceback.print_exc()
            return False, f"发生未预期的错误: {str(e)}"

    def input_presence(self, by, value, text):
        try:
            self.wait_presence(by, value)
            self.input(by, value, text)
        except Exception as e:
            traceback.print_exc()
            return False, f"发生未预期的错误: {str(e)}"

    def input_clickable(self, by, value,text):
        try:
            self.wait_clickable(by, value)
            self.input(by, value, text)
        except Exception as e:
            traceback.print_exc()
            return False, f"发生未预期的错误: {str(e)}"
    
    def Hover_to_the_button(self, by, value):
        try:
            self.action.move_to_element(self.locator(by, value)).perform()
        except Exception as e:
            traceback.print_exc()
            return False, f"发生未预期的错误: {str(e)}"
    
